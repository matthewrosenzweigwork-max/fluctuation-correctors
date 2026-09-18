#!/usr/bin/env python3
"""Exact, standard-library diagnostics for TASK063; not an analytic audit."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "AUDITS/ROUND_011_RESCALED_GRADIENT_INPUT_SHA256SUMS.txt"
COUNTS: dict[str, int] = {}


def check(section: str, assertion: bool, detail: str) -> None:
    if not assertion:
        raise AssertionError(f"{section}: {detail}")
    COUNTS[section] = COUNTS.get(section, 0) + 1


def qpow(value: Q, exponent: Q) -> Q:
    """Exact rational power, only for the deliberately perfect-power inputs."""
    value, exponent = Q(value), Q(exponent)
    if exponent < 0:
        return 1 / qpow(value, -exponent)
    numerator = value.numerator ** exponent.numerator
    denominator = value.denominator ** exponent.numerator

    def root_integer(number: int, degree: int) -> int:
        if degree == 1 or number < 2:
            return number
        low, high = 0, 1
        while high**degree < number:
            high *= 2
        while high - low > 1:
            middle = (low + high) // 2
            if middle**degree < number:
                low = middle
            else:
                high = middle
        if high**degree != number:
            raise ValueError("Checker input did not have a rational power")
        return high

    return Q(
        root_integer(numerator, exponent.denominator),
        root_integer(denominator, exponent.denominator),
    )


@dataclass(frozen=True)
class Jet:
    value: Q
    grad: tuple[Q, ...]
    hess: tuple[tuple[Q, ...], ...]

    @classmethod
    def constant(cls, value: Q, n: int) -> Jet:
        return cls(Q(value), (Q(0),) * n, tuple((Q(0),) * n for _ in range(n)))

    @classmethod
    def variable(cls, value: Q, index: int, n: int) -> Jet:
        grad = tuple(Q(j == index) for j in range(n))
        return cls(Q(value), grad, tuple((Q(0),) * n for _ in range(n)))

    def __add__(self, other: Jet | Q | int) -> Jet:
        n = len(self.grad)
        if not isinstance(other, Jet):
            other = Jet.constant(Q(other), n)
        return Jet(
            self.value + other.value,
            tuple(self.grad[i] + other.grad[i] for i in range(n)),
            tuple(tuple(self.hess[i][j] + other.hess[i][j] for j in range(n))
                  for i in range(n)),
        )

    __radd__ = __add__

    def __neg__(self) -> Jet:
        return self * -1

    def __sub__(self, other: Jet | Q | int) -> Jet:
        return self + (-other if isinstance(other, Jet) else -Q(other))

    def __mul__(self, other: Jet | Q | int) -> Jet:
        n = len(self.grad)
        if not isinstance(other, Jet):
            other = Jet.constant(Q(other), n)
        return Jet(
            self.value * other.value,
            tuple(self.grad[i] * other.value + self.value * other.grad[i]
                  for i in range(n)),
            tuple(tuple(
                self.hess[i][j] * other.value
                + self.grad[i] * other.grad[j]
                + self.grad[j] * other.grad[i]
                + self.value * other.hess[i][j]
                for j in range(n)) for i in range(n)),
        )

    __rmul__ = __mul__

    def power(self, exponent: Q) -> Jet:
        n = len(self.grad)
        exponent = Q(exponent)
        value = qpow(self.value, exponent)
        first = exponent * qpow(self.value, exponent - 1)
        second = exponent * (exponent - 1) * qpow(self.value, exponent - 2)
        return Jet(
            value,
            tuple(first * v for v in self.grad),
            tuple(tuple(first * self.hess[i][j]
                        + second * self.grad[i] * self.grad[j]
                        for j in range(n)) for i in range(n)),
        )


def multiply(matrix: list[list[Q]], vector: list[Q]) -> list[Q]:
    return [sum((a * b for a, b in zip(row, vector)), Q(0)) for row in matrix]


def cartesian_checks() -> None:
    for d in range(3, 9):
        exponents = sorted({Q(1, 2), Q(1), Q(d - 2, 2), Q(d - 2)})
        for s in exponents:
            if not (0 < s <= d - 2):
                continue
            p, q = s + 2, s + 1
            n = 2 * d
            x = [Jet.variable(Q(i == 0, 2), i, n) for i in range(d)]
            y = [Jet.variable(-Q(i == 0, 2), d + i, n) for i in range(d)]
            z = [x[i] - y[i] for i in range(d)]
            r2 = sum((v * v for v in z), Jet.constant(0, n))
            force = [s * v * r2.power(-p / 2) for v in z]
            for number in (2, 3, 11, 101):
                rows = [list((v * Q(1, number)).grad) for v in force]
                rows += [list((v * Q(-1, number)).grad) for v in force]
                k0 = Q(2) * s / number
                for axis in range(d):
                    center = [Q(0)] * n
                    center[axis] = center[d + axis] = 1
                    check("cartesian_pair_jacobian",
                          multiply(rows, center) == [0] * n, "center eigenvalue")
                    relative = [Q(0)] * n
                    relative[axis], relative[d + axis] = 1, -1
                    eigen = -(s + 1) * k0 if axis == 0 else k0
                    check("cartesian_pair_jacobian",
                          multiply(rows, relative) == [eigen * a for a in relative],
                          "radial versus transverse eigenvalues")
                for m in (Q(0), Q(1), Q(2), Q(2 * d + 1), Q(4 * d + 2)):
                    for alpha in (m + Q(1, 4), m + q, 2 * m + 3):
                        weight = r2.power(-alpha / 2)
                        lap = sum((weight.hess[i][i] for i in range(n)), Q(0))
                        drift = sum(
                            ((force[i] * Q(1, number)).value
                             * (weight.grad[i] - weight.grad[d + i])
                             for i in range(d)), Q(0))
                        check("cartesian_weight_generator",
                              lap == 2 * alpha * (alpha + 2 - d),
                              "two independent Laplacians")
                        check("cartesian_weight_generator",
                              drift + m * k0 == -(alpha - m) * k0,
                              "weighted Jacobian potential coefficient")
                        check("high_moment_thresholds", alpha > m,
                              "strict absorption threshold")
            # A non-diagonal symmetric Hessian tests both source terms.
            matrix = [[Q(i == j) * (i + 1) + Q(i + j == 1, 3)
                       for j in range(d)] for i in range(d)]
            hz = [sum((matrix[i][j] * z[j] for j in range(d)),
                      Jet.constant(0, n)) for i in range(d)]
            source = sum((force[i] * hz[i] for i in range(d)),
                         Jet.constant(0, n))
            e = [Q(i == 0) for i in range(d)]
            he = [matrix[i][0] for i in range(d)]
            expected = [s * (2 * he[i] - p * matrix[0][0] * e[i])
                        for i in range(d)]
            check("cartesian_source_gradient", source.value == s * matrix[0][0],
                  "one canceled source singularity")
            check("cartesian_source_gradient",
                  list(source.grad) == expected + [-v for v in expected],
                  "derivative of force and derivative of gradient difference")


def optimization_checks() -> None:
    for s in (Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5, 2), Q(3), Q(4)):
        p = s + 2
        for base in (2, 3, 5):
            vstar = Q(base**s.denominator)
            for b in (Q(1, 3), Q(2), Q(17, 5)):
                a = p * b * qpow(vstar, s) / 4
                maximum = s * a * vstar**2 / p
                evaluate = lambda v: a * v**2 - b * qpow(v, p) / 2
                derivative = lambda v: 2 * a * v - p * b * qpow(v, p - 1) / 2
                check("exact_radial_maximum", derivative(vstar) == 0,
                      "stationary point from independent derivative")
                check("exact_radial_maximum", evaluate(vstar) == maximum,
                      "maximum coefficient")
                for multiplier in (Q(1, 4), Q(1), Q(4)):
                    v = vstar * qpow(multiplier, Q(s.denominator))
                    check("exact_radial_maximum", evaluate(v) <= maximum,
                          "radial profile below maximum")
                    check("exact_radial_maximum",
                          (derivative(v) > 0) if v < vstar else
                          ((derivative(v) == 0) if v == vstar else derivative(v) < 0),
                          "derivative sign")
    # a=0 is a distinct endpoint, without evaluating 0 to a negative power.
    for s in (Q(1, 2), Q(1), Q(2)):
        for v in (Q(0), Q(1), Q(4)):
            value = -Q(3, 2) * qpow(v, s + 2)
            check("zero_noise_endpoint", value <= 0, "a=0 maximum is zero")
            check("zero_noise_endpoint", (value == 0) == (v == 0),
                  "zero-noise optimizer is at the origin")


def exponent_checks() -> None:
    for d in range(3, 16):
        exponents = sorted({Q(1, 2), Q(1), Q(d - 2, 2), Q(d - 2)})
        for s in exponents:
            if not (0 < s <= d - 2):
                continue
            p, q = s + 2, s + 1
            check("uniform_scaling", Q(2) / s - (Q(2) / p) * (p / s) == 0,
                  "N exponent in N^(2/s) nu^(p/s)")
            microscopic = s / d - 1 + Q(2) / p
            check("microscopic_exponent",
                  microscopic == s * (s + 2 - d) / (d * p),
                  "exact coupling exponent")
            check("microscopic_exponent", microscopic <= 0, "sign")
            check("microscopic_exponent", (microscopic == 0) == (s == d - 2),
                  "Coulomb endpoint only")
            check("integrability_and_boundary", d - 1 - s >= 1,
                  "deleted-tube value boundary")
            check("integrability_and_boundary", d - q >= 1,
                  "global gradient tail")
            check("integrability_and_boundary", d - s >= 2,
                  "global value tail")
            for b in (Q(3, 2), Q(2), Q(2 * d + 1)):
                check("high_moment_thresholds", b * q > b,
                      "source and terminal derivative UI")
                check("high_moment_thresholds", b * s > 0,
                      "source and terminal value UI")
            for base in (2, 3):
                # N=base^numerator(p), ell=base^-denominator(p).
                number = base**p.numerator
                ell = Q(1, base**p.denominator)
                for chi in (Q(0), Q(1, 3), Q(1), Q(7, 2)):
                    nu = chi * ell**2
                    check("exact_rescaled_potential",
                          nu / ell**2 == chi, "rescaled diffusion")
                    check("exact_rescaled_potential",
                          Q(1, number) * qpow(ell, -p) == 1,
                          "rescaled repulsive drift")
                    for alpha, m in ((s, Q(0)), (q, Q(1)),
                                     (2 * q, Q(2)), (Q(8 * d + 4), Q(4 * d + 2))):
                        a = 2 * alpha * max(alpha + 2 - d, Q(0))
                        b = 2 * s * (alpha - m)
                        original = a * nu * ell**-2 - b * Q(1, number) * qpow(ell, -p)
                        rescaled = a * chi - b
                        check("exact_rescaled_potential", original == rescaled,
                              "full positive diffusion minus repulsion")
    for dimension in (3, 4, 7, 12):
        n, Qmoment = 2 * dimension, Q(2 * dimension + 1)
        conjugate = Qmoment / (Qmoment - 1)
        check("common_start_spatial_exponent",
              n - (n - 1) * conjugate > 0,
              "integrability of segment-averaging kernel")


def fourier_checks() -> None:
    # Each pair mode uses one active spatial coordinate, embedded in d>=3.
    # Derivative multipliers below omit the common factor 2*pi*i.
    modes = {(k, l): Q((k + 4) * (l + 5), 7)
             for k in range(-3, 4) for l in range(-3, 4)}
    for c in (Q(1), Q(2, 3), Q(11)):
        def rx(items):
            return {mode: -c * val + (c * val if mode[0] == 0 else 0)
                    for mode, val in items.items()}

        def ry(items):
            return {mode: -c * val + (c * val if mode[1] == 0 else 0)
                    for mode, val in items.items()}

        xpart, ypart = rx(modes), ry(modes)
        total = {mode: xpart[mode] + ypart[mode] for mode in modes}
        for mode, val in modes.items():
            expected = -c * (int(mode[0] != 0) + int(mode[1] != 0)) * val
            check("coulomb_fourier_responses", total[mode] == expected,
                  "both compensated response slots")
            for axis in (0, 1):
                derivative = {key: key[axis] * value for key, value in modes.items()}
                drx, dry = rx(derivative), ry(derivative)
                check("coulomb_fourier_responses",
                      drx[mode] + dry[mode] == mode[axis] * total[mode],
                      "homogeneous response derivative commutation")
        check("coulomb_mutant_detection",
              -2 * c * modes[(0, 0)] != total[(0, 0)],
              "omitting Haar compensation changes constants")
        check("coulomb_mutant_detection",
              xpart[(1, 1)] != total[(1, 1)],
              "omitting one response changes mixed mode")
        check("coulomb_mutant_detection",
              -total[(1, 1)] != total[(1, 1)],
              "wrong response sign is detected")


def radial_characteristic_checks() -> None:
    # Verify the closed potential through jets in u=r0^p+c*tau, at rational
    # perfect-power u. These are diagnostic Euclidean characteristics only.
    for s in (Q(1, 2), Q(1), Q(2), Q(3), Q(4)):
        p = s + 2
        for number in (2, 3, 17):
            for radius_base in (1, 2):
                r0 = Q(radius_base**p.denominator)
                u0 = qpow(r0, p)
                r = Jet.variable(r0, 0, 2)
                tau = Jet.variable(Q(0), 1, 2)
                c = Q(2) * s * p / number
                potential = Q(number, 4) * ((r.power(p) + c * tau).power(Q(2) / p)
                                            - r * r)
                check("radial_characteristic", potential.value == 0,
                      "terminal-zero value")
                check("radial_characteristic", potential.grad[1] == s * qpow(r0, -s),
                      "time derivative recovers actual radial source")
                check("radial_characteristic", potential.grad[0] == 0,
                      "terminal-zero gradient")
                check("radial_characteristic",
                      potential.hess[0][1] == -s * s * qpow(r0, -s - 1),
                      "source gradient from closed characteristic")
        # At a shrinking start ell*xi, the N exponents of value and gradient.
        check("radial_characteristic_scaling", 1 - Q(2) / p == s / p,
              "inner value growth")
        check("radial_characteristic_scaling", 1 - Q(1) / p == (s + 1) / p,
              "inner gradient growth")
        check("radial_characteristic_scaling", s / p - s / p == 0,
              "weighted value exponent")
        check("radial_characteristic_scaling", (s + 1) / p - (s + 1) / p == 0,
              "weighted gradient exponent")


def factorial_volterra_checks() -> None:
    # Repeated exact integrations in remaining horizon tau. A constant input
    # J and scalar response r isolate the simplex coefficient, sign, and shift.
    for response in (Q(0), Q(-2), Q(3, 5)):
        for source in (Q(0), Q(1), Q(-7, 3)):
            coefficients = [Q(0), source]
            for k in range(12):
                factorial = 1
                for integer in range(1, k + 2):
                    factorial *= integer
                expected = source * response**k / factorial
                check("factorial_volterra", len(coefficients) == k + 2,
                      "k responses produce horizon degree k+1")
                check("factorial_volterra", coefficients[-1] == expected,
                      "ordered-simplex coefficient from exact integration")
                check("factorial_volterra", all(c == 0 for c in coefficients[:-1]),
                      "terminal-zero term and no lower powers")
                coefficients = [Q(0)] + [
                    response * coefficient / (power + 1)
                    for power, coefficient in enumerate(coefficients)
                ]


def verify_inputs() -> list[dict[str, str]]:
    rows = []
    for line in MANIFEST.read_text().splitlines():
        wanted, relative = line.split("  ", 1)
        found = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        check("frozen_input_hashes", found == wanted, relative)
        rows.append({"path": relative, "sha256": found})
    check("frozen_input_hashes", len(rows) == 20, "exact permitted input count")
    return rows


def main() -> None:
    inputs = verify_inputs()
    cartesian_checks()
    optimization_checks()
    exponent_checks()
    fourier_checks()
    radial_characteristic_checks()
    factorial_volterra_checks()
    result = {
        "task": "TASK063",
        "status": "PASS",
        "evidence": "Exact rational diagnostics and input integrity; same-context self-check, not independent analytic certification.",
        "arithmetic": "Python standard-library fractions and exact perfect-power roots; no floating-point tolerance or random seed.",
        "assertions": sum(COUNTS.values()),
        "sections": COUNTS,
        "inputs": inputs,
        "limitations": [
            "The checker does not certify stochastic common-start, uniform-integrability, response-continuity, or limiting-kernel proofs.",
            "The Euclidean response-free radial diagnostic is not an actual-periodic-inverse counterexample.",
            "No evolved-law, singular-tail, H1, or near-diagonal weighted-supremum convergence claim is tested or inferred.",
        ],
    }
    destination = Path(__file__).with_name("round011_rescaled_gradient_exact_results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "assertions": result["assertions"],
                      "sections": COUNTS, "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
