#!/usr/bin/env python3
"""Exact arithmetic support for the independent Round 004 reconstruction.

No simulation, floating-point approximation, external dependency, or theorem
certification is performed. The memorandum contains the parameter-uniform proof.
"""
from fractions import Fraction as Q
from math import ceil, lcm
import json
from pathlib import Path


def rational_power(k, common_denominator, exponent):
    power = Q(exponent) * common_denominator
    assert power.denominator == 1
    return Q(k) ** power.numerator


radial_checks = 0
angular_checks = 0
lyapunov_checks = 0
scale_checks = 0
exponent_checks = 0
parameters = []
for s in (Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3), Q(4)):
    p = s + 2
    for d in (ceil(p), ceil(p) + 1):
        assert d >= p and d >= 3
        assert Q(2 * s - d, p) - 1 == -Q(d + 2 - s, p)
        assert Q(d + 2 - s, p) > 0
        assert d + 4 == 2 * p + d - 2 * s
        exponent_checks += 1
        parameters.append({'s': str(s), 'd': d, 'threshold': d == p})
        for n in (2, 3, 17):
            for k in (1, 2, 3):
                # r=1, endpoint radius U=k**den(s). All powers are rational.
                den = s.denominator
                u = Q(k) ** den
                w = rational_power(k, den, p)
                u_minus_s = rational_power(k, den, -s)
                u_minus_2s_2 = rational_power(k, den, -2 * s - 2)
                tau = Q(n) * (w - 1) / (2 * s * p)
                f = s
                profile = Q(n, 4) * (u * u - 1)
                time_derivative = Q(n, 4) * (Q(2) / p) * u_minus_s * (2 * s * p / n)
                first_derivative = Q(n, 4) * ((Q(2) / p) * u_minus_s * p - 2)
                second_derivative = Q(n, 4) * (
                    (Q(2) / p) * (
                        (Q(2) / p - 1) * u_minus_2s_2 * p * p
                        + u_minus_s * p * (p - 1)
                    ) - 2
                )
                laplacian_direct = second_derivative + (d - 1) * first_derivative
                q = 1 / w
                laplacian_seed = Q(n, 2) * (u_minus_s * (d + s - s * q) - d)
                assert laplacian_direct == laplacian_seed
                assert time_derivative - (2 * s / n) * first_derivative == f
                assert -Q(n * d, 2) <= laplacian_direct <= 0
                assert d + s - (2 * s + 2) * q >= 0
                if tau == 0:
                    assert profile == first_derivative == laplacian_direct == 0
                else:
                    assert profile > 0 and laplacian_direct < 0
                for nu in (Q(0), Q(1, 10), Q(1), Q(10**6)):
                    residual = time_derivative - (2 * s / n) * first_derivative - 2 * nu * laplacian_direct
                    assert residual == f - 2 * nu * laplacian_seed
                    assert residual >= f
                    radial_checks += 1
                    # Unit direction (3/5,4/5,0,...); isotropic +/- and traceless.
                    for diagonal in ([Q(2)] * d, [Q(-2)] * d,
                                     [Q(1), Q(-1)] + [Q(0)] * (d - 2)):
                        angular = diagonal[0] * Q(9, 25) + diagonal[1] * Q(16, 25)
                        norm = max(abs(x) for x in diagonal)
                        assert norm * residual >= abs(f * angular)
                        angular_checks += 1
            for q_lyap in (Q(1, 2), Q(d - 2), Q(d + 1)):
                den = lcm(s.denominator, q_lyap.denominator)
                for k in (2, 3):
                    r = Q(k) ** den
                    power = lambda exponent: rational_power(k, den, exponent)
                    vp = 2 * r - q_lyap * power(-q_lyap - 1)
                    vpp = 2 + q_lyap * (q_lyap + 1) * power(-q_lyap - 2)
                    for nu in (Q(0), Q(1, 10), Q(1), Q(10**6)):
                        direct = 2 * nu * (vpp + (d - 1) * vp / r) + (2 * s / n) * power(-s - 1) * vp
                        seed = (4 * nu * d + (4 * s / n) * power(-s)
                                + 2 * nu * q_lyap * (q_lyap - d + 2) * power(-q_lyap - 2)
                                - (2 * s * q_lyap / n) * power(-q_lyap - s - 2))
                        assert direct == seed
                        lyapunov_checks += 1
                        if nu > 0:
                            log_scale_derivative = (1 - d) / r - (s / (n * nu)) * power(-s - 1)
                            radial_drift = 2 * nu * (d - 1) / r + (2 * s / n) * power(-s - 1)
                            assert 2 * nu * log_scale_derivative + radial_drift == 0
                            scale_checks += 1

report = {
    'status': 'all exact arithmetic assertions passed',
    'scope': 'finite sample checks supporting the memorandum, not proof certification',
    'arithmetic': 'fractions.Fraction; no floating point or external dependencies',
    'parameters': parameters,
    'particle_numbers': [2, 3, 17],
    'diffusivities': ['0', '1/10', '1', '1000000'],
    'radial_identity_and_comparison_checks': radial_checks,
    'isotropic_and_traceless_angular_checks': angular_checks,
    'lyapunov_identity_checks': lyapunov_checks,
    'scale_generator_checks': scale_checks,
    'iid_exponent_checks': exponent_checks,
}
path = Path(__file__).with_name('round004_diffusive_reconstruction_exact_output.json')
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
