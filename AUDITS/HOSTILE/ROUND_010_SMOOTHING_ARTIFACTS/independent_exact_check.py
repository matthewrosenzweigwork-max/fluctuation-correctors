#!/usr/bin/env python3
"""New TASK065 diagnostics; standard library, exact rational arithmetic only.

Laurent characters are exp(2*pi*i*k.x). D_j below multiplies by k_j,
so physical differentiation is 2*pi*i*D_j. The force generator divided
by (2*pi)^2 is (1/N) sum D_i g_ij D_i - nu sum D_i^2.
This program contains no imported checker and reads only the allowed manifest
and its 22 files for integrity. Polynomial diagnostics are not analytic proofs.
"""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

COUNTS = Counter()


def check(condition, family, detail):
    if not condition:
        raise AssertionError(f"{family}: {detail}")
    COUNTS[family] += 1


def clean(p):
    return {e: F(c) for e, c in p.items() if c}


def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for e, c in p.items():
            out[e] += c
    return clean(out)


def scale(p, c):
    return clean({e: c*v for e, v in p.items()})


def mul(p, q):
    out = defaultdict(F)
    for e, c in p.items():
        for f, b in q.items():
            out[tuple(a+z for a, z in zip(e, f))] += c*b
    return clean(out)


def deriv(p, j):
    return clean({e: e[j]*c for e, c in p.items()})


def embed(p, slots, n):
    out = defaultdict(F)
    for e, c in p.items():
        dst = [0]*n
        for j, slot in enumerate(slots):
            dst[slot] += e[j]
        out[tuple(dst)] += c
    return clean(out)


def one(n, c=1):
    return {(0,)*n: F(c)}


def cosine(e, amplitude=1):
    return add({tuple(e): F(amplitude, 2)},
               {tuple(-k for k in e): F(amplitude, 2)})


def integ(p):
    return sum((c for e, c in p.items() if not any(e)), F(0))


def inner(p, q):
    # Integral of a literal product, without materializing irrelevant modes.
    return sum((c*q.get(tuple(-k for k in e), 0) for e, c in p.items()), F(0))


def project_y(p):
    return clean({(e[0],): c for e, c in p.items() if e[1] == 0})


def rowcenter(p):
    return add(p, scale(embed(project_y(p), [0], 2), -1))


def symmetric(p):
    return scale(add(p, {tuple(reversed(e)): c for e, c in p.items()}), F(1, 2))


def pair_statistic(v, n):
    out = scale(one(n), F(1, 2)*integ(v))
    q = project_y(v)
    for i in range(n):
        out = add(out, scale(embed(q, [i], n), -F(1, n)))
        for j in range(n):
            if i != j:
                out = add(out, scale(embed(v, [i, j], n), F(1, 2*n*n)))
    return out


def exchangeable_density(n, sign):
    out = one(n)
    pairs = n*(n-1)//2
    for i in range(n):
        for j in range(i+1, n):
            e = [0]*n
            e[i], e[j] = 1, -1
            out = add(out, scale(cosine(e), F(sign, 4*pairs)))
    if n >= 3:
        count = n*(n-1)*(n-2)//2
        for i in range(n):
            rest = [j for j in range(n) if j != i]
            for pos, j in enumerate(rest):
                for k in rest[pos+1:]:
                    e = [0]*n
                    e[i], e[j], e[k] = 2, -1, -1
                    out = add(out, scale(cosine(e), F(-sign, 8*count)))
    # Sum of absolute nonconstant coefficients <=3/8 proves F >=5/8.
    check(integ(out) == 1, "exchangeable_density", (n, sign, "mass"))
    check(sum(abs(c) for e, c in out.items() if any(e)) <= F(3, 8),
          "exchangeable_density", (n, sign, "positive lower bound"))
    return out


def check_pair_algebra():
    kernels = [one(2, 7),
               add(cosine((1, 0)), cosine((0, 1))),
               cosine((1, -1)),
               symmetric(add(cosine((2, 1)), scale(cosine((1, -3)), -F(2, 3)),
                             cosine((2, 0)), one(2, F(3, 7)))),
               symmetric(add(cosine((3, 2)), scale(cosine((2, -2)), F(5, 4))))]
    for n in (2, 3, 4, 5):
        densities = [one(n), exchangeable_density(n, 1), exchangeable_density(n, -1)]
        for vi, v in enumerate(kernels):
            stat = pair_statistic(v, n)
            G = deriv(v, 0)
            A = project_y(G)
            H = rowcenter(G)
            grads = []
            for i in range(n):
                literal = deriv(stat, i)
                deleted = scale(embed(A, [i], n), -F(1, n))
                empirical = scale(embed(A, [i], n), -F(1, n))
                centered = scale(embed(A, [i], n), -F(1, n*n))
                for j in range(n):
                    empirical = add(empirical, scale(embed(G, [i, j], n), F(1, n*n)))
                    if j != i:
                        deleted = add(deleted, scale(embed(G, [i, j], n), F(1, n*n)))
                        centered = add(centered, scale(embed(H, [i, j], n), F(1, n*n)))
                empirical = add(empirical, scale(embed(G, [i, i], n), -F(1, n*n)))
                check(literal == deleted == empirical == centered, "pair_gradient",
                      (n, vi, i, "literal / deleted / missing-self / centered"))
                grads.append(literal)
            raw_square = scale(add(*(mul(g, g) for g in grads)), -1)
            # -1 restores i^2 for a product of physical derivatives / (2*pi)^2.
            haar_expected = -(F(n-1, n**3)*inner(G, G)-F(n-2, n**3)*inner(A, A))
            check(integ(raw_square) == haar_expected, "haar_bracket", (n, vi))
            for fi, density in enumerate(densities):
                H12, A1 = embed(H, [0, 1], n), embed(A, [0], n)
                rhs = (n-1)*inner(mul(H12, H12), density)
                if n >= 3:
                    rhs += (n-1)*(n-2)*inner(mul(H12, embed(H, [0, 2], n)), density)
                rhs -= 2*(n-1)*inner(mul(H12, A1), density)
                rhs += inner(mul(A1, A1), density)
                rhs *= -F(1, n**3)
                check(inner(raw_square, density) == rhs, "four_term_law", (n, vi, fi))
                for nu in (F(1, 8), F(1), F(3)):
                    b = min(F(1)/nu, F(1))
                    actual = 2*nu*n*b*inner(raw_square, density)
                    check(actual == 2*nu*n*b*rhs, "physical_bracket", (n, vi, fi, str(nu)))
                    check(nu*b <= 1, "noise_factor", str(nu))


def check_heat_diagonal():
    spectrum = {-3: F(1, 11), -2: F(2, 7), -1: F(4, 5),
                1: F(4, 5), 2: F(2, 7), 3: F(1, 11)}
    g = {(k, -k): c for k, c in spectrum.items()}
    self_value = sum(spectrum.values())
    for n in range(2, 10):
        raw = {}
        spectral = one(n, -self_value/2)
        for i in range(n):
            for j in range(i+1, n):
                raw = add(raw, scale(embed(g, [i, j], n), F(1, n)))
        for k, c in spectrum.items():
            eta = add(*(scale(embed({(k,): F(1)}, [i], n), F(1, n)) for i in range(n)))
            conjugate = {tuple(-m for m in e): v for e, v in eta.items()}
            spectral = add(spectral, scale(mul(eta, conjugate), F(n, 2)*c))
        check(raw == spectral, "energy_self_diagonal", n)


def check_initial_generator():
    probes = [
        [cosine((0, 1))],
        [cosine((1, 1)), scale(cosine((2, -1)), F(2, 3))],
        [add(cosine((1, 2)), scale(cosine((2, 1)), -F(3, 4))),
         add(cosine((3, -2)), cosine((0, 3)))],
        [{}],
    ]
    for n in (3, 4, 5):
        for d, s in ((3, 1), (4, 1), (4, 2), (5, 1), (6, 4)):
            # Only finitely many Fourier coefficients can pair with the probes.
            # c_(d,s) is a positive overall factor restored in the analytic report.
            spec = {k: F(abs(k))**(s-d) for k in range(-8, 9) if k}
            g = {(k, -k): c for k, c in spec.items()}
            D = {(k, -k): k*k*c for k, c in spec.items()}
            for hi, components in enumerate(probes):
                check(all(project_y(h) == {} for h in components), "probe_centering", (n, d, s, hi))
                a = add(*(mul(embed(h, [0, 1], n), embed(h, [0, 2], n)) for h in components))
                check(integ(a) == 0, "initial_covariance", (n, d, s, hi))
                force_mean = F(0)
                for i in range(n):
                    ai = deriv(a, i)
                    for j in range(n):
                        if i != j:
                            force_mean += F(1, n)*inner(deriv(embed(g, [i, j], n), i), ai)
                d12 = inner(embed(D, [0, 1], n), a)
                d13 = inner(embed(D, [0, 2], n), a)
                d23 = inner(embed(D, [1, 2], n), a)
                check(d12 == d13 == 0, "partial_contraction_cancellation", (n, d, s, hi))
                check(d23 >= 0, "positive_fourier_form", (n, d, s, hi))
                check(force_mean == -F(2, n)*d23, "initial_BBGKY", (n, d, s, hi))
                if s == d-2:
                    norm = sum((inner(h, h) for h in components), F(0))
                    check(d23 == norm, "coulomb_atom_and_compensation", (n, d, s, hi))
                for nu in (F(0), F(1, 7), F(4)):
                    diffusion_mean = -nu*sum((integ(deriv(deriv(a, i), i)) for i in range(n)), F(0))
                    check(diffusion_mean == 0, "initial_diffusion", (n, d, s, hi, str(nu)))
                z = rowcenter(add(cosine((1, 3)), cosine((2, 0))))
                adot = add(*(add(mul(embed(z, [0, 1], n), embed(h, [0, 2], n)),
                                 mul(embed(h, [0, 1], n), embed(z, [0, 2], n))) for h in components))
                check(integ(adot) == 0, "time_dependent_centering", (n, d, s, hi))


def factor_integer(n):
    out = Counter()
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def formal_log(q):
    assert q > 0
    out = defaultdict(F)
    for p, m in factor_integer(q.numerator).items():
        out[p] += m
    for p, m in factor_integer(q.denominator).items():
        out[p] -= m
    return {p: v for p, v in out.items() if v}


def logsum(terms):
    out = defaultdict(F)
    for weight, arg in terms:
        for prime, coefficient in formal_log(arg).items():
            out[prime] += weight*coefficient
    return {p: v for p, v in out.items() if v}


def marginal_density(density, indices):
    out = defaultdict(F)
    n = len(next(iter(density)))
    for x, value in density.items():
        out[tuple(x[i] for i in indices)] += value/F(2**(n-len(indices)))
    return dict(out)


def check_entropy_chain():
    for n in range(2, 8):
        density = {x: 1+F(sum(x)**2-n, 2*n*(n-1)) for x in product((-1, 1), repeat=n)}
        check(sum(density.values()) == 2**n and min(density.values()) > 0,
              "finite_entropy_model", n)
        full = logsum((value/F(2**n), value) for value in density.values())
        conditional_terms = []
        for i in range(n):
            prefix = marginal_density(density, list(range(i)))
            extended = marginal_density(density, list(range(i+1)))
            for x, value in density.items():
                conditional_terms.append((value/F(2**n), extended[x[:i+1]]/prefix[x[:i]]))
        check(full == logsum(conditional_terms), "entropy_conditional_chain", n)
        for k in range(1, n+1):
            blocks = [list(range(j, min(n, j+k))) for j in range(0, n, k)]
            marginals = [marginal_density(density, block) for block in blocks]
            block_terms, kl_terms = [], []
            for block, marginal in zip(blocks, marginals):
                block_terms.extend((value/F(2**len(block)), value) for value in marginal.values())
            for x, value in density.items():
                prod_value = F(1)
                for block, marginal in zip(blocks, marginals):
                    prod_value *= marginal[tuple(x[i] for i in block)]
                kl_terms.append((value/F(2**n), value/prod_value))
            check(full == logsum(block_terms+kl_terms), "entropy_block_chain", (n, k))
            if 2*k <= n:
                check(F(n//k) >= F(n, 2*k), "entropy_block_count", (n, k))


def check_exponents():
    for d in range(3, 17):
        for s in (F(1, 16), F(d-2, 3), F(d-2, 2), F(d-2)-F(1, 16), F(d-2)):
            alpha = F(d-s, 2)
            q = 1-s/d
            rs = F(d+1, 2)+F(d+F(d-s, 2), 2)
            rstar = 2*rs
            gamma = q/(2*rstar)
            equalities = {
                "Fourier pi normalization": F(d, 2)-2*alpha == s-F(d, 2),
                "Euclidean power normalization": alpha-F(d, 2)+s/2 == 0,
                "self floor exponent": (-s/2)*(-F(2, d)) == s/d,
                "low heat floor exponent": 1+alpha*(-F(2, d)) == s/d,
                "Gaussian weighted sum": rs == F(5*d-s+2, 4),
                "smoothing rstar": rstar == F(5*d-s+2, 2),
                "diagonal dominated": rstar >= 2*d+1,
                "delta rate": -q+gamma*rstar == -q/2,
                "gamma expression": gamma == (d-s)/(d*(5*d-s+2)),
                "q interval": 0 < q < 1,
                "shrinking window": 1-s/(s+2) == 2/(s+2),
                "critical diffusivity": -q == s/d-1,
            }
            for key, value in equalities.items():
                check(value, "rational_exponents", (d, str(s), key))


def main():
    base = Path(__file__).resolve().parents[3]
    manifest = base/"AUDITS/ROUND_010_SMOOTHING_HOSTILE_INPUT_SHA256SUMS.txt"
    inputs = []
    for line in manifest.read_text().splitlines():
        expected, relative = line.split("  ", 1)
        actual = hashlib.sha256((base/relative).read_bytes()).hexdigest()
        check(actual == expected, "sealed_input", relative)
        inputs.append({"path": relative, "sha256": actual})
    check(len(inputs) == 22, "dossier_count", len(inputs))
    check_pair_algebra()
    check_heat_diagonal()
    check_initial_generator()
    check_entropy_chain()
    check_exponents()
    result = {
        "task": "TASK065", "outcome": "PASS", "assertions": sum(COUNTS.values()),
        "families": dict(sorted(COUNTS.items())), "inputs": inputs,
        "arithmetic": "fractions.Fraction and exact formal logarithms factored into prime logs",
        "fourier_convention": "D_j is physical differentiation divided by 2*pi*i; force generator divided by (2*pi)^2; squared gradients include the restored minus sign",
        "evidence_limit": "Exact finite Fourier / finite label / finite entropy diagnostics support the separate analytic review; no simulation or singular uniform-integrability certificate.",
        "randomness": "none", "floating_point": "none",
    }
    out = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if len(sys.argv) == 3 and sys.argv[1] == "--output":
        Path(sys.argv[2]).write_text(out)
    else:
        print(out, end="")


if __name__ == "__main__":
    main()
