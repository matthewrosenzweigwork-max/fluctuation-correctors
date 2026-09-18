#!/usr/bin/env python3
"""Independent exact checks for TASK-052; no constructor checker imported.

Only Python's standard library is used. Exact rational automatic differentiation
and finite Fourier algebra support, but do not replace, the prose hostile review.
Local polynomial jets are tests of identities, not substitute global Riesz data.
"""
from fractions import Fraction as Q
from collections import Counter
from pathlib import Path
import hashlib
import json
import math
import platform

COUNTS = Counter()
EXAMPLES = []

def check(group, condition, detail):
    if not condition:
        raise AssertionError(group + ': ' + detail)
    COUNTS[group] += 1

def root_exact(n, k):
    if n == 0:
        return 0
    lo, hi = 0, max(2, n)
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if m ** k <= n:
            lo = m
        else:
            hi = m
    if hi ** k == n:
        return hi
    if lo ** k != n:
        raise ValueError('not an exact rational root')
    return lo

def power(v, a):
    v, a = Q(v), Q(a)
    if a.denominator == 1:
        return v ** a.numerator
    if v <= 0:
        raise ValueError('positive rational base required')
    return Q(root_exact(v.numerator, a.denominator),
             root_exact(v.denominator, a.denominator)) ** a.numerator

class Jet:
    """Value, gradient and Hessian, computed by chain/product rules."""
    def __init__(self, v, g, h=None):
        self.v, self.g = Q(v), tuple(map(Q, g))
        n = len(self.g)
        self.h = tuple(tuple(map(Q, row)) for row in h) if h is not None else tuple((Q(0),)*n for _ in range(n))
    @property
    def n(self):
        return len(self.g)
    def lift(self, x):
        return x if isinstance(x, Jet) else Jet(x, (0,)*self.n)
    def __add__(self, b):
        b = self.lift(b)
        return Jet(self.v+b.v, [x+y for x,y in zip(self.g,b.g)],
                   [[self.h[i][j]+b.h[i][j] for j in range(self.n)] for i in range(self.n)])
    __radd__ = __add__
    def __neg__(self):
        return self * (-1)
    def __sub__(self, b):
        return self + (-self.lift(b))
    def __rsub__(self, b):
        return self.lift(b) - self
    def __mul__(self, b):
        b = self.lift(b)
        return Jet(self.v*b.v, [self.g[i]*b.v+self.v*b.g[i] for i in range(self.n)],
            [[self.h[i][j]*b.v+self.g[i]*b.g[j]+self.g[j]*b.g[i]+self.v*b.h[i][j]
              for j in range(self.n)] for i in range(self.n)])
    __rmul__ = __mul__
    def __pow__(self, a):
        a = Q(a)
        v, p1, p2 = power(self.v,a), a*power(self.v,a-1), a*(a-1)*power(self.v,a-2)
        return Jet(v, [p1*x for x in self.g],
                   [[p1*self.h[i][j]+p2*self.g[i]*self.g[j] for j in range(self.n)] for i in range(self.n)])

def variables(values):
    n = len(values)
    return [Jet(v, [int(i==j) for j in range(n)]) for i,v in enumerate(values)]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def matvec(a,v):
    return [dot(row,v) for row in a]

def local_g(z,s):
    r2=dot(z,z)
    return r2**(-s/2)

def kernel(z,s,with_remainder=False):
    r2=dot(z,z)
    out=[s*zi*r2**(-(s+2)/2) for zi in z]
    if with_remainder:
        # Negative gradient of an even smooth quadratic plus quartic potential.
        out=[ki-Q(i+1,7)*z[i]-Q(1,5)*z[i]*r2 for i,ki in enumerate(out)]
    return out

def f_gradient(x):
    # Gradient of sum (i+1)x_i^2/2 + x_i^3/3 plus x_0*x_1.
    return [(i+1)*xi+xi*xi+(x[1] if i==0 else x[0] if i==1 else 0)
            for i,xi in enumerate(x)]

for d,s in [(3,Q(1)), (4,Q(1,2)), (4,Q(2)), (5,Q(3,2)), (6,Q(4))]:
    e=[Q(3,5),Q(4,5)]+[Q(0)]*(d-2)
    transverse=[-e[1],e[0]]+[Q(0)]*(d-2)
    z=variables(e)
    g=local_g(z,s)
    dk=[[-g.h[i][j] for j in range(d)] for i in range(d)]
    k=kernel(z,s)
    for i in range(d):
        check('force_from_potential', k[i].v == -g.g[i], f'd={d},s={s},i={i}')
        for j in range(d):
            check('force_from_potential', k[i].g[j] == dk[i][j], f'DK[{i},{j}]')
    check('one_sided_eigenvalues', matvec(dk,e)==[-s*(s+1)*v for v in e], 'radial')
    check('one_sided_eigenvalues', matvec(dk,transverse)==[s*v for v in transverse], 'transverse')
    for N in [2,3,11]:
        full=[[Q(0) for _ in range(2*d)] for _ in range(2*d)]
        for i in range(2*d):
            for j in range(2*d):
                sign=1 if (i<d)==(j<d) else -1
                full[i][j]=sign*dk[i%d][j%d]/N
        check('one_sided_eigenvalues', matvec(full,e+e)==[0]*(2*d), 'pair center')
        rel=e+[-v for v in e]
        tr=transverse+[-v for v in transverse]
        check('one_sided_eigenvalues',matvec(full,rel)==[-2*s*(s+1)*v/N for v in rel],'pair radial')
        check('one_sided_eigenvalues',matvec(full,tr)==[2*s*v/N for v in tr],'pair transverse')
        for alpha in [Q(5,4),Q(3),Q(2*d+3)]:
            pair=variables([v/2 for v in e]+[-v/2 for v in e])
            diff=[pair[i]-pair[d+i] for i in range(d)]
            w=dot(diff,diff)**(-alpha/2)
            kp=kernel(diff,s)
            bp=[ki.v/N for ki in kp]+[-ki.v/N for ki in kp]
            drift=dot(w.g,bp)
            lap=sum(w.h[i][i] for i in range(2*d))
            check('pair_weight_generator',drift==-2*s*alpha/N,'relative drift factor')
            check('pair_weight_generator',lap==2*alpha*(alpha+2-d),'relative diffusion factor')
            for p in [Q(0),Q(1),Q(2)]:
                if alpha>p:
                    check('pair_weight_generator',drift+p*2*s/N==-(alpha-p)*2*s/N,'strict repulsion')
    # Local source derivative: independently differentiate the entire expression.
    radius=Q(1,16)
    vals=[radius*v/2 for v in e]+[-radius*v/2 for v in e]
    pair=variables(vals)
    x,y=pair[:d],pair[d:]
    zz=[x[i]-y[i] for i in range(d)]
    for rem in [False,True]:
        kk=kernel(zz,s,rem)
        fx,fy=f_gradient(x),f_gradient(y)
        delta=[fx[i]-fy[i] for i in range(d)]
        jj=dot(kk,delta)
        for j in range(d):
            expected_x=sum(kk[i].g[j]*delta[i].v+kk[i].v*fx[i].g[j] for i in range(d))
            expected_y=sum(-kk[i].g[j]*delta[i].v-kk[i].v*fy[i].g[d+j] for i in range(d))
            check('source_both_derivatives',jj.g[j]==expected_x,'x product rule')
            check('source_both_derivatives',jj.g[d+j]==expected_y,'y product rule')
        zero=dot(kk,[Jet(0,(0,)*(2*d)) for _ in range(d)])
        check('constant_source',zero.v==0 and all(v==0 for v in zero.g),'constant f')

# Exact zero-noise local radial flow, independent of the weighted generator.
# The local principal model is only a diagnostic; no periodic remainder is omitted
# from the reviewed theorem. Its time is chosen so both radii stay in the chart.
for s in [Q(1),Q(2),Q(4)]:
    for N in [2,3,17]:
        r0,r1=Q(1,2**40),Q(1,2**20)
        exponent=s+2
        h=N*(power(r1,exponent)-power(r0,exponent))/(2*s*exponent)
        check('zero_noise_radial_flow',h>0 and power(r1,exponent)==power(r0,exponent)+2*s*exponent*h/N,'radial trajectory')
        radial=power(r0/r1,s+1)
        tangent=r1/r0
        check('zero_noise_radial_flow',radial<=1 and tangent>=1,'radial contraction/transverse growth')
        for q in [Q(5,4),Q(7,5)]:
            weighted=tangent*power(r1,-q)/power(r0,-q)
            check('zero_noise_radial_flow',weighted==power(r1/r0,1-q)<=1,'terminal weighted derivative')
        source_integral=Q(N,4)*(r1*r1-r0*r0)
        change_of_variables=Q(N,2)*(r1*r1-r0*r0)/2
        check('zero_noise_radial_source',source_integral==change_of_variables,'integral s r^(-s) dt')
        # Anisotropic quadratic test, e=(3/5,4/5), tangent=(-4/5,3/5).
        angular_derivative=Q(-48,25)
        tangent_derivative=angular_derivative*source_integral/r0
        integrated_derivative=angular_derivative*change_of_variables/r0
        check('zero_noise_radial_source',tangent_derivative==integrated_derivative,'angular source derivative including growth')

# Maximal-tail integration: the split integral of min(1,A/u^2) is 2 sqrt(A).
for aroot in [Q(1),Q(3,2),Q(7)]:
    A=aroot*aroot
    check('maximal_supermartingale_tail',aroot+A/aroot==2*aroot,'tail integral')

# Morrey averaging constant after angular integration, evaluated on radial monomials.
for n in [6,8,12]:
    for power_k in [0,1,3,7]:
        for b in [Q(1,4),Q(1,8)]:
            direct=Q(n,(power_k+1)*(n+power_k+1))*b**(power_k+1)
            fubini=(Q(1,power_k+1)-Q(1,n+power_k+1))*b**(power_k+1)
            upper=b**(power_k+1)/(power_k+1)
            check('morrey_averaging',direct==fubini and direct<=upper,'angular factor 1/(n omega_n)')
    for P in [Q(n+1),Q(2*n)]:
        conjugate=P/(P-1)
        check('morrey_exponent',n-(n-1)*conjugate==(P-n)/(P-1)>0,'kernel integrability')

for d,s,q in [(3,Q(1),Q(5,4)),(3,Q(1),Q(7,5)),(3,Q(1,2),Q(5,4)),(4,Q(3,2),Q(7,4)),(6,Q(4),Q(5,2))]:
    for N in [2,3,17]:
        for p in [Q(1),Q(2),Q(2*d+1)]:
            alpha=p*q
            check('moment_and_source_ranges',alpha>p and (p-alpha)*2*s/N==p*(1-q)*2*s/N,'moment weight')
    alpha=2*(s+2)+1
    check('moment_and_source_ranges',alpha>2 and alpha+s+2>=2*(s+1),'source UI weight')
    check('moment_and_source_ranges',q+s+2>=s+1,'source first moment')
    check('weak_H1_thresholds',q<d and 2*q<d,'integrable and square integrable gradient')
    check('weak_H1_thresholds',d-1>0,'vanishing bounded boundary term')
    # Both relevant densities are tested; Coulomb D is separately an atom.
    for a in [s+1]+([s+2] if s<d-2 else []):
        check('two_singularity_thresholds',a<d and q<d,'separate integrability requirements')
        check('two_singularity_thresholds',d-a-q-(-q)==d-a>0,'weighted dominance even above d')
        EXAMPLES.append({'d':d,'s':str(s),'q':str(q),'a':str(a),'near_second_power':str(d-a-q),'above_d':a+q>d})
    if d==3 and s==1:
        check('d3_coulomb_noise',2*q*(q+2-d)>0,'positive diffusion coefficient')
        check('d3_coulomb_noise',0*2*q*(q+2-d)==0,'zero-noise diffusion')

# Independent one-coordinate Fourier algebra in dimensionless angle units.
# Restore 2pi to K and (2pi)^2 to D; both sides then get identical factors.
# mu_m and Phi_(k,l) may be arbitrary, so checking coefficients suffices.
for decay in [2,3,4]:
    def gs(n):
        return Q(0) if n==0 else Q(1,abs(n)**decay)
    for m in range(-3,4):
        for k in range(-3,4):
            for l in range(-3,4):
                r=k+m
                direct=-k*r*gs(r)
                measure=-r*r*gs(r)
                background=m*r*gs(r)
                check('inhomogeneous_response',direct==measure+background,'R_x gradient versus compensated response')
                # Coefficients of i in the x derivative, with all four products.
                dmu_measure=-m*r*r*gs(r)
                dF_measure=-k*r*r*gs(r)
                hessian_mu=m*m*r*gs(r)
                grad_mu_grad_F=m*k*r*gs(r)
                check('all_response_derivative_products',r*direct==dmu_measure+dF_measure+hessian_mu+grad_mu_grad_F,'x derivative four terms')
                check('all_response_derivative_products',l*direct==l*measure+l*background,'y derivative two terms')
                r2=l+m
                direct_y=-l*r2*gs(r2)
                check('inhomogeneous_response',direct_y==-r2*r2*gs(r2)+m*r2*gs(r2),'R_y')
                if k==0:
                    check('response_constants',direct==0 and r*direct==0,'R_x kills constants with nonconstant mu')
                if decay==2:
                    atom_compensation=-1+int(r==0)
                    check('coulomb_atom_compensation',measure==atom_compensation,'atom plus constant density')
    for k in range(-3,4):
        for l in range(-3,4):
            multiplier=-(k*k*gs(k)+l*l*gs(l))
            direct_pair=-k*k*gs(k)-l*l*gs(l)
            check('homogeneous_fourier',multiplier==direct_pair,'both slots and negative sign')
            if decay==2:
                check('homogeneous_fourier',multiplier==-(int(k!=0)+int(l!=0)),'Coulomb zero/nonzero modes')

# Algebraic stationary value underlying M_s; integer s=1,2,4 with exact roots.
for s in [Q(1),Q(2),Q(4)]:
    for v in [Q(1),Q(2),Q(3,2)]:
        b=Q(2,3)
        a=(s+2)*b*power(v,s)/4
        derivative=2*a*v-(b/2)*(s+2)*power(v,s+1)
        value=a*v*v-(b/2)*power(v,s+2)
        declared=s*a*v*v/(s+2)
        check('absorption_stationary_value',derivative==0 and value==declared,'maximum coefficient')

assert all(COUNTS.values())
source=Path(__file__)
result={
  'status':'PASS',
  'python':platform.python_version(),
  'arithmetic':'exact fractions only; no floating-point tolerance, randomness, or external dependencies',
  'total_checks':sum(COUNTS.values()),
  'checks_by_group':dict(sorted(COUNTS.items())),
  'convolution_examples':EXAMPLES,
  'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
  'scope':'Supports local identities, coefficients, ranges and Fourier response algebra. Does not certify stochastic interchange, common flow, convergence, or the theorem; those are reviewed in prose.'
}
out=source.with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
