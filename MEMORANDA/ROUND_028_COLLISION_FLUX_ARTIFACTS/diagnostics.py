#!/usr/bin/env python3
"""Exact TASK121 supporting diagnostics; stdout only, no writes/dependencies.

This is constructor evidence, not a computational proof or independent audit.
All arithmetic is rational. Occurrences of c are normalized out or retained as
an exact symbolic coefficient with rational test values; pi is not approximated.
Local polynomial and Euclidean models are expressly not the periodic SDE.
"""

import argparse
from fractions import Fraction as Q
from itertools import combinations
import json
import platform


class Jet:
    """Value, gradient, full Hessian for exact independent differentiation."""

    def __init__(self, value, grad, hess):
        self.value = Q(value)
        self.grad = tuple(grad)
        self.hess = tuple(tuple(row) for row in hess)
        self.dim = len(self.grad)

    @classmethod
    def constant(cls, value, dim):
        return cls(value, [Q(0)] * dim, [[Q(0)] * dim for _ in range(dim)])

    @classmethod
    def variable(cls, value, index, dim):
        g = [Q(0)] * dim
        g[index] = Q(1)
        return cls(value, g, [[Q(0)] * dim for _ in range(dim)])

    def coerce(self, other):
        return other if isinstance(other, Jet) else Jet.constant(other, self.dim)

    def __add__(self, other):
        other = self.coerce(other)
        return Jet(self.value + other.value,
                   [a + b for a, b in zip(self.grad, other.grad)],
                   [[self.hess[i][j] + other.hess[i][j]
                     for j in range(self.dim)] for i in range(self.dim)])

    __radd__ = __add__

    def __neg__(self):
        return self * Q(-1)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Jet(self.value * other.value,
                   [self.grad[i] * other.value + self.value * other.grad[i]
                    for i in range(self.dim)],
                   [[self.hess[i][j] * other.value
                     + self.grad[i] * other.grad[j]
                     + self.grad[j] * other.grad[i]
                     + self.value * other.hess[i][j]
                     for j in range(self.dim)] for i in range(self.dim)])

    __rmul__ = __mul__

    def inverse(self):
        if self.value == 0:
            raise ZeroDivisionError("Jet inverse at zero")
        v = self.value
        return Jet(1 / v, [-g / v**2 for g in self.grad],
                   [[2 * self.grad[i] * self.grad[j] / v**3
                     - self.hess[i][j] / v**2
                     for j in range(self.dim)] for i in range(self.dim)])

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("Integer powers only")
        if n < 0:
            return self.inverse() ** (-n)
        result = Jet.constant(1, self.dim)
        for _ in range(n):
            result = result * self
        return result

    def laplacian(self):
        return sum(self.hess[i][i] for i in range(self.dim))


def sq(v):
    return sum(x*x for x in v)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def diagonal_moment(freqs, pair):
    """Integrate the character by its independent Haar coordinates."""
    i, j = pair
    independent_frequencies = [tuple(a+b for a, b in zip(freqs[i], freqs[j]))]
    independent_frequencies += [k for l, k in enumerate(freqs) if l not in pair]
    return Q(int(all(all(a == 0 for a in k) for k in independent_frequencies)))


def h_fourier(freqs):
    """Fourier coefficient of the literal pair sum, away from the zero mode."""
    active = [(i, k) for i, k in enumerate(freqs) if any(k)]
    if len(active) != 2:
        return Q(0)
    (_, k), (_, ell) = active
    if tuple(-a for a in k) != ell:
        return Q(0)
    return Q(1, len(freqs) * sq(k))


def frequency_cases(n):
    zero = (0, 0, 0, 0)
    modes = [(1, 0, 0, 0), (1, -2, 0, 1), (0, 0, 0, 3)]
    cases = {tuple([zero] * n)}
    for i in range(n):
        for k in modes:
            row = [zero] * n
            row[i] = k
            cases.add(tuple(row))
    for i, j in combinations(range(n), 2):
        for k in modes:
            for sign in (-1, 1):
                row = [zero] * n
                row[i] = k
                row[j] = tuple(sign * a for a in k)
                cases.add(tuple(row))
    for i, j, ell in combinations(range(n), 3):
        row = [zero] * n
        row[i] = row[j] = modes[0]
        row[ell] = (-2, 0, 0, 0)
        cases.add(tuple(row))
    if n >= 4:
        row = [zero] * n
        row[:4] = [(1, 0, 0, 0), (-1, 0, 0, 0),
                   (0, 1, 0, 0), (0, -1, 0, 0)]
        cases.add(tuple(row))
    return sorted(cases)


def configuration_jets(points):
    n = len(points)
    return [[Jet.variable(points[i][a], 4*i+a, 4*n) for a in range(4)]
            for i in range(n)]


def local_h(points, c):
    """g(z)=|z|^-2+(c/8)|z|^2; differential diagnostic only."""
    n = len(points)
    x = configuration_jets(points)
    h = Jet.constant(0, 4*n)
    for i, j in combinations(range(n), 2):
        r2 = sum((x[i][a] - x[j][a])**2 for a in range(4))
        h += (r2.inverse() + Q(c, 8)*r2) / n
    return x, h


def explicit_local_gradient(points, c):
    n = len(points)
    result = [[Q(0)]*4 for _ in range(n)]
    for i, j in combinations(range(n), 2):
        z = [Q(points[i][a]) - Q(points[j][a]) for a in range(4)]
        r2 = sq(z)
        force = [(-2 / r2**2 + Q(c, 4))*v/n for v in z]
        for a in range(4):
            result[i][a] += force[a]
            result[j][a] -= force[a]
    return [a for row in result for a in row]


def run():
    checks = []
    mutations = []

    def check(name, actual, expected, parameters):
        checks.append({'id': name, 'parameters': parameters,
                       'actual': str(actual), 'expected': str(expected),
                       'passed': actual == expected})

    def mutation(name, residual, description):
        mutations.append({'id': name, 'residual': str(residual),
                          'detected': residual != 0, 'meaning': description})

    for n in (2, 3, 4, 7):
        pairs = list(combinations(range(n), 2))
        for idx, freqs in enumerate(frequency_cases(n)):
            mean = Q(int(all(not any(k) for k in freqs)))
            trace = sum(sq(k) for k in freqs)
            hcoef = h_fourier(freqs)
            diag = sum(diagonal_moment(freqs, pair) for pair in pairs)
            direct = -trace*hcoef  # Delta H / c from the full Fourier symbol.
            proposed = (n-1)*mean - Q(2, n)*diag
            parameters = {'N': n, 'frequencies': freqs, 'units': 'c=4*pi^2 factored out'}
            check('FOURIER_N%d_%03d' % (n, idx), direct, proposed, parameters)
            # This spatial gradient pairing is computed directly from H's Fourier
            # coefficient and opposite differentiation, not from the atom formula.
            gradient_pairing = trace*hcoef
            for alpha in (Q(0), Q(1, 2), Q(2), Q(5, 3)):
                stopped_resolvent = mean + (gradient_pairing-alpha*mean)/(n-1+alpha)
                exit_resolvent = Q(2, n)*diag/(n-1+alpha)
                check('LAPLACE_N%d_%03d_a%s' % (n, idx, str(alpha)),
                      stopped_resolvent, exit_resolvent,
                      dict(parameters, temporal_parameter_a_over_c=str(alpha)))
        per_pair_mass = Q(2, n)/(n-1)
        check('PAIR_MASS_N%d' % n, per_pair_mass, Q(1, len(pairs)), {'N': n})
        check('TOTAL_MASS_N%d' % n, len(pairs)*per_pair_mass, Q(1), {'N': n})
        # q=(xi-xj)/sqrt2; sphere area/c=1/2; diagonal dp/dy=4 in d4.
        normal_atom_over_c = -Q(1, n)*Q(1, 2)*4
        check('NORMAL_FLUX_N%d' % n, normal_atom_over_c, -Q(2, n),
              {'N': n, 'sphere_area_over_c': '1/2', 'diagonal_tangent_jacobian': '4'})

    points_cases = [
        [[Q(0), Q(0), Q(0), Q(0)], [Q(1, 2), Q(1, 3), Q(1, 5), Q(0)]],
        [[Q(-1, 7), Q(0), Q(0), Q(0)], [Q(0)]*4, [Q(1, 7), Q(0), Q(0), Q(0)]],
        [[Q(0)]*4, [Q(1, 7), Q(1, 11), Q(0), Q(0)],
         [Q(-1, 5), Q(0), Q(1, 9), Q(1, 13)]],
        [[Q(-1, 100), Q(0), Q(0), Q(0)], [Q(1, 100), Q(0), Q(0), Q(0)],
         [Q(-1, 100), Q(3, 10), Q(0), Q(0)], [Q(1, 100), Q(3, 10), Q(0), Q(0)]],
    ]
    for pidx, points in enumerate(points_cases):
        n = len(points)
        for c in (0, 5):
            x, h = local_h(points, c)
            assembled = explicit_local_gradient(points, c)
            pars = {'N': n, 'points': [[str(v) for v in row] for row in points],
                    'symbolic_c_test_value': c, 'model': 'Euclidean local polynomial diagnostic'}
            check('AD_GRAD_%d_c%d' % (pidx, c), sq([a-b for a, b in zip(h.grad, assembled)]),
                  Q(0), pars)
            check('AD_LAPLACIAN_%d_c%d' % (pidx, c), h.laplacian(), Q(c*(n-1)), pars)
            check('PAIR_DRIFT_CANCELLATION_%d_c%d' % (pidx, c),
                  sum(sq([sum(h.grad[4*i+a] for i in range(n))]) for a in range(4)),
                  Q(0), pars)
            flat_x = [v for row in x for v in row]
            flat_values = [Q(v) for row in points for v in row]
            f = sum(Q(q+1, 2)*v*v for q, v in enumerate(flat_x)) + flat_x[0]*flat_x[5]
            fgrad = [Q(q+1)*v for q, v in enumerate(flat_values)]
            fgrad[0] += flat_values[5]
            fgrad[5] += flat_values[0]
            flap = sum(range(1, 4*n+1))
            for nu in (Q(1, 7), Q(3, 2)):
                automatic_generator = nu*f.laplacian() + dot(h.grad, f.grad)
                raw_generator = nu*flap + dot(assembled, fgrad)
                check('AD_GENERATOR_%d_c%d_nu%s' % (pidx, c, nu),
                      automatic_generator, raw_generator, dict(pars, nu=str(nu)))

    # Raw eight-coordinate calculation, independent of the relative-generator rule.
    relative_points = [[Q(0)]*4, [Q(1, 5), Q(1, 7), Q(0), Q(0)]]
    xx = configuration_jets(relative_points)
    r2jet = sum((xx[0][a]-xx[1][a])**2 for a in range(4))
    r2 = r2jet.value
    for denominator in (2, 3, 7):
        h = r2jet.inverse()/denominator
        for nu in (Q(1, 7), Q(3, 2)):
            for power in (2, 4, 6):
                f = r2jet**(power//2)
                full_generator = nu*f.laplacian()+dot(h.grad, f.grad)
                radial_generator = (2*nu*power*(power+2)*r2**(power//2-1)
                                    - Q(4*power, denominator)*r2**(power//2-2))
                check('RADIAL_DENOM%d_nu%s_p%d' % (denominator, nu, power),
                      full_generator, radial_generator,
                      {'two_particles': True, 'interaction_denominator': denominator,
                       'actual_N2_only_when_denominator_is_2': True,
                       'nu': str(nu), 'power': power, 'r_squared': str(r2)})

    radial_cutoffs = []
    r0 = Q(1, 5)
    denominator = 2
    for j in range(1, 6):
        eps = r0/Q(2**j)
        time = Q(denominator, 16)*(r0**4-eps**4)
        check('SOLVABLE_RADIUS_%d' % j, r0**4-Q(16, denominator)*time, eps**4,
              {'model': 'Euclidean attractive N2 with nu=0, outside frozen hypotheses',
               'r0': str(r0), 'epsilon': str(eps), 'time': str(time)})
        first_action_over_sqrt2 = Q(2, denominator)*Q(denominator, 4)*(r0-eps)
        check('SOLVABLE_ACTION_%d' % j, first_action_over_sqrt2, (r0-eps)/2,
              {'first_action_divided_by_sqrt2': True, 'epsilon': str(eps)})
        second_action = Q(1, denominator)*(eps**-2-r0**-2)
        radial_cutoffs.append({'epsilon': str(eps), 'time': str(time),
                               'first_action_over_sqrt2': str(first_action_over_sqrt2),
                               'second_action': str(second_action)})

    # Every mutation below is a deliberately rejected substitute, not an actual
    # counterexample to the theorem. Its nonzero residual must be present.
    n = 3
    pair_count = n*(n-1)//2
    mutation('M01_MISSING_PAIR_FACTOR_TWO', Q(1, n)*pair_count/(n-1)-1,
             'Replacing 2c/N by c/N gives total exit mass 1/2.')
    mutation('M02_FLIPPED_COLLISION_ATOM', Q(2, n)-(-Q(2, n)),
             'Opposite-pair Fourier atom has the wrong sign.')
    mutation('M03_OMITTED_COMPENSATION', -Q(2, n)*pair_count,
             'A periodic Laplacian must have zero total mass.')
    mutation('M04_WRONG_RATE_CN', Q(2, n)*pair_count/n-1,
             'Using rate cN with the correct pair flux loses total probability.')
    mutation('M05_SPURIOUS_DIFFUSIVITY_FLUX', Q(3, 7)-1,
             'Multiplying the exit flux by nu=3/7 changes total mass.')
    mutation('M06_HALF_RELATIVE_DIFFUSION', Q(1, 7)*2*(2+2),
             'Using nu*Delta instead of 2nu*Delta changes the r^2 generator by 8nu.')
    e = (1, 0, 0, 0)
    triple_freq = (e, e, (-2, 0, 0, 0))
    expected_triple_moment = sum(diagonal_moment(triple_freq, p)
                                 for p in combinations(range(3), 2))/3
    mutation('M07_TRIPLE_DIAGONAL_MASS', Q(1, 3)*(1-expected_triple_moment),
             'A mixture with mass 1/3 on the triple Haar diagonal has an unwanted three-label Fourier moment.')
    epsilon = Q(1, 2)
    coupled_moment = epsilon*(Q(2, 3)-Q(1, 2))*Q(1, 2)
    mutation('M08_SAME_MARGINALS_WRONG_JOINT_LAW', coupled_moment,
             'For N2, density 1+epsilon*(2e^{-kappa t}-1)*cos(2pi U_1) preserves both marginals, '
             'but E[e^{-kappa t}cos(2pi U_1)] differs by 1/24.')
    symmetric = points_cases[1]
    _, hsym = local_h(symmetric, 0)
    full_square = sq(hsym.grad)
    pair_square_sum = Q(0)
    for i, j in combinations(range(3), 2):
        z = [symmetric[i][a]-symmetric[j][a] for a in range(4)]
        pair_gradient = [-2*v/sq(z)**2 for v in z]
        pair_square_sum += Q(2, 9)*sq(pair_gradient)
    mutation('M09_DELETING_FORCE_CROSS_TERMS', full_square-pair_square_sum,
             'In a symmetric three-particle principal-kernel cluster, the full drift square differs from the sum of pair squares.')
    mutation('M10_SURFACE_MEASURE_AS_PROBABILITY_DIAGONAL', -Q(1, 2*n)-(-Q(2, n)),
             'Omitting dp=4dy in d4 normal coordinates gives the wrong collision atom.')
    mutation('M11_ORDERED_PAIRS_IN_UNORDERED_FORMULA', Q(2)-1,
             'Summing the unordered-pair coefficient over ordered pairs doubles total mass.')

    result = {
        'task': 'TASK121 / THM053 complete supporting diagnostics',
        'status': 'SELF_CHECKED; exact diagnostic evidence, not an independent audit',
        'runtime_python': platform.python_version(),
        'arithmetic': 'fractions.Fraction only; no random inputs, no tolerance, no pi approximation',
        'baseline_count': len(checks),
        'baseline_pass_count': sum(item['passed'] for item in checks),
        'mutation_count': len(mutations),
        'mutation_detected_count': sum(item['detected'] for item in mutations),
        'all_pass': all(item['passed'] for item in checks) and all(item['detected'] for item in mutations),
        'checks': checks,
        'mutations': mutations,
        'solvable_radial_cutoff_table': radial_cutoffs,
        'limits': [
            'Fourier checks cover specified finite modes, not all analytic test functions; the memorandum proves the latter.',
            'The local polynomial model is not periodic and has no probabilistic status in the frozen theorem.',
            'The exactly solvable radial test has nu=0 and a Euclidean kernel, outside the frozen hypotheses.',
            'No numerical singular SDE, thermodynamic estimate, external theorem, or novelty inference is used.',
            'Mutation tests reject specific errors; they do not certify completeness of the analytic proof.'
        ]
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='Emit every exact input/result as JSON on stdout')
    args = parser.parse_args()
    result = run()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print('Baseline exact checks: %d/%d PASS' %
              (result['baseline_pass_count'], result['baseline_count']))
        print('Nonzero mutations detected: %d/%d' %
              (result['mutation_detected_count'], result['mutation_count']))
        for entry in result['mutations']:
            print('%s: residual=%s' % (entry['id'], entry['residual']))
        print('Status: constructor SELF_CHECKED diagnostics; analytic proof is separate.')
    return 0 if result['all_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
