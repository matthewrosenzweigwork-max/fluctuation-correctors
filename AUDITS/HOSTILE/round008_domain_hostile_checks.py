#!/usr/bin/env python3
"""Independent TASK054 diagnostics. Standard library, exact rational arithmetic.

D0 e^(ik theta)=k e^(ik theta), so the physical angle derivative is i D0.
K0=-D0 g and actual K=i K0. Products K grad, the Laplacian, and
quadratic variations therefore carry the explicit minus signs below.
Embedding theta=2*pi*x in one torus coordinate restores a common (2*pi)^2
in all generator/bracket expressions. No singular analytic passage is tested.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
CHECKS = {}
MUTATIONS = {}

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS[name] = True

class Poly:
    def __init__(self, n, terms=None):
        self.n = n
        self.terms = {tuple(k): Q(v) for k,v in (terms or {}).items() if v}
        assert all(len(k)==n for k in self.terms)
    @staticmethod
    def constant(n, c):
        return Poly(n, {(0,)*n: c})
    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly.constant(self.n, other)
        assert self.n == other.n
        out = dict(self.terms)
        for k,v in other.terms.items():
            out[k] = out.get(k,Q(0))+v
        return Poly(self.n,out)
    __radd__ = __add__
    def __neg__(self):
        return Poly(self.n,{k:-v for k,v in self.terms.items()})
    def __sub__(self, other):
        return self + (-other)
    def __mul__(self, other):
        if not isinstance(other, Poly):
            return Poly(self.n,{k:v*Q(other) for k,v in self.terms.items()})
        assert self.n == other.n
        out = {}
        for k,v in self.terms.items():
            for l,w in other.terms.items():
                m = tuple(a+b for a,b in zip(k,l))
                out[m] = out.get(m,Q(0))+v*w
        return Poly(self.n,out)
    __rmul__ = __mul__
    def __truediv__(self, q):
        return self * (1/Q(q))
    def __eq__(self, other):
        return isinstance(other, Poly) and self.n==other.n and self.terms==other.terms
    def d0(self, j):
        return Poly(self.n,{k:v*k[j] for k,v in self.terms.items()})
    def lap(self):
        return Poly(self.n,{k:-v*sum(a*a for a in k) for k,v in self.terms.items()})
    def integrate(self, slots):
        slots = set(slots)
        out = {}
        for k,v in self.terms.items():
            if all(k[j]==0 for j in slots):
                l = tuple(a for j,a in enumerate(k) if j not in slots)
                out[l] = out.get(l,Q(0))+v
        return Poly(self.n-len(slots),out)
    def place(self, n, labels):
        assert len(labels)==self.n
        out = {}
        for k,v in self.terms.items():
            l = [0]*n
            for a,j in zip(k,labels):
                l[j] += a
            l = tuple(l)
            out[l] = out.get(l,Q(0))+v
        return Poly(n,out)
    def pair_exchange(self):
        assert self.n==2
        return self.place(2,[1,0])
    def real_conjugate(self):
        return Poly(self.n,{tuple(-a for a in k):v for k,v in self.terms.items()})

def cosine(freq):
    return Poly(len(freq),{tuple(freq):Q(1,2), tuple(-a for a in freq):Q(1,2)})

def symmetric(p):
    return (p+p.pair_exchange())/2

def rel(p,n,i,j):
    assert p.n==1
    out={}
    for (a,),v in p.terms.items():
        k=[0]*n
        k[i]+=a
        k[j]-=a
        out[tuple(k)]=out.get(tuple(k),Q(0))+v
    return Poly(n,out)

def pair_stat(phi,N):
    q=phi.integrate([1])
    r=q.integrate([0])
    out=Poly(N)
    for i in range(N):
        for j in range(N):
            if i!=j:
                out += phi.place(N,[i,j])/(2*N*N)
        out -= q.place(N,[i])/N
    return out+r.place(N,[])/2

def deleted_subset(phi,N):
    """Literal definition for every slot subset, independent of contraction formulas."""
    out=Poly(N)
    k=phi.n
    for m in range(k+1):
        for chosen in combinations(range(k),m):
            remaining=[j for j in range(k) if j not in chosen]
            kernel=phi.integrate(remaining)
            for labels in permutations(range(N),m):
                out += kernel.place(N,labels)*Q((-1)**(k-m),N**m)
    return out

def rx_gradient(phi,k0,slot):
    # Integrated coordinate is slot 2; the two output slots remain 0,1.
    labels=[0,1]
    labels[slot]=2
    integrand = -rel(k0,3,2,slot)*phi.d0(slot).place(3,labels)
    return integrand.integrate([2])

def response_multiplier(phi,g,slot):
    return Poly(2,{k:-v*k[slot]**2*g.terms.get((k[slot],),Q(0))
                   for k,v in phi.terms.items()})

def internal(phi,k0):
    return -rel(k0,2,0,1)*(phi.d0(0)-phi.d0(1))

def upward(phi,k0):
    raw=-rel(k0,3,0,2)*phi.d0(0).place(3,[0,1])
    return sum((raw.place(3,p) for p in permutations(range(3))),Poly(3))/6

def particle_generator(p,k0,N,nu):
    out=p.lap()*nu
    for i in range(N):
        drift=sum((rel(k0,N,i,j) for j in range(N) if j!=i),Poly(N))/N
        out -= drift*p.d0(i)
    return out

def d2_sum(phi,N):
    return sum((phi.place(N,[i,j]) for i in range(N) for j in range(N) if i!=j),Poly(N))/(N*N)

def rho_one(f,N):
    return sum((f.place(N,[i]) for i in range(N)),Poly(N))/N-f.integrate([0]).place(N,[])

def detect(name, true, false):
    if true != false:
        MUTATIONS[name]=MUTATIONS.get(name,0)+1

# Only the sealed eighteen-file dossier is opened as mathematical input.
manifest=ROOT/'AUDITS/HOSTILE/ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt'
input_hashes={}
lines=manifest.read_text().splitlines()
check('input_count_18', len(lines)==18)
for line in lines:
    expected,relative=line.split('  ',1)
    path=Path(relative)
    check('safe_path_'+relative,not path.is_absolute() and '..' not in path.parts)
    actual=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
    check('sha256_'+relative,actual==expected)
    input_hashes[relative]=actual

kernels={
    'constant':Poly.constant(2,1),
    'relative':cosine((1,-1)),
    'sum':cosine((1,1)),
    'additive':cosine((1,0))+cosine((0,1)),
    'separable':cosine((1,0))*cosine((0,2))+cosine((2,0))*cosine((0,1)),
    'mixed':symmetric(cosine((2,-1)))+Q(2,3)*cosine((1,1))+Q(3,5),
}
forces={
    'zero':Poly(1),
    'one_mode':cosine((1,)),
    'two_modes':cosine((1,))+Q(2,5)*cosine((2,)),
    'coulomb_modes':Poly(1,{(k,):Q(3,k*k) for k in range(-4,5) if k}),
}
nu_values=[Q(0),Q(2,7)]
for name,phi in kernels.items():
    check('symmetry_'+name,phi==phi.pair_exchange())
    check('real_'+name,phi==phi.real_conjugate())

for f_name,g in forces.items():
    k0=-g.d0(0)
    for p_name,phi in kernels.items():
        prefix=f'{f_name}/{p_name}'
        rx=rx_gradient(phi,k0,0)
        ry=rx_gradient(phi,k0,1)
        R=rx+ry
        check(prefix+'/response_x',rx==response_multiplier(phi,g,0))
        check(prefix+'/response_y',ry==response_multiplier(phi,g,1))
        B=internal(phi,k0)
        C=upward(phi,k0)
        q=phi.integrate([1])
        a=q.d0(0)
        # Physical A_a and v carry i^2=-1.
        Aa=-rel(k0,2,0,1)*(a.place(2,[0])-a.place(2,[1]))
        v=(-rel(k0,2,1,0)*a.place(2,[1])).integrate([1])
        check(prefix+'/C1',C.integrate([2])==(Aa+R)/6)
        check(prefix+'/C2',C.integrate([1,2])==v/3)
        check(prefix+'/C0',C.integrate([0,1,2])==Poly(0))
        check(prefix+'/R_mu',R.integrate([1])==v)
        check(prefix+'/R_mean',R.integrate([0,1])==Poly(0))
        if f_name=='coulomb_modes':
            check(prefix+'/coulomb_atom_x',rx==-3*(phi-phi.integrate([0]).place(2,[1])) )
            check(prefix+'/coulomb_atom_y',ry==-3*(phi-phi.integrate([1]).place(2,[0])) )
        for N in (2,3):
            P=pair_stat(phi,N)
            U3=deleted_subset(C,N)
            lower=rho_one(B.integrate([1]),N)/N
            scalar=B.integrate([0,1]).place(N,[])/(2*N)
            check(prefix+f'/N{N}/U2_literal',2*P==deleted_subset(phi,N))
            check(prefix+f'/N{N}/B_recenter',d2_sum(B,N)-2*pair_stat(B,N)==2*rho_one(B.integrate([1]),N)+B.integrate([0,1]).place(N,[]))
            gradients=[]
            for i in range(N):
                gi=sum((phi.d0(0).place(N,[i,j]) for j in range(N) if j!=i),Poly(N))/(N*N)-a.place(N,[i])/N
                check(prefix+f'/N{N}/gradient{i}',P.d0(i)==gi)
                gradients.append(gi)
            for nu in nu_values:
                label=prefix+f'/N{N}/nu{nu}'
                LP=particle_generator(P,k0,N,nu)
                rhs=pair_stat(phi.lap()*nu+R,N)+U3+d2_sum(B,N)/(2*N)
                check(label+'/raw_identity',LP==rhs)
                # Nonconstant f is a possible terminal test; this check is instantaneous algebra.
                f=cosine((1,))+Q(1,3)*cosine((2,))
                J=-rel(k0,2,0,1)*(f.d0(0).place(2,[0])-f.d0(0).place(2,[1]))
                dotphi=-(phi.lap()*nu+R+B/N+J)
                actual=LP+pair_stat(dotphi,N)
                target=-pair_stat(J,N)+U3+lower+scalar
                check(label+'/corrector_identity',actual==target)
                bracket=-2*nu*sum((gi*gi for gi in gradients),Poly(N))
                gamma=particle_generator(P*P,k0,N,nu)-2*P*LP
                check(label+'/bracket_product_rule',gamma==bracket)
                # Explicit all-distinct/repeated-label/background expansion of the bracket.
                expanded=Poly(N)
                for i in range(N):
                    for j in range(N):
                        if j==i:
                            continue
                        pij=phi.d0(0).place(N,[i,j])
                        expanded += pij*pij/Q(N**4)
                        expanded -= 2*pij*a.place(N,[i])/Q(N**3)
                        for k in range(N):
                            if k!=i and k!=j:
                                expanded += pij*phi.d0(0).place(N,[i,k])/Q(N**4)
                    expanded += a.place(N,[i])*a.place(N,[i])/Q(N*N)
                check(label+'/bracket_deleted_expansion',bracket==-2*nu*expanded)
                if nu==0:
                    check(label+'/zero_noise_bracket',bracket==Poly(N))
                detect('omit_upward',actual,target-U3)
                detect('omit_lower',actual,target-lower)
                detect('omit_scalar',actual,target-scalar)
                detect('omit_one_response_slot',LP,rhs-pair_stat(ry,N))
                detect('wrong_internal_half',LP,rhs-d2_sum(B,N)/(4*N))
                if N==2:
                    detect('N2_upward_incorrectly_empty',actual,target-U3)
                detect('omit_background_gradient',bracket,
                       -2*nu*sum(((gi+a.place(N,[i])/N)*(gi+a.place(N,[i])/N)
                                  for i,gi in enumerate(gradients)),Poly(N)))
    const=Poly.constant(1,7)
    zeroJ=-rel(k0,2,0,1)*(const.d0(0).place(2,[0])-const.d0(0).place(2,[1]))
    check(f_name+'/constant_test_J_zero',zeroJ==Poly(2))

for mutation in ('omit_upward','omit_lower','omit_scalar','omit_one_response_slot',
                 'wrong_internal_half','N2_upward_incorrectly_empty','omit_background_gradient'):
    check('sensitivity/'+mutation,MUTATIONS.get(mutation,0)>0)

# Second-order automatic differentiation at r=1 (all coefficients rational).
class Jet:
    def __init__(self,v,d,h):
        self.v=Q(v); self.d=tuple(map(Q,d)); self.h=tuple(tuple(map(Q,row)) for row in h)
        self.n=len(self.d)
    @staticmethod
    def const(v,n):
        return Jet(v,[0]*n,[[0]*n for _ in range(n)])
    @staticmethod
    def var(v,n,i):
        out=Jet.const(v,n)
        ds=[Q(0)]*n; ds[i]=Q(1)
        return Jet(v,ds,out.h)
    def __add__(self,b):
        if not isinstance(b,Jet): b=Jet.const(b,self.n)
        return Jet(self.v+b.v,[a+c for a,c in zip(self.d,b.d)],
                   [[self.h[i][j]+b.h[i][j] for j in range(self.n)] for i in range(self.n)])
    __radd__=__add__
    def __neg__(self): return self*(-1)
    def __sub__(self,b): return self+(-b)
    def __mul__(self,b):
        if not isinstance(b,Jet): b=Jet.const(b,self.n)
        n=self.n
        return Jet(self.v*b.v,[self.d[i]*b.v+self.v*b.d[i] for i in range(n)],
                   [[self.h[i][j]*b.v+self.d[i]*b.d[j]+self.d[j]*b.d[i]+self.v*b.h[i][j]
                     for j in range(n)] for i in range(n)])
    __rmul__=__mul__
    def pow_at_one(self,p):
        p=Q(p); assert self.v==1
        return Jet(1,[p*a for a in self.d],
                   [[p*self.h[i][j]+p*(p-1)*self.d[i]*self.d[j] for j in range(self.n)]
                    for i in range(self.n)])

for d in range(3,9):
    n=2*d
    z=[Jet.var(int(i==0),n,i)-Jet.var(0,n,d+i) for i in range(d)]
    rr=sum((v*v for v in z),Jet.const(0,n))
    for s in (Q(d-2,4),Q(d-2,2),Q(d-2)):
        K=[s*v*rr.pow_at_one(-(s+2)/2) for v in z]
        for N in (2,3):
            F=[k*Q(1,N) for k in K]+[-k*Q(1,N) for k in K]
            a=2*s/N
            prefix=f'jet/d{d}/s{s}/N{N}'
            for j in range(d):
                direction=[Q(0)]*n
                direction[j]=1;direction[d+j]=-1
                expected=-(s+1)*a if j==0 else a
                image=[sum(F[i].d[k]*direction[k] for k in range(n)) for i in range(n)]
                check(prefix+f'/relative_eigen{j}',image==[expected*v for v in direction])
                center=[Q(0)]*n; center[j]=1;center[d+j]=1
                check(prefix+f'/center_eigen{j}',all(sum(F[i].d[k]*center[k] for k in range(n))==0 for i in range(n)))
            for m in (Q(0),Q(1),Q(2),Q(7)):
                alpha=m+Q(1,2)
                weight=rr.pow_at_one(-alpha/2)
                for nu in nu_values:
                    actual=sum(F[i].v*weight.d[i] for i in range(n))+nu*sum(weight.h[i][i] for i in range(n))+m*a
                    expected=-a*(alpha-m)+2*nu*alpha*(alpha+2-d)
                    check(prefix+f'/barrier/m{m}/nu{nu}',actual==expected)
            for frac in (Q(1,4),Q(1,2),Q(3,4)):
                q1=1+(Q(d,2)-1)*frac
                q2=(q1+1+d)/2
                inequalities=(q1>1,2*q1<d,q1<d-1,q2>2,q2<d,
                              s+1<d,s<d,s+3+q1<q2+s+2)
                check(prefix+f'/weights/{frac}',all(inequalities))
            # The exact Coulomb punctured divergence is zero; its atom is separate.
            divergence=sum(K[i].d[i] for i in range(d))
            check(prefix+'/principal_divergence',divergence==s*(d-2-s))
            if s==d-2:
                check(prefix+'/coulomb_punctured_zero',divergence==0)

# Gamma values at half integers represented as rational * pi**rational.
def gamma_half(n):
    assert n>=1
    if n%2==0:
        c=Q(1)
        for j in range(1,n//2): c*=j
        return c,Q(0)
    c=Q(1)
    for j in range((n-1)//2): c*=Q(2*j+1,2)
    return c,Q(1,2)

def riesz_constant(d,s):
    a,pa=gamma_half(d-s); b,pb=gamma_half(s)
    return a/b,Q(s)-Q(d,2)+pa-pb

for d in range(3,12):
    s=d-2
    c,pc=riesz_constant(d,s)
    gd,pg=gamma_half(d)
    check(f'normalization/coulomb/d{d}',(4*c,pc+2)==(Q(2*(d-2))/gd,Q(d,2)-pg))
    for s in range(1,d-2):
        c,pc=riesz_constant(d,s); cp,pp=riesz_constant(d,s+2)
        check(f'normalization/subcoulomb/d{d}/s{s}',(4*c/cp,pc+2-pp)==(Q(s*(d-2-s)),Q(0)))

# Zero-noise radial diagnostic: r^p=r0^p+a*p*t, with r0=1,r=2.
# Differentiation with respect to time is evaluated exactly, not finite differences.
for N in (2,3):
    for s in range(1,7):
        p=s+2; a=Q(2*s,N); r=Q(2); r0=Q(1)
        t=(r**p-r0**p)/(a*p)
        rdot=a*r**(1-p)
        radial_initial=(r0/r)**(p-1)
        transverse_initial=r/r0
        occupation=Q(N,4)*(r*r-r0*r0)
        d_occupation=Q(N,2)*r*rdot
        check(f'zero_noise/N{N}/s{s}/source_potential',d_occupation==s*r**(-s))
        check(f'zero_noise/N{N}/s{s}/separation',r**p==r0**p+a*p*t and t>0)
        check(f'zero_noise/N{N}/s{s}/variations',radial_initial<1<transverse_initial)
        check(f'zero_noise/N{N}/s{s}/positive_potential',occupation>0)

result={
    'audit':'TASK054 independent exact diagnostics',
    'status':'PASS',
    'assertions_passed':len(CHECKS),
    'arithmetic':'fractions.Fraction; exact coefficient comparison; no tolerance or randomness',
    'force_models':list(forces),
    'pair_kernels':list(kernels),
    'particle_numbers':[2,3],
    'noise_values':[str(v) for v in nu_values],
    'mutation_witness_counts':MUTATIONS,
    'input_sha256':input_hashes,
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'limitations':[
        'Smooth one-coordinate Fourier polynomial identities test algebra only.',
        'Coulomb-mode response checks apply on the tested finite Fourier support; the genuine atom is justified analytically.',
        'Jet and radial checks concern local principal differential expressions, not the full periodic law.',
        'Common completeness, uniform integrability, weak derivatives, and singular Ito passage require the written audit.'
    ],
    'checks':list(CHECKS),
}
output=ROOT/'AUDITS/HOSTILE/ROUND_008_DOMAIN_CHECK_RESULTS.json'
if '--stdout' in sys.argv:
    print(json.dumps(result,indent=2,sort_keys=True))
else:
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('status','assertions_passed','mutation_witness_counts','checker_sha256')},indent=2,sort_keys=True))
