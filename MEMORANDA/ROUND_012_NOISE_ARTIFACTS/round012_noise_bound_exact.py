"""Exact finite diagnostics of physical normalization and strict parameter scope.

Algebraic arrays below are not laws of the singular dynamics. This checks the
configuration-field bound without assuming any cancellation or pair symmetry
of its first-slot gradient, and checks strict/equality regime distinctions.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

counts = {'configuration_bound': 0, 'physical_prefactor': 0,
          'strict_exponent_scope': 0, 'coulomb_occupation_excluded': 0,
          'boundary_controls': 0}
for n in (2, 3, 4):
    for xs in product(range(3), repeat=n):
        for mode in range(3):
            # Nonzero background and mixed-sign ordered pair fields.
            g = lambda x, y: F((x + 1) * (y - 1) + mode * (x - y), 3)
            row = lambda x: sum((g(x, y) for y in range(3)), F(0)) / 3
            field = [sum((g(xs[i], xs[j]) for j in range(n) if j != i), F(0)) - n * row(xs[i]) for i in range(n)]
            exact = sum((v*v for v in field), F(0)) / n**4
            upper = (2*(n-1)*sum((g(xs[i],xs[j])**2 for i in range(n) for j in range(n) if j!=i),F(0)) + 2*n*n*sum((row(x)**2 for x in xs),F(0))) / n**4
            assert exact <= upper
            counts['configuration_bound'] += 1
            for nu in (F(1,7),F(1),F(3)):
                beta=1/nu; b=min(beta,F(1))
                scaled=2*nu*n*b*upper
                pair_average=sum((g(xs[i],xs[j])**2 for i in range(n) for j in range(n) if j!=i),F(0))/(n*(n-1))
                row_average=sum((row(x)**2 for x in xs),F(0))/n
                assert scaled==4*nu*b*(F((n-1)**2,n*n)*pair_average+row_average)
                counts['physical_prefactor'] += 1
for d in range(3,13):
    for j in range(1,4*(d-2)):
        s=F(j,4); p=s+2; a=s/p; theta=1-s/d
        q=p/2
        assert 1<q<F(d,2) and q<=s+1
        assert 2*(s+1-q)/p==a
        assert (a<theta)==(s*p<2*d)
        chi_exponent=F(2)/p-theta
        assert chi_exponent==s*(s+2-d)/(d*p) and chi_exponent<0
        if s<2:
            assert (s-2)/p<0 and a<theta
        counts['strict_exponent_scope'] += 1
    s=F(d-2); assert s*(d-2-s)==0
    counts['coulomb_occupation_excluded'] += 1
# Exact equality: d=4,s=2 has zero noise-decay exponent and is Coulomb.
assert F(2,4)+F(2,4)-1==0
counts['boundary_controls']+=1
# Below Coulomb at d=6,s=3 lies above the claimed critical range.
assert 3<6-2 and F(3,5)+F(3,6)-1>0
counts['boundary_controls']+=1
# A strict admitted high-s case remains: d=6,s=5/2.
s=F(5,2);assert s<4 and s*(s+2)<12 and s>2
counts['boundary_controls']+=1
out={'status':'PASS','exact_cases':sum(counts.values()),'counts':counts,
     'arithmetic':'exact fractions; no random seed or tolerance',
     'scope':'root finite algebra self-check only; not proof, audit, or actual-law simulation'}
Path(__file__).with_name('ROUND_012_NOISE_EXACT_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
