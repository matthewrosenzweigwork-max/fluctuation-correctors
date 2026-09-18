#!/usr/bin/env python3
"""AUD053 independent exact checks. No input files or prior checker are read.
Fourier derivatives omit 2*pi. Thus every generator/source/bracket below is
in units of (2*pi)^2; multiplying those identities restores physical units.
Finite smooth Fourier examples test coefficients, not the singular theorem.
"""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import hashlib, json

ZERO=(F(0),F(0)); ONE=(F(1),F(0)); I=(F(0),F(1))
def c(x): return x if isinstance(x,tuple) else (F(x),F(0))
def ca(a,b): return (a[0]+b[0],a[1]+b[1])
def cm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cs(a,q): return (a[0]*q,a[1]*q)
def clean(p): return {k:v for k,v in p.items() if v!=ZERO}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=ca(out.get(k,ZERO),v)
    return clean(out)
def scale(p,q): return clean({k:cs(v,F(q)) for k,v in p.items()})
def mul(p,q):
    out={}
    for k,a in p.items():
        for l,b in q.items():
            e=tuple(x+y for x,y in zip(k,l))
            out[e]=ca(out.get(e,ZERO),cm(a,b))
    return clean(out)
def deriv(p,j): return clean({e:cs(cm(a,I),F(e[j])) for e,a in p.items()})
def embed(p,n,slots):
    out={}
    for e,a in p.items():
        ee=[0]*n
        for j,k in enumerate(slots): ee[k]+=e[j]
        ee=tuple(ee); out[ee]=ca(out.get(ee,ZERO),a)
    return clean(out)
def avg(p,n): return scale(add(*(embed(p,n,[i]) for i in range(n))),F(1,n))
def haar(p,n): return p.get((0,)*n,ZERO)
def constant(n,a): return {} if a==ZERO else {(0,)*n:a}
def contract_second(p):
    out={}
    for e,a in p.items():
        if e[1]==0: out[(e[0],)]=ca(out.get((e[0],),ZERO),a)
    return clean(out)
def j_kernel(g,h):
    force={ (k,-k):cs(cm(a,I),F(-k)) for (k,),a in g.items() if k }
    dh=deriv(h,0)
    return mul(force,add(embed(dh,2,[0]),scale(embed(dh,2,[1]),-1)))
def source(g,h,n):
    j=j_kernel(g,h)
    literal=scale(add(*(embed(j,n,[a,b]) for a in range(n) for b in range(n) if a!=b)),F(1,2*n*n))
    return add(literal,scale(avg(contract_second(j),n),-1),constant(n,cs(haar(j,2),F(1,2))))
def lap(p): return add(*(deriv(deriv(p,j),j) for j in range(len(next(iter(p),(0,)))))) if p else {}
def generator(g,p,n,nu):
    terms=[scale(lap(p),nu)]
    for i in range(n):
        force={}
        for j in range(n):
            if i==j: continue
            for (k,),a in g.items():
                if not k: continue
                e=[0]*n;e[i]=k;e[j]=-k;e=tuple(e)
                force[e]=ca(force.get(e,ZERO),cs(cm(a,I),F(-k,n)))
        terms.append(mul(force,deriv(p,i)))
    return add(*terms)
def response(g,h): return clean({(k,):cs(cm(a,g.get((k,),ZERO)),F(-k*k)) for (k,),a in h.items()})
def real_test(seed):
    out={(0,):c(F(seed,3))}
    for k in (1,2,3):
        a=(F(seed+k,3+k),F(seed-k,5+k))
        out[(k,)]=a;out[(-k,)]=(a[0],-a[1])
    return out

def centered(h): return {k:a for k,a in h.items() if k!=(0,)}
counts=Counter(); details={}
def check(category,condition):
    if not condition: raise AssertionError(category)
    counts[category]+=1

def main(output):
    kernels=[{(k,):c(F(seed+abs(k),1+abs(k)**2)) for k in (-2,-1,1,2)} for seed in (1,2,4)]
    for g in kernels:
        for seed in (1,2,4):
            h=real_test(seed);v=real_test(seed+1)
            j=j_kernel(g,h)
            check('source_symmetry',j=={(e[1],e[0]):a for e,a in j.items()})
            check('haar_response_sign',contract_second(j)==response(g,h))
            check('double_contraction_zero',haar(j,2)==ZERO)
            check('smooth_diagonal_zero',not embed(j,1,[0,0]))
            for n in range(2,7):
                for nu in (F(0),F(1,3),F(2)):
                    obs=avg(h,n)
                    raw=generator(g,obs,n,nu)
                    linear=avg(add(scale(lap(h),nu),response(g,h)),n)
                    residual=source(g,h,n)
                    check('ordered_first_order_generator',raw==add(linear,residual))
                    check('wrong_source_half_detected',raw!=add(linear,scale(residual,2)))
                    check('wrong_response_sign_detected',raw!=add(avg(add(scale(lap(h),nu),scale(response(g,h),-1)),n),residual))
                    check('wrong_denominator_detected',raw!=add(linear,scale(residual,F(n,n-1))))
                    bracket=scale(add(*(mul(deriv(avg(h,n),i),deriv(avg(v,n),i)) for i in range(n))),2*nu*n)
                    expected=scale(avg(mul(deriv(h,0),deriv(v,0)),n),2*nu)
                    check('exact_scaled_cross_bracket',bracket==expected)
                    check('initial_haar_cross_bracket',haar(bracket,n)==cs(haar(mul(deriv(h,0),deriv(v,0)),1),2*nu))
                    if nu:
                        check('wrong_martingale_normalization_detected',bracket!=scale(expected,F(1,n)))
                hc=centered(h);vc=centered(v)
                check('iid_vector_covariance',cs(haar(mul(avg(hc,n),avg(vc,n)),n),F(n))==haar(mul(hc,vc),1))
                check('initial_replacement_variance',cs(haar(mul(avg(hc,n),avg(hc,n)),n),F(n))==haar(mul(hc,hc),1))
    # A second route: literal initial generator of complex mode energy.
    for g in kernels:
        for n in range(2,7):
            for k in (1,2,3):
                z=avg({(k,):ONE},n);zb=avg({(-k,):ONE},n)
                energy=mul(z,zb)
                check('initial_mode_self_diagonal',haar(energy,n)==c(F(1,n)))
                for nu in (F(0),F(1,2),F(3)):
                    actual=haar(generator(g,energy,n,nu),n)
                    expected=cs(g.get((k,),ZERO),F(-2*(n-1)*k*k,n*n))
                    check('initial_mode_variance_derivative',actual==expected)
                    if k in (1,2):
                        check('wrong_initial_damping_sign_detected',actual!=cs(expected,F(-1)))
    # Joint covariance with actual semigroup multiplication represented exactly
    # by rational bases q_k raised to integer times; includes t=0/repeated times.
    h=real_test(2);v=real_test(4);times=[0,1,1,2,0,1,1]
    tests=[h,v,h,scale(h,2),{(0,):c(7)},h,scale(h,2)]
    for coulomb in (False,True):
        q={k:F(2,3) if coulomb else F(1,abs(k)+1) for k in (-3,-2,-1,1,2,3)}
        propagated=[{(k,):cs(a,q[k]**t) for (k,),a in hh.items() if k} for hh,t in zip(tests,times)]
        covariance=[]
        for i in range(7):
            row=[]
            for j in range(7):
                gram=haar(mul(propagated[i],propagated[j]),1)
                fourier=ZERO
                for (k,),a in tests[i].items():
                    if k:
                        fourier=ca(fourier,cs(cm(a,tests[j].get((-k,),ZERO)),q[k]**(times[i]+times[j])))
                check('joint_covariance_sum_of_times',gram==fourier)
                check('real_covariance',gram[1]==0)
                row.append(str(gram[0]))
            covariance.append(row)
        for i in range(7): check('constant_test_degeneracy',haar(mul(propagated[i],propagated[4]),1)==ZERO)
        repeated=add(propagated[2],scale(propagated[5],-1))
        check('repeated_test_exact_degeneracy',not repeated)
        check('scaled_test_exact_degeneracy',not add(propagated[6],scale(propagated[2],-2)))
        for i in range(7):
            check('repeated_covariance_rows',covariance[2][i]==covariance[5][i])
            check('scaled_covariance_rows',F(covariance[6][i])==2*F(covariance[2][i]))
        # Gram nonnegativity for deterministic rational linear combinations.
        for shift in range(-5,6):
            coeff=[F(shift+1),F(2-shift),F(shift,3),F(-2),F(3),F(2),F(-1)]
            comb=add(*(scale(f,a) for f,a in zip(propagated,coeff)))
            norm=haar(mul(comb,comb),1)
            check('gram_nonnegative',norm[1]==0 and norm[0]>=0)
        details['coulomb_covariance' if coulomb else 'nonconstant_damping_covariance']=covariance
    # Distinct label partitions in a fourth moment: independently count literal
    # index tuples, using iid centered scalar moments from one Haar Fourier test.
    import itertools
    scalar=centered(real_test(3));square=mul(scalar,scalar)
    moments={1:ZERO,2:haar(square,1),3:haar(mul(square,scalar),1),4:haar(mul(square,square),1)}
    for n in range(2,9):
        total=ZERO
        for indices in itertools.product(range(n),repeat=4):
            term=ONE
            for multiplicity in Counter(indices).values():term=cm(term,moments[multiplicity])
            total=ca(total,term)
        computed=cs(total,F(1,n*n))
        target=ca(cs(cm(moments[2],moments[2]),F(3*(n-1),n)),cs(moments[4],F(1,n)))
        check('iid_fourth_moment_label_partitions',computed==target)
    scaling=[]
    for d in range(3,13):
        for numerator in range(1,4*(d-2)+1):
            s=F(numerator,4)
            if s>F(d-2):continue
            a=s/d-F(1,2);b=s/d-1
            check('critical_beta_diverges',1-s/d>0)
            check('critical_noise_vanishes',b<0)
            check('source_scale_balance',-1+(-F(2,d))*(-s/2)==(-F(2,d))*((d-s)/2))
            if s<F(d,2):check('admitted_scaled_source_decays',a<0)
            elif s==F(d,2):check('excluded_boundary_only_bounded',a==0)
            else:check('excluded_high_exponent_grows',a>0)
            scaling.append({'d':d,'s':str(s),'source_scaled_exponent':str(a),'noise_exponent':str(b),'admitted_thm039':s<F(d,2)})
    result={'status':'PASS','audit':'AUD053','assertions':sum(counts.values()),'categories':dict(sorted(counts.items())),'evidence':'EXACT_FINITE_SMOOTH_DIAGNOSTIC_NOT_SINGULAR_PROOF','arithmetic':'Fraction and Gaussian rational; no randomness or tolerance','normalization':'D=(2*pi)^-1 derivative; physical source/generator/brackets multiply by (2*pi)^2','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'joint_examples':details,'scaling_cases':scaling}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'assertions':result['assertions'],'categories':len(counts)},indent=2))
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('round017_gaussian_blind_exact_results.json'))
    main(parser.parse_args().output)
