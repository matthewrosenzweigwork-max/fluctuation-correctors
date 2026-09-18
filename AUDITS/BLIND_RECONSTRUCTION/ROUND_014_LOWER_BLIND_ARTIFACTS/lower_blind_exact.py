#!/usr/bin/env python3
"""Independent TASK-074 exact diagnostics; Python standard library only.

This is finite algebra and range testing, not an analytic-limit certificate.
Fourier coordinates are angles, with normalized Haar. The unit-torus mapping
theta=2*pi*x, K_x=K_theta/(2*pi), nu_x=nu_theta/(2*pi)^2 preserves the tested
generator identities exactly. No Riesz approximation or singular limit is
claimed by these smooth polynomial examples.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
import json
import sys


@dataclass(frozen=True)
class Z:
    r: F = F(0)
    i: F = F(0)

    def __add__(self, other):
        other = as_z(other)
        return Z(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.r, -self.i)

    def __sub__(self, other):
        return self + -as_z(other)

    def __rsub__(self, other):
        return as_z(other) + -self

    def __mul__(self, other):
        other = as_z(other)
        return Z(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = F(scalar)
        return Z(self.r / scalar, self.i / scalar)

    def __str__(self):
        return str(self.r) if not self.i else f"({self.r})+({self.i})i"


def as_z(value):
    return value if isinstance(value, Z) else Z(F(value))


ZERO, ONE, I = Z(), Z(F(1)), Z(F(0), F(1))
ROOTS = (ONE, I, -ONE, -I)


def clean(poly):
    return {k: as_z(v) for k, v in poly.items() if as_z(v) != ZERO}


def add(*polys):
    result = {}
    for poly in polys:
        for mode, coeff in poly.items():
            result[mode] = result.get(mode, ZERO) + coeff
    return clean(result)


def scale(poly, scalar):
    return clean({k: v * scalar for k, v in poly.items()})


def multiply(a, b):
    result = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            mode = tuple(x + y for x, y in zip(ka, kb))
            result[mode] = result.get(mode, ZERO) + va * vb
    return clean(result)


def derivative(poly, slot):
    return clean({k: v * I * k[slot] for k, v in poly.items()})


def integrate(poly, slots):
    """Exact Haar integral in selected slots; no grid quadrature."""
    result = {}
    slots = set(slots)
    for k, v in poly.items():
        if all(k[j] == 0 for j in slots):
            mode = tuple(n for j, n in enumerate(k) if j not in slots)
            result[mode] = result.get(mode, ZERO) + v
    return clean(result)


def evaluate(poly, positions):
    return sum((v * ROOTS[sum(kj * xj for kj, xj in zip(k, positions)) % 4]
                for k, v in poly.items()), ZERO)


def cosine(mode):
    return {tuple(mode): Z(F(1, 2)), tuple(-x for x in mode): Z(F(1, 2))}


def sine(mode):
    return {tuple(mode): -I / 2, tuple(-x for x in mode): I / 2}


def lift(poly, target_slots, dimension):
    result = {}
    for k, v in poly.items():
        mode = [0] * dimension
        for slot, n in zip(target_slots, k):
            mode[slot] = n
        result[tuple(mode)] = v
    return result


def permute(poly, perm):
    result = {}
    for k, v in poly.items():
        mode = [0] * len(perm)
        for slot, destination in enumerate(perm):
            mode[destination] = k[slot]
        result[tuple(mode)] = v
    return result


def centered(poly, positions, order):
    """Literal subset formula with ordered distinct labels and N^j."""
    n = len(positions)
    ans = ZERO
    for bits in product((0, 1), repeat=order):
        particle_slots = [j for j, bit in enumerate(bits) if bit]
        haar_slots = [j for j, bit in enumerate(bits) if not bit]
        contracted = integrate(poly, haar_slots)
        sign = (-1) ** len(haar_slots)
        for labels in permutations(range(n), len(particle_slots)):
            ans += sign * evaluate(contracted, [positions[j] for j in labels]) / (n ** len(labels))
    return ans


def pair_stat(poly, positions):
    return centered(poly, positions, 2) / 2


def deletion_pair(poly, positions):
    n = len(positions)
    return sum((evaluate(poly, [positions[i], positions[j]])
                for i, j in permutations(range(n), 2)), ZERO) / (n * n)


checks = 0


def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def equal(a, b, message):
    require(a == b, f"{message}: {a} != {b}")


def coefficient_tests():
    force = add(sine((1,)), scale(sine((2,)), F(1, 3)))
    force_pair = add(sine((1, -1)), scale(sine((2, -2)), F(1, 3)))
    force_13 = add(sine((1, 0, -1)), scale(sine((2, 0, -2)), F(1, 3)))
    probes = {
        'constant': {(0, 0): Z(F(3))},
        'difference': cosine((1, -1)),
        'one_body': add(cosine((1, 0)), cosine((0, 1))),
        'sum': cosine((1, 1)),
        'mixed': add(cosine((1, -1)), cosine((1, 0)), cosine((0, 1)),
                     scale(cosine((1, 1)), F(2, 3)),
                     scale(add(sine((2, 1)), sine((1, 2))), F(3, 5))),
    }
    cases = 0
    witnesses = {}
    for name, phi in probes.items():
        gx, gy = derivative(phi, 0), derivative(phi, 1)
        lap = add(derivative(gx, 0), derivative(gy, 1))
        response_x = clean({k: v * force.get((-k[0],), ZERO) * I * k[0]
                            for k, v in phi.items()})
        response = clean({k: v * (force.get((-k[0],), ZERO) * I * k[0]
                                  + force.get((-k[1],), ZERO) * I * k[1])
                          for k, v in phi.items()})
        bphi = multiply(force_pair, add(gx, scale(gy, -1)))
        raw_triple = multiply(force_13, lift(gx, (0, 1), 3))
        cubic = scale(add(*(permute(raw_triple, perm)
                            for perm in permutations(range(3)))), F(1, 6))
        projection = integrate(phi, (1,))
        projection_x = derivative(projection, 0)
        projection_xx = derivative(projection_x, 0)
        lower = integrate(bphi, (1,))
        scalar = evaluate(integrate(bphi, (0, 1)), [])
        equal(evaluate(integrate(cubic, (0, 1, 2)), []), ZERO,
              f'{name}: full cubic Haar contraction')
        for n in (2, 3, 4, 5, 7):
            configurations = (tuple(j % 4 for j in range(n)),
                              tuple((j * j + 1) % 4 for j in range(n)),
                              tuple(0 if j < n - 1 else 1 for j in range(n)))
            for pos in configurations:
                for nu in (F(0), F(1, 7), F(2)):
                    cases += 1
                    direct = ZERO
                    for i in range(n):
                        velocity = sum((evaluate(force, [(pos[i] - pos[j]) % 4])
                                        for j in range(n) if j != i), ZERO) / n
                        gradient = sum((evaluate(gx, [pos[i], pos[j]])
                                        for j in range(n) if j != i), ZERO) / (n*n)
                        gradient -= evaluate(projection_x, [pos[i]]) / n
                        lap_i = sum((evaluate(derivative(gx, 0), [pos[i], pos[j]])
                                     for j in range(n) if j != i), ZERO) / (n*n)
                        lap_i -= evaluate(projection_xx, [pos[i]]) / n
                        direct += velocity * gradient + nu * lap_i
                    u3 = centered(cubic, pos, 3)
                    rho_lower = centered(lower, pos, 1)
                    exact_lower = rho_lower / n + scalar / (2*n)
                    core = pair_stat(add(scale(lap, nu), response,
                                         scale(bphi, F(1, n))), pos) + u3
                    equal(direct, core + exact_lower, f'{name}, N={n}: full identity')
                    equal(deletion_pair(bphi, pos) / (2*n) - pair_stat(bphi, pos) / n,
                          exact_lower, f'{name}, N={n}: exact lower conversion')
                    eta_lower = sum((evaluate(lower, [x]) for x in pos), ZERO) / n
                    equal(exact_lower, (eta_lower - scalar / 2) / n,
                          f'{name}, N={n}: scalar retained in centering')
                    variants = {
                        'scalar_omitted': core + rho_lower / n,
                        'scalar_doubled': core + rho_lower / n + scalar / n,
                        'lower_sign_reversed': core - rho_lower / n + scalar / (2*n),
                        'cubic_omitted': core - u3 + exact_lower,
                        'internal_pair_doubled': core + pair_stat(bphi, pos) / n + exact_lower,
                        'one_response_omitted': core - pair_stat(response_x, pos) + exact_lower,
                        'wrong_falling_factorial_pair':
                            core + exact_lower + deletion_pair(bphi, pos) / (2*n*(n-1)),
                    }
                    for mutation, candidate in variants.items():
                        if candidate != direct and mutation not in witnesses:
                            witnesses[mutation] = {'probe': name, 'N': n, 'positions_quarter_turns': list(pos),
                                                   'nu_angle': str(nu), 'exact_gap': str(candidate-direct)}
                    if n == 2 and u3 != ZERO and 'N2_nonzero_U3' not in witnesses:
                        witnesses['N2_nonzero_U3'] = {'probe': name, 'value': str(u3), 'positions_quarter_turns': list(pos)}
        if name == 'constant':
            equal(bphi, {}, 'constant pair B is zero')
            equal(cubic, {}, 'constant pair C is zero')
    for mutation in ('scalar_omitted', 'scalar_doubled', 'lower_sign_reversed',
                     'cubic_omitted', 'internal_pair_doubled', 'one_response_omitted', 'wrong_falling_factorial_pair',
                     'N2_nonzero_U3'):
        require(mutation in witnesses, f'No adversarial witness detected for {mutation}')
    # The simple counterexample to a parity-only scalar cancellation is exact.
    b_simple = multiply(sine((1, -1)),
                        add(derivative(cosine((1, -1)), 0),
                            scale(derivative(cosine((1, -1)), 1), -1)))
    equal(evaluate(integrate(b_simple, (0, 1)), []), Z(F(-1)),
          'symmetric Phi and odd K do not force scalar cancellation')
    return {'smooth_cases': cases, 'mutation_witnesses': witnesses}


def range_tests():
    admitted, critical, outside = 0, 0, 0
    for d in range(3, 41):
        for den in (1, 2, 3, 5, 11, 31):
            for num in range(1, den * (d - 2)):
                s = F(num, den)
                p = s + 2
                lo = max(F(1), s/2)
                hi = min(F(d, 2), d-s-1, s+1)
                allowed = 3*s < 2*d-2
                equal(lo < hi, allowed, 'exact admissibility interval criterion')
                if allowed:
                    admitted += 1
                    q = (lo+hi)/2
                    require(1 < q < F(d, 2), 'R12 open q range')
                    require(q <= s+1, 'R12 source weight range')
                    require(q < d-s-1, 'force-gradient integrability')
                    kappa = (2*q-s)/(2*p)
                    require(kappa > 0, 'strict decay exponent')
                    equal((s+1-q)/p-F(1, 2), -kappa, 'exact fluctuation exponent')
                else:
                    outside += 1
                if s*p < 2*d:
                    critical += 1
                    require(allowed, 'full critical decay range included')
                    theta = 1-s/d
                    equal(2/p-theta, s*(p-d)/(d*p), 'critical bounded-chi exponent')
                    require(2/p-theta < 0, 'critical chi tends to zero')
    d, s = 8, F(14, 3)
    lo, hi = max(F(1), s/2), min(F(d, 2), d-s-1, s+1)
    equal(lo, hi, 'excluded 3s=2d-2 boundary closes q interval')
    equal((2*lo-s)/(2*(s+2)), F(0), 'excluded boundary loses decay')
    equal(d-1-(s+1+hi), F(-1), 'excluded boundary gives logarithmic radial integral')
    for nu in (F(0), F(1, 1000), F(1), F(2), F(13, 2)):
        b = F(1) if nu == 0 else min(1/nu, F(1))
        require(0 < b <= 1, 'positive normalization b and zero-noise convention')
        if nu == 0:
            equal(b, F(1), 'zero noise never takes reciprocal')
    return {'admitted_parameter_cases': admitted, 'critical_cases': critical,
            'excluded_interval_cases': outside,
            'boundary_example': {'d': d, 's': str(s), 'q_lo_equals_q_hi': str(lo),
                                 'radial_power': '-1', 'kappa': '0'}}


def main():
    coefficient = coefficient_tests()
    ranges = range_tests()
    result = {'task': 'TASK-074', 'status': 'PASS', 'arithmetic': 'exact Gaussian rationals and fractions',
              'seed': None, 'dependencies': 'Python standard library only', 'checks': checks,
              'coefficient_diagnostic': coefficient, 'range_diagnostic': ranges,
              'limits': 'Finite diagnostics do not prove analytic estimates, singular passage, or asymptotic limits.'}
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
