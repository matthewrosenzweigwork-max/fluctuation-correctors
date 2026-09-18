#!/usr/bin/env python3
"""AUD079 fresh supporting diagnostics. Python standard library only.

Exact tests use integers/Fraction; floating tests are explicitly labelled.
No simulation claims to prove the actual singular-law moment theorem.
The default emits JSON to stdout and does not write any file.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, exp, factorial, isfinite, log, pi, sqrt
import argparse
import json
from pathlib import Path

CHECKS = Counter()
MUTATIONS = []
SAMPLES = []


def check(category, actual, expected, description=""):
    assert actual == expected, (category, description, actual, expected)
    CHECKS[category] += 1


def close(category, actual, expected, description="", atol=2e-11):
    assert isfinite(actual) and isfinite(expected)
    assert abs(actual - expected) <= atol * (1 + abs(actual) + abs(expected)), (
        category, description, actual, expected)
    CHECKS[category] += 1


def mutation(name, actual, altered, kind="exact"):
    residual = actual - altered
    assert (residual != 0 if kind == "exact" else abs(residual) > 1e-9), (
        "mutation not detected", name, actual, altered)
    MUTATIONS.append({"name": name, "kind": kind, "correct": str(actual),
                      "altered": str(altered), "nonzero_residual": str(residual)})


def finite_group(moduli):
    group = list(product(*(range(q) for q in moduli)))
    index = {x: i for i, x in enumerate(group)}
    def subtract(i, j):
        return index[tuple((a - b) % q for a, b, q in zip(group[i], group[j], moduli))]
    return group, subtract


def group_moments(values, subtract):
    q = len(values)
    cv = [sum((values[subtract(z, y)] * values[y] for y in range(q)), F(0)) / q
          for z in range(q)]
    mu2 = sum((x*x for x in values), F(0)) / q
    mu4 = sum((x**4 for x in values), F(0)) / q
    tau = sum((values[z]**2*cv[z] for z in range(q)), F(0)) / q
    chi = sum((x*x for x in cv), F(0)) / q
    return mu2, mu4, tau, chi


def four_terms(n, moments):
    mu2, mu4, tau, chi = moments
    return [comb(n, 2)*mu4, 18*comb(n, 3)*mu2**2,
            36*comb(n, 3)*tau, 18*comb(n, 4)*mu2**2,
            72*comb(n, 4)*chi]


def exhaustive_fourth(values, subtract, n):
    q = len(values)
    edge = [[values[subtract(i, j)] for j in range(q)] for i in range(q)]
    pairs = list(combinations(range(n), 2))
    total = F(0)
    for labels in product(range(q), repeat=n):
        h = sum((edge[labels[i]][labels[j]] for i, j in pairs), F(0))
        total += h**4
    return total / q**n


def graph_and_clipping_tests():
    saved = None
    for moduli in [(2,), (3,), (4,), (5,), (2, 2), (2, 3)]:
        group, sub = finite_group(moduli)
        q = len(group)
        raw_options = [[q-1 if i == 0 else -1 for i in range(q)],
                       [sum((j+1)*min(x, m-x) for j, (x, m) in
                            enumerate(zip(g, moduli))) for g in group]]
        for kid, raw in enumerate(raw_options):
            mean = F(sum(raw), q)
            values = [F(x)-mean for x in raw]
            check("exact_kernel_centering", sum(values), 0)
            for i in range(q):
                check("exact_kernel_evenness", values[sub(0, i)], values[i])
            moments = group_moments(values, sub)
            for n in range(2, 6):
                actual = exhaustive_fourth(values, sub, n)
                expected = sum(four_terms(n, moments), F(0))
                check("exact_exhaustive_Haar_fourth", actual, expected,
                      str((moduli, kid, n)))
                if moduli == (3,) and kid == 0 and n == 5:
                    saved = (actual, moments)
            mu2, _, tau, chi = moments
            check("exact_convolution_bounds", abs(tau) <= mu2**2 and
                  0 <= chi <= mu2**2, True)
    actual, moments = saved
    mu2, mu4, tau, chi = moments
    deltas = [comb(5, 2)*mu4, comb(5, 3)*mu2**2, comb(5, 3)*tau,
              comb(5, 4)*mu2**2, comb(5, 4)*chi]
    for label, delta in zip(["mu4 coefficient", "three-label doubled-path coefficient",
                            "triangle coefficient", "disjoint doubled-pair coefficient",
                            "four-cycle coefficient"], deltas):
        mutation("decrement " + label, actual, actual-delta)

    # Independent combinatorial enumeration: weighted unordered edge multisets.
    for n in range(2, 8):
        edges = list(combinations(range(n), 2))
        counts = Counter()
        for edge_list in combinations_with_replacement(edges, 4):
            degree = Counter(v for e in edge_list for v in e)
            if min(degree.values()) == 1:
                continue
            mult = Counter(edge_list)
            coefficient = factorial(4)
            for m in mult.values():
                coefficient //= factorial(m)
            num_vertices = len(degree)
            if num_vertices == 2:
                label = "one_edge"
            elif num_vertices == 3:
                label = "doubled_path" if len(mult) == 2 else "triangle"
            elif num_vertices == 4:
                label = "two_pairs" if len(mult) == 2 else "cycle"
            else:
                raise AssertionError(("unclassified leaf-free graph", edge_list))
            counts[label] += coefficient
        expected = {"one_edge": comb(n, 2), "doubled_path": 18*comb(n, 3),
                    "triangle": 36*comb(n, 3), "two_pairs": 18*comb(n, 4),
                    "cycle": 72*comb(n, 4)}
        for label, count in expected.items():
            check("exact_graph_multiplicities", counts[label], count, str((n, label)))

    group, sub = finite_group((5,))
    raw = [F(4)] + [F(-1)]*4
    clip = [min(v, F(1)) for v in raw]
    mean = sum(clip)/5
    centered = [v-mean for v in clip]
    n = 3
    good, bad = 0, 0
    for labels in product(range(5), repeat=n):
        raw_h = sum(raw[sub(labels[i], labels[j])] for i, j in combinations(range(n), 2))/n
        clp_h = sum(centered[sub(labels[i], labels[j])] for i, j in combinations(range(n), 2))/n
        event = any(raw[sub(labels[i], labels[j])] > 1 for i, j in combinations(range(n), 2))
        if event:
            bad += 1
        else:
            good += 1
            check("exact_clipping_recenter_on_good", raw_h, clp_h + F(n-1, 2)*mean)
    check("exact_clipping_union_bound", F(bad, 5**n) <= comb(n, 2)*F(1, 5), True)
    actual = exhaustive_fourth(clip, sub, 4)
    altered = sum(four_terms(4, group_moments(clip, sub)), F(0))
    mutation("omit zero-mean recentering in graph formula", actual, altered)
    SAMPLES.append({"clipping_finite_group": {"good": good, "bad": bad,
                    "mean": str(mean), "label": "auxiliary algebra only"}})


def dot(p, q):
    return sum(x*y for x, y in zip(p, q))


def add(p, q):
    return tuple(x+y for x, y in zip(p, q))


def neg(p):
    return tuple(-x for x in p)


ZERO = (0, 0, 0, 0)


def polynomial_add(poly, coefficient, n, terms):
    if not coefficient:
        return
    powers = [ZERO]*n
    for label, exponent in terms:
        powers[label] = add(powers[label], exponent)
    key = tuple(powers)
    poly[key] += coefficient
    if not poly[key]:
        del poly[key]


def fourier_polynomial_tests():
    support = [q for q in product(range(-2, 3), repeat=4) if 0 < sum(abs(x) for x in q) <= 2]
    ar = {q: F(1, dot(q, q)*(1+dot(q, q))) for q in support}
    mutation_done = False
    for k in [(1, 0, 0, 0), (1, 1, 0, 0), (2, 0, 0, 0)]:
        d = dot(k, k)*ar[k]  # c factored out; finite smooth even Fourier kernel.
        b = defaultdict(F)
        for q, aq in ar.items():
            b[q] += dot(k, q)*aq
            b[add(q, neg(k))] -= dot(k, q)*aq
        b[ZERO] += d
        b[neg(k)] += d
        all_m = set(b)
        for m in list(all_m):
            all_m.add(add(neg(k), neg(m)))
        for m in all_m:
            expected = dot(k, m)*ar.get(m, F(0)) - dot(k, add(m, k))*ar.get(add(m, k), F(0))
            expected += d*((m == ZERO)+(m == neg(k)))
            check("exact_Fourier_coefficients", b[m], expected)
            check("exact_Fourier_symmetry", b[m], b[add(neg(k), neg(m))])
        check("exact_zero_rows", b[ZERO], 0)
        check("exact_zero_rows", b[neg(k)], 0)
        check("exact_smooth_diagonal_sum", sum(b.values()), 2*d)
        for n in range(2, 6):
            direct, spectral, no_self = defaultdict(F), defaultdict(F), defaultdict(F)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        for q, aq in ar.items():
                            polynomial_add(direct, F(1, 2*n*n)*dot(k, q)*aq, n,
                                           [(i, add(k, q)), (j, neg(q))])
                            polynomial_add(direct, -F(1, 2*n*n)*dot(k, q)*aq, n,
                                           [(i, q), (j, add(k, neg(q)))])
                        polynomial_add(direct, d/F(2*n*n), n, [(i, k)])
                        polynomial_add(direct, d/F(2*n*n), n, [(j, k)])
                    for m, bm in b.items():
                        polynomial_add(spectral, bm/F(2*n*n), n,
                                       [(i, add(k, m)), (j, neg(m))])
                        polynomial_add(no_self, bm/F(2*n*n), n,
                                       [(i, add(k, m)), (j, neg(m))])
                polynomial_add(spectral, -d/F(n*n), n, [(i, k)])
            check("exact_empirical_deleted_polynomial", dict(direct), dict(spectral), str((k, n)))
            if not mutation_done:
                key = next(key for key in no_self if no_self[key] != direct.get(key, 0))
                mutation("discard smooth empirical diagonal", direct.get(key, F(0)), no_self[key])
                mutation("use c instead of heat row response d", F(0), 1-d)
                mutation_done = True


def label_tests():
    for n in range(2, 7):
        j = [[F((i+1)*(q+1)+i+q+3, 7) for q in range(n)] for i in range(n)]
        tags = [[F(i*i-3*i+1, 11) for i in range(n)],
                [F(2*i*i+i+2, 13) for i in range(n)]]
        u = sum(j[i][q] for i in range(n) for q in range(n) if i != q)/F(2*n*n)
        p = F((n-1)*(n-2), 2*n)
        for case, tag in enumerate(tags):
            a2 = sum((j[perm[0]][perm[1]]*tag[perm[0]] for perm in permutations(range(n))), F(0))/factorial(n)
            if n > 2:
                a3 = sum((j[perm[0]][perm[1]]*tag[perm[2]] for perm in permutations(range(n))), F(0))/factorial(n)
            else:
                a3 = F(0)
            actual = n*u*sum(tag)/n
            expected = F(n-1, n)*a2+p*a3
            check("exact_exchangeable_current_initial_counts", actual, expected, str((n, case)))
            if n == 4 and case == 1:
                mutation("halve the two overlapping orientations", actual, F(n-1, 2*n)*a2+p*a3)
                mutation("double the all-distinct triple multiplicity", actual, F(n-1, n)*a2+2*p*a3)
    n = 4
    current, initial = [1, 1, -1, 1], [1, -1, -1, 1]
    z, z0 = F(sum(current), n), F(sum(initial), n)
    cpair = sum(F(current[i]*current[j]) for i in range(n) for j in range(n) if i != j)/F(n*(n-1))
    opair = sum(F(current[i]*initial[j]) for i in range(n) for j in range(n) if i != j)/F(n*(n-1))
    same = sum(F(current[i]*initial[i]) for i in range(n))/n
    check("exact_same_label_current", cpair, (n*z*z-1)/(n-1))
    check("exact_same_label_mixed", opair, (n*z*z0-same)/(n-1))
    mutation("omit mixed same-label subtraction", opair, n*z*z0/(n-1))
    mutation("replace mixed same-label phase by one", opair, (n*z*z0-1)/(n-1))
    delta, weight_current, weight_mixed = F(2, 7), F(3, 5), F(1, 3)
    triples = [(i, j, l) for i in range(n) for j in range(n) for l in range(n) if len({i, j, l}) == 3]
    raw_rows = sum(delta*(current[i]+current[j])*(weight_current*current[l]-weight_mixed*initial[l])
                   for i, j, l in triples)/F(2*n)
    row_formula = F((n-1)*(n-2), n)*delta*(weight_current*cpair-weight_mixed*opair)
    # triple normalization in p_N E[...] is sum/(2N^2), not sum/(2N).
    raw_rows /= n
    check("exact_raw_tail_row_correction", raw_rows, row_formula)
    mutation("silently center the raw tail by dropping row correction", row_formula, F(0))


def martingale_tests():
    outcomes = list(product([-1, 1], repeat=3))  # eta is time-zero, x,y are independent increments.
    initial_left = initial_right = terminal_left = terminal_right = cross = bracket_cross = F(0)
    fourth = bracket_square = F(0)
    for eta, x, y in outcomes:
        m = x+(1+x)*y
        l = 2*x+(2-x)*y
        bracket = 1+(1+x)**2
        initial_event = eta == 1
        terminal_event = m > 2
        initial_left += F(initial_event*m*m, 8)
        initial_right += F(initial_event*bracket, 8)
        terminal_left += F(terminal_event*m*m, 8)
        terminal_right += F(terminal_event*bracket, 8)
        cross += F(m*l, 8)
        bracket_cross += F(2+(1+x)*(2-x), 8)
        fourth += F(max(abs(x), abs(m))**4, 8)
        bracket_square += F(bracket**2, 8)
    check("exact_time_zero_event_isometry", initial_left, initial_right)
    check("exact_common_driver_cross_bracket", cross, bracket_cross)
    check("finite_martingale_fourth_bound_diagnostic", fourth <= 100*bracket_square, True)
    mutation("replace time-zero event by terminal event", terminal_left, terminal_right)
    mutation("discard energy-observable common-noise cross term", cross, F(0))


def response_weight_tests():
    for n in [2, 3, 7, 19]:
        for t in [0.0, 0.03, 0.7]:
            nuell, c = 0.27, 1.0
            a = c+nuell
            at = a-c/n
            aa = exp(-a*t)
            e = exp(-at*t)
            i1 = -__import__('math').expm1(-at*t)/at
            i2 = -__import__('math').expm1(-2*at*t)/(2*at)
            ff, gg = 0.9, 0.4
            vv = e*e+(2*nuell+2*ff)*i2
            rr = e+gg*i1
            defect = vv+aa*aa-2*aa*rr
            exact = (e-aa)**2+2*nuell*i2+2*(ff*i2-aa*gg*i1)
            close("floating_two_response_weights", defect, exact, str((n, t)))
            if n == 7 and t == 0.7:
                wrong_mixed = (e-aa)**2+2*nuell*i2+2*(ff*i2-gg*i2)
                mutation("use current-current weight for mixed response", exact, wrong_mixed, "floating")
                wrong_original = vv+e*e-2*e*rr
                mutation("replace original backward weight by shifted rate", defect, wrong_original, "floating")


def gaussian_frequency_tests():
    c = 4*pi*pi
    modes = list(product(range(-3, 4), repeat=4))
    modes += [(j, 0, 0, 0) for j in [-64, -32, -16, -8, 8, 16, 32, 64]]
    modes += [(j, j, j, j) for j in [-32, -16, -8, 8, 16, 32]]
    for k in [(1, 0, 0, 0), (1, -1, 1, 0), (5, -3, 2, 1)]:
        ratios = []
        for r in [1/64, 1/256, 1/1024, 1e-6]:
            def aa(m):
                norm = dot(m, m)
                return exp(-c*r*norm)/norm if norm else 0.0
            dr = c*exp(-c*r*dot(k, k))
            def bb(m):
                return c*(dot(k, m)*aa(m)-dot(k, add(m, k))*aa(add(m, k)))+dr*((m == ZERO)+(m == neg(k)))
            close("floating_actual_heat_zero_rows", bb(ZERO), 0.0)
            close("floating_actual_heat_zero_rows", bb(neg(k)), 0.0)
            for m in modes:
                close("floating_actual_heat_symmetry", bb(m), bb(add(neg(k), neg(m))))
                norm = dot(m, m)
                if norm:
                    denominator = exp(-c*r*norm/8)/norm
                    assert denominator > 0
                    ratio = abs(bb(m))/denominator
                    assert isfinite(ratio)
                    CHECKS["floating_all_frequency_domination_sample"] += 1
                    ratios.append(ratio)
        SAMPLES.append({"heat_coefficient_sample": {"k": list(k), "max_r8_ratio": max(ratios),
                        "samples": len(ratios), "label": "finite floating support, not proof"}})
    # The proposed *wrong* same-scale domination has an analytic exponential obstruction.
    # At k=e1, m=-n e1: b/a_r(m)=c[-n+n^2/(n-1) exp(cr(2n-1))].
    r = 1/64
    def log_wrong_ratio(n):
        return log(c)+2*log(n)-log(n-1)+c*r*(2*n-1)+log(1-(n-1)/n*exp(-c*r*(2*n-1)))
    growth = log_wrong_ratio(64)-log_wrong_ratio(8)
    mutation("replace r/8 domination by uniformly bounded same-scale Gaussian ratio",
             growth, 0.0, "floating")
    check("exact_cutoff_first_power", -F(1, 2)+11*F(1, 24), -F(1, 24))
    check("exact_cutoff_noise_power", -F(3, 4)+F(1, 24), -F(17, 24))
    check("exact_open_delta_boundary", -F(1, 2)+11*F(1, 22), 0)
    mutation("claim decay at the excluded delta=1/22 boundary", F(0), -F(1, 24))


def main():
    graph_and_clipping_tests()
    fourier_polynomial_tests()
    label_tests()
    martingale_tests()
    response_weight_tests()
    gaussian_frequency_tests()
    assert len({m['name'] for m in MUTATIONS}) == len(MUTATIONS)
    return {"audit": "AUD079", "status": "PASS", "check_count": sum(CHECKS.values()),
            "checks_by_category": dict(sorted(CHECKS.items())), "mutation_count": len(MUTATIONS),
            "nonzero_mutations": MUTATIONS, "samples": SAMPLES,
            "scope": "Supporting exact finite algebra and labelled floating diagnostics; proof is REPORT.md.",
            "randomness": "None; exhaustive or deterministic inputs.",
            "actual_singular_process_simulated": False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(main(), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end='')
