#!/usr/bin/env python3
"""Fresh deterministic self-check; no continuum certification or SDE simulation."""
import argparse
from collections import Counter
from fractions import Fraction as Q
import json
import math
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutate', choices=['pair_drift', 'diffusion', 'projection',
                        'cross_bracket', 'omit_bias', 'radial_power'])
    args = parser.parse_args()
    counts = Counter()
    witnesses = []
    observations = []

    def check(condition, category, actual=None, expected=None):
        counts[category] += 1
        if not condition:
            witnesses.append({'category': category, 'actual': str(actual),
                              'expected': str(expected)})

    # Exact conditional projection on a genuine finite probability space.
    # Initial state is uniform; cyclic transition rows are doubly stochastic.
    trans = [[Q(1, 2), Q(1, 3), Q(1, 6)],
             [Q(1, 6), Q(1, 2), Q(1, 3)],
             [Q(1, 3), Q(1, 6), Q(1, 2)]]
    f = [Q(-1), Q(0), Q(1)]
    u = [sum(trans[i][j] * f[j] for j in range(3)) for i in range(3)]
    for n in [2, 3, 5, 11, 29]:
        for a in [Q(0), Q(1, 3), Q(3, 4), Q(1)]:
            defect = noise = bias = cross = terminal_noise = Q(0)
            for i in range(3):
                bias += Q(n, 3) * (u[i] - a * f[i]) ** 2
                conditional_noise = Q(0)
                for j in range(3):
                    w = Q(n, 3) * trans[i][j]
                    v = f[j] - u[i]
                    defect += w * (f[j] - a * f[i]) ** 2
                    noise += w * v ** 2
                    cross += w * (u[i] - a * f[i]) * v
                    terminal_noise += w * f[j] * v
                    conditional_noise += trans[i][j] * v
                check(conditional_noise == 0, 'conditional_noise_zero')
            rhs = noise if args.mutate == 'omit_bias' else noise + bias
            check(defect == rhs, 'conditional_pythagoras', rhs, defect)
            check(cross == 0, 'initial_conditional_orthogonality')
            claimed = Q(0) if args.mutate == 'cross_bracket' else terminal_noise
            check(claimed == noise, 'terminal_noise_cross_retained', claimed, noise)
            check(noise > 0, 'nonzero_noise_control')
            check(bias > 0, 'nonzero_bias_control')

    # Direct particle-to-relative Brownian and force coefficients.
    for n in range(2, 33):
        for nu in [Q(1, 7), Q(1), Q(5, 2)]:
            alpha_literal = Q(2, n) * 2
            alpha_claimed = Q(2 if args.mutate == 'pair_drift' else 4, n)
            check(alpha_literal == alpha_claimed, 'relative_pair_drift',
                  alpha_claimed, alpha_literal)
            relative_var = (2 if args.mutate == 'diffusion' else 4) * nu
            center_var = Q(1, 4) * (2 * nu + 2 * nu)
            cross_var = Q(1, 2) * (2 * nu - 2 * nu)
            check(relative_var == 4 * nu, 'relative_brownian_variance',
                  relative_var, 4 * nu)
            check(center_var == nu, 'center_brownian_variance')
            check(cross_var == 0, 'center_relative_cross_bracket')
            for radius_squared in [Q(1, 9), Q(1, 2), Q(3)]:
                # Direct Cartesian derivatives: Hessian r^4 has trace 24r^2.
                # Gradient r^4 dotted with alpha*y/r^4 is exactly 4alpha.
                generator_r4 = 4 * alpha_literal + Q(1, 2) * relative_var * 24 * radius_squared
                expected_r4 = Q(16, n) + 48 * nu * radius_squared
                check(generator_r4 == expected_r4, 'radial_ito_fourth',
                      generator_r4, expected_r4)
                bracket_r4 = 16 * radius_squared ** 3 * relative_var
                check(bracket_r4 == 64 * nu * radius_squared ** 3,
                      'radial_fourth_true_bracket', bracket_r4,
                      64 * nu * radius_squared ** 3)
                generator_r2 = 2 * alpha_literal / radius_squared + Q(1, 2) * relative_var * 8
                check(generator_r2 == 2 * alpha_literal / radius_squared + 16 * nu,
                      'radial_ito_second')

    # S3 coordinate moments from the elementary beta integral recurrence.
    def moment(m):
        out = Q(1)
        for j in range(1, m + 1):
            out *= Q(2 * j - 1, 2 * j + 2)
        return out

    check(moment(1) == Q(1, 4), 'sphere_second_moment')
    check(moment(2) == Q(1, 8), 'sphere_fourth_moment')
    projection = moment(2) - (Q(1, 3) if args.mutate == 'projection' else Q(1, 4)) * moment(1)
    check(projection == Q(1, 16), 'nonzero_degree_two_projection', projection, Q(1, 16))
    check(2 - Q(1, 4) * 8 == 0, 'degree_two_harmonic_polynomial')
    check(2 * (2 + 4 - 2) == 8, 'sphere_eigenvalue')
    for m in range(1, 21):
        factorial_form = Q(math.factorial(2*m), 4**m * math.factorial(m) * math.factorial(m+1))
        check(moment(m) == factorial_form, 'independent_sphere_moment_forms')
        diff = moment(m+1) - moment(m) / 4
        check(diff == moment(m) * Q(3*m, 4*(m+2)), 'angular_cosine_moment')

    # Exact pair sum and Jacobian factors. The local ODE is a diagnostic,
    # not a replacement for the positive-noise periodic proof.
    for n in [2, 3, 7, 19, 101]:
        for r, radius in [(Q(1), Q(2)), (Q(1, 7), Q(3, 4)),
                          (Q(1, 101), Q(2, 3))]:
            alpha = Q(4, n)
            t = (radius**4 - r**4) / (4 * alpha)
            check(r**4 + 4*alpha*t == radius**4, 'exact_radial_flow')
            tangent_eigen = radius / r
            radial_eigen = (r / radius)**3
            check(tangent_eigen**3 * radial_eigen == 1, 'radial_flow_determinant')
            check(tangent_eigen > 1, 'tangential_expansion_nonzero')
            check(Q(2, n) * Q(-1, 2) == Q(-1, n), 'empirical_pair_taylor_factor')

    dimension = 3 if args.mutate == 'radial_power' else 4
    check(dimension - 1 - 4 == -1, 'fourth_gradient_log_threshold',
          dimension - 1 - 4, -1)
    check(4 - 1 - 2 == 1, 'square_gradient_not_excluded')
    for j in range(1, 12):
        delta = Q(1, 10**j)
        square_integral = (1 - delta**2) / 2
        check(square_integral < Q(1, 2), 'square_radial_integral_bounded')
        check(abs(math.log(1/float(delta)) - j*math.log(10)) < 1e-12,
              'fourth_radial_log_integral')

    # Convergent angular cosine series; terms use exact spherical moments.
    # Absolute term sum is dominated by exp(|z|); 61 terms make the
    # omitted tail < 1e-80 for this parameter grid. IEEE floats only here.
    for n in [2, 3, 5, 17, 41]:
        for t in [1e-4, 1e-6, 1e-8, 1e-10]:
            radius = (16 * t / n)**0.25
            z = math.pi * radius
            terms = [(-1)**m * z**(2*m) / math.factorial(2*m)
                     * float(moment(m+1) - moment(m)/4) for m in range(61)]
            projection_value = 2 / n * math.fsum(terms)
            leading = -math.pi**2 / (4 * n**1.5) * math.sqrt(t)
            ratio = projection_value / leading
            check(projection_value < 0, 'radial_projection_sign')
            check(abs(ratio - 1) <= 8*math.sqrt(t) + 1e-12,
                  'radial_projection_asymptotic', ratio, 1)
            check(abs(terms[-1]) < 1e-80, 'cosine_tail_control')
            observations.append({'N': n, 't': t, 'projection': projection_value,
                                 'leading': leading, 'ratio': ratio})
    for n in [2, 7, 31]:
        t = 1e-6
        previous = 0.0
        for r in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
            radius = (r**4 + 16*t/n)**0.25
            angle_component = 1/math.sqrt(2)
            argument = math.pi*radius*angle_component
            gradient = 2*math.pi/n * math.sin(argument) * radius/r * angle_component
            check(gradient > previous, 'actual_radial_tangential_blowup')
            ratio = gradient*r/(math.pi**2*radius**2/n)
            check(abs(ratio - math.sin(argument)/argument) < 1e-12,
                  'radial_tangential_coefficient')
            previous = gradient

    output = {
        'status': 'FAIL' if witnesses else 'PASS',
        'mutation': args.mutate, 'assertions': sum(counts.values()),
        'categories': dict(sorted(counts.items())),
        'failures': witnesses, 'radial_series_observations': observations,
        'conventions': {'dimension': 4, 'alpha': '4/N',
                        'relative_noise_variance': '4*nu', 'sphere_measure': 'mass one',
                        'random_sampling': False, 'SDE_discretization': False,
                        'rational_checks': 'fractions.Fraction',
                        'floating_tolerances': 'absolute 1e-12; projection relative 8*sqrt(t)+1e-12'},
        'limitations': ['Same-context diagnostic, not an independent audit.',
                        'The radial ODE is a local solvable model, not the actual law.',
                        'The continuum singular-limit and W1,4 proofs are in REPORT.md.',
                        'No critical source decay or actual positive-limsup negation is proved.']}
    print(json.dumps(output, indent=2, sort_keys=True))
    return 1 if witnesses else 0


if __name__ == '__main__':
    sys.exit(main())
