# Round 011 rescaled-gradient statement-only reconstruction

TASK-068 / THM-032. Issued 2026-09-18 UTC.

**Verdict: every frozen analytic assertion is reconstructed, conditional on the existing singular base-process and bounded-full-inverse inputs in their issued scopes. No new failed line within THM-032 was found.** This is a fresh statement-only reconstruction, not a review of the withheld candidate. Root comparison and a separate hostile review remain necessary. Supporting exact computations below are same-context self-checks, not independent certification.

Worktree: /Users/matthewrosenzweig/.codex/worktrees/hocf-r011-gradient-blind. Branch: codex/hocf-r011-gradient-blind. Base: published R9 commit 29d7ce427ad7a98739b18d07781e71c4598b3579. Exactly the twenty-one permitted inputs were copied from the root and byte-hash verified before their mathematical use. The manifest and verification record accompany this report under ROUND_011_GRADIENT_BLIND_ARTIFACTS. Inherited non-allowlisted files were not read.

## 1. Isolation, assertion, and source status

The first two files read were TASKS/ACTIVE/TASK-068_ROUND011_RESCALED_GRADIENT_BLIND.md and AUDITS/ROUND_011_RESCALED_GRADIENT_BLIND_INPUT_SHA256SUMS.txt. The complete R11 candidate, construction seed, R10/R12 current proofs, current root audits/state/history, memory files, and previous checkers were withheld and were not read. Ambient exposure consisted of the supplied global/app instructions, repository instructions, the generic memory summary already embedded by the platform, and the parent's assignment identifying the assertion and output requirements. The generic summary mentioned a higher-corrector campaign but contained no R11 proof. The worktree-creation command printed the published R9 commit subject; this was not mathematical evidence. No memory lookup, external source lookup, children, installation, commit, push, canonical edit, or candidate exposure was used.

The applicable isolated task supersedes general orientation instructions to read README_FIRST, the full specification, MODEL_ORCHESTRATION, and canonical ledgers. Those non-allowlisted files were not opened. No premise is assigned a current independent-audit status from an unseen ledger. In particular the prior theorem cards and memoranda retain their issued qualifications; statements in an allowed source that refer to unavailable audit histories are not a substitute for those audits.

Fix integer \(d\ge3\), \(0<s\le d-2\), \(0\le T<\infty\), \(0\le L<\infty\), and a smooth real terminal function \(h\) on the unit Haar torus. For each \(N\ge2\) and
\[
 0\le\nu\le L N^{-2/(s+2)}
 \tag{1.1}
\]
use the frozen kernel, homogeneous reference, actual backward test, and existing bounded full inverse in THM-032. All constants asserted uniform below may depend on \(d,s,T,L,h\), the frozen periodic kernel, and the fixed weights, but not on \(N,\nu,t\).

The assertion is the uniform weighted value/first-gradient bound, joint off-diagonal value/first-derivative continuity, global weak \(W^{1,1}\) identification, continuous bounded differentiated contractions, the specified response-only solution, and convergence to it uniformly in \(t,\nu\) in every compact off-diagonal \(C^1\) norm and global Haar \(W^{1,1}\). Its exact negation is an admissible fixed datum and parameter sequence violating any one of those assertions, including their endpoints or representatives. Sections 3–11 exclude that negation, subject to the issued base/full-inverse premises.

The source preflight uses these complete allowed proofs.

| Input | Precisely used fact | Qualification retained |
|---|---|---|
| R1 algebra, Section 3, and frozen model | Unit Haar, Fourier characters \(e^{2\pi i k\cdot x}\), internal coefficient \(1/N\), and both response coefficients one | Smooth algebra fixes conventions; it is not a singular limit theorem. |
| R4 singular-response memorandum, Sections 2–4 | Coefficient-one local Riesz singularity, smooth even remainder, \(K\in L^1\), exact finite signed measure \(D\), compensated response | Complete proof, rather than the short card, supplies the local kernel premise. |
| R5 periodic-pair memorandum, Sections 2–6 | Per-start noncollision, measurable Markov evolution, absolute source potential bounded for fixed \(N\) | Its bound may grow with \(N\); source-potential heat convergence is not imported. |
| R5 conditional inverse and interface memoranda | Exact Borel Volterra inverse and actual homogeneous Fourier test | The inverse implication retains its explicit prerequisite assumptions. |
| R5 source/constant addendum and symmetry clarification | Common lower-divergence constant; exchange equivariance | Neither self-adjointness nor unavailable subsequent acceptance is inferred. |
| R7 and R8 complete memoranda | Earlier arguments and their explicitly \(N\)-dependent constants were inspected | No \(N\)-uniform conclusion is imported under THM-027/028. The estimates and limiting argument below are reconstructed. |
| THM-026 and the R6 realization memorandum | Scope of the actual-particle law bound, for the exclusion in Section 13 | This proof uses no actual-particle density or bracket estimate. |

All twenty-one input files were read as bytes for sealing. Mathematical inspection included all theorem cards, the frozen model, the two clarification files, the R5 inverse/interface proofs, the full R7/R8 proofs, relevant R4/R5 complete source arguments, and the R1 coefficient and R6 law-scope passages. This is not a claim to have independently re-audited all results contained in all twenty-one files.

## 2. Frozen operators, actual source, and weighted spaces

Set \(p=s+2\), \(E=\{(x,y)\in(\mathbb T^d)^2:x\ne y\}\), \(z=x-y\). The exact Fourier normalization is
\[
 \widehat g(0)=0,\qquad
 \widehat g(k)=c_{d,s}|k|^{s-d},\quad
 c_{d,s}=\pi^{s-d/2}\frac{\Gamma((d-s)/2)}{\Gamma(s/2)},\qquad K=-\nabla g.
\]
The R4 heat integral gives \(g(z)=|z|^{-s}+q(z)\) with \(q\) smooth and even on an embedded ball. Its Euclidean heat integral has coefficient one. The gamma recurrence gives
\[
 D:=\operatorname{div}K=
 \begin{cases}
 s(d-2-s)g_{s+2}(z)\,dz,&s<d-2,\\
 c_d(\delta_0-dz),&s=d-2,
 \end{cases}
 \qquad c_d=(d-2)|\mathbb S^{d-1}|.
 \tag{2.1}
\]
Indeed \(4\pi^2c_{d,s}/c_{d,s+2}=s(d-2-s)\) below the endpoint and \(4\pi^2c_{d,d-2}=c_d\). The total mass of \(D\) is zero. At Coulomb its total variation is \(2c_d\). These are the full compensated periodic distributions.

The homogeneous pair generator and responses are
\[
 G_{N,\nu}=\nu(\Delta_x+\Delta_y)
  +F_N\cdot\nabla_{x,y},\qquad
 F_N=N^{-1}(K(z),-K(z)),
\]
\[
 R_x v(x,y)=-\int v(x+w,y)D(dw),\qquad
 R_y v(x,y)=-\int v(x,y+w)D(dw),\qquad R=R_x+R_y.
 \tag{2.2}
\]
Each response has coefficient one. The Coulomb atom multiplies \(v(x,y)\); it does not sample \(v(x,x)\). These formulas make sense pointwise off the diagonal for the weighted classes proved below, independently of diagonal assignments.

For \(k\ne0\) put \(b_k=4\pi^2c_{d,s}|k|^{s+2-d}\). The actual test and source are
\[
 f_t^\nu(x)=\widehat h(0)+\sum_{k\ne0}\widehat h(k)
 e^{-(T-t)(4\pi^2\nu|k|^2+b_k)}e^{2\pi i k\cdot x},
 \qquad J_t^\nu=K(z)\cdot(\nabla f_t^\nu(x)-\nabla f_t^\nu(y)).
 \tag{2.3}
\]
The one-body response has multiplier \(-b_k\), so the backward sign is as in THM-025. Rapid Fourier decay proves every spatial bound uniformly for \(t\in[0,T]\), \(\nu\ge0\). On a bounded diffusivity interval the corresponding time derivatives also have all required uniform spatial bounds.

Choose \(R_0=1/16\), a smooth cutoff \(\chi\) equal to one for \(r\le R_0\), zero for \(r\ge2R_0\), and valued in \([0,1]\). All powers and derivatives of distance below are inside this embedded chart. Define
\[
 w_\alpha(z)=\exp\{\alpha\chi(z)\log(1/|z|)\}
\]
inside the chart and one outside. These weights satisfy \(w_\alpha\ge1\), \(w_\alpha^b=w_{b\alpha}\), and are exactly \(r^{-\alpha}\) near zero. Every fixed weight allowed in THM-032 is equivalent to this choice, with constants depending only on the fixed weights.

Let
\[
 Y_s=\{v:E\to\mathbb R\text{ Borel}:\|v\|_{Y_s}:=\sup_E|v|/w_s<\infty\},
\]
\[
 X=\{v\in C^1(E):\|v\|_X:=
       \sup_E|v|/w_s+\sup_E|\nabla_{x,y}v|/w_{s+1}<\infty\}.
 \tag{2.4}
\]
These are actual-function spaces, not Haar equivalence classes. They are Banach spaces: weighted uniform Cauchy convergence gives the value, and in \(X\) local uniform convergence of values and derivatives identifies a \(C^1\) limit by the segment fundamental theorem. \(Y_s\) need not be separable, and no strong continuity of the particle semigroup on all of \(Y_s\) or \(X\) is assumed.

The source satisfies
\[
 \sup_{t,\nu}\|J_t^\nu\|_X\le C_J<\infty.
 \tag{2.5}
\]
For specificity, if \(H=\sup_{B_{2R_0}}\|D(-\nabla q)\|\), \(K_j=\sup_{r\ge R_0}\|D^jK\|\), and \(M_j=\sup_{t,\nu}\|D^j f_t^\nu\|_\infty\), sufficient value and gradient constants are
\[
 J_0=\max\{M_2(s+H R_0^{s+2}),\,2M_1K_0\},
\]
\[
 J_1=\max\{\sqrt2M_2[s(s+2)+2H R_0^{s+2}],\,
                  \sqrt2(2M_1K_1+M_2K_0)\},\qquad C_J=J_0+J_1.
 \tag{2.6}
\]
Here
\[
 \nabla_xJ=DK(z)^T(\nabla f(x)-\nabla f(y))+D^2f(x)K(z)
\]
and the analogous \(y\) derivative has both signs reversed. The principal \(DK\) has absolute norm \(s(s+1)r^{-p}\) in this source calculation.

Termwise Fourier comparison using \(1-e^{-a}\le a\) proves, for every spatial order \(m\),
\[
 \sup_t\|f_t^\nu-f_t^0\|_{C^m}
 \le 4\pi^2T\nu
 \sum_{k\ne0}(1+2\pi|k|)^m|k|^2|\widehat h(k)|.
\]
Consequently \(J^\nu\to J^0\) in \(C([0,T];X)\), uniformly at rate \(O(\nu)\). Each source is continuously differentiable in time in \(X\). The time derivative statement uses a bounded diffusivity interval, available from (1.1).

## 3. Uniform radial barriers with every \(N,\nu\) factor exposed

Write \(K(z)=s r^{-p}z+k(z)\) near zero. Evenness gives \(k(0)=0\), \(|k(z)|\le Hr\). Let
\[
 a_N=2s/N,\quad M=\max(H,K_1),\quad
 \ell_N(z)=a_N\chi(z)r^{-p}+2M/N .
\]
The exact pair Jacobian is
\[
 DF_N=N^{-1}
 \begin{pmatrix}DK&-DK\\-DK&DK\end{pmatrix}.
\]
Its principal center eigenvalues are zero, its transverse relative eigenvalue is \(a_Nr^{-p}\), and its radial relative eigenvalue is \(-(s+1)a_Nr^{-p}\). Hence
\[
 \lambda_{\max}(\operatorname{Sym}DF_N)\le\ell_N .
 \tag{3.1}
\]
The largest eigenvalue, rather than the absolute norm, is required here.

Fix \(m\ge0\) and \(\alpha>m\). On \(r\le R_0\), direct differentiation gives
\[
 \frac{(G_{N,\nu}+m\ell_N)w_\alpha}{w_\alpha}
 \le -A_N r^{-p}+B_\alpha\nu r^{-2}
        +2\alpha H/N+2mM/N,
 \quad
 A_N=2s(\alpha-m)/N,\quad
 B_\alpha=2\alpha(\alpha+2-d)_+ .
 \tag{3.2}
\]
The exact diffusion term before taking its positive part is
\(2\nu\alpha(\alpha+2-d)r^{-2}\). Both the diffusion and relative drift contain their factor two.

For \(B_\alpha>0\), elementary maximization gives
\[
 B_\alpha\nu u^2-\frac{A_N}{2}u^{s+2}
 \le
 \frac{s}{s+2}B_\alpha\nu
       \left(\frac{4B_\alpha\nu}{(s+2)A_N}\right)^{2/s}.
\]
The right side is exactly
\[
 Y_{\alpha,m}(\nu,N)
 =\frac{s}{p}B_\alpha
   \left(\frac{2B_\alpha}{sp(\alpha-m)}\right)^{2/s}
   \big(\nu N^{2/p}\big)^{p/s}
 \le \overline Y_{\alpha,m},
 \tag{3.3}
\]
where \(\overline Y_{\alpha,m}\) is the displayed coefficient times \(L^{p/s}\). Set it to zero when \(B_\alpha=0\) or \(L=0\). The maximizer obeys \(u^s=4B_\alpha\nu/(pA_N)\). This computation is the uniform step; no old constant depending on \(N\) has been renamed.

All annular terms can be bounded by the following fixed quantities:
\[
 Q_{\alpha,1}=\sup_{r\ge R_0}|\nabla_z w_\alpha|/w_\alpha,\qquad
 Q_{\alpha,2}=\sup_{r\ge R_0}|\Delta_z w_\alpha|/w_\alpha,
\]
\[
 C_{\alpha,m}^{\rm out}
 =2LQ_{\alpha,2}+K_0Q_{\alpha,1}
          +m(M+sR_0^{-p}),
\]
\[
 C_{\alpha,m}
 =\max\{\alpha H+mM+\overline Y_{\alpha,m},
                   C_{\alpha,m}^{\rm out},0\}.
 \tag{3.4}
\]
We used only \(\nu\le L\) and \(2/N\le1\). The full periodic generator therefore obeys
\[
 (G_{N,\nu}+m\ell_N)w_\alpha
 \le C_{\alpha,m}w_\alpha
       -\frac{A_N}{2}\mathbf1_{\{r\le R_0\}}r^{-\alpha-p}.
 \tag{3.5}
\]
Every \(C_{\alpha,m}\) is uniform in (1.1), even for arbitrarily large fixed \(\alpha,m\). The occupation coefficient \(A_N/2\) remains proportional to \(1/N\).

For completeness, the underlying per-start singular process is the issued R5 one. Its elementary noncollision construction first patches smooth cutoff integral equations and applies stopped Itô to \(1+\chi r^{-(d-2)}\). The principal diffusion is zero, the principal drift is negative, and the remainder is bounded by a constant times that function. The probability of hitting radius \(\epsilon\) before \(T\) is at most a constant times the initial weight divided by \(1+\epsilon^{-(d-2)}\). The constant is uniform on bounded diffusivity intervals. Hence there is no collision for each fixed start, and no other explosion on the compact torus. This also covers \(\nu=0\). This is the per-start premise used below, not a premise about all starting points on one event.

In flow notation below, a starting argument \(z\in E\) denotes a pair state, and \(w_\alpha\) and \(\ell_N\) at such a state mean their values at its relative coordinate. Let \(Z_r^z\) denote the homogeneous pair process from that state and \(I_r=\int_0^r\ell_N(Z_b^z)\,db\). On a collision-excluded stop every Itô coefficient is bounded, so the stopped martingale is true. Apply (3.5) to
\[
 e^{mI_r-C_{\alpha,m}r}w_\alpha(Z_r^z).
\]
Its nonnegative terminal and occupation terms are retained. Per-start noncollision and Fatou give
\[
 \mathbb E_z e^{mI_r}w_\alpha(Z_r)
       \le e^{C_{\alpha,m}r}w_\alpha(z),\qquad 0\le r\le T.
 \tag{3.6}
\]
Monotone convergence gives the corresponding occupation bound with coefficient \(2/A_N\). That latter coefficient generally grows with \(N\) and is not used to prove the uniform source/gradient estimate. No uniform integrability of stopped weights is presumed.

Conditional Fatou after further localization shows that the discounted nonnegative terminal process is a supermartingale. Its stopped level-crossing estimate is
\[
 \mathbb P_z\{\sup_{r\le T}
 e^{mI_r-C_{\alpha,m}r}w_\alpha(Z_r)>u\}
 \le\min(1,w_\alpha(z)/u).
 \tag{3.7}
\]
For any \(b,l\ge0\) and finite \(Q>0\), choose \(q>Q\), \(m=lq\), and
\(\alpha>\max(lq,bq)\). The \(Q/q\) moment of (3.7) then proves
\[
 \sup_{N,\nu}\sup_{z\in H}
 \mathbb E_z\left[\sup_{r\le T}e^{lI_r}w_b(Z_r)\right]^Q<\infty
 \tag{3.8}
\]
for every compact \(H\Subset E\). The bound has explicit factors
\(e^{QC_{\alpha,m}T/q}/(1-Q/q)\) and
\(\sup_Hw_\alpha^{Q/q}\). Here \(w_b^q\le w_\alpha\).
All parameter suprema in (3.8) concern numerical expectations, not a common event over noise coefficients.

## 4. Actual derivatives: the exceptional-start and expectation passages

For each continuous driving path, subtract the additive noise and patch smooth-cutoff ordinary flows. This gives a measurable maximal flow, smooth in initial state locally wherever the full finite-horizon path remains separated. Along a good path its first variation \(A_r\) solves
\[
 \dot A_r=DF_N(Z_r)A_r,\qquad A_0=I,\qquad |A_r|\le e^{I_r}
 \tag{4.1}
\]
by (3.1). Per-start existence and (4.1) alone would not justify the segment argument required for expectation derivatives.

Here is the additional construction. Fix a coordinate ball \(O\Subset E\), an inner compact ball \(H\), one parameter tuple \(N,\nu\), and the finite horizon. For the maximal path set
\(V(z)=\sup_{r\le T}w_1(Z_r^z)\), taking \(V=\infty\) at starts whose lifetime does not extend through the horizon. If good starts approach a bad one and \(V\) stayed bounded, a single smooth cutoff below their common separation would agree along those paths. Its continuous dependence would give a separated limiting path at the allegedly bad start, a contradiction. Thus \(V\) tends to infinity on approach to a bad start from good starts.

For integers \(j\), \(V_j=\min(V,j)\) is locally Lipschitz on \(O\): on a good neighborhood it is a truncated supremum of a uniformly locally Lipschitz flow family, and near a bad point it is identically \(j\). At almost every good starting point,
\[
 |\nabla V_j(z)|\le C_w\sup_{r\le T} e^{I_r}w_2(Z_r^z),
 \qquad C_w=\sup_E|\nabla_{x,y}w_1|/w_2<\infty .
\]
Per-start noncollision makes the bad set Haar-null almost surely by Fubini. For any \(Q>2d\), (3.8) and spatial integration give
\[
 \sup_{N,\nu,j}\mathbb E\|V_j\|_{W^{1,Q}(O)}^Q<\infty.
 \tag{4.2}
\]
No measurable derivative is hidden: all local cutoff variations are measurable, and derivatives of locally Lipschitz truncations have measurable difference-quotient versions.

The local supremum inequality
\[
 \sup_H|v|\le C_{O,H,Q}
       (\|v\|_{L^Q(O)}+\|\nabla v\|_{L^Q(O)})
\]
follows by averaging the segment fundamental theorem on balls. In dimension \(n=2d\), the gradient kernel is a constant times \(|x-y|^{1-n}\); Hölder is integrable because \((n-1)Q'<n\). More explicitly its radial integral is
\(|\mathbb S^{n-1}|b^{n-(n-1)Q'}/[n-(n-1)Q']\)
for any fixed \(b\) less than the distance of \(H\) to the complement of \(O\). Apply this inequality to (4.2) and let \(j\) increase. Monotone convergence proves \(\sup_HV<\infty\) almost surely. Therefore there are no bad starts in \(H\). A countable exhaustion yields, for each fixed \(N,\nu\), a common locally smooth flow on all of \(E\), with path images of each compact initial set separated from the diagonal for the finite horizon. There is no common event assertion across \(N,\nu\).

Suppose now \(v\in X\). The random function \(v(Z_r^z)\) is \(C^1\) in \(z\) on each such initial ball on this event. Its derivative is \((A_r)^T\nabla v(Z_r)\). For example, (3.6) with \((\alpha,m)=(2(s+1),2)\) bounds its second moment uniformly on compact starting sets, since \(s+1>1\):
\[
 \mathbb E_z|(A_r)^T\nabla v(Z_r)|^2
 \le \|v\|_X^2 e^{C_{2(s+1),2}T}w_{2(s+1)}(z).
 \tag{4.3}
\]
Values have the analogous bound using \((2s,0)\). For the pathwise segment fundamental theorem, Jensen and Fubini give the same bound for difference quotients. Their tails are uniformly integrable. Pathwise convergence followed by that uniform integrability proves
\[
 \nabla S_r^{N,\nu}v(z)
       =\mathbb E_z[(A_r)^T\nabla v(Z_r)],\qquad
 S_r^{N,\nu}v(z)=\mathbb E_zv(Z_r).
 \tag{4.4}
\]
The sequence/uniform-integrability argument also proves joint continuity in \((r,z)\), including \(r=0\). It applies to jointly locally \(C^1\) time-dependent input families with a common \(X\) bound. In particular it applies under the source time integral. This supplies actual continuous derivatives, not just formal differentiated expectations.

Use (3.6) with \((s,0)\) for values and \((s+1,1)\) for derivatives. With
\[
 C_S=\max(C_{s,0},C_{s+1,1}),
\]
we obtain the uniform operator estimate
\[
 \|S_r^{N,\nu}v\|_X\le e^{C_Sr}\|v\|_X.
 \tag{4.5}
\]
The \(Y_s\) value estimate holds for all its Borel inputs by positivity and (3.6). The stronger source weight removes the need to divide by the small negative occupation coefficient in (3.5).

## 5. Global weak derivatives and both finite-measure responses

For every \(v\in X\), the local derivatives are its global Haar weak derivatives. Integrate by parts after deleting the diagonal tube of radius \(\epsilon\). The boundary contribution of \(v\) is at most
\[
 C\|v\|_X\epsilon^{d-1-s}\longrightarrow0,
\]
because \(d-1-s\ge1\). The volume gradient is absolutely integrable because \(s+1<d\). Thus
\[
 \|v\|_{W^{1,1}((\mathbb T^d)^2)}
 \le (W_s+W_{s+1})\|v\|_X,\qquad W_q=\int_{\mathbb T^d}w_q<\infty.
 \tag{5.1}
\]
This proof allows an unbounded value near the diagonal and makes no trace assignment.

Here is an explicit convolution estimate sufficient for (2.2). For \(0<a,q<d\) set
\[
 H_a=\frac{|\mathbb S^{d-1}|(2R_0)^{d-a}}{d-a},\quad
 C_{a,q}=R_0^{-q}\left[
       2^qH_a+
       \frac{2^{a+q-d}|\mathbb S^{d-1}|R_0^{d-a}}{d-q}
                 \right].
\]
For \(z\ne0\) put \(\rho=\min(\operatorname{dist}(z,0),R_0)\). On
\(\operatorname{dist}(w+z,0)\ge\rho/2\), the factor \(w_q(w+z)\) is at most
\(2^q\rho^{-q}\). On the complement, \(\operatorname{dist}(w,0)\ge\rho/2\), while
\[
 \int_{|v|<\rho/2}w_q(v)\,dv
   =\frac{|\mathbb S^{d-1}|}{d-q}(\rho/2)^{d-q}.
\]
Consequently
\[
 \int\chi(w)|w|^{-a}w_q(w+z)\,dw\le C_{a,q}w_q(z).
 \tag{5.2}
\]
We used \(\rho^{d-a}\le R_0^{d-a}\) and
\(\rho^{-q}\le R_0^{-q}w_q(z)\). This estimate requires separately \(a<d\) and \(q<d\); it does not require their sum to be below \(d\).

Below Coulomb write
\(D=s(d-2-s)\chi r^{-(s+2)}\,dw+Q_D(w)\,dw\),
where \(Q_D\) is smooth and bounded by the complete local kernel proof. Define
\[
 D_q=
 \begin{cases}
 s(d-2-s)C_{s+2,q}+\|Q_D\|_\infty W_q,&s<d-2,\\
 c_d(1+W_q),&s=d-2.
 \end{cases}
\]
Then
\[
 \int w_q(z+w)|D|(dw)\le D_q w_q(z).
 \tag{5.3}
\]
At Coulomb the left side is exactly \(c_d[w_q(z)+W_q]\). In particular the atom and negative Haar compensation have both been retained.

Equations (5.2)–(5.3) prove pointwise response convergence and bounds on \(Y_s\). Fubini against the finite measure and the global weak \(L^1\) derivatives from (5.1) gives, as a global weak identity,
\[
 \nabla R_xv=-\int\nabla v(x+w,y)D(dw),
 \qquad
 \nabla R_yv=-\int\nabla v(x,y+w)D(dw).
 \tag{5.4}
\]
No derivative of the measure is taken. These integrals converge absolutely at every off-diagonal point by (5.3). Their joint continuity follows by separating the displacement singularities \(w=0\) and \(w=y-x\). Near zero the translated input remains on a compact off-diagonal set and \(D\) is integrable; near the second point change variable to \(v=x+w-y\), where the density of \(D\) is smooth bounded and the input majorant is \(w_{s+1}(v)\in L^1\). On the complement ordinary compact continuity applies. At Coulomb first extract the atom, which is already a continuous local term. The same argument applies to values and to locally continuous time-dependent families.

Thus these continuous weak derivatives are the classical derivatives locally, as seen by local mollification and the segment fundamental theorem. With
\[
 C_R^Y=2D_s,\qquad C_R^X=2\max(D_s,D_{s+1})
\]
we have
\[
 \|R\|_{Y_s\to Y_s}\le C_R^Y,\qquad
 \|R\|_{X\to X}\le C_R^X.
 \tag{5.5}
\]
Both coefficients one are reflected in the factor two.

The original integrated-gradient response is also valid for this class at every off-diagonal point. Separate the singularities in the integration variable at \(w=0\) and \(w=y-x\). Near the first, apply the distributional divergence identity to a smooth input, retaining its Coulomb atom. Near the second, \(K\) is smooth, the gradient is integrable, and the boundary from \(v\) is \(O(\epsilon^{d-1-s})\). Thus
\(\int K(w)\cdot\nabla_xv(x+w,y)\,dw=R_xv(x,y)\),
and similarly for \(y\). A nonzero displaced singleton has no \(D\) mass; hence no diagonal representative enters any of these formulas.

## 6. Identification with the existing full inverse and uniform bounds

The direct source potential is
\[
 U_t^{N,\nu}=\int_0^{T-t}S_r^{N,\nu}J_{t+r}^\nu\,dr .
\]
Fubini and expectation differentiation are justified by (2.5), (3.6), and Section 4. It is jointly locally \(C^1\), and
\[
 \|U_t^{N,\nu}\|_X
 \le C_J(T-t)e^{C_S(T-t)}.
 \tag{6.1}
\]
Its fixed-\(N\) boundedness on all of \(E\), separately needed for identification, is the issued R5 absolute-source-potential bound. That complete proof uses the nonnegative profile
\[
 \frac N4\left[(r^{s+2}+2s(s+2)\tau/N)^{2/(s+2)}-r^2\right]
\]
and fixed annular errors. Its supremum is bounded by a fixed-data constant times
\(N^{s/(s+2)}T^{2/(s+2)}+T\), uniformly on a bounded diffusivity interval. We use this only as a finite-\(N\) number. No uniform bounded-value conclusion is extracted from it.

Let
\[
 (\mathcal V_{N,\nu}v)_t
 =\int_t^T S_{a-t}^{N,\nu}Rv_a\,da,\qquad
 v_{k,N,\nu}=\mathcal V_{N,\nu}^k U^{N,\nu}.
\]
Pointwise integrals and their derivatives are justified successively by (4.4)–(5.5). On the ordered simplex the propagation intervals add, so
\[
 \|v_{k,N,\nu}(t)\|_X
 \le C_J e^{C_S(T-t)}
         (C_R^X)^k\frac{(T-t)^{k+1}}{(k+1)!}.
 \tag{6.2}
\]
The series converges in the weighted norm and locally uniformly with its first derivatives. Its sum is jointly continuous in time and locally \(C^1\) in space, including terminal time. Separately, the same terms have the issued bounded-Borel factorial bound from the fixed-\(N\) bounded \(U\) and the finite-measure response sup norm. Consequently the \(X\) sum is pointwise the unique already-given bounded Borel full inverse. It has both exact responses and the actual \(f^\nu\).

In particular a sufficient uniform constant is
\[
 \sup_{N,\nu,t}\|\Phi_t^{N,\nu}\|_X
 \le C_*:=T C_J\exp[(C_S+C_R^X)T].
 \tag{6.3}
\]
When \(T=0\), \(\Phi=0\) and \(C_*=0\). Equivalent chosen weights only multiply the fixed comparison constants. Section 5 proves the global weak-derivative and uniform Haar \(W^{1,1}\) assertion.

## 7. Continuous differentiated contractions

For either the finite-\(N\) inverse or any jointly locally \(C^1\) family uniformly bounded in \(X\), define
\[
 Q_t(x)=\int\Phi_t(x,y)\,dy,\qquad
 A_t(x)=\int\nabla_x\Phi_t(x,y)\,dy .
\]
The slice bounds are uniform in \(x,t\):
\[
 |Q_t(x)|\le C_*W_s,\qquad |A_t(x)|\le C_*W_{s+1}.
 \tag{7.1}
\]
For continuity near a moving evaluation point, delete a ball about its diagonal point, containing the corresponding balls for all nearby evaluation points. The omitted value and gradient integrals are bounded uniformly by constants times
\(\delta^{d-s}\) and \(\delta^{d-s-1}\), respectively. The integrand on the remaining compact set is jointly continuous. First take the evaluation/time limit and then \(\delta\downarrow0\). This proves joint continuity; it does not use an invalid fixed-location majorant for a moving singularity.

Global weak differentiation and Fubini identify \(A_t\) as the weak gradient of \(Q_t\). Smooth mollification on the one-body torus makes both \(Q_t\) and its continuous weak gradient converge uniformly, so the segment fundamental theorem gives \(Q_t\in C^1\) and \(\nabla Q_t=A_t\). This proves the classical contraction assertion with the actual gradient representative.

## 8. Response-only limit: exact exponential and uniqueness classes

The bounded operator \(R\) on \(Y_s\) and \(X\) has the norm-convergent exponential
\[
 e^{rR}=\sum_{k\ge0}\frac{r^kR^k}{k!}.
 \tag{8.1}
\]
Its meanings on the two spaces agree on \(X\). It is uniformly continuous in operator norm and differentiable there, with derivative \(Re^{rR}\). This is a bounded signed response operator exponential; it is not claimed to be Markov or positive.

The map \(J^0:[0,T]\to X\) is continuously differentiable. Therefore
\[
 \Phi_t^0=\int_0^{T-t}e^{rR}J_{t+r}^0\,dr
         =\int_t^Te^{(a-t)R}J_a^0\,da
 \tag{8.2}
\]
is a genuine Bochner integral in \(X\), and also in \(Y_s\). The compact continuous image makes the relevant integrand strongly measurable despite possible nonseparability of the whole spaces. It belongs to \(C^1([0,T];X)\), with one-sided derivatives at endpoints, and
\[
 \partial_t\Phi_t^0+R\Phi_t^0=-J_t^0,\qquad\Phi_T^0=0.
 \tag{8.3}
\]
For example \(\partial_t\Phi_T^0=-J_T^0\). Its norm is at most \(T C_J e^{C_R^XT}\).

Here is an explicit maximal pointwise weighted uniqueness class. Let \(v\) be jointly Borel on \([0,T]\times E\), with \(\sup_t\|v_t\|_{Y_s}<\infty\), satisfying the response-only integral equation
\[
 v_t=\int_t^T[J_a^0+Rv_a]\,da
 \quad\hbox{at every }(t,x,y)\in[0,T]\times E .
 \tag{8.4}
\]
The integrals are pointwise measurable and absolutely dominated by the fixed weight. If \(v,\widetilde v\) are two such solutions, factorial iteration gives for every \(k\)
\[
 \|v_t-\widetilde v_t\|_{Y_s}
 \le \sup_a\|v_a-\widetilde v_a\|_{Y_s}
       \frac{[C_R^Y(T-t)]^k}{k!}.
\]
Hence they agree pointwise. In particular (8.2) is the unique solution in this entire uniformly weighted-value mild class, and is the unique norm-classical solution. For time-a.e. distributional formulations, uniqueness means the absolutely continuous representative satisfying (8.4); arbitrary alterations at isolated times are not a separate pointwise solution class.

The frozen short statement refers to weighted-space meanings in a withheld complete report. No such meanings have been guessed as evidence: (2.4), (8.1), and (8.4) give fully explicit, sufficient meanings reconstructed from the assertion. Candidate comparison must check that the withheld wording does not intend a different representative convention.

The response and the source preserve exchange symmetry, so \(\Phi^0\) is symmetric. Sections 5 and 7 apply to it: it has jointly continuous off-diagonal first derivatives, is a global weak Haar \(W^{1,1}\) representative, and has continuous differentiated contractions. Boundedness on the pair diagonal is not a premise or a conclusion.

## 9. Uniform small-motion limit for the base semigroup

Fix \(H\Subset E\). Choose a slightly larger compact neighborhood \(H'\Subset E\) and a distance margin \(\eta>0\). On \(H'\), the drift is bounded by \(M_H/N\) and its derivative by \(M'_H/N\). Couple the processes for each tuple with a standard \(2d\)-dimensional Brownian path; no simultaneous parameter event will be used.

Before leaving this neighborhood, the displacement of a consistent lift satisfies
\[
 \sup_{r\le T}|Z_r^z-z|
 \le \sqrt{2\nu}\sup_{r\le T}|W_r|+TM_H/N .
 \tag{9.1}
\]
For \(N\) large enough and on the event that the noise supremum is less than a chosen fraction of \(\eta\), this estimate prevents exit for every \(z\in H\). On that event
\[
 \sup_{z\in H,r\le T}|A_r^z-I|
       \le e^{M'_HT/N}-1.
 \tag{9.2}
\]
The good-event displacement tends to zero in probability uniformly in the allowed \(\nu\). For example, the one-dimensional exponential Brownian martingale stopped at its first crossing, applied to each sign and coordinate, gives
\[
 \mathbb P\{\sqrt{2\nu}\sup_{r\le T}|W_r|>\epsilon\}
 \le 4d\exp[-\epsilon^2/(8d\nu T)]
 \tag{9.3}
\]
when \(\nu T>0\), and probability zero for \(\nu T=0\). Since \(\sup\nu\le L N^{-2/p}\to0\), this tail tends to zero. One may first fix any smaller motion tolerance and then let it decrease; no rate for a general input modulus is claimed.

For a family \(v_\theta\in X\) uniformly bounded in \(X\) and jointly locally continuous together with its gradient on a compact parameter set, (9.1)–(9.2) give convergence of the integrands in (4.4) on the good event uniformly in \(z,r,\theta\). On the complement, the second moments from (3.6), with \((2s,0)\) and \((2(s+1),2)\), and Cauchy–Schwarz give a bound by a fixed constant times the square root of its probability. Thus
\[
 \sup_{\nu,r,\theta}
 \|S_r^{N,\nu}v_\theta-v_\theta\|_{C^1(H)}
 \longrightarrow0,\qquad 0\le r\le T.
 \tag{9.4}
\]
Here \(C^1(H)\) means the supremum of the restricted ambient value and first derivatives; no geometric regularity of \(H\) is needed.

A needed extension is equally justified: if \(v_{N,\nu,\theta}\) are uniformly \(X\)-bounded and converge to \(v_{0,\theta}\) locally in \(C^1\), uniformly in all displayed parameters, then
\[
 S_r^{N,\nu}v_{N,\nu,\theta}\longrightarrow v_{0,\theta}
\]
uniformly for \(r,\nu,\theta\) in \(C^1(H)\). On the good event use convergence on the larger compact neighborhood \(H'\); on the complement use the same moment bound for the difference. This statement requires no convergence in the global weighted norm.

## 10. Local response continuity and the full-kernel limit

We record the corresponding nonlocal stability fact. Suppose \(v_j(\theta)\) are uniformly \(X\)-bounded and converge locally in \(C^1\), uniformly over a compact parameter set, to \(v_0(\theta)\). Then
\[
 Rv_j(\theta)\to Rv_0(\theta)
 \quad\hbox{locally in }C^1,\hbox{ uniformly in }\theta .
 \tag{10.1}
\]
For points in \(H\Subset E\), the singular locations of the integration variable remain uniformly separated. In a small neighborhood of the input-diagonal location, the density of \(D\) is uniformly bounded, and the value/gradient tails are respectively \(O(\delta^{d-s})\) and \(O(\delta^{d-s-1})\). In a neighborhood of \(w=0\), translated inputs lie on a fixed compact subset of \(E\), so uniform local convergence times the finite total variation suffices. On the complement both are uniformly separated. At Coulomb extract the local atom first and handle the Haar part by the same integrable tails. This proves (10.1), including a moving evaluation point; it is not a claim of response operator-norm convergence on weighted spaces.

Start with \(v_{0,N,\nu}=U^{N,\nu}\) from Section 6. The source norm convergence and Section 9 show uniformly in \(t,\nu\)
\[
 U_t^{N,\nu}\to U_t^0:=\int_t^TJ_a^0\,da
       \quad\hbox{in }C^1(H).
\]
Inductively combine (10.1), the varying-family extension of (9.4), and the time integral on its compact triangular time domain. For each fixed integer \(k\),
\[
 v_{k,N,\nu}(t)\to v_{k,0}(t)
 \quad\hbox{in }C^1(H),\hbox{ uniformly in }t,\nu ,
\]
where \(v_{k,0}=\mathcal V_0^k U^0\) and
\((\mathcal V_0v)_t=\int_t^T Rv_a\,da\). The uniform weighted factorial bound (6.2) makes the tails locally uniformly summable, independently of \(N,\nu,t\). Hence the full inverses converge locally in \(C^1\), uniformly in these parameters.

Finally direct ordered integration gives
\[
 v_{k,0}(t)=\frac1{k!}\int_t^T(a-t)^kR^kJ_a^0\,da.
\]
The absolutely norm-convergent sum is exactly (8.2). This identifies the limiting kernel with the specified full response-only inverse, rather than a source-only diagnostic.

## 11. Global Haar \(W^{1,1}\) and uniform contraction convergence

All finite-\(N\) kernels and their limit have the same uniform \(X\) bound, after harmlessly increasing \(C_*\). For \(0<\delta<R_0\),
\[
 \int_{|x-y|<\delta}|\Phi_t^{N,\nu}-\Phi_t^0|\,dx\,dy
 \le \frac{2C_*|\mathbb S^{d-1}|}{d-s}\delta^{d-s},
\]
\[
 \int_{|x-y|<\delta}
    |\nabla\Phi_t^{N,\nu}-\nabla\Phi_t^0|\,dx\,dy
 \le \frac{2C_*|\mathbb S^{d-1}|}{d-s-1}\delta^{d-s-1}.
 \tag{11.1}
\]
On the complement the local \(C^1\) convergence is uniform in \(t,\nu\). First send \(N\to\infty\) for fixed \(\delta\), then send \(\delta\downarrow0\). This proves
\[
 \sup_{0\le\nu\le L N^{-2/p}}\sup_{0\le t\le T}
 \|\Phi_t^{N,\nu}-\Phi_t^0\|_{W^{1,1}((\mathbb T^d)^2)}
       \longrightarrow0.
 \tag{11.2}
\]
The weak gradients in this norm are the actual representatives already identified in Section 5.

The same estimates are uniform slice estimates in \(x\). Applying them to the contraction differences and using the uniform local convergence on \(\{|x-y|\ge\delta\}\) proves uniform convergence of both \(Q_t^{N,\nu}\) and \(A_t^{N,\nu}\) in \(t,x,\nu\). Symmetry gives the other slot, and integration gives scalar value/gradient contractions when desired. No diagonal trace or actual-law substitution is used.

The logical order of limits is explicit and is the same for each displayed supremum. No intersection of probability-one sets over an uncountable collection of \(\nu\) was taken. Bounds on numerical expectations were first proved with constants uniform in \(\nu\); the resulting deterministic suprema are legitimate.

## 12. Independent falsification calculations and endpoint checks

The falsification route uses the exact Coulomb response decomposition and a direct radial flow, rather than the barrier/Volterra construction.

At Coulomb let \(P_x,P_y\) denote Haar averaging in the indicated slot and \(c=c_d\). They commute and are idempotent. Exact compensation gives
\[
 R=-2cI+cP_x+cP_y,\qquad
 e^{rR}=e^{-2cr}[I+(e^{cr}-1)P_x][I+(e^{cr}-1)P_y].
 \tag{12.1}
\]
Omitting either response, its atom, or its Haar compensation changes this formula. Pair Fourier modes have eigenvalue
\(-c(\mathbf1_{k\ne0}+\mathbf1_{\ell\ne0})\); constants are killed.

At \(\nu=0\), \(f_t^0=\bar h+e^{-c(T-t)}(h-\bar h)\), so
\(J_t^0=e^{-c(T-t)}J_h\). Write \(\tau=T-t>0\). In (8.2), the term with no Haar projection is
\[
 \frac{e^{-c\tau}(1-e^{-c\tau})}{c}J_h.
 \tag{12.2}
\]
Every term with a projection is bounded and has bounded first derivatives: \(J_h\in X\), and Section 7 applies to its contractions. For \(h(x)=\cos(2\pi x_1)\), take \(y=0\), \(x=re_1\). Then
\[
 J_h(re_1,0)=-s(2\pi)^2r^{-s}+O(r^{2-s})+O(r^2).
\]
Thus (12.2) proves that the limiting full kernel is generally unbounded at the diagonal. Its leading first derivative is a nonzero multiple of \(r^{-s-1}\) on an open set of angular and center variables, so at Coulomb it is generally not in \(H^1\). This is consistent with \(s+1=d-1<d\) but \(2(s+1)\ge d\).

For each fixed \(N\), the existing inverse is bounded. Consequently \(r^s\Phi_t^{N,0}\to0\) as \(r\downarrow0\), whereas the preceding \(r^s\Phi_t^0\) has a nonzero limit for that test and direction. Weighted supremum convergence of the values is therefore false in general, already at \(\nu=0\). The asserted local \(C^1\)/global \(W^{1,1}\) convergence survives this check. This is a counterexample to an excluded strengthening, not to THM-032.

The principal zero-noise radial flow obeys
\[
 r(a)^{s+2}=r(0)^{s+2}+2s(s+2)a/N.
\]
For the scalar radial source \(s r^{-s}\), its integrated potential is
\[
 U=\frac N4[r(\tau)^2-r(0)^2].
\]
Differentiation at fixed \(\tau\) gives
\[
 \partial_{r(0)}U=\frac N2[
       r(\tau)^{-s}r(0)^{s+1}-r(0)].
\]
This checks the internal factor \(2s/N\), the sign of radial contraction, and the natural uniform source powers. It is a local solvable diagnostic, not the periodic actual source.

Additional boundary and range checks:

- \(T=0\): all kernels, derivatives, and time integrals in the target vanish.
- \(L=0\) or \(\nu=0\): the positive diffusion cost in (3.3) is zero. The deterministic flow and all proofs remain valid.
- \(N=2\): only \(2/N\le1\) was used in the uniform constants, so no large-\(N\) estimate is needed for boundedness.
- The strict inequality \(s>0\) makes both \(\alpha=s+1>1\) and the Young exponent \(2/s\) valid. No logarithmic substitution is allowed.
- At \(s=d-2\), the value diffusion term is zero, the gradient diffusion term can be positive, and (3.3) absorbs it while (2.1) retains the atom.
- Below Coulomb \(s+2<d\), so the finite-density convolution exponent is admissible. At Coulomb it is replaced by the exact atom/constant decomposition, not by an integrable \(r^{-d}\) density.
- The weak-boundary exponent is \(d-1-s\ge1\), and the gradient tail exponent is \(d-s-1\ge1\). Neither endpoint is borderline.
- For \(\nu_N=1/\beta_N\) and \(\beta_NN^{s/d-1}\to\lambda\in(0,\infty)\),
\[
 \nu_NN^{2/(s+2)}
 \sim\lambda^{-1}N^{\,s(s+2-d)/(d(s+2))}.
\]
It tends to zero below Coulomb and to \(1/\lambda\) at Coulomb. Thus every such sequence eventually has some finite \(L\). General subcriticality does not imply this auxiliary bound; for example \(\beta_N=1\) is subcritical on this range but has diverging rescaled diffusivity.

## 13. Claim disposition, remaining line, and law-class boundary

| Frozen claim | Reconstruction disposition | Exact argument |
|---|---|---|
| Uniform weighted value and full first gradient | Reconstructed | Uniform Young cost (3.3), terminal moments (3.6), semigroup (4.5), full-series bound (6.3). |
| Actual jointly continuous off-diagonal derivatives | Reconstructed | Common local flow proved per parameter, moment/UI differentiation, response and series continuity. |
| Global weak representative and Haar \(W^{1,1}\) | Reconstructed | Deleted-tube boundary and integrable gradient in Section 5. |
| Continuous contraction and its classical derivative | Reconstructed | Moving-tube continuity, weak Fubini, mollification in Section 7. |
| Full response-only kernel, exponential and uniqueness | Reconstructed with explicit function-space meanings | Bounded operator exponential on \(X,Y_s\), Bochner source integral, pointwise weighted mild uniqueness. |
| Uniform local \(C^1\) convergence | Reconstructed | Uniform small-motion/UI lemma, local response stability, fixed-order convergence and uniform factorial tails. |
| Uniform global Haar \(W^{1,1}\) and contraction convergence | Reconstructed | Uniform integrable diagonal tails followed by local convergence. |
| Coulomb/zero-noise/zero-time/critical-range qualifications | Checked | Sections 2, 3, and 12. |
| Current canonical acceptance of earlier modules | Not assigned here | Their issued qualifications remain; no withheld current state was read. |
| Actual evolved bracket, residual, fluctuation or hierarchy conclusion | Not proved and not claimed | Requires separate interacting-law estimates. |

There is no new first unsupported analytic line inside the frozen THM-032 assertion, under the existing inverse/process premises. There is a precise remaining comparison issue: the parent must check the candidate's withheld weighted-space wording against Section 8 and compare the full construction with this sealed proof. A separate hostile audit must test this reconstruction.

The first excluded dynamical line remains an \(N\)-uniform passage from these deterministic Haar kernel norms to the singular interacting law and its bracket/residual expressions. R6 supplies only the fixed-\(N\) density bound \(\|F_0\|_\infty e^{(N-1)\kappa T}\) when the external drift is zero, which cannot turn these bounds into a uniform evolved-law estimate. The gradient weight need not be square integrable, as the explicit Coulomb calculation demonstrates. No actual-law tail, \(H^1\), diagonal trace, second/time-derivative convergence, mean-to-fluctuation transfer, or finite critical hierarchy closure has been asserted.

## 14. Verification and immutable handoff

The fresh standard-library checker is ROUND_011_GRADIENT_BLIND_ARTIFACTS/round011_gradient_blind_exact.py. It checks the permitted input hashes, exact pair block eigenvectors, radial generator coefficients, Young maximization at exact rational points, rescaling and critical powers, all endpoint integrability exponents, the compensated two-slot Coulomb Fourier response and response-only coefficient recursion, and zero-noise radial profiles. It deliberately tests detectable wrong factors and missing responses. Exact arithmetic supports these identities; it does not prove the analytic compactness, expectation, convolution or convergence passages.

The companion JSON reports actual counts and results. README.md records the executed commands and output set. INPUT_SHA256SUMS.txt and input_verification.json preserve the twenty-one-input dossier. OUTPUT_SHA256SUMS.txt covers the immutable report, checker, results, README and input records. The archive contains exactly those inputs and outputs plus the output manifest; SEAL_SHA256SUMS.txt hashes the archive and output manifest. Archive verification checks the exact member set, CRC, and all member digests.

No TeX source was edited or generated. The requested deliverable is this Markdown reconstruction and its reproducibility packet; the short final handoff contains no mathematical LaTeX. No canonical ledger or source file was changed. Issued report bytes must not be edited after sealing; any later correction requires a separately named superseding report.
