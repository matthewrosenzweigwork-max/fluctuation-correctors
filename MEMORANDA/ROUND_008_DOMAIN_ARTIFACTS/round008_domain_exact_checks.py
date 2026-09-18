#!/usr/bin/env python3
"""Exact finite Fourier, deleted-label, radial and coefficient checks for TASK051.
All Fourier spatial second-order expressions divide out (2*pi)^2 consistently.
Finite Fourier fields live in one coordinate of the admitted d-dimensional torus.
No stochastic simulation or analytic regularity certification is claimed.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib, json, math, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
counts=defaultdict(int)
def check(ok,group,label):
 if not ok: raise AssertionError(group+': '+label)
 counts[group]+=1
def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
 r=defaultdict(F)
 for p in ps:
  for k,v in p.items(): r[k]+=v
 return clean(r)
def scale(p,c): return clean({k:c*v for k,v in p.items()})
def mul(p,q):
 r=defaultdict(F)
 for k,a in p.items():
  for l,b in q.items(): r[tuple(x+y for x,y in zip(k,l))]+=a*b
 return clean(r)
def subset_stat(p,k,N):
 r=defaultdict(F)
 for selected_count in range(k+1):
  for selected in combinations(range(k),selected_count):
   for labels in permutations(range(N),selected_count):
    for freqs,v in p.items():
     if any(freqs[a] for a in range(k) if a not in selected): continue
     out=[0]*N
     for a,i in zip(selected,labels): out[i]+=freqs[a]
     r[tuple(out)]+=F((-1)**(k-selected_count),N**selected_count)*v
 return clean(r)
def pair_stat(p,N): return scale(subset_stat(p,2,N),F(1,2))
def internal(p,g):
 r=defaultdict(F)
 for (a,b),v in p.items():
  for k,c in g.items(): r[(a+k,b-k)]+=k*(a-b)*c*v
 return clean(r)
def response(p,g,slots=(0,1)):
 return clean({ab:-sum(ab[j]**2*g.get(ab[j],F(0)) for j in slots)*v for ab,v in p.items()})
def lap(p): return clean({k:-sum(a*a for a in k)*v for k,v in p.items()})
def upper(p,g):
 raw=defaultdict(F)
 for (a,b),v in p.items():
  for k,c in g.items():
   key=(a+k,b,-k)
   for perm in permutations(range(3)):
    raw[tuple(key[j] for j in perm)]+=F(k*a,6)*c*v
 return clean(raw)
def marginal(p,slot=1):
 r=defaultdict(F)
 for k,v in p.items():
  if k[slot]==0: r[tuple(a for j,a in enumerate(k) if j!=slot)]+=v
 return clean(r)
def mean(p): return p.get(tuple(0 for _ in next(iter(p),())),F(0)) if p else F(0)
def generator(p,N,g,nu):
 out=scale(lap(p),nu)
 r=defaultdict(F)
 for freqs,v in p.items():
  for i in range(N):
   for j in range(N):
    if i==j: continue
    for k,c in g.items():
     key=list(freqs);key[i]+=k;key[j]-=k
     r[tuple(key)]+=F(k*freqs[i],N)*c*v
 return add(out,clean(r))
def grad_coeff(p,i): return clean({k:k[i]*v for k,v in p.items()})
def explicit_grad(p,N,i):
 r=defaultdict(F)
 for (a,b),v in p.items():
  for j in range(N):
   if j==i: continue
   key=[0]*N;key[i]+=a;key[j]+=b
   r[tuple(key)]+=F(a,N*N)*v
  if b==0:
   key=[0]*N;key[i]=a;r[tuple(key)]-=F(a,N)*v
 return clean(r)
manifest=OUT/'ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt'
for line in manifest.read_text().splitlines():
 expected,rel=line.split('  ',1)
 check(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==expected,'input_hash',rel)
kernels={
 'constant':{(0,0):F(3,7)},
 'relative':{(1,-1):F(1,2),(-1,1):F(1,2)},
 'separable':{(a,b):F(1,4) for a,b in product((-1,1),repeat=2)},
 'additive':{(1,0):F(1,2),(-1,0):F(1,2),(0,1):F(1,2),(0,-1):F(1,2)},
 'mixed':{(2,-1):F(1,4),(-2,1):F(1,4),(-1,2):F(1,4),(1,-2):F(1,4)}}
forces={'zero':{},'two_modes':{-2:F(1,7),-1:F(1,2),1:F(1,2),2:F(1,7)},
        'coulomb_cutoff':{k:F(1,k*k) for k in (-3,-2,-1,1,2,3)}}
fadd=kernels['additive']
mutations={'one_response':False,'no_U3_at_N2':False,'wrong_lower':False,'missing_scalar':False}
for N in (2,3):
 for nu in (F(0),F(1,3)):
  for gn,g in forces.items():
   J=internal(fadd,g)
   for name,phi in kernels.items():
    P=pair_stat(phi,N);B=internal(phi,g);R=response(phi,g);C=upper(phi,g)
    lower=scale(subset_stat(marginal(B),1,N),F(1,N))
    scalar={tuple([0]*N):mean(B)/F(2*N)}
    # Set the local time derivative to the exact corrector PDE at this instant.
    dt=scale(add(J,scale(lap(phi),nu),scale(B,F(1,N)),R),F(-1))
    left=add(generator(P,N,g,nu),pair_stat(dt,N))
    right=add(scale(pair_stat(J,N),F(-1)),subset_stat(C,3,N),lower,scalar)
    label=f'N={N},nu={nu},g={gn},Phi={name}'
    check(left==right,'full_corrector_identity',label)
    raw=add(pair_stat(add(dt,scale(lap(phi),nu),R),N),subset_stat(C,3,N))
    D2=add(scale(pair_stat(B,N),F(2)),scale(subset_stat(marginal(B),1,N),F(2)),{tuple([0]*N):mean(B)})
    check(left==add(raw,scale(D2,F(1,2*N))),'R1_raw_pair_identity',label)
    for i in range(N): check(grad_coeff(P,i)==explicit_grad(phi,N,i),'deleted_gradient',label)
    bracket=add(*[scale(mul(grad_coeff(P,i),grad_coeff(P,i)),F(-2)*nu) for i in range(N)])
    gamma=add(generator(mul(P,P),N,g,nu),scale(mul(P,generator(P,N,g,nu)),F(-2)))
    check(gamma==bracket,'quadratic_variation_2nu',label)
    if nu==0: check(not bracket,'zero_noise',label)
    if name=='constant': check(not B and not R and not C,'constant_pair_test',label)
    if N==2 and subset_stat(C,3,N): mutations['no_U3_at_N2']=True
    if lower: mutations['wrong_lower']=True
    if mean(B): mutations['missing_scalar']=True
    if response(phi,g,(0,))!=R: mutations['one_response']=True
    # Independently check the contracted cubic kernels from six slots.
    cp=marginal(C,2)
    a=grad_coeff(marginal(phi),0)
    diff=defaultdict(F)
    for (n,),v in a.items():
     for k,c in g.items():
      diff[(k+n,-k)]+=k*c*v
      diff[(k,n-k)]-=k*c*v
    # A_a=K.(a(x)-a(y)); grad_coeff omitted i, so interaction sign is +.
    check(scale(cp,F(6))==add(clean(diff),R),'partial_cubic_contraction',label)
    ra=clean({(k,):-k*k*g.get(k,F(0))*v for (k,),v in marginal(phi).items()})
    check(scale(marginal(cp),F(3))==ra,'double_cubic_contraction',label)
    check(mean(C)==0,'triple_background_mean',label)
for name,v in mutations.items(): check(v,'mutation_sensitivity',name)
for g in forces.values():
 const={(0,0):F(1)}
 check(not internal(const,g),'constant_terminal_source','constant h gives J=0')
# Exact local radial coefficients: no transverse eigenvalue is discarded.
for d in range(3,9):
 for s in range(1,d-1):
  for N in (2,3,7):
   a=F(2*s,N);p=s+2
   check(a*(1-p)==-F(2*s*(s+1),N),'radial_jacobian','radial contraction')
   check(a>0 and abs(a*(1-p))>a,'radial_jacobian','norm differs from top eigenvalue')
   for m in (0,1,2,4):
    alpha=F(max(d,m+1)+2)
    A=a*(alpha-m)
    check(A>0,'weighted_barrier','alpha greater than moment')
    diffusion=2*alpha*(alpha+2-d)
    check(diffusion>0,'weighted_barrier','positive diffusion must be absorbed')
    # Choose D=A*p/4 so the exact Young maximizer is u=1.
    D=A*p/4;young=A*s/4
    for u in (F(0),F(1,4),F(1,2),F(1),F(2),F(4)):
     check(D*u*u-A*F(1,2)*u**p<=young,'young_absorption','global exact maximum')
    for r in (F(1,4),F(1,2),F(1),F(2)):
     principal=-a*alpha*r**(-p)+m*a*r**(-p)
     check(principal==-A*r**(-p),'weighted_barrier','exact FK principal coefficient')
  for iq in range(1,9):
   q1=F(1)+F(iq,10)
   if q1>=F(d,2): continue
   q2=(q1+1+d)/2
   check(q2>2 and q2>q1+1 and q2<d,'weight_ranges','Hessian interval')
   check(q1<d-1 and 2*q1<d,'weak_derivatives','tube and H1 powers')
   check(s+3+q1<q2+s+2,'second_variation_source','occupation domination')
   check(s+1<d and q1<d,'triple_collision','independent variables each integrable')
# Frozen normalization and both Coulomb response slots.
for d in range(3,10):
 check(F(2*(d-2),1)/(F(d,2)-1)==4,'coulomb_constant','4*pi^(d/2)/Gamma((d-2)/2)')
for name,phi in kernels.items():
 g=forces['coulomb_cutoff']
 for (a,b),v in phi.items():
  check(response({(a,b):v},g)==clean({(a,b):-(int(a!=0)+int(b!=0))*v}),
        'coulomb_response','two compensated slots on supported modes')
result={'status':'PASS','task':'TASK051','classification':'construction self-check, not independent audit',
 'python':sys.version.split()[0],'arithmetic':'exact rational integers and SHA-256; no tolerance or random seed',
 'total_assertions':sum(counts.values()),'counts':dict(sorted(counts.items())),
 'limitations':'Finite Fourier/radial algebra tests do not certify the new analytic lemmas or any asymptotic statement.'}
(OUT/'ROUND_008_DOMAIN_EXACT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
