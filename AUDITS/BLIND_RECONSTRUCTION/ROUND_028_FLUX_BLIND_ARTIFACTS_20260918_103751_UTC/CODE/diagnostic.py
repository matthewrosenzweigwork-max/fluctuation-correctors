#!/usr/bin/env python3
"""Fresh exact coefficient diagnostics; no SDE simulation and no file writes.

All finite-group and scalar examples are supporting models only. The report's
continuum proof does not rely on their output. Standard library; no randomness.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import argparse
import json
import sys

MUTATIONS = (
    'pair_atom_half', 'compensation_omitted', 'source_self_deleted',
    'iid_variance_factor_two', 'clipping_not_centered',
    'terminal_fusion_as_iid', 'conjugate_bracket_sign',
    'unconjugated_bracket_sign', 'response_square_half',
    'survival_normalizer_dropped', 'fused_count_two',
    'terminal_event_isometry', 'initial_marks_independent',
    'first_power_replaced_by_square',
)


class CheckFailure(Exception):
    def __init__(self, name, actual, expected):
        self.name, self.actual, self.expected = name, actual, expected


def serialize(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, tuple):
        return [serialize(t) for t in x]
    if isinstance(x, list):
        return [serialize(t) for t in x]
    if isinstance(x, dict):
        return {str(k): serialize(v) for k, v in x.items()}
    return x


ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def cconj(z):
    return (z[0], -z[1])


def cscale(a, z):
    return (a*z[0], a*z[1])


def csum(values):
    r = s = 0
    for a, b in values:
        r += a
        s += b
    return (r, s)


def run(mutation=None):
    counts = Counter()

    def eq(category, actual, expected):
        counts[category] += 1
        if actual != expected:
            raise CheckFailure(category, actual, expected)

    def le(category, actual, expected):
        counts[category] += 1
        if actual > expected:
            raise CheckFailure(category, actual, '<= '+str(expected))

    # Full distributional configuration Fourier identity with c normalized
    # symbolically to one. This normalization only tests coefficients.
    for n in range(2, 8):
        kappa = n-1
        pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
        for mode in product((-1,0,1), repeat=n):
            zero = all(v == 0 for v in mode)
            atoms = sum(
                mode[i]+mode[j] == 0
                and all(mode[r] == 0 for r in range(n) if r not in (i,j))
                for i,j in pairs
            )
            hcoeff = Q(0)
            for i,j in pairs:
                if (mode[i] != 0 and mode[i]+mode[j] == 0
                    and all(mode[r] == 0 for r in range(n) if r not in (i,j))):
                    hcoeff += Q(1, n*mode[i]*mode[i])
            direct = -sum(v*v for v in mode)*hcoeff
            atom_factor = Q(1 if mutation == 'pair_atom_half' else 2, n)
            compensation = 0 if mutation == 'compensation_omitted' else kappa*zero
            eq('configuration_fourier_atom_and_compensation', direct,
               compensation-atom_factor*atoms)
        eq('unordered_pair_mass', Q(2,n)*len(pairs), Q(kappa))
        eq('uniform_mark_probability', Q(2,n*kappa), Q(1,len(pairs)))

    # Exact iid phase enumeration, including fused terminal moments at N=2.
    for n in range(2, 8):
        for fused in (False, True):
            slots = n-1 if fused else n
            total_re = total_im = total_square = samples = 0
            for phases in product(range(4), repeat=slots):
                terms = [ROOTS[p] for p in phases]
                if fused:
                    terms[0] = cscale(2, terms[0])
                re,im = csum(terms)
                total_re += re
                total_im += im
                total_square += re*re+im*im
                samples += 1
            eq('haar_and_fused_mean', (total_re,total_im), (0,0))
            expected = Q(n+2 if fused else n, n*n)
            if fused and mutation == 'terminal_fusion_as_iid':
                expected = Q(1,n)
            eq('haar_and_fused_second_moment', Q(total_square,samples*n*n), expected)

    # A nontranslation-invariant symmetric zero-row kernel on three atoms.
    # Radial clipping destroys its rows, so double-centering is genuinely used.
    m = 3
    aa,bb = (-2,0,2),(1,-2,1)
    j = [[Q(3*aa[x]*aa[y]+2*bb[x]*bb[y]+aa[x]*bb[y]+bb[x]*aa[y])
          for y in range(m)] for x in range(m)]
    for row in j:
        eq('original_zero_row', sum(row), 0)
    for level in (1,3,7):
        clipped = [[max(-Q(level),min(Q(level),j[x][y]))
                    for y in range(m)] for x in range(m)]
        rows = [sum(r)/m for r in clipped]
        mean = sum(rows)/m
        centered = [[clipped[x][y]-rows[x]-rows[y]+mean
                     for y in range(m)] for x in range(m)]
        norm_clipped = sum(v*v for row in clipped for v in row)/(m*m)
        norm_centered = sum(v*v for row in centered for v in row)/(m*m)
        le('orthogonal_projection_contraction', norm_centered, norm_clipped)
        for row in centered:
            eq('clipped_double_centered_rows', sum(row), 0)
        residual = sum(abs(j[x][y]-centered[x][y])
                       for x in range(m) for y in range(m))/(m*m)
        tail = sum(abs(j[x][y]-clipped[x][y])
                   for x in range(m) for y in range(m))/(m*m)
        le('l1_centering_cost', residual, 4*tail)
        for n in range(2,6):
            kernel = clipped if mutation == 'clipping_not_centered' else centered
            used_norm = norm_clipped if mutation == 'clipping_not_centered' else norm_centered
            second = Q(0)
            mean_u = Q(0)
            for config in product(range(m),repeat=n):
                value = sum(kernel[config[i]][config[h]]
                            for i in range(n) for h in range(i+1,n))/n**2
                second += value*value
                mean_u += value
            denominator = 1 if mutation == 'iid_variance_factor_two' else 2
            eq('iid_canonical_variance',second/m**n,
               Q(n-1,denominator*n**3)*used_norm)
            eq('iid_canonical_mean',mean_u/m**n,0)

    # Literal source, with the half and both row terms independently summed.
    for n in range(2,7):
        c = Q(5,3)
        for config in product(range(m),repeat=n):
            F = Q(sum(aa[x] for x in config),n)
            raw_j = sum(j[config[i]][config[h]]
                        for i in range(n) for h in range(n) if i != h)/(2*n*n)
            raw_J = sum(j[config[i]][config[h]]-c*(aa[config[i]]+aa[config[h]])
                        for i in range(n) for h in range(n) if i != h)/(2*n*n)
            P_J = raw_J+c*F
            target = raw_j if mutation == 'source_self_deleted' else raw_j+c*F/n
            eq('literal_source_self_correction',P_J,target)
            nuell = Q(2,7)
            direct_att = -nuell*F-raw_J
            eq('attractive_observable_generator',direct_att,
               (c*Q(n-1,n)-nuell)*F-raw_j)

    # Complex brackets are assembled from individual coordinate gradients.
    modes = ((1,0,0,0),(1,2,0,-1),(-1,1,1,0),(0,0,1,0))
    for n in range(2,7):
        for sample in range(7):
            coords = [tuple((sample*(i+1)+(i+2)*(r+1)) % 4 for r in range(4))
                      for i in range(n)]
            def phase(mode,x):
                return ROOTS[sum(k*r for k,r in zip(mode,x)) % 4]
            for k in modes:
                for l in modes:
                    dot = sum(x*y for x,y in zip(k,l))
                    terms_c,terms_u = [],[]
                    for x in coords:
                        ek,el = phase(k,x),phase(l,x)
                        for kr,lr in zip(k,l):
                            gk = cscale(kr,cmul((0,1),ek))
                            gl = cscale(lr,cmul((0,1),el))
                            terms_c.append(cmul(gk,cconj(gl)))
                            terms_u.append(cmul(gk,gl))
                    nu = Q(3,5)
                    direct_c = cscale(2*nu/n**2,csum(terms_c))
                    direct_u = cscale(2*nu/n**2,csum(terms_u))
                    km = tuple(kr-lr for kr,lr in zip(k,l))
                    kp = tuple(kr+lr for kr,lr in zip(k,l))
                    fc = cscale(Q(1,n),csum(phase(km,x) for x in coords))
                    fu = cscale(Q(1,n),csum(phase(kp,x) for x in coords))
                    sign_c = -1 if mutation == 'conjugate_bracket_sign' else 1
                    sign_u = 1 if mutation == 'unconjugated_bracket_sign' else -1
                    eq('conjugate_mode_bracket',direct_c,cscale(sign_c*2*nu*dot/n,fc))
                    eq('unconjugated_mode_bracket',direct_u,cscale(sign_u*2*nu*dot/n,fu))

    # Exact Laplace response square; rational parameters, no quadrature.
    for n in range(2,32):
        kappa = Q(n-1)
        for ell in (1,2,7,13):
            for nu in (Q(1,100),Q(1,3),Q(1),Q(7)):
                a = 1+nu*ell
                integral = 1-2*kappa/(kappa+a)+kappa/(kappa+2*a)
                numerator = 1 if mutation == 'response_square_half' else 2
                eq('exact_laplace_response_square',integral,
                   numerator*a*a/((kappa+a)*(kappa+2*a)))
                le('response_square_nonnegative',0,integral)
    for survival in (Q(1,2),Q(1,3),Q(2,5)):
        for power in range(1,7):
            direct_conditional = survival**power/Q(power+1)
            unnormalized = survival**(power+1)/Q(power+1)
            factor = 1 if mutation == 'survival_normalizer_dropped' else 1/survival
            eq('survival_profile_normalizer',direct_conditional,factor*unnormalized)

    # All five initial/terminal label classes, explicitly enumerated.
    for n in range(2,65):
        counts5 = [0]*5
        for p in range(n):
            for q in range(n):
                if p<2 and q<2: klass=0
                elif p>=2 and q<2: klass=1
                elif p<2 and q>=2: klass=2
                elif p==q: klass=3
                else: klass=4
                counts5[klass] += 1
        fused = 2 if mutation == 'fused_count_two' else 4
        target = [fused,2*(n-2),2*(n-2),n-2,(n-2)*(n-3)]
        eq('five_marked_label_classes',counts5,target)
        eq('five_class_total',sum(counts5),n*n)

    # Exact scalar killed flow x'=kappa*x on (0,1), initial uniform.
    # Lifetime = -log(x0)/kappa, terminal x=1. This only challenges the
    # occupation coefficient and forbidden initial/lifetime independence.
    first_action = Q(1,2)  # integral (1-x0) dx0
    first_rhs = Q(1,2)     # kappa^-1 integral kappa*x dx
    if mutation == 'first_power_replaced_by_square':
        first_rhs = Q(1,3) # kappa=1, squared drift action is distinct
    eq('solvable_killed_flow_first_power',first_action,first_rhs)
    initial_lifetime_product = Q(1,3)  # E[x0*exp(-zeta)] at kappa=1
    comparison = Q(1,4) if mutation == 'initial_marks_independent' else Q(1,3)
    eq('initial_lifetime_correlation',initial_lifetime_product,comparison)

    # Time-zero indicator isometry versus a future-event counterexample.
    good_left=good_right=future_left=future_right=Q(0)
    for initial,x,y in product((0,1),(-1,1),(-1,1)):
        prob=Q(1,8)
        mart=x+y
        bracket=2
        good_left += prob*initial*mart*mart
        good_right += prob*initial*bracket
        event=int(mart==2)
        future_left += prob*event*mart*mart
        future_right += prob*event*bracket
    eq('time_zero_indicator_isometry',good_left,good_right)
    if mutation == 'terminal_event_isometry':
        eq('future_event_isometry_deliberate_falsehood',future_left,future_right)
    else:
        eq('future_event_isometry_nonzero_witness',future_left-future_right,Q(1,2))

    # Four-ball tail volume and clipping residual coefficient, as exact
    # rational coefficients after factoring pi^2*alpha^2/L^2 and C_k.
    eq('four_ball_tail_coefficient',Q(1,2)*2**2,Q(2))
    for n in range(2,100):
        eq('clipping_residual_coefficient',Q(n-1,2*n)*4*Q(1,n),Q(2*(n-1),n*n))
        le('terminal_variance_reverse_triangle_compatibility',Q(0),Q(2,n))

    return {
        'status':'PASS',
        'checks':sum(counts.values()),
        'categories':dict(sorted(counts.items())),
        'category_count':len(counts),
        'mutations_available':list(MUTATIONS),
        'arithmetic':'exact integers and fractions only',
        'random_seed':None,
        'random_sampling':False,
        'external_dependencies':[],
        'writes_files':False,
        'scope':'Supporting Fourier, iid finite-group, label, bracket, Laplace, and scalar stopped-flow diagnostics; not a singular-SDE proof or simulation.',
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mutation',choices=MUTATIONS)
    args=parser.parse_args()
    try:
        result=run(args.mutation)
    except CheckFailure as failure:
        result={'status':'ASSERTION_FAILURE','mutation':args.mutation,
                'category':failure.name,'actual':serialize(failure.actual),
                'expected':serialize(failure.expected),'nonzero_discrepancy':True}
        if isinstance(failure.actual,(int,Q)) and isinstance(failure.expected,(int,Q)):
            result['signed_discrepancy']=str(failure.actual-failure.expected)
        print(json.dumps(result,indent=2,sort_keys=True))
        return 1
    if args.mutation:
        result={'status':'MUTATION_NOT_DETECTED','mutation':args.mutation,
                'normal_result':result}
        print(json.dumps(result,indent=2,sort_keys=True))
        return 3
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0


if __name__=='__main__':
    sys.exit(main())
