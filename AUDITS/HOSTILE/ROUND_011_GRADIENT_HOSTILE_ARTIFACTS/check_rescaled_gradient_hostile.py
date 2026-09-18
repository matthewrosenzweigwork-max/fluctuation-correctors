#!/usr/bin/env python3
"""Fresh exact diagnostics for TASK069; standard library only.

The checker does not open any constructor checker, prior result, or source
file. Univariate formal Taylor series reconstruct directional derivatives
from powers of squared distance. Finite tests corroborate the analytic
review; they are not a proof of any stochastic or convergence assertion.
"""
from fractions import Fraction as Q
from math import factorial
import json
from pathlib import Path
import sys


DEG = 4
COUNTS = {}


def check(group, condition, witness):
    if not condition:
        raise AssertionError((group, witness))
    COUNTS[group] = COUNTS.get(group, 0) + 1


def series(*coefficients):
    return [Q(x) for x in coefficients] + [Q(0)] * (DEG + 1 - len(coefficients))


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, c):
    return [Q(c) * x for x in a]


def mul(a, b):
    return [sum((a[j] * b[k-j] for j in range(k+1)), Q(0))
            for k in range(DEG+1)]


def unit_power(a, exponent):
    """Formal generalized binomial expansion, requiring constant term one."""
    assert a[0] == 1
    u = a[:]
    u[0] = Q(0)
    answer = series(1)
    power = series(1)
    coefficient = Q(1)
    for k in range(1, DEG+1):
        power = mul(power, u)
        coefficient *= (Q(exponent) - k + 1) / k
        answer = add(answer, scale(power, coefficient))
    return answer


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def squared_distance(direction):
    # Base relative vector e_1, perturbed by t*direction.
    return series(1, 2*direction[0], dot(direction, direction))


def force_series(s, direction):
    radial = unit_power(squared_distance(direction), -(s+2)/2)
    return [scale(mul(series(int(i == 0), direction[i]), radial), s)
            for i in range(len(direction))]


def matrix_vector(matrix, vector):
    return [dot(row, vector) for row in matrix]


def run():
    parameter_rows = []
    for d in range(3, 10):
        for denominator in (1, 2, 3):
            s = Q(d-2, denominator)
            p, q = s+2, s+1
            parameter_rows.append((d, s))
            unit = [[Q(int(i == j)) for i in range(d)] for j in range(d)]
            for n_particles in (2, 3, 17):
                # Full pair Jacobian obtained directly from force evaluations.
                columns = []
                for j in range(2*d):
                    direction = unit[j % d][:]
                    if j >= d:
                        direction = [-x for x in direction]
                    first_slot = [row[1]/n_particles for row in force_series(s, direction)]
                    columns.append(first_slot + [-x for x in first_slot])
                jacobian = [list(row) for row in zip(*columns)]
                for j in range(d):
                    center = unit[j] + unit[j]
                    relative = unit[j] + [-x for x in unit[j]]
                    eigenvalue = -2*s*(s+1)/n_particles if j == 0 else 2*s/n_particles
                    check('full_pair_jacobian', matrix_vector(jacobian, center) == [0]*(2*d),
                          (d, s, n_particles, j, 'center'))
                    check('full_pair_jacobian', matrix_vector(jacobian, relative) ==
                          [eigenvalue*x for x in relative], (d, s, n_particles, j, 'relative'))
                check('expansion_not_absolute_norm', 2*s*(s+1)/n_particles > 2*s/n_particles,
                      (d, s, n_particles))

                moment_rows = [(s, Q(0)), (q, Q(1))]
                for b in (Q(3, 2), Q(2), Q(5)):
                    moment_rows += [(b*s, Q(0)), (b*q, b)]
                spatial_order = 2*d+1
                moment_rows += [(Q(2*spatial_order), Q(spatial_order)),
                                (Q(4*spatial_order), Q(2*spatial_order))]
                for alpha, m in moment_rows:
                    derivatives = [unit_power(squared_distance(v), -alpha/2) for v in unit]
                    laplacian = sum((2*f[2] for f in derivatives), Q(0))
                    check('radial_laplacian', laplacian == alpha*(alpha+2-d), (d,s,alpha,m))
                    check('all_required_moments', alpha > m >= 0, (d,s,alpha,m))
                    for nu in (Q(0), Q(1, 7), Q(3)):
                        direct = 2*nu*laplacian + 2*s*derivatives[0][1]/n_particles + 2*s*m/n_particles
                        expected = 2*nu*alpha*(alpha+2-d)-2*s*(alpha-m)/n_particles
                        check('generator_and_relative_factors', direct == expected,
                              (d,s,n_particles,nu,alpha,m))
                        clipped = 2*nu*alpha*max(alpha+2-d,0)-2*s*(alpha-m)/n_particles
                        check('positive_part_majorant', direct <= clipped,
                              (d,s,n_particles,nu,alpha,m))

            # Direct differentiation of a quadratic-test source at e_1.
            hessian = [[Q(2 if i == j else (-1 if (i+j) % 2 else 1), 3)
                        for j in range(d)] for i in range(d)]
            hessian_bound = max(sum(abs(x) for x in row) for row in hessian)
            source_derivatives = []
            for direction in unit:
                positions = [series(int(i == 0), direction[i]) for i in range(d)]
                quadratic = series(0)
                for i in range(d):
                    for j in range(d):
                        quadratic = add(quadratic, scale(mul(positions[i], positions[j]), hessian[i][j]))
                direct_source = scale(mul(quadratic, unit_power(squared_distance(direction), -p/2)),s)
                source_derivatives.append(direct_source[1])
                expected = s*(2*hessian[direction.index(1)][0] -
                              p*hessian[0][0]*direction[0])
                check('source_difference_and_derivative', direct_source[1] == expected, (d,s,direction))
            check('source_gradient_constant', 2*dot(source_derivatives,source_derivatives) <=
                  2*(s*(s+2)*hessian_bound)**2, (d,s))

            # Exact exponent cancellation and endpoint integrability.
            check('rescaling_exponents', (Q(2)/p)*(p/s) == Q(2)/s, (d,s))
            check('rescaling_exponents', -1+p/p == 0 and Q(2)/p-Q(2)/p == 0, (d,s))
            exponent = s/d-1+Q(2)/p
            check('microscopic_regime', exponent == s*(s+2-d)/(d*p), (d,s))
            check('microscopic_regime', exponent <= 0 and ((exponent == 0) == (s == d-2)), (d,s))
            check('integrability_and_boundary', d-s > 0 and d-q >= 1 and d-1-s >= 1, (d,s))
            check('density_versus_atom', (p<d) if s<d-2 else (p==d), (d,s))

            # Choose an exact rational optimizer even for rational s.
            optimizer = Q(2)**s.denominator
            optimizer_to_s = Q(2)**s.numerator
            for bcoef in (Q(1), Q(7,3)):
                acoef = p*bcoef*optimizer_to_s/4
                derivative = 2*acoef*optimizer - (bcoef/2)*p*optimizer*optimizer_to_s
                value = acoef*optimizer**2 - (bcoef/2)*optimizer**2*optimizer_to_s
                check('young_optimizer', derivative == 0, (d,s,bcoef))
                check('young_optimizer', value == (s/p)*acoef*optimizer**2, (d,s,bcoef))
                for multiple in (Q(1,2),Q(1),Q(2)):
                    # Rational roots parameterize another point exactly.
                    trial = multiple**s.denominator
                    trial_s = multiple**s.numerator
                    trial_value = acoef*trial**2-(bcoef/2)*trial**2*trial_s
                    check('young_optimizer', trial_value <= value, (d,s,bcoef,multiple))

    # Fourier algebra: coefficients of g are rational in angle coordinates.
    # Constants 2*pi are factored out on both sides, never estimated numerically.
    for k in range(-3,4):
        for ell in range(-3,4):
            c = Q(7,5)
            d_k, d_ell = (c if k else Q(0)), (c if ell else Q(0))
            atom_plus_compensation = -2*c+c*int(k==0)+c*int(ell==0)
            multiplier = -d_k-d_ell
            check('both_coulomb_responses', atom_plus_compensation == multiplier, (k,ell))
            if k:
                g_k = c/(k*k)
                # i*k dot i*k*g_k = -k^2*g_k.
                check('direct_fourier_sign', -(k*k)*g_k == -d_k, k)
            for degree in (1,2,3):
                check('weak_derivative_commutation', k**degree*multiplier == multiplier*k**degree,(k,ell,degree))
            for order in range(6):
                # With constant source, the r^order response insertion has
                # integral tau^(order+1)/(order+1)!.
                coefficient = multiplier**order/Q(factorial(order+1))
                derivative_coefficient = (order+1)*coefficient
                check('time_simplex_and_limit_equation', derivative_coefficient ==
                      multiplier**order/Q(factorial(order)), (k,ell,order))

    for s_integer in range(1,6):
        s, p = Q(s_integer), Q(s_integer+2)
        for n_particles in (2,3,17):
            c = 2*s*p
            profile = scale(add(unit_power(series(1,c/n_particles),Q(2)/p),series(-1)),Q(n_particles,4))
            check('radial_exact_profile', profile[0] == 0 and profile[1] == s, (s,n_particles))
            check('radial_exact_profile', 2*profile[2] == -2*s**3/n_particles, (s,n_particles))
            tau = Q(n_particles)*(2**int(p)-1)/(2*s*p)
            value = Q(n_particles,4)*3
            derivative = Q(n_particles,2)*(Q(1,2)**int(s)-1)
            check('radial_weight_bounds', value <= s*tau and abs(derivative) <= s*s*tau,
                  (s,n_particles))
        # Shrinking-scale profile: final radius twice the rescaled initial radius.
        tau = Q(2**int(p)-1)/(2*s*p)
        check('excluded_weighted_sup_limit', Q(3,4) < s*tau, s)

    check('sobolev_spatial_exponent', all(2*d+1>2*d for d in range(3,10)), None)
    check('no_h1_from_weight', 2*(Q(1)+1)>3, (3,1))
    check('zero_horizon', all(Q(0)**(k+1)/factorial(k+1)==0 for k in range(12)), None)
    return {
        'status':'PASS',
        'evidence_class':'EXACT_FINITE_DIAGNOSTICS_NOT_ANALYTIC_CERTIFICATION',
        'total_checks':sum(COUNTS.values()),
        'counts':COUNTS,
        'parameter_rows':[{'d':d,'s':str(s)} for d,s in parameter_rows],
        'integer_particle_numbers':[2,3,17],
        'arithmetic':'fractions.Fraction and truncated formal Taylor series',
        'random_seed':None,
        'floating_point_tolerance':None,
        'dependencies':'Python standard library only',
        'source_reads':'none; no prior or constructor checker was read',
        'unverified_by_computation':['singular stochastic stopping passages','simultaneous local starts',
            'uniform integrability of derivatives','infinite response series convergence',
            'weighted convolution estimates','uniform local and global convergence'],
    }


if __name__ == '__main__':
    result = run()
    rendered = json.dumps(result,indent=2)+'\n'
    destination = Path(__file__).with_name('rescaled_gradient_hostile_exact_results.json')
    destination.write_text(rendered)
    sys.stdout.write(rendered)
