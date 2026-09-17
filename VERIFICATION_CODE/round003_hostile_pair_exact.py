#!/usr/bin/env python3
"""Independent exact algebra checks for TASK-023, using only the standard library.

No constructor code is read or invoked. These finite checks support the analytic
audit; they do not prove the infinite-dimensional or asymptotic assertions.
Finite probability spaces test the projection algebra. The cyclic model tests
the truncation identity with its finite-N mean shift, not Riesz asymptotics.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


checks = Counter()


def verify(category, condition):
    if not condition:
        raise AssertionError(category)
    checks[category] += 1


def weighted_matrix_norm(matrix, weights):
    return sum(
        weights[x] * weights[y] * matrix[x][y] ** 2
        for x in range(len(weights))
        for y in range(len(weights))
    )


def original_statistic(sample, matrix, weights):
    n = len(sample)
    one = [
        sum(weights[y] * matrix[x][y] for y in range(len(weights)))
        for x in range(len(weights))
    ]
    theta = sum(weights[x] * one[x] for x in range(len(weights)))
    ordered = sum(
        matrix[sample[i]][sample[j]]
        for i in range(n)
        for j in range(n)
        if i != j
    )
    return F(ordered, 2 * n * n) - sum(one[x] for x in sample) / n + theta / 2


def sample_weight(sample, weights):
    answer = F(1)
    for x in sample:
        answer *= weights[x]
    return answer


def projection_battery(matrix, weights, ns):
    size = len(weights)
    one = [
        sum(weights[y] * matrix[x][y] for y in range(size))
        for x in range(size)
    ]
    theta = sum(weights[x] * one[x] for x in range(size))
    first = [value - theta for value in one]
    canonical = [
        [matrix[x][y] - theta - first[x] - first[y] for y in range(size)]
        for x in range(size)
    ]
    first_norm = sum(weights[x] * first[x] ** 2 for x in range(size))
    canon_norm = weighted_matrix_norm(canonical, weights)
    full_norm = weighted_matrix_norm(matrix, weights)
    verify("projection_centering", sum(weights[x] * first[x] for x in range(size)) == 0)
    for row in canonical:
        verify("projection_centering", sum(weights[y] * row[y] for y in range(size)) == 0)
    verify("orthogonal_norm", full_norm == theta ** 2 + 2 * first_norm + canon_norm)
    for n in ns:
        expectation = F(0)
        second_moment = F(0)
        first_conditional = [F(0) for _ in range(size)]
        second_conditional = [[F(0) for _ in range(size)] for _ in range(size)]
        for sample in product(range(size), repeat=n):
            probability = sample_weight(sample, weights)
            actual = original_statistic(sample, matrix, weights)
            decomposition = (
                -theta / (2 * n)
                - sum(first[x] for x in sample) / (n * n)
                + sum(
                    canonical[sample[i]][sample[j]]
                    for i in range(n)
                    for j in range(i + 1, n)
                ) / (n * n)
            )
            verify("pointwise_decomposition", actual == decomposition)
            expectation += probability * actual
            second_moment += probability * actual ** 2
            first_conditional[sample[0]] += probability * actual / weights[sample[0]]
            second_conditional[sample[0]][sample[1]] += (
                probability * actual / (weights[sample[0]] * weights[sample[1]])
            )
        predicted = (
            theta ** 2 / (4 * n * n)
            + first_norm / n ** 3
            + F(n - 1, 2 * n ** 3) * canon_norm
        )
        verify("exact_mean", expectation == -theta / (2 * n))
        verify("exact_second_moment", second_moment == predicted)
        verify(
            "exact_variance",
            second_moment - expectation ** 2
            == first_norm / n ** 3 + F(n - 1, 2 * n ** 3) * canon_norm,
        )
        bound = F(n - 1, 2 * n ** 3) * full_norm
        verify("sharp_inequality", second_moment <= bound)
        verify(
            "equality_scope",
            (second_moment == bound) == (n == 2 or (theta == 0 and first_norm == 0)),
        )
        for x in range(size):
            verify(
                "first_conditional_projection",
                first_conditional[x] - expectation == -first[x] / n ** 2,
            )
            for y in range(size):
                verify(
                    "second_conditional_projection",
                    second_conditional[x][y]
                    - first_conditional[x]
                    - first_conditional[y]
                    + expectation
                    == canonical[x][y] / n ** 2,
                )
        for beta in (F(1, 37), F(1, 2), F(1), F(7, 3), F(21)):
            b = min(beta, F(1))
            verify("temperature_coefficient", n * b * F(n - 1, 2 * n ** 3) == b * F(n - 1, 2 * n ** 2))
            verify("scaled_norm_bound", n * b * second_moment <= b * F(n - 1, 2 * n ** 2) * full_norm)


weights_two = (F(1, 3), F(2, 3))
for a, b, c in product((-2, 0, 3), repeat=3):
    projection_battery([[F(a), F(b)], [F(b), F(c)]], weights_two, range(2, 7))
for matrix in (
    [[F(4), F(-2)], [F(-2), F(1)]],
    [[F(4), F(1)], [F(1), F(-2)]],
    [[F(1), F(0)], [F(0), F(0)]],
):
    projection_battery(matrix, weights_two, range(2, 7))

weights_three = (F(1, 5), F(1, 3), F(7, 15))
for j in range(8):
    matrix = [
        [F(((x + 1) * (y + 1) * (j + 1) + x + y) % 9 - 4) for y in range(3)]
        for x in range(3)
    ]
    projection_battery(matrix, weights_three, range(2, 6))
for value in (-2, 0, 3):
    projection_battery([[F(value)]], (F(1),), range(2, 7))

# Atomic diagonal values are part of the product-law kernel, despite label deletion.
atomic_matrix = [[F(1), F(0)], [F(0), F(0)]]
verify("atomic_diagonal_witness", original_statistic((0, 0), atomic_matrix, weights_two) != 0)

# An iid hypothesis cannot be removed: perfectly shared centered signs yield
# a nonvanishing canonical statistic despite identical one-particle marginals.
for n in range(2, 8):
    shared_sign_value = original_statistic((0,) * n, [[F(1), F(-1)], [F(-1), F(1)]], (F(1, 2), F(1, 2)))
    verify("iid_scope_witness", shared_sign_value == F(n - 1, 2 * n))


def cyclic_truncation_battery():
    size = 7
    weights = (F(1, size),) * size
    potential = tuple(map(F, (12, 2, -3, -5, -5, -3, 2)))
    verify("cyclic_zero_mean", sum(potential) == 0)
    matrix_g = [[potential[(x - y) % size] for y in range(size)] for x in range(size)]
    for removed in ({0}, {0, 1, size - 1}):
        truncated = tuple(F(0) if x in removed else potential[x] for x in range(size))
        mean = sum(truncated) / size
        discarded = sum(potential[x] for x in removed) / size
        centered = tuple(value - mean for value in truncated)
        matrix_h = [[truncated[(x - y) % size] for y in range(size)] for x in range(size)]
        matrix_k = [[centered[(x - y) % size] for y in range(size)] for x in range(size)]
        variance_kernel = sum(value ** 2 for value in centered) / size
        verify("discarded_mean", mean == -discarded)
        verify("centered_truncated_norm", variance_kernel == sum(value ** 2 for value in truncated) / size - mean ** 2)
        for n in (2, 3, 4):
            data = []
            bad_probability = F(0)
            centered_second = F(0)
            for sample in product(range(size), repeat=n):
                probability = F(1, size ** n)
                pg = original_statistic(sample, matrix_g, weights)
                ph = original_statistic(sample, matrix_h, weights)
                pk = original_statistic(sample, matrix_k, weights)
                good = all((sample[i] - sample[j]) % size not in removed for i in range(n) for j in range(i + 1, n))
                verify("nonzero_mean_truncated_statistic", ph == pk - mean / (2 * n))
                if good:
                    verify("good_event_mean_shift", pg == pk + F(n - 1, 2 * n) * mean)
                else:
                    bad_probability += probability
                centered_second += probability * pk ** 2
                data.append((pg, probability))
            union_bound = F(n * (n - 1), 2) * F(len(removed), size)
            verify("close_pair_union_bound", bad_probability <= union_bound)
            verify("truncated_second_moment", centered_second == F(n - 1, 2 * n ** 3) * variance_kernel)
            scales = (F(1, 2), F(1), F(2)) if n == 4 else (F(1, 2), F(1))
            for sigma in scales:
                b = sigma ** 2 / n
                verify("admissible_temperature", 0 < b <= 1)
                shift = sigma * F(n - 1, 2 * n) * abs(discarded)
                scaled_variance = b * F(n - 1, 2 * n ** 2) * variance_kernel
                for gap in (F(1, 10), F(1, 3), F(1), F(3)):
                    z = shift + gap
                    tail = sum(probability for pg, probability in data if abs(sigma * pg) > z)
                    verify("full_probability_bound", tail <= union_bound + scaled_variance / gap ** 2)


cyclic_truncation_battery()

# Integer shell bounds are tested directly, independently of any lattice sum.
for d in range(1, 10):
    for n in range(1, 21):
        exact_shell = (2 * n + 1) ** d - (2 * n - 1) ** d
        verify("max_norm_shell", 2 * d * n ** (d - 1) <= exact_shell <= 2 * d * 3 ** (d - 1) * n ** (d - 1))

# All exponent computations below are rational; no floating-point asymptotics.
for d in range(1, 9):
    for ratio in (F(j, 8) for j in range(1, 8)):
        s = d * ratio
        verify("radial_L2_threshold", (d - 1 - 2 * s > -1) == (2 * s < d))
        if 2 * s > d:
            q = 2 * s - d
            verify("first_heat_cutoff_power", -1 + F(2, d) * (s - F(d, 2)) == 2 * ratio - 2)
            verify("second_heat_cutoff_power", -1 + F(4, d) * (s - F(d, 2)) == 4 * ratio - 3)
            for gamma in (F(-1), F(0), F(1, 8), F(1, 2), F(1), F(3)):
                delta = max(gamma, F(0))
                criterion_power = 4 * ratio - 3 - delta
                if criterion_power < 0:
                    a_power = criterion_power / 2
                    radius_power = -F(2, d) + a_power / q
                    close_power = 2 + d * radius_power
                    mean_power = (1 - delta) / 2 + (d - s) * radius_power
                    variance_power = -1 - delta + (d - 2 * s) * radius_power
                    verify("temperature_radius_identity", close_power == a_power * d / q)
                    verify("temperature_radius_identity", mean_power == a_power * s / q)
                    verify("temperature_radius_identity", variance_power == a_power)
                    verify("temperature_three_limits", max(radius_power, close_power, mean_power, variance_power) < 0)
            verify("strict_three_quarters", (F(2, d) < 1 / q) == (s < F(3 * d, 4)))
        elif 2 * s == d:
            radius_power = -F(3, d)
            verify("borderline_radius", 2 + d * radius_power == -1)
            verify("borderline_radius", F(1, 2) + (d - s) * radius_power == -1)

print(json.dumps({
    "status": "PASS",
    "total_checks": sum(checks.values()),
    "checks_by_category": dict(sorted(checks.items())),
    "arithmetic": "standard-library exact integers and fractions",
    "constructor_code_read_or_run": False,
    "scope": "finite exact support; analytic audit supplies all universal and asymptotic proofs",
}, indent=2, sort_keys=True))
