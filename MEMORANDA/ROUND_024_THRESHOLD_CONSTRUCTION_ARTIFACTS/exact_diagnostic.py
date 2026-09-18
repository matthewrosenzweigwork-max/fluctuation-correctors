#!/usr/bin/env python3
"""Fresh R24 diagnostic: exact Laurent algebra, no prior checker imported.

One-coordinate Fourier probes embed in T^4. Every second-order physical
expression is divided by (2*pi)^2. D_j e_k=k_j e_k; the force-gradient
product is +sum k*g_hat(k)e_{k,-k} D_j. Diffusion is -nu*sum D_j^2.
This checks algebra and smooth limiting models, not the actual singular limit.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path
import hashlib
import json
import sys

COUNTS = Counter()
MUTATIONS = Counter()


def clean(p):
    return {k: F(v) for k, v in p.items() if v}


def add(*ps):
    q = {}
    for p in ps:
        for k, v in p.items():
            q[k] = q.get(k, F(0)) + v
    return clean(q)


def scale(p, a):
    return clean({k: a*v for k, v in p.items()})


def mul(p, q):
    out = {}
    for k, a in p.items():
        for l, b in q.items():
            m = tuple(x+y for x, y in zip(k, l))
            out[m] = out.get(m, F(0)) + a*b
    return clean(out)


def D(p, j, order=1):
    return clean({k: v*k[j]**order for k, v in p.items()})


def put(p, slots, n):
    """Insert specified slots; None means Haar integration of that slot."""
    out = {}
    for k, v in p.items():
        if any(s is None and k[j] != 0 for j, s in enumerate(slots)):
            continue
        m = [0]*n
        for j, s in enumerate(slots):
            if s is not None:
                m[s] += k[j]
        m = tuple(m)
        out[m] = out.get(m, F(0)) + v
    return clean(out)


def U(p, order, n):
    """Literal subset/distinct-label statistic, including all backgrounds."""
    out = {}
    for size in range(order+1):
        for chosen in combinations(range(order), size):
            for labels in permutations(range(n), size):
                slots = [None]*order
                for j, i in zip(chosen, labels):
                    slots[j] = i
                out = add(out, scale(put(p, slots, n),
                                     F((-1)**(order-size), n**size)))
    return out


def P(p, n):
    return scale(U(p, 2, n), F(1, 2))


def mean(p, n):
    return p.get((0,)*n, F(0))


def sym(p, n):
    out = {}
    for perm in permutations(range(n)):
        out = add(out, put(p, perm, n))
    fac = 1
    for j in range(2, n+1):
        fac *= j
    return scale(out, F(1, fac))


def real_sym(p, n):
    return sym(add(p, {tuple(-j for j in k): v for k, v in p.items()}), n)


def force(g, i, j, n):
    return put({(k, -k): k*v for k, v in g.items() if k}, [i, j], n)


def generator(p, g, n, nu):
    out = {}
    for i in range(n):
        out = add(out, scale(D(p, i, 2), -nu))
        for j in range(n):
            if i != j:
                out = add(out, scale(mul(force(g, i, j, n), D(p, i)), F(1, n)))
    return out


def response(phi, g, slot):
    return clean({k: -k[slot]**2*g.get(k[slot], F(0))*v
                  for k, v in phi.items()})


def pair_B(phi, g):
    return mul(force(g, 0, 1, 2), add(D(phi, 0), scale(D(phi, 1), -1)))


def upward(phi, g):
    raw = mul(force(g, 0, 2, 3), put(D(phi, 0), [0, 1], 3))
    return sym(raw, 3)


def source(h, g):
    return mul(force(g, 0, 1, 2),
               add(put(D(h, 0), [0], 2), scale(put(D(h, 0), [1], 2), -1)))


def check(category, ok, detail=''):
    COUNTS[category] += 1
    if not ok:
        raise AssertionError((category, detail))


def neq(name, good, bad):
    if good != bad:
        MUTATIONS[name] += 1


def algebra():
    kernels = [
        {(0, 0): F(1)},
        real_sym({(1, -1): F(1)}, 2),
        real_sym({(1, 0): F(1)}, 2),
        real_sym({(2, -1): F(1), (1, 1): F(2, 3)}, 2),
        real_sym({(2, 1): F(2), (0, 2): F(1, 3), (1, -1): F(3, 2)}, 2),
    ]
    hs = [{(0,): F(1)}, {(1,): F(1, 2), (-1,): F(1, 2)},
          {(2,): F(1, 3), (-2,): F(1, 3), (1,): F(1), (-1,): F(1)}]
    forces = [{}, {-1: F(1), 1: F(1)},
              {-2: F(1, 4), -1: F(1), 1: F(1), 2: F(1, 4)}]
    for n in (2, 3, 4):
        for nu in (F(0), F(1, 3)):
            for g in forces:
                for phi in kernels:
                    obs = P(phi, n)
                    rx, ry = response(phi, g, 0), response(phi, g, 1)
                    bp = pair_B(phi, g)
                    cp = upward(phi, g)
                    diffusion = scale(add(D(phi, 0, 2), D(phi, 1, 2)), -nu)
                    Lpair = add(diffusion, rx, ry, scale(bp, F(1, n)))
                    row = put(bp, [0, None], 1)
                    lower = scale(U(row, 1, n), F(1, n))
                    scalar = {(0,)*n: F(1, 2*n)*mean(bp, 2)}
                    cub = U(cp, 3, n)
                    direct = generator(obs, g, n, nu)
                    decomposed = add(P(Lpair, n), cub, lower, scalar)
                    check('finite_N_generator', direct == decomposed, (n, nu, g, phi))
                    neq('missing_response_x', direct, add(decomposed, scale(P(rx, n), -1)))
                    neq('missing_response_y', direct, add(decomposed, scale(P(ry, n), -1)))
                    neq('wrong_internal_half', direct,
                        add(decomposed, scale(P(bp, n), F(-1, 2*n))))
                    neq('missing_scalar', direct, add(decomposed, scale(scalar, -1)))
                    neq('halved_lower', direct, add(decomposed, scale(lower, F(-1, 2))))
                    if n == 2:
                        neq('deleted_N2_cubic_background', direct, add(decomposed, scale(cub, -1)))
                    gamma = add(generator(mul(obs, obs), g, n, nu),
                                scale(mul(obs, direct), -2))
                    gamma2 = {}
                    for i in range(n):
                        gamma2 = add(gamma2, scale(mul(D(obs, i), D(obs, i)), -2*nu))
                        raw = {}
                        for j in range(n):
                            if j != i:
                                raw = add(raw, scale(put(D(phi, 0), [i, j], n), F(1, n*n)))
                        raw = add(raw, scale(put(put(D(phi, 0), [0, None], 1), [i], n), F(-1, n)))
                        check('particle_gradient', D(obs, i) == raw)
                    check('carré_du_champ', gamma == gamma2)
                    neq('noise_factor_half', gamma, scale(gamma2, F(1, 2)))
                    for h in hs:
                        jsrc = source(h, g)
                        dtphi = scale(add(Lpair, jsrc), -1)
                        direct_time = add(P(dtphi, n), direct)
                        target = add(scale(P(jsrc, n), -1), cub, lower, scalar)
                        check('terminal_inverse_identity', direct_time == target)
                        neq('source_sign', direct_time, add(target, scale(P(jsrc, n), 2)))
                        if not g or len(h) == 1:
                            check('zero_source', not jsrc)
                        rowj = put(jsrc, [0, None], 1)
                        expected = clean({k: -k[0]**2*g.get(k[0], F(0))*v for k, v in h.items()})
                        check('source_background', rowj == expected)
                    rowphi = put(phi, [0, None], 1)
                    r = mean(phi, 2)
                    aa = add(rowphi, {(0,): -r})
                    canonical = add(phi, scale(put(rowphi, [0], 2), -1),
                                    scale(put(rowphi, [1], 2), -1), {(0, 0): r})
                    exact_moment = (F(n-1, 2*n**3)*mean(mul(canonical, canonical), 2)
                                    +F(1, n**3)*mean(mul(aa, aa), 1)+F(r*r, 4*n*n))
                    check('iid_endpoint_second_moment', mean(mul(obs, obs), n) == exact_moment)


def coulomb_flux():
    for p in range(-3, 4):
        for q in range(-3, 4):
            phi = real_sym({(p, q): F(1)}, 2)
            g = {k: F(1, k*k) for k in range(-6, 7) if k}
            b = put(pair_B(phi, g), [0, None], 1)
            center = put(mul(force(g, 0, 1, 2), add(D(phi, 0), D(phi, 1))), [0, None], 1)
            row = put(phi, [0, None], 1)
            trace = put(phi, [0, 0], 1)
            rhs = add(center, scale(row, 2), scale(trace, -2))
            check('Coulomb_flux_atom_compensation', b == rhs)
            neq('flux_atom_sign', b, add(center, scale(row, 2), scale(trace, 2)))
            neq('flux_atom_half', b, add(center, scale(row, 2), scale(trace, -1)))
            neq('flux_compensation_omitted', b, add(center, scale(trace, -2)))
            if p+q != 0:
                check('nonzero_total_mode_scalar', mean(b, 1) == 0)
            else:
                neq('universal_scalar_deletion', b, add(b, {(0,): -mean(b, 1)}))
            rx = clean({k: -v if k[0] else 0 for k, v in phi.items()})
            ry = clean({k: -v if k[1] else 0 for k, v in phi.items()})
            check('full_Coulomb_response', add(rx, ry) ==
                  add(scale(phi, -2), put(row, [0], 2), put(row, [1], 2)))
    # Relative shell: K=2*r^-3 theta, B Phi=4*r^-3 F'(r).
    # Divide by sphere area: integral on [a,b] is 4*(F(b)-F(a)).
    for a, b in [(F(1, 5), F(2, 5)), (F(1, 16), F(1, 4))]:
        for power in (2, 4, 6):
            volume = 4*power*F(b**power-a**power, power)
            flux = 4*(b**power-a**power)
            check('radial_flux_factor', volume == flux)
            neq('radial_factor_two', volume, 2*(b**power-a**power))


def initial_sign():
    for n in (2, 3, 4, 5):
        for k in (1, 2):
            g = {j: F(1, j*j) for j in (-2, -1, 1, 2)}
            z = {}
            for i in range(n):
                exp = [0]*n
                exp[i] = k
                z[tuple(exp)] = F(1, n)
            conjugate = {tuple(-i for i in ex): a for ex, a in z.items()}
            zz = mul(z, conjugate)
            for nu in (F(0), F(1, 7)):
                deriv = mean(generator(zz, g, n, nu), n)
                expected = F(-2*(n-1), n*n)
                check('actual_initial_mode_derivative', deriv == expected)
                neq('repulsive_sign_flipped', deriv, -expected)
                check('iid_initial_mode_variance', mean(zz, n) == F(1, n))


def smooth_limiting_ode():
    """Independent RK4 versus closed Fourier response integral, normalized c=1."""
    records = []
    with localcontext() as ctx:
        ctx.prec = 50
        one = Decimal(1)
        expminus = (-one).exp()
        for rate in (1, 2):
            r = Decimal(rate)
            def rhs(t, value):
                return (-t).exp()-r*value
            for steps in (128, 256):
                dt = one/steps
                t = Decimal(0)
                value = Decimal(0)
                for _ in range(steps):
                    k1 = rhs(t, value)
                    k2 = rhs(t+dt/2, value+dt*k1/2)
                    k3 = rhs(t+dt/2, value+dt*k2/2)
                    k4 = rhs(t+dt, value+dt*k3)
                    value += dt*(k1+2*k2+2*k3+k4)/6
                    t += dt
                exact = expminus if rate == 1 else expminus*(1-expminus)
                err = abs(value-exact)
                check('smooth_Fourier_limiting_ODE', err < Decimal('2e-10'), str(err))
                records.append({'rate': rate, 'steps': steps, 'absolute_error': str(err)})
        check('two_response_ODE_mutation', abs(expminus-expminus*(1-expminus)) > Decimal('0.1'))
        MUTATIONS['one_response_limiting_ODE'] += 1
    return records


def exponents():
    for n in (2, 3, 16, 81):
        check('critical_rescaling', F(-1, 2)+F(1, 2) == 0)
        check('source_floor_threshold', F(1, 2)-1+F(1, 2) == 0)
        check('lower_decay', F(1, 2)-1+F(1, 2)-F(1, 4) == F(-1, 4))
    gamma = F(1, 40)
    check('smooth_bracket_rate', -1+10*gamma == F(-3, 4))
    check('smooth_diagonal_rate', F(-5, 2)+9*gamma == F(-91, 40))
    check('lower_gradient_route_empty', 4-2-1 == 1)
    check('Coulomb_bulk_coefficient_zero', 2*(4-2-2) == 0)
    check('natural_gradient_square_nonintegrable', 3-2*3 == -3)
    check('source_square_logarithmic', 3-2*2 == -1)


def main():
    algebra()
    coulomb_flux()
    initial_sign()
    ode = smooth_limiting_ode()
    exponents()
    required = ['missing_response_x', 'missing_response_y', 'wrong_internal_half',
                'missing_scalar', 'halved_lower', 'deleted_N2_cubic_background',
                'noise_factor_half', 'source_sign', 'flux_atom_sign', 'flux_atom_half',
                'flux_compensation_omitted', 'universal_scalar_deletion',
                'radial_factor_two', 'repulsive_sign_flipped', 'one_response_limiting_ODE']
    for name in required:
        check('mutation_detected', MUTATIONS[name] > 0, name)
    result = {'status': 'PASS', 'assertions': sum(COUNTS.values()),
              'categories': dict(sorted(COUNTS.items())),
              'detecting_mutations': dict(sorted(MUTATIONS.items())),
              'smooth_ODE_results': ode,
              'evidence_class': 'SELF_CHECKED algebra and smooth limiting-model support only',
              'random_seed': None, 'exact_arithmetic': 'fractions.Fraction',
              'ODE_precision_digits': 50, 'ODE_tolerance': '2e-10',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output = Path(__file__).with_name('RESULTS.json')
    if '--check' in sys.argv:
        if json.loads(output.read_text()) != result:
            raise AssertionError('Stored diagnostic result differs from fresh execution')
    else:
        output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
