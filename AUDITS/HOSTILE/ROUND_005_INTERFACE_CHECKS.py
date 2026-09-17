#!/usr/bin/env python3
"""TASK044 independent finite tests. Standard library only; no random sampling.

Exact rational iid tests use the defining ordered deleted-label statistic.
Floating-point Fourier tests are diagnostics, not analytic certification.
The source manifest is checked again before any test is run.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import platform

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('ROUND_005_INTERFACE_CHECK_RESULTS.json')
manifest = Path(__file__).with_name('ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt')
verified = []
for line in manifest.read_text().splitlines():
    expected, name = line.split(None, 1)
    name = name.strip()
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected, (name, actual, expected)
    verified.append(name)

p = (F(1, 2), F(1, 3), F(1, 6))
z = (F(-1), F(0), F(3))
assert sum(p[i] * z[i] for i in range(3)) == 0
kernels = {
    'constant': tuple(tuple(F(7) for j in range(3)) for i in range(3)),
    'additive': tuple(tuple(z[i] + z[j] for j in range(3)) for i in range(3)),
    'canonical': tuple(tuple(z[i] * z[j] for j in range(3)) for i in range(3)),
    'mixed_matrix': ((F(2), F(-3), F(5)), (F(-3), F(7), F(1)), (F(5), F(1), F(-4))),
    'orthogonal_mixture': tuple(tuple(F(2) + 2*z[i] + 2*z[j] + z[i]*z[j]
                                     for j in range(3)) for i in range(3)),
}
iid_records = []
for name, kernel in kernels.items():
    rows = [sum(p[j] * kernel[i][j] for j in range(3)) for i in range(3)]
    theta = sum(p[i] * rows[i] for i in range(3))
    h = [rows[i] - theta for i in range(3)]
    H = [[kernel[i][j] - theta - h[i] - h[j] for j in range(3)] for i in range(3)]
    h2 = sum(p[i]*h[i]**2 for i in range(3))
    H2 = sum(p[i]*p[j]*H[i][j]**2 for i in range(3) for j in range(3))
    phi2 = sum(p[i]*p[j]*kernel[i][j]**2 for i in range(3) for j in range(3))
    assert phi2 == theta**2 + 2*h2 + H2
    for N in (2, 3, 4, 5):
        mean = F(0)
        second = F(0)
        for sample in product(range(3), repeat=N):
            weight = math.prod(p[i] for i in sample)
            # Defining statistic; no Hoeffding expansion is used here.
            pair_sum = sum(kernel[sample[i]][sample[j]] for i in range(N)
                           for j in range(N) if i != j)
            P = pair_sum/F(2*N*N) - sum(rows[x] for x in sample)/N + theta/2
            mean += weight*P
            second += weight*P*P
        target = theta**2/F(4*N*N) + h2/F(N**3) + F(N-1, 2*N**3)*H2
        sharp_bound = F(N-1, 2*N**3)*phi2
        assert mean == -theta/F(2*N)
        assert second == target
        assert second <= sharp_bound
        if N == 2 or name == 'canonical':
            assert second == sharp_bound
        for b in (F(1, 7), F(1)):
            assert N*b*second <= b*F(N-1, 2*N*N)*phi2 <= b*phi2/F(2*N)
        iid_records.append({'kernel': name, 'N': N, 'mean': str(mean),
                            'second_moment': str(second), 'sharp_bound': str(sharp_bound)})

# An exact atomless bounded-density example verifies the squared density factor.
# mu=2 on a half-volume set A, Phi=1_(A x A).
weighted_square, haar_square, M0 = F(1), F(1, 4), F(2)
assert weighted_square == M0**2 * haar_square
assert weighted_square > M0 * haar_square

configs = [(3, 1.0), (4, 2.0), (5, 1.25), (7, 5.0)]
fourier_error = 0.0
normalization_error = 0.0
coulomb_error = 0.0
ode_error = 0.0
fourier_cases = 0
for d, s in configs:
    c = math.pi**(s-d/2) * math.gamma((d-s)/2)/math.gamma(s/2)
    alpha = (d-s)/2
    heat_prefactor = c*(4*math.pi**2)**alpha/math.gamma(alpha)
    euclidean_integral_coefficient = 2**(s-d)*math.pi**(-d/2)*math.gamma(s/2)
    normalization_error = max(normalization_error, abs(heat_prefactor*euclidean_integral_coefficient-1))
    if s == d-2:
        cd = (d-2)*2*math.pi**(d/2)/math.gamma(d/2)
        coulomb_error = max(coulomb_error, abs(4*math.pi**2*c-cd)/cd)
    eps = 0.003
    cosine_coeff = {j: 2*c*j**(s-d)*math.exp(-4*math.pi**2*eps*j*j) for j in range(1, 5)}
    for m in range(1, 5):
        for x in (0.07, 0.23, 0.51):
            integral = 0.0
            Q = 1024
            for q in range(Q):
                w = (q+0.5)/Q
                K = sum(2*math.pi*j*a*math.sin(2*math.pi*j*w) for j,a in cosine_coeff.items())
                grad_f = -2*math.pi*m*math.sin(2*math.pi*m*(x+w))
                integral += K*grad_f/Q
            predicted = -4*math.pi**2*m*m*(cosine_coeff[m]/2)*math.cos(2*math.pi*m*x)
            err = abs(integral-predicted)/max(1.0, abs(predicted))
            fourier_error = max(fourier_error, err)
            assert err < 2e-12
            fourier_cases += 1
        for nu in (0.0, 0.25, 7.0):
            gamma = 4*math.pi**2*c*m**(s+2-d)
            a = 4*math.pi**2*nu*m*m + gamma
            assert a > 0
            for t in (0.0, 0.3, 0.7):
                amp = math.exp(-a*(0.7-t))
                dt, diffusion, response = a*amp, -4*math.pi**2*nu*m*m*amp, -gamma*amp
                err = abs(dt+diffusion+response)/max(1.0, abs(dt))
                ode_error = max(ode_error, err)
                assert err < 2e-14
                assert 0 <= amp <= 1
assert normalization_error < 2e-14
assert coulomb_error < 2e-14

# Every tested positive-power regime has a positive endpoint decay exponent.
rate_records = []
for d in range(3, 13):
    for j in range(1, 2*(d-2)+1):
        s = F(j, 2)
        critical_beta_power = 1-s/d
        assert critical_beta_power > 0
        assert critical_beta_power + 2*s/d-1 == s/d > 0
        if 2*s > d:
            decay = (d+2-s)/(s+2)
            assert decay > 0 and d+2-s >= 4
            assert (2*s-d)/(s+2)-1 == -decay
            rate_records.append({'d': d, 's': str(s), 'decay': str(decay)})
# This source-independent example distinguishes the three regime statements.
d, s = F(6), F(4)
assert s/d-1 < 0 < 2*s/d-1  # beta=1: subcritical, old floor fails.
assert -1+s/d-1 < 0          # beta=N^-1: subcritical, nu=N unbounded.

# Scalar bounded-response Volterra model: S=I, J=j, R=r.
# Its terminal-zero solution is j*(exp(r*(T-t))-1)/r.
volterra_error = 0.0
for r in (0.0, 0.2, 3.0):
    j, T = 1.3, 0.7
    for t in (0.0, 0.3, T):
        tau = T-t
        exact = j*tau if r == 0 else j*math.expm1(r*tau)/r
        series = sum(j*(r**n)*(tau**(n+1))/math.factorial(n+1) for n in range(40))
        volterra_error = max(volterra_error, abs(exact-series))
        assert abs(exact-series) < 2e-13
        assert abs(exact) <= j*T*math.exp(r*T) + 1e-14

results = {
    'status': 'PASS',
    'scope': 'Finite exact and floating-point diagnostics only; analytic arguments are in the review.',
    'python': platform.python_version(),
    'random_seed': None,
    'dependencies': 'Python standard library only',
    'verified_input_count': len(verified),
    'verified_inputs': verified,
    'iid_arithmetic': 'Exact rational exhaustive enumeration on three-point iid laws; spatial collisions retained.',
    'iid_case_count': len(iid_records),
    'iid_cases': iid_records,
    'density_factor': {'M0': '2', 'weighted_square': '1', 'haar_square': '1/4', 'squared_factor_required': True},
    'fourier_quadrature': {'case_count': fourier_cases, 'nodes': 1024, 'cutoff': 0.003,
                           'maximum_relative_or_absolute_error': fourier_error,
                           'precision': 'IEEE binary64', 'tolerance': 2e-12},
    'heat_normalization_maximum_error': normalization_error,
    'coulomb_constant_maximum_relative_error': coulomb_error,
    'backward_ode_maximum_relative_or_absolute_error': ode_error,
    'exact_rate_case_count': len(rate_records),
    'exact_rate_cases': rate_records,
    'scalar_volterra_maximum_absolute_error': volterra_error,
}
OUT.write_text(json.dumps(results, indent=2, sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in results.items() if k not in ('iid_cases','exact_rate_cases','verified_inputs')}, indent=2, sort_keys=True))
