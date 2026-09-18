#!/usr/bin/env python3
"""AUD074 fresh exact-algebra checks and a declared finite floating sweep.
Prints JSON only. No files are read or written; no simulation or dependencies.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from collections import Counter
import itertools
import json
import math
import sys

@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)
    @staticmethod
    def cast(v):
        return v if isinstance(v,Q) else Q(F(v))
    def __add__(self,v):
        v=Q.cast(v)
        return Q(self.re+v.re,self.im+v.im)
    __radd__=__add__
    def __neg__(self):
        return Q(-self.re,-self.im)
    def __sub__(self,v):
        return self+(-Q.cast(v))
    def __rsub__(self,v):
        return Q.cast(v)-self
    def __mul__(self,v):
        v=Q.cast(v)
        return Q(self.re*v.re-self.im*v.im,self.re*v.im+self.im*v.re)
    __rmul__=__mul__
    def __truediv__(self,v):
        v=Q.cast(v)
        return self*v.conj()*(1/v.norm2())
    def conj(self):
        return Q(self.re,-self.im)
    def norm2(self):
        return self.re*self.re+self.im*self.im
    def export(self):
        return {'real':str(self.re),'imag':str(self.im)}

Z=(0,0,0,0)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def n2(x): return dot(x,x)
def phase(k,p):
    return (Q(F(1)),Q(F(0),F(1)),Q(F(-1)),Q(F(0),F(-1)))[dot(k,p)%4]

counts=Counter()
mutations={}
def check(name,truth):
    counts[name]+=1
    if not truth:
        raise AssertionError(name)
def mutation(name,correct,wrong,context):
    correct,wrong=Q.cast(correct),Q.cast(wrong)
    if correct!=wrong and name not in mutations:
        mutations[name]={'context':context,'correct':correct.export(),
            'mutated':wrong.export(),'nonzero_difference':(wrong-correct).export()}

seeds=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
       (1,1,0,0),(1,-1,1,0),(2,0,0,0),(0,2,1,0),
       (2,1,0,1),(1,0,1,1)]
klist=[(1,0,0,0),(1,1,0,0),(2,0,0,0),(1,-1,1,0)]
curbase=[(0,0,0,0),(1,0,1,0),(0,2,0,1),(3,1,2,0),(2,3,0,1),(0,1,3,2)]
oldbase=[(1,1,0,0),(3,0,2,1),(0,3,1,0),(2,0,3,2),(1,2,1,3),(3,3,0,1)]

def run_exact():
    for kernel_id in (1,2):
        aa={}
        for m in seeds:
            aa[m]=aa[neg(m)]=F(1,1+kernel_id*n2(m))
        g0=sum(aa.values(),F(0))
        for k in klist:
            d=n2(k)*aa.get(k,F(0))
            poly={}
            def put(a,b,v):
                poly[(a,b)]=poly.get((a,b),F(0))+v
            for m,av in aa.items():
                v=dot(k,m)*av
                put(add(m,k),neg(m),v)
                put(m,sub(k,m),-v)
            put(k,Z,d)
            put(Z,k,d)
            check('haar_rows',all(v==0 for (a,b),v in poly.items() if a==Z or b==Z))
            check('smooth_diagonal_coefficient',sum(poly.values(),F(0))==2*d)
            mutation('wrong_unsmoothed_response',0,1-d,{'kernel':kernel_id,'k':k})
            mutation('reversed_centering',0,-2*d,{'kernel':kernel_id,'k':k})
            supp=set(aa)|{sub(m,k) for m in aa}|{Z,neg(k)}
            bb={}
            for m in supp:
                bb[m]=(dot(k,m)*aa.get(m,F(0))
                    -dot(k,add(m,k))*aa.get(add(m,k),F(0))
                    +d*((m==Z)+(m==neg(k))))
            check('spectral_zero_modes',bb[Z]==bb[neg(k)]==0)
            check('spectral_self_sum',sum(bb.values(),F(0))==2*d)
            for N in (2,3,4,5,6):
                for shift in (0,1):
                    cur=[tuple((a+shift*(j+1))%4 for a in p)
                         for j,p in enumerate(curbase[:N])]
                    old=oldbase[:N]
                    def mode(m):
                        return sum((phase(m,p) for p in cur),Q())/N
                    def fc(z):
                        return sum((dot(k,m)*av*phase(m,z) for m,av in aa.items()),Q())
                    def j(i,l):
                        return fc(sub(cur[i],cur[l]))*(phase(k,cur[i])-phase(k,cur[l]))+d*(phase(k,cur[i])+phase(k,cur[l]))
                    pairs=[(i,l) for i in range(N) for l in range(N) if i!=l]
                    js={(i,l):j(i,l) for i,l in pairs}
                    context={'kernel':kernel_id,'k':k,'N':N,'shift':shift}
                    for i,l in pairs:
                        check('literal_pair_symmetry',js[i,l]==js[l,i])
                        literal=js[i,l]*phase(k,cur[i]).conj()
                        spec=sum((v*phase(m,sub(cur[i],cur[l])) for m,v in bb.items()),Q())
                        check('literal_spectral_overlap',literal==spec)
                    U=sum(js.values(),Q())/(2*N*N)
                    zk=mode(k)
                    zold=sum((phase(k,p) for p in old),Q())/N
                    a2=sum((js[i,l]*phase(k,cur[i]).conj() for i,l in pairs),Q())/len(pairs)
                    b2=sum((js[i,l]*phase(k,old[i]).conj() for i,l in pairs),Q())/len(pairs)
                    sp=sum((v*mode(m).norm2() for m,v in bb.items() if m!=Z),F(0))
                    correct=F(N,N-1)*sp-F(2*d,N-1)
                    check('finite_N_overlap_identity',a2==Q(correct))
                    mutation('omit_overlap_self',a2,F(N,N-1)*sp,context)
                    mutation('reverse_overlap_self',a2,F(N,N-1)*sp+F(2*d,N-1),context)
                    mutation('halve_overlap_self',a2,F(N,N-1)*sp-F(d,N-1),context)
                    mutation('wrong_overlap_empirical_factor',a2,sp-F(2*d,N-1),context)
                    triples=[(i,l,h) for i,l in pairs for h in range(N) if h not in (i,l)]
                    if triples:
                        a3=sum((js[i,l]*phase(k,cur[h]).conj() for i,l,h in triples),Q())/len(triples)
                        b3=sum((js[i,l]*phase(k,old[h]).conj() for i,l,h in triples),Q())/len(triples)
                    else:
                        a3=b3=Q()
                        check('N2_no_third_label',not triples)
                    ow=F(N-1,N)
                    tw=F((N-1)*(N-2),2*N)
                    check('current_label_decomposition',N*U*zk.conj()==ow*a2+tw*a3)
                    check('mixed_label_decomposition',N*U*zold.conj()==ow*b2+tw*b3)
                    mutation('missing_one_overlap',N*U*zk.conj(),ow*a2/2+tw*a3,context)
                    mutation('double_three_label_weight',N*U*zk.conj(),ow*a2+2*tw*a3,context)
                    mutation('replace_initial_phase',b2,a2,context)
                    mutation('lose_ordered_half',U,2*U,context)
                    mutation('use_falling_factorial',U,sum(js.values(),Q())/(2*N*(N-1)),context)
                    Jsum=sum((js[i,l]-d*(phase(k,cur[i])+phase(k,cur[l])) for i,l in pairs),Q())
                    literal_P=Jsum/(2*N*N)+d*zk
                    check('positive_residual_row',literal_P==U+d*zk/N)
                    mutation('omit_residual_row',literal_P,U,context)
                    mutation('reverse_residual_row',literal_P,U-d*zk/N,context)
                    J2=sum((v.norm2() for v in js.values()),F(0))/len(pairs)
                    D2=sum(((phase(k,old[i])-phase(k,cur[i])).norm2() for i,l in pairs),F(0))/len(pairs)
                    check('mixed_Cauchy_Schwarz',(b2-a2).norm2()<=J2*D2)
                    gv=lambda z:sum((av*phase(m,z) for m,av in aa.items()),Q())
                    H=sum((gv(sub(cur[i],cur[l])) for i in range(N) for l in range(i+1,N)),Q())/N
                    M=sum((av*mode(m).norm2() for m,av in aa.items()),F(0))
                    check('energy_self_subtraction',H==Q(N*M/2-g0/2))
                    mutation('omit_energy_self',H,N*M/2,context)
                    # Positive q=2+cos(2pi z_1), an algebra-only splitting test.
                    qq=lambda z:Q(2)+(phase(seeds[0],z)+phase(neg(seeds[0]),z))/2
                    eq=sum((qq(sub(cur[i],cur[l])) for i,l in pairs),Q())/len(pairs)
                    eg=sum((gv(sub(cur[i],cur[l]))+qq(sub(cur[i],cur[l]))-2 for i,l in pairs),Q())/len(pairs)
                    coupled=F(N,N-1)*M+eq
                    check('coupled_exact_heat_split',coupled==eg+F(g0,N-1)+2)
                    mutation('omit_split_constant',coupled,eg+F(g0,N-1),context)
                    mutation('reverse_positive_q',coupled,F(N,N-1)*M-eq,context)
                    for l in klist:
                        direct=sum((dot(k,l)*phase(sub(k,l),p) for p in cur),Q())*F(2,7*N*N)
                        formula=F(2,7*N)*dot(k,l)*mode(sub(k,l))
                        check('modal_cross_bracket',direct==formula)

def radial():
    examples=[]
    # P(R=2^-j)=(15/16)16^-j, j>=0; infinite tail summed exactly.
    for L in range(1,31):
        r=F(1,4**L)
        cap=1/(r*r)
        summation=sum((F(15,16)*F(1,16**j)*16**j for j in range(L)),F(0))+F(1,16**L)*cap
        value=F(15,16)*L+1
        check('layer_cake_log_growth',summation==value)
        mutation('delete_logarithmic_term',value,F(1),{'L':L})
        for N in (2,16,256,65536):
            mixed=(1-F(1,N))*value+cap/N
            without=(1-F(1,N))*value
            check('finite_N_cutoff_term',mixed-without==1/(N*r*r))
            mutation('delete_finite_N_cutoff_term',mixed,without,{'L':L,'N':N,'r':str(r)})
        if L in (1,4,16,30):
            examples.append({'L':L,'r':str(r),'truncated_square':str(value)})
    rstar=F(1,64)
    for sqrtN in (2,4,16,256,65536):
        N=sqrtN*sqrtN
        r=rstar/sqrtN
        check('critical_cutoff_error_balance',(r+1/(N*r))*sqrtN==rstar+1/rstar)
        check('critical_cutoff_square_balance',1/(N*r*r)==1/(rstar*rstar))
    return examples

def modal_algebra():
    # Formal scalar ODE solution coefficients, not artificial-law realizability.
    for p,A,thermal,u,v,f,g in [
        (F(3,4),F(2,3),F(1,5),F(2,7),F(3,8),F(5,9),F(-1,6)),
        (F(4,5),F(3,5),F(1,7),F(3,11),F(5,12),F(-2,9),F(1,10))]:
        V=p*p+thermal+2*u*f
        R=p+v*g
        endpoint=V+A*A-2*A*R
        rem=u*f-A*v*g
        check('endpoint_modal_identity',endpoint==(p-A)**2+thermal+2*rem)
        mutation('lose_endpoint_factor_two',endpoint,(p-A)**2+thermal+rem,{'formal_ODE':True})
        mutation('change_mixed_response_weight',endpoint,(p-A)**2+thermal+2*(u*f-A*A*v*g),{'formal_ODE':True})
    check('T0_identity',F(1)+F(1)-2*F(1)==0)

def heat_sweep():
    c=4*math.pi**2
    radii=[2.0**(-j) for j in (1,2,4,8,12,20,30)]
    max_high=(0.0,None)
    max_low=(0.0,None)
    for k in klist:
        for m in itertools.product(range(-4,5),repeat=4):
            mm=n2(m)
            if mm==0:
                continue
            mk=add(m,k)
            vv=n2(mk)
            for r in radii:
                # Divide before exponentiation to avoid underflow ratios.
                t1=dot(k,m)*math.exp(-c*r*mm*7/8)
                t2=(dot(k,mk)*mm/vv*math.exp(-c*r*(vv-mm/8)) if vv else 0.0)
                delta=(math.exp(-c*r*n2(k))*mm*math.exp(c*r*mm/8) if m==neg(k) else 0.0)
                ratio=abs(t1-t2+delta)/n2(k)
                if mm>=4*n2(k):
                    check('heat_high_frequency_envelope',ratio<=8+1e-11)
                    if ratio>max_high[0]:
                        max_high=(ratio,{'k':k,'m':m,'r':r})
                else:
                    check('heat_low_frequency_finite',math.isfinite(ratio))
                    if ratio>max_low[0]:
                        max_low=(ratio,{'k':k,'m':m,'r':r})
    return {'type':'finite double-precision supporting sweep, not proof',
        'm_box':'[-4,4]^4 excluding zero','heat_scales':radii,
        'ratio':'abs(b)/(c*abs(k)^2*a_(r/8)(m))','high_bound':8,
        'max_high':{'value':max_high[0],'at':max_high[1]},
        'max_low':{'value':max_low[0],'at':max_low[1]}}

def main():
    run_exact()
    rad=radial()
    modal_algebra()
    heat=heat_sweep()
    check('nonzero_mutation_inventory',len(mutations)==20)
    for item in mutations.values():
        d=item['nonzero_difference']
        check('mutation_is_nonzero',F(d['real'])!=0 or F(d['imag'])!=0)
    return {'verdict':'PASS','python':sys.version,
        'arithmetic':'exact Gaussian rationals except declared heat sweep',
        'assertion_count':sum(counts.values()),'categories':dict(sorted(counts.items())),
        'mutation_count':len(mutations),'mutations':dict(sorted(mutations.items())),
        'radial_examples':rad,'heat_sweep':heat,
        'limits':['No SDE simulation or actual-law asymptotic certification.',
                  'Finite Fourier/radial models test algebra and majorants.',
                  'Infinite-frequency and singular-law proofs are in the audit.',
                  'No constructor code, results, or run history were read.']}
if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
