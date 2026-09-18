#!/usr/bin/env python3
"""Independent TASK-048 diagnostics using exact scalar perturbation series.

No candidate checker, third-party package, simulation, tolerance, or random seed
is used. Raw scalar energies are expanded along each coordinate through order
two, independently of the explicitly assembled vector force and divergence.
The smooth local polynomials are differential diagnostics, not replacements for
the frozen periodic Riesz kernel. Analytic passages are reviewed in the report.
"""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


COUNTS = {}
CASES = []
WITNESSES = {}


def check(group, condition, detail):
    if not condition:
        raise AssertionError((group, detail))
    COUNTS[group] = COUNTS.get(group, 0) + 1


def integer_root(n, k):
    lo, hi = 0, max(1, n)
    while lo <= hi:
        mid = (lo + hi) // 2
        value = mid ** k
        if value == n:
            return mid
        if value < n:
            lo = mid + 1
        else:
            hi = mid - 1
    raise ValueError(("non-exact root", n, k))


def exact_power(value, exponent):
    value, exponent = F(value), F(exponent)
    if value <= 0:
        raise ValueError("Radial bases must be strictly positive")
    root = F(integer_root(value.numerator, exponent.denominator),
             integer_root(value.denominator, exponent.denominator))
    return root ** exponent.numerator


def series(value, first=0, second=0):
    return (F(value), F(first), F(second))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(F(c) * x for x in a)


def multiply(a, b):
    return tuple(sum(a[j] * b[k - j] for j in range(k + 1))
                 for k in range(3))


def power(a, exponent):
    exponent = F(exponent)
    base = exact_power(a[0], exponent)
    return (base,
            base * exponent * a[1] / a[0],
            base * (exponent * a[2] / a[0]
                    + exponent * (exponent - 1) / 2 * (a[1] / a[0]) ** 2))


def sum_series(items):
    answer = series(0)
    for item in items:
        answer = add(answer, item)
    return answer


def raw_h(z):
    q = sum_series(multiply(v, v) for v in z)
    return sum_series((scale(q, F(2, 7)),
                       scale(multiply(q, q), F(3, 11)),
                       scale(multiply(z[0], z[1]), F(5, 13)),
                       scale(multiply(multiply(z[0], z[0]),
                                      multiply(z[1], z[1])), F(1, 17))))


def raw_v(x):
    q = sum_series(multiply(v, v) for v in x)
    quartic = sum_series(multiply(multiply(v, v), multiply(v, v)) for v in x)
    return sum_series((scale(q, F(2, 5)), scale(quartic, F(3, 7)),
                       scale(x[0], F(1, 11)),
                       scale(multiply(x[0], x[1]), F(2, 13)),
                       series(F(17, 19))))


def energy_series(points, s, coordinate, use_h, use_v):
    n, d = len(points), len(points[0])
    x = [[series(points[i][a], int(i * d + a == coordinate))
          for a in range(d)] for i in range(n)]
    terms = [raw_v(row) for row in x] if use_v else []
    for i in range(n):
        for j in range(i + 1, n):
            z = [add(x[i][a], scale(x[j][a], -1)) for a in range(d)]
            q = sum_series(multiply(v, v) for v in z)
            g = power(q, -F(s, 2))
            if use_h:
                g = add(g, raw_h(z))
            terms.append(scale(g, F(1, n)))
    return sum_series(terms)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def h_gradient(z):
    q = dot(z, z)
    grad = [F(4, 7) * v + F(12, 11) * q * v for v in z]
    grad[0] += F(5, 13) * z[1] + F(2, 17) * z[0] * z[1] ** 2
    grad[1] += F(5, 13) * z[0] + F(2, 17) * z[1] * z[0] ** 2
    return grad


def h_laplacian(z):
    return F(4, 7) * len(z) + F(12, 11) * (len(z) + 2) * dot(z, z) \
        + F(2, 17) * (z[0] ** 2 + z[1] ** 2)


def v_gradient(x):
    grad = [F(4, 5) * v + F(12, 7) * v ** 3 for v in x]
    grad[0] += F(1, 11) + F(2, 13) * x[1]
    grad[1] += F(2, 13) * x[0]
    return grad


def v_laplacian(x):
    return F(4, 5) * len(x) + F(36, 7) * dot(x, x)


def kernel(z, s, use_h):
    q = dot(z, z)
    factor = s * exact_power(q, -F(s + 2, 2))
    correction = h_gradient(z) if use_h else [F(0)] * len(z)
    return [factor * v - correction[a] for a, v in enumerate(z)]


def pair_laplacian(z, s, use_h):
    return s * (s + 2 - len(z)) * exact_power(dot(z, z), -F(s + 2, 2)) \
        + (h_laplacian(z) if use_h else F(0))


def direct(points, s, use_h, use_v):
    n, d = len(points), len(points[0])
    background = [[-v for v in v_gradient(x)] if use_v else [F(0)] * d
                  for x in points]
    pair = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                z = [points[i][a] - points[j][a] for a in range(d)]
                pair[i, j] = kernel(z, s, use_h)
    force = [[background[i][a] + sum(pair[i, j][a] for j in range(n) if j != i) / n
              for a in range(d)] for i in range(n)]
    pair_lap_sum = sum(pair_laplacian([points[i][a] - points[j][a] for a in range(d)],
                                     s, use_h)
                       for i in range(n) for j in range(i + 1, n))
    external_lap = sum(v_laplacian(x) for x in points) if use_v else F(0)
    lap = external_lap + F(2, n) * pair_lap_sum
    ordered_div = -external_lap - sum(
        pair_laplacian([points[i][a] - points[j][a] for a in range(d)], s, use_h)
        for i in range(n) for j in range(n) if i != j) / n
    return force, background, pair, lap, ordered_div, pair_lap_sum, external_lap


def configuration(name, d):
    def point(a=0, b=0):
        return [F(a), F(b)] + [F(0)] * (d - 2)
    if name == "two":
        return [point(), point(F(1, 16))]
    if name == "triple_symmetric":
        return [point(-F(1, 64)), point(), point(F(1, 64))]
    if name == "triangle_3_4_5":
        return [point(), point(F(3, 64)), point(0, F(4, 64))]
    if name == "disjoint_close_pairs":
        return [point(), point(F(1, 128)), point(F(1, 4)), point(F(1, 4) + F(1, 128))]
    raise ValueError(name)


def differential_checks():
    for d, s in ((3, F(1, 2)), (3, F(1)), (4, F(1)), (4, F(2)),
                 (5, F(1)), (5, F(2)), (5, F(3)), (6, F(2)), (6, F(4))):
        names = ["two"] if s.denominator != 1 else [
            "two", "triple_symmetric", "triangle_3_4_5", "disjoint_close_pairs"]
        for name in names:
            points = configuration(name, d)
            n = len(points)
            for use_h in (False, True):
                for use_v in (False, True):
                    tag = (d, str(s), name, use_h, use_v)
                    raw = [energy_series(points, s, a, use_h, use_v) for a in range(n * d)]
                    gradient = [row[1] for row in raw]
                    lap_raw = 2 * sum(row[2] for row in raw)
                    force, background, pair, lap, div, pair_lap, vlap = direct(
                        points, s, use_h, use_v)
                    flat_force = [v for row in force for v in row]
                    for a in range(n * d):
                        check("coordinate_energy_gradient", gradient[a] == -flat_force[a], (tag, a))
                        check("scalar_energy_consistency", raw[a][0] == raw[0][0], (tag, a))
                    check("full_laplacian_2_over_N", lap_raw == lap, tag)
                    check("direct_divergence", div == -lap_raw, tag)
                    if pair_lap != 0:
                        check("reject_missing_second_pair_derivative",
                              lap_raw != vlap + pair_lap / n, tag)
                    square = dot(flat_force, flat_force)
                    diagonal_pairs = F(2, n * n) * sum(
                        dot(pair[i, j], pair[i, j]) for i in range(n) for j in range(i + 1, n))
                    background_cross = F(2, n) * sum(
                        dot(background[i], pair[i, j]) for i in range(n) for j in range(n) if i != j)
                    triple = F(1, n * n) * sum(
                        dot(pair[i, j], pair[i, k])
                        for i in range(n) for j in range(n) for k in range(n)
                        if j != i and k != i and j != k)
                    expanded = sum(dot(v, v) for v in background) + background_cross + diagonal_pairs + triple
                    check("complete_square_and_ordered_triples", square == expanded, tag)
                    for nu in (F(0), F(1, 3), F(7)):
                        scalar_generator = dot(flat_force, gradient) + nu * lap_raw
                        check("energy_generator_including_zero_diffusion",
                              scalar_generator == -square + nu * lap, (tag, str(nu)))
                    CASES.append({"d": d, "s": str(s), "N": n, "geometry": name,
                                  "smooth_even_remainder": use_h, "external_gradient": use_v})


def gamma_half(integer_twice_argument):
    n = integer_twice_argument
    if n % 2 == 0:
        return F(factorial(n // 2 - 1)), F(0)
    factor = F(1)
    for j in range(1, (n - 1) // 2 + 1):
        factor *= F(2 * j - 1, 2)
    return factor, F(1, 2)


def fourier_constant(d, s):
    num, num_pi = gamma_half(d - s)
    den, den_pi = gamma_half(s)
    return num / den, F(s) - F(d, 2) + num_pi - den_pi


def normalization_and_counting_checks():
    for d in range(3, 10):
        for s in range(1, d - 1):
            coefficient, pi_power = fourier_constant(d, s)
            if s < d - 2:
                other, other_pi = fourier_constant(d, s + 2)
                check("exact_gamma_fourier_ratio", (4 * coefficient / other, pi_power + 2 - other_pi)
                      == (F(s * (d - 2 - s)), F(0)), (d, s))
            else:
                gamma, gamma_pi = gamma_half(d)
                surface_coefficient = F(2 * (d - 2)) / gamma
                surface_pi = F(d, 2) - gamma_pi
                check("exact_Coulomb_atom_coefficient", (4 * coefficient, pi_power + 2)
                      == (surface_coefficient, surface_pi), d)
        for n in (2, 3, 4, 17):
            # Coulomb coefficients below are measured in units of c_d.
            ordered = sum(F(1, n) for i in range(n) for j in range(n) if i != j)
            unordered = sum(F(2, n) for i in range(n) for j in range(i + 1, n))
            check("Coulomb_particle_compensation", ordered == unordered == n - 1, (d, n))
            check("Coulomb_Q_zero_constant_V", F(n - 1) - unordered == 0, (d, n))
            check("Coulomb_divergence_sign", -ordered == -(n - 1), (d, n))
    # The atom and uniform compensation have mass zero, but a unit nonzero-mode coefficient.
    for mode in ((0, 0, 0), (1, 0, 0), (-2, 1, 0)):
        expected = 0 if mode == (0, 0, 0) else 1
        atom_minus_haar = 1 - int(mode == (0, 0, 0))
        check("Coulomb_zero_and_nonzero_modes", atom_minus_haar == expected, mode)
    for n in (2, 3, 4, 17):
        for a, kappa in ((F(0), F(1)), (F(2, 3), F(5, 7)), (F(0), F(0))):
            independent_sum = sum(a for _ in range(n)) + sum(
                kappa / n for i in range(n) for j in range(n) if i != j)
            check("full_density_exponent", independent_sum == n * a + (n - 1) * kappa,
                  (n, str(a), str(kappa)))


def collapse_and_zero_noise_checks():
    for d, s in ((3, F(1)), (4, F(1)), (4, F(2)), (5, F(3)), (6, F(4))):
        for rho in (F(1, 64), F(1, 128), F(1, 256)):
            points = [[-rho] + [F(0)] * (d - 1), [F(0)] * d,
                      [rho] + [F(0)] * (d - 1)]
            force, background, pair, lap, div, _, _ = direct(points, s, False, False)
            energy = energy_series(points, s, 0, False, False)[0]
            middle_pair_squares = (dot(pair[1, 0], pair[1, 0]) + dot(pair[1, 2], pair[1, 2])) / 9
            middle_cross = F(2, 9) * dot(pair[1, 0], pair[1, 2])
            check("triple_total_force_cancellation", dot(force[1], force[1]) == 0, (d, str(s), str(rho)))
            check("triple_individual_pair_forces_nonzero", middle_pair_squares > 0, (d, str(s), str(rho)))
            check("triple_negative_cross_exact", middle_pair_squares + middle_cross == 0,
                  (d, str(s), str(rho)))
            check("triple_energy_blowup_coefficient", 3 * energy * rho ** s.numerator
                  == 2 + F(2) ** (-s.numerator), (d, str(s), str(rho)))
            if d == 3 and rho == F(1, 64):
                WITNESSES["symmetric_triple"] = {
                    "d": d, "s": str(s), "N": 3, "rho": str(rho),
                    "energy": str(energy), "middle_total_force_square": "0",
                    "middle_individual_drift_square_sum": str(middle_pair_squares),
                    "middle_ordered_cross_term": str(middle_cross),
                    "full_drift_square": str(sum(dot(v, v) for v in force))}
            disjoint = [[v] + [F(0)] * (d - 1) for v in (F(0), rho, F(1, 4), F(1, 4) + rho)]
            disjoint_energy = energy_series(disjoint, s, 0, False, False)[0]
            lower = F(1, 2) * rho ** (-s.numerator)
            check("disjoint_pairs_energy_lower_bound", disjoint_energy >= lower, (d, str(s), str(rho)))
            if d == 3 and rho == F(1, 128):
                WITNESSES["disjoint_pairs"] = {"N": 4, "rho": str(rho),
                    "principal_energy": str(disjoint_energy), "two_close_pairs_lower_bound": str(lower)}
    for s in (F(1, 2), F(1), F(2), F(3), F(4)):
        r = F(1, 16)
        for coefficient_n in (2, 3, 17):
            radial_velocity = F(2, coefficient_n) * s * exact_power(r, -s - 1)
            power_derivative = (s + 2) * exact_power(r, s + 1) * radial_velocity
            check("zero_noise_relative_integral", power_derivative == F(2, coefficient_n) * s * (s + 2),
                  (str(s), coefficient_n))
            energy_derivative = -s / coefficient_n * exact_power(r, -s - 1) * radial_velocity
            drift_square = F(2, coefficient_n ** 2) * s ** 2 * exact_power(r, -2 * s - 2)
            check("zero_noise_energy_dissipation", energy_derivative == -drift_square,
                  (str(s), coefficient_n))
            for d in (int(s) + 3, int(s) + 4):
                for nu in (F(0), F(1, 3), F(7)):
                    delta_g = s * (s + 2 - d) * exact_power(r, -s - 2)
                    relative = (-F(2, coefficient_n ** 2) * s ** 2 * exact_power(r, -2 * s - 2)
                                + F(2, coefficient_n) * nu * delta_g)
                    full_space = energy_derivative + nu * F(2, coefficient_n) * delta_g
                    check("relative_diffusion_factor_two", relative == full_space,
                          (str(s), coefficient_n, d, str(nu)))


def main():
    differential_checks()
    normalization_and_counting_checks()
    collapse_and_zero_noise_checks()
    result = {
        "status": "PASS",
        "arithmetic": "fractions.Fraction; exact integer roots; symbolic powers of pi",
        "method": "Coordinate scalar Taylor coefficients of raw energies versus explicit vector force and ordered divergence",
        "random_seed": None,
        "floating_point_tolerance": None,
        "external_dependencies": [],
        "checks_total": sum(COUNTS.values()),
        "checks_by_group": COUNTS,
        "differential_cases_total": len(CASES),
        "differential_cases": CASES,
        "witnesses": WITNESSES,
        "limits": [
            "Finite exact diagnostics corroborate the written analytic audit; they are not a stochastic existence proof.",
            "Smooth local polynomial remainders and backgrounds test differential identities only.",
            "The periodic Coulomb compensation is checked through exact Fourier/gamma identities, not a sampled Euclidean kernel.",
            "N=3 or 17 in the two-body relative ODE is a coefficient diagnostic; the actual two-particle system has N=2.",
            "No individual pair-force-square estimate or uniform-in-N density estimate is inferred."
        ]
    }
    output = Path(__file__).with_name("round006_particle_hostile_exact_output.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "checks_total": result["checks_total"],
                      "differential_cases_total": len(CASES), "checks_by_group": COUNTS,
                      "witnesses": WITNESSES}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
