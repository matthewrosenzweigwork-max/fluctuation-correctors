#!/usr/bin/env python3
"""Exact local coefficient and falsification checks for TASK-045.

Standard library only. Local powers/backgrounds test differential coefficients,
not a claim that a Euclidean polynomial is a periodic potential. The full proof
and its periodic compensation are in the accompanying Markdown memorandum.
All arithmetic is rational; no random input, tolerance, or numerical inference.
"""

from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path


COUNTS = {}
DETAILS = []


def check(category, condition, detail):
    if not condition:
        raise AssertionError(f"{category}: {detail}")
    COUNTS[category] = COUNTS.get(category, 0) + 1


def exact_root(n, degree):
    if n < 0 or degree <= 0:
        raise ValueError("Positive rational powers only in exact_root")
    lo, hi = 0, max(1, n)
    while lo <= hi:
        mid = (lo + hi) // 2
        value = mid ** degree
        if value == n:
            return mid
        if value < n:
            lo = mid + 1
        else:
            hi = mid - 1
    raise ValueError(f"{n} is not an exact {degree}-th power")


def rational_power(value, exponent):
    value, exponent = F(value), F(exponent)
    if value <= 0:
        raise ValueError("Fractional differentiation uses positive radius square")
    root = F(exact_root(value.numerator, exponent.denominator),
             exact_root(value.denominator, exponent.denominator))
    return root ** exponent.numerator


@dataclass(frozen=True)
class Jet:
    """Value, full gradient, and full Laplacian; ordinary product/chain rules."""

    value: F
    gradient: tuple
    laplacian: F

    def constant(self, value):
        return Jet(F(value), (F(0),) * len(self.gradient), F(0))

    def coerce(self, other):
        return other if isinstance(other, Jet) else self.constant(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Jet(self.value + other.value,
                   tuple(a + b for a, b in zip(self.gradient, other.gradient)),
                   self.laplacian + other.laplacian)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, tuple(-a for a in self.gradient), -self.laplacian)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        cross = sum(a * b for a, b in zip(self.gradient, other.gradient))
        return Jet(self.value * other.value,
                   tuple(self.value * b + other.value * a
                         for a, b in zip(self.gradient, other.gradient)),
                   self.value * other.laplacian
                   + other.value * self.laplacian + 2 * cross)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        exponent = F(exponent)
        if exponent.denominator == 1 and exponent >= 0:
            result = self.constant(1)
            for _ in range(exponent.numerator):
                result = result * self
            return result
        v = rational_power(self.value, exponent)
        first = exponent * v / self.value
        second = exponent * (exponent - 1) * v / (self.value ** 2)
        return Jet(v, tuple(first * a for a in self.gradient),
                   first * self.laplacian
                   + second * sum(a * a for a in self.gradient))


def variables(positions, d):
    n = len(positions)
    # The rational unit direction keeps all interparticle radii rational while
    # full Nd jets retain all transverse derivatives in the Laplacian.
    direction = [F(3, 5), F(4, 5)] + [F(0)] * (d - 2)
    out = []
    for i, scalar in enumerate(positions):
        row = []
        for a in range(d):
            grad = [F(0)] * (n * d)
            grad[i * d + a] = F(1)
            row.append(Jet(F(scalar) * direction[a], tuple(grad), F(0)))
        out.append(row)
    return out


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def evaluate_model(d, s, positions, background):
    s = F(s)
    x = variables(positions, d)
    n = len(x)
    zero = x[0][0].constant(0)
    energy = zero
    b = []
    expected_laplacian = F(0)
    for row in x:
        brow = []
        for xa in row:
            if background == "polynomial":
                energy += F(1, 2) * xa ** 2 + F(1, 12) * xa ** 4
                brow.append(-xa - F(1, 3) * xa ** 3)
                expected_laplacian += 1 + xa.value ** 2
            else:
                brow.append(zero)
        b.append(brow)

    kval = {}
    kjet = {}
    for i in range(n):
        for j in range(i + 1, n):
            z = [x[i][a] - x[j][a] for a in range(d)]
            q = sum((za ** 2 for za in z), zero)
            energy += F(1, n) * q ** (-s / 2)
            k = [s * za * q ** (-s / 2 - 1) for za in z]
            kjet[i, j] = k
            kjet[j, i] = [-ka for ka in k]
            kval[i, j] = [ka.value for ka in k]
            kval[j, i] = [-ka.value for ka in k]
            expected_laplacian += (F(2, n) * s * (s + 2 - d)
                                   * rational_power(q.value, -s / 2 - 1))

    drift = []
    divergence = F(0)
    for i in range(n):
        row = []
        for a in range(d):
            entry = b[i][a] + F(1, n) * sum(
                (kjet[i, j][a] for j in range(n) if j != i), zero)
            row.append(entry.value)
            divergence += entry.gradient[i * d + a]
            check("raw_energy_vs_direct_force",
                  entry.value == -energy.gradient[i * d + a],
                  [d, str(s), n, background, i, a])
        drift.append(row)

    check("full_laplacian", energy.laplacian == expected_laplacian,
          [d, str(s), n, background])
    check("full_divergence", divergence == -energy.laplacian,
          [d, str(s), n, background])

    norm = sum(dot(row, row) for row in drift)
    base = sum(dot([a.value for a in row], [a.value for a in row]) for row in b)
    base_cross = F(2, n) * sum(
        dot([a.value for a in b[i]], kval[i, j])
        for i in range(n) for j in range(n) if j != i)
    pair_squares = F(2, n * n) * sum(
        dot(kval[i, j], kval[i, j]) for i in range(n) for j in range(i + 1, n))
    triple_cross = F(1, n * n) * sum(
        dot(kval[i, j], kval[i, k]) for i in range(n)
        for j in range(n) if j != i for k in range(n) if k != i and k != j)
    check("full_square_with_triples",
          norm == base + base_cross + pair_squares + triple_cross,
          [d, str(s), n, background])
    check("gradient_dissipation", norm == dot(energy.gradient, energy.gradient),
          [d, str(s), n, background])
    for nu in [F(0), F(1, 7), F(5)] :
        generator_from_coordinates = sum(
            drift[i][a] * energy.gradient[i * d + a]
            for i in range(n) for a in range(d)) + nu * energy.laplacian
        check("ito_generator_and_noise_factor",
              generator_from_coordinates == -norm + nu * expected_laplacian,
              [d, str(s), n, background, str(nu)])
    if background == "constant":
        check("superharmonic_sign", energy.laplacian <= 0, [d, str(s), n])
        if s == d - 2:
            check("coulomb_punctured_laplacian", energy.laplacian == 0,
                  [d, str(s), n])
        if n == 3 and list(positions) == [-positions[2], F(0), positions[2]]:
            middle_cross = 2 * dot(kval[1, 0], kval[1, 2])
            check("triple_cluster_cancellation", all(v == 0 for v in drift[1]),
                  [d, str(s), str(positions[2])])
            check("negative_cross_term_retained", middle_cross < 0,
                  [d, str(s), str(positions[2])])
            check("nonzero_total_cluster_dissipation", norm > 0,
                  [d, str(s), str(positions[2])])
    return energy.value


def count_and_bound_checks():
    for n in [2, 3, 4, 7, 31]:
        for a in [F(0), F(2, 7), F(3)]:
            for kappa in [F(0), F(5, 11), F(8)]:
                ordered = sum(-kappa / n for i in range(n)
                              for j in range(n) if i != j)
                unordered = sum(-2 * kappa / n for i in range(n)
                                for j in range(i + 1, n))
                c = n * a + (n - 1) * kappa
                check("ordered_unordered_divergence", ordered == unordered,
                      [n, str(kappa)])
                check("density_and_energy_constant", -n * a + ordered == -c,
                      [n, str(a), str(kappa)])
                check("coulomb_compensation_count",
                      sum(2 * kappa / n for i in range(n)
                          for j in range(i + 1, n)) == (n - 1) * kappa,
                      [n, str(kappa)])
    for d in range(3, 9):
        for s in [F(1, 2), F(d - 2, 2), F(d - 2)]:
            gamma_recurrence = 4 * F(d - s - 2, 2) * F(s, 2)
            check("fourier_gamma_recurrence",
                  gamma_recurrence == s * (d - 2 - s), [d, str(s)])
            check("radial_laplacian_sign", s * (s + 2 - d) <= 0,
                  [d, str(s)])
    for n in [2, 3, 7]:
        for s in [1, 2, 3]:
            for denominator in [10, 100, 1000]:
                rho = F(1, denominator)
                a = F(3)
                bound = (rho ** (-s) - a) / n
                check("distance_exit_denominator", bound > 0,
                      [n, s, denominator])
                check("distance_exit_simplification",
                      bound >= rho ** (-s) / (2 * n), [n, s, denominator])


def solvable_checks():
    for n in [2, 3, 7]:
        for d, s in [(3, 1), (4, 1), (4, 2), (5, 3), (6, 4)]:
            for r in [F(1, 100), F(2, 7), F(3, 4)]:
                p = s + 2
                rdot = F(2 * s, n) * r ** (-s - 1)
                check("solvable_relative_power",
                      p * r ** (p - 1) * rdot == F(2 * s * p, n),
                      [n, d, s, str(r)])
                energy_derivative = -F(s, n) * r ** (-s - 1) * rdot
                square = F(2 * s * s, n * n) * r ** (-2 * s - 2)
                check("solvable_energy_identity", energy_derivative == -square,
                      [n, d, s, str(r)])
                dt_dr = F(n, 2 * s) * r ** (s + 1)
                check("solvable_integrated_dissipation",
                      square * dt_dr == F(s, n) * r ** (-s - 1),
                      [n, d, s, str(r)])
                for nu in [F(0), F(1, 3), F(2)]:
                    lap_g = s * (s + 2 - d) * r ** (-s - 2)
                    relative = -square + F(2, n) * nu * lap_g
                    full = energy_derivative + nu * F(2, n) * lap_g
                    check("relative_diffusion_factor", relative == full,
                          [n, d, s, str(r), str(nu)])
    DETAILS.append("The exact two-particle SDE has N=2; other N in this test"
                   " check the algebra of an assigned relative coefficient only.")


def main():
    count_and_bound_checks()
    solvable_checks()
    tuples = [(3, 1), (4, 1), (4, 2), (5, 2), (5, 3), (6, 4)]
    models = 0
    for d, s in tuples:
        for eps in [F(1, 100), F(1, 1000)]:
            shapes = [[F(0), eps], [-eps, F(0), eps],
                      [F(0), eps, F(1, 5)],
                      [F(0), eps, F(1, 8), F(1, 8) + eps]]
            for shape in shapes:
                for background in ["constant", "polynomial"]:
                    value = evaluate_model(d, s, shape, background)
                    models += 1
                    if background == "constant":
                        n = len(shape)
                        close_pair_count = 2 if n == 4 else 1
                        check("partial_cluster_energy_lower_bound",
                              value >= F(close_pair_count, n) * eps ** (-s),
                              [d, s, n, str(eps)])
    for s in [1, 2, 3, 4]:
        e1, e2 = F(1, 100), F(1, 1000)
        h1 = F(1, 3) * (2 * e1 ** (-s) + (2 * e1) ** (-s))
        h2 = F(1, 3) * (2 * e2 ** (-s) + (2 * e2) ** (-s))
        check("triple_collision_exact_scaling", h2 == 10 ** s * h1, s)
    payload = {
        "task": "TASK-045",
        "status": "PASS",
        "evidence_class": "EXACT_RATIONAL_SELF_CHECK_NOT_INDEPENDENT_AUDIT",
        "arithmetic": "Python standard-library Fraction; no floating-point values",
        "random_seed": None,
        "tolerance": None,
        "models_differentiated": models,
        "checks_by_category": COUNTS,
        "total_checks": sum(COUNTS.values()),
        "dimension_exponent_tuples": tuples,
        "finite_particle_counts_in_models": [2, 3, 4],
        "additional_counting_tests": [7, 31],
        "diffusivity_tests": ["0", "1/7", "5", "1/3", "2"],
        "details": DETAILS,
        "limits": [
            "No numerical SDE simulation or source theorem verification is implied.",
            "Euclidean principal powers and polynomial backgrounds test local coefficients only.",
            "Periodic compensation, noncollision, measurability, and measure passage require the written proof.",
            "This checker neither supplies pair-inverse derivatives nor certifies a fluctuation theorem."
        ],
    }
    output = Path(__file__).with_name("round006_particle_realization_exact_output.json")
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
