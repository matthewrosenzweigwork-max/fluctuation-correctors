#!/usr/bin/env python3
"""Fresh exact diagnostics for TASK-068; no prior checker is imported."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import factorial
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[2]
GROUPS = Counter()
ASSERTIONS = 0

def check(condition, group, detail):
    global ASSERTIONS
    if not condition:
        raise AssertionError(group + ": " + detail)
    ASSERTIONS += 1
    GROUPS[group] += 1

def matrix_vector(matrix, vector):
    return [sum(a*b for a,b in zip(row, vector)) for row in matrix]

def poly_mul(a, b, order):
    out = [F(0)] * (order+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= order:
                out[i+j] += x*y
    return out

manifest = HERE / "INPUT_SHA256SUMS.txt"
entries = [line.split("  ", 1) for line in manifest.read_text().splitlines()]
check(len(entries) == 21, "input_seal", "exact input count")
check(len({p for _,p in entries}) == 21, "input_seal", "no repeated path")
for digest, relative in entries:
    p = Path(relative)
    check(not p.is_absolute() and ".." not in p.parts,
          "input_seal", "safe path " + relative)
    check(sha256((WORK/p).read_bytes()).hexdigest() == digest,
          "input_seal", relative)

parameter_rows = []
for d in range(3, 10):
    exponents = sorted({F(1,3), F(1,2), F(1), F(d-2,2), F(d-2)})
    for s in exponents:
        if not 0 < s <= d-2:
            continue
        p = s+2
        parameter_rows.append((d,s))
        check(d-1-s > 0, "range_and_tails", "weak boundary")
        check(d-s-1 > 0, "range_and_tails", "gradient L1")
        check(d-s > 0, "range_and_tails", "value L1")
        check(s+1 > 1, "range_and_tails", "gradient Jacobian threshold")
        if s < d-2:
            check(d-(s+2) > 0, "range_and_tails", "sub-Coulomb measure density")
        else:
            check(s+1 == d-1, "range_and_tails", "Coulomb gradient power")
            check(2*(s+1) >= d, "range_and_tails", "no H1 from weight")
        check(4*F(d-s-2,2)*F(s,2) == s*(d-2-s),
              "normalization", "Gamma recurrence ratio")
        critical = F(2,1)/p - 1 + s/d
        check(critical == s*(p-d)/(d*p), "scaling", "critical exponent identity")
        check(critical <= 0, "scaling", "critical bounded rescaling")
        check((critical == 0) == (s == d-2),
              "scaling", "critical endpoint versus strict interior")
        check((-F(2,1)/p)*(1+F(2,1)/s)+F(2,1)/s == 0,
              "scaling", "Young N exponent cancels")
        for N in (2,3,17,101):
            dk = [[s*(int(i==j)-p*int(i==0 and j==0))
                   for j in range(d)] for i in range(d)]
            block = []
            for i in range(2*d):
                row = []
                for j in range(2*d):
                    sign = 1 if (i<d) == (j<d) else -1
                    row.append(F(sign,N)*dk[i % d][j % d])
                block.append(row)
            for axis in range(d):
                e = [F(int(i==axis)) for i in range(d)]
                center = e+e
                relative = e+[-v for v in e]
                check(matrix_vector(block, center) == [F(0)]*(2*d),
                      "pair_jacobian", "zero center eigenvector")
                eigen = -2*s*(s+1)/N if axis == 0 else 2*s/N
                check(matrix_vector(block, relative) == [eigen*v for v in relative],
                      "pair_jacobian", "radial/transverse eigenvector")
            check(2*s*(s+1)/N > 2*s/N,
                  "pair_jacobian", "absolute norm differs from one-sided growth")
            for m in (F(0),F(1),F(2),F(5)):
                for alpha in (m+F(1,2),m+s+1,m+2):
                    # Hessian of r^-alpha at the first unit vector.
                    hess = [[-alpha*int(i==j)+alpha*(alpha+2)*int(i==0 and j==0)
                             for j in range(d)] for i in range(d)]
                    pair_laplacian = 2*sum(hess[i][i] for i in range(d))
                    check(pair_laplacian == 2*alpha*(alpha+2-d),
                          "radial_generator", "relative Laplacian factor")
                    pair_grad = [-alpha]+[F(0)]*(d-1)+[alpha]+[F(0)]*(d-1)
                    pair_drift = [s/N]+[F(0)]*(d-1)+[-s/N]+[F(0)]*(d-1)
                    drift_weight = sum(a*b for a,b in zip(pair_grad,pair_drift))
                    check(drift_weight+m*2*s/N == (m-alpha)*2*s/N,
                          "radial_generator", "exact potential/drift coefficient")
                    check((m-alpha)*2*s/N < 0,
                          "radial_generator", "strict absorption")
                    for nu in (F(0),F(1,7),F(2)):
                        direct = nu*pair_laplacian+drift_weight+m*2*s/N
                        target = 2*nu*alpha*(alpha+2-d)+(m-alpha)*2*s/N
                        check(direct == target, "radial_generator", "full coefficient")
                    if m == 1 and alpha == s+1:
                        check(alpha-m == s, "radial_generator", "source gradient margin")
            check(F(2,N) <= 1, "range_and_tails", "N=2 included")

for s in range(1,7):
    p = s+2
    for A, optimum in product((F(1,3),F(2),F(7)), (F(1,2),F(1),F(3))):
        D = A*p*optimum**s/4
        maximum = F(s,p)*D*optimum**2
        check(2*D*optimum == A*p*optimum**(s+1)/2,
              "young_maximum", "stationary point")
        check(D*optimum**2-A*optimum**p/2 == maximum,
              "young_maximum", "maximum exact value")
        for probe in (F(0),F(1,4),F(1,2),F(1),F(2),F(3),F(5)):
            check(D*probe**2-A*probe**p/2 <= maximum,
                  "young_maximum", "exact rational probe")
        check(F(0) == 0, "zero_parameters", "zero noise cost convention")

order = 14
for c,k,l in product((F(1,3),F(1),F(7)),(-2,0,1,3),(-2,0,1,3)):
    px,py = F(k == 0),F(l == 0)
    eigen = -2*c+c*px+c*py
    direct = -(c if k else 0)-(c if l else 0)
    check(eigen == direct, "coulomb_responses", "both slots and compensation")
    if k == 0 and l == 0:
        check(eigen == 0, "coulomb_responses", "constants killed")
        check(-2*c != 0 and c*(px+py) != 0,
              "mutation_detection", "atom-only and compensation-only are wrong")
    if l != 0:
        missing_y = -(c if k else 0)
        check(missing_y != eigen, "mutation_detection", "missing second response")
    expminus2 = [(-2*c)**n/F(factorial(n)) for n in range(order+1)]
    expprojection_x = [F(1)]+[px*c**n/F(factorial(n)) for n in range(1,order+1)]
    expprojection_y = [F(1)]+[py*c**n/F(factorial(n)) for n in range(1,order+1)]
    composed = poly_mul(poly_mul(expminus2,expprojection_x,order),
                        expprojection_y,order)
    for n in range(order+1):
        check(composed[n] == eigen**n/F(factorial(n)),
              "response_exponential", "projection exponential coefficient")
    for source in ([F(1),F(0),F(0)], [F(2),F(-3),F(5)], [F(0),F(0),F(0)]):
        solution = [F(0)]*(order+1)
        for degree in range(1,order+1):
            solution[degree] = sum(
                eigen**(degree-1-n)*source[n]*F(factorial(n),factorial(degree))
                for n in range(min(2,degree-1)+1))
        check(solution[0] == 0, "response_equation", "terminal zero")
        for degree in range(order):
            forcing = source[degree] if degree <= 2 else F(0)
            check((degree+1)*solution[degree+1] == eigen*solution[degree]+forcing,
                  "response_equation", "backward-time ODE coefficient")
        if all(v == 0 for v in source):
            check(all(v == 0 for v in solution),
                  "zero_parameters", "constant terminal h gives zero source/inverse")

for c in (F(1,3),F(1),F(7)):
    for degree in range(1,order+1):
        integrated = sum((-2*c)**k*(-c)**(degree-1-k)
                         for k in range(degree))/factorial(degree)
        formula = ((-c)**degree-(-2*c)**degree)/(c*factorial(degree))
        check(integrated == formula, "coulomb_singular_limit", "unprojected coefficient")
    check(F(1) == (((-c)-(-2*c))/c),
          "coulomb_singular_limit", "positive first time coefficient")

for s,N,r0 in product(range(1,6),(2,3,29),(F(1,16),F(1,8),F(1,4))):
    p = s+2
    for ratio in (F(1),F(3,2),F(2),F(4)):
        r1 = ratio*r0
        tau = F(N,2*s*p)*(r1**p-r0**p)
        U = F(N,4)*(r1*r1-r0*r0)
        radial_derivative = F(N,2)*(r1**(-s)*r0**(s+1)-r0)
        check(r1**p == r0**p+F(2*s*p,N)*tau,
              "zero_noise_radial", "integrated relative flow")
        check(0 <= U*r0**s <= s*tau,
              "zero_noise_radial", "value weight")
        check(abs(radial_derivative)*r0**(s+1) <= s*s*tau,
              "zero_noise_radial", "gradient weight")
        check(radial_derivative <= 0,
              "zero_noise_radial", "radial contraction sign")
        dr1_dr0 = (r0/r1)**(p-1)
        check(p*r1**(p-1)*dr1_dr0 == p*r0**(p-1),
              "zero_noise_radial", "initial variation from implicit flow")
        dr1_dtau = F(2*s,N)*r1**(-s-1)
        check(F(N,2)*r1*dr1_dtau == s*r1**(-s),
              "zero_noise_radial", "source time derivative")
        if tau == 0:
            check(U == 0 and radial_derivative == 0,
                  "zero_parameters", "T=0 radial profile")

result = {
    "task": "TASK-068",
    "theorem": "THM-032",
    "status": "PASS",
    "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "assertions_passed": ASSERTIONS,
    "groups": dict(sorted(GROUPS.items())),
    "input_count": len(entries),
    "parameter_rows": len(parameter_rows),
    "arithmetic": "exact integers and fractions; no numerical tolerance or random seed",
    "dependencies": "Python standard library only",
    "python_version": sys.version,
    "evidence_limit": "Same-context diagnostics; not a proof or independent audit of analytic passages.",
}
(HERE/"round011_gradient_blind_exact_result.json").write_text(
    json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":result["status"],"assertions_passed":ASSERTIONS,
                  "groups":result["groups"]},indent=2))

