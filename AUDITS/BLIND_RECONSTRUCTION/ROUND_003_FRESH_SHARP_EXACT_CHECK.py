#!/usr/bin/env python3
"""Exact finite-group checks supporting the fresh THM-019 reconstruction.

This checks only finite iid algebra and exponent identities. It is not a
numerical verification of a singular-kernel probability limit.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json

checks = 0
configurations = 0
records = []
def check(condition):
    global checks
    assert condition
    checks += 1

m = 7
raw = [7, 4, -1, -5, -5, -1, 4]
avg = F(sum(raw), m)
g = [F(x) - avg for x in raw]
inside = [min(j, m-j) <= 1 for j in range(m)]
i = [g[j] if inside[j] else F(0) for j in range(m)]
h = [g[j] - i[j] for j in range(m)]
tau = sum(i, F(0)) / m
k = [z + tau for z in h]
q = F(sum(inside), m)
k2 = sum((z*z for z in k), F(0)) / m
check(sum(g, F(0)) == 0)
check(sum(k, F(0)) == 0)
check(all(z >= 0 for z in i))

for n in (2, 3, 4, 5):
    edges = list(combinations(range(n), 2))
    M = len(edges)
    sums = {name: F(0) for name in ('P', 'I', 'T', 'T2', 'absT', 'absInnerCentered', 'Z', 'Z2')}
    edge_pairs = list(combinations(range(M), 2))
    joint = [0 for _ in edge_pairs]
    D = F(M, n*n) * tau
    for x in product(range(m), repeat=n):
        configurations += 1
        ds = [(x[a]-x[b]) % m for a,b in edges]
        P = sum((g[z] for z in ds), F(0)) / (n*n)
        I = sum((i[z] for z in ds), F(0)) / (n*n)
        T = sum((k[z] for z in ds), F(0)) / (n*n)
        indicators = [inside[z] for z in ds]
        Z = sum(indicators)
        check(P == I + T - D)
        values = {'P':P, 'I':I, 'T':T, 'T2':T*T, 'absT':abs(T), 'absInnerCentered':abs(I-D), 'Z':F(Z), 'Z2':F(Z*Z)}
        for name, value in values.items():
            sums[name] += value
        for idx, (e,f) in enumerate(edge_pairs):
            joint[idx] += int(indicators[e] and indicators[f])
    denom = m**n
    means = {name:value/denom for name,value in sums.items()}
    check(means['P'] == 0)
    check(means['T'] == 0)
    check(means['I'] == D)
    check(means['T2'] == F(M,n**4)*k2)
    check(means['Z'] == M*q)
    check(means['Z2'] == M*q + M*(M-1)*q*q)
    check(means['absInnerCentered'] <= 2*D)
    check(means['absT']**2 <= means['T2'])
    for count in joint:
        check(F(count,denom) == q*q)
    records.append({'N':n, 'configurations':denom, 'mean_close_count':str(means['Z']), 'second_close_moment':str(means['Z2']), 'outer_variance':str(means['T2']), 'pairwise_indicator_checks':len(joint)})

samples = [(1,F(2,3)), (1,F(3,4)), (1,F(4,5)), (2,F(3,2)), (3,F(2)), (4,F(3))]
for d,s in samples:
    u = 2*s/d - 2
    check(-F(2,d)*(d-s) == u)
    check(-2-F(2,d)*(d-2*s) == 2*u)
    check(F(1,2)+u == 2*s/d-F(3,2))
    check(2*(F(1,2)+u) == 4*s/d-3)
    check(2*s-d > 0)
    check(d-s > 0)

result = {'status':'PASS', 'checks':checks, 'configurations':configurations, 'finite_group_order':m, 'normalization':'unordered pairs divided by N^2', 'records':records, 'limitations':'Exact finite iid algebra and exponent checks only; no claim of empirical probability-limit verification.'}
print(json.dumps(result, indent=2, sort_keys=True))
