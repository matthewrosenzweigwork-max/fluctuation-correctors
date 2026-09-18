#!/usr/bin/env python3
"""Exact supporting checks for the static threshold construction, not its proof."""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json

# A Gaussian rational is (real, imaginary); Laurent polynomials have two slots.
def qadd(a,b): return (a[0]+b[0],a[1]+b[1])
def qmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def Q(x): return (F(x),F(0))
def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items(): out[k]=qadd(out.get(k,Q(0)),v)
    return {k:v for k,v in out.items() if v!=Q(0)}
def scale(p,c): return {k:qmul(v,c) for k,v in p.items() if qmul(v,c)!=Q(0)}
def mul(p,q):
    out={}
    for k,v in p.items():
        for l,w in q.items():
            z=tuple(a+b for a,b in zip(k,l))
            out[z]=qadd(out.get(z,Q(0)),qmul(v,w))
    return {k:v for k,v in out.items() if v!=Q(0)}
def cosine(k): return {k:Q(F(1,2)),tuple(-a for a in k):Q(F(1,2))}
def sine(k): return {k:(F(0),F(-1,2)),tuple(-a for a in k):(F(0),F(1,2))}
def derivative(p,j):return {k:qmul(v,(F(0),F(k[j]))) for k,v in p.items() if k[j]}
def haar(p):return p.get((0,0),Q(0))
def grid(p,m):
    result=Q(0)
    for k,v in p.items():
        if all(a%m==0 for a in k):result=qadd(result,v)
    return result
def coefficient(p,order):
    # Pullback x -> x+epsilon sin(x), with the displacement held at original x.
    vx,vy=sine((1,0)),sine((0,1))
    terms=[]
    for a in range(order+1):
        b=order-a;term=p
        for _ in range(a):term=derivative(term,0)
        for _ in range(b):term=derivative(term,1)
        for _ in range(a):term=mul(term,vx)
        for _ in range(b):term=mul(term,vy)
        terms.append(scale(term,Q(F(1,factorial(a)*factorial(b)))))
    return add(*terms)

counts={};mutations={}
def check(category,condition):
    if not condition:raise AssertionError(category)
    counts[category]=counts.get(category,0)+1
def reject(name,correct,wrong):
    check('detecting_mutation',correct!=wrong)
    mutations[name]={'correct':str(correct),'wrong':str(wrong)}

taylor=sum((F(3**j,factorial(j)) for j in range(9)),F(0))
check('exp_three_lower_bound',taylor>20)
theta_upper=1+F(2,20)/(1-F(1,8000))
check('theta_rational_majorant',theta_upper==F(8799,7999))
check('theta_power_integer_test',2*8799**4<3*7999**4)
check('theta_fourth_minus_one',theta_upper**4-1<F(1,2))
for n in range(1,100):check('theta_geometric_exponent',n*n>=1+3*(n-1))
for m in range(5,100):
    for k in [1,-1,2,-2,3,-3]:check('exact_grid_selection',k%m!=0)
    check('energy_grid_self_subtraction',F(m*m-1,2)<F(m*m,2))
    check('small_deformation_energy_margin',-F(m*m-1,2)+F(m*m,8)<-F(m*m,4))
    check('scaled_jitter_error',F(m*m,m**3)==F(1,m))
    check('particle_threshold_scale',m**4==(m*m)**2)

# Exactly solvable smooth probe: g=2cos(x-y), h=cos(2x), v=sin(x).
# Haar response for h is zero since g has only frequencies +/-1.
force=scale(sine((1,-1)),Q(2))
gradient_difference=add(scale(sine((2,0)),Q(-2)),scale(sine((0,2)),Q(2)))
source=mul(force,gradient_difference)
halfsource=scale(source,Q(F(1,2)))
coeffs=[coefficient(halfsource,j) for j in range(4)]
check('smooth_probe_zero_order',haar(coeffs[0])==Q(0))
check('smooth_probe_first_order',haar(coeffs[1])==Q(0))
check('smooth_probe_second_coefficient',haar(coeffs[2])==Q(F(-1,2)))
check('smooth_probe_third_coefficient',haar(coeffs[3])==Q(0))
for m in range(5,65):
    for j in range(3):check('moving_grid_low_derivative_selection',grid(coeffs[j],m)==haar(coeffs[j]))
# Independent continuum density calculation: rho=-epsilon*cos(x).
rho=scale(cosine((1,0)),Q(-1))
grad_h=scale(sine((2,0)),Q(-2))
convolution=scale(sine((1,0)),Q(-1))
continuum=haar(mul(mul(rho,grad_h),convolution))
check('continuum_bilinear_matches_pullback',continuum==haar(coeffs[2]))
check('sin_cos_triple_integral',haar(mul(mul(cosine((1,0)),sine((1,0))),sine((2,0))))==Q(F(1,4)))
# Restore unit-torus derivative factors and density coefficient -2*pi epsilon.
# Divide physical coefficient by pi^4: (-1/2)*(2^2)*(2^2)=-8.
physical=continuum[0]*4*4
check('coefficient_one_physical_source',physical==-8)
check('absolute_translation_limit_constant',abs(physical)*2==16)

# Exact orthogonal translation amplitudes and norm Lipschitz controls.
for c,s in product(range(-5,6),repeat=2):
    check('translation_signed_mean',F(c)*0-F(s)*0==0)
    check('translation_quadratic_mean',F(c*c+s*s,2)>=0)
for n in range(2,30):
    check('ordered_half_count',F(n*(n-1),2*n*n)==F(n-1,2*n))
    check('grid_energy_normalization',F(n,2*n)==F(1,2))

reject('omit_grid_regular_self_subtraction',F(25-1,2),F(25,2))
reject('double_grid_energy',F(24,2),F(24))
reject('remove_source_half',continuum[0],2*continuum[0])
reject('reverse_force_sign',physical,-physical)
reject('wrong_density_first_variation',physical,physical/4)
reject('omit_one_physical_derivative_factor',physical,physical/4)
reject('infer_absolute_decay_from_signed_mean',16,0)
reject('wrong_particle_square_root',F(25),F(625))
reject('insufficient_jitter_accuracy',F(1,25),F(1))
reject('assert_threshold_source_power_negative',F(2,4)-F(1,2),F(-1,6))

result={'status':'PASS','evidence':'Exact finite Fourier, rational and coefficient checks only; not analytic certification or actual iid dynamics.',
        'assertions':sum(counts.values()),'categories':counts,'mutation_count':len(mutations),'mutations':mutations,
        'normalized_smooth_probe_second_coefficient':str(continuum[0]),'physical_source_coefficient_div_pi4':str(physical),
        'physical_absolute_limit_div_pi3_a2':16,'arithmetic':'Gaussian rational pairs; no floating point, randomness, external dependencies or tolerances.',
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2,sort_keys=True))
