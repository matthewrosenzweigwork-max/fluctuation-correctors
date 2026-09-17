#!/usr/bin/env python3
"""Exact finite self-checks for the statement-only Gaussian reconstruction.

These checks concern factors, overlap endpoints, degeneracy, and the free
heat covariance formulas. They do not constitute a CLT proof or an audit of
an unseen constructor. No random sampling or external library is used.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import json


COUNTS = {}


def check(name, actual, expected):
    if actual != expected:
        raise AssertionError((name, actual, expected))
    COUNTS[name] = COUNTS.get(name, 0) + 1


def det(matrix):
    n = len(matrix)
    total = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = F((-1)**inversions)
        for i in range(n):
            term *= matrix[i][perm[i]]
        total += term
    return total


def principal_minors_nonnegative(matrix):
    n = len(matrix)
    for size in range(1, n+1):
        for chosen in combinations(range(n), size):
            minor = [[matrix[i][j] for j in chosen] for i in chosen]
            check("free_heat_nonnegative_principal_minor", det(minor) >= 0, True)


def main():
    # x stands for exp(-nu*omega*time_unit). Its exact algebraic relations
    # are checked; rational x does not purport to approximate a fixed mode.
    for times in ((0, 1, 3), (1, 1, 2), (0, 0, 0), (0, 2, 2, 3)):
        for x in (F(1, 5), F(1, 2), F(1)):
            for beta in (F(1, 7), F(1), F(9)):
                nu = 1/beta
                a_squared = min(beta, F(1))
                c = min(F(1), 1/beta)
                check("temperature_identity", c/nu, a_squared)
                initial = []
                dynamic = []
                combined = []
                for s in times:
                    irow, drow, crow = [], [], []
                    for t in times:
                        overlap = min(s, t)
                        check("unequal_time_overlap_exponent", s+t-2*overlap, abs(s-t))
                        i = a_squared*x**(s+t)/2
                        d = c/nu*(x**(s+t-2*overlap)-x**(s+t))/2
                        covariance = a_squared*x**abs(s-t)/2
                        check("free_heat_covariance_split", i+d, covariance)
                        if s == 0 or t == 0:
                            check("zero_time_dynamic_covariance", d, F(0))
                        if x == 1:
                            check("zero_diffusion_degeneracy", d, F(0))
                        irow.append(i)
                        drow.append(d)
                        crow.append(covariance)
                    initial.append(irow)
                    dynamic.append(drow)
                    combined.append(crow)
                for matrix in (initial, dynamic, combined):
                    principal_minors_nonnegative(matrix)
                for i in range(len(times)):
                    for j in range(i):
                        if times[i] == times[j]:
                            check("duplicate_time_equal_rows", combined[i], combined[j])

    # Complex exponential: the +q/2 finite-variation term cancels the
    # second derivative contribution i^2*dq/2 exactly.
    check("complex_exponential_ito_cancellation", F(1, 2)-F(1, 2), F(0))

    # A diagnostic with random initial variance V=1 or 4: a centered
    # Gaussian conditional on V has fourth moment 3 E[V^2], which differs
    # from that of a fixed-variance Gaussian with variance E[V]. Thus zero
    # initial/martingale covariance alone cannot establish independence.
    mean_variance = F(1+4, 2)
    mixture_fourth = 3*F(1+16, 2)
    gaussian_fourth = 3*mean_variance**2
    check("random_bracket_mixture_diagnostic", mixture_fourth > gaussian_fourth, True)

    print(json.dumps({
        "status": "PASS",
        "total_checks": sum(COUNTS.values()),
        "checks": COUNTS,
        "arithmetic": "exact Fraction/integer; no random seed or tolerance",
        "scope": "same-context finite self-checks; unseen Gaussian proof not reviewed"
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
