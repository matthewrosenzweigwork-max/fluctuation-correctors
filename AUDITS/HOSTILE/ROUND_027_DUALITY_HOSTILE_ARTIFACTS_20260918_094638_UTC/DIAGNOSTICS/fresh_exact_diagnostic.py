#!/usr/bin/env python3
"""AUD076 fresh coefficient/path diagnostics, standard library, no file writes.

These are exact algebraic diagnostics, not a simulation or proof of the singular
SDE. The mathematical lifetime and continuous-path arguments are in REVIEW.md.
All fractions are exact. No seed, numerical tolerance, external input or package.
"""
from fractions import Fraction as R
from itertools import product
import json


CHECKS = []
MUTATIONS = []


def encode(value):
    if isinstance(value, R):
        return str(value)
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    return value


def check(name, left, right):
    assert left == right, (name, left, right)
    CHECKS.append({'name': name, 'pass': True})


def reject(name, expected, mutated, scope):
    difference = mutated - expected
    assert difference != 0, (name, expected, mutated)
    MUTATIONS.append({'name': name, 'expected': encode(expected),
                      'mutated': encode(mutated),
                      'nonzero_difference': encode(difference), 'scope': scope})


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def scale(a, r):
    return a[0]*r, a[1]*r


def abs2(a):
    return a[0]*a[0] + a[1]*a[1]


def conjugate(a):
    return a[0], -a[1]


def pair_probe():
    # Local probe only: |z|^-2 + c |z|^2 / 8 has the coefficient-one
    # d=4 Coulomb principal part and punctured Laplacian c.
    # c=3/2 tests rational coefficients; it is NOT the periodic kernel.
    d, c = 4, R(3, 2)
    configs = [
        [(0, 0, 0, 0), (1, 2, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 0, 0), (0, 2, 1, 0)],
        [(0, 0, 0, 0), (1, 2, 0, 0), (2, 1, 1, 0), (0, 1, 1, 2)],
    ]
    for points in configs:
        n = len(points)
        grad = [[R(0) for _ in range(d)] for _ in points]
        trace = R(0)
        individual_squares = R(0)
        for i in range(n):
            for j in range(i + 1, n):
                z = [R(points[i][a] - points[j][a]) for a in range(d)]
                rr = sum(q*q for q in z)
                principal_trace = sum(-R(2)/(rr*rr) + R(8)*q*q/(rr**3) for q in z)
                check('principal_laplacian_N%d_pair%d%d' % (n, i, j), principal_trace, R(0))
                pair_trace = principal_trace + c
                trace += R(2, n) * pair_trace
                dg = [(-R(2)/(rr*rr) + c/R(4))*q for q in z]
                for a in range(d):
                    grad[i][a] += dg[a]/n
                    grad[j][a] -= dg[a]/n
                individual_squares += R(2, n*n) * sum(q*q for q in dg)
        check('full_laplacian_N%d' % n, trace, c*(n-1))
        check('translation_gradient_N%d' % n,
              tuple(sum(grad[i][a] for i in range(n)) for a in range(d)),
              (R(0),)*d)
        reject('omit_second_particle_laplacian_N%d' % n, trace, trace/2,
               'Local coefficient test only; no torus-SDE claim.')
        full_square = sum(q*q for row in grad for q in row)
        if n >= 3:
            reject('discard_cross_force_terms_N%d' % n, full_square,
                   individual_squares, 'Complete square cannot be replaced by pair squares.')


def girsanov_probe():
    nu, kap, t = R(3, 5), R(7, 3), R(4, 9)
    h0, ht, force_integral = R(-2, 7), R(8, 5), R(11, 4)
    delta_h = ht - h0
    ito_integral = delta_h - nu*kap*t
    logs = {}
    for sign, label in [(-1, 'repulsive'), (1, 'attractive')]:
        direct = sign*ito_integral/(2*nu) - force_integral/(4*nu)
        endpoint = sign*delta_h/(2*nu) - sign*kap*t/2 - force_integral/(4*nu)
        check('girsanov_%s' % label, direct, endpoint)
        logs[label] = direct
    reverse_attractive = (-delta_h - nu*kap*t)/(2*nu) - force_integral/(4*nu)
    check('path_log_ratio', logs['repulsive'] - reverse_attractive, kap*t)
    reject('reverse_divergence_sign', logs['repulsive'],
           -delta_h/(2*nu) - kap*t/2 - force_integral/(4*nu),
           'Wrong repulsive kappa sign in the fixed-domain density.')
    reject('halve_noise_girsanov_denominator', logs['repulsive'],
           -ito_integral/nu - force_integral/(2*nu),
           'Wrong factors for Brownian covariance 2 nu.')
    reject('double_force_square_penalty', logs['repulsive'],
           -ito_integral/(2*nu) - force_integral/(2*nu),
           'The spatial force square is common with coefficient 1/(4 nu).')


def matrix_probe():
    # Three-point rational analogue of ONE discrete semigroup step. It has no
    # status as a singular diffusion or a time-discretization of that diffusion.
    p = [[R(1, 2), R(1, 3), R(1, 6)],
         [R(3, 4), R(1, 4), R(0)],
         [R(1, 4), R(1, 2), R(1, 4)]]
    factor = R(7, 4)
    q = [[p[j][i]/factor for j in range(3)] for i in range(3)]
    check('p_row_masses', tuple(sum(row) for row in p), (R(1),)*3)
    assert all(sum(row) <= 1 for row in q)
    CHECKS.append({'name': 'q_submarkov', 'pass': True})
    check('q_column_masses', tuple(sum(q[i][j] for i in range(3)) for j in range(3)),
          (1/factor,)*3)
    reject('point_start_survival_uniformization', 1/factor, sum(q[0]),
           'Finite-model distinction only; continuum point-start argument is analytic.')
    f = [(R(1), R(2)), (R(-2), R(1)), (R(3), R(-4))]
    a = (R(2, 3), R(1, 5))
    h = [[(R(i+1), R(1-i)) for i in range(3)],
         [(R(2-i), R(i+2)) for i in range(3)],
         [(R(3*i-1), R(2-i)) for i in range(3)]]
    witness = None
    for steps in range(6):
        survival = R(0)
        endpoint_mass = [R(0)]*3
        actual_defect = R(0)
        conditional_defect = R(0)
        wrong_orientation = R(0)
        wrong_conjugation = R(0)
        actual_cylinder, reverse_cylinder = (R(0), R(0)), (R(0), R(0))
        for xs in product(range(3), repeat=steps+1):
            pw, qw = R(1, 3), R(1, 3)
            ys = tuple(reversed(xs))
            for j in range(steps):
                pw *= p[xs[j]][xs[j+1]]
                qw *= q[ys[j]][ys[j+1]]
            check('path_weight_m%d_%s' % (steps, ''.join(map(str, xs))), pw, factor**steps*qw)
            survival += qw
            endpoint_mass[ys[-1]] += qw
            actual_defect += pw*abs2(sub(f[xs[-1]], mul(a, f[xs[0]])))
            conditional_defect += factor**steps*qw*abs2(sub(f[ys[0]], mul(a, f[ys[-1]])))
            wrong_orientation += factor**steps*qw*abs2(sub(f[ys[-1]], mul(a, f[ys[0]])))
            wrong_conjugation += factor**steps*qw*abs2(sub(f[ys[0]], mul(conjugate(a), f[ys[-1]])))
            cylinder, reversed_tests = (R(1), R(0)), (R(1), R(0))
            for j in range(steps+1):
                cylinder = mul(cylinder, h[j % 3][xs[j]])
                reversed_tests = mul(reversed_tests, h[j % 3][ys[steps-j]])
            actual_cylinder = add(actual_cylinder, scale(cylinder, pw))
            reverse_cylinder = add(reverse_cylinder, scale(reversed_tests, factor**steps*qw))
        check('survival_m%d' % steps, survival, factor**(-steps))
        check('surviving_endpoint_m%d' % steps, tuple(endpoint_mass),
              (factor**(-steps)/3,)*3)
        check('complex_cylinder_m%d' % steps, actual_cylinder, reverse_cylinder)
        check('complex_endpoint_m%d' % steps, actual_defect, conditional_defect)
        if steps == 3:
            reject('swap_response_endpoints', actual_defect, wrong_orientation,
                   'The reversed defect must be F(Y0)-A F(YT).')
            reject('conjugate_response_A', actual_defect, wrong_conjugation,
                   'Bilinear kernel transposition does not conjugate A.')
            reject('drop_survival_normalizer', actual_defect,
                   conditional_defect*survival,
                   'Conditioning requires the exact reciprocal surviving mass.')
            witness = {'steps': steps, 'normalizer': factor**steps,
                       'actual_and_correct_conditional': actual_defect,
                       'wrong_orientation': wrong_orientation,
                       'wrong_conjugation': wrong_conjugation,
                       'raw_unnormalized': conditional_defect*survival}
    return {'p': p, 'q': q, 'step_factor': factor, 'response_witness': witness}


def boundary_probe():
    # This finite sequence does not establish an infinite limit. It checks the
    # equality-time counterexample to replacing strict lifetime by weak lifetime.
    t = R(2)
    for level in range(1, 21):
        tau = t - R(1, level)
        check('strict_exit_at_equal_lifetime_L%d' % level, int(tau > t), 0)
    reject('include_lifetime_equality', 0, 1,
           'For tau_L=t-1/L and zeta=t, no domain survives t; 1_{t<=zeta} is false replacement.')
    # A killed reversible discrete path: fixed-domain event and symmetric
    # trapezoidal potential weight remain invariant under reversal.
    s = [[R(1, 2), R(1, 3), R(1, 6)],
         [R(1, 3), R(1, 3), R(1, 3)],
         [R(1, 6), R(1, 3), R(1, 2)]]
    allowed, weights = {0, 2}, [R(2, 3), R(3, 5), R(5, 7)]
    for xs in product(range(3), repeat=4):
        ys = tuple(reversed(xs))
        def weight(path):
            if any(v not in allowed for v in path):
                return R(0)
            out = R(1, 3)
            for j in range(3):
                out *= s[path[j]][path[j+1]]*weights[path[j]]*weights[path[j+1]]
            return out
        check('killed_symmetric_path_%s' % ''.join(map(str, xs)), weight(xs), weight(ys))
    # Omit the final endpoint from the killing event: a path starting inside
    # and ending outside breaks reversal of the event.
    bad_path, allowed = (0, 0, 1), {0}
    original = int(all(x in allowed for x in bad_path[:-1]))
    reversed_event = int(all(x in allowed for x in tuple(reversed(bad_path))[:-1]))
    reject('omit_terminal_domain_membership', reversed_event, original,
           'Whole [0,t] containment, including both endpoints, is essential.')


def main():
    pair_probe()
    girsanov_probe()
    matrix = matrix_probe()
    boundary_probe()
    result = {'status': 'PASS', 'arithmetic': 'exact rational', 'random_seed': None,
              'numerical_tolerance': None, 'external_dependencies': [],
              'checks_passed': len(CHECKS), 'mutations_rejected': len(MUTATIONS),
              'checks': CHECKS, 'mutations': MUTATIONS, 'matrix_diagnostic': matrix,
              'limitations': [
                  'No singular-SDE simulation or continuum estimate.',
                  'Finite path diagnostics do not prove Brownian reversal or path-space identification.',
                  'Local pair probe is not the periodic kernel; it tests differential factors only.',
                  'Mutations are deliberately false alternatives, not counterexamples to THM052.',
                  'No claim about modal defect decay, independent accepted gates or source history.']}
    print(json.dumps(encode(result), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
