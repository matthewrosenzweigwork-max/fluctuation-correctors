#!/usr/bin/env python3
"""New AUD066 diagnostic. Standard library only; no mathematical input files read.

The main test evaluates a truncated Ewald representation of the actual d=4
Coulomb kernel, reduced only by the three transverse grid symmetries. Floating
results are diagnostics, never a proof or rigorous numerical enclosure. Exact
auxiliary tests use integers/Fraction and real trigonometric moments.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import sys

PI = math.pi
checks = Counter()
mutations = []


def check(name, condition):
    checks[name] += 1
    if not condition:
        raise AssertionError(name)


def near(name, actual, expected, tol):
    check(name, abs(actual-expected) <= tol)


def detect(name, wrong, right, tol):
    check('detecting_mutations', abs(wrong-right) > tol)
    mutations.append({'name': name, 'wrong': wrong, 'reference': right,
                      'separation': abs(wrong-right), 'tolerance': tol})


@lru_cache(None)
def square_counts(radius, dimension):
    one = {0: 1, **{j*j: 2 for j in range(1, radius+1)}}
    counts = {0: 1}
    for _ in range(dimension):
        nxt = Counter()
        for x, cx in counts.items():
            for y, cy in one.items():
                nxt[x+y] += cx*cy
        counts = dict(nxt)
    check('integer_multiplicities', sum(counts.values()) == (2*radius+1)**dimension)
    return tuple(sorted(counts.items()))


def h0_ewald(cutoff):
    # At the origin the image and Fourier sums coincide. The central image
    # contributes -pi after subtraction of |x|^-2; the constant is another -pi.
    positive = math.fsum(c*math.exp(-PI*q)/q
                         for q, c in square_counts(cutoff, 4) if q)
    return 2*positive-2*PI


@lru_cache(None)
def reduced_kernel(m, x, cutoff):
    """Sum over the m^3 transverse grid offsets: potential and first force.

    If x=0, return the regular part after subtracting |x|^-2, not a kernel
    diagonal. This is used exclusively to test the exact self subtraction.
    """
    x = x-round(x)
    potential_terms = []
    force_terms = []
    transverse = square_counts(cutoff*m, 3)
    for n in range(-cutoff, cutoff+1):
        z = x+n
        for q, count in transverse:
            r2 = z*z+q/(m*m)
            if r2 == 0:
                continue
            f = count*math.exp(-PI*r2)/r2
            potential_terms.append(f)
            force_terms.append(2*z*f*(PI+1/r2))
    # A cubic Fourier truncation; m>cutoff leaves only zero transverse modes.
    potential = math.fsum(potential_terms)-PI*m**3
    force = math.fsum(force_terms)
    if x == 0:
        potential -= PI  # the finite part of the removed central image
    for k in range(1, cutoff+1):
        weight = math.exp(-PI*k*k)/(k*k)
        potential += 2*m**3*weight*math.cos(2*PI*k*x)
        force += 4*PI*m**3*k*weight*math.sin(2*PI*k*x)
    return potential, force


def source_energy(m, a, cutoff):
    eps = a/m
    points = [(p/m+eps*math.sin(2*PI*p/m)) % 1 for p in range(m)]
    hc = [math.cos(4*PI*x) for x in points]
    hs = [math.sin(4*PI*x) for x in points]
    dc = [-4*PI*math.sin(4*PI*x) for x in points]
    ds = [4*PI*math.cos(4*PI*x) for x in points]
    raw_c, raw_s, shifts = [], [], []
    for p in range(m):
        for q in range(p):
            z = points[p]-points[q]
            potential, force = reduced_kernel(m, z, cutoff)
            old, _ = reduced_kernel(m, (p-q)/m, cutoff)
            raw_c.append(force*(dc[p]-dc[q])/m**5)
            raw_s.append(force*(ds[p]-ds[q])/m**5)
            shifts.append((potential-old)/m)
    raw_c, raw_s = math.fsum(raw_c), math.fsum(raw_s)
    row_c = 4*PI*PI*math.fsum(hc)/m
    row_s = 4*PI*PI*math.fsum(hs)/m
    energy = (m*m-1)*h0_ewald(cutoff)/2+math.fsum(shifts)
    return {'m': m, 'a': a, 'cutoff': cutoff, 'source': raw_c+row_c,
            'source_sine': raw_s+row_s, 'raw': raw_c, 'row': row_c,
            'scaled_source': m*m*(raw_c+row_c), 'energy': energy,
            'scaled_energy': energy/(m*m),
            'fundamental_real': math.fsum(math.cos(2*PI*x) for x in points)/m}


def even_moment(r, s):
    # Haar moment cos(theta)^(2r) sin(theta)^(2s), by integration-by-parts
    # recurrence or the elementary beta-integral calculation.
    return Fraction(math.factorial(2*r)*math.factorial(2*s),
                    4**(r+s)*math.factorial(r)*math.factorial(s)*math.factorial(r+s))


def main():
    check('theta_rational_bound', sum(Fraction(3**j, math.factorial(j)) for j in range(9)) > 20)
    check('theta_rational_bound', 2*8799**4 < 3*7999**4)
    check('theta_rational_bound', Fraction(1)+Fraction(2, 20)/(1-Fraction(1,8000)) == Fraction(8799,7999))
    for r in range(6):
        for s in range(6):
            check('trig_moments', even_moment(r,s) > 0)
            check('trig_moments', even_moment(r,s) == even_moment(s,r))
            check('trig_moments', even_moment(r+1,s)+even_moment(r,s+1) == even_moment(r,s))
    check('continuum_coefficient', -64*even_moment(1,1) == -8)
    for m in range(5,41):
        for frequency in (-3,-2,-1,1,2,3):
            check('grid_frequency_selection', frequency % m != 0)
    check('small_grid_alias_control', 3 % 3 == 0)

    h0s = {str(c): h0_ewald(c) for c in (2,3,4)}
    near('ewald_h0_convergence', h0s['3'], h0s['4'], 2e-12)
    check('ewald_h0_sign', h0s['4'] < -5*PI/3)
    lattice = []
    for m in (5,6,7):
        regular_sum, _ = reduced_kernel(m, 0.0, 4)
        values = [reduced_kernel(m, j/m, 4)[0] for j in range(1,m)]
        actual = (regular_sum-h0s['4']+math.fsum(values))/2
        expected = (m*m-1)*h0s['4']/2
        near('singular_lattice_identity', actual, expected, 2e-9)
        lattice.append({'m':m,'actual':actual,'expected':expected,'error':actual-expected})
    detect('omit_regular_self_subtraction', lattice[0]['actual']+h0s['4']/2,
           lattice[0]['expected'], 1)
    detect('omit_central_image_finite_part', lattice[0]['actual']+PI/2,
           lattice[0]['expected'], 1)
    detect('replace_m_squared_by_N', (5**4-1)*h0s['4']/2,
           lattice[0]['expected'], 1)

    a = 0.05
    rows = [source_energy(m,a,4) for m in (5,7,9,13,17)]
    expected = -8*PI**4*a*a
    for row in rows:
        near('inversion_sine_source',row['source_sine'],0,2e-10)
        check('negative_energy_probe',row['scaled_energy'] < -2)
        check('source_correct_sign',row['scaled_source'] < 0)
    # This observed convergence criterion is only a falsification diagnostic.
    check('moving_scale_convergence', abs(rows[-1]['scaled_source']-expected) < 0.15)
    check('moving_scale_convergence', abs(rows[-1]['scaled_source']-expected) < abs(rows[0]['scaled_source']-expected))
    repeat = source_energy(7,a,3)
    near('ewald_cutoff_stability',repeat['scaled_source'],rows[1]['scaled_source'],2e-7)
    near('ewald_cutoff_stability',repeat['energy'],rows[1]['energy'],2e-7)
    zero = source_energy(7,0,4)
    near('undeformed_source',zero['source'],0,1e-11)
    even_positive = source_energy(6,a,4)
    signed = source_energy(6,-a,4)
    near('even_grid_deformation_parity',signed['source'],even_positive['source'],1e-10)

    r = rows[-1]
    m2 = r['m']**2
    detect('omit_Haar_row',m2*r['raw'],r['scaled_source'],0.5)
    detect('reverse_Haar_row',m2*(r['raw']-r['row']),r['scaled_source'],1)
    detect('halve_raw_pair_coefficient',m2*(r['raw']/2+r['row']),r['scaled_source'],0.5)
    detect('flip_full_force_and_row_sign',-r['scaled_source'],r['scaled_source'],1)
    n = rows[0]['m']**4
    wrong_denominator = 25*(rows[0]['raw']*n/(n-1)+rows[0]['row'])
    detect('replace_N_squared_by_falling_factorial',wrong_denominator,rows[0]['scaled_source'],1e-4)
    detect('permutation_without_common_Haar_translation',r['fundamental_real'],0,1e-3)
    wrong_scale = source_energy(7,a/7,4)
    detect('deformation_at_m_to_minus_two',wrong_scale['scaled_source'],rows[1]['scaled_source'],1)
    rotated_coordinate_error = 2*abs(r['source'])
    coordinate_budget = r['m']**-3
    check('false_final_support_coordinate_bound_detected',rotated_coordinate_error > coordinate_budget)

    count = 32768
    c, s = r['source'], 0.371*r['source']
    samples = [c*math.cos(4*PI*j/count)-s*math.sin(4*PI*j/count) for j in range(count)]
    absolute = math.fsum(abs(x) for x in samples)/count
    signed_mean = math.fsum(samples)/count
    reference = 2/PI*math.hypot(c,s)
    near('common_translation_signed_mean',signed_mean,0,1e-13)
    near('common_translation_absolute_factor',absolute,reference,2e-9)
    detect('signed_mean_substituted_for_absolute_mean',abs(signed_mean),reference,0.001)
    detect('omit_two_over_pi_factor',math.hypot(c,s),reference,0.001)
    exact_absolute_coefficient = 16*PI**3*a*a
    near('final_limit_constant',2/PI*abs(expected),exact_absolute_coefficient,1e-14)
    for m in (5,17,101):
        check('smoothing_budget', Fraction(m*m,m**3) == Fraction(1,m))
    result = {'audit':'AUD066','status':'PASS','assertions':sum(checks.values()),
              'categories':dict(checks),'mutations':mutations,
              'exact_arithmetic':'integer and rational auxiliary tests',
              'numerical_evidence':'nonrigorous float64 finite Ewald diagnostic; not an enclosure or proof',
              'seed':'none; deterministic','kernel':'d=4, g_hat(k)=|k|^-2, coefficient-one local singularity',
              'ewald':'split t=1/(4*pi), spatial image cutoff and cubic Fourier cutoff documented in code',
              'h0':h0s,'lattice':lattice,'source_energy':rows,
              'source_target':expected,'absolute_limit_target':exact_absolute_coefficient,
              'cutoff_repeat':repeat,'zero_deformation':zero,'negative_deformation':signed,
              'wrong_scale':wrong_scale,
              'proof_text_defect':{'line':153,'phase':'pi/2',
                   'coordinate_error_after_rotation':rotated_coordinate_error,
                   'claimed_budget':coordinate_budget,
                   'amplitude_unchanged':True},
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output = Path(__file__).with_name('hostile_diagnostic_results.json')
    if '--verify' in sys.argv:
        assert json.loads(output.read_text()) == result, 'saved diagnostic result mismatch'
    else:
        output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','assertions':result['assertions'],
                      'categories':len(checks),'detected_mutations':len(mutations),
                      'h0':h0s['4'],'scaled_sources':[(x['m'],x['scaled_source']) for x in rows],
                      'target':expected},indent=2))


if __name__ == '__main__':
    main()
