# Round 004: the coefficient-one diffusive comparison fails above s=d-2

2026-09-17. Root construction, PROVED_CANDIDATE / SELF_CHECKED only. No independent verdict is inferred. This statement is the exact negation of extending the local coefficient-one radial comparison beyond its declared range. It is not nonexistence of a corrector, failure of another majorant, or a fluctuation counterexample.

## Fixed data and claim

Fix an integer d>=1, 0<s<d with s>d-2, N>=2, nu>0 and any nonzero z0. Put p=s+2, v(z)=(2s/N)|z|^-s-2 z, L=2nu Delta+v.grad and j(z)=s|z|^-s. Work on a finite annulus D={a<|z|<R} containing z0 in its interior. Construct the process by the bounded Lipschitz drift cutoff equal to v near the closed annulus, killed at first exit rho. This is the elementary additive-noise Picard construction; on this annulus all coefficients and stopped stochastic integrals used below are bounded. Define the nonnegative killed source potential

    U_D(tau,z0)=E_z0 integral_0^(tau wedge rho) j(Z_h) dh.

It is finite since j is bounded on the annulus. Let F_(N,tau) be the exact zero-diffusion radial formula from THM017. Claim: there is tau0>0, depending on the fixed parameters and annulus, such that

    U_D(tau,z0)>F_(N,tau)(|z0|)  for every 0<tau<tau0.

Thus the asserted coefficient-one majorization by the transport profile fails even for the isotropic positive source A=I in an interior point of a killed annular realization. Exact negation: these fixed permitted data have no sufficiently small positive time interval with this strict inequality. The proof below excludes that negation.

## A compactly supported test supplies a rigorous lower expansion

Choose a smooth function chi in C_c^infinity(D) with 0<=chi<=1 and chi=1 on a neighborhood of z0, and set phi=chi j. Then 0<=phi<=j on D. Both phi and Lphi are smooth and compactly supported inside D, as is L^2 phi. Extend them by zero to the cemetery state. Their values are zero at the killed boundary, including Lphi. Stopped smooth Ito and bounded convergence therefore give the exact identities for the killed evolution S_h:

    S_h phi(z0)=phi(z0)+integral_0^h S_v Lphi(z0) dv,
    S_v Lphi(z0)=Lphi(z0)+integral_0^v S_w L^2 phi(z0) dw.

To see that no boundary term has been dropped, the value phi(Z_(h wedge rho)) equals 1_(h<rho) phi(Z_h), since phi=0 on the boundary; the same holds for Lphi. The stochastic integrands before exit are bounded, so their expectation is zero. The killed evolution contracts the sup norm by direct expectation. Consequently, with B=||L^2 phi||infinity on D,

    |S_h phi(z0)-phi(z0)-h Lphi(z0)| <= B h^2/2.

Integrating in h, and using phi<=j and Tonelli for the nonnegative bounded source, gives

    U_D(tau,z0) >= tau j(z0)+(tau^2/2)Lj(z0)-B tau^3/6.       (1)

The equalities phi(z0)=j(z0) and Lphi(z0)=Lj(z0) hold because chi is identically one on a neighborhood of the fixed interior point. No unbounded-source semigroup Taylor theorem, global diffusion existence, boundary regularity or origin Ito formula is used.

## Exact transport expansion and positive coefficient

At fixed r0=|z0|>0 the explicit profile is smooth in tau through zero and satisfies

    F_(N,tau)(r0) = tau j(z0)+(tau^2/2)(v.grad j)(z0)+R(tau),
    |R(tau)| <= C_F tau^3/6,  0<=tau<=1,

where one possible completely explicit bound is

    C_F = [4 s^3 (2s+2)/N^2] r0^(-3s-4).

Indeed partial_tau F=s(r0^p+2sp tau/N)^(-s/p), its second derivative at zero is -(2s^3/N)r0^(-2s-2)=v.grad j, and its third derivative is [4s^3(2s+2)/N^2](r0^p+2sp tau/N)^(-s/p-2), whose maximum is attained at tau=0. This checks all time and N factors.

Subtracting this expansion from (1),

    U_D(tau,z0)-F_(N,tau)(r0)
       >= nu Delta j(z0) tau^2 -(B+C_F) tau^3/6.             (2)

The radial Laplacian is

    Delta j(z0)=s^2(s+2-d) r0^(-s-2)>0.

Define c=nu s^2(s+2-d)r0^(-s-2)>0 and

    tau0=min(1, 3c/(B+C_F+1)).

For 0<tau<tau0 the right side of (2) is at least c tau^2/2>0. This proves the claimed strict failure with explicit positive time range. It also independently explains why the radial Laplacian of F has the wrong sign near zero remaining time in this exponent range.

## Scope and next audit

This proves a specific obstruction to extending the coefficient-one radial supersolution across s=d-2. At the threshold the second-order difference computed here vanishes; no strict failure there follows, and THM020 includes that threshold through its full superharmonic sign. For d>=3 and s<d-2, the second-order difference is negative, consistent with that theorem. For d=1,2 every allowed positive s satisfies the strict-failure condition above. The argument does not rule out a constant C>1, another profile, a smaller-nu perturbation, another domain realization or full corrected fluctuation closure. It does not use the interacting N-particle law.

If a global positive-source realization exists and agrees with the local process until annular exit, its full occupation dominates U_D and inherits the same failure at the chosen point; this last sentence is conditional and is not used by the annular counterexample.

Dependencies are the frozen coefficient conventions, THM017's explicit formula and the smooth stopped Ito identity on a bounded annulus. All expansions and finite-annulus construction steps are supplied above. No literature or novelty claim, numerical inference, limit as N tends to infinity, or critical regime conclusion is imported. The next step is a separate hostile review, with the root construction frozen before that review. Original positive theorem and source bytes remain unchanged.
