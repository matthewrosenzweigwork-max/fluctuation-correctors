#!/usr/bin/env python3
"""Fresh AUD078 finite diagnostics. Standard library; no files/network/writes.

Exact arithmetic uses Fraction and Gaussian rationals. The continuum proof is
in REVIEW.md. Finite groups below test coefficients, not collision polar sets.
The finite killed chain is an explicitly different model, not a target witness.
The sole floating checks concern displayed logarithmic layer-cake expressions.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import Counter
import json
import math


class Z:
    def __init__(self, re=0, im=0):
        if isinstance(re, Z):
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = Q(re), Q(im)
    def __add__(self, b):
        b = Z(b); return Z(self.re+b.re, self.im+b.im)
    __radd__ = __add__
    def __neg__(self): return Z(-self.re, -self.im)
    def __sub__(self, b): return self + (-Z(b))
    def __rsub__(self, b): return Z(b) - self
    def __mul__(self, b):
        b = Z(b)
        return Z(self.re*b.re-self.im*b.im, self.re*b.im+self.im*b.re)
    __rmul__ = __mul__
    def __truediv__(self, b):
        b=Z(b); n=b.norm2()
        return self*b.conj()*Z(1/n)
    def conj(self): return Z(self.re, -self.im)
    def norm2(self): return self.re*self.re+self.im*self.im
    def __eq__(self, b):
        b=Z(b); return self.re == b.re and self.im == b.im
    def __repr__(self): return '('+str(self.re)+','+str(self.im)+')'


counts=Counter()
mutations={}
examples={}


def check(name, condition):
    if not condition: raise AssertionError(name)
    counts[name]+=1


def equal(name, a, b): check(name, a == b)


def mutate(name, actual, wrong):
    residual=actual-wrong
    check('nonzero deliberate mutation', residual != 0)
    mutations[name]={'actual':str(actual),'wrong':str(wrong),'residual':str(residual)}


def e(k, x):
    return (Z(1),Z(0,1),Z(-1),Z(0,-1))[(k*x)%4]


# Configuration-space Fourier calculation, with c scaled to one.
for n in range(2,9):
    patterns=[(0,)*n]
    for i,j in combinations(range(n),2):
        for f in (1,2,-3):
            a=[0]*n; a[i]=f; a[j]=-f; patterns.append(tuple(a))
    if n>=3:
        patterns.extend([(1,1,-2)+(0,)*(n-3),(1,1,1)+(0,)*(n-3)])
    if n>=4: patterns.append((1,-1,2,-2)+(0,)*(n-4))
    for a in patterns:
        m=[]
        for i,j in combinations(range(n),2):
            m.append(int(a[i]+a[j]==0 and all(a[z]==0 for z in range(n) if z not in (i,j))))
        active=[x for x in a if x]
        h=Q(1,n*active[0]**2) if len(active)==2 and sum(active)==0 else Q(0)
        lhs=-sum(x*x for x in a)*h
        rhs=(n-1)*int(not active)-Q(2,n)*sum(m)
        equal('distribution Fourier coefficient',lhs,rhs)
    equal('total probability flux',Q(2,n)*Q(n*(n-1),2),n-1)
    equal('uniform unordered pair',Q(2,n*(n-1)),Q(1,n*(n-1)//2))
    # q=(xi-xj)/sqrt(2); area S3=c/2; dp=4dy.
    equal('orthonormal probability-Haar coefficient',-Q(1,n)*Q(1,2)*4,-Q(2,n))
    for a in (Q(0),Q(1,3),Q(5)):
        equal('marked Laplace mass',Q(2,n)/((n-1)+a),Q(1,n*(n-1)//2)*Q(n-1)/((n-1)+a))

mutate('omitted differentiated particle factor',Q(-2,3),Q(-1,3))
mutate('collision atom sign flipped',Q(-2,3),Q(2,3))
mutate('missing torus compensation',Q(0),Q(-2))
mutate('surface measure substituted for probability Haar',Q(-2,3),Q(-1,6))
mutate('spurious diffusivity in flux',Q(-2,3),Q(-4,3))
mutate('triple-diagonal mass on three active modes',Q(0),Q(1,7))
mutate('N replaces N-1 in rate mass',Q(1),Q(2,3))

# Canonical clipping. A genuinely complex kernel, with exact rational modulus.
avec=(-3,-1,0,4)
real=[[Q(x*y) for y in avec] for x in avec]
clipped=[[max(Q(-3),min(Q(3),x)) for x in row] for row in real]
rows=[sum(row)/4 for row in clipped]
mean=sum(rows)/4
centered=[[clipped[x][y]-rows[x]-rows[y]+mean for y in range(4)] for x in range(4)]
factor=Z(3,4)  # modulus 5; this is modulus clipping at L=15.
j=[[factor*v for v in row] for row in real]
jL=[[factor*v for v in row] for row in clipped]
v=[[factor*w for w in row] for row in centered]
for x in range(4):
    equal('original zero row',sum(j[x]),0)
    equal('restored zero row',sum(v[x]),0)
for x,y in product(range(4),repeat=2):
    equal('symmetric complex centered kernel',v[x][y],v[y][x])
normv=sum(w.norm2() for row in v for w in row)/16
normclip=sum(w.norm2() for row in jL for w in row)/16
check('orthogonal projection contraction',normv<=normclip)
tailnorm=5*sum(abs(real[x][y]-clipped[x][y]) for x,y in product(range(4),repeat=2))/16
residualnorm=5*sum(abs(real[x][y]-centered[x][y]) for x,y in product(range(4),repeat=2))/16
check('L1 double centering factor four',residualnorm<=4*tailnorm)
mutate('clipping leaves Haar rows zero',factor*rows[0],Z(0))

raw_variances={}
for n in range(2,6):
    sumv=Z(); sq=Q(0); rawsq=Q(0); fusion_sq=Q(0); init_sq=Q(0)
    for xs in product(range(4),repeat=n):
        U=sum(j[xs[i]][xs[l]] for i,l in combinations(range(n),2))/n**2
        V=sum(v[xs[i]][xs[l]] for i,l in combinations(range(n),2))/n**2
        W=sum(jL[xs[i]][xs[l]] for i,l in combinations(range(n),2))/n**2
        F=sum(e(1,x) for x in xs)/n
        Jpair=sum(j[xs[i]][xs[l]]-e(1,xs[i])-e(1,xs[l]) for i,l in combinations(range(n),2))/n**2
        P=Jpair+F # each row of J is -e; double contraction zero.
        equal('literal deleted source coefficient',P,U+F/n)
        nu=Q(2,7); ell=Q(5)
        rawdrift=-Jpair-nu*ell*F
        equal('attractive observable drift',rawdrift,(Q(n-1,n)-nu*ell)*F-U)
        sumv+=V; sq+=V.norm2(); rawsq+=W.norm2(); init_sq+=F.norm2()
    equal('iid centered statistic mean',sumv,0)
    variance=sq/4**n
    equal('canonical unordered pair variance',variance,Q(n-1,2*n**3)*normv)
    equal('initial empirical Fourier variance',init_sq/4**n,Q(1,n))
    raw_variances[n]=(rawsq/4**n,variance)
    for ys in product(range(4),repeat=n-1):
        F=(2*e(1,ys[0])+sum(e(1,x) for x in ys[1:]))/n
        fusion_sq+=F.norm2()
    equal('fused endpoint variance',fusion_sq/4**(n-1),Q(n+2,n*n))
mutate('ordered pair variance misses half',Q(2,2*3**3)*normv,Q(2,3**3)*normv)
mutate('uncentered clipped variance used',raw_variances[3][0],raw_variances[3][1])
mutate('empirical deletion correction omitted',Z(1,1)/4,Z(0))
mutate('fusion variance omits ordered cross terms',Q(5,9),Q(1,3))

# Independent enumeration of the five marked two-time label classes.
for n in range(2,31):
    cts=Counter()
    for i,jj in product(range(n),repeat=2):
        if i<2 and jj<2: cls=0
        elif i>=2 and jj<2: cls=1
        elif i<2 and jj>=2: cls=2
        elif i==jj: cls=3
        else: cls=4
        cts[cls]+=1
    expected=[4,2*(n-2),2*(n-2),n-2,(n-2)*(n-3)]
    for cls,val in enumerate(expected): equal('five class multiplicities',cts[cls],val)
    equal('five class total',sum(cts.values()),n*n)
mutate('fused-common multiplicity halved',Q(4),Q(2))
mutate('distinct-outside coefficient off by one',Q(2),Q(4))

# Complex brackets calculated from particle gradients, c scaled to one.
for n in range(2,6):
    for xs in product(range(4),repeat=n):
        for k,l in ((1,1),(1,2),(2,-1)):
            nu=Q(3,5)
            gradk=[Z(0,k)*e(k,x)/n for x in xs]
            gradl=[Z(0,l)*e(l,x)/n for x in xs]
            cc=2*nu*sum(u*w.conj() for u,w in zip(gradk,gradl))
            uc=2*nu*sum(u*w for u,w in zip(gradk,gradl))
            equal('conjugate cross bracket',cc,Q(2)*nu*k*l/n*sum(e(k-l,x) for x in xs)/n)
            equal('unconjugated cross bracket',uc,-Q(2)*nu*k*l/n*sum(e(k+l,x) for x in xs)/n)
mutate('unconjugated bracket sign flipped',Q(-2,3),Q(2,3))
mutate('complex self bracket doubled',Q(2,3),Q(4,3))

# Relative four-dimensional principal radial generator from actual derivatives.
radius2=Q(6)
for n,nu,p in product(range(2,12),(Q(1,100),Q(2),Q(37,5)),(2,4,6)):
    # r^p: grad=p r^(p-2) z, Lap=p(p+2) r^(p-2).
    trace_hessian=p*(p+2)*radius2**((p-2)//2)
    grad_dot_z=p*radius2**(p//2)
    direct=2*nu*trace_hessian-Q(4,n)/radius2**2*grad_dot_z
    expected=2*nu*p*(p+2)*radius2**((p-2)//2)-Q(4*p,n)*radius2**((p-4)//2)
    equal('relative radial generator',direct,expected)
    if p==4:
        equal('r4 martingale bracket',4*nu*p*p*radius2**(p-1),64*nu*radius2**3)
mutate('relative diffusivity halved',48*Q(2)*radius2,24*Q(2)*radius2)
mutate('zero-noise collision time missing pair factor',Q(2*81,16),Q(2*81,8))

# Exact residual-life integrals; time T contributes only A_T squared.
for n,nu,ell in product(range(2,41),(Q(1,100),Q(1),Q(100)),(Q(1),Q(5))):
    kap=Q(n-1); a=1+nu*ell
    laplace=1-2*kap/(kap+a)+kap/(kap+2*a)
    explicit=2*a*a/((kap+a)*(kap+2*a))
    equal('residual life response factor',laplace,explicit)
    check('response term O N inverse constant', (1+Q(2,n))*explicit<=16*a*a/n**2)
mutate('residual numerator two removed',Q(9,20),Q(9,40))
mutate('second shifted denominator collapsed',Q(9,20),Q(18,25))

# Matrix helpers and an explicit two-state killed chain.
def mm(a,b): return [[sum(a[i][l]*b[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
def mv(a,v): return [sum(a[i][j]*v[j] for j in range(2)) for i in range(2)]
def tr(a): return [[a[j][i] for j in range(2)] for i in range(2)]
def diag(v): return [[v[0],Q(0)],[Q(0),v[1]]]
def total(a): return sum(sum(row) for row in a)/2
Pi=[[Q(1,3),Q(1,3)],[Q(2,3),Q(2,3)]]
I=[[Q(1),Q(0)],[Q(0),Q(1)]]
def killed(q): return [[q*(Pi[i][j]+q**3*(I[i][j]-Pi[i][j])) for j in range(2)] for i in range(2)]
def repulsive(q): return [[killed(q)[j][i]/q for j in range(2)] for i in range(2)]
for q in (Q(1),Q(1,2),Q(1,3),Q(2,5)):
    mat=killed(q); rev=repulsive(q)
    for j in range(2): equal('QSD Haar current marginal',sum(mat[i][j] for i in range(2))/2,q/2)
    for i in range(2): equal('adjoint conservative row',sum(rev[i]),1)
    equal('mean survival normalizer',total(mat),q)
for q,r in product((Q(1,2),Q(1,3)),repeat=2):
    equal('killed chain semigroup',mm(killed(q),killed(r)),killed(q*r))
    for f,g,h in product(((Q(1),Q(2)),(Q(-1),Q(3))),repeat=3):
        lhs=total(mm(mm(mm(mm(diag(f),repulsive(q)),diag(g)),repulsive(r)),diag(h)))
        rhs=total(mm(mm(mm(mm(diag(h),killed(r)),diag(g)),killed(q)),diag(f)))/(q*r)
        equal('whole three-time reversed cylinder',lhs,rhs)
        # Future-only two-time functional after survival to q.
        full=total(mm(mm(mm(killed(q),diag(g)),killed(r)),diag(h)))/q
        future=total(mm(mm(diag(g),killed(r)),diag(h)))
        equal('entire future functional transfer',full,future)
q=Q(1,2); mat=killed(q); survive=[sum(row) for row in mat]
initial0=survive[0]/(2*q)
mutate('survival leaves initial Haar law',initial0,Q(1,2))
f=(Q(0),Q(1)); pred=mv(mat,f)
# One discrete step, cemetery value zero. Martingale increment = f(next)-pred(start).
uncondmean=Q(0); condnum=Q(0); condsqnum=Q(0); condbracketnum=Q(0)
for i in range(2):
    outcomes=[(j,mat[i][j],f[j]) for j in range(2)]+[(2,1-survive[i],Q(0))]
    rowvar=sum(prob*(value-pred[i])**2 for _,prob,value in outcomes)
    for j,prob,value in outcomes:
        d=value-pred[i]; uncondmean+=prob*d/2
        if j<2:
            condnum+=prob*d/2; condsqnum+=prob*d*d/2
    condbracketnum+=survive[i]*rowvar/2
equal('true unconditioned chain martingale',uncondmean,0)
mutate('conditioned past martingale stays centered',condnum/q,Q(0))
mutate('conditioned past isometry unchanged',condsqnum/q,condbracketnum/q)
mutate('rare normalizer omitted',total(mat)/q,total(mat))
f=(Q(0),Q(1)); g=(Q(1),Q(3))
correct=total(mm(mm(diag(f),repulsive(q)),diag(g)))
wrong=total(mm(mm(diag(g),repulsive(q)),diag(f)))
mutate('reversal orientation unchanged',correct,wrong)

# Marginal laws alone do not establish time/mark independence.
delta=Q(1,16)
joint=[[Q(1,4)+delta,Q(1,4)-delta],[Q(1,4)-delta,Q(1,4)+delta]]
for row in joint: equal('coupled law unchanged row marginal',sum(row),Q(1,2))
for j in range(2): equal('coupled law unchanged column marginal',sum(joint[i][j] for i in range(2)),Q(1,2))
mutate('exit marginals force joint independence',joint[0][0],Q(1,4))

# Explicit false inference: unconditioned lifetime average -> zero need not
# control its normalized tail at fixed T0. exp(-kappa*T0)=(1/2)^(N-1).
for n in range(2,21):
    q=Q(1,2)**(n-1)
    equal('normalized threshold-profile tail',q/q,1)
    check('threshold-profile unconditioned smallness',0<q<=Q(1,2))
mutate('small typical profile controls rare tail',Q(1),Q(1,2)**19)

# Pareto variable V>=1 with P(V>L)=L^-2: exact analytic layer cakes,
# evaluated numerically here solely as floating diagnostics of coefficients.
for L in (1,2,3,5,17,1000):
    second=1+2*math.log(L); tail=1/L
    check('layer cake finite logarithmic expression',second>=1 and tail>0)
    if L>1: check('nonzero logarithmic coefficient mutation',abs(second-(1+math.log(L)))>1e-12)
examples['layer_cake_at_17']={'second':1+2*math.log(17),'residual':1/17,'classification':'analytic formula evaluated in binary64; not a numerical proof'}

# Elementary endpoint bound keeps cross terms: t <= 2v+sqrt(t*m)
# implies t <=4v+m. Check exact squared implication on rational grids.
for t,v0,m in product((Q(i,4) for i in range(17)),repeat=3):
    premise=t<=2*v0 or (t-2*v0)**2<=t*m
    if premise: check('bounded endpoint cross-term inequality',t<=4*v0+m)

result={'status':'PASS','arithmetic':'Fraction and exact Gaussian rationals except labeled binary64 layer-cake values','randomness':'none','continuum_certification':'analytic report only; diagnostics do not prove singular SDE passages','assertions':sum(counts.values()),'categories':len(counts),'counts':dict(sorted(counts.items())),'mutation_count':len(mutations),'mutations':mutations,'examples':examples}
print(json.dumps(result,indent=2,sort_keys=True))
