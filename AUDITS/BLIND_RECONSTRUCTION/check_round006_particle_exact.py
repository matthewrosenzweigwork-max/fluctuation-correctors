#!/usr/bin/env python3
"""Exact supporting algebra for TASK-046. Standard library only; not an SDE proof."""
from fractions import Fraction as Q
from itertools import combinations

CHECKS = 0


def check(label, condition):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*polynomials):
    out = {}
    for p in polynomials:
        for k, v in p.items():
            out[k] = out.get(k, Q(0)) + v
    return clean(out)


def scale(p, c):
    return clean({k: c * v for k, v in p.items()})


def derivative(p, i):
    """Derivative divided by 2*pi*i; Fourier exponents remain exact integers."""
    return clean({k: k[i] * v for k, v in p.items()})


def laplacian(p):
    """The true Laplacian divided by (2*pi)^2."""
    return clean({k: -sum(e * e for e in k) * v for k, v in p.items()})


def cosine_mode(n, i, frequency, j=None):
    key = [0] * n
    key[i] = frequency
    if j is not None:
        key[j] = -frequency
    k = tuple(key)
    return {k: Q(1, 2), tuple(-e for e in k): Q(1, 2)}


def field_gradient(n, i, j):
    """d/dz g(z)/(2*pi*i), assembled with z=x_i-x_j."""
    pieces = []
    for frequency, coefficient in ((1, Q(1)), (2, Q(1, 3))):
        key = [0] * n
        key[i], key[j] = frequency, -frequency
        k = tuple(key)
        pieces.append({k: coefficient * frequency / 2,
                       tuple(-e for e in k): -coefficient * frequency / 2})
    return add(*pieces)


def field_laplacian(n, i, j):
    """Delta_z g/(2*pi)^2, assembled before insertion into particle slots."""
    return add(*(scale(cosine_mode(n, i, k, j), -a * k * k)
                 for k, a in ((1, Q(1)), (2, Q(1, 3)))))


for n in (2, 3, 4, 7):
    external = [add(scale(cosine_mode(n, i, 1), Q(2, 5)),
                    scale(cosine_mode(n, i, 3), Q(3, 7))) for i in range(n)]
    pairs = {pair: add(cosine_mode(n, *[pair[0], 1], j=pair[1]),
                       scale(cosine_mode(n, pair[0], 2, pair[1]), Q(1, 3)))
             for pair in combinations(range(n), 2)}
    h = add(*external, *(scale(g, Q(1, n)) for g in pairs.values()))
    independent_drift = []
    for i in range(n):
        interaction = add(*(scale(field_gradient(n, i, j), -Q(1, n))
                            for j in range(n) if j != i))
        drift = add(scale(derivative(external[i], i), -1), interaction)
        independent_drift.append(drift)
        check(f'N={n}: ordered force component {i}',
              drift == scale(derivative(h, i), -1))
    pair_trace = add(*(field_laplacian(n, i, j) for i, j in pairs))
    direct_trace = add(*(laplacian(v) for v in external),
                       scale(pair_trace, Q(2, n)))
    check(f'N={n}: full particle trace', laplacian(h) == direct_trace)
    wrong_trace = add(*(laplacian(v) for v in external),
                      scale(pair_trace, Q(1, n)))
    check(f'N={n}: missing factor two detected', laplacian(h) != wrong_trace)
    # Each normalized derivative contributes another factor 2*pi*i.
    div_normalized = scale(add(*(derivative(independent_drift[i], i)
                                 for i in range(n))), -1)
    check(f'N={n}: divergence equals negative energy Laplacian',
          div_normalized == scale(direct_trace, -1))
    check(f'N={n}: pair count in divergence bound',
          Q(2, n) * len(pairs) == n - 1)
    interaction_sum = add(*(add(*(scale(field_gradient(n, i, j), -Q(1, n))
                                   for j in range(n) if j != i))
                            for i in range(n)))
    check(f'N={n}: net internal force zero', interaction_sum == {})


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vmul(a, c):
    return tuple(c * x for x in a)


for u in ((Q(1), Q(-2), Q(3)), (Q(2, 3), Q(5, 7), Q(-1, 4))):
    grads2 = (vmul(u, Q(1, 2)), vmul(u, -Q(1, 2)))
    norm2 = sum(dot(x, x) for x in grads2)
    check('N=2 force square', norm2 == dot(u, u) / 2)
    for nu in (Q(0), Q(1), Q(7, 3)):
        check('N=2 energy bracket', 2 * nu * norm2 == nu * dot(u, u))

u = (Q(1), Q(-2), Q(3))
v = (Q(-4), Q(2, 3), Q(5, 7))
w = (Q(3, 2), Q(1), Q(-6))
grads3 = (vmul(vadd(u, v), Q(1, 3)),
          vmul(vadd(vmul(u, -1), w), Q(1, 3)),
          vmul(vadd(vmul(v, -1), vmul(w, -1)), Q(1, 3)))
square3 = sum(dot(a, a) for a in grads3)
formula3 = Q(2, 9) * (dot(u, u) + dot(v, v) + dot(w, w)
                       + dot(u, v) - dot(u, w) + dot(v, w))
check('N=3 full cross-term formula', square3 == formula3)
check('N=3 signed cross terms actually present',
      dot(u, v) - dot(u, w) + dot(v, w) != 0)


def principal_force(points, s):
    n = len(points)
    return [sum((Q(s, n) * (x - y) / abs(x - y) ** (s + 2)
                 for j, y in enumerate(points) if i != j), Q(0))
            for i, x in enumerate(points)]


def principal_energy(points, s):
    n = len(points)
    return sum((abs(points[i] - points[j]) ** (-s)
                for i, j in combinations(range(n), 2)), Q(0)) / n


for s in (1, 2):
    for r in (Q(1, 64), Q(1, 128), Q(1, 256)):
        points = (-r, Q(0), r)
        forces = principal_force(points, s)
        check('three-particle central force cancellation', forces[1] == 0)
        check('three-particle total internal force', sum(forces) == 0)
        check('three-particle leading energy coefficient',
              principal_energy(points, s) == (2 + Q(1, 2) ** s) / (3 * r ** s))
        check('three-particle nonzero exterior forces', forces[0] < 0 < forces[2])
        geometries = ((Q(0), r, Q(1, 4), Q(1, 4) + r),
                      (-r, Q(0), r, Q(1, 4)-r, Q(1, 4), Q(1, 4)+r))
        for points in geometries:
            n = len(points)
            close_pairs = sum(abs(points[i] - points[j]) <= 2 * r
                              for i, j in combinations(range(n), 2))
            lower = Q(close_pairs, n) / (2 * r) ** s
            check('multiple-close-pair energy counting',
                  principal_energy(points, s) >= lower)
            check('multiple-close-pair internal force balance',
                  sum(principal_force(points, s)) == 0)

for d in (3, 4, 5, 8):
    for s in (Q(d - 2, 3), Q(d - 2, 2), Q(d - 2)):
        radial_laplacian_coefficient = s * (s + 2 - d)
        divergence_coefficient = s * (d - 2 - s)
        check('admissible principal Laplacian sign', radial_laplacian_coefficient <= 0)
        check('opposite radial divergence sign',
              divergence_coefficient == -radial_laplacian_coefficient)
        check('Coulomb zero local principal Laplacian',
              (radial_laplacian_coefficient == 0) == (s == d - 2))
    s_above = Q(d - 2) + Q(1, 2)
    check('super-Coulomb sign excluded', s_above * (s_above + 2 - d) > 0)

for n in (2, 3, 4, 7):
    for nu in (Q(0), Q(1), Q(7, 3)):
        for cd in (Q(1), Q(4), Q(9, 2)):
            trace = Q(2, n) * Q(n * (n - 1), 2) * cd
            check('constant-potential Coulomb full periodic trace', trace == (n - 1) * cd)
            check('Coulomb heating carries diffusivity', nu * trace == nu * (n - 1) * cd)
            density_exponent = (n - 1) * cd
            check('density exponent is divergence coefficient', density_exponent == trace)

print(f'PASS: {CHECKS} exact checks')
print('Rational Fourier finite-sum checks: N=2,3,4,7; external and pair modes included.')
print('Vector, zero-diffusion, Coulomb, cancellation, and multiple-close-pair checks passed.')
print('No floating point, random seed, numerical SDE, external dependency, or theorem certification.')
