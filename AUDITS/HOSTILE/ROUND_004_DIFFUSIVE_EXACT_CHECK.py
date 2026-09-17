#!/usr/bin/env python3
"""TASK-035 exact finite checks; supplementary evidence, not an SDE proof.

Python standard library only. All arithmetic is Fraction/integer arithmetic.
There is no random seed, floating tolerance, simulation, or numerical limit.
The independently written chain-rule expressions are compared with D5-D8,
D13-D14, D29, and the scaling exponents of the sealed submitted proof.
"""

from fractions import Fraction as Q
from itertools import product
from math import gcd


def integer_root(value, degree):
    assert value >= 0 and degree >= 1
    lo, hi = 0, max(1, value)
    while lo <= hi:
        mid = (lo + hi) // 2
        power = mid**degree
        if power == value:
            return mid
        if power < value:
            lo = mid + 1
        else:
            hi = mid - 1
    raise AssertionError(("not an exact integer power", value, degree))


def exact_power(value, exponent):
    value, exponent = Q(value), Q(exponent)
    assert value > 0
    base = Q(integer_root(value.numerator, exponent.denominator),
             integer_root(value.denominator, exponent.denominator))
    return base**exponent.numerator


def lcm(a, b):
    return a * b // gcd(a, b)


exponents = [Q(1, 4), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5, 2),
             Q(3), Q(7, 2), Q(4), Q(5), Q(6), Q(7), Q(8)]
radial_count = 0
strict_count = 0
for d in range(3, 11):
    for s in exponents:
        if s > d - 2:
            continue
        p, gamma = s + 2, s / (s + 2)
        # The two independent expressions for the derivative coefficient.
        assert gamma * s + s == gamma * (2 * s + 2)
        assert d - s - 2 >= 0
        for n in [2, 3, 17, 127]:
            for base in [Q(1, 3), Q(1), Q(2)]:
                r = base**s.denominator
                for increment in [Q(0), Q(1, 2), Q(2)]:
                    end_r = (base + increment)**s.denominator
                    a = exact_power(end_r, p) - exact_power(r, p)
                    tau = Q(n) * a / (2 * s * p)
                    profile = Q(n, 4) * (end_r**2 - r**2)
                    f_tau = s * exact_power(end_r, -s)
                    # Direct differentiation of the endpoint-radius formula.
                    f_r = Q(n, 2) * (
                        exact_power(r, p - 1) * exact_power(end_r, -s) - r)
                    f_rr = Q(n, 2) * (
                        (p - 1) * exact_power(r, p - 2) * exact_power(end_r, -s)
                        - s * exact_power(r, 2 * p - 2)
                        * exact_power(end_r, -s - p) - 1)
                    lap_chain = f_rr + Q(d - 1) * f_r / r
                    q = exact_power(r, p) / exact_power(end_r, p)
                    lap_submitted = Q(n, 2) * (
                        exact_power(q, gamma) * (d + s - s * q) - d)
                    source = s * exact_power(r, -s)
                    assert -f_tau + Q(2) * s / n * exact_power(r, -s - 1) * f_r == -source
                    assert lap_chain == lap_submitted
                    assert -Q(n * d, 2) <= lap_chain <= 0
                    assert 0 <= profile <= tau * source
                    if tau == 0:
                        assert profile == 0 and lap_chain == 0
                    else:
                        assert lap_chain < 0
                        # Concavity bound, raised to integer powers exactly.
                        numerator, denominator = p.numerator, p.denominator
                        assert (end_r**2 - r**2)**numerator <= a**(2 * denominator)
                        strict_count += 1
                    for nu in [Q(0), Q(1, 1000000), Q(1), Q(10**12)]:
                        backward_generator = -source + 2 * nu * lap_chain
                        assert backward_generator <= -source
                    radial_count += 1


lyapunov_count = 0
for d in range(3, 11):
    for s in exponents:
        if s > d - 2:
            continue
        for n in [2, 3, 127]:
            eta = Q(d - 2)
            stationary_y = eta * (s + d) / (2 * s)
            aa, bb = 4 * s / n, 2 * s * eta / n
            assert -s * aa + (s + d) * bb / stationary_y == 0
            assert aa - bb / stationary_y == 4 * s * d / (n * (s + d))
            for eta in [Q(1, 2), Q(1), Q(2), Q(d - 2)]:
                for base in [Q(1, 3), Q(1), Q(2)]:
                    r = base**lcm(s.denominator, eta.denominator)
                    first = 2 * r - eta * exact_power(r, -eta - 1)
                    second = 2 + eta * (eta + 1) * exact_power(r, -eta - 2)
                    radial_lap = second + Q(d - 1) * first / r
                    for nu in [Q(0), Q(1), Q(10**12)]:
                        direct = 2 * nu * radial_lap + 2 * s / n * exact_power(r, -s - 1) * first
                        submitted = (4 * nu * d + 4 * s / n * exact_power(r, -s)
                                     + 2 * nu * eta * (eta - d + 2) * exact_power(r, -eta - 2)
                                     - 2 * s * eta / n * exact_power(r, -eta - s - 2))
                        assert direct == submitted
                        if eta == d - 2:
                            assert radial_lap == 2 * d
                        lyapunov_count += 1


prob = [Q(1, 2), Q(1, 3), Q(1, 6)]
f = [Q(1), Q(-1), Q(-1)]
q0 = [Q(1), Q(2), Q(-7)]
assert sum(prob[i] * f[i] for i in range(3)) == 0
assert sum(prob[i] * q0[i] for i in range(3)) == 0
kernels = {
    "zero": [[Q(0) for _ in range(3)] for _ in range(3)],
    "constant": [[Q(3) for _ in range(3)] for _ in range(3)],
    "separable": [[3 + q0[i] + q0[j] for j in range(3)] for i in range(3)],
    "canonical": [[f[i] * f[j] for j in range(3)] for i in range(3)],
    "mixed": [[3 + q0[i] + q0[j] + f[i] * f[j] for j in range(3)] for i in range(3)],
    "general": [[Q(3), Q(-2), Q(1)], [Q(-2), Q(5), Q(4)], [Q(1), Q(4), Q(-1)]],
}
iid_cases, iid_configurations = 0, 0
for name, h in kernels.items():
    hm = [sum(h[i][j] * prob[j] for j in range(3)) for i in range(3)]
    mean = sum(prob[i] * hm[i] for i in range(3))
    projection = [hm[i] - mean for i in range(3)]
    canonical = [[h[i][j] - mean - projection[i] - projection[j]
                  for j in range(3)] for i in range(3)]
    norm = sum(prob[i] * prob[j] * h[i][j]**2 for i, j in product(range(3), repeat=2))
    qnorm = sum(prob[i] * projection[i]**2 for i in range(3))
    rnorm = sum(prob[i] * prob[j] * canonical[i][j]**2 for i, j in product(range(3), repeat=2))
    assert norm == mean**2 + 2 * qnorm + rnorm
    for n in [2, 3, 4, 5]:
        first_moment, second_moment = Q(0), Q(0)
        for configuration in product(range(3), repeat=n):
            weight = Q(1)
            for x in configuration:
                weight *= prob[x]
            ordered_sum = sum(h[configuration[i]][configuration[j]]
                              for i in range(n) for j in range(n) if i != j)
            direct = (ordered_sum / n**2
                      - Q(2, n) * sum(hm[x] for x in configuration) + mean) / 2
            decomposed = (-mean / (2 * n)
                          - sum(projection[x] for x in configuration) / n**2
                          + sum(canonical[configuration[i]][configuration[j]]
                                for i in range(n) for j in range(i + 1, n)) / n**2)
            assert direct == decomposed
            first_moment += weight * direct
            second_moment += weight * direct**2
            iid_configurations += 1
        claimed = mean**2 / (4 * n**2) + qnorm / n**3 + Q(n - 1, 2 * n**3) * rnorm
        sharp_bound = Q(n - 1, 2 * n**3) * norm
        assert first_moment == -mean / (2 * n)
        assert second_moment == claimed <= sharp_bound
        if name == "canonical" or n == 2:
            assert second_moment == sharp_bound
        iid_cases += 1


scaling_cases = 0
regimes = set()
for d in range(3, 11):
    for s in exponents:
        if s > d - 2:
            continue
        p = s + 2
        assert 2 - Q(d + 4) / p == (2 * s - d) / p
        assert (2 * s - d) / p - 1 == -(d + 2 - s) / p
        assert (d + 2 - s) / p > 0
        if 2 * s == d:
            assert Q(d + 4) / p == 2
            regimes.add("2s=d")
        else:
            regimes.add("2s<d" if 2 * s < d else "2s>d")
        scaling_cases += 1

assert regimes == {"2s<d", "2s=d", "2s>d"}
print("PASS: TASK-035 independent exact arithmetic battery")
print("Arithmetic: Python integers and fractions.Fraction only; no floating-point tolerance.")
print("Randomness: none; no seed, sampling, stochastic simulation, or convergence claim.")
print(f"Radial/time/barrier tuples: {radial_count}; positive-time strict Laplacian tuples: {strict_count}.")
print("Radial N values: 2, 3, 17, 127; dimensions 3 through 10; 13 candidate rational s values filtered by 0<s<=d-2.")
print("Diffusivity test values: 0, 1/1000000, 1, 1000000000000 (all finite).")
print(f"Lyapunov chain-rule tuples: {lyapunov_count}; harmonic exponent and exact stationary-point coefficients checked.")
print(f"Iid kernel/N cases: {iid_cases}; exhaustive three-point configurations: {iid_configurations}.")
print("Iid law: masses 1/2, 1/3, 1/6; six symmetric kernels; N=2,3,4,5; spatial coincidences retained for distinct labels.")
print(f"Scaling tuples: {scaling_cases}; all three 2s versus d regimes represented.")
print("Scope: finite exact algebra checks support the written all-parameter audit; they do not establish SDE existence, stochastic limits, or PDE regularity.")
