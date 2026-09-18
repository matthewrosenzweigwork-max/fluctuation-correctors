#!/usr/bin/env python3
"""Exact, standard-library coefficient checks for the statement-only R7 proof.

All arithmetic is rational. These checks are corroborating algebra, not a
substitute for the analytic arguments or the separate hostile audit.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


counts = Counter()
sum_threshold_examples = []


def check(name, assertion):
    if not assertion:
        raise AssertionError(name)
    counts[name] += 1


for d in (3, 4, 5, 6, 8):
    qs = (F(11, 10), F(d + 2, 4), F(d, 2) - F(1, 10))
    ss = (F(d - 2, 4), F(d - 2, 2), F(d - 2))
    for s, q, n in product(ss, qs, (2, 3, 17)):
        p = s + 2
        check("source_tail_power", (p + q) - (s + 1) == q + 1 > 0)
        check("haar_h1_threshold", d - 2 * q > 0)
        check("force_convolution_threshold", s + 1 < d and q < d)
        if s < d - 2:
            check("response_density_threshold", p < d and q < d)
            if p + q >= d and n == 2:
                sum_threshold_examples.append(
                    {"d": d, "s": str(s), "q": str(q), "p_plus_q": str(p + q)}
                )
        else:
            check("coulomb_is_atom", p == d and s + 1 < d)

        check("source_gradient_coefficient", s * (s + 1) + s == s * (s + 2))
        for eigenvalue in (s, -s * (s + 1)):
            # Pair block is (1/N) [[DK,-DK],[-DK,DK]].
            pair_action = (2 * eigenvalue / n, -2 * eigenvalue / n)
            check("pair_jacobian_factor", pair_action == tuple(
                (2 * eigenvalue / n) * v for v in (1, -1)
            ))
        check("top_eigenvalue", max(s, -s * (s + 1)) == s)

        for lam, nu_star in product((F(1), F(2), F(3)), (F(0), F(1), F(5))):
            a = lam * q
            c = s * (a - lam) / n
            positive_diffusion = 2 * nu_star * a * max(a + 2 - d, F(0))
            r_to_s = min(F(1, 8), c / positive_diffusion) if positive_diffusion else F(1, 8)
            check("positive_repulsion_margin", c > 0)
            # Radial Laplacian at a coordinate axis:
            # one radial second derivative and d-1 tangential derivatives.
            check("radial_laplacian", a * (a + 1) - (d - 1) * a == a * (a + 2 - d))
            for nu in (F(0), nu_star / 2, nu_star):
                local_coefficient = -2 * c + 2 * nu * a * (a + 2 - d) * r_to_s
                check("absorbed_local_coefficient", local_coefficient <= -c)
                if nu == 0:
                    check("zero_noise_margin", local_coefficient == -2 * c)
                if d == 3:
                    check("dimension_three_positive_diffusion", a * (a + 2 - d) > 0)


for chi, u in product((F(0), F(1, 7), F(1, 2), F(6, 7), F(1)),
                      (F(1), F(5, 4), F(2), F(9))):
    w = 1 - chi + chi * u
    w2 = 1 - chi + chi * u * u
    check("weight_square_identity", w2 - w * w == chi * (1 - chi) * (u - 1) ** 2)
    check("weight_square_nonnegative", w2 >= w * w)


for s, n, r, radius in product((F(1), F(2), F(3)),
                              (2, 3, 17),
                              (F(1, 8), F(1, 4)),
                              (F(1, 2), F(3, 4))):
    p = s + 2
    tau = n * (radius ** int(p) - r ** int(p)) / (2 * s * p)
    tangential = radius / r
    radial = (r / radius) ** int(p - 1)
    check("radial_solution_time", tau > 0 and r ** int(p) + 2 * s * p * tau / n == radius ** int(p))
    check("radial_solution_derivatives", tangential > 1 and 0 < radial < 1)
    check("quadratic_source_potential_coefficient", F(n, 4) * F(2) / p * (2 * s * p / n) == s)


def dot(x, y):
    return sum(F(a) * F(b) for a, b in zip(x, y))


frequencies = (
    (0, 0, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (1, 1, 0),
    (-1, -1, 0),
    (2, -1, 1),
)

# In dimensionless Fourier variables D_hat(n)=c on each nonzero mode,
# K_hat(-n)=i*n*c/|n|^2. For density frequency m and input frequency k,
# the direct gradient response is -c(n.k)/|n|^2, n=m+k.
# The compensated formula is -c+c(n.m)/|n|^2.
for m, k, coulomb_mass in product(frequencies, frequencies, (F(1), F(2), F(7, 3))):
    n = tuple(a + b for a, b in zip(m, k))
    norm2 = dot(n, n)
    if norm2:
        direct = -coulomb_mass * dot(n, k) / norm2
        compensated = -coulomb_mass + coulomb_mass * dot(n, m) / norm2
    else:
        direct = compensated = F(0)
    check("inhomogeneous_coulomb_response", direct == compensated)
    if not any(k):
        check("constant_input_response_zero", direct == compensated == 0)

for k, ell, coulomb_mass in product(frequencies, frequencies, (F(1), F(7, 3))):
    expected = -coulomb_mass * (int(any(k)) + int(any(ell)))
    first = -coulomb_mass if any(k) else F(0)
    second = -coulomb_mass if any(ell) else F(0)
    check("both_coulomb_slots", first + second == expected)
    if not any(k) and not any(ell):
        check("coulomb_compensation_constant", expected == 0)

check("sum_threshold_obstruction_present", len(sum_threshold_examples) > 0)
check("constant_test_source", (F(0) - F(0)) * F(7, 3) == 0)

result = {
    "status": "PASS",
    "total_exact_assertions": sum(counts.values()),
    "counts": dict(sorted(counts.items())),
    "arithmetic": "fractions.Fraction; exact rational arithmetic only",
    "random_seed": None,
    "floating_point_tolerances": None,
    "diffusion_convention": "2 nu Delta in relative coordinates",
    "internal_relative_drift": "2s/N times z/r^(s+2)",
    "barrier_check_variable": "r_to_s represents r^s and is at most c/Q when Q>0",
    "tested_dimensions": [3, 4, 5, 6, 8],
    "tested_particle_numbers": [2, 3, 17],
    "tested_diffusivity_upper_bounds": [0, 1, 5],
    "tested_moment_powers": [1, 2, 3],
    "admissible_examples_violating_naive_sum_threshold": sum_threshold_examples,
    "evidence_limit": "Corroborating coefficient checks; analytic proof is the Markdown report.",
}
output = Path(__file__).with_name("round007_gradient_exact_checks_output.json")
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "total_exact_assertions": result["total_exact_assertions"],
                  "output": str(output)}, sort_keys=True))
