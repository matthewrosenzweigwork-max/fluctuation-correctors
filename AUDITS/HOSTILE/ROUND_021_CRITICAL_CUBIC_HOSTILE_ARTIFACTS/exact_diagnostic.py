#!/usr/bin/env python3
"""AUD062: fresh exact Fourier, initial, time-jet and exponent diagnostics.

No source/checker/result imports. Standard library; exact Gaussian rationals.
Run without arguments to print JSON; --write records RESULTS.json before seal.
Finite smooth probes test universal algebra, not singular analytic estimates.
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial, comb
from pathlib import Path
import hashlib
import json
import sys


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        other = cc(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + -cc(other)

    def __mul__(self, other):
        other = cc(other)
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.re or self.im)

    def as_json(self):
        return {"real": str(self.re), "imaginary": str(self.im)}


def cc(value):
    return value if isinstance(value, C) else C(F(value))


I = C(F(0), F(1))


def clean(poly):
    return {k: cc(v) for k, v in poly.items() if v}


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, C()) + v
    return clean(out)


def scale(p, a):
    return clean({k: cc(a) * v for k, v in p.items()})


def mul(p, q):
    out = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(a + b for a, b in zip(k, ell))
            out[key] = out.get(key, C()) + v * w
    return clean(out)


def deriv(p, j):
    return clean({k: v * I * k[j] for k, v in p.items()})


def lap(p, dim):
    return add(*(deriv(deriv(p, j), j) for j in range(dim)))


def place(p, slots, dim):
    """Insert variables into slots; None integrates that slot against Haar."""
    out = {}
    for k, v in p.items():
        if any(slot is None and freq for slot, freq in zip(slots, k)):
            continue
        key = [0] * dim
        for slot, freq in zip(slots, k):
            if slot is not None:
                key[slot] += freq
        key = tuple(key)
        out[key] = out.get(key, C()) + v
    return clean(out)


def mean(p, dim):
    return p.get((0,) * dim, C())


def trig(dim, freq, sine=False):
    freq = tuple(freq)
    neg = tuple(-a for a in freq)
    return clean({freq: -I * F(1, 2) if sine else C(F(1, 2)),
                  neg: I * F(1, 2) if sine else C(F(1, 2))})


def deleted(p, degree, n):
    """Literal subset/deleted-label definition, independent of contractions."""
    out = {}
    for count in range(degree + 1):
        for chosen in combinations(range(degree), count):
            for labels in permutations(range(n), count):
                slots = [None] * degree
                for a, label in zip(chosen, labels):
                    slots[a] = label
                out = add(out, scale(place(p, slots, n),
                                     F((-1) ** (degree-count), n ** count)))
    return out


def pair(p, n):
    return scale(deleted(p, 2, n), F(1, 2))


def force_poly(dim, i, j):
    freq = [0] * dim
    freq[i], freq[j] = 1, -1
    return add(trig(dim, freq, True), scale(trig(dim, [2*x for x in freq], True), F(2, 3)))


def generator(p, n, nu):
    terms = [scale(lap(p, n), nu)]
    for i in range(n):
        for j in range(n):
            if i != j:
                terms.append(scale(mul(force_poly(n, i, j), deriv(p, i)), F(1, n)))
    return add(*terms)


def pair_ops(phi):
    force = force_poly(2, 0, 1)
    bp = mul(force, add(deriv(phi, 0), scale(deriv(phi, 1), -1)))
    # An extra integration variable constructs each response independently.
    rx = place(mul(force_poly(3, 2, 0), place(deriv(phi, 0), [2, 1], 3)), [0, 1, None], 2)
    ry = place(mul(force_poly(3, 2, 1), place(deriv(phi, 1), [0, 2], 3)), [0, 1, None], 2)
    raw = mul(force_poly(3, 0, 2), place(deriv(phi, 0), [0, 1], 3))
    cubic = scale(add(*(place(raw, slots, 3) for slots in permutations(range(3)))), F(1, 6))
    return bp, rx, ry, cubic


def lower(bp, n):
    row = place(bp, [0, None], 1)
    scalar = mean(bp, 2)
    centered = add(*(scale(place(row, [i], n), F(1, n)) for i in range(n)),
                   {(0,)*n: -scalar})
    return add(scale(centered, F(1, n)), {(0,)*n: scalar * F(1, 2*n)})


counts = Counter()
witnesses = {}


def check(category, condition):
    assert condition, category
    counts[category] += 1


def equal(category, a, b):
    check(category, a == b)


def mutation(name, good, bad, context):
    residual = add(bad, scale(good, -1))
    if residual and name not in witnesses:
        key = min(residual)
        witnesses[name] = {"context": context, "frequency": key,
                           "nonzero_residual_coefficient": residual[key].as_json()}


def run():
    kernels = {
        "constant": {(0, 0): C(F(3, 2))},
        "relative": trig(2, (1, -1)),
        "rows": add(trig(2, (1, 0)), trig(2, (0, 1))),
        "mixed": add(trig(2, (2, -1)), trig(2, (-1, 2)),
                     scale(trig(2, (1, 1), True), F(3, 5))),
    }
    kernels["all_projections"] = add(*(scale(v, F(i+1, 3)) for i, v in enumerate(kernels.values())))
    jets = []
    for n, nu, (name, phi) in product(range(2, 6), (F(0), F(2, 5)), kernels.items()):
        context = {"N": n, "nu": str(nu), "kernel": name}
        bp, rx, ry, cubic = pair_ops(phi)
        obs = pair(phi, n)
        gp = add(scale(lap(phi, 2), nu), scale(bp, F(1, n)), rx, ry)
        cstat = deleted(cubic, 3, n)
        low = lower(bp, n)
        direct = generator(obs, n, nu)
        rhs = add(pair(gp, n), cstat, low)
        equal("literal_full_generator", direct, rhs)
        grad = [deriv(obs, i) for i in range(n)]
        gx = deriv(phi, 0)
        row_g = place(gx, [0, None], 1)
        for i in range(n):
            formula = add(*(scale(place(gx, [i, j], n), F(1, n*n))
                            for j in range(n) if j != i),
                          scale(place(row_g, [i], n), -F(1, n)))
            equal("deleted_particle_gradient", grad[i], formula)
        bracket = scale(add(*(mul(v, v) for v in grad)), 2*nu)
        gamma = add(generator(mul(obs, obs), n, nu), scale(mul(obs, direct), -2))
        equal("independent_carre_du_champ", gamma, bracket)
        raw_bracket = {}
        for i in range(n):
            a = place(row_g, [i], n)
            raw_bracket = add(raw_bracket, scale(mul(a, a), F(1, n*n)))
            for j in range(n):
                if j == i:
                    continue
                gij = place(gx, [i, j], n)
                raw_bracket = add(raw_bracket, scale(mul(gij, a), -F(2, n**3)))
                for k in range(n):
                    if k != i:
                        raw_bracket = add(raw_bracket, scale(mul(gij, place(gx, [i, k], n)), F(1, n**4)))
        equal("entire_empirical_background_bracket", bracket, scale(raw_bracket, 2*nu))
        m = mean(phi, 2)
        row = add(place(phi, [0, None], 1), {(0,): -m})
        fc = add(phi, scale(place(row, [0], 2), -1), scale(place(row, [1], 2), -1), {(0, 0): -m})
        equal("zero_hoeffding_rows", place(fc, [0, None], 1), {})
        predicted = (mean(mul(fc, fc), 2) * F(n-1, 2*n**3)
                     + mean(mul(row, row), 1) * F(1, n**3)
                     + m*m*F(1, 4*n*n))
        equal("exact_iid_endpoint_second_moment", mean(mul(obs, obs), n), predicted)
        equal("exact_iid_endpoint_bias", mean(obs, n), -m*F(1, 2*n))
        norm = mean(mul(phi, phi), 2)
        check("iid_uniform_bound", predicted.im == 0 and predicted.re <= norm.re*F(n-1, 2*n**3))
        mutation("omit_scalar_lower", direct, add(rhs, {(0,)*n: -mean(bp, 2)*F(1, 2*n)}), context)
        mutation("omit_response_slot", direct, add(rhs, scale(pair(ry, n), -1)), context)
        mutation("halve_internal_coefficient", direct, add(rhs, scale(pair(bp, n), -F(1, 2*n))), context)
        mutation("double_symmetrized_cubic", direct, add(rhs, cstat), context)
        raw_cubic = add(*(scale(place(cubic, p, n), F(1, n**3)) for p in permutations(range(n), 3)))
        mutation("discard_all_cubic_backgrounds", direct, add(pair(gp, n), raw_cubic, low), context)
        if n == 2:
            mutation("drop_N2_cubic", direct, add(pair(gp, n), low), context)
        wrong_p = add(obs, scale(add(*(place(phi, (i,j), n) for i in range(n) for j in range(n) if i != j)), F(1, 2*n*n*(n-1))))
        mutation("falling_factorial_pair_denominator", direct, generator(wrong_p, n, nu), context)
        wrong_grad = [add(g, scale(place(row_g, [i], n), F(1, n))) for i,g in enumerate(grad)]
        mutation("remove_background_from_bracket", bracket, scale(add(*(mul(g, g) for g in wrong_grad)), 2*nu), context)
        if n <= 3 and name in ("relative", "all_projections") and nu:
            # Phi_t=(H-t)F; J_t=F-(H-t)G_pair F. Compare expectation
            # jets from the actual finite-particle generator through H^4.
            pol = [obs, pair(gp, n), cstat, low]
            expectations = [[] for _ in pol]
            for order in range(4):
                for idx, p in enumerate(pol):
                    expectations[idx].append(mean(p, n))
                    if order < 3:
                        pol[idx] = generator(p, n, nu)
            for power in range(1, 5):
                source = expectations[0][power-1]*F(1, factorial(power))
                initial = expectations[0][0] if power == 1 else C()
                low_coeff = C()
                cubic_coeff = C()
                if power >= 2:
                    source -= expectations[1][power-2]*F(1, factorial(power))
                    low_coeff = expectations[3][power-2]*F(1, factorial(power))
                    cubic_coeff = expectations[2][power-2]*F(1, factorial(power))
                equal("terminal_zero_integrated_identity_jet", cubic_coeff, source-initial-low_coeff)
                if initial:
                    witnesses.setdefault("reverse_initial_sign", {"context": context, "horizon_power": power,
                        "nonzero_residual_coefficient": (2*initial).as_json()})
                if low_coeff:
                    witnesses.setdefault("reverse_lower_sign", {"context": context, "horizon_power": power,
                        "nonzero_residual_coefficient": (2*low_coeff).as_json()})
                jets.append({**context, "power": power, "cubic_coefficient": cubic_coeff.as_json()})

    admitted = set()
    for d in range(3, 31):
        for denominator in range(1, 18):
            for numerator in range(1, (d-2)*denominator):
                s = F(numerator, denominator)
                if s*(s+2) < 2*d:
                    admitted.add((d, s))
    for d, s in sorted(admitted):
        p, a, theta = s+2, s/(s+2), 1-s/d
        lo, hi = max(F(1), s/2), min(F(d,2), d-s-1, s+1)
        q = (lo+hi)/2
        kappa = (2*q-s)/(2*p)
        for category, truth in (
            ("strict_midpoint_interval", lo < hi),
            ("all_real_range_witness", 3*s < 2*d-2),
            ("initial_L2_range", 2*s < d),
            ("gradient_lower_admissibility", 1 < q < F(d,2) and q < s+1),
            ("absolute_lower_slice_integrability", s+1+q < d),
            ("strict_four_decay_exponents", max(s/d-F(1,2), -F(1,2), (a-theta)/2, -kappa) < 0),
            ("critical_chi_exact_power", 2/p-theta == s*(s+2-d)/(d*p) < 0),
            ("noise_condition_exact_factor", theta-a == (2*d-s*(s+2))/(d*p)),
            ("lower_decay_power", (s+1-q)/p-F(1,2) == -kappa),
            ("squared_gradient_power", 2*(s+1-p/2)/p == a),
            ("noise_gradient_admissibility", 1 < p/2 < F(d,2) and p/2 <= s+1),
        ):
            check(category, truth)

    # Exact positive heat-splitting Laplace moments: independent scale-uniform
    # logarithmic-slope test. The variable lambda absorbs 4*pi^2*|k|^2.
    for alpha, m, r, lam in product(range(1,5), range(3,8), (F(1,3), F(1), F(2)), (F(1,8), F(1,2), F(2), F(8))):
        i0 = sum(F((-1)**j * comb(m,j) * factorial(alpha-1), 1)/(lam+F(j)/r)**alpha for j in range(m+1))
        i1 = sum(F((-1)**j * comb(m,j) * factorial(alpha), 1)/(lam+F(j)/r)**(alpha+1) for j in range(m+1))
        check("positive_retained_laplace_moment", i0 > 0 and i1 > 0)
        check("scale_uniform_logarithmic_slope", 0 < 2*lam*i1/i0 <= 2*(alpha+m))

    exponent_mutations = {
        "include_noise_equality": {"d":12, "s":"4", "mutant_bracket_power":"0", "rejected":"not strictly negative"},
        "reciprocal_temperature_sign": {"d":3, "s":"1/2", "mutant_chi_power":str(F(2,1)/F(5,2)+F(5,6)), "rejected":"positive instead of negative"},
        "omit_square_gradient_factor": {"d":5, "s":"23/10", "mutant_power":str(F(23,86)), "correct_power":str(F(23,43)), "rejected":"scaling identity fails"},
        "drop_q_lower_one": {"d":3, "s":"1/10", "mutant_q":str((F(1,20)+F(11,10))/2), "rejected":"q is not greater than one"},
    }
    check("exponent_mutation_equality", F(4,6)+F(4,12)-1 == 0)
    check("exponent_mutation_temperature", F(2,1)/F(5,2)+F(5,6) > 0)
    check("exponent_mutation_square", F(23,86) != F(23,43))
    check("exponent_mutation_q", (F(1,20)+F(11,10))/2 < 1)
    required = {"omit_scalar_lower", "omit_response_slot", "halve_internal_coefficient", "double_symmetrized_cubic",
                "discard_all_cubic_backgrounds", "drop_N2_cubic", "falling_factorial_pair_denominator",
                "remove_background_from_bracket", "reverse_initial_sign", "reverse_lower_sign"}
    check("nonvacuous_coefficient_mutation_witnesses", set(witnesses) == required)
    check("strict_boundary_is_excluded", (12,F(4)) not in admitted)
    check("genuine_new_ranges_tested", all(item in admitted for item in ((3,F(1,2)),(5,F(23,10)),(12,F(15,4)))))
    return {"status":"PASS", "audit":"AUD062", "arithmetic":"exact Gaussian rational and rational; no random seed or tolerance",
            "total_assertions":sum(counts.values()), "categories":dict(sorted(counts.items())),
            "unique_admitted_parameter_pairs":len(admitted), "coefficient_mutations":witnesses,
            "exponent_mutations":exponent_mutations, "integrated_identity_jets":jets,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "limitations":"Finite smooth Fourier probes, finite exact parameter grid and Laplace moments support the analytic audit; they do not prove singular-domain or uniform limiting estimates."}


if __name__ == "__main__":
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if sys.argv[1:] == ["--write"]:
        Path(__file__).with_name("RESULTS.json").write_text(rendered)
    elif sys.argv[1:]:
        raise SystemExit("Use no arguments for read-only reproduction or --write before sealing.")
    print(rendered)
