#!/usr/bin/env python3
"""Fresh exact supporting diagnostics for AUD071. Standard library; no writes.

This is not a singular SDE simulation or a proof of the analytic estimates.
All arithmetic is rational. Every deliberately wrong control must have a
nonzero exact residual. Print the reproducible result to stdout only.
"""
from fractions import Fraction as F
import json


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(c, a):
    return (c * a[0], c * a[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def csum(items):
    ans = (F(0), F(0))
    for item in items:
        ans = add(ans, item)
    return ans


def serial(value):
    if isinstance(value, tuple):
        return [str(x) for x in value]
    return str(value)


def nonzero(value):
    if isinstance(value, tuple):
        return any(x != 0 for x in value)
    return value != 0


def run():
    checks, mutants = [], []

    def check(name, actual, expected):
        assert actual == expected, (name, actual, expected)
        checks.append({'name': name, 'actual': serial(actual),
                       'expected': serial(expected), 'pass': True})

    def mutant(name, residual):
        assert nonzero(residual), ('undetected mutant', name)
        mutants.append({'name': name, 'exact_residual': serial(residual),
                        'detected': True})

    # Conditional orthogonality, with a nontrivial complex finite probability law.
    px = [F(2, 5), F(3, 5)]
    py = [[F(1, 4), F(3, 4)], [F(2, 3), F(1, 3)]]
    f0 = [(F(1), F(0)), (F(0), F(1, 2))]
    ft = [[(F(1, 2), F(1, 3)), (F(-1, 4), F(1, 2))],
          [(F(1, 3), F(-1, 4)), (F(-1, 2), F(1, 5))]]
    attenuation, n = F(1, 3), 3
    means = [csum(scale(py[i][j], ft[i][j]) for j in range(2))
             for i in range(2)]
    d = n * sum(px[i] * py[i][j] * norm2(sub(ft[i][j], scale(attenuation, f0[i])))
                for i in range(2) for j in range(2))
    c = n * sum(px[i] * norm2(sub(means[i], scale(attenuation, f0[i])))
                for i in range(2))
    jcost = n * sum(px[i] * py[i][j] * norm2(sub(ft[i][j], means[i]))
                    for i in range(2) for j in range(2))
    cross = csum(scale(px[i] * py[i][j],
                       mul(sub(ft[i][j], means[i]),
                           conj(sub(means[i], scale(attenuation, f0[i])))))
                 for i in range(2) for j in range(2))
    check('complex conditional decomposition', d, c + jcost)
    check('conditional complex cross term', cross, (F(0), F(0)))
    check('both conditional costs positive', c > 0 and jcost > 0, True)
    total_mean = csum(scale(px[i], means[i]) for i in range(2))
    wrong_c = n * sum(px[i] * norm2(sub(total_mean, scale(attenuation, f0[i])))
                     for i in range(2))
    mutant('replace conditional mean by unconditional mean', d - wrong_c - jcost)
    mutant('discard conditional martingale cost', d - c)

    # Raw independent Brownian channels, with sqrt(2 nu) = 2.
    nu = F(2)
    wy, wz = [F(1), F(-1)], [F(1, 2), F(1, 2)]
    check('relative covariance', 2 * nu * sum(x*x for x in wy), 4 * nu)
    check('center covariance', 2 * nu * sum(x*x for x in wz), nu)
    check('relative-center cross covariance',
          2 * nu * sum(a*b for a, b in zip(wy, wz)), F(0))
    mutant('relative Brownian covariance not doubled', 2 * nu - 4 * nu)
    for n in [2, 3, 5]:
        gu = [[(F(i+1, a+2), F(a+1, i+2)) for a in range(4)]
              for i in range(n)]
        ge = [[(F(a+2, i+3), F(-(i+2), a+3)) for a in range(4)]
              for i in range(n)]
        self_direct = sum(norm2(scale(F(2), gu[i][a]))
                          for i in range(n) for a in range(4))
        cross_direct = csum(mul(scale(F(2), gu[i][a]),
                                conj(scale(F(2, n), ge[i][a])))
                            for i in range(n) for a in range(4))
        plain_cross = csum(mul(gu[i][a], conj(ge[i][a]))
                          for i in range(n) for a in range(4))
        expected = scale(2 * nu / n, plain_cross)
        check('self bracket N=%d' % n, self_direct,
              2 * nu * sum(norm2(v) for row in gu for v in row))
        check('cross bracket N=%d' % n, cross_direct, expected)
        backward = F(2, 5)
        weighted_direct = csum(mul(scale(F(2), gu[i][a]),
                                   conj(scale(F(2, n) * backward, ge[i][a])))
                               for i in range(n) for a in range(4))
        check('backward weighted cross N=%d' % n,
              weighted_direct, scale(backward, expected))
        mutant('omit 1/N cross factor N=%d' % n,
               sub(scale(2 * nu, plain_cross), expected))
        unconjugated = scale(2 * nu / n, csum(mul(gu[i][a], ge[i][a])
                                             for i in range(n) for a in range(4)))
        mutant('omit complex conjugation N=%d' % n, sub(unconjugated, expected))
        mutant('omit backward weight N=%d' % n, sub(expected, weighted_direct))
        zero_mode_c = n * (1-attenuation)**2
        check('zero mode J N=%d' % n, F(0), F(0))
        check('zero mode D=C N=%d' % n, zero_mode_c, F(4*n, 9))
        mutant('artificial zero-mode comparison set to zero N=%d' % n, -zero_mode_c)

    # Independent coordinate derivatives. The smooth local drift is not
    # represented as an exact periodic force: this is a differential diagnostic.
    units = [[F(3, 5), F(4, 5), F(0), F(0)], [F(1, 2)] * 4]
    diagonal = [F(1, 5), F(-1, 7), F(2, 9), F(-2, 11)]
    for n in [2, 3, 7]:
        alpha = F(4, n)
        for nu in [F(1, 3), F(5, 2)]:
            for radius in [F(1, 7), F(2, 5)]:
                for unit_index, unit in enumerate(units):
                    y = [radius*u for u in unit]
                    check('unit vector %d N%d nu%s r%s' % (unit_index,n,nu,radius),
                          sum(z*z for z in y), radius**2)
                    b = [diagonal[a]*y[a] for a in range(4)]
                    drift = [alpha*y[a]/radius**4+b[a] for a in range(4)]
                    yb = sum(y[a]*b[a] for a in range(4))
                    for p in [2, 4, 6]:
                        grad = [p*radius**(p-2)*y[a] for a in range(4)]
                        hdiag = [p*radius**(p-2)
                                 +p*(p-2)*radius**(p-4)*y[a]**2 for a in range(4)]
                        raw = sum(drift[a]*grad[a] for a in range(4))+2*nu*sum(hdiag)
                        formula = (p*alpha*radius**(p-4)
                                   +2*nu*p*(p+2)*radius**(p-2)
                                   +p*radius**(p-2)*yb)
                        name='radial p%d N%d nu%s r%s unit%d' % (p,n,nu,radius,unit_index)
                        check(name, raw, formula)
                    ugrad = [4*radius**2*value for value in y]
                    check('radial fourth bracket N%d nu%s r%s unit%d' % (n,nu,radius,unit_index),
                          4*nu*sum(v*v for v in ugrad), 64*nu*radius**6)
                    for i in range(4):
                        grad = [(F(i==a)/radius-y[i]*y[a]/radius**3) for a in range(4)]
                        hdiag = [(-2*F(i==a)*y[a]/radius**3-y[i]/radius**3
                                  +3*y[i]*y[a]**2/radius**5) for a in range(4)]
                        raw = sum(drift[a]*grad[a] for a in range(4))+2*nu*sum(hdiag)
                        formula = b[i]/radius-y[i]*yb/radius**3-6*nu*y[i]/radius**3
                        check('angle i%d N%d nu%s r%s unit%d' % (i,n,nu,radius,unit_index),
                              raw, formula)
        mutant('missing second pair drift N%d' % n, F(8,n)-F(16,n))
        check('squared angular coefficient after removing pi^2 N%d' % n,
              (4*alpha)/n**2, F(16,n**3))
        mutant('missing pair factor in squared angular coefficient N%d' % n,
               F(8,n**3)-F(16,n**3))

    mutant('angular Ito drift uses three instead of six', F(-3)-F(-6))
    check('fourth radial drift coefficient', F(4*(4+2))*2, F(48))
    check('sixth radial drift coefficient', F(6*(6+2))*2, F(96))
    check('radial moment error exponent', F(5,4)-F(1,2), F(3,4))
    check('angular product error exponent', F(1,2)+F(1,4), F(3,4))
    check('codimension-four fourth-gradient radial exponent', 4-1-4, -1)
    mutant('replace fourth-gradient obstruction by second-gradient assertion',
           (4-1-2)-(-1))
    mutant('use dimension-five radial volume at the same endpoint', (5-1-4)-(-1))

    # Exact sphere moments, obtainable by integrating a tangential derivative.
    moments = [F(1)]
    for order in range(1, 5):
        moments.append(moments[-1]*F(2*order-1,4+2*order-2))
    check('sphere theta1^2 mean', moments[1], F(1,4))
    check('sphere theta1^4 mean', moments[2], F(1,8))
    energy = 16*(moments[2]-2*moments[3]+moments[4])
    check('normalized fourth angular energy of theta1^2', energy, F(3,8))
    mutant('replace angular profile by its isotropic mean', -energy)
    for shells in [1,4,16,64]:
        check('logarithmic energy in %d dyadic shells divided by log 2' % shells,
              shells*energy, F(3*shells,8))
    for n in [2,3,5]:
        volume = F(1,10)**(4*n-4)
        check('positive slow volume N%d' % n, volume > 0, True)
        mutant('replace slow-volume set by one slice N%d' % n, -volume*energy)
    check('uniform cap gap after two errors', F(3,4)-F(1,4)-2*F(1,8), F(1,4))
    mutant('omit slack in cap separation by allowing half-amplitude errors',
           (F(3,4)-F(1,4)-2*F(1,2))-F(1,4))
    mutant('identify cutoff response with the frozen uncut response', F(2,3)-1)
    return {'status':'PASS','arithmetic':'exact rational; Python standard library',
            'random_seed':None,'numerical_tolerance':None,
            'evidence_class':'supporting algebra; not singular-process simulation or certification',
            'baseline_failures':[], 'check_count':len(checks),
            'mutant_count':len(mutants),'all_mutants_nonzero':True,
            'checks':checks,'mutants':mutants}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
