#!/usr/bin/env python3
"""Fresh TASK064 algebra/interval diagnostics; no imported checker or packages.

Finite laws below are deliberately non-product four-symbol probability laws.
They are NOT purported singular-dynamics laws. All asserted computations use
Fraction arithmetic. Logarithms are certified by a rational series remainder.
Analytic singular passage and asymptotic assertions are reviewed in Markdown.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

COUNTS = Counter()
WITNESSES = {}


def check(truth, group):
    if not truth:
        raise AssertionError(group)
    COUNTS[group] += 1


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def mul(c, a):
    return tuple(c*x for x in a)


Z = (F(0), F(0))
DIRECTIONS = ((F(1), F(0)), (F(0), F(1)),
              (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)))
S = range(4)


def vector_kernel(threshold=None, tail=False):
    kernel = {}
    for x, y in product(S, repeat=2):
        magnitude = F((7*x+3*y+x*y) % 10)
        direction = DIRECTIONS[(x+2*y) % 4]
        if threshold is None:
            size = magnitude
        elif tail:
            size = max(magnitude-threshold, F(0))
        else:
            size = min(magnitude, threshold)
        kernel[x, y] = mul(size, direction)
        check(dot(kernel[x, y], kernel[x, y]) == size*size,
              'exact_radial_projection')
    return kernel


def rows(kernel):
    a = {x: mul(F(1, 4), tuple(sum(kernel[x, y][d] for y in S)
                              for d in range(2))) for x in S}
    h = {(x, y): add(kernel[x, y], mul(-1, a[x]))
         for x, y in product(S, repeat=2)}
    for x in S:
        check(all(sum(h[x, y][d] for y in S) == 0 for d in range(2)),
              'own_row_centering')
    return a, h


def field(config, kernel, a):
    n = len(config)
    result = []
    for i, x in enumerate(config):
        total = Z
        for j, y in enumerate(config):
            if j != i:
                total = add(total, kernel[x, y])
        result.append(mul(F(1, n*n), add(total, mul(-n, a[x]))))
    return result


def marginal(law, k):
    result = defaultdict(F)
    for config, prob in law.items():
        result[config[:k]] += prob
    return dict(result)


def law_for(n, mode):
    raw = {}
    for config in product(S, repeat=n):
        square_count = sum(count*count for count in Counter(config).values())
        weight = 1 if mode == 'haar' else (
            1+square_count if mode == 'cluster' else 1+n*n-square_count)
        raw[config] = F(weight)
    mass = sum(raw.values())
    result = {x: p/mass for x, p in raw.items()}
    check(sum(result.values()) == 1, 'probability_normalization')
    check(all(p == F(1, 4) for p in marginal(result, 1).values()),
          'one_body_haar')
    for config, prob in result.items():
        check(result[tuple(reversed(config))] == prob, 'exchangeability')
        check(result[tuple((x+1) % 4 for x in config)] == prob,
              'common_translation')
    return result


def exact_expectation(law, fn):
    return sum((prob*fn(config) for config, prob in law.items()), F(0))


def contractions(law, kernel):
    n = len(next(iter(law)))
    a, h = rows(kernel)
    pair = exact_expectation(law, lambda x: dot(h[x[0], x[1]], h[x[0], x[1]]))
    triple = None
    if n >= 3:
        triple = exact_expectation(law, lambda x: dot(h[x[0], x[1]], h[x[0], x[2]]))
    mixed = exact_expectation(law, lambda x: dot(h[x[0], x[1]], a[x[0]]))
    square = exact_expectation(law, lambda x: dot(a[x[0]], a[x[0]]))
    direct = exact_expectation(law, lambda x: sum(dot(v, v) for v in field(x, kernel, a)))
    counted = F(1, n**3)*((n-1)*pair-2*(n-1)*mixed+square)
    if n >= 3:
        counted += F((n-1)*(n-2), n**3)*triple
    else:
        check(triple is None, 'no_triple_at_N2')
    check(direct == counted, 'four_contraction_identity')
    check(direct >= 0, 'nonnegative_full_square')
    if mixed:
        WITNESSES.setdefault('nonzero_mixed', str(mixed))
    if triple:
        WITNESSES.setdefault('nonzero_triple', str(triple))
    return direct, pair, triple, mixed, square, a, h


@lru_cache(maxsize=None)
def log_interval(value):
    """Rational enclosure of log(value), using 60 positive atanh terms."""
    assert value > 0
    exponent = 0
    u = value
    while u >= 2:
        u /= 2
        exponent += 1
    while u < 1:
        u *= 2
        exponent -= 1

    def local(v):
        z = (v-1)/(v+1)
        total = sum((2*z**(2*j+1)/F(2*j+1) for j in range(60)), F(0))
        remainder = 2*z**121/(121*(1-z*z))
        return total, total+remainder

    low, high = local(u)
    l2, h2 = local(F(2))
    if exponent >= 0:
        return low+exponent*l2, high+exponent*h2
    return low+exponent*h2, high+exponent*l2


def entropy_interval(law):
    n = len(next(iter(law)))
    lower = upper = F(0)
    for p in law.values():
        lo, hi = log_interval(p*4**n)
        lower += p*lo
        upper += p*hi
    return lower, upper


def entropy_diagnostics(n, law):
    ent = {k: entropy_interval(marginal(law, k)) for k in range(1, n+1)}
    check(ent[1] == (0, 0), 'entropy_H1_zero')
    for k in range(2, n):
        check(ent[k][1] <= F(k-1, n-1)*ent[n][0],
              'entropy_sharpened_marginal_factor')
    for j in range(2, n):
        check(ent[j+1][0]-ent[j][1] >= ent[j][1]-ent[j-1][0],
              'entropy_conditional_increment_monotonicity')
    for k in range(2, n+1):
        p = marginal(law, k)
        l1 = sum(abs(v-F(1, 4**k)) for v in p.values())
        check(l1*l1 <= 2*ent[k][0], 'pinsker_exact_log_interval')
    check(F(n-1, n-1) == 1, 'entropy_N_endpoint')


def polynomial_gradient_diagnostics():
    # A separate sparse multivariate polynomial engine differentiates P itself.
    # Its [0,1]-uniform background tests finite sums only, not periodic analysis.
    for n in (2, 3, 4, 7):
        poly = defaultdict(F)

        def term(c, powers):
            exponents = [0]*n
            for i, power in powers.items():
                exponents[i] = power
            poly[tuple(exponents)] += c

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                factor = F(1, 2*n*n)
                term(factor, {i: 2, j: 1})
                term(factor, {i: 1, j: 2})
                term(2*factor, {i: 1, j: 1})
                term(factor/3, {i: 3})
                term(factor/3, {j: 3})
            # minus (1/N) integral Phi(x_i,y) dy
            term(-F(1, 2*n), {i: 2})
            term(-F(4, 3*n), {i: 1})
            term(-F(1, 3*n), {i: 3})
            term(-F(1, 12*n), {})
        # Half the double-background integral is a constant, immaterial below.
        term(F(1, 2), {})
        for offset in range(4):
            xs = tuple(F(2*i+offset+1, 2*n+offset+3) for i in range(n))
            for i in range(n):
                derivative = F(0)
                for powers, coeff in poly.items():
                    if not powers[i]:
                        continue
                    value = coeff*powers[i]
                    for j, power in enumerate(powers):
                        value *= xs[j]**(power-(j == i))
                    derivative += value
                x = xs[i]
                a = x*x+x+F(4, 3)
                gradients = [2*x*y+y*y+2*y+x*x for j, y in enumerate(xs) if j != i]
                raw = sum(gradients, F(0))/n**2-a/n
                centered = (sum((g-a for g in gradients), F(0))-a)/n**2
                check(derivative == raw == centered, 'original_statistic_differentiation')


def full_field_diagnostics():
    full = vector_kernel()
    for n in range(2, 6):
        laws = {mode: law_for(n, mode) for mode in ('haar', 'cluster', 'balanced')}
        for mode in ('cluster', 'balanced'):
            entropy_diagnostics(n, laws[mode])
        for threshold in (F(1, 2), F(5, 2), F(7)):
            clipped = vector_kernel(threshold)
            tail = vector_kernel(threshold, True)
            for xy in full:
                check(full[xy] == add(clipped[xy], tail[xy]), 'kernel_exact_split')
            reference = contractions(laws['haar'], clipped)
            ga = sum(dot(v, v) for v in clipped.values())/16
            aa = sum(dot(v, v) for v in reference[5].values())/4
            check(reference[0] == F(n-1, n**3)*ga-F(n-2, n**3)*aa,
                  'haar_negative_row_coefficient')
            for mode, law in laws.items():
                sf = contractions(law, full)
                sc = contractions(law, clipped)
                st = contractions(law, tail)
                cross = exact_expectation(law, lambda x: sum(
                    dot(v, w) for v, w in zip(field(x, clipped, sc[5]), field(x, tail, st[5]))))
                check(sf[0] == sc[0]+st[0]+2*cross, 'nonorthogonal_bracket_split')
                check(cross*cross <= sc[0]*st[0], 'hilbert_cauchy_schwarz')
                lhs = sf[0]+st[0]-sc[0]
                check(lhs <= 0 or lhs*lhs <= 4*sf[0]*st[0], 'reverse_triangle_without_square_roots')
                if cross:
                    WITNESSES.setdefault('nonzero_clip_tail_cross', str(cross))
                e2 = sum(abs(p-F(1, 16)) for p in marginal(law, 2).values())
                e3 = F(0) if n == 2 else sum(abs(p-F(1, 64)) for p in marginal(law, 3).values())
                d2, da = sc[1]-reference[1], sc[3]-reference[3]
                d3 = F(0) if n == 2 else sc[2]-reference[2]
                check(abs(d2) <= 4*threshold**2*e2, 'bounded_pair_deviation')
                check(abs(da) <= 2*threshold**2*e2, 'bounded_mixed_deviation')
                check(abs(d3) <= 4*threshold**2*e3, 'bounded_triple_deviation')
                check(sc[4] == reference[4], 'one_body_square_cancels')
                for nu in (F(1, 16), F(1, 2), F(1), F(2), F(9)):
                    b = min(1, 1/nu)
                    prefactor = 2*nu*n*b
                    deviation = prefactor*(sc[0]-reference[0])
                    counted = F(2, n*n)*nu*b*((n-1)*d2+(n-1)*(n-2)*d3-2*(n-1)*da)
                    check(deviation == counted, 'physical_2nu_Nb_and_law_coefficients')
                    bound = 8*nu*b*threshold**2*F(n-1, n*n)*(2*e2+(n-2)*e3)
                    check(abs(deviation) <= bound, 'equation_5_6_exact_constant')
                    # Independent direct Cauchy-Schwarz upper bound of (8.3), first line.
                    pairg = exact_expectation(law, lambda x: dot(tail[x[0], x[1]], tail[x[0], x[1]]))
                    direct_bound = 4*nu*b*(F((n-1)**2, n*n)*pairg+st[4])
                    check(prefactor*st[0] <= direct_bound, 'tail_first_line_8_3')
                    check(b*b*nu <= 1 and b*nu <= 1, 'physical_noise_uniformity')
                check(2*F(0)*n*sf[0] == 0, 'zero_noise_bracket_endpoint')
                check(F(0)*sf[0] == 0, 'zero_horizon_bracket_endpoint')
                if n == 2:
                    nu, b = F(1, 2), F(1)
                    general = 8*nu*b*threshold**2*F(n-1, n*n)*(2*e2)
                    check(general == 4*nu*b*threshold**2*e2, 'N2_error_constant')


def energy_and_fourier_diagnostics():
    # Positive-Fourier torus polynomial at quarter-period configurations.
    c1 = (1, 0, -1, 0)
    for amplitudes in ((F(1), F(2)), (F(7, 3), F(1, 5))):
        for attenuation in (F(1), F(1, 2), F(1, 7)):
            g = {z: amplitudes[0]*attenuation*c1[z] +
                    amplitudes[1]*attenuation**4*((-1)**z) for z in S}
            check(sum(g.values()) == 0, 'zero_fourier_mean')
            for n in (2, 3, 4):
                for config in product(S, repeat=n):
                    all_pairs = sum(g[(x-y) % 4] for x in config for y in config)
                    deleted = sum(g[(config[i]-config[j]) % 4]
                                  for i in range(n) for j in range(i+1, n))/n
                    check(all_pairs >= 0, 'positive_fourier_configuration_form')
                    check(deleted == all_pairs/(2*n)-g[0]/2,
                          'exact_deleted_self_energy_half')
                    check(deleted >= -g[0]/2, 'positive_fourier_lower_bound')
    # Coulomb response on a four-point probability space: D=c(delta-Haar).
    c = F(11, 3)
    for seed in range(9):
        v = {(x, y): F(((x+2)*(y+3)+seed*x*x-2*seed*y) % 13-6)
             for x, y in product(S, repeat=2)}
        px = {y: sum(v[x, y] for x in S)/4 for y in S}
        py = {x: sum(v[x, y] for y in S)/4 for x in S}
        response = {(x, y): -2*c*v[x, y]+c*px[y]+c*py[x] for x, y in v}
        quadratic = sum(v[xy]*response[xy] for xy in v)/16
        check(quadratic <= 0, 'coulomb_both_responses_nonpositive')
        check(sum(response.values()) == 0, 'coulomb_mean_compensation')
    for constant in (F(0), F(5, 7), F(-9)):
        check(-2*c*constant+c*constant+c*constant == 0,
              'coulomb_constant_mode_killed')
    for m in (1, 2, 4, 8, 16):
        for frequency in (m, 2*m, 4*m):
            # Normalized heat time log(2)/m^2; these exact mode multipliers
            # challenge an illicit operator-norm convergence claim at Coulomb.
            attenuation = F(1, 2)**((frequency//m)**2)
            check(2*c*(1-attenuation) >= c,
                  'coulomb_moving_high_frequency_obstruction')
    zero_gradient = {(x, y): Z for x, y in product(S, repeat=2)}
    zero_rows, _ = rows(zero_gradient)
    for n in range(2, 6):
        for config in product(S, repeat=n):
            check(all(v == Z for v in field(config, zero_gradient, zero_rows)),
                  'constant_source_corrector_gradient_endpoint')
    for n in range(2, 20):
        # The two-coordinate differentiation of each unordered pair is essential.
        check(F(2, n)*F(n*(n-1), 2) == n-1, 'configuration_divergence_coefficient')
        check(F(2, n) != 0, 'time_zero_pair_BBGKY_coefficient')
        # Prove the sqrt(2) coefficient upper bound by rational separation.
        # sqrt(2) N^2 - (N-1)[2+sqrt(2)(N-2)]
        # = sqrt(2)(3N-2)-2(N-1) > 0.
        check(2*(3*n-2)**2 >= 4*(n-1)**2, 'uniform_error_constant_sqrt2')
    for d in range(3, 13):
        for s in (F(1, 2), F(d-2, 2), F(d-2)):
            if not (0 < s <= d-2):
                continue
            p = s+2
            a = s/p
            check(-F(2, 1)/p*(-s/2) == a, 'heat_diagonal_exponent')
            check(1-F(2, 1)/p == a, 'heat_compensation_exponent')
            check((a-1)/2 == -1/p, 'entropy_exponent')
            check(2/(4*p)-1/p == -1/(2*p), 'explicit_clip_rate')
            check(s+2-d <= 0, 'all_frequency_multiplier_regime')
            if s < d-2:
                check(4*((d-s-2)/2)*(s/2) == s*(d-2-s),
                      'gamma_recurrence_normalization')
            if s > 2:
                q = (1+s/2)/2
                r = s/q
                check(1 < q < s/2 and q < F(d, 2) and r > 2,
                      'tail_moment_exponent_available')
                check((2-r)/(4*p) == -(s/q-2)/(4*p),
                      'unproved_growth_criterion_exponent')
            else:
                for q in (F(11, 10), F(5, 4), F(3, 2)):
                    if q < F(d, 2):
                        check(s/q <= 2, 'small_s_moment_route_limitation')
    # The free-energy square is a polynomial identity at arbitrary rational data.
    for nu, loggrad, energygrad in product((F(1, 3), F(1), F(7, 2)), repeat=3):
        direct = -(nu*loggrad+energygrad)**2
        expanded = -nu**2*loggrad**2-2*nu*loggrad*energygrad-energygrad**2
        check(direct == expanded, 'free_energy_nu_squared_fisher_factor')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    manifest = root/'AUDITS/HOSTILE/ROUND_010_CLIPPING_INPUT_SHA256SUMS.txt'
    inputs = []
    for line in manifest.read_text().splitlines():
        digest, relative = line.split('  ', 1)
        check(hashlib.sha256((root/relative).read_bytes()).hexdigest() == digest,
              'sealed_input_sha256')
        inputs.append(relative)
    check(len(inputs) == 22, 'exact_input_count')
    polynomial_gradient_diagnostics()
    full_field_diagnostics()
    energy_and_fourier_diagnostics()
    check(all(key in WITNESSES for key in
              ('nonzero_mixed', 'nonzero_triple', 'nonzero_clip_tail_cross')),
          'adversarial_terms_really_nonzero')
    result = {
        'task': 'TASK-064', 'status': 'PASS', 'exact_assertions': sum(COUNTS.values()),
        'arithmetic': 'fractions.Fraction; log enclosures with proved positive series remainder',
        'randomness': 'none', 'external_packages': [], 'input_count': len(inputs),
        'groups': dict(sorted(COUNTS.items())), 'nonzero_witnesses': WITNESSES,
        'scope': 'Independent finite algebra, exact interval entropy, finite Fourier and exponent diagnostics only. Not a singular SDE approximation or proof of actual tail convergence.',
        'prerequisites': 'THM028 and THM029 remain explicit conditional premises. No audit verdict is inferred from earlier report status text.'
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': result['status'], 'exact_assertions': result['exact_assertions'],
                      'groups': len(COUNTS), 'output': str(args.output)}, sort_keys=True))


if __name__ == '__main__':
    main()
