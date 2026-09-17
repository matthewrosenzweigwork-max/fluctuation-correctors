#!/usr/bin/env python3
"""Exact rational Fourier checks of the independently reconstructed identities.

No third-party dependencies. In angular variables theta=2*pi*x, K=sin(theta)
and b=sin(2*theta)/3. Write K=-i*H and partial_theta=i*D; all generator
coefficients are then rational. Angular diffusivity is 2/5. This is exactly
the frozen unit-torus model with g=cos(2*pi*x)/(4*pi*pi),
V=cos(4*pi*x)/(24*pi*pi), nu=(2/5)/(4*pi*pi).
"""

from fractions import Fraction as Q
from itertools import permutations


def clean(p):
    return {e: c for e, c in p.items() if c}


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, Q(0)) + c
    return clean(out)


def scale(p, c):
    return clean({e: c * v for e, v in p.items()})


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            a = tuple(x + y for x, y in zip(e, f))
            out[a] = out.get(a, Q(0)) + c * d
    return clean(out)


def deriv(p, slot, order=1):
    return clean({e: c * e[slot] ** order for e, c in p.items()})


def embed(p, slots, size):
    out = {}
    for e, c in p.items():
        a = [0] * size
        for slot, power in zip(slots, e):
            a[slot] += power
        t = tuple(a)
        out[t] = out.get(t, Q(0)) + c
    return clean(out)


def integrate(p, slots, mu):
    out = {}
    for e, c in p.items():
        for slot in slots:
            c *= mu.get(-e[slot], Q(0))
        a = tuple(v for i, v in enumerate(e) if i not in slots)
        out[a] = out.get(a, Q(0)) + c
    return clean(out)


def factorial(p, degree, n):
    return scale(add(*(embed(p, a, n) for a in permutations(range(n), degree))),
                 Q(1, n ** degree))


def centered(p, degree, mu, n, mudot=None):
    out = {}
    for mask in range(1 << degree):
        selected = [i for i in range(degree) if mask & (1 << i)]
        other = [i for i in range(degree) if i not in selected]
        q = {}
        for e, c in p.items():
            weight = Q(0)
            if mudot is None:
                weight = Q(1)
                for slot in other:
                    weight *= mu.get(-e[slot], Q(0))
            else:
                for special in other:
                    w = Q(1)
                    for slot in other:
                        density = mudot if slot == special else mu
                        w *= density.get(-e[slot], Q(0))
                    weight += w
            a = tuple(e[i] for i in selected)
            q[a] = q.get(a, Q(0)) + c * weight
        out = add(out, scale(factorial(q, len(selected), n),
                             (-1) ** len(other)))
    return clean(out)


H_K = {(1, -1): Q(1, 2), (-1, 1): Q(-1, 2)}
H_B = {(2,): Q(1, 6), (-2,): Q(-1, 6)}
NU = Q(2, 5)


def h_u(mu, b):
    return add(b, {(1,): Q(1, 2) * mu.get(1, 0),
                   (-1,): Q(-1, 2) * mu.get(-1, 0)})


def mu_dot(mu, b):
    density = {(k,): v for k, v in mu.items()}
    p = add(scale(deriv(mul(h_u(mu, b), density), 0), -1),
            scale(deriv(density, 0, 2), -NU))
    return {e[0]: c for e, c in p.items()}


def generator(p, n, b):
    out = {}
    for i in range(n):
        drift = embed(b, [i], n)
        for j in range(n):
            if i != j:
                drift = add(drift, scale(embed(H_K, [i, j], n), Q(1, n)))
        out = add(out, mul(drift, deriv(p, i)), scale(deriv(p, i, 2), -NU))
    return out


def response(p, slot, mu):
    out = {}
    for e, c in p.items():
        for ell, h in [(1, Q(1, 2)), (-1, Q(-1, 2))]:
            a = list(e)
            a[slot] = -ell
            a = tuple(a)
            out[a] = out.get(a, Q(0)) + c * e[slot] * h * mu.get(-e[slot] - ell, 0)
    return clean(out)


def linearized(p, degree, mu, b):
    out = {}
    for slot in range(degree):
        out = add(out, mul(embed(h_u(mu, b), [slot], degree), deriv(p, slot)),
                  scale(deriv(p, slot, 2), -NU), response(p, slot, mu))
    return out


def pair_up(p):
    lifted = embed(p, [0, 1], 3)
    return add(mul(embed(H_K, [0, 2], 3), deriv(lifted, 0)),
               mul(embed(H_K, [1, 2], 3), deriv(lifted, 1)))


def pair_internal(p):
    return mul(H_K, add(deriv(p, 0), scale(deriv(p, 1), -1)))


def one_up(p):
    return scale(mul(H_K, add(embed(deriv(p, 0), [0], 2),
                               scale(embed(deriv(p, 0), [1], 2), -1))), Q(1, 2))


def v_at(p, i, n, mu):
    dp = deriv(p, 0)
    return add(scale(add(*(embed(dp, [i, j], n) for j in range(n) if j != i)), Q(1, n)),
               scale(embed(integrate(dp, [1], mu), [i], n), -1))


def require_zero(p, label):
    if p:
        raise AssertionError(f"{label}: nonzero exact Laurent polynomial: {p}")


def check_case(n, mu, b, name, phi):
    u2 = centered(phi, 2, mu, n)
    lhs = add(generator(u2, n, b), centered(phi, 2, mu, n, mu_dot(mu, b)))
    j = pair_internal(phi)
    rhs = add(centered(linearized(phi, 2, mu, b), 2, mu, n),
              centered(pair_up(phi), 3, mu, n), scale(factorial(j, 2, n), Q(1, n)))
    require_zero(add(lhs, scale(rhs, -1)), f"pair N={n} {name}")
    expanded = add(centered(j, 2, mu, n),
                   scale(centered(integrate(j, [1], mu), 1, mu, n), 2),
                   embed(integrate(j, [0, 1], mu), [], n))
    require_zero(add(factorial(j, 2, n), scale(expanded, -1)), "lower contractions")
    for i in range(n):
        require_zero(add(deriv(scale(u2, Q(1, 2)), i),
                         scale(v_at(phi, i, n, mu), Q(-1, n))), "martingale coefficient")
    psi = {(1, 0): Q(1, 2), (-1, 0): Q(1, 2),
           (0, 1): Q(1, 2), (0, -1): Q(1, 2)}
    p2 = scale(u2, Q(1, 2))
    q2 = scale(centered(psi, 2, mu, n), Q(1, 2))
    lhs_bracket = scale(add(*(mul(deriv(p2, i), deriv(q2, i)) for i in range(n))), -2 * NU)
    rhs_bracket = scale(add(*(mul(v_at(phi, i, n, mu), v_at(psi, i, n, mu))
                              for i in range(n))), Q(-2, n ** 2) * NU)
    require_zero(add(lhs_bracket, scale(rhs_bracket, -1)), "pair cross bracket")


def main():
    phis = {
        "constant": {(0, 0): Q(1)},
        "separable": {(a, b): Q(1, 4) for a in [-1, 1] for b in [-1, 1]},
        "difference mode": {(1, -1): Q(1, 2), (-1, 1): Q(1, 2)},
        "mixed mode": {(a, b): Q(1, 2) for a, b in [(1, 2), (2, 1), (-1, -2), (-2, -1)]},
    }
    backgrounds = {
        "uniform": ({0: Q(1)}, {}),
        "inhomogeneous": ({0: Q(1), 1: Q(1, 6), -1: Q(1, 6)}, H_B),
    }
    checks = 0
    for n in [2, 3]:
        for background, (mu, b) in backgrounds.items():
            for name, phi in phis.items():
                check_case(n, mu, b, f"{background}/{name}", phi)
                checks += 1
            for k in [1, 2]:
                p = {(k,): Q(1, 2), (-k,): Q(1, 2)}
                u1 = centered(p, 1, mu, n)
                lhs = add(generator(u1, n, b), centered(p, 1, mu, n, mu_dot(mu, b)))
                rhs = add(centered(linearized(p, 1, mu, b), 1, mu, n),
                          centered(one_up(p), 2, mu, n))
                require_zero(add(lhs, scale(rhs, -1)), f"one-body N={n} k={k}")
                checks += 1
    print(f"PASS: {checks} exact rational Fourier cases; all pair lower contractions, "
          "martingale coefficients, and pair cross brackets also agree.")


if __name__ == "__main__":
    main()
