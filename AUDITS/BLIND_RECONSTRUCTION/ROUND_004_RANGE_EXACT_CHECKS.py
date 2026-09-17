#!/usr/bin/env python3
"""Exact Fraction checks of THM022 local Taylor coefficients; no simulation.

Laurent exponents are rational. Differentiation, multiplication and the radial
Laplacian are implemented directly, separately from the closed-form identities
asserted by the reconstruction. Values at r=1 are exact. Boundary estimates are
proved analytically in the report and are not inferred from this script.
"""
from fractions import Fraction as Q
from math import factorial
import json


def clean(f):
    return {e: c for e, c in f.items() if c}


def add(*fs):
    ans = {}
    for f in fs:
        for e, c in f.items():
            ans[e] = ans.get(e, Q(0)) + c
    return clean(ans)


def scale(f, c):
    return clean({e: c*v for e, v in f.items()})


def shift(f, e):
    return clean({q+e: c for q, c in f.items()})


def deriv(f):
    return clean({e-1: c*e for e, c in f.items()})


def generator(f, d, s, N, nu):
    df = deriv(f)
    lap = add(deriv(df), scale(shift(df, Q(-1)), d-1))
    drift = scale(shift(df, -s-1), 2*s/N)
    return add(scale(lap, 2*nu), drift)


def at_one(f):
    return sum(f.values(), Q(0))


def binomial(alpha, k):
    ans = Q(1)
    for m in range(k):
        ans *= (alpha-m)/(m+1)
    return ans


def f_coefficient(s, N, k):
    alpha = 2/(s+2)
    return N/Q(4)*binomial(alpha, k)*(2*s*(s+2)/N)**k


def text(q):
    return str(q)


def check_row(d, s, N, nu, expected_sign):
    s, N, nu = Q(s), Q(N), Q(nu)
    j = {-s: s}
    # A separate backward-Itô residual route uses y=1+x and Delta F=N*G(x)/2.
    p = s+2
    beta = 2*(s+1)/p
    G = {-s/p: s+d, -beta: -s, Q(0): Q(-d)}
    expected_derivative = add({-beta-1: 2*s*(s+1)/p},
                              {-beta: -s*(s+d)/p})
    assert deriv(G) == expected_derivative
    assert at_one(G) == 0
    assert at_one(deriv(G)) == s*(s+2-d)/p
    assert N/2*(2*s*p/N)*at_one(deriv(G)) == s*s*(s+2-d)
    Lj = generator(j, d, s, N, nu)
    L2j = generator(Lj, d, s, N, nu)
    formula_Lj = clean({-s-2: 2*nu*s*s*(s+2-d), -2*s-2: -2*s**3/N})
    assert Lj == formula_Lj, (Lj, formula_Lj)
    formula_L2j = add(
        {-s-4: 4*nu**2*s**2*(s+2-d)*(s+2)*(s+4-d)},
        {-2*s-4: -4*nu*s**3/N*((s+2-d)*(s+2)+(2*s+2)*(2*s+4-d))},
        {-3*s-4: 8*s**4*(s+1)/N**2},
    )
    assert L2j == formula_L2j, (L2j, formula_L2j)
    coeff = [at_one(j), at_one(Lj)/2, at_one(L2j)/6]
    F = [f_coefficient(s, N, k) for k in (1, 2, 3)]
    assert F[0] == s
    assert F[1] == -s**3/N
    assert F[2] == Q(4, 3)*s**4*(s+1)/N**2
    gap2 = coeff[1]-F[1]
    gap3 = coeff[2]-F[2]
    assert gap2 == nu*s*s*(s+2-d)
    actual_sign = (gap2 > 0) - (gap2 < 0)
    assert actual_sign == expected_sign
    if s == d-2 and nu > 0:
        assert gap3 == -Q(4, 3)*nu*s**3*(s+1)*(s+2)/N
        assert gap3 < 0
    if nu == 0:
        state = j
        for k in range(1, 9):
            assert at_one(state)/factorial(k) == f_coefficient(s, N, k)
            state = generator(state, d, s, N, nu)
    return {'d': d, 's': text(s), 'N': text(N), 'nu': text(nu),
            'quadratic_gap_at_r1': text(gap2), 'cubic_gap_at_r1': text(gap3),
            'expected_quadratic_sign': expected_sign, 'status': 'PASS'}


def sample_annulus_check():
    # Integer s and rational geometry make every constant and inequality exact.
    d, s, N, nu = 3, Q(2), Q(2), Q(1)
    a, r0, R = Q(1, 2), Q(1), Q(2)
    delta = min(r0-a, R-r0)
    drift_bound = 2*s/(N*a**int(s+1))
    c = delta**2/(32*nu*d)
    kappa = nu*s*s*(s+2-d)*r0**int(-s-2)
    J = s*a**int(-s)
    Ad = 2*nu*s*s*(s+2-d)
    Bd = 2*s**3/N
    M1 = Ad*a**int(-s-2) + Bd*a**int(-2*s-2)
    M2 = (Ad*(2*nu*(s+2)*(s+4-d)*a**int(-s-4)
              +2*s*(s+2)/N*a**int(-2*s-4))
          +Bd*(2*nu*(2*s+2)*(2*s+4-d)*a**int(-2*s-4)
              +2*s*(2*s+2)/N*a**int(-3*s-4)))
    H = 8*s**4*(s+1)/N**2*r0**int(-3*s-4)
    C = (M2+H)/6
    t = Q(1)
    while not (t <= delta/(2*drift_bound)
               and C*t <= kappa/4
               and 12*d*J*t*t/c**3 <= kappa/4
               and 6*d*M1*t**3/c**3 <= kappa/4):
        t /= 2
    assert M2 == 249856 and H == 96 and kappa == 4
    return {'d': d, 's': text(s), 'N': text(N), 'nu': text(nu),
            'a': text(a), 'r0': text(r0), 'R': text(R),
            'explicit_time_valid_for_all_smaller_positive_times': text(t),
            'quadratic_gap_lower_bound_coefficient': text(kappa/4),
            'constants': {k: text(v) for k, v in
                          [('drift_bound', drift_bound), ('c', c), ('J', J),
                           ('M1', M1), ('M2', M2), ('H', H), ('C', C)]},
            'status': 'PASS'}


def main():
    admitted = []
    for d, s in [(1, Q(1, 2)), (2, Q(1, 2)), (2, Q(3, 2)),
                 (3, Q(3, 2)), (3, Q(2)), (4, Q(5, 2)),
                 (4, Q(3)), (5, Q(7, 2)), (8, Q(13, 2))]:
        assert 0 < s < d and s > d-2
        for N in (2, 3, 11):
            for nu in (Q(1, 4), Q(1), Q(7, 3)):
                admitted.append(check_row(d, s, N, nu, 1))
    excluded = [check_row(3, Q(1, 2), 2, 1, -1),
                check_row(4, Q(1), 3, Q(1, 4), -1),
                check_row(3, Q(1), 2, 1, 0),
                check_row(4, Q(2), 3, Q(1, 4), 0),
                check_row(3, Q(3, 2), 2, 0, 0)]
    result = {'method': 'Python standard-library Fraction exact arithmetic',
              'scope': 'algebraic coefficient checks, not a stochastic proof',
              'admitted_rows': len(admitted), 'excluded_diagnostic_rows': len(excluded),
              'failed_tests': [], 'status': 'PASS',
              'finite_annulus_constant_check': sample_annulus_check(),
              'admitted_cases': admitted, 'excluded_diagnostics': excluded}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
