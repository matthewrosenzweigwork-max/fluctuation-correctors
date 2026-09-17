#!/usr/bin/env python3
"""Exact self-checks for TASK-010; standard library, no random sampling.

These finite tests support, but do not replace, the universal proofs in
MEMORANDA/ROUND_002_COUPLING.md. Arithmetic is Fraction throughout.
"""

from fractions import Fraction as Q
from itertools import permutations, product
import json


COUNTS = {}
GRID = tuple(range(4))
COS = (Q(1), Q(0), Q(-1), Q(0))
SIN = (Q(0), Q(1), Q(0), Q(-1))
MU = (Q(1, 4),) * 4


def check(name, actual, expected):
    if actual != expected:
        raise AssertionError((name, actual, expected))
    COUNTS[name] = COUNTS.get(name, 0) + 1


def phi(x, y):
    return 1 + COS[x] * COS[y] + COS[(x - y) % 4]


def grad_phi(x, y):
    # The true first derivative divided by 2*pi.
    return -SIN[x] * COS[y] - SIN[(x - y) % 4]


def cubic_actual(x, y, z):
    # K=sin(2*pi*(x-z)); C Phi divided by 2*pi.
    args = (x, y, z)
    return sum(
        (SIN[(args[a] - args[c]) % 4]
         * grad_phi(args[a], args[b])
         for a, b, c in permutations(range(3))), Q(0)) / 6


def cubic_general(x, y, z):
    return (1 + COS[x] * COS[y] + COS[x] * COS[z]
            + COS[y] * COS[z] + COS[x] * COS[y] * COS[z])


def integrate(kernel, measures):
    result = Q(0)
    for positions in product(GRID, repeat=len(measures)):
        weight = Q(1)
        for position, measure in zip(positions, measures):
            weight *= measure[position]
        result += weight * kernel(*positions)
    return result


def check_configuration(xs):
    n = len(xs)
    eta = tuple(Q(xs.count(x), n) for x in GRID)
    rho = tuple(eta[x] - MU[x] for x in GRID)
    for kernel in (lambda x, y, z: Q(1), cubic_general, cubic_actual):
        direct = sum((kernel(xs[i], xs[j], xs[k])
                      for i, j, k in permutations(range(n), 3)), Q(0)) / n**3
        direct -= Q(3, n**2) * sum(
            (sum((kernel(xs[i], xs[j], z) * MU[z] for z in GRID), Q(0))
             for i, j in permutations(range(n), 2)), Q(0))
        direct += Q(3, n) * sum(
            (sum((kernel(x, y, z) * MU[y] * MU[z]
                  for y, z in product(GRID, repeat=2)), Q(0))
             for x in xs), Q(0))
        direct -= integrate(kernel, (MU, MU, MU))
        converted = integrate(kernel, (rho, rho, rho))
        converted -= Q(3, n) * sum(
            (kernel(x, x, y) * eta[x] * rho[y]
             for x, y in product(GRID, repeat=2)), Q(0))
        converted += Q(2, n**2) * sum(
            (kernel(x, x, x) * eta[x] for x in GRID), Q(0))
        check("cubic_diagonal_conversion", direct, converted)

    check("actual_cubic_full_diagonal",
          sum((abs(cubic_actual(x, x, x)) for x in GRID), Q(0)), Q(0))

    direct_pair = sum((phi(xs[i], xs[j])
                       for i, j in permutations(range(n), 2)), Q(0)) / (2*n**2)
    direct_pair -= Q(1, n) * sum(
        (sum((phi(x, y) * MU[y] for y in GRID), Q(0)) for x in xs), Q(0))
    direct_pair += integrate(phi, (MU, MU)) / 2
    converted_pair = integrate(phi, (rho, rho)) / 2
    converted_pair -= sum((phi(x, x) * eta[x] for x in GRID), Q(0)) / (2*n)
    check("pair_diagonal_conversion", direct_pair, converted_pair)

    direct_gradients = []
    roots = []
    for i, x in enumerate(xs):
        derivative = Q(0)
        for a, b in permutations(range(n), 2):
            if a == i:
                derivative += grad_phi(xs[a], xs[b]) / (2*n**2)
            if b == i:
                derivative += grad_phi(xs[b], xs[a]) / (2*n**2)
        derivative -= sum((grad_phi(x, y) * MU[y] for y in GRID), Q(0)) / n
        root = sum((grad_phi(x, y) * rho[y] for y in GRID), Q(0))
        root -= grad_phi(x, x) / n
        check("pair_rooted_gradient", derivative, root / n)
        direct_gradients.append(derivative)
        roots.append(root)

    for nu in (Q(1, 3), Q(1), Q(7)):
        # Both sides omit the same factor (2*pi)^2.
        direct_bracket = 2*nu*sum((z*z for z in direct_gradients), Q(0))
        root_bracket = Q(2, n**2)*nu*sum((z*z for z in roots), Q(0))
        check("pair_bracket_prefactor", direct_bracket, root_bracket)
        direct_cross = 2*nu*sum(
            (-SIN[xs[i]]*direct_gradients[i]/n for i in range(n)), Q(0))
        root_cross = Q(2, n**2)*nu*sum(
            (-SIN[xs[i]]*roots[i] for i in range(n)), Q(0))
        check("cross_bracket_prefactor", direct_cross, root_cross)


def check_iid_moments(n):
    # This four-atom cosine law has exactly the Haar cosine first through
    # fourth moments used in the analytic Fourier calculations. All sums
    # below are exact finite expectations, not Monte Carlo.
    values = (Q(-1), Q(-1, 2), Q(1, 2), Q(1))
    probabilities = (Q(1, 6), Q(1, 3), Q(1, 3), Q(1, 6))
    pair_second = cubic_second = bracket_root_second = Q(0)
    cross_mean = cross_second = Q(0)
    for indices in product(range(4), repeat=n):
        xs = tuple(values[i] for i in indices)
        weight = Q(1)
        for i in indices:
            weight *= probabilities[i]
        pair = sum((xs[i]*xs[j] for i, j in permutations(range(n), 2)), Q(0)) / (2*n**2)
        cubic = sum((xs[i]*xs[j]*xs[k]
                     for i, j, k in permutations(range(n), 3)), Q(0)) / n**3
        z = sum(((1-xs[i]**2)*xs[j]
                 for i, j in permutations(range(n), 2)), Q(0)) / n**2
        root_average = sum(
            ((1-xs[i]**2)*(sum((xs[j] for j in range(n) if j != i), Q(0))/n)**2
             for i in range(n)), Q(0)) / n
        pair_second += weight*pair**2
        cubic_second += weight*cubic**2
        cross_mean += weight*z
        cross_second += weight*z**2
        bracket_root_second += weight*root_average
    check("iid_pair_second_moment", pair_second, Q(n-1, 8*n**3))
    check("iid_cubic_second_moment", cubic_second,
          Q(6*n*(n-1)*(n-2), 8*n**6))
    check("iid_pair_bracket_root_moment", bracket_root_second, Q(n-1, 4*n**2))
    check("iid_cross_signed_mean", cross_mean, Q(0))
    check("iid_cross_second_moment", cross_second, Q((n-1)*(2*n-1), 16*n**3))


def main():
    for n in (2, 3):
        for xs in product(GRID, repeat=n):
            check_configuration(xs)
    for xs in ((0, 1, 2, 3, 0), (1, 1, 1, 1, 1), (0, 2, 0, 2, 1)):
        check_configuration(xs)
    for n in (2, 3, 4, 5):
        check_iid_moments(n)
        for beta in (Q(1, 100), Q(1), Q(100)):
            sigma_squared = n*min(beta, Q(1))
            check("temperature_prefactor", sigma_squared/(beta*n**2),
                  min(Q(1), 1/beta)/n)
        check("constant_pair", Q(n*(n-1), n**2)-2+1, -Q(1, n))
        check("constant_cubic",
              Q(n*(n-1)*(n-2), n**3)-3*Q(n*(n-1), n**2)+3-1,
              Q(2, n**2))
    for d in range(1, 101):
        q = d//2+2
        check("regularity_order", 3*q+1 <= 4*d+12, True)
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "exact Fraction; no tolerance or random seed",
        "total_equalities": sum(COUNTS.values()),
        "checks": COUNTS,
        "scope": "same-context finite self-checks; not an independent audit"
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
