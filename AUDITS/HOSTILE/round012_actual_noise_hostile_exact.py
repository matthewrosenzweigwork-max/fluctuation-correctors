#!/usr/bin/env python3
"""Fresh TASK067 supporting diagnostics. Standard library; exact arithmetic only.

Finite tests do not certify any singular analytic limit. No prior checker is read.
Fourier derivatives omit 2*pi: D exp(i*k*x)=i*k exp(i*k*x).
Restoring physical coordinates multiplies each spatial derivative by 2*pi.
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import argparse
import json
import platform
import sys


@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        other = qq(other)
        return Q(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-qq(other))

    def __mul__(self, other):
        other = qq(other)
        return Q(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__


def qq(value):
    return value if isinstance(value, Q) else Q(F(value))


ZERO, I = Q(), Q(F(0), F(1))
counts, failures = Counter(), []


def check(category, label, condition):
    counts[category] += 1
    if not condition:
        failures.append({"category": category, "label": label})


def clean(poly):
    return {k: qq(v) for k, v in poly.items() if qq(v) != ZERO}


def add(*polys):
    out = {}
    for poly in polys:
        for k, v in poly.items():
            out[k] = out.get(k, ZERO) + v
    return clean(out)


def scale(poly, value):
    return clean({k: qq(value) * v for k, v in poly.items()})


def derivative(poly, slot):
    return clean({k: I * k[slot] * v for k, v in poly.items()})


def laplacian(poly):
    return clean({k: -sum(j*j for j in k) * v for k, v in poly.items()})


def embed(poly, slots, n):
    out = {}
    for freqs, value in poly.items():
        key = [0] * n
        for slot, freq in zip(slots, freqs):
            key[slot] += freq
        key = tuple(key)
        out[key] = out.get(key, ZERO) + value
    return clean(out)


def norm2(vector):
    return sum(x*x for x in vector)


def matvec(matrix, vector):
    return [sum(a*b for a, b in zip(row, vector)) for row in matrix]


root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, default=Path(__file__).with_name('ROUND_012_ACTUAL_NOISE_EXACT_RESULTS.json'))
args = parser.parse_args()
manifest = root / 'AUDITS/ROUND_012_NOISE_HOSTILE_INPUT_SHA256SUMS.txt'
input_rows = []
for row in manifest.read_text().splitlines():
    expected, relative = row.split('  ', 1)
    data = (root / relative).read_bytes()
    actual = sha256(data).hexdigest()
    check('input_integrity', relative, actual == expected)
    input_rows.append({'path': relative, 'sha256': actual, 'bytes': len(data)})
check('input_integrity', 'exactly24_inputs', len(input_rows) == 24)

# Cartesian differentiation of |z|^(-s) at |z|=1 using the power chain rule.
# The second-order jet of v^a at v=1 has derivatives a and a(a-1).
for d in range(3, 10):
    for s in (F(1, 4), F(1, 2), F(1), F(3, 2), F(2), F(3), F(4)):
        if not 0 < s < d-2:
            continue
        for n in (2, 3, 17):
            z = [F(3, 5), F(4, 5)] + [F(0)] * (d-2)
            a = -s/2
            dg = [2*a*x for x in z]
            hessian = [[4*a*(a-1)*z[i]*z[j] + (2*a if i == j else 0)
                        for j in range(d)] for i in range(d)]
            dk = [[-v for v in row] for row in hessian]
            check('cartesian_jet', f'force:{d},{s},{n}', [-v for v in dg] == [s*x for x in z])
            check('cartesian_jet', f'divergence:{d},{s},{n}', sum(dk[i][i] for i in range(d)) == s*(d-2-s))
            block = [[dk[i % d][j % d] * (1 if (i < d) == (j < d) else -1)/n
                      for j in range(2*d)] for i in range(2*d)]
            transverse = [F(-4, 5), F(3, 5)] + [F(0)] * (d-2)
            for name, vector, eigenvalue in (
                ('center', z+z, F(0)),
                ('radial', z+[-v for v in z], -2*s*(s+1)/n),
                ('transverse', transverse+[-v for v in transverse], 2*s/n),
            ):
                check('cartesian_jet', f'{name}:{d},{s},{n}', matvec(block, vector) == [eigenvalue*v for v in vector])
            for q in (F(5, 4), (s+2)/2):
                if not 1 < q < F(d, 2) or q > s+1:
                    continue
                aw = -q/2
                dw = [2*aw*x for x in z]
                hw = [[4*aw*(aw-1)*z[i]*z[j] + (2*aw if i == j else 0)
                       for j in range(d)] for i in range(d)]
                for nu in (F(0), F(1, 7), F(3, 2)):
                    value = 2*nu*sum(hw[i][i] for i in range(d)) + sum((2*s*x/n)*v for x, v in zip(z, dw)) + 2*s/n
                    predicted = -2*s*(q-1)/n + 2*nu*q*(q+2-d)
                    check('weighted_generator', f'{d},{s},{n},{q},{nu}', value == predicted)

# Exact maximizer diagnostics for a v^2-(b/2)v^(s+2), including both endpoints.
for s in (1, 2, 3, 4, 6):
    p = s+2
    for b in (F(1, 17), F(1), F(5)):
        for vstar in (F(1, 3), F(1), F(4)):
            a = p*b*vstar**s/4
            maximum = F(s, p)*a*vstar**2
            check('maximizer', f'critical:{s},{b},{vstar}', 2*a*vstar - p*b*vstar**(p-1)/2 == 0)
            check('maximizer', f'value:{s},{b},{vstar}', a*vstar**2 - b*vstar**p/2 == maximum)
            for v in (F(0), vstar/2, vstar, 2*vstar, 10*vstar):
                check('maximizer', f'bound:{s},{b},{vstar},{v}', a*v*v-b*v**p/2 <= maximum)

# Independent finite Fourier algebra for both original integrated-gradient responses.
kernel = {k: F(1, abs(k)+1) for k in (-3, -2, -1, 1, 2, 3)}
K = {k: -I*k*g for k, g in kernel.items()}
D = {k: k*k*g for k, g in kernel.items()}
test_pairs = [clean({(k,l): F(1)}) for k in range(-4,5) for l in range(-4,5)]
for idx, phi in enumerate(test_pairs):
    direct = {}
    for (k,l), value in phi.items():
        # The w-integration selects K_{-k} and K_{-l}, retaining both slots.
        multiplier = K.get(-k, ZERO)*I*k + K.get(-l, ZERO)*I*l
        direct[(k,l)] = value*multiplier
    direct = clean(direct)
    expected = clean({(k,l): -(D.get(k,0)+D.get(l,0))*value for (k,l),value in phi.items()})
    check('two_response_fourier', f'multiplier:{idx}', direct == expected)
    for slot in (0,1):
        differentiated_input = derivative(phi, slot)
        after = clean({(k,l): -(D.get(k,0)+D.get(l,0))*value for (k,l),value in differentiated_input.items()})
        check('two_response_fourier', f'commute:{idx},{slot}', derivative(direct,slot) == after)

# Literal ordered deleted-pair statistic and particle energy, at finite N.
pair_kernels = [
    {(0,0): F(7,3)},
    {(1,0):F(1),(-1,0):F(1),(0,1):F(1),(0,-1):F(1)},
    {(1,-1):F(1,2),(-1,1):F(1,2)},
    {(1,2):F(1), (2,1):F(1), (-1,-2):F(1),(-2,-1):F(1)},
    {(0,0):F(2), (2,0):F(1,3),(0,2):F(1,3),(-2,0):F(1,3),(0,-2):F(1,3),(1,-1):F(2,5),(-1,1):F(2,5)},
]
for n in range(2,8):
    zero_key = (0,)*n
    for case, raw in enumerate(pair_kernels):
        phi = clean(raw)
        projection = clean({(k,):v for (k,l),v in phi.items() if l == 0})
        literal = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    literal = add(literal, scale(embed(phi,(i,j),n),F(1,2*n*n)))
            literal = add(literal, scale(embed(projection,(i,),n),F(-1,n)))
        literal = add(literal,{zero_key:phi.get((0,0),ZERO)*F(1,2)})
        G = derivative(phi,0)
        A = derivative(projection,0)
        for i in range(n):
            expected = scale(embed(A,(i,),n),F(-1,n))
            for j in range(n):
                if i != j:
                    expected = add(expected,scale(embed(G,(i,j),n),F(1,n*n)))
            check('literal_deleted_gradient',f'{n},{case},{i}',derivative(literal,i)==expected)
        if case == 0:
            check('literal_deleted_gradient',f'constant:{n}',literal=={zero_key:qq(F(-7,6*n))})
    energy, divergence_sum = {}, {}
    gpair = clean({(k,-k):v for k,v in kernel.items()})
    dpair = clean({(k,-k):v for k,v in D.items()})
    kpair = clean({(k,-k):v for k,v in K.items()})
    for i in range(n):
        for j in range(i+1,n):
            energy=add(energy,scale(embed(gpair,(i,j),n),F(1,n)))
            divergence_sum=add(divergence_sum,scale(embed(dpair,(i,j),n),F(-2,n)))
    check('literal_energy',f'laplacian:{n}',laplacian(energy)==divergence_sum)
    for i in range(n):
        force={}
        for j in range(n):
            if i!=j:
                force=add(force,scale(embed(kpair,(i,j),n),F(1,n)))
        check('literal_energy',f'force:{n},{i}',scale(derivative(energy,i),-1)==force)
    check('literal_energy',f'pair_expectation_coefficient:{n}',F(2,n)*F(n*(n-1),2)==n-1)

# Configuration-space inequalities and factors after summation/scaling.
for n in range(2,18):
    for case in range(7):
        gs = [[[F(((i+1)*(j+2)*(a+1)+case)%11-5,case+1) for a in range(3)]
               for j in range(n) if j!=i] for i in range(n)]
        aa = [[F((i+a+case)%7-3,case+2) for a in range(3)] for i in range(n)]
        lhs=F(0)
        for row, avec in zip(gs,aa):
            total=[sum(v[a] for v in row)-n*avec[a] for a in range(3)]
            lhs += norm2(total)/n**4
        rhs = F(2*(n-1),n**4)*sum(norm2(v) for row in gs for v in row) + F(2,n*n)*sum(norm2(v) for v in aa)
        check('configuration_square',f'{n},{case}',lhs<=rhs)
    check('configuration_square',f'exchangeable_pair:{n}',F(2*(n-1),n**4)*n*(n-1)==F(2*(n-1)**2,n**3))
    check('configuration_square',f'exchangeable_background:{n}',F(2,n*n)*n==F(2,n))
    for nu in (F(0),F(1,19),F(1),F(7,3)):
        b=min(1/nu,F(1)) if nu else None
        if not nu:
            check('noise_factors',f'zero:{n}',2*nu*n == 0)
            continue
        factor=2*nu*n*b
        check('noise_factors',f'pair:{n},{nu}',factor*F(2*(n-1)**2,n**3)==4*nu*b*F((n-1)**2,n*n))
        check('noise_factors',f'background:{n},{nu}',factor*F(2,n)==4*nu*b)
        check('noise_factors',f'leading:{n},{nu}',factor*F(n,n*n)==2*nu*b and nu*b<=1)
    for case in range(5):
        first=[F((j+case)%9-4,j+1) for j in range(3*n)]
        second=[F((2*j+case)%7-3,j+2) for j in range(3*n)]
        check('cross_cauchy_schwarz',f'{n},{case}',sum(a*b for a,b in zip(first,second))**2 <= norm2(first)*norm2(second))

# Rational exponent and endpoint tests, independent of candidate diagnostics.
admitted=[]
for d in range(3,21):
    for denominator in (1,2,3,5):
        for numerator in range(1,(d-2)*denominator):
            s=F(numerator,denominator)
            p=s+2; a=s/p; theta=1-s/d; q=p/2; eta=s+1-q
            admitted.append((d,s))
            check('range_and_scaling',f'q:{d},{s}',1<q<F(d,2) and q<=s+1 and 2*q==p)
            check('range_and_scaling',f'gradient_square:{d},{s}',2*eta/p==a)
            check('range_and_scaling',f'critical_chi:{d},{s}',-theta+2/p==s*(p-d)/(d*p)<0)
            check('range_and_scaling',f'critical_decay:{d},{s}',a-theta==(s*p-2*d)/(d*p) and ((a<theta)==(s*p<2*d)))
            check('range_and_scaling',f'bounded_chi:{d},{s}',a-2/p==(s-2)/p)
            check('range_and_scaling',f'barrier_uniformity:{d},{s}',F(2)/s-F(2)/p*(p/s)==0)
            check('range_and_scaling',f'occupation_N:{d},{s}',(eta/p-1)+1==eta/p)
            check('range_and_scaling',f'convolution_integrability:{d},{s}',d-p>0 and d-q>0 and (d-p-q)-(-q)==d-p)
            if s<2:
                check('range_and_scaling',f'all_bounded_chi:{d},{s}',a<theta and a-2/p<0)
            # Rational powers are evaluated exactly by selecting a perfect denominator power.
            den=eta.denominator*p.denominator
            for t in (F(1,3),F(1),F(3)):
                check('weight_interpolation',f'{d},{s},{t}',t**int(den*eta)<=1+t**int(den*p))
check('excluded_endpoints','Coulomb_density_zero',F(1)*(3-2-F(1))==0)
check('excluded_endpoints','critical_equality_admitted',F(4,6)+F(4,12)-1==0 and 4<12-2)
check('excluded_endpoints','s2_bounded_chi_no_decay',F(2,4)-F(2,4)==0 and 2<5-2)
check('excluded_endpoints','large_s_bound_grows',F(4,6)+F(4,8)-1>0 and 4<8-2)

# Independent zero-noise radial model: exact integrated principal source and scaling.
# r_T^p=r_0^p+(2*s*p/N)T; U=N/4*(r_T^2-r_0^2) times a fixed angular factor.
for s in (1,2,3,4):
    p=s+2
    for base in (2,3,5):
        n=base**p
        for v,w in ((F(1,3),F(2)),(F(1),F(3)),(F(2),F(5))):
            r0=v/base; rt=w/base; horizon=(w**p-v**p)/(2*s*p)
            check('radial_model',f'flow:{s},{base},{v},{w}',rt**p==r0**p+F(2*s*p,n)*horizon)
            u=F(n,4)*(rt**2-r0**2)
            # Tangential coefficient U/r0 has the claimed rescaled homogeneity.
            check('radial_model',f'source_scale:{s},{base},{v},{w}',u/base**s==(w*w-v*v)/4)
            check('radial_model',f'tangent_scale:{s},{base},{v},{w}',(u/r0)/base**(s+1)==(w*w-v*v)/(4*v))

result={
    'task':'TASK-067',
    'status':'PASS' if not failures else 'FAIL',
    'assertion_count':sum(counts.values()),
    'counts_by_category':dict(sorted(counts.items())),
    'unique_dimension_exponent_pairs':len(set(admitted)),
    'failures':failures,
    'arithmetic':'fractions.Fraction and Gaussian rational sparse Fourier polynomials; no floating point, tolerance, simulation, or random seed',
    'scope':'Finite supporting diagnostics only. The analytic proof and conditional source status are in ROUND_012_ACTUAL_NOISE_REVIEW.md.',
    'python_version':platform.python_version(),
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'input_manifest_sha256':sha256(manifest.read_bytes()).hexdigest(),
    'inputs':input_rows,
}
output=args.output
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','assertion_count','counts_by_category','failures')},indent=2))
sys.exit(bool(failures))
