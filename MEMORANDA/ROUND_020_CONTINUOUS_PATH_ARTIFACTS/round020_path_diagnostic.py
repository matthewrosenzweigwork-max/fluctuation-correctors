#!/usr/bin/env python3
"""Fresh exact TASK090 path diagnostics; standard library, no prior checker.

Run without arguments to emit a deterministic JSON record on stdout. The
program reads only its own bytes to record its digest. It writes no files.
Exponential polynomials are finite formal sums with exact rational exponents
and coefficients; continuum inequalities are proved in the memorandum.
"""

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from json import dumps
from math import factorial
from pathlib import Path


counts = defaultdict(int)
mutations = {}
examples = {}


def check(category, assertion, description):
    if not assertion:
        raise AssertionError(category + ": " + description)
    counts[category] += 1


def reject(name, actual, mutated, explanation):
    if actual == mutated:
        raise AssertionError("Vacuous mutation: " + name)
    if name in mutations:
        raise AssertionError("Duplicate mutation name: " + name)
    mutations[name] = {
        "status": "REJECTED",
        "actual": repr(actual),
        "mutated": repr(mutated),
        "reason": explanation,
    }
    counts["nonvacuous_mutation_controls"] += 1


def ep_clean(p):
    return {F(e): F(c) for e, c in p.items() if c}


def ep(e=0, c=1):
    return ep_clean({F(e): F(c)})


def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for e, c in p.items():
            out[e] += c
    return ep_clean(out)


def scale(p, c):
    return ep_clean({e: v * F(c) for e, v in p.items()})


def multiply(*ps):
    out = ep()
    for p in ps:
        new = defaultdict(F)
        for e, c in out.items():
            for f, d in p.items():
                new[e + f] += c * d
        out = ep_clean(new)
    return out


def cov_integral(D, a, nu, b, t, u):
    """Initial Gram plus direct evaluation of 2 nu b a time integral."""
    L = D + nu * a
    v = min(t, u)
    initial = ep(L * (t + u), b)
    upper = ep(L * (t + u - 2 * v), nu * b * a / L)
    lower = ep(L * (t + u), -nu * b * a / L)
    return add(initial, upper, lower)


def cov_card(D, a, nu, b, t, u):
    L = D + nu * a
    return add(ep(L * (t + u), b * D / L),
               ep(L * abs(t - u), b * nu * a / L))


def exp_taylor(rate, order=4):
    return [F((-rate) ** k, factorial(k)) for k in range(order + 1)]


def series_add(*xs):
    return [sum((x[k] for x in xs), F()) for k in range(len(xs[0]))]


def series_scale(xs, c):
    return [F(c) * x for x in xs]


def series_mul(xs, ys):
    return [sum((xs[j] * ys[k - j] for j in range(k + 1)), F())
            for k in range(len(xs))]


def moment(distribution, power):
    return sum((p * x ** power for x, p in distribution), F())


def literal_iid_fourth(distribution, N):
    out = F()
    for atoms in product(distribution, repeat=N):
        total, prob = F(), F(1)
        for x, p in atoms:
            total += x
            prob *= p
        out += prob * total ** 4
    return out / N ** 2


def tent(n, j, t):
    left, right = F(j, n), F(j + 1, n)
    if t <= left or t >= right:
        return F()
    mid = (left + right) / 2
    return 2 * n * (t - left if t <= mid else right - t)


def run():
    Ds = [F(1, 3), F(1), F(7, 2)]
    aas = [F(1, 2), F(1), F(5)]
    nus = [F(0), F(1, 5), F(1), F(3)]
    times = [F(0), F(1, 7), F(2, 3), F(1), F(5, 2)]

    for D, a, nu, t, u in product(Ds, aas, nus, times, times):
        b = min(F(1), 1 / nu) if nu else F(1)
        got = cov_integral(D, a, nu, b, t, u)
        wanted = cov_card(D, a, nu, b, t, u)
        check("modal_covariance_integral_vs_card", got == wanted,
              repr((D, a, nu, t, u)))
        check("modal_covariance_symmetry", got == cov_card(D, a, nu, b, u, t),
              repr((D, a, nu, t, u)))
        if not t or not u:
            check("zero_time_covariance", got == ep((D + nu * a) * (t + u), b),
                  "initial thermal integral must vanish")
        if not nu:
            check("zero_noise_covariance", got == ep(D * (t + u), b),
                  "deterministic propagated initial Gaussian")

    # Several observables, including a constant (zero nonconstant coefficients)
    # and an exact linear dependency, at equal and unequal deterministic times.
    modes = [(F(1), F(2)), (F(3), F(1)), (F(1, 2), F(5))]
    coeffs = [[F(1), F(2), F(-1)], [F(0), F(1), F(3)],
              [F(1), F(3), F(2)], [F(0), F(0), F(0)]]
    for nu, t, u in product(nus, times, times):
        b = min(F(1), 1 / nu) if nu else F(1)
        matrix = [[add(*(scale(cov_integral(D, a, nu, b, t, u),
                                    coeffs[i][k] * coeffs[j][k])
                         for k, (D, a) in enumerate(modes)))
                   for j in range(4)] for i in range(4)]
        for j in range(4):
            check("cross_observable_linear_dependence",
                  matrix[2][j] == add(matrix[0][j], matrix[1][j]),
                  "h_2 = h_0 + h_1")
            check("constant_observable", matrix[3][j] == {}, "constant row")

    # Exact small-delta series, leaving E = exp(-2 L u) as an independent
    # formal coefficient. Compare increment variance from covariance against
    # an independently assembled OU restart identity.
    one = [F(1), F(), F(), F(), F()]
    for D, a, nu in product(Ds, aas, nus):
        b = min(F(1), 1 / nu) if nu else F(1)
        L = D + nu * a
        e1, e2 = exp_taylor(L), exp_taylor(2 * L)
        diff = series_add(e1, series_scale(one, -1))
        squared = series_mul(diff, diff)
        initial_cov_series = series_scale(
            series_add(e2, one, series_scale(e1, -2)), b * D / L)
        thermal_cov_series = series_scale(
            series_add(series_scale(one, 2), series_scale(e1, -2)), b * nu * a / L)
        initial_restart = series_scale(squared, b * D / L)
        thermal_restart = series_add(
            series_scale(squared, b * nu * a / L),
            series_scale(series_add(one, series_scale(e2, -1)), b * nu * a / L))
        check("increment_series_initial", initial_cov_series == initial_restart,
              "coefficient of exp(-2 L u)")
        check("increment_series_thermal", thermal_cov_series == thermal_restart,
              "constant coefficient in exp(-2 L u)")
        check("increment_diffusion_cusp", initial_cov_series[1] == 0 and
              thermal_cov_series[1] == 2 * b * nu * a, "right linear coefficient")
        if not nu:
            check("zero_noise_increment_quadratic", initial_cov_series[2] == b * D ** 2
                  and thermal_cov_series == [F()] * 5, "zero-noise quadratic scale")

    # The common-history part of a stochastic-convolution increment.
    for D, a, nu, u, delta in product(Ds, aas, [F(1, 5), F(1), F(3)],
                                     [F(1, 3), F(1)], [F(1, 7), F(1, 2)]):
        b, L = min(F(1), 1 / nu), D + nu * a
        old = scale(multiply(add(ep(L * delta), ep(0, -1)),
                             add(ep(L * delta), ep(0, -1)),
                             add(ep(), ep(2 * L * u, -1))), b * nu * a / L)
        recent = scale(add(ep(), ep(2 * L * delta, -1)), b * nu * a / L)
        thermal = lambda t, v: add(cov_integral(D, a, nu, b, t, v),
                                   ep(L * (t + v), -b))
        direct = add(thermal(u + delta, u + delta), thermal(u, u),
                     scale(thermal(u + delta, u), -2))
        check("moving_terminal_common_history", direct == add(old, recent),
              "full old-plus-recent variance")
        check("common_history_nonzero", old != {}, "positive factors for u, delta, nu > 0")

    distributions = [
        [(F(-1), F(1, 2)), (F(1), F(1, 2))],
        [(F(-2), F(1, 4)), (F(-1), F(1, 4)),
         (F(1), F(1, 4)), (F(2), F(1, 4))],
        [(F(-1), F(1, 2)), (F(0), F(1, 4)), (F(2), F(1, 4))],
    ]
    for dist in distributions:
        check("iid_distribution_preflight", moment(dist, 0) == 1 and moment(dist, 1) == 0,
              "unit mass and zero mean")
        mu2, mu4 = moment(dist, 2), moment(dist, 4)
        for N in range(2, 7):
            literal = literal_iid_fourth(dist, N)
            formula = mu4 / N + 3 * F(N - 1, N) * mu2 ** 2
            check("literal_iid_fourth_moment", literal == formula, repr((dist, N)))
            for b, delta in product([F(1), F(1, 3)], [F(0), F(1, 7), F(1, 2)]):
                check("iid_increment_scaling", b ** 2 * delta ** 4 * literal ==
                      b ** 2 * (delta ** 4 * mu4 / N +
                                3 * F(N - 1, N) * (delta ** 2 * mu2) ** 2),
                      "b squared, N normalization and fourth increment power")

    # Exact random-tent counterexample: at each t at most one tent is nonzero,
    # but every chosen continuous path has supremum and small-scale modulus 1.
    for n in [2, 3, 4, 8, 16, 24]:
        for k in range(4 * n + 1):
            t = F(k, 4 * n)
            values = [tent(n, j, t) for j in range(n)]
            check("tent_each_time_mean", sum(values, F()) / n <= F(1, n),
                  "each-time expected size")
            check("tent_disjoint_supports", sum(v > 0 for v in values) <= 1,
                  "at most one active tent")
        for j in range(n):
            mid, left = F(2 * j + 1, 2 * n), F(j, n)
            check("tent_supremum", tent(n, j, mid) == 1, "every path reaches one")
            check("tent_modulus", abs(tent(n, j, mid) - tent(n, j, left)) == 1
                  and mid - left == F(1, 2 * n), "small-scale modulus one")

    # Dyadic union counts and the exact threshold for the fourth-moment proof.
    gamma = F(1, 8)
    check("dyadic_exponent", 1 - 4 * gamma == F(1, 2), "positive summability exponent")
    for n in range(2, 22, 2):
        union_bound = F(2) ** n * F(2) ** (-2 * n) * F(2) ** (n // 2)
        check("dyadic_interval_count", union_bound == F(2) ** (-n // 2),
              "2^n adjacent intervals, fourth moment and threshold")
    for d in range(3, 11):
        for s in [F(1, 2), F(1), F(d - 2, 2), F(d - 2)]:
            if not 0 < s <= d - 2:
                continue
            alpha = F(d, 2) - s / 2
            exponent_self = -1 + (-s / 2) * F(-2, d)
            exponent_mass = alpha * F(-2, d)
            check("source_balanced_scaling", exponent_self == exponent_mass == s / d - 1,
                  repr((d, s)))
            if s < F(d, 2):
                check("path_remainder_decay", F(1, 2) + exponent_self < 0,
                      repr((d, s)))

    # Independent adapted-Brownian example with exact half-Gaussian moments.
    cplus, cminus = F(2), F(1)
    expected_bracket = 1 + (cplus ** 2 + cminus ** 2) / 2
    fourth = F(3) + 3 * (cplus ** 2 + cminus ** 2) + F(3, 2) * (cplus ** 4 + cminus ** 4)
    bracket_bound = 1 + max(cplus ** 2, cminus ** 2)
    check("adapted_martingale_fourth_bound", fourth <= 3 * bracket_bound ** 2,
          "deterministic bracket bound is valid")
    check("adapted_martingale_values", expected_bracket == F(7, 2) and fourth == F(87, 2),
          "exact non-Gaussian adapted terminal moments")
    examples["adapted_Brownian"] = {
        "expected_bracket": str(expected_bracket), "fourth_moment": str(fourth),
        "three_times_mean_bracket_squared": str(3 * expected_bracket ** 2),
        "valid_deterministic_bound": str(3 * bracket_bound ** 2),
    }

    D, a, nu, b, t, u = F(1), F(2), F(1, 2), F(1), F(1), F(1, 3)
    L = D + nu * a
    actual = cov_integral(D, a, nu, b, t, u)
    init = ep(L * (t + u), b)
    thermal = add(actual, scale(init, -1))
    reject("remove_Brownian_factor_two", actual, add(init, scale(thermal, F(1, 2))),
           "Direct 2 nu b a integral disagrees when the noise factor two is removed.")
    reject("remove_thermal_term", actual, init, "Positive noise and positive common horizon.")
    reject("conflate_initial_time_sum_with_difference", actual,
           add(ep(L * abs(t - u), b * D / L), ep(L * abs(t - u), b * nu * a / L)),
           "Initial transient depends on the sum of the terminal times.")
    reject("insert_deleted_pair_factor_in_bracket", actual,
           add(init, scale(thermal, F(2, 3))),
           "A one-body Brownian bracket has no (N-1)/N factor, here N=3.")
    reject("omit_initial_Gaussian", actual, thermal, "Initial iid variance is nonzero.")
    reject("wrong_modal_decay_sign", ep(L * t), ep(-L * t), "Damping sign is fixed by the generator.")
    reject("wrong_increment_diffusion_cusp", 2 * b * nu * a, b * nu * a,
           "The right small-increment variance coefficient is 2 nu b a.")

    delta = t - u
    old = scale(multiply(add(ep(L * delta), ep(0, -1)),
                         add(ep(L * delta), ep(0, -1)),
                         add(ep(), ep(2 * L * u, -1))), b * nu * a / L)
    reject("drop_common_history_convolution_increment", old, {},
           "Factorization is (b nu a/L)(1-exp(-L delta))^2(1-exp(-2 L u)) > 0.")
    reject("source_each_time_mean_controls_supremum", F(1), F(1, 8),
           "For eight random tents E sup=1 but sup_t E=1/8.")
    reject("ignore_dyadic_number_of_intervals", F(1, 4), F(1, 64),
           "At n=4 the required union includes 16 adjacent intervals.")
    dist, N = distributions[2], 3
    mu2, mu4 = moment(dist, 2), moment(dist, 4)
    reject("omit_one_iid_pair_partition", literal_iid_fourth(dist, N),
           mu4 / N + 2 * F(N - 1, N) * mu2 ** 2,
           "Fourth moments have three pair partitions.")
    reject("replace_random_bracket_by_its_mean", fourth, 3 * expected_bracket ** 2,
           "The exact adapted Brownian fourth moment differs by 27/4.")
    literal_variance = sum((F(1, 8) * (sum(signs) * F(1, 7)) ** 2 / 3
                            for signs in product([-1, 1], repeat=3)), F())
    reject("incorrect_initial_triangular_sqrt_N_loss", literal_variance, F(3, 49),
           "Three independent centered summands divided by sqrt(3) retain one-summand variance.")

    return {
        "status": "PASS",
        "task": "TASK-090 / THM042",
        "evidence": "Exact constructor diagnostic; not an independent gate or continuum proof",
        "arithmetic": "fractions and finite formal exponential polynomials",
        "randomness": "none",
        "dependencies": "Python standard library only",
        "program_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "assertions": sum(counts.values()),
        "categories": dict(sorted(counts.items())),
        "mutation_controls": mutations,
        "examples": examples,
        "limitations": [
            "Modal rates D and a are exact positive rational diagnostic parameters; physical Riesz normalization is proved analytically.",
            "Formal exponential-polynomial equality checks coefficient algebra, not an estimated numerical continuum error.",
            "The tent and adapted-Brownian examples reject probability shortcuts; they are not admitted particle-law counterexamples.",
            "Singular energy, source domination, tightness and weak convergence are established by the memorandum, not by sampled trajectories.",
        ],
    }


if __name__ == "__main__":
    print(dumps(run(), indent=2, sort_keys=True))
