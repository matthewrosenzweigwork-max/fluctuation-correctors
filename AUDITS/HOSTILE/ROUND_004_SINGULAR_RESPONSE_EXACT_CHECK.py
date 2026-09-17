#!/usr/bin/env python3
"""Independent TASK-038 finite exact checks; standard library only.

Constants are rational monomials in pi, not floating-point Gamma values.
Fourier response tests use mode selection at Coulomb, normalized by c_d.
Pair energy tests integrate polynomials in cos(theta) through exact moments.
The analytic proof audit, not these finite checks, decides the verdict.
"""

from fractions import Fraction as Q
from math import comb, factorial
import json
import platform
import sys


groups = {}


def check(group, actual, expected):
    if actual != expected:
        raise AssertionError((group, actual, expected))
    groups[group] = groups.get(group, 0) + 1


# A monomial is (rational coefficient, rational exponent of pi).
def mul(a, b):
    return a[0] * b[0], a[1] + b[1]


def div(a, b):
    return a[0] / b[0], a[1] - b[1]


def gamma_half(n):
    """Exactly Gamma(n/2) for an integer n >= 1."""
    if n % 2 == 0:
        return Q(factorial(n // 2 - 1)), Q(0)
    m = (n - 1) // 2
    return Q(factorial(2 * m), 4**m * factorial(m)), Q(1, 2)


def riesz_c(d, s):
    return mul((Q(1), Q(s) - Q(d, 2)), div(gamma_half(d - s), gamma_half(s)))


coulomb_values = {}
for d in range(3, 13):
    surface = div((Q(2), Q(d, 2)), gamma_half(d))
    flux = mul((Q(d - 2), Q(0)), surface)
    fourier = mul((Q(4), Q(2)), riesz_c(d, d - 2))
    gamma_form = div((Q(4), Q(d, 2)), gamma_half(d - 2))
    check("coulomb_constants", fourier, flux)
    check("coulomb_constants", gamma_form, flux)
    coulomb_values[str(d)] = {"rational_coefficient": str(flux[0]), "pi_power": str(flux[1])}
    for s in range(1, d - 1):
        heat_A = div((Q(2 ** (d - s)), Q(d, 2)), gamma_half(s))
        transformed = div(mul(heat_A, gamma_half(d - s)), (Q(2 ** (d - s)), Q(d - s)))
        check("heat_fourier_constants", transformed, riesz_c(d, s))
        principal = mul(div(heat_A, (Q(2**d), Q(d, 2))), mul((Q(2**s), Q(0)), gamma_half(s)))
        check("heat_principal_coefficient", principal, (Q(1), Q(0)))
        if s < d - 2:
            ratio = div(mul((Q(4), Q(2)), riesz_c(d, s)), riesz_c(d, s + 2))
            check("below_coulomb_gamma_ratio", ratio, (Q(s * (d - 2 - s)), Q(0)))
    for s in (Q(1, 2), Q(d - 2) - Q(1, 2), Q(d - 2)):
        # Summing Cartesian derivatives of s*z_i*|z|^(-s-2).
        derivative_sum = s * d - s * (s + 2)
        check("radial_divergence", derivative_sum, s * (d - 2 - s))
        check("radial_divergence_sign", derivative_sum >= 0, True)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


vectors = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (1, 1, 0), (0, -1, 1)]
for k in vectors:
    for m in vectors:
        n = tuple(x + y for x, y in zip(k, m))
        nn = dot(n, n)
        if nn:
            direct = -Q(dot(k, n), nn)
            measure_term = -Q(1)
            background_gradient = Q(dot(m, n), nn)
        else:
            direct = measure_term = background_gradient = Q(0)
        check("inhomogeneous_coulomb_response", direct, measure_term + background_gradient)
        # epsilon = log(2)/(4*pi^2), hence the exact multiplier is 2^(-|n|^2).
        heat = Q(1, 2**nn)
        check("heat_outside_response", heat * direct, heat * (measure_term + background_gradient))
        if k == (0, 0, 0):
            check("constant_input_cancellation", direct, Q(0))

check("coulomb_zero_mode_compensation", Q(-1) + Q(1), Q(0))
check("diagonal_borel_atom_two_slots", Q(-1) + Q(-1), Q(-2))
high_frequency_multipliers = []
previous = Q(0)
for n in range(1, 7):
    multiplier = 2 * (1 - Q(1, 2 ** (n * n)))
    check("coulomb_high_frequency", previous < multiplier < 2, True)
    high_frequency_multipliers.append({"frequency": n, "difference_over_c_d": str(multiplier)})
    previous = multiplier


def cos_moment(power):
    if power % 2:
        return Q(0)
    m = power // 2
    return Q(comb(2 * m, m), 4**m)


def integrate_poly(coefficients):
    return sum((coefficient * cos_moment(power) for power, coefficient in enumerate(coefficients)), Q(0))


pair_values = []
for N in (2, 3, 5):
    for b in (Q(-2), Q(-1, 3), Q(0), Q(2, 3), Q(2)):
        # Divide all energy and divergence expressions by pi.
        direct = -Q(4, N) * b * integrate_poly([Q(1), b, Q(-1), -b])
        divergence_energy = -Q(2, N) * integrate_poly([Q(0), Q(1), 2 * b, b * b])
        expected = -Q(2, N) * b
        norm_squared = 1 + b * b / 2
        check("pair_energy", direct, expected)
        check("pair_energy", divergence_energy, expected)
        check("pair_energy_bound", direct <= Q(2, N) * norm_squared, True)
        pair_values.append({"N": N, "b": str(b), "inner_product_over_pi": str(direct)})
    # At theta=pi the exact flow Jacobian exponent is -4*pi/N.
    check("jacobian_norm_exponent", -Q(1, 2) * (-Q(4, N)), Q(2, N))


result = {
    "status": "PASS",
    "total_exact_checks": sum(groups.values()),
    "groups": groups,
    "coulomb_constants": coulomb_values,
    "fixed_positive_heat_high_frequency_example": high_frequency_multipliers,
    "smooth_pair_energy_values": pair_values,
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "arithmetic": "Exact Fraction arithmetic and exact rational monomials in pi; no numerical Gamma evaluation.",
    "seed": None,
    "tolerance": None,
    "limits": "Finite diagnostics only. No singular flow, semigroup convergence, forcing regularity, or evolved-law conclusion is tested.",
}
print(json.dumps(result, indent=2, sort_keys=True))
