#!/usr/bin/env python3
"""AUD065 independent diagnostics. Standard library only; no external inputs.

Exact Gaussian-rational Fourier algebra and direct finite-label evaluations
are separate from an approximate transverse-mode summation of the singular
four-dimensional grid. None of these finite checks proves the limiting claim.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform


class C:
    """A Gaussian rational; no floating point enters the exact checks."""
    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)

    def __add__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-other if isinstance(other, C) else -C(other))

    def __mul__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (F(1) / other)

    def __eq__(self, other):
        other = other if isinstance(other, C) else C(other)
        return self.r == other.r and self.i == other.i

    def conj(self):
        return C(self.r, -self.i)

    def norm2(self):
        return self.r * self.r + self.i * self.i

    def record(self):
        return {"real": str(self.r), "imag": str(self.i)}


def add(*polys):
    result = {}
    for p in polys:
        for k, v in p.items():
            result[k] = result.get(k, C()) + v
    return {k: v for k, v in result.items() if v != 0}


def mul(p, q):
    result = {}
    for k, v in p.items():
        for ell, w in q.items():
            result[k + ell] = result.get(k + ell, C()) + v * w
    return {k: v for k, v in result.items() if v != 0}


def scale(p, c):
    return {k: v * c for k, v in p.items()}


def derivative(p):
    # D = (2*pi)^(-1) d/dx.
    return {k: C(0, k) * v for k, v in p.items() if k}


def force_convolution(p, prefactor=F(1)):
    # K/(2*pi), with ghat(k)=1/k^2.
    return {k: C(0, -prefactor / k) * v for k, v in p.items() if k}


def integral(p):
    return p.get(0, C())


def cos_poly(k):
    return {k: C(F(1, 2)), -k: C(F(1, 2))} if k else {0: C(1)}


def sin_poly(k):
    return {k: C(0, F(-1, 2)), -k: C(0, F(1, 2))}


ROOTS = [C(1), C(0, 1), C(-1), C(0, -1)]


def ev(p, quarter):
    return sum((v * ROOTS[(k * quarter) % 4] for k, v in p.items()), C())


def exact_diagnostics():
    checks = 0
    mutations = {}

    def check(condition, label):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    # This rational inequality is sufficient for the analytic Robin sign.
    check(F(17, 15) ** 4 - 1 < 1, "theta upper bound")
    check(sum(F(3) ** k / math.factorial(k) for k in range(5)) > 16,
          "e^3 > 16 via positive series")

    coefficient_rows = []
    for p in range(1, 5):
        u = sin_poly(p)
        r1 = scale(derivative(u), -1)
        r2 = scale(derivative(derivative(mul(u, u))), F(1, 2))
        check(integral(r1) == 0 and integral(r2) == 0, "density mass")
        for q in range(11):
            h = cos_poly(q)
            quadratic = integral(mul(mul(derivative(h),
                                         force_convolution(r1)), r1))
            linear2 = integral(mul(derivative(h), force_convolution(r2)))
            background2 = -integral(mul(h, r2))
            raw2 = quadratic + linear2
            original2 = raw2 - background2
            expected = C(F(-p * p, 2)) if q == 2 * p else C()
            check(linear2 == background2, "Coulomb original background")
            check(quadratic == expected, "independent Fourier resonance")
            check(original2 == expected, "full density expansion")
            if p == 1 and q == 2:
                coefficient_rows.append({
                    "normalization": "coefficient of (2*pi)^4*t^2 at theta=0",
                    "quadratic": quadratic.record(),
                    "raw_pair": raw2.record(),
                    "subtracted_background": background2.record(),
                    "literal_source": original2.record(),
                })
                probes = {
                    "omit_original_background": raw2,
                    "reverse_background_sign": raw2 + background2,
                    "omit_pair_factor_one_half": 2 * raw2 - background2,
                    "halve_kernel_and_background": original2 / 2,
                }
                for name, wrong in probes.items():
                    check(wrong != expected, name)
                    mutations[name] = {
                        "detected": True, "wrong": wrong.record(),
                        "correct": expected.record(),
                    }

    # Direct finite-label evaluation, independent of the density expansion.
    # Repeated coordinates are legitimate here: these are smooth diagnostics.
    g = {1: C(1), -1: C(1), 2: C(F(1, 4)), -2: C(F(1, 4))}
    kg = scale(derivative(g), -1)
    h = {1: C(1)}  # Complex Fourier probe; identities are complex-linear.
    v = derivative(h)
    smooth_self = ev(g, 0)
    detected = {name: 0 for name in [
        "omit_energy_self", "divide_energy_self_by_N",
        "replace_source_N_squared_by_falling_factorial",
        "replace_constant_pair_fraction_by_one",
    ]}
    finite_rows = []
    for n in range(2, 9):
        for offset in range(4):
            x = [(j * j + offset * j + 1) % 4 for j in range(n)]
            eta = lambda k: sum((ROOTS[(-k * z) % 4] for z in x), C()) / n
            rho = lambda k: C() if k == 0 else eta(k)
            direct_energy = sum((ev(g, x[i] - x[j])
                                 for i in range(n) for j in range(i + 1, n)), C()) / n
            spectral_full = sum((a * eta(k).norm2() for k, a in g.items()), C()) * F(n, 2)
            energy_formula = spectral_full - smooth_self / 2
            check(direct_energy == energy_formula, "finite energy self subtraction")
            detected["omit_energy_self"] += direct_energy != spectral_full
            detected["divide_energy_self_by_N"] += direct_energy != spectral_full - smooth_self / (2*n)

            ordered_j = sum((
                ev(kg, x[i] - x[j]) * (ev(v, x[i]) - ev(v, x[j]))
                for i in range(n) for j in range(n) if i != j
            ), C())
            # In D-coordinates the original contraction is A=-h.
            background = -sum((ev(h, z) for z in x), C()) / n
            literal = ordered_j / (2*n*n) - background
            centered_fourier = sum((
                a * k * rho(k) * rho(-1-k) for k, a in g.items()
            ), C())
            check(literal == centered_fourier, "literal deleted source versus Fourier product")
            wrong_source = ordered_j / (2*n*(n-1)) - background
            detected["replace_source_N_squared_by_falling_factorial"] += wrong_source != literal

            # Exact coefficient of an auxiliary constant in g=g_r+Q-c.
            constant = F(3, 7)
            e_r = spectral_full / n
            s_r = C(constant * F(n-1, 2*n))
            right = e_r + s_r - smooth_self / (2*n) - constant * F(n-1, 2*n)
            check(right == direct_energy / n, "energy split self and background")
            wrong = e_r + s_r - smooth_self / (2*n) - constant / 2
            detected["replace_constant_pair_fraction_by_one"] += wrong != direct_energy / n
            finite_rows.append({"N": n, "offset": offset,
                                "source": literal.record(), "energy": direct_energy.record()})
    for name, count in detected.items():
        check(count > 0, "mutation has detecting cases: " + name)
        mutations[name] = {"detected": True, "detecting_cases": count, "cases": len(finite_rows)}
    return {
        "status": "PASS", "exact_assertions": checks,
        "arithmetic": "fractions.Fraction Gaussian rationals; no tolerance",
        "density_coefficient": coefficient_rows,
        "finite_label_cases": len(finite_rows),
        "mutations": mutations,
    }


def radial_counts(dim, cutoff):
    counts = Counter()
    for vector in product(range(-cutoff, cutoff+1), repeat=dim):
        n2 = sum(v*v for v in vector)
        if n2:
            counts[n2] += 1
    return sorted(counts.items())


def transverse_kernels(m, z, radial):
    """Cube-truncated exact transverse Fourier representation, z in (0,1)."""
    force = 4*math.pi**2 * (0.5-z)
    potential = 2*math.pi**2 * (z*z-z+F(1, 6))
    for n2, multiplicity in radial:
        radius = math.sqrt(n2)
        b = 2*math.pi*m*radius
        low = math.exp(-b*z)
        high = math.exp(-b*(1-z))
        denom = -math.expm1(-b)
        force += 2*math.pi**2*multiplicity*(low-high)/denom
        potential += math.pi*multiplicity*(low+high)/(m*radius*denom)
    return force, potential


def force_tail_bound(m, cutoff):
    # min(m*z,m*(1-z)) >= 1/2 for every pair used below.
    q = math.exp(-math.pi)
    r = cutoff+1
    sum_j2 = q**r * (r*r/(1-q) + 2*r*q/(1-q)**2
                      + q*(1+q)/(1-q)**3)
    tail = 24*sum_j2 + 2*q**r/(1-q)
    return 4*math.pi**2*tail/(1-math.exp(-2*math.pi*m))


def approximate_singular_probe():
    cutoff = 12
    radial = radial_counts(3, cutoff)
    robin = 2*sum(mult*math.exp(-math.pi*n2)/n2
                  for n2, mult in radial_counts(4, 4)) - 2*math.pi
    a = 0.05
    target = -8*math.pi**4*a*a
    rows = []
    for m in (8, 12, 16, 24, 32, 48, 64, 96, 192):
        t = a/m
        y = [j/m + t*math.sin(2*math.pi*j/m) for j in range(m)]
        h = [math.cos(4*math.pi*x) for x in y]
        hp = [-4*math.pi*math.sin(4*math.pi*x) for x in y]
        source_terms = []
        potential_changes = []
        min_scaled = m
        for j in range(m):
            for k in range(j+1, m):
                z = (y[j]-y[k]) % 1
                z0 = ((j-k)/m) % 1
                min_scaled = min(min_scaled, m*z, m*(1-z))
                force, potential = transverse_kernels(m, z, radial)
                _, base_potential = transverse_kernels(m, z0, radial)
                source_terms.append(force*(hp[j]-hp[k]))
                potential_changes.append(potential-base_potential)
        if min_scaled < 0.5:
            raise AssertionError("outside analytic transverse-tail separation")
        raw_scaled = math.fsum(source_terms)
        background_correction_scaled = 4*math.pi**2*m*math.fsum(h)
        scaled_source = raw_scaled + background_correction_scaled
        scaled_energy = 0.5*(1-1/(m*m))*robin + math.fsum(potential_changes)
        tail = force_tail_bound(m, cutoff)
        rows.append({
            "m": m, "N": m**4, "a": a,
            "m_squared_times_literal_source_at_theta_zero": scaled_source,
            "target_at_theta_zero": target,
            "absolute_error": abs(scaled_source-target),
            "wrong_without_background": raw_scaled,
            "H_N_over_m_squared": scaled_energy,
            "minimum_first_coordinate_gap_times_m": min_scaled,
            "scaled_source_analytic_cube_tail_bound": 4*math.pi*m*m*tail,
        })
    validations = {
        "error_decreased": rows[-1]["absolute_error"] < rows[0]["absolute_error"],
        "original_0_002_tolerance": rows[-1]["absolute_error"] < 0.002,
        "negative_energy_probe": all(row["H_N_over_m_squared"] < -2 for row in rows),
        "omitted_background_detected": abs(rows[-1]["wrong_without_background"]-target) > 1,
    }
    if not all(validations.values()):
        raise AssertionError(validations)
    return {
        "status": "PASS_SUPPORTING_ONLY",
        "arithmetic": "Python binary64; deterministic, no random seed",
        "transverse_cube_cutoff": cutoff,
        "robin_four_dimensional_cube_cutoff": 4,
        "robin_approximation": robin,
        "tail_scope": "Analytic truncation bound only; floating-roundoff is not interval certified.",
        "expected_absolute_limit_for_a": 16*math.pi**3*a*a,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "audit": "AUD065 / TASK100",
        "diagnostic": "new independent exact Fourier/finite-label and transverse singular probes",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact": exact_diagnostics(),
        "approximate": approximate_singular_probe(),
        "epistemic_scope": "Finite diagnostics support the analytic proof and do not certify it.",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "exact": result["exact"]["status"],
        "exact_assertions": result["exact"]["exact_assertions"],
        "detected_mutations": len(result["exact"]["mutations"]),
        "approximate": result["approximate"]["status"],
        "last_row": result["approximate"]["rows"][-1],
    }, indent=2))


if __name__ == "__main__":
    main()
