#!/usr/bin/env python3
"""Exact Fourier diagnostics for TASK-011; Python standard library only.

Angles are theta_i=2*pi*x_i. All derivatives below are in theta; restore
q=2*pi by multiplying brackets and generators by q^2. The interacting
generator corresponds to g(x)=a*cos(2*pi*x), K=a*q*sin(2*pi*x).
No sampling, floating point, symbolic package, or constructor code is used.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, a):
    a = Q(a)
    return {k: a*v for k, v in p.items() if a*v}


def mul(p, q):
    out = {}
    for k, a in p.items():
        for l, b in q.items():
            m = tuple(x+y for x, y in zip(k, l))
            out[m] = out.get(m, Q(0)) + a*b
    return {k: v for k, v in out.items() if v}


def conj(p):
    return {tuple(-x for x in k): v for k, v in p.items()}


def const(N, c=1):
    return {(0,)*N: Q(c)} if c else {}


def mon(N, i, k):
    v = [0]*N
    v[i] = k
    return {tuple(v): Q(1)}


def z(N, k):
    return scale(add(*(mon(N, i, k) for i in range(N))), Q(1, N))


def cosmean(N):
    return scale(add(z(N, 1), z(N, -1)), Q(1, 2))


def mean(p, m=Q(0)):
    """Product law with mu(e_0)=1, mu(e_1)=mu(e_-1)=m."""
    value = Q(0)
    for k, a in p.items():
        for n in k:
            a *= Q(1) if n == 0 else m if abs(n) == 1 else Q(0)
        value += a
    return value


def gradprod(p, q):
    """Sum_i (partial_theta_i p)(partial_theta_i q), exactly."""
    out = {}
    for k, a in p.items():
        for l, b in q.items():
            coeff = -sum(x*y for x, y in zip(k, l))*a*b
            m = tuple(x+y for x, y in zip(k, l))
            out[m] = out.get(m, Q(0)) + coeff
    return {k: v for k, v in out.items() if v}


def generator(p, a, nu):
    """The interacting generator divided by (2*pi)^2."""
    N = len(next(iter(p))) if p else 0
    out = {}
    for k, value in p.items():
        out[k] = out.get(k, Q(0)) - nu*sum(n*n for n in k)*value
        for i in range(N):
            for j in range(N):
                if i == j or not k[i]:
                    continue
                c = a*k[i]*value/(2*N)
                plus, minus = list(k), list(k)
                plus[i] += 1
                plus[j] -= 1
                minus[i] -= 1
                minus[j] += 1
                plus, minus = tuple(plus), tuple(minus)
                out[plus] = out.get(plus, Q(0)) + c
                out[minus] = out.get(minus, Q(0)) - c
    return {k: v for k, v in out.items() if v}


def dstat(N, k):
    """Ordered distinct-label statistic for e_1 tensor power k."""
    out = {}
    for inds in permutations(range(N), k):
        key = [0]*N
        for i in inds:
            key[i] += 1
        out[tuple(key)] = out.get(tuple(key), Q(0)) + Q(1, N**k)
    return out


def equal(p, q):
    assert p == q, (p, q)


checks = 0
for N in (2, 3, 4, 6):
    Z, Z2, Z3 = z(N, 1), z(N, 2), z(N, 3)
    U2 = add(mul(Z, Z), scale(Z2, -Q(1, N)))
    U3 = add(mul(mul(Z, Z), Z), scale(mul(Z, Z2), -Q(3, N)),
             scale(Z3, Q(2, N*N)))
    equal(U2, dstat(N, 2))
    equal(U3, dstat(N, 3))
    assert mean(mul(U2, conj(U2))) == Q(2*N*(N-1), N**4)
    assert mean(mul(U3, conj(U3))) == Q(6*N*(N-1)*(N-2), N**6)
    P = scale(U2, Q(1, 2))
    assert mean(gradprod(P, conj(P))) == Q(N-1, N**3)
    Qdiff = add(mul(Z, conj(Z)), const(N, -Q(1, N)))
    equal(gradprod(Z2, conj(P)), scale(Qdiff, Q(2, N)))
    assert mean(mul(Qdiff, Qdiff)) == Q(N-1, N**3)
    for k in (2, 3):
        bias = sum((-1)**(k-r)*Q(factorial(k), factorial(r)*factorial(k-r))
                   * Q(factorial(N), factorial(N-r)*N**r)
                   for r in range(min(k, N)+1))
        assert bias == (-Q(1, N) if k == 2 else Q(2, N*N))
    checks += 9

    for m in (Q(1, 4), Q(1, 8)):
        rho = add(Z, const(N, -m))
        V2 = add(mul(rho, rho), scale(Z2, -Q(1, N)))
        V3 = add(mul(mul(rho, rho), rho),
                 scale(mul(Z2, rho), -Q(3, N)), scale(Z3, Q(2, N*N)))
        direct = add(dstat(N, 3), scale(dstat(N, 2), -3*m),
                     scale(Z, 3*m*m), const(N, -m**3))
        equal(V3, direct)
        assert mean(V2, m) == -m*m/N
        assert mean(V3, m) == 2*m**3/(N*N)

        C = cosmean(N)
        rhoC = add(C, const(N, -m))
        etaC2 = add(const(N, Q(1, 2)),
                    scale(add(z(N, 2), z(N, -2)), Q(1, 4)))
        PC = scale(add(mul(rhoC, rhoC), scale(etaC2, -Q(1, N))), Q(1, 2))
        pair = ((N-1)*(Q(1, 2)-m*m)+m*m)/(2*N**3)
        assert mean(gradprod(PC, PC), m) == pair
        assert mean(gradprod(C, PC), m) == -m/(2*N*N)
        checks += 5

    # Nonzero smooth interaction: instantaneous correlation creation.
    for a in (Q(-1), Q(1, 2)):
        for nu in (Q(0), Q(1, 3), Q(3)):
            assert mean(generator(Qdiff, a, nu)) == -a*(N-1)/(N*N)
            checks += 1

    # J for terminal cos(theta), after removing a*(2*pi)^2.
    # Exact P[J] is (a*q^2/2) Re(Z_2 conjugate Z_1).
    R = scale(add(mul(Z2, conj(Z)), mul(conj(Z2), Z)), Q(1, 2))
    PJ = scale(R, Q(1, 2))
    assert mean(PJ) == 0
    assert mean(mul(PJ, PJ)) == Q(1, 8*N*N)
    assert mean(gradprod(PJ, PJ)) == Q(5*N-4, 8*N**3)
    assert mean(gradprod(cosmean(N), PJ)) == Q(1, 4*N*N)
    checks += 4

print(f"PASS: {checks} exact rational checks")
print("Free heat: deleted U2/U3, constant biases, moments, pair and cross brackets.")
print("Moving iid background: nonzero biases, pair bracket, signed cross bracket.")
print("Nonzero interaction: correlation creation and actual source J diagnostics.")
print("Evidence: exact finite tests; no numerical sampling; not a universal proof.")
