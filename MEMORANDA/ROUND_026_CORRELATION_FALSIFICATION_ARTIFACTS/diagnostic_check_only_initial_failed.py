#!/usr/bin/env python3
"""Fresh exact finite-Fourier and scalar cutoff diagnostic; no SDE simulation."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import itertools, json, math, sys

class Q:
    def __init__(self, r=0, i=0): self.r,self.i=F(r),F(i)
    def __add__(self,o):
        if not isinstance(o,Q): o=Q(o)
        return Q(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return Q(-self.r,-self.i)
    def __sub__(self,o): return self+-asq(o)
    def __rsub__(self,o): return asq(o)+-self
    def __mul__(self,o):
        o=asq(o); return Q(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asq(o); d=o.r*o.r+o.i*o.i
        return Q((self.r*o.r+self.i*o.i)/d,(self.i*o.r-self.r*o.i)/d)
    def conj(self): return Q(self.r,-self.i)
    def abs2(self): return self.r*self.r+self.i*self.i
    def __eq__(self,o):
        o=asq(o); return self.r==o.r and self.i==o.i
    def out(self): return [str(self.r),str(self.i)]
def asq(o): return o if isinstance(o,Q) else Q(o)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def phase(k,x): return (Q(1),Q(0,1),Q(-1),Q(0,-1))[dot(k,x)%4]
def polyadd(p,key,val):
    p[key]=p.get(key,F(0))+val
    if not p[key]: del p[key]

counts=Counter(); controls={}; assertions=0

def check(category,condition):
    global assertions
    assertions+=1; counts[category]+=1
    if not condition: raise AssertionError(category)

def control(name,expected,mutated,detail):
    if expected!=mutated and name not in controls:
        controls[name]={'expected': asq(expected).out(), 'mutated':asq(mutated).out(), 'detail':detail}

zero=(0,0)
configs=[[(0,0),(1,0)],[(0,0),(1,1),(2,0)],
         [(0,0),(1,0),(1,2),(3,1)],
         [(0,0),(0,1),(1,3),(2,1),(3,2)]]
for heat in [F(1,2),F(3,4)]:
    a={q:heat**dot(q,q)/dot(q,q)
       for q in itertools.product(range(-2,3),repeat=2) if q!=zero}
    for k in [(1,0),(1,1),(2,0),(3,1)]:
        d=dot(k,k)*a.get(k,F(0))
        jpoly={}
        for q,weight in a.items():
            t=dot(q,k)*weight
            polyadd(jpoly,(add(q,k),neg(q)),t)
            polyadd(jpoly,(q,sub(k,q)),-t)
        polyadd(jpoly,(k,zero),d); polyadd(jpoly,(zero,k),d)
        rows={}; cols={}
        for (p,q),v in jpoly.items():
            if q==zero: polyadd(rows,p,v)
            if p==zero: polyadd(cols,q,v)
            check('pair symmetry',jpoly.get((q,p),F(0))==v)
        check('both zero Haar rows',not rows and not cols)
        am={}
        for (p,q),v in jpoly.items():
            check('translation covariance',add(p,q)==k)
            polyadd(am,sub(p,k),v)
        all_m=set(a)|{sub(q,k) for q in a}|{zero,neg(k)}
        formula={m:dot(k,m)*a.get(m,F(0))-dot(k,add(m,k))*a.get(add(m,k),F(0))
                    +d*(int(m==zero)+int(m==neg(k))) for m in all_m}
        formula={m:v for m,v in formula.items() if v}
        check('derived overlap Fourier coefficient',am==formula)
        check('constant overlap Fourier coefficient',am.get(zero,F(0))==0)
        check('finite smooth self trace',sum(am.values(),F(0))==2*d)
        wrong_rows=F(1)-d
        control('Coulomb response inserted at finite heat cutoff',F(0),wrong_rows,{'heat':str(heat),'k':k})
        control('wrong background sign',F(0),-2*d,{'heat':str(heat),'k':k})
        def j(x,y):
            z=sub(x,y); ekx=phase(k,x); eky=phase(k,y)
            raw=sum((dot(q,k)*weight*phase(q,z)*(ekx-eky) for q,weight in a.items()),Q())
            return raw+d*(ekx+eky)
        for current in configs:
            n=len(current)
            initial=[((x[0]+i+1)%4,(x[1]+2*i+1)%4) for i,x in enumerate(current)]
            ec=[phase(k,x) for x in current]; e0=[phase(k,x) for x in initial]
            z=sum(ec,Q())/n; z0=sum(e0,Q())/n
            js={(i,jj):j(current[i],current[jj]) for i in range(n) for jj in range(n) if i!=jj}
            rawJ=sum((v-d*(ec[i]+ec[jj]) for (i,jj),v in js.items()),Q())/(2*n*n)
            U=sum(js.values(),Q())/(2*n*n)
            P=rawJ+d*z
            check('deleted residual row',P==U+d*z/n)
            control('delete residual row',P,U,{'n':n,'k':k,'heat':str(heat)})
            control('reverse residual row',P,U-d*z/n,{'n':n,'k':k,'heat':str(heat)})
            A2=sum((v*ec[i].conj() for (i,jj),v in js.items()),Q())/(n*(n-1))
            B2=sum((v*e0[i].conj() for (i,jj),v in js.items()),Q())/(n*(n-1))
            spec=sum((v*(sum((phase(m,x) for x in current),Q())/n).abs2() for m,v in am.items()),F(0))
            rhs=F(n,n-1)*spec-F(2,n-1)*d
            check('new overlap spectral self subtraction',A2==rhs)
            control('omit overlap self subtraction',A2,F(n,n-1)*spec,{'n':n,'k':k,'heat':str(heat)})
            control('wrong overlap self denominator',A2,F(n,n-1)*spec-F(2,n)*d,{'n':n,'k':k,'heat':str(heat)})
            A3=B3=Q()
            if n>=3:
                A3=sum((v*ec[l].conj() for (i,jj),v in js.items() for l in range(n) if l not in (i,jj)),Q())/(n*(n-1)*(n-2))
                B3=sum((v*e0[l].conj() for (i,jj),v in js.items() for l in range(n) if l not in (i,jj)),Q())/(n*(n-1)*(n-2))
            f=F(n-1,n)*A2+F((n-1)*(n-2),2*n)*A3
            g=F(n-1,n)*B2+F((n-1)*(n-2),2*n)*B3
            check('exact current overlaps',n*U*z.conj()==f)
            check('exact mixed initial overlaps',n*U*z0.conj()==g)
            control('omit ordered half',n*U*z.conj(),2*f,{'n':n,'k':k,'heat':str(heat)})
            control('falling-factorial source denominator',n*U*z.conj(),F(n,n-1)*f,{'n':n,'k':k,'heat':str(heat)})
            control('miss one pair overlap',n*U*z.conj(),F(n-1,2*n)*A2+F((n-1)*(n-2),2*n)*A3,{'n':n,'k':k,'heat':str(heat)})
            control('double distinct-label coefficient',n*U*z.conj(),F(n-1,n)*A2+F((n-1)*(n-2),n)*A3,{'n':n,'k':k,'heat':str(heat)})
            control('replace initial phase by current phase',B2,A2,{'n':n,'k':k,'heat':str(heat)})
            sj=sum((v.abs2() for v in js.values()),F(0))/(n*(n-1))
            sd=sum(((e0[i]-ec[i]).abs2() for i in range(n)),F(0))/n
            check('mixed-overlap Cauchy Schwarz',(B2-A2).abs2()<=sj*sd)
            smooth_pair_energy=sum((sum((weight*phase(q,sub(current[i],current[jj])) for q,weight in a.items()),Q()) for i in range(n) for jj in range(n) if i!=jj),Q())/(2*n)
            sm=sum((weight*(sum((phase(q,x) for x in current),Q())/n).abs2() for q,weight in a.items()),F(0))
            energy_rhs=F(n,2)*sm-sum(a.values(),F(0))/2
            check('exact energy diagonal',smooth_pair_energy==energy_rhs)
            control('omit energy self term',smooth_pair_energy,F(n,2)*sm,{'n':n,'k':k,'heat':str(heat)})
            control('factor two energy self term',smooth_pair_energy,F(n,2)*sm-sum(a.values(),F(0)),{'n':n,'k':k,'heat':str(heat)})

# Exact dyadic radial diagnostic. The uniform 4D radius has P(r<=R)=R^4.
# r lies in shells (2^-(j+1),2^-j]; the inverse fourth-power upper envelope
# has expectation at most 16 times the exact truncated radial integral.
radial=[]
for m in range(1,21):
    eps=F(1,4**m); n=16**m
    # eps=n^-1/2, and r^-4 truncated at eps^-2.
    moment=F(0)
    for j in range(m):
        shell=F(1,16**j)-F(1,16**(j+1))
        moment+=shell*16**(j+1)
    moment+=F(1,16**m)*16**m
    check('exact dyadic logarithmic moment',moment==15*m+1)
    # An abstract 1/N atom at the cutoff is a permitted small-ball-majorant
    # diagnostic only, not an actual particle-law witness.
    atom=F(1,n)*eps**-2
    check('self error gives constant at microscopic heat cutoff',atom==1)
    control('drop growing logarithmic truncated moment',moment,F(16),{'m':m,'n':n})
    bad_eps=eps*eps
    amplified=F(1,n)*bad_eps**-2
    check('finer cutoff retains N inverse epsilon squared error',amplified==n)
    control('drop finite N cutoff term',amplified,F(1),{'m':m,'n':n})
    radial.append({'m':m,'N':str(n),'epsilon':str(eps),'dyadic_second_moment':str(moment),'finer_cutoff_term':str(amplified)})

# Deterministic heat-multiplier comparison: finite sample diagnostic only.
# The proof, not this loop, handles all lattice modes and parameters.
ratios=[]
c=4*math.pi**2
for k in [(1,0,0,0),(1,1,0,0),(2,1,1,0)]:
    for eps in [1e-6,1e-4,1e-2,0.1]:
        for m in itertools.product(range(-6,7),repeat=4):
            if m==(0,0,0,0): continue
            mp=tuple(a+b for a,b in zip(m,k)); r2=dot(m,m); s2=dot(mp,mp)
            x=dot(k,m)*math.exp(-c*eps*r2)/r2
            if s2: x-=dot(k,mp)*math.exp(-c*eps*s2)/s2
            dk=math.exp(-c*eps*dot(k,k))
            if m==tuple(-a for a in k): x+=dk
            den=math.exp(-c*eps*r2/8)/r2
            ratio=abs(x)/den
            check('finite heat divided-difference envelope',ratio<500)
            ratios.append(ratio)

check('nonvacuous mutation coverage',len(controls)>=14)
result={'status':'PASS','python':sys.version.split()[0], 'assertions':assertions,
 'categories':dict(sorted(counts.items())), 'mutation_controls':controls,
 'mutation_count':len(controls), 'heat_multiplier_sample_max_ratio':max(ratios),
 'radial_diagnostics':radial,
 'limitations':['No SDE simulation or numerical asymptotic theorem.',
  'Finite Fourier algebra is a regularized diagnostic; c=(2*pi)^2 is divided out.',
  'Rational heat multipliers in exact tests are powers of 1/2 or 3/4; no singular law is substituted.',
  'Heat-envelope sample uses IEEE double arithmetic and bound 500, not interval certification.',
  'Dyadic atom model is a negative control for a majorant, not an admitted dynamic counterexample.']}
result_path=Path(__file__).with_name('DIAGNOSTIC_RESULT.json')
if '--check-only' in sys.argv:
    stored=json.loads(result_path.read_text())
    for key in result:
        if key != 'python' and stored[key] != result[key]:
            raise AssertionError('Stored result mismatch: '+key)
else:
    result_path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'assertions':assertions,'categories':len(counts),'nonvacuous_mutations':len(controls),'heat_sample_max_ratio':max(ratios)},sort_keys=True))
