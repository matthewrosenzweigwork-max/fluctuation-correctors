#!/usr/bin/env python3
"""Fresh coefficient/scaling diagnostics. Standard library, exact arithmetic only.

Smooth finite Fourier examples test identities, not the singular estimate.
One derivative is divided by 2*pi. Generator values and source values restore
(2*pi)^2. The Riesz normalization constant is factored out of the probes.
No previous checker, random sampling, or external input is used.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, G) else G(value)

    def __add__(self, other):
        other = self.coerce(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        norm = other.re ** 2 + other.im ** 2
        assert norm
        return self * G(other.re / norm, -other.im / norm)

    def conj(self):
        return G(self.re, -self.im)


ZERO, ONE, I = G(), G(1), G(0, 1)
checks = {}


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks[name] = checks.get(name, 0) + 1


def phase(power):
    return (ONE, I, -ONE, -I)[power % 4]


def evaluate(poly, point):
    return sum((value * phase(k * point) for k, value in poly.items()), ZERO)


def empirical(points, k):
    return sum((phase(-k * x) for x in points), ZERO) / len(points)


def smooth_source_identity():
    kernels = [
        {1: F(1), -1: F(1)},
        {k: F(1, k * k) for k in (-3, -2, -1, 1, 2, 3)},
        {k: F(1, k ** 4) for k in (-3, -2, -1, 1, 2, 3)},
    ]
    tests = [
        {0: G(5)},
        {-1: G(F(1, 2)), 1: G(F(1, 2))},
        {-2: G(0, F(1, 3)), 2: G(0, -F(1, 3)),
         -1: G(F(2, 5)), 1: G(F(2, 5)), 0: G(7)},
        {-3: G(F(1, 7), F(1, 4)), 3: G(F(1, 7), -F(1, 4))},
    ]
    for n in range(2, 10):
        for pattern in range(4):
            points = [((i * i + pattern * i + pattern) % 4) for i in range(n)]
            for a in kernels:
                force = {k: -I * k * value for k, value in a.items()}
                for h in tests:
                    v = {k: I * k * value for k, value in h.items()}
                    contraction = {k: I * k * a.get(k, 0) * value
                                   for k, value in v.items()}
                    def source(x, y):
                        return evaluate(force, x-y) * (evaluate(v, x)-evaluate(v, y))
                    raw = sum((source(points[i], points[j])
                               for i in range(n) for j in range(n) if i != j), ZERO)
                    background = sum((evaluate(contraction, x) for x in points), ZERO)
                    statistic = raw / (2*n*n) - background/n
                    check("smooth_source_real", statistic.im == 0)
                    check("smooth_source_diagonal_zero", all(source(x, x) == ZERO for x in points))
                    radius = max(map(abs, a)) + max(map(abs, h))
                    modes = [k for k in range(-radius, radius+1) if k]
                    fourier = ZERO
                    for k in modes:
                        for ell in modes:
                            difference = k*a.get(k, 0)-ell*a.get(ell, 0)
                            fourier += (-I/2 * difference * v.get(ell-k, ZERO)
                                        * empirical(points, k) * empirical(points, ell).conj())
                    check("ordered_source_commutator_identity", statistic == fourier)
                    check("constant_test_zero", h != tests[0] or statistic == ZERO)


def exact_energy_coefficients():
    a = {1: F(1, 3), -1: F(1, 3), 2: F(1, 7), -2: F(1, 7)}
    c = F(2)
    q = {0: c, 1: F(1, 5), -1: F(1, 5), 3: F(1, 9), -3: F(1, 9)}
    check("diagnostic_near_kernel_nonnegative", c > sum(abs(x) for k, x in q.items() if k))
    full = dict(a)
    for k, value in q.items():
        if k:
            full[k] = full.get(k, F(0)) + value
    wrong_self_detected = False
    wrong_background_detected = False
    for n in range(2, 13):
        for pattern in range(4):
            points = [(i*i+pattern*i) % 4 for i in range(n)]
            deleted = lambda p: sum((evaluate(p, points[i]-points[j])
                                    for i in range(n) for j in range(n) if i != j), ZERO)/(2*n*n)
            energy = deleted(full)
            positive = sum((value * empirical(points, k)*empirical(points, k).conj()
                            for k, value in a.items()), ZERO)/2
            near = deleted(q)
            self_term = G(sum(a.values()))/(2*n)
            background = G(F(n-1, 2*n)*c)
            check("exact_energy_self_background_identity", energy == positive+near-self_term-background)
            check("positive_fourier_energy", positive.im == 0 and positive.re >= 0)
            check("positive_deleted_near_energy", near.im == 0 and near.re >= 0)
            wrong_self_detected |= energy != positive+near-background
            wrong_background_detected |= energy != positive+near-self_term-G(c/2)
    check("missing_self_mutation_detected", wrong_self_detected)
    check("missing_finite_N_background_mutation_detected", wrong_background_detected)


def add_term(poly, exponent, value):
    poly[exponent] = poly.get(exponent, ZERO) + value
    if poly[exponent] == ZERO:
        del poly[exponent]


def derivative(poly, i):
    return {exponent: value*I*exponent[i]
            for exponent, value in poly.items() if exponent[i]}


def product(p, q):
    out = {}
    for x, a in p.items():
        for y, b in q.items():
            add_term(out, tuple(u+v for u, v in zip(x, y)), a*b)
    return out


def initial_generator_test():
    for n in range(2, 7):
        zero = (0,)*n
        for alpha in (1, 2, 3):
            a = {m: F(1, abs(m)**(2*alpha)) for m in (-3,-2,-1,1,2,3)}
            for probe in (1, 2, 3, 4):
                obs = {}
                for i in range(n):
                    for j in range(n):
                        exponent = [0]*n
                        exponent[i] -= probe
                        exponent[j] += probe
                        add_term(obs, tuple(exponent), G(F(1,n*n)))
                check("iid_empirical_mode_variance", obs.get(zero, ZERO) == G(F(1,n)))
                for nu in (F(0), F(1,3), F(2), F(1000)):
                    generator = {}
                    for i in range(n):
                        drift = {}
                        for j in range(n):
                            if j == i:
                                continue
                            for m, value in a.items():
                                exponent = [0]*n
                                exponent[i], exponent[j] = m, -m
                                add_term(drift, tuple(exponent), -I*m*value/n)
                        for exponent, value in product(drift, derivative(obs, i)).items():
                            add_term(generator, exponent, value)
                        for exponent, value in derivative(derivative(obs,i),i).items():
                            add_term(generator, exponent, nu*value)
                    target = G(-F(2*(n-1),n*n)*probe*probe*a.get(probe, F(0)))
                    check("literal_actual_initial_generator", generator.get(zero,ZERO) == target)
                    check("initial_repulsive_variance_sign", target.im == 0 and target.re <= 0)


def smoothing_and_scaling():
    moment_records = []
    for alpha in (1,2,3):
        for m in (2,3,5,8):
            tail_mass = factorial(alpha-1)*sum(
                (F((-1)**(j+1)*comb(m,j),j**alpha) for j in range(1,m+1)), F(0))
            check("positive_tail_mass", tail_mass > 0)
            for r in (F(1), F(1,2), F(1,8)):
                for lam in (F(1),F(4),F(9),F(64)):
                    moment = lambda power: factorial(power-1)*sum(
                        (F((-1)**j*comb(m,j))/(lam+F(j)/r)**power
                         for j in range(m+1)), F(0))
                    weight, next_moment = moment(alpha), moment(alpha+1)
                    check("positive_polynomial_smoothing_weight", weight > 0)
                    check("uniform_log_derivative_bound", 0 < lam*next_moment <= (alpha+m)*weight)
                    tail = factorial(alpha-1)*sum(
                        (F((-1)**(j+1)*comb(m,j))/(lam+F(j)/r)**alpha
                         for j in range(1,m+1)),F(0))
                    check("exact_heat_split_nonzero_mode", weight+tail == F(factorial(alpha-1))/lam**alpha)
                    check("positive_near_nonzero_mode", tail > 0)
                    moment_records.append({"alpha":alpha,"M":m,"r":str(r),"lambda":str(lam),
                                           "weight":str(weight),"log_radial_slope":str(2*lam*next_moment/weight)})
    regimes = []
    for d in range(3,13):
        for s in (F(1,3), F(d-2,2), F(d-2)):
            alpha = (d-s)/2
            source = s/d-1
            check("balanced_self_scale", -1+(-F(2,d))*(-s/2) == source)
            check("balanced_near_mass_scale", (-F(2,d))*alpha == source)
            scaled = source+F(1,2)
            check("scaled_exponent", scaled == s/d-F(1,2))
            regimes.append({"d":d,"s":str(s),"source_exponent":str(source),
                            "scaled_exponent":str(scaled),
                            "consequence":"decay" if scaled<0 else "bounded" if scaled==0 else "upper bound may grow"})
    check("d3_coulomb_included", F(1,3)-F(1,2) < 0)
    check("d4_coulomb_only_bounded", F(2,4)-F(1,2) == 0)
    check("d5_coulomb_no_decay_claim", F(3,5)-F(1,2) > 0)
    return moment_records, regimes


def main():
    smooth_source_identity()
    exact_energy_coefficients()
    initial_generator_test()
    moments, regimes = smoothing_and_scaling()
    result = {
        "status":"PASS", "assertions":sum(checks.values()),"checks":checks,
        "arithmetic":"exact Fraction and Gaussian rational arithmetic; no random seed or tolerance",
        "scope":"Coefficient, heat-moment and scaling diagnostics; analytic proof is in the memorandum.",
        "normalization":"One spatial derivative divided by 2*pi; source and generator restore (2*pi)^2. Frozen Riesz prefactor factored out.",
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "heat_moment_cases":moments,"regimes":regimes,
    }
    target=Path(__file__).with_name("round016_exact_diagnostic_results.json")
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"assertions":result["assertions"],
                      "categories":len(checks),"results":str(target)},indent=2))


if __name__ == "__main__":
    main()
