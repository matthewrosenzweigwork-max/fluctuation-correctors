#!/usr/bin/env python3
"""Fresh exact diagnostics for TASK070; Python standard library only.

These finite algebra checks support, but do not prove, the analytic statements.
No supplied or previous verification program is imported or read.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import platform


CHECKS = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


ZERO = (F(0), F(0))
GRID = range(3)
UNIT = (F(3, 5), F(4, 5))


def scalar(x, y):
    return F(((x + 1) * (y + 2)) % 7 - 3, 2)


def fields(level):
    def g(x, y):
        return scale(UNIT, scalar(x, y))

    def clipped(x, y):
        z = scalar(x, y)
        return scale(UNIT, max(-level, min(level, z)))

    def tail(x, y):
        return sub(g(x, y), clipped(x, y))

    return {"full": g, "clipped": clipped, "tail": tail}


def field_data(g):
    a = {x: scale(tuple(sum((g(x, y)[j] for y in GRID), F(0))
                        for j in range(2)), F(1, 3)) for x in GRID}

    def h(x, y):
        return sub(g(x, y), a[x])

    return a, h


def particle_fields(config, g, a):
    n = len(config)
    out = []
    for i, x in enumerate(config):
        val = ZERO
        for j, y in enumerate(config):
            if i != j:
                val = add(val, g(x, y))
        out.append(scale(sub(val, scale(a[x], n)), F(1, n * n)))
    return out


def expectation(configs, weights, func):
    denominator = sum(weights)
    return sum((w * func(c) for c, w in zip(configs, weights)), F(0)) / denominator


def finite_label_checks():
    for n in range(2, 6):
        configs = list(product(GRID, repeat=n))
        weights = [1 + sum(c[i] == c[j] for i, j in combinations(range(n), 2))
                   for c in configs]
        # This explicitly correlated law is exchangeable and cyclic-translation
        # invariant, so every one-coordinate marginal is uniform.
        for x in GRID:
            check(f"one_body_Haar_N{n}_x{x}",
                  expectation(configs, weights, lambda c: F(c[0] == x)) == F(1, 3))
        for level in (F(1, 4), F(3, 4), F(5, 4)):
            all_fields = fields(level)
            all_values = {}
            for label, g in all_fields.items():
                a, h = field_data(g)
                val = {c: particle_fields(c, g, a) for c in configs}
                all_values[label] = val
                for x in GRID:
                    check(f"row_center_N{n}_{level}_{label}_x{x}",
                          all(sum((h(x, y)[j] for y in GRID), F(0)) == 0
                              for j in range(2)))
                direct = expectation(configs, weights,
                                     lambda c: sum((dot(v, v) for v in val[c]), F(0)))
                pair = expectation(configs, weights, lambda c: dot(h(c[0], c[1]), h(c[0], c[1])))
                triple = (expectation(configs, weights,
                                      lambda c: dot(h(c[0], c[1]), h(c[0], c[2])))
                          if n >= 3 else F(0))
                mixed = expectation(configs, weights, lambda c: dot(h(c[0], c[1]), a[c[0]]))
                one = expectation(configs, weights, lambda c: dot(a[c[0]], a[c[0]]))
                expanded = F(1, n**3) * ((n - 1) * pair + (n - 1) * (n - 2) * triple
                                         - 2 * (n - 1) * mixed + one)
                check(f"four_contractions_N{n}_{level}_{label}", direct == expanded)
                haar = expectation(configs, [1] * len(configs),
                                   lambda c: sum((dot(v, v) for v in val[c]), F(0)))
                g2 = sum((dot(g(x, y), g(x, y)) for x, y in product(GRID, repeat=2)), F(0)) / 9
                a2 = sum((dot(a[x], a[x]) for x in GRID), F(0)) / 3
                check(f"Haar_identity_N{n}_{level}_{label}",
                      haar == F(n - 1, n**3) * g2 - F(n - 2, n**3) * a2)
                # Direct deletion compared with an empirical full sum. The
                # missing self is evaluated only in this smooth finite model.
                for c in configs:
                    x = c[0]
                    empirical = ZERO
                    for y in c:
                        empirical = add(empirical, scale(g(x, y), F(1, n)))
                    missing_self = scale(sub(sub(empirical, a[x]), scale(g(x, x), F(1, n))), F(1, n))
                    check(f"missing_self_N{n}_{level}_{label}_{c}", val[c][0] == missing_self)
            for c in configs:
                check(f"clip_tail_linearity_N{n}_{level}_{c}",
                      all(add(a, b) == z for a, b, z in
                          zip(all_values['clipped'][c], all_values['tail'][c], all_values['full'][c])))
            norm = {}
            for label, val in all_values.items():
                norm[label] = expectation(configs, weights,
                                          lambda c: sum((dot(v, v) for v in val[c]), F(0)))
            cross = expectation(configs, weights,
                                lambda c: sum((dot(a, b) for a, b in
                                               zip(all_values['clipped'][c], all_values['tail'][c])), F(0)))
            check(f"norm_polarization_N{n}_{level}",
                  norm['full'] == norm['clipped'] + norm['tail'] + 2 * cross)
            check(f"Cauchy_tail_metric_N{n}_{level}", cross**2 <= norm['clipped'] * norm['tail'])
        check(f"clipping_combinatoric_constant_N{n}",
              2 * (n - 1) + (n - 1) * (n - 2) == n * (n - 1))


def polynomial_product(a, b):
    out = defaultdict(F)
    for ka, ca in a.items():
        for kb, cb in b.items():
            out[tuple(x + y for x, y in zip(ka, kb))] += ca * cb
    return dict(out)


def cosine_pair(terms):
    out = defaultdict(F)
    for (kx, ky), coefficient in terms:
        out[(kx, ky)] += coefficient / 2
        out[(-kx, -ky)] += coefficient / 2
    return dict(out)


def lift(poly, slots):
    out = {}
    for key, value in poly.items():
        full = [0, 0, 0]
        for index, frequency in zip(slots, key):
            full[index] = frequency
        out[tuple(full)] = value
    return out


def covariance_checks():
    # Real trigonometric polynomials; all second-slot frequencies are nonzero.
    h = cosine_pair([((0, 1), F(1)), ((1, 2), F(1, 2)), ((2, -1), F(1, 3)),
                     ((-1, 3), F(2, 5))])
    ht = cosine_pair([((1, 1), F(2, 3)), ((0, 2), F(-1, 4))])
    z = polynomial_product(lift(h, (0, 1)), lift(h, (0, 2)))
    zt1 = polynomial_product(lift(ht, (0, 1)), lift(h, (0, 2)))
    zt2 = polynomial_product(lift(h, (0, 1)), lift(ht, (0, 2)))
    check("initial_triple_zero", z.get((0, 0, 0), F(0)) == 0)
    check("time_derivative_centering_zero", zt1.get((0, 0, 0), F(0)) + zt2.get((0, 0, 0), F(0)) == 0)
    for n in (3, 4, 7, 29):
        for coulomb in (False, True):
            d = {k: (F(7, 3) if coulomb else F(1, abs(k))) for k in (-3, -2, -1, 1, 2, 3)}
            contributions = {}
            generator = F(0)
            for i, j in combinations(range(3), 2):
                term = F(0)
                for k, dk in d.items():
                    mode = [0, 0, 0]
                    mode[i], mode[j] = k, -k
                    opposite = tuple(-v for v in mode)
                    coefficient = z.get(opposite, F(0))
                    term += dk * coefficient
                    # In angular coordinates K_hat(k)=-i*d_k/k and the
                    # derivative contributes i*(m_i-m_j). Their product is real.
                    generator += F(1, n) * dk * F(opposite[i] - opposite[j], k) * coefficient
                contributions[(i, j)] = term
            fourier_energy = sum((d[ky] * value**2 for (kx, ky), value in h.items()), F(0))
            density_derivative = -F(2, n) * sum(contributions.values(), F(0))
            check(f"pairs12_13_cancel_N{n}_C{coulomb}", contributions[(0, 1)] == contributions[(0, 2)] == 0)
            check(f"BBGKY_sign_coefficient_N{n}_C{coulomb}", density_derivative == -F(2, n) * fourier_energy)
            check(f"generator_reconstruction_N{n}_C{coulomb}", generator == density_derivative)
            check(f"initial_sign_N{n}_C{coulomb}", density_derivative < 0)
            if coulomb:
                l2 = sum((v**2 for v in h.values()), F(0))
                check(f"Coulomb_Parseval_N{n}", density_derivative == -F(14, 3 * n) * l2)


def power_and_constant_checks():
    for d in range(3, 10):
        for s in (F(1, 2), F(d - 2, 2), F(d - 2)):
            p = s + 2
            a = s / p
            theta = 1 - s / d
            rstar = F(5 * d + 2, 2) - s / 2
            gamma = (d - s) / (d * (5 * d - s + 2))
            suffix = f"d{d}_s{s}"
            check("energy_floor_power_" + suffix, a - 1 == -2 / p)
            check("entropy_test_power_" + suffix, (a - 1) / 2 == -1 / p)
            check("clip_explicit_power_" + suffix, 2 / (4 * p) - 1 / p == -1 / (2 * p))
            check("sharp_floor_balance_" + suffix, 1 - (d - s) / d == s / d)
            check("smoothing_rate_" + suffix, -theta + gamma * rstar == -theta / 2)
            check("diagonal_delta_exponent_" + suffix, rstar - (2 * d + 1) == (d - s) / 2 > 0)
            check("density_small_window_power_" + suffix, a < 1)
            if s > 2:
                r = (1 + s / 2) / 2
                check("tail_moment_admissible_" + suffix, 1 < r < s / 2 < F(d, 2))
                check("tail_moment_threshold_" + suffix,
                      (2 - s / r) / (4 * p) == -(s / r - 2) / (4 * p) < 0)
            else:
                check("low_s_moment_obstruction_" + suffix, s / 2 <= 1)
    for nu in (F(1, 20), F(1, 2), F(1), F(3), F(17)):
        b = min(1 / nu, F(1))
        check(f"uniform_noise_weight_{nu}", nu * b <= 1 and b * b * nu <= 1)
    for n in range(2, 100):
        check(f"entropy_N_over_Nminus1_{n}", F(n, n - 1) <= 2)
        check(f"clipping_constant_16_{n}", F(2 * (n - 1) + (n - 1) * (n - 2), n*n) <= 1)


def main():
    finite_label_checks()
    covariance_checks()
    power_and_constant_checks()
    source = Path(__file__).resolve()
    result = {
        "task": "TASK070 whole-card statement-only reconstruction",
        "status": "PASS",
        "arithmetic": "exact fractions; deterministic exhaustive finite-grid and Laurent-polynomial checks",
        "python": platform.python_version(),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "check_count": len(CHECKS),
        "check_name_digest": hashlib.sha256("\n".join(CHECKS).encode()).hexdigest(),
        "groups": ["deleted-label four contractions", "Haar identity", "radial clipping with own row",
                   "missing-self coefficient", "tail norm polarization", "initial covariance from generator",
                   "BBGKY and Coulomb factors", "exponents and uniform constants"],
        "limitations": "These exact checks do not prove analytic estimates, singular limit passages, prior modules, or the unproved actual singular tail. No numerical simulation or external dependency is used.",
    }
    output = source.with_name("round010_two_reductions_diagnostics_result.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
