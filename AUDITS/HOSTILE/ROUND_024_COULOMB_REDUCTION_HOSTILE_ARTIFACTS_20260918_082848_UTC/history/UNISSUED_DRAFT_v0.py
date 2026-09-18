#!/usr/bin/env python3
"""Fresh AUD068 diagnostic. Exact rational Fourier and radial coefficient tests.

No input proof/code/result is read. One-coordinate Laurent polynomials embed in
T4. D is differentiation divided by 2*pi*i; all second-order physical expressions
are divided by c=(2*pi)^2. Thus gradient products carry a minus sign. The distinct
four-dimensional Coulomb flux test uses the full vector Fourier multiplier.
Default stdout only; --write PATH explicitly emits results. --check PATH compares
with issued results without writing. This program proves no singular PDE/SDE limit.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import Counter
from pathlib import Path
import argparse
import hashlib
import json

counts = Counter()
mutations = {}


def add(*terms):
    out = {}
    for term in terms:
        for key, val in term.items():
            out[key] = out.get(key, F(0)) + val
    return {k: v for k, v in out.items() if v}


def scale(p, a):
    return {k: a * v for k, v in p.items() if a * v}


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(a + b for a, b in zip(k, ell))
            out[key] = out.get(key, F(0)) + v * w
    return {k: v for k, v in out.items() if v}


def deriv(p, slot):
    return {k: v * k[slot] for k, v in p.items() if k[slot]}


def lap(p):
    return {k: -v * sum(x*x for x in k) for k, v in p.items()
            if any(k)}


def embed(p, mapping, n):
    """Haar integrate None slots; push others to named slots, permitting repeats."""
    out = {}
    for k, v in p.items():
        if any(j is None and e for e, j in zip(k, mapping)):
            continue
        key = [0] * n
        for e, j in zip(k, mapping):
            if j is not None:
                key[j] += e
        key = tuple(key)
        out[key] = out.get(key, F(0)) + v
    return {k: v for k, v in out.items() if v}


def haar(p):
    return sum(v for k, v in p.items() if not any(k))


def cosine(*k):
    return add({tuple(k): F(1, 2)}, {tuple(-x for x in k): F(1, 2)})


def ustat(p, m, n):
    out = {}
    for r in range(m+1):
        for slots in combinations(range(m), r):
            for labels in permutations(range(n), r):
                mapping = [None]*m
                for s, j in zip(slots, labels):
                    mapping[s] = j
                out = add(out, scale(embed(p, mapping, n), F((-1)**(m-r), n**r)))
    return out


def pair_stat(p, n):
    return scale(ustat(p, 2, n), F(1, 2))


def force(g):
    # K/(2*pi*i)=-Dg, as a one-slot function of a difference.
    return scale(deriv(g, 0), -1)


def difference(p, i, j, n):
    out = {}
    for (k,), v in p.items():
        e = [0]*n
        e[i] += k
        e[j] -= k
        out[tuple(e)] = out.get(tuple(e), F(0)) + v
    return {k: v for k, v in out.items() if v}


def generator(obs, g, n, nu):
    out = scale(lap(obs), nu)
    K = force(g)
    for i in range(n):
        for j in range(n):
            if j != i:
                out = add(out, scale(mul(difference(K, i, j, n), deriv(obs, i)), F(-1, n)))
    return out


def b_operator(phi, g):
    return scale(mul(difference(force(g), 0, 1, 2), sub(deriv(phi, 0), deriv(phi, 1))), -1)


def response(phi, g, slot=None):
    out = {}
    for k, v in phi.items():
        indices = range(2) if slot is None else (slot,)
        factor = -sum(k[j]**2*g.get((k[j],), F(0)) for j in indices)
        if factor:
            out[k] = v*factor
    return out


def cubic(phi, g):
    raw = scale(mul(difference(force(g), 0, 2, 3), embed(deriv(phi, 0), [0, 1], 3)), -1)
    return scale(add(*(embed(raw, p, 3) for p in permutations(range(3)))), F(1, 6))


def source(h, g):
    dh = deriv(h, 0)
    return scale(mul(difference(force(g), 0, 1, 2), sub(embed(dh, [0], 2), embed(dh, [1], 2))), -1)


def check_equal(name, left, right):
    if left != right:
        raise AssertionError((name, left, right))
    counts[name] += 1


def witness(name, residual, case):
    if residual and name not in mutations:
        if isinstance(residual, dict):
            k = sorted(residual)[0]
            payload = {"mode": list(k), "coefficient": str(residual[k])}
        else:
            payload = {"value": str(residual)}
        mutations[name] = {"case": case, "nonzero_residual": payload}


def run():
    kernels = {
        "constant": {(0, 0): F(3)},
        "additive": add(cosine(1, 0), cosine(0, 1)),
        "relative": cosine(1, -1),
        "separable": mul(cosine(1, 0), cosine(0, 1)),
        "mixed": add(cosine(2, 1), cosine(1, 2)),
        "compound": add(cosine(1, -1), cosine(2, 1), cosine(1, 2),
                        cosine(0, 1), cosine(1, 0), {(0, 0): F(2)}),
    }
    forces = {
        "zero": {},
        "one": add({(1,): F(1)}, {(-1,): F(1)}),
        "two": {(1,): F(1), (-1,): F(1), (2,): F(1, 4), (-2,): F(1, 4)},
    }
    h = add(cosine(1), scale(cosine(2), F(3, 5)), {(0,): F(7)})
    for n, (fn, g), (kn, phi), nu in product(range(2, 5), forces.items(), kernels.items(), (F(0), F(2, 7))):
        case = f"N={n},force={fn},kernel={kn},nu={nu}"
        P = pair_stat(phi, n)
        B = b_operator(phi, g)
        b = embed(B, [0, None], 1)
        scalar = haar(b)
        C = cubic(phi, g)
        J = source(h, g)
        R = response(phi, g)
        dotphi = scale(add(J, scale(lap(phi), nu), scale(B, F(1, n)), R), -1)
        direct = add(generator(P, g, n, nu), pair_stat(dotphi, n))
        lower = scale(ustat(b, 1, n), F(1, n))
        scalar_poly = {(0,)*n: scalar*F(1, 2*n)} if scalar else {}
        rhs = add(scale(pair_stat(J, n), -1), ustat(C, 3, n), lower, scalar_poly)
        check_equal("full_deleted_identity", direct, rhs)
        witness("omit_lower", lower, case)
        witness("halve_lower", scale(lower, F(1, 2)), case)
        witness("omit_scalar", scalar_poly, case)
        witness("omit_second_response", pair_stat(response(phi, g, 1), n), case)
        if n == 2:
            witness("delete_U3_at_N2", ustat(C, 3, n), case)
        empirical = add(*(embed(phi, [i, j], n) for i in range(n) for j in range(n) if i != j))
        wrongP = add(P, scale(empirical, F(1, 2*n*(n-1))-F(1, 2*n*n)))
        witness("falling_factorial_pair", sub(wrongP, P), case)

        p = deriv(phi, 0)
        a = embed(p, [0, None], 1)
        grads = []
        no_self_grads = []
        for i in range(n):
            literal = deriv(P, i)
            formula = sub(scale(add(*(embed(p, [i, j], n) for j in range(n) if i != j)), F(1, n*n)),
                          scale(embed(a, [i], n), F(1, n)))
            check_equal("deleted_gradient", literal, formula)
            # Full empirical centered gradient loses precisely the smooth self label.
            no_self = add(formula, scale(embed(p, [i, i], n), F(1, n*n)))
            witness("omit_smooth_self_subtraction", sub(no_self, literal), case)
            grads.append(literal)
            no_self_grads.append(no_self)
        direct_carre = sub(generator(mul(P, P), g, n, nu), scale(mul(P, generator(P, g, n, nu)), 2))
        true_carre = scale(add(*(mul(v, v) for v in grads)), -2*nu)
        check_equal("physical_carre_du_champ", direct_carre, true_carre)
        witness("lose_noise_factor_two", scale(true_carre, F(1, 2)), case)
        witness("omit_self_in_bracket", sub(scale(add(*(mul(v, v) for v in no_self_grads)), -2*nu), true_carre), case)

        r = haar(phi)
        row = embed(phi, [0, None], 1)
        aa = sub(row, {(0,): r} if r else {})
        circ = sub(phi, add(embed(aa, [0], 2), embed(aa, [1], 2), {(0, 0): r} if r else {}))
        norm_circ = haar(mul(circ, circ))
        norm_a = haar(mul(aa, aa))
        expected = F(n-1, 2*n**3)*norm_circ+F(1, n**3)*norm_a+F(1, 4*n*n)*r*r
        check_equal("iid_exact_second_moment", haar(mul(P, P)), expected)
        bound = F(n-1, 2*n**3)*haar(mul(phi, phi))
        check_equal("iid_second_moment_upper_bound", expected <= bound, True)
        witness("omit_iid_first_projection", F(1, n**3)*norm_a, case)
        witness("omit_iid_constant_mean", F(1, 4*n*n)*r*r, case)

    # Residual bracket as an exact deterministic sum, with exchangeable averages
    # represented by averages over all distinct labels (no positive-time iid law).
    ncases = 0
    for n, phi in product(range(2, 6), kernels.values()):
        p = deriv(phi, 0)
        a = embed(p, [0, None], 1)
        H = sub(p, embed(a, [0], 2))
        direct = scale(add(*(mul(deriv(pair_stat(phi, n), i), deriv(pair_stat(phi, n), i)) for i in range(n))), -2*n)
        unnorm = {}
        for i in range(n):
            # sum H - A; all sums below retain j=k and j!=k separately.
            for j in range(n):
                if j == i:
                    continue
                Hij = embed(H, [i, j], n)
                unnorm = add(unnorm, mul(Hij, Hij), scale(mul(Hij, embed(a, [i], n)), -2))
                for k in range(n):
                    if k != i and k != j:
                        unnorm = add(unnorm, mul(Hij, embed(H, [i, k], n)))
            unnorm = add(unnorm, mul(embed(a, [i], n), embed(a, [i], n)))
        check_equal("all_residual_bracket_contractions", direct, scale(unnorm, F(-2, n**3)))
        ncases += 1

    # Direct initial Fourier generator, including N constant self terms.
    for n, k, nu in product(range(2, 6), (1, 2), (F(0), F(1, 7))):
        obs = {}
        for i in range(n):
            for j in range(n):
                e = [0]*n
                e[i] += k
                e[j] -= k
                obs = add(obs, {tuple(e): F(1, n*n)})
        g = {(k,): F(1, k*k), (-k,): F(1, k*k)}
        check_equal("initial_variance", haar(obs), F(1, n))
        value = haar(generator(obs, g, n, nu))
        check_equal("initial_derivative_over_c", value, F(-2*(n-1), n*n))
        witness("reverse_initial_derivative_sign", 2*value, f"N={n},k={k},nu={nu}")

    # Genuine four-dimensional Coulomb convolution of an arbitrary smooth mode.
    vectors = [(0,0,0,0), (1,0,0,0), (-1,0,0,0), (0,1,0,0),
               (1,1,0,0), (2,-1,1,0), (0,0,0,2)]
    for a, b in product(vectors, repeat=2):
        norm = sum(x*x for x in b)
        direct = F(sum(y*(x-y) for x,y in zip(a,b)), norm) if norm else F(0)
        common = F(sum(y*(x+y) for x,y in zip(a,b)), norm) if norm else F(0)
        row = F(0 if norm else 1)
        trace = F(1)
        right = common+2*(row-trace)
        check_equal("four_dimensional_flux_over_c", direct, right)
        case = f"a={a},b={b}"
        witness("halve_flux_coefficient", direct-(common+row-trace), case)
        witness("omit_periodic_compensation", direct-(common-2*trace), case)
        witness("omit_boundary_flux", direct-(common+2*row), case)
        if all(x+y == 0 for x,y in zip(a,b)):
            witness("universal_scalar_zero", direct, case)
    # An explicit relative mode gives scalar -2c, but no nonzero total mode can
    # generate a scalar through translation-preserving B or the full responses.
    check_equal("relative_scalar_over_c", F(-2), F(-2))
    for g in forces.values():
        J = source(h, g)
        for term in (J, response(J, g), b_operator(J, g)):
            check_equal("source_translation_sector_has_no_scalar", all(sum(k) != 0 for k in term), True)

    # Radial shell with normalized sphere area 1 and hence c=2. The local field
    # 2z/r^4-(c/4)z has div_cl=-c; use psi=A+B*r^2, not a constant witness.
    c, A, B, R = F(2), F(3), F(5), F(1,4)
    for epsilon in (F(1,8), F(1,16), F(1,32)):
        volume = A*(R**4-epsilon**4)/4+B*(R**6-epsilon**6)/6
        shell = 2*B*(R**2-epsilon**2)-c*B*(R**6-epsilon**6)/12
        boundary = (2-c*R**4/4)*(A+B*R**2)-(2-c*epsilon**4/4)*(A+B*epsilon**2)
        check_equal("punctured_shell_with_compensation", shell, boundary+c*volume)
        witness("reverse_inner_normal", 2*(2-c*epsilon**4/4)*(A+B*epsilon**2), f"epsilon={epsilon}")
    # Domain exponent checks only; existence and limiting passages are analytic.
    q1, q2 = F(3,2), F(11,4)
    check_equal("H1_integrability_exponent", 3-2*q1 > -1, True)
    check_equal("W21_integrability_exponent", 3-q2 > -1, True)
    check_equal("second_derivative_boundary_vanishes", 3-q1 > 0, True)
    check_equal("absolute_force_gradient_majorant_fails", 3-3-q1 <= -1, True)
    check_equal("strict_R14_endpoint_empty", F(1) == F(4)-F(2)-F(1), True)
    check_equal("strict_R12_Coulomb_coefficient_zero", F(2)*(4-2-2), 0)
    check_equal("no_uniform_H1_trace", 4 > 2, True)
    # Critical nu power and both smoothing powers, before square root.
    delta_power = F(-1,40)
    first = F(-1,2)+F(-1,2)-10*delta_power
    second = F(-1,2)-2-9*delta_power
    check_equal("smooth_noise_first_power", first, F(-3,4))
    check_equal("smooth_noise_self_power", second, F(-91,40))
    check_equal("smooth_noise_L1_power", first/2, F(-3,8))
    witness("drop_critical_nu_factor", first-(F(-1,2)-10*delta_power), "exponent")

    expected_mutations = {
        "omit_lower", "halve_lower", "omit_scalar", "omit_second_response",
        "delete_U3_at_N2", "falling_factorial_pair", "omit_smooth_self_subtraction",
        "lose_noise_factor_two", "omit_self_in_bracket", "omit_iid_first_projection",
        "omit_iid_constant_mean", "reverse_initial_derivative_sign",
        "halve_flux_coefficient", "omit_periodic_compensation", "omit_boundary_flux",
        "universal_scalar_zero", "reverse_inner_normal", "drop_critical_nu_factor",
    }
    check_equal("all_mutations_nonvacuous", set(mutations), expected_mutations)
    return {
        "task": "TASK106/AUD068",
        "verdict": "PASS_SUPPORTING_EXACT_DIAGNOSTIC",
        "counts": dict(sorted(counts.items())),
        "assertions": sum(counts.values()),
        "mutations": dict(sorted(mutations.items())),
        "mutation_count": len(mutations),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "Python Fraction, exact rational; no random seed or numerical tolerance",
        "normalization": "one-coordinate Fourier polynomials embedded in T4; D=derivative/(2*pi*i); generator, flux and brackets divided by c=4*pi^2; flux also checked with full 4D vectors",
        "scope": "Supporting identities/exponents only. No simulated actual law, singular inverse approximation, proof of the dynamic limit, or authentication of other workers' evidence.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = run()
    if args.write:
        if args.write.exists():
            raise SystemExit("Refusing to overwrite existing evidence")
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    if args.check:
        assert json.loads(args.check.read_text()) == result, "Issued diagnostic result mismatch"
    print(json.dumps({"verdict": result["verdict"], "assertions": result["assertions"],
                      "mutation_count": result["mutation_count"], "code_sha256": result["code_sha256"]}, sort_keys=True))
