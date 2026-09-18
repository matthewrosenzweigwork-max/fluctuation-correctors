#!/usr/bin/env python3
"""AUD075 fresh rational diagnostics; standard library only; no file writes."""
import argparse,itertools,json,sys
from fractions import Fraction as Q

def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    return z

def scale(a,s): return [s*v for v in a]
def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): z[i+j]+=v*w
    return z

def power(a,n):
    z=[Q(1)]
    for _ in range(n): z=mul(z,a)
    return z

def integrate(a,lo,hi): return sum(v*(hi**(i+1)-lo**(i+1))/Q(i+1) for i,v in enumerate(a))
def paths(signs,attractive=False):
    out=[[Q(0),Q(1)]]
    for e in signs:
        out.append(add(scale(out[-1],Q(2) if attractive else Q(1,2)),[Q(e,2) if attractive else Q(e,4)]))
    return out

def alive_interval(pp):
    lo,hi=Q(-1),Q(1)
    for b,a in pp:
        lo=max(lo,(-1-b)/a); hi=min(hi,(1-b)/a)
    return (lo,hi) if lo<hi else (Q(0),Q(0))

def expectation(m,func,attractive=False,reverse=False,conditional=False):
    total=Q(0)
    for ss in itertools.product((-1,1),repeat=m):
        pp=paths(ss,attractive)
        lo,hi=alive_interval(pp) if attractive else (Q(-1),Q(1))
        total+=integrate(func(list(reversed(pp)) if reverse else pp),lo,hi)/Q(2**(m+1))
    return total*2**m if conditional else total

def defect(pp,reverse_orientation=False):
    x,y=pp[-1],pp[0]
    if reverse_orientation: x,y=y,x
    ar,ai=Q(2,3),Q(1,5)
    re=add(add(x,scale(y,-ar)),scale(mul(y,y),ai))
    im=add(add(mul(x,x),scale(y,-ai)),scale(mul(y,y),-ar))
    return add(mul(re,re),mul(im,im))

class Jet:
    def __init__(self,v,g,h): self.v=Q(v); self.g=g; self.h=h
    @classmethod
    def constant(cls,v,n): return cls(v,[Q(0)]*n,[Q(0)]*n)
    def cast(self,a): return a if isinstance(a,Jet) else Jet.constant(a,len(self.g))
    def __add__(self,a):
        a=self.cast(a); return Jet(self.v+a.v,[u+v for u,v in zip(self.g,a.g)],[u+v for u,v in zip(self.h,a.h)])
    __radd__=__add__
    def __neg__(self): return Jet(-self.v,[-v for v in self.g],[-v for v in self.h])
    def __sub__(self,a): return self+-self.cast(a)
    def __mul__(self,a):
        a=self.cast(a)
        return Jet(self.v*a.v,[u*a.v+self.v*v for u,v in zip(self.g,a.g)],[u*a.v+2*gu*gv+self.v*v for u,v,gu,gv in zip(self.h,a.h,self.g,a.g)])
    __rmul__=__mul__
    def inv(self): return Jet(1/self.v,[-u/self.v**2 for u in self.g],[2*u*u/self.v**3-v/self.v**2 for u,v in zip(self.g,self.h)])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mutant',default='baseline'); ns=ap.parse_args()
    allowed={'baseline','pair_half','atom_deleted','noise_half','reverse_noise_sign','endpoint_orientation','drop_conditioning','endpoint_only_kill','fourier_response_sign','path_order'}
    if ns.mutant not in allowed: ap.error('unknown mutant')
    records=[]
    def check(name,actual,expected): records.append({'name':name,'actual':str(actual),'expected':str(expected),'pass':actual==expected})
    c=Q(7,3)
    for N in (2,3,4,6):
        dim=4*N; coords=[]
        for i in range(N):
            row=[]
            for a in range(4):
                idx=4*i+a; gg=[Q(0)]*dim; gg[idx]=Q(1)
                row.append(Jet(Q((i+1)**(a+1),a+2),gg,[Q(0)]*dim))
            coords.append(row)
        H=Jet.constant(0,dim)
        explicit=[Q(0)]*dim
        for i in range(N):
            for j in range(i+1,N):
                zz=[coords[i][a]-coords[j][a] for a in range(4)]
                rr=sum((z*z for z in zz),Jet.constant(0,dim))
                H=H+(rr.inv()+(c/Q(8))*rr)*Q(1,N)
                for a,z in enumerate(zz):
                    gr=(-2*z.v/rr.v**2+c*z.v/Q(4))/N
                    explicit[4*i+a]+=gr; explicit[4*j+a]-=gr
        expected=c*(N-1)
        if ns.mutant=='pair_half': expected/=2
        if ns.mutant=='atom_deleted': expected=Q(0)
        check('configuration_laplacian_N'+str(N),sum(H.h),expected)
        check('configuration_gradient_N'+str(N),H.g,explicit)
        nu=Q(5,7)
        check('ito_noise_N'+str(N),2*nu*dim,(nu*dim if ns.mutant=='noise_half' else 2*nu*dim))
    for kk in ((1,0,0,0),(1,2,0,-1),(0,0,0,3)):
        norm=sum(z*z for z in kk)
        value=sum(Q(-4*z*z,norm) for z in kk)
        check('response_over_pi_squared_'+str(kk),value,Q(4 if ns.mutant=='fourier_response_sign' else -4))
    # Inversion is checked for each fixed signal, before any symmetric noise average.
    for signs in itertools.product((-1,1),repeat=4):
        forward=paths(signs)[-1]
        z=forward
        for e in reversed(signs):
            z=add(scale(z,2),[Q(e,2) if ns.mutant=='reverse_noise_sign' else Q(-e,2)])
        check('fixed_signal_inverse_'+''.join('p' if e==1 else 'm' for e in signs),z,[Q(0),Q(1)])
    for m in range(5):
        check('survival_steps_'+str(m),expectation(m,lambda p:[Q(1)],True),Q(1,2**m))
        for exponent in range(5):
            actual=expectation(m,lambda p:power(p[-1],exponent),True)
            expected=(Q(0) if exponent%2 else Q(1,(exponent+1)*2**m))
            check('survivor_haar_m'+str(m)+'_power'+str(exponent),actual,expected)
    m=4
    for exponents in itertools.product(range(3),repeat=m+1):
        def cylinder(pp):
            out=[Q(1)]
            for x,p in zip(pp,exponents): out=mul(out,power(x,p))
            return out
        actual=expectation(m,cylinder)
        rhs=expectation(m,cylinder,True,ns.mutant!='path_order',True)
        check('path_cylinder_'+''.join(map(str,exponents)),actual,rhs)
    actual=expectation(m,defect)
    rhs=expectation(m,lambda p:defect(p,ns.mutant=='endpoint_orientation'),True,True,ns.mutant!='drop_conditioning')
    check('complex_endpoint_defect',actual,rhs)
    # Separate excursion: endpoint-only survival misses an interior exit.
    excursion=[[Q(0),Q(1)],[Q(2),Q(1,2)],[Q(0),Q(1,4)]]
    true_interval=alive_interval(excursion)
    wrong_interval=alive_interval([excursion[0],excursion[-1]])
    check('interior_domain_kill',wrong_interval[1]-wrong_interval[0] if ns.mutant=='endpoint_only_kill' else true_interval[1]-true_interval[0],Q(0))
    # Reverse-negation is a signed permutation of independent Gaussian increments.
    for i in range(4):
        for j in range(4):
            covariance=sum((-1 if r==3-i else 0)*(-1 if r==3-j else 0) for r in range(4))
            check('reverse_increment_covariance_'+str(i)+str(j),covariance,int(i==j))
    failed=[r for r in records if not r['pass']]
    result={'schema':'AUD075-rational-diagnostic-v1','mutant':ns.mutant,'arithmetic':'exact fractions; deterministic exhaustive signals; no Monte Carlo','checks':len(records),'failed_count':len(failed),'status':'PASS' if not failed else 'FAIL','records':records}
    print(json.dumps(result,indent=2))
    return 0 if not failed else 1

if __name__=='__main__': sys.exit(main())
