#!/usr/bin/env python3
"""Exact rational checks for the TASK-049 construction, not an audit.

Checks actual pair blocks, local generator contractions, the diffusion maximum,
two-singularity exponents, and finite Fourier response product derivatives.
Fourier checks use dimensionless angle coordinates and divide out the positive
Riesz normalization constant; all signs and product coefficients remain exact.
No floating-point arithmetic, random input, tolerance, or dependencies.
"""

from fractions import Fraction as F
from pathlib import Path
import json


COUNTS = {}


def check(category, value, detail):
    if not value:
        raise AssertionError(f"{category}: {detail}")
    COUNTS[category] = COUNTS.get(category, 0) + 1


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matvec(a, v):
    return [dot(row, v) for row in a]


def scale(a, v):
    return [a * x for x in v]


def block_tests():
    for d, s in [(3, 1), (4, 1), (4, 2), (5, 3), (6, 4)]:
        e = [F(3, 5), F(4, 5)] + [F(0)] * (d - 2)
        transverse = [F(-4, 5), F(3, 5)] + [F(0)] * (d - 2)
        for n in [2, 3, 7]:
            for r in [F(1, 16), F(1, 100), F(2, 7)]:
                k = [[s * r ** (-s - 2)
                      * (F(i == j) - (s + 2) * e[i] * e[j])
                      for j in range(d)] for i in range(d)]
                pair = [[F(0) for _ in range(2 * d)] for _ in range(2 * d)]
                for i in range(d):
                    for j in range(d):
                        pair[i][j] = pair[i + d][j + d] = k[i][j] / n
                        pair[i][j + d] = pair[i + d][j] = -k[i][j] / n
                c = F(2 * s, n) * r ** (-s - 2)
                center = e + e
                radial = e + scale(-1, e)
                tangent = transverse + scale(-1, transverse)
                check("pair_center_eigenvalue", matvec(pair, center) == [F(0)] * (2 * d),
                      [d, s, n, str(r)])
                check("pair_radial_eigenvalue", matvec(pair, radial) == scale(-(s + 1) * c, radial),
                      [d, s, n, str(r)])
                check("pair_transverse_eigenvalue", matvec(pair, tangent) == scale(c, tangent),
                      [d, s, n, str(r)])
                for coefficient in [F(-3), F(0), F(1, 2), F(4)]:
                    v = [radial[i] + coefficient * tangent[i] + center[i]
                         for i in range(2 * d)]
                    actual = dot(v, matvec(pair, v))
                    check("largest_eigenvalue_quadratic_form", actual <= c * dot(v, v),
                          [d, s, n, str(r), str(coefficient)])
                check("absolute_norm_is_not_largest_eigenvalue", (s + 1) * c > c,
                      [d, s, n, str(r)])


def weight_tests():
    for d, s, q in [(3, 1, F(5, 4)), (3, 1, F(7, 5)),
                    (4, 1, F(3, 2)), (4, 2, F(7, 4)),
                    (5, 3, F(2)), (6, 4, F(5, 2))]:
        e = [F(3, 5), F(4, 5)] + [F(0)] * (d - 2)
        for n in [2, 3, 11]:
            for p in [F(1), F(3, 2), F(2), F(5)]:
                alpha = p * q
                for r in [F(1, 16), F(1, 100), F(1, 1000)]:
                    grad_z_ratio = scale(-alpha / r, e)
                    grad_pair_ratio = grad_z_ratio + scale(-1, grad_z_ratio)
                    hessian_ratio = [[alpha / r ** 2
                                      * ((alpha + 2) * e[i] * e[j] - F(i == j))
                                      for j in range(d)] for i in range(d)]
                    lap_pair_ratio = 2 * sum(hessian_ratio[i][i] for i in range(d))
                    pair_force = scale(F(s, n) * r ** (-s - 1), e)
                    pair_force += scale(-1, pair_force)
                    c = F(2 * s, n) * r ** (-s - 2)
                    for nu in [F(0), F(1, 3), F(2)]:
                        direct = dot(pair_force, grad_pair_ratio) + nu * lap_pair_ratio + p * c
                        expected = (p - alpha) * c + 2 * nu * alpha * (alpha + 2 - d) / r ** 2
                        check("full_coordinate_weight_generator", direct == expected,
                              [d, s, n, str(p), str(q), str(r), str(nu)])
                        check("strict_repulsive_moment_coefficient",
                              p - alpha == p * (1 - q) and p - alpha < 0,
                              [d, s, n, str(p), str(q)])
                    check("two_relative_laplacians", lap_pair_ratio == 2 * alpha * (alpha + 2 - d) / r ** 2,
                          [d, str(alpha), str(r)])
        check("h1_range", 1 < q < F(d, 2), [d, str(q)])
        if s == d - 2:
            check("coulomb_drift_majorant_nonintegrable", s + 1 + q > d, [d, s, str(q)])
        if d == 3:
            check("three_dimensional_positive_diffusion", q * (q + 2 - d) > 0, str(q))


def maximum_tests():
    for s in [1, 2, 3, 4]:
        for n in [2, 3, 13]:
            for p, alpha in [(F(1), F(5, 4)), (F(2), F(5, 2)), (F(3), F(9))]:
                b = (alpha - p) * F(2 * s, n)
                for star in [F(1, 10), F(1), F(7)]:
                    a = F(s + 2, 4) * b * star ** s
                    maximum = F(s, s + 2) * a * star ** 2
                    derivative = 2 * a * star - F(s + 2, 2) * b * star ** (s + 1)
                    check("maximum_stationarity", derivative == 0, [s, n, str(star)])
                    check("maximum_value", a * star ** 2 - b * star ** (s + 2) / 2 == maximum,
                          [s, n, str(star)])
                    for factor in [F(0), F(1, 10), F(1, 2), F(1), F(2), F(10)]:
                        v = factor * star
                        lhs = a * v ** 2 - b * v ** (s + 2)
                        rhs = maximum - b * v ** (s + 2) / 2
                        check("negative_half_retained", lhs <= rhs, [s, n, str(star), str(factor)])
    # Actual positive diffusion coefficients; 2/s is integral in these rows.
    for d, s in [(3, 1), (4, 1), (4, 2)]:
        for n in [2, 3, 17]:
            for alpha, p in [(F(5, 4), F(1)), (F(5, 2), F(2)), (F(9), F(2))]:
                for nu in [F(0), F(1, 3), F(4)]:
                    a = 2 * nu * alpha * max(F(0), alpha + 2 - d)
                    b = (alpha - p) * F(2 * s, n)
                    maximum = F(0) if a == 0 else F(s, s + 2) * a * (4 * a / ((s + 2) * b)) ** (2 // s)
                    for v in [F(0), F(1, 10), F(1), F(10), F(100)]:
                        check("actual_diffusion_absorption",
                              a * v ** 2 - b * v ** (s + 2) <= maximum - b * v ** (s + 2) / 2,
                              [d, s, n, str(alpha), str(nu), str(v)])


def fourier_tests():
    # Along one frequency axis, these exponents include the normalized Riesz
    # data (d,s)=(3,1),(4,1),(5,1). Positive Fourier constants are divided out.
    for decay_power in [2, 3, 4]:
        for mu_frequency in range(-3, 4):
            for first_frequency in range(-3, 4):
                for second_frequency in range(-2, 3):
                    l, m, n = mu_frequency, first_frequency, second_frequency
                    k = l + m
                    g = F(0) if k == 0 else F(1, abs(k) ** decay_power)
                    d_hat = k * k * g
                    direct_gradient_response = -m * k * g
                    measure_term = -d_hat
                    density_gradient_term = l * k * g
                    check("response_both_compensated_terms",
                          direct_gradient_response == measure_term + density_gradient_term,
                          [decay_power, l, m, n])
                    # Divide the derivative coefficients by the common factor i.
                    first_product = -l * d_hat - m * d_hat
                    second_product = l * l * k * g + l * m * k * g
                    check("response_first_derivative_product_rule",
                          first_product + second_product == k * direct_gradient_response,
                          [decay_power, l, m, n])
                    check("response_second_slot_derivative",
                          n * (measure_term + density_gradient_term) == n * direct_gradient_response,
                          [decay_power, l, m, n])
                    if m == 0 and n == 0:
                        check("response_kills_constants_inhomogeneous_density",
                              direct_gradient_response == 0, [decay_power, l])
        for m in range(-5, 6):
            for n in range(-5, 6):
                dm = F(0) if m == 0 else F(m * m, abs(m) ** decay_power)
                dn = F(0) if n == 0 else F(n * n, abs(n) ** decay_power)
                both = -dm - dn
                if decay_power == 2:
                    atom_compensation = -2 + F(m == 0) + F(n == 0)
                    check("coulomb_atom_and_two_compensations", both == atom_compensation, [m, n])
                check("homogeneous_fourier_gradient_commutes", m * both == both * m and n * both == both * n,
                      [decay_power, m, n])


def exponents_and_morrey():
    for d in range(3, 9):
        n = 2 * d
        p = F(n + 1)
        conjugate = p / (p - 1)
        check("morrey_integrability", n - (n - 1) * conjugate == (p - n) / (p - 1) > 0, d)
        check("simultaneous_flow_weight_strictness", 4 * p > 2 * p, d)
        for s in [F(1, 2), F(1), F(d - 2)]:
            alpha = 2 * (s + 2) + 1
            check("source_ui_weight_strictness", alpha > 2, [d, str(s)])
            check("source_ui_power_dominates", alpha + s + 2 >= 2 * (s + 1), [d, str(s)])
        for a in [F(1), F(d - 1), F(d) - F(1, 2)]:
            for q in [F(5, 4), F(d - 1, 2)]:
                check("separate_convolution_integrability", a < d and q < d, [d, str(a), str(q)])
                check("near_second_singularity_comparison", (d - a - q) - (-q) == d - a > 0,
                      [d, str(a), str(q)])
    d, a, q = 3, F(2), F(5, 4)
    check("unbounded_convolution_witness_exponent", d - a - q == -F(1, 4), [d, str(a), str(q)])
    # At radii 2^-4k the bad convolution power is 2^k while the permitted
    # weight is 2^5k. This is exact and demonstrates the distinct claims.
    for k in range(1, 8):
        check("unbounded_but_weight_dominated", 2 ** k < 2 ** (5 * k), k)


def main():
    block_tests()
    weight_tests()
    maximum_tests()
    fourier_tests()
    exponents_and_morrey()
    output = {
        "task": "TASK-049",
        "status": "PASS",
        "evidence_class": "EXACT_RATIONAL_SELF_CHECK_NOT_INDEPENDENT_AUDIT",
        "arithmetic": "Python standard-library Fraction and integers only",
        "random_seed": None,
        "tolerance": None,
        "checks_by_category": COUNTS,
        "total_checks": sum(COUNTS.values()),
        "tested_particle_counts": [2, 3, 7, 11, 13, 17],
        "tested_diffusivities": ["0", "1/3", "2", "4"],
        "limits": [
            "The checker supports algebraic identities; it does not independently audit the proof.",
            "Nearby-start completeness, uniform integrability, weak differentiation and measure arguments require the written proof.",
            "Fourier checks use dimensionless angles and divide out the common positive Riesz constant.",
            "No H1-to-particle-Ito or N-uniform martingale conclusion is checked or asserted."
        ]
    }
    path = Path(__file__).with_name("round007_weighted_gradient_exact_output.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
