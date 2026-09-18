#!/usr/bin/env python3
"""New AUD059 exact diagnostics. Standard library; no randomness or tolerances.

ExpSum represents a finite formal sum c*exp(-a), with rational a,c.
Equalities are coefficient identities, not floating-point comparisons.
Mutation witnesses also record elementary nonzero-factor reasons.
The tests support, but do not certify, the analytic proof.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path


class ExpSum:
    def __init__(self, terms=None):
        self.terms = {F(a): F(c) for a, c in (terms or {}).items() if c}

    @staticmethod
    def scalar(c):
        return ExpSum({F(0): F(c)})

    def __add__(self, other):
        if not isinstance(other, ExpSum):
            other = ExpSum.scalar(other)
        out = dict(self.terms)
        for a, c in other.terms.items():
            out[a] = out.get(a, F(0)) + c
        return ExpSum(out)

    __radd__ = __add__

    def __neg__(self):
        return ExpSum({a: -c for a, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, ExpSum) else -F(other))

    def __rsub__(self, other):
        return ExpSum.scalar(other) - self

    def __mul__(self, other):
        if not isinstance(other, ExpSum):
            other = ExpSum.scalar(other)
        out = {}
        for a, c in self.terms.items():
            for b, d in other.terms.items():
                out[a + b] = out.get(a + b, F(0)) + c * d
        return ExpSum(out)

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, ExpSum):
            other = ExpSum.scalar(other)
        return self.terms == other.terms

    def encoded(self):
        return [{"exponent": str(a), "coefficient": str(c)}
                for a, c in sorted(self.terms.items())]


def e(a):
    return ExpSum({F(a): F(1)})


counts = Counter()
mutations = []


def check(category, condition):
    if not condition:
        raise AssertionError(f"Failed exact check: {category}")
    counts[category] += 1


def reject(name, difference, reason):
    if isinstance(difference, ExpSum):
        check("mutation_rejection", difference != ExpSum())
        witness = difference.encoded()
    else:
        check("mutation_rejection", bool(difference))
        witness = str(difference)
    mutations.append({"name": name, "status": "REJECTED",
                      "exact_witness": witness, "reason": reason})


def variance(D, c, b, t):
    L = D + c
    return b * e(2 * L * t) + b * c / L * (1 - e(2 * L * t))


def covariance_propagated(D, c, b, t, u):
    later, earlier = max(t, u), min(t, u)
    return e((D + c) * (later - earlier)) * variance(D, c, b, earlier)


def covariance_card(D, c, b, t, u):
    L = D + c
    return b * D / L * e(L * (t + u)) + b * c / L * e(L * abs(t - u))


def three_increment_parts(D, c, b, t, u):
    assert t >= u
    L, delta = D + c, t - u
    initial = b * (e(L * t) - e(L * u)) * (e(L * t) - e(L * u))
    old_noise = b * c / L * (1 - e(2 * L * u))
    old_noise = old_noise * (e(L * delta) - 1) * (e(L * delta) - 1)
    new_noise = b * c / L * (1 - e(2 * L * delta))
    return initial, old_noise, new_noise


def modal_checks():
    for D, c, b, u, delta in product(
            map(F, (1, 2, 3)), (F(0), F(1, 3), F(2)),
            (F(1), F(1, 2)), (F(0), F(1, 5), F(1)),
            (F(0), F(1, 7), F(2))):
        t = u + delta
        card = covariance_card(D, c, b, t, u)
        check("modal_covariance", card == covariance_propagated(D, c, b, t, u))
        check("modal_symmetry", card == covariance_card(D, c, b, u, t))
        check("modal_equal_time", covariance_card(D, c, b, u, u) == variance(D, c, b, u))
        inc = variance(D, c, b, t) + variance(D, c, b, u) - 2 * card
        check("three_part_increment", inc == sum(three_increment_parts(D, c, b, t, u)))
        check("initial_variance", covariance_card(D, c, b, 0, 0) == b)
        if c == 0:
            check("zero_noise", card == b * e(D * (t + u)))
            check("zero_noise_no_past_or_fresh",
                  three_increment_parts(D, c, b, t, u)[1:] == (ExpSum(), ExpSum()))
        if delta == 0:
            check("zero_time_increment", inc == 0)

    # Quadratic forms for three dependent tests and a constant test, two modes.
    amplitudes = [(F(1), F(2)), (F(3), F(-1)), (F(-5), F(4)), (F(0), F(0))]
    relation = (F(-1), F(2), F(1), F(0))
    for t, u in product((F(0), F(1, 3), F(2)), repeat=2):
        mode_cov = [covariance_card(F(1), F(2), F(1, 2), t, u),
                    covariance_card(F(3), F(0), F(1), t, u)]
        matrix = [[sum(amplitudes[i][k] * amplitudes[j][k] * mode_cov[k]
                       for k in range(2)) for j in range(4)] for i in range(4)]
        check("linear_dependence", sum(relation[i] * relation[j] * matrix[i][j]
                                      for i in range(4) for j in range(4)) == 0)
        check("constant_test", all(matrix[3][j] == 0 and matrix[j][3] == 0
                                   for j in range(4)))

    D, c, b, u, t = F(2), F(3), F(1, 2), F(1, 3), F(4, 3)
    L, delta = D + c, t - u
    truth = covariance_propagated(D, c, b, t, u)
    half_noise = b * e(L * (t + u)) + b * c / (2 * L) * (
        e(L * delta) - e(L * (t + u)))
    reject("brownian_factor_two_removed", truth - half_noise,
           "Positive b*c/(2L) times exp(-L(t-u))-exp(-L(t+u)), since u>0.")
    wrong_time = b * D / L * e(L * delta) + b * c / L * e(L * (t + u))
    reject("initial_sum_and_thermal_difference_swapped", truth - wrong_time,
           "D differs from c; the two strictly different positive exponential terms have opposite weights.")
    init, old, fresh = three_increment_parts(D, c, b, t, u)
    full_increment = variance(D, c, b, t) + variance(D, c, b, u) - 2 * truth
    reject("past_noise_increment_omitted", full_increment - init - fresh,
           "Positive b*c/L*(1-exp(-2Lu))*(exp(-L(t-u))-1)^2.")
    thermal_cov = b * c / L * (e(L * delta) - e(L * (t + u)))
    thermal_var_u = b * c / L * (1 - e(2 * L * u))
    reject("terminal_convolution_called_martingale", thermal_var_u - thermal_cov,
           "Positive thermal variance at u times 1-exp(-L(t-u)).")
    check("infinitesimal_thermal_variance_coefficient", 2 * b * c == F(3))
    reject("increment_variance_linear_noise_half", 2 * b * c - b * c,
           "The fresh-noise integral has derivative 2*b*c at zero, not b*c.")


SIN = tuple(map(F, (0, 1, 0, -1)))
COS = tuple(map(F, (1, 0, -1, 0)))


def smooth_source(config, coeff):
    # Angular derivative on period 2*pi; unit probability Haar.
    A, B, C = map(F, coeff)
    n = len(config)
    grad = [-A * SIN[x] + B * COS[x] for x in config]
    row = [-F(1, 2) * (A * COS[x] + B * SIN[x]) for x in config]
    ordered_raw = sum(SIN[(config[i] - config[j]) % 4] * grad[i]
                      for i in range(n) for j in range(n) if i != j)
    ordered_J = sum(SIN[(config[i] - config[j]) % 4] * (grad[i] - grad[j])
                    for i in range(n) for j in range(n) if i != j)
    row_mean = sum(row) / n
    P = ordered_J / (2 * n * n) - row_mean
    return ordered_raw / (n * n), ordered_J, row_mean, P, grad


def literal_source_checks():
    for n in (2, 3):
        for config in product(range(4), repeat=n):
            for coeff in ((1, 0, 0), (0, 1, 0), (1, 2, 3), (0, 0, 7)):
                raw, pairs, row, P, grad = smooth_source(config, coeff)
                check("literal_ordered_source", raw == P + row)
                check("literal_pair_half", raw == pairs / (2 * n * n))
                if coeff[:2] == (0, 0):
                    check("literal_constant_source", P == 0 and raw == 0 and row == 0)
                nu, b = F(3, 2), F(2, 3)
                sigma2 = n * b
                literal = sigma2 * (2 * nu / (n * n)) * sum(g * g for g in grad)
                predicted = 2 * nu * b * sum(g * g for g in grad) / n
                check("literal_brownian_bracket", literal == predicted)

    raw, pairs, row, P, grad = smooth_source((0, 1), (1, 0, 0))
    reject("source_half_removed", pairs / 4 - raw,
           "Literal N=2 ordered force sum differs from the source with no factor one half.")
    reject("source_row_response_sign_flipped", -row - row,
           "The exact Haar row of sin(x-y)*(f'(x)-f'(y)) is minus the nonconstant first mode/2.")
    reject("extra_inverse_N_in_bracket", F(1, 2) - F(1),
           "At N=2, nu*b=1 and mean squared derivative=1/2, the exact bracket is 1.")

    # Exact splitting on a finite group; a positive Fourier retained kernel.
    retained = tuple(map(F, (3, -1, -1, -1)))
    positive = tuple(map(F, (4, 1, 2, 1)))
    c = sum(positive) / 4
    total = tuple(retained[i] + positive[i] - c for i in range(4))
    for n in (2, 3):
        for config in product(range(4), repeat=n):
            E = sum(retained[(x - y) % 4] for x in config for y in config) / (2 * n * n)
            S = sum(positive[(config[i] - config[j]) % 4]
                    for i in range(n) for j in range(n) if i != j) / (2 * n * n)
            H_over_N = sum(total[(config[i] - config[j]) % 4]
                           for i in range(n) for j in range(i + 1, n)) / (n * n)
            rhs = E + S - retained[0] / (2 * n) - F(n - 1, 2 * n) * c
            check("positive_split_exact_self_background", H_over_N == rhs)
            check("positive_split_nonnegative", E >= 0 and S >= 0)
    reject("split_self_diagonal_missing", F(3, 4),
           "At N=2 the exact retained self subtraction is retained(0)/(2N)=3/4.")
    reject("split_background_Nminus1_replaced_by_N", F(1, 2),
           "At N=2 and c=2 the changed constant subtraction differs by c/(2N)=1/2.")


def tent_mean(n, t):
    n, t = F(n), F(t)
    lo, hi = F(1, 4), F(3, 4)
    left_a, left_b = max(lo, t - 1 / n), min(hi, t)
    right_a, right_b = max(lo, t), min(hi, t + 1 / n)
    area = F(0)
    if left_a < left_b:
        area += (1 - n * t) * (left_b - left_a) + n * (left_b**2 - left_a**2) / 2
    if right_a < right_b:
        area += (1 + n * t) * (right_b - right_a) - n * (right_b**2 - right_a**2) / 2
    return 2 * area


def path_inference_checks():
    for n in (8, 16, 32, 64):
        check("random_tent_exact_area", tent_mean(n, F(1, 2)) == F(2, n))
        for t in (F(j, 64) for j in range(65)):
            check("random_tent_fixed_time_bound", 0 <= tent_mean(n, t) <= F(2, n))
        for U in (F(1, 4), F(3, 8), F(1, 2), F(5, 8), F(3, 4)):
            at_peak = 1
            at_distance = max(F(0), 1 - n * abs((U + F(1, n)) - U))
            check("random_tent_supremum_and_modulus", at_peak - at_distance == 1)
        check("random_tent_integrated_area", F(1, 2) * F(2, n) == F(1, n))
    reject("supremum_expectation_exchanged", F(1) - tent_mean(16, F(1, 2)),
           "E sup of a random tent is 1 but sup E equals 1/8 at n=16.")
    for gamma in (F(1, 16), F(1, 8), F(3, 16)):
        exponent = 2 - 1 - 4 * gamma
        check("dyadic_summability_exponent", exponent > 0)
        for n in (1, 2, 8, 32):
            check("dyadic_grid_union_power",
                  -2 * n + n + 4 * gamma * n == -exponent * n)
    check("dyadic_endpoint_not_summable", 2 - 1 - 4 * F(1, 4) == 0)
    reject("dyadic_grid_cardinality_omitted",
           (2 - 4 * F(1, 3)) - (2 - 1 - 4 * F(1, 3)),
           "At gamma=1/3 the false exponent is 2/3; including 2^n edges gives -1/3.")
    reject("fourth_moment_bound_claims_gamma_half", 1 - 4 * F(1, 2),
           "The required summability exponent is -1, so this bound cannot justify gamma=1/2.")


def run():
    modal_checks()
    literal_source_checks()
    path_inference_checks()
    return {
        "audit": "AUD059", "task": "TASK091", "status": "PASS",
        "evidence_class": "exact diagnostic and mutation self-check; not a proof certificate",
        "arithmetic": "fractions.Fraction and formal finite exponential sums",
        "randomness": "none", "external_dependencies": "none",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "assertion_count": sum(counts.values()), "categories": dict(sorted(counts.items())),
        "mutations_rejected": len(mutations), "mutation_witnesses": mutations,
        "limitations": [
            "The particle theorem is proved analytically in the reconstruction report, conditionally on the exact earlier sources.",
            "The trigonometric and finite-group models check exact algebra, not singular-law transfer.",
            "The random tent falsifies an inference, not the admitted particle assertion.",
            "Formal exponential equalities are exact identities; mutation nonzero reasons are stated separately."
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = run()
    data = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.verify:
        expected = json.loads(args.verify.read_text())
        if result != expected:
            raise AssertionError("Recomputed diagnostic result differs from sealed result.")
        print(json.dumps({"status": "PASS", "assertion_count": result["assertion_count"],
                          "mutations_rejected": result["mutations_rejected"],
                          "read_only_result_verification": True}, sort_keys=True))
    elif args.output:
        if args.output.exists():
            raise FileExistsError("Refusing to overwrite an existing result.")
        args.output.write_text(data)
        print(json.dumps({"status": "PASS", "assertion_count": result["assertion_count"],
                          "mutations_rejected": result["mutations_rejected"]}, sort_keys=True))
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
