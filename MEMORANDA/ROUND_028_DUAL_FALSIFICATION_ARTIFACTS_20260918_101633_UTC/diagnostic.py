#!/usr/bin/env python3
"""Fresh, deterministic support checks. Standard library; read-only."""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import Counter
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()
MUTATIONS = []

def check(category, actual, expected=True):
    COUNTS[category] += 1
    if actual != expected:
        raise AssertionError((category, str(actual), str(expected)))

def mutation(name, correct, wrong, limitation):
    check("nonzero_mutation", correct != wrong)
    MUTATIONS.append({"name": name, "correct": str(correct),
                      "mutated": str(wrong), "limitation": limitation})

class G:
    __slots__ = ("r", "i")
    def __init__(self, r=0, i=0):
        if isinstance(r, G):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = Q(r), Q(i)
    def __add__(self, other):
        other=G(other)
        return G(self.r+other.r,self.i+other.i)
    __radd__=__add__
    def __neg__(self):
        return G(-self.r,-self.i)
    def __sub__(self, other):
        return self+-G(other)
    def __rsub__(self, other):
        return G(other)+-self
    def __mul__(self, other):
        other=G(other)
        return G(self.r*other.r-self.i*other.i,
                 self.r*other.i+self.i*other.r)
    __rmul__=__mul__
    def __truediv__(self, other):
        other=Q(other)
        return G(self.r/other,self.i/other)
    def conj(self):
        return G(self.r,-self.i)
    def norm2(self):
        return self.r*self.r+self.i*self.i
    def __eq__(self, other):
        other=G(other)
        return self.r==other.r and self.i==other.i
    def __str__(self):
        return str(self.r)+"+("+str(self.i)+")i"

def avg(seq):
    seq=list(seq)
    return sum(seq)/len(seq)

def center(table):
    m=len(table)
    rows=[avg(row) for row in table]
    cols=[avg(table[x][y] for x in range(m)) for y in range(m)]
    mu=avg(rows)
    return [[table[x][y]-rows[x]-cols[y]+mu
             for y in range(m)] for x in range(m)]

def ustat(table,x):
    n=len(x)
    return sum(table[x[i]][x[j]] for i in range(n)
               for j in range(n) if i!=j)/(2*n*n)

def norm2(x):
    return x.norm2() if isinstance(x,G) else x*x

# Complete input read-back, never reading a neighboring repository source.
manifest=(ROOT/"INPUT_SHA256SUMS.txt").read_text().splitlines()
check("input_count",len(manifest),17)
for line in manifest:
    digest,rel=line.split("  ",1)
    p=ROOT/"INPUTS"/rel
    check("input_regular",p.is_file() and not p.is_symlink())
    check("input_hash",hashlib.sha256(p.read_bytes()).hexdigest(),digest)

# Literal finite iid laws and canonical clipping.
m=4
e=[G(1),G(0,1),G(-1),G(0,-1)]
w=[Q(0),Q(3),Q(1),Q(3)]
complex_j=[[(e[x]+e[y])*(w[(x-y)%m]-Q(3,2))
            for y in range(m)] for x in range(m)]
for row in complex_j:
    check("complex_zero_row",avg(row),G(0))
for x in range(m):
    for y in range(m):
        check("complex_symmetry",complex_j[x][y],complex_j[y][x])
raw=[[Q((x-y)%m == 0)*9-Q((x-y)%m == 2)*5+Q(x+y,3)
      for y in range(m)] for x in range(m)]
real_j=center(raw)
for row in real_j:
    check("real_zero_row",avg(row),Q(0))
for cutoff in [Q(1,2),Q(1),Q(2),Q(4)]:
    clip=[[max(-cutoff,min(cutoff,z)) for z in row] for row in real_j]
    v=center(clip)
    for row in v:
        check("clipped_zero_row",avg(row),Q(0))
    check("orthogonal_projection_contraction",
          avg(z*z for row in v for z in row)
          <=avg(z*z for row in clip for z in row))
    check("projection_l1_residual",
          avg(abs(real_j[x][y]-v[x][y]) for x in range(m)
              for y in range(m))
          <=4*avg(abs(real_j[x][y]-clip[x][y]) for x in range(m)
                   for y in range(m)))
    for n in range(2,6):
        values=[ustat(v,x) for x in product(range(m),repeat=n)]
        check("clipped_ustat_mean",avg(values),Q(0))
        direct=avg(z*z for z in values)
        formula=Q(n-1,2*n**3)*avg(z*z for row in v for z in row)
        check("clipped_ustat_variance",direct,formula)
        if cutoff==1 and n==3:
            mutation("replace_N_power_by_falling_factorial",
                     direct, direct*Q(n*n,(n*(n-1)))**2,
                     "Finite iid coefficient witness, not singular dynamics.")
        if cutoff==1 and n==2:
            mutation("omit_ordered_pair_half",direct,4*direct,
                     "Double orientation must combine exactly once.")

for n in range(2,6):
    squares=[]
    modes=[]
    for x in product(range(m),repeat=n):
        F=sum(e[y] for y in x)/n
        U=ustat(complex_j,x)
        J=[[complex_j[y][z]-(e[y]+e[z]) for z in range(m)]
           for y in range(m)]
        raw_force=ustat(J,x)
        check("literal_row_deletion",raw_force,U-Q(n-1,n)*F)
        squares.append(U.norm2())
        modes.append(F.norm2())
    check("complex_ustat_variance",avg(squares),
          Q(n-1,2*n**3)*avg(z.norm2() for row in complex_j for z in row))
    check("iid_mode_variance",avg(modes),Q(1,n))
mutation("use_c_in_place_of_c_one_minus_one_over_N",
         Q(2,3),Q(1),"Exact N=3 response-row coefficient.")

# Fusion law: enumerate all pair choices and all independent remaining slots.
for n in range(2,6):
    vals=[]
    first=[]
    for i,j in combinations(range(n),2):
        for base in product(range(m),repeat=n-1):
            x=[None]*n
            x[i]=x[j]=base[0]
            rest=iter(base[1:])
            for r in range(n):
                if r not in (i,j):
                    x[r]=next(rest)
            F=sum(e[z] for z in x)/n
            vals.append(F.norm2())
            first.append(F)
    check("fusion_mean",avg(first),G(0))
    check("fusion_mode_variance",avg(vals),Q(n+2,n*n))
    mutation("fusion_is_product_Haar_N"+str(n),avg(vals),Q(1,n),
             "Collision endpoint differs from an iid current configuration.")
for n in range(2,20):
    check("flux_mass",Q(2,n)*Q(n*(n-1),2),Q(n-1))
    check("laplacian_pair_factor",Q(2,n)*len(list(combinations(range(n),2))),
          Q(n-1))
    counts=Counter()
    for i,j in product(range(n),repeat=2):
        if j<2:
            counts["fused_fused" if i<2 else "outside_fused"]+=1
        elif i<2:
            counts["fused_outside"]+=1
        elif i==j:
            counts["same_outside"]+=1
        else:
            counts["distinct_outside"]+=1
    expected={"fused_fused":4,"outside_fused":2*(n-2),
              "fused_outside":2*(n-2),"same_outside":n-2,
              "distinct_outside":(n-2)*(n-3)}
    for key,val in expected.items():
        check("five_marked_label_classes",counts[key],val)
    check("all_marked_terms_counted",sum(counts.values()),n*n)
mutation("single_instead_of_double_collision_flux",
         Q(2,5)*10,Q(1,5)*10,
         "One pair contributes from two differentiated coordinates.")

# Finite sub-Markov model, solely a normalization/conditioning diagnostic.
Qm=[[Q(6,10),Q(1,10),Q(0)],
    [Q(0),Q(6,10),Q(2,10)],
    [Q(1,10),Q(0),Q(5,10)]]
p=Q(7,10)
pi=[Q(1,3)]*3
kill=[1-sum(row) for row in Qm]
gamma=[pi[i]*kill[i]/(1-p) for i in range(3)]
Pm=[[Qm[j][i]/p for j in range(3)] for i in range(3)]
for j in range(3):
    check("qsd_column_sum",sum(Qm[i][j] for i in range(3)),p)
    check("dual_Markov_row",sum(Pm[j]),Q(1))
check("death_mark_mass",sum(gamma),Q(1))
f=[Q(1),Q(-2),Q(3)]
response=Q(2,5)
for length in range(1,6):
    mass=Q(0)
    final=[Q(0)]*3
    initial=[Q(0)]*3
    err=Q(0)
    wrong_orientation=Q(0)
    death=[Q(0)]*3
    mark_cross=Q(0)
    initial_mark=Q(0)
    final_mark=Q(0)
    for path in product(range(3),repeat=length+1):
        weight=pi[path[0]]
        reverse=pi[path[-1]]
        for s in range(length):
            weight*=Qm[path[s]][path[s+1]]
            reverse*=Pm[path[length-s]][path[length-s-1]]
        check("whole_path_normalization",weight/(p**length),reverse)
        mass+=weight
        final[path[-1]]+=weight
        initial[path[0]]+=weight
        err+=weight*(f[path[0]]-response*f[path[-1]])**2
        wrong_orientation+=weight*(f[path[-1]]-response*f[path[0]])**2
        dw=weight*kill[path[-1]]
        death[path[-1]]+=dw
        mark_cross+=dw*f[path[0]]*f[path[-1]]
        initial_mark+=dw*f[path[0]]
        final_mark+=dw*f[path[-1]]
    check("exact_survival_mass",mass,p**length)
    for j in range(3):
        check("survivor_current_Haar",final[j]/mass,pi[j])
        check("death_time_mark_independent",
              death[j]/(p**length*(1-p)),gamma[j])
    if length==3:
        mutation("drop_rare_survival_normalizer",err/mass,err,
                 "Finite killed-chain analogue of exp(kappa T).")
        mutation("reverse_response_orientation",err/mass,wrong_orientation/mass,
                 "Initial/final conditional law is not symmetric.")
        death_mass=mass*(1-p)
        mutation("initial_and_collision_marks_independent",
                 mark_cross/death_mass,
                 (initial_mark/death_mass)*(final_mark/death_mass),
                 "Lifetime/mark independence does not imply initial/mark independence.")
        mutation("surviving_initial_is_Haar",
                 initial[0]/mass,pi[0],
                 "Only the surviving current state is exactly Haar.")

Qf=[sum(Qm[i][j]*f[j] for j in range(3)) for i in range(3)]
mart_mean=Q(0)
mart_alive=Q(0)
for i in range(3):
    mart_mean+=pi[i]*kill[i]*(-Qf[i])
    for j in range(3):
        term=pi[i]*Qm[i][j]*(f[j]-Qf[i])
        mart_mean+=term
        mart_alive+=term
check("unconditioned_martingale_mean",mart_mean,Q(0))
mutation("conditioned_survival_keeps_martingale_centered",
         mart_alive/p,Q(0),
         "Future survival changes conditional martingale increments.")

# Exact Laplace response error.
for n in range(2,30):
    kap=Q(n-1)
    for nu in [Q(1,7),Q(1,2),Q(3)]:
        for ell in [Q(1),Q(2),Q(5)]:
            a=1+nu*ell
            direct=1-2*kap/(kap+a)+kap/(kap+2*a)
            factored=2*a*a/((kap+a)*(kap+2*a))
            check("Laplace_response_exact",direct,factored)
            check("Laplace_response_positive",direct>0)
            check("Laplace_response_large_N_bound",
                  direct*n*n<=8*a*a)
            if n==3 and nu==Q(1,2) and ell==2:
                mutation("omit_Laplace_numerator_two",direct,factored/2,
                         "Exact change from fixed T to actual lifetime.")
                mutation("replace_lifetime_response_without_error",direct,Q(0),
                         "The response-time correction is small but not zero.")
# Check typical versus rare profile by an exact geometric analogue.
for n in range(2,20):
    survival=Q(1,2)**n
    check("rare_profile_typical_bound",survival<Q(1,n))
    check("rare_profile_conditioning",survival/survival,Q(1))
mutation("unconditional_smallness_implies_rare_tail_smallness",
         Q(1),Q(1,2)**12,
         "Scalar profile/conditioning countermodel; not admitted dynamics.")

# Local radial generator and actual two-particle coefficient checks.
for n in range(2,10):
    for r2 in [Q(1,16),Q(1,4),Q(1),Q(3,2)]:
        for nu in [Q(0),Q(1,3),Q(2)]:
            d=4
            grad_r4_sq=16*r2**3
            lap_r4=4*(d+2)*r2
            drift_pair=-Q(16,n)
            generator=2*nu*lap_r4+drift_pair
            check("relative_radial_generator",generator,48*nu*r2-Q(16,n))
            check("relative_radial_bracket",4*nu*grad_r4_sq,64*nu*r2**3)
        collision=Q(n,16)*r2*r2
        check("local_absorption_time",r2*r2-Q(16,n)*collision,Q(0))
        if n==2:
            check("physical_N2_absorption",collision,r2*r2/8)
mutation("relative_diffusion_missing_factor_two",Q(48,3),Q(24,3),
         "Dimension four local radial generator.")
mutation("relative_force_missing_second_label",Q(16,2),Q(8,2),
         "Two attractive particle drifts act on the relative separation.")

# One-body martingale and endpoint cross term, no false orthogonality.
for n in range(2,20):
    for nu in [Q(1,5),Q(2)]:
        ell=Q(3)
        kappa=Q(n-1)
        literal=2*nu/Q(n*n)*n*ell/kappa
        check("stopped_modal_bracket",literal,2*nu*ell/(n*kappa))
mutation("noise_covariance_missing_two",Q(2,3),Q(1,3),
         "One-body complex Ito bracket coefficient.")
M=[Q(-1),Q(1)]
I=[z/2 for z in M]
delta=[x+y for x,y in zip(I,M)]
lhs=avg(z*z for z in delta)
check("bounded_endpoint_inequality",lhs<=4*avg(abs(z) for z in I)+avg(z*z for z in M))
mutation("drop_endpoint_drift_martingale_cross",lhs,
         avg(z*z for z in I)+avg(z*z for z in M),
         "No independence or cross-term cancellation is available.")
check("endpoint_bound",max(abs(z) for z in delta)<=2)

RESULT={
    "status":"PASS",
    "arithmetic":"Exact Fraction and Gaussian-rational arithmetic; no random input or tolerance.",
    "checks":sum(COUNTS.values()),
    "categories":dict(sorted(COUNTS.items())),
    "mutation_count":len(MUTATIONS),
    "nonzero_mutations":MUTATIONS,
    "diagnostic_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "limitations":[
        "Finite cyclic examples check canonical clipping and label coefficients, not singular law convergence.",
        "Finite sub-Markov paths check survival normalization and dependence, not the Coulomb diffusion.",
        "The local radial model has no periodic background; zero noise is only a limiting diagnostic.",
        "No critical positive-limsup witness, boundary-profile decay or independent mathematical audit is supplied.",
        "The continuum proof and all singular passages remain in REPORT.md for fresh review."
    ]
}
print(json.dumps(RESULT,indent=2,sort_keys=True))
