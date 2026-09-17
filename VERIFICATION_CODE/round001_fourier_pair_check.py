#!/usr/bin/env python3
"""Independent exact Laurent-polynomial check, no symbolic dependencies.

Unit torus, uniform stationary reference, V=0, g=cos(2pi x).
All generator expressions are divided by (2pi)^2; rational coefficients
are compared exactly. This finite battery supports, but does not prove,
the general identity. Differentiation is by particle coordinates after
expanding the observable, independently of the hierarchy algorithm.
"""
from fractions import Fraction as F
from itertools import product, combinations, permutations
import json


def add(*polys):
    out = {}
    for p in polys:
        for k,v in p.items(): out[k] = out.get(k,F(0)) + v
    return {k:v for k,v in out.items() if v}


def scale(p,c): return {k:v*c for k,v in p.items() if v*c}


def mul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            z=tuple(x+y for x,y in zip(k,l));out[z]=out.get(z,F(0))+v*w
    return {k:v for k,v in out.items() if v}


def diff(p,i,order=1):
    # Actual derivative is (2pi i)^order times this polynomial.
    return {k:v*k[i]**order for k,v in p.items() if k[i]}


def insert(phi,slots,n):
    out={}
    for modes,c in phi.items():
        key=[0]*n;ok=True
        for mode,slot in zip(modes,slots):
            if slot is None and mode:ok=False;break
            if slot is not None:key[slot]+=mode
        if ok:out[tuple(key)]=out.get(tuple(key),F(0))+c
    return {k:v for k,v in out.items() if v}


def p_observable(phi,n):
    terms=[]
    for i in range(n):
        for j in range(n):
            if i!=j:terms.append(scale(insert(phi,(i,j),n),F(1,2*n*n)))
        terms.append(scale(insert(phi,(i,None),n),-F(1,n)))
    terms.append(scale(insert(phi,(None,None),n),F(1,2)))
    return add(*terms)


def generator(observable,n,nu):
    ans=[]
    g={(1,-1):F(1,2),(-1,1):F(1,2)}
    for i in range(n):
        force=add(*(scale(diff(insert(g,(i,j),n),i),-F(1,n)) for j in range(n) if i!=j))
        ans.append(scale(mul(force,diff(observable,i)),-1))
        ans.append(scale(diff(observable,i,2),-nu))
    return add(*ans)


def direct_pair_rhs(phi,n,nu):
    # Independently assemble deleted-label diffusion and force discrepancy.
    lap={k:-nu*(k[0]**2+k[1]**2)*v for k,v in phi.items()}
    ans=[p_observable(lap,n)]
    grad={(a,b):a*c for (a,b),c in phi.items()}
    kforce={(1,-1):-F(1,2),(-1,1):F(1,2)}
    for i in range(n):
        force=add(*(scale(insert(kforce,(i,j),n),F(1,n)) for j in range(n) if i!=j))
        h=add(*(scale(insert(grad,(i,j),n),F(1,n)) for j in range(n) if i!=j),scale(insert(grad,(i,None),n),-1))
        ans.append(scale(mul(force,h),-F(1,n)))
    return add(*ans)



def centered_stat(phi,n):
    order=len(next(iter(phi))) if phi else 0
    terms=[]
    for size in range(order+1):
        for subset in combinations(range(order),size):
            for labels in permutations(range(n),size):
                slots=[None]*order
                for slot,label in zip(subset,labels):slots[slot]=label
                terms.append(scale(insert(phi,slots,n),F((-1)**(order-size),n**size)))
    return add(*terms)


def decomposed_pair_rhs(phi,n,nu):
    linear={k:-c*(nu*(k[0]**2+k[1]**2)+sum(F(a*a,2) for a in k if abs(a)==1)) for k,c in phi.items()}
    internal={}
    cubic={}
    for (a,b),c in phi.items():
        for m in (-1,1):
            key=(a+m,b-m)
            internal[key]=internal.get(key,F(0))+F(m*(a-b),2)*c
            key=(a+m,b,-m)
            cubic[key]=cubic.get(key,F(0))+F(m*a,2)*c
    out=[p_observable(linear,n),scale(p_observable(internal,n),F(1,n)),centered_stat(cubic,n)]
    # Lower linear plus deterministic contribution is
    # (eta-mu)(integral B Phi(x,y)mu(dy))/N + mu^2(B Phi)/(2N).
    for i in range(n):out.append(scale(insert(internal,(i,None),n),F(1,n*n)))
    out.append(scale(insert(internal,(None,None),n),-F(1,2*n)))
    return add(*out)

def main():
    kernels={
      'constant':{(0,0):F(1)},
      'sum_mode':{(1,1):F(1,2),(-1,-1):F(1,2)},
      'difference_mode':{(1,-1):F(1,2),(-1,1):F(1,2)},
      'one_body_sum':{(1,0):F(1,2),(-1,0):F(1,2),(0,1):F(1,2),(0,-1):F(1,2)},
      'mixed_symmetric':{(2,-1):F(1,4),(-2,1):F(1,4),(-1,2):F(1,4),(1,-2):F(1,4)},
    }
    checks=[]
    for n,nu,(name,phi) in product((2,3,4),(F(0),F(1,3),F(2)),kernels.items()):
        p=p_observable(phi,n)
        error=add(generator(p,n,nu),scale(direct_pair_rhs(phi,n,nu),-1))
        assert not error,(n,nu,name,error)
        decomposed=add(generator(p,n,nu),scale(decomposed_pair_rhs(phi,n,nu),-1))
        assert not decomposed,('decomposition',n,nu,name,decomposed)
        checks.append({'N':n,'nu':str(nu),'kernel':name,'residual_terms':0})
    # Diagonal trace diagnostic: Phi=cos(theta_x-theta_y), K=0.
    # Full-product statistic has an extra +nu/N trace. Deleted-label P
    # cancels that term exactly through differentiation of its diagonal.
    print(json.dumps({'status':'PASS','exact_rational_checks':2*len(checks),'raw_checks':len(checks),'decomposed_checks':len(checks),'scope':'smooth uniform 1D finite Fourier pair; generator divided by (2pi)^2','checks':checks},indent=2))


if __name__=='__main__':main()
