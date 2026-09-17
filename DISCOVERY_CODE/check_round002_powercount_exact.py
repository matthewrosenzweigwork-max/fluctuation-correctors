#!/usr/bin/env python3
"""Exact finite self-checks for TASK-013; no external libraries or randomness."""

from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import comb, factorial
import json


COUNTS = {}


def check(name, actual, expected):
    if actual != expected:
        raise AssertionError((name, actual, expected))
    COUNTS[name] = COUNTS.get(name, 0) + 1


def prod(items):
    out = F(1)
    for item in items:
        out *= item
    return out


@lru_cache(None)
def partitions(n):
    if n == 0:
        return ((),)
    out = []
    for previous in partitions(n-1):
        out.append(previous + ((n-1,),))
        for i in range(len(previous)):
            out.append(previous[:i] + (previous[i] + (n-1,),) + previous[i+1:])
    return tuple(out)


def kernel(xs):
    return 2 + sum(xs) + prod(1+x for x in xs)


def background_average(prefix, count):
    mu = (F(1, 3), F(2, 3))
    return sum((prod(mu[y] for y in tail)*kernel(tuple(prefix)+tail)
                for tail in product((0, 1), repeat=count)), F(0))


def direct_u(xs, k):
    n = len(xs)
    return sum(((-1)**(k-r)*F(comb(k, r), n**r)
                * sum((background_average(tuple(xs[i] for i in labels), k-r)
                       for labels in permutations(range(n), r)), F(0))
                for r in range(min(k, n)+1)), F(0))


def partition_u(xs, k):
    n = len(xs)
    eta = (F(xs.count(0), n), F(xs.count(1), n))
    rho = (eta[0]-F(1, 3), eta[1]-F(2, 3))
    total = F(0)
    for pi in partitions(k):
        exponent = k-len(pi)
        coefficient = F((-1)**exponent, n**exponent)
        coefficient *= prod(factorial(len(block)-1) for block in pi)
        term = F(0)
        for values in product((0, 1), repeat=len(pi)):
            args = [None]*k
            weight = F(1)
            for block, value in zip(pi, values):
                weight *= (rho if len(block) == 1 else eta)[value]
                for position in block:
                    args[position] = value
            term += weight*kernel(args)
        total += coefficient*term
    return total


def factorial_h(xs, labels, r):
    return sum((prod(1+xs[i] for i in selected)
                for selected in permutations(labels, r)), F(0))


def check_root_gradient(xs, k, i):
    n = len(xs)
    mu_h = F(5, 3)
    labels = tuple(j for j in range(n) if j != i)
    direct = sum(((-1)**(k-r)*F(comb(k, r)*r, n**r)
                  * mu_h**(k-r)*factorial_h(xs, labels, r-1)
                  for r in range(1, min(k, n)+1)), F(0))
    rooted = F(k, n)*sum(
        ((-1)**(k-1-r)*F(comb(k-1, r), n**r)
         * mu_h**(k-1-r)*factorial_h(xs, labels, r)
         for r in range(min(k-1, n-1)+1)), F(0))
    check("rooted_gradient", direct, rooted)


def cycle_types(total, size=1):
    if size > total:
        yield {}
        return
    # This generator uses an independent integer-partition construction.
    def rec(remaining, r, counts):
        if r == total+1:
            if remaining == 0:
                yield dict(counts)
            return
        for number in range(remaining//r+1):
            if number:
                counts[r] = number
            else:
                counts.pop(r, None)
            yield from rec(remaining-r*number, r+1, counts)
        counts.pop(r, None)
    yield from rec(total, 1, {})


def partition_constant_types(k, sqrt_n, singleton):
    total = F(0)
    for counts in cycle_types(k):
        denominator = prod(factorial(number)*r**number for r, number in counts.items())
        extra = sum((r-2)*number for r, number in counts.items() if r >= 2)
        total += F(factorial(k), 1)/denominator * singleton**counts.get(1, 0)/sqrt_n**extra
    return total


def bell_recurrence(kmax, weights):
    result = [F(1)]
    for k in range(1, kmax+1):
        result.append(sum((comb(k-1, r-1)*weights(r)*result[k-r]
                           for r in range(1, k+1)), F(0)))
    return result


def falling(n, r):
    if r > n:
        return 0
    return factorial(n)//factorial(n-r)


def double_factorial_odd(m):
    return factorial(2*m)//(2**m*factorial(m))


def main():
    configurations = ((0, 1), (1, 1), (0, 0, 1), (0, 1, 1))
    for xs in configurations:
        for k in range(8):
            check("partition_conversion", partition_u(xs, k), direct_u(xs, k))
            if k:
                for i in range(len(xs)):
                    check_root_gradient(xs, k, i)

    for singleton in (F(1), F(2), F(5)):
        unweighted = bell_recurrence(12, lambda r: singleton if r == 1 else factorial(r-1))
        for k in range(13):
            closed = factorial(k)*sum(((singleton-1)**r/F(factorial(r))
                                      for r in range(k+1)), F(0))
            check("fixed_point_cycle_polynomial", unweighted[k], closed)
        for sqrt_n in (F(2), F(3)):
            weighted = bell_recurrence(
                12, lambda r: singleton if r == 1 else F(factorial(r-1))/sqrt_n**(r-2))
            for k in range(13):
                check("weighted_partition_order_constant", weighted[k],
                      partition_constant_types(k, sqrt_n, singleton))

    for n in (2, 3, 7):
        bias_from_log = bell_recurrence(
            16, lambda r: F(0) if r == 1 else F((-1)**(r-1)*factorial(r-1), n**(r-1)))
        for k in range(17):
            bias_direct = sum(((-1)**(k-r)*F(comb(k, r)*falling(n, r), n**r)
                               for r in range(k+1)), F(0))
            check("iid_bias_generating_function", bias_from_log[k], bias_direct)

    for vectors in (((1, 0), (0, 2), (-1, 1)), ((1, 2), (1, -2)), ((0, 0), (3, 0))):
        square_norm_sum = sum(sum(a*a for a in v) for v in vectors)
        for m in range(1, 9):
            expected = F(0)
            for signs in product((-1, 1), repeat=len(vectors)):
                point = tuple(sum(sign*v[a] for sign, v in zip(signs, vectors)) for a in range(2))
                expected += F(sum(x*x for x in point)**m, 2**len(vectors))
            bound = double_factorial_odd(m)*square_norm_sum**m
            check("hilbert_rademacher_moment_bound", expected <= bound, True)

    for sqrt_n in (F(2), F(3)):
        n = sqrt_n**2
        for beta in (F(1, 100), F(1), F(100)):
            sigma_squared = n*min(beta, F(1))
            for k, ell in product(range(1, 6), repeat=2):
                check("all_order_temperature_bracket_power",
                      sigma_squared/beta/sqrt_n**(k+ell),
                      min(F(1), 1/beta)*n/sqrt_n**(k+ell))

    print(json.dumps({
        "status": "PASS",
        "total_checks": sum(COUNTS.values()),
        "checks": COUNTS,
        "arithmetic": "exact Fraction/integer; no tolerance or random seed",
        "scope": "same-context finite self-checks, not an independent audit"
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
