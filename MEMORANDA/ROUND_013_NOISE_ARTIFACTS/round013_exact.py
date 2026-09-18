#!/usr/bin/env python3
"""Exact supporting diagnostics for the new bounded-noise implication.
No source checker is imported. These finite probes do not prove analytic limits.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import hashlib,json
counts=Counter()
def check(value,group):
    if not value: raise AssertionError(group)
    counts[group]+=1
# Compute the radial generator coefficients from the trace of the radial Hessian:
# radial eigenvalue q(q+1), d-1 transverse eigenvalues -q; pair diffusion 2nu.
for d in range(4,13):
    for j in range(1,24):
        s=F(j,12);p=s+2;a=s/p;theta=1-s/d
        for q in [p/2,1+s/4]:
            eta=s+1-q
            trace=q*(q+1)-(d-1)*q
            check(2*trace==-2*q*(d-2-q)<0,'radial_diffusion')
            check(-2*s*q+2*s==-2*s*(q-1)<0,'one_sided_jacobian')
            check(1<q<min(d-2,F(d,2)) and 0<=eta<2,'admissible_weights')
            check(eta/p+1/p*q==(s+1)/p,'source_N_balance')
            check(-eta/2+F(1,2)*(s+1-q)==0,'source_diffusion_balance')
        q=1+s/4;eta=s+1-q;r=p/q;eps=1/(6*p*p)
        check(r>2 and q*r==p,'actual_tail_moment')
        check(eps*eta*r/2+(2-r)/(4*p)==-s/(4*p*(s+4))<0,'tail_power')
        check(eps*(1-s/2)==(2-s)/(12*p*p)>0,'small_diffusion_power')
        check(a-theta<0 and (s-2)/p<0,'remaining_decay')
        check(eps<2/p,'scale_order')
# A literal finite-label vector-field test. Use a finite three-point probability
# space with a nonproduct exchangeable law: all labels equal. Haar here is only
# a discrete algebra diagnostic; no claim identifies this with actual dynamics.
points=[F(-2),F(1),F(3)]
for N in range(2,10):
 for x in points:
  for L in [F(1),F(2),F(5)]:
   def G(x,y): return x*x+y*y+x*y+F(1,2)
   def clipped(x,y): return min(G(x,y),L)
   A=sum(G(x,y) for y in points)/3
   AL=sum(clipped(x,y) for y in points)/3
   raw=((N-1)*G(x,x)-N*A)/(N*N)
   clip=((N-1)*clipped(x,x)-N*AL)/(N*N)
   residual=((N-1)*(G(x,x)-clipped(x,x))-N*(A-AL))/(N*N)
   check(raw==clip+residual,'exact_field_decomposition')
   check(raw*raw<=2*clip*clip+2*residual*residual,'field_hilbert_bound')
   upper=F(2*(N-1)**2,N**3)*(G(x,x)-clipped(x,x))**2+F(2,N)*(A-AL)**2
   check(N*residual*residual<=upper,'deleted_label_bound')
   for nu in [F(1,9),F(1),F(7)]:
    b=min(1/nu,F(1))
    check(b*b*nu<=1 and nu*b<=1,'physical_factors')
# Explicit excluded boundaries are not given a false strict sign.
for d in range(3,9):
 s=F(d-2);check(s*(d-2-s)==0,'Coulomb_exclusion')
s=F(2);check(1-s/2==0,'s2_exclusion')
check(F(3)-2==1,'d3_weight_exclusion')
here=Path(__file__).resolve().parent
root=here.parent.parent
inputs={}
for line in (here/'INPUT_SHA256SUMS.txt').read_text().splitlines():
 h,name=line.split(None,1);actual=hashlib.sha256((root/name).read_bytes()).hexdigest()
 check(h==actual,'input_seals');inputs[name]=actual
result={'status':'PASS: exact supporting diagnostics, not analytic certification','assertions':sum(counts.values()),'groups':dict(counts),'arithmetic':'stdlib Fraction; no random input or floating tolerance','inputs':inputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(here/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'assertions':result['assertions'],'groups':dict(counts)}))
