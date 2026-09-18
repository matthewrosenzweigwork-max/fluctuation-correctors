#!/usr/bin/env python3
"""Independent TASK059 diagnostic: exact Q(i) Fourier algebra, standard library.

One angular coordinate is embedded in the d-dimensional unit torus. Angular
derivatives are physical derivatives divided by 2*pi; squared-gradient tests
therefore have a common omitted factor (2*pi)^2 on both sides. The Coulomb
drift calculation restores the cancelling force/derivative factors and uses
c_d=1. These are finite algebra diagnostics, not a singular-domain proof.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ComplexQ = tuple[F, F]
Polynomial = dict[tuple[int, ...], ComplexQ]
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
COUNTS: Counter[str] = Counter()
WITNESSES: dict[str, object] = {}


def cq(real=0, imag=0) -> ComplexQ:
    return F(real), F(imag)


def ca(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] + b[0], a[1] + b[1]


def cm(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def cs(a: ComplexQ, scale) -> ComplexQ:
    return a[0] * scale, a[1] * scale


def clean(poly: Polynomial) -> Polynomial:
    return {key: value for key, value in poly.items() if value != ZERO}


def add(*polys: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for poly in polys:
        for key, value in poly.items():
            result[key] = ca(result.get(key, ZERO), value)
    return clean(result)


def scale(poly: Polynomial, factor) -> Polynomial:
    return clean({key: cs(value, F(factor)) for key, value in poly.items()})


def multiply(a: Polynomial, b: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x + y for x, y in zip(ka, kb))
            result[key] = ca(result.get(key, ZERO), cm(va, vb))
    return clean(result)


def constant(dim: int, value=1) -> Polynomial:
    return clean({(0,) * dim: cq(value)})


def cosine(*frequency: int) -> Polynomial:
    neg = tuple(-x for x in frequency)
    return add({tuple(frequency): cq(F(1, 2))}, {neg: cq(F(1, 2))})


def sine(*frequency: int) -> Polynomial:
    neg = tuple(-x for x in frequency)
    return add({tuple(frequency): cq(0, F(-1, 2))}, {neg: cq(0, F(1, 2))})


def derivative(poly: Polynomial, slot: int) -> Polynomial:
    return clean({k: cm(v, cq(0, k[slot])) for k, v in poly.items()})


def marginal(poly: Polynomial, slots: tuple[int, ...]) -> Polynomial:
    # Integrate every variable not retained; used for both kernels and laws.
    result: Polynomial = {}
    for key, value in poly.items():
        if all(k == 0 for i, k in enumerate(key) if i not in slots):
            projected = tuple(key[i] for i in slots)
            result[projected] = ca(result.get(projected, ZERO), value)
    return clean(result)


def lift(poly: Polynomial, dim: int, slots: tuple[int, ...]) -> Polynomial:
    result: Polynomial = {}
    for key, value in poly.items():
        expanded = [0] * dim
        for slot, k in zip(slots, key):
            expanded[slot] += k
        key2 = tuple(expanded)
        result[key2] = ca(result.get(key2, ZERO), value)
    return clean(result)


def expectation(poly: Polynomial, law: Polynomial) -> F:
    value = ZERO
    for key, coeff in poly.items():
        value = ca(value, cm(coeff, law.get(tuple(-k for k in key), ZERO)))
    check(value[1] == 0, "real_expectations")
    return value[0]


def check(condition: bool, category: str) -> None:
    if not condition:
        raise AssertionError(category)
    COUNTS[category] += 1


def square(poly: Polynomial) -> Polynomial:
    return multiply(poly, poly)


def swap(poly: Polynomial) -> Polynomial:
    return {(key[1], key[0]): value for key, value in poly.items()}


def invariant_law(n: int, epsilon: F, harmonic: int) -> Polynomial:
    # Since every cosine is in [-1,1], this density is >= 1-|epsilon| > 0.
    pairs = [lift(cosine(harmonic, -harmonic), n, (i, j))
             for i in range(n) for j in range(i + 1, n)]
    return add(constant(n), scale(add(*pairs), epsilon / F(n * (n - 1), 2)))


def biased_law(n: int, epsilon: F) -> Polynomial:
    # Exchangeable, bounded positive, and generally not Haar in one variable.
    terms = [lift(cosine(2), n, (i,)) for i in range(n)]
    return add(constant(n), scale(add(*terms), epsilon / n))


def statistic(phi: Polynomial, n: int) -> Polynomial:
    raw = [lift(phi, n, (i, j)) for i in range(n) for j in range(n) if i != j]
    projection = marginal(phi, (0,))
    mixed = [lift(projection, n, (i,)) for i in range(n)]
    scalar = phi.get((0, 0), ZERO)
    return add(scale(add(*raw), F(1, 2 * n * n)),
               scale(add(*mixed), F(-1, n)), {(0,) * n: cs(scalar, F(1, 2))})


def pair_and_law_checks() -> None:
    phi_cases = {
        "constant": constant(2, 7),
        "separable": add(scale(add(cosine(1, 0), cosine(0, 1)), 2),
                         sine(1, 0), sine(0, 1)),
        "relative": add(cosine(1, -1), scale(cosine(2, -2), F(1, 3))),
        "mixed_third_frequency": add(cosine(1, 0), cosine(0, 1),
                                      cosine(3, -2), cosine(-2, 3),
                                      scale(sine(1, 1), F(2, 3))),
    }
    nonzero_deviations = set()
    for name, phi in phi_cases.items():
        check(phi == swap(phi), "pair_symmetry")
        g = derivative(phi, 0)
        a = marginal(g, (0,))
        h = add(g, scale(lift(a, 2, (0,)), -1))
        check(marginal(h, (0,)) == {}, "conditional_Haar_centering")
        gnorm = expectation(square(g), constant(2))
        anorm = expectation(square(a), constant(1))
        hnorm = expectation(square(h), constant(2))
        check(hnorm == gnorm - anorm, "orthogonal_decomposition")
        check(expectation(square(derivative(phi, 1)), constant(2)) == gnorm,
              "both_gradient_slots")
        for n in (2, 3, 4):
            p = statistic(phi, n)
            gradients = [derivative(p, i) for i in range(n)]
            for i in range(n):
                field = scale(add(*[lift(h, n, (i, j)) for j in range(n) if i != j],
                                  scale(lift(a, n, (i,)), -1)), F(1, n * n))
                check(gradients[i] == field, "raw_statistic_gradient")
            q = add(*[square(x) for x in gradients])
            ref = expectation(q, constant(n))
            expected_ref = F(n - 1, n**3) * gnorm - F(n - 2, n**3) * anorm
            check(ref == expected_ref, "Haar_exact_coefficients")
            if name == "separable":
                check(ref == anorm / n**3 and ref > 0, "deletion_survives_for_G_equals_A")
            if n == 2:
                check(ref == gnorm / 8, "N2_Haar_coefficient")
            if n == 3:
                check(ref == (2 * gnorm - anorm) / 27, "N3_Haar_coefficient")
            laws = {
                "Haar": constant(n),
                "invariant_plus": invariant_law(n, F(1, 3), 2),
                "invariant_minus": invariant_law(n, F(-2, 5), 2),
                "biased_exchangeable": biased_law(n, F(2, 5)),
            }
            for law_name, law in laws.items():
                check(expectation(constant(n), law) == 1, "law_normalization")
                for permutation in itertools.permutations(range(n)):
                    permuted = {tuple(k[i] for i in permutation): v for k, v in law.items()}
                    check(permuted == law, "law_exchangeability")
                h12 = lift(h, n, (0, 1))
                a1 = lift(a, n, (0,))
                e2 = expectation(square(h12), law)
                e3 = (expectation(multiply(h12, lift(h, n, (0, 2))), law)
                      if n >= 3 else F(0))
                em = expectation(multiply(h12, a1), law)
                ea = expectation(square(a1), law)
                actual = expectation(q, law)
                expanded = ((n - 1) * e2 + (n - 1) * (n - 2) * e3
                            - 2 * (n - 1) * em + ea) / n**3
                check(actual == expanded, "arbitrary_exchangeable_four_terms")
                if law_name.startswith("invariant"):
                    check(all(sum(k) == 0 for k in law), "common_translation_invariance")
                    check(marginal(law, (0,)) == constant(1), "one_body_Haar")
                    check(marginal(law, (0, 1)) != constant(2), "nonproduct_pair")
                    f2 = marginal(law, (0, 1))
                    delta2 = expectation(square(h), add(f2, scale(constant(2), -1)))
                    deltaA = expectation(multiply(h, lift(a, 2, (0,))),
                                         add(f2, scale(constant(2), -1)))
                    delta3 = F(0)
                    if n >= 3:
                        f3 = marginal(law, (0, 1, 2))
                        delta3 = expectation(multiply(lift(h, 3, (0, 1)),
                                                       lift(h, 3, (0, 2))),
                                             add(f3, scale(constant(3), -1)))
                    for label, value in (("pair", delta2), ("triple", delta3), ("mixed", deltaA)):
                        if value:
                            nonzero_deviations.add(label)
                    for nu in (F(0), F(1, 2), F(1), F(2), F(7, 3)):
                        b = min(1 / nu, F(1)) if nu else F(1)
                        factor = 2 * nu * n * b
                        delta = ((n - 1) * delta2 + (n - 1) * (n - 2) * delta3
                                 - 2 * (n - 1) * deltaA)
                        check(factor * (actual - ref) == 2 * nu * b * delta / n**2,
                              "scaled_pair_triple_mixed_reduction")
                        check(abs(factor * (actual - ref)) <= 2 * nu * b / n**2 *
                              ((n - 1) * abs(delta2) + (n - 1) * (n - 2) * abs(delta3)
                               + 2 * (n - 1) * abs(deltaA)), "absolute_law_error_majorant")
                elif law_name == "biased_exchangeable" and ea != anorm:
                    WITNESSES["non_Haar_one_body_square_requires_its_own_term"] = str(ea - anorm)
            for nu in (F(0), F(1, 2), F(1), F(2), F(7, 3)):
                b = min(1 / nu, F(1)) if nu else F(1)
                check(0 <= b * nu <= 1, "temperature_normalization")
                check(2 * nu * n * b * ref <= b * F(n - 1, n * n) * nu * 2 * gnorm,
                      "reference_noise_prefactor")
            if name == "mixed_third_frequency" and n in (2, 3):
                WITNESSES[f"Haar_N{n}_mixed_kernel"] = str(ref)
    check(nonzero_deviations == {"pair", "triple", "mixed"}, "all_law_deviations_exercised")
    check("non_Haar_one_body_square_requires_its_own_term" in WITNESSES,
          "non_Haar_one_body_term_exercised")

    for m in (2, 3, 4):
        phi = add(cosine(1, 0), cosine(0, 1), cosine(m, 1 - m), cosine(1 - m, m))
        g = derivative(phi, 0)
        a = marginal(g, (0,))
        h = add(g, scale(lift(a, 2, (0,)), -1))
        epsilon = F(2, 5)
        law = add(constant(2), scale(cosine(m - 1, 1 - m), epsilon))
        mixed = expectation(multiply(h, lift(a, 2, (0,))), law)
        check(mixed == epsilon * m / 4, "nonzero_invariant_mixed_contraction")
        WITNESSES[f"invariant_mixed_m{m}"] = str(mixed)


def response_and_flux_checks() -> None:
    phi_cases = [constant(2), add(constant(2), scale(cosine(1, -1), -1)),
                 add(cosine(1, 0), cosine(0, 1), cosine(3, -2), cosine(-2, 3)),
                 sine(1, 1)]
    for exponent in (0, -1, -2, -3):
        def d(k: int) -> F:
            return F(abs(k)) ** exponent if k else F(0)

        for phi in phi_cases:
            response = {k: cs(v, -d(k[0]) - d(k[1])) for k, v in phi.items()}
            form = expectation(multiply(phi, response), constant(2))
            spectral = -sum((d(k[0]) + d(k[1])) * (v[0]**2 + v[1]**2)
                            for k, v in phi.items())
            check(form == spectral <= 0, "response_Fourier_positivity_both_slots")

            # Compute <Phi,B Phi> directly from K_hat(m)=-i*d_m/(2*pi*m)
            # and the physical derivative i*2*pi*(b_x-b_y), without a flux rule.
            direct = ZERO
            divergence_form = ZERO
            for ka, va in phi.items():
                for kb, vb in phi.items():
                    m = -(ka[0] + kb[0])
                    if m and ka[1] + kb[1] == m:
                        product = cm(va, vb)
                        direct = ca(direct, cs(product, d(m) * F(kb[0] - kb[1], m)))
                        divergence_form = ca(divergence_form, cs(product, -d(m)))
            check(direct == divergence_form, "direct_force_vs_divergence_factor")
            if exponent == 0:
                trace: Polynomial = {}
                for k, v in phi.items():
                    trace = add(trace, {(sum(k),): v})
                bulk = expectation(square(phi), constant(2))
                flux = -expectation(square(trace), constant(1))
                check(direct == cq(bulk + flux), "Coulomb_bulk_plus_retained_flux")
                check(flux <= 0 and direct[0] <= bulk, "Coulomb_flux_sign_upper_bound")
                if phi == constant(2):
                    check(bulk == 1 and flux == -1 and direct == ZERO,
                          "Coulomb_constant_cancellation")
                    WITNESSES["Coulomb_constant"] = {"bulk": "1", "flux": "-1", "sum": "0"}
                if phi == phi_cases[1]:
                    check(flux == 0 and direct == cq(F(3, 2)),
                          "Coulomb_B_is_not_dissipative")
                    WITNESSES["Coulomb_zero_diagonal_B_form"] = "3/2"
        for k in ((1, 0), (0, 1), (1, 1), (1, -1), (0, 0)):
            check(-d(k[0]) - d(k[1]) == -(int(k[0] != 0) + int(k[1] != 0)),
                  "one_and_two_slot_unit_modes")

    # Exact inner/outer radial flux on an annulus for principal Riesz drift.
    for dim in range(3, 9):
        for s in range(1, dim - 1):
            for m in (0, 1, 2, 3):
                lower, upper = F(1, 5), F(2, 3)
                power = dim - s - 2 + 2 * m
                radial_integral = ((upper**power - lower**power) / power if power else F(0))
                direct = 2 * s * m * radial_integral
                outer = s * upper**power
                inner = -s * lower**power
                bulk = -s * (dim - s - 2) * radial_integral
                check(direct == outer + inner + bulk, "annular_drift_flux_exact")
                check(inner <= 0, "inner_radial_flux_sign")


def energy_and_uniformity_checks() -> None:
    for n, nu, lam, drift, response in itertools.product(
            (2, 3, 17), (F(0), F(1, 3), F(2)), (F(1), F(5)),
            (F(-3), F(0), F(3)), (F(0), F(2))):
        # u(t)=1-t on [0,1], J(t)=1+(nu*lam-drift/N+response)*(1-t).
        source_pairing = F(1, 2) + (nu * lam - drift / n + response) / 3
        rhs = source_pairing + drift / (3 * n) - response / 3
        correct_lhs = F(1, 2) + nu * lam / 3
        check(rhs == correct_lhs, "terminal_zero_energy_sign")
        check(rhs != -F(1, 2) + nu * lam / 3, "wrong_initial_energy_sign_detected")
    for a in (F(0), F(1), F(7, 3)):
        check(a - a == 0, "backward_Fourier_sign")

    for dim in range(3, 15):
        exponents = {F(1, 4), F(dim - 2, 3), F(dim - 2, 2), F(dim - 2)}
        for s in exponents:
            p, a = s + 2, s / (s + 2)
            q1 = F(dim + 2, 4)
            q2 = (q1 + 1 + dim) / 2
            check(0 < a < 1 and 2 * a - 1 <= a, "uniform_N_power_absorption")
            check(a - 1 == -2 / p and (a - 1) / 2 == -1 / p,
                  "two_reference_noise_exponents")
            check(1 < q1 < F(dim, 2) and q1 + 1 < q2 < dim,
                  "domain_weights_exist_at_all_dimensions")
            check(dim - 1 - q1 > 0 and dim - 2 * q1 > 0,
                  "diffusion_flux_and_H1_exponents")
            check(dim - s - 2 >= 0 and dim - s > 0,
                  "Coulomb_endpoint_and_source_integrability")
            if 2 * s > dim:
                check((2 * s - dim) / p < 1, "sharper_L2_power_divided_by_N")

    for dim in range(3, 9):
        for s in range(1, dim - 1):
            p, c = s + 2, 2 * s * (s + 2)
            for n, r, z in itertools.product((2, 3, 17), (F(1, 3), F(2, 3)),
                                            (F(1), F(1, 2), F(2, 3))):
                tau = n * r**p * (z**(-p) - 1) / c
                profile = F(n, 4) * r**2 * (z**(-2) - 1)
                radial_first = F(n, 2) * r * (z**s - 1)
                time_first = s * r**(-s) * z**s
                principal_drift = F(2 * s, n) * r**(-s - 1)
                laplacian = F(n, 2) * (z**s * (dim + s - s * z**p) - dim)
                check(time_first - principal_drift * radial_first == s * r**(-s),
                      "source_profile_exact_transport")
                check(laplacian <= 0, "source_profile_diffusion_sign")
                check(-r * radial_first <= s * profile, "source_profile_regular_drift_absorption")
                check((4 * profile / n)**p <= (c * tau / n)**2,
                      "source_profile_supremum_all_N")

    for a, b in itertools.product((F(-2), F(0), F(3, 2)), repeat=2):
        check(a*a + (b-a)**2 == 2*a*a + b*b - 2*a*b, "deleted_tube_metric")
        check(a - (b-a) == 2*a-b, "deleted_tube_internal_vector")


def cross_and_symmetry_checks() -> None:
    samples = [([F(1), F(2), F(-1)], [F(3), F(-2), F(1)]),
               ([F(1)], [F(1)]), ([F(1)], [F(-1)]),
               ([F(0), F(0)], [F(2), F(3)])]
    for left, right in samples:
        la = sum(x*x for x in left)
        lb = sum(x*x for x in right)
        dot = sum(x*y for x, y in zip(left, right))
        minors = sum((left[i]*right[j] - left[j]*right[i])**2
                     for i in range(len(left)) for j in range(i+1, len(left)))
        check(la*lb-dot*dot == minors >= 0, "absolute_cross_Lagrange_identity")
    check((abs(F(1)) + abs(F(-1))) / 2 == 1 and abs((F(1)+F(-1))/2) == 0,
          "absolute_inside_integral_cannot_be_replaced")
    WITNESSES["absolute_vs_signed_average"] = {"absolute_average": "1", "signed_average": "0"}
    for n in (2, 3, 4):
        x = [F(i*i + 1, 7) for i in range(n)]
        def drift(values):
            return [sum(((values[i]-values[j])**3 - (values[i]-values[j]))
                        for j in range(n) if j != i) / n for i in range(n)]
        raw = drift(x)
        for shift in (F(-4, 3), F(2, 7)):
            check(drift([v+shift for v in x]) == raw, "drift_common_translation_algebra")
        for perm in itertools.permutations(range(n)):
            check(drift([x[i] for i in perm]) == [raw[i] for i in perm],
                  "drift_label_permutation_algebra")
    # Leading statistic differentiation from its raw empirical average.
    f = add(cosine(1), sine(2))
    fg = derivative(f, 0)
    norm = expectation(square(fg), constant(1))
    for n in (2, 3, 4):
        eta = scale(add(*[lift(f, n, (i,)) for i in range(n)]), F(1, n))
        q1 = add(*[square(derivative(eta, i)) for i in range(n)])
        for nu in (F(0), F(1, 2), F(1), F(2)):
            b = min(1 / nu, F(1)) if nu else F(1)
            expected = 2 * nu * n * b * expectation(q1, constant(n))
            check(expected == 2 * nu * b * norm, "leading_noise_exact_prefactor")
            if nu == 0:
                check(expected == 0, "zero_noise_functionals")


def verify_inputs(root: Path) -> dict[str, str]:
    manifest = root / "AUDITS/ROUND_009_ENERGY_HOSTILE_INPUT_SHA256SUMS.txt"
    lines = manifest.read_text().splitlines()
    check(len(lines) == 20, "twenty_input_allowlist")
    digests = {}
    for line in lines:
        expected, relative = line.split("  ", 1)
        actual = hashlib.sha256((root / relative).read_bytes()).hexdigest()
        check(actual == expected, "input_SHA256")
        digests[relative] = actual
    return digests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True,
                        help="New result path; refuses to overwrite an issued result.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    inputs = verify_inputs(root)
    pair_and_law_checks()
    response_and_flux_checks()
    energy_and_uniformity_checks()
    cross_and_symmetry_checks()
    output = {
        "task": "TASK059",
        "status": "PASS",
        "evidence_class": "INDEPENDENT_EXACT_DIAGNOSTIC_NOT_ANALYTIC_CERTIFICATION",
        "arithmetic": "fractions.Fraction with exact complex rational Fourier coefficients",
        "random_seed": None,
        "assertions": sum(COUNTS.values()),
        "counts": dict(sorted(COUNTS.items())),
        "witnesses": WITNESSES,
        "input_manifest_sha256": hashlib.sha256(
            (root / "AUDITS/ROUND_009_ENERGY_HOSTILE_INPUT_SHA256SUMS.txt").read_bytes()).hexdigest(),
        "input_sha256": inputs,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    with args.output.open("x") as target:
        json.dump(output, target, indent=2, sort_keys=True)
        target.write("\n")
    print(f"PASS: {sum(COUNTS.values())} exact assertions; result: {args.output}")


if __name__ == "__main__":
    main()
