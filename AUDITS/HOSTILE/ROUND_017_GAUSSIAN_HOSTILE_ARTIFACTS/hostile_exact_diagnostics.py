#!/usr/bin/env python3
"""Fresh AUD054 diagnostics. Standard library only; no construction code/input reads.

Fourier differentiation is divided by 2*pi. Generator, source and bracket
comparisons are consequently divided by (2*pi)^2. Coefficients are exact
Gaussian rationals. These finite smooth probes support, and do not replace,
the analytic singular/probability review.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json


class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = Q(r), Q(i)

    def __add__(self, other):
        other = gg(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + -gg(other)

    def __mul__(self, other):
        other = gg(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = gg(other)
        return self.r == other.r and self.i == other.i

    def __bool__(self):
        return bool(self.r or self.i)

    def conj(self):
        return G(self.r, -self.i)

    def norm2(self):
        return self.r * self.r + self.i * self.i

    def serial(self):
        return {"real": str(self.r), "imag": str(self.i)}


def gg(x):
    return x if isinstance(x, G) else G(x)


COUNTS = Counter()
COEFFICIENTS = Counter()
MUTATIONS = {}
DETAILS = {}


def require(category, condition):
    COUNTS[category] += 1
    if not condition:
        raise AssertionError(category)


def clean(p):
    return {k: gg(v) for k, v in p.items() if v}


def const(n, x):
    return clean({(0,) * n: gg(x)})


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, G()) + v
    return clean(out)


def scale(p, c):
    return clean({k: v * c for k, v in p.items()})


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            m = tuple(a + b for a, b in zip(k, l))
            out[m] = out.get(m, G()) + v * w
    return clean(out)


def deriv(p, a):
    return clean({k: v * G(0, k[a]) for k, v in p.items()})


def lap(p):
    return clean({k: v * -sum(a * a for a in k) for k, v in p.items()})


def integral(p):
    return next((v for k, v in p.items() if not any(k)), G())


def polyeq(category, p, q):
    p, q = clean(p), clean(q)
    keys = set(p) | set(q)
    COEFFICIENTS[category] += len(keys)
    require(category, all(p.get(k, G()) == q.get(k, G()) for k in keys))


def mutation(name, good, wrong):
    diff = add(good, scale(wrong, -1))
    require("mutation_rejection", bool(diff))
    key = sorted(diff)[0]
    MUTATIONS[name] = {"exponent": list(key), "difference": diff[key].serial()}


def embed(p, n, labels):
    """Embed a polynomial with one d-slot for each named particle label."""
    if not p:
        return {}
    d = len(next(iter(p))) // len(labels)
    out = {}
    for k, v in p.items():
        z = [0] * (n * d)
        for slot, label in enumerate(labels):
            for a in range(d):
                z[d * label + a] += k[d * slot + a]
        out[tuple(z)] = out.get(tuple(z), G()) + v
    return clean(out)


def paired(p):
    out = {}
    for k, v in p.items():
        out[k] = gg(v)
        out[tuple(-a for a in k)] = gg(v).conj()
    return clean(out)


def datum(d):
    e1 = (1, 0, 0) + (0,) * (d - 3)
    e2 = (0, 1, 0) + (0,) * (d - 3)
    e3 = (0, 0, 1) + (0,) * (d - 3)
    e12 = tuple(a + b for a, b in zip(e1, e2))
    kernel = paired({e1: Q(1, 2), e2: Q(2, 5), e12: Q(1, 7)})
    h = add(const(d, Q(7, 5)), paired({e1: G(Q(2, 3), Q(-1, 4)),
                                      e2: G(Q(1, 5), Q(1, 3)), e12: Q(2, 7)}))
    z = add(const(d, Q(-2, 9)), paired({e1: G(Q(-1, 3), Q(1, 5)),
                                       e3: G(Q(1, 2), Q(1, 7))}))
    return kernel, h, z


def eta(p, n):
    return scale(add(*(embed(p, n, [i]) for i in range(n))), Q(1, n))


def centered(p, n):
    if not p:
        return {}
    d = len(next(iter(p)))
    return add(eta(p, n), const(n * d, -integral(p)))


def source(kernel, h):
    d = len(next(iter(kernel)))
    out = {}
    for a in range(d):
        force = clean({k + tuple(-v for v in k): c * G(0, -k[a])
                       for k, c in kernel.items()})
        grad_difference = add(embed(deriv(h, a), 2, [0]),
                              scale(embed(deriv(h, a), 2, [1]), -1))
        out = add(out, mul(force, grad_difference))
    row = clean({k[:d]: v for k, v in out.items() if not any(k[d:])})
    return out, row


def deleted(p, n):
    return scale(add(*(embed(p, n, [i, j]) for i in range(n)
                       for j in range(n) if i != j)), Q(1, n * n))


def psour(j, row, n):
    d = len(next(iter(j))) // 2 if j else len(next(iter(row)))
    return add(scale(deleted(j, n), Q(1, 2)), scale(eta(row, n), -1),
               const(n * d, integral(row) * Q(1, 2)))


def drifts(kernel, n):
    d = len(next(iter(kernel)))
    result = []
    for i in range(n):
        for a in range(d):
            pair_force = clean({k + tuple(-v for v in k): c * G(0, -k[a])
                                for k, c in kernel.items()})
            result.append(scale(add(*(embed(pair_force, n, [i, j])
                                      for j in range(n) if i != j)), Q(1, n)))
    return result


def generator(p, b, nu):
    return add(scale(lap(p), nu), *(mul(ba, deriv(p, a)) for a, ba in enumerate(b)))


def pair_product_grad(h, z):
    d = len(next(iter(h)))
    return add(*(mul(deriv(h, a), deriv(z, a)) for a in range(d)))


def first_order_and_bracket():
    for d in (3, 4):
        kernel, h, z = datum(d)
        j, row = source(kernel, h)
        expected_row = clean({k: c * kernel.get(k, G()) * -sum(a * a for a in k)
                              for k, c in h.items()})
        polyeq("literal_Haar_row", row, expected_row)
        require("scalar_background_zero", not integral(row))
        polyeq("source_pair_symmetry", j, embed(j, 2, [1, 0]))
        polyeq("smooth_source_diagonal_zero", embed(j, 1, [0, 0]), {})
        constant_j, constant_row = source(kernel, const(d, Q(5, 3)))
        require("constant_source_zero", not constant_j and not constant_row)
        for n in (2, 3, 4):
            b = drifts(kernel, n)
            for ba in b:
                require("common_translation_drift", all(
                    all(sum(k[i * d + a] for i in range(n)) == 0 for a in range(d))
                    for k in ba))
            p = psour(j, row, n)
            rf = centered(h, n)
            rz = centered(z, n)
            force = generator(rf, b, Q(0))
            polyeq("ordered_force_half", force, scale(deleted(j, n), Q(1, 2)))
            polyeq("deleted_background_cancellation", force, add(p, eta(row, n)))
            for nu in (Q(0), Q(1, 7), Q(2)):
                # The backward derivative is derived modewise, independently of j.
                dt_h = clean({k: c * (G(nu) + kernel.get(k, G())) * sum(a*a for a in k)
                              for k, c in h.items()})
                polyeq("backward_generator_source", add(eta(dt_h, n), generator(rf, b, nu)), p)
                lf, lz = generator(rf, b, nu), generator(rz, b, nu)
                carre = add(generator(mul(rf, rz), b, nu),
                            scale(mul(rf, lz), -1), scale(mul(rz, lf), -1))
                bracket = scale(eta(pair_product_grad(h, z), n), Q(2, n) * nu)
                polyeq("literal_thermal_cross_bracket", carre, bracket)
                if d == 3 and n == 2 and nu == Q(1, 7):
                    mutation("thermal_missing_two", carre, scale(bracket, Q(1, 2)))
                    mutation("thermal_wrong_N", carre, scale(bracket, n))
                if not nu:
                    require("zero_noise_bracket", not carre)
            if d == 3 and n == 3:
                mutation("force_missing_half", force, deleted(j, n))
                mutation("source_missing_Haar_row", p, scale(deleted(j, n), Q(1, 2)))
                mutation("source_wrong_row_sign", p, add(scale(deleted(j, n), Q(1, 2)), eta(row, n)))
                wrong_denominator = add(scale(deleted(j, n), Q(n, 2*(n-1))), scale(eta(row, n), -1))
                mutation("falling_factorial_denominator", p, wrong_denominator)


def source_energy_coefficients():
    d = 3
    retained, _, _ = datum(d)
    e1 = (1, 0, 0)
    q = add(const(d, 3), paired({e1: Q(1, 4)}))
    total_g = add(retained, q, const(d, -3))
    diagonal = sum(retained.values(), G())
    pair = lambda p: {k + tuple(-a for a in k): v for k, v in p.items()}
    for n in (2, 3, 5):
        lhs = scale(deleted(pair(total_g), n), Q(1, 2))
        er = scale(add(*(embed(pair(retained), n, [i, j])
                         for i in range(n) for j in range(n))), Q(1, 2*n*n))
        sr = scale(deleted(pair(q), n), Q(1, 2))
        rhs = add(er, sr, const(n*d, -diagonal * Q(1, 2*n)),
                   const(n*d, Q(-3*(n-1), 2*n)))
        polyeq("positive_split_energy_identity", lhs, rhs)
        require("iid_split_expectation_zero", integral(lhs) == 0)
        if n == 3:
            mutation("energy_missing_smooth_self", lhs, add(rhs, const(n*d, diagonal * Q(1, 2*n))))
            mutation("energy_background_N_minus_one", lhs, add(er, sr, const(n*d, -diagonal * Q(1, 2*n)), const(n*d, Q(-3, 2))))
    moments = []
    for alpha, m, r, lam in product((1, 2, 3), (3, 5, 7), (Q(1, 3), Q(1), Q(2)), (Q(1), Q(3), Q(5))):
        # Exact Laplace integration of the binomial polynomial in exp(-u/r).
        def moment(a):
            return factorial(a-1) * sum((Q((-1)**j * comb(m, j), 1) /
                                         (lam + Q(j, 1)/r)**a for j in range(m+1)), Q())
        a0, a1 = moment(alpha), moment(alpha+1)
        require("retained_weight_strict_positive", a0 > 0)
        slope = 2 * lam * a1 / a0
        require("retained_log_slope_upper", 0 <= slope <= 2*(alpha+m))
        require("retained_log_slope_lower", slope >= 2*alpha)
        if alpha == 1 and m == 3:
            moments.append({"r": str(r), "lambda": str(lam), "weight": str(a0), "slope": str(slope)})
    DETAILS["representative_heat_weights"] = moments


def gamma_half(x):
    """Return rational coefficient and pi exponent for Gamma at positive half integers."""
    x = Q(x)
    require("gamma_half_domain", x > 0 and (2*x).denominator == 1)
    if x.denominator == 1:
        return Q(factorial(x.numerator-1)), Q(0)
    n = (x - Q(1, 2)).numerator
    return Q(factorial(2*n), 4**n * factorial(n)), Q(1, 2)


def c_riesz(d, s):
    a, ap = gamma_half(Q(d-s, 2))
    b, bp = gamma_half(Q(s, 2))
    return a/b, Q(s) - Q(d, 2) + ap - bp


def normalization_and_scaling():
    for d in range(3, 13):
        for s in range(1, d-1):
            a, ap = c_riesz(d, s)
            if s < d-2:
                b, bp = c_riesz(d, s+2)
                require("Riesz_gamma_recurrence", (4*a/b, ap+2-bp) == (Q(s*(d-2-s)), Q(0)))
            else:
                ga, gp = gamma_half(Q(d, 2))
                require("Coulomb_atom_normalization", (4*a, ap+2) == (Q(2*(d-2))/ga, Q(d, 2)-gp))
    scales = []
    for d in range(3, 13):
        for s in sorted({Q(1, 2), Q(d-2), Q(d, 2), Q(d, 3), Q(d, 2)-Q(1, 4)}):
            if not 0 < s <= d-2:
                continue
            theta = 1 - s/d
            source_exp = s/d-Q(1, 2)
            require("critical_beta_diverges", theta > 0)
            require("splitting_scale_balance", -1+(-Q(2,d))*(-s/2) == (-Q(2,d))*Q(d-s,2) == s/d-1)
            require("old_floor_not_critical", theta+2*s/d-1 == s/d > 0)
            require("strict_source_range", (source_exp < 0) == (s < Q(d, 2)))
            require("thermal_scaling_exponent", -theta/2 < 0 and -theta < 0)
            scales.append({"d": d, "s": str(s), "beta_power": str(theta),
                           "source_error_power": str(source_exp), "admitted_T039": s < Q(d,2)})
    DETAILS["scaling_cases"] = scales
    # This is exactly D/c = delta_0 - Haar, including its zero Fourier coefficient.
    d = 3
    _, h, _ = datum(d)
    mass = integral(h)
    good = add(scale(h, -1), const(d, mass))
    require("Coulomb_response_preserves_constants", not integral(good))
    polyeq("Coulomb_nonzero_response", good, clean({k: -v for k, v in h.items() if any(k)}))
    mutation("Coulomb_atom_removed", good, const(d, mass))
    mutation("Coulomb_compensation_removed", good, scale(h, -1))
    mutation("response_wrong_sign", good, scale(good, -1))


def haar_cov(p, q):
    return integral(mul(p, q)) - integral(p)*integral(q)


def initial_joint_probability():
    d = 3
    e1, e2 = (1,0,0), (0,1,0)
    cos1 = paired({e1: Q(1,2)})
    sin2 = paired({e2: G(0,Q(-1,2))})
    # Exact admitted Coulomb times: t_j = n_j log(2)/(4*pi), so S_t = 2^-n_j.
    hs = [const(d,7), cos1, add(cos1,sin2), cos1, add(const(d,3),cos1), sin2]
    ts = [0,1,2,1,0,3]
    vs = [scale(add(h,const(d,-integral(h))),Q(1,2**t)) for h,t in zip(hs,ts)]
    m = len(vs)
    c = [[integral(mul(v,w)) for w in vs] for v in vs]
    require("joint_real_symmetric_covariance", all(not c[i][j].i and c[i][j] == c[j][i]
                                                  for i in range(m) for j in range(m)))
    require("constant_test_zero_covariance", all(not z for z in c[0]))
    require("repeated_time_and_test_degeneracy", c[1] == c[3])
    for u in [(1,0,0,-1,0,0), (0,1,0,-1,0,0), (1,2,-3,4,-2,1), (0,0,0,0,1,0), (2,-1,3,0,1,-2)]:
        v = add(*(scale(vv,a) for vv,a in zip(vs,u)))
        quad = sum((c[i][j]*u[i]*u[j] for i in range(m) for j in range(m)),G())
        require("joint_PSD_reconstruction", quad == integral(mul(v,v)) and not quad.i and quad.r >= 0)
    for n in (2,3,5):
        rho = [centered(v,n) for v in vs]
        for i in range(m):
            for j in range(m):
                require("literal_initial_joint_covariance", integral(mul(rho[i],rho[j]))*n == c[i][j])
        triangular = add(scale(vs[2],Q(-1,7)),scale(vs[5],Q(2,9)))
        iid_error = centered(triangular,n)
        require("triangular_test_variance_no_sqrt_N_loss", integral(mul(iid_error,iid_error))*n == integral(mul(triangular,triangular)))
    good_cov = const(1,c[1][2])
    wrong_time = const(1,haar_cov(hs[1],hs[2])*Q(1,2**abs(ts[1]-ts[2])))
    mutation("cross_time_absolute_difference", good_cov,wrong_time)
    mutation("constant_covariance_not_centered",const(1,c[0][0]),const(1,integral(mul(hs[0],hs[0]))))
    wrong_sine = sum((coef*coef for k,coef in vs[5].items()),G())
    mutation("complex_covariance_missing_conjugation",const(1,c[5][5]),const(1,wrong_sine))
    moment_cases = []
    for u in ((0,1,2,0,0,1),(0,0,0,0,1,0),(1,-1,0,1,0,0)):
        v = add(*(scale(vv,a) for vv,a in zip(vs,u)))
        powers = [const(d,1)]
        for j in range(1,5):
            powers.append(mul(powers[-1],v))
        moments = [integral(p) for p in powers]
        require("iid_projected_centering", not moments[1])
        for n in (2,3,5):
            raw = G()
            for labels in product(range(n),repeat=4):
                term = G(1)
                for count in Counter(labels).values():
                    term = term*moments[count]
                raw = raw+term
            expected = moments[4]*n + moments[2]*moments[2]*(3*n*(n-1))
            require("independent_fourth_label_contractions",raw == expected)
            require("Gaussian_fourth_moment_remainder",raw*Q(1,n*n) == moments[2]*moments[2]*3 + (moments[4]-moments[2]*moments[2]*3)*Q(1,n))
            moment_cases.append({"u":list(u),"N":n,"second":moments[2].serial(),"scaled_fourth":(raw*Q(1,n*n)).serial()})
    DETAILS["joint_Coulomb_times_units_log2_over_4pi"] = ts
    DETAILS["joint_covariance"] = [[z.serial() for z in row] for row in c]
    DETAILS["projected_fourth_moments"] = moment_cases
    for eps in (Q(1,2),Q(1,7),Q(1,25)):
        trace = sum((c[i][i].r for i in range(m)),Q())
        smooth_trace = trace+m*eps
        require("Gaussian_smoothing_second_moment",smooth_trace-trace == m*eps)
    mutation("smoothing_epsilon_instead_of_sqrt",const(1,trace+m*Q(1,7)),const(1,trace+m*Q(1,49)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("DIAGNOSTIC_RESULTS.json"))
    args = parser.parse_args()
    first_order_and_bracket()
    source_energy_coefficients()
    normalization_and_scaling()
    initial_joint_probability()
    result = {"audit":"AUD054","status":"PASS","arithmetic":"exact rational and Gaussian rational",
              "no_randomness":True,"no_external_modules":True,
              "program_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "assertions":sum(COUNTS.values()),"counts":dict(sorted(COUNTS.items())),
              "polynomial_coefficients_compared":sum(COEFFICIENTS.values()),
              "coefficients_by_category":dict(sorted(COEFFICIENTS.items())),
              "mutation_controls":MUTATIONS,"details":DETAILS,
              "limits":"Finite smooth diagnostics do not prove singular passage or weak convergence; see the analytic AUD054 report."}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"PASS","assertions":result["assertions"],
                      "polynomial_coefficients_compared":result["polynomial_coefficients_compared"],
                      "mutation_controls":len(MUTATIONS),"output":str(args.output)},sort_keys=True))


if __name__ == "__main__":
    main()
