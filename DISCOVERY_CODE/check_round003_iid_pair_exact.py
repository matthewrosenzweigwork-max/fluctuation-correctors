#!/usr/bin/env python3
"""Exact self-checks for TASK-021; no numerical inference is used in its proof.

Finite probability spaces here can be realized by cellwise constant kernels
on a partition of the Haar torus with the displayed cell probabilities.
All sample sums are evaluated directly from the ordered deleted-label formula.
This program is a construction self-check, not an independent audit.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from math import prod


CHECKS: Counter[str] = Counter()


def equal(left: F | int, right: F | int, category: str) -> None:
    if left != right:
        raise AssertionError(f"{category}: {left} != {right}")
    CHECKS[category] += 1


def less_equal(left: F | int, right: F | int, category: str) -> None:
    if left > right:
        raise AssertionError(f"{category}: {left} > {right}")
    CHECKS[category] += 1


def projections(p: tuple[F, ...], phi: list[list[F]]):
    size = len(p)
    row = [sum(p[y] * phi[x][y] for y in range(size)) for x in range(size)]
    theta = sum(p[x] * row[x] for x in range(size))
    h = [row[x] - theta for x in range(size)]
    canon = [[phi[x][y] - theta - h[x] - h[y] for y in range(size)]
             for x in range(size)]
    h2 = sum(p[x] * h[x] ** 2 for x in range(size))
    canon2 = sum(p[x] * p[y] * canon[x][y] ** 2
                 for x in range(size) for y in range(size))
    phi2 = sum(p[x] * p[y] * phi[x][y] ** 2
               for x in range(size) for y in range(size))
    equal(phi2, theta ** 2 + 2 * h2 + canon2, "orthogonal_kernel_norm")
    equal(sum(p[x] * h[x] for x in range(size)), 0, "zero_first_projection")
    for x in range(size):
        equal(sum(p[y] * canon[x][y] for y in range(size)), 0,
              "zero_canonical_projection")
    return row, theta, h, canon, h2, canon2, phi2


def check_kernel(p: tuple[F, ...], phi: list[list[F]], name: str) -> None:
    row, theta, h, canon, h2, canon2, phi2 = projections(p, phi)
    size = len(p)
    for n in (2, 3, 4, 5):
        mean = F(0)
        moment = F(0)
        cond1 = [F(0) for _ in range(size)]
        cond2 = [[F(0) for _ in range(size)] for _ in range(size)]
        for sample in product(range(size), repeat=n):
            weight = prod(p[x] for x in sample)
            direct = (sum(phi[sample[i]][sample[j]]
                          for i in range(n) for j in range(n) if i != j)
                      / (2 * n ** 2)
                      - sum(row[x] for x in sample) / n + theta / 2)
            decomposed = (-theta / (2 * n) - sum(h[x] for x in sample) / n ** 2
                          + sum(canon[sample[i]][sample[j]]
                                for i in range(n) for j in range(i + 1, n))
                          / n ** 2)
            equal(direct, decomposed, "pointwise_ordered_sum")
            mean += weight * direct
            moment += weight * direct ** 2
            cond1[sample[0]] += weight * direct / p[sample[0]]
            cond2[sample[0]][sample[1]] += (
                weight * direct / (p[sample[0]] * p[sample[1]]))

        predicted = (theta ** 2 / (4 * n ** 2) + h2 / n ** 3
                     + F(n - 1, 2 * n ** 3) * canon2)
        equal(mean, -theta / (2 * n), "nonzero_mean_coefficient")
        equal(moment, predicted, "exact_second_moment")
        equal(moment - mean ** 2,
              h2 / n ** 3 + F(n - 1, 2 * n ** 3) * canon2,
              "exact_variance")
        less_equal(moment, F(n - 1, 2 * n ** 3) * phi2, "sharp_l2_bound")
        for x in range(size):
            equal(cond1[x] - mean, -h[x] / n ** 2, "conditional_first_projection")
            for y in range(size):
                equal(cond2[x][y] - cond1[x] - cond1[y] + mean,
                      canon[x][y] / n ** 2, "conditional_second_projection")
        if n == 2:
            equal(moment, phi2 / 16, "n2_all_kernel_equality")
        if name == "canonical":
            equal(moment, F(n - 1, 2 * n ** 3) * phi2, "canonical_sharpness")
        if name == "constant":
            equal(moment, phi[0][0] ** 2 / (4 * n ** 2), "constant_test")
        if name == "separable":
            f = [F(-1), F(0), F(2)]
            m = sum(p[x] * f[x] for x in range(size))
            variance = sum(p[x] * (f[x] - m) ** 2 for x in range(size))
            equal(moment, m ** 4 / (4 * n ** 2) + m ** 2 * variance / n ** 3
                  + F(n - 1, 2 * n ** 3) * variance ** 2, "separable_test")


def main() -> None:
    distributions = [(F(1, 6), F(1, 3), F(1, 2)), (F(1, 3),) * 3]
    cases = 0
    for p in distributions:
        f = [F(-1), F(0), F(2)]
        m = sum(p[x] * f[x] for x in range(3))
        u = [v - m for v in f]
        kernels = {
            "constant": [[F(2) for _ in range(3)] for _ in range(3)],
            "separable": [[x * y for y in f] for x in f],
            "canonical": [[x * y for y in u] for x in u],
            "additive": [[F(3) + x + y for y in u] for x in u],
            "general": [[F(v) for v in row] for row in
                        [[3, -2, 1], [-2, 5, 4], [1, 4, -1]]],
            "zero": [[F(0) for _ in range(3)] for _ in range(3)],
        }
        for name, phi in kernels.items():
            check_kernel(p, phi, name)
            cases += 1

    for n in (2, 3, 10, 101):
        for beta in (F(1, 7), F(1), F(9)):
            b = min(beta, F(1))
            scaled = n * b * F(n - 1, 2 * n ** 3)
            equal(scaled, b / (2 * n) * (1 - F(1, n)), "temperature_prefactor")
            less_equal(b / (4 * n), scaled, "temperature_lower_bound")
            less_equal(scaled, b / (2 * n), "temperature_upper_bound")

    for d in range(1, 9):
        for n in range(1, 11):
            shell = (2 * n + 1) ** d - (2 * n - 1) ** d
            less_equal(2 * d * n ** (d - 1), shell, "lattice_shell_lower")
            less_equal(shell, 2 * d * 3 ** (d - 1) * n ** (d - 1),
                       "lattice_shell_upper")
        for ratio in (F(2, 3), F(3, 4), F(7, 8), F(99, 100)):
            s = ratio * d
            alpha = 2 * s - d
            equal(-1 + F(2, d) * alpha / 2, 2 * ratio - 2,
                  "cutoff_2_over_d_exponent")
            equal(-1 + F(4, d) * alpha / 2, 4 * ratio - 3,
                  "cutoff_4_over_d_exponent")
            less_equal(2 * ratio - 2, 0, "first_cutoff_negative_exponent")
        equal(4 * F(3, 4) - 3, 0, "second_cutoff_threshold")
        less_equal(4 * F(2, 3) - 3, 0, "below_second_threshold")
        less_equal(0, 4 * F(7, 8) - 3, "above_second_threshold")

    print(json.dumps({
        "task": "TASK-021",
        "evidence": "EXACT_FINITE_SUM_SELF_CHECK",
        "status": "PASS",
        "kernel_distribution_cases": cases,
        "particle_numbers": [2, 3, 4, 5],
        "arithmetic": "fractions.Fraction; exhaustive enumeration; no random sampling",
        "checks_by_category": dict(sorted(CHECKS.items())),
        "total_checks": sum(CHECKS.values()),
        "limitations": "Supports the written proof; not an independent mathematical audit."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
