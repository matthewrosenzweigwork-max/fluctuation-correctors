#!/usr/bin/env python3
"""Exact supporting diagnostics for the root R22 Hilbert path implication."""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path

counts=Counter();mutations={}
def check(name,p):
    assert p,name
    counts[name]+=1

def reject(name,correct,wrong):
    assert correct!=wrong,name
    mutations[name]={'correct':str(correct),'mutated':str(wrong)}

def main():
    # Literal iid sampling on the finite cyclic probability space Z/4Z.
    # This checks real/complex Fourier normalization, not a singular particle law.
    chars=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
    for N in range(2,7):
        er=ei=ec=F(0)
        for labels in product(range(4),repeat=N):
            x=sum((chars[i][0] for i in labels),F(0))/N
            y=sum((chars[i][1] for i in labels),F(0))/N
            complex_pair=2*N*(x*x+y*y)
            real_pair=N*(2*x*x+2*y*y)
            check('literal_real_complex_Hilbert_pair',complex_pair==real_pair)
            er+=2*N*x*x/F(4**N);ei+=2*N*y*y/F(4**N);ec+=complex_pair/F(4**N)
        check('iid_orthonormal_cosine_variance',er==1)
        check('iid_orthonormal_sine_variance',ei==1)
        check('two_opposite_mode_trace',ec==2)
        reject('drop_real_basis_normalization_N'+str(N),ec,ec/2)
    # Exact positive-kernel convolution identity, including the old-history term.
    for q in [F(0),F(1,4),F(1,2),F(9,10),F(1)]:
        for increments in product([-2,-1,0,1,2],repeat=4):
            B=[F(0)];M=[F(0)]
            for inc in increments:
                B.append(B[-1]+inc);M.append(q*M[-1]+inc)
            for j in range(1,5):
                rhs=B[j]-(1-q)*sum((q**(j-1-i)*B[i] for i in range(1,j)),F(0))
                check('literal_convolution_integration_by_parts',M[j]==rhs)
            check('pathwise_convolution_maximum',max(map(abs,M))<=2*max(map(abs,B)))
    q=F(1,2);old=q-1
    reject('moving_terminal_convolution_is_martingale',old,F(0))
    # Exact orthogonal weighted projections and supremum versus coordinate sums.
    for r in [2,5,11]:
        weights=[F(1,(1+k*k)**r) for k in [1,2,3]]
        for v in product([-2,0,3],repeat=3):
            total=sum((w*x*x for w,x in zip(weights,v)),F(0))
            for K in range(4):
                lo=sum((weights[j]*v[j]**2 for j in range(K)),F(0))
                hi=sum((weights[j]*v[j]**2 for j in range(K,3)),F(0))
                check('orthogonal_projection_Pythagoras',total==lo+hi)
                check('projection_tail_contraction',hi<=total)
        trajectories=[(F(1),F(0),F(0)),(F(0),F(2),F(0)),(F(0),F(0),F(3))]
        maxnorm=max(sum((weights[j]*v[j]**2 for j in range(3)),F(0)) for v in trajectories)
        summax=sum((weights[j]*max(v[j]**2 for v in trajectories) for j in range(3)),F(0))
        check('supremum_sum_direction',maxnorm<=summax)
        reject('supremum_sum_equality_r'+str(r),maxnorm,summax)
    # Range inequalities and explicit dyadic shell power counting.
    for d in range(3,31):
        for numerator in range(1,8*(d-2)+1):
            s=F(numerator,8)
            if not (s<=d-2 and s<F(d,2)):continue
            alpha=F(d,2)-s/2;R=alpha+d+5;threshold=R+F(d,2)
            check('frozen_topology_threshold',threshold==2*d+5-s/2)
            for gap in [F(1,8),F(1),F(3)]:
                r=threshold+gap
                check('source_Hilbert_summability',d+2*R-2*r<0)
                check('linear_Hilbert_summability',d+2-2*r<0)
                check('actual_delta_continuity_range',2*r>d)
                check('source_scaled_decay',s/d-F(1,2)<0)
            check('source_threshold_equality_no_geometric_decay',d+2*R-2*threshold==0)
    for d in range(3,9):
        for K in [1,2,4,8,16]:
            shell=(4*K+1)**d-(2*K+1)**d
            check('dyadic_lattice_shell_upper_count',0<shell<=(5*K)**d)
    d0,R0=3,9; r0=F(21,2)
    reject('omit_mode_count_in_source_threshold',d0+2*R0-2*r0,2*R0-2*r0)
    # In a Hilbert space the unit vectors converge coordinatewise to zero,
    # yet have norm1 and pairwise squared distance2: no tightness conclusion.
    vectors=[[F(int(i==j)) for i in range(12)] for j in range(12)]
    for j,v in enumerate(vectors):
        check('escaping_mode_unit_norm',sum(x*x for x in v)==1)
        for k,u in enumerate(vectors):
            if k!=j:check('escaping_mode_pair_distance',sum((x-y)**2 for x,y in zip(v,u))==2)
        for K in range(j+1):check('fixed_projection_can_miss_entire_path',sum(v[:K])==0)
    escape=vectors[-1]; unseen_norm=sum(x*x for x in escape)
    visible_norm=sum(x*x for x in escape[:6])
    reject('coordinate_convergence_implies_Hilbert_tightness',unseen_norm,visible_norm)
    distance=sum((x-y)**2 for x,y in zip(vectors[-1],vectors[-2]))
    reject('fixed_radius_compact_neighborhood_is_compact',distance,F(0))
    result={'status':'PASS','assertions':sum(counts.values()),'categories':dict(sorted(counts.items())),
            'mutation_witnesses':mutations,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'seed':None,'tolerance':None,'limitations':'Exact finite normalization, convolution, projection and range checks. Escaping-mode sequences challenge invalid inference, not the admitted particle law. Singular source estimates, infinite series and weak path convergence require the analytic proof and fresh independent gates.'}
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','assertions':result['assertions'],'categories':len(counts),'mutation_families':len(mutations)}))

if __name__=='__main__':main()
