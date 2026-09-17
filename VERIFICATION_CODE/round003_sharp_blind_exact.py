"""Exact finite cyclic-Haar diagnostics for pair counts and centered sums.

These are algebraic diagnostics, not a discretization proof of the Riesz theorem.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json


checks = 0
configurations = 0
rows = []
for modulus in [5, 7]:
    q = F(3, modulus)
    for n in [2, 3, 4]:
        pairs = list(combinations(range(n), 2))
        pair_count = len(pairs)
        distribution = Counter()
        triangle_count = 0
        for x in product(range(modulus), repeat=n):
            events = []
            for i, j in pairs:
                distance = min((x[i] - x[j]) % modulus, (x[j] - x[i]) % modulus)
                events.append(distance <= 1)
            distribution[sum(events)] += 1
            if n == 3 and all(events):
                triangle_count += 1
            configurations += 1
        denominator = modulus ** n
        mean = sum(F(k * count, denominator) for k, count in distribution.items())
        second = sum(F(k * k * count, denominator) for k, count in distribution.items())
        probability = F(denominator - distribution[0], denominator)
        lam = pair_count * q
        assert mean == lam
        assert second == pair_count * q + pair_count * (pair_count - 1) * q * q
        assert probability >= mean * mean / second
        centered_pair_second = sum(F(count, denominator) * ((F(k) - lam) / n ** 2) ** 2 for k, count in distribution.items())
        assert centered_pair_second == F(n - 1, 2 * n ** 3) * q * (1 - q)
        checks += 4
        row = {"cyclic_size": modulus, "N": n, "pair_count": pair_count, "event_probability": str(q), "mean_count": str(mean), "second_count_moment": str(second), "probability_nonzero": str(probability), "centered_pair_second_moment": str(centered_pair_second)}
        if n == 3:
            triangle_probability = F(triangle_count, denominator)
            assert triangle_probability == F(7, modulus ** 2)
            assert triangle_probability != q ** 3
            checks += 2
            row["joint_triangle_probability"] = str(triangle_probability)
            row["incorrect_joint_independence_value"] = str(q ** 3)
        rows.append(row)

print(json.dumps({"status": "PASS", "arithmetic": "exact rational", "checks": checks, "configurations": configurations, "cases": rows}, indent=2))
