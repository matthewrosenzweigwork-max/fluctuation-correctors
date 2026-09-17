#!/usr/bin/env python3
"""Exact rational self-checks for the Round 001 smooth pair memorandum.

All operator coefficients below are divided by pi**2. The model is the
one-dimensional unit torus, mu=1, b=0, g(x)=a*cos(2*pi*x). This is a
finite Fourier coefficient check, not an independent theorem certificate.
Only the Python standard library is used; there is no random input.
"""

from fractions import Fraction
from typing import Dict, Tuple


Mode = Tuple[int, int]
Polynomial = Dict[Mode, Fraction]


def add_term(poly: Polynomial, mode: Mode, value: Fraction) -> None:
    poly[mode] = poly.get(mode, Fraction(0)) + value
    if not poly[mode]:
        del poly[mode]


def scale(poly: Polynomial, factor: Fraction) -> Polynomial:
    return {mode: value * factor for mode, value in poly.items() if value * factor}


def add(*polys: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for poly in polys:
        for mode, value in poly.items():
            add_term(result, mode, value)
    return result


def cosine(p: int, q: int) -> Polynomial:
    return add({(p, q): Fraction(1, 2)}, {(-p, -q): Fraction(1, 2)})


def pair_operator(poly: Polynomial, a: Fraction, nu: Fraction, n: int) -> Polynomial:
    """Return (L_2+B/N)poly, divided by pi**2, by Fourier multiplication."""
    assert n >= 2 and nu >= 0
    result: Polynomial = {}
    for (p, q), value in poly.items():
        heat = -4 * nu * (p * p + q * q)
        response = -2 * a * (int(abs(p) == 1) + int(abs(q) == 1))
        add_term(result, (p, q), value * (heat + response))
        interaction = Fraction(2, n) * a * (p - q)
        add_term(result, (p + 1, q - 1), value * interaction)
        add_term(result, (p - 1, q + 1), -value * interaction)
    return result


def main() -> None:
    n_values = (2, 3, 17)
    a_values = (Fraction(-2), Fraction(0), Fraction(3, 2))
    nu_values = (Fraction(0), Fraction(1, 3), Fraction(1), Fraction(7))
    checks = 0
    for n in n_values:
        for nu in nu_values:
            heat_mode = cosine(2, 3)
            assert pair_operator(heat_mode, Fraction(0), nu, n) == scale(
                heat_mode, -52 * nu
            )
            checks += 1
            for a in a_values:
                sum_mode = cosine(1, 1)
                assert pair_operator(sum_mode, a, nu, n) == scale(
                    sum_mode, -(8 * nu + 4 * a)
                )
                checks += 1

                h1, h2, h3 = (cosine(k, -k) for k in (1, 2, 3))
                expected = add(
                    scale(h2, -32 * nu),
                    scale(h3, Fraction(8, n) * a),
                    scale(h1, -Fraction(8, n) * a),
                )
                assert pair_operator(h2, a, nu, n) == expected
                checks += 1

                # For Phi(t)=(T-t)H_2 and F=H_2-(T-t)G H_2,
                # the coefficients of both 1 and T-t in d_t Phi+G Phi+F vanish.
                assert add(scale(h2, Fraction(-1)), h2) == {}
                assert add(pair_operator(h2, a, nu, n), scale(expected, Fraction(-1))) == {}
                checks += 1

    print(f"PASS: {checks} exact rational Fourier identities; N=2,3,17; nu=0,1/3,1,7.")
    print("PASS: heat mode, full symmetric sum mode, and forced difference-mode solution.")
    print("Status: REPRODUCED / SELF_CHECKED; no floating-point tolerance and no random seed.")


if __name__ == "__main__":
    main()
