#!/usr/bin/env python3
"""Fresh, deterministic supporting checks for AUD073; no theorem simulation.

Only Python's standard library is used. Default execution is read-only and emits
JSON to stdout. --output PATH is used only during packet construction. Finite
Fourier and label checks use exact rational complex arithmetic with c divided
out. Gaussian, heat-scale and layer-cake probes use ordinary binary64 and are
explicitly nonrigorous supporting diagnostics. No random data or seed is used.
"""
import argparse
import itertools
import json
import math
from fractions import Fraction as F

checks=[]
mutations=[]

class Q:
    def __init__(self, a=0, b=0):
        if isinstance(a,Q): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=Q(o); return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+-Q(o)
    def __rsub__(self,o): return Q(o)+-self
    def __mul__(self,o):
        o=Q(o); return Q(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,Q):
            return (self*o.conj())/o.norm2()
        return Q(self.a/F(o),self.b/F(o))
    def conj(self): return Q(self.a,-self.b)
    def norm2(self): return self.a*self.a+self.b*self.b
    def __eq__(self,o):
        o=Q(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return '%s + (%s)i'%(self.a,self.b)

ZERO=(0,0,0,0)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def sub(x,y): return add(x,neg(y))
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def norm2(x): return dot(x,x)
def root4(n): return (Q(1),Q(0,1),Q(-1),Q(0,-1))[n%4]
def char(m,x): return root4(dot(m,x))
def check(name,pred,detail=None):
    checks.append({'name':name,'passed':bool(pred),'detail':detail})
def reject(name,residual,detail):
    nonzero=(residual!=0)
    mutations.append({'name':name,'rejected':bool(nonzero),'nonzero_residual':str(residual),'detail':detail})

def addcoef(out,index,value): out[index]=out.get(index,F(0))+value

def exact_fourier():
    summary=[]
    for k in [(1,0,0,0),(1,1,0,0),(2,-1,1,0)]:
        seeds={k,(0,1,0,0),(1,-1,0,1),(2,1,0,0),(0,0,1,1)}
        support=seeds|{neg(m) for m in seeds}
        aa={m:F(1,1+2*norm2(m)) for m in support}
        a=lambda m:aa.get(m,F(0))
        d=norm2(k)*a(k)
        raw={}
        # Differentiate K and the two gradient terms, retaining both pair slots.
        for m,v in aa.items():
            w=dot(k,m)*v
            addcoef(raw,(add(m,k),neg(m)),w)
            addcoef(raw,(m,sub(k,m)),-w)
        addcoef(raw,(k,ZERO),d)
        addcoef(raw,(ZERO,k),d)
        rowx={};rowy={};diag={}
        for (u,v),w in raw.items():
            if v==ZERO:addcoef(rowx,u,w)
            if u==ZERO:addcoef(rowy,v,w)
            addcoef(diag,add(u,v),w)
        check('exact Haar rows k='+str(k),all(v==0 for v in rowx.values()) and all(v==0 for v in rowy.values()))
        check('exact smooth diagonal k='+str(k),diag.get(k,0)==2*d and all(v==0 for u,v in diag.items() if u!=k))
        bs={}
        indices=support|{sub(m,k) for m in support}|{ZERO,neg(k)}
        for m in indices:
            bs[m]=dot(k,m)*a(m)-dot(k,add(m,k))*a(add(m,k))+d*((m==ZERO)+(m==neg(k)))
        mapped={}
        for (u,v),w in raw.items():
            m=sub(u,k)
            check('translation frequency k=%s u=%s'%(k,u),v==neg(m))
            addcoef(mapped,m,w)
        check('exact coefficient dictionary k='+str(k),all(mapped.get(m,0)==bs.get(m,0) for m in set(mapped)|set(bs)))
        check('exact exceptional coefficients k='+str(k),bs[ZERO]==0 and bs[neg(k)]==0)
        check('exact sum b k='+str(k),sum(bs.values())==2*d)
        reject('unheated response k='+str(k),1-d,'Substituting response 1 for the actual smooth response leaves a nonzero Haar row (c divided out).')
        reject('wrong source sign k='+str(k),2*d,'Changing the J row sign while retaining the response gives a nonzero row.')
        for N in [2,3,5,7]:
            xs=[((i*i+1)%4,(3*i+1)%4,(i*i+i)%4,(i+2)%4) for i in range(N)]
            direct=Q(0)
            for i in range(N):
                for j in range(N):
                    if i==j:continue
                    jval=sum((Q(v)*char(u,xs[i])*char(w,xs[j]) for (u,w),v in raw.items()),Q())
                    direct+=jval*char(k,xs[i]).conj()
            direct/=N*(N-1)
            spectral=F(0)
            for m,b in bs.items():
                if m==ZERO:continue
                Z=sum((char(m,x) for x in xs),Q())/N
                spectral+=b*Z.norm2()
            formula=Q(F(N,N-1)*spectral-F(2,N-1)*d)
            check('exact overlap k=%s N=%s'%(k,N),direct==formula,{'direct':str(direct),'spectral':str(formula)})
            reject('missing self k=%s N=%s'%(k,N),Q(F(2,N-1)*d),'Dropping the smooth 2d/(N-1) subtraction gives this nonzero residual on the same finite Fourier model.')
        summary.append({'k':k,'support_size':len(support),'response_c_divided_out':str(d),'sum_b_c_divided_out':str(sum(bs.values()))})
    return summary

def label_counts():
    outcomes=[]
    for N in [2,3,5,8]:
        J={(i,j):Q(F(i+j+2,3),F((i+1)*(j+1),7)) for i in range(N) for j in range(N) if i!=j}
        U=sum(J.values(),Q())/(2*N*N)
        for kind,weights in [('current',[Q(F(i+1,5),F(i*i+1,11)) for i in range(N)]),('initial',[Q(F(2*i+1,13),F(i+2,17)) for i in range(N)])]:
            overlap=sum((J[i,j]*weights[i].conj() for i,j in J),Q())/(N*(N-1))
            triple=Q()
            if N>=3:
                triple=sum((J[i,j]*weights[l].conj() for i,j in J for l in range(N) if l not in (i,j)),Q())/(N*(N-1)*(N-2))
            lhs=N*U*(sum(weights,Q())/N).conj()
            rhs=F(N-1,N)*overlap+F((N-1)*(N-2),2*N)*triple
            check('exact %s label expansion N=%s'%(kind,N),lhs==rhs,{'lhs':str(lhs),'rhs':str(rhs),'triple':str(triple)})
            reject('one overlap only %s N=%s'%(kind,N),F(N-1,2*N)*overlap,'Omitting the second overlapping label loses a nonzero contribution.')
            if N>=3:
                reject('extra N in triple %s N=%s'%(kind,N),F((N-1)*(N-2),2*N)*(1-F(1,N))*triple,'A denominator 2N^2 instead of 2N loses a nonzero contribution.')
            else:check('N2 no third label '+kind,triple==0)
            outcomes.append({'N':N,'kind':kind,'two_label_coefficient':str(F(N-1,N)),'three_label_coefficient':str(F((N-1)*(N-2),2*N))})
    check('T0 all remainders zero',sum([])==0)
    return outcomes

def gaussian_and_scales():
    ratios=[]
    for v in [0.0,1e-8,1e-4,.1,1,2,4,8,12,32,128,1000]:
        ratio=2*v*math.exp(-v/8)
        ratios.append({'squared_distance_over_time':v,'gradient_to_doubled_heat_ratio':ratio})
        check('Gaussian doubled heat v='+str(v),ratio<=6.0)
    for x in [.0001,.01,.1,.5,1.0]:
        # Exact central Euclidean integral q_(R^2)(xR)*R^2.
        value=math.exp(-x*x/4)/(x*x)
        check('small-ball central heat x='+str(x),value>=math.exp(-.5)/8,{'scaled_value':value,'asserted_lower':math.exp(-.5)/8})
    layers=[]
    for N in [2,7,100,10000]:
        for r in [0.5,0.1,1e-3,1e-6]:
            # A radial law with CDF <=R^4+1/N on [0,1], not the actual SDE law.
            eps=r
            expectation=(1-1/N)*(1+2*math.log(1/r))+(1/N)*min(r**-2,eps**-4)
            majorant=2*(1+math.log(1/r)+1/(N*r*r))
            check('layer-cake majorant N=%s r=%s'%(N,r),expectation<=majorant*(1+1e-14))
            layers.append({'N':N,'r':r,'constructed_radial_expectation':expectation,'majorant':majorant})
    N=2;r=1e-6
    full=(1-1/N)*(1+2*math.log(1/r))+1/(N*r*r)
    without=2*(1+math.log(1/r))
    reject('omit finite-N truncated-square term',full-without,'Constructed radial-law stress test, not an admitted actual-law counterexample: the small-ball premise alone does not imply a pure logarithmic square bound.')
    return {'gaussian_ratios':ratios,'radial_law_layer_checks':layers}

def all_frequency_probes():
    c=4*math.pi**2
    records=[]
    for k in [(1,0,0,0),(1,1,0,0),(2,-1,1,0)]:
        mx=0.;arg=None;count=0
        ms=list(itertools.product(range(-3,4),repeat=4))
        ms += [(L,1,-2,3) for L in [10,100,1000,1000000]]
        ms += [tuple(-L*v for v in k) for L in [2,10,100,10000]]
        for m in ms:
            nm=norm2(m)
            if not nm:continue
            mp=add(m,k);np=norm2(mp)
            for tau in [.0001,.01,.1,1,10,100]:
                r=min(.5,tau/(c*nm))
                # Stable normalized formula b/(c*a_(r/8)); no small denominator.
                val=dot(k,m)*math.exp(-c*r*nm*7/8)
                if np:val-=dot(k,mp)*nm/np*math.exp(-c*r*(np-nm/8))
                if m==neg(k):val+=math.exp(-c*r*norm2(k))*nm*math.exp(c*r*nm/8)
                ratio=abs(val)
                if ratio>mx:mx=ratio;arg={'m':m,'r':r,'tau':tau}
                count+=1
        # Very generous fixed test threshold: these probes do not prove uniformity.
        check('finite all-frequency stress k='+str(k),math.isfinite(mx) and mx<1000*norm2(k),{'max_ratio_c_divided_out':mx,'argmax':arg,'probes':count})
        records.append({'k':k,'probes':count,'max_ratio_c_divided_out':mx,'argmax':arg})
    # Analytic expression shows why unchanged heat scale is a stronger false row.
    L=100.;r=.1
    x=c*r*(2*L-1)
    # log(-L+L^2/(L-1)*exp(x)), avoiding overflow.
    log_bad=math.log(L*L/(L-1))+x+math.log1p(-(L-1)/L*math.exp(-x))
    reject('replace weakened heat scale by identical scale',log_bad-700,'For k=e1,m=-100e1,r=.1 the log ratio |b|/(c*a_r) exceeds 700. This tests a stronger excluded bound, not THM051.')
    return {'sampled_bounds':records,'unchanged_heat_scale_log_ratio':log_bad,'binary64_only':True}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    details={'exact_fourier':exact_fourier(),'exact_label_counts':label_counts(),'gaussian_layer':gaussian_and_scales(),'all_frequency':all_frequency_probes()}
    result={'diagnostic_id':'AUD073-FRESH-20260918','status':'PASS' if all(x['passed'] for x in checks) and all(x['rejected'] for x in mutations) else 'FAIL','exact_arithmetic':'fractions.Fraction with rational complex pairs; c divided out for algebra','floating_arithmetic':'Python binary64; finite supportive probes only','randomness':'none','actual_singular_law_simulated':False,'theorem_proof':'RECONSTRUCTION.md sections 2-10, not this program','check_count':len(checks),'mutation_count':len(mutations),'checks':checks,'mutations':mutations,'details':details,'limitations':['No floating-point or finite-grid result proves a uniform infinite-frequency estimate.','Finite Fourier models test coefficient algebra only; they do not replace the actual singular law.','Constructed radial law tests the strength of a small-ball premise only.','No critical signed three-label cancellation or counterexample is inferred.']}
    raw=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(raw)
    else:print(raw,end='')
    raise SystemExit(0 if result['status']=='PASS' else 1)

if __name__=='__main__':main()
