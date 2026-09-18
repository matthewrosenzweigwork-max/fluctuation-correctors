#!/usr/bin/env python3
"""AUD070 fresh exact diagnostics. Standard library; stdout only; no input reads.

Finite groups and martingale trees test coefficients, not singular SDE limits.
All assertions use integers/Fraction, including symbolic logarithmic integrals.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from collections import Counter
import json


class C:
    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)
    @staticmethod
    def cast(z):
        return z if isinstance(z, C) else C(z)
    def __add__(self, z):
        z = C.cast(z)
        return C(self.re + z.re, self.im + z.im)
    __radd__ = __add__
    def __neg__(self):
        return C(-self.re, -self.im)
    def __sub__(self, z):
        return self + (-C.cast(z))
    def __rsub__(self, z):
        return C.cast(z) - self
    def __mul__(self, z):
        z = C.cast(z)
        return C(self.re*z.re-self.im*z.im, self.re*z.im+self.im*z.re)
    __rmul__ = __mul__
    def __truediv__(self, z):
        z = C.cast(z)
        return self*z.conj()*F(1, z.abs2())
    def conj(self):
        return C(self.re, -self.im)
    def abs2(self):
        return self.re*self.re+self.im*self.im
    def __eq__(self, z):
        z = C.cast(z)
        return self.re == z.re and self.im == z.im
    def __repr__(self):
        return "(%s,%s)" % (self.re, self.im)


counts = Counter()
mutations = {}
details = {}


def check(category, condition):
    if not condition:
        raise AssertionError(category)
    counts[category] += 1


def witness(name, correct, mutated, datum):
    if correct != mutated and name not in mutations:
        mutations[name] = {"correct": repr(correct), "mutated": repr(mutated), "datum": datum}


I = C(0, 1)
roots = (C(1), I, C(-1), -I)
def e(k, x):
    return roots[(k*x) % 4]


# Exact Laplace moments of the retained heat weight, with c absorbed into z.
for r in (F(1, 8), F(1, 2), F(1), F(2)):
    mass = sum((F((-1)**(j+1)*comb(6, j), j) for j in range(1, 7)), F())*r
    check("heat_discarded_mass", mass == F(49, 20)*r)
    for z in (F(1, 7), F(1), F(2), F(17), F(100)):
        moment = sum((F((-1)**j*comb(6, j))/(z+F(j)/r) for j in range(7)), F())
        u_moment = sum((F((-1)**j*comb(6, j))/(z+F(j)/r)**2 for j in range(7)), F())
        denominator = F(1)
        for j in range(7):
            denominator *= z*r+j
        check("heat_beta_product", moment == 720*r/denominator and moment > 0)
        slope = 2*z*u_moment/moment
        check("heat_log_slope", 2 <= slope <= 14)
        witness("slope_cap_two_is_false", slope <= 14, slope <= 2, {"r": str(r), "z": str(z), "slope": str(slope)})


# Exact deleted energy splitting in a finite Haar group; all positions allowed.
ar = {1:F(1), 2:F(2), 3:F(1)}
gr = [sum((ar[k]*e(k, x) for k in ar), C()).re for x in range(4)]
qr = list(map(F, (7, 2, 3, 2)))
cr = sum(qr)/4
gg = [gr[x]+qr[x]-cr for x in range(4)]
for n in range(2, 5):
    for xs in product(range(4), repeat=n):
        hn = sum((gg[(xs[i]-xs[j]) % 4] for i in range(n) for j in range(i+1, n)), F())/n
        fr = sum((ar[k]*(sum((e(k, x) for x in xs), C())/n).abs2() for k in ar), F())/2
        vr = sum((qr[(xs[i]-xs[j]) % 4] for i in range(n) for j in range(n) if i != j), F())/(2*n*n)
        rhs = fr+vr-F(gr[0], 2*n)-F(n-1, 2*n)*cr
        check("deleted_energy_identity", hn/n == rhs)
        witness("energy_self_N_squared", hn/n, fr+vr-F(gr[0], 2*n*n)-F(n-1, 2*n)*cr, {"N": n, "x": xs})
        witness("energy_background_undeleted", hn/n, fr+vr-F(gr[0], 2*n)-cr/2, {"N": n, "x": xs})


# The retained Fourier identity with 2*pi factored out of the derivative.
af = {-1:F(2), 1:F(2)}
vf = {-2:C(1,1), -1:C(2,-1), 1:C(2,1), 2:C(1,-1)}
def force(x):
    return sum((-I*k*a*e(k, x) for k, a in af.items()), C())
def velocity(x):
    return sum((v*e(k, x) for k, v in vf.items()), C())
def retained_source(x, y):
    return force(x-y)*(velocity(x)-velocity(y))
def row(x):
    return sum((I*k*a*vf.get(k,C())*e(k,x) for k,a in af.items()), C())
for n in range(2, 5):
    for xs in product(range(4), repeat=n):
        direct = sum((retained_source(xs[i],xs[j]) for i in range(n) for j in range(n) if i != j), C())/(2*n*n)
        direct -= sum((row(x) for x in xs), C())/n
        rh = {k:sum((e(-k,x) for x in xs), C())/n for k in range(-3,4) if k}
        raw = C()
        for k in rh:
            for l in rh:
                raw += (k*af.get(k,F())-l*af.get(l,F()))*vf.get(l-k,C())*rh[k]*rh[l].conj()
        fourier = -I*raw/2
        check("retained_commutator_exact", direct == fourier)
        witness("commutator_missing_half", direct, -I*raw, {"N":n,"x":xs})


# Canonical initial clipping, including every overlapping pair covariance.
g = list(map(F, (9,-3,-3,-3)))
for level in (F(0), F(1), F(2)):
    clipped = [min(a, level) for a in g]
    mean = sum(clipped)/4
    canonical = [a-mean for a in clipped]
    norm2 = sum(a*a for a in canonical)/4
    check("clip_zero_rows", sum(canonical) == 0 and mean < 0)
    overlap = sum((canonical[(x-y)%4]*canonical[(x-z)%4] for x,y,z in product(range(4),repeat=3)), F())/64
    uncentered = sum((clipped[(x-y)%4]*clipped[(x-z)%4] for x,y,z in product(range(4),repeat=3)), F())/64
    check("clip_overlap_orthogonality", overlap == 0 and uncentered == mean*mean)
    witness("uncentered_clip_overlap", overlap, uncentered, {"level":str(level)})
    for n in range(2, 6):
        hmean, hsecond, badcount = F(), F(), 0
        for xs in product(range(4),repeat=n):
            raw = sum((g[(xs[i]-xs[j])%4] for i in range(n) for j in range(i+1,n)),F())/n
            hc = sum((canonical[(xs[i]-xs[j])%4] for i in range(n) for j in range(i+1,n)),F())/n
            bad = any(g[(xs[i]-xs[j])%4] > level for i in range(n) for j in range(i+1,n))
            hmean += hc
            hsecond += hc*hc
            badcount += int(bad)
            if not bad:
                check("clip_good_event_identity", raw == hc+F(n-1,2)*mean)
                check("clip_good_event_positive_part", max(raw,F()) <= abs(hc))
                witness("clip_shift_missing_N_minus_one", raw, hc+mean/2, {"N":n,"level":str(level),"x":xs})
        hmean /= 4**n
        hsecond /= 4**n
        target = F(n-1,2*n)*norm2
        check("clip_energy_exact_variance", hmean == 0 and hsecond == target)
        witness("clip_variance_missing_half", hsecond, F(n-1,n)*norm2, {"N":n,"level":str(level)})
        prob = F(badcount,4**n)
        union = F(n*(n-1),2)*F(1,4)
        check("bad_pair_union", prob <= union)
        if prob > F(1,4):
            witness("bad_event_missing_pair_count", True, False, {"N":n,"actual_probability":str(prob),"wrong_bound":"1/4"})


# Conditional isometry on an exact martingale tree; the event is initial.
initial_square = initial_bracket = terminal_square = terminal_bracket = F()
endpoint_cross = endpoint_square = noise_square = source_square = F()
for initial, r1, r2 in product((0,1),(-1,1),(-1,1)):
    a1, a2 = initial+1, (2*initial-1)*(2+r1)
    mart = a1*r1+a2*r2
    bracket = a1*a1+a2*a2
    probability = F(1,8)
    if initial == 1:
        initial_square += probability*mart*mart
        initial_bracket += probability*bracket
    if r2 == 1:
        terminal_square += probability*mart*mart
        terminal_bracket += probability*bracket
    endpoint = mart+initial
    endpoint_cross += probability*endpoint*mart
    endpoint_square += probability*endpoint*endpoint
    noise_square += probability*mart*mart
    source_square += probability*initial*initial
check("initial_event_isometry", initial_square == initial_bracket)
check("terminal_event_countermodel", terminal_square != terminal_bracket)
witness("isometry_terminal_event", terminal_square, terminal_bracket, {"event":"r2=1"})
check("endpoint_shared_noise_cross", source_square == endpoint_square+noise_square-2*endpoint_cross and endpoint_cross != 0)
witness("endpoint_noise_independence", source_square, endpoint_square+noise_square, {"cross":str(endpoint_cross)})


# Exact radial tail model, using formal log coefficients plus rational parts.
radial = []
for level in (0,1,2,7,31,100):
    a = F(level+2)
    mean_by_density = -2/a+2/(a*a)+F(level)/(a*a)
    second_rational = 8/a-4/(a*a)-4+F(level*level)/(a*a)
    variance = (F(2),second_rational-mean_by_density**2)
    asserted = (F(2),-3+4/a-1/(a*a))
    check("radial_clipped_mean", mean_by_density == -1/a)
    check("radial_clipped_variance", variance == asserted)
    witness("radial_variance_uncentered", variance, (F(2),second_rational), {"level":level})
    radial.append({"L":level,"mean":str(mean_by_density),"variance_log_coefficient":"2","variance_rational_part":str(variance[1])})
for n in (2,3,5,16,100,10000):
    a=F(n+2)
    # Integrate (y-2)^2 2/y^3 from 2 to a, divide by N, add cap tail.
    direct = (F(2,n), (8/a-4/(a*a)-3)/n+F(n)/(a*a))
    formula = (F(2,n), (4/a-2)/n)
    check("radial_capped_second_moment", direct == formula)
details["radial_exact_forms"] = radial


# Exchangeable finite-group analogues, preserving current and initial labels.
rf = (F(1),F(-1),F(3),F(-1))
def jk(x,y):
    return rf[(x-y)%4]*(e(1,x)+e(1,y))
def Jk(x,y):
    return jk(x,y)-e(1,x)-e(1,y)
for x in range(4):
    check("centered_j_zero_row", sum((jk(x,y) for y in range(4)),C()) == 0)
    check("original_J_row", sum((Jk(x,y) for y in range(4)),C())/4 == -e(1,x))
    check("smooth_diagnostic_J_diagonal", Jk(x,x) == 0)
for n in range(2,7):
    xs=(0,0,1,3,2,1)[:n]
    ys=(1,2,0,1,3,0)[:n]
    z=sum((e(1,x) for x in xs),C())/n
    z0=sum((e(1,x) for x in ys),C())/n
    u=sum((jk(xs[i],xs[j]) for i in range(n) for j in range(n) if i!=j),C())/(2*n*n)
    p=sum((Jk(xs[i],xs[j]) for i in range(n) for j in range(n) if i!=j),C())/(2*n*n)+z
    check("deleted_modal_source_identity", p == u+z/n)
    witness("modal_deleted_correction_sign", p, u-z/n, {"N":n})
    for label,positions,empirical in (("current",xs,z),("initial",ys,z0)):
        overlap=sum((jk(xs[i],xs[j])*e(1,positions[i]).conj() for i in range(n) for j in range(n) if i!=j),C())/(n*(n-1))
        value=F(n-1,n)*overlap
        if n>2:
            disjoint=sum((jk(xs[i],xs[j])*e(1,positions[m]).conj() for i in range(n) for j in range(n) if i!=j for m in range(n) if m!=i and m!=j),C())/(n*(n-1)*(n-2))
            value += F((n-1)*(n-2),2*n)*disjoint
            wrong=F(n-1,n)*overlap+F((n-1)*(n-2),n)*disjoint
            witness("modal_"+label+"_disjoint_missing_half", n*u*empirical.conj(), wrong, {"N":n,"A_or_B3":repr(disjoint)})
        check("modal_"+label+"_overlap_count", n*u*empirical.conj() == value)
    for k,l in product((-2,-1,1,2),repeat=2):
        nu=F(3,7)
        direct=2*nu*sum(((I*k*e(k,x))*(I*l*e(l,x)).conj() for x in xs),C())/(n*n)
        computed=F(2,n)*nu*k*l*sum((e(k-l,x) for x in xs),C())/n
        check("modal_cross_bracket", direct == computed)
        if k!=l:
            witness("off_mode_bracket_zero", direct, C(), {"N":n,"k":k,"l":l})
        if k==l:
            check("modal_self_bracket", direct == 2*nu*k*k/n)


# Pure response/noise exact algebra and response-slot counting.
for n in range(2,30):
    c,nu,ell=F(5),F(2,7),F(11)
    a=c+nu*ell
    at=a-c/n
    check("response_lower_bound", at >= c/2)
    check("energy_laplacian_pair_count", F(2,n)*F(n*(n-1),2)*c == c*(n-1))
    witness("energy_laplacian_missing_two", c*(n-1), F(1,n)*F(n*(n-1),2)*c, {"N":n})
    witness("current_current_one_slot", -2*at, -at, {"N":n})
    witness("current_initial_two_slots", -at, -2*at, {"N":n})
for q,a,noise,fc,gc in product((F(1,4),F(3,4)),(F(1,8),F(1,2)),(F(0),F(1,7)),(F(-1,9),F(2,5)),(F(-1,3),F(1,4))):
    v=q*q+noise+2*fc
    r=q+gc
    endpoint=v+a*a-2*a*r
    formula=(q-a)**2+noise+2*(fc-a*gc)
    check("signed_correlation_solution_algebra", endpoint == formula)
    witness("correlation_missing_initial_response", endpoint, (q-a)**2+noise+2*(fc-gc), {"q":str(q),"A":str(a),"G_integral":str(gc)})


# Positive-limsup and UI stress tests: exact abstract scalar examples only.
for A in (F(0),F(1),F(3,2),F(4)):
    for j in range(81):
        x=F(j,7)
        check("tail_to_L1_L2_scalar", x*x <= 2*A*x+2*max(x-A,F())**2)
        if x>2*A:
            check("overshoot_tail_scalar", x*x <= 4*max(x-A,F())**2)
        witness("omit_overshoot_remainder", x*x <= 2*A*x+2*max(x-A,F())**2, x*x <= 2*A*x, {"x":str(x),"A":str(A)})
for n in (2,3,10,100,10000):
    prob=F(1,n*n)
    check("rare_spike_not_UI", prob*n == F(1,n) and prob*n*n == 1)
    check("bounded_nonzero_not_decay", max(F(1)-F(1),F())**2 == 0 and F(1)>0)


required = {
    "slope_cap_two_is_false", "energy_self_N_squared", "energy_background_undeleted",
    "commutator_missing_half", "uncentered_clip_overlap", "clip_shift_missing_N_minus_one",
    "clip_variance_missing_half", "bad_event_missing_pair_count", "isometry_terminal_event",
    "endpoint_noise_independence", "radial_variance_uncentered", "modal_deleted_correction_sign",
    "modal_current_disjoint_missing_half", "modal_initial_disjoint_missing_half",
    "off_mode_bracket_zero", "energy_laplacian_missing_two", "current_current_one_slot",
    "current_initial_two_slots", "correlation_missing_initial_response", "omit_overshoot_remainder"
}
check("all_mutations_nonvacuous", required <= set(mutations))
print(json.dumps({
    "audit":"AUD070", "status":"PASS", "arithmetic":"exact Fraction and Gaussian rational; formal logarithmic coefficients",
    "randomness":"none", "dependencies":"Python standard library only", "assertions":sum(counts.values()),
    "categories":dict(sorted(counts.items())), "mutation_count":len(mutations), "mutations":mutations,
    "details":details, "limitation":"Diagnostics do not prove continuum singular stochastic passages or THM046 decay."
}, indent=2, sort_keys=True))
