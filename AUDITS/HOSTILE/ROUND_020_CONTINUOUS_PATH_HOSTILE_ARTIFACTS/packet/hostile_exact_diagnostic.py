#!/usr/bin/env python3
"""AUD060 fresh exact controls; stdout only; no old checker or source imports.

The continuum Volterra tests use Brownian isometry on polynomial kernels.
Finite Fourier and abstract Gram examples check coefficients, not singular
particle estimates. All arithmetic is rational; no samples or tolerances.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json

counts = {}
mutations = {}
witnesses = {}


def enc(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def check(category, statement):
    if not statement:
        raise AssertionError(category)
    counts[category] = counts.get(category, 0) + 1


def reject(name, correct, mutant, case):
    check('mutation_' + name, correct != mutant)
    mutations[name] = enc({'correct': correct, 'mutant': mutant, 'case': case})


def integral_product(p, q, left, right):
    return sum((a * b * (right ** (i + j + 1) - left ** (i + j + 1))
                / F(i + j + 1) for i, a in enumerate(p)
                for j, b in enumerate(q)), F(0))


def kernel(t, lam):
    return [1 - lam * t, lam]


def volterra_cov(t, u, lam):
    return integral_product(kernel(t, lam), kernel(u, lam), F(0), min(t, u))


def brownian_integral_cov(t, u):
    # Cov(B_t, integral_0^u B_r dr), from the min kernel.
    if t >= u:
        return u * u / 2
    return t * u - t * t / 2


def area_area_cov(t, u):
    hi, lo = max(t, u), min(t, u)
    return hi * lo * lo / 2 - lo ** 3 / 6


# A continuum stochastic convolution with a nonexponential, exactly integrable
# kernel. Its two constructions are M_t=int(1-lambda(t-r))dB_r and
# B_t-lambda int_0^t B_r dr. This tests terminal-time memory, not just a modal
# covariance formula copied from the candidate.
times = [F(0), F(1, 8), F(1, 3), F(1, 2), F(1), F(2)]
for lam in [F(0), F(1, 4), F(1), F(3, 2)]:
    for t, u in product(times, repeat=2):
        by_parts = (min(t, u) - lam * (brownian_integral_cov(t, u)
                    + brownian_integral_cov(u, t))
                    + lam * lam * area_area_cov(t, u))
        check('continuum_volterra_two_constructions', volterra_cov(t, u, lam) == by_parts)
        check('continuum_covariance_symmetry', by_parts == volterra_cov(u, t, lam))
        hi, lo = max(t, u), min(t, u)
        delta = hi - lo
        old = lam * lam * delta * delta * lo
        recent = delta - lam * delta * delta + lam * lam * delta ** 3 / 3
        actual = volterra_cov(t, t, lam) + volterra_cov(u, u, lam) - 2 * by_parts
        check('continuum_old_and_recent_noise', actual == old + recent)
        check('continuum_increment_nonnegative', actual >= 0)
        # On [0,2], a deterministic bracket-density majorant gives C*delta.
        envelope = (lam * delta) ** 2 * lo + (1 + 2 * lam) ** 2 * delta
        check('continuum_increment_majorant', actual <= envelope)
    for horizon in times:
        # The time integral of M has stochastic kernel w-lambda*w^2/2.
        k = [horizon - lam * horizon * horizon / 2,
             -1 + lam * horizon, -lam / 2]
        impulse = integral_product(k, k, F(0), horizon)
        temporal = horizon ** 3 / 3 - lam * horizon ** 4 / 4 + lam * lam * horizon ** 5 / 20
        check('continuum_integrated_path_functional', impulse == temporal)
        check('continuum_integrated_variance_nonnegative', impulse >= 0)
    # Three-time arbitrary linear combinations: split the Brownian integral at
    # every terminal time and integrate its squared combined kernel directly.
    grid = [F(0), F(1, 4), F(3, 4), F(1)]
    for weights in [(1, -2, 1), (2, 0, -1), (0, 0, 0), (1, 1, 1)]:
        c = sum((F(weights[i] * weights[j]) * volterra_cov(grid[i+1], grid[j+1], lam)
                 for i, j in product(range(3), repeat=2)), F(0))
        squared = F(0)
        for left, right in zip(grid[:-1], grid[1:]):
            active = [j for j in range(3) if grid[j+1] >= right]
            p = [sum((F(weights[j]) * kernel(grid[j+1], lam)[a] for j in active), F(0))
                 for a in range(2)]
            squared += integral_product(p, p, left, right)
        check('continuum_path_functional_gram', c == squared)
        check('continuum_path_functional_psd', squared >= 0)

lam, t, u = F(1), F(1), F(1, 2)
delta = t - u
actual = volterra_cov(t, t, lam) + volterra_cov(u, u, lam) - 2 * volterra_cov(t, u, lam)
recent = delta - lam * delta * delta + lam * lam * delta ** 3 / 3
reject('delete_earlier_noise', actual, recent, {'lambda': lam, 't': t, 'u': u})
reject('treat_convolution_as_martingale', volterra_cov(t, u, lam), volterra_cov(u, u, lam),
       {'lambda': lam, 't': t, 'u': u})
reject('erase_path_integral_memory', integral_product([F(1, 2), F(0), F(-1, 2)],
                                                     [F(1, 2), F(0), F(-1, 2)], F(0), F(1)),
       integral_product([F(1), F(-1)], [F(1), F(-1)], F(0), F(1)), {'T': 1, 'lambda': 1})


# Smooth Fourier coefficient tests. Angle derivative means physical derivative
# divided by 2*pi. Four-point Haar quadrature is exact here (frequencies <=2).
cosine = [F(1), F(0), F(-1), F(0)]
sine = [F(0), F(1), F(0), F(-1)]
grad = [-sine[x] + 2 * cosine[x] for x in range(4)]
grad2 = [-2 * sine[x] - cosine[x] for x in range(4)]
force = lambda x, y: sine[(x-y) % 4]
J = lambda x, y: force(x, y) * (grad[x] - grad[y])
rows = [sum((J(x, y) for y in range(4)), F(0)) / 4 for x in range(4)]
for x in range(4):
    check('smooth_haar_response', rows[x] == -(cosine[x] + 2*sine[x]) / 2)
check('smooth_double_contraction', sum(rows) == 0)
first_source_case = None
first_cross_case = None
for n in [2, 3, 4]:
    for conf in product(range(4), repeat=n):
        raw = sum((force(conf[i], conf[j]) * grad[conf[i]]
                   for i in range(n) for j in range(n) if i != j), F(0)) / (n*n)
        ordered = sum((J(conf[i], conf[j])
                       for i in range(n) for j in range(n) if i != j), F(0))
        row = sum((rows[x] for x in conf), F(0)) / n
        deleted = ordered / (2*n*n) - row
        check('literal_deleted_source_identity', raw == deleted + row)
        check('source_symmetric_label_half', ordered / (2*n*n) == raw)
        if ordered and first_source_case is None:
            first_source_case = (raw, ordered/(n*n), conf, n, deleted, row)
        for nu in [F(0), F(1, 2), F(1), F(3)]:
            b = min(F(1), 1/nu) if nu else F(1)
            cross = 2 * nu * b * sum((grad[x]*grad2[x] for x in conf), F(0)) / n
            by_labels = sum((2*nu*b/F(n)*grad[x]*grad2[x] for x in conf), F(0))
            check('literal_cross_bracket_scaling', cross == by_labels)
            if cross and first_cross_case is None:
                first_cross_case = (cross, n, nu, conf)
v, w, conf, n, deleted, row = first_source_case
reject('remove_ordered_source_half', v, w, {'N': n, 'configuration': conf})
reject('flip_haar_response', v, deleted-row, {'N': n, 'configuration': conf})
v, n, nu, conf = first_cross_case
reject('remove_noise_factor_two', v, v/2, {'N': n, 'nu': nu, 'configuration': conf})
reject('insert_deleted_factor_in_bracket', v, v*F(n-1, n), {'N': n, 'nu': nu, 'configuration': conf})


# The self/background algebra is independent of a Fourier expansion: direct
# unordered pairs versus the full Gram sum, with no remainder diagonal.
for n in range(2, 10):
    vectors = []
    for i in range(n):
        a = F(i+1, n+1)
        vectors.append(((1-a*a)/(1+a*a), 2*a/(1+a*a)))
    g = [[sum((x*y for x, y in zip(vectors[i], vectors[j])), F(0))
          for j in range(n)] for i in range(n)]
    rem = {(i, j): F(i+j+1, n+3) for i in range(n) for j in range(n) if i != j}
    c = F(2, 7)
    H = sum((g[i][j] + rem[i, j] - c for i in range(n) for j in range(i+1, n)), F(0))/n
    E = sum((g[i][j] for i in range(n) for j in range(n)), F(0))/(2*n*n)
    S = sum(rem.values(), F(0))/(2*n*n)
    exact = E+S-F(1, 2*n)-F(n-1, 2*n)*c
    check('energy_full_self_and_background', H/n == exact)
    check('energy_nonnegative_terms', E >= 0 and S >= 0)
    check('no_singular_remainder_diagonal', all((i, i) not in rem for i in range(n)))
    if n == 3:
        reject('double_energy_self_subtraction', H/n, E+S-F(1, n)-F(n-1, 2*n)*c, {'N': n})
        reject('erase_finite_background_factor', H/n, E+S-F(1, 2*n)-c/2, {'N': n})


# Positive heat-retention moments, evaluated twice: alternating Laplace sum,
# and derivatives of a positive beta-product. No float cancellation or assumed
# positivity of an alternating sum enters these checks.
def laplace_moment(alpha, M, lam, scale):
    return factorial(alpha-1)*sum((F((-1)**j*comb(M, j), 1)/(lam+F(j)/scale)**alpha
                                  for j in range(M+1)), F(0))


def beta_product_moment(alpha, M, lam, scale):
    base = F(factorial(M), 1) * scale
    for j in range(M+1):
        base /= lam*scale+j
    h1 = sum((1/(lam+F(j)/scale) for j in range(M+1)), F(0))
    h2 = sum((1/(lam+F(j)/scale)**2 for j in range(M+1)), F(0))
    h3 = sum((1/(lam+F(j)/scale)**3 for j in range(M+1)), F(0))
    factor = {1: F(1), 2: h1, 3: h1*h1+h2, 4: h1**3+3*h1*h2+2*h3}[alpha]
    return base*factor


for alpha, M in [(1, 5), (2, 7), (3, 9)]:
    for lam, scale in product([F(1, 16), F(1, 2), F(1), F(4), F(16)],
                              [F(1, 8), F(1, 2), F(1), F(2)]):
        a = laplace_moment(alpha, M, lam, scale)
        a1 = laplace_moment(alpha+1, M, lam, scale)
        check('retained_laplace_positive_product', a == beta_product_moment(alpha, M, lam, scale))
        check('retained_next_moment_positive_product', a1 == beta_product_moment(alpha+1, M, lam, scale))
        check('retained_weight_positive', a > 0 and a1 > 0)
        slope = 2*lam*a1/a
        check('retained_uniform_log_slope', 0 <= slope <= 2*(alpha+M))
        if alpha == 1 and M == 5 and lam == 16 and scale == 1:
            reject('use_unretained_log_slope_bound', True, slope <= 2*alpha,
                   {'alpha': alpha, 'M': M, 'lambda': lam, 'scale': scale, 'slope': slope})

for d in range(3, 10):
    for s in [F(1, 4), F(1), F(d-2), F(d, 2), F(d, 2)-F(1, 8)]:
        if not 0 < s <= d-2:
            continue
        alpha = (d-s)/2
        check('balanced_source_exponent', -1+(-F(2, d))*(-s/2) == (-F(2, d))*alpha)
        check('scaled_source_threshold', (s/d-F(1, 2) < 0) == (s < F(d, 2)))
reject('reuse_three_dimensional_coulomb_decay', F(2, 4)-F(1, 2), F(1, 3)-F(1, 2),
       {'actual_d': 4, 'actual_s': 2, 'mutant_reuses_d': 3, 'mutant_reuses_s': 1})


# Exact dyadic union-bound bookkeeping and a noncompact-neighborhood control.
for j in range(1, 16):
    mesh = F(1, 2**(8*j))
    threshold = F(1, 2**j)
    union = 2**(8*j)*mesh**2/threshold**4
    check('dyadic_fourth_moment_summability', union == F(1, 2**(4*j)))
    boundary_mesh = F(1, 2**(4*j))
    critical = 2**(4*j)*boundary_mesh**2/threshold**4
    check('dyadic_critical_exponent_not_summable', critical == 1)
mutation_mesh, mutation_threshold, mutation_edges = F(1, 2**8), F(1, 2), 2**8
reject('drop_squared_time_increment', mutation_edges*mutation_mesh**2/mutation_threshold**4,
       mutation_edges*mutation_mesh/mutation_threshold**4, {'subsampled_level': 1})


def tent(t, left, right, height):
    midpoint = (left+right)/2
    if t <= left or t >= right:
        return F(0)
    return height*(t-left)/(midpoint-left) if t <= midpoint else height*(right-t)/(right-midpoint)


supports = [(F(1, 2**(j+1)), F(1, 2**j)) for j in range(1, 11)]
for i, j in product(range(len(supports)), repeat=2):
    vertices = sorted(set([F(0), F(1)] + [a for pair in [supports[i], supports[j]]
                                         for a in [pair[0], sum(pair)/2, pair[1]]]))
    dist = max(abs(tent(t, *supports[i], F(1, 2))-tent(t, *supports[j], F(1, 2))) for t in vertices)
    check('compact_neighborhood_separated_paths', dist == (F(0) if i == j else F(1, 2)))
all_in_tube = all(tent(sum(pair)/2, *pair, F(1, 2)) <= F(1, 2) for pair in supports)
packing_distance = min(max(abs(tent(t, *supports[i], F(1, 2))
                                  -tent(t, *supports[j], F(1, 2)))
                              for t in [sum(supports[i])/2, sum(supports[j])/2])
                       for i in range(len(supports)) for j in range(i+1, len(supports)))
reject('fixed_compact_neighborhood_erases_packing', packing_distance, F(0),
       {'radius_about_zero': '1/2', 'all_in_tube': all_in_tube,
        'tested_paths': len(supports), 'analytic_infinite_extension': 'same disjoint dyadic supports'})


def linear_value(values, t):
    n = len(values)-1
    if t == 1:
        return values[-1]
    raw = t*n
    left = raw.numerator//raw.denominator
    return values[left]+(raw-left)*(values[left+1]-values[left])


paths = [[F(0), F(1), F(-1), F(2), F(0), F(1, 3), F(1), F(0), F(-1)],
         [F(0), F(0), F(0), F(1), F(0), F(0), F(0), F(0), F(0)],
         [F(3)]*9]
for values in paths:
    for coarse in [1, 2, 4, 8]:
        samples = [linear_value(values, F(i, coarse)) for i in range(coarse+1)]
        error = max(abs(values[i]-linear_value(samples, F(i, 8))) for i in range(9))
        modulus = max(abs(values[i]-values[j]) for i, j in product(range(9), repeat=2)
                      if abs(i-j) <= 8//coarse)
        check('linear_interpolation_uniform_modulus', error <= modulus)
hidden_samples = [linear_value(paths[1], F(i, 2)) for i in range(3)]
hidden_error = max(abs(paths[1][i]-linear_value(hidden_samples, F(i, 8))) for i in range(9))
reject('grid_values_identify_uniform_path', hidden_error, max(map(abs, hidden_samples)),
       {'fine_path': paths[1], 'coarse_grid': ['0', '1/2', '1'], 'uniform_error': '1'})


# A bounded initial-measurable stochastic integrand. Conditional on S=+/-1,
# M is a Brownian integral with deterministic bracket v_S. Its even moments
# and compensated characteristic power series are exact Gaussian identities.
def series_mul(p, q, degree):
    return [sum((p[i]*q[n-i] for i in range(n+1)), F(0)) for n in range(degree+1)]


def exponential_series(a, degree):
    return [a**n/F(factorial(n)) for n in range(degree+1)]


vp, vm = F(3, 2), F(13, 2)
mean_v = (vp+vm)/2
mixed = (vp-vm)/2
fourth = 3*(vp*vp+vm*vm)/2
check('initial_martingale_orthogonality_not_independence', mixed != 0)
check('bounded_density_fourth_majorant', fourth <= 3*max(vp, vm)**2)
for v in [vp, vm, F(0)]:
    # The variable x stands for z^2, through degree eight in x.
    series = series_mul(exponential_series(-v/2, 8), exponential_series(v/2, 8), 8)
    check('conditional_positive_compensator', series == [F(1)]+[F(0)]*8)
reject('random_bracket_replaced_by_mean', fourth, 3*mean_v**2,
       {'conditional_brackets': [vp, vm], 'fourth_moment': fourth})
reject('finite_N_initial_thermal_independence', mixed, F(0),
       {'E_S_M_squared': mixed, 'E_S': 0, 'E_S_M': 0})
wrong_sign = series_mul(exponential_series(-vp/2, 8), exponential_series(-vp/2, 8), 8)
reject('negative_exponential_compensator', F(0), wrong_sign[1], {'bracket': vp})
wrong_mean = series_mul(exponential_series(-vp/2, 8), exponential_series(mean_v/2, 8), 8)
reject('conditional_compensator_uses_mean', F(0), wrong_mean[1], {'conditional_bracket': vp, 'mean': mean_v})

result = {
    'audit': 'AUD060',
    'status': 'PASS',
    'evidence_class': 'Exact diagnostic support; not analytic certification or an admitted particle counterexample.',
    'arithmetic': 'Python standard-library Fraction; no randomness, floating point, numerical tolerance or installs.',
    'assertions': sum(counts.values()),
    'categories': dict(sorted(counts.items())),
    'mutation_count': len(mutations),
    'mutations_rejected_with_nonzero_witness': dict(sorted(mutations.items())),
    'scope': [
        'Continuum polynomial-kernel Brownian convolution, temporal increments and integrated path functionals.',
        'Literal smooth Fourier source and bracket factors; abstract positive splitting algebra and Laplace moments.',
        'Dyadic summability, interpolation, noncompact neighborhoods and conditional probability-inference controls.',
        'No actual singular law, compactness theorem or continuum source estimate is proved by this program.'
    ],
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
print(json.dumps(result, indent=2, sort_keys=True))
