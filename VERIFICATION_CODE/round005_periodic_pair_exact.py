#!/usr/bin/env python3
"""Exact finite checks supporting TASK-036; the memorandum supplies the proof."""
from fractions import Fraction as Q
from math import ceil
from pathlib import Path
import json


def power(base, den, exponent):
    n = Q(exponent) * den
    assert n.denominator == 1
    return Q(base) ** n.numerator


counts = {'profile_derivative_checks': 0, 'cutoff_product_checks': 0,
          'barrier_absorption_checks': 0, 'norm_factor_checks': 0}
for s in (Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3), Q(4)):
    p = s + 2
    den = s.denominator
    rbase = Q(1, 4)
    r = power(rbase, den, 1)
    rp = lambda exponent: power(rbase, den, exponent)
    for d in (ceil(p), ceil(p) + 1):
        for n in (2, 3, 17):
            for k in (1, 2, 3):
                ubase = k * rbase
                up = lambda exponent: power(ubase, den, exponent)
                tau = n * (up(p) - rp(p)) / (2 * s * p)
                f = Q(n, 4) * (up(2) - rp(2))
                fr = Q(n, 4) * ((Q(2)/p)*up(-s)*p*rp(p-1) - 2*r)
                frr = Q(n, 4) * (
                    (Q(2)/p)*((Q(2)/p-1)*up(-2*s-2)*(p*rp(p-1))**2
                               + up(-s)*p*(p-1)*rp(p-2)) - 2)
                ft = s * up(-s)
                lap = frr + (d-1)*fr/r
                q = rp(p)/up(p)
                qgamma = power(rbase/ubase, den, s)
                assert lap == Q(n, 2)*(qgamma*(d+s-s*q)-d)
                assert ft - (2*s/n)*rp(-s-1)*fr == s*rp(-s)
                assert lap <= 0
                assert 0 <= -r*fr <= s*f
                assert 0 <= f <= s*tau*rp(-s)
                assert abs(fr) <= s*s*tau*rp(-s-1)
                assert abs(frr) <= 3*s*s*(s+1)*tau*rp(-s-2)
                if k == 1:
                    assert tau == f == fr == frr == 0
                counts['profile_derivative_checks'] += 1
    for lipschitz in (Q(0), Q(1, 7), Q(3)):
        alpha = 1 + s*lipschitz
        for hessian in (Q(0), Q(2, 3), Q(5)):
            for error in (Q(0), Q(11, 2), Q(10**6)):
                for bounded_source in (Q(0), Q(7, 3)):
                    cb = bounded_source + hessian*error/alpha
                    assert alpha - s*lipschitz == 1
                    assert cb >= bounded_source
                    assert alpha*cb-hessian*error == alpha*bounded_source
                    counts['barrier_absorption_checks'] += 1

# An exact local polynomial product-rule check, including the 4 nu cross term.
for z in (Q(1, 5), Q(1, 3), Q(2, 3)):
    chi = 1-z*z+z**5
    cp = -2*z+5*z**4
    cpp = -2+20*z**3
    polynomial = z**3+2*z**4
    first = 3*z*z+8*z**3
    second = 6*z+24*z*z
    for nu in (Q(0), Q(1, 10), Q(1), Q(10**6)):
        for drift in (Q(-3), Q(0), Q(5)):
            for tau in (Q(0), Q(1, 7), Q(2)):
                direct = (chi*polynomial
                          -2*nu*tau*(cpp*polynomial+2*cp*first+chi*second)
                          -drift*tau*(cp*polynomial+chi*first))
                decomposed = (chi*(polynomial-2*nu*tau*second-drift*tau*first)
                              -tau*polynomial*(2*nu*cpp+drift*cp)
                              -4*nu*cp*tau*first)
                assert direct == decomposed
                counts['cutoff_product_checks'] += 1

for n in (2, 3, 17):
    for d_lower in (Q(0), Q(2, 5), Q(7)):
        for c_lower in (Q(0), Q(3, 7), Q(11)):
            pair_div_lower = -d_lower-d_lower-Q(2,n)*c_lower
            norm_exponent = d_lower+c_lower/n
            assert pair_div_lower == -2*norm_exponent
            assert -pair_div_lower/2 == norm_exponent
            counts['norm_factor_checks'] += 1

out = {'status':'all exact rational arithmetic checks passed',
       'scope':'finite checks supporting, not certifying, the parameter-uniform proof',
       'arithmetic':'Python standard-library fractions; no floating point',
       'counts':counts,'total_checks':sum(counts.values()),
       'particle_numbers':[2,3,17],
       'riesz_exponents':['1/2','1','3/2','2','3','4']}
Path(__file__).with_name('round005_periodic_pair_exact_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
