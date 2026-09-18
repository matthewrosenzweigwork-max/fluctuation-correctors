# THM-046 / PO-033 — actual critical Coulomb threshold source

Status OPEN / UNAUDITED. Round024,2026-09-18 UTC. This is a bounded subgate of the unchanged campaign mission, not a replacement target.

Fix d=4,s=2, coefficient-one mean-zero periodic Coulomb g (nonzero Fourier coefficient |k|^-2), K=-grad g. Actual singular gradient particles solve dX_i=N^-1 sum_(j!=i)K(X_i-X_j)dt+sqrt(2nu_N)dW_i, starting iid unit Haar independently of their Brownian drivers. beta_N>0,nu_N=1/beta_N,lambda_N=beta_N N^-1/2 ->lambda in(0,infinity). Set b_N=min(beta_N,1),sigma_N=sqrt(N b_N). Fix finite T>=0 and real h in C-infinity(T^4). The backward response semigroup Q_t^nu has nonzero-mode multiplier exp[-t(4pi^2+4pi^2nu|k|^2)] and preserves constants.

With J^f(x,y)=K(x-y).(grad f(x)-grad f(y)), literal ordered deleted-diagonal U2 including both Haar row/background terms, and P_N=U2/2, the primary assertion is

sigma_N E | integral_0^T P_N[J^(Q_(T-t)^nu_N h)](X(t)) dt | ->0.

Absolute value is after the time integral. Constants may depend on h,T,lambda and eventual upper/lower bounds on lambda_N, never on N. No replacement by signed expectation, iid positive-time law, bounded N-body density or static energy/Haar class. No claimed rate, test-uniformity, process theorem or hierarchy closure.

Exact negation: there exist admitted T,h,lambda>0 and sequence beta_N with lambda_N->lambda for which the displayed nonnegative quantity has positive limsup. A static well-prepared law, altered preparation/dynamics, T_N or N-dependent h does not negate it.

Current accepted R16 supplies only O(1) after scaling at s=d/2. R12/R14 strict sub-Coulomb estimates do not apply at s=d-2. R8 supplies the actual finite-N pair identity/domain but not a uniform threshold remainder. The old energy-floor condition beta_N N^(2s/d-1)->0 and full subcritical lambda_N->0 are distinct from this critical row. Partial progress must prove an exact smaller obligation or rule out a precisely stated route, without declaring the assertion false or proved.
