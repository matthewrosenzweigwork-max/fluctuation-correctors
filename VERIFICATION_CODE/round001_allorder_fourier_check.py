#!/usr/bin/env python3
"""Independent k=1..4 Fourier check of the frozen recursion statement.

Direct differentiation of expanded U_k versus incidence-defined operators.
Standard-library exact fractions; uniform stationary reference, g=cos(2pi x).
No discovery code is imported. Common polynomial primitives come only from
root's earlier, independently authored pair verifier.
"""
from fractions import Fraction as F
from itertools import product,permutations
from math import comb
import json
from round001_fourier_pair_check import add,scale,centered_stat,generator


def internal(phi,pairs):
    out={}
    for modes,c in phi.items():
        for a,b in pairs:
            for m in (-1,1):
                v=list(modes);v[a]+=m;v[b]-=m;v=tuple(v)
                out[v]=out.get(v,F(0))+F(m*(modes[a]-modes[b]),2)*c
    return {k:v for k,v in out.items() if v}


def integrate_last(phi,count):
    out={}
    for modes,c in phi.items():
        if not any(modes[-count:]):
            key=modes[:-count];out[key]=out.get(key,F(0))+c
    return {k:v for k,v in out.items() if v}


def operators(phi,k,nu):
    linear={m:-c*(nu*sum(a*a for a in m)+sum(F(a*a,2) for a in m if abs(a)==1)) for m,c in phi.items()}
    pair=internal(phi,[(a,b) for a in range(k) for b in range(a+1,k)])
    up={}
    for modes,c in phi.items():
        for a in range(k):
            for m in (-1,1):
                key=list(modes)+[-m];key[a]+=m;key=tuple(key)
                up[key]=up.get(key,F(0))+F(m*modes[a],2)*c
    q=integrate_last(internal(phi,[(a,k-1) for a in range(k-1)]),1) if k>=2 else {}
    r=integrate_last(internal(phi,[(k-2,k-1)]),2) if k>=2 else {}
    return linear,pair,up,q,r


def evaluate(phi,n,order):
    if order==0:return {(0,)*n:phi.get((),F(0))} if phi.get((),F(0)) else {}
    return centered_stat(phi,n) if phi else {}


def test_kernel(k,kind):
    if kind=='constant':return {(0,)*k:F(1)}
    if kind=='sum':return {(1,)*k:F(1,2),(-1,)*k:F(1,2)}
    if kind=='product':return {m:F(1,2**k) for m in product((-1,1),repeat=k)}
    base=(2,-1)+(0,)*(k-2) if k>=2 else (2,)
    modes=set(permutations(base));out={}
    for m in modes:
        out[m]=out.get(m,F(0))+F(1,2*len(modes))
        neg=tuple(-a for a in m);out[neg]=out.get(neg,F(0))+F(1,2*len(modes))
    return out


def main():
    cases=[]
    for k,n,nu,kind in product(range(1,5),(2,3,4),(F(0),F(1,3),F(2)),('constant','sum','product','mixed')):
        phi=test_kernel(k,kind)
        left=generator(evaluate(phi,n,k),n,nu)
        l,c,a,q,r=operators(phi,k,nu)
        right=add(evaluate(l,n,k),scale(evaluate(c,n,k),F(1,n)),evaluate(a,n,k+1),scale(evaluate(q,n,k-1),F(k,n)),scale(evaluate(r,n,k-2),F(comb(k,2),n)) if k>=2 else {})
        error=add(left,scale(right,-1))
        assert not error,(k,n,str(nu),kind,error)
        cases.append({'k':k,'N':n,'nu':str(nu),'kernel':kind,'residual_terms':0})
    print(json.dumps({'status':'PASS','exact_rational_cases':len(cases),'scope':'k1-k4 uniform smooth Fourier model, no singular power counting','cases':cases},indent=2))


if __name__=='__main__':main()
