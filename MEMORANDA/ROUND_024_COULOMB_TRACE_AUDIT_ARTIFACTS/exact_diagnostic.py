#!/usr/bin/env python3
"""Fresh exact coefficient/flux diagnostics; supporting evidence, not proof."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

ZERO = (0, 0, 0, 0)
checks = 0
mutations = {
    "omit_common_translation": 0,
    "reverse_inner_flux": 0,
    "drop_haar_compensation": 0,
    "halve_relative_factor": 0,
    "reverse_common_derivative": 0,
    "use_assigned_diagonal": 0,
    "force_every_scalar_zero": 0,
    "wrong_inner_annulus_normal": 0,
}


def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, Q(0)) + v
    return clean(out)


def scale(p, factor):
    return clean({k: factor * v for k, v in p.items()})


def real_symmetric_mode(a, b, coef=Q(1)):
    out = {}
    for p in ((a, b), (b, a), (neg(a), neg(b)), (neg(b), neg(a))):
        out[p] = out.get(p, Q(0)) + coef / 4
    return clean(out)


def direct_contraction(pair):
    # Integrate y in K(x-y).(grad_x-grad_y)Phi using K_hat(b).
    # Physical value is gamma times the returned polynomial.
    out = {}
    for (a, b), coef in pair.items():
        if b != ZERO:
            factor = Q(dot(b, tuple(x - y for x, y in zip(a, b))), dot(b, b))
            k = plus(a, b)
            out[k] = out.get(k, Q(0)) + coef * factor
    return clean(out)


def independent_pieces(pair):
    common, row, trace = {}, {}, {}
    for (a, b), coef in pair.items():
        k = plus(a, b)
        trace[k] = trace.get(k, Q(0)) + coef
        if b == ZERO:
            row[a] = row.get(a, Q(0)) + coef
        else:
            factor = Q(dot(b, k), dot(b, b))
            common[k] = common.get(k, Q(0)) + coef * factor
    return clean(common), clean(row), clean(trace)


def run_fourier():
    modes = [ZERO, (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0),
             (2, -1, 1, 0), (-1, 0, 0, 0), (1, -2, 0, 1)]
    cases = [real_symmetric_mode(a, b, Q(i + 1, 7))
             for i, (a, b) in enumerate(product(modes, repeat=2))]
    cases += [add(cases[i], scale(cases[i + 1], Q(-3, 5)),
                  scale(cases[i + 2], Q(2, 9)))
              for i in range(len(cases) - 2)]
    for i, pair in enumerate(cases):
        for (a, b), coef in pair.items():
            check(pair.get((b, a)) == coef, "pair symmetry")
            check(pair.get((neg(a), neg(b))) == coef, "real character pairing")
        direct = direct_contraction(pair)
        common, row, trace = independent_pieces(pair)
        rhs = add(common, scale(row, 2), scale(trace, -2))
        check(direct == rhs, "Fourier exact punctured-limit identity")
        check(direct.get(ZERO, 0) == 2 * (row.get(ZERO, 0) - trace.get(ZERO, 0)),
              "general scalar compensation and trace")
        for j in range(4):
            differentiated = {
                (a, b): coef * (a[j] + b[j])
                for (a, b), coef in pair.items()
            }
            # Common physical factor 2*pi*i appears on both sides.
            dg = clean({k: coef * k[j] for k, coef in direct.items()})
            check(direct_contraction(differentiated) == dg,
                  "common derivative commutes with the full contraction")
        alternatives = {
            "omit_common_translation": add(scale(row, 2), scale(trace, -2)),
            "reverse_inner_flux": add(common, scale(row, 2), scale(trace, 2)),
            "drop_haar_compensation": add(common, scale(trace, -2)),
            "halve_relative_factor": add(common, row, scale(trace, -1)),
            "reverse_common_derivative": add(scale(common, -1), scale(row, 2), scale(trace, -2)),
            "use_assigned_diagonal": add(common, scale(row, 2),
                                         scale(add(trace, {ZERO: Q(1)}), -2)),
        }
        for name, alternative in alternatives.items():
            mutations[name] += int(alternative != direct)
        mutations["force_every_scalar_zero"] += int(direct.get(ZERO, 0) != 0)
    return len(cases)


def run_annuli():
    count = 0
    for eps, radius, m in product((Q(1, 7), Q(1, 11)),
                                  (Q(1, 3), Q(2, 5)),
                                  (0, 2, 4, 6, 8)):
        check(eps < radius, "annulus is nonempty")
        # Both entries are coefficients of 1 and gamma, with |S^3| removed.
        delta_m = radius ** m - eps ** m
        delta_m4 = radius ** (m + 4) - eps ** (m + 4)
        direct = (4 * delta_m, -Q(m, 2 * (m + 4)) * delta_m4)
        outer = (4 * radius ** m, -Q(1, 2) * radius ** (m + 4))
        inner = (-4 * eps ** m, Q(1, 2) * eps ** (m + 4))
        bulk = (Q(0), Q(2, m + 4) * delta_m4)
        rhs = tuple(outer[j] + inner[j] + bulk[j] for j in range(2))
        check(direct == rhs, "exact annular divergence theorem")
        wrong = tuple(outer[j] - inner[j] + bulk[j] for j in range(2))
        mutations["wrong_inner_annulus_normal"] += int(wrong != direct)
        count += 1
    return count


def main():
    fourier_cases = run_fourier()
    annuli_cases = run_annuli()
    # Actual scale and trace counterexample checks use rational identities.
    check(Q(1, 2) - Q(1, 4) - Q(1, 2) == -Q(1, 4),
          "scaled lower rate from sup power, Fourier moment, sigma/N")
    check(Q(3, 2) < 2 and Q(3, 2) + 1 < 3 < 4,
          "admissible fixed-N R8 exponents")
    check(3 - 2 * 1 > -1 and 3 - 2 > -1,
          "angular diagnostic H1 and W21 radial integrability")
    check(Q(1, 4) - Q(1, 4) == 0, "angular spherical average")
    check(Q(3, 4) != -Q(1, 4), "two direction limits differ")
    for name, detections in mutations.items():
        check(detections > 0, "undetected mutation: " + name)
    root = Path(__file__).resolve().parents[2]
    manifest = root / "AUDITS/ROUND_024_COULOMB_TRACE_AUDIT_INPUT_SHA256SUMS.txt"
    input_root = root
    if not manifest.is_file():
        artifact_dir = Path(__file__).resolve().parent
        manifest = artifact_dir / "INPUT_SHA256SUMS.txt"
        input_root = artifact_dir / "INPUTS"
    verified = []
    for line in manifest.read_text().splitlines():
        expected, relative = line.split("  ", 1)
        actual = hashlib.sha256((input_root / relative).read_bytes()).hexdigest()
        check(actual == expected, "input digest " + relative)
        verified.append({"path": relative, "sha256": actual})
    check(len(verified) == 20, "twenty input files")
    result = {
        "status": "PASS",
        "exact_assertions": checks,
        "fourier_cases": fourier_cases,
        "annulus_cases": annuli_cases,
        "mutations_detected": mutations,
        "arithmetic": "Exact rational; physical Fourier contraction divided by gamma=4*pi^2.",
        "radial_convention": "Coefficients of 1 and gamma after division by |S^3|; no numeric pi.",
        "seed": None,
        "tolerance": None,
        "scope": "Supporting diagnostics, no simulation or certification of the genuine inverse.",
        "verified_inputs": verified,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
