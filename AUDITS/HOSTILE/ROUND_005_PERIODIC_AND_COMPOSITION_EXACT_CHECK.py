#!/usr/bin/env python3
"""TASK-041 independent exact tests; finite evidence, not a proof certificate.

Only Python's standard library is used. No source input is modified. The
independent routes are formal radial time coefficients, exact core bounds,
complete finite-space iid enumeration, and a signed, noncommuting response
model with an exact piecewise-polynomial solution.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import ceil, factorial, isqrt
from pathlib import Path
import json


counts = defaultdict(int)


def verify(assertion, group):
    if not assertion:
        raise AssertionError(group)
    counts[group] += 1


def binomial(a, k):
    result = Q(1)
    for j in range(k):
        result *= (a - j) / (j + 1)
    return result


def qpower(base, exponent):
    exponent = Q(exponent)
    if exponent.denominator == 1:
        return base ** exponent.numerator
    assert exponent.denominator == 2
    numerator = isqrt(base.numerator)
    denominator = isqrt(base.denominator)
    assert numerator * numerator == base.numerator
    assert denominator * denominator == base.denominator
    return Q(numerator, denominator) ** exponent.numerator


# Directly expand (N/4) r^2 [(1 + 2sp tau/(N r^p))^(2/p) - 1].
# Coefficients carry their own radial powers; no submitted derivative formula
# or checker routine is called.
for s in (Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5, 2), Q(3), Q(4)):
    p = s + 2
    for d in (ceil(p), ceil(p) + 1, ceil(p) + 2):
        for n in (2, 3, 17):
            coefficient = {
                k: Q(n, 4) * binomial(2 / p, k) * (2 * s * p / n) ** k
                for k in range(1, 9)
            }
            verify(coefficient[1] == s, 'radial_formal_coefficients')
            for k in range(1, 8):
                verify((k + 1) * coefficient[k + 1]
                       == (2 * s / n) * (2 - p * k) * coefficient[k],
                       'radial_formal_coefficients')
            first_laplacian = coefficient[1] * (2 - p) * (d - p)
            verify(first_laplacian <= 0, 'laplacian_threshold')
            if d == p:
                second_laplacian = coefficient[2] * (2 - 2 * p) * (d - 2 * p)
                verify(first_laplacian == 0 and second_laplacian < 0,
                       'laplacian_threshold')
            harmonic_power = 2 - d
            verify(harmonic_power * (harmonic_power + d - 2) == 0,
                   'relative_generator')
            verify((2 * s / n) * harmonic_power == -2 * s * (d - 2) / n,
                   'relative_generator')
            for nu in (Q(0), Q(1, 7), Q(13)):
                verify(2 * nu * 2 * (2 + d - 2) == 4 * nu * d,
                       'relative_generator')
                verify((2 * s / n) * 2 == 4 * s / n,
                       'relative_generator')

    # This excluded-range test must have the opposite small-time sign.
    if p > 3:
        verify(s * (2 - p) * (3 - p) > 0, 'excluded_range_negative_control')

    radius = Q(1, 4) ** s.denominator
    for n in (2, 3, 17):
        for ell in (radius / 16, radius, radius * 16):
            tau = n * qpower(ell, p) / (2 * s * p)
            for d in (ceil(p), ceil(p) + 1, ceil(p) + 2):
                a0 = (2 * s * p) ** 2 / (16 * d)
                core = Q(n * n, 16 * d) * ell ** 4 * min(radius, ell) ** d
                rewritten = a0 * tau ** 2 * qpower(ell, -2 * s) * min(radius, ell) ** d
                verify(core == rewritten, 'all_n_core_and_tail')
                delta = d - 2 * s
                if delta > 0:
                    tail = (s * s * tau * tau
                            * (qpower(radius, delta) - qpower(ell, delta)) / delta
                            if ell < radius else Q(0))
                    upper = tau * tau * qpower(radius, delta) * (a0 + s * s / delta)
                    verify(core + tail <= upper, 'all_n_core_and_tail')
                elif delta < 0:
                    kappa = -delta
                    tail = (s * s * tau * tau
                            * (qpower(ell, -kappa) - qpower(radius, -kappa)) / kappa
                            if ell < radius else Q(0))
                    upper = tau * tau * qpower(ell, -kappa) * (a0 + s * s / kappa)
                    verify(core + tail <= upper, 'all_n_core_and_tail')
                    verify(2 - kappa / p == Q(d + 4) / p, 'threshold_exponents')
                else:
                    # The tail is s^2 tau^2 log_+(R/ell); its coefficient is
                    # exact. This check addresses the core on both sides of R.
                    verify(core <= a0 * tau * tau, 'all_n_core_and_tail')
                verify((2 * s - d) / p - 1 == -(d + 2 - s) / p,
                       'threshold_exponents')


def iid_statistics(probability, kernel, n):
    states = range(len(probability))
    marginal = [sum(probability[j] * kernel[i][j] for j in states) for i in states]
    theta = sum(probability[i] * marginal[i] for i in states)
    h = [value - theta for value in marginal]
    canonical = [[kernel[i][j] - theta - h[i] - h[j] for j in states] for i in states]
    h2 = sum(probability[i] * h[i] ** 2 for i in states)
    canonical2 = sum(probability[i] * probability[j] * canonical[i][j] ** 2
                     for i in states for j in states)
    kernel2 = sum(probability[i] * probability[j] * kernel[i][j] ** 2
                  for i in states for j in states)
    moment1 = Q(0)
    moment2 = Q(0)
    for sample in product(states, repeat=n):
        weight = Q(1)
        for value in sample:
            weight *= probability[value]
        ordered = sum(kernel[sample[i]][sample[j]]
                      for i in range(n) for j in range(n) if i != j)
        statistic = (ordered / (2 * n * n)
                     - sum(marginal[value] for value in sample) / n + theta / 2)
        decomposition = (-theta / (2 * n)
                         - sum(h[value] for value in sample) / (n * n)
                         + sum(canonical[sample[i]][sample[j]]
                               for i in range(n) for j in range(i + 1, n)) / (n * n))
        verify(statistic == decomposition, 'iid_configuration_identities')
        moment1 += weight * statistic
        moment2 += weight * statistic ** 2
    verify(moment1 == -theta / (2 * n), 'iid_exact_moments')
    verify(moment2 == theta ** 2 / (4 * n * n) + h2 / n ** 3
           + Q(n - 1, 2 * n ** 3) * canonical2, 'iid_exact_moments')
    verify(kernel2 == theta ** 2 + 2 * h2 + canonical2, 'iid_exact_moments')
    verify(moment2 <= Q(n - 1, 2 * n ** 3) * kernel2, 'iid_exact_moments')
    if n == 2:
        verify(moment2 == Q(n - 1, 2 * n ** 3) * kernel2, 'iid_exact_moments')
    return moment2, kernel2


for probability in ((Q(1, 2), Q(1, 3), Q(1, 6)),
                    (Q(1, 4), Q(3, 4), Q(0))):
    a = [Q(-2), Q(1), Q(4)]
    mean_a = sum(probability[i] * a[i] for i in range(3))
    centered = [value - mean_a for value in a]
    kernels = [
        [[Q(2) for _ in range(3)] for _ in range(3)],
        [[a[i] + a[j] for j in range(3)] for i in range(3)],
        [[centered[i] * centered[j] for j in range(3)] for i in range(3)],
        [[Q(-3), Q(1), Q(5)], [Q(1), Q(2), Q(-2)], [Q(5), Q(-2), Q(7)]],
    ]
    for kernel in kernels:
        for n in (2, 3, 4):
            iid_statistics(probability, kernel, n)

# A measurable four-cell torus model witnesses the need for the square of the
# density bound. A single density factor would fail the relaxed N=3 estimate.
probability = (Q(1, 2), Q(1, 2), Q(0), Q(0))
haar = (Q(1, 4),) * 4
a = (Q(1), Q(-1), Q(0), Q(0))
kernel = [[a[i] * a[j] for j in range(4)] for i in range(4)]
moment, mu_norm2 = iid_statistics(probability, kernel, 3)
haar_norm2 = sum(haar[i] * haar[j] * kernel[i][j] ** 2
                 for i in range(4) for j in range(4))
density_bound = Q(2)
verify(mu_norm2 == density_bound ** 2 * haar_norm2 == 1, 'density_factor_sharpness')
verify(3 * moment == Q(1, 9), 'density_factor_sharpness')
verify(3 * moment > density_bound * haar_norm2 / 6, 'density_factor_sharpness')
verify(3 * moment <= density_bound ** 2 * haar_norm2 / 6, 'density_factor_sharpness')


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(a, x):
    return tuple(a * b for b in x)


def apply(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(2)) for row in matrix)


# Identity base evolution on a constant continuous process. On two equal-Haar
# pair-exchange-invariant cells, A and B are bounded finite-rank responses.
# They are signed, square-zero, and generally do not commute.
noncommuting_witnesses = 0
for a, b in product((Q(-2), Q(-1, 3), Q(1, 2), Q(3)), repeat=2):
    A = ((Q(0), a), (Q(0), Q(0)))
    B = ((Q(0), Q(0)), (b, Q(0)))
    for source in ((Q(1), Q(2)), (Q(-3), Q(1, 5))):
        for h in (Q(1, 2), Q(1), Q(3, 2)):
            # R=B on [h,2h], and R=A on [0,h].
            def late(tau):
                return add(scale(tau, source), scale(tau * tau / 2, apply(B, source)))

            midpoint = late(h)
            for r in (Q(0), h / 3, h):
                early = add(add(midpoint, scale(r, add(source, apply(A, midpoint)))),
                            scale(r * r / 2, apply(A, source)))
                derivative = add(add(source, apply(A, midpoint)), scale(r, apply(A, source)))
                verify(derivative == add(source, apply(A, early)), 'response_polynomial_ode')
                integrated_early_response = add(scale(r, apply(A, midpoint)),
                                                 scale(r * r / 2, apply(A, source)))
                integrated_late_response = scale(h * h / 2, apply(B, source))
                mild_rhs = add(scale(h + r, source),
                               add(integrated_early_response, integrated_late_response))
                verify(early == mild_rhs, 'response_mild_and_martingale')
                if r == 0:
                    verify(early == midpoint, 'response_mild_and_martingale')
                for tau in (Q(0), h / 4, h):
                    verify(add(source, scale(tau, apply(B, source)))
                           == add(source, apply(B, late(tau))), 'response_polynomial_ode')
                chronological = apply(A, apply(B, source))
                reversed_order = apply(B, apply(A, source))
                if r > 0 and chronological != reversed_order:
                    noncommuting_witnesses += 1
    verify(apply(A, apply(A, (Q(1), Q(1)))) == (0, 0), 'response_nilpotence')
    verify(apply(B, apply(B, (Q(1), Q(1)))) == (0, 0), 'response_nilpotence')
verify(noncommuting_witnesses > 0, 'response_order_negative_control')

for k in range(13):
    coefficient = Q(1)
    for j in range(1, k + 1):
        coefficient /= j
    verify(coefficient == Q(1, factorial(k)), 'time_simplex_coefficients')
    for c in (Q(0), Q(1, 7), Q(13)):
        times = [Q(j, k + 2) for j in range(k + 2)]
        exponent = sum(c * (times[j + 1] - times[j]) for j in range(k + 1))
        verify(exponent == c * (times[-1] - times[0]), 'time_simplex_exponent')

result = {
    'status': 'PASS: all independent exact checks passed',
    'evidence_label': 'finite exact checks; analytic parameter-uniform proof reviewed separately',
    'arithmetic': 'Python standard-library Fraction; no floating point, random seed, or dependency',
    'counts': dict(sorted(counts.items())),
    'total_assertions': sum(counts.values()),
    'noncommuting_order_witnesses': noncommuting_witnesses,
    'density_negative_control': {
        'density_bound': str(density_bound),
        'haar_pair_norm_squared': str(haar_norm2),
        'initial_law_pair_norm_squared': str(mu_norm2),
        'N_3_scaled_second_moment_b_equals_1': str(3 * moment),
        'incorrect_single_density_factor_relaxed_bound': str(density_bound * haar_norm2 / 6),
        'interpretation': 'confirms why the submitted squared density factor is necessary',
    },
    'scope': 'THM023 algebra and all-N rates; THM024 conditional response/iid implication only',
}
output = Path(__file__).with_name('ROUND_005_PERIODIC_AND_COMPOSITION_EXACT_CHECK.json')
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
