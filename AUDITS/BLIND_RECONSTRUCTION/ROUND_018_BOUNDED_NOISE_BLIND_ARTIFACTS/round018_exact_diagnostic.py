#!/usr/bin/env python3
"""Fresh AUD055 coefficient/probability diagnostics; Python standard library only.

No prior checker is read. Exact rational/Gaussian-rational arithmetic only.
This supports, and does not replace, the analytic proof or conditional R16 input.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


@dataclass(frozen=True)
class Q:
    r: F = F(0)
    i: F = F(0)

    def __add__(self, other):
        z = cq(other)
        return Q(self.r + z.r, self.i + z.i)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-cq(other))

    def __rsub__(self, other):
        return cq(other) - self

    def __mul__(self, other):
        z = cq(other)
        return Q(self.r*z.r - self.i*z.i, self.r*z.i + self.i*z.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Q):
            den = other.r**2 + other.i**2
            return (self * other.conj()) / den
        den = F(other)
        return Q(self.r/den, self.i/den)

    def conj(self):
        return Q(self.r, -self.i)


def cq(x):
    return x if isinstance(x, Q) else Q(F(x))


ZERO = Q()
ONE = Q(F(1))
IM = Q(F(0), F(1))
counts = Counter()
mutations = Counter()


def eq(a, b, category):
    assert a == b, (category, a, b)
    counts[category] += 1


def check(condition, category):
    assert condition, category
    counts[category] += 1


def reject(a, b, mutation):
    assert a != b, ("mutation not detected", mutation, a)
    mutations[mutation] += 1


def addterm(poly, k, value):
    value = poly.get(k, ZERO) + cq(value)
    if value == ZERO:
        poly.pop(k, None)
    else:
        poly[k] = value


def padd(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            addterm(out, k, v)
    return out


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c != ZERO}


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            addterm(out, tuple(a+b for a, b in zip(k, l)), v*w)
    return out


def conj(p):
    return {tuple(-a for a in k): v.conj() for k, v in p.items()}


def deriv(p, slot):
    return {k: v*IM*k[slot] for k, v in p.items() if k[slot]}


def empirical_mode(n, mode):
    out = {}
    for j in range(n):
        k = [0]*n
        k[j] = -mode
        addterm(out, tuple(k), F(1, n))
    return out


G = {-3: F(1, 7), -2: F(1, 3), -1: F(1),
     1: F(1), 2: F(1, 3), 3: F(1, 7)}


def literal_generator(p, n, nu):
    """The physical coordinate generator is (2*pi)^2 times this one."""
    out = {}
    for j in range(n):
        out = padd(out, scale(deriv(deriv(p, j), j), nu))
        dj = deriv(p, j)
        for l in range(n):
            if j == l:
                continue
            force = {}
            for mode, coeff in G.items():
                k = [0]*n
                k[j] = mode
                k[l] = -mode
                addterm(force, tuple(k), -IM*mode*coeff)
            out = padd(out, scale(mul(force, dj), F(1, n)))
    return out


def haar(p, n):
    return p.get((0,)*n, ZERO)


def generator_checks():
    # Full finite-particle differentiation, not a substituted reduced formula.
    for n, mode, nu in product(range(2, 7), (1, 2, 3), (F(0), F(1, 4), F(1), F(3))):
        z = empirical_mode(n, mode)
        zbar = conj(z)
        lz = literal_generator(z, n, nu)
        cross = haar(mul(lz, zbar), n)
        equal_time = haar(literal_generator(mul(z, zbar), n, nu), n)
        dk = mode*mode*G[mode]
        ak = mode*mode
        eq(haar(mul(z, zbar), n), cq(F(1, n)), "iid Fourier self term")
        eq(cross, cq(-nu*ak/n-F(n-1, n*n)*dk), "literal two-time initial generator")
        eq(equal_time, cq(-F(2*(n-1), n*n)*dk), "literal equal-time initial generator")
        gamma = equal_time-cross-cross.conj()
        eq(gamma, cq(2*nu*ak/n), "literal diffusion contraction")
        reject(equal_time, cq(-F(n-1, n*n)*dk), "lost ordered-pair factor two")
        reject(cross, cq(-nu*ak/n-dk/n), "replaced N minus one by N")
        if nu:
            reject(gamma, cq(nu*ak/n), "lost noise factor two")
        reject(cross, cq(-nu*ak/n+F(n-1, n*n)*dk), "reversed response sign")


ROOTS = (ONE, IM, -ONE, -IM)


def eval1(p, quarter):
    return sum((cq(v)*ROOTS[(k*quarter) % 4] for k, v in p.items()), ZERO)


def d1(p):
    return {k: cq(v)*IM*k for k, v in p.items() if k}


def d2(p):
    return {k: cq(v)*(-k*k) for k, v in p.items() if k}


TESTS = (
    {0: F(2), -1: F(1, 2), 1: F(1, 2)},
    {-1: IM/2, 1: -IM/2},
    {0: F(7, 3), -1: F(1, 2), 1: F(1, 2), -2: F(1, 3), 2: F(1, 3)},
    {0: F(5)},
)


def source_bracket_checks():
    configs = ((0, 1), (0, 1, 3), (0, 0, 1, 2), (0, 1, 2, 3, 1), (0, 1, 1, 2, 3, 0))
    force = {k: -IM*k*v for k, v in G.items()}
    found_background = found_bracket = found_diagonal_stat = False
    for base, shift, f, nu in product(configs, range(4), TESTS, (F(0), F(1, 3), F(1), F(5, 2))):
        points = tuple((p+shift) % 4 for p in base)
        n = len(points)
        grad = {p: eval1(d1(f), p) for p in range(4)}
        af = {k: -k*k*G.get(k, F(0))*cq(v) for k, v in f.items() if k}
        av = [eval1(af, p) for p in points]
        raw_force = sum((eval1(force, (points[i]-points[l]) % 4)*grad[points[i]]
                         for i in range(n) for l in range(n) if i != l), ZERO)/(n*n)
        raw_pair = sum((eval1(force, (points[i]-points[l]) % 4)
                       *(grad[points[i]]-grad[points[l]])
                       for i in range(n) for l in range(n) if i != l), ZERO)/(2*n*n)
        source = raw_pair-sum(av, ZERO)/n
        eq(raw_force, raw_pair, "raw ordered source symmetrization")
        time_deriv = {k: (nu*k*k+k*k*G.get(k, F(0)))*cq(v) for k, v in f.items() if k}
        full_drift = (sum((eval1(time_deriv, p)+nu*eval1(d2(f), p) for p in points), ZERO)/n
                      +raw_force)
        eq(full_drift, source, "literal one-body backward cancellation")
        eq(sum((eval1(af, p) for p in range(4)), ZERO)/4,
           ZERO, "original Haar double contraction")
        if sum(av, ZERO) != ZERO:
            reject(full_drift, raw_pair, "deleted original Haar contraction")
            found_background = True
        if raw_pair != ZERO:
            reject(raw_pair, raw_pair*F(n, n-1), "used falling-factorial denominator")
            found_diagonal_stat = True
        other = TESTS[2]
        gg = [eval1(d1(other), p) for p in points]
        gprod = sum((grad[p]*w for p, w in zip(points, gg)), ZERO)
        b = min(F(1), F(1)/nu) if nu else F(1)
        direct = F(2)*nu*(n*b)/(n*n)*gprod
        bracket = 2*nu*b*gprod/n
        eq(direct, bracket, "literal one-body cross bracket coefficient")
        if bracket != ZERO:
            reject(bracket, bracket*n, "extra N in cross bracket")
            reject(bracket, bracket/2, "half cross bracket")
            found_bracket = True
        if set(f) == {0}:
            eq(source, ZERO, "constant source exactly zero")
            eq(bracket, ZERO, "constant bracket exactly zero")
    check(found_background and found_bracket and found_diagonal_stat,
          "nonvacuous source and bracket mutation witnesses")


def expsum(*terms):
    out = {}
    for rate, coeff in terms:
        addterm(out, F(rate), cq(coeff))
    return out


def covariance_checks():
    # An exact formal sum represents sum c*exp(-rate*tau), for a free tau>0.
    for dk, ak, nu, ti, tj in product((F(1, 3), F(1), F(5, 2)),
                                     (F(1), F(4), F(9)),
                                     (F(0), F(1, 3), F(1), F(2), F(5)),
                                     (F(0), F(1, 4), F(1), F(2)),
                                     (F(0), F(1, 4), F(1), F(2))):
        b = min(F(1), F(1)/nu) if nu else F(1)
        lk = dk+nu*ak
        total, diff = (ti+tj)*lk, abs(ti-tj)*lk
        initial = expsum((total, b))
        thermal = expsum((diff, nu*b*ak/lk), (total, -nu*b*ak/lk))
        direct = padd(initial, thermal)
        card = expsum((total, b*dk/lk), (diff, b*nu*ak/lk))
        eq(direct, card, "integrated thermal and initial covariance")
        if ti == 0 or tj == 0:
            eq(thermal, {}, "zero-time cross bracket")
            eq(card, initial, "zero-time total covariance")
        if nu == 0:
            eq(thermal, {}, "zero-noise thermal term")
            eq(card, initial, "zero-noise covariance")
        if ti == tj == 0:
            eq(card, expsum((0, b)), "initial variance normalization")
        if nu and ti and tj:
            reject(card, padd(initial, scale(thermal, F(1, 2))), "half thermal integral")
            reject(card, expsum((total, b*dk/lk), (total, b*nu*ak/lk)), "sum time for thermal lag")
            reject(card, expsum((total, b), (diff, b*nu*ak/lk)), "uncorrected initial covariance coefficient")
            reject(card, thermal, "lost initial fluctuation")


def gram_checks():
    # Exact rational OU samples: exp(-L)=u. Positive weights and arbitrary tests.
    times = (0, 1, 1, 1, 2, 2)
    tests = ((F(1), F(0)), (F(1), F(1)), (F(2), F(2)),
             (F(0), F(0)), (F(1), F(-1)), (F(1), F(-1)))
    b = F(2, 3)
    modes = ((F(1, 2), F(2, 5)), (F(1, 3), F(4, 7)))
    n = len(times)
    card = [[F(0) for _ in range(n)] for _ in range(n)]
    gram = [[F(0) for _ in range(n)] for _ in range(n)]
    for mode, (u, w) in enumerate(modes):
        for i, j in product(range(n), repeat=2):
            factor = tests[i][mode]*tests[j][mode]*b/2
            card[i][j] += factor*(w*u**(times[i]+times[j])+(1-w)*u**abs(times[i]-times[j]))
            value = u**(times[i]+times[j])
            for l in range(1, min(times[i], times[j])+1):
                value += (1-w)*(1-u*u)*u**(times[i]-l)*u**(times[j]-l)
            gram[i][j] += factor*value
    for i, j in product(range(n), repeat=2):
        eq(card[i][j], gram[i][j], "joint covariance Gram representation")
        eq(card[i][j], card[j][i], "joint covariance symmetry")
    for v in product((-1, 0, 1), repeat=n):
        qf = sum(F(v[i]*v[j])*card[i][j] for i, j in product(range(n), repeat=2))
        check(qf >= 0, "joint covariance nonnegative probes")
    for i in range(n):
        eq(card[3][i], F(0), "constant-test covariance row")
        eq(card[2][i], 2*card[1][i], "linear dependence at repeated time")
        eq(card[4][i], card[5][i], "identical repeated tuple")
    reject(card[3][3], card[3][3]+1, "nonzero variance for constant test")
    # An exact null direction would acquire negative variance under this mutation.
    v = (0, -2, 1, 0, 0, 0)
    qf = sum(F(v[i]*v[j])*card[i][j] for i, j in product(range(n), repeat=2))
    eq(qf, F(0), "exact degenerate linear direction")
    reject(qf, qf-1, "forced nondegenerate covariance")


def initial_checks():
    cos = (F(1), F(0), F(-1), F(0))
    sin = (F(0), F(1), F(0), F(-1))
    for n in range(2, 6):
        eps = F(1, n)
        b = F(2, 3)
        second = replacement = mean = F(0)
        for positions in product(range(4), repeat=n):
            s = sum(cos[p]+eps*sin[p] for p in positions)
            delta = sum(eps*sin[p] for p in positions)
            mean += s
            second += s*s
            replacement += delta*delta
        den = 4**n
        eq(mean/den, F(0), "initial centering exact enumeration")
        eq(b*second/(n*den), b*(1+eps*eps)/2, "initial sqrt N normalization")
        eq(b*replacement/(n*den), b*eps*eps/2, "initial triangular-test L2 replacement")
        reject(b*second/(n*den), b*second/den, "N instead of sqrt N initial scale")


def conditional_exponential_checks():
    # Brownian integrand a(I), with an initial independent fair label I.
    # Conditional Gaussian integration is exact; M=a(I)W, V=a(I)^2.
    amplitudes = (F(1), F(2))
    for phase in ((ONE, ONE), (ONE, -ONE), (ONE, IM)):
        initial = expsum((0, sum(phase, ZERO)/2))
        compensated = {}
        wrong_sign = {}
        joint = {}
        mart_char = {}
        for a, p in zip(amplitudes, phase):
            compensated = padd(compensated, expsum((a*a/2-a*a/2, p/2)))
            wrong_sign = padd(wrong_sign, expsum((a*a, p/2)))
            joint = padd(joint, expsum((a*a/2, p/2)))
            mart_char = padd(mart_char, expsum((a*a/2, F(1, 2))))
        eq(compensated, initial, "conditional positive-half-bracket compensation")
        reject(compensated, wrong_sign, "negative-half-bracket exponential")
        if phase[0] != phase[1]:
            reject(joint, scale(mart_char, sum(phase, ZERO)/2), "finite N initial martingale independence")
    ei, em2, eim2 = F(1, 2), F(5, 2), F(2)
    eq(eim2-ei*em2, F(3, 4), "zero martingale mean does not imply independence")
    for n in (2, 3, 10, 100, 1000):
        a = 1+F(1, n)
        eq(a*a-1, F(2, n)+F(1, n*n), "exact bounded bracket deviation")
        check(a*a-1 <= F(3, n), "bracket deviation vanishes without independence")


def exponent_checks():
    for d in range(3, 15):
        for half_s in range(1, 2*(d-2)+1):
            s = F(half_s, 2)
            if s >= F(d, 2):
                continue
            q = 1-s/d
            check(q > 0, "actual empirical concentration exponent")
            check(s/d-F(1, 2) < 0, "full admitted source decay exponent")
            eq(-1+F(2, d)*s/2, s/d-1, "source heat-splitting power")
            eq(-F(2, d)*(d-s)/2, s/d-1, "source discarded-mass power")
    for nu in (F(0), F(1, 100), F(1), F(101, 100), F(10)):
        b = min(F(1), 1/nu) if nu else F(1)
        check(0 < b <= 1 and 0 <= nu*b <= 1, "bounded normalization endpoints")


def main():
    generator_checks()
    source_bracket_checks()
    covariance_checks()
    gram_checks()
    initial_checks()
    conditional_exponential_checks()
    exponent_checks()
    here = Path(__file__).resolve()
    result = {
        "audit": "AUD055", "task": "TASK-085", "status": "PASS",
        "assertions": sum(counts.values()), "categories": dict(sorted(counts.items())),
        "mutation_rejections": sum(mutations.values()),
        "mutation_categories": dict(sorted(mutations.items())),
        "script_sha256": sha256(here.read_bytes()).hexdigest(),
        "arithmetic": "Exact Fraction and Gaussian rational; no float, random seed or tolerance.",
        "physical_convention": "The implemented first derivative is the physical derivative divided by 2*pi; force, gradient and response probes restore (2*pi)^2 in generator/source/bracket formulas. Rational Fourier polynomials are smooth coefficient probes, not replacements for the singular Riesz model.",
        "formal_exponentials": "D, a, diffusivity and time probes are exact rationals; maps represent sums c*exp(-rate*tau) for a free positive common tau. Positive Gram examples set exp(-L)=a rational number and retain all positive variance weights.",
        "limits": "Finite exact checks support coefficients and invalid-inference controls only. The report proves singular passages and actual joint probability convergence; R16 remains an expressly conditional source premise.",
    }
    target = here.with_name("round018_exact_diagnostic_output.json")
    target.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": result["status"], "assertions": result["assertions"],
                      "categories": len(counts), "mutation_rejections": result["mutation_rejections"],
                      "mutation_categories": len(mutations), "output": str(target)}, sort_keys=True))


if __name__ == "__main__":
    main()
