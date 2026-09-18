#!/usr/bin/env python3
"""Fresh exact diagnostics for TASK-075; Python standard library only.

Fourier coefficients are Fractions. D0 e_k = k e_k, so the physical
derivative is 2*pi*i*D0. With K=-grad g, each K.grad product is positive
K0*D0 after removing the common factor (2*pi)^2. Laplacians are -D0^2.
This is an algebraic diagnostic, not independent mathematical certification.
No prior checker or non-allowlisted file is read.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

COUNTS = Counter()
MUTATIONS = Counter()


def check(condition, category, detail=""):
    if not condition:
        raise AssertionError((category, detail))
    COUNTS[category] += 1


def clean(a):
    return {k: v for k, v in a.items() if v}


def add(*args):
    out = {}
    for a in args:
        for k, v in a.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(a, c):
    return clean({k: c * v for k, v in a.items()})


def mul(a, b):
    out = {}
    for k, c in a.items():
        for ell, d in b.items():
            key = tuple(x + y for x, y in zip(k, ell))
            out[key] = out.get(key, F(0)) + c * d
    return clean(out)


def d0(a, i):
    return clean({k: v * k[i] for k, v in a.items()})


def lap(a):
    return clean({k: -v * sum(n * n for n in k) for k, v in a.items()})


def embed(a, slots, n):
    """Pull back a Fourier polynomial to distinct indicated slots."""
    out = {}
    for key, value in a.items():
        target = [0] * n
        for i, slot in enumerate(slots):
            target[slot] += key[i]
        target = tuple(target)
        out[target] = out.get(target, F(0)) + value
    return clean(out)


def integrate(a, keep):
    out = {}
    dimension = len(next(iter(a))) if a else max(keep, default=-1) + 1
    removed = set(range(dimension)) - set(keep)
    for key, value in a.items():
        if any(key[j] for j in removed):
            continue
        target = tuple(key[j] for j in keep)
        out[target] = out.get(target, F(0)) + value
    return clean(out)


def U(a, k, n):
    """Literal subset definition; integrated slots must have zero frequency."""
    out = {}
    for mask in range(1 << k):
        active = [j for j in range(k) if mask & (1 << j)]
        inactive = set(range(k)) - set(active)
        c = F((-1) ** (k - len(active)), n ** len(active))
        for labels in permutations(range(n), len(active)):
            for key, value in a.items():
                if any(key[j] for j in inactive):
                    continue
                target = [0] * n
                for slot, label in zip(active, labels):
                    target[label] += key[slot]
                target = tuple(target)
                out[target] = out.get(target, F(0)) + c * value
    return clean(out)


def P(a, n):
    return scale(U(a, 2, n), F(1, 2))


def K0(g):
    return {(k, -k): F(k) * value for k, value in g.items() if k}


def pair_B(phi, g):
    return mul(K0(g), add(d0(phi, 0), scale(d0(phi, 1), -1)))


def response(phi, g, slot):
    return clean({key: -value * key[slot] ** 2 * g.get(key[slot], F(0))
                  for key, value in phi.items()})


def cubic(phi, g):
    raw = mul(embed(K0(g), [0, 2], 3), embed(d0(phi, 0), [0, 1], 3))
    return scale(add(*(embed(raw, perm, 3)
                       for perm in permutations(range(3)))), F(1, 6))


def source(test, g):
    dx = {(k, 0): k * c for k, c in test.items() if k}
    dy = {(0, k): k * c for k, c in test.items() if k}
    return mul(K0(g), add(dx, scale(dy, -1)))


def generator(obs, n, g, nu):
    terms = [scale(lap(obs), nu)]
    for i in range(n):
        for j in range(n):
            if i != j:
                terms.append(scale(mul(embed(K0(g), [i, j], n), d0(obs, i)), F(1, n)))
    return add(*terms)


def symmetric_real(seed):
    out = {}
    for (a, b), c in seed.items():
        for key in set(((a, b), (b, a), (-a, -b), (-b, -a))):
            out[key] = out.get(key, F(0)) + c
    return clean(out)


def exact_pair_diagnostics():
    gs = [{}, {1: F(1, 2), -1: F(1, 2)},
          {1: F(1, 2), -1: F(1, 2), 2: F(1, 7), -2: F(1, 7)}]
    tests = [{0: F(2)}, {1: F(2, 3), -1: F(2, 3), 2: F(1, 5), -2: F(1, 5)}]
    phis = [symmetric_real(seed) for seed in (
        {(0, 0): F(3, 7)}, {(1, 0): F(1, 3)}, {(1, -1): F(1, 5)},
        {(2, -1): F(1, 11), (1, 1): F(1, 13)},
        {(0, 0): F(3, 7), (1, 0): F(1, 3), (1, -1): F(1, 5), (2, -1): F(1, 11)})]
    for n, gi, ti, pi, nu in product((2, 3, 4), range(len(gs)), range(len(tests)), range(len(phis)), (F(0), F(2, 5))):
        g, test, phi = gs[gi], tests[ti], phis[pi]
        J = source(test, g)
        B = pair_B(phi, g)
        R1, R2 = response(phi, g, 0), response(phi, g, 1)
        R = add(R1, R2)
        C = cubic(phi, g)
        phidot = scale(add(J, scale(lap(phi), nu), scale(B, F(1, n)), R), -1)
        obs = P(phi, n)
        lhs = add(P(phidot, n), generator(obs, n, g, nu))
        b = integrate(B, [0])
        scalar = integrate(B, []).get((), F(0))
        lower = scale(U(b, 1, n), F(1, n))
        scalar_term = {(0,) * n: scalar / (2 * n)} if scalar else {}
        upward = U(C, 3, n)
        rhs = add(scale(P(J, n), -1), upward, lower, scalar_term)
        check(lhs == rhs, "literal_full_pair_identity", (n, gi, ti, pi, str(nu)))
        C1, C2, Czero = integrate(C, [0, 1]), integrate(C, [0]), integrate(C, [])
        Aphi = integrate(d0(phi, 0), [0])
        Aa = mul(K0(g), add(embed(Aphi, [0], 2), scale(embed(Aphi, [1], 2), -1)))
        vphi = integrate(R, [0])
        check(C1 == scale(add(Aa, R), F(1, 6)), "one_background_contraction")
        check(C2 == scale(vphi, F(1, 3)), "two_background_contraction")
        check(not Czero, "scalar_cubic_contraction")
        if upward and n == 2:
            MUTATIONS["omitted_N2_cubic_backgrounds"] += 1
        if P(R2, n):
            MUTATIONS["omitted_second_response"] += 1
        if lower:
            MUTATIONS["omitted_lower_contraction"] += 1
        if scalar_term:
            MUTATIONS["omitted_scalar_contraction"] += 1
        for i in range(n):
            direct_gradient = d0(obs, i)
            pair_terms = [scale(embed(d0(phi, 0), [i, j], n), F(1, n*n))
                          for j in range(n) if i != j]
            expected_gradient = add(*pair_terms, scale(embed(Aphi, [i], n), F(-1, n)))
            check(direct_gradient == expected_gradient, "particle_gradient_deletion")
        if gi == 0 and ti == 0 and nu == 0:
            mean = integrate(phi, []).get((), F(0))
            qzero = add(integrate(phi, [0]), {(0,): -mean})
            canonical = add(phi, scale(embed(qzero, [0], 2), -1),
                            scale(embed(qzero, [1], 2), -1), {(0, 0): -mean})
            norm_canonical = integrate(mul(canonical, canonical), []).get((), F(0))
            norm_q = integrate(mul(qzero, qzero), []).get((), F(0))
            direct_second = integrate(mul(obs, obs), []).get((), F(0))
            predicted = F(n-1, 2*n**3) * norm_canonical + norm_q/n**3 + mean**2/(4*n*n)
            check(direct_second == predicted, "iid_endpoint_second_moment")
        # Full generator product rule, independent of the source identity.
        if n <= 3 and pi in (0, 2, 3) and gi in (0, 2) and ti == 1:
            product_lhs = add(generator(mul(obs, obs), n, g, nu),
                              scale(mul(obs, generator(obs, n, g, nu)), -2))
            product_rhs = scale(add(*(mul(d0(obs, i), d0(obs, i)) for i in range(n))), -2 * nu)
            check(product_lhs == product_rhs, "full_generator_bracket")

    for g, test in product(gs, tests):
        J = source(test, g)
        candidate = {}
        # Finite convolution support permits zero frequencies in either slot.
        bound = 7
        for u, v in product(range(-bound, bound + 1), repeat=2):
            m = u + v
            coeff = -test.get(m, F(0)) * m * (u * g.get(u, F(0)) + v * g.get(v, F(0)))
            if coeff:
                candidate[(u, v)] = coeff
        check(J == candidate, "commutator_Fourier_coefficient")
        diagonal = {}
        for (u, v), value in J.items():
            diagonal[(u + v,)] = diagonal.get((u + v,), F(0)) + value
        check(not clean(diagonal), "smooth_commutator_zero_self_diagonal")
    for name in ("omitted_N2_cubic_backgrounds", "omitted_second_response", "omitted_lower_contraction", "omitted_scalar_contraction"):
        check(MUTATIONS[name] > 0, "mutation_witnesses", name)


def positive_heat_algebra_diagnostic():
    # Exact two-point compact-group surrogate for the decomposition and labels.
    # The positive smooth energy coefficient is a. W=c+b*character is positive.
    # This checks finite-sum algebra only, not Gaussian or actual-law analysis.
    a, b, c = F(2, 3), F(1, 5), F(7, 5)
    for n in range(2, 9):
        for xs in product((-1, 1), repeat=n):
            eta = F(sum(xs), n)
            pair = lambda fn: sum((fn(xs[i] * xs[j]) for i in range(n) for j in range(n) if i != j), F(0)) / (n*n)
            Dg = pair(lambda z: (a + b) * z)
            DW = pair(lambda z: c + b * z)
            Dcut = pair(lambda z: a * z)
            check(Dcut == a * eta * eta - a / n, "positive_kernel_exact_self_subtraction")
            check(a * eta * eta + DW == Dg + a / n + F(n-1, n) * c, "positive_tail_joint_identity")
            label_W = DW / F(n-1, n)
            check(DW == F(n-1, n) * label_W, "D2_vs_labelled_pair_normalization")
            if Dg <= 0:
                check(DW <= a / n + F(n-1, n) * c, "D2_positive_tail_inequality")
                check(label_W <= a / (n-1) + c, "labelled_positive_tail_inequality")


def high_frequency_diagnostic():
    # d=5,s=1 gives alpha=2. Pure coefficient |k|^-4 is rational.
    # Both frequencies are necessary to improve k^-3 to k^-4.
    for m in range(1, 7):
        for u in range(2*m + 1, 150):
            v = m - u
            numerator = abs(m * (F(u, abs(u)**4) + F(v, abs(v)**4)))
            energy_geometric_mean = F(1, u*u*v*v)
            check(numerator <= 12*m*m*energy_geometric_mean, "solvable_high_frequency_cancellation")
    m, u, v = 1, 149, -148
    unsym = abs(m * F(u, u**4))
    check(unsym > 12*m*m*F(1, u*u*v*v), "missing_gradient_difference_detected")


def exponent_diagnostic():
    for d in range(4, 13):
        for numerator in range(1, 40):
            s = F(numerator, 20)
            p = s + 2
            theta = 1 - s/d
            a = s/p
            omega = min(s, d-s-2, F(d, 2)-1) / 2
            r = 1 + omega
            e = (s-omega)/p
            check(0 < omega and 1 < r < F(d, 2) and r <= s+1, "chosen_gradient_exponent")
            check(s+1+r < d, "integrable_internal_contraction")
            check(F(1, 2)-e == (2-s+2*omega)/(2*p) > 0, "lower_physical_decay")
            check(theta-F(1, 2) > 0, "source_physical_decay")
            check(theta-a == (2*d-s*p)/(d*p) > 0, "genuine_noise_decay")
            check(-theta+2/p == s*(p-d)/(d*p) < 0, "critical_rescaled_diffusivity")
            check(F(d, 1)-s == 2*((d-s)/2), "heat_Fourier_normalization_exponent")


def verify_inputs(worktree):
    manifest = worktree / "AUDITS/ROUND_015_CUBIC_CONSTRUCTION_INPUT_SHA256SUMS.txt"
    rows = manifest.read_text().splitlines()
    check(len(rows) == 27, "dossier_count")
    for line in rows:
        digest, name = line.split("  ", 1)
        actual = hashlib.sha256((worktree / name).read_bytes()).hexdigest()
        check(actual == digest, "input_sha256", name)


def main():
    worktree = Path(__file__).resolve().parents[2]
    verify_inputs(worktree)
    exact_pair_diagnostics()
    positive_heat_algebra_diagnostic()
    high_frequency_diagnostic()
    exponent_diagnostic()
    result = {
        "task": "TASK-075",
        "status": "PASS",
        "evidence_class": "EXACT_ALGEBRA_SELF_CHECK; not independent analytic certification",
        "arithmetic": "fractions.Fraction; no floats, random seed, or tolerance",
        "assertions": sum(COUNTS.values()),
        "counts": dict(sorted(COUNTS.items())),
        "mutation_witness_counts": dict(sorted(MUTATIONS.items())),
        "normalization": "All spatial second-order diagnostics factor out (2*pi)^2; full source sign, two response coefficients, deleted N powers, and bracket factor 2*nu are checked.",
        "nonclaims": ["No singular law is simulated.", "No prior checker was read.", "The two-point surrogate checks decomposition/label algebra only.", "Exact calculations support but do not certify the analytic proof."]
    }
    target = Path(__file__).with_name("round015_cubic_exact_results.json")
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
