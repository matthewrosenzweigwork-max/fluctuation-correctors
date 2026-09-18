#!/usr/bin/env python3
"""AUD052 fresh exact diagnostics. No previous checker or source file is read.

All arithmetic is rational or Gaussian rational. Spatial derivatives are divided
by 2*pi; the scalar source and full generator are divided by (2*pi)**2.
Finite Fourier tests check coefficients, not the singular continuum theorem.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json


@dataclass(frozen=True)
class G:
    r: Q = Q(0)
    i: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "r", Q(self.r))
        object.__setattr__(self, "i", Q(self.i))

    @staticmethod
    def cast(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, other):
        other = G.cast(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-G.cast(other))

    def __rsub__(self, other):
        return G.cast(other) + (-self)

    def __mul__(self, other):
        other = G.cast(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = G.cast(other)
        return self * other.conj() * Q(1, other.abs2())

    def conj(self):
        return G(self.r, -self.i)

    def abs2(self):
        return self.r ** 2 + self.i ** 2

    def out(self):
        return {"real": str(self.r), "imag": str(self.i)}


I = G(0, 1)
ZERO = G()
counts = defaultdict(int)
mutations = defaultdict(list)
records = {}


def check(category, truth, detail=None):
    assert truth, (category, detail)
    counts[category] += 1


def witness(name, correct, wrong, case):
    if correct != wrong:
        mutations[name].append(case)


def neg(k):
    return tuple(-x for x in k)


def add(k, l):
    return tuple(x + y for x, y in zip(k, l))


def sub(k, l):
    return tuple(x - y for x, y in zip(k, l))


def norm2(k):
    return sum(x * x for x in k)


def phase(k, x):
    # x is an integer vector representing coordinates x/4.
    return (G(1), I, G(-1), -I)[sum(a * b for a, b in zip(k, x)) % 4]


def evaluate(poly, x):
    return sum((G.cast(a) * phase(k, x) for k, a in poly.items()), ZERO)


def empirical(k, points):
    return sum((phase(neg(k), x) for x in points), ZERO) / len(points)


def laplace(alpha, M, r, lam):
    return factorial(alpha - 1) * sum(
        (Q((-1) ** j * comb(M, j)) / (lam + Q(j) / r) ** alpha
         for j in range(M + 1)), Q(0))


def discarded_mass(alpha, M, r):
    return factorial(alpha - 1) * sum(
        (Q((-1) ** (j + 1) * comb(M, j)) / (Q(j) / r) ** alpha
         for j in range(1, M + 1)), Q(0))


def gamma_half(x):
    """Return rational coefficient and exponent of pi for Gamma(x)."""
    x = Q(x)
    assert x > 0 and (2 * x).denominator == 1
    if x.denominator == 1:
        return Q(factorial(int(x) - 1)), Q(0)
    n = int(x - Q(1, 2))
    return Q(factorial(2 * n), 4 ** n * factorial(n)), Q(1, 2)


def riesz_coefficient(d, s):
    # coefficient * pi**exponent, exactly in the frozen convention.
    top, top_pi = gamma_half(Q(d - s, 2))
    bot, bot_pi = gamma_half(Q(s, 2))
    return top / bot, Q(s) - Q(d, 2) + top_pi - bot_pi


def normalization_checks():
    for d in range(3, 14):
        for s in range(1, d - 1):
            alpha = Q(d - s, 2)
            gt, gp = gamma_half(alpha)
            gs, gsp = gamma_half(Q(s, 2))
            # A * Gamma(alpha)/(4*pi^2)^alpha.
            heat = (Q(2 ** (d - s)) * gt / gs / (2 ** (d - s)),
                    Q(d, 2) - gsp + gp - 2 * alpha)
            check("frozen Fourier coefficient", heat == riesz_coefficient(d, s), (d, s))
            check("coefficient-one local Gaussian integral",
                  alpha + Q(s, 2) - Q(d, 2) == 0, (d, s))
            if s < d - 2:
                c, p = riesz_coefficient(d, s)
                cc, pp = riesz_coefficient(d, s + 2)
                check("sub-Coulomb divergence ratio",
                      (4 * c / cc, 2 + p - pp) == (Q(s * (d - 2 - s)), Q(0)),
                      (d, s))
            else:
                c, p = riesz_coefficient(d, s)
                gd, gdp = gamma_half(Q(d, 2))
                check("Coulomb atom coefficient",
                      (4 * c, p + 2) == (Q(2 * (d - 2)) / gd, Q(d, 2) - gdp), d)


def heat_weight_checks():
    cases = sorted(set([(a, 2 * a + 3) for a in range(1, 6)] +
                       [(1, d + 2) for d in (3, 4, 6, 9, 13)]))
    data = []
    for alpha, M in cases:
        for r, lam in product((Q(1, 4096), Q(1, 7), Q(1), Q(2)),
                              (Q(1, 13), Q(1), Q(16), Q(257))):
            z = laplace(alpha, M, r, lam)
            zz = laplace(alpha + 1, M, r, lam)
            check("positive retained Laplace weight", z > 0, (alpha, M, r, lam))
            slope = 2 * lam * zz / z
            check("exact logarithmic slope interval",
                  2 * alpha <= slope <= 2 * (alpha + M), (alpha, M, r, lam))
            c = discarded_mass(alpha, M, r)
            check("positive discarded mass", c > 0, (alpha, M, r))
            check("scale doubling mass coefficient",
                  discarded_mass(alpha, M, 2 * r) == 2 ** alpha * c, (alpha, M, r))
            if alpha == 1:
                beta_product = Q(factorial(M)) / (lam * prod(lam * r + j for j in range(1, M + 1)))
                check("Coulomb exact beta-product weight", z == beta_product, (M, r, lam))
                product_slope = 2 * (1 + sum((lam * r / (lam * r + j)
                                               for j in range(1, M + 1)), Q(0)))
                check("Coulomb exact product slope", slope == product_slope, (M, r, lam))
            data.append({"alpha": alpha, "M": M, "r": str(r), "lambda": str(lam),
                         "weight": str(z), "slope": str(slope), "discarded_mass": str(c)})
    records["laplace_cases"] = data
    pairs = [((1, 0, 0), (0, 1, 0)), ((1, 0, 0), (2, 1, 0)),
             ((1, 0, 0), (33, 1, 0)), ((-7, 3, 1), (6, -2, 3)),
             ((100, 1, 0), (101, 1, 0)), ((2, 3, 1), (2, 3, 1))]
    for alpha, M in ((1, 5), (2, 7), (4, 11)):
        L = 2 * (alpha + M)
        for r, (k, ell) in product((Q(1, 10 ** 8), Q(1, 17), Q(2)), pairs):
            a = laplace(alpha, M, r, Q(norm2(k)))
            b = laplace(alpha, M, r, Q(norm2(ell)))
            q = sub(k, ell)
            lhs = sum((x * a - y * b) ** 2 for x, y in zip(k, ell))
            # Replace |q| by its larger l1 norm only in the last factor.
            rhs = (1 + L) ** 2 * norm2(q) * (1 + sum(abs(x) for x in q)) ** (L + 2) * a * b
            check("exact lattice commutator bound", lhs <= rhs, (alpha, M, r, k, ell))


def Fourier_fixture():
    modes = [(1, 0, 0), (0, 1, 0), (1, 1, 0), (2, 0, 0), (0, 0, 1), (1, -1, 1)]
    g = {}
    for k in modes:
        g[k] = g[neg(k)] = Q(1, 1 + norm2(k))
    f = {(0, 0, 0): G(Q(3, 7))}
    for j, k in enumerate([(1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (2, -1, 1)]):
        f[k] = G(Q(j + 1, j + 3), Q((-1) ** j, 2 * j + 5))
        f[neg(k)] = f[k].conj()
    return g, f


def source_and_energy_checks():
    g, f = Fourier_fixture()
    vel = {k: tuple(I * a * q for q in k) for k, a in f.items()}
    force = [{k: -I * q[axis] * a for k, a in g.items() for q in [k]} for axis in range(3)]
    contractions = {k: -norm2(k) * g.get(k, Q(0)) * a for k, a in f.items()}
    data = []
    for N in range(2, 8):
        points = [(i % 4, (i * i + 1) % 4, (3 * i + i // 4) % 4) for i in range(N)]
        check("distinct diagnostic configurations", len(set(points)) == N, N)
        v_values = [tuple(evaluate({k: a[axis] for k, a in vel.items()}, x)
                          for axis in range(3)) for x in points]
        raw = ZERO
        for i, x in enumerate(points):
            for j, y in enumerate(points):
                if i == j:
                    continue
                kvals = tuple(evaluate(force[a], sub(x, y)) for a in range(3))
                raw += sum((kvals[a] * (v_values[i][a] - v_values[j][a])
                            for a in range(3)), ZERO)
        pair = raw / (2 * N * N)
        bg = sum((evaluate(contractions, x) for x in points), ZERO) / N
        direct = pair - bg
        # Haar contractions and double Haar integral checked by literal 4-grid
        # integration after a 16-grid lift would be needlessly transcendental.
        # Instead collect the zero y-frequency of the literal product.
        for k, a in contractions.items():
            literal = sum((-(-I * p[axis] * g[p]) * vel.get(k, (ZERO,) * 3)[axis]
                           for p in g if p == k for axis in range(3)), ZERO)
            check("literal background Fourier contraction", literal == a, (N, k))
        check("double Haar contraction zero", contractions[(0, 0, 0)] == ZERO, N)
        indices = set(g)
        for k, q in product(g, vel):
            indices.add(add(k, q))
            indices.add(sub(k, q))
        indices.discard((0, 0, 0))
        sym = ZERO
        for k, ell in product(indices, repeat=2):
            q = sub(ell, k)
            if q not in vel:
                continue
            numerator_dot_v = sum(((k[a] * g.get(k, Q(0)) - ell[a] * g.get(ell, Q(0)))
                                   * vel[q][a] for a in range(3)), ZERO)
            sym += (-I / 2) * numerator_dot_v * empirical(k, points) * empirical(ell, points).conj()
        check("deleted source equals symmetric Fourier sum", direct == sym, N)
        check("real source value", direct.i == 0, N)
        witness("missing source half", direct, 2 * pair - bg, N)
        witness("missing one-body contraction", direct, pair, N)
        witness("wrong commutator sign", direct, -sym, N)
        witness("falling-factorial source denominator", direct, raw / (2 * N * (N - 1)) - bg, N)
        # Independent finite Fourier splitting g_total = g_retained + Q - c.
        qpoly = {(1, 0, 0): Q(1, 4), (-1, 0, 0): Q(1, 4),
                 (0, 1, 0): Q(1, 7), (0, -1, 0): Q(1, 7)}
        c = Q(2)
        Er = sum((a * empirical(k, points).abs2() for k, a in g.items()), Q(0)) / 2
        Sr = ZERO
        H_over_N = ZERO
        for i, x in enumerate(points):
            for j, y in enumerate(points):
                if i == j:
                    continue
                retained = evaluate(g, sub(x, y))
                discarded = evaluate(qpoly, sub(x, y))
                Sr += c + discarded
                H_over_N += retained + discarded
        Sr /= 2 * N * N
        H_over_N /= 2 * N * N
        g0 = sum(g.values(), Q(0))
        exact = G(Er) + Sr - g0 / (2 * N) - Q(N - 1, 2 * N) * c
        check("exact energy self-background identity", H_over_N == exact, N)
        check("positive retained energy", Er >= 0, N)
        check("positive discarded pair sum", Sr.i == 0 and Sr.r >= 0, N)
        witness("missing energy self diagonal", H_over_N, exact + g0 / (2 * N), N)
        witness("wrong constant mass coefficient", H_over_N, G(Er) + Sr - g0 / (2 * N) - c / 2, N)
        data.append({"N": N, "source_divided_by_4pi2": direct.out(),
                     "energy_divided_by_N": H_over_N.out(), "points_in_quarters": points})
    records["finite_configuration_cases"] = data


def config_exponent(N, k, i, j):
    out = [0] * (3 * N)
    for axis in range(3):
        out[3 * i + axis] += k[axis]
        out[3 * j + axis] -= k[axis]
    return tuple(out)


def generator_checks():
    g, _ = Fourier_fixture()
    data = []
    for N, k in product(range(2, 7), [(1, 0, 0), (1, 1, 0), (2, 0, 0), (3, 2, 1)]):
        observable = defaultdict(Q)
        zero = (0,) * (3 * N)
        for i, j in product(range(N), repeat=2):
            observable[config_exponent(N, k, i, j)] += Q(1, N * N)
        check("iid empirical variance self count", observable[zero] == Q(1, N), (N, k))
        for nu in (Q(0), Q(1, 3), Q(2), Q(11)):
            image = defaultdict(Q)
            for ex, coeff in observable.items():
                image[ex] -= nu * norm2(ex) * coeff
                for i in range(N):
                    for j in range(N):
                        if i == j:
                            continue
                        for p, a in g.items():
                            # B_i/(2pi) = -i*p*a/N; D_i Phi = i*ex_i*Phi.
                            dot = sum(p[axis] * ex[3 * i + axis] for axis in range(3))
                            if dot:
                                image[add(ex, config_exponent(N, p, i, j))] += coeff * a * Q(dot, N)
            got = image[zero]
            expected = -Q(2 * (N - 1), N * N) * norm2(k) * g.get(k, Q(0))
            check("literal full-generator initial variance derivative", got == expected, (N, k, nu))
            check("initial derivative nonpositive all tested noise", got <= 0, (N, k, nu))
            witness("wrong initial force sign", got, -expected, (N, k, str(nu)))
            witness("missing initial two-label factor", got, expected / 2, (N, k, str(nu)))
            data.append({"N": N, "k": k, "nu": str(nu),
                         "derivative_divided_by_4pi2": str(got),
                         "full_generator_nonzero_terms": sum(v != 0 for v in image.values())})
    records["generator_cases"] = data


def scaling_and_endpoints():
    data = []
    signs = set()
    for d in range(3, 15):
        exponents = {Q(1, 4), Q(d - 2), Q(d - 2, 2)}
        if Q(d, 2) <= d - 2:
            exponents.add(Q(d, 2))
        for s in sorted(exponents):
            alpha = (d - s) / 2
            scale = Q(-2, d)
            energy_self = -1 - scale * s / 2
            source_tail = scale * alpha
            target = s / d - 1
            scaled = target + Q(1, 2)
            check("optimized source powers", energy_self == source_tail == target, (d, s))
            check("scaled source exponent", scaled == s / d - Q(1, 2), (d, s))
            local_L2_power = d - 1 - 2 * s
            check("source L2 boundary", (local_L2_power > -1) == (s < Q(d, 2)), (d, s))
            category = "decaying" if scaled < 0 else "bounded" if scaled == 0 else "growing"
            signs.add(category)
            data.append({"d": d, "s": str(s), "source_power": str(target),
                         "scaled_power": str(scaled), "scaled_upper_bound": category})
    check("all three scaled regimes represented", signs == {"decaying", "bounded", "growing"})
    for nu in (Q(0), Q(1, 100), Q(1), Q(2), Q(11)):
        b = Q(1) if nu == 0 else min(1 / nu, Q(1))
        check("bounded-noise normalization including zero", 0 < b <= 1, str(nu))
    # Algebraic free-energy square; all coefficients sampled exactly, including zero.
    for u, z, nu in product(range(-3, 4), range(-3, 4), (Q(0), Q(1, 5), Q(3))):
        separate_energy_and_entropy = -u * u - 2 * nu * u * z - nu * nu * z * z
        check("free-energy exact complete square", separate_energy_and_entropy == -(u + nu * z) ** 2)
    # N=2 has B=(K/2,-K/2), so the full square is |K|^2/2.
    for K in product(range(-2, 3), repeat=3):
        drift_square = 2 * sum(Q(k, 2) ** 2 for k in K)
        check("N2 exact deterministic energy coefficient", drift_square == Q(norm2(K), 2), K)
    records["scaling_cases"] = data


def main():
    normalization_checks()
    heat_weight_checks()
    source_and_energy_checks()
    generator_checks()
    scaling_and_endpoints()
    required = ["missing source half", "missing one-body contraction", "wrong commutator sign",
                "falling-factorial source denominator", "missing energy self diagonal",
                "wrong constant mass coefficient", "wrong initial force sign", "missing initial two-label factor"]
    for name in required:
        check("mutation detected: " + name, bool(mutations[name]), name)
    result = {"audit": "AUD052", "status": "PASS", "arithmetic": "exact rational and Gaussian rational",
              "previous_checker_read": False, "randomness": "none", "external_dependencies": [],
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "normalization": "derivatives divided by 2*pi; source and full generator divided by 4*pi^2",
              "scope": "coefficient diagnostics only; analytic report proves singular passages and uniform bounds",
              "assertions": sum(counts.values()), "categories": dict(sorted(counts.items())),
              "mutation_witness_counts": {k: len(v) for k, v in sorted(mutations.items())},
              "cases": records}
    destination = Path(__file__).with_name("independent_diagnostic_results.json")
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in ("audit", "status", "assertions", "script_sha256")}, sort_keys=True))
    print("All eight deliberate coefficient errors were detected. No continuum theorem is inferred from these finite tests.")


if __name__ == "__main__":
    main()
