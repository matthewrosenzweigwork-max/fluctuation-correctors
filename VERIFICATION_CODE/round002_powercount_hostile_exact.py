#!/usr/bin/env python3
"""Independent rational checks for TASK-018, without constructor code.

The four-state table contains values and first derivatives (divided by 2*pi)
of smooth Fourier functions on the quarter-circle grid. Arbitrary finite
background weights test the algebraic identity; they are not a new law-class
assumption in the smooth stochastic theorem.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial

ONE, COS, SIN, MIX = range(4)
vals = (
    (1, 1, 1, 1),
    (1, 0, -1, 0),
    (0, 1, 0, -1),
    (2, 2, 0, 0),
)
ders = (
    (0, 0, 0, 0),
    (0, -1, 0, 1),
    (1, 0, -1, 0),
    (1, -1, -1, 1),
)
mu = (F(1, 2), F(1, 4), F(1, 8), F(1, 8))
muval = tuple(sum(p*x for p, x in zip(mu, v)) for v in vals)


@lru_cache(None)
def partitions(k):
    if k == 0:
        return ((),)
    ans = []
    for pi in partitions(k-1):
        ans.append(pi + ((k-1,),))
        for j in range(len(pi)):
            ans.append(pi[:j] + (pi[j] + (k-1,),) + pi[j+1:])
    return tuple(ans)


def direct(terms, positions, den, excluded=None, root_derivative=None):
    """Original occupied-subset/injective-label definition, no partitions."""
    available = tuple(i for i in range(len(positions)) if i != excluded)
    k = len(terms[0][1])
    total = F(0)
    for coeff, hs in terms:
        for r in range(min(k, len(available))+1):
            for slots in combinations(range(k), r):
                vacant = tuple(j for j in range(k) if j not in slots)
                base = coeff * F((-1)**(k-r), den**r)
                for j in vacant:
                    base *= muval[hs[j]]
                for labels in permutations(available, r):
                    if root_derivative is not None and root_derivative not in labels:
                        continue
                    value = base
                    for j, i in zip(slots, labels):
                        table = ders if i == root_derivative else vals
                        value *= table[hs[j]][positions[i]]
                    total += value
    return total


def partition_value(terms, positions, den, excluded=None):
    """Claimed partition formula, as a separate evaluation algorithm."""
    available = tuple(i for i in range(len(positions)) if i != excluded)
    k = len(terms[0][1])
    total = F(0)
    for coeff, hs in terms:
        for pi in partitions(k):
            a = k-len(pi)
            term = coeff*F((-1)**a, den**a)
            for block in pi:
                term *= factorial(len(block)-1)
                table = [1]*4
                for j in block:
                    table = [x*y for x, y in zip(table, vals[hs[j]])]
                eta = sum(F(table[positions[i]], den) for i in available)
                if len(block) == 1:
                    eta -= sum(p*x for p, x in zip(mu, table))
                term *= eta
            total += term
    return total


def types(k, r=1):
    if r > k:
        yield ()
        return
    if k == 0:
        yield ()
        return
    # Return a tuple (m_1,...,m_k), using a simple independent recursion.
    def go(size, remaining, acc):
        if size > k:
            if remaining == 0:
                yield tuple(acc)
            return
        for multiplicity in range(remaining//size+1):
            yield from go(size+1, remaining-size*multiplicity,
                          acc+[multiplicity])
    yield from go(1, k, [])


checks = 0
for positions in ((0, 0), (0, 2), (0, 1, 3), (1, 1, 2), (0, 1, 2, 3)):
    N = len(positions)
    for k in range(0, 8):
        families = [
            [(F(1), (ONE,)*k)],
            [(F(1), (MIX,)*k)],
            [(F(1), tuple((COS, SIN, ONE, MIX)[j % 4] for j in range(k)))],
        ]
        if k:
            families.append([
                (F(1, k), tuple(COS if j == a else ONE for j in range(k)))
                for a in range(k)
            ])
        for terms in families:
            assert direct(terms, positions, N) == partition_value(terms, positions, N)
            checks += 1
            for root in (0, N-1):
                assert direct(terms, positions, N, excluded=root) == partition_value(
                    terms, positions, N, excluded=root)
                checks += 1
        if 1 <= k <= 5:
            for terms in (families[0], families[1], families[-1]):
                for root in range(N):
                    lhs = direct(terms, positions, N, root_derivative=root)
                    rooted_terms = [
                        (c*ders[hs[0]][positions[root]], hs[1:])
                        for c, hs in terms
                    ]
                    rhs = F(k, N)*direct(rooted_terms, positions, N, excluded=root)
                    assert lhs == rhs, (N, k, root, lhs, rhs)
                    checks += 1

for rootN in (2, 3):
    N = rootN**2
    A = F(7, 2)
    for k in range(0, 9):
        for p in (1, 2):
            # A rational surrogate R_{pj}=pj+2 tests the exact cycle grouping.
            lhs = F(0)
            for pi in partitions(k):
                j = sum(len(block) == 1 for block in pi)
                delta2 = sum(len(block)-2 for block in pi if len(block) >= 2)
                weight = F(1, rootN**delta2)
                for block in pi:
                    weight *= factorial(len(block)-1)
                lhs += weight*(p*j+2)**j
            rhs = F(0)
            for ms in types(k):
                if not ms:
                    rhs += 1
                    continue
                j = ms[0]
                denom = factorial(j)
                delta2 = 0
                for r, mr in enumerate(ms[1:], 2):
                    denom *= factorial(mr)*r**mr
                    delta2 += (r-2)*mr
                rhs += F(factorial(k)*(p*j+2)**j, denom*rootN**delta2)
            assert lhs == rhs
            checks += 1

        weighted = F(0)
        for pi in partitions(k):
            j = sum(len(block) == 1 for block in pi)
            delta2 = sum(len(block)-2 for block in pi if len(block) >= 2)
            weight = F(1, rootN**delta2)
            for block in pi:
                weight *= factorial(len(block)-1)
            weighted += weight*A**j
        gf = factorial(k)*sum(
            (A-rootN)**(k-r)/factorial(k-r)
            * F(comb(N+r-1, r), rootN**r)
            for r in range(k+1)
        )
        assert weighted == gf
        checks += 1

for N in (2, 3, 5):
    for k in range(0, 13):
        falling = 1
        theta = F(0)
        for r in range(k+1):
            if r:
                falling *= N-r+1
            theta += F((-1)**(k-r)*comb(k, r)*falling, N**r)
        # Independent coefficient of e^-z times (1+z/N)^N.
        coeff = factorial(k)*sum(
            F((-1)**(k-r)*comb(N, r), factorial(k-r)*N**r)
            for r in range(min(k, N)+1)
        )
        assert theta == coeff
        checks += 1

vectors = ((3, 4), (5, 12), (-4, 3), (-8, -6))
norms = (5, 13, 5, 10)
for m in range(1, 9):
    hilbert = scalar = F(0)
    for signs in product((-1, 1), repeat=len(vectors)):
        x = sum(s*v[0] for s, v in zip(signs, vectors))
        y = sum(s*v[1] for s, v in zip(signs, vectors))
        z = sum(s*n for s, n in zip(signs, norms))
        hilbert += F((x*x+y*y)**m, 2**len(vectors))
        scalar += F(z**(2*m), 2**len(vectors))
    gaussian = factorial(2*m)//(2**m*factorial(m)) * sum(n*n for n in norms)**m
    assert hilbert <= scalar <= gaussian
    checks += 2

for k in range(1, 9):
    for ell in range(1, 9):
        for beta in (F(1, 100), F(1, 2), F(1), F(3), F(100)):
            rootN, N = 3, 9
            sigma2 = N*min(beta, F(1))
            raw = F(1, 1)/beta / rootN**(k+ell)
            claimed = min(F(1), 1/beta)*F(N, rootN**(k+ell))
            assert sigma2*raw == claimed
            checks += 1

# Scope witness: the compact first-slot derivative formula requires symmetry.
for positions in ((1, 0), (1, 0, 2)):
    N = len(positions)
    nonsymmetric = [(F(1), (ONE, COS))]
    derivative = direct(nonsymmetric, positions, N, root_derivative=0)
    assert derivative == F(1, N*N)  # h'(quarter circle)/(2*pi)=-1.
    first_slot_rhs = F(2, N)*direct(
        [(F(0), (COS,))], positions, N, excluded=0)
    assert first_slot_rhs == 0 and derivative != first_slot_rhs
    symmetric = [(F(1, 2), (ONE, COS)), (F(1, 2), (COS, ONE))]
    rooted = [(c*ders[hs[0]][positions[0]], hs[1:]) for c, hs in symmetric]
    assert direct(symmetric, positions, N, root_derivative=0) == (
        F(2, N)*direct(rooted, positions, N, excluded=0))
    checks += 3

print(f"PASS: {checks} independent exact rational checks")
print("Partition/rooted conversion through order 7; root derivatives through order 5.")
print("Coincident coordinates, unused slots, nonuniform finite background, k>N included.")
print("Cycle grouping and generating function through order 8; iid biases through 12.")
print("Hilbert sign moments through degree 16; every tested temperature/bracket power.")
print("Scope witness confirmed: unsymmetrized first-slot gradient formula fails.")
print("No constructor code used; finite tests support, but do not replace, the analytic audit.")
