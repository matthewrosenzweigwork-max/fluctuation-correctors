#!/usr/bin/env python3
"""Exact finite algebra supporting R28. No simulation or continuum certification."""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import json
import sys

EXPECTED_MUTANTS = {
    'drop_same_edge', 'drop_adjacent_double', 'drop_triangle',
    'drop_disjoint_double', 'drop_four_cycle', 'omit_clip_recentering',
    'drop_heat_self', 'lose_ordered_half', 'wrong_falling_factorial',
    'merge_backward_weights', 'replace_initial_tag', 'drop_overlap_self',
    'drop_row_same_label', 'drop_mixed_same_label', 'drop_noise_cross',
    'wrong_cutoff_dimension', 'wrong_clipping_power'
}


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, tuple):
        return [serial(a) for a in x]
    if isinstance(x, dict):
        return {str(k): serial(v) for k, v in x.items()}
    if isinstance(x, list):
        return [serial(a) for a in x]
    return x


class Runner:
    def __init__(self, mutant):
        self.mutant = mutant
        self.counts = Counter()
        self.witnesses = {}

    def equal(self, category, lhs, rhs, context, variants=None):
        self.counts[category] += 1
        if lhs != rhs:
            raise AssertionError(json.dumps(serial({
                'kind': 'BASELINE_FAILURE', 'category': category,
                'lhs': lhs, 'rhs': rhs, 'context': context}), sort_keys=True))
        for name, wrong in (variants or {}).items():
            if wrong != lhs:
                witness = serial({'category': category, 'correct': lhs,
                                  'mutated': wrong, 'context': context})
                self.witnesses.setdefault(name, witness)
                if self.mutant == name:
                    raise AssertionError(json.dumps({
                        'kind': 'MATHEMATICAL_MUTATION_CAUGHT',
                        'mutant': name, 'witness': witness}, sort_keys=True))

    def truth(self, category, value, context):
        self.equal(category, bool(value), True, context)


def cn(n, k):
    return comb(n, k) if n >= k else 0


def fourth_graphs(r):
    for n in range(2, 7):
        edges = tuple(combinations(range(n), 2))
        counts = Counter()
        for ordered_edges in product(edges, repeat=4):
            degree = Counter(v for edge in ordered_edges for v in edge)
            if 1 in degree.values():
                counts['zero_row'] += 1
                continue
            multiplicities = sorted(Counter(ordered_edges).values())
            vertices = len(degree)
            if vertices == 2:
                key = 'same_edge'
            elif vertices == 3:
                key = 'adjacent_double' if multiplicities == [2, 2] else 'triangle'
            elif vertices == 4:
                key = 'disjoint_double' if multiplicities == [2, 2] else 'four_cycle'
            else:
                raise AssertionError('Unclassified surviving graph')
            counts[key] += 1
        expected = {
            'same_edge': cn(n, 2), 'adjacent_double': 18*cn(n, 3),
            'triangle': 36*cn(n, 3), 'disjoint_double': 18*cn(n, 4),
            'four_cycle': 72*cn(n, 4)
        }
        for key, value in expected.items():
            r.equal('four_edge_graph_counts', counts[key], value, (n, key))
        r.equal('four_edge_graph_exhaustion', sum(counts.values()), len(edges)**4, n)


def exact_haar_moments(r):
    for q, raw in [(3, [F(2), F(-1), F(-1)]),
                   (5, [F(4), F(-1), F(-1), F(-1), F(-1)])]:
        for cap in (F(1, 2), F(2), F(5)):
            clipped = [min(v, cap) for v in raw]
            mean = sum(clipped)/q
            h = [v-mean for v in clipped]
            r.equal('clipped_zero_row', sum(h)/q, F(0), (q, cap),
                    {'omit_clip_recentering': sum(clipped)/q})
            mu2 = sum(v*v for v in h)/q
            mu4 = sum(v**4 for v in h)/q
            conv = [sum(h[y]*h[(z-y) % q] for y in range(q))/q for z in range(q)]
            tau = sum(h[z]**2*conv[z] for z in range(q))/q
            chi = sum(v*v for v in conv)/q
            r.truth('triangle_convolution_bound', abs(tau) <= mu2**2, (q, cap))
            r.truth('cycle_convolution_bound', 0 <= chi <= mu2**2, (q, cap))
            for n in range(2, 6):
                edges = tuple(combinations(range(n), 2))
                second = F(0)
                fourth = F(0)
                for config in product(range(q), repeat=n):
                    energy = sum(h[(config[i]-config[j]) % q] for i, j in edges)/n
                    second += energy**2
                    fourth += energy**4
                second /= q**n
                fourth /= q**n
                terms = {
                    'same_edge': cn(n, 2)*mu4,
                    'adjacent_double': 18*cn(n, 3)*mu2**2,
                    'triangle': 36*cn(n, 3)*tau,
                    'disjoint_double': 18*cn(n, 4)*mu2**2,
                    'four_cycle': 72*cn(n, 4)*chi
                }
                rhs = sum(terms.values())/n**4
                mutants = {'drop_'+key: rhs-value/n**4 for key, value in terms.items()}
                r.equal('fourth_haar_energy', fourth, rhs, (q, cap, n), mutants)
                r.equal('second_haar_energy', second, F(n-1, 2*n)*mu2, (q, cap, n))
                r.truth('fourth_energy_bound', fourth <= 20*(mu4/n**2+mu2**2),
                        (q, cap, n))
    phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for n in range(2, 7):
        total = 0
        for indices in product(range(4), repeat=n):
            real = sum(phases[j][0] for j in indices)
            imag = sum(phases[j][1] for j in indices)
            total += (real*real+imag*imag)**2
        r.equal('iid_modal_fourth', F(total, n*n*4**n), F(2)-F(1, n), n)


# Gaussian rational arithmetic: every real and imaginary component is exact.
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def scale(a, t):
    return (a[0]*t, a[1]*t)


def conj(a):
    return (a[0], -a[1])


def sumc(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[0], -a[1])


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def phase(m, x):
    value = dot(m, x) % 4
    return ((F(1), F(0)), (F(0), F(1)),
            (F(-1), F(0)), (F(0), F(-1)))[value]


def empirical(m, xs):
    return scale(sumc(phase(m, x) for x in xs), F(1, len(xs)))


def coeffs(k, a):
    d = dot(k, k)*a.get(k, F(0))
    modes = set(a) | {vadd(m, neg(k)) for m in a} | {(0, 0), neg(k)}
    b = {}
    for m in sorted(modes):
        mk = vadd(m, k)
        b[m] = dot(k, m)*a.get(m, F(0))-dot(k, mk)*a.get(mk, F(0))
        if m == (0, 0) or m == neg(k):
            b[m] += d
    return d, b


def direct_j(k, a, d, x, y):
    # The common continuum factor c=(2*pi)^2 is divided out everywhere.
    difference = sub(phase(k, x), phase(k, y))
    xy = vadd(x, neg(y))
    force = sumc(scale(mul(phase(m, xy), difference), dot(k, m)*weight)
                 for m, weight in a.items())
    return add(force, scale(add(phase(k, x), phase(k, y)), d))


def fourier_and_labels(r):
    supports = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 0), (0, 2)]
    for kernel_index in range(2):
        a = {}
        for j, m in enumerate(supports):
            value = F(1, dot(m, m)*(j+1+kernel_index))
            a[m] = value
            a[neg(m)] = value
        for k in [(1, 0), (1, 1), (2, 0)]:
            d, b = coeffs(k, a)
            r.equal('zero_fourier_rows', (b.get((0, 0), 0), b.get(neg(k), 0)),
                    (F(0), F(0)), (kernel_index, k))
            r.equal('smooth_diagonal_coefficients', sum(b.values()), 2*d, (kernel_index, k))
            for m, value in b.items():
                r.equal('pair_symmetry', value, b.get(neg(vadd(k, m)), 0), (k, m))
            for n in range(2, 7):
                for case in range(8):
                    xs = tuple(((i*i+case*i+case) % 4,
                                (3*i+case*case+i*i) % 4) for i in range(n))
                    ys = tuple(((2*i+case+1) % 4,
                                (i*i+2*case*i+3) % 4) for i in range(n))
                    ctx = (kernel_index, k, n, case)
                    ecur = [phase(k, x) for x in xs]
                    einit = [phase(k, x) for x in ys]
                    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
                    jvals = {(i, j): direct_j(k, a, d, xs[i], xs[j]) for i, j in pairs}
                    for i, j in pairs:
                        rhs = sumc(scale(mul(phase(vadd(k, m), xs[i]), phase(neg(m), xs[j])), value)
                                   for m, value in b.items())
                        r.equal('direct_pair_fourier', jvals[i, j], rhs, (ctx, i, j))
                    z = empirical(k, xs)
                    z0 = empirical(k, ys)
                    raw_product = sumc(scale(mul(empirical(vadd(k, m), xs), empirical(neg(m), xs)), value)
                                       for m, value in b.items())
                    u = scale(sumc(jvals.values()), F(1, 2*n*n))
                    formula = sub(scale(raw_product, F(1, 2)), scale(z, F(d, n)))
                    r.equal('deleted_fourier_source', u, formula, ctx, {
                        'drop_heat_self': scale(raw_product, F(1, 2)),
                        'lose_ordered_half': sub(raw_product, scale(z, F(d, n)))})
                    a2 = scale(sumc(mul(jvals[i, j], conj(ecur[i])) for i, j in pairs), F(1, n*(n-1)))
                    b2 = scale(sumc(mul(jvals[i, j], conj(einit[i])) for i, j in pairs), F(1, n*(n-1)))
                    spectral_overlap = sumc(scale(mul(empirical(m, xs), conj(empirical(m, xs))), value)
                                            for m, value in b.items())
                    overlap_rhs = sub(scale(spectral_overlap, F(n, n-1)), (F(2*d, n-1), F(0)))
                    r.equal('overlap_diagonal', a2, overlap_rhs, ctx, {
                        'drop_overlap_self': scale(spectral_overlap, F(n, n-1))})
                    if n >= 3:
                        triples = [(i, j, l) for i, j in pairs for l in range(n) if l not in (i, j)]
                        a3 = scale(sumc(mul(jvals[i, j], conj(ecur[l])) for i, j, l in triples),
                                   F(1, n*(n-1)*(n-2)))
                        b3 = scale(sumc(mul(jvals[i, j], conj(einit[l])) for i, j, l in triples),
                                   F(1, n*(n-1)*(n-2)))
                    else:
                        a3 = b3 = ZERO
                    pn = F((n-1)*(n-2), 2*n)
                    fcur = scale(mul(u, conj(z)), n)
                    ginit = scale(mul(u, conj(z0)), n)
                    r.equal('current_label_count', fcur, add(scale(a2, F(n-1, n)), scale(a3, pn)), ctx)
                    r.equal('mixed_label_count', ginit, add(scale(b2, F(n-1, n)), scale(b3, pn)), ctx)
                    back = F(2, 3)
                    initial_weight = F(3, 7)
                    literal = scale(sub(scale(a3, back**2), scale(b3, initial_weight*back)), pn)
                    reconstructed = sub(
                        scale(sub(fcur, scale(a2, F(n-1, n))), back**2),
                        scale(sub(ginit, scale(b2, F(n-1, n))), initial_weight*back))
                    r.equal('signed_triple_two_weights', literal, reconstructed, ctx, {
                        'wrong_falling_factorial': scale(sub(scale(a3, back**2), scale(b3, initial_weight*back)), F(n-1, 2)),
                        'merge_backward_weights': scale(sub(scale(a3, back**2), scale(b3, back**2)), pn),
                        'replace_initial_tag': scale(sub(scale(a3, back**2), scale(a3, initial_weight*back)), pn)})
                    cpair = scale(sumc(mul(ecur[i], conj(ecur[j])) for i, j in pairs), F(1, n*(n-1)))
                    opair = scale(sumc(mul(ecur[i], conj(einit[j])) for i, j in pairs), F(1, n*(n-1)))
                    stag = scale(sumc(mul(ecur[i], conj(einit[i])) for i in range(n)), F(1, n))
                    c_rhs = scale(sub(scale(mul(z, conj(z)), n), ONE), F(1, n-1))
                    o_rhs = scale(sub(scale(mul(z, conj(z0)), n), stag), F(1, n-1))
                    r.equal('row_current_same_label', cpair, c_rhs, ctx, {
                        'drop_row_same_label': scale(mul(z, conj(z)), F(n, n-1))})
                    r.equal('row_mixed_same_label', opair, o_rhs, ctx, {
                        'drop_mixed_same_label': scale(mul(z, conj(z0)), F(n, n-1))})
                    if n >= 3:
                        row_a = scale(sumc(mul(add(ecur[i], ecur[j]), conj(ecur[l])) for i, j, l in triples),
                                      F(1, n*(n-1)*(n-2)))
                        row_b = scale(sumc(mul(add(ecur[i], ecur[j]), conj(einit[l])) for i, j, l in triples),
                                      F(1, n*(n-1)*(n-2)))
                        r.equal('row_triple_reduction_current', row_a, scale(cpair, 2), ctx)
                        r.equal('row_triple_reduction_mixed', row_b, scale(opair, 2), ctx)


def moment_and_cutoff_stress(r):
    ed2 = el2 = edl = es2 = F(0)
    for initial, noise in product((-1, 1), repeat=2):
        endpoint = F(2, 3)*initial+F(3, 5)*noise
        martingale = F(1, 4)*noise
        source = endpoint-martingale
        ed2 += endpoint**2/4
        el2 += martingale**2/4
        edl += endpoint*martingale/4
        es2 += source**2/4
    r.equal('endpoint_noise_cross', es2, ed2+el2-2*edl, 'independent input coins; dependent endpoint and noise',
            {'drop_noise_cross': ed2+el2})
    r.truth('endpoint_noise_cross_nonzero', edl != 0, edl)
    exponent = F(4+20-2, 2)
    r.equal('four_dimensional_heat_power', exponent, F(11), 'dimension plus modal weights minus Coulomb power',
            {'wrong_cutoff_dimension': F(3+20-2, 2)})
    for delta, expected in [(F(1, 24), F(-1, 24)), (F(1, 44), F(-1, 4))]:
        r.equal('shrinking_heat_rate', -F(1, 2)+exponent*delta, expected, delta)
        r.truth('finite_N_square_term_retained', -1+2*delta < 0, delta)
    for n in (2, 3, 8, 32):
        cap = n*n
        pair_cost = F(cap*cap, n**4)
        rare_cost = F(n**4, cap*cap)
        r.equal('balanced_fourth_clipping', (pair_cost, rare_cost), (F(1), F(1)), n,
                {'wrong_clipping_power': (F(n*n, n**4), F(n**4, n*n))})
        r.truth('undersized_clip_bad_event_fails', F(n**4, n*n) > 1, n)
        r.truth('oversized_clip_same_edge_fails', F(n**6, n**4) > 1, n)
    # Uniform fourth moments alone do not imply decay: this is an abstract
    # scalar stress test only, not a particle-law counterexample.
    r.equal('bounded_fourth_not_decay', F(1)**4, F(1), 'constant nonzero scalar')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutant', choices=sorted(EXPECTED_MUTANTS))
    args = parser.parse_args()
    r = Runner(args.mutant)
    fourth_graphs(r)
    exact_haar_moments(r)
    fourier_and_labels(r)
    moment_and_cutoff_stress(r)
    if args.mutant:
        raise RuntimeError('Selected mutant did not encounter a nonzero witness')
    if set(r.witnesses) != EXPECTED_MUTANTS:
        raise RuntimeError('Missing mutation witnesses: '+str(EXPECTED_MUTANTS-set(r.witnesses)))
    print(json.dumps({'status': 'PASS', 'arithmetic': 'exact rational and Gaussian rational',
                      'assertions': sum(r.counts.values()), 'categories': dict(sorted(r.counts.items())),
                      'mutation_count': len(r.witnesses), 'mutation_witnesses': r.witnesses,
                      'limitations': ['finite algebra only', 'no SDE simulation',
                                      'no continuum or asymptotic certification',
                                      'finite Fourier kernels are diagnostic substitutes only']},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
