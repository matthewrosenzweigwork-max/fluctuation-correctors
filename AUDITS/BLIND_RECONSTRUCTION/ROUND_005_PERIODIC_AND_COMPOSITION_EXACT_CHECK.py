#!/usr/bin/env python3
"""Independent exact checks for TASK-040; standard library only.

These finite checks support, and do not replace, the accompanying analytic proof.
Run from any directory; the JSON output is written next to this script.
"""

from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json


counts = {
    "radial_identities_and_bounds": 0,
    "cutoff_product_rule": 0,
    "all_N_radial_core_and_nonlog_tail": 0,
    "pair_divergence_factor": 0,
    "iid_exact_configurations": 0,
    "iid_law_kernel_cases": 0,
    "density_factor_sharpness": 0,
    "rate_exponents": 0,
    "volterra_simplex_coefficients": 0,
}


def check(condition, label):
    if not condition:
        raise AssertionError(label)


for d in range(3, 10):
    for half_s in range(1, 2 * (d - 2) + 1):
        s = F(half_s, 2)
        numerator, denominator = s.numerator, s.denominator
        p = s + 2
        integer_p = numerator + 2 * denominator
        c_s = 2 * s * p
        a_s = c_s**2 / (16 * d)
        for N, alpha, beta in product(
            (2, 3, 11), (F(1, 2), F(2, 3), F(1)), (F(1, 2), F(1), F(3, 2))
        ):
            radius = beta**denominator
            w = (beta / alpha)**integer_p
            radius_p = beta**integer_p
            tau = F(N, 1) * (w - radius_p) / c_s
            v = alpha**integer_p
            v_sp = alpha**numerator
            profile = F(N, 4) * ((beta / alpha)**(2 * denominator) - radius**2)
            f_tau = s * (beta / alpha)**(-numerator)
            f_r = F(N, 2) * radius * (v_sp - 1)
            f_rr = F(N, 2) * (v_sp * (1 + s - s * v) - 1)
            lap = F(N, 2) * (v_sp * (d + s - s * v) - d)
            b_rad = 2 * s / N * beta**(-numerator - denominator)
            source = s * beta**(-numerator)
            check(f_rr + F(d - 1, 1) / radius * f_r == lap, "radial Laplacian")
            check(f_tau - b_rad * f_r == source, "transport source identity")
            check(lap <= 0, "superharmonic sign")
            check(d + s - (2 * s + 2) * v >= 0, "endpoint derivative sign")
            check(profile >= 0, "profile positivity")
            check(profile <= tau * source, "outer profile bound")
            check(radius * abs(f_r) <= s * profile, "logarithmic derivative bound")
            check(abs(f_r) <= s**2 * tau * beta**(-numerator - denominator), "annular gradient bound")
            L0 = F(3, 7)
            background = -L0 * radius
            check(s * L0 * profile - background * f_r >= 0, "background compensation")
            for nu in (F(0), F(1, 7), F(3)):
                check(f_tau - 2 * nu * lap - b_rad * f_r >= source, "diffusive comparison")
                counts["radial_identities_and_bounds"] += 1
                chi, chi_r, chi_rr = F(2, 5), F(-3, 7), F(4, 9)
                drift = b_rad + background
                raw = 2 * nu * (
                    chi_rr * profile + 2 * chi_r * f_r + chi * f_rr
                    + F(d - 1, 1) / radius * (chi_r * profile + chi * f_r)
                ) + drift * (chi_r * profile + chi * f_r)
                L_f = 2 * nu * lap + drift * f_r
                L_chi = 2 * nu * (chi_rr + F(d - 1, 1) / radius * chi_r) + drift * chi_r
                split = chi * L_f + profile * L_chi + 4 * nu * chi_r * f_r
                check(raw == split, "cutoff diffusion and drift product rule")
                counts["cutoff_product_rule"] += 1

        delta = F(d) - 2 * s
        for N, u, v_root in product(
            (2, 3, 11), (F(1, 3), F(1, 2)), (F(1, 4), F(1, 3), F(1, 2), F(1))
        ):
            R = u**denominator
            ell = v_root**denominator
            tau = F(N) * v_root**integer_p / c_s
            core = F(N * N, 16 * d) * ell**4 * min(R, ell)**d
            alternate = a_s * tau**2 * v_root**(-2 * numerator) * min(R, ell)**d
            check(core == alternate, "finite-N core exact rewrite")
            if delta > 0:
                R_delta = u**(denominator * d - 2 * numerator)
                ell_delta = v_root**(denominator * d - 2 * numerator)
                tail = s**2 * tau**2 * (R_delta - ell_delta) / delta if ell < R else F(0)
                bound = (a_s + s**2 / delta) * tau**2 * R_delta
                check(core + tail <= bound, "subthreshold all-N integral bound")
            elif delta < 0:
                R_delta = u**(denominator * d - 2 * numerator)
                ell_delta = v_root**(denominator * d - 2 * numerator)
                tail = s**2 * tau**2 * (R_delta - ell_delta) / delta if ell < R else F(0)
                bound = (a_s + s**2 / (-delta)) * tau**2 * ell_delta
                check(core + tail <= bound, "superthreshold all-N integral bound")
            else:
                check(core <= a_s * tau**2, "threshold all-N core bound")
            counts["all_N_radial_core_and_nonlog_tail"] += 1

        check((2 * s - d) / p - 1 == -(d + 2 - s) / p, "iid final exponent")
        check((d + 4) / p == 2 - (2 * s - d) / p, "radial time exponent")
        check(d + 2 - s >= 4, "strict final exponent in declared range")
        counts["rate_exponents"] += 1

for N, D, C0, positive_1, positive_2, positive_k in product(
    (2, 3, 11), (F(0), F(3, 7)), (F(0), F(5, 9)),
    (F(0), F(1)), (F(0), F(2)), (F(0), F(3))
):
    div_pair = (-D + positive_1) + (-D + positive_2) + F(2, N) * (-C0 + positive_k)
    check(div_pair >= -2 * (D + C0 / N), "pair divergence lower bound")
    counts["pair_divergence_factor"] += 1

mu = (F(1, 6), F(1, 3), F(1, 2))
values = (F(-2), F(1), F(3))
mean_value = sum(mu[i] * values[i] for i in range(3))
centered = tuple(value - mean_value for value in values)
kernels = {
    "constant": tuple(tuple(F(2) for _ in range(3)) for _ in range(3)),
    "additive": tuple(tuple(values[i] + values[j] for j in range(3)) for i in range(3)),
    "canonical": tuple(tuple(centered[i] * centered[j] for j in range(3)) for i in range(3)),
    "general": ((F(2), F(-1, 2), F(4, 3)),
                (F(-1, 2), F(-3), F(5, 7)),
                (F(4, 3), F(5, 7), F(1, 4))),
}
for name, phi in kernels.items():
    phi_mu = tuple(sum(mu[j] * phi[i][j] for j in range(3)) for i in range(3))
    theta = sum(mu[i] * phi_mu[i] for i in range(3))
    h = tuple(phi_mu[i] - theta for i in range(3))
    canonical = tuple(tuple(phi[i][j] - theta - h[i] - h[j] for j in range(3)) for i in range(3))
    norm = sum(mu[i] * mu[j] * phi[i][j]**2 for i, j in product(range(3), repeat=2))
    h_norm = sum(mu[i] * h[i]**2 for i in range(3))
    H_norm = sum(mu[i] * mu[j] * canonical[i][j]**2 for i, j in product(range(3), repeat=2))
    check(norm == theta**2 + 2 * h_norm + H_norm, "Hoeffding norm decomposition")
    for N in (2, 3, 4):
        expectation, second = F(0), F(0)
        for labels in product(range(3), repeat=N):
            weight = F(1)
            for label in labels:
                weight *= mu[label]
            ordered = sum(phi[labels[i]][labels[j]] for i, j in product(range(N), repeat=2) if i != j)
            statistic = F(1, 2 * N * N) * ordered - F(1, N) * sum(phi_mu[i] for i in labels) + theta / 2
            projected = -theta / (2 * N) - F(1, N * N) * sum(h[i] for i in labels)
            projected += F(1, N * N) * sum(canonical[labels[i]][labels[j]] for i in range(N) for j in range(i + 1, N))
            check(statistic == projected, "exact mean-field centering")
            expectation += weight * statistic
            second += weight * statistic**2
            counts["iid_exact_configurations"] += 1
        target = theta**2 / (4 * N * N) + h_norm / N**3 + F(N - 1, 2 * N**3) * H_norm
        upper = F(N - 1, 2 * N**3) * norm
        check(expectation == -theta / (2 * N), "iid exact bias")
        check(second == target, "iid exact second moment")
        check(second <= upper, "iid sharp upper bound")
        if N == 2 or name == "canonical":
            check(second == upper, "sharp equality case")
        check(F(N - 1, 2 * N * N) <= F(1, 2 * N), "scaled endpoint coefficient")
        counts["iid_law_kernel_cases"] += 1

for M in (F(2), F(3), F(7, 2)):
    haar_kernel_norm_squared = 1 / M**2
    density_kernel_norm_squared = F(1)
    check(density_kernel_norm_squared == M**2 * haar_kernel_norm_squared, "squared density sharpness")
    check(density_kernel_norm_squared > M * haar_kernel_norm_squared, "one density factor counterexample")
    counts["density_factor_sharpness"] += 1

for n in range(13):
    coefficient = F(1, factorial(n))
    integrated = coefficient / (n + 1)
    check(integrated == F(1, factorial(n + 1)), "Volterra simplex integration")
    times = [F(j, n + 2) for j in range(n + 2)]
    check(sum(times[j] - times[j - 1] for j in range(1, len(times))) == times[-1] - times[0], "evolution exponent telescoping")
    counts["volterra_simplex_coefficients"] += 1

result = {
    "task": "TASK-040",
    "status": "PASS",
    "arithmetic": "Exact fractions; Python standard library; no simulation or external dependencies",
    "checks": counts,
    "analytic_limit_status": "Established in the companion proof, not certified by these finite checks",
    "scope": "Frozen THM-023 and conditional THM-024; initial iid only",
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, sort_keys=True))
