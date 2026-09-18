#!/usr/bin/env python3
"""AUD064 supporting exact diagnostics. No source/checker imports or random draws.

This tests finite algebra and inference countermodels; it does not certify the
singular particle theorem. All arithmetic in mathematical checks is Fraction/int.
Run with no arguments for read-only JSON output; --output creates a new result.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


COUNTS = {}
MUTATIONS = []
EXAMPLES = {}


def check(category, statement, detail):
    if not statement:
        raise AssertionError(f"{category}: {detail}")
    COUNTS[category] = COUNTS.get(category, 0) + 1


def mutation(name, correct, wrong, detail):
    check("mutation_witnesses", correct != wrong, name)
    MUTATIONS.append({"name": name, "correct": str(correct),
                      "mutated": str(wrong), "witness": detail})


def sqnorm(x, weights=None):
    if weights is None:
        weights = [F(1)] * len(x)
    return sum((w * a * a for w, a in zip(weights, x)), F(0))


def real_complex():
    # Fourier coefficients are (a-ib)/sqrt(2) and its conjugate. Work with
    # numerators; dividing the complex pair by two removes both square roots.
    scalars = [F(-3, 2), F(-1), F(0), F(2, 3), F(2)]
    for a, b, c, d in product(scalars, repeat=4):
        pair_real = ((a*c+b*d) + (a*c+b*d)) / 2
        pair_imag = ((a*d-b*c) + (b*c-a*d)) / 2
        check("real_complex_pair", pair_real == a*c+b*d and pair_imag == 0,
              (a,b,c,d))
        if a == c and b == d:
            check("real_complex_pair", pair_real == a*a+b*b, "norm")
    pair_norm = sqnorm([F(2),F(3)])
    mutation("omit_sqrt2_in_real_basis", pair_norm, pair_norm/2,
             "Real coefficients (2,3): orthonormal pair norm squared is 13.")
    mutation("count_only_one_complex_frequency", pair_norm, pair_norm/2,
             "The opposite complex frequency has the same squared modulus.")
    mutation("double_count_real_opposite_pair", pair_norm, pair_norm*2,
             "There are two real modes, not four, per opposite complex pair.")


def source_operator():
    # Actual admitted d=3,s=1 gives alpha=1,M=5,R=9; r=11 is admitted.
    for modes in (2, 3, 5, 9, 18):
        weights = [F(1, (1+k*k)**11) for k in range(1,modes+1)]
        envelope = [(1+k)**9 for k in range(1,modes+1)]
        norm_squared = sum((w*c*c for w,c in zip(weights,envelope)),F(0))
        for phase in product((F(-1), F(0), F(1)), repeat=min(modes,5)):
            theta = [phase[j % len(phase)] for j in range(modes)]
            for value in (F(0), F(1,3), F(2)):
                source = [value*c*t for c,t in zip(envelope,theta)]
                check("simultaneous_source_operator",
                      sqnorm(source,weights) <= value*value*norm_squared,
                      (modes, value, phase))
        check("simultaneous_source_operator",
              sqnorm(envelope,weights) == norm_squared, "envelope is attained")
        # A time-integrated finite source: Minkowski squared without sqrt.
        # If each modal integral is bounded by c_j times the same integrated V,
        # the weighted square sum uses that single V; no source square moment.
        v = [F(1,3),F(5,7),F(2,9)]
        dt = [F(1,5),F(2,5),F(2,5)]
        mass = sum((a*b for a,b in zip(v,dt)),F(0))
        integrals = [mass*c for c in envelope]
        check("integrated_source_envelope",
              sqnorm(integrals,weights) == mass*mass*norm_squared,
              "common integrable envelope, all modes active")
    w = [F(1,2**11),F(1,5**11)]
    c = [2**9,3**9]
    terms = [a*b*b for a,b in zip(w,c)]
    mutation("replace_squared_sum_by_maximum", sum(terms), max(terms),
             "Two simultaneously active modes attain the sum, not its maximum.")
    # E|S_j|=1 separately is not a family bound: one atom for each test.
    for m in (2,3,4,9,16):
        matrix = [[F(m if i==j else 0) for j in range(m)] for i in range(m)]
        expected_columns = [sum(row[j] for row in matrix)/m for j in range(m)]
        mean_sup = sum(max(row) for row in matrix)/m
        check("expectation_supremum_countermodel",
              expected_columns == [F(1)]*m and mean_sup == m,
              "each separate mean is 1; expected family maximum is m")
    mutation("move_supremum_outside_expectation", mean_sup, max(expected_columns),
             "Sixteen equiprobable atoms, S_j=16 times indicator of atom j.")


def adaptive_martingales():
    records=[]
    for steps in (2,3,5,7):
        for q in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            for strategy in (0,1,2):
                totals = {name:F(0) for name in ("terminal","bracket","maxB","maxM")}
                count=2**steps
                for signs in product((-1,1),repeat=steps):
                    B=[F(0)]; M=[F(0)]; bracket=F(0)
                    for j,sign in enumerate(signs,1):
                        if strategy==0:
                            coeff=F(1)
                        elif strategy==1:
                            coeff=F(2 if B[-1]>0 else 1)
                        else:
                            coeff=F((1+abs(B[-1])) if j%2 else 1, j)
                        bracket += coeff*coeff
                        B.append(B[-1]+coeff*sign)
                        M.append(q*M[-1]+coeff*sign)
                        history=(1-q)*sum((q**(j-1-i)*B[i] for i in range(1,j)),F(0))
                        check("adaptive_convolution_identity", M[j] == B[j]-history,
                              (steps,q,strategy,j,signs))
                    maxB=max(x*x for x in B); maxM=max(x*x for x in M)
                    check("adaptive_convolution_maximum", maxM <= 4*maxB,
                          (steps,q,strategy,signs))
                    totals["terminal"] += B[-1]**2/count
                    totals["bracket"] += bracket/count
                    totals["maxB"] += maxB/count
                    totals["maxM"] += maxM/count
                check("adaptive_isometry_and_maximum",totals["terminal"]==totals["bracket"],
                      "exact finite-tree adapted isometry")
                check("adaptive_isometry_and_maximum",totals["maxB"]<=4*totals["terminal"],
                      "finite-tree L2 maximum")
                check("adaptive_isometry_and_maximum",totals["maxM"]<=16*totals["bracket"],
                      "combined convolution upper bound")
                records.append({"steps":steps,"q":str(q),"strategy":strategy,
                                **{k:str(v) for k,v in totals.items()}})
    EXAMPLES["adaptive_tree_cases"]=records
    node=F(1); damping=F(1,2)
    next_conditional=sum(damping*node+F(2)*sign for sign in (-1,1))/2
    mutation("convolution_is_terminal_time_martingale",next_conditional,node,
             "At first node M_1=1, q=1/2; conditional E[M_2|F_1]=1/2.")
    B=[F(0),F(1),F(1)]
    convolution=sum((damping**(2-j)*(B[j]-B[j-1]) for j in (1,2)),F(0))
    mutation("drop_old_history_in_integration_by_parts",convolution,B[2],
             "B=(0,1,1), q=1/2; M_2=1/2, whereas B_2=1.")
    adapted_bracket=F(1)+sum(F(2 if sign>0 else 1)**2 for sign in (-1,1))/2
    iid_coefficient_bracket=2*F(1)**2
    mutation("replace_adapted_bracket_by_iid_coefficient",adapted_bracket,iid_coefficient_bracket,
             "Two steps, first coefficient 1, second coefficient 2 on B_1>0 and 1 otherwise.")


def modal_covariances():
    for q,theta,b in product((F(1,5),F(1,2),F(3,4)),
                             (F(0),F(1,4),F(2,3)),(F(1),F(1,3))):
        # Innovation form of the exact OU skeleton; this is independently
        # assembled from the two-exponential formula being tested.
        variances=[b]
        for j in range(1,8):
            variances.append(q*q*variances[-1]+b*theta*(1-q*q))
        for i,j in product(range(8),repeat=2):
            skeleton=q**abs(i-j)*variances[min(i,j)]
            target=b*((1-theta)*q**(i+j)+theta*q**abs(i-j))
            check("OU_skeleton_covariance",skeleton==target,(q,theta,b,i,j))
        check("OU_skeleton_covariance",variances[0]==b,"initial variance")
    b=F(1);theta=F(1,2);q=F(1,2)
    proper=b*((1-theta)*q*q+theta)
    wrong_half=b*q*q+b*(theta/2)*(1-q*q)
    mutation("remove_Brownian_factor_two",proper,wrong_half,
             "One OU step, q=1/2, thermal fraction 1/2, initial variance 1.")
    wrong_stationary=b*((1-theta)*q**abs(1-1)+theta*q**abs(1-1))
    mutation("replace_initial_time_sum_by_difference",proper,wrong_stationary,
             "Equal one-step times for the same q and thermal fraction.")
    mutation("suppress_thermal_contribution",proper,b*q*q,
             "Positive thermal fraction; pure damped initial variance is too small.")


def thresholds_and_shells():
    rows=[]
    for d in range(3,13):
        for s in [F(j,2) for j in range(1,2*(d-2)+1)]:
            alpha=(d-s)/2; M=d+2; R=alpha+M+3
            threshold=R+F(d,2)
            check("exact_range_and_scaling",threshold==2*d+5-s/2,(d,s))
            check("exact_range_and_scaling",(-1+s/d)==-2*alpha/d,(d,s))
            check("exact_range_and_scaling",(s/d-F(1,2)<0)==(s<F(d,2)),(d,s))
            for margin in (F(1,4),F(1,2),F(1),F(3)):
                r=threshold+margin
                check("exact_range_and_scaling",d+2*R-2*r==-2*margin,(d,s,r))
                check("exact_range_and_scaling",r>F(d,2)+1,(d,s,r))
                # Radius 4^n makes quarter-margin shell models rational.
                for n in range(1,7):
                    shell=F(2)**int(2*n*(d+2*R-2*r))
                    check("source_shell_decay",shell==F(2)**int(-4*n*margin),
                          (d,s,margin,n))
            rows.append({"d":d,"s":str(s),"threshold":str(threshold),
                         "THM044_admitted":s<F(d,2)})
        for a in (1,2,4,8,16,32):
            # Exact annulus a <= max_i |k_i| < 2a.
            count=(4*a-1)**d-(2*a-1)**d
            check("lattice_shell_count",count>=a**d,(d,a,count))
            check("lattice_shell_count",count<=(4*a)**d,(d,a,count))
    EXAMPLES["range_rows"]=rows
    d=3;R=F(9);r=R+F(d,2)
    endpoint_shell_sum=sum((F(2)**int(n*(d+2*R-2*r)) for n in range(8)),F(0))
    mutation("allow_source_summation_endpoint",endpoint_shell_sum,F(0),
             "At r=R+d/2, eight dyadic shell lower terms sum to 8; no decay occurs.")
    d=4;s=F(d,2)
    mutation("infer_decay_at_s_equal_d_over_two",s/d-F(1,2),-F(1,2),
             "The residual N exponent is s/d-1/2=0 at this excluded endpoint.")


def projections_and_tightness():
    for dimension in (3,7,13):
        basis=[[F(int(i==j)) for i in range(dimension)] for j in range(dimension)]
        for i in range(dimension):
            check("escaping_modes_countermodel",sqnorm(basis[i])==1,"unit vectors")
            for j in range(i):
                check("escaping_modes_countermodel",
                      sqnorm([a-b for a,b in zip(basis[i],basis[j])])==2,
                      "no finite net of radius below sqrt(2)/2")
            for cutoff in range(dimension+1):
                low=sqnorm(basis[i][:cutoff]);high=sqnorm(basis[i][cutoff:])
                check("orthogonal_projection_identity",low+high==1,(dimension,i,cutoff))
                if i>=cutoff:
                    check("escaping_modes_countermodel",low==0 and high==1,"finite projections vanish")
    escaped=basis[-1]
    mutation("finite_projections_imply_field_tightness",sqnorm(escaped),sqnorm(escaped[:-1]),
             "Constant paths in successive Hilbert unit modes: every fixed projection eventually zero, norms stay one.")
    separate=sqnorm([a-b for a,b in zip(basis[-1],basis[-2])])
    coincident_centers=sqnorm([F(0)]*len(basis[-1]))
    mutation("compact_neighborhood_is_compact",separate,coincident_centers,
             "The radius-one neighborhood of {0} contains unit modes at squared pair distance 2.")
    # A small total error cannot inherit an arbitrary frequency rate of Y.
    ratios=[]
    for n in (4,8,16,32):
        error_sq=F(1,n*n); imposed_tail=F(1,2**n)
        ratios.append(str(error_sq/imposed_tail))
        check("small_error_has_no_fixed_tail_rate",error_sq/imposed_tail>=1,(n,error_sq))
    EXAMPLES["source_error_to_prescribed_tail_ratio"]=ratios
    mutation("assign_linear_tail_rate_to_actual_error",error_sq,imposed_tail,
             "Error path e_(2^N)/N with N=32 has small total norm but violates the proposed geometric high-mode rate.")
    # Exact constants in the root's union-bound construction.
    eps=F(1,5)
    for j in range(1,10):
        e=F(1,2**j); p=eps/F(2**(j+3))
        # gamma=1/6 for (d,s)=(3,1). Pick a perfect sixth power.
        base=2/(e*p); assert base.denominator==1
        N=base.numerator**6
        residual_bound=F(1,base.numerator)
        check("finite_prefix_compact_construction",2*residual_bound/e==p,(j,N))
        check("finite_prefix_compact_construction",2*p+p==3*p,"tail plus projection failures")
    check("finite_prefix_compact_construction",3*eps/F(8)<eps,
          "sum from j=1 of eps/2^(j+3) is eps/8")


def infimal_approximation():
    # Compact scalar path set [0,1], F(x)=sqrt(x). The exact infimal envelope
    # is min(L*x,sqrt(x)). Its maximal error is 1/(4L), attained at 1/(4L^2).
    for L in (1,2,3,5,8,16,32):
        for j in range(65):
            root=F(j,64);x=root*root
            envelope=min(L*x,root)
            check("bounded_continuous_approximation",0<=root-envelope<=F(1,4*L),(L,j))
        root=F(1,2*L);x=root*root
        check("bounded_continuous_approximation",root-min(L*x,root)==F(1,4*L),
              "exact nonzero sharp compact approximation error")
    at_one=F(1);zero_L_envelope=min(0*at_one,at_one)
    mutation("fixed_zero_L_approximates_all_continuous_functions",at_one,zero_L_envelope,
             "F(x)=sqrt(x) on compact [0,1]; its L=0 infimal envelope is zero.")


def main():
    real_complex(); source_operator(); adaptive_martingales(); modal_covariances()
    thresholds_and_shells(); projections_and_tightness(); infimal_approximation()
    return {"audit":"AUD064", "status":"PASS", "evidence":"SUPPORTING_EXACT_FINITE_DIAGNOSTIC",
            "program_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "arithmetic":"integer and fractions.Fraction only; no random seed or tolerance",
            "assertions":sum(COUNTS.values()),"categories":COUNTS,
            "mutation_controls":MUTATIONS,"mutation_count":len(MUTATIONS),
            "examples":EXAMPLES,
            "limits":"Finite diagnostics do not prove singular particle estimates, infinite sums, or weak convergence. Countermodels attack inference shortcuts, not admitted particle laws."}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    data=json.dumps(main(),indent=2,sort_keys=True)+'\n'
    if args.output:
        with args.output.open('x') as target:
            target.write(data)
        result=json.loads(data)
        print(json.dumps({"status":result["status"],"assertions":result["assertions"],
                          "categories":len(result["categories"]),"mutations":result["mutation_count"],
                          "result":str(args.output)}))
    else:
        print(data,end='')
