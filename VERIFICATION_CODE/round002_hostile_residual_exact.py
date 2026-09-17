#!/usr/bin/env python3
"""Independent exact Laurent-polynomial audit of the sealed residual dossier.

The angular frequency is one; physical 2*pi|k| factors are restored analytically.
All coefficients are rational. Differentiation contributes i*exponent, so a
bilinear Brownian bracket contributes minus the product of exponent factors.
No constructor verification code is imported.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json


def put(out, exponent, value):
    exponent = tuple(exponent)
    out[exponent] = out.get(exponent, F(0)) + value
    if out[exponent] == 0:
        del out[exponent]


def multiply(P, Q):
    out = {}
    for e, a in P.items():
        for f, b in Q.items():
            put(out, (x+y for x, y in zip(e, f)), a*b)
    return out


def conjugate(P):
    return {tuple(-x for x in e): a for e, a in P.items()}


def moment(n, m):
    return F(1) if n == 0 else (m if abs(n) == 1 else F(0))


def mean(P, m=F(0)):
    out = F(0)
    for e, a in P.items():
        for n in e:
            a *= moment(n, m)
        out += a
    return out


def U(N, kernel, m=F(0)):
    """Direct original deleted-label definition, as a particle polynomial."""
    k = len(next(iter(kernel)))
    out = {}
    for occupied_count in range(k+1):
        for A in combinations(range(k), occupied_count):
            rest = [a for a in range(k) if a not in A]
            for labels in permutations(range(N), occupied_count):
                for modes, coefficient in kernel.items():
                    coefficient *= F((-1)**len(rest), N**occupied_count)
                    for a in rest:
                        coefficient *= moment(modes[a], m)
                    e = [0]*N
                    for a, label in zip(A, labels):
                        e[label] += modes[a]
                    put(out, e, coefficient)
    return out


def scaled(P, c):
    return {e: a*c for e, a in P.items() if a*c}


def bracket(P, Q, N, nu):
    out = {}
    for i in range(N):
        for e, a in P.items():
            for f, b in Q.items():
                put(out, (x+y for x, y in zip(e, f)),
                    -2*nu*e[i]*f[i]*a*b)
    return out


def generator(P, N, amplitude, nu):
    out = {}
    for e, coefficient in P.items():
        put(out, e, -nu*sum(n*n for n in e)*coefficient)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                for sign in (-1, 1):
                    mode = list(e)
                    mode[i] += sign
                    mode[j] -= sign
                    put(out, mode,
                        sign*amplitude*e[i]*coefficient/F(2*N))
    return out


def source_kernel(amplitude):
    out = {}
    for pair, sign in [((1, -2), 1), ((2, -1), 1), ((1, 0), -1), ((0, 1), -1)]:
        for direction in (-1, 1):
            put(out, (direction*x for x in pair), sign*amplitude/F(4))
    return out


def main():
    counts = {"constants_and_iid_biases": 0, "free_complex_moments": 0,
              "moving_background_brackets": 0,
              "interacting_source_and_correlation": 0,
              "temperature_equalities": 0}
    cos = {(1,): F(1, 2), (-1,): F(1, 2)}
    cos_pair = {e: F(1, 4) for e in product((-1, 1), repeat=2)}
    difference_cos = {(1, -1): F(1, 2), (-1, 1): F(1, 2)}
    for N in (2, 3, 4, 6):
        for m in (F(0), F(1, 4), F(1, 8)):
            assert mean(U(N, {(0, 0): F(1)}, m), m) == -F(1, N)
            assert mean(U(N, {(0, 0, 0): F(1)}, m), m) == F(2, N*N)
            assert mean(U(N, {(1, 1): F(1)}, m), m) == -m*m/N
            assert mean(U(N, {(1, 1, 1): F(1)}, m), m) == 2*m*m*m/(N*N)
            counts["constants_and_iid_biases"] += 4
        pair = scaled(U(N, {(1, 1): F(1)}), F(1, 2))
        triple = U(N, {(1, 1, 1): F(1)})
        assert mean(multiply(pair, conjugate(pair))) == F(N-1, 2*N**3)
        assert mean(multiply(triple, conjugate(triple))) == F(6*N*(N-1)*(N-2), N**6)
        assert mean(bracket(pair, conjugate(pair), N, F(1))) == F(2*(N-1), N**3)
        counts["free_complex_moments"] += 3
        for m in (F(1, 4), F(1, 8)):
            real_pair = scaled(U(N, cos_pair, m), F(1, 2))
            one = U(N, cos, m)
            for nu in (F(1, 3), F(3)):
                expected = nu*((N-1)*(F(1, 2)-m*m)+m*m)/N**3
                assert mean(bracket(real_pair, real_pair, N, nu), m) == expected
                assert mean(bracket(one, real_pair, N, nu), m) == -nu*m/N**2
                counts["moving_background_brackets"] += 2
        for amplitude in (F(-1), F(1, 2)):
            pair = scaled(U(N, source_kernel(amplitude)), F(1, 2))
            one = U(N, cos)
            Q = U(N, difference_cos)
            assert mean(pair) == 0
            assert mean(multiply(pair, pair)) == amplitude*amplitude/(8*N*N)
            assert mean(Q) == 0
            assert mean(multiply(Q, Q)) == F(N-1, N**3)
            counts["interacting_source_and_correlation"] += 4
            for nu in (F(0), F(1, 3), F(3)):
                assert mean(generator(Q, N, amplitude, nu)) == -amplitude*(N-1)/N**2
                assert mean(bracket(pair, pair, N, nu)) == (
                    nu*amplitude*amplitude*(5*N-4)/(4*N**3))
                assert mean(bracket(one, pair, N, nu)) == nu*amplitude/(2*N*N)
                counts["interacting_source_and_correlation"] += 3
        for beta in (F(1, 9), F(1), F(9)):
            sigma2 = N*min(beta, F(1))
            assert sigma2/(beta*N*N) == min(F(1), 1/beta)/N
            counts["temperature_equalities"] += 1
    print(json.dumps({"status": "PASS", "arithmetic": "exact rational Laurent polynomials",
                      "frequency_convention": "angular frequency one; physical powers checked analytically",
                      "counts": counts, "total": sum(counts.values()),
                      "N": [2, 3, 4, 6], "randomness": "none",
                      "nu_zero": "algebraic diagnostic only"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
