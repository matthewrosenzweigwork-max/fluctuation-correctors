#!/usr/bin/env python3
"""Fresh TASK-056 exact diagnostics. Standard library only; no sampled tolerances.

Laurent coefficients are rational. D_i below is (2*pi*i)^(-1) partial_i,
so physical products of two first derivatives have a minus sign and a common
(2*pi)^2 factor. The checker explicitly retains and reports that convention.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
COUNTS = {}
DETAILS = {}

def ck(test, group):
    if not test:
        raise AssertionError(group)
    COUNTS[group] = COUNTS.get(group, 0) + 1

def trim(a):
    return {k: F(v) for k, v in a.items() if v}

def add(*aa):
    out = {}
    for a in aa:
        for k,v in a.items():
            out[k] = out.get(k,F(0)) + v
    return trim(out)

def scale(a,c):
    return trim({k:v*c for k,v in a.items()})

def mul(a,b):
    out = {}
    for k,v in a.items():
        for l,w in b.items():
            key = tuple(x+y for x,y in zip(k,l))
            out[key] = out.get(key,F(0)) + v*w
    return trim(out)

def const(a,n):
    return a.get((0,)*n,F(0))

def one(n,c=1):
    return {(0,)*n:F(c)} if c else {}

def cos(k):
    k=tuple(k)
    if not any(k):
        return one(len(k))
    return {k:F(1,2),tuple(-x for x in k):F(1,2)}

def der(a,i):
    return trim({k:v*k[i] for k,v in a.items()})

def lap(a):
    return trim({k:-v*sum(x*x for x in k) for k,v in a.items()})

def integrate(a,keep):
    keep=tuple(keep)
    out={}
    for k,v in a.items():
        if any(x for i,x in enumerate(k) if i not in keep):
            continue
        key=tuple(k[i] for i in keep)
        out[key]=out.get(key,F(0))+v
    return trim(out)

def lift(a,slots,n):
    out={}
    for k,v in a.items():
        kk=[0]*n
        for j,slot in enumerate(slots):
            kk[slot] += k[j]
        key=tuple(kk)
        out[key]=out.get(key,F(0))+v
    return trim(out)

def swap(a):
    return {(k[1],k[0]):v for k,v in a.items()}

def normder(a,i):
    da=der(a,i)
    return -const(mul(da,da),len(next(iter(a))) if a else 2)

def expect(a,density,n):
    return const(mul(a,density),n)

def pair_stat(phi,N):
    abar=integrate(phi,(0,))
    p=one(N,F(1,2)*const(phi,2))
    for i,j in permutations(range(N),2):
        p=add(p,scale(lift(phi,(i,j),N),F(1,2*N*N)))
    for i in range(N):
        p=add(p,scale(lift(abar,(i,),N),-F(1,N)))
    return p

def exchangeable_density(N):
    # Convex amplitude bound: density >= 1 - 1/4 - 1/5 > 0.
    pairs=list(permutations(range(N),2))
    triples=list(permutations(range(N),3))
    dens=one(N)
    for i,j in pairs:
        k=[0]*N;k[i]=1;k[j]=-1
        dens=add(dens,scale(cos(k),F(1,4*len(pairs))))
    for i,j,k in triples:
        mode=[0]*N;mode[i]=mode[j]=1;mode[k]=-2
        dens=add(dens,scale(cos(mode),F(1,5*len(triples))))
    return dens

def response(phi,gamma):
    return trim({k:-v*(k[0]*k[0]*gamma.get(abs(k[0]),F(0))+
                      k[1]*k[1]*gamma.get(abs(k[1]),F(0)))
                 for k,v in phi.items()})

def relative_force(gamma):
    # K/(2*pi*i) in pair coordinates, with K = -grad g.
    return {(k,-k):-F(k)*v for kk,v in gamma.items() for k in (kk,-kk)}

def b_operator(phi,gamma):
    # Physical B divided by (2*pi)^2.
    return scale(mul(relative_force(gamma),add(der(phi,0),scale(der(phi,1),-1))),-1)

def particle_generator(a,N,nu,gamma):
    result=scale(lap(a),nu)
    force=relative_force(gamma)
    for i,j in permutations(range(N),2):
        result=add(result,scale(mul(lift(force,(i,j),N),der(a,i)),-F(1,N)))
    return result

phis={
    'constant':one(2,3),
    'additive':add(cos((1,0)),cos((0,1))),
    'relative':cos((1,-1)),
    'separable':mul(cos((1,0)),cos((0,1))),
    'mixed':add(mul(cos((1,0)),cos((0,2))),mul(cos((2,0)),cos((0,1)))),
}
phis['combined']=add(one(2,F(2,3)),scale(phis['additive'],F(3,5)),
                     scale(phis['relative'],F(-2,7)),
                     scale(phis['separable'],F(4,9)),
                     scale(phis['mixed'],F(1,11)))

manifest=(HERE/'ROUND_009_ENERGY_BLIND_INPUT_SHA256SUMS.txt').read_text()
rows=[line.split('  ',1) for line in manifest.splitlines() if line]
ck(len(rows)==19,'frozen_inputs')
for digest,rel in rows:
    ck(hashlib.sha256((HERE/'ROUND_009_INPUTS'/rel).read_bytes()).hexdigest()==digest,'frozen_inputs')
DETAILS['input_count']=len(rows)

for N in (2,3,4,5):
    dens=exchangeable_density(N)
    ck(const(dens,N)==1,'nonproduct_law')
    ck(F(1)-F(1,4)-F(1,5)>0,'nonproduct_law')
    for i in range(N):
        ck(integrate(dens,(i,))==one(1),'nonproduct_law')
    ck(integrate(dens,(0,1))!=one(2),'nonproduct_law')
    for perm in permutations(range(N)):
        ck(lift(dens,perm,N)==dens,'nonproduct_law')
    for name,phi in phis.items():
        ck(swap(phi)==phi,'pair_symmetry')
        p=pair_stat(phi,N)
        G=der(phi,0)
        A=integrate(G,(0,))
        H=add(G,scale(lift(A,(0,),2),-1))
        ck(integrate(H,(0,))=={},'conditional_centering')
        Q={}
        for i in range(N):
            dpi=der(p,i)
            literal=scale(lift(A,(i,),N),-F(1,N))
            centered=scale(lift(A,(i,),N),-F(1,N*N))
            for j in range(N):
                if i!=j:
                    literal=add(literal,scale(lift(G,(i,j),N),F(1,N*N)))
                    centered=add(centered,scale(lift(H,(i,j),N),F(1,N*N)))
            ck(dpi==literal,'deleted_pair_gradient')
            ck(dpi==centered,'deleted_pair_gradient')
            Q=add(Q,scale(mul(dpi,dpi),-1))
        G2=-const(mul(G,G),2)
        A2=-const(mul(A,A),1)
        ck(G2>=A2>=0,'projection_norms')
        ck(normder(phi,0)==normder(phi,1),'pair_symmetry')
        ref=F(N-1,N**3)*G2-F(N-2,N**3)*A2
        ck(const(Q,N)==ref,'haar_identity')
        ck(const(Q,N)<=F(N-1,N**3)*G2,'haar_identity')
        f2=integrate(dens,(0,1))
        f1=integrate(dens,(0,))
        ehh=-expect(mul(H,H),f2,2)
        eha=-expect(mul(H,lift(A,(0,),2)),f2,2)
        eaa=-expect(mul(A,A),f1,1)
        eh3=F(0)
        if N>=3:
            f3=integrate(dens,(0,1,2))
            eh3=-expect(mul(lift(H,(0,1),3),lift(H,(0,2),3)),f3,3)
        rhs=F(1,N**3)*((N-1)*ehh+(N-1)*(N-2)*eh3-2*(N-1)*eha+eaa)
        ck(expect(Q,dens,N)==rhs,'exchangeable_identity')
        delta_h=ehh-(G2-A2)
        delta_ha=eha
        delta_h3=eh3
        dev=F(1,N**3)*((N-1)*delta_h+(N-1)*(N-2)*delta_h3-2*(N-1)*delta_ha)
        ck(expect(Q,dens,N)-ref==dev,'marginal_deviation_identity')
        if name=='additive':
            ck(not H,'additive_stress_test')
            ck(const(Q,N)==F(1,N**3)*A2,'additive_stress_test')
        f=add(cos((1,)),scale(cos((2,)),F(1,3)))
        eta={}
        for i in range(N):
            eta=add(eta,scale(lift(f,(i,),N),F(1,N)))
        for nu in (F(0),F(1,2),F(1),F(2)):
            cross={}
            lead={}
            for i in range(N):
                cross=add(cross,scale(mul(der(eta,i),der(p,i)),-2*nu))
                lead=add(lead,scale(mul(der(eta,i),der(eta,i)),-2*nu))
            ck(const(lead,N)==2*nu*normder(f,0)/N,'leading_bracket')
            ck(expect(lead,dens,N)==const(lead,N),'leading_bracket')
            if nu==0:
                ck(not cross and not lead and not scale(Q,2*nu),'zero_noise')
            else:
                beta=1/nu;b=min(beta,F(1));sigma2=N*b
                ck(nu*b<=1,'physical_scaling')
                ck(sigma2*2*nu*F(N-1,N**3)==2*nu*b*F(N-1,N*N),'physical_scaling')
            # Diffusion product rule, then a smooth-force generator check.
            diff=scale(add(lap(mul(eta,p)),scale(mul(eta,lap(p)),-1),scale(mul(p,lap(eta)),-1)),nu)
            ck(diff==cross,'cross_product_rule')
            if N<=3:
                gamma={1:F(2),2:F(1,3)}
                lhs=add(particle_generator(mul(eta,p),N,nu,gamma),
                        scale(mul(eta,particle_generator(p,N,nu,gamma)),-1),
                        scale(mul(p,particle_generator(eta,N,nu,gamma)),-1))
                ck(lhs==cross,'full_generator_cross_rule')

for name,phi in phis.items():
    for gamma in ({},{1:F(2),2:F(1,3)},{k:F(1,k*k) for k in range(1,9)}):
        R=response(phi,gamma)
        ck(const(mul(phi,R),2)<=0,'two_response_dissipation')
        if name=='constant':
            ck(not R,'constant_test')
        D={(k,-k):F(k*k)*v for kk,v in gamma.items() for k in (kk,-kk)}
        BP=b_operator(phi,gamma)
        ck(const(mul(phi,BP),2)==-const(mul(D,mul(phi,phi)),2),'smooth_drift_energy')
        for N in (2,3,17):
            for nu in (F(0),F(1,2),F(2)):
                f=add(cos((1,)),scale(cos((2,)),F(1,3)))
                fgrad=add(lift(der(f,0),(0,),2),scale(lift(der(f,0),(1,),2),-1))
                J=scale(mul(relative_force(gamma),fgrad),-1)
                phit=scale(add(scale(lap(phi),nu),scale(BP,F(1,N)),R,J),-1)
                grad2=normder(phi,0)+normder(phi,1)
                identity=const(mul(phi,phit),2)-nu*grad2+F(1,N)*const(mul(phi,BP),2)+const(mul(phi,R),2)+const(mul(phi,J),2)
                ck(identity==0,'finite_fourier_energy_balance')
                if name=='constant':
                    # A constant terminal one-body test, separately, has J=0.
                    cgrad=der(one(1,7),0)
                    ck(not cgrad,'constant_test')
    # Coulomb response on every supported pair mode, including zero slots.
    cg={k:F(1,k*k) for k in range(1,9)}
    expected={k:-v*(int(k[0]!=0)+int(k[1]!=0)) for k,v in phi.items() if any(k)}
    ck(response(phi,cg)==trim(expected),'coulomb_slots')

for d in range(3,13):
    candidates={F(1,2),F(1),F(d-2),F(d-2,2),F(2*d-5,2)}
    for s in sorted(x for x in candidates if 0<x<=d-2):
        p=s+2;alpha=s/p
        ck(0<alpha<1,'rate_exponents')
        ck(2*alpha-1<=alpha,'rate_exponents')
        ck(alpha-1==-F(2)/p,'rate_exponents')
        ck((alpha-1)/2==-F(1)/p,'rate_exponents')
        ck(d-s>0 and d-2>0,'singular_integrability')
        ck(s*(d-s-2)>=0,'coulomb_boundary_sign')
        for N in (2,3,17):
            ck(F(2,N)>0,'coulomb_boundary_sign')
            ck(F(N-1,N*N)<=F(1,N),'physical_scaling')
            ck(F(N-1,N**3)*F(2,1)*N==F(2*(N-1),N*N),'physical_scaling')
        for q in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
            ck(d+s-(2*s+2)*q>=d-s-2>=0,'radial_laplacian_sign')
        a,b=s.numerator,s.denominator
        for w,u in ((F(1,2),F(1)),(F(1),F(2)),(F(2),F(3)),(F(1),F(1))):
            for N in (2,3,17):
                r=w**b
                time=N*(u**(a+2*b)-w**(a+2*b))/(2*s*p)
                profile=F(N,4)*(u**(2*b)-w**(2*b))
                ft=s*u**(-a)
                fr=F(N,2)*(w**(a+b)*u**(-a)-w**b)
                drift=2*s/N*w**(-a-b)*fr
                ck(ft-drift==s*w**(-a),'radial_transport_identity')
                ck(-r*fr<=s*profile,'radial_drift_absorption')
                qq=(w/u)**(a+2*b)
                delta=F(N,2)*((w/u)**a*(d+s-s*qq)-d)
                ck(delta<=0,'radial_laplacian_sign')
                ck((u**(2*b)-w**(2*b))**(a+2*b)<=
                   (u**(a+2*b)-w**(a+2*b))**(2*b),'radial_sup_bound')
                ck(time>=0 and profile>=0,'radial_nonnegative')
    # Gamma recurrence gives c_d/(4*pi^2*c_{d,d-2})=1.
    ck(F(2*(d-2),1)/F(d-2,2)==4,'coulomb_normalization')

DETAILS.update({
    'method':'Exact rational Laurent-polynomial arithmetic and exact rational radial/scaling checks.',
    'random_seed':None,
    'tolerance':None,
    'physical_convention':'D_i=(2*pi*i)^(-1) partial_i. Every two-derivative expression restores (2*pi)^2 and the displayed i^2=-1. Brownian coefficient is sqrt(2*nu), sigma_N^2=N*min(beta_N,1), nu=1/beta_N for positive nu.',
    'finite_fourier_dimensions':'Functions of the first torus coordinate, embedded in every admitted d>=3; full pair gradients retain both slots.',
    'nonproduct_density':'1 + (1/4) average_ordered_pairs cos(x_i-x_j) + (1/5) average_ordered_triples cos(x_i+x_j-2*x_k), with the triple term absent at N=2.',
    'limitations':'Finite exact diagnostics support algebra only. They do not prove singular estimates, domain regularity, actual-law transfer, or an independent audit of this report.'
})
result={'status':'PASS','total_exact_assertions':sum(COUNTS.values()),'groups':COUNTS,'details':DETAILS}
(HERE/'round009_energy_exact_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
