#!/usr/bin/env python3
"""Fresh finite diagnostics for AUD080; exact assertions unless marked floating.
No repository or constructor code is read. Stdlib only; stdout only.
A named mathematical mutation must produce a nonzero witness and exit 7.
"""
import collections
import fractions
import itertools
import json
import math
import sys

F = fractions.Fraction
I = (F(0), F(1))
Z = (F(0), F(0))
ONE = (F(1), F(0))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sc(a,t): return (a[0]*t,a[1]*t)
def conj(a): return (a[0],-a[1])
def total(seq):
    ans=Z
    for a in seq: ans=add(ans,a)
    return ans
def char(m,x):
    v=sum(a*b for a,b in zip(m,x))%4
    return (ONE,I,neg(ONE),neg(I))[v]
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def opp(a): return tuple(-x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)
def comb(n,k): return math.comb(n,k) if n>=k else 0
mutation=sys.argv[1] if len(sys.argv)>1 else "baseline"
counts=collections.Counter()
witnesses={}
def serial(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [serial(y) for y in x]
    return x
def check(cat,a,b):
    counts[cat]+=1
    if a!=b:
        raise AssertionError(json.dumps(serial({'category':cat,'left':a,'right':b})))
def witness(name,right,wrong,data):
    if name not in witnesses and right!=wrong:
        witnesses[name]=serial({'right':right,'mutated':wrong,'difference':sub(right,wrong) if isinstance(right,tuple) else right-wrong,'data':data})
    if mutation==name and right!=wrong:
        print(json.dumps({'status':'DELIBERATE_MATHEMATICAL_MUTATION_REJECTED','mutation':name,'witness':witnesses[name]},sort_keys=True))
        sys.exit(7)

# Exhaust all four-edge multisets on four named vertices; identify all
# nonzero-row-surviving patterns and their exact ordered multiplicities.
edges=list(itertools.combinations(range(4),2))
patterns=collections.Counter()
for es in itertools.combinations_with_replacement(edges,4):
    deg=collections.Counter(v for e in es for v in e)
    if any(d==1 for d in deg.values()): continue
    mult=collections.Counter(es)
    ways=math.factorial(4)
    for n in mult.values(): ways//=math.factorial(n)
    nv=len(deg)
    if nv==2: p='same_edge'
    elif nv==3: p='adjacent_doubles' if sorted(mult.values())==[2,2] else 'doubled_triangle'
    else: p='disjoint_doubles' if sorted(mult.values())==[2,2] else 'cycle'
    patterns[p]+=ways
check('graph_enumeration',dict(patterns),{'same_edge':6,'adjacent_doubles':72,'doubled_triangle':144,'disjoint_doubles':18,'cycle':72})

# Complete iid Haar sums on cyclic compact abelian groups with rational
# even, zero-row kernels. Negative tau occurs for signed Fourier weights.
kernels=[(3,[F(2),F(-1),F(-1)]),(4,[F(3),F(1),F(-5),F(1)]),(5,[F(6),F(-4),F(1),F(1),F(-4)]),(4,[F(-3),F(-1),F(5),F(-1)])]
for q,h in kernels:
    check('zero_row',sum(h),0)
    conv=[sum(h[y]*h[(x-y)%q] for y in range(q))/q for x in range(q)]
    mu2=sum(v*v for v in h)/q
    mu4=sum(v**4 for v in h)/q
    tau=sum(h[x]**2*conv[x] for x in range(q))/q
    chi=sum(v*v for v in conv)/q
    for n in range(2,6):
        lhs=F(0)
        second=F(0)
        for xs in itertools.product(range(q),repeat=n):
            s=sum(h[(xs[i]-xs[j])%q] for i in range(n) for j in range(i+1,n))
            lhs+=s**4
            second+=s*s
        lhs/=q**n
        second/=q**n*n*n
        terms=[comb(n,2)*mu4,18*comb(n,3)*mu2**2,36*comb(n,3)*tau,18*comb(n,4)*mu2**2,72*comb(n,4)*chi]
        rhs=sum(terms)
        check('haar_graph_fourth',lhs,rhs)
        check('haar_graph_second',second,F(n-1,2*n)*mu2)
        witness('graph_triangle_18',rhs,rhs-18*comb(n,3)*tau,(q,n))
        witness('graph_adjacent_omit',rhs,rhs-terms[1],(q,n))
        witness('graph_disjoint_omit',rhs,rhs-terms[3],(q,n))
        witness('graph_cycle_24',rhs,rhs-48*comb(n,4)*chi,(q,n))
        witness('graph_ordered_energy',rhs,16*rhs,(q,n))

# Two-dimensional finite Fourier kernels embedded in T^4.
# Common c is divided out. All phases are Gaussian rationals.
a={}
for x in range(-2,3):
    for y in range(-2,3):
        if x or y: a[(x,y)]=F(1,(1+x*x+y*y)**2)
ks=[(1,0),(0,1),(1,1)]
Xall=[(0,0),(1,2),(3,1),(2,3),(1,1)]
Yall=[(1,0),(0,3),(2,2),(3,0),(2,1)]
for k in ks:
    d=norm2(k)*a.get(k,F(0))
    support=set(a)|{minus(m,k) for m in a}|{(0,0),opp(k)}
    b={m:dot(k,m)*a.get(m,F(0))-dot(k,plus(m,k))*a.get(plus(m,k),F(0))+(d if m in [(0,0),opp(k)] else 0) for m in support}
    check('b_zero_modes',b[(0,0)],0)
    check('b_zero_modes',b[opp(k)],0)
    check('b_diagonal_sum',sum(b.values()),2*d)
    for m in support: check('b_symmetry',b[m],b.get(minus(opp(k),m),F(0)))
    def j(x,y):
        dz=minus(x,y)
        ev=sub(char(k,x),char(k,y))
        raw=total(sc(mul(char(m,dz),ev),dot(k,m)*am) for m,am in a.items())
        return add(raw,sc(add(char(k,x),char(k,y)),d))
    def jf(x,y): return total(sc(mul(char(plus(k,m),x),char(opp(m),y)),bm) for m,bm in b.items())
    # Grid row integral resolves all relevant finite frequencies (period4
    # aliases may occur at upper modes but rows are independently checked
    # by the exact zero-frequency coefficients above).
    for x in Xall:
        for y in Yall:
            check('direct_fourier_kernel',j(x,y),jf(x,y))
    for n in range(2,6):
        X=Xall[:n];Y=Yall[:n]
        def z(m,C): return sc(total(char(m,x) for x in C),F(1,n))
        ur=sc(total(j(X[i],X[jj]) for i in range(n) for jj in range(n) if i!=jj),F(1,2*n*n))
        full=sc(total(sc(mul(z(plus(k,m),X),z(opp(m),X)),bm) for m,bm in b.items()),F(1,2))
        rhs=sub(full,sc(z(k,X),d/n))
        check('smooth_deletion',ur,rhs)
        witness('smooth_self_omit',ur,full,(k,n))
        witness('smooth_self_sign',ur,add(full,sc(z(k,X),d/n)),(k,n))
        witness('ordered_half_omit',ur,sc(rhs,2),(k,n))
        for mixed,C in [(False,X),(True,Y)]:
            over=sc(total(mul(j(X[i],X[jj]),conj(char(k,C[i]))) for i in range(n) for jj in range(n) if i!=jj),F(1,n*(n-1)))
            tri=sc(total(mul(j(X[i],X[jj]),conj(char(k,C[l]))) for i in range(n) for jj in range(n) for l in range(n) if len({i,jj,l})==3),F(1,n*(n-1)*(n-2))) if n>=3 else Z
            p=F((n-1)*(n-2),2*n)
            lhs=sc(mul(ur,conj(z(k,C))),n)
            rhs=add(sc(over,F(n-1,n)),sc(tri,p))
            check('mixed_label_counts' if mixed else 'current_label_counts',lhs,rhs)
            witness('triple_prefactor_twice',lhs,add(sc(over,F(n-1,n)),sc(tri,2*p)),(k,n,mixed))
            witness('overlap_missing_orientation',lhs,add(sc(over,F(n-1,2*n)),sc(tri,p)),(k,n,mixed))
            if not mixed:
                spectral=sc(total(sc(mul(z(m,X),conj(z(m,X))),bm) for m,bm in b.items()),F(n,n-1))
                check('spectral_overlap',over,sub(spectral,(F(2*d,n-1),F(0))))
                witness('overlap_self_omit',over,spectral,(k,n))
            else:
                mixed_over=over
            if n>=3:
                if not mixed: current_tri=tri
                else:
                    u=F(2,3);AA=F(1,5)
                    correct=sc(sub(sc(current_tri,u*u),sc(tri,AA*u)),p)
                    witness('merge_time_weights',correct,sc(sub(sc(current_tri,u*u),sc(tri,u*u)),p),(k,n))
                    witness('initial_tag_replaced',correct,sc(sub(sc(current_tri,u*u),sc(current_tri,AA*u)),p),(k,n))
        ct=sc(total(mul(char(k,X[i]),conj(char(k,X[jj]))) for i in range(n) for jj in range(n) if i!=jj),F(1,n*(n-1)))
        st=sc(total(mul(char(k,X[i]),conj(char(k,Y[i]))) for i in range(n)),F(1,n))
        ot=sc(total(mul(char(k,X[i]),conj(char(k,Y[jj]))) for i in range(n) for jj in range(n) if i!=jj),F(1,n*(n-1)))
        check('current_row_deletion',ct,sc(sub(sc(mul(z(k,X),conj(z(k,X))),n),ONE),F(1,n-1)))
        mx=sc(mul(z(k,X),conj(z(k,Y))),n)
        check('mixed_row_deletion',ot,sc(sub(mx,st),F(1,n-1)))
        witness('mixed_same_label_omit',ot,sc(mx,F(1,n-1)),(k,n))
        if n>=3:
            rawrow=sc(total(mul(add(char(k,X[i]),char(k,X[jj])),conj(char(k,Y[l]))) for i in range(n) for jj in range(n) for l in range(n) if len({i,jj,l})==3),F(1,n*(n-1)*(n-2)))
            check('tail_row_twice',rawrow,sc(ot,2))
            witness('tail_row_factor_one',rawrow,ot,(k,n))
        # Actual energy and observable use same noise; the normalized
        # deterministic cross integrand sum grad H dot grad e is -N times
        # the literal raw pair source, not zero.
        raw_source=sub(ur,sc(z(k,X),d*F(n-1,n)))
        witness('energy_noise_cross_zero',sc(raw_source,-n),Z,(k,n))

# Initial Fourier fourth moment: exact character sums on C5 for n<=5.
for n in range(2,6):
    # independent combinatorial zero exponent count; no complex rounding
    cnt=0
    for i,j,p,q in itertools.product(range(n),repeat=4):
        bal=collections.Counter((i,j))
        bal.subtract((p,q))
        cnt+=all(v==0 for v in bal.values())
    check('initial_mode_fourth',F(cnt,n*n),F(2)-F(1,n))
    witness('initial_all_equal_twice',F(cnt,n*n),F(2),n)

# Time-zero indicator versus a future event: E=(W^2-1)/2 and its bracket
# at unit time, selected on W_1>0 is not a suitable easy finite counter;
# use a two-step symmetric random walk with predictable second multiplier.
# For M=epsilon1+2epsilon2, bracket=5; event M=3 is terminal.
paths=list(itertools.product([-1,1],repeat=2))
terminal_M2=sum(F((a+2*b)**2,4) for a,b in paths if a+2*b==3)
terminal_br=sum(F(5,4) for a,b in paths if a+2*b==3)
witness('terminal_event_isometry',terminal_M2,terminal_br,'M=epsilon1+2epsilon2, event M=3')
check('terminal_control_nonzero',terminal_M2-terminal_br,F(1))
# Independent Bernoulli time-zero flag, all eight atoms.
goodM4=sum(F((a+2*b)**4,8) for flag,a,b in itertools.product([0,1],[-1,1],[-1,1]) if flag)
check('initial_event_fourth',goodM4,F(41,2))

# Exact exponents, showing both clipping costs force L=N^2 in this proof.
q=F(2)
check('clip_same_edge_exponent',2*q-4,0)
check('clip_bad_event_exponent',4-2*q,0)
witness('clip_linear_power',2*q-4,2*F(1)-4,'L=N instead of N^2')
delta=F(1,24)
check('cutoff_balance',-F(1,2)+11*delta,-delta)
check('gaussian_shell_power',18+3,21)
check('gaussian_integral_exponent',F(21+1,2),11)
witness('cutoff_endpoint_claim',-F(1,2)+11*F(1,22),-F(1,22),'delta=1/22 not admissible for decay')
# Scalar atom of mass 1/N below a cutoff demonstrates why the finite-N
# term cannot be deleted from a small-ball-based truncated-square bound.
N=16;r=F(1,16)
atom_square=F(1,N)*r**-2
witness('finite_N_square_term_drop',atom_square,F(0),(N,str(r)))

# Floating diagnostics only: exact derivative envelope after normalization
# c=1, r rescaled. The proof, not this sweep, covers every lattice mode.
max_ratio=0.0;argmax=None
for kk in [(1,0,0,0),(1,1,0,0),(2,-1,1,0)]:
    for m in itertools.product(range(-3,4),repeat=4):
        s=norm2(m)
        if not s: continue
        mp=plus(m,kk);sp=norm2(mp)
        for r in [0.0001,0.001,0.01,0.1,0.25]:
            aa=math.exp(-r*s)/s
            ap=math.exp(-r*sp)/sp if sp else 0.0
            dd=math.exp(-r*norm2(kk))
            bb=dot(kk,m)*aa-dot(kk,mp)*ap+(dd if m==(0,0,0,0) or m==opp(kk) else 0.0)
            envelope=math.exp(-r*s/8)/s
            ratio=abs(bb)/envelope
            counts['floating_heat_envelope']+=1
            if ratio>max_ratio:max_ratio=ratio;argmax=(kk,m,r)
            if ratio>1000*(1+norm2(kk)):
                raise AssertionError('floating heat envelope exceeded loose diagnostic constant')

expected=['graph_triangle_18','graph_adjacent_omit','graph_disjoint_omit','graph_cycle_24','graph_ordered_energy','smooth_self_omit','smooth_self_sign','ordered_half_omit','triple_prefactor_twice','overlap_missing_orientation','overlap_self_omit','merge_time_weights','initial_tag_replaced','mixed_same_label_omit','tail_row_factor_one','energy_noise_cross_zero','initial_all_equal_twice','terminal_event_isometry','clip_linear_power','cutoff_endpoint_claim','finite_N_square_term_drop']
check('all_mutations_nonzero',set(witnesses),set(expected))
if mutation!='baseline':
    raise AssertionError('Unknown mutation '+mutation)
print(json.dumps(serial({'status':'PASS','assertions':sum(counts.values()),'categories':dict(counts),'mutations':witnesses,'floating_heat_max_ratio':max_ratio,'floating_heat_argmax':argmax,'limits':'Finite exact algebra and finite floating diagnostics support the analytic audit only; no actual-law simulation or continuum certification.'}),sort_keys=True,indent=2))

