#!/usr/bin/env python3
"""New root exact diagnostics; normalized spatial second derivatives omit (2*pi)^2.
K=-i sum k*g_k e_k, grad=i D, so force-gradient products are K0*D.
This is a finite smooth algebra check, not a singular-law simulation or proof.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

counts=Counter(); witnesses=Counter()
def check(ok,name):
    if not ok: raise AssertionError(name)
    counts[name]+=1

def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return clean(out)
def scale(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
    out={}
    for k,v in p.items():
        for l,w in q.items():
            n=tuple(a+b for a,b in zip(k,l));out[n]=out.get(n,F(0))+v*w
    return clean(out)
def derivative(p,i):return clean({k:v*k[i] for k,v in p.items()})
def lap(p):return clean({k:-v*sum(a*a for a in k) for k,v in p.items()})
def pull(p,slots,n):
    out={}
    for k,v in p.items():
        target=[0]*n
        for a,slot in zip(k,slots):target[slot]+=a
        target=tuple(target);out[target]=out.get(target,F(0))+v
    return clean(out)
def row(p):return clean({(k[0],):v for k,v in p.items() if k[1]==0})
def mean(p):return p.get(tuple(0 for _ in next(iter(p),())),F(0)) if p else F(0)
def eta(p,n):return scale(add(*(pull(p,[i],n) for i in range(n))),F(1,n))
def D2(p,n):return scale(add(*(pull(p,[i,j],n) for i,j in permutations(range(n),2))),F(1,n*n))
def pair(p,n):return add(scale(D2(p,n),F(1,2)),scale(eta(row(p),n),-1),{(0,)*n:mean(p)/2})

kernels=[{}, {(1,):F(1,2),(-1,):F(1,2)}, {(1,):F(2,3),(-1,):F(2,3),(2,):F(1,5),(-2,):F(1,5)}]
tests=[{(0,):F(2)}, {(1,):F(1,2),(-1,):F(1,2)}, {(0,):F(3),(1,):F(1,3),(-1,):F(1,3),(3,):F(1,7),(-3,):F(1,7)}]
for g in kernels:
    K={(k[0],-k[0]):k[0]*v for k,v in g.items()}
    for f in tests:
        J=mul(K,add(pull(derivative(f,0),[0],2),scale(pull(derivative(f,0),[1],2),-1)))
        R=clean({k:-k[0]**2*g.get(k,F(0))*v for k,v in f.items()})
        check(row(J)==R,'source_row_is_full_response')
        check(mean(J)==0,'source_scalar_zero')
        check(pull(J,[0,0],1)=={},'smooth_source_diagonal_zero')
        for n in [2,3,4,5]:
            observable=eta(f,n)
            force={}
            for i,j in permutations(range(n),2):
                force=add(force,scale(mul(pull(K,[i,j],n),derivative(observable,i)),F(1,n)))
            check(force==scale(D2(J,n),F(1,2)),'ordered_force_symmetrization')
            check(force==add(pair(J,n),eta(R,n)),'all_background_first_order_identity')
            for nu in [F(0),F(1,3),F(2)]:
                time_derivative=add(scale(lap(f),-nu),scale(R,-1))
                full=add(eta(time_derivative,n),scale(lap(observable),nu),force)
                check(full==pair(J,n),'backward_generator_cancellation')
                bracket=scale(add(*(mul(derivative(observable,i),derivative(observable,i)) for i in range(n))),-2*nu)
                direct=scale(eta(scale(mul(derivative(f,0),derivative(f,0)),-1),n),2*nu/n)
                check(bracket==direct,'whole_first_order_bracket')
                check(n*mean(bracket)==2*nu*mean(scale(mul(derivative(f,0),derivative(f,0)),-1)),'scaled_Haar_bracket')
            if force!=add(pair(J,n),scale(eta(R,n),-1)):witnesses['flipped_response']+=1
            if force!=add(scale(pair(J,n),2),eta(R,n)):witnesses['doubled_pair_source']+=1
            if force!=add(scale(pair(J,n),F(n,n-1)),eta(R,n)):witnesses['falling_factorial_source']+=1

# Direct initial iid covariance for centered bounded Fourier polynomials.
for f in tests:
    centered=add(f,{(0,):-mean(f)})
    for h in tests:
        centered_h=add(h,{(0,):-mean(h)})
        for n in [2,3,4,5]:
            check(n*mean(mul(eta(centered,n),eta(centered_h,n)))==mean(mul(centered,centered_h)),'initial_iid_vector_covariance')

# Exact semigroup factor check at integer times, with rational dampings.
for damp in [F(1,2),F(2,3),F(3,4)]:
    for ti,tj in [(0,0),(0,2),(1,1),(1,3),(2,4)]:
        f={(1,):damp**ti/2,(-1,):damp**ti/2}
        h={(1,):damp**tj/2,(-1,):damp**tj/2}
        covariance=mean(mul(f,h))
        check(covariance==damp**(ti+tj)/2,'joint_time_covariance_uses_sum')
        if covariance!=damp**abs(ti-tj)/2:witnesses['stationary_time_difference_covariance']+=1
        determinant=mean(mul(f,f))*mean(mul(h,h))-covariance**2
        check(determinant==0,'admitted_degenerate_covariance')

for d in range(3,17):
    for denominator in range(2,10):
        for numerator in range(1,denominator*(d-2)+1):
            s=F(numerator,denominator)
            if s>=F(d,2):continue
            theta=1-s/d
            check(s/d-F(1,2)<0,'source_scaled_exponent')
            check(-theta/2<0,'thermal_scaled_exponent')
            check(-theta<0,'backward_test_replacement_exponent')
            check(s<=d-2 and d-s>=2,'Coulomb_inclusive_kernel_range')
for name in ['flipped_response','doubled_pair_source','falling_factorial_source','stationary_time_difference_covariance']:
    check(witnesses[name]>0,'mutation_detected_'+name)
result={'status':'PASS','assertions':sum(counts.values()),'counts':dict(sorted(counts.items())),'mutation_witnesses':dict(sorted(witnesses.items())),'arithmetic':'fractions.Fraction; exact Laurent coefficients; no random seed or tolerance','physical_convention':'Force/generator/bracket second-order expressions restore (2*pi)^2; normalized diffusion has Laplacian multiplier -k^2.','limitations':['No actual singular law is simulated.','Polynomial semigroup probes check covariance factors only.','Finite algebra and rational exponents do not certify continuum estimates or weak convergence.','Root constructor self-check, not independent audit.']}
Path(__file__).with_name('EXACT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,sort_keys=True))
