#!/usr/bin/env python3
"""Read-only default diagnostic; --write-result writes only the requested JSON.
Exact finite-group coefficient tests and a deterministic radial tail test.
No particle simulation, external libraries, or proof certification.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path

COUNTS = {}
WITNESSES = {}

def check(name, condition):
    COUNTS[name] = COUNTS.get(name, 0) + 1
    if not condition:
        raise AssertionError(name)

def mutation(name, wrong, right, context):
    if wrong != right and name not in WITNESSES:
        WITNESSES[name] = {"wrong": str(wrong), "correct": str(right), "context": context}

def mean(items):
    return sum(items, F(0)) / len(items)

def finite_tests():
    kernels = [(F(6), F(1), F(-4), F(-4), F(1)),
               (F(8), F(-1), F(-3), F(-3), F(-1))]
    cases = []
    for kernel in kernels:
        m = len(kernel)
        check('kernel_even', all(kernel[j] == kernel[-j % m] for j in range(m)))
        check('kernel_zero_mean', sum(kernel) == 0)
        for cap in [F(2), F(4), F(10)]:
            clipped = tuple(min(x, cap) for x in kernel)
            mu = mean(clipped)
            centered = tuple(x - mu for x in clipped)
            norm2 = mean([x*x for x in centered])
            check('clip_mean_nonpositive', mu <= 0)
            check('clip_centered', sum(centered) == 0)
            check('tail_mean_identity', mu == -mean([max(x-cap, F(0)) for x in kernel]))
            for n in range(2, 6):
                samples = list(itertools.product(range(m), repeat=n))
                hs, hls, bad_count = [], [], 0
                pairs = list(itertools.combinations(range(n), 2))
                for x in samples:
                    terms = [kernel[(x[i]-x[j]) % m] for i,j in pairs]
                    h = sum(terms, F(0))/n
                    hl = sum((centered[(x[i]-x[j]) % m] for i,j in pairs), F(0))/n
                    bad = any(z > cap for z in terms)
                    hs.append(h); hls.append(hl); bad_count += bad
                    if not bad:
                        check('good_event_exact_recenter', h == hl + F(n-1,2)*mu)
                        check('good_event_positive_domination', max(h, F(0)) <= abs(hl))
                empirical = mean([v*v for v in hls])
                right = F(n-1,2*n)*norm2
                check('initial_energy_mean', mean(hs) == 0)
                check('canonical_energy_mean', mean(hls) == 0)
                check('canonical_variance_coefficient', empirical == right)
                one_tail = F(sum(z>cap for z in kernel),m)
                check('unordered_bad_union_bound', F(bad_count,len(samples)) <= len(pairs)*one_tail)
                mutation('missing_unordered_half', F(n-1,n)*norm2, empirical, f'N={n},cap={cap}')
                mutation('wrong_N_denominator', F(n-1,2*n*n)*norm2, empirical, f'N={n},cap={cap}')
                mutation('replace_N_by_Nminus1', F(n,2*(n-1))*norm2, empirical, f'N={n},cap={cap}')
                if mu:
                    x = next(x for x in samples if all(kernel[(x[i]-x[j])%m] <= cap for i,j in pairs))
                    h = sum((kernel[(x[i]-x[j])%m] for i,j in pairs),F(0))/n
                    hl = sum((centered[(x[i]-x[j])%m] for i,j in pairs),F(0))/n
                    mutation('omit_clip_mean', hl, h, f'N={n},cap={cap},x={x}')
                    mutation('reverse_clip_mean', hl-F(n-1,2)*mu, h, f'N={n},cap={cap},x={x}')
                cases.append({'N':n, 'cap':str(cap), 'variance':str(empirical), 'bad_probability':str(F(bad_count,len(samples)))})
            # Independent conditional overlap test on three Haar coordinates.
            overlap = mean([centered[(x-y)%m]*centered[(x-z)%m]
                            for x,y,z in itertools.product(range(m),repeat=3)])
            raw_overlap = mean([clipped[(x-y)%m]*clipped[(x-z)%m]
                                for x,y,z in itertools.product(range(m),repeat=3)])
            check('canonical_one_label_overlap', overlap == 0)
            check('uncentered_overlap_equals_mean_square', raw_overlap == mu*mu)
            mutation('uncentered_clip_is_degenerate', F(0), raw_overlap, f'cap={cap},mean={mu}')
    # Literal ordered overlap counts for the dynamic correlation identity.
    for n in range(2,10):
        overlap = distinct = 0
        for i,j,k in itertools.product(range(n),repeat=3):
            if i == j: continue
            if k in (i,j): overlap += 1
            else: distinct += 1
        check('dynamic_overlap_count', overlap == 2*n*(n-1))
        check('dynamic_distinct_count', distinct == n*(n-1)*(n-2))
        check('dynamic_overlap_coefficient', F(overlap,2*n*n) == F(n-1,n))
        check('dynamic_distinct_coefficient', F(distinct,2*n*n) == F((n-1)*(n-2),2*n))
        mutation('drop_dynamic_overlap_two', F(overlap,4*n*n),F(n-1,n),f'N={n}')
        mutation('drop_dynamic_distinct_half', F(distinct,n*n),F((n-1)*(n-2),2*n),f'N={n}')
    return cases

def martingale_tests():
    # a is time-zero information; u,v are independent symmetric innovations.
    states = list(itertools.product([-1,1],repeat=3))
    rows=[]
    for a,u,v in states:
        first = (2 if a == 1 else 1)*u
        second = (3 if u == 1 else 1)*v
        terminal = first+second
        bracket = (2 if a == 1 else 1)**2+(3 if u == 1 else 1)**2
        rows.append((a,u,v,terminal,bracket))
    for a_value in [-1,1]:
        weighted_sq = mean([F(t*t if a == a_value else 0) for a,u,v,t,b in rows])
        weighted_br = mean([F(b if a == a_value else 0) for a,u,v,t,b in rows])
        check('time_zero_event_isometry',weighted_sq == weighted_br)
    weighted_sq = mean([F(t*t if t == 5 else 0) for a,u,v,t,b in rows])
    weighted_br = mean([F(b if t == 5 else 0) for a,u,v,t,b in rows])
    mutation('replace_initial_by_terminal_event',weighted_br,weighted_sq,'terminal event M=5')
    check('terminal_event_countercontrol_nonzero',weighted_sq != weighted_br)
    # Common-driver martingales need not have zero cross variation.
    cross = mean([F(u*(2*u+v)) for a,u,v in states])
    check('shared_driver_cross_term',cross == 2)
    mutation('drop_shared_driver_cross',F(0),cross,'U and 2U+V')


def scalar_tests():
    for a in [F(0),F(1,3),F(1),F(5)]:
        for x in [F(k,7) for k in range(100)]:
            excess=max(x-a,F(0))
            check('L1_L2_scalar_transfer',x*x <= 2*a*x+2*excess*excess)
            if x>2*a:
                check('uniform_integrability_tail',x*x <= 4*excess*excess)
    for n in [4,9,16,25,100]:
        # X=sqrt(N) with probability 1/N: E|X|->0, EX^2=1.
        root=int(math.isqrt(n))
        check('rare_spike_L1',F(root,n) == F(1,root))
        check('rare_spike_L2',F(n,n) == 1)
        check('rare_spike_breaks_new_overshoot',F((root-1)**2,n) > 0)
    # Critical rates in the exceptional event with L=N^2.
    for n in range(2,50):
        cap=n*n
        check('bad_event_N_cost',F(n**3,cap**2) == F(1,n))
        wrong=F(n**3,n**2) # Clipping at L=N is insufficient for this bound.
        mutation('clip_at_N_gives_vanishing_bad_cost',F(1,n),wrong,f'N={n}')
    # A fixed nonzero bounded random variable obeys a zero overshoot bound.
    check('tail_bound_does_not_force_zero', max(F(1)-F(2),F(0))**2 == 0)


def radial_tests():
    rows=[]
    # Deterministic quadrature in the logarithmic coordinate y=exp(t).
    # Simpson on a finite smooth interval; tolerance is diagnostic, not certification.
    for cap in [0.0,1.0,5.0,30.0,100.0]:
        r=cap+2
        mu=-1/r
        variance=2*math.log(r)-3+4/r-1/(r*r)
        m=20000; top=math.log(r); dt=top/m
        def fun(t):
            y=math.exp(t)
            return 2*(y-2-mu)**2*math.exp(-2*t)
        total=fun(0)+fun(top)
        total += 4*sum(fun(j*dt) for j in range(1,m,2))
        total += 2*sum(fun(j*dt) for j in range(2,m,2))
        quad=total*dt/3+(cap-mu)**2/r**2
        check('radial_clipped_variance_quadrature',abs(variance-quad) < 2e-10*max(1,abs(variance)))
        check('radial_clip_mean_sign',mu < 0)
        if cap>0:
            mutation('radial_omit_centering',2*math.log(r)-3+4/r,variance,f'L={cap}')
        rows.append({'L':cap,'tail':1/r**2,'mean':mu,'variance':variance,'quadrature':quad})
    for n in [2,4,16,256,4096,65536]:
        value=(2*math.log((n+2)/2)+4/(n+2)-2)/n
        check('radial_capped_second_nonnegative',value>0)
        check('radial_capped_second_log_rate',value<=2*math.log(n+2)/n)
        rows.append({'N':n,'capped_second':value})
    return rows


def run():
    finite=finite_tests(); martingale_tests(); scalar_tests(); radial=radial_tests()
    required=['missing_unordered_half','wrong_N_denominator','replace_N_by_Nminus1',
              'omit_clip_mean','reverse_clip_mean','uncentered_clip_is_degenerate',
              'drop_dynamic_overlap_two','drop_dynamic_distinct_half',
              'replace_initial_by_terminal_event','drop_shared_driver_cross',
              'clip_at_N_gives_vanishing_bad_cost','radial_omit_centering']
    for name in required:
        check('nonvacuous_mutation_witness',name in WITNESSES)
    return {'status':'PASS','assertions':sum(COUNTS.values()),'categories':COUNTS,
            'mutation_types':len(WITNESSES),'mutation_witnesses':WITNESSES,
            'finite_cases':finite,'radial_cases':radial,
            'reproducibility':{'arithmetic':'Fraction exact except labeled radial float quadrature',
                'random_seed':None,'sampling':'none','python':'standard library >=3.9',
                'radial_tolerance':'2e-10 * max(1,abs(exact_expression))',
                'radial_simpson_subintervals':20000,
                'scope':'coefficient/tail diagnostics, not a singular-SDE simulation or proof'},
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-result',type=Path)
    args=parser.parse_args()
    result=run()
    if args.write_result:
        args.write_result.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'assertions':result['assertions'],
                      'categories':len(result['categories']),'mutation_types':result['mutation_types']},sort_keys=True))
