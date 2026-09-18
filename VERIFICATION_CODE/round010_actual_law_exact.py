#!/usr/bin/env python3
"""Independent exact finite-Fourier diagnostics for TASK-061.

Only Python's standard library is used. Derivatives are divided by 2*pi;
the physical generator is (2*pi)^2 times the one implemented here. All
coefficients lie in Q(i). This checks coefficients, not the singular proof.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from pathlib import Path
import hashlib
import json


@dataclass(frozen=True)
class C:
    r: F = F(0)
    i: F = F(0)

    def __add__(self, other):
        other = cv(other)
        return C(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-cv(other))

    def __mul__(self, other):
        other = cv(other)
        return C(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def conj(self):
        return C(self.r, -self.i)


def cv(x):
    return x if isinstance(x, C) else C(F(x))


ZERO = C()
I = C(F(0), F(1))
assertions = 0


def check(x, message):
    global assertions
    if not x:
        raise AssertionError(message)
    assertions += 1


def clean(p):
    return {k: v for k, v in p.items() if v != ZERO}


def add(*polys):
    p = {}
    for q in polys:
        for k, v in q.items():
            p[k] = p.get(k, ZERO) + v
    return clean(p)


def scale(p, a):
    return clean({k: cv(a) * v for k, v in p.items()})


def mul(p, q):
    z = {}
    for k, v in p.items():
        for l, w in q.items():
            m = tuple(a + b for a, b in zip(k, l))
            z[m] = z.get(m, ZERO) + v * w
    return clean(z)


def deriv(p, j):
    return clean({k: I * k[j] * v for k, v in p.items()})


def haar(p, n):
    return p.get((0,) * n, ZERO)


def cosmode(k, a=F(1)):
    return {tuple(k): C(a / 2), tuple(-x for x in k): C(a / 2)}


def lift(p, slots, n):
    out = {}
    for k, v in p.items():
        full = [0] * n
        for j, a in zip(slots, k):
            full[j] += a
        key = tuple(full)
        out[key] = out.get(key, ZERO) + v
    return clean(out)


def partial_y(p):
    return {(k[0],): v for k, v in p.items() if k[1] == 0}


def eval_grid(p, points):
    roots = (C(F(1)), I, C(F(-1)), -I)
    z = ZERO
    for k, v in p.items():
        z += v * roots[sum(a * b for a, b in zip(k, points)) % 4]
    return z


def generator(p, n, nu, g):
    out = {}
    force = scale(deriv(g, 0), -1)
    for i in range(n):
        out = add(out, scale(deriv(deriv(p, i), i), nu))
        dpi = deriv(p, i)
        for j in range(n):
            if i == j:
                continue
            kij = lift({(k[0], -k[0]): v for k, v in force.items()},
                       (i, j), n)
            out = add(out, scale(mul(kij, dpi), F(1, n)))
    return out


def literal_p(psi, n):
    q = partial_y(psi)
    c = haar(q, 1)
    out = {(0,) * n: c * F(1, 2)} if c != ZERO else {}
    for i in range(n):
        out = add(out, scale(lift(q, (i,), n), F(-1, n)))
        for j in range(n):
            if i != j:
                out = add(out, scale(lift(psi, (i, j), n), F(1, 2*n*n)))
    return out


def check_pair_gradient(psi, n):
    p = literal_p(psi, n)
    g = deriv(psi, 0)
    a = partial_y(g)
    for i in range(n):
        rhs = scale(lift(a, (i,), n), F(-1, n))
        for j in range(n):
            if i != j:
                rhs = add(rhs, scale(lift(g, (i, j), n), F(1, n*n)))
        check(deriv(p, i) == rhs, f"literal gradient N={n}, i={i}")


def check_triple(psi, n, nu, g):
    grad = deriv(psi, 0)
    a = partial_y(grad)
    h = add(grad, scale(lift(a, (0,), 2), -1))
    check(partial_y(h) == {}, "partner centering")
    q = mul(lift(h, (0, 1), n), lift(h, (0, 2), n))
    check(haar(q, n) == ZERO, "zero initial triple")
    dq = haar(generator(q, n, nu, g), n)
    d = scale(deriv(deriv(g, 0), 0), -1)
    d23 = lift({(k[0], -k[0]): v for k, v in d.items()}, (1, 2), n)
    energy = haar(mul(q, d23), n)
    check(energy.i == 0 and energy.r >= 0, "D convolution energy positivity")
    check(dq == energy * F(-2, n), "initial derivative -2/N")
    for slots in ((0, 1), (0, 2)):
        dij = lift({(k[0], -k[0]): v for k, v in d.items()}, slots, n)
        check(haar(mul(q, dij), n) == ZERO, "partial contraction vanishes")
    return str(energy.r)


def check_energy(g, n, points):
    h = ZERO
    for i in range(n):
        for j in range(i + 1, n):
            h += eval_grid(g, ((points[i] - points[j]) % 4,)) * F(1, n)
    spectral = ZERO
    roots = (C(F(1)), I, C(F(-1)), -I)
    for k, coefficient in g.items():
        eta = sum((roots[(k[0]*x) % 4] for x in points), ZERO) * F(1, n)
        spectral += coefficient * eta * eta.conj()
    rhs = spectral * F(n, 2) - eval_grid(g, (0,)) * F(1, 2)
    check(h == rhs, "smooth Fourier energy exact deleted diagonal")
    check(spectral.i == 0 and spectral.r >= 0, "positive Fourier quadratic form")


def main():
    root = Path(__file__).resolve().parents[1]
    input_root = root / "COPIED_INPUTS" if (root / "COPIED_INPUTS").is_dir() else root
    manifest = root / "AUDITS/ROUND_010_LAW_FALSIFICATION_INPUT_SHA256SUMS.txt"
    inputs = []
    for line in manifest.read_text().splitlines():
        digest, name = line.split("  ", 1)
        actual = hashlib.sha256((input_root/name).read_bytes()).hexdigest()
        check(actual == digest, "input hash: " + name)
        inputs.append({"path": name, "sha256": actual})
    check(len(inputs) == 20, "twenty inputs only")

    tests = [
        cosmode((1, 1)),
        cosmode((1, -1)),
        add(cosmode((2, 1)), cosmode((1, 2))),
        add(cosmode((1, 0)), cosmode((0, 1))),
        add(cosmode((2, -2), F(2, 3)), cosmode((1, 1), F(1, 4)),
            cosmode((2, 1), F(1, 5)), cosmode((1, 2), F(1, 5))),
        {(0, 0): C(F(3, 7))},
    ]
    kernels = [cosmode((1,), F(2)),
               add(cosmode((1,), F(2)), cosmode((2,), F(1, 3)),
                   cosmode((3,), F(1, 5)))]
    energies = []
    for psi in tests:
        check(psi == {tuple(reversed(k)): v for k, v in psi.items()}, "pair symmetry")
        for n in (2, 3, 4, 5):
            check_pair_gradient(psi, n)
        for n in (3, 4, 5):
            for nu in (F(0), F(1, 3), F(7)):
                for g in kernels:
                    energies.append(check_triple(psi, n, nu, g))

    for g in kernels:
        for n in range(2, 10):
            for shift in range(4):
                for step in (0, 1, 2, 3):
                    points = [(shift+i*step) % 4 for i in range(n)]
                    check_energy(g, n, points)

    for d in range(3, 13):
        for s in (F(1, 2), F(d-2, 2), F(d-2)):
            alpha = (F(d)-s)/2
            q = 1-s/d
            r = (5*F(d)-s+2)/2
            gamma = q/(2*r)
            check(alpha > 0 and q > 0, "positive heat and rate exponents")
            check(-2*alpha/d == -q, "heat truncation error exponent")
            check(s/d-1 == -q, "deleted self-energy exponent")
            check(-q+gamma*r == -q/2, "chosen smoothing rate")
            check(r >= 2*d+1, "smoothing exponent dominates trace bound")

    result = {
        "status": "PASS", "assertions": assertions,
        "scope": "Exact finite Fourier coefficients, label counts, and exponent diagnostics; not a singular stochastic proof.",
        "arithmetic": "Q(i), exact fractions; no numerical tolerances or random seed",
        "normalization": "derivatives divided by 2*pi; physical generator multiplies by (2*pi)^2; a physical gradient-product derivative multiplies by (2*pi)^4",
        "nonzero_initial_convolution_energies": sorted(set(energies)-{"0"}),
        "input_manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
        "inputs": inputs,
    }
    out = root/"VERIFICATION_CODE/round010_actual_law_exact_output.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "PASS", "assertions": assertions,
                      "result": str(out)}, sort_keys=True))


if __name__ == "__main__":
    main()
