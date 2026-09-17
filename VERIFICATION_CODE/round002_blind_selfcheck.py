#!/usr/bin/env python3
"""Exact Gaussian-rational Fourier checks of the independently derived identities.

No third-party libraries. Angular coordinates theta=2*pi*x remove transcendental
constants. Every equality below is exact; these finite checks support, not replace,
the proof in the sealed blind reconstruction.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial
import json


@dataclass(frozen=True)
class QI:
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    @staticmethod
    def coerce(x):
        return x if isinstance(x, QI) else QI(x)

    def __add__(self, y):
        y = self.coerce(y)
        return QI(self.a + y.a, self.b + y.b)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.a, -self.b)

    def __sub__(self, y):
        return self + (-self.coerce(y))

    def __rsub__(self, y):
        return self.coerce(y) - self

    def __mul__(self, y):
        y = self.coerce(y)
        return QI(self.a*y.a - self.b*y.b, self.a*y.b + self.b*y.a)

    __rmul__ = __mul__

    def __truediv__(self, y):
        y = self.coerce(y)
        norm = y.a*y.a + y.b*y.b
        return self * QI(y.a/norm, -y.b/norm)

    def __pow__(self, n):
        if n < 0:
            return (QI(1)/self)**(-n)
        ans = QI(1)
        for _ in range(n):
            ans = ans*self
        return ans

    def conjugate(self):
        return QI(self.a, -self.b)


ZERO = QI()
ONE = QI(1)
II = QI(0, 1)


def addterm(p, e, c):
    e = tuple(e)
    c = QI.coerce(c)
    p[e] = p.get(e, ZERO) + c
    if p[e] == ZERO:
        del p[e]


def plus(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            addterm(out, e, c)
    return out


def scale(p, c):
    return {e: v*c for e, v in p.items() if v*c != ZERO}


def symmetric_monomial(e):
    return {p: ONE for p in set(permutations(e))}


def realify(p):
    out = {}
    for e, c in p.items():
        addterm(out, e, c/F(2))
        addterm(out, tuple(-n for n in e), c.conjugate()/F(2))
    return out


def test_kernel(k, variant=0):
    if variant == 0:
        exps = (2,) + ((-1,) if k > 1 else ()) + (0,)*max(0, k-2)
        return realify(plus(symmetric_monomial(exps),
                           scale(symmetric_monomial((1,)*k), F(1, 2))))
    exps = (-2,) + ((1,) if k > 1 else ()) + (0,)*max(0, k-2)
    return realify(plus(symmetric_monomial(exps),
                       scale(symmetric_monomial((-1,)*k), F(1, 3))))


def subsets(indices):
    indices = tuple(indices)
    for r in range(len(indices)+1):
        yield from combinations(indices, r)


class Model:
    def __init__(self, phases, c):
        self.phases = tuple(phases)
        self.N = len(phases)
        self.q = F(1, self.N)
        self.c = F(c)
        self.nu = F(3, 7)
        # K(theta)=sin(theta)+(1/7)sin(2theta).
        self.K = {1: QI(0, F(-1, 2)), -1: QI(0, F(1, 2)),
                  2: QI(0, F(-1, 14)), -2: QI(0, F(1, 14))}
        # b(theta)=(1/3)sin(theta)+(1/5)cos(2theta).
        self.b = {1: QI(0, F(-1, 6)), -1: QI(0, F(1, 6)),
                  2: QI(F(1, 10)), -2: QI(F(1, 10))}
        self.u = dict(self.b)
        for n, a in self.K.items():
            self.u[n] = self.u.get(n, ZERO) + a*self.moment(-n)
        self.v = []
        for i, z in enumerate(self.phases):
            vel = sum((a*z**n for n, a in self.b.items()), ZERO)
            for j, w in enumerate(self.phases):
                if j != i:
                    vel += self.q*sum((a*(z/w)**n for n, a in self.K.items()), ZERO)
            self.v.append(vel)

    def moment(self, n):
        if n == 0:
            return ONE
        if abs(n) == 1:
            return QI(self.c/2)
        return ZERO

    def moment_dt(self, n):
        return (sum((a*QI(0, n)*self.moment(n+m)
                     for m, a in self.u.items()), ZERO)
                - self.nu*n*n*self.moment(n))

    @lru_cache(None)
    def factorial_monomial(self, e):
        if len(e) > self.N:
            return ZERO
        ans = ZERO
        for ids in permutations(range(self.N), len(e)):
            term = ONE
            for n, i in zip(e, ids):
                term *= self.phases[i]**n
            ans += term
        return self.q**len(e)*ans

    @lru_cache(None)
    def centered_monomial(self, e):
        ans = ZERO
        for A in subsets(range(len(e))):
            aset = set(A)
            term = self.factorial_monomial(tuple(e[a] for a in A))
            for a, n in enumerate(e):
                if a not in aset:
                    term *= -self.moment(n)
            ans += term
        return ans

    def U(self, p):
        return sum((c*self.centered_monomial(tuple(sorted(e)))
                    for e, c in p.items()), ZERO)

    def integrate(self, p, B):
        B = set(B)
        out = {}
        for e, c in p.items():
            for a in B:
                c *= self.moment(e[a])
            addterm(out, tuple(n for a, n in enumerate(e) if a not in B), c)
        return out

    def direct(self, p):
        """Original signed subset sum; microscopic drift and particle gradient."""
        k = len(next(iter(p)))
        drift = ZERO
        gradients = [ZERO]*self.N
        for e, coeff in p.items():
            for A in subsets(range(k)):
                aset = set(A)
                rest = tuple(a for a in range(k) if a not in aset)
                signscale = (-1)**len(rest)*self.q**len(A)*coeff
                mu = ONE
                for a in rest:
                    mu *= self.moment(e[a])
                mudot = ZERO
                for a in rest:
                    term = self.moment_dt(e[a])
                    for b in rest:
                        if b != a:
                            term *= self.moment(e[b])
                    mudot += term
                for ids in permutations(range(self.N), len(A)):
                    value = ONE
                    for a, i in zip(A, ids):
                        value *= self.phases[i]**e[a]
                    local = ZERO
                    for a, i in zip(A, ids):
                        local += QI(0, e[a])*self.v[i] - self.nu*e[a]*e[a]
                        gradients[i] += signscale*mu*value*QI(0, e[a])
                    drift += signscale*value*(mu*local + mudot)
        return drift, gradients

    def reconstructed_drift(self, p):
        k = len(next(iter(p)))
        linear, upward = {}, {}
        for e, coeff in p.items():
            for a in range(k):
                addterm(linear, e, -self.nu*e[a]*e[a]*coeff)
                for n, val in self.u.items():
                    f = list(e)
                    f[a] += n
                    addterm(linear, f, coeff*val*QI(0, e[a]))
                for n, val in self.K.items():
                    # Response: integrate original target y, replace its slot by z.
                    f = list(e)
                    f[a] = -n
                    addterm(linear, f,
                            coeff*val*QI(0, e[a])*self.moment(e[a]+n))
                    f = list(e) + [-n]
                    f[a] += n
                    addterm(upward, f, coeff*val*QI(0, e[a]))
        ans = self.U(linear) + self.U(upward)
        for a in range(k):
            for b in range(k):
                if a == b:
                    continue
                force = {}
                for e, coeff in p.items():
                    for n, val in self.K.items():
                        f = list(e)
                        f[a] += n
                        f[b] -= n
                        addterm(force, f, coeff*val*QI(0, e[a]))
                for B in subsets((a, b)):
                    ans += self.q*self.U(self.integrate(force, B))
        return ans

    def reconstructed_bracket(self, P, Q):
        k, ell = len(next(iter(P))), len(next(iter(Q)))
        ans = ZERO
        for p in range(1, min(k, ell)+1):
            for A in combinations(range(k), p):
                for B in combinations(range(ell), p):
                    for permB in permutations(B):
                        matching = dict(zip(permB, A))
                        unmatched = [b for b in range(ell) if b not in matching]
                        jmap = {b: matching[b] if b in matching
                                else k+unmatched.index(b) for b in range(ell)}
                        for a, b in zip(A, permB):
                            H = {}
                            for e, ce in P.items():
                                for f, cf in Q.items():
                                    exps = list(e) + [0]*len(unmatched)
                                    for j, n in enumerate(f):
                                        exps[jmap[j]] += n
                                    # Differentiate before identification.
                                    addterm(H, exps, -e[a]*f[b]*ce*cf)
                            for D in subsets(A):
                                ans += 2*self.nu*self.q**p*self.U(self.integrate(H, D))
        return ans


def main():
    counts = {"drift_equalities": 0, "bracket_equalities": 0,
              "constant_equalities": 0, "matching_count_equalities": 0,
              "finite_cancellation_equalities": 0}
    models = [Model([ONE, II], 0), Model([ONE, II], F(1, 2)),
              Model([ONE, II, -ONE], F(1, 2)),
              Model([ONE, ONE], F(1, 2))]
    for model in models:
        for k in range(1, 6):
            P = test_kernel(k)
            actual, _ = model.direct(P)
            expected = model.reconstructed_drift(P)
            assert actual == expected, ("drift", model.N, model.c, k, actual, expected)
            counts["drift_equalities"] += 1
            constant = {(0,)*k: ONE}
            actual, grad = model.direct(constant)
            assert actual == ZERO and all(g == ZERO for g in grad)
            assert model.reconstructed_drift(constant) == ZERO
            ck = sum((F((-1)**(k-r)*comb(k, r)*factorial(model.N),
                        factorial(model.N-r)*model.N**r)
                      for r in range(min(k, model.N)+1)), F(0))
            assert model.U(constant) == QI(ck)
            counts["constant_equalities"] += 1
        for k in range(1, 5):
            for ell in range(1, 5):
                P, Q = test_kernel(k), test_kernel(ell, 1)
                _, gradP = model.direct(P)
                _, gradQ = model.direct(Q)
                actual = 2*model.nu*sum((a*b for a, b in zip(gradP, gradQ)), ZERO)
                expected = model.reconstructed_bracket(P, Q)
                assert actual == expected, ("bracket", model.N, model.c, k, ell,
                                           actual, expected)
                counts["bracket_equalities"] += 1
    for k in range(1, 9):
        for ell in range(1, 9):
            for p in range(1, min(k, ell)+1):
                assert p*comb(k, p)*comb(ell, p)*factorial(p) == (
                    k*ell*comb(k-1, p-1)*comb(ell-1, p-1)*factorial(p-1))
                counts["matching_count_equalities"] += 1
    for m in range(8):
        for S in subsets(range(m)):
            for A in subsets(range(m)):
                free = set(S)-set(A)
                coefficient = sum((-1)**len(B) for B in subsets(free))
                assert coefficient == (1 if not free else 0)
                counts["finite_cancellation_equalities"] += 1
    print(json.dumps({"status": "PASS", "arithmetic": "exact Gaussian rationals",
                      "randomness": "none", "counts": counts,
                      "N": [2, 3], "drift_orders": [1, 2, 3, 4, 5],
                      "bracket_orders": [1, 2, 3, 4],
                      "includes_k_greater_than_N": True,
                      "includes_coincident_coordinates_with_distinct_labels": True,
                      "nu_theta": "3/7", "mu": ["1", "1+(1/2)cos(theta)"],
                      "K_theta": "sin(theta)+(1/7)sin(2theta)",
                      "b_theta": "(1/3)sin(theta)+(1/5)cos(2theta)"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
