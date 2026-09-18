#!/usr/bin/env python3
"""Fresh exact finite killed-chain diagnostics; no singular-diffusion simulation."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json

counts=Counter();mutations={}
def check(cat,ok):
    if not ok: raise AssertionError(cat)
    counts[cat]+=1
def mutation(name,right,wrong):
    if right != wrong and name not in mutations:
        mutations[name]={'correct':str(right),'mutated':str(wrong)}
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def trans(a):return [list(x) for x in zip(*a)]
def power(a,n):
    out=[[F(int(i==j)) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):out=mm(out,a)
    return out
P=[[F(1,2),F(1,3),F(1,6)],[F(1,4),F(1,2),F(1,4)],[F(1,8),F(3,8),F(1,2)]]
m=len(P);lam=F(1,2);Q=[[lam*P[j][i] for j in range(m)] for i in range(m)]
for i in range(m):
    check('P_conservative',sum(P[i])==1)
    check('Q_subMarkov',0<sum(Q[i])<1)
    check('killed_Haar_left_eigenmeasure',sum(Q[j][i] for j in range(m))==lam)
check('survival_depends_on_start',len({sum(row) for row in Q})>1)
mutation('pretend_attractive_conservative',sum(Q[0]),F(1))
mutation('pretend_pointwise_survival_constant',sum(Q[0]),lam)
observations=[]
for n in range(1,7):
    pn=power(P,n);qn=power(Q,n)
    surviving=sum((sum(row) for row in qn),F(0))/m
    check('exact_survival_normalization',surviving==lam**n)
    for i,j in product(range(m),repeat=2):
        check('semigroup_adjoint_factor',pn[i][j]==qn[j][i]/lam**n)
        mutation('drop_exponential_factor',pn[i][j],qn[j][i])
        mutation('reverse_exponential_sign',pn[i][j],qn[j][i]*lam**n)
    for j in range(m):
        check('surviving_terminal_Haar',sum(qn[i][j] for i in range(m))/m==lam**n/m)
        density=sum(pn[i][j] for i in range(m))
        check('actual_density_from_survival',density==sum(qn[j])/lam**n)
        mutation('mistake_repulsive_law_for_Haar',density,F(1))
    for path in product(range(m),repeat=n+1):
        forward=F(1,m);reverse=F(1,m)
        for a,b in zip(path,path[1:]):
            forward*=P[a][b];reverse*=Q[b][a]
        check('entire_discrete_path_reversal',forward==reverse/lam**n)
        mutation('one_step_normalization_for_long_path',forward,reverse/lam)
        nonreversed=F(1,m)
        for a,b in zip(path,path[1:]):nonreversed*=Q[a][b]
        mutation('omit_path_reversal',forward,nonreversed/lam**n)
    for values in [(F(-1),F(0),F(2)),(F(1,3),F(-2,7),F(5,6))]:
        for A in [F(0),F(1,3),F(3,4),F(1)]:
            direct=sum((F(1,m)*pn[i][j]*(values[j]-A*values[i])**2 for i,j in product(range(m),repeat=2)),F(0))
            dual=sum((F(1,m)*qn[j][i]*(values[j]-A*values[i])**2 for i,j in product(range(m),repeat=2)),F(0))/lam**n
            wrong=sum((F(1,m)*qn[j][i]*(values[i]-A*values[j])**2 for i,j in product(range(m),repeat=2)),F(0))/lam**n
            check('conditional_endpoint_defect_orientation',direct==dual)
            mutation('reverse_response_orientation',direct,wrong)
    observations.append({'steps':n,'survival':str(surviving),'actual_density':[str(sum(pn[i][j] for i in range(m))) for j in range(m)]})
# Exact bounded-domain conjugation algebra, using rational positive weights.
# These are abstract symmetric-kernel checks, not proposed killed SDE kernels.
for weights in [(F(1),F(2),F(3)),(F(1,2),F(3,2),F(5,2))]:
    S=[[F(2,101),F(1,101),F(3,101)],[F(1,101),F(4,101),F(2,101)],[F(3,101),F(2,101),F(5,101)]]
    for b in [F(3,2),F(2),F(5,3)]:
        p=[[b*weights[i]*S[i][j]/weights[j] for j in range(m)] for i in range(m)]
        q=[[S[i][j]*weights[j]/(b*weights[i]) for j in range(m)] for i in range(m)]
        for i,j in product(range(m),repeat=2):
            check('bounded_domain_conjugation',p[i][j]==b*b*q[j][i])
            mutation('wrong_potential_weight_direction',p[i][j],b*weights[j]*S[i][j]/weights[i])
            mutation('use_half_divergence_exponent',p[i][j],b*q[j][i])
# Formal coefficient balances in the actual 4D diffusion formulas.
for N in range(2,42):
    pairs=F(N*(N-1),2)
    kappa_over_c=2*pairs/N
    check('two_coordinate_Coulomb_laplacian',kappa_over_c==N-1)
    mutation('omit_pair_coordinate_two',kappa_over_c,pairs/N)
    for nu in [F(1,11),F(1),F(7,3)]:
        covariance=2*nu
        ito_drift=covariance/2*kappa_over_c
        coefficient=F(1,2)/nu
        check('Girsanov_Ito_divergence_half',coefficient*ito_drift==kappa_over_c/2)
        mutation('use_noise_variance_nu',coefficient*ito_drift,coefficient*(nu/2*kappa_over_c))
        check('Feynman_Kac_force_square_coefficient',F(1,2)/covariance==F(1,4)/nu)
        mutation('omit_Girsanov_quadratic_half',F(1,2)/covariance,F(1)/covariance)
# Full generator/transposition identity in a finite sub-Markov analogue.
G=[[F(-3),F(1),F(2)],[F(2),F(-3),F(1)],[F(1),F(4),F(-5)]]
kappa=F(5)
A=[[G[j][i]-kappa*int(i==j) for j in range(m)] for i in range(m)]
for j in range(m):
    check('killed_generator_left_eigenmeasure',sum(A[i][j] for i in range(m))==-kappa)
for i in range(m):check('killed_generator_nonpositive_row_sum',sum(A[i])<=0)
required={'pretend_attractive_conservative','pretend_pointwise_survival_constant','drop_exponential_factor','reverse_exponential_sign','mistake_repulsive_law_for_Haar','one_step_normalization_for_long_path','omit_path_reversal','reverse_response_orientation','wrong_potential_weight_direction','use_half_divergence_exponent','omit_pair_coordinate_two','use_noise_variance_nu','omit_Girsanov_quadratic_half'}
check('all_mutations_nonzero',set(mutations)==required)
print(json.dumps({'status':'PASS','assertions':sum(counts.values()),'categories':dict(sorted(counts.items())),'mutations':mutations,'mutation_count':len(mutations),'observations':observations,'arithmetic':'exact Fraction','seed':None,'dependencies':'Python standard library','scope':'Finite sub-Markov and coefficient diagnostics only. No singular process simulation, proof of lifetime law by computation, or critical cancellation.'},indent=2,sort_keys=True))
