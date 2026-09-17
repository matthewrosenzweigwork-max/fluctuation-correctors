#!/usr/bin/env python3
"""Independent exact arithmetic checks supporting TASK-027's hostile review."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


COUNTS: Counter[str] = Counter()


def eq(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: {left} != {right}")
    COUNTS[label] += 1


def le(left, right, label):
    if left > right:
        raise AssertionError(f"{label}: {left} > {right}")
    COUNTS[label] += 1


def characteristic_checks():
    for d in range(1, 7):
        for ratio in (F(1, 4), F(1, 2), F(3, 4), F(7, 8)):
            s = d * ratio
            p = s + 2
            c = 2 * s * p
            alpha = 2 / p
            eq(alpha * c / 4, s, "far_leading_coefficient")
            eq(alpha * (alpha - 1) * c ** 2 / 8, -s ** 3,
               "far_second_coefficient")
            eq(alpha * (alpha - 1) * (alpha - 2) * c ** 3 / 24,
               F(4, 3) * s ** 4 * (s + 1), "far_third_coefficient")
            eq(alpha / 4, 1 / (2 * p), "near_first_nonpolynomial_coefficient")
            eq(2 - 4 / p, 2 * s / p, "large_core_n_power")
            eq(2 - (d + 4) / p, (2 * s - d) / p, "small_core_n_power")
            eq(-1 + (2 * s - d) / p, -(d + 2 - s) / p,
               "supercritical_endpoint_power")
            eq(d + 4 - (d - 2 * s), 2 * p, "subcritical_ell_power")
            eq(2 * s / p - 1 + (d + 2 - s) / p, d / p,
               "all_n_constant_enlargement_power")
            le(0, (d + 2 - s) / p, "positive_endpoint_decay_exponent")
            eq((-s - 1) - s, -2 * s - 1, "annular_source_power")
            num, den = s.numerator, s.denominator
            rbase, endbase = F(1, 2), F(2)
            r, end = rbase ** den, endbase ** den
            r_p, end_p = rbase ** (num + 2 * den), endbase ** (num + 2 * den)
            for n in (2, 3, 7):
                tau = n * (end_p - r_p) / c
                eq(r_p + c * tau / n, end_p, "characteristic_endpoint")
                f = F(n, 4) * (end ** 2 - r ** 2)
                le(0, f, "positive_radial_amplitude")
                f_tau = s * endbase ** (-num)
                f_r = F(n, 2) * (rbase ** (num + den)
                                  * endbase ** (-num) - r)
                drift = F(2, n) * s * rbase ** (-num - den)
                eq(-f_tau + drift * f_r, -s * rbase ** (-num),
                   "direct_pde_substitution")
                eq(F(n, 4) * (r ** 2 - r ** 2), 0, "zero_terminal_value")
                eq(F(n, 2) * (rbase ** (num + den) * rbase ** (-num) - r),
                   0, "zero_terminal_spatial_derivative")


def angular_checks():
    for d in range(1, 7):
        matrices = [
            [[F(int(i == j)) for j in range(d)] for i in range(d)],
            [[F((i + 1) * (j + 1)) for j in range(d)] for i in range(d)],
        ]
        if d >= 2:
            matrices.append([[F((1 if i == 0 else -1 if i == 1 else 0)
                                if i == j else 0) for j in range(d)]
                             for i in range(d)])
        for a in matrices:
            contraction = F(0)
            for i, j, k, ell in product(range(d), repeat=4):
                wick = int(i == j and k == ell) + int(i == k and j == ell)
                wick += int(i == ell and j == k)
                contraction += a[i][j] * a[k][ell] * F(wick, d * (d + 2))
            trace = sum(a[i][i] for i in range(d))
            trace_square = sum(a[i][j] * a[j][i]
                               for i in range(d) for j in range(d))
            eq(contraction, (trace ** 2 + 2 * trace_square) / (d * (d + 2)),
               "angular_fourth_moment_contraction")
            le(0, contraction, "nonnegative_angular_square")
        if d >= 2:
            eq(F(4, d * (d + 2)), 2 * F(2, d * (d + 2)),
               "traceless_angular_square")


def iid_checks():
    probs = [F(1, 6), F(1, 3), F(1, 2)]
    kernel = [[F(v) for v in row] for row in
              [[2, -1, 3], [-1, 4, 0], [3, 0, -2]]]
    row = [sum(probs[j] * kernel[i][j] for j in range(3)) for i in range(3)]
    m = sum(probs[i] * row[i] for i in range(3))
    q = [v - m for v in row]
    canon = [[kernel[i][j] - m - q[i] - q[j] for j in range(3)]
             for i in range(3)]
    q2 = sum(probs[i] * q[i] ** 2 for i in range(3))
    c2 = sum(probs[i] * probs[j] * canon[i][j] ** 2
             for i in range(3) for j in range(3))
    norm2 = sum(probs[i] * probs[j] * kernel[i][j] ** 2
                for i in range(3) for j in range(3))
    for n in (2, 3):
        mean = moment = F(0)
        for sample in product(range(3), repeat=n):
            weight = F(1)
            for x in sample:
                weight *= probs[x]
            direct = (sum(kernel[sample[i]][sample[j]]
                          for i in range(n) for j in range(n) if i != j)
                      / (2 * n ** 2) - sum(row[x] for x in sample) / n + m / 2)
            projected = (-m / (2 * n) - sum(q[x] for x in sample) / n ** 2
                         + sum(canon[sample[i]][sample[j]]
                               for i in range(n) for j in range(i + 1, n))
                         / n ** 2)
            eq(direct, projected, "iid_full_centering_decomposition")
            mean += weight * direct
            moment += weight * direct ** 2
        eq(mean, -m / (2 * n), "iid_nonzero_mean")
        eq(moment, m ** 2 / (4 * n ** 2) + q2 / n ** 3
           + F(n - 1, 2 * n ** 3) * c2, "iid_exact_second_moment")
        le(moment, F(n - 1, 2 * n ** 3) * norm2, "iid_sharp_bound")
        if n == 2:
            eq(moment, norm2 / 16, "n2_all_kernel_equality")
    density = [F(1, 2), F(1), F(3, 2)]
    for z in range(3):
        autocorrelation = sum(density[(y + z) % 3] * density[y]
                              for y in range(3)) / 3
        le(autocorrelation, max(density), "one_density_factor")
    for n in range(2, 22):
        beta = F(n ** 4) if n % 2 == 0 else F(1, n ** 4)
        b = min(beta, F(1))
        eq(b, F(1) if n % 2 == 0 else F(1, n ** 4),
           "varying_temperature_minimum")
        eq(n * b * F(n - 1, 2 * n ** 3), b * F(n - 1, 2 * n ** 2),
           "scaled_iid_coefficient")


def main():
    characteristic_checks()
    angular_checks()
    iid_checks()
    print(json.dumps({
        "task": "TASK-027",
        "status": "PASS",
        "arithmetic": "fractions.Fraction; exhaustive coefficient and finite-sum checks",
        "checks_by_category": dict(sorted(COUNTS.items())),
        "total_checks": sum(COUNTS.values()),
        "scope": "Computational support for the independent written hostile review."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
