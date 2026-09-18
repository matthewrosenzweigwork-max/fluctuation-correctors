#!/usr/bin/env python3
"""Fresh exact smooth/Fourier checks for TASK103; no prior checker is read.

Spatial dimension two is embedded in T^4. All derivatives/generators are
divided by (2*pi)^2, so rational Fourier coefficients suffice. This is a
finite smooth algebra diagnostic, never a simulation of singular dynamics.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


Poly = dict[tuple[int, ...], F]
counts: Counter[str] = Counter()
mutations: dict[str, dict] = {}


def clean(p: Poly) -> Poly:
    return {k: v for k, v in p.items() if v}


def add(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(p: Poly, c: F | int) -> Poly:
    return clean({k: v * c for k, v in p.items()})


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for a, x in p.items():
        for b, y in q.items():
            k = tuple(v + w for v, w in zip(a, b))
            out[k] = out.get(k, F(0)) + x * y
    return clean(out)


def conj(p: Poly) -> Poly:
    return {tuple(-v for v in k): c for k, c in p.items()}


def abs2(p: Poly) -> Poly:
    return mul(p, conj(p))


def twice_real(p: Poly) -> Poly:
    return add(p, conj(p))


def one(n: int) -> Poly:
    return {(0,) * (4 * n): F(1)}


def char(n: int, label: int, k: tuple[int, int], initial=False) -> Poly:
    a = [0] * (4 * n)
    off = 4 * label + (2 if initial else 0)
    a[off:off + 2] = k
    return {tuple(a): F(1)}


def mode(n: int, k: tuple[int, int], initial=False) -> Poly:
    return scale(add(*(char(n, i, k, initial) for i in range(n))), F(1, n))


def norm2(k) -> int:
    return sum(x * x for x in k)


def dot(a, b) -> int:
    return sum(x * y for x, y in zip(a, b))


def shift(key, i, j, m):
    a = list(key)
    for r in range(2):
        a[4 * i + r] += m[r]
        a[4 * j + r] -= m[r]
    return tuple(a)


def generator(p: Poly, n: int, nu: F, g) -> Poly:
    """Literal ordered N-particle generator acting only on current slots."""
    out: Poly = {}
    for key, c in p.items():
        sq = sum(key[4*i+r] ** 2 for i in range(n) for r in range(2))
        out[key] = out.get(key, F(0)) - nu * sq * c
        for i in range(n):
            ni = key[4*i:4*i+2]
            for j in range(n):
                if i == j:
                    continue
                for m, gm in g.items():
                    v = F(dot(m, ni), n) * gm * c
                    if v:
                        target = shift(key, i, j, m)
                        out[target] = out.get(target, F(0)) + v
    return clean(out)


def pair_source(n, i, j, k, g) -> Poly:
    """K(x-y).(grad e_k(x)-grad e_k(y)), derived from its two factors."""
    out: Poly = {}
    zero = (0,) * (4*n)
    for m, gm in g.items():
        force_mode = {shift(zero, i, j, m): gm * dot(m, k)}
        out = add(out, mul(force_mode, char(n, i, k)),
                  scale(mul(force_mode, char(n, j, k)), -1))
    return out


def canonical_pair(n, i, j, k, g) -> Poly:
    d = norm2(k) * g.get(k, F(0))
    return add(pair_source(n, i, j, k, g),
               scale(add(char(n, i, k), char(n, j, k)), d))


def haar_row(p, label):
    return {key: c for key, c in p.items()
            if key[4*label:4*label+2] == (0, 0)}


def initial_haar(p):
    """At time zero current and initial coordinates of each label coincide."""
    return sum((c for key, c in p.items()
                if all(key[4*i+r]+key[4*i+2+r] == 0
                       for i in range(len(key)//4) for r in range(2))), F(0))


def orbit(p):
    """Exact quotient by simultaneous current/initial label exchangeability."""
    out = {}
    for key, c in p.items():
        blocks = tuple(sorted(key[i:i+4] for i in range(0, len(key), 4)))
        out[blocks] = out.get(blocks, F(0)) + c
    return clean(out)


def check(category, actual, expected):
    assert actual == expected, (category, actual, expected)
    counts[category] += 1


def reject(name, good, bad, case):
    assert good != bad, ("vacuous mutation", name, case)
    counts["mutation:" + name] += 1
    if name not in mutations:
        if isinstance(good, dict):
            diff = add(good, scale(bad, -1))
            first = next(iter(sorted(diff, key=repr)))
            witness = {"coefficient_key": repr(first), "difference": str(diff[first])}
        else:
            witness = {"difference": str(good - bad)}
        mutations[name] = {"case": case, **witness}


def run():
    base_modes = [(1, 0), (0, 1), (1, 1), (2, 0)]
    kernels = []
    for variant in range(2):
        g = {}
        for m in base_modes:
            amp = F(1, norm2(m)) if variant == 0 else F(2+norm2(m), 3*norm2(m))
            g[m] = amp
            g[tuple(-a for a in m)] = amp
        kernels.append(g)

    for variant, g in enumerate(kernels):
        for k in base_modes:
            d = norm2(k) * g[k]
            j2 = pair_source(2, 0, 1, k, g)
            check("row response sign", haar_row(j2, 1), scale(char(2, 0, k), -d))
            check("zero full Haar contraction", initial_haar(j2), F(0))
            check("canonical first row", haar_row(canonical_pair(2, 0, 1, k, g), 1), {})
            check("canonical second row", haar_row(canonical_pair(2, 0, 1, k, g), 0), {})
            for n in range(2, 7):
                case = {"N": n, "mode": k, "kernel_variant": variant}
                z, z0 = mode(n, k), mode(n, k, True)
                raw = add(*(pair_source(n, i, j, k, g)
                            for i in range(n) for j in range(n) if i != j))
                canon = add(*(canonical_pair(n, i, j, k, g)
                              for i in range(n) for j in range(n) if i != j))
                p = add(scale(raw, F(1, 2*n*n)), scale(z, d))
                u = scale(canon, F(1, 2*n*n))
                check("finite N row compensation", p, add(u, scale(z, d/n)))
                reject("omit contact d_over_N", p, u, case)
                reject("reverse contact sign", p, add(u, scale(z, -d/n)), case)
                reject("delete ordered pair half", p, add(scale(raw, F(1, n*n)), scale(z, d)), case)
                reject("reverse background sign", p, add(scale(raw, F(1, 2*n*n)), scale(z, -d)), case)
                reject("falling factorial denominator", p,
                       add(scale(raw, F(1, 2*n*(n-1))), scale(z, d)), case)

                a2 = mul(canonical_pair(n, 0, 1, k, g), conj(char(n, 0, k)))
                b2 = mul(canonical_pair(n, 0, 1, k, g), conj(char(n, 0, k, True)))
                a3 = mul(canonical_pair(n, 0, 1, k, g), conj(char(n, 2, k))) if n >= 3 else {}
                b3 = mul(canonical_pair(n, 0, 1, k, g), conj(char(n, 2, k, True))) if n >= 3 else {}
                w2, w3 = F(n-1, n), F((n-1)*(n-2), 2*n)
                full_f, full_g = orbit(scale(mul(u, conj(z)), n)), orbit(scale(mul(u, conj(z0)), n))
                check("same time overlap coefficients", full_f, orbit(add(scale(a2, w2), scale(a3, w3))))
                check("two time overlap coefficients", full_g, orbit(add(scale(b2, w2), scale(b3, w3))))
                reject("pair overlap extra N", full_f, orbit(add(scale(a2, w2/n), scale(a3, w3))), case)
                reject("mixed pair overlap extra N", full_g, orbit(add(scale(b2, w2/n), scale(b3, w3))), case)
                if n >= 3:
                    reject("triple overlap missing half", full_f, orbit(add(scale(a2, w2), scale(a3, 2*w3))), case)
                    reject("mixed triple missing half", full_g, orbit(add(scale(b2, w2), scale(b3, 2*w3))), case)
                else:
                    check("N2 triple coefficient", w3, F(0))
                for p0 in (a2, b2, a3, b3):
                    check("iid canonical mixed means", initial_haar(p0), F(0))

                for a in (F(1, 3), F(3, 5), F(1)):
                    xi = add(z, scale(z0, -a))
                    xi1 = add(char(n, 0, k), scale(char(n, 0, k, True), -a))
                    xi2 = add(char(n, 1, k), scale(char(n, 1, k, True), -a))
                    endpoint = orbit(scale(abs2(xi), n))
                    decomposition = orbit(add(abs2(xi1), scale(mul(xi1, conj(xi2)), n-1)))
                    check("endpoint self and distinct labels", endpoint, decomposition)
                    reject("endpoint N instead Nminus1", endpoint,
                           orbit(add(abs2(xi1), scale(mul(xi1, conj(xi2)), n))), {**case, "a": str(a)})

                for nu in (F(0), F(1, 7), F(3, 2)):
                    case_nu = {**case, "nu": str(nu)}
                    ell = norm2(k)
                    alpha = d + nu*ell
                    corrected = alpha - d/n
                    lz = generator(z, n, nu, g)
                    check("literal one body duality", lz, add(scale(z, -alpha), p))
                    reject("response sign", lz, add(scale(z, d-nu*ell), p), case_nu)
                    lv = scale(generator(abs2(z), n, nu, g), n)
                    variance_rhs = add(scale(abs2(z), -2*corrected*n),
                                       scale(one(n), 2*nu*ell),
                                       scale(twice_real(mul(u, conj(z))), n))
                    check("variance generator including Ito diagonal", lv, variance_rhs)
                    if nu:
                        reject("Ito bracket missing two", lv,
                               add(variance_rhs, scale(one(n), -nu*ell)), case_nu)
                    rpoly = scale(mul(z, conj(z0)), n)
                    check("mixed endpoint generator", generator(rpoly, n, nu, g),
                          add(scale(rpoly, -corrected), scale(mul(u, conj(z0)), n)))
                    pair = mul(char(n, 0, k), conj(char(n, 1, k)))
                    same = mul(char(n, 0, k), conj(char(n, 0, k, True)))
                    other = mul(char(n, 0, k), conj(char(n, 1, k, True)))
                    cp = initial_haar(generator(pair, n, nu, g))
                    sp = initial_haar(generator(same, n, nu, g))
                    op = initial_haar(generator(other, n, nu, g))
                    vp = initial_haar(lv)
                    check("initial pair BBGKY", cp, -2*d/n)
                    check("initial same tag", sp, -nu*ell)
                    check("initial distinct tag", op, -d/n)
                    check("initial empirical variance", vp, -2*d*F(n-1, n))
                    check("initial endpoint defect derivative", vp-2*(sp+(n-1)*op), 2*nu*ell)
                    check("initial source first cross", initial_haar(mul(p, conj(z))), d/(n*n))
                    reject("initial BBGKY sign", cp, 2*d/n, case_nu)
                    reject("initial BBGKY missing two", cp, -d/n, case_nu)

    # Coulomb atom and compensation, including the constant response.
    for k in [(0, 0), (1, 0), (7, -3)]:
        true_d = F(int(k != (0, 0)))
        atom_only = F(1)
        compensation_only = F(-int(k == (0, 0)))
        check("compensated Coulomb mass", true_d, atom_only+compensation_only)
        if k == (0, 0):
            reject("Coulomb omit compensation", -true_d, -atom_only, {"mode": k})
        else:
            reject("Coulomb omit atom", -true_d, -compensation_only, {"mode": k})

    check("critical radial source square exponent", 4-1-2*2, -1)
    check("Coulomb positive occupation coefficient", 2*(4-2-2), 0)
    check("critical inverse temperature exponent", F(2, 4)-1, F(-1, 2))
    check("critical response test polynomial domination exponent", F(4-2, 2)+(4+2)+3, F(10))

    result = {
        "status": "PASS",
        "assertions": sum(counts.values()),
        "categories": dict(sorted(counts.items())),
        "nonvacuous_mutations": mutations,
        "arithmetic": "exact fractions; sparse Fourier polynomials; no random seed or tolerance",
        "normalization": "generator, source and Coulomb constant divided by (2*pi)^2; dimension two embedded in T^4",
        "scope": "finite smooth algebra support only; no singular evolution or limiting estimate certified",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_name('DIAGNOSTIC_RESULT.json')
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(f"PASS: {result['assertions']} exact assertions, {len(counts)} categories, {len(mutations)} nonvacuous mutations")


if __name__ == '__main__':
    run()
