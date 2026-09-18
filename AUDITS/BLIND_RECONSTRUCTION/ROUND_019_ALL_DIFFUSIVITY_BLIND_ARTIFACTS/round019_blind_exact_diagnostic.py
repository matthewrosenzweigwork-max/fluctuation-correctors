#!/usr/bin/env python3
"""Fresh exact coefficient diagnostics for AUD057; no earlier checker inputs.

Only Python standard library and exact Fraction arithmetic. No stochastic
simulation, floating-point inference, outside source, or analytic certification.
Fourier generator units divide spatial derivatives by 2*pi, so D=k^2*g_hat;
restoring physical units multiplies drift/noise rates by (2*pi)^2 consistently.
Covariance probes use independent real normalized modes and rational semigroup
attenuations q**L on a common time grid Delta=-log(q).
"""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import hashlib
import json

COUNTS = Counter()
MUTATIONS = Counter()

def check(condition, category):
    if not condition:
        raise AssertionError(category)
    COUNTS[category] += 1

def killed(wrong, expected, category):
    if wrong == expected:
        raise AssertionError('mutation survived: ' + category)
    MUTATIONS[category] += 1


def generator_haar(N, k, g, nu, denominator=None, interaction=None):
    """Constant Fourier coefficient of literal generator of full |eta_k|^2."""
    den = N*N if denominator is None else denominator
    scale = F(1,N) if interaction is None else interaction
    answer = F(0)
    diffusion = F(0)
    # Keep i=j constant self terms, distinct pairs, and every force label.
    for left in range(N):
        for right in range(N):
            alpha = [0]*N
            alpha[left] += k
            alpha[right] -= k
            observable_coefficient = F(1,den)
            if all(a == 0 for a in alpha):
                diffusion += -nu * sum(a*a for a in alpha)*observable_coefficient
            for i in range(N):
                for j in range(N):
                    if i == j:
                        continue
                    for p in (-k,k):
                        beta = alpha.copy()
                        beta[i] += p
                        beta[j] -= p
                        if all(a == 0 for a in beta):
                            # (-i*p*g_hat) * (i*alpha_i) = p*alpha_i*g_hat.
                            answer += observable_coefficient*scale*alpha[i]*p*g
    return answer+diffusion, diffusion

GENERATOR_CASES=[]
for N in range(2,8):
    for k in (1,2,3):
        g=F(1,k+2)
        D=k*k*g
        for nu in (F(0),F(1,3),F(1),F(7),F(128)):
            value,diff=generator_haar(N,k,g,nu)
            target=-2*F(N-1,N*N)*D
            check(value == target,'literal initial generator')
            check(diff == 0,'initial diffusion cancellation')
            b=F(1) if nu<=1 else 1/nu
            check(N*b*value - (-2*b*D) == 2*b*D/N,
                  'finite N versus target derivative')
            wrong_den,_=generator_haar(N,k,g,nu,N*(N-1))
            killed(wrong_den,target,'ordered deleted denominator N(N-1)')
            wrong_force,_=generator_haar(N,k,g,nu,interaction=F(1))
            killed(wrong_force,target,'missing interaction 1/N')
            GENERATOR_CASES.append({'N':N,'k':k,'nu':str(nu),'derivative':str(value)})


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]

def gram_add(matrix, weight, vector):
    for i in range(len(vector)):
        for j in range(len(vector)):
            matrix[i][j] += weight*vector[i]*vector[j]

def quadratic(matrix, vector):
    return sum((matrix[i][j]*vector[i]*vector[j]
                for i in range(len(vector)) for j in range(len(vector))),F(0))

TIME_LISTS=[(0,1,1,3,4),(0,0,0,0,0),(2,2,3,3,4),(0,1,2,3,4)]
AMPLITUDES=[(F(1),F(-2),F(3,2),F(1,3),F(0)),
            (F(-1),F(1),F(2,3),F(-3),F(0)),
            (F(2),F(1,2),F(-1),F(2),F(0))]
MODE_DATA=[(1,1),(3,2),(2,5)]
COVARIANCE_CASES=[]
for nu in (0,1,2,9,64):
    b=F(1,max(1,nu))
    for base in (F(1,2),F(2,3)):
        for times in TIME_LISTS:
            m=len(times)
            closed=zeros(m)
            gram=zeros(m)
            initial=zeros(m)
            bracket=zeros(m)
            columns=[]
            for (D,a),amps in zip(MODE_DATA,AMPLITUDES):
                r=nu*a
                L=D+r
                z=base**L
                vi=[amps[i]*z**times[i] for i in range(m)]
                gram_add(initial,b,vi)
                gram_add(gram,b,vi)
                columns.append((b,vi))
                for level in range(1,max(times)+1):
                    v=[amps[i]*z**(times[i]-level) if times[i]>=level else F(0)
                       for i in range(m)]
                    weight=b*F(r,L)*(1-z*z)
                    check(weight>=0,'nonnegative increment Gram weight')
                    gram_add(bracket,weight,v)
                    gram_add(gram,weight,v)
                    columns.append((weight,v))
                for i in range(m):
                    for j in range(m):
                        closed[i][j] += b*amps[i]*amps[j]*(
                            F(D,L)*z**(times[i]+times[j])+
                            F(r,L)*z**abs(times[i]-times[j]))
            for i in range(m):
                for j in range(m):
                    check(closed[i][j]==gram[i][j],'complete covariance identity')
                    check(gram[i][j]==initial[i][j]+bracket[i][j],
                          'initial plus martingale split')
                    check(closed[i][j]==closed[j][i],'real covariance symmetry')
                energy=sum((amps[i]**2 for amps in AMPLITUDES),F(0))
                check(0<=closed[i][i]<=b*energy,'uniform high noise diagonal bound')
                check(closed[4][i]==0,'constant test degeneracy')
            for vector in ((1,0,0,0,0),(1,-1,2,-2,3),(0,1,1,0,0),(-3,2,1,4,0)):
                value=quadratic(closed,vector)
                gram_value=sum((w*sum((v[i]*vector[i] for i in range(m)),F(0))**2
                                for w,v in columns),F(0))
                check(value==gram_value and value>=0,'exact covariance quadratic Gram check')
            if nu==0:
                check(bracket==zeros(m),'exact zero noise martingale')
                check(closed==initial,'zero noise covariance')
            if times[0]==0:
                check(all(bracket[0][j]==0 for j in range(m)),'zero time cross bracket')
            if max(times)>0:
                active=next(i for i,t in enumerate(times) if t>0 and i<4)
                if nu>0:
                    killed(initial[active][active]+bracket[active][active]/2,
                           closed[active][active],'missing Brownian factor two')
                    killed(bracket[active][active],closed[active][active],
                           'omitted initial vector')
                    if nu>1:
                        killed(closed[active][active]/b,closed[active][active],
                               'missing b normalization')
                    D,a=MODE_DATA[0]
                    L=D+nu*a
                    z=base**L
                    t=times[active]
                    correct=b*(F(D,L)*z**(2*t)+F(nu*a,L))
                    wrong=b*(F(D,L)*z**(2*t)+F(nu*a,L)*z**(2*t))
                    killed(wrong,correct,'sum replaces absolute time difference')
            COVARIANCE_CASES.append({'nu':nu,'base':str(base),'times':times,
                                     'trace':str(sum(closed[i][i] for i in range(m)))})

# Exact mixed moments in a conditional Gaussian martingale toy.
# U is equiprobable +/-1; B is independent centered variance-one Gaussian.
a={-1:F(1),1:F(2)}
EU=sum((F(u,2) for u in a),F(0))
EM2=sum((a[u]**2/2 for u in a),F(0))
EUM2=sum((u*a[u]**2/2 for u in a),F(0))
check(EU==0 and EM2==F(5,2),'conditional Gaussian moment normalization')
check(EUM2==F(3,2),'initial martingale dependence witness')
check(sum((F(1,2)*abs(a[u]**2-EM2) for u in a),F(0))==F(3,2),
      'random bracket error remains visible')
killed(EU*EM2,EUM2,'zero cross covariance implies independence')

# Scaling and the upper-noise normalization are checked exactly.
for d in range(3,10):
    for s in (F(1,2),F(1),F(d-2)):
        if not 0<s<=d-2:
            continue
        alpha=F(d,2)-s/2
        q=1-s/d
        check(-1+s/d == -2*alpha/d == -q,'balanced singular source powers')
        if s<F(d,2):
            check(s/d-F(1,2)<0,'strict source residual threshold')
        for nu in (F(0),F(1,10),F(1),F(7),F(10**8)):
            b=F(1) if nu<=1 else 1/nu
            check(0<=nu*b<=1,'all finite noise bracket normalization')

output={
 'status':'PASS',
 'evidence_label':'EXACT_FINITE_DIAGNOSTICS_NOT_ANALYTIC_CERTIFICATION',
 'assertions':sum(COUNTS.values()),
 'categories':dict(COUNTS),
 'killed_mutations':dict(MUTATIONS),
 'mutation_rejections':sum(MUTATIONS.values()),
 'generator_cases':GENERATOR_CASES,
 'covariance_cases':COVARIANCE_CASES,
 'martingale_toy':{'E_U_M2':str(EUM2),'E_U_times_E_M2':str(EU*EM2),
                   'label':'logical dependence control, not a particle counterexample'},
 'arithmetic':'exact fractions; no random seed or floating-point tolerances',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
Path(__file__).with_name('diagnostic_results.json').write_text(json.dumps(output,indent=2)+'\n')
print('PASS:',output['assertions'],'exact assertions in',len(COUNTS),'categories;',
      output['mutation_rejections'],'mutation rejections in',len(MUTATIONS),'classes')
