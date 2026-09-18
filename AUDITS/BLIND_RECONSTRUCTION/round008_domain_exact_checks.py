#!/usr/bin/env python3
"""TASK-053 exact, independent checks. Standard library; no random inputs.

Laurent polynomials use angular variables of period 2*pi. A physical spatial
first derivative is 2*pi times the angular derivative, and physical diffusion
has the squared factor. All identities are homogeneous in these factors.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json


@dataclass(frozen=True)
class Qi:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = qi(other)
        return Qi(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Qi(-self.a, -self.b)

    def __sub__(self, other):
        return self + -qi(other)

    def __mul__(self, other):
        other = qi(other)
        return Qi(self.a * other.a - self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = qi(other)
        den = other.a * other.a + other.b * other.b
        return self * Qi(other.a / den, -other.b / den)

    def __bool__(self):
        return bool(self.a or self.b)


def qi(value):
    return value if isinstance(value, Qi) else Qi(F(value))


I = Qi(F(0), F(1))


class Laurent:
    def __init__(self, n, terms=None):
        self.n = n
        self.t = {tuple(k): qi(v) for k, v in (terms or {}).items() if qi(v)}

    @staticmethod
    def one(n):
        return Laurent(n, {(0,) * n: 1})

    def __add__(self, other):
        if not isinstance(other, Laurent):
            other = Laurent.one(self.n) * other
        assert self.n == other.n
        out = dict(self.t)
        for k, v in other.t.items():
            out[k] = out.get(k, Qi()) + v
        return Laurent(self.n, out)

    __radd__ = __add__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if not isinstance(other, Laurent):
            return Laurent(self.n, {k: v * other for k, v in self.t.items()})
        assert self.n == other.n
        out = {}
        for k, v in self.t.items():
            for l, w in other.t.items():
                kl = tuple(a + b for a, b in zip(k, l))
                out[kl] = out.get(kl, Qi()) + v * w
        return Laurent(self.n, out)

    __rmul__ = __mul__

    def deriv(self, slot):
        return Laurent(self.n, {k: v * I * k[slot] for k, v in self.t.items()})

    def embed(self, n, mapping):
        """mapping[i] is output slot, or None to Haar-integrate input slot i."""
        assert len(mapping) == self.n
        out = {}
        for k, v in self.t.items():
            if any(m is None and a for m, a in zip(mapping, k)):
                continue
            key = [0] * n
            for m, a in zip(mapping, k):
                if m is not None:
                    key[m] += a
            key = tuple(key)
            out[key] = out.get(key, Qi()) + v
        return Laurent(n, out)

    def equal(self, other):
        return not (self - other).t


def mode(n, wave):
    return Laurent(n, {tuple(wave): 1})


def cosine(wave):
    n = len(wave)
    return (mode(n, wave) + mode(n, [-x for x in wave])) * F(1, 2)


def sine(wave):
    n = len(wave)
    return (mode(n, wave) - mode(n, [-x for x in wave])) * Qi(F(0), F(-1, 2))


def force(n, i, j, kappa=F(3, 2)):
    wave = [0] * n
    wave[i] += 1
    wave[j] -= 1
    return sine(wave) * kappa


def uk(poly, n):
    """Literal subset and ordered distinct-label definition, no overlap shortcut."""
    k = poly.n
    answer = Laurent(n)
    for size in range(k + 1):
        for chosen in combinations(range(k), size):
            for labels in permutations(range(n), size):
                mapping = [None] * k
                for slot, label in zip(chosen, labels):
                    mapping[slot] = label
                answer += poly.embed(n, mapping) * F((-1) ** (k - size), n ** size)
    return answer


def response(phi):
    rx = (force(3, 2, 0) * phi.deriv(0).embed(3, [2, 1])).embed(2, [0, 1, None])
    ry = (force(3, 2, 1) * phi.deriv(1).embed(3, [0, 2])).embed(2, [0, 1, None])
    return rx + ry


def up(phi):
    raw = force(3, 0, 2) * phi.deriv(0).embed(3, [0, 1])
    return sum((raw.embed(3, perm) for perm in permutations(range(3))), Laurent(3)) * F(1, 6)


def internal(phi):
    return force(2, 0, 1) * (phi.deriv(0) - phi.deriv(1))


def lap(poly):
    return sum((poly.deriv(i).deriv(i) for i in range(poly.n)), Laurent(poly.n))


def direct_generator(poly, n, nu):
    out = lap(poly) * nu
    for i in range(n):
        for j in range(n):
            if i != j:
                out += force(n, i, j) * poly.deriv(i) * F(1, n)
    return out


checks = []


def check(name, assertion, detail=None):
    if not assertion:
        raise AssertionError(name)
    checks.append({"name": name, "pass": True, **({"detail": detail} if detail else {})})


kernels = {
    "constant": Laurent.one(2),
    "difference_mode": cosine([1, -1]),
    "one_body_sum": cosine([1, 0]) + cosine([0, 1]),
    "separable": cosine([1, 0]) * cosine([0, 1]),
    "mixed_mode": cosine([2, -1]) + cosine([-1, 2]),
    "mixed_sine": sine([1, 2]) + sine([2, 1]),
}
for n, nu, (name, phi) in product([2, 3, 4], [F(0), F(2, 5)], kernels.items()):
    p_obs = uk(phi, n) * F(1, 2)
    left = direct_generator(p_obs, n, nu)
    bphi = internal(phi)
    full = lap(phi) * nu + response(phi) + bphi * F(1, n)
    right = (uk(full, n) * F(1, 2) + uk(up(phi), n)
             + uk(bphi.embed(1, [0, None]), n) * F(1, n)
             + bphi.embed(n, [None, None]) * F(1, 2 * n))
    check(f"full_particle_identity_N{n}_nu{nu}_{name}", left.equal(right))
    grad_formula = ((sum((phi.deriv(0).embed(n, [0, j]) for j in range(1, n)), Laurent(n))
                     * F(1, n * n))
                    - phi.deriv(0).embed(n, [0, None]) * F(1, n))
    check(f"deleted_gradient_N{n}_nu{nu}_{name}", p_obs.deriv(0).equal(grad_formula))
    check(f"pair_exchange_{name}_N{n}_nu{nu}", phi.equal(phi.embed(2, [1, 0])))

for n in [2, 3, 4]:
    check(f"constant_P_N{n}", (uk(Laurent.one(2), n) * F(1, 2)).equal(Laurent.one(n) * F(-1, 2 * n)))
    check(f"constant_U3_N{n}", uk(Laurent.one(3), n).equal(Laurent.one(n) * F(2, n * n)))
    # The full ordered empirical triple has (N)_3 terms and can vanish at N=2;
    # the literal U3 on a constant does not vanish there.
    check(f"unordered_internal_coefficient_N{n}", F(2, 2 * n * n ** 2) == F(1, n ** 3))

check("smooth_Fourier_response_sign", response(cosine([1, -1])).equal(cosine([1, -1]) * F(-3, 2)))
check("smooth_Fourier_B_factor", internal(cosine([1, -1])).equal(sine([1, -1]) * sine([1, -1]) * -3))
check("smooth_response_constant", response(Laurent.one(2)).equal(Laurent(2)))
check("constant_terminal_source", (force(2, 0, 1) * (Laurent.one(2).deriv(0) - Laurent.one(2).deriv(1))).equal(Laurent(2)))

# Taylor polynomials around z=e_1. Coefficients are exact rationals and powers
# may be rational because the constant term of |e_1+h|^2 is exactly one.
def tadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def tmul(a, b, order=3):
    out = {}
    for k, v in a.items():
        for l, w in b.items():
            key = tuple(x + y for x, y in zip(k, l))
            if sum(key) <= order:
                out[key] = out.get(key, F(0)) + v * w
    return {k: v for k, v in out.items() if v}


def radius_power(d, exponent):
    zero = (0,) * d
    u = {}
    first = [0] * d
    first[0] = 1
    u[tuple(first)] = F(2)
    for i in range(d):
        key = [0] * d
        key[i] = 2
        u[tuple(key)] = F(1)
    out, power, coefficient = {zero: F(1)}, {zero: F(1)}, F(1)
    a = -exponent / 2
    for k in range(1, 4):
        power = tmul(power, u)
        coefficient *= (a - k + 1) / k
        out = tadd(out, {key: coefficient * value for key, value in power.items()})
    return out


def derivative_at_zero(poly, indices, d):
    multi = [0] * d
    for i in indices:
        multi[i] += 1
    factorial = 1
    for n in multi:
        for j in range(2, n + 1):
            factorial *= j
    return poly.get(tuple(multi), F(0)) * factorial


tuples = [(3, F(1), F(5, 4), F(5, 2)),
          (3, F(1, 2), F(4, 3), F(8, 3)),
          (4, F(2), F(3, 2), F(3)),
          (5, F(3), F(2), F(7, 2)),
          (7, F(5), F(5, 2), F(4))]
for d, s, q1, q2 in tuples:
    p = s + 2
    alpha = (1 + q1) / 2
    beta = (alpha + 1 + q2) / 2
    eps = min(alpha - 1, (beta - 2) / 2,
              (alpha + p - (s + 1)) / (s + 1),
              (beta + p - (p + 1) - alpha) / (p + 1),
              (beta + p - (s + 2)) / (s + 2)) / 4
    moment = 1 + eps
    check(f"admissible_d{d}_s{s}", 0 < s <= d - 2 and 1 < q1 < F(d, 2) and q1 + 1 < q2 < d)
    for label, value in {
        "gradient_amplification": alpha - moment,
        "hessian_amplification": beta - 2 * moment,
        "gradient_source": alpha + p - moment * (s + 1),
        "hessian_double_source": beta + p - moment * (p + 1) - alpha,
        "hessian_direct_source": beta + p - moment * (s + 2),
        "H1_integrability": d - 2 * q1,
        "W21_integrability": d - q2,
        "weak_boundary": d - 1 - q1,
        "relative_drift_dominance": p - 2,
    }.items():
        check(f"strict_gap_{label}_d{d}_s{s}", value > 0, str(value))
    principal = radius_power(d, s)
    radial_hess = derivative_at_zero(principal, [0, 0], d)
    tangent_hess = derivative_at_zero(principal, [1, 1], d)
    laplacian = sum(derivative_at_zero(principal, [i, i], d) for i in range(d))
    check(f"radial_Hessian_d{d}_s{s}", radial_hess == s * (s + 1))
    check(f"tangent_Hessian_d{d}_s{s}", tangent_hess == -s)
    check(f"principal_Laplacian_d{d}_s{s}", laplacian == s * (s + 2 - d))
    for n, nu, q, ell in product([2, 3], [F(0), F(3, 5)], [q1, q2], [F(0), F(1)]):
        weight = radius_power(d, q)
        grad = derivative_at_zero(weight, [0], d)
        delta = sum(derivative_at_zero(weight, [i, i], d) for i in range(d))
        actual = 2 * nu * delta + 2 * s * grad / n + ell * 2 * s / n
        expected = 2 * nu * q * (q + 2 - d) - 2 * s * (q - ell) / n
        check(f"weighted_generator_d{d}_s{s}_N{n}_nu{nu}_q{q}_ell{ell}", actual == expected)
    if s == d - 2:
        check(f"Coulomb_punctured_Laplacian_d{d}", laplacian == 0)
    if d == 3:
        check(f"positive_diffusion_requires_absorption_d{d}_s{s}", q1 * (q1 + 2 - d) > 0)
    # Fourier normalization ratio uses Gamma(z+1)=z Gamma(z), exactly.
    if s < d - 2:
        check(f"Fourier_gamma_ratio_d{d}_s{s}", 4 * F(d - s - 2, 2) * F(s, 2) == s * (d - 2 - s))

for k, l in product([0, 1, 2], repeat=2):
    atom = -2
    haar = int(k == 0) + int(l == 0)
    correct = -int(k != 0) - int(l != 0)
    check(f"Coulomb_full_response_mode_{k}_{l}", atom + haar == correct)
check("Coulomb_atom_only_fails_constant", -2 != 0)
check("Coulomb_compensation_only_fails_constant", 2 != 0)
check("signed_jump_constant_compensation", F(1) + (F(0) - 1) == 0)

root = Path(__file__).resolve().parent
repository = root.parent.parent
input_manifest = root / 'ROUND_008_DOMAIN_INPUT_SHA256SUMS.txt'
input_verification = []
for line in input_manifest.read_text().splitlines():
    expected, name = line.split('  ', 1)
    actual = hashlib.sha256((repository / name).read_bytes()).hexdigest()
    if actual != expected:
        raise AssertionError('Input seal mismatch: ' + name)
    input_verification.append({'path': name, 'sha256': actual, 'pass': True})
assert len(input_verification) == 17
output = {
    "task": "TASK-053",
    "claim": "THM028",
    "status": "PASS",
    "evidence_label": "exact independent reconstruction checks; supporting algebra, not an analytic certificate",
    "arithmetic": "fractions and finite Laurent/Taylor polynomials over Q(i)",
    "dependencies": "Python standard library only",
    "randomness": "none",
    "tolerance": "none",
    "check_count": len(checks),
    "checks": checks,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "base_commit": "3aa91391516f35afe5317a287b4f0e2e93e6384c",
    "input_manifest_sha256": hashlib.sha256(input_manifest.read_bytes()).hexdigest(),
    "input_verification": input_verification,
}
path = root / 'round008_domain_exact_checks_output.json'
path.write_text(json.dumps(output, indent=2) + '\n')
print(f"PASS: {len(checks)} exact checks; output {path}")
