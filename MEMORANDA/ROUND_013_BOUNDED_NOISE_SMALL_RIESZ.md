# Round013 — full actual-noise decay throughout a bounded diffusivity interval

2026-09-18 UTC. Root Astra Ultra construction, SELF_CHECKED. Fresh independent reconstruction and hostile review required. No gate is promoted by this memorandum. This proof was constructed after the R12 root proof and fresh Ultra reconstruction; that exposure is explicit. It also uses the complete R10 constructor reports and the R11 constructor, but no R11 claim is a mathematical premise. Earlier supplied proofs and the new R10 floor/clipping implication retain their conditional source statuses until separately accepted.

## 1. Statement, law and logical negation

Fix d>=4, 0<s<2, N>=2, T finite, a smooth real test h, and finite nu_*. The genuine homogeneous full pair inverse Phi has both response slots and the actual Fourier test. Its particle law starts from iid unit Haar, independent of Brownian drivers, with zero external drift, K=-grad g and noise sqrt(2nu). Write p=s+2, a=s/p, theta=1-s/d and, at positive nu, beta=1/nu, b=min(beta,1), sigma_N^2=Nb. The corrector uses the literal ordered deleted-pair coefficient 1/(2N^2), empirical mean-field background subtraction 1/N, and the scalar Haar background 1/2. The R8 complete domain premise supplies the genuine L2 martingale, with no new singular Ito claim here.

We prove the precise THM034 assertion, including uniform decay of

    Q_N=2nu Nb E integral_0^T sum_i |grad_i P_N[Phi_t](X_t)|^2dt

over the entire interval 0<=nu<=nu_*. All constants below depend only on fixed data, the stated weight exponent and the fixed kernel/cutoff; none depend on N or the selected nu. A violating admitted family or sequence, as specified in THM034, is the exact negation. Fixed N does not suffice for any uniform conclusion. At zero diffusivity Q_N is zero directly; no reciprocal is taken.

## 2. Retain the favorable diffusion contribution

Use the actual auxiliary pair process and fixed periodic weights in R7 Sections2–5: w_alpha=w_1^alpha>=1, equal to r^-alpha for r<=R=1/16 and smooth and bounded on the complement of a smaller collision tube. For the homogeneous generator G and its one-sided Jacobian potential ell, the inner radial calculation is

    (G+ell)w_q
      <=-2nu q(d-2-q) w_(q+2)
         -2s(q-1)N^-1 w_(q+p)+C N^-1 w_q.       (2.1)

Here 1<q<min(d-2,d/2), q<=s+1, eta=s+1-q<2. The largest transverse eigenvalue, not the absolute Hessian norm, gives ell=2s r^-p/N+O(1/N). Both strict coefficients in (2.1) are positive after moving the terms to the left. Smooth local remainders and fixed annular derivatives contribute at most C(nu+1/N)w_q. Since nu<=nu_*, they have a uniform bound. Reducing the retained coefficients if needed gives on the entire punctured torus

    (G+ell)w_q<=C w_q
        -c_1 nu 1_(r<=R) w_(q+2)
        -c_2 N^-1 1_(r<=R) w_(q+p),             (2.2)

with fixed c_1,c_2>0. There is no positive singular diffusion term to maximize and no assumption on chi=nu N^(2/p). This is the change from the R12 argument. In d=3 there is no q>1 below d-2; at s=2 the later choice q=p/2 reaches a boundary in d=4 and the low-noise decay power also vanishes.

Apply the same stopped exponential-weight Ito calculation as the supplied R7 proof, at collision cutoffs before their fixed-N removal. Multiplying by exp(-C(u-t)+integral_t^u ell), retaining both nonnegative occupations and the terminal weight, gives

    E exp(integral_t^u ell) w_q(Z_u)<=e^(C(u-t))w_q(z),
    nu E integral_t^T exp(integral_t^u ell)
           1_(r_u<=R)w_(q+2)(Z_u)du<=C w_q(z),
    N^-1 E integral_t^T exp(integral_t^u ell)
           1_(r_u<=R)w_(q+p)(Z_u)du<=C w_q(z).   (2.3)

The positive terminal/occupation bounds pass by conditional Fatou and fixed-start noncollision; no new uniform-integrability claim for a singular terminal weight is needed. The fixed-N higher moments, common-start differentiability and legitimate differentiation of expectations remain those fully proved in R7. They are invoked before estimating the resulting derivative with (2.3), so no old N-dependent differentiation constant enters the bound.

## 3. Two source scales, the same full inverse

The actual Fourier source obeys |grad_pair J|<=C_h w_(s+1) uniformly in t,N,nu. For eta=s+1-q in[0,2), the elementary inequality x^eta<=1+x^m applies with m=p and m=2. On the inner ball, insert x=w_1/N^(1/p) and x=sqrt(nu)w_1, respectively. On its fixed complement increase a constant depending only on nu_* and the weights. This gives

    w_(s+1)<=C N^(eta/p)w_q
           +N^(eta/p-1)1_(r<=R)w_(q+p),
    w_(s+1)<=C nu^(-eta/2)w_q
           +nu^(1-eta/2)1_(r<=R)w_(q+2).        (3.1)

For eta=0 these statements are still valid; zero powers are one. For nu>0 all factors are finite. The second bound may have a constant larger than one when nu_*>1, but that constant is fixed, not a hidden N/nu parameter.

R7's genuine derivative formula for U_t=integral_t^T S_(t,u)J_u du bounds its derivative by the Jacobian-weighted source derivative. Apply separately the two inequalities (3.1), using the matching occupation estimate and the terminal bound in (2.3). With |F|_q=sup_(x!=y)|grad_pair F|/w_q, this proves

    sup_t |U_t|_q<=C min(N^(eta/p),nu^(-eta/2)). (3.2)

For the homogeneous responses,

    R F=-integral F(x+w,y)D(dw)-integral F(x,y+w)D(dw).

Both finite signed-measure convolutions are retained. The supplied R7 weighted convolution proof gives |RF|_q<=2C_(D,q)|F|_q. Weak differentiation acts on F, not on D, and there is no term involving a separate value-amplitude norm. The first bound in (2.3) similarly gives |S_(t,u)F|_q<=e^(C(u-t))|F|_q. Each identity is applied to the already constructed genuine full inverse, whose weighted derivative is finite uniformly in time for every fixed N and nu by R7. Its differentiated Volterra equation and backward Gronwall then yield

    sup_t |Phi_t|_q<=C_q min(N^(eta/p),nu^(-eta/2)). (3.3)

All quantities entering Gronwall are explicitly bounded as above; its response constant and finite horizon are fixed. Existence is not inferred from a seminorm. Identification is with the already supplied bounded Borel full inverse, not a formal source potential, an internal-only diagnostic, a truncated response series or the R11 response-only limit. The derivative-only norm therefore does not impose an extra N^a amplitude factor.

## 4. Actual occupation and the small-diffusivity part

In this range p<d, and the actual punctured divergence satisfies D_cl>=c w_p-C with c>0 from s(d-2-s). The exact R6 energy identity, iid-Haar initial mean energy zero, and the supplied R10 sharp heat-integral lower bound H_N>=-C N^(s/d) give

    nu E integral_0^T w_p(X1-X2)dt<=C(N^-theta+nu). (4.1)

Indeed the energy identity contains the nonnegative total-force square and nu(N-1) integral E D_cl; discarding only that whole square and using N/(N-1)<=2 gives (4.1). No individual pair-force square or new collision integration by parts is inserted. The prior domain and energy results are exact prerequisites with their original singular-limit proofs.

Choose q_*=p/2=1+s/2. Since d>=4 and s<2, it lies strictly below d-2 and d/2, and eta=s/2<1. Thus (3.3) gives, with G=grad_x Phi,

    |G|^2<=C min(N^a,nu^(-s/2))w_p.              (4.2)

Put A(x)=integral G(x,y)dy. The Haar integral of w_p is finite; Jensen and the actual one-body Haar marginal control the A term. The exact statistic derivative is N^-2[sum_(j!=i)G(Xi,Xj)-N A(Xi)]. Finite-sum Cauchy–Schwarz, exchangeability and multiplication by the physical 2nu Nb imply

    Q_N<=4nu b integral[(N-1)^2/N^2 E|G12|^2+||A||_2^2]dt
       <=C b min(N^a,nu^(-s/2))(N^-theta+nu).    (4.3)

This proves the displayed THM034 estimate for all positive nu, without a chi restriction. It controls the full nonnegative bracket directly; no assumption of small separate pair/triple/mixed marginal errors is made.

For 0<nu<=delta<=min(1,nu_*), split at nu_0=N^-2/p. Below nu_0 use the N^a option in (4.3); above it use nu^-s/2. Since nu_0^-s/2=N^a and 1-s/2>0,

    sup_(0<nu<=delta) Q_N
       <=C[N^(a-theta)+N^((s-2)/p)+delta^(1-s/2)]. (4.4)

This remains a valid bound when either subinterval is empty. The inequality a<theta follows from s(s+2)<2d, which is strict because s<2 and d>=4. Thus first N->infinity and then delta->0 control the low-diffusivity portion uniformly.

## 5. Actual radial clipping for the remaining interval

For nu>=delta>0 choose instead q_-=1+s/4, eta_-=3s/4<2 and

    r=p/q_-=4(s+2)/(s+4)>2.

This q also lies strictly in (1,min(d-2,d/2)) and is at most s+1. Equation (3.3) gives |G|<=C delta^(-eta_-/2)w_(q_-). Define radial clipping G^L=G min(1,L/|G|), with value zero at G=0, and R_L=G-G^L. Its own Haar background is A_R=integral R_L dy. No claim that a clipped vector field is itself a pair-potential gradient is needed: its predictable particle field defines the clipped martingale in the exact supplied R10 construction.

The elementary radial tail inequality yields

    |R_L|^2<=L^(2-r)|G|^r
      <=C delta^(-eta_- r/2)L^(2-r)w_p.         (5.1)

Apply the same configuration-space square bound as in Section4 to the residual field N^-2 sum R_L-N^-1 A_R. Use (4.1) for the actual pair and Haar Jensen for its own background. If T_N(L) is its expected scaled bracket, then

    T_N(L)<=C b delta^(-eta_- r/2)L^(2-r)(N^-theta+nu)
           <=C delta^(-eta_- r/2)L^(2-r).       (5.2)

The final constant uses only nu_* and N>=2. Crucially, the occupation input already controls nu times the pair moment. There is no extra delta^-1 factor. At this point r>2, despite s<2; this differs from a tail argument using only the energy moment w_s and a merely fixed-N derivative constant.

The complete supplied R10 clipping theorem applies to the same G, the same actual law and its own mean. At L_N=N^(1/(4p)) its bound is

    Q_N^clip<=C[b N^-2/p+b sqrt(nu)L_N^2 N^-1/p]
            <=C[N^-2/p+N^-1/(2p)],             (5.3)

because b<=1 and b sqrt(nu)<=1. The underlying entropy/free-energy estimate, exact low-order marginal formula and Haar energy estimate are the precise R10 premises; scalar mean zero or actual exchangeability alone would not justify (5.3). The physical sigma_N scaling is identical on all three martingales.

In the probability-time-particle L2 space, the genuine field equals its clipped field plus residual, so Q_N<=2Q_N^clip+2T_N(L_N). For every fixed delta>0, (5.2) tends uniformly to zero over delta<=nu<=nu_*. Together with (4.4) and then delta->0 this proves the uniform conclusion in THM034. No interchange of a fixed-N singular approximation limit with N is hidden here: (5.2) is the actual quantitative tail estimate that supplies the needed uniform passage.

## 6. One explicit rate and cross-variation

For a single quantitative choice, take delta_N=N^-epsilon with epsilon=1/(6p^2). Eventually delta_N<=min(1,nu_*) when nu_*>0. Since epsilon<2/p, the low- and high-diffusivity estimates apply with a nonempty scale separation; empty intervals would cause no problem anyway. Compute

    r-2=2s/(s+4),
    eta_- r/2=3s(s+2)/(2(s+4)),
    epsilon eta_- r/2-(r-2)/(4p)=-s/(4p(s+4)),
    epsilon(1-s/2)=(2-s)/(12p^2).

Substitution into (4.4),(5.2),(5.3), and absorption of the faster N^((s-2)/p) term yields

    Q_N<=C[ N^(a-theta)+N^(-(2-s)/(12p^2))
            +N^(-s/(4p(s+4)))+N^-1/(2p)+N^-2/p ]. (6.1)

Every displayed exponent is strictly negative on the fixed range; the final two terms mean N^(-1/(2p)) and N^(-2/p). This is sufficient rather than optimal. If nu_*=0, Q_N=0 identically and the same conclusion needs no positive-noise estimate. The actual leading scaled bracket is at most C nu b<=C from the uniform Fourier-test gradient and one-body Haar marginal. Cauchy–Schwarz in probability, time and particle components bounds the expected integral of absolute scaled cross-variation by C sqrt(Q_N), hence it vanishes uniformly too.

## 7. Scope, status and first remaining assertion

This construction closes the entire actual-noise smallness assertion only in the conditional homogeneous range d>=4,0<s<2,bounded diffusivity. No finite-chi or nu->0 hypothesis survives. It is a candidate awaiting independent gates, and its R10 premises remain conditional until their separate acceptance. It does not prove the evolved cubic residual, lower contractions, endpoint-time corrector concentration under evolved laws, higher hierarchy, a fluctuation law, or the remaining d=3/Coulomb/larger-s ranges. The old beta_N N^(2s/d-1)->0, full subcritical lambda_N=beta_N N^(s/d-1)->0 and positive finite criticality are unchanged and distinct. The logarithmic case is separate.

Within this proposed range, the next load-bearing equation is the actual evolved cubic drift residual with all lower contractions from the exact R8 identity, once this noise candidate is independently accepted. Outside it, PO024 remains open. No source novelty or necessity claim is made. The proof is a new combination of complete supplied exact arguments, not a replacement by a radial toy computation. All supporting arithmetic must be separately labeled as diagnostic and must not assign an audit pass.
