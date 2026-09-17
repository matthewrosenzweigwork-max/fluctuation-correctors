"""Exact independent checks of the centered factorial partition identity.
Python standard library; rational arithmetic; deterministic inputs; zero tolerance.
Finite tests corroborate the separate general proof and are not that proof.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import factorial


def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for j, block in enumerate(p):
            yield p[:j] + ((first,) + block,) + p[j + 1:]


def product(xs):
    ans = Q(1)
    for x in xs:
        ans *= x
    return ans


def h(slot, x):
    return (x + Q(slot + 1, slot + 2)) ** (1 + slot % 3)


def direct(k, points, mu):
    n = len(points)
    ans = Q(0)
    for r in range(k + 1):
        for slots in combinations(range(k), r):
            unused = [j for j in range(k) if j not in slots]
            bg = product(sum(w * h(j, x) for x, w in mu) for j in unused)
            empirical = sum(product(h(j, points[i]) for j, i in zip(slots, labels))
                            for labels in permutations(range(n), r))
            ans += (-1) ** (k-r) * bg * empirical / n**r
    return ans


def expanded(k, points, mu):
    n = len(points)
    ans = Q(0)
    for p in partitions(list(range(k))):
        coef = product((-1) ** (len(b)-1) * factorial(len(b)-1) for b in p)
        terms = []
        for b in p:
            eta = sum(product(h(j, x) for j in b) for x in points) / n
            if len(b) == 1:
                eta -= sum(w*h(b[0], x) for x,w in mu)
            terms.append(eta)
        ans += coef * product(terms) / n**(k-len(p))
    return ans


def main():
    tests = 0
    measures = [((Q(-1), Q(1,3)), (Q(2), Q(2,3))),
                ((Q(-2), Q(1,5)), (Q(0), Q(1,2)), (Q(3), Q(3,10)))]
    for k in range(1,8):
        ps = list(partitions(list(range(k))))
        assert sum(product(factorial(len(b)-1) for b in p) for p in ps) == factorial(k)
        for p in ps:
            singles = sum(len(b)==1 for b in p)
            assert 2*(k-len(p))+singles >= k
        for n in (2,3,4):
            for shift in (0,1):
                points = [Q(2*i-n+shift,n+1) for i in range(n)]
                for mu in measures:
                    a,b = direct(k,points,mu), expanded(k,points,mu)
                    assert a == b, (k,n,shift,a,b)
                    tests += 1
    print(f"PASS: {tests} exact rational identities, k=1..7, N=2,3,4, including k>N")
    print("PASS: absolute partition weight k! and fluctuation exponent inequality through k=7")
    print("Interpretation: deterministic finite tests, not an all-order proof or singular estimate")


if __name__ == '__main__':
    main()
