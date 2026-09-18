#!/usr/bin/env python3
"""TASK-076 independent exact checks. Python standard library only.

Polynomials use e^(2 pi i x) with rational Laurent coefficients. delta_j
multiplies a coefficient by its frequency, so physical differentiation is
2 pi i delta_j. For an odd rational Laurent force F, the physical real force
is i F. Every force-drift expression below is therefore the physical one
divided by -2 pi. The physical diffusion expression is -4 pi^2 times the
delta-Laplacian checked separately. Haar integration is zero-mode extraction.

No prior checker, simulation, floating tolerance, singular limit, or numerical
inverse is used. A polynomial identity is tested on complete coefficients,
not at selected configurations. Finite probes do not prove analytic limits.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import argparse
import hashlib
import json
import platform


class Poly:
    def __init__(self, n, terms=None):
        self.n = n
        self.c = {tuple(k): F(v) for k, v in (terms or {}).items() if v}
        assert all(len(k) == n for k in self.c)

    def __add__(self, other):
        assert self.n == other.n
        out = dict(self.c)
        for k, v in other.c.items():
            out[k] = out.get(k, F(0)) + v
        return Poly(self.n, out)

    def __sub__(self, other):
        return self + other.scale(-1)

    def scale(self, a):
        return Poly(self.n, {k: F(a) * v for k, v in self.c.items()})

    def __mul__(self, other):
        assert self.n == other.n
        out = {}
        for k, a in self.c.items():
            for l, b in other.c.items():
                m = tuple(x + y for x, y in zip(k, l))
                out[m] = out.get(m, F(0)) + a * b
        return Poly(self.n, out)

    def diff(self, j):
        return Poly(self.n, {k: k[j] * v for k, v in self.c.items()})

    def embed(self, slots, dimension):
        assert len(slots) == self.n
        out = {}
        for k, a in self.c.items():
            m = [0] * dimension
            for axis, j in enumerate(slots):
                m[j] += k[axis]
            key = tuple(m)
            out[key] = out.get(key, F(0)) + a
        return Poly(dimension, out)

    def integrate_except(self, slots):
        out = {}
        omitted = set(range(self.n)) - set(slots)
        for k, a in self.c.items():
            if any(k[j] for j in omitted):
                continue
            key = tuple(k[j] for j in slots)
            out[key] = out.get(key, F(0)) + a
        return Poly(len(slots), out)

    def __eq__(self, other):
        return self.n == other.n and self.c == other.c


def total(items, dimension):
    out = Poly(dimension)
    for item in items:
        out = out + item
    return out


def cosine(*frequency):
    k = tuple(frequency)
    if not any(k):
        return Poly(len(k), {k: 1})
    return Poly(len(k), {k: F(1, 2), tuple(-x for x in k): F(1, 2)})


def sym(poly):
    return total((poly.embed(p, poly.n) for p in permutations(range(poly.n))),
                 poly.n).scale(F(1, 6) if poly.n == 3 else F(1, 2))


def relative(force, dimension, a, b):
    out = {}
    for (k,), v in force.c.items():
        m = [0] * dimension
        m[a] += k
        m[b] -= k
        key = tuple(m)
        out[key] = out.get(key, F(0)) + v
    return Poly(dimension, out)


def statistic(poly, number):
    """Literal subset + injective-label definition; no overlap formulas."""
    result = Poly(number)
    for size in range(poly.n + 1):
        factor = F((-1) ** (poly.n - size), number ** size)
        for subset in combinations(range(poly.n), size):
            contracted = poly.integrate_except(subset)
            for labels in permutations(range(number), size):
                result = result + contracted.embed(labels, number).scale(factor)
    return result


def pair_stat(poly, number):
    return statistic(poly, number).scale(F(1, 2))


def deleted_pair(poly, number, falling=False):
    denominator = number * (number - 1) if falling else number ** 2
    return total((poly.embed(labels, number)
                  for labels in permutations(range(number), 2)), number).scale(F(1, denominator))


def response_slots(phi, force):
    """Use minus-divergence convolution, independently of C contractions."""
    derivative_force = force.diff(0)
    rx = (relative(derivative_force, 3, 2, 0)
          * phi.embed((2, 1), 3)).integrate_except((0, 1)).scale(-1)
    ry = (relative(derivative_force, 3, 2, 1)
          * phi.embed((0, 2), 3)).integrate_except((0, 1)).scale(-1)
    return rx, ry


def direct_force_generator(observable, force):
    number = observable.n
    return total((relative(force, number, i, j) * observable.diff(i)
                  for i in range(number) for j in range(number) if j != i),
                 number).scale(F(1, number))


def laplacian(poly):
    return total((poly.diff(j).diff(j) for j in range(poly.n)), poly.n)


def witness(poly):
    key = min(poly.c)
    return {"frequency": list(key), "coefficient": str(poly.c[key])}


def main(output):
    count = {}
    mutations = {}
    samples = []

    def check(category, condition):
        count[category] = count.get(category, 0) + 1
        if not condition:
            raise AssertionError((category, count[category]))

    def try_mutation(name, defect, context):
        if defect.c and name not in mutations:
            mutations[name] = {"context": context, **witness(defect)}

    constant = Poly(2, {(0, 0): F(7, 5)})
    kernels = {
        "constant": constant,
        "relative_two": cosine(2, -2),
        "additive_three": cosine(3, 0) + cosine(0, 3),
        "center_one": cosine(1, 1),
        "mixed_2_3": sym(cosine(2, 3)),
        "separable": cosine(2, 0) * cosine(0, 2),
        "combined": sym(cosine(1, -3)) + cosine(2, -2).scale(F(2, 3))
                    + (cosine(3, 0) + cosine(0, 3)).scale(F(5, 7)) + constant,
    }
    forces = {
        "zero": Poly(1),
        "mode_two": Poly(1, {(2,): F(3, 5), (-2,): F(-3, 5)}),
        "modes_1_3": Poly(1, {(1,): F(1, 7), (-1,): F(-1, 7),
                             (3,): F(2, 5), (-3,): F(-2, 5)}),
    }
    for label, phi in kernels.items():
        check("pair_symmetry", phi == phi.embed((1, 0), 2))
        check("real_pair_modes", phi.c == {tuple(-x for x in k): v for k, v in phi.c.items()})
        for force_label, force in forces.items():
            check("odd_force", force.c == {(-k[0],): -v for k, v in force.c.items()})
            check("force_zero_haar", not force.integrate_except(()).c)
            rx, ry = response_slots(phi, force)
            response = rx + ry
            bphi = relative(force, 2, 0, 1) * (phi.diff(0) - phi.diff(1))
            cube = sym(relative(force, 3, 0, 2) * phi.diff(0).embed((0, 1), 3))
            a = phi.diff(0).integrate_except((0,))
            aa = relative(force, 2, 0, 1) * (a.embed((0,), 2) - a.embed((1,), 2))
            v = (relative(force, 2, 1, 0) * a.embed((1,), 2)).integrate_except((0,))
            check("cubic_one_background", cube.integrate_except((0, 1)) == (aa + response).scale(F(1, 6)))
            check("cubic_two_background", cube.integrate_except((0,)) == v.scale(F(1, 3)))
            check("cubic_scalar_zero", not cube.integrate_except(()).c)
            check("response_slice", response.integrate_except((0,)) == v)
            check("response_scalar_zero", not response.integrate_except(()).c)
            # An independent integrated-gradient formula checks the convolution sign.
            rx_grad = (relative(force, 3, 2, 0) * phi.diff(0).embed((2, 1), 3)).integrate_except((0, 1))
            check("response_integration_by_parts", rx == rx_grad)
            for number in (2, 3, 4, 6):
                context = {"N": number, "pair": label, "force": force_label}
                observable = pair_stat(phi, number)
                direct = direct_force_generator(observable, force)
                cubic = statistic(cube, number)
                raw_repeated = deleted_pair(bphi, number).scale(F(1, 2 * number))
                linear_response = pair_stat(response, number)
                check("full_raw_force_identity", direct == cubic + linear_response + raw_repeated)
                g = bphi.integrate_except((0,))
                c = g.integrate_except(())
                rho_g = statistic(g, number)
                scalar = c.embed((), number).scale(F(1, 2 * number))
                lower = rho_g.scale(F(1, number)) + scalar
                internal = pair_stat(bphi, number).scale(F(1, number))
                check("full_inverse_force_identity", direct == cubic + linear_response + internal + lower)
                check("lower_regrouping", raw_repeated - internal == lower)
                empirical_g = total((g.embed((i,), number) for i in range(number)), number).scale(F(1, number))
                check("lower_empirical_form", lower == empirical_g.scale(F(1, number)) - scalar)
                check("diffusion_no_extra_trace", laplacian(observable) == pair_stat(laplacian(phi), number))
                try_mutation("omit_scalar", scalar, context)
                try_mutation("halve_centered_lower", rho_g.scale(F(1, 2 * number)), context)
                try_mutation("flip_scalar_sign", scalar.scale(2), context)
                try_mutation("omit_x_response", pair_stat(rx, number), context)
                try_mutation("omit_y_response", pair_stat(ry, number), context)
                try_mutation("halve_internal_repeated", raw_repeated.scale(F(1, 2)), context)
                try_mutation("falling_factorial_pair", (deleted_pair(bphi, number, True) - deleted_pair(bphi, number)).scale(F(1, 2 * number)), context)
                try_mutation("double_cubic", cubic, context)
                if number == 2:
                    try_mutation("drop_N2_background_cubic", cubic, context)
                if label == "relative_two" and force_label == "mode_two" and number == 2:
                    samples.append({"case": context, "scalar_B_formal": str(c.c.get((), 0)),
                                    "lower_formal": witness(lower), "N2_cubic_formal": witness(cubic),
                                    "rho_g_identically_zero": not rho_g.c})
    required_mutations = {"omit_scalar", "halve_centered_lower", "flip_scalar_sign", "omit_x_response",
                          "omit_y_response", "halve_internal_repeated", "falling_factorial_pair",
                          "double_cubic", "drop_N2_background_cubic"}
    check("all_mutations_detected", set(mutations) == required_mutations)

    admitted = critical = 0
    mesh = sorted({F(a, den) for den in range(1, 18) for a in range(1, 29 * den)})
    for dimension in range(3, 31):
        for s in mesh:
            if not 0 < s < dimension - 2:
                continue
            p = s + 2
            low = max(F(1), s / 2)
            high = min(F(dimension, 2), dimension - s - 1, s + 1)
            midpoint = (low + high) / 2
            restriction = 3 * s < 2 * dimension - 2
            check("interval_equivalence", (low < high) == restriction)
            if restriction:
                admitted += 1
                check("six_admissibility_inequalities", all(a < b for a in (F(1), s / 2)
                                                           for b in (F(dimension, 2), dimension-s-1, s+1)))
                check("midpoint_admissible", 1 < midpoint < F(dimension, 2)
                      and midpoint < s + 1 and midpoint < dimension - s - 1 and midpoint > s / 2)
                exponent = (s + 1 - midpoint) / p
                kappa = (2 * midpoint - s) / (2 * p)
                check("decay_exponent", exponent - F(1, 2) == -kappa and kappa > 0)
                q2 = (midpoint + 1 + dimension) / 2
                check("R8_second_exponent", midpoint + 1 < q2 < dimension)
            if s * p < 2 * dimension:
                critical += 1
                check("critical_included", restriction and low < high)
            theta = 1 - s / dimension
            chi_power = 2 / p - theta
            check("critical_rescaled_noise", chi_power == s * (s + 2 - dimension) / (dimension * p)
                  and chi_power < 0)

    boundaries = []
    for dimension, s in [(7, F(4)), (8, F(5)), (3, F(0)), (3, F(1)), (12, F(4))]:
        low = max(F(1), s / 2)
        high = min(F(dimension, 2), dimension - s - 1, s + 1)
        q = (low + high) / 2
        row = {"d": dimension, "s": str(s), "q_low": str(low), "q_high": str(high),
               "q": str(q), "product_margin": str(dimension - s - 1 - q),
               "kappa": str((2*q-s)/(2*(s+2))),
               "strict_R12_critical": bool(0 < s < dimension-2 and s*(s+2)<2*dimension)}
        boundaries.append(row)
    check("lower_boundary_log", boundaries[0]["q_low"] == boundaries[0]["q_high"] == "2"
          and boundaries[0]["product_margin"] == boundaries[0]["kappa"] == "0")
    check("empty_exponent_range", F(boundaries[1]["q_low"]) > F(boundaries[1]["q_high"]))
    check("log_and_coulomb_excluded", all(row["q_low"] == row["q_high"] for row in boundaries[2:4]))
    check("R12_equality_not_lower_counterexample", not boundaries[4]["strict_R12_critical"]
          and F(boundaries[4]["q_low"]) < F(boundaries[4]["q_high"]))
    for q, s, dimension, category in [(F(2), F(4), 7, "product_radial_log"),
                                      (F(7, 2), F(1), 7, "squared_weight_radial_log")]:
        power = dimension - 1 - (s + 1 + q) if category == "product_radial_log" else dimension - 1 - 2*q
        check(category, power == -1)
    for nu in (F(0), F(1, 100), F(1), F(5, 2)):
        b = F(1) if nu == 0 else min(1 / nu, F(1))
        check("noise_convention", 0 < b <= 1 and (nu == 0 or nu*b <= 1))
    check("regimes_distinct", F(5, 6) + 2*F(1, 2)/3 - 1 == F(1, 6)
          and F(3, 4) + F(1, 2)/3 - 1 == -F(1, 12)
          and F(3, 4) + 2*F(1, 2)/3 - 1 == F(1, 12))

    # Finite signed functions and empirical measures test only the elementary
    # deterministic inequality; they are not asserted to be singular inverses.
    for values in product((F(-1), F(-1, 3), F(0), F(2, 5), F(1)), repeat=3):
        c = sum(values, F(0)) / 3
        maximum = max(abs(x) for x in values)
        for number in (2, 3, 5):
            for labels in product(range(3), repeat=number):
                eta = sum((values[j] for j in labels), F(0)) / number
                lower = (eta-c)/number + c/(2*number)
                check("pathwise_triangle_constant", abs(lower) <= F(3, 2)*maximum/number)
    segments = [(F(1, 3), F(2)), (F(2, 3), F(-1))]
    signed = sum((length * value for length, value in segments), F(0))
    absolute = sum((length * abs(value) for length, value in segments), F(0))
    check("two_time_norms_distinct", signed == 0 and absolute == F(4, 3))
    for x in (F(-5), F(-1, 3), F(0), F(2, 7), F(9)):
        for y in (F(-2), F(-1, 11), F(0), F(1, 13), F(3)):
            check("reverse_triangle_perturbation", abs(abs(x+y)-abs(x)) <= abs(y))
    manifest = Path(__file__).resolve().parent / 'INPUT_SHA256SUMS.txt'
    input_root = Path(__file__).resolve().parent / 'INPUTS'
    input_records = []
    for row in manifest.read_text().splitlines():
        expected, name = row.split('  ', 1)
        actual = hashlib.sha256((input_root/name).read_bytes()).hexdigest()
        check("allowed_input_seal", expected == actual)
        input_records.append({"path": name, "sha256": actual})
    result = {"status": "PASS", "task": "TASK-076", "python": platform.python_version(),
              "assertions": sum(count.values()), "categories": count,
              "admitted_mesh_cases": admitted, "strict_critical_mesh_cases": critical,
              "coefficient_parameter_cases": len(kernels)*len(forces)*4,
              "mutations": mutations, "exact_samples": samples, "boundary_cases": boundaries,
              "norm_probe": {"signed_integral": str(signed), "absolute_integral": str(absolute)},
              "input_seals": input_records,
              "evidence_limit": "Finite exact coefficient/range checks and newly written reviewer self-check; not a proof of the singular inverse, any analytic limit, cubic smallness, or earlier premise certification.",
              "convention": "Physical real odd force = i times formal force; physical derivative = 2 pi i times delta; all formal force drifts multiply by -2 pi, diffusion by -4 pi^2.",
              "random_seed": None, "floating_tolerance": None}
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({key: result[key] for key in ('status', 'assertions', 'admitted_mesh_cases',
                                                   'strict_critical_mesh_cases', 'coefficient_parameter_cases')}))
    print('Detected coefficient mutations:', len(mutations))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('RESULTS.json'))
    main(parser.parse_args().output)
