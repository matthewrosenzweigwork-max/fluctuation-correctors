#!/usr/bin/env python3
"""Bounded hostile-audit tests; independent of constructor helper code.

Standard library, exact rational arithmetic, no random inputs. These tests
support the mathematical audit and are not a proof of its all-order claims.

The bracket and free-diffusion tests use legitimate smooth unit-torus data:
K=b=0, mu=1, theta=2*pi*x, angular diffusivity 3/7, and separable kernels
made from a(theta)=2+sin(theta), c(theta)=3+cos(theta)+sin(2*theta).
All configurations use multiples of pi/2, including coincident coordinates.
Particle derivatives of U are computed from elementary symmetric polynomials;
the proposed bracket is assembled separately by counting partial matchings.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb, factorial
import json


def elementary(values, order):
    if order < 0 or order > len(values):
        return Q(0)
    out = Q(0)
    for subset in combinations(values, order):
        term = Q(1)
        for value in subset:
            term *= value
        out += term
    return out


def centered_separable(values, mean, order):
    n = len(values)
    return sum((Q(comb(order, r) * factorial(r), n ** r)
                * (-mean) ** (order-r) * elementary(values, r)
                for r in range(min(n, order)+1)), Q(0))


def value_derivative(values, mean, order, i):
    """Derivative with respect to the independent value a(x_i), not x_i."""
    n = len(values)
    other = values[:i] + values[i+1:]
    return sum((Q(comb(order, r) * factorial(r), n ** r)
                * (-mean) ** (order-r) * elementary(other, r-1)
                for r in range(1, min(n, order)+1)), Q(0))


def subset_observable(factors, means, n):
    """Literal centered subset sum for a possibly nonsymmetric product kernel."""
    degree = len(factors)
    answer = Q(0)
    for mask in range(1 << degree):
        occupied = [a for a in range(degree) if mask & (1 << a)]
        if len(occupied) > n:
            continue
        weight = Q((-1) ** (degree-len(occupied)), n ** len(occupied))
        for a in range(degree):
            if a not in occupied:
                weight *= means[a]
        for labels in permutations(range(n), len(occupied)):
            term = weight
            for a, i in zip(occupied, labels):
                term *= factors[a][i]
            answer += term
    return answer


def quotient_factorial(root, shared, left, right, q, a, b):
    """D on the actual quotient classes: root, q shared, a left, b right."""
    n = len(root)
    count = 1 + q + a + b
    if count > n:
        return Q(0)
    factors = [root] + [shared]*q + [left]*a + [right]*b
    answer = Q(0)
    for labels in permutations(range(n), count):
        term = Q(1)
        for factor, i in zip(factors, labels):
            term *= factor[i]
        answer += term
    return answer / n ** count


def proposed_matching_bracket(k, ell, left, right, left_prime, right_prime,
                              mean_left, mean_right, nu):
    n = len(left)
    root = tuple(x*y for x, y in zip(left_prime, right_prime))
    shared = tuple(x*y for x, y in zip(left, right))
    answer = Q(0)
    for a in range(k):
        for b in range(ell):
            background = mean_left ** (k-1-a) * mean_right ** (ell-1-b)
            subset_count = comb(k-1, a) * comb(ell-1, b)
            sign = (-1) ** (k+ell-2-a-b)
            for q in range(min(a, b)+1):
                matching_count = comb(a, q) * comb(b, q) * factorial(q)
                quotient = quotient_factorial(root, shared, left, right,
                                               q, a-q, b-q)
                answer += (Q(sign * subset_count * matching_count, n ** (1+q))
                           * background * quotient)
    return 2 * nu * k * ell * answer


def require_equal(left, right, label):
    if left != right:
        raise AssertionError((label, left, right, left-right))


def main():
    subset_checks = 0
    for k in range(1, 9):
        full = (1 << k)-1
        supports = [(1 << a) for a in range(k)]
        supports += [(1 << a) | (1 << b) for a, b in combinations(range(k), 2)]
        for force in supports:
            for kept in range(1 << k):
                required = force | kept
                observed = sum((-1) ** (k - bin(a).count('1'))
                               for a in range(1 << k) if a & required == required)
                require_equal(observed, int(required == full),
                              ('subset coefficient', k, force, kept))
                subset_checks += 1

    fixtures = ((0, 0), (0, 1), (0, 0, 0), (0, 1, 2),
                (0, 0, 0, 0), (0, 1, 2, 3))
    sin = (Q(0), Q(1), Q(0), Q(-1))
    cos = (Q(1), Q(0), Q(-1), Q(0))
    cos_double = (Q(1), Q(-1), Q(1), Q(-1))
    nu = Q(3, 7)
    bracket_checks = diffusion_checks = constant_checks = 0
    for positions in fixtures:
        n = len(positions)
        left = tuple(2 + sin[t] for t in positions)
        right = tuple(3 + cos[t] for t in positions)
        left_prime = tuple(cos[t] for t in positions)
        right_prime = tuple(-sin[t] + 2*cos_double[t] for t in positions)
        left_second = tuple(-sin[t] for t in positions)
        right_second = tuple(-cos[t] for t in positions)
        for k in range(1, 7):
            for values, mean, second in ((left, Q(2), left_second),
                                        (right, Q(3), right_second)):
                # U is separately affine in each particle's value, so its
                # particle Laplacian is a''(x_i) times its value derivative.
                direct = nu * sum((second[i] * value_derivative(values, mean, k, i)
                                   for i in range(n)), Q(0))
                # Independently apply the k-slot diffusion before inserting U.
                proposed = nu * k * subset_observable(
                    [second] + [values]*(k-1), [Q(0)] + [mean]*(k-1), n)
                require_equal(direct, proposed, ('free diffusion', positions, k, mean))
                diffusion_checks += 1
            for ell in range(1, 7):
                direct = 2 * nu * sum((
                    left_prime[i] * value_derivative(left, Q(2), k, i)
                    * right_prime[i] * value_derivative(right, Q(3), ell, i)
                    for i in range(n)), Q(0))
                proposed = proposed_matching_bracket(
                    k, ell, left, right, left_prime, right_prime, Q(2), Q(3), nu)
                require_equal(direct, proposed, ('matching bracket', positions, k, ell))
                bracket_checks += 1
        expected = (Q(0), Q(-1, n), Q(2, n*n), Q(3, n*n)-Q(6, n**3))
        for k, value in enumerate(expected, 1):
            require_equal(centered_separable((Q(1),)*n, Q(1), k), value,
                          ('constant', n, k))
            constant_checks += 1

    print(json.dumps({
        'status': 'PASS', 'arithmetic': 'exact rational', 'random_inputs': False,
        'subset_coefficient_checks': subset_checks,
        'partial_matching_bracket_checks': bracket_checks,
        'free_diffusion_checks': diffusion_checks,
        'constant_checks': constant_checks,
        'particle_numbers': [2, 3, 4], 'kernel_orders': [1, 2, 3, 4, 5, 6],
        'includes_order_above_particle_number': True,
        'includes_coincident_coordinates': True,
        'angular_diffusivity': str(nu),
        'scope': 'Bounded tests only; general drift and bracket verdicts rely on proof examination.'
    }, indent=2))


if __name__ == '__main__':
    main()
