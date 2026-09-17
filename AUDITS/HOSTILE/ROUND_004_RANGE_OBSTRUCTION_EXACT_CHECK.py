#!/usr/bin/env python3
"""Exact finite checks for TASK037; standard library only, no simulation.

The continuum proof is in the hostile report.  These rational cases are a
separate falsification battery, including exact transport remainders that
detect the factor missing from the preserved V1 submission.
"""

from fractions import Fraction as Q
import json


def falling(value, order):
    product = Q(1)
    for index in range(order):
        product *= value - index
    return product


def main():
    exponent_rows = [
        (1, Q(1, 4)), (1, Q(1, 2)), (1, Q(9, 10)),
        (2, Q(1, 4)), (2, Q(1)), (2, Q(3, 2)), (2, Q(199, 100)),
        (3, Q(1, 2)), (3, Q(1)), (3, Q(101, 100)),
        (3, Q(3, 2)), (3, Q(2)), (3, Q(299, 100)),
        (4, Q(1)), (4, Q(2)), (4, Q(201, 100)),
        (4, Q(3)), (4, Q(399, 100)),
        (5, Q(3)), (5, Q(31, 10)), (5, Q(4)), (5, Q(499, 100)),
        (6, Q(4)), (6, Q(401, 100)), (6, Q(5)), (6, Q(599, 100)),
    ]
    derivative_checks = 0
    time_checks = 0
    sign_counts = {"above": 0, "threshold": 0, "below": 0}
    for dimension, s in exponent_rows:
        assert 0 < s < dimension
        p = s + 2
        source_laplacian = s * (-s) * (-s + dimension - 2)
        claimed_laplacian = s**2 * (s + 2 - dimension)
        assert source_laplacian == claimed_laplacian
        sign = "above" if s > dimension - 2 else (
            "threshold" if s == dimension - 2 else "below"
        )
        sign_counts[sign] += 1
        assert (source_laplacian > 0) == (sign == "above")
        assert (source_laplacian == 0) == (sign == "threshold")
        for particles in (2, 3, 97):
            speed = 2 * s * p / particles
            outer_power = 2 / p
            independently_differentiated = [
                Q(particles, 4) * falling(outer_power, order) * speed**order
                for order in (1, 2, 3)
            ]
            submitted = [
                s,
                -2 * s**3 / particles,
                4 * s**4 * (2*s + 2) / particles**2,
            ]
            assert independently_differentiated == submitted
            derivative_checks += 3
            assert (2*s / particles) * (-s*s) == submitted[1]
            for nu in (Q(1, 100), Q(1), Q(7, 2)):
                assert nu * source_laplacian == (
                    2*nu*source_laplacian + submitted[1] - submitted[1]
                ) / 2
                if sign != "above":
                    continue
                c = nu * source_laplacian  # r0=1
                cf = submitted[2]
                for bound_b in (Q(0), Q(1, 7), Q(5), Q(10**6)):
                    total_bound = bound_b + cf
                    tau0 = min(Q(1), 3*c/(total_bound + 1))
                    assert tau0 > 0
                    for fraction in (Q(1, 100), Q(1, 2), Q(999, 1000), Q(1)):
                        tau = fraction * tau0
                        lower = c*tau**2 - total_bound*tau**3/6
                        assert lower >= c*tau**2/2 > 0
                        time_checks += 1

    remainder_rows = []
    v1_underbounds = 0
    for s in (Q(1, 4), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3), Q(4)):
        p = s + 2
        power = 2/p
        for particles in (2, 3, 97):
            speed = 2*s*p/particles
            for delta in (Q(1, 1000), Q(1, 10000), Q(1, 100000)):
                # At r0=1, choose A=(1+delta)^denominator(power).
                # Its power-th power is the exact rational below.
                base = 1 + delta
                shifted_radius = base**power.denominator
                tau = (shifted_radius - 1)/speed
                assert 0 < tau <= 1
                exact_f = Q(particles, 4) * (base**power.numerator - 1)
                second_derivative = -2*s**3/particles
                remainder = exact_f - s*tau - second_derivative*tau**2/2
                cf_v2 = 4*s**4*(2*s+2)/particles**2
                cf_v1 = 4*s**3*(2*s+2)/particles**2
                assert 0 <= remainder <= cf_v2*tau**3/6
                v1_fails = remainder > cf_v1*tau**3/6
                assert v1_fails == (s > 1)
                v1_underbounds += int(v1_fails)
                remainder_rows.append({
                    "s": str(s), "N": particles, "delta": str(delta),
                    "tau": str(tau), "v2_bound_pass": True,
                    "v1_bound_fails": v1_fails,
                })

    print(json.dumps({
        "evidence": "EXACT-RATIONAL-FINITE-TESTS; not a proof of all parameters",
        "arithmetic": "Python standard-library Fraction; no floats, no random seed",
        "radius_for_time_and_remainder_cases": "r0=1",
        "source_exponent_rows": len(exponent_rows),
        "range_sign_counts": sign_counts,
        "exact_transport_derivative_comparisons": derivative_checks,
        "explicit_positive_time_checks": time_checks,
        "exact_transport_remainder_cases": len(remainder_rows),
        "preserved_v1_actual_remainder_underbounds": v1_underbounds,
        "all_v2_checks_pass": True,
        "remainder_cases": remainder_rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
