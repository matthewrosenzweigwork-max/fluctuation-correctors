#!/usr/bin/env python3
"""Independent exact finite-law checks for the bounded R3 hostile audit.

Uses only the Python standard library.  These finite computations support,
but do not replace, the analytic proof review.  No other worker code is read.
"""

import itertools
import json
import platform
from fractions import Fraction as F
from pathlib import Path


def average(values, weights):
    return sum((x * w for x, w in zip(values, weights)), F(0))


def main():
    probabilities = [F(1, 5), F(1, 3), F(7, 15)]
    assert sum(probabilities) == 1
    raw = [[F(x) for x in row] for row in
           [[2, -3, 5], [-3, 7, -11], [5, -11, 13]]]
    h = [F(1), F(2), -F(13, 7)]
    assert average(h, probabilities) == 0
    kernels = {
        "constant": [[F(4) for _ in range(3)] for _ in range(3)],
        "first_projection": [[h[i] + h[j] for j in range(3)] for i in range(3)],
        "canonical": [[h[i] * h[j] for j in range(3)] for i in range(3)],
        "mixed": raw,
    }
    configuration_checks = 0
    moment_checks = 0
    for name, kernel in kernels.items():
        projection = [average(row, probabilities) for row in kernel]
        mean = average(projection, probabilities)
        first = [x - mean for x in projection]
        canonical = [[kernel[i][j] - mean - first[i] - first[j]
                      for j in range(3)] for i in range(3)]
        norm = sum(probabilities[i] * probabilities[j] * kernel[i][j] ** 2
                   for i in range(3) for j in range(3))
        first_norm = average([x * x for x in first], probabilities)
        canonical_norm = sum(probabilities[i] * probabilities[j] * canonical[i][j] ** 2
                             for i in range(3) for j in range(3))
        assert norm == mean ** 2 + 2 * first_norm + canonical_norm
        for n in [2, 3, 4, 5]:
            expected = F(0)
            second = F(0)
            for configuration in itertools.product(range(3), repeat=n):
                weight = F(1)
                for x in configuration:
                    weight *= probabilities[x]
                original = (sum(kernel[configuration[i]][configuration[j]]
                                for i in range(n) for j in range(n) if i != j)
                            / F(2 * n * n)
                            - sum(projection[x] for x in configuration) / n
                            + mean / 2)
                decomposed = (-mean / (2 * n)
                              - sum(first[x] for x in configuration) / (n * n)
                              + sum(canonical[configuration[i]][configuration[j]]
                                    for i in range(n) for j in range(i + 1, n))
                              / (n * n))
                assert original == decomposed, (name, n, configuration)
                expected += weight * original
                second += weight * original ** 2
                configuration_checks += 1
            theoretical = (mean ** 2 / (4 * n * n)
                           + first_norm / (n ** 3)
                           + F(n - 1, 2 * n ** 3) * canonical_norm)
            assert expected == -mean / (2 * n)
            assert second == theoretical
            assert second <= F(n - 1, 2 * n ** 3) * norm
            if n == 2 or name == "canonical":
                assert second == F(n - 1, 2 * n ** 3) * norm
            moment_checks += 1

    # A finite translation-invariant Haar model. Pair indicators are pairwise
    # independent, while the three indicators of a triangle are not jointly so.
    group_size = 7
    q = F(3, group_size)

    def near(x, y):
        return (x - y) % group_size in [0, 1, group_size - 1]

    close_pair_checks = 0
    triangle_probability = F(0)
    for n in [3, 4]:
        mean_count = F(0)
        square_count = F(0)
        event_probability = F(0)
        weight = F(1, group_size ** n)
        for configuration in itertools.product(range(group_size), repeat=n):
            count = sum(near(configuration[i], configuration[j])
                        for i in range(n) for j in range(i + 1, n))
            mean_count += weight * count
            square_count += weight * count ** 2
            event_probability += weight * (count > 0)
            if n == 3 and count == 3:
                triangle_probability += weight
        pair_count = n * (n - 1) // 2
        m = pair_count * q
        assert mean_count == m
        assert square_count == m + pair_count * (pair_count - 1) * q ** 2
        assert event_probability >= m / (1 + m)
        close_pair_checks += 1
    assert triangle_probability != q ** 3

    exponent_checks = 0
    for d in range(1, 10):
        for numerator in range(1, 8 * d):
            s = F(numerator, 8)
            p = s + 2
            assert F(2, 1) / p - 1 + s / d == s * (s + 2 - d) / (d * p)
            assert 2 - (d + 4) / p == (2 * s - d) / p
            assert 1 - (d + 4) / p == -(d + 2 - s) / p
            assert F(1, 2) + 2 * s / d - 2 == 2 * s / d - F(3, 2)
            assert -F(2, d) * (d - s) == 2 * s / d - 2
            assert -2 - F(2, d) * (d - 2 * s) == 2 * (2 * s / d - 2)
            exponent_checks += 1

    result = {
        "status": "PASS",
        "arithmetic": "exact fractions; exhaustive finite configurations",
        "python": platform.python_version(),
        "configuration_identity_checks": configuration_checks,
        "iid_moment_and_bound_cases": moment_checks,
        "translation_invariant_pair_count_cases": close_pair_checks,
        "triangle_probability": str(triangle_probability),
        "product_of_triangle_marginals": str(q ** 3),
        "rational_exponent_parameter_cases": exponent_checks,
        "limitations": [
            "No singular or dynamic theorem is inferred from the finite-law tests.",
            "No simulation, floating-point approximation, external dependency, or worker code is used.",
        ],
    }
    output = Path(__file__).resolve().parents[1] / "CERTIFICATES/OUTPUTS/round003_fresh_hostile_exact.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
