#!/usr/bin/env python3
"""Independent exact support for TASK-026; no submitted worker code is used.

Finite cyclic Haar laws check pair-indicator moments and centering algebra.
Rational parameter checks verify constants and exponents, not an asymptotic
Riesz theorem. Universal and real-space arguments are supplied in the audit.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


checks = Counter()


def check(name, truth):
    if not truth:
        raise AssertionError(name)
    checks[name] += 1


def raw_pair(values, sample):
    n = len(sample)
    group_order = len(values)
    return sum(
        values[(sample[i] - sample[j]) % group_order]
        for i in range(n)
        for j in range(i + 1, n)
    ) / (n * n)


group_order = 5
potential = tuple(map(F, (10, 1, -6, -6, 1)))
check("zero_mean_potential", sum(potential) == 0)
for inner_set in ({0}, {0, 1, 4}, {0, 2, 3}):
    q = F(len(inner_set), group_order)
    inner = tuple(value if x in inner_set else F(0) for x, value in enumerate(potential))
    outer = tuple(potential[x] - inner[x] for x in range(group_order))
    tau = sum(inner) / group_order
    absolute_mass = sum(abs(value) for value in inner) / group_order
    centered_inner = tuple(value - tau for value in inner)
    centered_outer = tuple(value + tau for value in outer)
    norm_inner = sum(abs(value) for value in centered_inner) / group_order
    variance_outer = sum(value ** 2 for value in centered_outer) / group_order
    check("inner_L1_norm", norm_inner <= 2 * absolute_mass)
    check("centered_kernel_sum", all(centered_inner[x] + centered_outer[x] == potential[x] for x in range(group_order)))
    check("centered_kernel_means", sum(centered_inner) == sum(centered_outer) == 0)

    shared_joint = F(0)
    triangle_joint = F(0)
    for sample in product(range(group_order), repeat=3):
        first = (sample[0] - sample[1]) % group_order in inner_set
        second = (sample[0] - sample[2]) % group_order in inner_set
        third = (sample[1] - sample[2]) % group_order in inner_set
        if first and second:
            shared_joint += F(1, group_order ** 3)
        if first and second and third:
            triangle_joint += F(1, group_order ** 3)
    check("shared_label_pair_independence", shared_joint == q ** 2)
    if inner_set == {0}:
        check("not_mutually_independent", triangle_joint != q ** 3)

    for n in range(2, 6):
        pair_count = F(n * (n - 1), 2)
        ez = F(0)
        ez2 = F(0)
        positive_probability = F(0)
        eabs_inner = F(0)
        eabs_outer = F(0)
        eabs_full = F(0)
        second_outer = F(0)
        mean_outer = F(0)
        for sample in product(range(group_order), repeat=n):
            weight = F(1, group_order ** n)
            z = sum(
                (sample[i] - sample[j]) % group_order in inner_set
                for i in range(n)
                for j in range(i + 1, n)
            )
            ez += weight * z
            ez2 += weight * z * z
            positive_probability += weight * bool(z)
            pg = raw_pair(potential, sample)
            po = raw_pair(centered_outer, sample)
            pi = raw_pair(centered_inner, sample)
            raw_inner = raw_pair(inner, sample)
            check("global_centered_decomposition", pg == po + pi)
            check("positive_inner_decomposition", pg == po + raw_inner - F(n - 1, 2 * n) * tau)
            eabs_inner += weight * abs(pi)
            eabs_outer += weight * abs(po)
            eabs_full += weight * abs(pg)
            second_outer += weight * po * po
            mean_outer += weight * po
        m = pair_count * q
        check("exact_count_mean", ez == m)
        check("exact_count_second_moment", ez2 == m + pair_count * (pair_count - 1) * q ** 2)
        check("count_second_upper", ez2 <= m + m * m)
        check("count_positive_lower", positive_probability >= m * m / ez2 >= m / (1 + m))
        check("outer_exact_mean", mean_outer == 0)
        check("outer_exact_variance", second_outer == F(n - 1, 2 * n ** 3) * variance_outer)
        check("inner_exact_coefficient", eabs_inner <= F(n - 1, 2 * n) * norm_inner)
        inner_bound = F(n - 1, n) * absolute_mass
        check("inner_absolute_mass_bound", eabs_inner <= inner_bound)
        check("outer_Cauchy_bound", eabs_outer ** 2 <= second_outer)
        check("full_L1_triangle", eabs_full <= eabs_inner + eabs_outer)
        check("full_L1_combined_bound", max(eabs_full - inner_bound, F(0)) ** 2 <= second_outer)


def exact_two_power(exponent):
    exponent = F(exponent)
    if exponent.denominator != 1:
        raise AssertionError("noninteger power in exact arithmetic")
    if exponent >= 0:
        return F(2 ** exponent.numerator)
    return F(1, 2 ** (-exponent.numerator))


# Treat the geometric volume as an arbitrary positive parameter. Actual torus
# volumes need not be rational; the analytic calculation covers those values.
for d in range(1, 7):
    for ratio in (F(3, 5), F(2, 3), F(3, 4), F(4, 5), F(7, 8), F(9, 10)):
        s = d * ratio
        check("strict_positive_power", 2 * s - d > 0)
        for volume in (F(2), F(7, 3)):
            c0 = volume / (4 * (1 + volume / 2))
            for c_tau in (F(1), F(3), F(11)):
                for c_var in (F(2), F(8), F(50)):
                    exponent = s.denominator
                    while True:
                        delta_s_inverse = exact_two_power(exponent * s)
                        delta_d = exact_two_power(-exponent * d)
                        delta_2s = exact_two_power(-2 * exponent * s)
                        if delta_s_inverse >= 2 * c_tau and 32 * c_var * delta_2s <= c0 * delta_d / 2:
                            break
                        exponent += s.denominator
                    check("compatible_fixed_delta", exponent > 0)
                    check("mean_absorption", delta_s_inverse / 2 - c_tau / 2 >= delta_s_inverse / 4)
                    check("Chebyshev_constant", (c_var / 2) / (delta_s_inverse / 8) ** 2 == 32 * c_var * delta_2s)
                    check("bad_event_smaller", 32 * c_var * delta_2s <= c0 * delta_d / 2)
                    check("threshold_after_cancellation", delta_s_inverse / 4 - delta_s_inverse / 8 == delta_s_inverse / 8)
                    for n in (2, 3, 7):
                        m = volume * delta_d * F(n - 1, 2 * n)
                        check("finite_N_count_interval", volume * delta_d / 4 <= m <= volume * delta_d / 2)
                        check("c0_lower_constant", m / (1 + m) >= c0 * delta_d)
        radius_power = -F(2, d)
        u_power = 2 * ratio - 2
        check("spike_power", -2 - s * radius_power == u_power)
        check("discarded_mean_power", (d - s) * radius_power == u_power)
        check("outer_variance_power", -2 + (d - 2 * s) * radius_power == 2 * u_power)
        check("L1_outer_power", -F(1, 2) + (2 * s - d) / d == 2 * ratio - F(3, 2))
        check("L1_inner_power", F(1, 2) - 2 * (d - s) / d == 2 * ratio - F(3, 2))
        for gamma in (F(0), F(1, 4), F(1), F(3)):
            check("scaled_square_root_A", (1 - gamma) / 2 + u_power == (4 * ratio - 3 - gamma) / 2)

# At the L2 endpoint, the same radius balances an N^-1/2 inner rate with the
# logarithmic outer norm. No logarithm is approximated numerically.
for d in range(1, 9):
    s = F(d, 2)
    check("endpoint_inner_power", F(1, 2) - F(2, d) * (d - s) == -F(1, 2))
    check("explicit_radius_threshold", (2 ** d) ** 2 == 4 ** d)
    for k0, omega, log_value in product((F(0), F(1), F(7)), (F(1), F(3)), (F(0), F(1, 2), F(4))):
        check("endpoint_constant_majorant", k0 / 2 + 2 * omega * log_value / d <= (k0 / 2 + 2 * omega / d) * (1 + log_value))

print(json.dumps({
    "status": "PASS",
    "total_checks": sum(checks.values()),
    "checks_by_category": dict(sorted(checks.items())),
    "arithmetic": "standard-library exact integers and fractions",
    "submitted_worker_code_read_or_run": False,
    "scope": "finite algebra and constant checks; analytic review proves universal probability bounds and asymptotic consequences",
}, indent=2, sort_keys=True))
