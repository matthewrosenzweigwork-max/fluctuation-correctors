#!/usr/bin/env python3
"""Fresh exact algebra checks for TASK-077; standard library, no imported checker.
D e_k = i k e_k. Physical first derivatives restore 2*pi and each generator
or source expression restores (2*pi)^2. Tests use one coordinate embedded in
the permitted d-dimensional torus. They do not simulate singular particles.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

class Q:
    __slots__ = ('r','i')
    def __init__(self, r=0, i=0): self.r,self.i=F(r),F(i)
    def __add__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return Q(-self.r,-self.i)
    def __sub__(self,o): return self+-asq(o)
    def __mul__(self,o):
        o=asq(o); return Q(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o): return Q(self.r/F(o),self.i/F(o))
    def __bool__(self): return bool(self.r or self.i)
    def __eq__(self,o):
        o=asq(o); return self.r==o.r and self.i==o.i
    def __repr__(self): return f'Q({self.r},{self.i})'

def asq(o): return o if isinstance(o,Q) else Q(o)
def clean(p): return {k:asq(v) for k,v in p.items() if v}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,Q())+v
    return clean(out)
def scale(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
    out={}
    for k,a in p.items():
        for l,b in q.items():
            key=tuple(x+y for x,y in zip(k,l))
            out[key]=out.get(key,Q())+a*b
    return clean(out)
def der(p,j): return clean({k:v*Q(0,k[j]) for k,v in p.items()})
def lap(p): return clean({k:v*(-sum(x*x for x in k)) for k,v in p.items()})
def embed(p, slots, dim):
    out={}
    for k,v in p.items():
        kk=[0]*dim
        for j,slot in enumerate(slots): kk[slot]+=k[j]
        kk=tuple(kk);out[kk]=out.get(kk,Q())+v
    return clean(out)
def integrate(p, keep):
    out={}
    for k,v in p.items():
        if any(k[j] for j in range(len(k)) if j not in keep): continue
        kk=tuple(k[j] for j in keep);out[kk]=out.get(kk,Q())+v
    return clean(out)
def const(c,dim): return clean({(0,)*dim:asq(c)})
def mean(p): return p.get((0,)*len(next(iter(p))),Q()) if p else Q()
def norm2_real(p): return mean(mul(p,p))
def even_modes(modes):
    out={}
    for k,v in modes.items():
        out[k]=out.get(k,Q())+asq(v)
        nk=tuple(-x for x in k);out[nk]=out.get(nk,Q())+asq(v)
    return clean(out)
def swap(p): return embed(p,[1,0],2)
def sym(p): return scale(add(p,swap(p)),F(1,2))
def U(p,arity,N):
    out={}
    for r in range(arity+1):
        for subset in combinations(range(arity),r):
            part=integrate(p,subset)
            for labels in permutations(range(N),r):
                out=add(out,scale(embed(part,labels,N),F((-1)**(arity-r),N**r)))
    return out

def P(phi,N): return scale(U(phi,2,N),F(1,2))
def D2(phi,N): return scale(add(*(embed(phi,(i,j),N) for i in range(N) for j in range(N) if i!=j)),F(1,N*N))
def rho(v,N): return U(v,1,N)
def force(g): return scale(der(g,0),-1)
def relative(k,dim=2,a=0,b=1):
    return {tuple((m[0] if j==a else -m[0] if j==b else 0) for j in range(dim)):v for m,v in k.items()}
def response_direct(phi,k,slot):
    if slot==0:
        p3=embed(der(phi,0),(2,1),3)
        ans=integrate(mul(relative(k,3,2,0),p3),(0,1))
    else:
        p3=embed(der(phi,1),(0,2),3)
        ans=integrate(mul(relative(k,3,2,1),p3),(0,1))
    return ans

def objects(phi,g):
    k=force(g);p=der(phi,0)
    B=mul(relative(k),add(p,scale(der(phi,1),-1)))
    R=add(response_direct(phi,k,0),response_direct(phi,k,1))
    raw=mul(relative(k,3,0,2),embed(p,(0,1),3))
    C=scale(add(*(embed(raw,pi,3) for pi in permutations(range(3)))),F(1,6))
    return B,R,C

def generator(v,g,nu,N):
    k=force(g);out=scale(lap(v),nu)
    for i in range(N):
        bi=scale(add(*(relative(k,N,i,j) for j in range(N) if j!=i)),F(1,N))
        out=add(out,mul(bi,der(v,i)))
    return out

counts={}
def check(name,condition):
    if not condition: raise AssertionError(name)
    counts[name.split(':')[0]]=counts.get(name.split(':')[0],0)+1

potentials=[{},even_modes({(1,):F(1,2)}),even_modes({(1,):F(1,2),(2,):F(1,3),(3,):F(1,7)})]
phis=[const(3,2),even_modes({(1,-1):F(1,2)}),sym(even_modes({(1,0):F(2,3)})),sym(even_modes({(1,2):F(1,3)})),sym(even_modes({(1,-2):F(2,5)}))]
phis.append(add(*phis))
h=even_modes({(1,):F(2,3),(3,):F(1,5)})
for gi,g in enumerate(potentials):
    k=force(g)
    J=mul(relative(k),add(embed(der(h,0),(0,),2),scale(embed(der(h,0),(1,),2),-1)))
    expected={}
    for a,b in product(range(-7,8),repeat=2):
        n=a+b;coef=-((g.get((a,),Q())*a+g.get((b,),Q())*b)*n)*h.get((n,),Q())
        if coef:expected[(a,b)]=coef
    check('source_coefficients',J==expected)
    check('smooth_source_diagonal',not embed(J,(0,0),1))
    for pi,phi in enumerate(phis):
        B,R,C=objects(phi,g)
        multiplier=clean({(a,b):-v*(g.get((a,),Q())*(a*a)+g.get((b,),Q())*(b*b)) for (a,b),v in phi.items()})
        check('both_response_slots',R==multiplier)
        a=integrate(der(phi,0),(0,));Aa=mul(relative(k),add(embed(a,(0,),2),scale(embed(a,(1,),2),-1)))
        v=integrate(response_direct(phi,k,0),(0,))
        check('cubic_one_background',integrate(C,(0,1))==scale(add(Aa,R),F(1,6)))
        check('cubic_two_background',integrate(C,(0,))==scale(v,F(1,3)))
        check('cubic_scalar',not integrate(C,()))
        for N in (2,3,4,5):
            obs=P(phi,N);row=integrate(B,(0,));scalar=mean(B)
            theta=mean(phi);q=integrate(phi,(0,));a0=add(q,const(-theta,1))
            deg=add(phi,scale(embed(q,(0,),2),-1),scale(embed(q,(1,),2),-1),const(theta,2))
            endpoint=theta*theta/F(4*N*N)+norm2_real(a0)/F(N**3)+norm2_real(deg)*F(N-1,2*N**3)
            check('iid_endpoint_exact',norm2_real(obs)==endpoint)
            check('iid_endpoint_bound',(norm2_real(phi)/F(2*N*N)-endpoint).r>=0)
            for i in range(N):
                manual=add(scale(add(*(embed(der(phi,0),(i,j),N) for j in range(N) if j!=i)),F(1,N*N)),scale(embed(a,(i,),N),F(-1,N)))
                check('particle_gradient',der(obs,i)==manual)
            for nu in (F(0),F(1,3),F(2)):
                time_phi=scale(add(J,scale(lap(phi),nu),scale(B,F(1,N)),R),-1)
                direct=add(P(time_phi,N),generator(obs,g,nu,N))
                hierarchy=add(scale(P(J,N),-1),U(C,3,N),scale(rho(row,N),F(1,N)),const(scalar/F(2*N),N))
                check('full_drift_identity',direct==hierarchy)
                # Four distinct pieces of the bracket, assembled literally.
                pp=der(phi,0)
                triple=add(*(mul(embed(pp,(i,j),N),embed(pp,(i,l),N)) for i,j,l in permutations(range(N),3)))
                pair=add(*(mul(embed(pp,(i,j),N),embed(pp,(i,j),N)) for i,j in permutations(range(N),2)))
                mixed=add(*(mul(embed(pp,(i,j),N),embed(a,(i,),N)) for i,j in permutations(range(N),2)))
                background=add(*(mul(embed(a,(i,),N),embed(a,(i,),N)) for i in range(N)))
                expanded=scale(add(scale(add(triple,pair),F(1,N**4)),scale(mixed,F(-2,N**3)),scale(background,F(1,N*N))),2*nu)
                bracket=scale(add(*(mul(der(obs,i),der(obs,i)) for i in range(N))),2*nu)
                check('four_bracket_contractions',expanded==bracket)
                product_generator=add(generator(mul(obs,obs),g,nu,N),scale(mul(obs,generator(obs,g,nu,N)),-2))
                check('generator_product_bracket',product_generator==bracket)
            if N==2 and C:
                # Direct literal U3 need not vanish with only two actual labels.
                if U(C,3,N):check('N2_nonzero_background_witness',True)
for N in range(2,10):
    for g in potentials:
        rel=relative(g);full=scale(add(*(embed(rel,(i,j),N) for i in range(N) for j in range(N))),F(1,N*N))
        g0=sum(g.values(),Q())
        check('energy_self_diagonal',D2(rel,N)==add(full,const(-g0/F(N),N)))
for d in range(4,15):
    for j in range(1,40):
        s=F(j,20);alpha=(d-s)/2;p=s+2;theta=1-s/d;aa=s/p
        eps=min(s,d-s-2)/2;q=1+eps;zeta=(s-eps)/p
        check('range_alpha',alpha>1)
        check('range_source_decay',F(1,2)-theta<0)
        check('range_critical_noise',aa-theta<0)
        check('range_bounded_chi',F(2)/p-theta==s*(s+2-d)/(d*p) and F(2)/p-theta<0)
        check('range_lower_weight',1<q< F(d,2) and q<=s+1 and s+1+q<d)
        check('range_lower_decay',zeta-F(1,2)<0)
        check('heat_N_powers',-1+s/d==-theta and -2*alpha/d==-theta)
        check('smooth_test_polynomial',2*alpha+2+s==d+2)
        check('spectral_slack',F(13,256)<F(1,8))
art=Path(__file__).resolve().parent
root=art.parents[2]
inputs=[]
for line in (art/'INPUT_SHA256SUMS.txt').read_text().splitlines():
    digest,rel=line.split('  ',1)
    found=hashlib.sha256((root/rel).read_bytes()).hexdigest()
    check('input_sha256',found==digest)
    inputs.append({'path':rel,'sha256':found})
result={'status':'PASS','evidence':'Exact algebraic and rational-parameter diagnostics; not an analytic proof or independent certification of conditional premises.','assertions':sum(counts.values()),'categories':counts,'arithmetic':'Gaussian rationals; no tolerance and no random seed','normalization':'D e_k=i k e_k; physical first derivatives multiply by 2*pi and generators/sources by (2*pi)^2. One coordinate is embedded in allowed dimensions.','input_count':len(inputs),'inputs':inputs}
(art/'EXACT_DIAGNOSTIC_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='inputs'},indent=2))
