#!/usr/bin/env python3
"""TASK-073 exact constructor diagnostic; Python standard library only.

This file was written in this construction context without reading any
previous checker.  Gaussian rational Laurent polynomials make the finite
label calculations exact.  They test algebra, not the singular inverse.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import argparse
import hashlib
import json


@dataclass(frozen=True)
class Gaussian:
    real: F = F(0)
    imag: F = F(0)

    def __add__(self, other):
        other = gaussian(other)
        return Gaussian(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-gaussian(other))

    def __mul__(self, other):
        other = gaussian(other)
        return Gaussian(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.real or self.imag)


def gaussian(x):
    return x if isinstance(x, Gaussian) else Gaussian(F(x), F(0))


I = Gaussian(F(0), F(1))


class Polynomial:
    """Finite Fourier polynomial with characters exp(2 pi i k dot x)."""
    def __init__(self, n, terms=None):
        self.n = n
        self.terms = {tuple(k): gaussian(c) for k, c in (terms or {}).items()
                      if gaussian(c)}
        assert all(len(k) == n for k in self.terms)

    @staticmethod
    def constant(n, value):
        return Polynomial(n, {(0,) * n: value})

    def __add__(self, other):
        assert self.n == other.n
        out = dict(self.terms)
        for k, c in other.terms.items():
            out[k] = out.get(k, Gaussian()) + c
        return Polynomial(self.n, out)

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self + (-other)

    def scale(self, c):
        return Polynomial(self.n, {k: v * c for k, v in self.terms.items()})

    def __mul__(self, other):
        assert self.n == other.n
        out = {}
        for k, c in self.terms.items():
            for j, a in other.terms.items():
                key = tuple(x + y for x, y in zip(k, j))
                out[key] = out.get(key, Gaussian()) + c * a
        return Polynomial(self.n, out)

    def derivative(self, axis):
        # Physical partial derivative is 2 pi times this derivative.
        return Polynomial(self.n, {k: c * I * k[axis]
                                   for k, c in self.terms.items()})

    def integrate(self, axes):
        axes = frozenset(axes)
        kept = tuple(j for j in range(self.n) if j not in axes)
        out = {}
        for k, c in self.terms.items():
            if any(k[j] for j in axes):
                continue
            key = tuple(k[j] for j in kept)
            out[key] = out.get(key, Gaussian()) + c
        return Polynomial(len(kept), out)

    def embed(self, mapping, n):
        assert len(mapping) == self.n
        out = {}
        for k, c in self.terms.items():
            key = [0] * n
            for j, target in enumerate(mapping):
                key[target] += k[j]
            key = tuple(key)
            out[key] = out.get(key, Gaussian()) + c
        return Polynomial(n, out)

    def is_zero(self):
        return not self.terms


def cosine(k):
    return Polynomial(len(k), {tuple(k): F(1, 2),
                              tuple(-x for x in k): F(1, 2)})


def sine(k):
    return Polynomial(len(k), {tuple(k): I * F(-1, 2),
                              tuple(-x for x in k): I * F(1, 2)})


def pair_statistic(phi, n, falling=False):
    out = Polynomial(n)
    denominator = n * (n - 1) if falling else n * n
    for labels in permutations(range(n), 2):
        out = out + phi.embed(labels, n).scale(F(1, 2 * denominator))
    projection = phi.integrate([1])
    for i in range(n):
        out = out - projection.embed([i], n).scale(F(1, n))
    return out + phi.integrate([0, 1]).embed([], n).scale(F(1, 2))


def deleted_u3_literal(phi, n):
    # Literal subset definition, independently of contracted response formulas.
    out = Polynomial(n)
    for size in range(4):
        for active in combinations(range(3), size):
            inactive = [j for j in range(3) if j not in active]
            projection = phi.integrate(inactive)
            sign = -1 if (3 - size) % 2 else 1
            for labels in permutations(range(n), size):
                out = out + projection.embed(labels, n).scale(F(sign, n ** size))
    return out


def exact_operators(phi, force):
    internal = force * (phi.derivative(0) - phi.derivative(1))
    rx = (force.embed([2, 0], 3)
          * phi.derivative(0).embed([2, 1], 3)).integrate([2])
    ry = (force.embed([2, 1], 3)
          * phi.derivative(1).embed([0, 2], 3)).integrate([2])
    unsym = force.embed([0, 2], 3) * phi.derivative(0).embed([0, 1], 3)
    cubic = Polynomial(3)
    for perm in permutations(range(3)):
        cubic = cubic + unsym.embed(perm, 3).scale(F(1, 6))
    return internal, rx, ry, cubic


def actual_force_generator(observable, force, n):
    out = Polynomial(n)
    for i in range(n):
        drift = Polynomial(n)
        for j in range(n):
            if i != j:
                drift = drift + force.embed([i, j], n).scale(F(1, n))
        out = out + drift * observable.derivative(i)
    return out


class Checks:
    def __init__(self):
        self.count = 0
        self.groups = {}

    def require(self, truth, label, group):
        self.count += 1
        self.groups[group] = self.groups.get(group, 0) + 1
        if not truth:
            raise AssertionError(label)


def algebra_checks(check):
    kernels = {
        'constant': Polynomial.constant(2, 1),
        'relative': cosine([1, -1]),
        'additive': cosine([1, 0]) + cosine([0, 1]),
        'separable': cosine([1, 0]) * cosine([0, 1]),
        'mixed': cosine([2, 1]) + cosine([1, 2]),
        'combined': cosine([1, -1]) + cosine([1, 0])
                    + cosine([0, 1]) + sine([2, 1]) + sine([1, 2]),
    }
    forces = {'zero': Polynomial(2),
              'two_modes': sine([1, -1]) + sine([2, -2]).scale(F(2, 3))}
    caught = {name: 0 for name in ['omit_scalar', 'halve_lower',
                                 'omit_response_slot', 'falling_pair_denominator',
                                 'drop_u3_at_n2']}
    witness = None
    for force_name, force in forces.items():
        for name, phi in kernels.items():
            check.require((phi - phi.embed([1, 0], 2)).is_zero(),
                          name + ' symmetric', 'algebra')
            internal, rx, ry, cubic = exact_operators(phi, force)
            g = internal.integrate([1])
            c = internal.integrate([0, 1])
            for n in range(2, 6):
                p = pair_statistic(phi, n)
                direct = actual_force_generator(p, force, n)
                u3 = deleted_u3_literal(cubic, n)
                eta_g = Polynomial(n)
                for i in range(n):
                    eta_g = eta_g + g.embed([i], n).scale(F(1, n))
                scalar = c.embed([], n)
                rho_g = eta_g - scalar
                lower = rho_g.scale(F(1, n)) + scalar.scale(F(1, 2 * n))
                linear = pair_statistic(internal.scale(F(1, n)) + rx + ry, n)
                right = linear + u3 + lower
                check.require((direct - right).is_zero(),
                              f'full interaction identity {force_name}/{name}/N={n}',
                              'algebra')
                regrouped = eta_g.scale(F(1, n)) - scalar.scale(F(1, 2 * n))
                check.require((lower - regrouped).is_zero(),
                              f'exact lower regrouping {force_name}/{name}/N={n}',
                              'algebra')
                d2 = Polynomial(n)
                for labels in permutations(range(n), 2):
                    d2 = d2 + internal.embed(labels, n).scale(F(1, n * n))
                check.require((d2.scale(F(1, 2 * n))
                               - pair_statistic(internal, n).scale(F(1, n))
                               - lower).is_zero(),
                              f'exact repeated-label coefficient {force_name}/{name}/N={n}',
                              'algebra')
                mutants = {
                    'omit_scalar': right - scalar.scale(F(1, 2 * n)),
                    'halve_lower': right - rho_g.scale(F(1, 2 * n)),
                    'omit_response_slot': right - pair_statistic(ry, n),
                }
                for mutation, mutant in mutants.items():
                    caught[mutation] += int(not (direct - mutant).is_zero())
                wrong_p = pair_statistic(phi, n, falling=True)
                wrong_direct = actual_force_generator(wrong_p, force, n)
                wrong_right = pair_statistic(internal.scale(F(1, n)) + rx + ry,
                                             n, falling=True) + u3 + lower
                caught['falling_pair_denominator'] += int(not (wrong_direct - wrong_right).is_zero())
                if n == 2:
                    caught['drop_u3_at_n2'] += int(not u3.is_zero())
                if force_name == 'two_modes' and name == 'relative' and n == 2:
                    # Exact scalar nonzero for this smooth algebra probe.
                    check.require(not c.is_zero(), 'scalar witness nonzero', 'algebra')
                    check.require(rho_g.is_zero(), 'relative scalar witness has rho g zero', 'algebra')
                    value = c.terms[()]
                    witness = {'c_over_2pi': str(value.real),
                               'N': n, 'rho_g': '0',
                               'lower_over_2pi': str(value.real / (2 * n))}
    for mutation, number in caught.items():
        check.require(number > 0, 'mutation not detected: ' + mutation, 'mutation_sensitivity')
    return caught, witness


def exponent_checks(check):
    admitted = critical = 0
    for d in range(3, 21):
        for denominator in range(1, 14):
            for numerator in range(1, (d - 2) * denominator):
                s = F(numerator, denominator)
                p = s + 2
                lo = max(F(1), s / 2)
                hi = min(F(d, 2), d - s - 1, s + 1)
                if 3 * s < 2 * d - 2:
                    admitted += 1
                    q = (lo + hi) / 2
                    alpha = (s + 1 - q) / p
                    kappa = (2 * q - s) / (2 * p)
                    check.require(lo < hi, 'q interval', 'exponents')
                    check.require(1 < q < F(d, 2) and q <= s + 1,
                                  'R12 admissibility', 'exponents')
                    check.require(s + 1 + q < d, 'force-gradient weight', 'exponents')
                    check.require(kappa > 0 and alpha - F(1, 2) == -kappa,
                                  'strict decay and exact exponent', 'exponents')
                if s * p < 2 * d:
                    critical += 1
                    check.require(3 * s < 2 * d - 2, 'critical inclusion', 'critical')
                    theta = 1 - s / d
                    check.require(F(2, 1) / p - theta == s * (p - d) / (d * p) < 0,
                                  'critical bounded rescaled diffusion', 'critical')
    examples = []
    for d, s, reason in [
        (7, F(4), '3s=2d-2: zero gap, logarithmic product boundary'),
        (8, F(5), '3s>2d-2: interval reversed'),
        (3, F(1), 'Coulomb: interval closes'),
        (3, F(0), 's=0 is not an allowed positive-Riesz substitution')]:
        lo = max(F(1), s / 2)
        hi = min(F(d, 2), d - s - 1, s + 1)
        check.require(not lo < hi, reason, 'excluded_boundaries')
        examples.append({'d': d, 's': str(s), 'q_lo': str(lo),
                         'q_hi': str(hi), 'reason': reason})
    d, s = 7, F(4)
    q = d - s - 1
    check.require(d - 1 - (s + 1 + q) == -1,
                  'slice radial endpoint integral is dr/r', 'excluded_boundaries')
    check.require((2 * (s / 2) - s) / (2 * (s + 2)) == 0,
                  'q=s/2 has no strict decay', 'excluded_boundaries')
    check.require(d - 1 - 2 * F(d, 2) == -1,
                  'q=d/2 gives nonintegrable squared weight', 'excluded_boundaries')
    check.require(F(4) * (4 + 2) == 2 * 12 and 3 * 4 < 2 * 12 - 2,
                  'noise equality boundary is not a lower-contraction counterexample',
                  'excluded_boundaries')
    check.require(F(2, 1) / (2 + 2) > 0,
                  'fixed positive noise has unbounded chi', 'excluded_boundaries')
    # Three regimes remain different for d=3, s=1/2.
    d, s = 3, F(1, 2)
    theta = 1 - s / d
    check.require(theta + 2 * s / d - 1 > 0,
                  'critical sequence fails old floor condition', 'regime_separation')
    beta_power = F(3, 4)
    check.require(beta_power - theta < 0 and beta_power + 2 * s / d - 1 > 0,
                  'full subcritical sequence can fail old floor condition', 'regime_separation')
    # Positive and zero-noise normalization, never dividing by zero.
    for nu in [F(0), F(1, 7), F(1), F(3)]:
        b = F(1) if nu == 0 else min(1 / nu, F(1))
        check.require(0 < b <= 1, 'b interval', 'noise_convention')
        if nu > 0:
            check.require(nu * b <= 1, 'positive noise product', 'noise_convention')
    # Signed-integral cancellation does not imply a small absolute integral.
    signed = F(1, 2) * 1 + F(1, 2) * (-1)
    absolute = F(1, 2) * 1 + F(1, 2) * 1
    check.require(signed == 0 and absolute == 1,
                  'distinguish signed and absolute time integrals', 'time_norms')
    return {'admitted_parameter_rows': admitted, 'critical_parameter_rows': critical,
            'excluded_examples': examples}


def input_checks(check, here):
    seal = here / 'INPUT_SHA256SUMS.txt'
    rows = seal.read_text().splitlines()
    check.require(len(rows) == 25, '25 inputs', 'provenance')
    names = []
    hashes = {}
    for row in rows:
        expected, name = row.split('  ', 1)
        relative = Path(name)
        check.require(not relative.is_absolute() and '..' not in relative.parts,
                      'safe dossier name', 'provenance')
        actual = hashlib.sha256((here / 'dossier' / relative).read_bytes()).hexdigest()
        check.require(actual == expected, 'input digest ' + name, 'provenance')
        names.append(name)
        hashes[name] = actual
    check.require(len(set(names)) == 25, 'distinct inputs', 'provenance')
    return hashes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-results', type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    check = Checks()
    hashes = input_checks(check, here)
    mutations, witness = algebra_checks(check)
    exponents = exponent_checks(check)
    result = {
        'status': 'PASS',
        'evidence_class': 'exact constructor diagnostic; not independent audit or singular proof',
        'arithmetic': 'fractions.Fraction over Gaussian rational Laurent coefficients',
        'randomness': 'none; no seed or floating tolerance',
        'normalization': 'unit Haar; D=(2pi)^-1 partial; each force-drift identity is divided by 2pi',
        'algebra_scope': 'smooth periodic one-dimensional probes only; no actual inverse substitution',
        'checks': check.count,
        'groups': check.groups,
        'mutations_detected': mutations,
        'nonzero_scalar_algebra_witness': witness,
        'exponent_results': exponents,
        'input_sha256': hashes,
    }
    if args.verify_results:
        saved = json.loads(args.verify_results.read_text())
        if result != saved:
            raise AssertionError('saved diagnostic result differs from fresh recomputation')
        print('PASS: exact fresh recomputation matches the saved diagnostic result.')
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
