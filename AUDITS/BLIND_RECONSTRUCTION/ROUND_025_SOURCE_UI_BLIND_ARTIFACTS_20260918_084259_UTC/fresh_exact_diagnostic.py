#!/usr/bin/env python3
"""Fresh standard-library rational diagnostics for AUD069.

These finite algebraic models are supporting checks, not a proof of the
singular stochastic estimates. No previous checker or external input is read.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        if not isinstance(other, C):
            other = C(F(other))
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, C):
            other = C(F(other))
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self):
        return C(self.re, -self.im)

    def norm2(self):
        return self.re**2 + self.im**2


counts = {}
mutations = {}
details = {}


def check(category, condition):
    if not condition:
        raise AssertionError(category)
    counts[category] = counts.get(category, 0) + 1


def mutant(name, actual, changed):
    if actual != changed:
        mutations[name] = mutations.get(name, 0) + 1


def heat_splitting():
    for z in [F(1, 7), F(1, 2), F(1), F(3, 2), F(7), F(19), F(101)]:
        integral = sum(F((-1)**j * comb(6, j), 1) / (z + j)
                       for j in range(7))
        denominator = F(1)
        for j in range(7):
            denominator *= z + j
        closed = F(factorial(6)) / denominator
        check('heat_beta_identity', integral == closed > 0)
        derivative = -sum(F((-1)**j * comb(6, j), 1) / (z + j)**2
                          for j in range(7))
        log_slope = -2 * z * derivative / integral
        direct = 2 * sum(z / (z + j) for j in range(7))
        check('heat_log_slope_identity', log_slope == direct)
        check('heat_log_slope_bound', 2 <= log_slope <= 14)
        mutant('omit_heat_factorial', integral, F(1) / denominator)
    mass = sum(F((-1)**(j + 1) * comb(6, j), j) for j in range(1, 7))
    check('positive_remainder_mass', mass == sum(F(1, j) for j in range(1, 7)) == F(49, 20))
    details['heat_mass_over_cr'] = str(mass)


def initial_truncation():
    # Independent uniform points on Z/5Z. This is a finite exact Haar proxy,
    # not a singular periodic particle simulation.
    g = [F(20), F(2), F(-12), F(-12), F(2)]
    check('finite_group_zero_mean', sum(g) == 0)
    rows = []
    for cap in (3, 7, 17):
        truncated = [min(x, F(cap)) for x in g]
        mean = sum(truncated) / 5
        second = sum(x*x for x in truncated) / 5
        for fixed in range(5):
            row = sum(truncated[(fixed-y) % 5] for y in range(5)) / 5
            check('constant_conditional_row', row == mean)
        shared_raw = sum(truncated[(x-y) % 5] * truncated[(x-z) % 5]
                         for x, y, z in product(range(5), repeat=3)) / 125
        check('shared_label_centered_covariance', shared_raw == mean*mean)
        mutant('assume_raw_shared_product_zero', shared_raw, F(0))
        for n in (2, 3, 4, 5):
            sum_h = F(0)
            sum_h2 = F(0)
            configurations = 5**n
            for x in product(range(5), repeat=n):
                energy = sum(truncated[(x[i]-x[j]) % 5]
                             for i in range(n) for j in range(i+1, n)) / n
                sum_h += energy
                sum_h2 += energy**2
            eh = sum_h / configurations
            eh2 = sum_h2 / configurations
            expected_mean = F(n-1, 2) * mean
            variance = F(n-1, 2*n) * (second-mean*mean)
            check('truncated_energy_mean', eh == expected_mean)
            check('truncated_energy_variance', eh2-eh*eh == variance)
            check('truncated_energy_second_moment', eh2 == variance+expected_mean**2)
            mutant('omit_truncated_bias', eh2, variance)
            mutant('replace_energy_N_by_N_squared', eh2, eh2/F(n*n))
            rows.append({'N':n, 'cap':cap, 'mean':str(eh), 'variance':str(variance)})
    details['truncated_iid_exact_cases'] = rows


def literal_fourier_source():
    # g(x)=cos(2pi*x), e=exp(2pi*i*x). Divide force/source generators by
    # c=(2pi)^2. The response multiplier is d=1/2 for this smooth probe.
    e = [C(F(1)), C(F(0), F(1)), C(F(-1)), C(F(0), F(-1))]
    sine = [F(0), F(1), F(0), F(-1)]
    imaginary = C(F(0), F(1))
    d = F(1, 2)

    def jraw(x, y):
        return imaginary * sine[(x-y) % 4] * (e[x]-e[y])

    for x in range(4):
        row = sum((jraw(x, y) for y in range(4)), C()) * F(1, 4)
        check('literal_haar_row', row == e[x]*(-d))
        mutant('wrong_row_sign', row, e[x]*d)
    for n in (2, 3, 4):
        for x in product(range(4), repeat=n):
            z = sum((e[y] for y in x), C()) * F(1, n)
            raw = sum((jraw(x[i], x[j]) for i in range(n)
                       for j in range(n) if i != j), C()) * F(1, 2*n*n)
            u = sum((jraw(x[i], x[j])+d*(e[x[i]]+e[x[j]])
                     for i in range(n) for j in range(n) if i != j), C()) * F(1, 2*n*n)
            direct = sum((imaginary * e[x[i]] * sine[(x[i]-x[j]) % 4]
                          for i in range(n) for j in range(n) if i != j), C()) * F(1, n*n)
            p = raw+d*z
            check('ordered_pair_symmetrization', raw == direct)
            check('literal_finite_label_correction', p == u+F(1, n)*d*z)
            mutant('omit_finite_label_correction', p, u)
            mutant('omit_pair_half', direct, 2*raw)
            for nu in (F(0), F(1, 7), F(2)):
                drift = -nu*z+direct
                alternative = -(nu+d-d/F(n))*z+u
                check('shifted_modal_drift', drift == alternative)
                mutant('use_unshifted_modal_drift', drift, -(nu+d)*z+u)


def label_overlaps():
    for n in range(2, 16):
        two = 0
        three = 0
        for i, j, ell in product(range(n), repeat=3):
            if i == j:
                continue
            if ell == i or ell == j:
                two += 1
            else:
                three += 1
        # N * (1/(2N^2)) * (1/N) is 1/(2N^2).
        coeff2 = F(two, 2*n*n)
        coeff3 = F(three, 2*n*n)
        check('two_label_overlap', coeff2 == F(n-1, n))
        check('three_label_overlap', coeff3 == F((n-1)*(n-2), 2*n))
        check('all_label_count', two+three == n*n*(n-1))
        if n == 2:
            check('N2_no_third_particle', three == 0)
        mutant('missing_overlap_two', coeff2, F(n-1, 2*n))
        mutant('replace_N_minus_2_by_N', coeff3, F((n-1)*n, 2*n))


def moment_identity():
    for E, A, noise, f, g in product(
            (F(1, 3), F(3, 4)), (F(1, 5), F(1, 2)),
            (F(1, 7), F(2, 3)), (F(-2, 5), F(3, 7)),
            (C(F(1, 9), F(1, 3)), C(F(-2, 11), F(-1, 5)))):
        v = E*E+noise+2*f
        q = C(E)+g
        direct = v+A*A-2*A*q.re
        r = C(f)-g*A
        formula = (E-A)**2+noise+2*r.re
        check('endpoint_moment_expansion', direct == formula)
        mutant('missing_noise_factor', direct, (E-A)**2+noise/F(2)+2*r.re)
        mutant('omit_current_initial_correlation', direct, (E-A)**2+noise+2*f)
    for nu in (F(1, 13), F(1), F(3)):
        for n in range(2, 11):
            ell = F(7)
            complex_norm_bracket = F(2)*nu*ell/n
            real_cos_plus_sin = sum(F(2)*nu*ell/n * F(1, 2) for _ in range(2))
            check('complex_noise_bracket', complex_norm_bracket == real_cos_plus_sin)
            mutant('complex_noise_missing_two', complex_norm_bracket, nu*ell/n)


def conditioning_and_noise_cross():
    em = F(0)
    eb = F(0)
    emean = F(0)
    anticipative_mean = F(0)
    source_cross = F(0)
    square_direct = F(0)
    false_sum = F(0)
    for initial, xi, eta in product((0, 1), (-1, 1), (-1, 1)):
        weight = F(1, 8)
        m = (1+initial)*xi+xi*eta
        bracket = (1+initial)**2+xi**2
        if initial:
            em += weight*m*m
            eb += weight*bracket
            emean += weight*m
        if xi == 1:
            anticipative_mean += weight*m
        s = xi
        noise = xi+eta
        source_cross += weight*s*noise
        square_direct += weight*(s+noise)**2
        false_sum += weight*(s*s+noise*noise)
    check('initial_event_conditional_isometry', em == eb == F(5, 2))
    check('initial_event_conditional_mean', emean == 0)
    check('anticipative_event_warning', anticipative_mean != 0)
    check('source_noise_cross_not_zero', source_cross == 1)
    check('source_noise_cross_retained', square_direct == false_sum+2*source_cross == 5)
    mutant('silently_drop_source_noise_cross', square_direct, false_sum)
    details['conditioning'] = {'conditional_second_moment':str(em),
                               'anticipative_mean':str(anticipative_mean),
                               'nonzero_source_noise_cross':str(source_cross)}


def singular_powers_and_rare_event():
    check('instantaneous_square_log_divergence', 4-1-2*2 == -1)
    check('initial_energy_first_moment_integrable', 4-1-2 > -1)
    for n in range(2, 101):
        cutoff = F(n*n)
        pareto_tail_union = F(n*(n-1), 2) / cutoff**2
        check('rare_event_probability_power', pareto_tail_union <= F(1, 2*n*n))
        check('rare_event_endpoint_square_power', n*pareto_tail_union <= F(1, 2*n))
        truncated_bias = F(n-1, 2) / cutoff
        check('truncated_bias_power', truncated_bias**2/n <= F(1, 4*n**3))
        mutant('cut_pairs_at_N_instead_of_N_squared', pareto_tail_union,
               F(n*(n-1), 2)/F(n*n))
    for n, radius_squared, terminal_root in product(
            (2, 3, 7), (F(1, 4), F(1), F(2)), (F(3), F(4))):
        T = F(n, 16)*(terminal_root**2-radius_squared**2)
        fourth_power = radius_squared**2+F(16, n)*T
        integral = F(n, 8)*(terminal_root-radius_squared)
        check('principal_pair_flow', fourth_power == terminal_root**2)
        check('principal_pair_integral', F(8, n)*integral == terminal_root-radius_squared)
        mutant('wrong_relative_force_two', fourth_power, radius_squared**2+F(8, n)*T)
    details['singular_test_scope'] = 'Principal-part zero-noise diagnostic only; actual proof uses localization and endpoint duality.'


def main():
    for routine in (heat_splitting, initial_truncation, literal_fourier_source,
                    label_overlaps, moment_identity, conditioning_and_noise_cross,
                    singular_powers_and_rare_event):
        routine()
    required_mutants = {
        'omit_heat_factorial', 'assume_raw_shared_product_zero', 'omit_truncated_bias',
        'replace_energy_N_by_N_squared', 'wrong_row_sign', 'omit_finite_label_correction',
        'omit_pair_half', 'use_unshifted_modal_drift', 'missing_overlap_two',
        'replace_N_minus_2_by_N', 'missing_noise_factor', 'omit_current_initial_correlation',
        'complex_noise_missing_two', 'silently_drop_source_noise_cross',
        'cut_pairs_at_N_instead_of_N_squared', 'wrong_relative_force_two'
    }
    assert set(mutations) == required_mutants
    assert all(value > 0 for value in mutations.values())
    report = {
        'status':'PASS', 'arithmetic':'exact rational and Gaussian rational',
        'random_seed':None, 'external_dependencies':[],
        'source_reads':'This fresh script only; no earlier checker or external mathematical input.',
        'diagnostic_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'total_assertions':sum(counts.values()), 'categories':counts,
        'mutation_nonzero_case_counts':mutations, 'details':details,
        'limitations':'These checks support finite algebra and scaling. They do not certify singular SDE limits or prove source decay.'
    }
    output = json.dumps(report, indent=2, sort_keys=True)+'\n'
    if len(sys.argv) == 3 and sys.argv[1] == '--output':
        Path(sys.argv[2]).write_text(output)
    elif len(sys.argv) != 1:
        raise SystemExit('Usage: fresh_exact_diagnostic.py [--output RESULTS.json]')
    print(output, end='')


if __name__ == '__main__':
    main()
