#!/usr/bin/env python3
"""Exact, standard-library coefficient checks for the Round 001 recursion.

The direct side differentiates the complete particle-coordinate Laurent
polynomial.  The proposed side applies the stated hierarchy to kernel Laurent
polynomials.  Arithmetic is Q(i); equality means equality of every coefficient.
This is discovery/self-check code, not an independent audit certificate.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial


@dataclass(frozen=True)
class QI:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def of(value):
        return value if isinstance(value, QI) else QI(F(value))

    def __add__(self, other):
        other = QI.of(other)
        return QI(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-QI.of(other))

    def __mul__(self, other):
        other = QI.of(other)
        return QI(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.re or self.im)


ZERO = QI()
ONE = QI(F(1))
I = QI(F(0), F(1))


class Poly:
    """Sparse Laurent polynomial in exp(i theta_1),...,exp(i theta_n)."""

    def __init__(self, n, terms=None):
        self.n = n
        self.terms = {key: QI.of(value) for key, value in (terms or {}).items()
                      if value}
        assert all(len(key) == n for key in self.terms)

    @classmethod
    def monomial(cls, powers, coefficient=1):
        return cls(len(powers), {tuple(powers): QI.of(coefficient)})

    def __add__(self, other):
        assert self.n == other.n
        result = defaultdict(lambda: ZERO, self.terms)
        for powers, value in other.terms.items():
            result[powers] += value
        return Poly(self.n, result)

    def scale(self, value):
        value = QI.of(value)
        return Poly(self.n, {powers: value * coefficient
                             for powers, coefficient in self.terms.items()})

    def __sub__(self, other):
        return self + other.scale(-1)

    def __mul__(self, other):
        assert self.n == other.n
        result = defaultdict(lambda: ZERO)
        for p, c in self.terms.items():
            for q, d in other.terms.items():
                result[tuple(a + b for a, b in zip(p, q))] += c * d
        return Poly(self.n, result)

    def derivative(self, slot):
        return Poly(self.n, {p: c * I * p[slot] for p, c in self.terms.items()})

    def lift(self, n, slots):
        assert len(slots) == self.n
        result = defaultdict(lambda: ZERO)
        for powers, coefficient in self.terms.items():
            target = [0] * n
            for slot, power in zip(slots, powers):
                target[slot] += power
            result[tuple(target)] += coefficient
        return Poly(n, result)

    def integrate(self, slot, moment):
        result = defaultdict(lambda: ZERO)
        for p, c in self.terms.items():
            result[p[:slot] + p[slot + 1:]] += c * moment(p[slot])
        return Poly(self.n - 1, result)

    def symmetric(self):
        result = Poly(self.n)
        for perm in permutations(range(self.n)):
            result += self.lift(self.n, perm)
        return result.scale(F(1, factorial(self.n)))


def psum(n, values):
    result = Poly(n)
    for value in values:
        result += value
    return result


def subsets(items):
    items = tuple(items)
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def moment(power):
    # Positive density 1 + cos(theta)/3 + sin(2 theta)/5, against dtheta/(2pi).
    return {0: ONE, 1: QI(F(1, 6)), -1: QI(F(1, 6)),
            2: I * F(1, 10), -2: I * F(-1, 10)}.get(power, ZERO)


def sine(n, a, b=None, frequency=1):
    p = [0] * n
    p[a] = frequency
    if b is not None:
        p[b] = -frequency
    return (Poly.monomial(p, -I * F(1, 2))
            + Poly.monomial([-x for x in p], I * F(1, 2)))


def confining(n, a):
    return sine(n, a, frequency=2)


def q_field(n, a, interaction=True):
    if not interaction:
        return Poly(n)
    return sine(2, 0, 1).integrate(1, moment).lift(n, [a])


def mean_moment_dt(power, nu, interaction=True):
    f = Poly.monomial((power,))
    u = confining(1, 0) + q_field(1, 0, interaction)
    applied = u * f.derivative(0) + f.derivative(0).derivative(0).scale(nu)
    return sum((c * moment(p[0]) for p, c in applied.terms.items()), ZERO)


def raw_statistic(phi, n_particles, active, derivative_mu_slot=None):
    """D_A mu^(S minus A) applied to phi, optionally differentiating one mu."""
    active = tuple(active)
    inactive = tuple(a for a in range(phi.n) if a not in active)
    result = defaultdict(lambda: ZERO)
    for labels in permutations(range(n_particles), len(active)):
        for powers, coefficient in phi.terms.items():
            target = [0] * n_particles
            for slot, label in zip(active, labels):
                target[label] += powers[slot]
            for slot in inactive:
                measure = derivative_mu_slot[1] if derivative_mu_slot and slot == derivative_mu_slot[0] else moment
                coefficient *= measure(powers[slot])
            result[tuple(target)] += coefficient * F(1, n_particles ** len(active))
    return Poly(n_particles, result)


def U(phi, n_particles):
    return psum(n_particles,
                (raw_statistic(phi, n_particles, active)
                 .scale((-1) ** (phi.n - len(active)))
                 for active in subsets(range(phi.n))))


def U_background_dt(phi, n_particles, nu, interaction=True):
    result = Poly(n_particles)
    dm = lambda power: mean_moment_dt(power, nu, interaction)
    for active in subsets(range(phi.n)):
        for slot in range(phi.n):
            if slot not in active:
                result += raw_statistic(phi, n_particles, active, (slot, dm)).scale(
                    (-1) ** (phi.n - len(active)))
    return result


def particle_generator(poly, nu, interaction=True):
    """Direct differentiation AFTER constructing a polynomial in N particles."""
    n = poly.n
    result = Poly(n)
    for a in range(n):
        force = confining(n, a)
        if interaction:
            force += psum(n, (sine(n, a, b) for b in range(n) if a != b)).scale(F(1, n))
        result += force * poly.derivative(a)
        result += poly.derivative(a).derivative(a).scale(nu)
    return result


def L(phi, nu, interaction=True):
    k = phi.n
    result = Poly(k)
    for a in range(k):
        result += (confining(k, a) + q_field(k, a, interaction)) * phi.derivative(a)
        result += phi.derivative(a).derivative(a).scale(nu)
        if interaction:
            slots = list(range(k))
            slots[a] = k
            response = sine(k + 1, k, a) * phi.derivative(a).lift(k + 1, slots)
            result += response.integrate(k, moment)
    return result


def pair_action(phi, a, b):
    return sine(phi.n, a, b) * (phi.derivative(a) - phi.derivative(b))


def C(phi):
    return psum(phi.n, (pair_action(phi, a, b) for a, b in combinations(range(phi.n), 2)))


def Q(phi):
    k = phi.n
    return psum(k, (pair_action(phi, a, k - 1) for a in range(k - 1))).integrate(k - 1, moment)


def R(phi):
    k = phi.n
    return pair_action(phi, k - 2, k - 1).integrate(k - 1, moment).integrate(k - 2, moment)


def upward(phi):
    k = phi.n
    # U symmetrizes its input automatically, so the averaged symmetrization is unnecessary here.
    return psum(k + 1, (sine(k + 1, a, k) * phi.derivative(a).lift(k + 1, range(k))
                         for a in range(k)))


def proposed_drift(phi, n_particles, nu, interaction=True):
    k = phi.n
    result = U(L(phi, nu, interaction), n_particles)
    if interaction:
        result += U(C(phi), n_particles).scale(F(1, n_particles))
        result += U(upward(phi), n_particles)
        if k >= 2:
            result += U(Q(phi), n_particles).scale(F(k, n_particles))
            result += U(R(phi), n_particles).scale(F(comb(k, 2), n_particles))
    return result


def rooted_gradient(phi, n_particles, anchor):
    """Explicit excluded-anchor subset formula, without differentiating U."""
    k = phi.n
    derivative = phi.derivative(0)
    result = defaultdict(lambda: ZERO)
    for active in subsets(range(1, k)):
        for labels in permutations([i for i in range(n_particles) if i != anchor], len(active)):
            for powers, coefficient in derivative.terms.items():
                target = [0] * n_particles
                target[anchor] += powers[0]
                for slot, label in zip(active, labels):
                    target[label] += powers[slot]
                for slot in range(1, k):
                    if slot not in active:
                        coefficient *= moment(powers[slot])
                coefficient *= F(k * (-1) ** (k - 1 - len(active)),
                                  n_particles ** (len(active) + 1))
                result[tuple(target)] += coefficient
    return Poly(n_particles, result)


def partial_bijections(a, b):
    for size in range(min(len(a), len(b)) + 1):
        for domain in combinations(a, size):
            for targets in permutations(b, size):
                yield tuple(zip(domain, targets))


def bracket_by_matchings(phi, psi, n_particles, nu):
    """Enumerate EVERY coincidence between the two rooted label families."""
    k, ell = phi.n, psi.n
    left = phi.derivative(0)
    right = psi.derivative(0)
    result = defaultdict(lambda: ZERO)
    for a in subsets(range(1, k)):
        for b in subsets(range(1, ell)):
            for matching in partial_bijections(a, b):
                # Index 0 is the common Brownian/particle anchor. Different
                # quotient classes receive distinct labels, including anchor.
                classes_a = {slot: q + 1 for q, slot in enumerate(a)}
                classes_b = {}
                target_to_source = {target: source for source, target in matching}
                next_class = 1 + len(a)
                for slot in b:
                    if slot in target_to_source:
                        classes_b[slot] = classes_a[target_to_source[slot]]
                    else:
                        classes_b[slot] = next_class
                        next_class += 1
                coefficient_factor = (2 * nu * k * ell
                    * F((-1) ** (k + ell - 2 - len(a) - len(b)),
                        n_particles ** (2 + len(a) + len(b))))
                for labels in permutations(range(n_particles), next_class):
                    for p, pc in left.terms.items():
                        for q, qc in right.terms.items():
                            powers = [0] * n_particles
                            powers[labels[0]] += p[0] + q[0]
                            coefficient = pc * qc * coefficient_factor
                            for slot in range(1, k):
                                if slot in classes_a:
                                    powers[labels[classes_a[slot]]] += p[slot]
                                else:
                                    coefficient *= moment(p[slot])
                            for slot in range(1, ell):
                                if slot in classes_b:
                                    powers[labels[classes_b[slot]]] += q[slot]
                                else:
                                    coefficient *= moment(q[slot])
                            result[tuple(powers)] += coefficient
    return Poly(n_particles, result)


def assert_equal(label, left, right):
    difference = left - right
    if difference.terms:
        first = next(iter(difference.terms.items()))
        raise AssertionError(f'{label}: {len(difference.terms)} nonzero coefficients; first={first}')
    print(f'PASS {label}: {len(left.terms)} coefficients, exact Q(i) equality')


def test_kernel(k):
    frequencies = {1: (2,), 2: (1, -2), 3: (1, -1, 2), 4: (2, -1, 1, -2)}[k]
    return Poly.monomial(frequencies).symmetric() + Poly.monomial((1,) * k).scale(F(2, 7))


def check_subset_coefficients(max_k=9):
    # For every active B, independently enumerate supersets A and check the
    # two-support alternating-sum coefficient used in the general proof.
    count = 0
    for k in range(1, max_k + 1):
        universe = frozenset(range(k))
        for support_size in (1, 2):
            if support_size > k:
                continue
            for support in combinations(range(k), support_size):
                for b in subsets(range(k)):
                    required = frozenset(b) | frozenset(support)
                    complement = universe - required
                    coefficient = sum((-1) ** (k - len(required) - len(extra))
                                      for extra in subsets(complement))
                    assert coefficient == int(required == universe)
                    count += 1
    print(f'PASS general subset cancellation through k={max_k}: {count} exact integer coefficients')


def main():
    nu = F(3, 5)
    check_subset_coefficients()
    for n in (2, 3, 4):
        for k in (1, 2, 3, 4):
            phi = test_kernel(k)
            direct = particle_generator(U(phi, n), nu) + U_background_dt(phi, n, nu)
            assert_equal(f'drift N={n}, k={k}, inhomogeneous mu', direct,
                         proposed_drift(phi, n, nu))
            # Scalar time derivative commutes with the defining finite sum;
            # adding a second kernel exercises the full deterministic dt slot.
            dt_phi = Poly.monomial((2,) * k).symmetric()
            assert_equal(f'time-dependent kernel N={n}, k={k}', direct + U(dt_phi, n),
                         proposed_drift(phi, n, nu) + U(dt_phi, n))
            for anchor in range(n):
                assert_equal(f'rooted gradient N={n}, k={k}, i={anchor}',
                             U(phi, n).derivative(anchor), rooted_gradient(phi, n, anchor))
        phi = test_kernel(4)
        direct = particle_generator(U(phi, n), nu, False) + U_background_dt(phi, n, nu, False)
        assert_equal(f'K=0 N={n}, k=4', direct, proposed_drift(phi, n, nu, False))
        constant = Poly.monomial((0,) * 4)
        assert_equal(f'constant kernel N={n}, k=4', proposed_drift(constant, n, nu), Poly(n))
    for n, k, ell in ((2, 1, 1), (2, 2, 2), (3, 2, 3), (3, 1, 4)):
        phi, psi = test_kernel(k), test_kernel(ell)
        u, v = U(phi, n), U(psi, n)
        direct = psum(n, (u.derivative(i) * v.derivative(i) for i in range(n))).scale(2 * nu)
        assert_equal(f'bracket matchings N={n}, k={k}, ell={ell}', direct,
                     bracket_by_matchings(phi, psi, n, nu))
    print('ALL ROUND 001 RECURSION SELF-CHECKS PASSED')


if __name__ == '__main__':
    main()
