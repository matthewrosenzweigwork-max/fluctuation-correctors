#!/usr/bin/env python3
"""Exact coefficient and uniform-parameter probes; not an analytic proof."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json

counts = {}
mutations = {}


def check(category, condition):
    if not condition:
        raise AssertionError(category)
    counts[category] = counts.get(category, 0) + 1


def reject(category, condition):
    check('mutation_' + category, condition)
    mutations[category] = mutations.get(category, 0) + 1


def determinant(matrix):
    if not matrix:
        return F(1)
    return sum((-1)**j * matrix[0][j] * determinant(
        [row[:j] + row[j+1:] for row in matrix[1:]])
        for j in range(len(matrix)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    for nu, D, a, r in product(
            [F(0), F(1, 1000), F(1, 2), F(1), F(2), F(10), F(10**6)],
            [F(1, 3), F(1), F(7, 2)], [F(1, 2), F(1), F(5)],
            [F(1, 2), F(2, 3), F(7, 8)]):
        b = min(1, 1/nu) if nu else F(1)
        L = D + nu*a
        check('uniform_normalization', 0 < b <= 1 and 0 <= nu*b <= 1)
        check('modal_partition', D/L + nu*a/L == 1)
        # Times are i * (-log r)/L: exact algebraic probes, not fixed-time proof.
        initial = [[b*r**(i+j) for j in range(4)] for i in range(4)]
        thermal = [[b*nu*a/L*(r**abs(i-j)-r**(i+j))
                    for j in range(4)] for i in range(4)]
        C = [[initial[i][j]+thermal[i][j] for j in range(4)] for i in range(4)]
        for i,j in product(range(4), repeat=2):
            closed = b*(D/L*r**(i+j)+nu*a/L*r**abs(i-j))
            check('integrated_covariance', C[i][j] == closed)
            # Independent discrete Gram realization of the integrated OU noise.
            gram = b*nu*a/L*(1-r*r)*sum(
                r**(i-z)*r**(j-z) for z in range(1,min(i,j)+1))
            check('thermal_gram', thermal[i][j] == gram)
            check('symmetry', C[i][j] == C[j][i])
            if not nu:
                check('zero_noise', thermal[i][j] == 0 and C[i][j] == r**(i+j))
            if i == 0 or j == 0:
                check('zero_time', thermal[i][j] == 0)
        for i in range(4):
            check('uniform_trace', 0 <= C[i][i] <= b)
            if nu > 1:
                check('hot_trace', C[i][i] <= 1/nu)
        for size in range(1,5):
            for indices in combinations(range(4),size):
                for label,matrix in [('total',C),('thermal',thermal),('initial',initial)]:
                    check(label+'_principal_minor', determinant(
                        [[matrix[i][j] for j in indices] for i in indices]) >= 0)
        if nu > 0:
            reject('missing_thermal', C[1][1] != initial[1][1])
            reject('missing_factor_two', C[1][1] != initial[1][1]+thermal[1][1]/2)
            reject('time_sum_for_thermal', thermal[1][1] != 0)
        reject('lag_for_initial', initial[1][1] != b)
        if nu > 1:
            reject('missing_b', C[0][0] != 1)
    # Literal finite-label Brownian bracket: N independent coordinates cancel N.
    for n,nu in product(range(2,15),[F(0),F(1,3),F(1),F(3),F(10**6)]):
        b = min(1,1/nu) if nu else F(1)
        field = [F(i+1,n) for i in range(n)]
        literal = sum(2*nu*b/n*x*x for x in field)
        empirical = 2*nu*b*sum(x*x for x in field)/n
        check('literal_bracket', literal == empirical)
        if nu:
            reject('deleted_label_bracket', literal != empirical*F(n-1,n))
    # F0-measurable variance: orthogonality does not imply independence.
    for e in [F(1,7),F(1,3),F(3,4)]:
        check('conditional_mixture', ((1+e)-(1-e))/2 == e)
        reject('finite_N_independence', e != 0)
        # Conditional Gaussian CF exp(-q z²/2) times compensator exp(q z²/2).
        for q in [1-e,1+e]:
            check('positive_compensator', -q/2+q/2 == 0)
            reject('negative_compensator', -q/2-q/2 != 0)
            reject('mean_bracket_substitution', -q/2+F(1,2) != 0)
    for d in range(3,15):
        for s in [F(j,4) for j in range(1,4*(d-2)+1)]:
            theta=1-s/d; kappa=F(1,2)-s/d
            check('source_exponents', s < d and theta > 0)
            check('strict_decay_boundary', (kappa > 0) == (s < F(d,2)))
            check('energy_balance', -1+s/d == -(d-s)/d)
    result = {'status':'PASS','assertions':sum(counts.values()),'categories':counts,
              'mutation_rejections':mutations,'randomness':None,'tolerance':None,
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'limitations':'Exact rational coefficient probes only. Grid times vary with modal parameters. No singular, uniform-limit, or probabilistic theorem is computationally certified.'}
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','assertions':result['assertions'],
                      'categories':len(counts),'mutation_families':len(mutations)}))


if __name__ == '__main__':
    main()
