#!/usr/bin/env python3
"""Floating-point self-check of the fully decomposed smooth pair identity.

Only Python's standard library is used. The two sides are computed differently:
the left side differentiates the explicit deleted-pair particle observable and
the background PDE; the right side evaluates the centered U-statistics by the
literal subset/distinct-label definition. Trigonometric quadrature is exact in
exact arithmetic at the specified grid size, but floating-point evaluation is
EXPLORATORY evidence, not an independent certificate or a proof.
"""

from itertools import product
from math import cos, sin, pi
import platform


TAU = 2 * pi
GRID_SIZE = 24
TOLERANCE = 2e-10


class PairKernel:
    def __init__(self, name, terms):
        self.name = name
        self.terms = terms  # (cos coefficient, sin coefficient, x mode, y mode)

    def at(self, x, y, dx=0, dy=0):
        return sum(
            (TAU * a) ** dx * (TAU * b) ** dy
            * (c * cos(TAU * (a * x + b * y) + (dx + dy) * pi / 2)
               + s * sin(TAU * (a * x + b * y) + (dx + dy) * pi / 2))
            for c, s, a, b in self.terms
        )


KERNELS = [
    PairKernel("constant", [(1., 0., 0, 0)]),
    PairKernel("separable_sin_sin", [(0.5, 0., 1, -1), (-0.5, 0., 1, 1)]),
    PairKernel("one_difference_mode", [(1., 0., 1, -1)]),
    PairKernel("one_body_sum", [(1., 0., 1, 0), (1., 0., 0, 1)]),
    PairKernel("symmetric_mixed_modes", [(0.7, 0.3, 1, 2), (0.7, 0.3, 2, 1),
                                          (0., 0.2, 1, 1)]),
]


def mu(x, derivative=0):
    modes = [(0.25, 0., 1), (0., 0.125, 1), (0.1, 0., 2)]
    return (1. if derivative == 0 else 0.) + sum(
        (TAU * k) ** derivative
        * (a * cos(TAU * k * x + derivative * pi / 2)
           + b * sin(TAU * k * x + derivative * pi / 2))
        for a, b, k in modes
    )


def force(x, enabled):
    return enabled * (sin(TAU * x) + sin(2 * TAU * x) / 3)


def drift_b(x):
    return -sin(TAU * x) / 5


def velocity(x, enabled, derivative=0):
    # The convolution K*mu is evaluated analytically, independently of quadrature.
    return (TAU ** derivative
            * ((-1 / 5 + enabled / 8) * sin(TAU * x + derivative * pi / 2)
               - enabled / 16 * cos(TAU * x + derivative * pi / 2))
            + enabled / 60 * (2 * TAU) ** derivative
            * sin(2 * TAU * x + derivative * pi / 2))


def check_pair(xs, enabled, nu, phi):
    n = len(xs)
    grid = [q / GRID_SIZE for q in range(GRID_SIZE)]
    points = list(xs) + grid
    count = len(points)
    mass = [mu(x) / GRID_SIZE for x in grid]
    rho_weights = [1 / n] * n + [-w for w in mass]
    mudot = [(-velocity(x, enabled, 1) * mu(x)
              - velocity(x, enabled) * mu(x, 1) + nu * mu(x, 2)) / GRID_SIZE
             for x in grid]
    values = [[phi.at(x, y) for y in points] for x in points]
    px = [[phi.at(x, y, 1, 0) for y in points] for x in points]
    py = [[phi.at(x, y, 0, 1) for y in points] for x in points]
    pxx = [[phi.at(x, y, 2, 0) for y in points] for x in points]
    pyy = [[phi.at(x, y, 0, 2) for y in points] for x in points]
    k = [[force(x - y, enabled) for y in points] for x in points]
    u = [velocity(x, enabled) for x in points]
    b2 = [[k[a][b] * (px[a][b] - py[a][b]) for b in range(count)]
          for a in range(count)]

    # Direct configuration generator and exact reference-density derivative.
    direct = 0.
    for i, x in enumerate(xs):
        grad = sum(px[i][j] for j in range(n) if j != i) / n ** 2
        grad -= sum(mass[z] * px[i][n + z] for z in range(GRID_SIZE)) / n
        lap = sum(pxx[i][j] for j in range(n) if j != i) / n ** 2
        lap -= sum(mass[z] * pxx[i][n + z] for z in range(GRID_SIZE)) / n
        actual_velocity = drift_b(x) + sum(k[i][j] for j in range(n) if j != i) / n
        direct += actual_velocity * grad + nu * lap
        direct -= sum(mudot[z] * values[i][n + z] for z in range(GRID_SIZE)) / n
    direct += sum(mudot[a] * mass[b] * values[n + a][n + b]
                  for a, b in product(range(GRID_SIZE), repeat=2))

    def pair_operator(a, b):
        response = sum(mass[z] * (k[n + z][a] * px[n + z][b]
                                 + k[n + z][b] * py[a][n + z])
                       for z in range(GRID_SIZE))
        return (u[a] * px[a][b] + u[b] * py[a][b]
                + nu * (pxx[a][b] + pyy[a][b]) + response + b2[a][b] / n)

    # Literal U2: labels of particle slots must be distinct; grid slots have no label.
    pair = sum(rho_weights[a] * rho_weights[b] * pair_operator(a, b) / 2
               for a, b in product(range(count), repeat=2)
               if not (a < n and b < n and a == b))

    # Literal U3: no product-measure-to-U3 contraction formula is used here.
    upward = 0.
    for a, b, c in product(range(count), repeat=3):
        labels = [i for i in (a, b, c) if i < n]
        if len(set(labels)) != len(labels):
            continue
        sym = (k[a][c] * px[a][b] + k[a][b] * px[a][c]
               + k[b][c] * px[b][a] + k[b][a] * px[b][c]
               + k[c][b] * px[c][a] + k[c][a] * px[c][b]) / 6
        upward += rho_weights[a] * rho_weights[b] * rho_weights[c] * sym
    lower_one = sum(rho_weights[a] * mass[z] * b2[a][n + z]
                    for a in range(count) for z in range(GRID_SIZE)) / n
    lower_zero = sum(mass[a] * mass[b] * b2[n + a][n + b]
                     for a, b in product(range(GRID_SIZE), repeat=2)) / (2 * n)
    decomposed = pair + upward + lower_one + lower_zero
    return direct, decomposed


def check_one_body(xs, enabled, nu):
    n = len(xs)
    grid = [q / GRID_SIZE for q in range(GRID_SIZE)]
    points = list(xs) + grid
    weights = [1 / n] * n + [-mu(x) / GRID_SIZE for x in grid]
    def f(x, m=0):
        return (TAU ** m * sin(TAU * x + m * pi / 2)
                + 0.3 * (2 * TAU) ** m * cos(2 * TAU * x + m * pi / 2))
    direct = sum((drift_b(x) + sum(force(x - y, enabled)
                                  for j, y in enumerate(xs) if i != j) / n)
                 * f(x, 1) + nu * f(x, 2) for i, x in enumerate(xs)) / n
    direct -= sum(f(x) * (-velocity(x, enabled, 1) * mu(x)
                          - velocity(x, enabled) * mu(x, 1) + nu * mu(x, 2))
                  for x in grid) / GRID_SIZE
    rhs = 0.
    for w, x in zip(weights, points):
        response = sum(mu(z) * force(z - x, enabled) * f(z, 1)
                       for z in grid) / GRID_SIZE
        rhs += w * (velocity(x, enabled) * f(x, 1) + nu * f(x, 2) + response)
    rhs += sum(weights[a] * weights[b] * force(x - y, enabled)
               * (f(x, 1) - f(y, 1)) / 2
               for a, x in enumerate(points) for b, y in enumerate(points)
               if not (a < n and b < n and a == b))
    return direct, rhs


def main():
    configs = [(0.07, 0.36), (0.11, 0.42, 0.79), (0.2, 0.2), (0.1, 0.1, 0.45)]
    worst_pair = 0.
    worst_one = 0.
    pair_checks = 0
    one_checks = 0
    for xs, enabled, nu in product(configs, (0, 1), (1 / 3, 2.)):
        left, right = check_one_body(xs, enabled, nu)
        error = abs(left - right)
        assert error < TOLERANCE, ("one-body", xs, enabled, nu, left, right)
        worst_one = max(worst_one, error)
        one_checks += 1
        for phi in KERNELS:
            left, right = check_pair(xs, enabled, nu, phi)
            error = abs(left - right)
            assert error < TOLERANCE, ("pair", xs, enabled, nu, phi.name, left, right)
            worst_pair = max(worst_pair, error)
            pair_checks += 1
    print("Python", platform.python_version())
    print("Status: EXPLORATORY constructor self-check; no random inputs")
    print("Quadrature grid:", GRID_SIZE, "points; tolerance:", TOLERANCE)
    print("One-body checks:", one_checks, "maximum absolute error:", format(worst_one, ".3e"))
    print("Pair checks:", pair_checks, "maximum absolute error:", format(worst_pair, ".3e"))
    print("N=2,3; positive and zero force; nu=1/3,2; nonconstant positive background;")
    print("constant, separable, difference-mode, one-body-sum, mixed-mode kernels;")
    print("both distinct and coincident coordinates. PASS")


if __name__ == "__main__":
    main()
