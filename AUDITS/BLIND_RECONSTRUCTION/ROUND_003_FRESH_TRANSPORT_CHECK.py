#!/usr/bin/env python3
"""Exact finite-sample and radial checks for the fresh reconstruction."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path


def exact_nth_root(value, degree):
    """Return a rational root only when numerator and denominator are perfect powers."""
    def integer_root(number):
        lower, upper = 0, max(1, number)
        while lower < upper:
            middle = (lower + upper + 1) // 2
            if middle ** degree <= number:
                lower = middle
            else:
                upper = middle - 1
        assert lower ** degree == number
        return lower
    return F(integer_root(value.numerator), integer_root(value.denominator))


class Dual:
    """Value and exact first derivatives with respect to time and radius."""
    def __init__(self, value, dt=0, dr=0):
        self.value, self.dt, self.dr = F(value), F(dt), F(dr)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Dual) else Dual(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Dual(self.value + other.value, self.dt + other.dt, self.dr + other.dr)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.dt, -self.dr)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __mul__(self, other):
        other = self.coerce(other)
        return Dual(
            self.value * other.value,
            self.dt * other.value + self.value * other.dt,
            self.dr * other.value + self.value * other.dr,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent):
        exponent = F(exponent)
        value = exact_nth_root(self.value, exponent.denominator) ** exponent.numerator
        coefficient = exponent * value / self.value
        return Dual(value, coefficient * self.dt, coefficient * self.dr)


weights = [F(1, 2), F(1, 3), F(1, 6)]
values = [F(-1), F(0), F(2)]
mean_value = sum(w * x for w, x in zip(weights, values))
centered = [x - mean_value for x in values]
kernels = {
    "constant": [[F(7, 3) for _ in values] for _ in values],
    "additive": [[x + y for y in values] for x in values],
    "canonical": [[x * y for y in centered] for x in centered],
    "mixed": [
        [F(1), F(-2, 3), F(5, 7)],
        [F(-2, 3), F(3, 2), F(-4)],
        [F(5, 7), F(-4), F(2, 5)],
    ],
}


def pair_norm(matrix):
    return sum(
        weights[i] * weights[j] * matrix[i][j] ** 2
        for i in range(3) for j in range(3)
    )


iid_cases = []
for name, kernel in kernels.items():
    marginal = [
        sum(weights[j] * kernel[i][j] for j in range(3))
        for i in range(3)
    ]
    m = sum(weights[i] * marginal[i] for i in range(3))
    h = [entry - m for entry in marginal]
    canonical = [
        [kernel[i][j] - m - h[i] - h[j] for j in range(3)]
        for i in range(3)
    ]
    hnorm = sum(weights[i] * h[i] ** 2 for i in range(3))
    qnorm = pair_norm(canonical)
    knorm = pair_norm(kernel)
    assert knorm == m * m + 2 * hnorm + qnorm
    for n in (2, 3, 4):
        observed_mean = F(0)
        observed_second = F(0)
        for sample in itertools.product(range(3), repeat=n):
            probability = F(1)
            for index in sample:
                probability *= weights[index]
            ordered = sum(
                kernel[sample[i]][sample[j]]
                for i in range(n) for j in range(n) if i != j
            )
            p = (
                ordered / (2 * n * n)
                - sum(marginal[index] for index in sample) / n
                + m / 2
            )
            qordered = sum(
                canonical[sample[i]][sample[j]]
                for i in range(n) for j in range(n) if i != j
            )
            decomposition = (
                -m / (2 * n)
                - sum(h[index] for index in sample) / (n * n)
                + qordered / (2 * n * n)
            )
            assert p == decomposition
            observed_mean += probability * p
            observed_second += probability * p * p
        expected_second = (
            m * m / (4 * n * n)
            + hnorm / (n ** 3)
            + F(n - 1, 2 * n ** 3) * qnorm
        )
        upper = F(n - 1, 2 * n ** 3) * knorm
        gap = F(n - 2, 4 * n ** 3) * m * m + F(n - 2, n ** 3) * hnorm
        assert observed_mean == -m / (2 * n)
        assert observed_second == expected_second
        assert upper - observed_second == gap
        assert gap >= 0
        if n == 2 or name == "canonical":
            assert gap == 0
        iid_cases.append({
            "kernel": name,
            "N": n,
            "mean": str(observed_mean),
            "second_moment": str(observed_second),
            "upper_bound_gap": str(gap),
        })

transport_cases = []
for s, n, (r, terminal_radius), a in itertools.product(
    (1, 2, 3), (2, 3, 7), ((1, 2), (2, 3)), (F(-2), F(0), F(3, 5))
):
    p = s + 2
    c = 2 * s * p
    tau = F(n * (terminal_radius ** p - r ** p), c)
    assert r ** p + F(c, n) * tau == terminal_radius ** p
    radial_variable = Dual(r, dr=1)
    backward_time_variable = Dual(tau, dt=-1)
    candidate = F(n, 4) * a * (
        (radial_variable ** p + F(c, n) * backward_time_variable) ** F(2, p)
        - radial_variable ** 2
    )
    phi = candidate.value
    speed = F(2 * s, n * r ** (s + 1))
    residual = candidate.dt + speed * candidate.dr + s * a / r ** s
    assert phi == F(n, 4) * a * (terminal_radius ** 2 - r ** 2)
    assert residual == 0
    transport_cases.append({
        "s": s,
        "admissible_dimension": s + 1,
        "N": n,
        "initial_radius": r,
        "terminal_radius": terminal_radius,
        "angular_coefficient": str(a),
        "tau": str(tau),
        "phi": str(phi),
        "PDE_residual": str(residual),
    })

output = {
    "status": "PASS",
    "arithmetic": "exact rational arithmetic; iid laws fully enumerated",
    "iid_moment_case_count": len(iid_cases),
    "transport_substitution_case_count": len(transport_cases),
    "iid_moment_cases": iid_cases,
    "transport_substitutions": transport_cases,
}
destination = Path(__file__).with_name("ROUND_003_FRESH_TRANSPORT_CHECK_OUTPUT.json")
destination.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps({
    key: output[key]
    for key in (
        "status", "arithmetic", "iid_moment_case_count",
        "transport_substitution_case_count"
    )
}, indent=2))
