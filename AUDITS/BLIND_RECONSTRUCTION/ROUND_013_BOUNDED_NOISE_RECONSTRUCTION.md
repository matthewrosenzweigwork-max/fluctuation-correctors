# Round 013: statement-only reconstruction of the full bounded-noise claim

TASK-071. Issued 2026-09-18 UTC. **CONDITIONAL RECONSTRUCTION PASS; no unconditional promotion.**

The frozen THM-034 follows from the earlier conditional modules identified below. The argument covers every diffusivity in the prescribed bounded interval, including arbitrary dependence on the particle number. It does not replace the frozen claim by a rescaled subfamily. No counterexample or unsupported new line was found in this conditional implication. The earlier particle, inverse/domain, and R10 clipping premises retain their issued conditional status; this report does not independently certify those premises.

This is a statement-only reconstruction. The TASK-071 card and its input manifest were read first. The prescribed R9-base worktree was created, and exactly the 27 allowed input byte strings were copied and hash-checked before their mathematics was read. The constructor proof, root seed, current R11/R12/R13 constructions and audits, prior checker programs, canonical state/history, and memory files were not read. The automatically supplied ambient memory summary was visible; it contains broad research/workspace context and was not used as a mathematical premise. The parent assignment disclosed that the frozen claim was unexpectedly stronger, but supplied no mathematical route. No candidate comparison occurred before sealing.

## 1. Frozen assertion and logical negation

Fix integer \(d\ge4\), \(0<s<2\), finite \(T\), a smooth real terminal function \(h\), and \(0\le\nu_*<\infty\). The torus has Haar mass one, Fourier characters \(e^{2\pi i k\cdot x}\), and the frozen potential is

\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\qquad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad
 K=-\nabla g.
 \tag{1.1}
\]

For \(N\ge2\), the actual particles have zero external drift and satisfy

\[
 dX_i=\frac1N\sum_{j\ne i}K(X_i-X_j)\,dt+\sqrt{2\nu}\,dW_i.
 \tag{1.2}
\]

They start from independent unit Haar points, independently of the independent Brownian drivers. The reference density is one. The test is the actual homogeneous Fourier backward solution from THM-025. The pair kernel \(\Phi\) is the genuine symmetric terminal-zero full inverse with source
\(J_t(x,y)=K(x-y)\cdot(\nabla f_t(x)-\nabla f_t(y))\) and both exact response slots. Define

\[
 p=s+2,\quad a=s/p,\quad \theta=1-s/d,\quad
 \beta=1/\nu,\quad b_N=\min(\beta,1),\quad \sigma_N^2=Nb_N
 \tag{1.3}
\]

for positive \(\nu\). Use the R7 weights \(w_\alpha=w_1^\alpha\), where \(w_1\ge1\), \(w_1=r^{-1}\) on a fixed embedded ball, and \(w_1=1\) outside a slightly larger ball. All constants below may depend on \(d,s,T,\nu_*,h\) and these fixed kernel/weight choices, and on a displayed weight exponent, but never on \(N\) or the selected \(\nu\).

The first frozen conclusion is, for every fixed

\[
 1<q<\min(d-2,d/2),\qquad q\le s+1,\qquad
 \eta=s+1-q\in[0,2),
\]

\[
 \sup_{0\le t\le T}\sup_{x\ne y}
 \frac{|\nabla_{x,y}\Phi_t(x,y)|}{w_q(x-y)}
 \le C_q\min\{N^{\eta/p},\nu^{-\eta/2}\}.
 \tag{1.4}
\]

The literal statistic is

\[
 P_N[\Phi]=\frac1{2N^2}\sum_{i\ne j}\Phi(X_i,X_j)
       -\frac1N\sum_i\int\Phi(X_i,y)\,dy
       +\frac12\int\Phi(x,y)\,dx\,dy.
 \tag{1.5}
\]

With its actual martingale \(M_2\), let

\[
 Q_N=\sigma_N^2\mathbb E\langle M_2\rangle_T
     =2\nu Nb_N\mathbb E\int_0^T\sum_i
                 |\nabla_iP_N[\Phi_t](X_t)|^2dt.
 \tag{1.6}
\]

We reconstruct both

\[
 Q_N\le C b_N\min\{N^a,\nu^{-s/2}\}
                    (N^{-\theta}+\nu)
 \tag{1.7}
\]

and the full uniform conclusion

\[
 \sup_{0\le\nu\le\nu_*}Q_N\longrightarrow0,
 \tag{1.8}
\]

where \(Q_N=0\) is defined directly from the noise coefficient at \(\nu=0\). In fact the following stipulated bound is obtained:

\[
 Q_N\le C\left[
 N^{a-\theta}+N^{-(2-s)/(12p^2)}
 +N^{-s/(4p(s+4))}+N^{-1/(2p)}+N^{-2/p}\right].
 \tag{1.9}
\]

The leading scaled martingale has a deterministic uniform bracket bound, and the expected integral of the absolute scaled cross-variation tends uniformly to zero.

The exact negation is an admitted fixed tuple and a sequence \(N\to\infty\), \(\nu_N\in[0,\nu_*]\), violating one of the uniform bounds or having positive limsup of \(Q_N\), or an admitted weighted estimate for which every \(N,\nu\)-independent constant fails. None of the admitted conditions is replaced below.

## 2. Source and normalization preflight

Every source in this table is in the verified input manifest. The cited earlier results are conditional premises as issued, irrespective of any status language inside their old cards or reports. No unseen audit status, external literature statement, private source, or novelty claim is used.

| Source | Exact input and boundary |
|---|---|
| R1 model; `ROUND_001_ALGEBRA.md`, §§1, 2, 5 | Haar mass, Fourier convention, independent noise coefficient, ordered deleted labels, denominator \(N^2\), factor \(1/2\), and mean-field centering. The gradient and law contractions are also derived afresh in §6. |
| THM-021 and `ROUND_004_SINGULAR_RESPONSE.md`, §§2–4 | Coefficient-one local expansion, \(K\in L^1\), the finite compensated measure \(D=\operatorname{div}K\), and both response convolutions. The local premise comes from the complete proof, not the short card alone. |
| THM-023 and `ROUND_005_PERIODIC_PAIR_POTENTIAL.md`, §§4–6 | The noncolliding auxiliary pair evolution, bounded absolute-source potential for each fixed \(N\), and its pointwise true-martingale source class. |
| THM-024/025, both R5 full-inverse/interface memoranda, and the two R5 addenda | The bounded Borel Volterra inverse with both responses; actual homogeneous Fourier data; off-diagonal representative consistency. Symmetry means pair exchange, not self-adjointness of the base evolution. Divergence constants can be enlarged to a common bound as the addendum specifies. |
| THM-027 and `ROUND_007_WEIGHTED_PAIR_GRADIENT.md`, §§2–8 | The exact weights and one-sided Jacobian bound; fixed-\(N\) expectation differentiation and nearby-start justification; finite-measure weighted response differentiation. The large high-moment constants are used only for fixed-\(N\) validity, never as uniform estimates. |
| THM-026 and `ROUND_006_SINGULAR_PARTICLE_REALIZATION.md`, §§3–5, 7–8 | The actual noncolliding particle paths, legitimate compact energy stops, finite-\(N\) density/domain passage, and independent initial-data integration. Its exponential density estimate is not used as a uniform law bridge. |
| THM-028 and `ROUND_008_HOMOGENEOUS_PARTICLE_DOMAIN.md`, §§8–11 | Genuine corrector identification in the finite-particle Itô domain, background differentiation and singular square-integrable martingale passage. The full domain premise remains conditional. |
| THM-029 and `ROUND_009_HAAR_NOISE_ENERGY.md`, §§2–5 | The integrated Haar energy, conditional on the complete domain premise. It enters through the issued R10 clipping theorem only. No stronger timewise statement or audit addendum is imported. |
| THM-030 and `ROUND_010_ACTUAL_NOISE_LAW_TRANSFER.md`, §§2–7 | Actual free energy and entropy transfer; the exact re-centered radial clipping bound and martingale triangle inequality. This is an actual-law clipping premise, with all four contractions retained. |
| THM-031 and `ROUND_010_ACTUAL_LAW_FALSIFICATION.md`, §§2–3 | Actual symmetries and the sharp deterministic energy floor \(\mathcal H_N\ge-CN^{s/d}\), with the exact smooth self-diagonal subtraction. Its smoothing or initial-covariance conclusions are not used to infer the singular claim. |

For clarity, the heat normalization underlying these inputs is

\[
 g(z)=A\int_0^\infty t^{(d-s)/2-1}(p_t(z)-1)dt,
 \quad A=\frac{4^{(d-s)/2}\pi^{d/2}}{\Gamma(s/2)},
 \quad \widehat p_t(k)=e^{-4\pi^2t|k|^2}.
 \tag{2.1}
\]

Taking the gamma integral gives (1.1). Replacing \(p_t\) by the Euclidean Gaussian and setting \(v=|z|^2/(4t)\) gives exactly \(|z|^{-s}\), with coefficient one. The other lattice translates yield a smooth even local remainder. Hence on a fixed small ball

\[
 g(z)=r^{-s}+h_s(z),\qquad K(z)=s r^{-p}z+k(z),
 \quad k=-\nabla h_s,\quad k(0)=0.
 \tag{2.2}
\]

Because \(d\ge4\) and \(s<2\), we have \(p<d\) and \(s<d-2\) strictly. Thus in this report

\[
 D=s(d-p)g_p(z)\,dz,
 \quad \widehat D(k)=4\pi^2c_{d,s}|k|^{p-d}\ (k\ne0),
 \quad \widehat D(0)=0.
 \tag{2.3}
\]

The identity \(4\pi^2c_{d,s}/c_{d,p}=s(d-p)\) is the gamma recurrence. The measure is signed and includes its full torus compensation; it is not replaced by a globally positive local power. In particular \(D\in L^1\) and has no atom in the admitted range.

At homogeneous density the responses are exactly

\[
 R_xF(x,y)=-\int F(x+w,y)D(w)dw,\qquad
 R_yF(x,y)=-\int F(x,y+w)D(w)dw.
 \tag{2.4}
\]

Their sum has sup norm at most \(2\|D\|_1\), and its pair-Fourier multiplier is
\(-[\widehat D(k)+\widehat D(l)]\). Both slots and the negative sign are retained. No singular measure is differentiated.

The one-body solution is

\[
 f_t(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)[4\pi^2\nu|k|^2+\widehat D(k)]}e^{2\pi i k\cdot x}.
 \tag{2.5}
\]

Rapid Fourier decay and multipliers of modulus at most one give every fixed spatial derivative bound uniformly in \(N,t,\nu\). The differentiated commutator consequently satisfies

\[
 |\nabla_{x,y}J_t(x,y)|\le C_J w_{s+1}(x-y).
 \tag{2.6}
\]

For example the first-slot derivative is
\(DK(z)^T(\nabla f(x)-\nabla f(y))+D^2f(x)K(z)\); the other slot has the corresponding negative terms. The local bound is \(C r^{-s-1}\). Its absolute Hessian coefficient is used here only for the source derivative, and is not substituted for the one-sided flow eigenvalue below.

## 3. Two simultaneous occupation controls for the auxiliary pair

Write \(\mathcal G=\nu\Delta_{x,y}+N^{-1}K(x-y)\cdot(\nabla_x-\nabla_y)\). Use exactly the R7 cutoff \(\chi\), equal to one on \(r\le R\), and the R7 weights. Set

\[
 H=\sup_{r\le2R}\|Dk\|,\qquad
 K_0=\sup_{r\ge R}|K|,\qquad K_1=\sup_{r\ge R}\|DK\|,
 \quad L_*=\max(H,K_1),
\]

\[
 \ell(z)=\frac{2s}{N}\chi(z)r^{-p}+\frac{2L_*}{N}.
 \tag{3.1}
\]

The first term is extended by zero outside the embedded chart. The full pair drift Jacobian has principal center eigenvalue zero, transverse relative eigenvalue \(2s r^{-p}/N\), and radial relative eigenvalue \(-2s(s+1)r^{-p}/N\). The remainder is bounded above by \(2H/N\) locally and by \(2K_1/N\) outside the inner ball. Consequently its largest symmetric eigenvalue is at most \(\ell\). The variational matrix \(\mathcal A_{t,u}\) along a noncolliding pair path satisfies

\[
 \|\mathcal A_{t,u}\|\le e^{I_u},\qquad
 I_u=\int_t^u\ell(Z_v)dv,
 \tag{3.2}
\]

where \(Z_v=(X_v,Y_v)\) here denotes the auxiliary pair, not a pair marginal of the actual \(N\)-particle system.

For an allowed \(q\), direct differentiation on \(r\le R\) gives

\[
 \frac{(\mathcal G+\ell)w_q}{w_q}
 \le -\frac{2s(q-1)}N r^{-p}
      -2\nu q(d-2-q)r^{-2}
      +\frac{2qH+2L_*}{N}.
 \tag{3.3}
\]

The diffusion coefficient is \(2\nu\), because both independent pair Laplacians act on the relative variable. Both displayed negative coefficients are strictly positive in magnitude: \(q>1\) and \(q<d-2\). This is the step which supplies two uniform controls without imposing any relation between \(N\) and \(\nu\).

For explicit uniform constants put

\[
 A_{q,1}=\sup_{r\ge R}|\nabla w_q|/w_q,\qquad
 A_{q,2}=\sup_{r\ge R}|\Delta w_q|/w_q,
\]

\[
 C_q^0=\max\{qH+L_*,\,
 2\nu_*A_{q,2}+K_0A_{q,1}+sR^{-p}+L_*,\,0\},
\]

\[
 c_{q,1}=2s(q-1)>0,\qquad c_{q,2}=2q(d-2-q)>0.
\]

All are independent of \(N,\nu\), and the full torus inequality is

\[
 (\mathcal G+\ell)w_q\le C_q^0w_q
 -\mathbf1_{r\le R}w_q
       \left(\frac{c_{q,1}}N r^{-p}+c_{q,2}\nu r^{-2}\right).
 \tag{3.4}
\]

Apply ordinary Itô before a shrinking collision-tube stop to
\(e^{I_u-C_q^0(u-t)}w_q(Z_u)\). The stopped stochastic integral is square integrable on its compact stopped domain. Keep the nonnegative terminal term and both nonnegative occupation terms. The conditional particle premise gives noncollision from each fixed off-diagonal start. Fatou for the terminal term and monotone convergence for the increasing occupation intervals give, for \(t\le u\le T\),

\[
 \mathbb E_{t,z}e^{I_u}w_q(Z_u)\le e^{C_q^0T}w_q(z),
\]

\[
 \mathbb E_{t,z}\int_t^T e^{I_u}w_q(Z_u)du
       \le T e^{C_q^0T}w_q(z),
 \tag{3.5}
\]

\[
 \mathbb E_{t,z}\int_t^T e^{I_u}w_q(Z_u)
      \mathbf1_{r_u\le R}r_u^{-p}du
       \le \frac{N}{c_{q,1}}e^{C_q^0T}w_q(z),
\]

\[
 \mathbb E_{t,z}\int_t^T e^{I_u}w_q(Z_u)
      \mathbf1_{r_u\le R}r_u^{-2}du
       \le \frac{1}{c_{q,2}\nu}e^{C_q^0T}w_q(z)
       \quad(\nu>0).
 \tag{3.6}
\]

No uniform integrability of the stopped singular weight is assumed. Its sign allows precisely the Fatou direction used here. The last bound is not interpreted by division at zero noise.

## 4. Identification and bound of the genuine derivative

The conditional R7 result supplies the legitimate identities

\[
 \nabla S_{t,u}F=\mathbb E_{t,z}[\mathcal A_{t,u}^T\nabla F(Z_u)],
 \quad
 \nabla U_t=\mathbb E_{t,z}\int_t^T
                   \mathcal A_{t,u}^T\nabla J_u(Z_u)du.
 \tag{4.1}
\]

These are pointwise off-diagonal derivatives, not just a formal derivative of a pathwise expression. The exact fixed-\(N\) prerequisite used in (4.1) is R7 §§3–5: for any moment order \(m>1\), choose \(\alpha>m\) with \(\alpha+p\ge m(s+1)\); the negative term \(-2s(\alpha-m)r^{-p}/N\) absorbs any positive \(r^{-2}\) coefficient at that fixed \(N\). Stopped occupation bounds then give locally uniform \(m\)-moments of the differentiated terminal/source functionals. The R7 nearby-start argument establishes common local flow neighborhoods, and its line-segment/Jensen argument makes the difference quotients uniformly integrable and identifies their expectations. Those auxiliary constants may grow badly with \(N\). We use them only to justify (4.1). The new quantitative bounds are (3.5)–(3.6), not those high-moment constants. Thus there is no unproved exchange of expectation and derivative and no inference of simultaneous completeness from pointwise noncollision alone.

For the source bound use the finite positive measure

\[
 d\mathfrak m_{t,z}(u,\omega)=e^{I_u}w_q(Z_u)\,du\,d\mathbb P_{t,z}(\omega).
\]

Its total mass and two moments are (3.5)–(3.6). On the inner ball, (2.6) divided by \(w_q\) is at most \(C r^{-\eta}\). Outside, it is bounded by a fixed constant. Hölder on this measure gives, when \(\eta>0\),

\[
 \int_{r\le R}r^{-\eta}\,d\mathfrak m
 \le\left(\int_{r\le R}r^{-p}d\mathfrak m\right)^{\eta/p}
       \mathfrak m(1)^{1-\eta/p}
 \le C_q N^{\eta/p}w_q(z),
 \tag{4.2}
\]

\[
 \int_{r\le R}r^{-\eta}\,d\mathfrak m
 \le\left(\int_{r\le R}r^{-2}d\mathfrak m\right)^{\eta/2}
       \mathfrak m(1)^{1-\eta/2}
 \le C_q\nu^{-\eta/2}w_q(z).
 \tag{4.3}
\]

The powers add to one, so the initial weight remains \(w_q(z)\), not a fractional power of it. The conditions are \(\eta<p\) and \(\eta<2\), both satisfied. For \(\eta=0\) the total mass alone suffices and both powers in the claimed minimum are one. The outside contribution is absorbed into the first estimate since \(N^{\eta/p}\ge1\), and into the second since \(1\le\max(1,\nu_*^{\eta/2})\nu^{-\eta/2}\). Together with (3.2) and (4.1), this proves

\[
 |U|_q:=\sup_{t,x\ne y}|\nabla U_t|/w_q
 \le C_q\min\{N^{\eta/p},\nu^{-\eta/2}\}.
 \tag{4.4}
\]

The first identity in (4.1) and (3.5) similarly give
\(|S_{t,u}F|_q\le e^{C_q^0(u-t)}|F|_q\).

We must restore both responses without paying the much larger undifferentiated inverse norm. For the homogeneous responses (2.4), their actual global weak derivatives are translations of \(\nabla F\), since weak differentiation commutes with translation and Fubini against the finite measure is legitimate. R7 §§6–7 give

\[
 \int |D(w)|w_q(z+w)dw\le C_{D,q}w_q(z),\qquad
 |(R_x+R_y)F|_q\le2C_{D,q}|F|_q.
 \tag{4.5}
\]

Here is the needed content of that convolution estimate. The singular part of \(|D|\) is bounded by a fixed multiple of \(r^{-p}\) with \(p<d\), plus a bounded remainder. Split the convolution into disjoint balls about \(w=0\) and \(w=-z\) of radius proportional to their separation and their complement. Near the second singularity the bound is \(C r^{d-p-q}\le C r^{-q}\); on the other pieces it is \(C r^{-q}\int|D|\). The bounded remainder uses \(\int w_q<\infty\). This works even when \(p+q\ge d\); it does not assert a bounded convolution. Continuity of the differentiated response off the diagonal follows by the same separated-singularity split, fixing the moving second singularity by translation. It identifies its continuous weak derivative with its classical derivative. There is no diagonal evaluation and no discarded compensation.

Crucially, (4.5) is a bound in the derivative seminorm alone. Homogeneity removes all derivatives of the background density. No term containing \(\|F\|_\infty\) is needed in this estimate.

Let \(V\) be the exact Volterra operator \((VF)_t=\int_t^T S_{t,u}(R_x+R_y)F_u\,du\). The genuine inverse is \(\Phi=\sum_{j\ge0}V^jU\). At each fixed \(N\) its values converge uniformly by the R5 bounded-response argument. Equations (4.4)–(4.5) give

\[
 |V^jU|_q\le C_q\min\{N^{\eta/p},\nu^{-\eta/2}\}
 e^{C_q^0T}\frac{(2C_{D,q}T)^j}{j!}.
 \tag{4.6}
\]

The propagator time intervals on a simplex add to at most \(T\); their exponential is not charged \(j\) times. Derivatives converge locally uniformly and in the weighted seminorm. Time integrals are differentiated using the local uniform bound and the line-segment fundamental theorem. The resulting derivative belongs to the same bounded Borel inverse by pointwise uniqueness. This proves (1.4) for the true full inverse, including \(t=T\) where both source potential and derivative vanish. No radial surrogate, truncated-response inverse, or merely weakly identified representative is substituted.

## 5. An actual-law occupation bound at the higher pair power

Use \(\mathcal H_N=N^{-1}\sum_{i<j}g(X_i-X_j)\) for the actual total potential, reserving \(Q_N\) for the noise. The R10 sharp floor is

\[
 \mathcal H_N\ge-C_F N^{s/d}.
 \tag{5.1}
\]

Its normalization can be seen directly from (2.1). Set \(\alpha=(d-s)/2\), truncate the heat integral below \(r\), and call the resulting smooth positive-Fourier kernel \(g^{>r}\). Then

\[
 \mathcal H_N\ge \frac N2\sum_{k\ne0}\widehat g^{>r}(k)|\widehat\eta_N(k)|^2
 -\frac12g^{>r}(0)-\frac{N-1}{2\alpha}Ar^\alpha.
 \tag{5.2}
\]

The diagonal subtraction is exactly \(g^{>r}(0)/2\). The heat kernel gives \(g^{>r}(0)\le Cr^{-s/2}\); choosing \(r=N^{-2/d}\) proves (5.1). This uses positive Fourier coefficients of a specified kernel, not positivity of an arbitrarily weighted interaction.

By the strictly positive local coefficient in (2.3) and the bounded periodic remainder, fixed constants \(c_D>0,C_D<\infty\) satisfy

\[
 D(z)\ge c_Dw_p(z)-C_D\qquad(z\ne0).
 \tag{5.3}
\]

The fact \(p<d\) also gives \(\int w_p<\infty\). At the Coulomb endpoint the coefficient in (5.3) would vanish; it is not used there.

The actual configuration drift is \(B=-\nabla\mathcal H_N\), and on collision-free configurations

\[
 \Delta_{Nd}\mathcal H_N=-\frac2N\sum_{i<j}D(X_i-X_j),
\]

\[
 L_N\mathcal H_N=-|B|^2-\frac{2\nu}N\sum_{i<j}D(X_i-X_j)
 \le-|B|^2-\frac{2c_D\nu}N\sum_{i<j}w_p(X_i-X_j)
       +C_D\nu(N-1).
 \tag{5.4}
\]

This keeps the entire total-force square. No individual squared pair force is extracted from it.

To justify the expectation, use precisely the compact energy stops of R6 §4, with stop zero if the random initial state is already outside the sublevel. On a stopped compact set the stochastic integral is square integrable, so its expectation is zero. The iid initial mean is \(\mathbb E\mathcal H_N(X_0)=0\), finite because \(g\in L^1\). The initial energy above the stop is integrable and the integrand there is zero. Apply (5.4), use the deterministic floor (5.1) at the stopped endpoint, and discard only the complete nonnegative force square. This yields

\[
 \frac{2c_D\nu}N\sum_{i<j}
 \mathbb E\int_0^{T\wedge\tau_m}w_p(X_i-X_j)dt
 \le C_FN^{s/d}+C_D\nu(N-1)T.
 \tag{5.5}
\]

The noncollision premise makes \(\tau_m\uparrow\infty\) on each fixed finite horizon almost surely. Monotone convergence removes the increasing stops from the nonnegative integrals. No global singular Fisher-information identity, boundary integration across collisions, or uniform integrability of stopped energy is invoked.

Permutation equivariance, common translation equivariance, and pathwise uniqueness preserve exchangeability and one-body Haar marginals of the actual law. Thus (5.5), with the exact number \(N(N-1)/2\) of unordered pairs, gives

\[
 \boxed{\quad
 \nu\int_0^T\mathbb E w_p(X_1-X_2)dt
 \le C(N^{-\theta}+\nu).
 \quad}
 \tag{5.6}
\]

Indeed \(N^{s/d}/(N-1)\le2N^{-\theta}\). This is an estimate for the actual interacting law. A positive-time product law is never asserted. All singular expectations used subsequently are controlled by (5.6) and the finite Haar \(w_p\) moment.

## 6. Every physical and deleted-label factor in the noise

Let \(G_t=\nabla_x\Phi_t\), \(A_t(x)=\int G_t(x,y)dy\), and \(H_t=G_t-A_t\). The finite-\(N\) domain premise justifies differentiation of the background projection. Direct differentiation of the two orientations in (1.5) cancels the factor \(1/2\), giving exactly

\[
 v_i=\nabla_iP_N[\Phi]
 =\frac1{N^2}\sum_{j\ne i}G(X_i,X_j)-\frac1NA(X_i)
 =\frac1{N^2}\left[\sum_{j\ne i}H(X_i,X_j)-A(X_i)\right].
 \tag{6.1}
\]

The final missing-self term is \(-A/N^2\); it is not dropped. Exchangeability and expansion of the square give

\[
 Q_N=\frac{2\nu b_N}{N^2}\int_0^T\left[
 (N-1)\mathbb E|H_{12}|^2
 +(N-1)(N-2)\mathbb EH_{12}\cdot H_{13}
 -2(N-1)\mathbb EH_{12}\cdot A_1
 +\|A\|_2^2\right]dt.
 \tag{6.2}
\]

For \(N=2\), the triple term is absent and no third random variable is introduced. The Haar equality of the last term uses only one-body invariance. The other marginals are the actual interacting marginals.

For estimates it is useful to keep all contractions together in a nonnegative expression. For any measurable vector field \(F(x,y)\), define its own row \(A_F\) and its configuration field by the first expression in (6.1), with \(G\) replaced by \(F\). This is a noise integrand, whether or not it is a potential gradient. Finite-sum Cauchy–Schwarz and one-body Haar invariance give

\[
 \mathbb E\sum_i|v_i[F]|^2
 \le\frac{2(N-1)^2}{N^3}\mathbb E|F(X_1,X_2)|^2
       +\frac2N\|A_F\|_2^2.
\]

Multiplication by exactly \(2\nu Nb_N\), followed by Haar Jensen for the row, yields

\[
 Q_N[F]\le4\nu b_N\int_0^T
 \left[\frac{(N-1)^2}{N^2}\mathbb E|F(X_1,X_2)|^2
                            +\|F\|_{L^2(dxdy)}^2\right]dt.
 \tag{6.3}
\]

This does not discard a signed triple term individually, assume its sign, or substitute an iid law.

Choose \(q=p/2=1+s/2\). It is strictly between one and \(\min(d-2,d/2)\) because \(d\ge4,s<2\), and it satisfies \(q\le s+1\). Its \(\eta=s/2\). The proved derivative estimate gives

\[
 |G_t(x,y)|^2\le C\min\{N^a,\nu^{-s/2}\}w_p(x-y).
 \tag{6.4}
\]

Apply (6.3), (5.6), and \(\int w_p<\infty\). This proves precisely (1.7). The original finite-\(N\) singular Itô/martingale premise identifies this functional with the genuine corrector bracket. The resulting integrability also directly justifies the particular bracket and tail expectations estimated here. Neither a heat-regularized corrector bracket nor a reference-law functional has been substituted.

## 7. Closing the entire bounded-diffusivity interval

Bound (1.7) alone has a nonvanishing upper bound when \(\nu\) stays positive. That is a limitation of that bound, not a counterexample. The full conclusion requires the issued R10 clipping theorem and a second, strictly smaller derivative weight.

For \(L>0\), let \(G^L\) be radial clipping at magnitude \(L\), and set \(F^{>L}=G-G^L\). Re-center each field using its own row. Write \(Q_N^L=Q_N[G^L]\) and \(\mathcal T_N(L)=Q_N[F^{>L}]\). The issued conditional THM-030 estimate is

\[
 Q_N^L\le C_E b_NN^{-2/p}
          +C_*b_N\sqrt\nu\,L^2N^{-1/p}.
 \tag{7.1}
\]

It follows from the actual entropy comparison with bounded clipped two-/three-body tests, with all four terms of (6.2). Its Haar input is the integrated R9 energy only. Since \(b_N\sqrt\nu\le1\), the choice

\[
 L_N=N^{1/(4p)}
 \tag{7.2}
\]

gives
\(Q_N^{L_N}\le C(N^{-2/p}+N^{-1/(2p)})\), uniformly on the whole admitted noise interval. The triangle inequality for the actual predictable noise integrands gives

\[
 \sqrt{Q_N}\le\sqrt{Q_N^{L_N}}+\sqrt{\mathcal T_N(L_N)},
 \quad Q_N\le2Q_N^{L_N}+2\mathcal T_N(L_N).
 \tag{7.3}
\]

No orthogonality between the clipped and tail fields is asserted.

For the tail choose instead

\[
 q_0=1+s/4=(s+4)/4,\qquad
 \eta_0=3s/4,\qquad
 \gamma=\frac{p-2q_0}{q_0}=\frac{2s}{s+4}>0.
 \tag{7.4}
\]

Again \(q_0\) satisfies every frozen restriction, and \(2q_0<p<d\). Estimate (1.4) supplies \(|G|\le A_\nu w_{q_0}\), where \(A_\nu=C\nu^{-\eta_0/2}\). The exact multiplicative weights imply the pointwise tail estimate

\[
 |F^{>L}|^2\le A_\nu^2w_{2q_0}
               \mathbf1_{w_{q_0}>L/A_\nu}
 \le A_\nu^{p/q_0}L^{-\gamma}w_p.
 \tag{7.5}
\]

This uses \(2+\gamma=p/q_0\). It is valid globally for every \(L>0\), even if \(L/A_\nu<1\); no unstated large-threshold assumption is needed. If \(A_\nu=0\), the tail is identically zero and the estimate is interpreted directly. Applying (6.3) and (5.6) to this tail gives

\[
 \mathcal T_N(L)\le C b_N
 \nu^{-\eta_0p/(2q_0)}L^{-\gamma}(N^{-\theta}+\nu).
 \tag{7.6}
\]

This step supplies the actual singular uniform integrability that the earlier clipping theorem alone left open. It uses an integrable higher pair-power occupation, not an expectation of the original energy promoted into concentration.

Now choose the deterministic split exponent

\[
 \delta=\frac1{6p^2}.
 \tag{7.7}
\]

For \(0<\nu\le N^{-\delta}\), apply (1.7), using the two sides of the minimum separately:

\[
 Q_N\le C\left[N^{a-\theta}+\nu^{1-s/2}\right]
 \le C\left[N^{a-\theta}+N^{-(2-s)/(12p^2)}\right].
 \tag{7.8}
\]

For \(N^{-\delta}\le\nu\le\nu_*\), use (7.6), \(b_N\le1\), \(N^{-\theta}+\nu\le1+\nu_*\), and (7.2). The exponent is exactly

\[
 \frac{\delta\eta_0p}{2q_0}-\frac{\gamma}{4p}
 =\frac{s}{4p(s+4)}-\frac{s}{2p(s+4)}
 =-\frac{s}{4p(s+4)}.
 \tag{7.9}
\]

Consequently

\[
 \mathcal T_N(L_N)\le C N^{-s/(4p(s+4))},
 \quad
 Q_N\le C\left[N^{-s/(4p(s+4))}+N^{-1/(2p)}+N^{-2/p}\right]
 \tag{7.10}
\]

on that entire second interval. The two intervals exhaust every positive admitted diffusivity for each \(N\), including the moving dividing value. Either interval may be empty when \(\nu_*\) is small. At zero diffusivity the noise vanishes by definition. Combining (7.8) and (7.10) proves exactly (1.9).

Every exponent is strictly negative where required. In particular

\[
 a-\theta=\frac{s^2+2s-2d}{d(s+2)}<0,
\]

since \(s^2+2s<8\le2d\). The remaining decay exponents in (1.9) are strictly positive because \(0<s<2\). This proves the supremum in (1.8), rather than merely a conclusion along a preselected noise subfamily.

## 8. Leading bracket, absolute cross-variation, and endpoints

The leading one-body martingale is

\[
 dM_1=\frac{\sqrt{2\nu}}N\sum_i\nabla f_t(X_i)\cdot dW_i.
\]

Let \(F_h=\sup_{t,\nu}\|\nabla f_t\|_\infty<\infty\). Its scaled bracket obeys the pathwise deterministic bound

\[
 \sigma_N^2\langle M_1\rangle_T
 =2\nu b_N\int_0^T\frac1N\sum_i|\nabla f_t(X_i)|^2dt
 \le2TF_h^2,
 \tag{8.1}
\]

because \(\nu b_N\le1\). The physical scaled cross-variation density is exactly
\(2\nu Nb_N\sum_i v_i\cdot\nabla f_t(X_i)/N\). Pointwise Cauchy–Schwarz in the particle vector, followed by Cauchy–Schwarz in probability and time, yields

\[
 \mathbb E\int_0^T
 \left|\sigma_N^2\frac{d\langle M_1,M_2\rangle_t}{dt}\right|dt
 \le (2TF_h^2 Q_N)^{1/2}\longrightarrow0
 \tag{8.2}
\]

uniformly in \(\nu\). This bounds the integral of the absolute density, not merely the absolute value of the integrated signed cross-variation.

If \(h\) is constant, (2.5) is constant, \(J=0\), and bounded inverse uniqueness gives \(\Phi=0\). If \(T=0\), all potentials and integrated noises vanish. At \(\nu=0\), noise functionals are zero directly; neither a finite reciprocal temperature nor division by \(\nu\) is used. All finite-label identities include \(N=2\), with its triple term absent. The endpoints \(q=s+1\) and \(\eta=0\) were treated by the total-mass estimate. The strict conditions on \(q,d,s\) are retained.

## 9. Independent falsification route and exact diagnostics

The analytic construction was challenged by an independent coefficient/endpoint route. The fresh supporting checker uses only Python standard-library exact rational arithmetic and was written in this isolated worktree without reading any previous program or result. Its source and result are in `ROUND_013_NOISE_BLIND_ARTIFACTS/`. The executed result is **PASS, 2,513 exact assertions**. This is supporting self-check evidence for this reconstruction, not independent certification of its analytic proof.

The checker differentiates a literal ordered-pair Fourier statistic and applies a literal finite-particle Fourier generator, independently of the compact formulas (6.1)–(6.2). It compares its carré-du-champ with the physical \(2\nu\) gradient square, checks both actual-label and background contractions under Haar and an explicitly positive exchangeable nonproduct Fourier density, tests the two homogeneous response slots and their compensation, and recomputes the radial Jacobian and Laplacian coefficients from matrices. The diagnostic density is used solely to challenge finite-label algebra; it is not represented as the actual interacting law or used to prove its asymptotic estimate.

The normalized Fourier derivative is \(D_j=(2\pi i)^{-1}\partial_j\). The physical gradient square is \(-(2\pi)^2\sum_j(D_jP)^2\), and the physical generator is \((2\pi)^2\) times the checker generator. All compensating signs are explicit in the program. The symbolic rational probes are embedded in one coordinate of the admitted torus; they do not replace the Riesz dynamics. No random seed, floating-point tolerance, empirical fit, or numerical law inference is involved.

The exact endpoint tests deliberately detect the failure of the relevant mechanism outside the frozen range: positive diffusion coefficient when \(d=3,q>1\), vanishing diffusion occupation coefficient at \(q=d-2\), vanishing repulsive coefficient at \(q=1\), loss of the local \(w_p\) occupation at Coulomb, and vanishing low-noise decay exponent when \(s=2\). They do not claim counterexamples to every possible theorem at those endpoints. These diagnostics support the displayed algebra; the proof is §§2–8 and the expressly conditional source modules.

| Adversarial question | Exact resolution |
|---|---|
| Does a pathwise variational equation alone identify an expectation derivative? | No. The fixed-\(N\) R7 UI/nearby-start prerequisite is explicit in §4; its large constants do not enter the uniform estimates. |
| Is the source estimate for a radial model rather than the full inverse? | The source is the actual commutator; derivative-seminorm Volterra summation restores both finite-measure responses and invokes pointwise inverse uniqueness. |
| Does the value norm of the inverse spoil the improved exponent? | Homogeneity makes (4.5) a pure derivative-seminorm bound. No \(N^a\) value norm is charged to the derivative series. |
| Are the negative diffusion and repulsion terms allowed simultaneously? | Both are retained in one stopped nonnegative inequality (3.4), with exact coefficients; no relation between \(N\) and \(\nu\) is assumed. |
| Is an actual marginal silently replaced by product Haar? | No. (5.6) is an actual stopped-energy occupation estimate; (6.3) uses only exchangeability and one-body Haar invariance. |
| Does (1.7) alone prove the full bounded-noise claim? | No. §7 identifies its limitation at positive diffusivity and supplies the separate clipping/tail argument covering the remaining interval. |
| Is tail uniformity deduced from a mean-energy bound alone? | No. The strict gap \(2q_0<p\), the improved derivative constant, and the actual higher-power occupation yield (7.5)–(7.6). |
| Are stopping expectations or a pair-force square assumed finite? | Compact stopped Itô and the sharp deterministic energy floor imply (5.5); monotone convergence supplies the occupation. The total-force square is kept whole. |
| Is a missing-self or triple term lost? | (6.1)–(6.2) retain all four contractions; the fresh literal Fourier checker challenges them, including \(N=2\). |
| Does the result prove a fluctuation law? | No. It proves the specified noise and cross-variation conclusions only; cubic residual, centering limit, and higher hierarchy remain outside this assertion. |

## 10. Verdict and recoverable handoff

The exact conditional frozen THM-034 is reconstructed in full. There is no newly unsupported line in that conditional implication. The indispensable old premises remain the finite-\(N\) singular particle/inverse/domain modules and the issued R10 clipping theorem with its integrated R9 energy input. If an earlier premise fails, this report does not replace or certify it. In particular no unseen current R8–R13 audit status is an input to this verdict.

This report establishes only the admitted homogeneous, bounded-diffusivity, \(d\ge4\), \(0<s<2\) noise range. It asserts no \(d=3\) extension, Coulomb case, \(s=2\) endpoint, unbounded diffusivity, general background, logarithmic interaction, cubic residual estimate, higher hierarchy closure, or fluctuation law. The old energy-floor condition, full microscopic subcritical condition, and positive finite critical condition retain their distinct powers and meanings. No scientific mission or centering convention is altered.

The unique auxiliary directory contains the fresh checker/result, exposure and README records, verified input/output manifests, and an archive containing precisely the allowed inputs and this output packet. The archive and output manifest are sealed separately and verified member by member. The issued bytes are immutable; any later correction must be a new, separately named report. No canonical state, historical inputs, commits, pushes, dependencies, or other worktrees were changed. Root alone may compare this sealed reconstruction with a candidate and decide promotion.
