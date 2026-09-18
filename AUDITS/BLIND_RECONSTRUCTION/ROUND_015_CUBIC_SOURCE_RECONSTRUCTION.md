# Round 015 — isolated reconstruction of the critical cubic and uniform source

TASK-077. Issued 2026-09-18 UTC. **FULL CONDITIONAL CONJUNCTION RECONSTRUCTED.** This report independently proves both frozen assertions from the exact supplied earlier conditional modules. It does not certify those earlier modules, assign a campaign audit pass, or prove a fluctuation law. No current constructor proof or current audit was exposed before this report was sealed. The independent falsification attempts below produce no counterexample to either frozen assertion.

The decisive new estimate is an actual-law absolute quadratic-source bound at the microscopic energy scale. Its proof retains the positive low-heat-time remainder and controls the remaining Fourier commutator with a less strongly truncated positive quadratic energy. A frequency-dependent cutoff gives a polynomial bound in each terminal-test frequency; summing that bound handles every fixed smooth test. The cubic conclusion then uses the exact integrated identity, its initial endpoint, both lower contractions, and the supplied genuine-martingale estimate. In particular, the cubic conclusion concerns the absolute value after time integration. No bound on the absolute instantaneous cubic statistic is claimed.

## 1. Frozen conjunction, negation, isolation, and premises

Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r015-cubic-blind. Branch: codex/hocf-r015-cubic-blind. Assigned base: 072cab684b9ce41855ead6c48f435c8fc184ec35. All 28 allowed inputs were individually SHA-256 checked at the source, copied, and checked again before reconstruction. The accompanying input manifest fixes their bytes. The task and its transport manifest were the first files read. Inherited non-allowlisted files were ignored. No state, history, memory file, current R15 construction, R13/R14 result, other current audit, prior checker, external source, or root scratch was opened. The source dossier contains historical self-check/audit descriptions; none is used as a premise of mathematical certification. Complete prior constructions are treated conditionally as issued.

Ambient exposure: the automatically supplied global/user instructions included a high-level memory summary concerning the campaign, unrelated research projects, and user preferences. No mathematical claim is imported from it. The assignment stated that this route may close a strong critical drift assertion, but supplied no mechanism. The worktree command automatically printed the base commit's short subject; that is disclosed in EXPOSURE.md and supplies no premise. The task's exact allowlist and prohibition on canonical edits supersede the general instruction to read README_FIRST, the specification, all state ledgers, and MODEL_ORCHESTRATION. The parent explicitly authorized the isolated branch/worktree. No commit, push, installation, child, or canonical edit occurs in this lane.

Fix an integer d at least 4, 0<s<2, T finite and nonnegative, a real smooth terminal test h on the unit-Haar torus, the frozen positive Fourier Riesz kernel g, K=-grad g, and zero external drift. Actual particles start from iid Haar independently of their independent Brownian drivers. Their noise is sqrt(2 nu). The pair inverse is the genuine symmetric bounded-Borel, terminal-zero inverse supplied by the earlier modules, with source

\[
 J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y))
\]

and both coefficient-one responses. The representatives and particle domain are precisely R8's. No diagonal value is assigned to J, Phi, their derivatives, or the singular cubic.

For THM-037, fix a finite nu_* and let N>=2 and 0<=nu<=nu_*. The claim is a common constant depending only on d,s,T,nu_*,h and the frozen kernel such that

\[
 \sup_{0\le t\le T}\mathbb E|P_N[J_t](X_t)|
 \le C N^{s/d-1}.                                            \tag{1.1}
\]

The exact negation is admitted fixed data and choices of N, nu, and deterministic t for which no common constant works; equivalently the supremum of N^{1-s/d} times the displayed expectation is infinite. This is an absolute-statistic assertion under the actual law, including zero noise.

For THM-036, let lambda_N=beta_N N^{s/d-1} converge to a finite positive lambda, nu_N=1/beta_N, b_N=min(beta_N,1), and sigma_N=sqrt(N b_N). Define C Phi=Sym_3[K(x-z) dot grad_x Phi(x,y)], with the average over all six permutations, and the literal ordered deleted-label U3 including every Haar contraction. The claim is

\[
 \sigma_N\mathbb E\left|\int_0^T U_3[C\Phi_t](X_t)\,dt\right|
 \longrightarrow0.                                          \tag{1.2}
\]

Its exact negation is a fixed admitted tuple and positive finite critical sequence with positive limsup of (1.2). A nonvanishing upper bound, a generic exchangeable law, or an initial derivative is not this negation. The conjunction fails exactly if either of these negations occurs.

The exact source preflight is as follows. Source locations refer only to the frozen, allowed files.

| Complete supplied source | Premise used and scope retained |
|---|---|
| R1 frozen model and ROUND_001_ALGEBRA, Sections 1–5 | Unit Haar, Fourier characters exp(2 pi i k.x), K=-grad g, coefficient 1/N, ordered distinct labels with N^k denominator, P=U2/2, both response slots. Section 6 below reconstructs the needed coefficients without singular diagonal formulas. |
| ROUND_004_SINGULAR_RESPONSE, Sections 2–4; THM021 | Exact positive heat representation and coefficient-one local singularity; K in L1; D=div K=s(d-2-s)g_(s+2) in this strict range, including the complete periodic compensation and lower bound D>=-kappa. |
| ROUND_005_PERIODIC_PAIR_POTENTIAL, Sections 4–9; THM023 | Singular auxiliary pair process, bounded absolute source potential at each fixed N, Haar L2 propagation, and its actual bounded-Borel source potential. This is not an N-particle estimate. |
| Complete R5 conditional composition and full interface, THM024/025, both supplied R5 addenda | The genuine full inverse, bounded-response series with both slots, uniform Haar L2 bound because 2s<d, and actual Fourier test. The common divergence constant is enlarged as prescribed by the source addendum. Pair symmetry means coordinate-exchange equivariance, not self-adjointness. |
| ROUND_006_SINGULAR_PARTICLE_REALIZATION, Sections 3–8; THM026 | Actual noncolliding particle paths, same-noise heat passage at fixed N, finite-N density domination, and exact total-force energy identity. Its exponential density bound is used only for fixed-N integrability, never as a uniform law estimate. |
| ROUND_007_WEIGHTED_PAIR_GRADIENT, Sections 2–8; THM027 | Fixed-N legitimate expectation derivatives, fixed weights, and the two-response weighted convolution estimates entering the later R12 bound. No untracked fixed-N constant is made uniform. |
| ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN, Sections 5–11; THM028 | Genuine local/weak derivatives, classical off-diagonal equation, all background contractions, finite-N singular Itô identity, and true square-integrable corrector martingale. This entire provisional domain statement remains a conditional premise. |
| ROUND_010_ACTUAL_LAW_FALSIFICATION, Sections 2–4; THM031 | Actual expected energy at most zero including zero noise, heat-integral floor, and exact energy passage. The energy and truncation steps needed here are repeated in Sections 2–3. Its conditional R9 result and its singular-tail conclusion are not imported. |
| ROUND_012_SUBCOULOMB_ACTUAL_NOISE, Sections 2–7; THM033 | Explicit N-dependent weighted gradient bound and genuine actual bracket estimate at bounded rescaled diffusivity. Section 7 below checks their precise ranges and recomputes the consequences used here. Its earlier prerequisites remain conditional. |
| THM032 and ROUND_011_BOUNDED_RESCALED_DIFFUSION_GRADIENT | Allowed alternative source, not used in this proof. No unsupplied consequence of its limit or its gradients is assumed. |

No external-source theorem, citation, novelty assessment, full CLT, critical total-variation convergence, or hidden product marginal enters. The earlier conditional sources are complete inputs rather than selected favorable lines from current audit outcomes.

## 2. Actual energy and the exact positive heat decomposition

Set

\[
 \alpha=(d-s)/2>1,\quad A=\frac{4^\alpha\pi^{d/2}}{\Gamma(s/2)},
 \quad p_u(z)=\sum_{m\in\mathbb Z^d}(4\pi u)^{-d/2}
              e^{-|z+m|^2/(4u)}.
\]

Then the supplied kernel normalization is

\[
 g(z)=A\int_0^\infty u^{\alpha-1}(p_u(z)-1)\,du,
 \qquad \widehat g(k)=c_{d,s}|k|^{-2\alpha},\quad k\ne0,       \tag{2.1}
\]

where c_(d,s)=pi^(s-d/2) Gamma((d-s)/2)/Gamma(s/2). Taking a Fourier coefficient gives A Gamma(alpha)/(4 pi^2)^alpha=c_(d,s). Unfolding the Euclidean Gaussian and substituting v=|z|^2/(4u) gives local singularity exactly |z|^-s. These checks fix both the 4 pi^2 and the coefficient one. The torus compensation is the -1 inside the integral; it is not dropped.

Let

\[
 H_N=\frac1N\sum_{i<j}g(X_i-X_j),\qquad
 D_2[v]=N^{-2}\sum_{i\ne j}v(X_i,X_j),\qquad
 E_t H_N\le0.                                                \tag{2.2}
\]

The last inequality is an actual-law input whose passage is worth making explicit. At a fixed interaction heat smoothing epsilon and positive nu, the smooth density F satisfies

\[
 \frac d{dt}\left(\nu\int F\log F+\int H_N^\epsilon F\right)
 =-\int F|\nabla H_N^\epsilon+\nu\nabla\log F|^2\le0.
\]

The initial energy and entropy are zero under iid Haar. The entropy is nonnegative, so E H_N^epsilon<=0. The supplied R6 heat passage gives almost sure path convergence for fixed N and nu, and the limiting path stays a positive distance from every collision on the finite horizon. Therefore H_N^epsilon(X_t^epsilon) converges to H_N(X_t). Since g_epsilon>=g_*:=inf g> -infinity, Fatou after the common shift (N-1)g_*/2 yields (2.2). At nu=0 the exact deterministic energy decrease yields it directly after integrating the iid initial energy zero. No division by nu is made. This proves the same signed bound for every chosen nu and deterministic t with no noise-dependent constant. Finite-N integrability is supplied by R6; alternatively the shifted nonnegative energy and this bound prove it.

For 0<r<=1 introduce different, auxiliary cutoffs of the heat integral:

\[
 g_r(z)=A\int_r^\infty u^{\alpha-1}(p_u(z)-1)\,du,
 \quad H_r(z)=A\int_0^r u^{\alpha-1}p_u(z)\,du,
 \quad c_r=Ar^\alpha/\alpha.                                  \tag{2.3}
\]

The exact off-diagonal equality is g=g_r+H_r-c_r. Here H_r is nonnegative and Haar-integrable; g_r is smooth, mean zero, and has positive Fourier coefficients

\[
 a_r(k)=A\int_r^\infty u^{\alpha-1}e^{-4\pi^2|k|^2u}\,du,
 \quad k\ne0.                                                \tag{2.4}
\]

Let eta=N^-1 sum delta_Xi and eta_hat(k)=N^-1 sum exp(-2 pi i k.Xi). Define

\[
 \mathcal E_r(\eta)=\sum_{k\ne0}a_r(k)|\widehat\eta(k)|^2\ge0.
\]

The smooth self subtraction is exactly

\[
 D_2[g_r]=\mathcal E_r(\eta)-\frac{g_r(0)}N.                    \tag{2.5}
\]

In particular it has neither denominator N(N-1) nor a lost factor one half. Since D2[g]=2H_N/N, the identity (2.3) gives

\[
 \mathcal E_r+D_2[H_r]
 =D_2[g]+\frac{g_r(0)}N+\frac{N-1}{N}c_r.                     \tag{2.6}
\]

Both left terms are nonnegative. The Gaussian estimate at zero and the exponentially decaying large-time heat kernel give 0<=g_r(0)<=C r^-s/2. Taking actual-law expectations, using (2.2), and retaining both nonnegative terms proves the central bound

\[
 \mathbb E\mathcal E_r+\mathbb E D_2[H_r]
 \le C\big(N^{-1}r^{-s/2}+r^\alpha\big)=:C\varepsilon_N(r),   \tag{2.7}
\]

uniformly in deterministic t and chosen nu. Every expectation is legitimate: H_r=g-g_r+c_r, g has a finite actual first absolute moment, and g_r is bounded for fixed r. Formula (2.7) does not assume pointwise nonnegativity of a weighted Riesz kernel.

Choosing r=N^-2/d makes both terms equal N^{s/d-1}. A later modewise choice changes only a polynomial frequency factor. The truncation in (2.3) is used only to estimate observables; it does not change the actual particle evolution or full pair inverse.

## 3. The singular source tail, with every background term

For any C2 scalar v, let J[v]=K(x-y) dot (grad v(x)-grad v(y)), and define the smooth J_r[v] with K replaced by -grad g_r. Work first with one complex Fourier character v=e_n, n nonzero; real and imaginary parts give the same estimates. Set L_n=1+|n|. Its Hessian norm is at most (2 pi)^2 |n|^2, so

\[
 |\nabla e_n(x)-\nabla e_n(y)|
 \le (2\pi)^2 |n|^2\operatorname{dist}(x-y,0).
\]

Write delta(z)=dist(z,0). For the periodized Gaussian,

\[
 \delta(z)|\nabla p_u(z)|
 \le \sum_m\frac{|z+m|^2}{2u}(4\pi u)^{-d/2}
                      e^{-|z+m|^2/(4u)}
 \le C_d p_{2u}(z).                                          \tag{3.1}
\]

The first inequality uses delta(z)<=|z+m| for every lattice translate; the second is the boundedness of a e^-a/8 on a>=0 with the Gaussian normalization restored. It is valid over the entire torus, not only a local chart. Differentiation of the truncated heat integral is locally uniform off zero. Integration of (3.1), with the change v=2u, gives

\[
 |J[e_n](x,y)-J_r[e_n](x,y)|
 \le C L_n^2 H_{2r}(x-y).                                    \tag{3.2}
\]

Take r<=1/2. The exact statistic is

\[
 P_N[V]=\tfrac12D_2[V]-\int V(x,y)\eta(dx)dy
                      +\tfrac12\int V(x,y)dxdy.              \tag{3.3}
\]

Both row integrals of the positive majorant H_(2r)(x-y) are c_(2r). Consequently (2.7) and (3.2), retaining the three terms of (3.3), show

\[
 \mathbb E|P_N[J[e_n]-J_r[e_n]]|
 \le C L_n^2\varepsilon_N(r).                                \tag{3.4}
\]

This uses E D2 H_(2r) for the ordered actual pairs, and c_(2r) for the empirical-background and scalar-background terms. There is no singular diagonal evaluation. It also proves absolute integrability of this tail under the genuine evolving law, including zero noise.

## 4. A uniform Fourier estimate for the smooth part

All constants in this section depend only on d,s and the frozen kernel. Put b=4 pi^2. For a nonzero real vector v, define a_r(v) by the same radial integral as (2.4), and F_r(v)=v a_r(v). Differentiating this integral and then substituting w=|v|^2 u yields

\[
 \|DF_r(v)\|
 \le C |v|^{-2\alpha}e^{-(b/2)r|v|^2}.                        \tag{4.1}
\]

Indeed the relevant integrals are bounded by a constant times the integral from r|v|^2 to infinity of (w^(alpha-1)+w^alpha)e^-bw; extracting e^[-(b/2)r|v|^2] leaves a finite integral. No lower bound on r or v is used except v nonzero. Also, because alpha>1, integrating over w between r|v|^2+1 and r|v|^2+2 proves

\[
 a_r(v)\ge c |v|^{-2\alpha}e^{-br|v|^2},
 \qquad a_r(v)\le C |v|^{-2\alpha}.                           \tag{4.2}
\]

The lower constant includes A e^-2b and is positive and independent of r. These deliberately nonoptimal constants are sufficient.

For n=k+l nonzero and k,l nonzero integer vectors, suppose r|n|^2<=1. Then

\[
 |n\cdot(k a_r(k)+l a_r(l))|
 \le C L_n^{2\alpha+2}
       \sqrt{a_{r/32}(k)a_{r/32}(l)}.                         \tag{4.3}
\]

Here is the full split proving this uniform coefficient estimate. If |k|>=2|n|, then l=-(k-n), all points of the segment from k-n to k have norms between |k|/2 and 3|k|/2, and F_r is odd. The mean-value integral and (4.1) give an upper bound C |n|^2 |k|^-2alpha e^[-br|k|^2/8]. The square root on the right of (4.3), by (4.2), is at least c |k|^-2alpha e^[-13br|k|^2/256]. Since 13/256<1/8, the former exponential is smaller. Thus this case has even L_n^2 in place of L_n^(2alpha+2).

If |k|<2|n|, then |l|<3|n|. Both are nonzero integer vectors and have norm at least one. The upper estimate in (4.2) bounds the left side by C |n|, because 1-2alpha<0. The right square root is at least c L_n^-2alpha: the polynomial factors have this lower bound, and the exponential is bounded below since r|n|^2<=1. Its required coefficient is thus at most C L_n^(2alpha+1), which is also covered by (4.3). These two cases exhaust the indices. Large terminal-test frequencies have a polynomial cost, not an untracked exponential.

The exact Fourier coefficient of J_r[e_n] at the pair mode (k,l) with k+l=n is

\[
 -4\pi^2\big((n\cdot k)a_r(k)+(n\cdot l)a_r(l)\big),           \tag{4.4}
\]

taking a_r(0)=0 when necessary. It follows directly by multiplying -2 pi i m a_r(m) with 2 pi i n in the two gradient slots. The cancellation between k and l in (4.4) is essential; estimating the two summands separately would lose a frequency power and not prove (4.3).

For this smooth source J_r[e_n](x,x)=0 because the gradient difference is zero. This is a property of the smooth auxiliary source alone. Hence, with rho=eta-dx,

\[
 P_N[J_r[e_n]]=\tfrac12\iint J_r[e_n](x,y)\rho(dx)\rho(dy).    \tag{4.5}
\]

The zero modes in either slot vanish against rho. Its Fourier series is absolutely convergent for fixed r,n, so (4.3) gives, pointwise for every configuration,

\[
 |P_N[J_r[e_n]]|
 \le C L_n^{2\alpha+2}
 \sum_{k+l=n\atop k,l\ne0}\sqrt{a_{r/32}(k)a_{r/32}(l)}
                          |\widehat\eta(k)\widehat\eta(l)|
 \le C L_n^{2\alpha+2}\mathcal E_{r/32}(\eta).                 \tag{4.6}
\]

The last step is Cauchy-Schwarz for the two sequences indexed by k. The mapping k to n-k is a bijection of the admitted index set; each squared sum is bounded by the full nonnegative energy. This is a pointwise estimate, so it assumes no independence between empirical modes or labels. Taking actual expectations and (2.7) gives

\[
 \mathbb E|P_N[J_r[e_n]]|
 \le C L_n^{2\alpha+2}\varepsilon_N(r).                       \tag{4.7}
\]

Replacing r by r/32 changes the two terms of epsilon_N by fixed factors 32^(s/2) and 32^-alpha only.

## 5. Every fixed smooth test and the full THM-037 conclusion

For each N and nonzero n choose only within its estimating argument

\[
 r_{N,n}=N^{-2/d}L_n^{-2}.                                    \tag{5.1}
\]

Then r<=1/4, r|n|^2<=1, and the exact powers are

\[
 N^{-1}r_{N,n}^{-s/2}=N^{s/d-1}L_n^s,
 \qquad r_{N,n}^{\alpha}=N^{s/d-1}L_n^{-2\alpha}.              \tag{5.2}
\]

Combining (3.4), (4.7), and 2alpha+s=d proves

\[
 \mathbb E|P_N[J[e_n]]|
 \le C L_n^{d+2}N^{s/d-1}.                                   \tag{5.3}
\]

The uniform constant is independent of n,N,t,nu. Its dependence on n has been explicitly isolated in the displayed polynomial, so a bound for a finite Fourier polynomial is not being substituted for the arbitrary smooth-test statement.

For the actual backward test,

\[
 f_t^\nu=\widehat h(0)+\sum_{n\ne0}\widehat h(n)
 e^{-(T-t)(4\pi^2\nu|n|^2+4\pi^2c_{d,s}|n|^{s+2-d})}e_n.
                                                                    \tag{5.4}
\]

Every exponential in modulus is at most one uniformly over 0<=t<=T and nu>=0. Define the finite seminorm

\[
 S_{d+2}(h)=\sum_{n\ne0}|\widehat h(n)|(1+|n|)^{d+2}<\infty.    \tag{5.5}
\]

Its finiteness follows by applying sufficiently many integer powers of 1-Delta to h and integrating Fourier coefficients; for example an integer m>d+1 gives decay (1+|n|^2)^-m whose product with this weight is summable. Smoothness supplies any such m.

For a finite Fourier sum, linearity and (5.3) prove (1.1) with constant C S_(d+2)(h). To justify the infinite sum under the actual law rather than formally, note first that the Fourier sums of f converge in C2 uniformly over the admitted t,nu. The local kernel bound implies

\[
 |J[v](x,y)|\le C\|v\|_{C^2}w_s(x-y).
\]

The actual w_s pair moment is finite and uniformly bounded: the coefficient-one local expansion gives w_s<=C(g-g_*+1), and exchangeability with (2.2) gives E g(X1-X2)<=0. Row and scalar Haar moments are finite as well. Thus P_N[J[f^{(M)}]] converges in actual L1 to the genuine P_N[J[f]], uniformly in t and nu for each fixed N (in fact this elementary convergence bound is uniform in N). The summable right side of (5.3) also proves convergence in L1 with its stated N-rate. The two limits agree by the previous genuine-kernel convergence. Passing to the limit establishes exactly (1.1).

All time integrands are jointly measurable by the supplied deterministic regularity and particle measurability. Tonelli now gives, for positive noise with b=min(1/nu,1) and for zero noise with b=1,

\[
 \sqrt{Nb}\,\mathbb E\int_0^T|P_N[J_t]|dt
 \le C\sqrt b\,N^{s/d-1/2}\longrightarrow0                    \tag{5.6}
\]

uniformly over the bounded noise interval, since b<=1 and s<2<=d/2, strictly s/d<1/2. T=0 is included with zero time integral; (1.1) itself at t=0 follows from the same proof. Constants h give J=0. This completes THM-037, including its absolute expectation, singular integrability, N/nu/t uniformity, and stated consequence.

## 6. Exact cubic identity, without singular self evaluation

For the genuine inverse put

\[
 p(x,y)=\nabla_x\Phi(x,y),\quad
 q(x)=\int\Phi(x,y)dy,\quad a(x)=\int p(x,y)dy,
 \quad B\Phi=K(x-y)\cdot(\nabla_x-\nabla_y)\Phi.
\]

R8 supplies the local/weak derivatives and differentiated backgrounds. Define

\[
 A_a(x,y)=K(x-y)\cdot(a(x)-a(y)),\quad
 v(x)=\int K(z-x)\cdot a(z)dz,\quad R=R_x+R_y.
\]

Integrating the six actual permutations gives, with all integrals absolutely justified by R8,

\[
 (C\Phi)_1(x,y)=\tfrac16(A_a+R\Phi)(x,y),\quad
 (C\Phi)_2(x)=\tfrac13v(x),\quad (C\Phi)_0=0,                 \tag{6.1}
\]

and (R Phi)_mu=v, integral R Phi=0. In (6.1) the terms whose integrated variable appears only in K vanish by int K=0; those in its integrated gradient give the respective first and second responses; the remaining two give A_a. This explains each contribution and the factor six. The literal statistic is

\[
 U_3[C\Phi]=N^{-3}\!\sum_{i,j,k\ {\rm distinct}}C\Phi_{ijk}
 -3N^{-2}\!\sum_{i\ne j}(C\Phi)_1(X_i,X_j)
 +3N^{-1}\!\sum_i(C\Phi)_2(X_i)-(C\Phi)_0.                    \tag{6.2}
\]

The first sum is empty for N=2, while its background contractions generally survive. All triples are ordered.

Differentiate the literal P statistic on a collision-excluded compact set. The actual force contribution, before any estimate, is

\[
 Q=N^{-3}\sum_{i\ne j}\sum_{k\ne i}K(X_i-X_k)\cdot p(X_i,X_j)
       -N^{-2}\sum_{i\ne k}K(X_i-X_k)\cdot a(X_i).             \tag{6.3}
\]

Separate k=j from the first sum. Symmetrizing its two orientations gives (2N)^-1 D2[B Phi]. The all-distinct part is the ordered sum of C Phi. Oddness converts the last sum into -D2[A_a]/2. Substitution of (6.1) into (6.2) consequently gives exactly

\[
 Q=U_3[C\Phi]+P_N[R\Phi]+\frac1{2N}D_2[B\Phi].               \tag{6.4}
\]

Independent diffusion and the time derivative contribute P_N[(partial_t+nu Delta_pair)Phi]. No mixed-particle Brownian contraction appears because the two labels in the pair sum are distinct. The integrated Haar diffusion terms vanish by the weak/slice derivative conclusion of R8. Thus no singular full-product diagonal or separate trace is assigned. Both responses in (6.4) have coefficient one.

Since D2[B Phi]=2P_N[B Phi]+2rho[(B Phi)_mu]+integral B Phi, insertion of the genuine full equation

\[
 \partial_t\Phi+\nu\Delta_{pair}\Phi+N^{-1}B\Phi+R\Phi=-J
\]

gives exactly

\[
 dP_N[\Phi_t]=\left[-P_N[J_t]+U_3[C\Phi_t]
 +\frac1N\rho_t[(B\Phi_t)_\mu]+\frac1{2N}\int B\Phi_t\right]dt+dM_t,
                                                                  \tag{6.5}
\]

where

\[
 \nabla_iP_N[\Phi]=N^{-2}\sum_{j\ne i}p(X_i,X_j)-N^{-1}a(X_i),
 \quad M=\sqrt{2\nu}\sum_i\int\nabla_iP_N[\Phi_t]\cdot dW_i.
                                                                  \tag{6.6}
\]

For completeness, its self bracket has all four pieces:

\[
 \frac{d\langle M\rangle}{dt}=2\nu\left[
 N^{-4}\sum_{i,j,k\ distinct}p_{ij}\cdot p_{ik}
 +N^{-4}\sum_{i\ne j}|p_{ij}|^2
 -2N^{-3}\sum_{i\ne j}p_{ij}\cdot a_i
 +N^{-2}\sum_i|a_i|^2\right].                                \tag{6.7}
\]

Neither the signed triple term nor the repeated-pair term is discarded from the identity. Its whole sum is nonnegative by (6.6). R8's full finite-N domain premise supplies finite expected absolute time integrals of every drift term, a true square-integrable M, and the singular passage from collision stops. Its proof uses absolute Haar triple integrability with the two separate relative singularities, structurally justified B Phi, finite-N density domination, L1 passage for drift, and L2 passage for noise. These are imported as the declared conditional domain theorem rather than derived from a merely Borel inverse. No new regularized corrector or diagonal passage is substituted.

Because Phi_T=0, integration of (6.5) gives the precise sign identity

\[
 \int_0^T U_3[C\Phi_t]dt
 =-P_N[\Phi_0]+\int_0^T P_N[J_t]dt
 -\frac1N\int_0^T\rho_t[(B\Phi_t)_\mu]dt
 -\frac1{2N}\int_0^T\int B\Phi_t\,dt-M_T.                    \tag{6.8}
\]

The lower and scalar contractions are both visible and are bounded separately next.

## 7. Uniform endpoint, lower contractions, and genuine noise

Write theta=1-s/d, p_*=s+2, and a_*=s/(s+2). At criticality nu_N=lambda_N^-1 N^-theta and beta_N tends to infinity, so b_N=1 eventually. Moreover

\[
 \chi_N=\nu_N N^{2/(s+2)}
 =\lambda_N^{-1}N^{s(s+2-d)/(d(s+2))}\longrightarrow0.         \tag{7.1}
\]

Here d>s+2 follows strictly from d>=4 and s<2. Hence the complete R12 module applies with a fixed finite L and bounded nu_* on every eventual critical tail. Constants may depend on that fixed L and on positive upper/lower bounds for lambda_N on the tail; no untracked N-dependent constant remains.

First, since 2s<d, the supplied R5 full inverse has a common Haar L2 bound. It also follows directly from J in L2, the singular L2 propagator, and the two-response series. An exact iid computation retaining the deleted-label bias is useful. For a real symmetric kernel F set m=int F, q_F(x)=int F(x,y)dy, a_F=q_F-m, and H_F=F-q_F(x)-q_F(y)+m. At the iid initial law,

\[
 P_N[F]=-\frac m{2N}-\frac1{N^2}\sum_i a_F(X_i)
                +\frac1{2N^2}\sum_{i\ne j}H_F(X_i,X_j),
\]

\[
 \mathbb E P_N[F]^2=\frac{m^2}{4N^2}
 +\frac{\|a_F\|_2^2}{N^3}
 +\frac{N-1}{2N^3}\|H_F\|_2^2
 \le\frac{\|F\|_2^2}{2N^2}.                                 \tag{7.2}
\]

The orthogonal decomposition uses exact partner centering; only equal unordered pairs survive the degenerate square. It is used solely at time zero. Therefore

\[
 \sigma_N\mathbb E|P_N[\Phi_0]|\le C\sqrt{b_N}\,N^{-1/2}.     \tag{7.3}
\]

For the lower contractions choose the fixed numbers

\[
 \epsilon=\tfrac12\min\{s,d-s-2\}>0,\quad q_*=1+\epsilon,
 \quad \zeta=\frac{s-\epsilon}{s+2}.                          \tag{7.4}
\]

They obey 1<q_*<d/2, q_*<=s+1, s+1+q_*<d, and zeta<1/2. Indeed epsilon<=s/2<1 gives q_*<2<=d/2; epsilon< s gives q_*<s+1; epsilon<d-s-2 gives s+1+q_*<d; and zeta<s/(s+2)<1/2. These strict inequalities are essential. R12's weighted gradient estimate, with its explicit N power, gives

\[
 |\nabla_{pair}\Phi_t(x,y)|\le C N^\zeta w_{q_*}(x-y).
\]

Since |K|<=C w_(s+1), the true product is now integrable in a single relative variable:

\[
 \sup_{t,x}\int|B\Phi_t(x,y)|dy
 \le C N^\zeta\int w_{s+1+q_*}(z)dz\le C N^\zeta.             \tag{7.5}
\]

This is justified in the strict range of the present theorem; it would fail for every q>1 at Coulomb. R8 was needed for the exact identity before this new estimate; an unjustified crude product was not used outside the allowed range. The total variation of rho=eta-dx is at most two. Thus, separately,

\[
 \frac{\sigma_N}{N}\mathbb E\int_0^T
             |\rho_t[(B\Phi_t)_\mu]|dt
 \le C\sqrt{b_N}\,N^{\zeta-1/2},
\]

\[
 \frac{\sigma_N}{2N}\int_0^T\left|\int B\Phi_t\right|dt
 \le C\sqrt{b_N}\,N^{\zeta-1/2}.                             \tag{7.6}
\]

No assertion that either scalar or random contraction has zero absolute value is used. A possible additional symmetry cancellation is unnecessary and is not substituted for (7.6).

Finally the exact earlier genuine-noise estimate is

\[
 Q_N:=\sigma_N^2\mathbb E\langle M\rangle_T
 \le C b_N N^{a_*}(N^{-\theta}+\nu_N).                        \tag{7.7}
\]

Its constants are uniform on the bounded-chi class. To verify the interface, R12 uses its gradient with q=(s+2)/2, which lies strictly between 1 and d/2 and is <=s+1. Squaring gives C N^{a_*}w_(s+2). The exact R6 energy identity and D_cl>=c w_(s+2)-C yield

\[
 \nu\int_0^T\mathbb Ew_{s+2}(X_1-X_2)dt
 \le C(N^{-\theta}+\nu),                                    \tag{7.8}
\]

using the heat-integral floor H_N>=-C N^{s/d} and retaining the whole nonnegative total-force square. The coefficient before the pair divergence in the unscaled energy identity is nu(N-1), so division by N-1 costs at most the factor N/(N-1)<=2. No individual-pair-force-square bound is extracted.

From (6.6), Cauchy-Schwarz in the finite label sum gives exactly

\[
 \mathbb E\sum_i|\nabla_iP_N|^2
 \le\frac{2(N-1)^2}{N^3}\mathbb E|p(X_1,X_2)|^2
       +\frac2N\|a\|_2^2.
\]

The second expectation uses only the genuine one-body Haar marginal, obtained by common-translation equivariance, not a product pair law. Multiplication by 2nu N b_N, (7.8), and the Haar integrability of w_(s+2) give (7.7), including every contraction in (6.7) through an upper bound on the whole square. At zero noise M is zero directly. At positive criticality nu_N=lambda_N^-1 N^-theta, and

\[
 a_*-\theta<0\quad\Longleftrightarrow\quad s(s+2)<2d.
\]

The inequality holds strictly because s<2 and d>=4. Since M is the supplied true square-integrable martingale, the isometry and Cauchy-Schwarz in probability give

\[
 \sigma_N\mathbb E|M_T|\le\sqrt{Q_N}
 \le C N^{(a_*-\theta)/2}\longrightarrow0.                   \tag{7.9}
\]

This is the genuine unsmoothed corrector noise. No critical TV statement or equality of higher marginals with product Haar enters.

## 8. The complete cubic conclusion and its actual strength

Combine (6.8), (5.6), (7.3), the two separate bounds (7.6), and (7.9). On every eventual critical tail,

\[
 \sigma_N\mathbb E\left|\int_0^T U_3[C\Phi_t]dt\right|
 \le C\left[N^{-1/2}+N^{s/d-1/2}
                 +N^{\zeta-1/2}+N^{(a_*-\theta)/2}\right]
 \longrightarrow0.                                         \tag{8.1}
\]

Each exponent is strictly negative in the frozen range. Finitely many early N do not affect the limit. All constants and parameter restrictions used to apply the earlier modules have been displayed. This proves exactly THM-036 from the complete supplied conditional premises, together with the new THM-037 estimate.

The theorem conjunction is therefore reconstructed conditionally without weakening either card. The proof of the cubic target is a bound on the absolute value of a time-integrated identity. In particular it does not prove sigma_N E integral |U3[C Phi_t]| dt tends to zero, does not assert concentration for the evolved pair observable at an intermediate endpoint, and does not establish an infinite critical hierarchy or limiting Gaussian law. The old beta_N N^(2s/d-1) condition is unused, and no replacement of microscopic criticality by that older condition occurs. No logarithmic, Coulomb, s=2, d=3, inhomogeneous, or general-law conclusion is added.

## 9. Independent falsification route and diagnostic evidence

The reconstruction tried to break the conclusion separately from the energy construction.

1. **High terminal frequencies.** An estimate with g_r energy on the same exponential Fourier scale need not be uniform under shifts. Replacing an arbitrary smooth test by a fixed finite polynomial would leave a gap. The explicit r/32 slack in (4.3) and the mode-dependent r_(N,n) remove this obstruction with the polynomial L_n^(d+2), which is summable for the stipulated fixed smooth h. No analytic dependence on h is needed.
2. **Very close actual pairs.** An upper estimate from the Fourier energy alone would omit the singular remainder. The nonnegative D2[H_r] in (2.6) controls exactly that omitted mass under the actual energy inequality. This was not inferred from mean-zero symmetry.
3. **N=2 and scalar tests.** The literal U3 has nonzero background terms even without an actual three-label sum, and P of a constant is -constant/(2N). The independent checker tests both, including the exact iid second moment with its constant bias.
4. **Repeated-pair integrability.** Using only the R11 gradient of order w_(s+1) would give a possibly nonintegrable w_(2s+2) majorant in dimension four. The explicit q_* in (7.4) has a provably integrable exponent and an N power strictly below sqrt(N). No failed bound is labeled a counterexample.
5. **Actual martingale versus reference law.** A Haar norm does not transfer to a critical higher marginal. Equations (7.7)–(7.8) instead use the supplied actual Laplacian occupation and the complete nonnegative particle-gradient square. Its triple term is retained in (6.7).
6. **Endpoint and limiting regimes.** T=0, constant h, zero noise for THM037, and fixed N=2 all satisfy the corresponding formulas. The boundary s=2,d=4 makes the source exponent zero and also makes the critical noise exponent zero, so the strict exclusions are structurally visible. They are not silently included.

The accompanying independently written Python diagnostic uses only the standard library and Gaussian rational arithmetic. It reads no earlier checker and imports no formula from an executable input. It builds the finite-particle observables from literal subset/ordered-label sums and applies a direct Fourier polynomial generator. Separately it constructs the hierarchy, integrated response slots, singular-source coefficient formula in its smooth diagnostic, four bracket pieces, exact iid endpoint coefficients, and the smooth energy self subtraction. It tests nonzero and zero kernels, constant/additive/relative/mixed symmetric pair tests, N=2,3,4,5 and extra N through 9 for energy, and nu=0,1/3,2. A dense rational set of admitted s and dimensions checks every strict power and weight inequality. Exact finite Fourier diagnostics test coefficients, not the analytic singular theorem.

Run from the isolated worktree:

    python3 AUDITS/BLIND_RECONSTRUCTION/ROUND_015_CUBIC_BLIND_ARTIFACTS/round015_exact_diagnostic.py

The executed result is PASS: 5,045 exact assertions, including all 28 input hashes. The issued JSON records the category outcomes. Arithmetic has no tolerance and no random seed. In its one-coordinate character convention D e_k=i k e_k; each physical first derivative restores 2 pi and each generator/source restores (2 pi)^2. The coordinate is embedded in the admitted d-dimensional torus. The tests support this derivation and are not a separate-context certification of its analytic argument or any earlier module.

## 10. Disposition and sealed handoff

| Frozen assertion or dependency | Reconstruction disposition |
|---|---|
| THM037 genuine source integrability and uniform absolute expectation | PROVED HERE FROM THE SUPPLIED KERNEL/PARTICLE PREMISES, with explicit smooth-test seminorm and all N/nu/t dependence. |
| THM037 integrated scaled consequence and zero-noise endpoint | PROVED HERE, uniformly on every bounded noise interval. |
| Full ordered cubic, responses, lower/scalar terms and Itô contractions | RECONSTRUCTED EXACTLY; singular domain/passage retains the supplied complete R8 conditional premise. |
| THM036 critical integrated cubic | PROVED CONDITIONALLY ON THE COMPLETE EARLIER MODULES, using (8.1). No claim for the absolute instantaneous cubic integral. |
| Earlier particle, inverse, domain and weighted/noise modules | CONDITIONAL AS ISSUED; no unseen audit status or current construction supplies a premise. |
| Exact negations of either frozen card | No admitted counterexample found; the conditional conjunction excludes them under the stated premises. |
| Full critical fluctuation law and campaign completion | NOT CLAIMED. Root alone compares and promotes. |

No remaining mathematical line inside the requested conditional conjunction is left unproved by this report plus the expressly retained prior premises. Independent evaluation of this new argument and disposition of those earlier premises remain the coordinator's responsibility. The artifact folder contains README, exposure disclosure, independent diagnostic and results, frozen input manifest, output manifest, verification record, immutable archive, and external seal. The report and archive are sealed before any candidate comparison. No canonical state is edited, and no commit, push, source installation, or child is used. Any correction after issuance must be a separately named addendum or superseding report; these issued bytes are immutable.
