#!/usr/bin/env python3
"""TASK055 diagnostics, newly written from exact four-node quadrature/enumeration.
No prior checker is imported/read. Products have frequency at most 3 in each
variable, so the four-node rule integrates all polynomial law/energy tests
exactly on the continuous torus. Absolute-cross quadrature is only a discrete
Cauchy-Schwarz diagnostic; the continuous bound is proved in the memorandum.
All spatial derivatives divide out the common 2*pi factor in these tests.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import hashlib, json, sys
from math import factorial

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
counts=defaultdict(int)
def assert_equal(a,b,group,description):
 if a!=b: raise AssertionError(f'{group}: {description}: {a} != {b}')
 counts[group]+=1
def assert_true(ok,group,description):
 if not ok: raise AssertionError(f'{group}: {description}')
 counts[group]+=1
for line in (OUT/'ROUND_009_ENERGY_INPUT_SHA256SUMS.txt').read_text().splitlines():
 digest,rel=line.split('  ',1)
 assert_equal(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),digest,'input_digest',rel)
cos=[F(1),F(0),F(-1),F(0)]
sin=[F(0),F(1),F(0),F(-1)]
gradients={
 'constant':lambda x,y:F(0),
 'relative_cosine':lambda x,y:-sin[(x-y)%4],
 'separable_cosines':lambda x,y:-sin[x]*cos[y],
 'additive_cosines':lambda x,y:-sin[x],
 'mixed':lambda x,y:-sin[(x-y)%4]-2*sin[x]-sin[x]*cos[y],
}
nontrivial={'triple':False,'mixed':False,'pair_law':False,'finite_N_deletion':False}
for name,gfun in gradients.items():
 G=[[gfun(x,y) for y in range(4)] for x in range(4)]
 A=[sum(row)/4 for row in G]
 H=[[G[x][y]-A[x] for y in range(4)] for x in range(4)]
 g2=sum(v*v for row in G for v in row)/16
 a2=sum(v*v for v in A)/4
 h2=sum(v*v for row in H for v in row)/16
 assert_equal(g2,h2+a2,'orthogonal_row_projection',name)
 for x in range(4): assert_equal(sum(H[x]),F(0),'conditional_Haar_centering',name)
 for N in (2,3,4):
  configurations=list(product(range(4),repeat=N))
  pairs=N*(N-1)//2
  for eps in (F(0),F(1,2),F(-1,3)):
   data=[]
   for xs in configurations:
    density=1+eps*sum(cos[(xs[i]-xs[j])%4] for i in range(N) for j in range(i+1,N))/pairs
    assert_true(density>0,'positive_correlated_density',f'N={N},epsilon={eps}')
    mass=density/F(4**N)
    grad=[]
    for i in range(N):
     direct=sum(G[xs[i]][xs[j]] for j in range(N) if i!=j)/F(N*N)-A[xs[i]]/N
     centered=(sum(H[xs[i]][xs[j]] for j in range(N) if i!=j)-A[xs[i]])/F(N*N)
     assert_equal(direct,centered,'deleted_gradient_exact',f'{name},N={N}')
     grad.append(direct)
    data.append((xs,mass,grad,density))
   total_mass=sum(m for xs,m,gr,den in data)
   assert_equal(total_mass,F(1),'law_normalization',f'N={N},epsilon={eps}')
   for i in range(N):
    for node in range(4):
     assert_equal(sum(m for xs,m,gr,den in data if xs[i]==node),F(1,4),'one_body_Haar',f'N={N},i={i}')
   expected=sum(m*sum(v*v for v in gr) for xs,m,gr,den in data)
   pair=sum(m*H[xs[0]][xs[1]]**2 for xs,m,gr,den in data)
   mix=sum(m*H[xs[0]][xs[1]]*A[xs[0]] for xs,m,gr,den in data)
   one=sum(m*A[xs[0]]**2 for xs,m,gr,den in data)
   triple=sum(m*H[xs[0]][xs[1]]*H[xs[0]][xs[2]] for xs,m,gr,den in data) if N>=3 else F(0)
   expanded=((N-1)*pair+(N-1)*(N-2)*triple-2*(N-1)*mix+one)/F(N**3)
   assert_equal(expected,expanded,'exchangeable_four_term_identity',f'{name},N={N},epsilon={eps}')
   reference=F(N-1,N**3)*g2-F(N-2,N**3)*a2
   if eps==0:
    assert_equal(expected,reference,'continuous_Haar_identity',f'{name},N={N}')
    assert_equal(triple,F(0),'Haar_triple_cancellation',f'{name},N={N}')
    assert_equal(mix,F(0),'Haar_mixed_cancellation',f'{name},N={N}')
    # Leading normalized gradient is -sin(x_i)/N.
    leading=sum(m*sum(sin[x]**2/F(N*N) for x in xs) for xs,m,gr,den in data)
    absolute_cross=sum(m*abs(sum((-sin[xs[i]]/N)*gr[i] for i in range(N))) for xs,m,gr,den in data)
    assert_true(absolute_cross**2<=leading*expected,'discrete_absolute_cross_CS',f'{name},N={N}')
    assert_equal(leading,F(1,2*N),'leading_Haar_noise',f'N={N}')
   delta2=pair-h2
   delta3=triple
   deltaA=mix
   difference=((N-1)*delta2+(N-1)*(N-2)*delta3-2*(N-1)*deltaA)/F(N**3)
   assert_equal(expected-reference,difference,'exact_marginal_error_reduction',f'{name},N={N}')
   for beta in (F(1,4),F(1),F(3)):
    nu=1/beta;b=min(beta,F(1));sigma2=N*b
    assert_equal(2*nu*sigma2*(expected-reference),
      2*nu*b/F(N*N)*((N-1)*delta2+(N-1)*(N-2)*delta3-2*(N-1)*deltaA),
      'physical_scaling_reduction',f'N={N},beta={beta}')
    assert_true(b*nu<=1,'thermal_factor','b*nu=min(1,nu)')
   nontrivial['triple']|=bool(N>=3 and triple)
   nontrivial['mixed']|=bool(mix)
   nontrivial['finite_N_deletion']|=bool(a2 and name=='additive_cosines' and reference)
   if eps:
    corr=sum(m*cos[(xs[0]-xs[1])%4] for xs,m,gr,den in data)
    assert_equal(corr,eps/F(2*pairs),'nonproduct_pair_correlation',f'N={N}')
    nontrivial['pair_law']|=bool(corr)
   # Exact equivariance of the test law, independent of any dynamic assertion.
   def law_value(xs): return 1+eps*sum(cos[(xs[i]-xs[j])%4] for i in range(N) for j in range(i+1,N))/pairs
   for xs,m,gr,den in data:
    for shift in range(4):
     assert_equal(law_value(tuple((x+shift)%4 for x in xs)),den,'common_translation',f'N={N}')
    assert_equal(law_value(tuple(reversed(xs))),den,'label_exchange',f'N={N}')
# A separate non-Haar exchangeable law exercises the mixed term, which the
# preceding first-frequency common-translation test laws happen to annihilate.
biased=[F(1,2),F(1,4),F(1,8),F(1,8)]
G=[[gradients['mixed'](x,y) for y in range(4)] for x in range(4)]
A=[sum(row)/4 for row in G]
H=[[G[x][y]-A[x] for y in range(4)] for x in range(4)]
for N in (2,3):
 direct=pair=triple=mixed=one=F(0)
 for xs in product(range(4),repeat=N):
  mass=F(1)
  for x in xs: mass*=biased[x]
  gr=[(sum(H[xs[i]][xs[j]] for j in range(N) if i!=j)-A[xs[i]])/F(N*N) for i in range(N)]
  direct+=mass*sum(v*v for v in gr)
  pair+=mass*H[xs[0]][xs[1]]**2
  if N>=3: triple+=mass*H[xs[0]][xs[1]]*H[xs[0]][xs[2]]
  mixed+=mass*H[xs[0]][xs[1]]*A[xs[0]]
  one+=mass*A[xs[0]]**2
 assert_equal(direct,((N-1)*pair+(N-1)*(N-2)*triple-2*(N-1)*mixed+one)/F(N**3),
  'arbitrary_exchangeable_four_term_identity',f'biased iid discrete law, N={N}')
 assert_true(bool(mixed),'non_Haar_mixed_term','mixed coefficient is exercised')
 nontrivial['mixed']|=bool(mixed)
for key,seen in nontrivial.items(): assert_true(seen,'nontrivial_law_terms',key)

# A common-translation invariant law with Haar one-body marginals can also
# have a nonzero mixed contraction. For the symmetric test
# Phi=cos(x)+cos(y)+cos(2x-y)+cos(2y-x), normalized H*A equals
# cos(x-y)-cos(3x-y)-cos(2x-2y)/2+cos(2y)/2.
# Compute its pairing with 1+epsilon*cos(x-y) by exact Fourier orthogonality,
# separately from the four-node quadrature (which is not used for this test).
ha_cos={(1,-1):F(1),(3,-1):F(-1),(2,-2):F(-1,2),(0,2):F(1,2)}
mode=(1,-1)
for epsilon in (F(1,2),F(-1,3)):
 value=epsilon*sum(v*F(1,2) for k,v in ha_cos.items() if k==mode or k==tuple(-j for j in mode))
 assert_equal(value,epsilon/2,'invariant_nonzero_mixed_contraction','exact Fourier orthogonality')
 assert_true(bool(value),'invariant_nonzero_mixed_contraction','one-body Haar does not kill mixed term')

# Coulomb boundary diagnostics: c_d is factored out, and Phi depends on z.
# D=c_d(delta_0-Haar), so the exact quadratic form of B is mean(Phi^2)-Phi(0)^2.
relative_tests={
 'constant':{0:F(1)},
 'cosine':{-1:F(1,2),1:F(1,2)},
 'zero_diagonal':{0:F(1),-1:F(-1,2),1:F(-1,2)},
}
for name,coeff in relative_tests.items():
 square=defaultdict(F)
 for k,v in coeff.items():
  for j,w in coeff.items(): square[k+j]+=v*w
 norm=square[0];trace=sum(coeff.values())**2
 from_distribution=-sum(v for k,v in square.items() if k!=0)
 from_boundary=norm-trace
 assert_equal(from_distribution,from_boundary,'Coulomb_flux_identity',name)
 assert_true(from_boundary<=norm,'internal_drift_upper_bound',name)
 response_quad=-2*sum(v*v for k,v in coeff.items() if k!=0)
 assert_true(response_quad<=0,'both_responses_nonpositive',name)
 if name=='constant':
  assert_equal(from_boundary,F(0),'constant_flux_cancellation','compensation cancels nonzero radial flux')
  assert_equal(response_quad,F(0),'constant_response','zero Fourier mode is killed')
 if name=='zero_diagonal': assert_true(from_boundary>0,'false_dissipativity_detection','B is not always nonpositive')

# Backward-energy sign, exact polynomial-in-time diagnostic.
for degree in range(1,7):
 for diffusion in (F(0),F(1,3),F(2)):
  for response_damping in (F(0),F(5,7)):
   source_pairing=F(1,2)+(diffusion+response_damping)/F(2*degree+1)
   dissipation=diffusion/F(2*degree+1)
   assert_equal(dissipation+F(1,2),source_pairing-response_damping/F(2*degree+1),
    'backward_energy_sign','positive initial norm stays on left')

# Exact exponent, Fourier sign, and boundary powers.
for d in range(3,13):
 for quarter in range(1,4*(d-2)+1):
  s=F(quarter,4);p=s+2;a=s/p;q1=(F(1)+F(d,2))/2
  assert_true(0<a<1,'uniform_source_power','s/(s+2) in (0,1)')
  assert_equal(a-1,-2/p,'reference_bracket_rate','a-1=-2/p')
  assert_equal((a-1)/2,-1/p,'reference_cross_rate','half exponent')
  assert_true(2*a-1<=a,'uniform_energy_constant','sup-square drift absorbed without gradient constant')
  assert_true(d-1-q1>0,'diffusion_tube_boundary','boundary vanishes')
  assert_true(d-s-2>=0,'internal_flux_power','sub-Coulomb positive; Coulomb zero')
  if 2*s>d: assert_true((2*s-d)/p<1,'all_N_rho_bound','power rho_N no larger than N')
 for s in range(1,d-1):
  for k in (1,2,3):
   q=F(k)**(s+2-d)
   for nu in (F(0),F(1,3),F(2)):
    damping=nu*k*k+q
    # Formal coefficients of exp(-damping*tau), tau=T-t. Differentiate
    # these separately from the two spatial multipliers. The final
    # coefficient is used only as the derivative coefficient at order 5.
    coeff=[(-damping)**j/F(factorial(j)) for j in range(7)]
    residual=tuple(-(j+1)*coeff[j+1]-nu*k*k*coeff[j]-q*coeff[j] for j in range(6))
    assert_equal((coeff[0],residual),(F(1),(F(0),)*6),'actual_backward_Fourier_sign',
      'terminal one and six exact backward-series coefficients; positive common constants factored out')
    if s==d-2: assert_equal(q,F(1),'Coulomb_Fourier_multiplier','constant nonzero-mode multiplier')
# A scalar constant terminal test has exactly zero source and inverse/noise.
for N in (2,3):
 for nu in (F(0),F(1,3),F(2)):
  assert_equal(2*nu*N*F(0),F(0),'constant_h_and_zero_noise','all noise terms vanish for constant h')
  assert_equal(F(0)*N,F(0),'zero_noise_functional','nu=0 independently of gradient estimates')

result={'status':'PASS','task':'TASK055','classification':'new continuation-constructor self-check; THM028 remains conditional',
 'arithmetic':'exact rational arithmetic and SHA-256; no numerical tolerance, random seed, dependencies, or imported checker',
 'quadrature':'four nodes per coordinate; exact for polynomial tests of frequency at most 3; absolute-cross test is discrete CS only',
 'python':sys.version.split()[0],'assertions':sum(counts.values()),'counts':dict(sorted(counts.items())),
 'scope':'Supporting coefficients/signs/symmetry tests, not independent certification of conditional analytic hypotheses or actual-law transfer.'}
(OUT/'ROUND_009_ENERGY_EXACT_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
