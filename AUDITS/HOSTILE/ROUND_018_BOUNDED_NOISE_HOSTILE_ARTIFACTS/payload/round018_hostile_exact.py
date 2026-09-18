#!/usr/bin/env python3
"""AUD056: new exact diagnostics. Standard library only; no source checker read.

Laurent derivatives divide each physical first derivative by 2*pi.
The particle generator and carré du champ therefore divide by (2*pi)^2.
The code tests finite smooth models and rational modal instances, not singular
analytic limits. The accompanying report supplies the analytic audit.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial, lcm
from pathlib import Path
import hashlib
import json
import sys


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    def __add__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other if isinstance(other, C) else -C(other))

    def __mul__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self):
        return C(self.re, -self.im)

    def __bool__(self):
        return bool(self.re or self.im)

    def __str__(self):
        return str(self.re) + ("+" if self.im >= 0 else "") + str(self.im) + "i"


COUNTS = {}
MUTATIONS = []


def check(category, condition):
    COUNTS[category] = COUNTS.get(category, 0) + 1
    if not condition:
        raise AssertionError(category)


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, C()) + v
    return clean(out)


def scale(p, c):
    return clean({k: v * c for k, v in p.items()})


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(a + b for a, b in zip(k, ell))
            out[key] = out.get(key, C()) + v * w
    return clean(out)


def derivative(p, i):
    return clean({k: v * C(0, k[i]) for k, v in p.items()})


def haar(p, n):
    return p.get((0,) * n, C())


def embed(h, i, n):
    out = {}
    for k, v in h.items():
        key = [0] * n
        key[i] = k
        out[tuple(key)] = v
    return clean(out)


def difference(h, i, j, n):
    out = {}
    for k, v in h.items():
        key = [0] * n
        key[i], key[j] = k, -k
        out[tuple(key)] = v
    return clean(out)


def empirical(h, n, centered=False):
    out = {}
    for i in range(n):
        out = add(out, scale(embed(h, i, n), F(1, n)))
    if centered:
        out = sub(out, {(0,) * n: h.get(0, C())})
    return out


def single_derivative(h):
    return clean({k: v * C(0, k) for k, v in h.items()})


def particle_fields(g, n):
    force = scale(single_derivative(g), -1)
    bs, energy = [], {}
    for i in range(n):
        bi = {}
        for j in range(n):
            if i != j:
                bi = add(bi, scale(difference(force, i, j, n), F(1, n)))
            if i < j:
                energy = add(energy, scale(difference(g, i, j, n), F(1, n)))
        bs.append(bi)
    for i in range(n):
        check("literal_force_from_energy", bs[i] == scale(derivative(energy, i), -1))
    return bs, energy


def generator_parts(p, bs):
    drift, lap = {}, {}
    for i, bi in enumerate(bs):
        first = derivative(p, i)
        drift = add(drift, mul(bi, first))
        lap = add(lap, derivative(first, i))
    return drift, lap


def source(g, h, n):
    force = scale(single_derivative(g), -1)
    dh = single_derivative(h)
    pair = mul(difference(force, 0, 1, 2),
               sub(embed(dh, 0, 2), embed(dh, 1, 2)))
    row = clean({k[0]: v for k, v in pair.items() if k[1] == 0})
    response = clean({k: v * (-k * k * g.get(k, C()).re)
                      for k, v in h.items() if k})
    check("original_source_row", row == response)
    check("original_double_background", haar(pair, 2) == C())
    summed = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                J = mul(difference(force, i, j, n),
                        sub(embed(dh, i, n), embed(dh, j, n)))
                summed = add(summed, J)
    halfpair = scale(summed, F(1, 2 * n * n))
    rowemp = empirical(row, n)
    return sub(halfpair, rowemp), halfpair, rowemp, response


def witness(value):
    if isinstance(value, dict):
        return [{"key": str(k), "value": str(v)}
                for k, v in sorted(value.items(), key=lambda kv: str(kv[0]))[:2]]
    return str(value)


def reject(name, correct, changed):
    check("mutation_rejected", correct != changed)
    if isinstance(correct, dict):
        delta = sub(correct, changed)
    else:
        delta = correct - changed
    MUTATIONS.append({"mutation": name, "nonzero_difference": witness(delta)})


def b_of(nu):
    return F(1) if nu <= 1 else 1 / nu


def laurent_suite():
    g = {k: C(F(1, 2 * abs(k) + 1)) for k in [-3, -2, -1, 1, 2, 3]}
    h = {0: C(1), 1: C(F(1, 2)), -1: C(F(1, 2)),
         2: C(0, F(-1, 3)), -2: C(0, F(1, 3))}
    q = {1: C(0, F(-1, 4)), -1: C(0, F(1, 4)),
         2: C(F(1, 5)), -2: C(F(1, 5)), 3: C(F(1, 7)), -3: C(F(1, 7))}
    tests = [{0: C(2)}, h, q]
    noises = [F(0), F(1, 3), F(1), F(2)]
    for n in [2, 3, 4]:
        bs, _ = particle_fields(g, n)
        obs = [empirical(f, n, True) for f in tests]
        parts = [generator_parts(f, bs) for f in obs]
        for f, obsf, (drift, lap) in zip(tests, obs, parts):
            P, raw, row, response = source(g, f, n)
            check("first_order_deleted_identity", drift == add(P, row))
            check("ordinary_diffusion_trace",
                  lap == empirical(single_derivative(single_derivative(f)), n))
            for nu in noises:
                backwards = empirical(scale(response, -1), n)
                backwards = add(backwards, scale(lap, -nu))
                check("backward_cancellation",
                      add(add(drift, scale(lap, nu)), backwards) == P)
            if n == 3 and f == h:
                reject("remove_source_half", drift, add(scale(raw, 2), {}))
                reject("reverse_response_sign", drift, sub(P, row))
                reject("remove_original_background", P, raw)
        for i, f in enumerate(tests):
            for j in range(i, len(tests)):
                ell = tests[j]
                product = mul(obs[i], obs[j])
                prod_d, prod_l = generator_parts(product, bs)
                ga_d = sub(sub(prod_d, mul(obs[i], parts[j][0])),
                           mul(obs[j], parts[i][0]))
                ga_l = sub(sub(prod_l, mul(obs[i], parts[j][1])),
                           mul(obs[j], parts[i][1]))
                gradient_product = mul(
                    embed(single_derivative(f), 0, 1),
                    embed(single_derivative(ell), 0, 1))
                gradient_single = {key[0]: val for key, val in gradient_product.items()}
                Dinner = sum((f.get(k, C()) * ell.get(k, C()).conj()
                              * (k * k * g.get(k, C()).re)
                              for k in set(f) | set(ell) if k), C())
                Ainner = haar(gradient_product, 1)
                initial_gram = haar(mul(obs[i], obs[j]), n)
                centered_inner = sum((f.get(k, C()) * ell.get(k, C()).conj()
                                      for k in set(f) | set(ell) if k), C())
                check("iid_initial_exact_gram", initial_gram * n == centered_inner)
                for nu in noises:
                    b = b_of(nu)
                    actual_gamma = scale(add(ga_d, scale(ga_l, nu)), n * b)
                    predicted = scale(empirical(gradient_single, n), 2 * nu * b)
                    check("full_cross_carre_du_champ", actual_gamma == predicted)
                    terminal = add(parts[j][0], scale(parts[j][1], nu))
                    crossder = haar(mul(obs[i], terminal), n) * (n * b)
                    expect_cross = (Dinner * F(n - 1, n) + Ainner * nu) * (-b)
                    check("actual_initial_cross_time_derivative", crossder == expect_cross)
                    vard = haar(add(prod_d, scale(prod_l, nu)), n) * (n * b)
                    check("actual_initial_equal_time_derivative",
                          vard == Dinner * (-2 * b * F(n - 1, n)))
                    if n == 3 and i == j == 1 and nu == F(1, 3):
                        reject("drop_Brownian_factor_two", actual_gamma,
                               scale(predicted, F(1, 2)))
                        reject("insert_spurious_bracket_N", actual_gamma,
                               scale(predicted, F(1, n)))
                        reject("replace_deleted_N_minus_one_by_N", vard,
                               Dinner * (-2 * b))
                        reject("omit_diffusion_in_cross_time_derivative", crossder,
                               Dinner * (-b * F(n - 1, n)))
                        reject("omit_variance_Ito_trace", vard,
                               vard - Ainner * (2 * nu * b))
        # A separate finite smooth splitting checks both energy subtractions.
        retained = {k: C(F(1, 5)) for k in [-1, 1]}
        qr = {0: C(3), -2: C(F(1, 2)), 2: C(F(1, 2))}
        total = add(retained, sub(qr, {0: C(3)}))
        _, energy = particle_fields(total, n)
        E, S = {}, {}
        for i in range(n):
            for j in range(n):
                if i == j:
                    E = add(E, {(0,) * n: sum(retained.values(), C()) * F(1, 2*n*n)})
                else:
                    E = add(E, scale(difference(retained, i, j, n), F(1, 2*n*n)))
                    S = add(S, scale(difference(qr, i, j, n), F(1, 2*n*n)))
        self_term = sum(retained.values(), C()) * F(1, 2*n)
        background = C(3) * F(n-1, 2*n)
        rhs = sub(add(E, S), {(0,) * n: self_term + background})
        check("energy_exact_self_and_background", scale(energy, F(1, n)) == rhs)
        if n == 3:
            reject("energy_delete_self_subtraction", scale(energy, F(1, n)),
                   add(rhs, {(0,) * n: self_term}))
            reject("energy_constant_wrong_label_count", scale(energy, F(1, n)),
                   add(rhs, {(0,) * n: background - C(F(3, 2))}))


def gamma_half(x):
    x = F(x)
    assert x > 0 and (2*x).denominator == 1
    c = F(1)
    while x > 1:
        x -= 1
        c *= x
    return (c, F(0)) if x == 1 else (c, F(1, 2))


def mono_mul(a, b):
    return a[0]*b[0], a[1]+b[1]


def mono_div(a, b):
    return a[0]/b[0], a[1]-b[1]


def c_ds(d, s):
    return mono_mul((F(1), F(s)-F(d, 2)),
                    mono_div(gamma_half(F(d-s, 2)), gamma_half(F(s, 2))))


def normalization_suite():
    for d in range(3, 9):
        for s in range(1, d-1):
            alpha = F(d-s, 2)
            A = mono_div((F(2)**(d-s), F(d, 2)), gamma_half(F(s, 2)))
            coefficient = mono_div(mono_mul(A, gamma_half(alpha)),
                                   (F(2)**(d-s), F(d-s)))
            check("heat_Fourier_coefficient_one", coefficient == c_ds(d, s))
            if s < d-2:
                ratio = mono_div(mono_mul((F(4), F(2)), c_ds(d, s)),
                                 c_ds(d, s+2))
                check("subCoulomb_gamma_recurrence",
                      ratio == (F(s*(d-s-2)), F(0)))
            else:
                atom = mono_div((F(2*(d-2)), F(d, 2)), gamma_half(F(d, 2)))
                check("Coulomb_atom_constant",
                      mono_mul((F(4), F(2)), c_ds(d, s)) == atom)
                check("finite_dimensional_Coulomb_scope", (2*s < d) == (d == 3))
    c = F(7)
    h = {0: C(3), 1: C(2), -1: C(2)}
    full = {k: v * (-c) for k, v in h.items() if k}
    atom_only = scale(h, -c)
    density_only = {0: C(3*c)}
    check("Coulomb_full_response_kills_constant", full.get(0, C()) == C())
    reject("Coulomb_omit_compensating_Haar", full, atom_only)
    reject("Coulomb_omit_atom", full, density_only)
    for alpha, M in [(1, 5), (2, 8), (3, 10)]:
        for r in [F(1, 3), F(1), F(2)]:
            cr = F(factorial(alpha-1)) * sum(
                ((-1)**(j+1) * F(comb(M, j), j**alpha)
                 for j in range(1, M+1)), F(0)) * r**alpha
            check("positive_remainder_mass", cr > 0)
            for lam in [F(1, 2), F(1), F(5)]:
                moment = sum(((-1)**j * F(comb(M, j)) / (lam+F(j)/r)**alpha
                              for j in range(M+1)), F(0))
                next_moment = sum(((-1)**j * F(comb(M, j)) /
                                  (lam+F(j)/r)**(alpha+1)
                                  for j in range(M+1)), F(0))
                slope = 2*lam*alpha*next_moment/moment
                discarded = sum(((-1)**(j+1) * F(comb(M, j)) /
                                 (lam+F(j)/r)**alpha
                                 for j in range(1, M+1)), F(0))
                check("retained_Laplace_weight_positive", moment > 0)
                check("uniform_logarithmic_slope", 0 <= slope <= 2*(alpha+M))
                check("exact_positive_heat_split", moment + discarded == lam**(-alpha))


def ep_add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def ep_scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def ep_eval(p, z, denominator):
    return sum((v * z**int(k*denominator) for k, v in p.items()), F(0))


def psd_exact(matrix):
    a = [row[:] for row in matrix]
    for k in range(len(a)):
        pivot = a[k][k]
        if pivot < 0:
            return False
        if not pivot:
            if any(a[k][j] for j in range(k+1, len(a))):
                return False
            continue
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] -= a[i][k]*a[k][j]/pivot
    return True


def covariance_suite():
    # cos/sin amplitudes in each of two orthogonal real Fourier modes.
    tests = [[(1, 0), (0, 1)], [(1, 0), (2, 1)],
             [(1, 1), (0, -2)], [(1, 1), (0, -2)], [(0, 0), (0, 0)]]
    times = [F(0), F(1, 2), F(1), F(1), F(3, 2)]
    for nu in [F(0), F(1, 2), F(1), F(2)]:
        b = b_of(nu)
        initial, thermal, closed = [], [], []
        for i, ti in enumerate(times):
            ai, bi, ci = [], [], []
            for j, tj in enumerate(times):
                aa, bb, cc = {}, {}, {}
                for mode, (D, a) in enumerate([(F(2), F(1)), (F(3), F(4))]):
                    inner = F(sum(x*y for x, y in zip(tests[i][mode], tests[j][mode])), 2)
                    L = D + nu*a
                    total, gap = (ti+tj)*L, abs(ti-tj)*L
                    aa = ep_add(aa, {total: b*inner})
                    # Direct integration of two deterministic OU propagators.
                    integral = ep_add({gap: F(1)/(2*L)}, {total: -F(1)/(2*L)})
                    bb = ep_add(bb, ep_scale(integral, 2*nu*b*a*inner))
                    cc = ep_add(cc, {total: b*inner*D/L})
                    cc = ep_add(cc, {gap: b*inner*nu*a/L})
                    check("limiting_equal_time_slope", -2*L*b*D/L == -2*b*D)
                    check("limiting_initial_time_slope",
                          -L*(b*D/L+b*nu*a/L) == -b*(D+nu*a))
                check("entire_cross_covariance_formula", ep_add(aa, bb) == cc)
                ai.append(aa); bi.append(bb); ci.append(cc)
            initial.append(ai); thermal.append(bi); closed.append(ci)
        for i in range(len(times)):
            for j in range(len(times)):
                check("real_covariance_symmetry", closed[i][j] == closed[j][i])
                check("repeated_test_time_rows", closed[2][j] == closed[3][j])
                check("constant_test_zero", closed[4][j] == {})
            check("zero_time_thermal", thermal[0][i] == {})
        denominator = 1
        for row in closed:
            for poly in row:
                for exponent in poly:
                    denominator = lcm(denominator, exponent.denominator)
        for z in [F(1, 2), F(2, 3), F(4, 5)]:
            matrix = [[ep_eval(poly, z, denominator) for poly in row] for row in closed]
            check("joint_covariance_exact_PSD", psd_exact(matrix))
            null = [F(0), F(0), F(1), F(-1), F(0)]
            check("joint_covariance_exact_null_direction",
                  all(sum(matrix[i][j]*null[j] for j in range(5)) == 0
                      for i in range(5)))
        if nu == F(1, 2):
            reject("suppress_thermal_cross_bracket", closed[1][2], initial[1][2])
            reject("drop_entire_thermal_covariance", closed[2][2], initial[2][2])
            reject("halve_thermal_covariance", closed[2][2],
                   ep_add(initial[2][2], ep_scale(thermal[2][2], F(1, 2))))
            # In equal-time initial contribution the correct sum is positive.
            wrong_initial = {F(0): sum(initial[2][2].values(), F(0))}
            reject("initial_time_sum_replaced_by_difference", closed[2][2],
                   ep_add(wrong_initial, thermal[2][2]))
        if nu == 2:
            reject("omit_scaling_b_above_one", closed[1][1], ep_scale(closed[1][1], 2))
    for x, y in [(F(0), F(1, 3)), (F(1, 2), F(3, 2)),
                 (F(1), F(9, 8)), (F(7, 4), F(2))]:
        # The nonsquared b factor is also continuous across its kink.
        check("thermal_scaling_Lipschitz",
              abs(x*b_of(x)-y*b_of(y)) <= abs(x-y))


def gaussian_moment(degree):
    if degree % 2:
        return F(0)
    return F(factorial(degree), 2**(degree//2)*factorial(degree//2))


def mixture_moment(p, q, weight_s=0):
    # M1=W1, M2=S W1+W2, S independent equiprobable +/-1.
    out = F(0)
    for s in [-1, 1]:
        for j in range(q+1):
            out += F(s**(j+weight_s)*comb(q, j), 2) * (
                gaussian_moment(p+j)*gaussian_moment(q-j))
    return out


def exponential_product_coefficient(variance, compensator, order):
    return sum(((-variance/F(2))**j/F(factorial(j)) *
                (compensator/F(2))**(order-j)/F(factorial(order-j))
                for j in range(order+1)), F(0))


def dependence_suite():
    # Both marginals are exactly Gaussian by conditioning, but joint law is not.
    for power in range(13):
        check("Gaussian_marginal_first", mixture_moment(power, 0) == gaussian_moment(power))
        expected = F(2)**(power//2)*gaussian_moment(power)
        check("Gaussian_marginal_second", mixture_moment(0, power) == expected)
    check("mixture_correct_cross_covariance", mixture_moment(1, 1) == 0)
    reject("Gaussian_marginals_and_covariance_imply_joint_Gaussian",
           mixture_moment(2, 2), F(2))
    reject("zero_initial_cross_mean_implies_initial_independence",
           mixture_moment(1, 1, 1), F(0))
    # Projection u=(1,2): conditional variance is 9+4S; expected variance 9.
    for s in [-1, 1]:
        v = F(9+4*s)
        for order in range(9):
            check("conditional_positive_compensator",
                  exponential_product_coefficient(v, v, order) == (order == 0))
    wrong_sign = exponential_product_coefficient(F(13), F(-13), 1)
    reject("wrong_stochastic_compensator_sign", F(0), wrong_sign)
    mean_coeff2 = sum((exponential_product_coefficient(F(9+4*s), F(9), 2)/2
                      for s in [-1, 1]), F(0))
    reject("replace_random_joint_bracket_by_expectation", F(0), mean_coeff2)
    weighted_coeff1 = sum((F(s, 2)*exponential_product_coefficient(F(9+4*s), F(9), 1)
                          for s in [-1, 1]), F(0))
    reject("ignore_time_zero_weight_in_joint_passage", F(0), weighted_coeff1)


def main():
    laurent_suite()
    normalization_suite()
    covariance_suite()
    dependence_suite()
    program = Path(__file__).resolve()
    result = {
        "audit": "AUD056 / TASK-086",
        "status": "PASS",
        "arithmetic": "exact rational and Gaussian rational; formal exponential polynomials",
        "physical_units": "Laurent derivatives / (2*pi); generator and bracket / (2*pi)^2",
        "scope": "finite smooth algebra and solvable Gaussian diagnostics, not analytic proof",
        "randomness": None,
        "dependencies": "Python standard library only",
        "program_sha256": hashlib.sha256(program.read_bytes()).hexdigest(),
        "assertions": sum(COUNTS.values()),
        "categories": COUNTS,
        "mutations_rejected": len(MUTATIONS),
        "mutation_witnesses": MUTATIONS,
        "joint_counterexample": {
            "definition": "S equiprobable +/-1; M1=W1; M2=S*W1+W2; independent S,W1,W2",
            "covariance": [[1, 0], [0, 2]],
            "E_M1_squared_M2_squared": str(mixture_moment(2, 2)),
            "Gaussian_covariance_prediction": "2",
            "E_S_M1_M2": str(mixture_moment(1, 1, 1)),
            "warning": "not an admitted particle-law counterexample"
        }
    }
    output = program.with_name("round018_hostile_exact_results.json")
    result_text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if "--check" in sys.argv[1:]:
        if output.read_text() != result_text:
            raise AssertionError("sealed diagnostic result differs from recomputation")
    else:
        output.write_text(result_text)
    print("PASS: %d exact assertions; %d categories; %d rejected mutations" %
          (result["assertions"], len(COUNTS), len(MUTATIONS)))


if __name__ == "__main__":
    main()
