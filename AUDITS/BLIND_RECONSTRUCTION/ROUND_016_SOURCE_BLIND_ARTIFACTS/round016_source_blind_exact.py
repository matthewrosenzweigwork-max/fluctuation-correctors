#!/usr/bin/env python3
"""AUD051 exact, independently written finite-label/Fourier diagnostics.

Arithmetic is in Gaussian rationals. Spatial derivatives use theta=2*pi*x,
so the physical source is (2*pi)^2 times the source constructed here.
These finite Fourier diagnostics verify algebra, not singular estimates.
No prior checker or non-allowlisted input is read.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    def __add__(self, other):
        other = gaussian(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-gaussian(other))

    def __mul__(self, other):
        other = gaussian(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def conj(self):
        return G(self.r, -self.i)

    def norm2(self):
        return self.r * self.r + self.i * self.i


def gaussian(value):
    return value if isinstance(value, G) else G(F(value))


ZERO = G()
I = G(F(0), F(1))
counts = {}


def check(condition, group, explanation):
    if not condition:
        raise AssertionError(group + ': ' + explanation)
    counts[group] = counts.get(group, 0) + 1


def neg(v):
    return tuple(-x for x in v)


def addv(v, w):
    return tuple(x + y for x, y in zip(v, w))


def subv(v, w):
    return tuple(x - y for x, y in zip(v, w))


def dot(v, w):
    return sum(x * y for x, y in zip(v, w))


def put(poly, power, coefficient):
    value = poly.get(power, ZERO) + coefficient
    if value == ZERO:
        poly.pop(power, None)
    else:
        poly[power] = value


def scale(poly, c):
    result = {}
    for p, a in poly.items():
        put(result, p, a * c)
    return result


def plus(*polys):
    result = {}
    for poly in polys:
        for p, a in poly.items():
            put(result, p, a)
    return result


def times(left, right):
    result = {}
    for p, a in left.items():
        for q, b in right.items():
            put(result, addv(p, q), a * b)
    return result


def l2(poly):
    return sum((a.norm2() for a in poly.values()), F(0))


def real_polynomial(poly):
    return all(poly.get(neg(p), ZERO) == a.conj() for p, a in poly.items())


def sym_real_modes(positive, constant=None):
    result = {}
    for p, a in positive.items():
        result[p] = gaussian(a)
        result[neg(p)] = gaussian(a).conj()
    if constant is not None:
        dimension = len(next(iter(positive)))
        result[(0,) * dimension] = gaussian(constant)
    return result


def literal_kernel(g, h, d):
    """Differentiate g and h separately, then multiply K.(grad h diff)."""
    z = (0,) * d
    result = {}
    for axis in range(d):
        force = {k + neg(k): -I * k[axis] * a for k, a in g.items()
                 if k[axis] != 0}
        difference = {}
        for m, a in h.items():
            put(difference, m + z, I * m[axis] * a)
            put(difference, z + m, -I * m[axis] * a)
        result = plus(result, times(force, difference))
    return result


def first_contraction(kernel, d):
    z = (0,) * d
    return {p[:d]: a for p, a in kernel.items() if p[d:] == z}


def embed_pair(poly, first, second, n, d):
    result = {}
    for pq, a in poly.items():
        exponent = [0] * (n * d)
        for axis in range(d):
            exponent[first * d + axis] += pq[axis]
            exponent[second * d + axis] += pq[d + axis]
        put(result, tuple(exponent), a)
    return result


def embed_one(poly, label, n, d):
    result = {}
    for m, a in poly.items():
        exponent = [0] * (n * d)
        exponent[label * d:(label + 1) * d] = m
        put(result, tuple(exponent), a)
    return result


def empirical(mode, n, d, centered):
    if centered and mode == (0,) * d:
        return {}
    return plus(*(scale(embed_one({mode: G(F(1))}, i, n, d), F(1, n))
                  for i in range(n)))


def literal_statistic(kernel, n, d):
    result = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                result = plus(result, scale(embed_pair(kernel, i, j, n, d),
                                            F(1, 2 * n * n)))
    contraction = first_contraction(kernel, d)
    for i in range(n):
        result = plus(result, scale(embed_one(contraction, i, n, d), F(-1, n)))
    put(result, (0,) * (n * d), kernel.get((0,) * (2 * d), ZERO) * F(1, 2))
    return result


def contracted_fourier_statistic(g, h, n, d):
    result = {}
    for m, hm in h.items():
        candidates = set(g) | {subv(m, ell) for ell in g}
        for k in candidates:
            ell = subv(m, k)
            # Direct commutator formula, separate from literal differentiation.
            coefficient = -(g.get(k, ZERO) * dot(m, k)
                            + g.get(ell, ZERO) * dot(m, ell)) * hm * F(1, 2)
            result = plus(result, scale(times(empirical(k, n, d, True),
                                              empirical(ell, n, d, True)),
                                        coefficient))
    return result


def verify_dataset(name, g, h, d):
    kernel = literal_kernel(g, h, d)
    group = 'kernel_' + name
    check(real_polynomial(kernel), group, 'real test and interaction give real J')
    check(all(kernel.get(p[d:] + p[:d], ZERO) == a for p, a in kernel.items()),
          group, 'pair exchange symmetry')
    diagonal = {}
    for p, a in kernel.items():
        put(diagonal, addv(p[:d], p[d:]), a)
    check(not diagonal, group, 'smooth source diagonal is exactly zero')
    q = first_contraction(kernel, d)
    predicted_q = {}
    for m, hm in h.items():
        put(predicted_q, m, -g.get(m, ZERO) * dot(m, m) * hm)
    check(q == predicted_q, group, 'signed background convolution')
    check(kernel.get((0,) * (2 * d), ZERO) == ZERO, group, 'double Haar contraction')
    z = (0,) * d
    kernel0 = dict(kernel)
    for m, a in q.items():
        put(kernel0, m + z, -a)
        put(kernel0, z + m, -a)
    check(not first_contraction(kernel0, d), group, 'partner centering')
    for n in range(2, 7):
        actual = literal_statistic(kernel, n, d)
        predicted = contracted_fourier_statistic(g, h, n, d)
        check(actual == predicted, 'source_identity', name + ' N=' + str(n))
        check(actual.get((0,) * (n * d), ZERO) == ZERO,
              'actual_initial_mean', name + ' N=' + str(n))
        ho = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    ho = plus(ho, scale(embed_pair(kernel0, i, j, n, d),
                                        F(1, 2 * n * n)))
            ho = plus(ho, scale(embed_one(q, i, n, d), F(-1, n * n)))
        check(actual == ho, 'initial_hoeffding_identity', name + ' N=' + str(n))
        variance = F(n - 1, 2 * n ** 3) * l2(kernel0) + F(1, n ** 3) * l2(q)
        check(l2(actual) == variance, 'initial_variance', name + ' N=' + str(n))
        # Energy is constructed with unordered pairs, then divided by N.
        energy_kernel = {k + neg(k): a for k, a in g.items()}
        direct = {}
        for i in range(n):
            for j in range(i + 1, n):
                direct = plus(direct, scale(embed_pair(energy_kernel, i, j, n, d),
                                            F(1, n * n)))
        spectral = {}
        for k, a in g.items():
            spectral = plus(spectral, scale(times(empirical(k, n, d, False),
                                                  empirical(neg(k), n, d, False)),
                                            a * F(1, 2)))
        put(spectral, (0,) * (n * d), -sum(g.values(), ZERO) * F(1, 2 * n))
        check(direct == spectral, 'energy_self_subtraction', name + ' N=' + str(n))
        check(direct.get((0,) * (n * d), ZERO) == ZERO,
              'initial_energy_mean', name + ' N=' + str(n))
    return {'name': name, 'dimension': d, 'kernel_terms': len(kernel),
            'largest_input_frequency_coordinate':
            max(abs(x) for mode in list(g) + list(h) for x in mode)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true',
                        help='Run every check without changing the sealed results file.')
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    input_hashes = {}
    for line in (folder / 'INPUT_SHA256SUMS.txt').read_text().splitlines():
        expected, rel = line.split('  ', 1)
        actual = hashlib.sha256((folder / 'inputs' / rel).read_bytes()).hexdigest()
        check(actual == expected, 'input_hash', rel)
        input_hashes[rel] = actual
    check(len(input_hashes) == 9, 'input_hash', 'exactly nine frozen inputs')

    low_g = sym_real_modes({(1, 0, 0): F(1), (2, 0, 0): F(2, 3),
                            (0, 1, 0): F(3, 5), (1, 1, 0): F(7, 11),
                            (0, 0, 1): F(5, 8)})
    mixed_h = sym_real_modes({(1, 0, 0): G(F(1, 3), F(1, 5)),
                              (0, 2, 0): G(F(-2, 7), F(3, 8)),
                              (1, -1, 1): G(F(1, 9), F(-2, 5))}, F(3, 4))
    datasets = [
        ('constant', low_g, {(0, 0, 0): G(F(7, 4))}, 3),
        ('low_mixed', low_g, mixed_h, 3),
        ('single_mode', low_g, sym_real_modes({(1, 0, 0): F(1, 2)}), 3),
        ('large_terminal', sym_real_modes({(4096, 0, 0): F(1, 13),
                                         (4103, 0, 0): F(2, 17),
                                         (1, 0, 0): F(3, 19)}),
         sym_real_modes({(4099, 0, 0): G(F(2, 5), F(3, 7))}), 3),
        ('very_large_internal', sym_real_modes({(1000033, 2, 0): F(3, 23),
                                               (1000030, 1, 0): F(7, 29),
                                               (3, 1, 0): F(2, 31)}),
         sym_real_modes({(3, 1, 0): G(F(5, 11), F(-2, 13))}), 3),
        ('dimension_five', sym_real_modes({(1, 0, 0, 0, 0): F(3, 5),
                                          (0, 0, 0, 0, 2): F(4, 7)}),
         sym_real_modes({(1, 0, 0, 0, 0): F(3, 8),
                         (0, 1, 0, -1, 2): G(F(2, 9), F(1, 3))}), 5),
    ]
    records = [verify_dataset(*data) for data in datasets]

    # Coulomb's finite-measure response: the zero mode is compensated and
    # every nonzero mode sees the atom. Only contraction coefficients are tested.
    cd = F(7, 3)
    hc = sym_real_modes({(1, 0, 0): G(F(1, 3), F(2, 5)),
                         (97, -2, 1): G(F(3, 11), F(-1, 7))}, F(5, 2))
    gc = {m: G(cd / dot(m, m)) for m in hc if dot(m, m)}
    jc = literal_kernel(gc, hc, 3)
    qc = first_contraction(jc, 3)
    expected = {m: -a * cd for m, a in hc.items() if dot(m, m)}
    check(qc == expected, 'coulomb_measure', 'atom gives -cd times nonconstant part')
    check((0, 0, 0) not in qc, 'coulomb_measure', 'Haar compensation cancels constant')
    check(bool(qc), 'coulomb_measure', 'punctured constant alone would miss response')
    check(cd * (G(F(1)) - G(F(1))) == ZERO,
          'coulomb_measure', 'full divergence measure has mass zero')

    scaling_rows = []
    for d in range(3, 13):
        for numerator in range(1, 4 * (d - 2) + 1):
            s = F(numerator, 4)
            alpha = (F(d) - s) / 2
            raw = s / d - 1
            scaled = s / d - F(1, 2)
            check(alpha >= 1, 'scaling', 'admitted alpha at least one')
            check(F(-2, d) * alpha == raw, 'scaling', 'positive short heat power')
            check(-1 + F(-2, d) * (-s / 2) == raw,
                  'scaling', 'exact smooth self power')
            check(2 * alpha + 2 + s == d + 2,
                  'scaling', 'terminal Fourier seminorm loss')
            check(raw < 0, 'scaling', 'raw decay in full card range')
            check((scaled < 0) == (s < F(d, 2)), 'scaling', 'strict decay threshold')
            check((scaled == 0) == (s == F(d, 2)), 'scaling', 'bounded threshold')
            if s < d - 2:
                check(4 * ((F(d) - s - 2) / 2) * (s / 2) == s * (d - 2 - s),
                      'normalization', 'sub-Coulomb gamma recurrence factor')
            else:
                check(alpha == 1, 'normalization', 'Coulomb treated separately')
            if scaled == 0 or s == d - 2:
                scaling_rows.append({'d': d, 's': str(s), 'alpha': str(alpha),
                                     'raw_exponent': str(raw),
                                     'scaled_exponent': str(scaled)})
    for nu in [F(0), F(1, 10), F(1), F(3), F(17)]:
        b = F(1) if nu == 0 else min(1 / nu, F(1))
        check(0 < b <= 1, 'noise', 'defined bounded b, including zero noise')
        check(nu * b <= 1, 'noise', 'physical normalization')
        if nu == 0:
            check(b == 1, 'noise', 'zero noise convention')
    for n in range(2, 19):
        abstract_Qmean = F(5, 7)
        abstract_G0 = F(7, 3)
        mean_L = F(n - 1, n) * abstract_Qmean
        mean_E = abstract_G0 / n
        check(mean_L + mean_E - F(n - 1, n) * abstract_Qmean - abstract_G0 / n == 0,
              'initial_positive_identity', 'both exact compensations N=' + str(n))

    result = {
        'status': 'PASS',
        'assertion_count': sum(counts.values()),
        'counts_by_group': counts,
        'arithmetic': 'Gaussian rationals using Python Fraction; no tolerance or random seed',
        'physical_units': 'Each diagnostic source is the physical source divided by (2*pi)^2; source variances restore (2*pi)^4.',
        'scope': 'Exact finite Fourier and finite-label identities, normalization factors and scaling implications. The singular analytical bounds are proved in the reconstruction, not numerically certified here.',
        'datasets': records,
        'threshold_rows': scaling_rows,
        'input_hashes': input_hashes,
        'diagnostic_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if not args.check_only:
        (folder / 'round016_source_blind_exact_results.json').write_text(
            json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': result['status'], 'assertions': result['assertion_count'],
                      'counts': counts}, sort_keys=True))


if __name__ == '__main__':
    main()
