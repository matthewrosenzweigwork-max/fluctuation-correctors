#!/usr/bin/env python3
"""Fresh, deterministic, read-only exact diagnostics for AUD067.

All coefficients are Fractions. Laurent characters use the first coordinate
of T4. Formal derivative d e_k=k e_k is physical derivative/(2*pi*i).
The force is -d g, so every generator/source drift identity is divided by
(2*pi*i)^2. Diagnostics do not approximate a singular stochastic process.
"""
from fractions import Fraction as F
from itertools import permutations, combinations, product
from collections import Counter
import json

counts=Counter()
mutations={}

def clean(p): return {k:F(v) for k,v in p.items() if v}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return clean(out)
def scale(p,c): return clean({k:v*F(c) for k,v in p.items()})
def mul(p,q):
    out={}
    for k,v in p.items():
        for l,w in q.items():
            a=tuple(x+y for x,y in zip(k,l))
            out[a]=out.get(a,F(0))+v*w
    return clean(out)
def const(n,c): return {} if not c else {(0,)*n:F(c)}
def der(p,i): return clean({k:v*k[i] for k,v in p.items()})
def embed(p,mapping,n):
    out={}
    for k,v in p.items():
        a=[0]*n
        for i,j in enumerate(mapping): a[j]+=k[i]
        a=tuple(a); out[a]=out.get(a,F(0))+v
    return clean(out)
def haar(p,keep):
    out={}
    keep=tuple(keep)
    for k,v in p.items():
        if any(k[i] for i in range(len(k)) if i not in keep): continue
        a=tuple(k[i] for i in keep); out[a]=out.get(a,F(0))+v
    return clean(out)
def mean(p): return p.get((0,)*len(next(iter(p))),F(0)) if p else F(0)
def square_mean(p): return mean(mul(p,p))
def eq(p,q,label):
    assert clean(p)==clean(q), (label,add(p,scale(q,-1)))
    counts[label]+=1
def yes(b,label):
    assert b,label
    counts[label]+=1
def witness(name,good,bad,case):
    diff=add(good,scale(bad,-1))
    if diff and name not in mutations:
        k=sorted(diff)[0]
        mutations[name]={'case':case,'nonzero_frequency':list(k),'difference':str(diff[k])}

def row(p): return haar(p,(0,))
def sym(p,n): return scale(add(*(embed(p,perm,n) for perm in permutations(range(n)))),F(1,1 if n<2 else 2 if n==2 else 6))
def P(phi,N):
    q=row(phi); r=mean(phi)
    pairs=scale(add(*(embed(phi,(i,j),N) for i in range(N) for j in range(N) if i!=j)),F(1,2*N*N))
    rows=scale(add(*(embed(q,(i,),N) for i in range(N))),F(-1,N))
    return add(pairs,rows,const(N,r/2))
def D2(phi,N): return scale(add(*(embed(phi,(i,j),N) for i in range(N) for j in range(N) if i!=j)),F(1,N*N))
def U(phi,k,N):
    terms=[]
    for size in range(k+1):
        for slots in combinations(range(k),size):
            contracted=haar(phi,slots)
            for labels in permutations(range(N),size):
                terms.append(scale(embed(contracted,labels,N),F((-1)**(k-size),N**size)))
    return add(*terms)
def rho(a,N): return add(scale(add(*(embed(a,(i,),N) for i in range(N))),F(1,N)),const(N,-mean(a)))
def force_from_g(g): return {(m,-m):-m*v for (m,),v in g.items() if m}
def B(phi,K): return mul(K,add(der(phi,0),scale(der(phi,1),-1)))
def responses(phi,K):
    rx=haar(mul(embed(K,(2,0),3),embed(der(phi,0),(2,1),3)),(0,1))
    ry=haar(mul(embed(K,(2,1),3),embed(der(phi,1),(0,2),3)),(0,1))
    return rx,ry

def C(phi,K):
    base=mul(embed(K,(0,2),3),embed(der(phi,0),(0,1),3))
    return sym(base,3)
def lower(phi,K,N):
    bp=B(phi,K); b=row(bp)
    return add(scale(rho(b,N),F(1,N)),const(N,mean(bp)/F(2*N)))
def generator(p,K,N,nu):
    diffusion=scale(add(*(der(der(p,i),i) for i in range(N))),nu)
    drift={}
    for i in range(N):
        bi=scale(add(*(embed(K,(i,j),N) for j in range(N) if j!=i)),F(1,N))
        drift=add(drift,mul(bi,der(p,i)))
    return add(diffusion,drift)

a={(1,):F(1,2),(-1,):F(1,2)}
b={(2,):F(1,3),(-2,):F(1,3)}
phi_cases={
    'constant':const(2,F(5,7)),
    'additive':add(embed(a,(0,),2),embed(a,(1,),2)),
    'relative':{(1,-1):F(1,2),(-1,1):F(1,2)},
    'product':mul(embed(a,(0,),2),embed(a,(1,),2)),
    'mixed':sym(mul(embed(a,(0,),2),embed(b,(1,),2)),2),
    'with_mean_and_rows':add(const(2,F(2,5)),embed(a,(0,),2),embed(a,(1,),2),sym(mul(embed(a,(0,),2),embed(b,(1,),2)),2))
}
g_cases={'zero':{},'two_mode':{(1,):F(1),(-1,):F(1),(2,):F(1,4),(-2,):F(1,4)}}
f=add(a,b)
for N,gn,pn in product((2,3,4),g_cases,phi_cases):
    K=force_from_g(g_cases[gn]); phi=phi_cases[pn]; case=f'N={N};g={gn};phi={pn}'
    p=P(phi,N); rx,ry=responses(phi,K); resp=add(rx,ry)
    cc=C(phi,K); u=U(cc,3,N); bp=B(phi,K); low=lower(phi,K,N)
    eq(scale(U(phi,2,N),F(1,2)),p,'literal_subset_U2')
    force=generator(p,K,N,F(0))
    rhs=add(u,P(resp,N),scale(D2(bp,N),F(1,2*N)))
    eq(force,rhs,'direct_force_and_backgrounds')
    eq(add(scale(D2(bp,N),F(1,2*N)),scale(P(bp,N),F(-1,N))),low,'two_lower_coefficients')
    witness('omitted_scalar',low,scale(rho(row(bp),N),F(1,N)),case)
    witness('halved_lower_coefficient',low,add(scale(rho(row(bp),N),F(1,2*N)),const(N,mean(bp)/F(2*N))),case)
    witness('omitted_response_slot',force,add(u,P(rx,N),scale(D2(bp,N),F(1,2*N))),case)
    if N==2: witness('dropped_N2_cubic',force,add(P(resp,N),scale(D2(bp,N),F(1,2*N))),case)
    j=mul(K,add(embed(der(f,0),(0,),2),scale(embed(der(f,0),(1,),2),-1)))
    for nu in (F(0),F(2,7)):
        time_derivative=scale(add(j,scale(add(der(der(phi,0),0),der(der(phi,1),1)),nu),scale(bp,F(1,N)),resp),-1)
        eq(add(P(time_derivative,N),generator(p,K,N,nu)),add(scale(P(j,N),-1),u,low),'full_instantaneous_inverse_identity')
        carré=add(generator(mul(p,p),K,N,nu),scale(mul(p,generator(p,K,N,nu)),-2))
        eq(carré,scale(add(*(mul(der(p,i),der(p,i)) for i in range(N))),2*nu),'physical_bracket_coefficient')
    # Fresh iid second-moment calculation, with all nondegenerate pieces.
    r=mean(phi); q0=add(row(phi),const(1,-r))
    canonical=add(phi,scale(embed(q0,(0,),2),-1),scale(embed(q0,(1,),2),-1),const(2,-r))
    predicted=F(N-1,2*N**3)*square_mean(canonical)+F(1,N**3)*square_mean(q0)+r*r/F(4*N*N)
    yes(square_mean(p)==predicted,'iid_exact_second_moment')
    yes(N*predicted<=F(N-1,2*N*N)*square_mean(phi),'iid_endpoint_inequality')
    # Differentiate the literal deleted statistic, preserving the smooth self label.
    G=der(phi,0); A=row(G)
    for i in range(N):
        vi=add(scale(add(*(embed(G,(i,j),N) for j in range(N))),F(1,N)),scale(embed(A,(i,),N),-1))
        corrected=scale(add(vi,scale(embed(G,(i,i),N),F(-1,N))),F(1,N))
        eq(der(p,i),corrected,'smoothed_gradient_self_subtraction')
        witness('omitted_smooth_self_label',der(p,i),scale(vi,F(1,N)),case)
    # The formal factorial pair replacement changes the observable already at N=2.
    factorial_pair=add(scale(D2(phi,N),F(N,2*(N-1))),scale(add(*(embed(row(phi),(i,),N) for i in range(N))),F(-1,N)),const(N,mean(phi)/2))
    witness('falling_factorial_denominator',p,factorial_pair,case)

# Exact singular Coulomb flux tests: only finitely many Fourier coefficients
# of the true singular K pair against these smooth finite-mode derivatives.
g_coulomb={(m,):F(1,m*m) for m in range(-8,9) if m}
K=force_from_g(g_coulomb)
for name,phi in phi_cases.items():
    bbar=row(B(phi,K)); dbar=row(mul(K,add(der(phi,0),der(phi,1))))
    q=row(phi); tau=embed(phi,(0,0),1)
    actual=scale(bbar,-1) # physical b divided by c=4*pi^2
    expected=add(scale(dbar,-1),scale(add(q,scale(tau,-1)),2))
    eq(actual,expected,'exact_Coulomb_flux_and_compensation')
    witness('omitted_periodic_compensation',actual,add(scale(dbar,-1),scale(tau,-2)),name)
    witness('halved_trace_flux',actual,add(scale(dbar,-1),scale(q,2),scale(tau,-1)),name)
    witness('omitted_common_translation_term',actual,scale(add(q,scale(tau,-1)),2),name)

# Exact positive Fourier energy/self subtraction for a smooth diagnostic.
for N in range(2,8):
    g=g_cases['two_mode']; gr={(m,-m):v for (m,),v in g.items()}
    raw=scale(add(*(embed(gr,(i,j),N) for i in range(N) for j in range(i+1,N))),F(1,N*N))
    full=scale(add(*(embed(gr,(i,j),N) for i in range(N) for j in range(N))),F(1,2*N*N))
    selfterm=const(N,sum(g.values())/F(2*N))
    eq(raw,add(full,scale(selfterm,-1)),'energy_self_diagonal')
    witness('omitted_energy_self_diagonal',raw,full,f'N={N}')

# Solvable local zero-noise d=4,s=2 repulsive pair profile.
# r^4(t)=r^4(0)+16t/N; F=N/4*(sqrt(r^4+16tau/N)-r^2).
for N,r,u in product((2,3,7,19),(F(1,2),F(1),F(3,2)),(F(3),F(5),F(9))):
    if u<=r*r: continue
    tau=F(N,16)*(u*u-r**4)
    potential=F(N,4)*(u-r*r)
    dtau=F(2)/u
    dr=F(N,2)*(r**3/u-r)
    drift=F(4,N)/r**3
    yes(dtau-drift*dr==F(2)/(r*r),'solvable_radial_transport_identity')
    lap=F(N,2)*((r*r/u)*(6-2*r**4/(u*u))-4)
    yes(lap<=0,'Coulomb_radial_diffusion_sign')
    yes(potential>=0 and potential<=2*tau/(r*r),'solvable_profile_bounds')
    # Squared comparison to its averaged collision value sqrt(N*tau).
    yes(potential*potential<=N*tau,'solvable_sqrtN_trace_scale')
    witness('halved_relative_drift',const(0,dtau-drift*dr),const(0,dtau-drift*dr/2),f'N={N};r={r};u={u}')

# All claimed critical powers are exact rational identities.
d=4; s=2; q=F(1,2); gamma=F(1,40); rstar=F(5*d-s+2,2)
first=-F(1,2)-q+gamma*rstar
second=-F(1,2)-2+gamma*(2*d+1)
yes(rstar==10 and first==-F(3,4) and first/2==-F(3,8),'critical_smoothed_martingale_rate')
yes(second<first,'smooth_self_remainder_smaller')
yes(-q/2==-F(1,4),'absolute_lower_drift_power')
# A signed mean alone has no control of absolute size.
yes((F(1)+F(-1))/2==0 and (abs(F(1))+abs(F(-1)))/2==1,'signed_mean_is_not_absolute_control')

required={'omitted_scalar','halved_lower_coefficient','omitted_response_slot','dropped_N2_cubic','omitted_smooth_self_label','falling_factorial_denominator','omitted_periodic_compensation','halved_trace_flux','omitted_common_translation_term','omitted_energy_self_diagonal','halved_relative_drift'}
yes(set(mutations)==required,'all_mutations_have_nonzero_witnesses')
result={'status':'PASS','assertions':sum(counts.values()),'categories':dict(sorted(counts.items())),'mutation_witnesses':mutations,'arithmetic':'exact fractions and rational Laurent polynomials; no random seed or tolerance','scope':'supporting identities and solvable tests only; no stochastic asymptotic certification','critical_exponents':{'bracket_main':str(first),'bracket_self':str(second),'martingale_L1':str(first/2),'lower_drift':str(-q/2)}}
print(json.dumps(result,indent=2,sort_keys=True))
