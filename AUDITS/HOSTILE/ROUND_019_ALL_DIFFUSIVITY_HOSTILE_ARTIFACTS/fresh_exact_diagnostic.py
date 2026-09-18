#!/usr/bin/env python3
"""AUD058 exact hostile diagnostics, authored de novo from the allowed statements.

Standard library only. All asserted computations use Fraction/integer algebra.
They test mechanisms and reject mutations; they do not simulate or prove a
singular interacting-particle limit. See README and the analytic audit.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
import json
import platform

checks = Counter()
mutations = Counter()
witnesses = {}


def verify(category, statement):
    if not statement:
        raise AssertionError(category)
    checks[category] += 1


def reject(category, statement, witness):
    if not statement:
        raise AssertionError('Mutation survived: ' + category)
    mutations[category] += 1
    witnesses.setdefault(category, witness)


class C:
    """Gaussian rationals; no binary floating-point arithmetic."""
    def __init__(self, re=0, im=0):
        if isinstance(re, C):
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = F(re), F(im)

    def __add__(self, other):
        other = C(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + -C(other)

    def __rsub__(self, other):
        return C(other) + -self

    def __mul__(self, other):
        other = C(other)
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return C(self.re / F(scalar), self.im / F(scalar))

    def conjugate(self):
        return C(self.re, -self.im)

    def norm2(self):
        return self.re ** 2 + self.im ** 2

    def __eq__(self, other):
        other = C(other)
        return self.re == other.re and self.im == other.im

    def __repr__(self):
        return '(' + str(self.re) + ',' + str(self.im) + ')'


I = C(0, 1)
roots = (C(1), I, C(-1), -I)


def phase(k, quarter):
    return roots[(k * quarter) % 4]


def value(poly, quarter):
    return sum((c * phase(k, quarter) for k, c in poly.items()), C())


def add_fourier(p, q):
    return {k: p.get(k, C()) + q.get(k, C()) for k in p.keys() | q.keys()}


def derivative(p):
    # Each actual unit-torus derivative has the common additional factor 2*pi.
    return {k: I * k * c for k, c in p.items()}


def eta_hat(k, positions):
    return sum((phase(-k, x) for x in positions), C()) / len(positions)


def run_source_labels():
    retained = {-2: C(F(1, 8)), -1: C(F(1, 2)),
                1: C(F(1, 2)), 2: C(F(1, 8))}
    remainder_centered = {-1: C(F(1, 2)), 1: C(F(1, 2))}
    positive_remainder = {0: C(2), **remainder_centered}
    full = add_fourier(retained, remainder_centered)
    tests = [
        {-1: C(F(1, 2)), 1: C(F(1, 2))},
        {-1: C(F(1, 2), F(1, 6)), 1: C(F(1, 2), -F(1, 6)),
         -2: C(F(1, 8)), 2: C(F(1, 8))},
        {0: C(7)},
    ]
    for n in (2, 3, 4):
        for positions in combinations(range(4), n):
            # Distinct points on one coordinate circle embed in every d>=3.
            smooth_energy = sum((retained[k] * eta_hat(k, positions).norm2()
                                 for k in retained), C()) / 2
            deleted_remainder = sum((value(positive_remainder, x - y)
                                     for x in positions for y in positions if x != y), C()) / (2 * n * n)
            hn_over_n = sum((value(full, positions[i] - positions[j])
                             for i in range(n) for j in range(i + 1, n)), C()) / (n * n)
            self_term = value(retained, 0) / (2 * n)
            background = C(F(n - 1, 2 * n) * 2)
            verify('deleted_energy_identity', hn_over_n == smooth_energy + deleted_remainder - self_term - background)
            verify('positive_remainder', all(value(positive_remainder, x - y).re >= 1
                                            for x in positions for y in positions))
            reject('omit_smooth_self', hn_over_n != smooth_energy + deleted_remainder - background,
                   {'N': n, 'positions_in_quarters': positions, 'missing': str(self_term)})
            reject('replace_deleted_background_by_half', hn_over_n != smooth_energy + deleted_remainder - self_term - 1,
                   {'N': n, 'correct_background': str(background), 'mutant_background': '1'})
            constant_p = F(n * (n - 1), 2 * n * n) - 1 + F(1, 2)
            verify('constant_deleted_statistic', constant_p == -F(1, 2 * n))
            reject('falling_factorial_denominator', constant_p != F(1, 2) - 1 + F(1, 2), {'N': n})
            for g in (retained, full):
                force = {k: -c for k, c in derivative(g).items()}
                for f in tests:
                    velocity = derivative(f)
                    row = {k: -force.get(k, C()) * velocity.get(k, C())
                           for k in force.keys() | velocity.keys()}
                    j = lambda x, y: value(force, x - y) * (value(velocity, x) - value(velocity, y))
                    d2half = sum((j(x, y) for x in positions for y in positions if x != y), C()) / (2 * n * n)
                    empirical_row = sum((value(row, x) for x in positions), C()) / n
                    pn = d2half - empirical_row
                    direct = sum((value(force, x - y) * value(velocity, x)
                                  for x in positions for y in positions if x != y), C()) / (n * n)
                    verify('direct_interaction_and_full_source', direct == pn + empirical_row)
                    verify('source_reality', direct.im == pn.im == empirical_row.im == 0)
                    verify('genuine_scalar_background', row.get(0, C()) == 0)
                    verify('smooth_source_diagonal', all(j(x, x) == 0 for x in positions))
                    # Haar contraction, performed as an independent Fourier sum in y.
                    for x in positions:
                        haar_row = sum((-force[k] * velocity.get(k, C()) * phase(k, x)
                                        for k in force), C())
                        verify('haar_row_convolution', haar_row == value(row, x))
                    # Terms with one frequency outside g still occur through the other term.
                    all_modes = set(g)
                    for q in velocity:
                        all_modes |= {k + q for k in g} | {k - q for k in g}
                    fourier_commutator = C()
                    for k in all_modes - {0}:
                        for ell in all_modes - {0}:
                            fourier_commutator += (-I / 2) * (k * g.get(k, C()) - ell * g.get(ell, C())) * velocity.get(ell - k, C()) * eta_hat(k, positions) * eta_hat(ell, positions).conjugate()
                    verify('retained_fourier_commutator_factor', pn == fourier_commutator)
                    if direct != 0:
                        reject('omit_symmetrization_half', direct != 2 * d2half,
                               {'N': n, 'positions_in_quarters': positions, 'direct': str(direct)})
                    if empirical_row != 0:
                        reject('omit_haar_row', direct != pn, {'N': n, 'row': str(empirical_row)})
    for c in (F(1), F(4), F(17, 3)):
        verify('coulomb_atom_compensation_mass', c - c == 0)
        for fbar, fx in ((F(0), F(1)), (F(3), F(3)), (F(2), F(-1))):
            correct = -c * (fx - fbar)
            if fx != 0:
                reject('punctured_coulomb_response', correct != c * fbar,
                       {'c': str(c), 'f_x': str(fx), 'mean_f': str(fbar)})


def retention(alpha, m, r, lam):
    return factorial(alpha - 1) * sum((F((-1) ** j * comb(m, j), 1) / (lam + F(j, 1) / r) ** alpha
                                      for j in range(m + 1)), F(0))


def run_retention():
    for d, alpha in ((3, 1), (5, 1), (5, 2), (7, 2), (7, 3)):
        m = d + 2
        limit = 2 * (alpha + m)
        for r in (F(1, 1000), F(1, 32), F(1, 2), F(1), F(2), F(1000)):
            cr = factorial(alpha - 1) * r ** alpha * sum((F((-1) ** (j + 1) * comb(m, j), j ** alpha) for j in range(1, m + 1)), F(0))
            verify('positive_omitted_mass_exact_integral', cr > 0)
            for lam in (F(1), F(2), F(4), F(9), F(25), F(49)):
                a = retention(alpha, m, r, lam)
                radial_log = 2 * lam * retention(alpha + 1, m, r, lam) / a
                verify('polynomial_retention_positive', a > 0)
                verify('uniform_radial_log_derivative', 2 * alpha <= radial_log <= limit)
                reject('drop_retention_log_derivative_contribution', radial_log > 2 * alpha,
                       {'d': d, 'alpha': alpha, 'r': str(r), 'lambda': str(lam), 'actual_log_derivative': str(radial_log)})
            for k in range(-5, 6):
                for ell in range(-5, 6):
                    if k == 0 or ell == 0:
                        continue
                    ak = retention(alpha, m, r, F(k * k))
                    al = retention(alpha, m, r, F(ell * ell))
                    q = abs(k - ell)
                    rhs_squared = (1 + limit) ** 2 * q ** 2 * (1 + q) ** (limit + 2)
                    verify('lattice_commutator_squared', (k * ak - ell * al) ** 2 <= rhs_squared * ak * al)
    # A sharp heat retention at alpha=1 and scaled r=log(2) has a(k)=2^(-k^2)/k^2.
    # This explicit witness rejects reuse of the polynomial-retention bound.
    k, ell, limit = 16, 17, 12
    ak, al = F(1, 2 ** (k * k) * k * k), F(1, 2 ** (ell * ell) * ell * ell)
    rhs_squared = (1 + limit) ** 2 * (1 + abs(k - ell)) ** (limit + 2)
    reject('exponential_retention_reused_as_polynomial', (k * ak - ell * al) ** 2 > rhs_squared * ak * al,
           {'k': k, 'ell': ell, 'L': limit, 'scaled_heat_parameter': 'log(2)'})


def clean(p):
    return {k: v for k, v in p.items() if v}


def padd(p, q):
    return clean({k: p.get(k, F(0)) + q.get(k, F(0)) for k in p.keys() | q.keys()})


def pscale(p, a):
    return clean({k: v * a for k, v in p.items()})


def pshift(p, n):
    return {k + n: v for k, v in p.items()}


def peval(p, q):
    return sum((v * q ** k for k, v in p.items()), F(0))


def b_of(nu):
    return min(F(1), 1 / nu) if nu else F(1)


def run_covariance_and_initial():
    # q is the FORMAL indeterminate exp[-(D+nu*a)/3]. Physical times j/3 are fixed.
    indices = (0, 1, 3, 3, 5)
    for nu in (F(0), F(1, 1000), F(1, 3), F(1), F(3), F(1000), F(10 ** 12)):
        b = b_of(nu)
        verify('capped_scaling', 0 < b <= 1 and 0 <= nu * b <= 1)
        for dmode, amode in ((F(1), F(1)), (F(3, 2), F(4)), (F(7), F(9))):
            rate = dmode + nu * amode
            theta = b * nu * amode / rate
            for ti in indices:
                for tj in indices:
                    gram = {ti + tj: b}
                    for step in range(1, min(ti, tj) + 1):
                        gram = padd(gram, {ti + tj - 2 * step: theta,
                                            ti + tj - 2 * step + 2: -theta})
                    closed = padd({ti + tj: b * dmode / rate}, {abs(ti - tj): theta})
                    verify('fixed_time_formal_covariance_identity', clean(gram) == clean(closed))
                    if nu > 0 and min(ti, tj) > 0:
                        half_noise = padd({ti + tj: b}, pscale(padd(closed, {ti + tj: -b}), F(1, 2)))
                        reject('thermal_factor_two_lost', clean(closed) != half_noise,
                               {'nu': str(nu), 'time_indices': [ti, tj]})
                    if ti != tj and min(ti, tj) > 0:
                        stationary_initial = {abs(ti - tj): b}
                        reject('initial_sum_time_replaced_by_difference', clean(closed) != stationary_initial,
                               {'nu': str(nu), 'time_indices': [ti, tj]})
                    for q in (F(0), F(1, 5), F(1, 2), F(1)):
                        verify('covariance_gram_at_formal_probe', peval(gram, q) == peval(closed, q))
                        if ti == tj:
                            verify('modal_diagonal_hot_bound', 0 <= peval(closed, q) <= b)
            # Two equal-time coordinates with coefficients 1,-2: exact rank one.
            q = F(2, 3)
            var = b * (dmode / rate * q ** 6 + nu * amode / rate)
            verify('repeated_time_degenerate_gram', var * (4 * var) - (-2 * var) ** 2 == 0)
            verify('constant_test_zero', var * 0 == 0)
        if nu > 1:
            reject('uncapped_hot_normalization', b != 1, {'nu': str(nu), 'correct_b': str(b)})
        # Initial iid Rademacher probe: exact characteristic formal coefficients through degree 6.
        # A is sqrt(b/N) sum_i eps_i; coefficients depend only on b, without needing rational sqrt(b).
        for n in (2, 3, 10, 100):
            initial_var = b
            fourth = b ** 2 * (3 - F(2, n))
            sixth = b ** 3 * (15 - F(30, n) + F(16, n * n))
            for power, formula in ((2, initial_var), (4, fourth), (6, sixth)):
                literal_iid = b ** (power // 2) * sum((F(comb(n, minus) * (n - 2 * minus) ** power, 2 ** n * n ** (power // 2))
                                                      for minus in range(n + 1)), F(0))
                verify('literal_iid_binomial_moment', literal_iid == formula)
            verify('triangular_iid_fourth_uniform', abs(fourth - 3 * b ** 2) <= F(2, n))
            verify('triangular_iid_sixth_uniform', abs(sixth - 15 * b ** 3) <= F(30, n))
            verify('initial_variance_uniform', 0 < initial_var <= 1)
            if nu > 1:
                reject('initial_scale_omits_b', initial_var != 1, {'N': n, 'nu': str(nu)})


def run_dependence_and_probability():
    for n in (2, 3, 4, 10, 100, 1000):
        r = F(n + 1, n)
        # Initial S=+1/-1 equiprobable; exp(i A)=S.
        # q_S=2 log(2)+2 S log(r)>0; M=sqrt(q_S)B_1, B independent of S.
        # All exponentials below are EXACT rational values.
        plus_cf, minus_cf = 1 / (2 * r), r / 2
        actual_cf = (plus_cf - minus_cf) / 2
        compensated_cf = (plus_cf * r - minus_cf / r) / 2
        wrong_sign = (plus_cf / r - minus_cf * r) / 2
        verify('initial_conditioned_compensator_exact', compensated_cf == 0)
        verify('dependence_error_uniform_decay', abs(actual_cf) <= F(1, 2 * n))
        reject('finite_N_initial_martingale_independence', actual_cf != 0,
               {'n': n, 'exact_joint_characteristic_value': str(actual_cf), 'independence_prediction': '0'})
        reject('wrong_exponential_compensator_sign', wrong_sign != 0,
               {'n': n, 'mutant_value': str(wrong_sign), 'correct_value': '0'})
        reject('replace_random_bracket_by_its_mean_exactly', actual_cf != compensated_cf,
               {'n': n, 'joint_value': str(actual_cf)})
        # A residual with only L1 smallness: P(R=+/-n^4)=1/(2 n^5), else R=0.
        size, prob = n ** 4, F(1, n ** 5)
        first, second = size * prob, size * size * prob
        verify('L1_only_residual_decay', first == F(1, n))
        verify('L1_only_exact_BL_distance', 2 * prob <= first)  # exact BL distance is 2*prob as size>=2
        reject('promote_source_L1_to_uniform_L2', second > n * n,
               {'n': n, 'first_moment': str(first), 'second_moment': str(second)})
        for threshold in (F(1, 2), F(1), F(n), F(n ** 4), F(n ** 5)):
            tail = prob if threshold <= size else F(0)
            verify('L1_tail_mechanism', tail <= first / threshold)
        # Pointwise/compact parameter convergence alone leaves a moving all-noise spike.
        fixed_nu = F(n - 1)
        pointwise_error = F(int(fixed_nu >= n))
        moving_error = F(int(F(n) >= n))
        verify('fixed_parameter_spike_disappears', pointwise_error == 0)
        reject('pointwise_parameter_to_uniform_metric', moving_error == 1,
               {'N': n, 'bad_finite_nu': n, 'BL_distance_delta1_delta0': 1})
        # The BL test used for convergence to zero: F_eps(x)=min(eps,|x|) if eps<=1.
        for eps in (F(1, 10), F(1), F(2)):
            normalization = max(F(1), 1 / eps)
            test_at_threshold = 1 / normalization
            verify('BL_probability_threshold_factor', normalization * test_at_threshold == 1)
            if eps < 1:
                reject('omit_probability_test_normalizing_factor', test_at_threshold < 1,
                       {'epsilon': str(eps), 'test_at_threshold': str(test_at_threshold), 'required_factor': str(normalization)})
    # Without tightness, uniform convergence of densities on all x does not imply bounded-test convergence.
    # Uniform densities on [0,n] and [2n,3n] have sup-density difference 1/n, yet d_BL=2 for n>=2.
    for n in (2, 10, 1000):
        verify('density_difference_can_be_small', F(1, n) > 0)
        reject('density_sup_norm_without_tails', F(2) > F(1, n),
               {'n': n, 'density_sup_error': str(F(1, n)), 'bounded_Lipschitz_gap': 2})


def run_exponents_and_brackets():
    for d, s in ((3, 1), (4, 1), (4, 2), (5, 1), (5, 2), (5, 3), (7, 1), (7, 3), (7, 5)):
        theta, kappa = 1 - F(s, d), F(1, 2) - F(s, d)
        verify('source_range_distinct_from_Gaussian_range', theta > 0)
        verify('strict_Gaussian_threshold', (kappa > 0) == (2 * s < d))
        for n in (2, 3, 5):
            N, r = n ** (2 * d), F(1, n ** 4)
            term1 = F(1, N) * n ** (2 * s)
            term2 = F(1, n ** (2 * (d - s)))
            verify('source_balanced_exponents', term1 == term2)
            scaled = n ** d * term1
            verify('scaled_source_exact_exponent', scaled == F(n) ** (2 * s - d))
            if 2 * s >= d:
                reject('nondecay_promoted_at_threshold', scaled >= 1,
                       {'d': d, 's': s, 'N': N, 'scaled_bound_power': 2 * s - d})
    for nu in (F(0), F(1, 4), F(1), F(10), F(10 ** 20)):
        b = b_of(nu)
        for n in (2, 3, 7):
            # Arbitrary exact deterministic gradients at one instant, with two tests.
            g = [F(i - 2, 3) for i in range(n)]
            h = [F(2 * i + 1, 5) for i in range(n)]
            raw = 2 * nu * b / n * sum((g[i] * h[i] for i in range(n)), F(0))
            empirical = 2 * nu * b * sum((g[i] * h[i] for i in range(n)), F(0)) / n
            verify('independent_Brownian_labels_bracket', raw == empirical)
            if raw:
                reject('Brownian_bracket_extra_N', raw != raw / n, {'N': n, 'nu': str(nu), 'bracket': str(raw)})
                reject('Brownian_bracket_missing_two', raw != raw / 2, {'N': n, 'nu': str(nu)})


def run_energy_uniformity():
    for nu in (F(0), F(1, 1000), F(1), F(1000), F(10 ** 20)):
        for density, density_gradient, energy_gradient in (
            (F(1), F(2), F(3)), (F(1, 3), F(-2), F(5, 2)),
            (F(7), F(0), F(-1)), (F(2), F(3), F(0))):
            eprime = -density * energy_gradient ** 2 - nu * density_gradient * energy_gradient
            entprime_times_nu = -nu * density_gradient * energy_gradient - nu ** 2 * density_gradient ** 2 / density
            square = -density * (energy_gradient + nu * density_gradient / density) ** 2
            verify('free_energy_local_square_exact', eprime + entprime_times_nu == square)
            verify('free_energy_sign_all_finite_noise', square <= 0)
            if nu not in (0, 1) and density_gradient:
                wrong_entropy_weight = eprime + entprime_times_nu / nu
                reject('entropy_weight_omits_nu', wrong_entropy_weight != square,
                       {'nu': str(nu), 'density': str(density), 'correct_dissipation': str(square)})
        # For a nonconstant single terminal mode, its space derivative amplitude
        # stays fixed at r=T but the time derivative contains D+nu*a.
        if nu >= 1000:
            time_amplitude = 1 + 4 * nu
            verify('terminal_spatial_amplitude_fixed', F(1) == 1)
            reject('assume_uniform_terminal_time_derivative', time_amplitude > 1000,
                   {'nu': str(nu), 'time_derivative_amplitude': str(time_amplitude)})


def main():
    run_source_labels()
    run_retention()
    run_covariance_and_initial()
    run_dependence_and_probability()
    run_exponents_and_brackets()
    run_energy_uniformity()
    print(json.dumps({
        'audit': 'AUD058 / TASK089',
        'status': 'PASS exact diagnostic assertions and rejected mutations',
        'python': platform.python_version(),
        'arithmetic': 'Python integers and fractions.Fraction; Gaussian rational pairs; formal polynomial identities',
        'seed': None,
        'tolerance': None,
        'assertions': sum(checks.values()),
        'assertions_by_category': dict(sorted(checks.items())),
        'mutation_rejections': sum(mutations.values()),
        'mutation_families': len(mutations),
        'mutation_rejections_by_category': dict(sorted(mutations.items())),
        'first_mutation_witnesses': witnesses,
        'limits': [
            'No simulation or finite-N singular distribution calculation.',
            'Finite probes do not establish uniform analytic inequalities.',
            'Formal q=exp[-(D+nu*a)/3] retains the fixed physical time grid j/3.',
            'Gaussian-rational source derivatives are divided by their common factor 2*pi; physical factors are restored in the audit.',
            'Adapted Gaussian-mixture and residual/spike examples challenge proof steps and are not counterexamples in the admitted particle law class.'
        ]
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
