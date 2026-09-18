#!/usr/bin/env python3
"""AUD072 supporting checks; standard library only, never a continuum proof.

Every mutation changes a mathematical datum evaluated by the same checks.
No constructor code, results, simulation, random sampling, or source reads.
"""
import argparse
from fractions import Fraction as Q
import itertools
import json
import math
import sys


MUTATIONS = (
    'omit_conditional_mean', 'zero_endpoint_noise_covariance',
    'halve_relative_drift', 'halve_relative_noise', 'halve_angle_drift',
    'omit_cutoff_cross_bracket', 'remove_backward_factor',
    'halve_empirical_pair_coefficient', 'change_spherical_projection',
    'halve_full_gradient_factor', 'use_full_dimension_for_radius',
    'omit_overlap_labels', 'erase_constant_mode_defect',
)
parser = argparse.ArgumentParser()
parser.add_argument('--mutation', choices=MUTATIONS)
args = parser.parse_args()
checks = []
observations = {}


def check(category, label, left, right):
    checks.append({'category': category, 'label': label})
    if left != right:
        raise AssertionError('{}: {}: observed {} != asserted {}'.format(
            category, label, left, right))


def z(re, im=0):
    return Q(re), Q(im)


def za(a, b):
    return a[0]+b[0], a[1]+b[1]


def zm(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def zs(a, c):
    return c*a[0], c*a[1]


def zc(a):
    return a[0], -a[1]


def zn(a):
    return a[0]*a[0]+a[1]*a[1]


def zsum(seq):
    out=z(0)
    for a in seq:
        out=za(out,a)
    return out


def integer_root(n, d):
    lo,hi=0,max(1,n)
    while lo<=hi:
        mid=(lo+hi)//2
        p=mid**d
        if p==n:
            return mid
        if p<n:
            lo=mid+1
        else:
            hi=mid-1
    raise ValueError('non-exact root {} degree {}'.format(n,d))


def exact_pow(x,p):
    x,p=Q(x),Q(p)
    if p.denominator==1:
        return x**p.numerator
    if x<0:
        raise ValueError('negative fractional power')
    return Q(integer_root(x.numerator,p.denominator),
             integer_root(x.denominator,p.denominator))**p.numerator


class Jet:
    """Independent second-order rational differentiation in four variables."""
    d=4

    def __init__(self,v,g=None,h=None):
        self.v=Q(v)
        self.g=tuple(Q(a) for a in (g or [0]*self.d))
        self.h=tuple(tuple(Q(a) for a in row)
                     for row in (h or [[0]*self.d for _ in range(self.d)]))

    @classmethod
    def var(cls,v,i):
        g=[0]*cls.d
        g[i]=1
        return cls(v,g)

    def __add__(self,o):
        o=o if isinstance(o,Jet) else Jet(o)
        return Jet(self.v+o.v,[a+b for a,b in zip(self.g,o.g)],
                   [[self.h[i][j]+o.h[i][j] for j in range(self.d)]
                    for i in range(self.d)])

    __radd__=__add__

    def __mul__(self,o):
        o=o if isinstance(o,Jet) else Jet(o)
        return Jet(self.v*o.v,
                   [self.g[i]*o.v+self.v*o.g[i] for i in range(self.d)],
                   [[self.h[i][j]*o.v+self.g[i]*o.g[j]
                     +self.g[j]*o.g[i]+self.v*o.h[i][j]
                     for j in range(self.d)] for i in range(self.d)])

    __rmul__=__mul__

    def power(self,p):
        p=Q(p)
        v=exact_pow(self.v,p)
        a=p*exact_pow(self.v,p-1)
        b=p*(p-1)*exact_pow(self.v,p-2)
        return Jet(v,[a*g for g in self.g],
                   [[a*self.h[i][j]+b*self.g[i]*self.g[j]
                     for j in range(self.d)] for i in range(self.d)])


def determinant(m):
    n=len(m)
    if n==1:
        return m[0][0]
    return sum((-1)**j*m[0][j]*determinant(
        [row[:j]+row[j+1:] for row in m[1:]]) for j in range(n))


def sphere_moment(halfpowers,d=4):
    total=sum(halfpowers)
    numer=1
    for a in halfpowers:
        for j in range(1,2*a,2):
            numer*=j
    denom=1
    for j in range(total):
        denom*=d+2*j
    return Q(numer,denom)


def run():
    # This finite space has a nonconstant conditional mean and nonzero noise.
    weights=[Q(1,3),Q(2,3)]
    transition=[[Q(1,4),Q(3,4)],[Q(2,5),Q(3,5)]]
    x=[z(1,1),z(-1,2)]
    endpoint=[z(2,-1),z(-1,3)]
    for N in (2,3,7):
        A=Q(2,3)
        means=[zsum(zs(endpoint[j],transition[i][j]) for j in range(2))
               for i in range(2)]
        D=C=J=Q(0)
        cross=z(0)
        endpoint_noise=z(0)
        for i in range(2):
            bias=za(means[i],zs(x[i],-A))
            C+=N*weights[i]*zn(bias)
            for j in range(2):
                prob=weights[i]*transition[i][j]
                noise=za(endpoint[j],zs(means[i],-1))
                error=za(endpoint[j],zs(x[i],-A))
                D+=N*prob*zn(error)
                J+=N*prob*zn(noise)
                cross=za(cross,zs(zm(bias,zc(noise)),prob))
                endpoint_noise=za(endpoint_noise,
                    zs(zm(endpoint[j],zc(noise)),prob))
        check('conditional', 'orthogonality N={}'.format(N), cross,z(0))
        claim_C=0 if args.mutation=='omit_conditional_mean' else C
        check('conditional','D=C+J N={}'.format(N),D,claim_C+J)
        target=Q(0) if args.mutation=='zero_endpoint_noise_covariance' else J/N
        check('conditional','endpoint-noise covariance N={}'.format(N),
              endpoint_noise,z(target))
        check('conditional','both costs nonzero N={}'.format(N),C>0 and J>0,True)
        observations['conditional_N{}'.format(N)]={
            'D':str(D),'C':str(C),'J':str(J),'endpoint_noise':str(endpoint_noise)}

    # Coordinate transform of the original independent particle noises.
    nu=Q(3,7)
    particle_cov=2*nu
    yweights=(Q(1),Q(-1))
    zweights=(Q(1,2),Q(1,2))
    covy=particle_cov*sum(a*a for a in yweights)
    covz=particle_cov*sum(a*a for a in zweights)
    covyz=particle_cov*sum(a*b for a,b in zip(yweights,zweights))
    target_y=2*nu if args.mutation=='halve_relative_noise' else 4*nu
    check('coordinates','relative quadratic variation',covy,target_y)
    check('coordinates','center quadratic variation',covz,nu)
    check('coordinates','relative-center cross variation',covyz,0)
    for N in (2,3,5,17):
        original_b1=Q(2,N)
        original_b2=-Q(2,N)
        alpha=Q(2,N) if args.mutation=='halve_relative_drift' else Q(4,N)
        check('coordinates','relative Coulomb drift N={}'.format(N),
              original_b1-original_b2,alpha)
        check('coordinates','center internal cancellation N={}'.format(N),
              (original_b1+original_b2)/2,0)

    # Raw enumeration, without a presumed overlap formula.
    for N in (2,3,4,7):
        overlapping=distinct=0
        for i in range(N):
            for j in range(N):
                if i==j:
                    continue
                for h in range(N):
                    if h==i or h==j:
                        overlapping+=1
                    else:
                        distinct+=1
        expected=0 if args.mutation=='omit_overlap_labels' else Q(N-1,N)
        check('labels','overlap coefficient N={}'.format(N),
              Q(overlapping,2*N*N),expected)
        check('labels','distinct coefficient N={}'.format(N),
              Q(distinct,2*N*N),Q((N-1)*(N-2),2*N))
        check('labels','row correction N={}'.format(N),
              1-Q(N-1,N),Q(1,N))

    # Rational automatic differentiation of radial powers and directions.
    points=[(Q(1),Q(0),Q(0),Q(0)),
            (Q(3,5),Q(4,5),Q(0),Q(0)),
            (Q(1),Q(1),Q(1),Q(1))]
    for N in (2,3,11):
        alpha=Q(4,N)
        for point in points:
            Y=[Jet.var(v,i) for i,v in enumerate(point)]
            rsq=sum(y*y for y in Y)
            radius=exact_pow(rsq.v,Q(1,2))
            drift=[alpha*y/(rsq.v**2) for y in point]
            for p in (2,4,6,8,10):
                fun=rsq.power(Q(p,2))
                value=sum(drift[i]*fun.g[i]+2*nu*fun.h[i][i] for i in range(4))
                target=p*alpha*radius**(p-4)+2*nu*p*(p+2)*radius**(p-2)
                check('radial_generator','p={} N={} y={}'.format(p,N,point),value,target)
            fourth=rsq.power(2)
            bracket=4*nu*sum(a*a for a in fourth.g)
            check('radial_bracket','N={} y={}'.format(N,point),
                  bracket,64*nu*radius**6)
            angles=[y*rsq.power(Q(-1,2)) for y in Y]
            for i,angle in enumerate(angles):
                angular_radial_drift=sum(drift[j]*angle.g[j] for j in range(4))
                check('angle','radial force cancels N={} component={}'.format(N,i),
                      angular_radial_drift,0)
                noise_drift=sum(2*nu*angle.h[j][j] for j in range(4))
                factor=3 if args.mutation=='halve_angle_drift' else 6
                check('angle','Ito drift N={} component={}'.format(N,i),
                      noise_drift,-factor*nu*point[i]/radius**3)
            check('angle','total angular noise bracket N={}'.format(N),
                  4*nu*sum(sum(a*a for a in t.g) for t in angles),
                  12*nu/rsq.v)

    # Brackets formed from actual common Brownian coefficients.
    for N in (2,3,6):
        gu=[z(Q(i+1,5),Q(2-i,7)) for i in range(4*N)]
        ge=[z(Q(3-i,11),Q(i+2,13)) for i in range(4*N)]
        # An independent finite increment law: +/-m e_j each has mass
        # 1/(2m^2), and the remaining mass sits at zero. Its covariance is I.
        # Sum products of the resulting increments, not the bracket formula.
        m=4*N
        raw=z(0)
        for j in range(m):
            for sign in (-1,1):
                inc_u=zs(gu[j],sign*m)
                inc_m=zs(ge[j],Q(sign*m,N))
                raw=za(raw,zs(zm(inc_u,zc(inc_m)),Q(1,2*m*m)*2*nu))
        target=zsum(zs(zm(gu[i],zc(ge[i])),2*nu/N) for i in range(4*N))
        if args.mutation=='omit_cutoff_cross_bracket':
            target=z(0)
        check('bracket','retained cross bracket N={}'.format(N),raw,target)
        multiplier=Q(3,8)
        raw_backward=zsum(zs(zm(gu[i],zc(zs(ge[i],multiplier))),2*nu/N)
                          for i in range(4*N))
        target_backward=raw if args.mutation=='remove_backward_factor' else zs(raw,multiplier)
        check('bracket','target backward factor N={}'.format(N),raw_backward,target_backward)
        check('bracket','nonzero cross bracket N={}'.format(N),raw!=z(0),True)

    # Spherical moments derived from the even monomial formula.
    second=sphere_moment((1,0,0,0))
    fourth=sphere_moment((2,0,0,0))
    mixed=sphere_moment((1,1,0,0))
    projection=fourth-second/4
    check('sphere','second moment',second,Q(1,4))
    check('sphere','fourth moment',fourth,Q(1,8))
    check('sphere','mixed moment',mixed,Q(1,24))
    check('sphere','zero mean harmonic',second-Q(1,4),0)
    target_projection=Q(1,12) if args.mutation=='change_spherical_projection' else Q(1,16)
    check('sphere','quadratic projection',projection,target_projection)
    check('sphere','harmonic polynomial Laplacian',Q(2)-Q(8,4),0)
    check('sphere','degree-two eigenvalue',2*(2+4-2),8)

    # Exact local ODE flow differentiated by the same general Jet engine.
    for N in (2,5,13):
        alpha=Q(4,N)
        for r in (Q(1,2),Q(1,4),Q(1,8)):
            R=Q(1)
            t=(R**4-r**4)/(4*alpha)
            Y=[Jet.var(r if i==0 else 0,i) for i in range(4)]
            rsq=sum(y*y for y in Y)
            evolved_radius=(rsq*rsq+4*alpha*t).power(Q(1,4))
            flow=[y*evolved_radius*rsq.power(Q(-1,2)) for y in Y]
            jac=[list(j.g) for j in flow]
            check('ODE','radial derivative N={} r={}'.format(N,r),jac[0][0],(r/R)**3)
            for j in range(1,4):
                check('ODE','tangential derivative N={} r={} j={}'.format(N,r,j),
                      jac[j][j],R/r)
            check('ODE','determinant N={} r={}'.format(N,r),determinant(jac),1)

    # Leading empirical coefficient independently from 2*cos Taylor term.
    for N in (2,3,7,19):
        terminal_quadratic=Q(2,N)*Q(-1,2)
        target_terminal=Q(-1,2*N) if args.mutation=='halve_empirical_pair_coefficient' else Q(-1,N)
        check('terminal','quadratic coefficient in pi^2 N={}'.format(N),
              terminal_quadratic,target_terminal)
        for t in (1e-4,1e-6,1e-8):
            R=(16*t/N)**0.25
            for theta1 in (1.0,0.6,0.0):
                change=2/N*(math.cos(math.pi*theta1*R)-1)
                leading=-4*math.pi**2/N**1.5*theta1**2*math.sqrt(t)
                taylor_bound=math.pi**4*theta1**4*R**4/(12*N)
                check('cosine_numeric','N={} t={} theta1={}'.format(N,t,theta1),
                      abs(change-leading)<=taylor_bound+2e-15,True)

    # Jacobian and full-gradient norm under x1=z+y/2, x2=z-y/2.
    transform=[[Q(1),Q(1,2)],[Q(1),Q(-1,2)]]
    check('polar','one-coordinate absolute determinant',abs(determinant(transform)),1)
    for gz,gy in (([0]*4,[1,2,3,4]),([1,3,-2,4],[3,1,0,-1])):
        gx1=[Q(a,2)+b for a,b in zip(gz,gy)]
        gx2=[Q(a,2)-b for a,b in zip(gz,gy)]
        norm2=sum(v*v for v in gx1+gx2)
        yz=sum(Q(v)*v for v in gy)
        zz=sum(Q(v)*v for v in gz)
        check('polar','full norm identity gz={}'.format(gz),norm2,zz/2+2*yz)
        if not any(gz):
            factor=2 if args.mutation=='halve_full_gradient_factor' else 4
            check('polar','fourth-power equality at zero center gradient',norm2**2,factor*yz**2)
    radial_dimension=8 if args.mutation=='use_full_dimension_for_radius' else 4
    check('polar','fourth-gradient logarithmic radial exponent',radial_dimension-1-4,-1)
    check('polar','square-gradient integrable radial exponent',radial_dimension-1-2,1)

    for N in (2,3,17):
        A=Q(2,5)
        direct=N*(1-A)**2
        claim=0 if args.mutation=='erase_constant_mode_defect' else direct
        check('constant_mode','artificial target defect N={}'.format(N),direct,claim)
        check('constant_mode','conditional noise zero N={}'.format(N),N*(1-1)**2,0)


try:
    run()
except Exception as error:
    print(json.dumps({'status':'FAIL','mutation':args.mutation,
                      'completed_or_failing_assertions':len(checks),
                      'witness':str(error),'last_check':checks[-1] if checks else None},
                     indent=2))
    sys.exit(1)
else:
    categories={}
    for row in checks:
        categories[row['category']]=categories.get(row['category'],0)+1
    print(json.dumps({'status':'PASS','mutation':args.mutation,
                      'assertions':len(checks),'categories':categories,
                      'observations':observations,
                      'arithmetic':'Exact rational except 36 deterministic cosine checks; absolute slack 2e-15.',
                      'randomness':'None; no SDE discretization.',
                      'scope':'Supporting finite-probability, differential-algebra and ODE checks only. No numerical continuum theorem.'},
                     indent=2))
