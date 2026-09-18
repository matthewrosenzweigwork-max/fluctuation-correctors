#!/usr/bin/env python3
"""TASK060: new exact diagnostics; no earlier checker is read or imported.
Three-symbol laws and bounded fields test finite-N algebra only, not the
singular dynamics. Logarithms use certified rational intervals from the
atanh series. Finite-group Fourier tests check normalization and deletion,
not a numerical approximation of the continuum Riesz equation.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from functools import lru_cache
import hashlib,json,sys

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
counts=defaultdict(int)
def eq(x,y,group,detail=''):
 if x!=y: raise AssertionError(f'{group}: {detail}: {x} != {y}')
 counts[group]+=1
def ok(x,group,detail=''):
 if not x: raise AssertionError(f'{group}: {detail}')
 counts[group]+=1
for line in (OUT/'ROUND_010_LAW_INPUT_SHA256SUMS.txt').read_text().splitlines():
 digest,rel=line.split('  ',1)
 eq(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),digest,'input_hash',rel)

@lru_cache(None)
def log_interval(x):
 assert x>0
 z=(x-1)/(x+1)
 if not z: return F(0),F(0)
 terms=40
 val=2*sum((z**(2*j+1))/F(2*j+1) for j in range(terms))
 err=2*abs(z)**(2*terms+1)/(F(2*terms+1)*(1-z*z))
 return val-err,val+err

def marginal(law,k):
 out=defaultdict(F)
 for xs,mass in law.items(): out[xs[:k]]+=mass
 return dict(out)
def entropy_interval(law):
 k=len(next(iter(law)))
 lower=upper=F(0)
 for xs,mass in law.items():
  if mass:
   lo,hi=log_interval(mass*3**k)
   lower+=mass*lo;upper+=mass*hi
 return lower,upper

def norm_l1(law):
 k=len(next(iter(law)))
 return sum(abs(m-F(1,3**k)) for m in law.values())

def table_data(G):
 A=[sum(row)/3 for row in G]
 H=[[G[x][y]-A[x] for y in range(3)] for x in range(3)]
 return A,H

def fields(G,N):
 A,H=table_data(G)
 out={}
 for xs in product(range(3),repeat=N):
  direct=[sum(G[xs[i]][xs[j]] for j in range(N) if j!=i)/F(N*N)-A[xs[i]]/N for i in range(N)]
  centered=[(sum(H[xs[i]][xs[j]] for j in range(N) if j!=i)-A[xs[i]])/F(N*N) for i in range(N)]
  eq(direct,centered,'deleted_field_identity',f'N={N}')
  out[xs]=direct
 return out,A,H

def contraction_check(law,N,G,field,A,H,label):
 direct=sum(m*sum(v*v for v in field[xs]) for xs,m in law.items())
 pair=sum(m*H[xs[0]][xs[1]]**2 for xs,m in law.items())
 triple=sum(m*H[xs[0]][xs[1]]*H[xs[0]][xs[2]] for xs,m in law.items()) if N>=3 else F(0)
 mixed=sum(m*H[xs[0]][xs[1]]*A[xs[0]] for xs,m in law.items())
 one=sum(m*A[xs[0]]**2 for xs,m in law.items())
 expanded=((N-1)*pair+(N-1)*(N-2)*triple-2*(N-1)*mixed+one)/F(N**3)
 eq(direct,expanded,'four_term_exchangeable_identity',f'{label},N={N}')
 return direct,pair,triple,mixed,one

gradient_tables={
 'constant_test':[[F(0)]*3 for _ in range(3)],
 'row_only':[[F(v)]*3 for v in (-2,0,2)],
 'mixed_field':[[F(v) for v in row] for row in ((0,3,-2),(-4,1,5),(6,-1,-3))],
 'large_tail':[[F(v) for v in row] for row in ((-9,0,7),(2,-5,12),(-3,11,1))],
}
seen={'mixed':False,'triple':False,'tail':False,'cross':False}
base=[F(1,2),F(1,3),F(1,6)]
for N in (2,3,4):
 states=list(product(range(3),repeat=N))
 uniform={xs:F(1,3**N) for xs in states}
 for mixing in (F(0),F(1,2),F(1)):
  law={}
  for xs in states:
   correlated=F(0)
   for shift in range(3):
    term=F(1,3)
    for x in xs: term*=base[(x-shift)%3]
    correlated+=term
   law[xs]=(1-mixing)*uniform[xs]+mixing*correlated
  eq(sum(law.values()),F(1),'law_mass',f'N={N}')
  for xs,m in law.items():
   for shift in range(3): eq(law[tuple((x+shift)%3 for x in xs)],m,'common_translation')
   eq(law[tuple(reversed(xs))],m,'exchangeability')
  eq(marginal(law,1),{(x,):F(1,3) for x in range(3)},'one_body_Haar')
  full_lo,full_hi=entropy_interval(law)
  for k in range(1,N+1):
   mk=marginal(law,k);lo,hi=entropy_interval(mk)
   if k==1: eq((lo,hi),(F(0),F(0)),'one_body_entropy_zero')
   elif k==N: eq((lo,hi),(full_lo,full_hi),'entropy_factor_endpoint')
   else: ok(F(k-1,N-1)*full_lo-hi>=0,'certified_entropy_marginal_factor',f'N={N},k={k},mix={mixing}')
   ok(lo>=norm_l1(mk)**2/2,'certified_Pinsker_normalization',f'N={N},k={k},mix={mixing}')
  tv2=norm_l1(marginal(law,2))
  tv3=norm_l1(marginal(law,3)) if N>=3 else F(0)
  for name,G in gradient_tables.items():
   vf,A,H=fields(G,N)
   Q,_,tr,mx,_=contraction_check(law,N,G,vf,A,H,name)
   seen['mixed']|=bool(mx);seen['triple']|=bool(tr)
   for L in (F(1),F(2),F(5)):
    clipped=[[max(-L,min(L,v)) for v in row] for row in G]
    tail=[[G[x][y]-clipped[x][y] for y in range(3)] for x in range(3)]
    vc,Ac,Hc=fields(clipped,N);vt,At,Ht=fields(tail,N)
    Qc,pc,tc,mc,oc=contraction_check(law,N,clipped,vc,Ac,Hc,'clipped')
    Qt,pt,tt,mt,ot=contraction_check(law,N,tail,vt,At,Ht,'tail')
    ref=sum(uniform[xs]*sum(v*v for v in vc[xs]) for xs in states)
    g2=sum(v*v for row in clipped for v in row)/9;a2=sum(v*v for v in Ac)/3
    eq(ref,F(N-1,N**3)*g2-F(N-2,N**3)*a2,'clipped_Haar_identity')
    dc2=pc-sum(v*v for row in Hc for v in row)/9
    dc3=tc;dcA=mc
    eq(Qc-ref,((N-1)*dc2+(N-1)*(N-2)*dc3-2*(N-1)*dcA)/F(N**3),'clipped_law_reduction')
    ok(abs(dc2)<=4*L*L*tv2,'bounded_pair_deviation')
    ok(abs(dc3)<=4*L*L*tv3,'bounded_triple_deviation')
    ok(abs(dcA)<=2*L*L*tv2,'bounded_mixed_deviation')
    cross=sum(law[xs]*sum(vc[xs][i]*vt[xs][i] for i in range(N)) for xs in states)
    for xs in states: eq(vf[xs],[vc[xs][i]+vt[xs][i] for i in range(N)],'field_full_clip_tail')
    eq(Q,Qc+Qt+2*cross,'bracket_full_clip_tail')
    ok(cross*cross<=Qc*Qt,'tail_triangle_CS')
    seen['tail']|=bool(Qt);seen['cross']|=bool(cross)
    for beta in (F(1,4),F(1),F(5)):
     nu=1/beta;b=min(beta,F(1));scale=2*nu*N*b
     bound=8*nu*b*L*L*F(N-1,N*N)*(2*tv2+(N-2)*tv3)
     ok(scale*abs(Qc-ref)<=bound,'scaled_clipped_error_constant',f'N={N}')
     eq(scale*Qt,2*nu*b/F(N*N)*((N-1)*pt+(N-1)*(N-2)*tt-2*(N-1)*mt+ot),'scaled_tail_all_coefficients')
     ok(b*b*nu<=1,'physical_b_sqrt_nu_factor')
    if name=='constant_test': eq((Q,Qc,Qt),(F(0),F(0),F(0)),'constant_h_noise_zero')
    eq(F(0)*N*(Q+Qc+Qt),F(0),'zero_noise_no_reciprocal')
for key,value in seen.items(): ok(value,'nontrivial_contractions',key)

# Finite-group positive Fourier energy: Haar on Z_2^2, no continuum approximation.
def character(k,x): return F(-1 if bin(k&x).count('1')%2 else 1)
eigen={1:1,2:2,3:3};c=F(3,2)
coeff={k:c/eigen[k] for k in eigen}
D=[sum(c*character(k,x) for k in eigen) for x in range(4)]
eq(sum(D),F(0),'Coulomb_compensation_mass')
eq(D,[3*c,-c,-c,-c],'Coulomb_atom_minus_Haar')
for k in range(4):
 for x in range(4):
  conv=sum(D[x^y]*character(k,y) for y in range(4))/4
  eq(conv,c*character(k,x) if k else F(0),'Coulomb_Fourier_sign')
for q1,q2 in ((F(1),F(1,2)),(F(3,4),F(1,3))):
 ga=[sum(coeff[k]*q1**eigen[k]*character(k,x) for k in eigen) for x in range(4)]
 gb=[sum(coeff[k]*(q1*q2)**eigen[k]*character(k,x) for k in eigen) for x in range(4)]
 heat_error=max(gb[x]-ga[x] for x in range(4))
 ok(heat_error>=0,'heat_comparison_sign')
 for N in (2,3):
  for xs in product(range(4),repeat=N):
   complete=sum(gb[x^y] for x in xs for y in xs)
   spectral=sum(coeff[k]*(q1*q2)**eigen[k]*sum(character(k,x) for x in xs)**2 for k in eigen)
   eq(complete,spectral,'positive_Fourier_configuration_energy')
   ok(complete>=0,'positive_Fourier_configuration_energy')
   ordered=sum(gb[xs[i]^xs[j]] for i in range(N) for j in range(N) if i!=j)
   eq(ordered,complete-N*gb[0],'exact_deleted_self_energy')
   Ua=sum(ga[xs[i]^xs[j]] for i in range(N) for j in range(i+1,N))/N
   Ub=ordered/F(2*N)
   ok(Ua>=Ub-F(N-1,2)*heat_error,'heat_energy_pair_coefficient')
   ok(Ua>=-gb[0]/2-F(N-1,2)*heat_error,'uniform_energy_lower_bound_algebra')

# Free-energy integration-by-parts coefficients. Scores and forces are exact
# rational vectors, checking the completed square rather than importing a PDE.
weights=[F(1,2),F(1,3),F(1,6)]
score=[F(-2),F(1,2),F(3)];force=[F(1),F(-3),F(2,3)]
for nu in (F(1,4),F(1),F(3)):
 Hdot=-nu*sum(w*l*l for w,l in zip(weights,score))-sum(w*l*u for w,l,u in zip(weights,score,force))
 Udot=-nu*sum(w*l*u for w,l,u in zip(weights,score,force))-sum(w*u*u for w,u in zip(weights,force))
 square=sum(w*(nu*l+u)**2 for w,l,u in zip(weights,score,force))
 eq(nu*Hdot+Udot,-square,'free_energy_nu_squared_identity')
 ok(square>=0,'free_energy_dissipation_sign')

for d in range(3,13):
 for quarter in range(1,4*(d-2)+1):
  s=F(quarter,4);p=s+2;a=s/p;heat_power=-2/p;clip_power=1/(4*p)
  eq(-s*heat_power/2,a,'heat_self_energy_exponent')
  eq(1+heat_power,a,'heat_compensation_exponent')
  eq((a-1)/2,-1/p,'entropy_TV_exponent')
  eq(2*clip_power-1/p,-1/(2*p),'actual_clipped_rate')
  ok(0<clip_power<1/(2*p),'admissible_growing_threshold')
  critical=1-s/d-2/p
  eq(critical,s*(d-s-2)/(d*p),'critical_entropy_factor_distinct')
  ok(critical>=0,'critical_entropy_factor_distinct')
  if s==d-2: eq(critical,F(0),'Coulomb_critical_entropy_borderline')
  if s>2:
   q=(1+s/2)/2;r=s/q
   ok(1<q<s/2 and r>2 and 2-r<0,'pair_energy_tail_power')
  else:
   q=(1+F(d,2))/2
   ok(s/q<2,'low_s_pair_energy_insufficient')
for N in range(2,51):
 ok(4*(N-1)**2<=2*(3*N-2)**2,'uniform_clipped_constant_all_N')

result={'task':'TASK060','status':'PASS','classification':'continuation-constructor exact self-check; full actual-noise assertion remains OPEN',
 'arithmetic':'exact Fraction arithmetic; logarithm bounds from 40-term atanh series with rational remainder; no floating-point tolerance or random seed',
 'python':sys.version.split()[0],'assertions':sum(counts.values()),'counts':dict(sorted(counts.items())),
 'scope':'Finite-law algebra and certified entropy diagnostics support the analytic proof. They are not simulated singular dynamics, independent audit, or proof of the remaining large-gradient tail.'}
(OUT/'ROUND_010_LAW_EXACT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
