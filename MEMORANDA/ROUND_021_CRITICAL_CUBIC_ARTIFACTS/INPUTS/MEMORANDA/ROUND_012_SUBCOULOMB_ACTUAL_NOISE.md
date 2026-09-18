# Round012 — a strict sub-Coulomb actual-noise candidate

2026-09-18 UTC. ROOT CONSTRUCTION / SELF_CHECKED; INDEPENDENT RECONSTRUCTION AND HOSTILE REVIEW REQUIRED. This is an additional subrange theorem candidate, not replacement of the campaign target. The current R10 actual-energy construction is a conditional input until its fresh review; prior R6/R7/R8 and full-pair sources retain their frozen scopes. The independent R11 worker has not supplied or certified this argument, and its current proof was not read. No actual-noise gate is promoted by this memorandum.

## 1. Exact assertion and negation

Fix integer d>=3,0<s<d-2,T finite,smooth real h,finite L and nu_*. Let N>=2 and 0<=nu<=nu_* satisfy chi_N=nu N^(2/(s+2))<=L. Use the genuine homogeneous full pair inverse Phi, both response slots, unit Haar, K=-grad g, actual iid-Haar-prepared particles and ordered-pair P=U2/2. Set p=s+2,a=s/p,theta=1-s/d. At positive nu, beta=1/nu,b_N=min(beta,1),sigma_N^2=N b_N. At zero noise the relevant noise functionals are zero without taking a reciprocal.

First claim, with any fixed exponent 1<q<d/2 satisfying q<=s+1, is

    sup_(t,x!=y) |grad_pair Phi_t(x,y)|/w_q(x-y)
        <= C_q N^((s+1-q)/p).                         (1.1)

The weights are exactly R7(2.1), w_alpha=w_1^alpha>=1, equal to r^-alpha on r<=R=1/16 and bounded on the fixed annulus. The constant depends on d,s,q,T,h,L,nu_* and the fixed kernel/cutoff, not N or the chosen diffusivity.

The second claim is an actual, rather than Haar-reference, bound:

    Q_N:=2nu N b_N E integral_0^T sum_i|grad_i P_N[Phi_t](X_t)|^2 dt
       <= C b_N N^a (N^-theta+nu).                   (1.2)

The first claim with q=p/2 is admissible because s>0 and p<d. The particle domain/true L2 martingale is the supplied R8 premise. If s(s+2)<2d, every microscopic critical sequence lambda_N=beta_N N^-theta->lambda in(0,infinity) satisfies Q_N->0. In addition, for 0<s<min(2,d-2), every bounded-chi sequence in this scope satisfies Q_N->0. At s=2 bounded chi alone does not suffice for this conclusion; the more general sufficient conditions are N^(a-theta)->0 and N^a nu_N->0. No boundary equality is silently included.

Exact negation: an admitted fixed data tuple and bounded-chi family violate (1.1) or (1.2) with every uniform constant, or a sequence in a stated strict limiting subrange has positive limsup Q_N. No counterexample is presumed or constructed here. Coulomb is excluded from (1.2), since the occupation mechanism below vanishes there.

## 2. Uniform weighted evolution at bounded chi

Use the complete R7 weighted-gradient proof, Sections2–5, not an unspecified C_N. For its auxiliary pair evolution S, write ell=(2s/N)chi_cut r^-p+O(1/N) in the homogeneous model. The Jacobian operator norm is bounded by exp(integral ell), using the largest transverse eigenvalue and not the absolute Hessian norm. For moment1 and weightq the local calculation is exactly

    ((G+ell)w_q)/w_q
       <= -2s(q-1)r^-p/N+2nu q(q+2-d)_+ r^-2+C/N.  (2.1)

The annular cutoff terms are bounded by constants times nu+1/N. Retain half the negative term and maximize the remaining expression A nu r^-2-B r^-p/N. With v=1/r its maximum is at most

    C_(s,q) N^(2/s) nu^(p/s)=C_(s,q) chi_N^(p/s).   (2.2)

If the diffusion coefficient in (2.1) is nonpositive there is no positive maximum cost. Thus one uniform C_L works in the full torus inequality

    (G+ell)w_q <= C_L w_q-c_q N^-1 1_(r<=R) w_(q+p),
    c_q=s(q-1)>0.                                 (2.3)

The exact R7 stopped exponential-weight argument retains its nonnegative terminal and occupation terms. Its fixed-start noncollision premise and conditional Fatou passage therefore give, for every t<=u<=T,

    E exp(integral_t^u ell) w_q(Z_u)<=exp(C_L(u-t)) w_q(z),
    N^-1 E integral_t^T exp(integral_t^u ell)
         1_(r_u<=R) w_(q+p)(Z_u)du<=C w_q(z).      (2.4)

Constants are uniform over the bounded-chi family. This does not use uniform integrability of a stopped singular terminal weight. R7's higher moments and common-start differentiability remain available at each fixed N; they need not be uniform to justify the derivative formula before applying (2.4).

## 3. Recovering the correct power for the true source

The actual Fourier test has uniform C3 norm for bounded nu, by the supplied homogeneous full-interface source. Hence |grad_pair J_t|<=C_h w_(s+1). Put eta=s+1-q, so 0<=eta<p. For every v>=0, v^eta<=1+v^p. Apply this with v=w_1/N^(1/p). On the inner ball this gives

    w_(s+1)<=N^(eta/p)w_q+N^(eta/p-1)w_(q+p).

On the fixed annulus and complement w_1 is uniformly bounded and N^(eta/p)>=1. Thus a single fixed constant gives globally

    w_(s+1)<=C N^(eta/p)w_q
             +N^(eta/p-1)1_(r<=R)w_(q+p).         (3.1)

For the true base source potential U_t=integral_t^T S_(t,u)J_u du, R7(5.8) supplies its actual off-diagonal derivative as expectation of the path Jacobian times grad J. Combine its absolute bound with both parts of (2.4) and (3.1):

    sup_t |U_t|_q<=C N^(eta/p),
    |F|_q:=sup_(x!=y)|grad_pair F(x,y)|/w_q(x-y).   (3.2)

The factor N from occupation is exactly canceled by N^(eta/p-1), yielding the desired power rather than an untracked O(N) bound. No source derivative is heat-truncated or replaced by its leading radial term. R7's fixed-N finite-difference/uniform-integrability proof justifies the derivative representation; no new exchange of expectation and a singular derivative is presumed. At T=0 both derivatives vanish.

## 4. The two full responses do not cost another N power

In the homogeneous model the complete response is precisely

    R F=-integral F(x+w,y)D(dw)-integral F(x,y+w)D(dw).

Global weak differentiation of the shifted function, established in R7 Sections6–8, differentiates F and not D. The finite-measure weighted convolution bound for every q<d gives

    |R F|_q<=2 C_(D,q)|F|_q.                       (4.1)

C_(D,q) depends only on the fixed kernel and weight. The periodic compensation is included. A Coulomb atom would also satisfy this bound, though the later occupation proof is strictly below Coulomb. For the auxiliary propagator, the same Jacobian formula and first part of (2.4) give

    |S_(t,u)F|_q<=exp(C_L(u-t))|F|_q.              (4.2)

The already constructed full inverse has a finite uniform-in-time weighted gradient at each fixed N by R7. Its actual Volterra identity is Phi=U+integral S R Phi. All derivative formulas needed here are already established in that proof. Applying (3.2),(4.1),(4.2) and the elementary backward Gronwall inequality to this finite norm gives

    |Phi_t|_q <= C N^(eta/p) exp(2C_(D,q)exp(C_LT)T).

This proves (1.1), retaining both responses. No self-adjointness, positivity or contraction of R is needed. Its coefficient1 in each slot is unchanged. Fixed-N constants are used only for existence/differentiation; the displayed estimate explicitly controls the resulting norm uniformly.

## 5. Actual Laplacian occupation below Coulomb

For this strict range p=s+2<d, the punctured divergence satisfies

    D_cl(z)=s(d-2-s)r^-p+smooth local remainder.

The coefficient is strictly positive. With the same fixed weight there are c>0,C<infinity such that D_cl>=c w_p-C globally off zero. The exact actual energy identity of R6, averaged over iid Haar initial data, is

    E H_N(X_T)+E integral sum_i|B_i|^2
       +nu(N-1) integral E D_cl(X1-X2)dt=0.        (5.1)

Its singular Laplacian occupation is integrable at each positive nu by that supplied theorem; no new singular Ito step is introduced. The new R10 heat-integral lower bound H_N>=-C N^(s/d), equation(3.5) of the complete TASK061 report, is a conditional input pending its own fresh review. Apply it to (5.1), discard only the nonnegative full force square, and use D_cl>=c w_p-C. Since N/(N-1)<=2,

    nu integral_0^T E w_p(X1-X2)dt
       <= C(N^-theta+nu), theta=1-s/d.             (5.2)

No individual pair-force square is extracted from the total-force square. The new moment is obtained from the Laplacian term itself. At zero nu the noise is handled directly, without dividing this inequality by zero. At Coulomb D_cl is a negative constant, its positive singular-density coefficient vanishes, and (5.2) does not follow. This is a structural range restriction of this proof.

## 6. The genuine full martingale

Use (1.1) with q=p/2. It lies strictly between1 and d/2, and q<=s+1. Since w_q^2=w_p, its exponent gives

    |G_t(x,y)|^2<=C N^a w_p(x-y), G=grad_x Phi.    (6.1)

The Haar integral of w_p is finite because p<d. Set A_t(x)=integral G_t(x,y)dy. Jensen gives ||A_t||2^2<=||G_t||2^2<=C N^a.

Differentiate the genuine ordered deleted-pair statistic using its supplied domain:

    grad_i P=N^-2[sum_(j!=i)G(Xi,Xj)-N A(Xi)].

The elementary square bound, followed by exchangeability and the actual one-body Haar marginal, gives exactly

    E sum_i|grad_i P|^2
       <=2(N-1)^2 N^-3 E|G(X1,X2)|^2+2N^-1||A||2^2.

Multiplying by2nu N b_N and integrating time yields

    Q_N<=4nu b_N integral[(N-1)^2 N^-2 E|G12|^2+||A||2^2]dt.

Apply (6.1),(5.2) and the Haar A bound to obtain (1.2). This controls the entire nonnegative actual bracket, including the possible signed triple and mixed terms, by a direct configuration-space inequality. It does not separately bound their absolute marginal errors. The actual martingale and its finite-N square integrability are those of R8; no clipped or smoothed replacement remains in Q_N.

For the leading martingale, actual one-body Haar and the uniform Fourier-test gradient give Q_1<=C nu b_N<=C. Cauchy–Schwarz in probability,time and particle components bounds the expected integral of absolute scaled cross-variation by C sqrt(Q_N). It therefore vanishes in every subrange where (1.2) tends to zero. This does not address the cubic drift residual or higher correctors.

## 7. Limiting ranges, checked separately

At microscopic criticality, nu_N=N^-theta/lambda_N. Also

    chi_N=lambda_N^-1 N^[s(s+2-d)/(d(s+2))].

Since d>s+2 in this strict sub-Coulomb range, chi_N tends to zero and is eventually bounded. Further

    a-theta=s/(s+2)+s/d-1<0 iff s(s+2)<2d.

Thus (1.2) is O(N^(a-theta)) and tends to zero in exactly the claimed strict critical subrange. Finitely many initial N are irrelevant to this limit and do not change the fixed-data quantifiers. For 0<s<min(2,d-2), bounded chi implies N^a nu<=L N^((s-2)/p)->0, while d>p and s<2 imply sp<2d, so the other term vanishes too. Neither argument covers equality s(s+2)=2d or the s=2 bounded-chi case without an extra smallness condition.

These ranges are sufficient consequences of the proved candidate estimate, not a necessity theorem or a redefinition of microscopic subcriticality. The old energy-floor condition, full microscopic subcriticality and positive finite criticality remain distinct. General subcritical beta->0, Coulomb, larger s, general backgrounds, logarithmic interactions, evolved cubic residual, hierarchy closure and full fluctuation laws remain open or outside this claim.

## 8. Status and next verification

The first unsupported external premise in this report is the newly constructed R10 sharp heat-integral energy floor until its fresh review is issued; all additional arguments above are root constructions and require fresh independent reconstruction and hostile review. No numerical check or root rereading can upgrade them. TASK063's separate R11 theorem is not a source here. A fresh reconstruction should receive only the exact assertion, definitions and complete permitted prior sources, withholding this proof and its interpolation/occupation narrative until its report is sealed. A fresh hostile reviewer should receive this complete proof and recompute every uniform constant and range. Any repair must be a new artifact after this memorandum is issued.
