#!/usr/bin/env python3
"""Fresh exact supporting diagnostics for TASK-071; standard library only.

Finite Fourier coefficients are rational. D_j = partial_j/(2*pi*i).
Thus physical gradient products divide by (2*pi)^2 to minus products of D_j.
The physical particle generator divides by (2*pi)^2 to generator() below.
These tests verify algebra and endpoint diagnostics, not singular analytic proofs.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

COUNTS = Counter()


def check(condition, category):
    if not condition:
        raise AssertionError(category)
    COUNTS[category] += 1


def clean(poly):
    return {k: F(v) for k, v in poly.items() if v}


def add(*polys):
    out = {}
    for poly in polys:
        for k, value in poly.items():
            out[k] = out.get(k, F(0)) + value
    return clean(out)


def scale(poly, value):
    return clean({k: value * c for k, c in poly.items()})


def mul(left, right):
    out = {}
    for k, c in left.items():
        for l, b in right.items():
            m = tuple(x + y for x, y in zip(k, l))
            out[m] = out.get(m, F(0)) + c * b
    return clean(out)


def deriv(poly, slot):
    return clean({k: k[slot] * c for k, c in poly.items()})


def embed(poly, slots, n):
    out = {}
    for k, c in poly.items():
        m = [0] * n
        for i, j in enumerate(slots):
            m[j] += k[i]
        m = tuple(m)
        out[m] = out.get(m, F(0)) + c
    return clean(out)


def integrate(poly, slot):
    out = {}
    for k, c in poly.items():
        if k[slot] == 0:
            m = k[:slot] + k[slot + 1:]
            out[m] = out.get(m, F(0)) + c
    return clean(out)


def expectation(poly, density, n):
    return mul(poly, density).get((0,) * n, F(0))


def cosine(k):
    if all(v == 0 for v in k):
        return {tuple(k): F(1)}
    return {tuple(k): F(1, 2), tuple(-v for v in k): F(1, 2)}


def literal_statistic(phi, n):
    q = integrate(phi, 1)
    mean = q.get((0,), F(0))
    out = {(0,) * n: mean / 2}
    for i in range(n):
        for j in range(n):
            if i != j:
                out = add(out, scale(embed(phi, (i, j), n), F(1, 2 * n * n)))
        out = add(out, scale(embed(q, (i,), n), F(-1, n)))
    return clean(out)


def generator(poly, n, nu, kernel):
    """Direct finite-N generator on Fourier monomials, including all forces."""
    out = {}
    for l, value in poly.items():
        out[l] = out.get(l, F(0)) - nu * sum(v * v for v in l) * value
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for (k,), g in kernel.items():
                    m = list(l)
                    m[i] += k
                    m[j] -= k
                    m = tuple(m)
                    out[m] = out.get(m, F(0)) + F(k * l[i], n) * g * value
    return clean(out)


def nonproduct_density(n):
    # 1 + epsilon sum_(i<j) cos(2*pi*(x_i-x_j)) >= 1/2.
    pairs = n * (n - 1) // 2
    epsilon = F(1, 2 * pairs)
    out = {(0,) * n: F(1)}
    for i in range(n):
        for j in range(i + 1, n):
            out = add(out, scale(embed(cosine((1, -1)), (i, j), n), epsilon))
    check(F(1) - epsilon * pairs == F(1, 2), "diagnostic_density_positive")
    for i in range(n):
        marginal = out
        for j in reversed(range(n)):
            if j != i:
                marginal = integrate(marginal, j)
        check(marginal == {(0,): F(1)}, "diagnostic_one_body_haar")
    return out


def literal_pair_and_noise():
    additive = add(cosine((1, 0)), cosine((0, 1)))
    separable = mul(cosine((1, 0)), cosine((0, 1)))
    mixed = add(cosine((1, 2)), cosine((2, 1)))
    probes = [cosine((0, 0)), cosine((1, -1)), additive, separable,
              mixed, add(additive, separable, scale(mixed, F(2, 3)))]
    kernels = [{}, cosine((1,)), add(cosine((1,)), scale(cosine((2,)), F(1, 3)))]
    mutation_hits = Counter()
    for n in (2, 3, 4, 5):
        density_cases = [{(0,) * n: F(1)}, nonproduct_density(n)]
        for phi in probes:
            check(phi == {(b, a): c for (a, b), c in phi.items()}, "pair_exchange")
            stat = literal_statistic(phi, n)
            G = deriv(phi, 0)
            A = integrate(G, 1)
            H = add(G, scale(embed(A, (0,), 2), -1))
            direct_gradients = [deriv(stat, i) for i in range(n)]
            for i, actual in enumerate(direct_gradients):
                field = scale(embed(A, (i,), n), F(-1, n * n))
                for j in range(n):
                    if i != j:
                        field = add(field, scale(embed(H, (i, j), n), F(1, n * n)))
                check(actual == field, "literal_deleted_gradient")
                without_missing_self = add(field, scale(embed(A, (i,), n), F(1, n * n)))
                if actual != without_missing_self:
                    mutation_hits["missing_self"] += 1
            squares = scale(add(*(mul(v, v) for v in direct_gradients)), -1)
            for density in density_cases:
                H12 = embed(H, (0, 1), n)
                A1 = embed(A, (0,), n)
                e2 = -expectation(mul(H12, H12), density, n)
                eA = -expectation(mul(H12, A1), density, n)
                eAA = -expectation(mul(A1, A1), density, n)
                e3 = F(0)
                if n >= 3:
                    H13 = embed(H, (0, 2), n)
                    e3 = -expectation(mul(H12, H13), density, n)
                predicted = ((n - 1) * e2 + (n - 1) * (n - 2) * e3
                             - 2 * (n - 1) * eA + eAA) / n ** 3
                observed = expectation(squares, density, n)
                check(observed == predicted, "four_law_contractions")
                check(observed >= 0, "nonnegative_combined_bracket")
                if e3:
                    mutation_hits["missing_triple"] += 1
                if density == {(0,) * n: F(1)}:
                    GG = -mul(G, G).get((0, 0), F(0))
                    AA = -mul(A, A).get((0,), F(0))
                    check(observed == F(n - 1, n ** 3) * GG - F(n - 2, n ** 3) * AA,
                          "exact_haar_projection")
            # Limit expensive literal product-generator probes to N<=4.
            if n <= 4:
                for nu in (F(0), F(1, 7), F(3, 2)):
                    for kernel in kernels:
                        car = add(generator(mul(stat, stat), n, nu, kernel),
                                  scale(mul(stat, generator(stat, n, nu, kernel)), -2))
                        check(car == scale(squares, 2 * nu), "physical_carre_du_champ")
                        if nu and squares:
                            check(car != scale(squares, 4 * nu), "wrong_noise_factor_rejected")
            for kernel in kernels:
                energy = {}
                for i in range(n):
                    for j in range(i + 1, n):
                        rel = {(k[0], -k[0]): c for k, c in kernel.items()}
                        energy = add(energy, scale(embed(rel, (i, j), n), F(1, n)))
                fourier = {(0,) * n: -sum(kernel.values(), F(0)) / 2}
                for (k,), c in kernel.items():
                    eta = {}
                    eta_negative = {}
                    for i in range(n):
                        eta = add(eta, embed({(k,): F(1, n)}, (i,), n))
                        eta_negative = add(eta_negative, embed({(-k,): F(1, n)}, (i,), n))
                    fourier = add(fourier, scale(mul(eta, eta_negative), F(n, 2) * c))
                check(energy == clean(fourier), "literal_energy_self_diagonal")
    check(mutation_hits["missing_self"] > 0, "mutation_coverage_missing_self")
    check(mutation_hits["missing_triple"] > 0, "mutation_coverage_missing_triple")


def response_convolution():
    phi = add(cosine((1, 0)), cosine((0, 1)), cosine((1, 2)), cosine((2, 1)),
              cosine((1, -1)), cosine((0, 0)))
    d = {(0,): F(0), (1,): F(2), (-1,): F(2), (2,): F(3), (-2,): F(3)}
    direct_slots = []
    for slot in (0, 1):
        shifted = {}
        for (k, l), c in phi.items():
            shifted[(k, l, (k, l)[slot])] = c
        direct = scale(integrate(mul(shifted, embed(d, (2,), 3)), 2), -1)
        expected = clean({(k, l): -d.get(((k, l)[slot],), F(0)) * c
                          for (k, l), c in phi.items()})
        check(direct == expected, "response_slot_direct_convolution")
        direct_slots.append(direct)
    total = add(*direct_slots)
    expected_total = clean({(k, l): -(d.get((k,), F(0)) + d.get((l,), F(0))) * c
                            for (k, l), c in phi.items()})
    check(total == expected_total, "both_compensated_responses")
    check(total != direct_slots[0], "missing_response_slot_rejected")
    check((0, 0) not in total, "response_kills_constant")
    for slot in (0, 1):
        expected_derivative = clean({(k, l): -(d.get((k,), F(0)) + d.get((l,), F(0))) * c
                                     for (k, l), c in deriv(phi, slot).items()})
        check(deriv(total, slot) == expected_derivative, "homogeneous_derivative_commutation")


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def matvec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def radial_and_rates():
    for d in range(4, 11):
        e = [F(3, 5), F(4, 5)] + [F(0)] * (d - 2)
        tang = [F(-4, 5), F(3, 5)] + [F(0)] * (d - 2)
        check(dot(e, e) == 1 and dot(e, tang) == 0, "radial_probe_geometry")
        for s in (F(1, 100), F(1, 8), F(1, 2), F(1), F(3, 2), F(199, 100)):
            p = s + 2
            a = s / p
            theta = 1 - s / d
            delta = 1 / (6 * p * p)
            q0 = 1 + s / 4
            eta0 = s + 1 - q0
            gamma = (p - 2 * q0) / q0
            for q in (p / 2, q0):
                eta = s + 1 - q
                check(1 < q < min(d - 2, F(d, 2)), "frozen_q_range")
                check(q <= s + 1 and 0 <= eta < 2, "frozen_eta_range")
                hess = [[q * (q + 2) * e[i] * e[j] - (q if i == j else 0)
                         for j in range(d)] for i in range(d)]
                trace = sum((hess[i][i] for i in range(d)), F(0))
                check(trace == q * (q + 2 - d), "radial_laplacian_from_hessian")
                check(trace < 0, "negative_diffusion_weight")
                for n in (2, 3, 7):
                    force_jac = [[s * ((1 if i == j else 0) - p * e[i] * e[j])
                                  for j in range(d)] for i in range(d)]
                    pair_jac = [[F(1, n) * force_jac[i % d][j % d]
                                 * (1 if (i < d) == (j < d) else -1)
                                 for j in range(2 * d)] for i in range(2 * d)]
                    center = e + e
                    radial = e + [-v for v in e]
                    transverse = tang + [-v for v in tang]
                    check(matvec(pair_jac, center) == [F(0)] * (2 * d), "pair_center_eigenvalue")
                    check(matvec(pair_jac, transverse) == [2 * s / n * v for v in transverse],
                          "pair_transverse_eigenvalue")
                    check(matvec(pair_jac, radial) == [-2 * s * (s + 1) / n * v for v in radial],
                          "pair_radial_eigenvalue")
                    weight_gradient = [-q * v for v in e]
                    drift = [2 * s / n * v for v in e]
                    coefficient = dot(drift, weight_gradient) + 2 * s / n
                    check(coefficient == -2 * s * (q - 1) / n < 0,
                          "repulsive_weight_coefficient")
            check(a - theta == (s*s + 2*s - 2*d) / (d*p) < 0, "strict_energy_decay")
            check(delta * (1 - s/2) == (2-s)/(12*p*p) > 0, "low_noise_rate")
            check(gamma == 2*s/(s+4) and 2 + gamma == p/q0, "tail_weight_identity")
            check(delta*eta0*p/(2*q0) - gamma/(4*p) == -s/(4*p*(s+4)) < 0,
                  "full_high_noise_tail_rate")
            check(2*q0 < p < d, "tail_strict_moment_gap")
            check(s * (d-p) > 0, "positive_actual_occupation_coefficient")
            for n in (2, 3, 9):
                pairs = n * (n-1) // 2
                check(F(2, n) * pairs == n-1, "actual_unordered_laplacian_factor")
                check(F(n, n-1) <= 2, "floor_to_pair_uniform_factor")
            if s < 1:
                check(s + 1 < min(d-2, F(d, 2)), "eta_zero_admitted")
                check(s+1-(s+1) == 0, "eta_zero_endpoint")
    q = F(5, 4)
    check(2*q*(q+2-3) > 0, "d3_diffusion_obstruction")
    for d in (4, 5, 6):
        q = F(d-2)
        check(2*q*(d-2-q) == 0, "q_endpoint_loses_diffusion_occupation")
        s = F(d-2)
        check(s*(d-s-2) == 0, "coulomb_loses_power_occupation")
    check(2*F(1)*(1-1) == 0, "q1_loses_repulsion")
    check(1-F(2, 2) == 0, "s2_loses_low_noise_decay")


def verify_inputs():
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    manifest = here / "INPUT_SHA256SUMS.txt"
    inputs = []
    for row in manifest.read_text().splitlines():
        expected, name = row.split("  ", 1)
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        check(actual == expected, "input_sha256")
        inputs.append({"path": name, "sha256": actual})
    check(len(inputs) == 27, "allowed_input_count")
    return inputs, hashlib.sha256(manifest.read_bytes()).hexdigest()


def main():
    inputs, manifest_digest = verify_inputs()
    literal_pair_and_noise()
    response_convolution()
    radial_and_rates()
    result = {
        "status": "PASS",
        "assertions": sum(COUNTS.values()),
        "categories": dict(sorted(COUNTS.items())),
        "arithmetic": "Python fractions.Fraction, no floating point, randomness, or tolerance",
        "scope": "Exact supporting algebra and endpoint diagnostics; not independent certification of singular analysis",
        "normalization": "D_j=partial_j/(2*pi*i); generator normalized by (2*pi)^2; gradient square=-sum(D_j P)^2 in those units",
        "input_manifest_sha256": manifest_digest,
        "inputs": inputs,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = Path(__file__).with_name("EXACT_RESULT.json")
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "assertions": result["assertions"],
                      "result": str(target)}, indent=2))


if __name__ == "__main__":
    main()
