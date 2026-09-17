"""Independent finite-space iid checks; exact rational arithmetic only."""

from fractions import Fraction as F
from itertools import product
from math import prod
import json


weights = [F(1, 2), F(1, 3), F(1, 6)]
centered = [F(-1), F(0), F(3)]
kernels = {
    "constant": [[F(3, 2) for _ in weights] for _ in weights],
    "first_projection": [[a + b for b in centered] for a in centered],
    "canonical_rank_one": [[a * b for b in centered] for a in centered],
    "mixed": [[F(x) for x in row] for row in [[2, -3, 1], [-3, 4, 2], [1, 2, -5]]],
}
counts = {"configuration_identities": 0, "moment_and_norm_checks": 0, "temperature_factors": 0}
rows = []
for name, phi in kernels.items():
    marginal = [sum(weights[j] * phi[i][j] for j in range(3)) for i in range(3)]
    mean = sum(weights[i] * marginal[i] for i in range(3))
    first = [x - mean for x in marginal]
    second = [[phi[i][j] - mean - first[i] - first[j] for j in range(3)] for i in range(3)]
    first_norm = sum(weights[i] * first[i] ** 2 for i in range(3))
    second_norm = sum(weights[i] * weights[j] * second[i][j] ** 2 for i in range(3) for j in range(3))
    full_norm = sum(weights[i] * weights[j] * phi[i][j] ** 2 for i in range(3) for j in range(3))
    assert full_norm == mean ** 2 + 2 * first_norm + second_norm
    counts["moment_and_norm_checks"] += 1
    for n in [2, 3, 4, 6]:
        expected = F(0)
        square = F(0)
        for states in product(range(3), repeat=n):
            probability = prod(weights[i] for i in states)
            deleted_ordered = sum(phi[states[i]][states[j]] for i in range(n) for j in range(n) if i != j)
            statistic = deleted_ordered / (2 * n * n) - sum(marginal[i] for i in states) / n + mean / 2
            reconstructed = -mean / (2 * n) - sum(first[i] for i in states) / (n * n)
            reconstructed += sum(second[states[i]][states[j]] for i in range(n) for j in range(i + 1, n)) / (n * n)
            assert statistic == reconstructed, (name, n, states)
            counts["configuration_identities"] += 1
            expected += probability * statistic
            square += probability * statistic ** 2
        predicted = mean ** 2 / (4 * n * n) + first_norm / n ** 3 + F(n - 1, 2 * n ** 3) * second_norm
        assert expected == -mean / (2 * n)
        assert square == predicted
        assert square <= F(n - 1, 2 * n ** 3) * full_norm
        counts["moment_and_norm_checks"] += 3
        if name == "canonical_rank_one" or n == 2:
            assert square == F(n - 1, 2 * n ** 3) * full_norm
            counts["moment_and_norm_checks"] += 1
        rows.append({"kernel": name, "N": n, "mean": str(expected), "second_moment": str(square)})

for n in [2, 3]:
    for beta in [F(1, 9), F(1, 2), F(1), F(3), F(10)]:
        minimum = min(beta, F(1))
        sigma_squared = n * minimum
        raw_canonical_coefficient = F(n - 1, 2 * n ** 3)
        assert sigma_squared * raw_canonical_coefficient == minimum * F(n - 1, 2 * n ** 2)
        counts["temperature_factors"] += 1

print(json.dumps({"status": "PASS", "arithmetic": "exact rational", "counts": counts, "total_checks": sum(counts.values()), "cases": rows}, indent=2))
