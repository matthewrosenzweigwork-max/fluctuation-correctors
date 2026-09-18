# AUD050 — hostile review of the complete critical cubic/source conjunction

Issued 2026-09-18 05:10:31 UTC; immutable upon completion of the accompanying archive seal.

TASK-078. **Verdict: CONDITIONAL PASS for every assertion in the frozen THM-036 and THM-037 cards.** No mathematical repair to the candidate is required within their exact stated hypotheses and supplied earlier-module premises. No admitted counterexample was found. This verdict certifies the reviewed implication, not the correctness of every older module. Root comparison with the separately isolated reconstruction remains required before any campaign promotion.

The reviewed candidate is `MEMORANDA/ROUND_015_CRITICAL_CUBIC_RESIDUAL.md`, SHA-256 `5ac57cf35afdfa16c8923966f6984be3e18dbc6f70049aaf09acebdababe23cc`. The two target hashes are `313a1edfd9e5e47b204de94d7a323fe070266d6d3e7527594a74ab72763f3a28` and `5108030bafb41065ed9f4e11629effc4c3cad818d4ac7c7cde2728985d783aac`, respectively. This is a fresh candidate-exposed hostile review, not a statement-only blind reconstruction. The new diagnostic was written here without reading any previous checker.

## 1. Scope, exact assertions, and their negations

Fix an integer \(d\ge4\), \(0<s<2\), a finite horizon \(T\), a fixed smooth real terminal test \(h\), and the unit-Haar torus with characters \(e^{2\pi i k\cdot x}\). The interaction has the frozen Fourier coefficients

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
\]

The actual particles solve

\[
 dX_i=N^{-1}\sum_{j\ne i}K(X_i-X_j)dt+\sqrt{2\nu}\,dW_i,
\]

from iid Haar coordinates independent of their independent Brownian drivers. The reference is Haar and \(\rho=\eta_N-dx\). The genuine Fourier test and genuine symmetric terminal-zero pair inverse retain both coefficient-one responses, the full internal drift \(B/N\), and all issued singular representatives. No evolving product law is assumed.

Write \(\theta=1-s/d\). THM-037 asserts, for each fixed finite \(\nu_*\), a constant uniform in every \(N\ge2\), \(\nu\in[0,\nu_*]\), and deterministic \(t\in[0,T]\), such that

\[
 \mathbb E|P_N[J_t](X_t)|\le C N^{-\theta},\qquad
 J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y)). \tag{H1}
\]

It also asserts genuine integrability and the stated uniform time-integrated scaled consequence, including zero noise. Its exact negation is an admitted fixed tuple for which

\[
 \sup_{N\ge2,\,0\le\nu\le\nu_*,\,0\le t\le T}
 N^\theta\mathbb E|P_N[J_t](X_t)|=\infty.
\]

Failure of a method to give this bound is not that negation.

For THM-036, let \(\lambda_N=\beta_NN^{-\theta}\to\lambda\in(0,\infty)\), \(\nu_N=1/\beta_N\), \(b_N=\min(\beta_N,1)\), and \(\sigma_N=\sqrt{Nb_N}\). Its assertion is exactly

\[
 \sigma_N\mathbb E\left|\int_0^T U_3[C\Phi_t](X_t)dt\right|\longrightarrow0,
 \quad C\Phi=\operatorname{Sym}_3[K(x-z)\cdot\nabla_x\Phi(x,y)]. \tag{H2}
\]

The symmetrization averages six permutations, and the deleted tuple denominators are powers of \(N\). Its exact negation is an admitted fixed tuple and a positive finite critical sequence for which the displayed quantity has positive limsup. A different law, inverse, source, or order of absolute value is not an admitted counterexample.

The strict inequalities \(s<d-2\) and \(2s<d\) follow from the frozen range, including \(d=4\). The source proof below uses only the actual particle/heat-passage premise and the verified local kernel structure. The cubic implication additionally uses the complete full-inverse, R8 domain, and R12 weighted-gradient/noise premises in their stated scopes. Historical audit or proof-status text is not a premise.

## 2. Claim-by-claim verdict

Each PASS below means a pass of this conditional implication. The locations refer to the immutable candidate. The complete input inventory and source qualifications are in `ROUND_015_CUBIC_HOSTILE_ARTIFACTS/SOURCE_PREFLIGHT.md` and `INPUT_SHA256SUMS.txt`.

| Audit claim | Assertion and candidate location | Verdict and reason |
|---|---|---|
| AUD050-C01 | Frozen kernel, force, Fourier sign, noise, centering, both responses; (1.1)–(1.8), (2.1)–(2.3) | PASS. Recomputed constants and signs below; no logarithmic substitution or changed model. |
| AUD050-C02 | Actual nonpositive expected energy; (3.2)–(3.4) | PASS. Smooth free energy, fixed-N same-noise convergence, common lower bound and Fatou have the correct directions. Zero noise follows from the supplied exact deterministic energy identity. |
| AUD050-C03 | Positive retained energy plus close-pair remainder; (3.5)–(3.10) | PASS. Both nonnegative quantities are retained jointly, with the exact smooth self coefficient and the distinct labelled-pair coefficient. |
| AUD050-C04 | Absolute singular source tail, including all backgrounds; (4.1)–(4.3) | PASS. The differentiated Gaussian estimate is pointwise and integrates to a positive majorant. Every empirical/background coefficient is included. |
| AUD050-C05 | Uniform low-test-band multiplier estimate; (5.1)–(5.5) | PASS. The two frequency cases, derivative estimate, smaller cutoff and polynomial test-mode cost are valid. The low-band hypothesis is essential and is respected. |
| AUD050-C06 | Source Fourier coefficient and smooth zero self diagonal; (5.6)–(5.8) | PASS. Both gradient contributions have the stated sum and negative physical sign. Only the genuinely smooth commutator is evaluated on its diagonal. |
| AUD050-C07 | Every fixed smooth terminal test, arbitrary high modes; (6.1)–(6.4) | PASS. The exact mode split and the fixed Fourier seminorm control the complementary tail without an exponential mode loss. |
| AUD050-C08 | THM-037 genuine absolute integrability and deterministic-time uniformity, including \(\nu=0\) | PASS. The proof gives (H1) throughout the frozen bounded-noise class. The candidate's short zero-noise sentence is justified explicitly in Section 3 below. No added hypothesis is needed. |
| AUD050-C09 | THM-037 scaled absolute time-integral consequence | PASS. Tonelli gives \(C\sqrt b\,N^{s/d-1/2}\), uniformly, with \(b=1\) defined directly at zero noise. |
| AUD050-C10 | Genuine R8 representatives, partial diagonals and fixed-N expectation passages; Section 7 | PASS as application of the complete R8/R6 premises. Separate relative-variable integrability and the fixed-N density bound suffice; no uniform-N density estimate is used. |
| AUD050-C11 | All six cubic terms, Haar contractions and finite-label coefficients; (7.1)–(7.7) | PASS. Direct distinct-label reconstruction and new exact tests agree. Both lower contractions and both responses are necessary in nonvacuous diagnostic cases. |
| AUD050-C12 | True martingale, no extra thermal trace, terminal integrated identity; (7.6)–(7.8) | PASS. The R8 bracket integrability supports the true martingale and L2 stop passage; the integrated signs are correct. |
| AUD050-C13 | Initial iid correction, exact mean/first projection/degenerated part; (8.2a)–(8.2b) | PASS. Independently recounted; the uniform pair L2 premise applies because \(2s<d\). Product sampling is used only at time zero. |
| AUD050-C14 | Uniform lower/scalar contractions and chosen exponent; (1.10), (8.3)–(8.5) | PASS. The chosen weight is in the R12 range and its force product is integrable. Each lower term vanishes separately with its exact coefficient. |
| AUD050-C15 | Full actual noise and critical regime; (8.1), (8.6)–(8.8) | PASS. Recomputed weighted-gradient, occupation and bracket factors; the critical sequence enters the required bounded-rescaled-noise class. |
| AUD050-C16 | Complete THM-036 quantitative conclusion and exact negation; (1.11), (8.8) | PASS. All four powers are strictly negative, including the \(d=4,s\uparrow2\) corner for each fixed admitted \(s\). |
| AUD050-C17 | Zero horizon, constant terminal test, and stated exclusions | PASS. Zero horizon is immediate; constant test gives the zero source/inverse. No instantaneous absolute cubic estimate, full fluctuation law or broader law/geometry/endpoint theorem follows. |

No failed proof line or admitted counterexample was identified. Therefore there is no repaired or weakened substitute theorem in this report. The strongest established result is the conjunction of the two frozen assertions, with the candidate's quantitative cubic bound and exactly the retained conditional premises.

## 3. Recomputed actual energy, positive remainder, and source estimate

Set \(\alpha=(d-s)/2>1\), \(c=4\pi^2\), and \(A=4^\alpha\pi^{d/2}/\Gamma(s/2)\). The periodized Gaussian has mass one and Fourier multiplier \(e^{-ct|k|^2}\). Therefore

\[
 A\Gamma(\alpha)c^{-\alpha}
 =\pi^{s-d/2}\frac{\Gamma(\alpha)}{\Gamma(s/2)}=c_{d,s}.
\]

The Euclidean part of \(A\int_0^\infty t^{\alpha-1}p_t\,dt\), with the substitution \(u=|z|^2/(4t)\), is exactly \(|z|^{-s}\). Nonzero lattice terms have exponentially small short-time derivatives near zero; the long-time subtractions and their derivatives are integrable. This reproduces the coefficient-one local expansion. In particular \(K\in L^1\), and

\[
 D=\operatorname{div}K=s(d-2-s)g_{s+2}\,dx,
 \quad \int D=0,\quad D\ge-\kappa dx,
 \quad \frac{4\pi^2c_{d,s}}{c_{d,s+2}}=s(d-2-s).
\]

The one-body response multiplier is \(-4\pi^2c_{d,s}|k|^{s+2-d}\). Hence the frozen backward Fourier test has coefficients bounded in modulus by \(|\widehat h(k)|\), uniformly in time and the entire prescribed diffusivity class. Spatial derivatives of any fixed order are uniformly bounded; bounded noise also controls the required time derivatives in the older inverse/domain premises.

Let \(H_N=N^{-1}\sum_{i<j}g(X_i-X_j)\). Its particle drift is precisely \(-\nabla H_N\). For each fixed positive particle-interaction heat cutoff \(\eta\) and \(\nu>0\), differentiation of the smooth periodic density equation gives

\[
 \frac d{dt}\left(\nu\int F^\eta\log F^\eta+
                         \int H_N^\eta F^\eta\right)
 =-\int F^\eta|\nabla H_N^\eta+\nu\nabla\log F^\eta|^2\le0. \tag{H3}
\]

The initial terms vanish because the initial density is one and the kernel has mean zero. Entropy is nonnegative on the unit-mass Haar space. At this fixed cutoff smooth positive density justifies the logarithm and the integrations by parts. If \(g_*\) is the finite negative infimum of the off-zero kernel, positivity of heat convolution gives \(H_N^\eta\ge(N-1)g_*/2\). The complete R6 same-noise result gives convergence of the particle paths and, on their positive realized separation, local uniform convergence of the energy observables. Fatou after subtracting this common fixed-N lower bound yields

\[
 \mathbb EH_N(X_t)\le0. \tag{H4}
\]

This does not pass a singular Fisher-information identity and does not require uniformity of the density bound in N. At zero noise, R6(5.6) is the pathwise identity

\[
 H_N(X_t)+\int_0^t\sum_i|B_i(X_u)|^2du=H_N(X_0).
\]

The iid initial energy is integrable with expectation zero. Averaging this identity gives (H4) at \(\nu=0\) directly. Thus the zero-noise statement in the candidate is supported, rather than a limit obtained by dividing by diffusivity.

Exchangeability and \(|g|\le g+2|g_*|\) give \(\mathbb E|g(X_1-X_2)|\le2|g_*|\). This bounds the local inverse-s-power distance moment uniformly in N, noise and deterministic time. It does not bound a squared pair force.

For an observable cutoff \(\tau>0\), distinct from the particle regularization, put

\[
 g^{>\tau}=A\int_\tau^\infty t^{\alpha-1}(p_t-1)dt,
 \quad W_\tau=A\int_0^\tau t^{\alpha-1}p_tdt\ge0,
 \quad c_\tau=A\tau^\alpha/\alpha.
\]

Off zero, \(g=g^{>\tau}+W_\tau-c_\tau\). The retained kernel is smooth, mean zero and has positive coefficients

\[
 a_\tau(k)=A\int_\tau^\infty t^{\alpha-1}e^{-c|k|^2t}dt.
\]

Also \(g^{>\tau}(0)\le C\tau^{-s/2}\) for \(0<\tau\le2\). This follows by integrating \(Ct^{-s/2-1}\) at small times and the exponentially decaying Fourier remainder at large times; for \(\tau\in[1,2]\) enlarge the fixed constant.

Writing \(D_2=N^{-2}\sum_{i\ne j}\), exact smooth self subtraction gives

\[
 D_2[g]=\sum_{k\ne0}a_\tau(k)|\widehat\eta_N(k)|^2
 -\frac{g^{>\tau}(0)}N+D_2[W_\tau]
 -\frac{N-1}{N}c_\tau. \tag{H5}
\]

All terms are integrable: at fixed cutoff the retained part is smooth; the remainder is off-zero equal to an integrable energy observable plus bounded terms. Since \(D_2[g]=2H_N/N\), (H4) proves

\[
 \mathbb E\sum_{k\ne0}a_\tau(k)|\widehat\eta_N(k)|^2
 +\mathbb ED_2[W_\tau]
 \le\frac{g^{>\tau}(0)}N+\frac{N-1}{N}c_\tau
 \le C(N^{-1}\tau^{-s/2}+\tau^\alpha). \tag{H6}
\]

The two quantities on the left are nonnegative. In particular the labelled-pair inequality is

\[
 \mathbb EW_\tau(X_1-X_2)\le
 \frac{g^{>\tau}(0)}{N-1}+c_\tau,
\]

not the N-squared-sum bound with its self coefficient left unchanged. The same calculation without expectation gives the deterministic floor \(H_N\ge-CN^{s/d}\) at \(\tau=N^{-2/d}\), supplying exactly the floor later used in the R12 occupation estimate.

For torus distance \(\ell(z)\), termwise Gaussian differentiation gives

\[
 \ell(z)|\nabla p_t(z)|\le C_dp_{2t}(z).
\]

Indeed \(\ell(z)\le|z+n|\) in every Gaussian summand, and the resulting squared-distance factor is absorbed by replacing \(e^{-|z+n|^2/(4t)}\) by a constant times \(e^{-|z+n|^2/(8t)}\). The factor \(2^{d/2}\) is fixed. For smooth v, the shortest torus segment bounds the gradient difference by \(\|D^2v\|_\infty\ell(z)\). Integrating the preceding inequality in positive heat time gives

\[
 |J_v-J_v^{>\varepsilon}|\le
 C\|D^2v\|_\infty W_{2\varepsilon}. \tag{H7}
\]

The row and scalar integrals are bounded by the same constant times \(c_{2\varepsilon}\). In the literal P statistic the particle term contributes one half of \(\mathbb ED_2W\), the mixed term at most \(c_{2\varepsilon}\), and the scalar at most \(c_{2\varepsilon}/2\). Thus

\[
 \mathbb E|P_N[J_v-J_v^{>\varepsilon}]|
 \le C\|D^2v\|_\infty(N^{-1}\varepsilon^{-s/2}+\varepsilon^\alpha). \tag{H8}
\]

No signed tail expectation is substituted for this absolute estimate.

## 4. Recomputed commutator estimate and high test modes

For nonzero real k,

\[
 a_\delta(k)=Ac^{-\alpha}|k|^{-2\alpha}\Gamma(\alpha,c\delta|k|^2).
\]

For fixed \(\alpha>1\), direct integration over \([x,x+1]\) for \(x\ge1\) and over \([1,2]\) for \(x\le1\) gives \(\Gamma(\alpha,x)\ge c_\alpha e^{-x}\). Also \(a_\delta(k)\le C|k|^{-2\alpha}\).

Let nonzero lattice vectors u,v obey \(m=u+v\ne0\) and \(\varepsilon|m|^2\le1\). The candidate estimate is

\[
 |m\cdot(ua_\varepsilon(u)+va_\varepsilon(v))|
 \le C|m|^{2\alpha+1}
       \sqrt{a_{\varepsilon/64}(u)a_{\varepsilon/64}(v)}. \tag{H9}
\]

If \(|u|\le2|m|\), then \(|v|\le3|m|\). The incomplete-gamma lower bound gives the square root at least \(c|m|^{-2\alpha}\), since the relevant scaled squared norms are bounded. The numerator is at most \(C|m|\), using \(|u|,|v|\ge1\) and \(1-2\alpha<0\). This proves (H9) in the first case without a constant depending on m.

If \(|u|>2|m|\), set \(L(k)=ka_\varepsilon(k)\). Evenness gives the difference \(L(u)-L(u-m)\). Differentiating under the absolutely convergent heat integral yields

\[
 \|DL(k)\|\le A\int_\varepsilon^\infty
 t^{\alpha-1}(1+2c|k|^2t)e^{-c|k|^2t}dt
 \le C|k|^{-2\alpha}e^{-c\varepsilon|k|^2/2}.
\]

On the segment from u to u-m, the norm is between \(|u|/2\) and \(3|u|/2\). The mean-value integral therefore bounds the numerator in (H9) by

\[
 C|m|^2|u|^{-2\alpha}e^{-c\varepsilon|u|^2/8}.
\]

The denominator in (H9) is at least

\[
 c|u|^{-2\alpha}
 e^{-c\varepsilon(|u|^2+|v|^2)/128}
 \ge c|u|^{-2\alpha}e^{-13c\varepsilon|u|^2/512}.
\]

The exponent gap is positive: \(1/8-13/512=51/512\). Thus their ratio is bounded by \(C|m|^2\), which is at most \(C|m|^{2\alpha+1}\) because \(|m|\ge1\). For m=0 the numerator vanishes exactly. This recomputation confirms the smaller-cutoff margin and all uniformity claims in the lemma.

Direct multiplication of the two test gradients gives the physical pair Fourier coefficient

\[
 \widehat J_v^{>\varepsilon}(u,v')
 =-4\pi^2\widehat v(u+v')
 (u+v')\cdot(ua_\varepsilon(u)+v'a_\varepsilon(v')). \tag{H10}
\]

The two terms have the same final sign; removing either destroys the high pair-frequency cancellation. The new exact diagnostic checks this coefficient including zero frequencies. Since the retained source is smooth and its gradient difference is zero at equal arguments, its actual smooth diagonal is zero. Therefore

\[
 P_N[J_v^{>\varepsilon}]=\tfrac12\langle\rho^{\otimes2},J_v^{>\varepsilon}\rangle.
\]

The rho zero mode is zero. For \(b(k)=\sqrt{a_{\varepsilon/64}(k)}|\widehat\rho(k)|\), Cauchy–Schwarz and reindexing give \(\sum_u b(u)b(m-u)\le\sum_kb(k)^2\). At each positive cutoff this series is summable. For test support \(|m|\le\varepsilon^{-1/2}\), (H9)–(H10) prove the configuration-wise bound

\[
 |P_N[J_v^{>\varepsilon}]|
 \le C\sum_m|\widehat v(m)|(1+|m|)^{d-s+1}
          \sum_{k\ne0}a_{\varepsilon/64}(k)|\widehat\eta_N(k)|^2. \tag{H11}
\]

Only the positive Fourier energy in (H6) is used. No arbitrary weighted kernel is declared positive semidefinite.

Now take \(\varepsilon=N^{-2/d}\), \(R=\varepsilon^{-1/2}\), and split the actual Fourier series exactly into \(f_t^{\le R}+f_t^{>R}\). The low part has uniformly bounded Hessian and the seminorm in (H11). Combining (H6), (H8) and (H11) gives its source bound \(CN^{-\theta}\). For

\[
 H_*:=\sum_m(1+|m|)^{d+4}|\widehat h(m)|<\infty,
\]

absolute Fourier summation gives \(\sup_{t,\nu}\|f_t^{>R}\|_{C^2}\le CH_*R^{-(d+2)}\). The original unsmoothed source satisfies

\[
 |J_w(x,y)|\le C\|w\|_{C^2}(1+\ell(x-y)^{-s}).
\]

The actual pair moment and uniform background row bound from Section 3 therefore yield

\[
 \mathbb E|P_N[J_{f_t^{>R}}]|
 \le CH_*\varepsilon^{(d+2)/2}\le CH_*\varepsilon^\alpha.
\]

This proves (H1) for every fixed smooth real h. All constants are independent of N, selected noise and deterministic time. The arguments establish measurable genuine integrable representatives, so Tonelli gives

\[
 \sigma\mathbb E\int_0^T|P_N[J_t]|dt
 \le C_T\sqrt b\,N^{s/d-1/2}\to0,
\]

uniformly on the bounded-noise class. Here \(0<b\le1\) at positive noise and \(b=1\) is defined directly at zero noise. This verifies all of THM-037, including its absolute-value placement.

A useful adversarial test is to remove the low-test-band restriction from (H9). At fixed \(\varepsilon>0\), take \(u=e_1\), \(v=(m-1)e_1\), and let the integer m grow. The numerator is asymptotic to \(m a_\varepsilon(e_1)\), while the denominator has exponential Gaussian decay in m up to polynomial factors. No fixed polynomial test-mode bound survives. The candidate explicitly avoids this false stronger lemma by its exact low/high split. This is a failure of a discarded extension, not a counterexample to either frozen theorem.

## 5. Singular representatives, exact identity, and martingale

Let \(G=\nabla_x\Phi\), \(A_\Phi(x)=\int G(x,y)dy\), and \(R=R_x+R_y\). In the supplied R8 domain choose \(1<q_1<d/2\) and \(q_1+1<q_2<d\). The gradient and Hessian bounds are finite at each fixed N, with respective weights \(w_{q_1}\) and \(w_{q_2}\). Global weak differentiation and integrable time/internal drift are exactly the issued R8 statements. Their slice results give the derivatives of \(\int\Phi(x,y)dy\) and \(\int\Delta_y\Phi(x,y)dy=0\).

For the raw cubic term,

\[
 \int|K(x-z)||G(x,y)|dxdydz
 \le\|K\|_1\sup_x\int|G(x,y)|dy<\infty.
\]

This uses the two independent relative variables: \(s+1<d\) and \(q_1<d\) separately. A one-background integral with two fixed distinct empirical points has separated singular locations; near either location the other factor is locally bounded. Two-background integrals follow by absolute Fubini. No gradient value on a pair diagonal is introduced. Repeated empirical pairs in the drift must be grouped by symmetry before applying the structural R8 internal-drift bound.

Integration of the six terms yields

\[
 (C\Phi)_1=\tfrac16\{K(x-y)\cdot(A_\Phi(x)-A_\Phi(y))+R\Phi(x,y)\},
\]
\[
 (C\Phi)_2=\tfrac13v_\Phi,\quad (C\Phi)_0=0,
 \quad v_\Phi(x)=\int K(z-x)\cdot A_\Phi(z)dz,
 \quad (R\Phi)_\mu=v_\Phi. \tag{H12}
\]

To recount the finite labels directly, differentiate the genuine P statistic on a collision-excluded configuration set. Its force part is

\[
 Q=N^{-3}\sum_{i\ne j}\sum_{k\ne i}K(X_i-X_k)\cdot G(X_i,X_j)
   -N^{-2}\sum_{i\ne k}K(X_i-X_k)\cdot A_\Phi(X_i).
\]

Separate \(k=j\) from all-distinct labels. Pairing the two repeated-pair orientations produces \(D_2[B\Phi]/(2N)\). Inserting (H12) in the exact U3 definition cancels the remaining mixed-background force, leaving

\[
 Q=U_3[C\Phi]+P_N[R\Phi]+\frac1{2N}D_2[B\Phi]. \tag{H13}
\]

This calculation is valid even at N=2: only the all-distinct triple sum is empty, while the Haar contraction terms need not vanish. The independent diffusion is precisely \(P_N[\nu\Delta_{x,y}\Phi]\). Distinct Brownian drivers have no cross variation, and the Haar background Laplacian integrates to zero. Hence there is no additional thermal trace.

Let \(b_t(x)=\int B\Phi_t(x,y)dy\) and \(\bar b_t=\int B\Phi_t\). The purely finite-label identity

\[
 D_2[B\Phi]=2P_N[B\Phi]+2\rho[b_t]+\bar b_t
\]

and the full inverse equation imply

\[
 dP_N[\Phi_t]=\{-P_N[J_t]+U_3[C\Phi_t]+N^{-1}\rho_t[b_t]+(2N)^{-1}\bar b_t\}dt+dM_t^2,
\]
\[
 \nabla_iP_N[\Phi]=N^{-2}\sum_{j\ne i}G(X_i,X_j)-N^{-1}A_\Phi(X_i),
 \quad M_t^2=\sqrt{2\nu}\sum_i\int_0^t\nabla_iP_N[\Phi_u]\cdot dW_i. \tag{H14}
\]

The complete R6/R8 finite-N density bound is \(F_t\le e^{(N-1)\kappa T}\). It is sufficient to transfer the just-checked Haar drift integrability and gradient square integrability to finite absolute expected time integrals and a finite expected bracket. Thus the stochastic integral is a square-integrable true martingale. R8's collision-stop removal is by L1 convergence of the grouped drift and L2 convergence of the stochastic integral; boundedness of the finite-N undifferentiated inverse controls the endpoint. None of these exponential-in-N constants is used in the later uniform estimates.

Since \(\Phi_T=0\), integration of (H14) gives, with every sign retained,

\[
 \int_0^TU_3[C\Phi_t]dt
 =\int_0^TP_N[J_t]dt-P_N[\Phi_0]-M_T^2
   -N^{-1}\int_0^T\rho_t[b_t]dt-(2N)^{-1}\int_0^T\bar b_tdt. \tag{H15}
\]

This identity controls the absolute value after the cubic time integral. It does not establish a uniform estimate for the time integral of the absolute cubic integrand.

## 6. Recomputed endpoint, lower terms, and complete actual noise

For a symmetric real Haar-L2 pair kernel F, put \(m=\int F\), \(q_0(x)=\int F(x,y)dy-m\), and \(F_\circ=F-q_0(x)-q_0(y)-m\). Direct substitution gives

\[
 P_N[F]=\tfrac12D_2[F_\circ]-N^{-1}\eta_N[q_0]-m/(2N).
\]

Under iid Haar, a product of two centered pair summands integrates to zero unless the unordered labels coincide; single projections are orthogonal to those pair terms. The exact second moment is consequently

\[
 \mathbb E|P_N[F]|^2
 =\frac{N-1}{2N^3}\|F_\circ\|_2^2+rac1{N^3}\|q_0\|_2^2+rac{m^2}{4N^2},
 \quad \|F\|_2^2=\|F_\circ\|_2^2+2\|q_0\|_2^2+m^2. \tag{H16}
\]

Approximation in Haar L2 justifies the same formula for the genuine kernel. The complete R5 full inverse has \(\|\Phi_0\|_2\le C\) because \(2s<d\) and the critical noise is eventually bounded. Multiplication of (H16) by \(Nb_N\) gives \(\sigma_N^2\mathbb E|P_N[\Phi_0]|^2\le Cb_N/N\). Thus the endpoint contributes \(CN^{-1/2}\). No evolved iid argument occurs.

Put \(p=s+2\), \(a=s/p\), and

\[
 \omega=\tfrac12\min\{s,d-s-2,d/2-1\},\quad r=1+\omega,
 \quad e=(s-\omega)/p.
\]

Then \(\omega>0\), \(1<r<d/2\), \(r\le s+1\), and \(s+1+r=p+\omega<d\). The complete R12 gradient premise gives

\[
 |\nabla_{\rm pair}\Phi_t|\le C N^e w_r,
 \quad |B\Phi_t|\le C N^e w_{s+1+r}.
\]

The second weight is Haar integrable, so \(\|b_t\|_\infty+|\bar b_t|\le CN^e\). Thus each lower term in (H15), separately, contributes at most \(CN^{e-1/2}\), using \(|\rho[b_t]|\le2\|b_t\|_\infty\), \(\sigma_N\le\sqrt N\), and retaining the scalar factor one half.

For clarity, I also recomputed the analytic powers in the imported R12 noise implication. In the homogeneous auxiliary pair flow, the largest transverse Jacobian eigenvalue has principal part \(2sN^{-1}r^{-p}\). Acting on a weight \(w_q\) with its exponential Jacobian factor gives the retained negative coefficient \(-2s(q-1)N^{-1}r^{-p}\). The possible positive diffusion cost is controlled by maximizing

\[
 A\nu v^2-BN^{-1}v^p,
\]

which is \(C N^{2/s}\nu^{p/s}=C(\nu N^{2/p})^{p/s}\). Thus it is uniform in the specified bounded-rescaled-noise class. The source interpolation

\[
 w_{s+1}\le C N^{(s+1-q)/p}w_q
 +N^{(s+1-q)/p-1}\mathbf1_{r\le R}w_{q+p}
\]

uses the elementary inequality \(v^{s+1-q}\le1+v^p\). The retained occupation term costs one factor N and cancels exactly the N inverse in the second summand. The homogeneous two-response derivative bound depends only on the weighted convolution of the finite compensated divergence, with both slots included; it introduces no extra N power. These checks reproduce the explicit uniform gradient power while leaving the older R7 expectation-differentiation and inverse identification results as conditional premises.

For the actual law, the sharp deterministic energy floor following (H5) and the exact R6 energy identity give

\[
 \mathbb EH_N(X_T)+\mathbb E\int_0^T\sum_i|B_i|^2dt
 +\nu(N-1)\int_0^T\mathbb ED_{\rm cl}(X_1-X_2)dt=0.
\]

Since \(D_{\rm cl}\ge c_0w_p-C\) with \(c_0>0\) in the strict range \(p<d\), and \(H_N\ge-CN^{s/d}\), it follows that

\[
 \nu\int_0^T\mathbb Ew_p(X_1-X_2)dt\le C(N^{-\theta}+\nu). \tag{H17}
\]

Only the full nonnegative force square is discarded. The coefficient \(N-1\) comes from the exact \(2/N\) unordered-pair Laplacian. No individual-pair-force-square bound or Coulomb-density argument is substituted. At zero noise the stochastic integral is zero directly.

Choose \(q=p/2\), which satisfies \(1<q<d/2\) and \(q\le s+1\). Then \(|G|^2\le CN^aw_p\) and \(\|A_\Phi\|_2^2\le CN^a\). The one-body Haar marginal is valid under the actual law by common-translation equivariance of the SDE and the initial law, not by product structure. A direct square estimate on (H14) gives

\[
 \mathbb E\sum_i|\nabla_iP_N|^2
 \le\frac{2(N-1)^2}{N^3}\mathbb E|G(X_1,X_2)|^2+rac2N\|A_\Phi\|_2^2.
\]

Multiplying by \(2\nu Nb_N\), integrating, and using (H17) proves the precise full-bracket bound

\[
 Q_N=\sigma_N^2\mathbb E\langle M^2\rangle_T
 \le Cb_NN^a(N^{-\theta}+\nu_N). \tag{H18}
\]

This bounds the complete square including all mixed and triple contributions. The exact diagnostic separately verifies its finite-label four-term expansion. The analytic estimate does not require the terms in that expansion to have individual favorable signs.

At positive finite criticality,

\[
 \nu_N=\lambda_N^{-1}N^{-\theta},\qquad
 \nu_NN^{2/p}=\lambda_N^{-1}N^{s(s+2-d)/(d(s+2))}\to0.
\]

Thus the actual parameters eventually satisfy every fixed bounded-rescaled-noise premise; also \(\beta_N\to\infty\) and \(b_N=1\) eventually. The true-martingale property and Itô isometry give \(\sigma_N\mathbb E|M_T^2|\le C N^{(a-\theta)/2}\). Combining this with (H1), (H15), (H16) and the lower bounds proves exactly

\[
 \sigma_N\mathbb E\left|\int_0^TU_3[C\Phi_t]dt\right|
 \le C\left(N^{1/2-\theta}+N^{-1/2}+N^{e-1/2}+N^{(a-\theta)/2}\right). \tag{H19}
\]

The strict margins are

\[
 \theta-\tfrac12=\tfrac12-\frac sd>0,\qquad
 \tfrac12-e=\frac{2-s+2\omega}{2(s+2)}>0,\qquad
 \theta-a=\frac{2d-s(s+2)}{d(s+2)}>0.
\]

For the last inequality, \(s(s+2)<8\le2d\). Constants may deteriorate as the fixed parameters approach an excluded endpoint. No uniform estimate in s approaching 2 is asserted. This completes THM-036 and excludes its exact negation under the retained premises.

## 7. New diagnostics and falsification work

`ROUND_015_CUBIC_HOSTILE_ARTIFACTS/diagnostic.py` uses only Python's standard library and exact rational Laurent-polynomial arithmetic. There is no randomness, floating tolerance, external dependency, imported checker, or copied checker implementation. All **1,422 checks passed**. The exact results are in `results.json`.

The checks independently build the statistic from slot subsets and injective label assignments, then differentiate the resulting N-particle polynomial. They compare this with the response/cubic/lower decomposition for constant, additive, relative, product, mixed and combined symmetric pair kernels, N=2,3,4, and zero/positive noise. Other checks cover N through 6, all cubic contractions, the two response contractions, the full bracket expansion, exact iid second moments, source Fourier coefficients and zero smooth diagonal, positive-energy self subtraction, and N versus N-1 conversion. All physical second-order differential expressions carry the same restored factor \(-(2\pi)^2\) in the documented formal-derivative convention; no factor is removed from only one side.

The tests are nonvacuous: omitting the response causes nonzero defects in 15 kernel/N cases, omitting the linear lower contraction in 9, omitting the scalar in 9, and substituting N-1 for the internal N coefficient in 15. These are exact finite smooth diagnostics, not counterexamples to the supplied singular theorem.

There are 258 rational parameter rows for the critical exponents, including fixed values within one millionth of both s endpoints. The exact cancellation diagnostic at \(d=5,s=1\), total test frequency one and zero observable cutoff, compares the two opposite pair frequencies. Its normalized sum is

\[
 \frac{3u^2-3u+1}{u(u-1)}\in(3,7/2]\quad(u\ge2),
\]

whereas summing their absolute contributions grows above \(2u-1\). This is a useful exact test of the cancellation mechanism, not a substitute for the positive-cutoff proof in Section 4. A separate analytic attempted falsification there shows why the candidate's low/high test split cannot be dropped.

The principal adversarial checks were: wrong free-energy direction; missing smooth self contribution; labelled-pair normalization; converting signed energy directly into absolute source without a positive remainder; false weighted positivity; uncontrolled high modes of a merely smooth test; missing cubic background or scalar terms at N=2; unjustified singular derivatives/diagonal traces; product-law transfer at positive time; loss of a factor in the full bracket; and the d=4, s near 2 corner. None produces a failure of the candidate with its actual hypotheses.

## 8. Limitations, immutable handoff, and root disposition

This review does not certify the earlier modules unconditionally. It has not inspected current audit files or used a historical or current status as a mathematical premise; the late ambient status-only message is disclosed in EXPOSURE.md. It does not inspect or incorporate the current blind reconstruction. Root must compare the separately sealed reports and determine canonical disposition. No campaign ledger, theorem card, constructor memorandum, prior report, or immutable input was edited.

No stronger instantaneous absolute cubic estimate, full CLT, higher-order closure or infinite resummation follows from this conjunction. No claim is made for s=2, d=3, Coulomb, logarithmic interaction, inhomogeneous backgrounds, another preparation or unbounded-noise cubic parameters. The proof of the frozen source assertion uses the stipulated bounded-noise interval. No external citation or novelty claim was needed; there is no unverified external reference supporting a load-bearing line.

The bounded task ends with the sealed packet. The artifact README records reproduction and byte verification; `EXPOSURE.md` discloses the ambient context and intentional candidate exposure; `SOURCE_PREFLIGHT.md` inventories all 30 permitted sources and their uses. `OUTPUT_SHA256SUMS.txt` identifies the payload, and the externally stored archive seal verifies exact membership and member bytes. The audit report becomes immutable upon seal issuance. No commit, push, installation, external search, child agent or canonical integration was performed.
