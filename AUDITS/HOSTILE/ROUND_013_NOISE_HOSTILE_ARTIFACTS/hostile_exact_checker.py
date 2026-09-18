#!/usr/bin/env python3
"""Fresh TASK072 diagnostics. Exact rational arithmetic, no third-party imports.

These tests support the accompanying analytic audit; they do not prove any
stochastic limit, regularity theorem, entropy inequality, or audit verdict.
Finite-state laws below are coefficient probes, not particle-dynamics laws.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path


COUNTS = Counter()


def check(group, condition):
    if not condition:
        raise AssertionError(group)
    COUNTS[group] += 1


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def mv(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def rational_norm(v):
    from math import isqrt
    square = dot(v, v)
    a, b = isqrt(square.numerator), isqrt(square.denominator)
    assert a*a == square.numerator and b*b == square.denominator
    return F(a, b)


def source_hashes(base):
    manifest = base / "AUDITS/ROUND_013_BOUNDED_NOISE_HOSTILE_INPUT_SHA256SUMS.txt"
    rows = []
    for line in manifest.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        path = Path(relative)
        check("input_paths_safe", not path.is_absolute() and ".." not in path.parts)
        raw = (base / path).read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        check("frozen_input_hashes", actual == digest)
        rows.append({"path": relative, "sha256": actual, "bytes": len(raw)})
    check("input_count", len(rows) == 28)
    return rows


def radial_differential_checks():
    ss = (F(1,1000), F(1,4), F(1,2), F(1), F(3,2),
          F(19,10), F(1999,1000))
    for d, s in itertools.product(range(4, 9), ss):
        p = s+2
        qs = {p/2, 1+s/4}
        if s+1 < min(d-2, F(d,2)):
            qs.add(s+1)
        for q, N, nu in itertools.product(
                sorted(qs), (2,3,7,41), (F(0),F(1,37),F(1),F(7,3))):
            check("admitted_weight_range",
                  1 < q < min(d-2,F(d,2)) and q <= s+1)
            # Evaluate derivatives at z=e_1 after factoring the radial power.
            # For R=sum z_j^2, w=R^(-q/2); second derivatives are
            # q(q+2) z_j z_k - q delta_jk at R=1.
            z = (F(1),) + (F(0),)*(d-1)
            hz = [[q*(q+2)*z[j]*z[k]-q*(j==k)
                   for k in range(d)] for j in range(d)]
            dk = [[s*(j==k)-s*p*z[j]*z[k]
                   for k in range(d)] for j in range(d)]
            db = [[F(0) for _ in range(2*d)] for _ in range(2*d)]
            for j, k in itertools.product(range(d), repeat=2):
                db[j][k] = dk[j][k]/N
                db[j][d+k] = -dk[j][k]/N
                db[d+j][k] = -dk[j][k]/N
                db[d+j][d+k] = dk[j][k]/N
            for j in range(d):
                ej = tuple(F(i==j) for i in range(d))
                center, difference = ej+ej, ej+scale(-1,ej)
                check("pair_center_jacobian", mv(db,center) == (F(0),)*(2*d))
                eigen = -2*s*(s+1)/N if j==0 else 2*s/N
                check("pair_radial_transverse_jacobian",
                      mv(db,difference) == scale(eigen,difference))
            diffusion = 2*nu*sum(hz[j][j] for j in range(d))
            drift = dot(scale(s/N,z)+scale(-s/N,z),
                        scale(-q,z)+scale(q,z))
            one_sided = 2*s/N
            independently_assembled = diffusion+drift+one_sided
            claimed = -2*nu*q*(d-2-q)-2*s*(q-1)/N
            check("retained_generator_identity",
                  independently_assembled == claimed)
            check("strict_repulsive_coefficient", 2*s*(q-1)>0)
            check("strict_diffusion_coefficient", 2*q*(d-2-q)>0)
            check("density_divergence_coefficient",
                  sum(dk[j][j] for j in range(d)) == s*(d-2-s))
            # Independently differentiate J=K dot Az for a quadratic local test.
            aa = [[F((j+1)*(k+1)+(j==k)) for k in range(d)]
                  for j in range(d)]
            az = mv(aa,z)
            source = dot(scale(s,z),az)
            grad_source = add(mv(dk,az),mv(aa,scale(s,z)))
            check("quadratic_source_homogeneity", dot(z,grad_source) == -s*source)


def exponent_checks():
    for d in range(4, 14):
        for numerator in range(1, 80):
            s = F(numerator,40)
            p, a, theta = s+2, s/(s+2), 1-s/d
            qstar, qminus = p/2, 1+s/4
            eta, eta_minus = s+1-qstar, s+1-qminus
            r, epsilon = p/qminus, 1/(6*p*p)
            check("qstar_admissible", 1<qstar<min(d-2,F(d,2)))
            check("qminus_admissible", 1<qminus<min(d-2,F(d,2)))
            check("gradient_square_weight", 2*qstar == p and 2*eta/p == a)
            check("gradient_tail_weight", qminus*r == p and r>2)
            check("eta_range", 0<=eta<2 and 0<=eta_minus<2)
            check("noise_crossover", (-2/p)*(-s/2) == a)
            check("low_noise_power", a-2/p == (s-2)/p)
            check("floor_gap_identity", a-theta == (s*p-2*d)/(d*p))
            check("floor_gap_strict", s*p < 2*d)
            check("heat_floor_self_power", (-2/F(d))*(-s/2) == s/d)
            check("heat_floor_pair_power", 1+(-2/F(d))*((d-s)/2) == s/d)
            check("sharp_floor_occupation_power", s/d-1 == -theta)
            check("tail_excess", r-2 == 2*s/(s+4))
            check("tail_diffusivity_power", eta_minus*r/2 == 3*s*p/(2*(s+4)))
            check("tail_final_power",
                  epsilon*eta_minus*r/2-(r-2)/(4*p) == -s/(4*p*(s+4)))
            check("low_final_power",
                  epsilon*(1-s/2) == (2-s)/(12*p*p))
            check("clipping_power", 2/(4*p)-1/p == -1/(2*p))
            check("haar_energy_power", a-1 == -2/p)
            check("scale_separation", epsilon < 2/p)
            check("faster_low_term_absorption",
                  (s-2)/p < -(2-s)/(12*p*p))
            exponents = (a-theta, -(2-s)/(12*p*p),
                         -s/(4*p*(s+4)), -1/(2*p), -2/p)
            check("all_five_rate_powers_negative", all(x<0 for x in exponents))
    # The obstruction at excluded endpoints is also tested explicitly.
    check("d3_weight_interval_empty", not (1 < 3-2))
    check("s2_low_power_zero", 1-F(2,2) == 0)
    check("d4_s2_weight_boundary", (F(2)+2)/2 == 4-2 == F(4,2))
    check("d4_s2_floor_gap_zero", F(2,4)-(1-F(2,4)) == 0)


def exact_scalar_tail_checks():
    for s in (F(1,100),F(1,4),F(1),F(3,2),F(199,100)):
        r=(s+2)/(1+s/4)
        for x,L in itertools.product(
                (F(0),F(1,5),F(1),F(9,4),F(5),F(21)),
                (F(1,10),F(1,2),F(1),F(7,3),F(30))):
            residual=max(x-L,F(0))
            # Raising both nonnegative sides to denominator(r) removes
            # every irrational power and preserves the inequality.
            m,n=r.numerator,r.denominator
            lhs=(residual*residual)**n
            rhs=L**(2*n-m)*x**m
            check("radial_tail_inequality_exact", lhs<=rhs)
    # x^eta <= 1+x^m is checked without floating powers on rational grids.
    for eta,m,x in itertools.product(
            (F(0),F(1,4),F(1,2),F(1),F(7,4)), (F(2),F(3)),
            (F(1,16),F(1,2),F(1),F(3),F(16))):
        if eta>m:
            continue
        from math import gcd
        den=eta.denominator*m.denominator//gcd(eta.denominator,m.denominator)
        # Use x=y^den, so the original nonnegative real-power inequality
        # is the following exact rational-power-free test.
        check("source_split_scalar_exact",
              x**int(eta*den) <= 1+x**int(m*den))


def field(matrix, xs):
    n,m=len(xs),len(matrix)
    zero=(F(0),)*len(matrix[0][0])
    means=[scale(F(1,m),tuple(sum(matrix[x][y][c] for y in range(m))
                              for c in range(len(zero)))) for x in range(m)]
    values=[]
    for i,xi in enumerate(xs):
        total=zero
        for j,xj in enumerate(xs):
            if i!=j:
                total=add(total,matrix[xi][xj])
        values.append(scale(F(1,n*n),sub(total,scale(n,means[xi]))))
    return values,means


def finite_law_checks():
    m=3
    directions=((F(3),F(4)),(F(5),F(12)),(F(8),F(15)))
    gg=[[scale(F((x+1)*(y+2)-4,3),directions[(x+2*y)%3])
         for y in range(m)] for x in range(m)]
    witnessed={"nonzero_triple":False,"nonzero_mixed":False,
               "nonzero_clip_tail_cross":False}
    examples=[]
    for n in (2,3,4,5):
        xs_all=list(itertools.product(range(m),repeat=n))
        weights=[F(1+sum(xs[i]==xs[j] for i in range(n) for j in range(i+1,n)))
                 for xs in xs_all]
        z=sum(weights)
        probs=[w/z for w in weights]
        haar=[F(1,m**n)]*len(xs_all)
        for x in range(m):
            check("finite_law_one_body_haar",
                  sum(prob for xs,prob in zip(xs_all,probs) if xs[0]==x)==F(1,m))
        pair=defaultdict(F)
        triple=defaultdict(F)
        for xs,prob in zip(xs_all,probs):
            pair[xs[:2]]+=prob
            if n>=3:
                triple[xs[:3]]+=prob
        e2=sum(abs(pair[(x,y)]-F(1,m*m))
               for x,y in itertools.product(range(m),repeat=2))
        e3=(sum(abs(triple[(x,y,z)]-F(1,m**3))
                for x,y,z in itertools.product(range(m),repeat=3)) if n>=3 else F(0))
        for threshold in (F(1,2),F(2),F(7)):
            clip=[]
            for row in gg:
                clipped=[]
                for v in row:
                    norm=rational_norm(v)
                    clipped.append(v if norm<=threshold else scale(threshold/norm,v))
                clip.append(clipped)
            tail=[[sub(gg[x][y],clip[x][y]) for y in range(m)] for x in range(m)]
            energies={}
            all_fields={}
            for name,matrix in (("full",gg),("clip",clip),("tail",tail)):
                values=[field(matrix,xs)[0] for xs in xs_all]
                means=field(matrix,xs_all[0])[1]
                all_fields[name]=values
                actual=sum(prob*sum(dot(v,v) for v in vv)
                           for prob,vv in zip(probs,values))
                reference=sum(prob*sum(dot(v,v) for v in vv)
                              for prob,vv in zip(haar,values))
                gn=sum(dot(v,v) for row in matrix for v in row)/m**2
                an=sum(dot(v,v) for v in means)/m
                check("exact_haar_deleted_coefficient",
                      reference==F(n-1,n**3)*gn-F(n-2,n**3)*an)
                h=[[sub(matrix[x][y],means[x]) for y in range(m)] for x in range(m)]
                pairterm=sum(prob*dot(h[xs[0]][xs[1]],h[xs[0]][xs[1]])
                             for xs,prob in zip(xs_all,probs))
                tripleterm=(sum(prob*dot(h[xs[0]][xs[1]],h[xs[0]][xs[2]])
                                for xs,prob in zip(xs_all,probs)) if n>=3 else F(0))
                mixed=sum(prob*dot(h[xs[0]][xs[1]],means[xs[0]])
                          for xs,prob in zip(xs_all,probs))
                one=sum(prob*dot(means[xs[0]],means[xs[0]])
                        for xs,prob in zip(xs_all,probs))
                expanded=((n-1)*pairterm+(n-1)*(n-2)*tripleterm
                          -2*(n-1)*mixed+one)/n**3
                check("all_four_actual_contractions", actual==expanded)
                check("actual_one_body_background", one==an)
                pairg=sum(prob*dot(matrix[xs[0]][xs[1]],matrix[xs[0]][xs[1]])
                          for xs,prob in zip(xs_all,probs))
                bound=F(2*(n-1)**2,n**3)*pairg+F(2,n)*an
                check("configuration_square_bound", actual<=bound)
                witnessed["nonzero_triple"] |= tripleterm!=0
                witnessed["nonzero_mixed"] |= mixed!=0
                energies[name]=(actual,reference)
                for nu in (F(0),F(1,17),F(1,2),F(1),F(2),F(7)):
                    if nu==0:
                        check("zero_noise_no_reciprocal", 2*nu*n*actual==0)
                        continue
                    b=min(1,1/nu)
                    physical=2*nu*n*b*actual
                    raw_bound=4*nu*b*(F((n-1)**2,n*n)*pairg+an)
                    check("physical_square_prefactor", physical<=raw_bound)
                    check("physical_bounds", b<=1 and nu*b<=1 and nu*b*b<=1)
                    if name=="clip":
                        actual_q=2*nu*n*b*actual
                        haar_q=2*nu*n*b*reference
                        error=8*nu*b*threshold**2*F(n-1,n*n)*(2*e2+(n-2)*e3)
                        check("clipped_law_error_all_contractions", abs(actual_q-haar_q)<=error)
            for idx,xs in enumerate(xs_all):
                for vf,vc,vr in zip(all_fields["full"][idx],
                                    all_fields["clip"][idx],all_fields["tail"][idx]):
                    check("field_full_clip_tail_identity", vf==add(vc,vr))
                    check("pointwise_hilbert_square", dot(vf,vf)<=2*dot(vc,vc)+2*dot(vr,vr))
            cross=sum(prob*sum(dot(vc,vr) for vc,vr in zip(cc,rr))
                      for prob,cc,rr in zip(probs,all_fields["clip"],all_fields["tail"]))
            af,ac,ar=(energies[k][0] for k in ("full","clip","tail"))
            check("nonorthogonal_energy_decomposition", af==ac+ar+2*cross)
            check("hilbert_cross_cauchy", cross*cross<=ac*ar)
            witnessed["nonzero_clip_tail_cross"] |= cross!=0
            if n in (2,3) and threshold==2:
                examples.append({"N":n,"clip_threshold":"2",
                                 "full_unscaled_energy":str(af),
                                 "clip_unscaled_energy":str(ac),
                                 "tail_unscaled_energy":str(ar),
                                 "clip_tail_cross":str(cross)})
    for name,value in witnessed.items():
        check("nontrivial_"+name,value)
    return examples


def polynomial_statistic_check():
    # Symmetric phi(x,y)=x^2*y+x*y^2+3*x^2+3*y^2+2*x*y.
    # Background is uniform on {0,1,2}; this is purely finite-sum algebra.
    def gradx(x,y):
        return 2*x*y+y*y+6*x+2*y
    for n in (2,3,4):
        for xs in itertools.product(map(F,range(3)),repeat=n):
            for i,x in enumerate(xs):
                ordered=F(0)
                for j,k in itertools.permutations(range(n),2):
                    if j==i:
                        ordered+=gradx(xs[j],xs[k])/(2*n*n)
                    if k==i:
                        ordered+=gradx(xs[k],xs[j])/(2*n*n)
                mean=sum(gradx(x,F(y)) for y in range(3))/3
                direct=ordered-mean/n
                claimed=(sum(gradx(x,xs[j]) for j in range(n) if j!=i)-n*mean)/n**2
                check("raw_ordered_statistic_derivative", direct==claimed)
    for n in (2,3,4,17):
        unordered=list(itertools.combinations(range(n),2))
        diagonal_laplacian_coefficient=sum((F(2,n) for _ in unordered),F(0))
        check("actual_energy_divergence_label_factor", diagonal_laplacian_coefficient==n-1)
        check("heat_floor_self_diagonal_factor", F(n,2*n)==F(1,2))


def response_slot_checks():
    m=4
    density=(F(2),F(-1),F(0),F(-1))
    characters=((1,1,1,1),(1,0,-1,0),(1,-1,1,-1))
    eigenvalues=(0,2,4)
    def response(matrix):
        return [[-sum(density[w]*(matrix[(x+w)%m][y]+matrix[x][(y+w)%m])
                       for w in range(m)) for y in range(m)] for x in range(m)]
    for k,l in itertools.product(range(3),repeat=2):
        matrix=[[F(characters[k][x]*characters[l][y]) for y in range(m)] for x in range(m)]
        result=response(matrix)
        check("both_response_slots_fourier",
              result==[[-(eigenvalues[k]+eigenvalues[l])*v for v in row] for row in matrix])
        for slot in (0,1):
            def difference(mat):
                return [[(mat[(x+1)%m][y]-mat[x][y]) if slot==0
                         else (mat[x][(y+1)%m]-mat[x][y]) for y in range(m)] for x in range(m)]
            check("homogeneous_translation_derivative_commutation",
                  difference(result)==response(difference(matrix)))
    check("compensated_response_total_mass", sum(density)==0)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    parser.add_argument("--verify-results",type=Path)
    args=parser.parse_args()
    base=Path(__file__).resolve().parents[3]
    rows=source_hashes(base)
    radial_differential_checks()
    exponent_checks()
    exact_scalar_tail_checks()
    examples=finite_law_checks()
    polynomial_statistic_check()
    response_slot_checks()
    result={
        "task":"TASK072",
        "role":"fresh hostile supporting diagnostics",
        "arithmetic":"exact fractions and integer arithmetic only",
        "randomness":"none",
        "prior_checker_imports":"none",
        "scope_warning":"Diagnostics support the written proof audit and assign no mathematical or audit certification.",
        "input_count":len(rows),
        "candidate_sha256":next(r["sha256"] for r in rows if r["path"]=="MEMORANDA/ROUND_013_BOUNDED_NOISE_SMALL_RIESZ.md"),
        "check_count":sum(COUNTS.values()),
        "groups":dict(sorted(COUNTS.items())),
        "nontrivial_finite_law_examples":examples,
        "result":"PASS_EXACT_DIAGNOSTICS"
    }
    if args.verify_results:
        expected=json.loads(args.verify_results.read_text())
        if result!=expected:
            raise AssertionError("Issued deterministic results differ from the fresh recomputation.")
    data=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(data)
    print(data,end="")


if __name__=="__main__":
    main()
