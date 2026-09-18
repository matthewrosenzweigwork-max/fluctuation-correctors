#!/usr/bin/env python3
"""Fresh AUD061 exact coefficient diagnostics; no analytic certification."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse
import hashlib
import json

class Q:
    __slots__ = ("r", "i")
    def __init__(self, r=0, i=0):
        if isinstance(r, Q):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = F(r), F(i)
    def __add__(self, other):
        other = Q(other)
        return Q(self.r + other.r, self.i + other.i)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.r, -self.i)
    def __sub__(self, other):
        return self + -Q(other)
    def __rsub__(self, other):
        return Q(other) + -self
    def __mul__(self, other):
        other = Q(other)
        return Q(self.r*other.r-self.i*other.i,
                 self.r*other.i+self.i*other.r)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = Q(other)
        den = other.r**2 + other.i**2
        return Q((self.r*other.r+self.i*other.i)/den,
                 (self.i*other.r-self.r*other.i)/den)
    def __eq__(self, other):
        other = Q(other)
        return self.r == other.r and self.i == other.i
    def __bool__(self):
        return bool(self.r or self.i)
    def encode(self):
        return {"real": str(self.r), "imag": str(self.i)}

def clean(poly):
    return {k: Q(v) for k,v in poly.items() if Q(v)}
def add(*polys):
    out = {}
    for p in polys:
        for k,v in p.items():
            out[k] = out.get(k,Q()) + v
    return clean(out)
def scale(poly, scalar):
    return clean({k:v*scalar for k,v in poly.items()})
def sub(a,b):
    return add(a,scale(b,-1))
def mul(a,b):
    out = {}
    for k,v in a.items():
        for l,w in b.items():
            m = tuple(x+y for x,y in zip(k,l))
            out[m] = out.get(m,Q()) + v*w
    return clean(out)
def const(c,n):
    return clean({(0,)*n: Q(c)})
def cosine(k):
    return clean({tuple(k): Q(F(1,2)),
                  tuple(-x for x in k): Q(F(1,2))})
def sine(k):
    return clean({tuple(k): Q(0,F(-1,2)),
                  tuple(-x for x in k): Q(0,F(1,2))})
def diff(poly, slot):
    return clean({k:v*Q(0,k[slot]) for k,v in poly.items()})
def lap(poly,n):
    return add(*(diff(diff(poly,i),i) for i in range(n)))
def embed(poly, mapping, n):
    """None means an independently integrated Haar slot; repeated maps combine."""
    out = {}
    for k,v in poly.items():
        if any(j is None and a != 0 for a,j in zip(k,mapping)):
            continue
        m=[0]*n
        for a,j in zip(k,mapping):
            if j is not None:
                m[j]+=a
        m=tuple(m)
        out[m]=out.get(m,Q())+v
    return clean(out)
def haar(poly,n):
    return poly.get((0,)*n,Q())
def norm2_real(poly,n):
    return haar(mul(poly,poly),n)
def U(poly,k,n):
    out={}
    for mask in range(1<<k):
        slots=[j for j in range(k) if mask & (1<<j)]
        r=len(slots)
        factor=F((-1)**(k-r),n**r)
        for labels in permutations(range(n),r):
            mapping=[None]*k
            for j,label in zip(slots,labels):
                mapping[j]=label
            out=add(out,scale(embed(poly,mapping,n),factor))
    return out
def P(poly,n):
    return scale(U(poly,2,n),F(1,2))
def raw(poly,k,n):
    return scale(add(*(embed(poly,labels,n)
                       for labels in permutations(range(n),k))),F(1,n**k))
def response(phi,K,slot):
    if slot == 0:
        integrand=mul(embed(K,(2,0),3),
                      embed(diff(phi,0),(2,1),3))
    else:
        integrand=mul(embed(K,(2,1),3),
                      embed(diff(phi,1),(0,2),3))
    return embed(integrand,(0,1,None),2)
def cubic(phi,K):
    base=mul(embed(K,(0,2),3),embed(diff(phi,0),(0,1),3))
    return scale(add(*(embed(base,perm,3)
                       for perm in permutations(range(3)))),F(1,6))
def generator(obs,n,K,nu):
    out=scale(lap(obs,n),nu)
    for i in range(n):
        field=scale(add(*(embed(K,(i,j),n) for j in range(n) if i!=j)),F(1,n))
        out=add(out,mul(field,diff(obs,i)))
    return out

counts={}
mutations={}
def check(condition, category, detail=""):
    counts[category]=counts.get(category,0)+1
    if not condition:
        raise AssertionError(category+": "+detail)
def eq(a,b,category,detail=""):
    check(not sub(a,b),category,detail)
def witness(name,difference,case):
    if difference and name not in mutations:
        freq=min(difference)
        mutations[name]={"case":case,"frequency":list(freq),
                         "nonzero_difference":difference[freq].encode()}
def scalar_witness(name,difference,case):
    witness(name,const(difference,0),case)

def run():
    c1=cosine((1,0)); c2=cosine((0,1))
    s1=sine((1,0)); s2=sine((0,1))
    probes={
        "constant":const(3,2),
        "additive":add(c1,c2,scale(add(s1,s2),F(2,3))),
        "relative":add(cosine((1,-1)),scale(cosine((2,-2)),F(1,3))),
        "separable":add(mul(c1,c2),scale(mul(s1,s2),F(1,4))),
        "mixed":add(cosine((2,1)),cosine((1,2)),
                    scale(add(sine((1,-2)),sine((-2,1))),F(1,3))),
    }
    probes["dense"]=add(*probes.values())
    potential=add(scale(cosine((1,-1)),F(1,2)),
                  scale(cosine((2,-2)),F(1,7)))
    forces={"zero":{},"two_mode":scale(diff(potential,0),-1)}
    for name,phi in probes.items():
        eq(phi,embed(phi,(1,0),2),"pair_symmetry",name)
        row=embed(phi,(0,None),1)
        c=haar(phi,2)
        u=sub(row,const(c,1))
        deg=sub(phi,add(const(c,2),embed(u,(0,),2),embed(u,(1,),2)))
        eq(embed(deg,(0,None),1),{},"degenerate_slices",name)
        eq(embed(deg,(None,0),1),{},"degenerate_slices",name)
        for n in (2,3,4):
            obs=P(phi,n)
            actual_second=haar(mul(obs,obs),n)
            exact_second=(Q(F(n-1,2*n**3))*norm2_real(deg,2)
                          +Q(F(1,n**3))*norm2_real(u,1)+c*c/F(4*n*n))
            check(actual_second==exact_second,"iid_endpoint",f"{name},N={n}")
            check(actual_second.r>=0 and actual_second.i==0,"iid_nonnegative")
            bound=Q(F(n-1,2*n**3))*norm2_real(phi,2)
            check(actual_second.r<=bound.r,"iid_endpoint_bound")
            scalar_witness("omit_initial_bias",actual_second-
                           (exact_second-c*c/F(4*n*n)),f"{name},N={n}")
            scalar_witness("omit_initial_projection",actual_second-
                           (exact_second-norm2_real(u,1)/n**3),f"{name},N={n}")
            eq(obs,add(scale(raw(deg,2,n),F(1,2)),
                        scale(add(*(embed(u,(i,),n) for i in range(n))),F(-1,n*n)),
                        const(-c/(2*n),n)),"iid_decomposition")
            for force_name,K in forces.items():
                Rx=response(phi,K,0); Ry=response(phi,K,1)
                B=mul(K,sub(diff(phi,0),diff(phi,1)))
                C=cubic(phi,K)
                uc=U(C,3,n)
                g=embed(B,(0,None),1); scalar=haar(B,2)
                low=scale(U(g,1,n),F(1,n))
                zero=const(scalar/(2*n),n)
                G=diff(phi,0); bg=embed(G,(0,None),1)
                aa=mul(K,sub(embed(bg,(0,),2),embed(bg,(1,),2)))
                vv=embed(mul(embed(K,(1,0),2),embed(bg,(1,),2)),(0,None),1)
                eq(embed(C,(0,1,None),2),scale(add(aa,Rx,Ry),F(1,6)),
                   "all_cubic_first_backgrounds")
                eq(embed(C,(0,None,None),1),scale(vv,F(1,3)),
                   "all_cubic_second_backgrounds")
                check(haar(C,3)==0,"cubic_scalar")
                for i in range(n):
                    formula=add(scale(add(*(embed(G,(i,j),n)
                                           for j in range(n) if j!=i)),F(1,n*n)),
                                scale(embed(bg,(i,),n),F(-1,n)))
                    eq(diff(obs,i),formula,"particle_gradient")
                    witness("omit_gradient_background",
                            sub(diff(obs,i),add(formula,
                                scale(embed(bg,(i,),n),F(1,n)))),
                            f"{name},{force_name},N={n},i={i}")
                for nu in (F(0),F(2,3)):
                    case=f"{name},{force_name},N={n},nu={nu}"
                    operator=add(scale(lap(phi,2),nu),scale(B,F(1,n)),Rx,Ry)
                    rhs=add(P(operator,n),uc,low,zero)
                    direct=generator(obs,n,K,nu)
                    eq(direct,rhs,"whole_particle_identity",case)
                    variants={
                       "omit_response_x":sub(rhs,P(Rx,n)),
                       "omit_response_y":sub(rhs,P(Ry,n)),
                       "drop_all_cubic_backgrounds":add(sub(rhs,uc),raw(C,3,n)),
                       "symmetrization_sum_not_average":add(rhs,scale(uc,5)),
                       "internal_1_over_N_plus_1":add(rhs,scale(P(B,n),F(1,n+1)-F(1,n))),
                       "omit_centered_lower":sub(rhs,low),
                       "halve_centered_lower":sub(rhs,scale(low,F(1,2))),
                       "omit_scalar_lower":sub(rhs,zero),
                       "flip_scalar_lower":sub(rhs,scale(zero,2)),
                    }
                    for mut,wrong in variants.items():
                        witness(mut,sub(direct,wrong),case)
                    if n==2:
                        witness("drop_N2_cubic",sub(direct,sub(rhs,uc)),case)
                    wrong_obs=add(obs,scale(raw(phi,2,n),F(1,2*(n-1))))
                    witness("falling_factorial_pair_denominator",
                            sub(generator(wrong_obs,n,K,nu),rhs),case)
                    carré=sub(generator(mul(obs,obs),n,K,nu),
                               scale(mul(obs,direct),2))
                    expected=scale(add(*(mul(diff(obs,i),diff(obs,i))
                                         for i in range(n))),2*nu)
                    eq(carré,expected,"full_martingale_bracket",case)
                    witness("omit_noise_factor_two",
                            sub(carré,scale(expected,F(1,2))),case)
    for n in range(2,10):
        triple=add(const(2,3),cosine((1,0,-1)),
                   cosine((0,1,-1)),cosine((1,-1,0)))
        check(haar(U(triple,3,n),n)==haar(triple,3)*F(2,n*n),
              "literal_U3_iid_mean")
    admitted=0
    for d in range(3,31):
        for den in range(1,12):
            for numerator in range(1,(d-2)*den):
                s=F(numerator,den)
                if s*(s+2)>=2*d:
                    continue
                admitted+=1
                p=s+2; theta=1-s/d; a=s/p
                lo=max(F(1),s/2); hi=min(F(d,2),d-s-1,s+1); q=(lo+hi)/2
                kappa=(2*q-s)/(2*p)
                for condition in (lo<hi,1<q<F(d,2),q<s+1,q<d-s-1,
                                  q>s/2,s<F(d,2),3*s<2*d-2,kappa>0,
                                  s/d-F(1,2)<0,a-theta<0,
                                  F(2)/p-theta<0):
                    check(condition,"full_range")
                check(F(2)/p-theta==s*(p-d)/(d*p),"chi_exponent")
                check((s+1-q)/p-F(1,2)==-kappa,"lower_exponent")
                check(a-theta==(s*p-2*d)/(d*p),"noise_exponent")
    check(F(3)*(3+2)<2*8 and 3<8-2,"admitted_s_greater_than_two")
    check(F(4)*(4+2)==2*12,"excluded_noise_equality")
    check(F(1)==3-2,"excluded_coulomb")
    check(F(2,3)-(1-F(1,3))==0,"bounded_chi_critical_boundary")
    # Independent one-dimensional polynomial time integration on [0,1].
    def integ(coeff):
        return sum((F(c,i+1) for i,c in enumerate(coeff)),F(0))
    P0=F(2); PT=F(0); J=integ([2,3]); lower=integ([1,1]); increment=integ([4,2])
    Utime=integ([-2,-6])  # P'=1-6t; U=P'+J-lower-increment_derivative.
    check(PT-P0==-J+Utime+lower+increment,"integrated_fundamental_identity")
    check(Utime==-P0+J-lower-increment,"integrated_cubic_rearrangement")
    scalar_witness("flip_initial_endpoint_sign",Utime-(P0+J-lower-increment),"time polynomial")
    scalar_witness("flip_martingale_increment_sign",Utime-(-P0+J-lower+increment),"time polynomial")
    scalar_witness("flip_integrated_lower_sign",Utime-(-P0+J+lower-increment),"time polynomial")
    check(integ([1,-2])==0 and F(1,2)>0,"absolute_after_integral_distinction")
    required={
       "omit_initial_bias","omit_initial_projection","omit_gradient_background",
       "omit_response_x","omit_response_y","drop_all_cubic_backgrounds",
       "symmetrization_sum_not_average","internal_1_over_N_plus_1",
       "omit_centered_lower","halve_centered_lower","omit_scalar_lower",
       "flip_scalar_lower","drop_N2_cubic","falling_factorial_pair_denominator",
       "omit_noise_factor_two","flip_initial_endpoint_sign",
       "flip_martingale_increment_sign","flip_integrated_lower_sign",
    }
    check(set(mutations)==required,"nonvacuous_mutation_coverage")
    return {
       "status":"PASS",
       "audit":"AUD061/TASK094",
       "evidence":"Exact smooth algebra and rational parameter diagnostics only; not singular analytic proof.",
       "arithmetic":"fractions.Fraction Gaussian rationals; no floating point, tolerance, seed, or dependency",
       "fourier_convention":"Derivative=(2*pi)^(-1)*physical derivative; force=-that derivative of potential. Second-order equations divided by common (2*pi)^2.",
       "whole_identity_cases":counts["whole_particle_identity"],
       "assertion_count":sum(counts.values()),
       "categories":dict(sorted(counts.items())),
       "admitted_rational_parameter_cases":admitted,
       "mutation_count":len(mutations),
       "mutation_witnesses":dict(sorted(mutations.items())),
       "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    parser.add_argument("--check-existing",type=Path)
    args=parser.parse_args()
    result=run()
    encoded=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.check_existing:
        if json.loads(args.check_existing.read_text())!=result:
            raise SystemExit("FAIL: saved diagnostic result differs")
        print("PASS: exact diagnostic reproduces saved results")
    elif args.output:
        if args.output.exists():
            raise SystemExit("Refusing to overwrite an existing result")
        args.output.write_text(encoded)
        print(f"PASS: {result['assertion_count']} assertions; {result['whole_identity_cases']} whole identities; {result['mutation_count']} mutations")
    else:
        print(encoded,end="")
