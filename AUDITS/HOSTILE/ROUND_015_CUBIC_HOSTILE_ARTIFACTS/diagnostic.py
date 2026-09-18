#!/usr/bin/env python3
"""AUD050: new exact checks, independently written in the hostile context.

Finite real Laurent polynomials in one coordinate of the unit torus are embedded
in the admitted higher-dimensional space. D e_k = k e_k is used for exact rational
algebra: restoring ordinary derivatives multiplies each second-order differential
expression, including K.grad, Delta, J and R, by -(2*pi)^2. No singular analytic
estimate, positive-time particle law, or actual inverse is replaced by this test.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json
import platform


def tidy(p):
    return {k: F(v) for k,v in p.items() if v}


def const(n,c):
    return {} if not c else {(0,)*n:F(c)}


def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return tidy(out)


def scale(p,a):
    return tidy({k:v*a for k,v in p.items()})


def mul(p,q):
    out={}
    for k,a in p.items():
        for l,b in q.items():
            kl=tuple(x+y for x,y in zip(k,l))
            out[kl]=out.get(kl,F(0))+a*b
    return tidy(out)


def deriv(p,j):
    return tidy({k:v*k[j] for k,v in p.items()})


def lap(p,n):
    return add(*(deriv(deriv(p,j),j) for j in range(n)))


def embed(p,n,slots):
    out={}
    for k,v in p.items():
        new=[0]*n
        for exponent,slot in zip(k,slots): new[slot]+=exponent
        new=tuple(new)
        out[new]=out.get(new,F(0))+v
    return tidy(out)


def contract(p,n,keep):
    gone=set(range(n))-set(keep)
    out={}
    for k,v in p.items():
        if any(k[j] for j in gone): continue
        kk=tuple(k[j] for j in keep)
        out[kk]=out.get(kk,F(0))+v
    return tidy(out)


def integral(p,n):
    return p.get((0,)*n,F(0))


def cos_mode(k,a=F(1)):
    return add({tuple(k):F(a,2)},{tuple(-v for v in k):F(a,2)})


def difference(p):
    return tidy({(k[0],-k[0]):v for k,v in p.items()})


def U(p,k,N):
    """Definition by all slot subsets and injective empirical assignments."""
    out={}
    for count in range(k+1):
        coefficient=F((-1)**(k-count),N**count)
        for keep in combinations(range(k),count):
            projected=contract(p,k,keep)
            for labels in permutations(range(N),count):
                out=add(out,scale(embed(projected,N,labels),coefficient))
    return out


def P(p,N):
    return scale(U(p,2,N),F(1,2))


def D2(p,N):
    return scale(add(*(embed(p,N,ij) for ij in permutations(range(N),2))),F(1,N*N))


def empirical(p,N):
    return scale(add(*(embed(p,N,[i]) for i in range(N))),F(1,N))


def rho(p,N):
    return add(empirical(p,N),const(N,-integral(p,1)))


def responses(phi,K2):
    rx=contract(mul(embed(K2,3,[2,0]),embed(deriv(phi,0),3,[2,1])),3,[0,1])
    ry=contract(mul(embed(K2,3,[2,1]),embed(deriv(phi,1),3,[0,2])),3,[0,1])
    return rx,ry


def cubic(phi,K2):
    raw=mul(embed(K2,3,[0,2]),embed(deriv(phi,0),3,[0,1]))
    return scale(add(*(embed(raw,3,p) for p in permutations(range(3)))),F(1,6))


def generator(observable,N,nu,K2):
    pieces=[scale(lap(observable,N),nu)]
    for i in range(N):
        force=scale(add(*(embed(K2,N,[i,j]) for j in range(N) if j!=i)),F(1,N))
        pieces.append(mul(force,deriv(observable,i)))
    return add(*pieces)


checks={}

def check(group,name,left,right):
    residue=add(left,scale(right,-1))
    if residue:
        raise AssertionError(f'{group}/{name}: {len(residue)} nonzero coefficients; first={next(iter(residue.items()))}')
    checks[group]=checks.get(group,0)+1


def scalar_check(group,name,condition):
    if not condition: raise AssertionError(f'{group}/{name}')
    checks[group]=checks.get(group,0)+1


g=add(cos_mode([1],F(3,5)),cos_mode([2],F(2,7)),cos_mode([3],F(1,11)))
K2=scale(deriv(difference(g),0),-1)
phis={
    'constant':const(2,F(3,7)),
    'additive':add(cos_mode([1,0],F(2,5)),cos_mode([0,1],F(2,5))),
    'relative':cos_mode([1,-1],F(5,11)),
    'product':mul(cos_mode([1,0],F(7,13)),cos_mode([0,1])),
    'mixed':add(cos_mode([2,-1],F(4,9)),cos_mode([-1,2],F(4,9))),
}
phis['combined']=add(*phis.values())
mutations={'omit_response':0,'omit_linear_lower':0,'omit_scalar_lower':0,'replace_N_by_N_minus_one':0}
for name,phi in phis.items():
    G=deriv(phi,0)
    A=contract(G,2,[0])
    B=mul(K2,add(G,scale(deriv(phi,1),-1)))
    b=contract(B,2,[0]); bar=integral(B,2)
    rx,ry=responses(phi,K2); R=add(rx,ry)
    C=cubic(phi,K2)
    Aa=mul(K2,add(embed(A,2,[0]),scale(embed(A,2,[1]),-1)))
    v=contract(mul(embed(K2,2,[1,0]),embed(A,2,[1])),2,[0])
    check('cubic_contractions',name+'/one-background',contract(C,3,[0,1]),scale(add(Aa,R),F(1,6)))
    check('cubic_contractions',name+'/two-background',contract(C,3,[0]),scale(v,F(1,3)))
    scalar_check('cubic_contractions',name+'/scalar',integral(C,3)==0)
    check('response_contractions',name,contract(R,2,[0]),v)
    for N in [2,3,4]:
        pn=P(phi,N); u3=U(C,3,N)
        linear=scale(rho(b,N),F(1,N)); scalar=const(N,F(bar,2*N))
        for nu in [F(0),F(2,7)]:
            left=generator(pn,N,nu,K2)
            right=add(P(add(scale(lap(phi,2),nu),R,scale(B,F(1,N))),N),u3,linear,scalar)
            check('full_generator',f'{name}/N{N}/nu{nu}',left,right)
            check('raw_internal_split',f'{name}/N{N}/nu{nu}',left,add(P(add(scale(lap(phi,2),nu),R),N),u3,scale(D2(B,N),F(1,2*N))))
        mutants={
            'omit_response':P(R,N),
            'omit_linear_lower':linear,
            'omit_scalar_lower':scalar,
            'replace_N_by_N_minus_one':scale(D2(B,N),F(1,2*(N-1))-F(1,2*N)),
        }
        for kind,residue in mutants.items():
            if residue: mutations[kind]+=1
        # Direct derivative of the full polynomial is compared with the particle-row formula.
        grad=[]
        for i in range(N):
            gi=deriv(pn,i); grad.append(gi)
            rhs=add(scale(add(*(embed(G,N,[i,j]) for j in range(N) if j!=i)),F(1,N*N)),scale(embed(A,N,[i]),F(-1,N)))
            check('particle_gradient',f'{name}/N{N}/label{i}',gi,rhs)
        # Recompute the three marginal types and the mixed/background square separately.
        bracket=add(*(mul(gi,gi) for gi in grad))
        diag=scale(add(*(embed(mul(G,G),N,[i,j]) for i,j in permutations(range(N),2))),F(1,N**4))
        triple={}
        for i,j,k in permutations(range(N),3):
            triple=add(triple,mul(embed(G,N,[i,j]),embed(G,N,[i,k])))
        triple=scale(triple,F(1,N**4))
        mixed={}
        for i,j in permutations(range(N),2):
            mixed=add(mixed,mul(embed(G,N,[i,j]),embed(A,N,[i])))
        mixed=scale(mixed,F(-2,N**3))
        back=scale(add(*(embed(mul(A,A),N,[i]) for i in range(N))),F(1,N*N))
        check('full_bracket_expansion',f'{name}/N{N}',bracket,add(diag,triple,mixed,back))
        # Haar constant coefficients are exact iid expectations; no evolving law enters.
        m=integral(phi,2)
        q0=add(contract(phi,2,[0]),const(1,-m))
        Fc=add(phi,scale(embed(q0,2,[0]),-1),scale(embed(q0,2,[1]),-1),const(2,-m))
        second=integral(mul(pn,pn),N)
        rhs=F(N-1,2*N**3)*integral(mul(Fc,Fc),2)+F(1,N**3)*integral(mul(q0,q0),1)+F(m*m,4*N*N)
        scalar_check('iid_second_moment',f'{name}/N{N}',second==rhs)
        scalar_check('iid_bound',f'{name}/N{N}',N*second<=integral(mul(phi,phi),2)/F(2*N))
        check('iid_decomposition',f'{name}/N{N}',pn,add(scale(D2(Fc,N),F(1,2)),scale(empirical(q0,N),F(-1,N)),const(N,F(-m,2*N))))
for name,count in mutations.items(): scalar_check('nonvacuous_mutations',name,count>0)

# A separate direct Fourier source test includes zero frequencies and the full smooth diagonal.
f=add(const(1,F(2,9)),cos_mode([1],F(3,4)),cos_mode([2],F(-2,5)),cos_mode([5],F(1,17)))
source=mul(K2,add(embed(deriv(f,0),2,[0]),scale(embed(deriv(f,0),2,[1]),-1)))
expected={}
for u in range(-10,11):
    for v in range(-10,11):
        m=u+v
        coefficient=f.get((m,),F(0))*m*(u*g.get((u,),F(0))+v*g.get((v,),F(0)))
        if coefficient: expected[(u,v)]=coefficient
check('source_multiplier','all pair coefficients',source,expected)
check('source_zero_diagonal','collapse x=y',embed(source,1,[0,0]),{})
for N in [2,3,5]:
    fullpair=scale(add(*(embed(source,N,[i,j]) for i in range(N) for j in range(N))),F(1,2*N*N))
    q=contract(source,2,[0]); mean=integral(source,2)
    centered=add(fullpair,scale(empirical(q,N),-1),const(N,mean/F(2)))
    check('source_full_vs_deleted',f'N{N}',P(source,N),centered)

# Positive-kernel algebra: W=(1+cos)^2 is nonnegative, and retained g has positive modes.
W=mul(add(const(1,1),cos_mode([1])),add(const(1,1),cos_mode([1])))
cW=integral(W,1)
gtotal=add(g,W,const(1,-cW))
selfvalue=sum(g.values(),F(0))
for N in [2,3,4,5,6]:
    energy=scale(add(*(embed(difference(g),N,[i,j]) for i in range(N) for j in range(N))),F(1,N*N))
    right=add(energy,const(N,-selfvalue/F(N)),D2(difference(W),N),const(N,-F(N-1,N)*cW))
    check('positive_energy_self_and_tail',f'N{N}',D2(difference(gtotal),N),right)
    scalar_check('labelled_pair_conversion',f'N{N}',F(N,N-1)*(selfvalue/F(N)+F(N-1,N)*cW)==selfvalue/F(N-1)+cW)
    scalar_check('iid_joint_energy_equality',f'N{N}',integral(energy,N)+integral(D2(difference(W),N),N)==selfvalue/F(N)+F(N-1,N)*cW)

# Exact rational critical exponents, with fine corner sequences; no decimal signs.
exponent_rows=[]
s_values=sorted(set([F(j,20) for j in range(1,40)]+[F(1,1000),F(1999,1000),F(1,10**6),F(1999999,10**6)]))
for d,s in product([4,5,6,8,16,32],s_values):
    theta=1-s/F(d); p=s+2; a=s/p
    omega=min(s,F(d)-s-2,F(d,2)-1)/2; r=1+omega; e=(s-omega)/p
    margins=[theta-F(1,2),F(1,2)-e,(theta-a)/2]
    scalar_check('critical_exponents',f'd{d}/s{s}',all(x>0 for x in margins) and 1<r<F(d,2) and r<=s+1 and s+1+r<d)
    scalar_check('critical_rescaled_noise',f'd{d}/s{s}',-theta+2/p==s*(s+2-d)/(F(d)*p) and -theta+2/p<0)
    scalar_check('explicit_margins',f'd{d}/s{s}',F(1,2)-e==(2-s+2*omega)/(2*p) and theta-a==(2*d-s*p)/(F(d)*p))
    exponent_rows.append({'d':d,'s':str(s),'omega':str(omega),'r':str(r),'source_decay':str(margins[0]),'lower_decay':str(margins[1]),'noise_decay':str(margins[2])})

# Independent cancellation test at alpha=2 (admitted d=5,s=1), m=1, epsilon=0.
# This is a multiplier diagnostic, not a substitution for the positive-cutoff proof.
for u in list(range(2,201))+[10**3,10**6]:
    v=1-u
    numerator=abs(F(u,abs(u)**4)+F(v,abs(v)**4))
    ratio=numerator*u*u*v*v
    exact=F(3*u*u-3*u+1,u*(u-1))
    scalar_check('high_frequency_cancellation',f'u{u}',ratio==exact and 3<ratio<=F(7,2))
    separate=(F(abs(u),abs(u)**4)+F(abs(v),abs(v)**4))*u*u*v*v
    scalar_check('cancellation_is_essential',f'u{u}',separate>2*u-1)

result={
    'audit':'AUD050','status':'PASS_EXACT_FINITE_DIAGNOSTICS',
    'evidence_class':'Exact rational Laurent-polynomial algebra and rational exponent checks; supporting evidence, not analytic certification.',
    'runtime':{'python':platform.python_version(),'external_dependencies':[],'randomness':'none','arithmetic':'fractions.Fraction; no numerical tolerance'},
    'groups':checks,'total_checks':sum(checks.values()),'mutation_witness_counts':mutations,
    'scope':{'particle_counts':[2,3,4,5,6],'generator_particle_counts':[2,3,4],'diffusivities':['0','2/7'],'pair_kernels':list(phis),'physical_derivative_factor':'-(2*pi)^2 for every second-order differential expression; no physical factors discarded selectively'},
    'critical_parameter_rows':exponent_rows,
    'not_certified_by_this_program':['singular analytic limits','N-uniform constants in multiplier estimates','actual positive-time law estimates','true full pair inverse construction','full fluctuation law'],
}
out=Path(__file__).with_name('results.json')
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':result['status'],'groups':checks,'total_checks':result['total_checks'],'mutation_witness_counts':mutations},indent=2))
