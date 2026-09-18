#!/usr/bin/env python3
"""Exact range and initial-endpoint diagnostics; no singular proof claim."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

counts={}
mutations={}


def check(category,condition):
    assert condition,category
    counts[category]=counts.get(category,0)+1


def reject(category,condition):
    assert condition,category
    mutations[category]=mutations.get(category,0)+1


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    for d in range(3,31):
        for j in range(1,8*(d-2)):
            s=F(j,8)
            if s*(s+2)>=2*d:
                continue
            p=s+2;a=s/p;theta=1-s/d
            lo=max(1,s/2);hi=min(F(d,2),d-s-1,s+1);q=(lo+hi)/2
            kappa=(2*q-s)/(2*p)
            check('strict_source_range',s<F(d,2))
            check('lower_range',3*s<2*d-2)
            check('admissible_midpoint',lo<q<hi and 1<q<F(d,2) and q<=s+1)
            check('source_decay',s/d-F(1,2)<0)
            check('initial_decay',-F(1,2)<0)
            check('noise_decay',(a-theta)/2<0)
            check('lower_decay',kappa>0)
            check('critical_rescaling',-theta+2/p==s*(s+2-d)/(d*p)<0)
            check('noise_polynomial',theta-a==(2*d-s*(s+2))/(d*p))
            reject('missing_noise_1_over_N', (a-theta+2)/2 >= 0)
        s0=F(2*(d-1),3)
        check('range_factorization',s0*(s0+2)-2*d==F(2*(2*d+1)*(d-4),9))
    check('source_equality_no_decay',F(1,2)-F(1,2)==0)
    check('noise_equality_no_decay',F(2,4)-(1-F(2,4))==0)
    reject('strict_endpoint_mutation', not (F(2,4)-(1-F(2,4))<0))
    # Three distinct finite probability-space kernels: constant, additive, mixed.
    points=[F(-1),F(0),F(1)]
    kernels=[[[F(2) for y in points] for x in points],
             [[x+y+1 for y in points] for x in points],
             [[2*x*y+x*x+y*y+x+y+F(1,3) for y in points] for x in points]]
    for table in kernels:
        row=[sum(r)/3 for r in table];m=sum(row)/3
        q0=[r-m for r in row]
        fc=[[table[i][j]-q0[i]-q0[j]-m for j in range(3)] for i in range(3)]
        norm=sum(v*v for r in table for v in r)/9
        cnorm=sum(v*v for r in fc for v in r)/9
        qnorm=sum(v*v for v in q0)/3
        check('orthogonal_norm',norm==cnorm+2*qnorm+m*m)
        check('zero_rows',all(sum(r)==0 for r in fc))
        for n in range(2,7):
            moment=F(0)
            for x in product(range(3),repeat=n):
                raw=sum(table[x[i]][x[j]] for i in range(n) for j in range(n) if i!=j)
                value=raw/(2*n*n)-sum(row[k] for k in x)/n+m/2
                deg=sum(fc[x[i]][x[j]] for i in range(n) for j in range(n) if i!=j)
                canonical=deg/(2*n*n)-sum(q0[k] for k in x)/(n*n)-m/(2*n)
                check('literal_deleted_decomposition',value==canonical)
                moment+=value*value
            moment/=3**n
            claimed=F(n-1,2*n**3)*cnorm+qnorm/n**3+m*m/(4*n*n)
            check('exact_iid_second_moment',moment==claimed)
            check('initial_scaled_L2_bound',n*moment<=norm/(2*n))
            if m:
                reject('missing_scalar_endpoint',moment!=claimed-m*m/(4*n*n))
    # Exact lower functional: rho[g]=eta[g]-c, both original terms retained.
    for n,eta,c in product(range(2,8),[F(-1),F(2,3),F(4)],[F(-2),F(1,5),F(3)]):
        lower=(eta-c)/n+c/(2*n)
        check('lower_scalar_half',lower==eta/n-c/(2*n))
        reject('discard_scalar_lower',lower!=(eta-c)/n)
    result={'status':'PASS','assertions':sum(counts.values()),'categories':counts,
            'mutation_rejections':mutations,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'random_seed':None,'tolerance':None,
            'limitations':'Finite exact range and iid/normalization diagnostics. Singular dynamics, imported analytic estimates and their uniformity are proved in full source documents, not by this program.'}
    if args.output.exists():raise FileExistsError(args.output)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','assertions':result['assertions'],'categories':len(counts),'mutation_families':len(mutations)}))


if __name__=='__main__':main()
