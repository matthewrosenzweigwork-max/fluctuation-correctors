# THM-028 — homogeneous genuine corrector in the finite-particle Ito domain

2026-09-18 UTC. OPEN / UNAUDITED at statement freeze. This is the next bounded PO023 assertion, not a fluctuation theorem. No unproved THM027 operator lemmas are imported under that card's name.

Fix d>=3,0<s<=d-2,N>=2,finite T and0<=nu<=nu_*<infinity, unit Haar torus and frozen Riesz K=-gradg. Set external b=0,reference mu_t=1,u_t=0, and choose real smooth terminal h. Let f be the exact homogeneous Fourier backward solution from THM025. Let Phi be its unique terminal-zero bounded Borel full pair inverse, with source J=K(x-y).(gradf(x)-gradf(y)) and both compensated responses. These modules are already independently audited. THM026 supplies the actual singular N-particle realization for b=0.

The assertion is that Phi is C1 in time (one-sided at endpoints) and C2 in pair space off the diagonal, with jointly continuous indicated derivatives there. For every1<q1<d/2 and q1+1<q2<d, fixed smooth positive weights w_a equal to r^-a near the diagonal give finite uniform-in-time bounds

    ||Phi||infty + sup |gradPhi|/w_q1 + sup |D2Phi|/w_q2
                   + sup |partial_t Phi|/w_s <= C,

where C may depend on N,nu_*,T,d,s,q1,q2,h and the fixed cutoffs, but is uniform in nu in that interval. The equation partial_t Phi+nu(Delta_x+Delta_y)Phi+(B/N)Phi+(R_x+R_y)Phi=-J holds classically off diagonal. Its derivatives extend as weak derivatives with Phi in global Haar H1 and W^{2,1}; partial_t Phi and B Phi are globally Haar L1 uniformly in time. The B Phi assertion must use proved structure, not the generally nonintegrable crude product K times gradPhi.

Define eta=N^-1 sum_i delta_Xi,rho=eta-dx, and P_t[Phi] by ordered distinct-label sums with denominator N^2 and factor1/2, subtracting eta tensor Haar and adding half Haar squared. Under any independent initial N-body probability density F0 with finite supremum, the actual singular particle paths obey

    dP_t[Phi_t] = { -P_t[J_t]+U3_t[C Phi_t]
       +(1/N)rho_t[(B Phi_t)_mu]+(1/(2N))int B Phi_t dxdy }dt + dM2_t,

with C Phi=Sym3[K(x-z).grad_xPhi(x,y)], Sym3 the average over all six permutations, (B Phi)_mu(x)=int B Phi(x,y)dy, and the exact deleted-label U3 of ROUND_001_ALGEBRA.md(1.4). The stochastic integral is M2=sqrt(2nu)sum_i int grad_i P_t[Phi_t](X_t).dW_i, a square-integrable true martingale with its usual2nu sum|grad_iP|^2 bracket. Every displayed drift term has finite absolute expectation integrated over[0,T], with constants allowed to depend on N and ||F0||infty. All mixed empirical/background integrals, partial diagonals, and passage from compact collision stops must be justified. Values on true coinciding coordinates do not create diagonal traces under the stated density law.

Exact negation: an admissible tuple/test/exponent/initial bounded density violates any stated regularity, weak derivative, classical equation, integrability, exact coefficient or true-martingale passage. No uniform-in-N residual or bracket smallness, centering limit, CLT, actual inhomogeneous theorem, beta->0 uniformity or critical hierarchy is claimed. If only a conditional assertion can be proved, identify precisely the missing lemma rather than treating it as established.
