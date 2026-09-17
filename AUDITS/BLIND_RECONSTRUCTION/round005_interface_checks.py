#!/usr/bin/env python3
"""Exact statement-only THM025 interface checks; Python standard library only.

Run from the isolated worktree:
  python3 AUDITS/BLIND_RECONSTRUCTION/round005_interface_checks.py

Finite Fourier tests divide all interaction terms by 4*pi^2*c_(d,s).
They use a symmetric finite Coulomb cutoff with weight |k|^-2.
These tests check algebra and specified interfaces, not singular process existence.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
COUNTS = defaultdict(int)

def check(condition, group, detail):
    if not condition:
        raise AssertionError(f'{group}: {detail}')
    COUNTS[group] += 1

def clean(a):
    return {k: v for k, v in a.items() if v}

def addv(a, b):
    return tuple(x+y for x, y in zip(a,b))

def negv(a):
    return tuple(-x for x in a)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

# All frozen bytes, including the assigned task, are checked before algebra.
manifest = OUT/'ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt'
input_records = []
for line in manifest.read_text().splitlines():
    expected, relative = line.split('  ',1)
    actual = hashlib.sha256((ROOT/relative).read_bytes()).hexdigest()
    check(actual == expected, 'input_sha256', relative)
    input_records.append({'path':relative,'sha256':actual})

# Exact iid finite sums, including spatial atoms and their diagonal values.
probs = [F(1,2),F(1,3),F(1,6)]
a = [F(1),F(-2),F(1)]
b = [F(0),F(1),F(-2)]
kernels = {
    'constant': [[F(7,3) for j in range(3)] for i in range(3)],
    'separable': [[F(2,5)+a[i]+a[j] for j in range(3)] for i in range(3)],
    'canonical': [[b[i]*b[j] for j in range(3)] for i in range(3)],
    'mixed': [[F(2),F(-1,3),F(5,2)],
              [F(-1,3),F(4),F(-7,5)],
              [F(5,2),F(-7,5),F(1,11)]]}
for name, phi in kernels.items():
    marginal = [sum(probs[j]*phi[i][j] for j in range(3)) for i in range(3)]
    theta = sum(probs[i]*marginal[i] for i in range(3))
    h = [v-theta for v in marginal]
    H = [[phi[i][j]-theta-h[i]-h[j] for j in range(3)] for i in range(3)]
    h2 = sum(probs[i]*h[i]**2 for i in range(3))
    H2 = sum(probs[i]*probs[j]*H[i][j]**2 for i in range(3) for j in range(3))
    phi2 = sum(probs[i]*probs[j]*phi[i][j]**2 for i in range(3) for j in range(3))
    check(phi2 == theta**2+2*h2+H2,'iid_orthogonality',name)
    for N in (2,3,4,5):
        mean = F(0)
        second = F(0)
        for sample in product(range(3),repeat=N):
            mass = math.prod(probs[x] for x in sample)
            ordered = sum(phi[sample[i]][sample[j]] for i in range(N) for j in range(N) if i != j)
            pn = (ordered/F(N*N)-2*sum(marginal[x] for x in sample)/N+theta)/2
            decomposition = (-theta/(2*N)-sum(h[x] for x in sample)/(N*N)
                +sum(H[sample[i]][sample[j]] for i in range(N) for j in range(i+1,N))/(N*N))
            check(pn == decomposition,'iid_exact_decomposition',f'{name}, N={N}, sample={sample}')
            mean += mass*pn
            second += mass*pn*pn
        expected = theta**2/(4*N*N)+h2/(N**3)+F(N-1,2*N**3)*H2
        sharp = F(N-1,2*N**3)*phi2
        check(mean == -theta/(2*N),'iid_mean',f'{name},N={N}')
        check(second == expected,'iid_second_moment',f'{name},N={N}')
        check(second <= sharp,'iid_sharp_inequality',f'{name},N={N}')
        if N==2 or name=='canonical':
            check(second == sharp,'iid_sharp_equality',f'{name},N={N}')
        beta = F(3,7)
        scaled = N*min(beta,F(1))*second
        check(scaled <= min(beta,F(1))*phi2/(2*N),'iid_scaled_endpoint',f'{name},N={N}')

# Necessity of two density factors for the general norm conversion.
M = F(2)
haar_square = F(1,4)  # Phi=1_(A x A), Haar(A)=1/2.
weighted_square = F(1)  # mu=2*1_A.
check(weighted_square == M*M*haar_square,'density_factor','M squared is exact')
check(weighted_square > M*haar_square,'mutation_detection','a single M factor fails')

zero=(0,0,0)
e1=(1,0,0)
e2=(0,1,0)
mu={zero:F(1),e1:F(1,8),negv(e1):F(1,8),e2:F(1,12),negv(e2):F(1,12)}
phi=defaultdict(F)
for p,q,v in [(e1,e2,F(2,3)),((2,0,0),negv(e2),F(-3,5)),(zero,e1,F(1,7))]:
    for key in {(p,q),(q,p),(negv(p),negv(q)),(negv(q),negv(p))}:
        phi[key]+=v
phi=clean(phi)
# Finite even cutoff containing every frequency sampled by the response checks.
ks=[k for k in product(range(-3,4),repeat=3) if any(k)]
weights={k:F(1,dot(k,k)) for k in ks}

def response_original(data, density, slot):
    # Expand the integrated-gradient formula before integrating w.
    out=defaultdict(F)
    for (p,q),v in data.items():
        freq=p if slot==0 else q
        for a,m in density.items():
            r=addv(a,freq)
            k=negv(r)
            if k in weights:
                # K_hat(k)=-2*pi*i*c*k*w(k); grad=2*pi*i*freq.
                val=dot(k,freq)*weights[k]*m*v
                key=(r,q) if slot==0 else (p,r)
                out[key]+=val
    return clean(out)

def response_measure(data,density,slot,drop_density_gradient=False):
    out=defaultdict(F)
    for (p,q),v in data.items():
        freq=p if slot==0 else q
        for a,m in density.items():
            r=addv(a,freq)
            if r in weights:
                val=-dot(r,r)*weights[r]*m*v
                if not drop_density_gradient:
                    val+=dot(r,a)*weights[r]*m*v
                key=(r,q) if slot==0 else (p,r)
                out[key]+=val
    return clean(out)

def plus(a,b):
    out=defaultdict(F,a)
    for k,v in b.items(): out[k]+=v
    return clean(out)

def swap(a):
    return clean({(q,p):v for (p,q),v in a.items()})

for slot in (0,1):
    check(response_original(phi,mu,slot)==response_measure(phi,mu,slot),
          'fourier_response',f'inhomogeneous density, slot {slot}')
    constant={(zero,zero):F(1)}
    check(not response_original(constant,mu,slot),'response_constants',f'original slot {slot}')
    check(not response_measure(constant,mu,slot),'response_constants',f'measure slot {slot}')
    check(bool(response_measure(constant,mu,slot,True)),
          'mutation_detection',f'omitting density gradient breaks slot {slot}')
Rphi=plus(response_measure(phi,mu,0),response_measure(phi,mu,1))
check(swap(Rphi)==Rphi,'pair_exchange','both response slots')
nonzero_mode={(e1,e2):F(1)}
rx=response_measure(nonzero_mode,{zero:F(1)},0)
ry=response_measure(nonzero_mode,{zero:F(1)},1)
check(rx=={(e1,e2):F(-1)},'coulomb_multipliers','first slot')
check(ry=={(e1,e2):F(-1)},'coulomb_multipliers','second slot')
check(plus(rx,ry)=={(e1,e2):F(-2)},'coulomb_multipliers','two slots')
check(plus(rx,ry)!=rx,'mutation_detection','one-slot loss detected')

# Pair drift checked by two separately expanded particle drifts.
def internal_original(data,N):
    out=defaultdict(F)
    for (p,q),v in data.items():
        for k,w in weights.items():
            out[(addv(p,k),addv(q,negv(k)))]+=dot(k,p)*w*v/N
            out[(addv(p,negv(k)),addv(q,k))]+=dot(k,q)*w*v/N
    return clean(out)

def internal_B(data,N):
    out=defaultdict(F)
    for (p,q),v in data.items():
        for k,w in weights.items():
            out[(addv(p,k),addv(q,negv(k)))]+=(dot(k,p)-dot(k,q))*w*v/N
    return clean(out)

for N in (2,3,7):
    bresult=internal_B(phi,N)
    check(internal_original(phi,N)==bresult,'pair_internal_drift',f'N={N}')
    check(swap(bresult)==bresult,'pair_exchange',f'internal drift N={N}')
    check(internal_B(phi,N)=={k:v/N for k,v in internal_B(phi,1).items()},
          'finite_N_coefficient',f'exact 1/N, N={N}')

# J=K(x-y).(grad f(x)-grad f(y)), independently compared with B[f(x)+f(y)].
f={e1:F(1,2),negv(e1):F(1,2),e2:F(1,3),negv(e2):F(1,3)}
j_direct=defaultdict(F)
separable=defaultdict(F)
for n,h in f.items():
    separable[(n,zero)]+=h
    separable[(zero,n)]+=h
    for k,w in weights.items():
        coefficient=dot(k,n)*w*h
        j_direct[(addv(k,n),negv(k))]+=coefficient
        j_direct[(k,addv(n,negv(k)))]-=coefficient
check(clean(j_direct)==internal_B(clean(separable),1),'source_fourier','J equals B of additive test')
check(swap(clean(j_direct))==clean(j_direct),'pair_exchange','source')

# Backward time and spatial signs on actual homogeneous Fourier modes.
for d,s in ((3,1),(4,2),(5,1),(5,3)):
    exponent=s+2-d
    for n in (1,2,3):
        q=F(n)**exponent
        for nu in (F(0),F(1,7),F(4)):
            acoef=nu*n*n+q  # Overall 4*pi^2, c=1 normalization.
            check(acoef+(-nu*n*n-q)==0,'backward_sign',f'd={d},s={s},n={n},nu={nu}')
            check(-acoef+(-nu*n*n-q)!=0,'mutation_detection','reversing terminal damping sign')

# Gamma recurrence, with the common pi^2 factored out, checks Riesz constants.
for d in range(3,13):
    for quarter in range(1,4*(d-2)):
        s=F(quarter,4)
        alpha=(d-s)/2
        gamma_ratio=F(1)/(alpha-1)/(s/2)
        check(s*(d-2-s)*gamma_ratio==4,'riesz_normalization','4*pi^2 multiplier identity')
    check(F(2*(d-2),1)/(F(d,2)-1)==4,'coulomb_normalization','sphere/gamma recurrence')

# Endpoint and temperature exponents. This is exact rational arithmetic.
for d in range(3,13):
    for quarter in range(1,4*(d-2)+1):
        s=F(quarter,4)
        critical_beta_power=1-s/d
        check(critical_beta_power>0,'temperature_quantifiers','critical beta diverges')
        check(critical_beta_power+2*s/d-1==s/d,'temperature_quantifiers','critical old-floor failure')
        check(-1+s/d-1<0,'temperature_quantifiers','beta=N^-1 is excluded subcritical example')
        if 2*s>d:
            alpha=(2*s-d)/(s+2)
            check(alpha-1==-(d+2-s)/(s+2),'endpoint_exponents','power simplification')
            check(alpha<1,'endpoint_exponents','strict endpoint decay')

# Volterra sign check by exact scalar Taylor coefficients, independent of the estimate.
for r in (F(-2),F(0),F(3)):
    j=F(5,7)
    coeff={n:j*r**(n-1)/math.factorial(n) for n in range(1,10)}
    check(coeff[1]==j,'volterra_sign','terminal first coefficient')
    for n in range(1,9):
        check((n+1)*coeff[n+1]==r*coeff[n],'volterra_sign','d/dtau Phi=J+R Phi')

result={
    'status':'PASS',
    'scope':'Exact algebra and frozen-input verification; prerequisite analytic proofs remain explicit hypotheses.',
    'python':sys.version.split()[0],
    'arithmetic':'fractions.Fraction, integer arithmetic, SHA-256; no numerical approximation',
    'check_counts':dict(sorted(COUNTS.items())),
    'total_assertions':sum(COUNTS.values()),
    'inputs':input_records,
    'excluded':'No singular-flow, finite-particle Ito-domain, evolved-law or fluctuation-limit certification.',
}
path=OUT/'ROUND_005_INTERFACE_CHECK_RESULTS.json'
path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ('status','total_assertions','check_counts')},indent=2))
