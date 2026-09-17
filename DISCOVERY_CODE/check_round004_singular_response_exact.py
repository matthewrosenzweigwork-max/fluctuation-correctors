#!/usr/bin/env python3
"""Exact supporting checks for TASK-034; standard library, no random input.

Fourier calculations use angle coordinates: derivative of mode n is i*n,
the Coulomb divergence multiplier is 1 for n != 0, and the force multiplier
is -i/n. Thus c_d and 2*pi have been divided out explicitly. This checks
finite algebra, not the singular-limit proof or independent audit status.
"""

from __future__ import annotations

import argparse
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

Polynomial = dict[int, Q]


def clean(poly: Polynomial) -> Polynomial:
    return {n: value for n, value in poly.items() if value}


def add(*polys: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for poly in polys:
        for n, value in poly.items():
            out[n] = out.get(n, Q(0)) + value
    return clean(out)


def scale(poly: Polynomial, factor: Q) -> Polynomial:
    return clean({n: factor * value for n, value in poly.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for j, a in left.items():
        for ell, b in right.items():
            n = j + ell
            out[n] = out.get(n, Q(0)) + a * b
    return clean(out)


def first_derivative_without_i(poly: Polynomial) -> Polynomial:
    return clean({n: n * value for n, value in poly.items()})


def zero_mode(poly: Polynomial) -> Q:
    return poly.get(0, Q(0))


def direct_gradient_response(mu: Polynomial, test: Polynomial) -> Polynomial:
    # Integral K(z-x) f'(z) mu(z) dz: Khat(-n) = i/n.
    numerator = multiply(mu, first_derivative_without_i(test))
    return clean({n: -value / n for n, value in numerator.items() if n})


def integrated_response(mu: Polynomial, test: Polynomial) -> Polynomial:
    product = multiply(mu, test)
    divergence_term = {n: -value for n, value in product.items() if n}
    mu_derivative_product = multiply(first_derivative_without_i(mu), test)
    gradient_mu_term = {
        n: value / n for n, value in mu_derivative_product.items() if n
    }
    return add(divergence_term, gradient_mu_term)


def run_checks() -> dict[str, object]:
    counts = {
        "inhomogeneous_response_identities": 0,
        "constant_input_cancellation": 0,
        "missing_gradient_term_detected": 0,
        "homogeneous_pair_fourier_modes": 0,
        "smooth_pair_energy_identities": 0,
        "smooth_pair_energy_bounds": 0,
        "missing_pair_factor_detected": 0,
        "positive_energy_growth_detected": 0,
        "radial_coefficients_and_flux_masses": 0,
        "coulomb_high_frequency_obstruction": 0,
    }
    one: Polynomial = {0: Q(1)}
    cosine: Polynomial = {-1: Q(1, 2), 1: Q(1, 2)}
    mu_cases = [
        one,
        {0: Q(1), -1: Q(1, 4), 1: Q(1, 4)},
        {0: Q(1), -2: Q(1, 6), 2: Q(1, 6)},
    ]
    test_cases = [
        one,
        cosine,
        {0: Q(1), -2: Q(1, 3), 2: Q(1, 3)},
        {-3: Q(2, 5), -1: Q(1, 7), 1: Q(1, 7), 3: Q(2, 5)},
        {2: Q(1)},
    ]
    for mu in mu_cases:
        for test in test_cases:
            assert direct_gradient_response(mu, test) == integrated_response(mu, test)
            counts["inhomogeneous_response_identities"] += 1
        assert direct_gradient_response(mu, one) == {}
        assert integrated_response(mu, one) == {}
        counts["constant_input_cancellation"] += 1
        if mu != one:
            incorrect = {n: -value for n, value in mu.items() if n}
            assert incorrect
            assert incorrect != integrated_response(mu, one)
            counts["missing_gradient_term_detected"] += 1

    for k in range(-3, 4):
        for ell in range(-3, 4):
            first = direct_gradient_response(one, {k: Q(1)}).get(k, Q(0))
            second = direct_gradient_response(one, {ell: Q(1)}).get(ell, Q(0))
            expected = -Q(int(k != 0) + int(ell != 0))
            assert first + second == expected
            counts["homogeneous_pair_fourier_modes"] += 1

    sine_squared: Polynomial = {0: Q(1, 2), -2: Q(-1, 4), 2: Q(-1, 4)}
    for particle_count in (2, 3, 5):
        for amplitude in (Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)):
            test = add(one, scale(cosine, amplitude))
            test_squared = multiply(test, test)
            # Divide G and pair divergence by 2*pi throughout this test.
            generator_test = scale(sine_squared, -2 * amplitude / particle_count)
            direct_energy = zero_mode(multiply(test, generator_test))
            pair_divergence = scale(cosine, Q(2, particle_count))
            integration_by_parts_energy = -Q(1, 2) * zero_mode(
                multiply(pair_divergence, test_squared)
            )
            assert direct_energy == integration_by_parts_energy == -amplitude / particle_count
            assert zero_mode(test_squared) == 1 + amplitude * amplitude / 2
            counts["smooth_pair_energy_identities"] += 1
            assert direct_energy <= zero_mode(test_squared) / particle_count
            counts["smooth_pair_energy_bounds"] += 1
            if amplitude:
                wrong_factor_energy = integration_by_parts_energy / 2
                assert wrong_factor_energy != direct_energy
                counts["missing_pair_factor_detected"] += 1
            if amplitude < 0:
                assert direct_energy > 0
                counts["positive_energy_growth_detected"] += 1

    for dimension in (3, 4, 5, 8):
        for exponent in (Q(dimension - 2, 3), Q(dimension - 2, 2), Q(dimension - 2)):
            flux_power = Q(dimension) - exponent - 2
            divergence_coefficient = exponent * (dimension - (exponent + 2))
            assert divergence_coefficient == exponent * flux_power
            if flux_power:
                assert flux_power > 0
                assert divergence_coefficient / flux_power == exponent
            else:
                assert divergence_coefficient == 0
                assert exponent == dimension - 2
            counts["radial_coefficients_and_flux_masses"] += 1

    # q = exp(-4*pi^2*epsilon) = 1/2 fixes a genuine positive heat time.
    # On symmetric pair modes k=ell=n, the normalized difference is 2(1-q^(n*n)).
    previous = Q(0)
    for frequency in (1, 2, 4, 8):
        attenuation = Q(1, 2) ** (frequency * frequency)
        difference = 2 * (1 - attenuation)
        assert previous < difference < 2
        assert 2 - difference == 2 * attenuation
        previous = difference
        counts["coulomb_high_frequency_obstruction"] += 1

    return {
        "task": "TASK-034",
        "status": "PASS",
        "computation_status": "REPRODUCED",
        "audit_status": "SELF_CHECKED",
        "arithmetic": "fractions.Fraction, exact",
        "random_seed": None,
        "external_dependencies": [],
        "python": platform.python_version(),
        "normalization": "angle derivative i*n; Coulomb c_d=1; pair energy divided by 2*pi",
        "checks": counts,
        "total_checks": sum(counts.values()),
        "limitations": "Finite algebra only; not a singular-limit proof or an independent certificate.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run_checks(), indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(result, encoding="utf-8")
    print(result, end="")


if __name__ == "__main__":
    main()
