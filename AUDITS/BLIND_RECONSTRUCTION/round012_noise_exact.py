#!/usr/bin/env python3
"""Fresh exact supporting checks for TASK066; no previous checker is imported.

Local radial and polynomial probes test coefficients only. The analytic report
uses the actual singular periodic inverse and is not proved by these probes.
All arithmetic is rational; no random input, floating tolerance, or dependency.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib
import json


COUNTS = {}


def check(condition, group, label):
    if not condition:
        raise AssertionError(f"{group}: {label}")
    COUNTS[group] = COUNTS.get(group, 0) + 1


def rational_power(x, exponent):
    x, exponent = F(x), F(exponent)
    if x == 1:
        return F(1)
    if exponent.denominator == 1:
        return x ** exponent.numerator
    if exponent.denominator == 2:
        a, b = isqrt(x.numerator), isqrt(x.denominator)
        if a * a != x.numerator or b * b != x.denominator:
            raise ValueError("non-rational square root is outside this checker")
        return F(a, b) ** exponent.numerator
    raise ValueError("non-rational power is outside this checker")


class Jet:
    """Value, full gradient and full Hessian, with literal chain/product rules."""
    def __init__(self, value, n, grad=None, hess=None):
        self.value, self.n = F(value), n
        self.grad = [F(0)] * n if grad is None else grad
        self.hess = [[F(0)] * n for _ in range(n)] if hess is None else hess

    @classmethod
    def variable(cls, value, n, index):
        result = cls(value, n)
        result.grad[index] = F(1)
        return result

    def cast(self, other):
        return other if isinstance(other, Jet) else Jet(other, self.n)

    def __add__(self, other):
        other = self.cast(other)
        return Jet(self.value + other.value, self.n,
                   [x + y for x, y in zip(self.grad, other.grad)],
                   [[self.hess[i][j] + other.hess[i][j]
                     for j in range(self.n)] for i in range(self.n)])

    __radd__ = __add__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) - self

    def __mul__(self, other):
        other = self.cast(other)
        return Jet(self.value * other.value, self.n,
                   [self.grad[i] * other.value + self.value * other.grad[i]
                    for i in range(self.n)],
                   [[self.hess[i][j] * other.value
                     + self.grad[i] * other.grad[j]
                     + self.grad[j] * other.grad[i]
                     + self.value * other.hess[i][j]
                     for j in range(self.n)] for i in range(self.n)])

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * self.cast(other) ** -1

    def __pow__(self, exponent):
        exponent = F(exponent)
        v = rational_power(self.value, exponent)
        first = exponent * v / self.value
        second = exponent * (exponent - 1) * v / self.value ** 2
        return Jet(v, self.n, [first * x for x in self.grad],
                   [[second * self.grad[i] * self.grad[j]
                     + first * self.hess[i][j] for j in range(self.n)]
                    for i in range(self.n)])


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def lap(jet):
    return sum((jet.hess[i][i] for i in range(jet.n)), F(0))


def matvec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def local_pair_checks():
    for d, s in [(3, F(1, 2)), (4, F(1)), (4, F(3, 2)),
                 (5, F(2)), (6, F(3)), (3, F(1)), (4, F(2))]:
        p = s + 2
        n = 2 * d
        vals = [F(0)] * n
        vals[0] = F(1)
        x = [Jet.variable(v, n, i) for i, v in enumerate(vals)]
        rel = [x[j] - x[d + j] for j in range(d)]
        radius2 = sum((z * z for z in rel), Jet(0, n))
        g = radius2 ** (-s / 2)
        for N in [2, 3, 7]:
            energy = g / N
            drift = [-v for v in energy.grad]
            jac = [[-v for v in row] for row in energy.hess]
            for axis in range(d):
                for center in [False, True]:
                    vector = [F(0)] * n
                    vector[axis] = F(1)
                    vector[d + axis] = F(1 if center else -1)
                    eigenvalue = (F(0) if center else
                                  (-2 * s * (s + 1) / N if axis == 0
                                   else 2 * s / N))
                    check(matvec(jac, vector) == [eigenvalue * v for v in vector],
                          "pair_jacobian", f"d={d},s={s},N={N},axis={axis},center={center}")
            check(lap(energy) == -2 * s * (d - s - 2) / N,
                  "pair_laplacian", "both particle Laplacians")
            for q in [F(5, 4), p / 2, s + 1]:
                if not 1 < q < F(d, 2):
                    continue
                weight = radius2 ** (-q / 2)
                for nu in [F(0), F(1, 11), F(3, 2)]:
                    raw = nu * lap(weight) + dot(drift, weight.grad) + 2 * s / N
                    target = 2 * nu * q * (q + 2 - d) - 2 * s * (q - 1) / N
                    check(raw == target, "weighted_generator", "relative diffusion and one-sided potential")
                    check(-2 * s * (q - 1) / N < 0,
                          "weighted_generator", "strict weight absorption")


def full_particle_energy_checks():
    for N in [2, 3, 4, 5]:
        for s in [1, 2, 3]:
            d, n = s + 3, N * (s + 3)
            vals = [F(0)] * n
            for i in range(N):
                vals[i * d] = F(i * i + i + 1)
            x = [Jet.variable(v, n, j) for j, v in enumerate(vals)]
            energy = Jet(0, n)
            force = [F(0)] * n
            div_sum = F(0)
            for i in range(N):
                for j in range(i + 1, N):
                    rel = [x[i * d + k] - x[j * d + k] for k in range(d)]
                    rad2 = sum((z * z for z in rel), Jet(0, n))
                    energy += rad2 ** F(-s, 2) / N
                    r = abs(vals[i * d] - vals[j * d])
                    div_sum += s * (d - s - 2) * r ** (-s - 2)
                    pair_force = s * (vals[i * d] - vals[j * d]) * r ** (-s - 2) / N
                    force[i * d] += pair_force
                    force[j * d] -= pair_force
            check(energy.grad == [-b for b in force],
                  "particle_energy", f"full gradient N={N},s={s}")
            check(lap(energy) == -F(2, N) * div_sum,
                  "particle_energy", f"exact pair Laplacian N={N},s={s}")
            for nu in [F(0), F(2, 7)]:
                generator = dot(force, energy.grad) + nu * lap(energy)
                check(generator == -dot(force, force) - 2 * nu * div_sum / N,
                      "particle_energy", "full force square retained")
            check(F(2, N) * F(N * (N - 1), 2) == N - 1,
                  "particle_energy", "exchangeable labelled Laplacian coefficient")


def statistic_checks():
    # A symmetric polynomial probe on [0,1]^2; this is an algebra test only.
    def phi(x, y):
        return x * x * y * y + x * x + y * y + x * y + 3

    def background(x):
        return F(4, 3) * x * x + x / 2 + F(10, 3)

    def gradphi(x, y):
        return 2 * x * y * y + 2 * x + y

    def gradbackground(x):
        return F(8, 3) * x + F(1, 2)

    for N in [2, 3, 4, 5, 6]:
        vals = [F(i + 1, N + 2) for i in range(N)]
        xs = [Jet.variable(v, N, i) for i, v in enumerate(vals)]
        statistic = sum((phi(xs[i], xs[j]) for i in range(N)
                         for j in range(N) if i != j), Jet(0, N)) / (2 * N * N)
        statistic -= sum((background(x) for x in xs), Jet(0, N)) / N
        # Integral phi over [0,1]^2 = 145/36.
        statistic += F(145, 72)
        raw_grad = []
        for i in range(N):
            g = sum((gradphi(vals[i], vals[j]) for j in range(N) if i != j), F(0))
            A = gradbackground(vals[i])
            literal = g / (N * N) - A / N
            centered = (sum((gradphi(vals[i], vals[j]) - A
                             for j in range(N) if i != j), F(0)) - A) / (N * N)
            check(statistic.grad[i] == literal, "deleted_statistic", "literal ordered derivative")
            check(literal == centered, "deleted_statistic", "missing-self background retained")
            raw_grad.append(literal)
        upper = F(2 * (N - 1), N ** 4) * sum(
            (gradphi(vals[i], vals[j]) ** 2 for i in range(N)
             for j in range(N) if i != j), F(0))
        upper += F(2, N * N) * sum((gradbackground(x) ** 2 for x in vals), F(0))
        check(dot(raw_grad, raw_grad) <= upper, "deleted_statistic", "pointwise finite-sum estimate")
        drift = [F((-1) ** i * (i + 2), N + 1) for i in range(N)]
        for nu in [F(0), F(1, 3), F(2)]:
            generator = lambda v: dot(drift, v.grad) + nu * lap(v)
            variance = generator(statistic * statistic) - 2 * statistic.value * generator(statistic)
            check(variance == 2 * nu * dot(raw_grad, raw_grad),
                  "carre_du_champ", "full generator product identity")
            b = min(1 / nu, F(1)) if nu > 0 else F(1)
            scaled = 2 * nu * N * b * F(2 * (N - 1) ** 2, N ** 3)
            check(scaled == 4 * nu * b * F((N - 1) ** 2, N ** 2),
                  "bracket_scaling", "exact self bracket coefficient")
            check(nu * b <= 1, "bracket_scaling", "leading scaled noise factor")


def exponent_checks():
    for d in range(3, 13):
        for numerator in range(1, 4 * (d - 2)):
            s = F(numerator, 4)
            p, a, theta = s + 2, s / (s + 2), 1 - s / d
            check(-F(2, 1) / p * (1 + 2 / s) + 2 / s == 0,
                  "exponents", "bounded rescaled diffusion cancels N")
            check(theta - 2 / p == s * (d - s - 2) / (d * p) > 0,
                  "exponents", "critical sequence enters bounded-chi family")
            check((a < theta) == (s * (s + 2) < 2 * d),
                  "exponents", "strict critical equivalence")
            q = p / 2
            check(1 < q < F(d, 2) and q <= s + 1,
                  "exponents", "admissible squared-gradient weight")
            check(2 * (s + 1 - q) / p == a,
                  "exponents", "gradient-square power")
            if s < 2:
                check(a < theta and a - 2 / p < 0,
                      "exponents", "strict small-s corollary")
            for q in [F(5, 4), p / 2, s + 1]:
                if not 1 < q < F(d, 2) or q > s + 1:
                    continue
                k = s + 1 - q
                check(0 <= k < p, "exponents", "source split range")
                check(k / p + (q + p) / p - 1 == (s + 1) / p,
                      "exponents", "inner scale matching")
    # Two excluded equality boundaries must remain exactly zero, not negative.
    s, d = F(2), 4
    check(s / (s + 2) == 1 - s / d,
          "boundaries", "critical equality gives no decay")
    check((s - 2) / (s + 2) == 0,
          "boundaries", "s=2 diffusion exponent gives no decay")
    for d in range(3, 10):
        s = F(d - 2)
        check(s * (d - s - 2) == 0 and (s + 2) / 2 == F(d, 2),
              "boundaries", "Coulomb loses density and strict H1 weight")


def main():
    local_pair_checks()
    full_particle_energy_checks()
    statistic_checks()
    exponent_checks()
    here = Path(__file__).resolve().parent
    root = here.parent.parent
    inputs = {}
    for line in here.joinpath("INPUT_SHA256SUMS.txt").read_text().splitlines():
        expected, name = line.split(None, 1)
        observed = hashlib.sha256(root.joinpath(name).read_bytes()).hexdigest()
        check(observed == expected, "input_seal", name)
        inputs[name] = observed
    check(len(inputs) == 23, "input_seal", "exact permitted dossier count")
    result = {
        "outcome": "PASS: supporting exact checks only; no theorem/audit pass assigned",
        "assertions": sum(COUNTS.values()),
        "groups": COUNTS,
        "arithmetic": "Python standard-library Fraction; exact first and second automatic derivatives",
        "random_seed": None,
        "floating_point_tolerance": None,
        "scope": "Local radial and polynomial coefficient diagnostics, exact exponent identities, input hashes. Not a numerical replacement for the actual full inverse.",
        "input_count": len(inputs),
        "input_sha256": inputs,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    here.joinpath("round012_noise_exact_result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"outcome": result["outcome"], "assertions": result["assertions"], "groups": COUNTS}, indent=2))


if __name__ == "__main__":
    main()
