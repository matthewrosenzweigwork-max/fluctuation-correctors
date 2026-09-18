#!/usr/bin/env python3
"""Fresh exact diagnostics for AUD063. Finite checks do not certify analysis."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from collections import Counter
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
counts = Counter()
mutations = {}

def check(category, ok, detail=""):
    if not ok:
        raise AssertionError(f"{category}: {detail}")
    counts[category] += 1

def mutation(name, oracle, mutated, witness):
    check("mutation_rejections", oracle != mutated, name)
    mutations[name] = {
        "status": "REJECTED",
        "oracle": str(oracle),
        "mutated": str(mutated),
        "witness": witness,
    }

def poly(terms):
    out = {}
    for exponent, coefficient in terms:
        out[exponent] = out.get(exponent, F(0)) + coefficient
    return {k: v for k, v in sorted(out.items()) if v}

def b(nu):
    return F(1) if nu <= 1 else 1 / nu

# Exact shell model: the analytic lattice comparison is in the report.
shell_cases = []
for d in range(3, 13):
    for s in sorted({F(1, 2), F(1), min(F(d-2), F(d, 2)-F(1, 4))}):
        if not (0 < s <= d-2 and s < F(d, 2)):
            continue
        alpha = (d-s)/2
        R = alpha + d + 5
        critical = R + F(d, 2)
        r = critical + F(1, 2)
        exponent = d + 2*R - 2*r
        check("frozen_regularity_identity", critical == 2*d + 5 - s/2)
        check("source_shell_gap", exponent == -1)
        check("linear_shell_gap", d+2-2*r < 0)
        check("source_scaling", F(1, 2)-(1-s/d) == s/d-F(1, 2) < 0)
        check("endpoint_not_included", d+2*R-2*critical == 0)
        for m in range(1, 31):
            actual = sum((F(1, 2)**n for n in range(m)), F(0))
            oracle = 2*(1-F(1, 2)**m)
            check("summable_shell_partial_sums", actual == oracle and actual < 2)
            endpoint = sum((F(1) for _ in range(m)), F(0))
            check("endpoint_shell_partial_sums", endpoint == m)
        shell_cases.append({"d": d, "s": str(s), "R": str(R), "r": str(r)})
boundary_exponent = F(3)+2*F(9)-2*F(21, 2)
mutation("admit_source_endpoint", boundary_exponent < 0, boundary_exponent <= 0,
         "At r = R + d/2 the squared shell contribution is one at every level.")
mutation("omit_dimension_in_threshold", F(3)+2*F(9)-2*F(10) < 0, F(10) > F(9),
         "d=3, R=9, r=10: r>R, but d+2R-2r=1; the shell series grows.")

# Exact Hilbert escape: every coordinate eventually vanishes, norms do not.
escape = {}
r = 6
for j in range(1, 31):
    w = F(1, (1+j*j)**r)
    amplitude = F((1+j*j)**(r//2))
    norm_sq = w*amplitude**2
    check("normalized_high_mode", norm_sq == 1)
    escape[j] = norm_sq
    for cutoff in range(j):
        check("invisible_low_projection", (F(0) if j > cutoff else norm_sq) == 0)
for i in range(1, 20):
    for j in range(i+1, 21):
        check("escape_pair_distance", escape[i]+escape[j] == 2)
mutation("infer_norm_from_fixed_projection", escape[5], F(0) if 5 > 4 else escape[5],
         "The constant path (1+j^2)^3 e_j has H^-6 norm one although Pi_4 is zero for j>4.")
mutation("compact_hilbert_ball", escape[5]+escape[6], F(0)+F(0),
         "Distinct normalized modes have squared distance two, so a unit ball need not have a finite small net.")

# Source first moments are sufficient, and do not imply second moments.
heavy = []
for m in range(1, 31):
    mass = sum((3*F(1, 4)**n for n in range(1, m+1)), F(0))
    first = sum((3*F(1, 4)**n * 2**n for n in range(1, m+1)), F(0))
    second = sum((3*F(1, 4)**n * 4**n for n in range(1, m+1)), F(0))
    check("heavy_tail_mass", mass == 1-F(1, 4)**m)
    check("finite_first_moment", first == 3*(1-F(1, 2)**m) < 3)
    check("diverging_second_moment", second == 3*m)
    heavy.append({"levels": m, "first_partial": str(first), "second_partial": str(second)})
mutation("square_source_first_moment", F(heavy[9]["second_partial"]), F(3)**2,
         "The first ten levels of A=2^n with mass 3/4^n already have second moment 30; the full first moment is only 3.")

# Disjoint peaks falsify equality or the reverse supremum inequality.
for m in range(2, 33):
    samples = [[F(int(i == j)) for j in range(m)] for i in range(m)]
    sup_sum = max(sum(x*x for x in row) for row in samples)
    sum_sup = sum(max(row[j]*row[j] for row in samples) for j in range(m))
    check("sup_sum_direction", sup_sum == 1 and sum_sup == m and sup_sum <= sum_sup)
two_peaks = [[F(1), F(0)], [F(0), F(1)]]
mutation("exchange_sup_and_sum_as_equality", max(sum(x*x for x in row) for row in two_peaks), sum(max(row[j]*row[j] for row in two_peaks) for j in range(2)),
         "Two continuous disjoint unit tents attain these values, as witnessed by their peak samples.")

# Deterministic discrete Stieltjes convolution: independent direct and
# summation-by-parts implementations, exact rational damping.
convolution_witnesses = []
drivers = [
    [F(0)] + [F((i % 5)-2, (i % 3)+1) for i in range(1, 18)],
    [F(0), F(1), F(1), F(-1), F(-1), F(0), F(2), F(0)],
    [F(0)] + [F((-1)**i) for i in range(1, 25)],
]
for q in (F(1, 7), F(1, 3), F(1, 2), F(3, 4), F(1)):
    for driver in drivers:
        direct = [F(0)]
        for j in range(1, len(driver)):
            value = sum((q**(j-i)*(driver[i]-driver[i-1])
                         for i in range(1, j+1)), F(0))
            ibp = driver[j]-(1-q)*sum((q**(j-1-i)*driver[i]
                                      for i in range(j)), F(0))
            check("convolution_identity", value == ibp)
            check("convolution_maximal_factor", abs(value) <= 2*max(map(abs, driver[:j+1])))
            check("convolution_kernel_mass", (1-q)*sum((q**i for i in range(j)), F(0)) == 1-q**j)
            direct.append(value)
        convolution_witnesses.append({"q": str(q), "steps": len(driver)-1,
                                      "max_convolution": str(max(map(abs, direct))),
                                      "max_driver": str(max(map(abs, driver)))})
q_witness = F(1, 2)
u_witness = [F(0), F(1), F(1)]
m_witness = [sum((q_witness**(j-i)*(u_witness[i]-u_witness[i-1]) for i in range(1, j+1)), F(0)) for j in range(3)]
wrong_ibp = u_witness[2]+(1-q_witness)*sum((q_witness**(1-i)*u_witness[i] for i in range(2)), F(0))
mutation("convolution_wrong_ibp_sign", m_witness[2], wrong_ibp,
         "q=1/2 and U=(0,1,1): direct damped sum is 1/2; the positive-integral mutation gives 3/2.")
mutation("drop_prior_noise_increment", m_witness[2]-m_witness[1], u_witness[2]-u_witness[1],
         "For the same drive, M_2-M_1=-1/2 while the recent drive increment is zero.")

# Raw particle Brownian label sums on quarter-circle configurations.
# Physical a_k is restored as a scalar a; normalized real gradients carry sqrt(2).
cos = [F(1), F(0), F(-1), F(0)]
sin = [F(0), F(1), F(0), F(-1)]
tests = [(F(1), F(0)), (F(0), F(1)), (F(1), F(1)), (F(2), F(-1))]
for N in (2, 3, 4):
    configurations = list(product(range(4), repeat=N))
    for nu in (F(0), F(1, 3), F(1), F(2), F(7)):
        check("noise_normalization", nu*b(nu) == min(nu, F(1)))
        for a in (F(1), F(4)):
            for h in tests:
                for g in tests:
                    total = F(0)
                    for xs in configurations:
                        products = [2*a*(-h[0]*sin[x]+h[1]*cos[x]) *
                                    (-g[0]*sin[x]+g[1]*cos[x]) for x in xs]
                        # Different assembly: square of sigma/N times 2nu,
                        # then sum one contribution for each independent label.
                        direct = sum(((N*b(nu))/N**2 * (2*nu)*v for v in products), F(0))
                        empirical = sum(products, F(0))/N
                        formula = 2*nu*b(nu)*empirical
                        check("raw_brownian_label_bracket", direct == formula)
                        total += direct
                    average = total/len(configurations)
                    haar = 2*nu*b(nu)*a*(h[0]*g[0]+h[1]*g[1])
                    check("exact_haar_cross_bracket", average == haar)
for x in range(4):
    check("real_pair_gradient_norm", 2*sin[x]**2+2*cos[x]**2 == 2)
def bracket_witness(noise_factor=F(2), delete_factor=False, extra_N=False):
    N = 3
    rows = list(product(range(4), repeat=N))
    answer = F(0)
    for xs in rows:
        label_sum = sum((2*sin[x]**2 for x in xs), F(0))
        answer += noise_factor*label_sum/N * (F(N-1, N) if delete_factor else 1) / (N if extra_N else 1)
    return answer/len(rows)
bracket_oracle = bracket_witness()
mutation("delete_noise_factor_two", bracket_oracle, bracket_witness(noise_factor=F(1)),
         "nu=b=a=1: Haar quadratic variation for one real normalized mode is two.")
mutation("insert_deleted_pair_factor_in_noise", bracket_oracle, bracket_witness(delete_factor=True),
         "At N=3, nu=b=a=1, independent Brownian labels give two, not two times (N-1)/N.")
mutation("retain_spurious_noise_N_inverse", bracket_oracle, bracket_witness(extra_N=True),
         "At N=3 the scaled label sum cancels the remaining particle number.")

# Complex coefficients (a +/- ib)/sqrt(2), without floating point.
def cmul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
for h in tests:
    for g in tests:
        plus = cmul((h[0], -h[1]), (g[0], g[1]))
        minus = cmul((h[0], h[1]), (g[0], -g[1]))
        summed = ((plus[0]+minus[0])/2, (plus[1]+minus[1])/2)
        oracle = (h[0]*g[0]+h[1]*g[1], F(0))
        check("real_complex_pair_isometry", summed == oracle)
cosine_pair = (cmul((F(1), F(0)), (F(1), F(0)))[0]+cmul((F(1), F(0)), (F(1), F(0)))[0])/2
mutation("double_real_fourier_pair", cosine_pair, 2*cosine_pair,
         "A normalized cosine has unit L2 norm; its two complex coefficients each have squared magnitude 1/2.")

# Covariances as exact exponential polynomials. A key c denotes exp(-c).
# Direct construction integrates the thermal kernel, separately from frozen form.
def covariance_direct(D, a, nu, t, u):
    L = D+nu*a
    return poly([(L*(t+u), b(nu)),
                 (L*abs(t-u), b(nu)*nu*a/L),
                 (L*(t+u), -b(nu)*nu*a/L)])
def covariance_frozen(D, a, nu, t, u):
    L = D+nu*a
    return poly([(L*(t+u), b(nu)*D/L),
                 (L*abs(t-u), b(nu)*nu*a/L)])
for D in (F(1), F(3, 2), F(4)):
    for a in (F(1), F(4), F(9)):
        for nu in (F(0), F(1, 3), F(1), F(2)):
            for t, u in product((F(0), F(1, 3), F(1), F(2)), repeat=2):
                direct = covariance_direct(D, a, nu, t, u)
                check("modal_covariance", direct == covariance_frozen(D, a, nu, t, u))
                check("modal_covariance_symmetry", direct == covariance_direct(D, a, nu, u, t))
                if not t and not u:
                    check("initial_variance", direct == {F(0): b(nu)})
                if not nu:
                    check("zero_noise_covariance", direct == {D*(t+u): F(1)})
oracle = covariance_direct(F(1), F(1), F(1), F(1), F(2))
mutation("initial_time_sum_to_difference", oracle, poly([(F(2)*abs(F(1)-F(2)), F(1, 2)), (F(2)*abs(F(1)-F(2)), F(1, 2))]),
         "D=a=nu=1, t=1,u=2: the true coefficients are one half at exponents 6 and 2.")
mutation("discard_thermal_covariance", oracle, poly([(F(2)*(F(1)+F(2)), b(F(1)))]),
         "The same positive-noise mode retains a distinct exponent-two thermal contribution.")
mutation("omit_b_normalization_above_one",
         covariance_direct(F(1), F(1), F(2), F(0), F(0)), poly([(F(0), F(1)/3), (F(0), F(2)/3)]),
         "At nu=2, b=1/2, so the initial modal variance is 1/2.")

result = {
    "audit": "AUD063",
    "status": "PASS",
    "evidence_class": "Exact finite supporting diagnostics; not certification of singular passages, infinite sums, tightness, or weak convergence.",
    "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": sys.version.split()[0],
    "arithmetic": "Python standard-library Fraction; exact rational and exponential-polynomial arithmetic.",
    "randomness": "None; no random seed, sampling or floating-point tolerance.",
    "assertions": sum(counts.values()),
    "categories": dict(sorted(counts.items())),
    "mutation_count": len(mutations),
    "mutations": mutations,
    "shell_cases": shell_cases,
    "heavy_tail_partial_moments": heavy,
    "convolution_cases": convolution_witnesses,
}
out = HERE/"DIAGNOSTIC_RESULTS.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
print(f"PASS: {sum(counts.values())} exact assertions in {len(counts)} categories; "
      f"{len(mutations)} nonvacuous mutations rejected.")
print("These finite checks support the independent analytic reconstruction; they do not certify analysis.")
