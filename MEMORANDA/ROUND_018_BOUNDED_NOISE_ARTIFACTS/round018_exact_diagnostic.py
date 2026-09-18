#!/usr/bin/env python3
"""Fresh exact self-check for TASK-084; no prior checker or external package.

Finite Fourier kernels are coefficient diagnostics, not singular-model proofs.
D = physical derivative/(2*pi); restore (2*pi)^2 in generators and brackets.
All arithmetic is rational, Gaussian rational, or exact formal exp(-r).
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json

@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))
    def __add__(self, other):
        z = asq(other)
        return Q(self.re + z.re, self.im + z.im)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.re, -self.im)
    def __sub__(self, other):
        return self + (-asq(other))
    def __rsub__(self, other):
        return asq(other) + (-self)
    def __mul__(self, other):
        z = asq(other)
        return Q(self.re*z.re - self.im*z.im, self.re*z.im + self.im*z.re)
    __rmul__ = __mul__
    def __truediv__(self, other):
        z = asq(other)
        norm = z.re*z.re + z.im*z.im
        if not norm:
            raise ZeroDivisionError
        return self*z.conj()*Q(1/norm)
    def conj(self):
        return Q(self.re, -self.im)
    def __bool__(self):
        return bool(self.re or self.im)

def asq(x):
    return x if isinstance(x, Q) else Q(x)

I = Q(0, 1)
ZERO = Q()
COUNTS = Counter()
MUTATIONS = Counter()
WITNESSES = {}
def check(condition, category):
    COUNTS[category] += 1
    if not condition:
        raise AssertionError(category)

def reject(name, mutated_equal, witness):
    """Call only on a nondegenerate case: the wrong identity must fail."""
    check(not mutated_equal, "mutation_control")
    MUTATIONS[name] += 1
    WITNESSES.setdefault(name, witness)

def clean(p):
    return {k: asq(v) for k, v in p.items() if asq(v)}

def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, ZERO) + v
    return clean(out)

def scale(p, c):
    return clean({k: v*c for k, v in p.items()})

def mul(p, q):
    out = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(a+b for a, b in zip(k, ell))
            out[key] = out.get(key, ZERO) + v*w
    return clean(out)

def derivative(p, i):
    return clean({k: v*I*k[i] for k, v in p.items()})

def embed(h, i, n):
    out = {}
    for k, v in h.items():
        key = [0]*n
        key[i] = k
        out[tuple(key)] = asq(v)
    return clean(out)

def mean(p, n):
    return p.get((0,)*n, ZERO)

def one_diff(h):
    return {k: asq(v)*I*k for k, v in h.items() if k and asq(v)}

def one_mul(h, f):
    out = {}
    for k, v in h.items():
        for ell, w in f.items():
            out[k+ell] = out.get(k+ell, ZERO) + asq(v)*asq(w)
    return {k:v for k,v in out.items() if v}

def one_add(h, f, c=F(1)):
    out = {k:asq(v) for k,v in h.items()}
    for k,v in f.items():
        out[k] = out.get(k, ZERO) + asq(v)*c
    return {k:v for k,v in out.items() if v}

def empirical(h, n, centered=False):
    p = scale(add(*(embed(h, i, n) for i in range(n))), F(1,n))
    if centered:
        p = add(p, {(0,)*n: -asq(h.get(0, 0))})
    return p

def force(g, i, j, n):
    out = {}
    for k, v in g.items():
        if not k:
            continue
        key = [0]*n
        key[i], key[j] = k, -k
        out[tuple(key)] = -I*k*asq(v)
    return clean(out)

def full_generator(p, n, drifts, nu):
    out = {}
    for i in range(n):
        first = derivative(p, i)
        out = add(out, mul(drifts[i], first),
                  scale(derivative(first, i), nu))
    return out

def row_of_pair(p, n):
    out = {}
    for k,v in p.items():
        if all(k[j] == 0 for j in range(1,n)):
            out[k[0]] = out.get(k[0], ZERO) + v
    return {k:v for k,v in out.items() if v}

def response(h, g):
    return {k: -asq(v)*asq(g.get(k, 0))*k*k
            for k,v in h.items() if k and asq(g.get(k, 0)) and asq(v)}

def diffusion(h):
    return {k: -asq(v)*k*k for k,v in h.items() if k and asq(v)}

def pair_source(g, h, i, j, n):
    return mul(force(g,i,j,n),
               add(derivative(embed(h,i,n),i),
                   scale(derivative(embed(h,j,n),j),-1)))

def bfun(nu):
    return F(1) if nu <= 1 else 1/nu

def spectral_energies(h, g):
    interaction = ZERO
    kinetic = ZERO
    for k, v in h.items():
        if k:
            sq = asq(v)*asq(v).conj()
            kinetic += sq*k*k
            interaction += sq*k*k*asq(g.get(k,0))
    return interaction, kinetic

# Real Fourier tests include constants, sine/cosine mixtures and two modes.
tests = [
    {0:Q(3,0)},
    {1:Q(F(1,2)), -1:Q(F(1,2))},
    {0:Q(F(2,5)), 1:Q(F(1,3),F(1,4)), -1:Q(F(1,3),-F(1,4)),
     2:Q(F(1,7),F(1,9)), -2:Q(F(1,7),-F(1,9))}
]
kernels = [
    {1:Q(1), -1:Q(1)},
    {1:Q(F(2,3)), -1:Q(F(2,3)), 2:Q(F(1,5)), -2:Q(F(1,5))}
]
noises = [F(0), F(1,3), F(1), F(3)]

def run_particle_checks():
    for n in range(2,6):
        for gi,g in enumerate(kernels):
            drifts = [scale(add(*(force(g,i,j,n) for j in range(n) if j!=i)),F(1,n))
                      for i in range(n)]
            for hi,h in enumerate(tests):
                rh = response(h,g)
                j01 = pair_source(g,h,0,1,n)
                check(row_of_pair(j01,n) == rh, "literal_Haar_row_response")
                check(mean(j01,n) == ZERO, "literal_double_contraction")
                ordered = add(*(pair_source(g,h,i,j,n) for i in range(n)
                                for j in range(n) if i!=j))
                half_pair = scale(ordered,F(1,2*n*n))
                row = empirical(rh,n)
                pn = add(half_pair,scale(row,-1))
                uh = empirical(h,n,centered=True)
                en_d,en_a = spectral_energies(h,g)
                for nu in noises:
                    b = bfun(nu)
                    lh = full_generator(uh,n,drifts,nu)
                    rhs = add(empirical(one_add(rh,diffusion(h),nu),n),pn)
                    check(lh == rhs,"literal_first_order_generator")
                    if half_pair:
                        wrong = add(empirical(one_add(rh,diffusion(h),nu),n),
                                    scale(half_pair,2),scale(row,-1))
                        reject("missing_source_half",lh==wrong,{"N":n,"kernel":gi,"test":hi,"nu":str(nu)})
                    if row:
                        wrong = add(empirical(one_add(scale_one(rh,-1),diffusion(h),nu),n),pn)
                        reject("response_sign",lh==wrong,{"N":n,"kernel":gi,"test":hi,"nu":str(nu)})
                    variance_deriv = mean(full_generator(mul(uh,uh),n,drifts,nu),n)*n*b
                    check(variance_deriv == -2*b*F(n-1,n)*en_d,
                          "actual_initial_variance_derivative")
                    mixed_deriv = mean(mul(uh,lh),n)*n*b
                    check(mixed_deriv == -b*(F(n-1,n)*en_d+nu*en_a),
                          "actual_initial_time_covariance_derivative")
                    for pj,p in enumerate(tests):
                        up = empirical(p,n,centered=True)
                        lp = full_generator(up,n,drifts,nu)
                        gamma = add(full_generator(mul(uh,up),n,drifts,nu),
                                    scale(mul(uh,lp),-1),scale(mul(up,lh),-1))
                        gradproduct = one_mul(one_diff(h),one_diff(p))
                        expected = scale(empirical(gradproduct,n),2*nu*b)
                        scaled_gamma = scale(gamma,n*b)
                        check(scaled_gamma == expected,"literal_cross_carre_du_champ")
                        if expected:
                            witness={"N":n,"kernel":gi,"tests":[hi,pj],"nu":str(nu)}
                            reject("missing_Brownian_two",scaled_gamma==scale(expected,F(1,2)),witness)
                            reject("extra_bracket_inverse_N",scaled_gamma==scale(expected,F(1,n)),witness)
                            if hi!=pj:
                                reject("suppressed_cross_bracket",scaled_gamma=={},witness)
                # Initial iid replacement: no square-root-N loss.
                v = {k:v for k,v in h.items() if k}
                sum_v = add(*(embed(v,i,n) for i in range(n)))
                left = mean(mul(sum_v,sum_v),n)/n
                right = one_mul(v,v).get(0,ZERO)
                check(left==right,"iid_centered_triangular_variance")

def scale_one(h,c):
    return {k:asq(v)*c for k,v in h.items() if asq(v)*c}

# Formal exponential polynomials: {r: c} represents sum c exp(-r).
def ep_add(*ps):
    out={}
    for p in ps:
        for r,c in p.items():
            out[F(r)] = out.get(F(r),F(0))+F(c)
    return {r:c for r,c in out.items() if c}

def ep_scale(p,c):
    return {r:v*c for r,v in p.items() if v*c}

def modal_integral_cov(t,u,d,a,nu,b):
    l=d+nu*a
    initial={l*(t+u):b}
    # Direct backward-gradient time integral, integrated before summing.
    thermal=ep_add({l*abs(t-u):nu*b*a/l},
                   {l*(t+u):-nu*b*a/l})
    return ep_add(initial,thermal)

def modal_card_cov(t,u,d,a,nu,b):
    l=d+nu*a
    return ep_add({l*(t+u):b*d/l},{l*abs(t-u):b*nu*a/l})

def real_mode_weight(h,p,k):
    value=asq(h.get(k,0))*asq(p.get(k,0)).conj()
    return 2*value.re

def covariance(h,p,t,u,nu,method=modal_integral_cov):
    out={}
    b=bfun(nu)
    for k in [1,2]:
        # Positive exact modal parameters; not a claim of a singular approximation.
        d=F(3,2*k); a=F(k*k)
        out=ep_add(out,ep_scale(method(t,u,d,a,nu,b),real_mode_weight(h,p,k)))
    return out

def run_covariance_checks():
    times=[F(0),F(1,4),F(1),F(3,2)]
    for t,u,nu,d,a in product(times,times,noises,[F(2,3),F(3)],[F(1),F(4)]):
        b=bfun(nu); l=d+nu*a
        correct=modal_integral_cov(t,u,d,a,nu,b)
        check(correct==modal_card_cov(t,u,d,a,nu,b),"integrated_vs_card_modal_covariance")
        # Independent linear OU reconstruction: Cov(t,u)=exp(-L|t-u|) Var(min).
        small=min(t,u)
        variance=ep_add({2*l*small:b*d/l},{F(0):b*nu*a/l})
        propagated={r+l*abs(t-u):c for r,c in variance.items()}
        check(correct==propagated,"OU_conditional_covariance_reconstruction")
        if nu and min(t,u)>0:
            wrong={l*(t+u):b}
            reject("discarded_thermal_covariance",correct==wrong,{"t":str(t),"u":str(u),"nu":str(nu)})
        if t and u:
            wrong={l*abs(t-u):b}
            reject("time_sum_conflated_with_difference",correct==wrong,{"t":str(t),"u":str(u),"nu":str(nu)})
        if nu==0:
            check(correct=={d*(t+u):b},"zero_noise_covariance")
        if t==0 or u==0:
            check(correct=={l*(t+u):b},"zero_time_covariance")
    h=tests[1]; p=tests[2]; combined=one_add(h,p,F(2))
    constant=tests[0]
    for t,u,nu in product(times,times,noises):
        for f in [h,p,combined,constant]:
            check(covariance(combined,f,t,u,nu)==
                  ep_add(covariance(h,f,t,u,nu),ep_scale(covariance(p,f,t,u,nu),2)),
                  "same_time_linear_dependency")
            check(covariance(constant,f,t,u,nu)=={},"constant_test_null_row")
            check(covariance(h,f,t,u,nu)==covariance(f,h,u,t,nu),
                  "real_covariance_symmetry")
            check(covariance(h,f,t,u,nu)==
                  covariance(h,f,t,u,nu,modal_card_cov),
                  "full_real_test_covariance")

def convolve_series(a,b,order):
    return [sum((a[k]*b[n-k] for k in range(n+1)),F(0)) for n in range(order+1)]

def run_probability_checks():
    order=8  # Coefficient n is z^(2n), checked through degree sixteen.
    for eps in [F(1,2),F(1,3),F(1,7)]:
        weighted_mean_comp=[F(0)]*(order+1)
        for sign in [-1,1]:
            var=1+eps*sign
            char=[(-var)**n/(2**n*factorial(n)) for n in range(order+1)]
            comp=[var**n/(2**n*factorial(n)) for n in range(order+1)]
            correct=convolve_series(char,comp,order)
            for n,c in enumerate(correct):
                check(c==(F(1) if n==0 else F(0)),
                      "conditional_compensated_Gaussian_series")
            wrong=convolve_series(char,char,order)
            reject("wrong_exponential_compensator_sign",wrong==correct,
                   {"epsilon":str(eps),"initial_sign":sign})
            mean_comp=[F(1,2)**n/F(factorial(n)) for n in range(order+1)]
            wrong_mean=convolve_series(char,mean_comp,order)
            weighted_mean_comp=[c+F(sign,2)*z for c,z in zip(weighted_mean_comp,wrong_mean)]
        check(weighted_mean_comp[1]==-eps/2,
              "initial_weight_exposes_random_bracket")
        reject("random_bracket_replaced_by_mean",all(c==0 for c in weighted_mean_comp),
               {"epsilon":str(eps),"weighted_z2_coefficient":str(weighted_mean_comp[1])})
        # Orthogonality is exact but independence fails at the next moment.
        mixed_second=((1+eps)-(1-eps))/2
        check(mixed_second==eps,"dependent_martingale_mixed_second_moment")
        check(((1+eps)+(1-eps))/2==1,"dependent_martingale_variance")
    for n in range(2,9):
        # Exhaustive initial-sign enumeration is independent of the Taylor proof.
        fourth=sum((F(sum(signs)**4,n*n) for signs in product([-1,1],repeat=n)),F(0))/2**n
        check(fourth==3-F(2,n),"literal_iid_fourth_moment")
        eps=F(1,n)
        check((abs(eps)+abs(-eps))/2==eps,"bounded_bracket_flattening")
    # The two decay exponents are distinct; check all admitted rational examples.
    for d in range(3,10):
        for s in [F(1,4),F(1,2),F(1),F(3,2),F(2),F(5,2),F(3)]:
            if 0<s<=d-2 and s<F(d,2):
                check(s/d-F(1,2)<0,"source_decay_exponent")
                check(-(1-s/d)/2<0,"bracket_decay_exponent")
    for nu in [F(0),F(1,5),F(1),F(3,2),F(4)]:
        check(nu*bfun(nu)==min(nu,F(1)),"diffusivity_scale_normalization")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("round018_exact_diagnostic_results.json"))
    args=parser.parse_args()
    run_particle_checks()
    run_covariance_checks()
    run_probability_checks()
    required={
        "missing_source_half","response_sign","missing_Brownian_two",
        "extra_bracket_inverse_N","suppressed_cross_bracket",
        "discarded_thermal_covariance","time_sum_conflated_with_difference",
        "wrong_exponential_compensator_sign","random_bracket_replaced_by_mean"
    }
    check(required==set(MUTATIONS),"all_required_mutations_rejected")
    record={
        "status":"PASS",
        "evidence":"constructor exact diagnostics; not mathematical or independent certification",
        "assertions":sum(COUNTS.values()),
        "categories":dict(sorted(COUNTS.items())),
        "mutation_rejections":dict(sorted(MUTATIONS.items())),
        "mutation_first_witnesses":WITNESSES,
        "arithmetic":"fractions.Fraction; exact Gaussian rationals; formal exponential polynomials",
        "random_seed":None,
        "floating_point_tolerance":None,
        "external_packages":[],
        "prior_checkers_read":[],
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope":"literal smooth finite Fourier and conditional Gaussian diagnostics; singular proof is the memorandum",
        "normalization":"physical first derivative = 2*pi times implemented derivative; restore (2*pi)^2 in generators/brackets"
    }
    args.output.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":record["status"],"assertions":record["assertions"],
                      "categories":len(COUNTS),"mutation_families":len(MUTATIONS),
                      "output":str(args.output)},sort_keys=True))

if __name__=="__main__":
    main()
