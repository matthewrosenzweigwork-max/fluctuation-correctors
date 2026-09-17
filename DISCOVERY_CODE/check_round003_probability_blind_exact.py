#!/usr/bin/env python3
"""Exact finite-sum and exponent self-checks for the TASK-024 reconstruction.

The cyclic-group examples test the finite-N centering algebra only; they do
not stand in for the continuous singularity proof or an independent audit.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


COUNTS: Counter[str] = Counter()


def equal(left, right, category: str) -> None:
    if left != right:
        raise AssertionError(f"{category}: {left} != {right}")
    COUNTS[category] += 1


def less_equal(left, right, category: str) -> None:
    if left > right:
        raise AssertionError(f"{category}: {left} > {right}")
    COUNTS[category] += 1


def cyclic_checks() -> None:
    size = 5
    g = [F(v) for v in (8, -3, -1, -1, -3)]
    equal(sum(g), 0, "zero_original_mean")
    for discarded in ({0}, {0, 1, 4}):
        outer = [F(0) if x in discarded else g[x] for x in range(size)]
        inner = [g[x] if x in discarded else F(0) for x in range(size)]
        m = sum(outer) / size
        a = sum(inner) / size
        dmass = sum(abs(v) for v in inner) / size
        h = [v - m for v in outer]
        j = [v - a for v in inner]
        equal(a, -m, "opposite_truncation_means")
        equal(sum(h), 0, "zero_outer_mean")
        equal(sum(j), 0, "zero_inner_mean")
        h2 = sum(v * v for v in h) / size
        outer2 = sum(v * v for v in outer) / size
        equal(h2, outer2 - m * m, "centered_outer_kernel_variance")
        j1 = sum(abs(v) for v in j) / size
        less_equal(j1, 2 * dmass, "centered_inner_mass_bound")
        for n in (2, 3, 4):
            weight = F(1, size ** n)
            mean_g = mean_h = mean_outer = mean_campaign = F(0)
            moment_h = abs_inner = bad_probability = F(0)
            for sample in product(range(size), repeat=n):
                diffs = [(sample[i] - sample[k]) % size
                         for i in range(n) for k in range(i + 1, n)]
                bare = sum(g[x] for x in diffs) / n ** 2
                fout = sum(outer[x] for x in diffs) / n ** 2
                zout = sum(h[x] for x in diffs) / n ** 2
                zin = sum(j[x] for x in diffs) / n ** 2
                campaign = fout - m / 2
                equal(bare, zout + zin, "global_centered_split")
                equal(zout, campaign + m / (2 * n),
                      "campaign_vs_exact_centering")
                equal(zout, fout - F(n - 1, 2 * n) * m,
                      "finite_n_outer_mean_subtraction")
                good = all(x not in discarded for x in diffs)
                if good:
                    equal(bare, zout + F(n - 1, 2 * n) * m,
                          "on_event_discarded_mean")
                    equal(bare, fout, "on_event_bare_equality")
                else:
                    bad_probability += weight
                mean_g += weight * bare
                mean_h += weight * zout
                mean_outer += weight * fout
                mean_campaign += weight * campaign
                moment_h += weight * zout ** 2
                abs_inner += weight * abs(zin)
            equal(mean_g, 0, "mean_original_statistic")
            equal(mean_h, 0, "mean_centered_outer_statistic")
            equal(mean_outer, F(n - 1, 2 * n) * m, "mean_outer_bare_statistic")
            equal(mean_campaign, -m / (2 * n), "mean_campaign_statistic")
            equal(moment_h, F(n - 1, 2 * n ** 3) * h2,
                  "exact_centered_outer_variance")
            less_equal(abs_inner, F(n - 1, 2 * n) * j1,
                       "exact_inner_l1_factor")
            less_equal(abs_inner, F(n - 1, n) * dmass,
                       "discarded_mass_l1_bound")
            less_equal(bad_probability,
                       F(n * (n - 1), 2) * F(len(discarded), size),
                       "close_pair_union_bound")
            for beta in (F(1, 7), F(1), F(9)):
                b = min(beta, F(1))
                equal(n * b * moment_h,
                      b * F(n - 1, 2 * n ** 2) * h2,
                      "temperature_variance_coefficient")


def exponent_checks() -> None:
    for d in range(1, 9):
        for ratio in (F(1, 4), F(1, 2), F(2, 3), F(3, 4), F(7, 8)):
            s = d * ratio
            tau = (d - s) / 2
            equal(s - F(d, 2) + 2 * tau, F(d, 2),
                  "heat_prefactor_pi_exponent")
            equal(tau - F(d, 2) + s / 2, 0,
                  "principal_singularity_four_exponent")
            equal(-2 * tau, s - d, "frozen_fourier_power")
            if ratio > F(1, 2):
                q = 2 * s - d
                p = d - s
                aexp = 4 * ratio - 3
                equal(-1 + 2 * q / d, aexp, "variance_n_exponent")
                equal(1 - 4 * p / d, aexp, "squared_mean_n_exponent")
                equal(1 - q / (2 * q), F(1, 2),
                      "chosen_radius_variance_a_exponent")
                equal(1 + 2 * p / (2 * q), 1 + p / q,
                      "chosen_radius_mean_a_exponent")
                less_equal(0, d / (2 * q), "positive_collision_a_exponent")
                equal(-F(1, 2) + q / d, 2 * ratio - F(3, 2),
                      "outer_l1_n_exponent")
                equal(F(1, 2) - 2 * p / d, 2 * ratio - F(3, 2),
                      "inner_l1_n_exponent")
                equal(2 * (2 * ratio - F(3, 2)), aexp,
                      "l1_rate_is_sqrt_a")
        equal(2 - F(3, d) * d, -1, "l2_boundary_collision_power")
        equal(1 - F(3, d) * d, -2, "l2_boundary_squared_mean_power")
        equal(4 * F(3, 4) - 3, 0, "probability_sufficient_threshold")


def main() -> None:
    cyclic_checks()
    exponent_checks()
    print(json.dumps({
        "task": "TASK-024",
        "status": "PASS",
        "evidence": "EXACT_FINITE_SUM_AND_EXPONENT_SELF_CHECK",
        "arithmetic": "fractions.Fraction; exhaustive finite enumeration",
        "checks_by_category": dict(sorted(COUNTS.items())),
        "total_checks": sum(COUNTS.values()),
        "limitations": "Same-context support for the written reconstruction; no audit verdict."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
