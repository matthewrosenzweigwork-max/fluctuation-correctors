# TASK-012: independent reconstruction of the smooth all-order identities

Reconstruction date: 2026-09-17 UTC. Status before comparison: **BLIND RECONSTRUCTION; SELF-CHECKED ONLY**. The coordinator alone may compare this sealed document with constructor outputs or promote a campaign claim.

## Isolation and inputs

This context previously performed a read-only Codex concurrency-configuration task. That task included the repository's `README_FIRST.md`, `MODEL_ORCHESTRATION.md`, configuration example, and Git status, but no constructor proof, theorem source, mathematical memorandum, or mathematical audit. The subsequent mathematical work read only the present worktree's `AGENTS.md`, `TASKS/ACTIVE/ROUND_001_MODEL.md`, and `TASKS/ACTIVE/TASK-012_ROUND002_BLIND.md`. No other worktree or constructor narrative was inspected during reconstruction. This is a reused operational context, not a newly allocated context; its mathematical isolation is the precise claim made here.

- Worktree: `/private/tmp/hocf-round002-blind-20260917`.
- Baseline HEAD: `475a5399828bc6e2ccbade08c59b8778638df14a`.
- Model input SHA-256: `3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57`.
- Task input SHA-256: `48c32ac48f1648c686bedef9420b314d1834638ecf9c27df6e2de7be229202c4`.
- Assigned model/effort: Astra Max, as supplied by the coordinator; no claim of independent runtime attestation is made.
- Imported tools: finite sums, finite combinatorics, and smooth Itô calculus, all expressly permitted by the model. No literature theorem or unverified private input is used.

The primary assertion is that the drift and bracket formulas below hold for every permitted smooth model, every finite particle number, and every finite order, including orders exceeding the particle number. Its exact negation is the existence of permissible data for which either coefficient identity fails. The proof route is an expansion in finite subsets; the falsification route computes the original microscopic generator and particle derivatives directly in exact Fourier arithmetic.

## 1. Definitions and regularity

Fix an integer \(N\geq2\), \(\beta_N>0\), \(q=N^{-1}\), and \(\nu=\beta_N^{-1}\). Work on the unit torus with Haar mass one and the frozen smooth model

\[
 dX_i=\left(b(X_i)+q\sum_{j\ne i}K(X_i-X_j)\right)dt+\sqrt{2\nu}\,dW_i,
 \qquad K=-\nabla g,
\]

where \(g\) is smooth, real and even, \(b=-\nabla V\) is smooth, and the \(W_i\) are independent standard Brownian motions in dimension \(d\). Thus \(K\) is odd and \(K(0)=0\). The deterministic smooth probability density \(\mu_t\) satisfies

\[
 \partial_t\mu=-\operatorname{div}(u\mu)+\nu\Delta\mu,
 \qquad u=b+K*\mu.
\]

All test kernels below are deterministic, real, \(C^1\) in time and smooth in every spatial variable on a fixed compact time interval. It is enough to impose the spatial derivatives used by the displayed formulas and Itô's formula; the stated smooth class avoids any extension issue. Constants or kernels may depend on \(N,\beta_N,g\), and time; that dependence is not suppressed in any estimate. The initial law is arbitrary. No exchangeability or independence of the initial coordinates is needed.

For a finite labelled slot set \(I\), write

\[
 F_I[H]=q^{|I|}\sum_{\iota:I\hookrightarrow[N]}H((X_{\iota(a)})_{a\in I}),
 \qquad F_\varnothing[c]=c.
\]

An injection refers to particle labels, including when two particle coordinates coincide. If \(|I|>N\), the sum is empty. For \(B\subset I\), let \(P_BH\) denote integration of the slots in \(B\) against independent copies of \(\mu_t\), retaining the remaining slot labels. Define

\[
 U_I[H]=\sum_{A\subset I}(-1)^{|I|-|A|}F_A[P_{I\setminus A}H]. \tag{1}
\]

Write \(U_k\) when the slot set is \([k]\), with \(U_0[c]=c\). This is exactly the frozen normalization, with denominator \(N^{|A|}\), not a falling factorial. The definition makes sense for nonsymmetric kernels; symmetrizing a kernel leaves its value unchanged. Symmetry is assumed only when using the compressed coefficient formulas below.

For comparison with the full empirical product,

\[
 U_1[f]=\langle\eta-\mu,f\rangle,\qquad
 U_2[\Phi]=\langle(\eta-\mu)^{\otimes2},\Phi\rangle
            -q\langle\eta,\Phi(x,x)\rangle. \tag{2}
\]

Higher-order empirical products are not silently identified with \(U_k\). All collision identifications used below are explicitly specified maps on kernels.

## 2. The finite subset cancellation

For \(S\subset I\), define a functional whose slots in \(S\) are forced to use particle labels:

\[
 E_{I,S}[H]=\sum_{S\subset A\subset I}
 (-1)^{|I|-|A|}F_A[P_{I\setminus A}H].
\]

Then, without any condition on \(|I|\) relative to \(N\),

\[
 \boxed{\displaystyle
 E_{I,S}[H]=\sum_{B\subset S}U_{I\setminus B}[P_BH].} \tag{3}
\]

Indeed, after expanding the right side by (1), the coefficient of
\(F_A[P_{I\setminus A}H]\) is

\[
 \sum_{B\subset S\setminus A}(-1)^{|I|-|B|-|A|}
 =(-1)^{|I|-|A|}(1-1)^{|S\setminus A|}.
\]

It vanishes unless \(S\subset A\), and is then the coefficient in \(E_{I,S}\). Empty-injection terms cause no change to this argument. In particular,

\[
 E_{I,\{a,b\}}[H]=U_I[H]
 +U_{I\setminus\{a\}}[P_aH]
 +U_{I\setminus\{b\}}[P_bH]
 +U_{I\setminus\{a,b\}}[P_{a,b}H]. \tag{4}
\]

All four signs are positive. This identity supplies the lower internal-force contractions and, with arbitrary \(S\), every lower bracket contraction.

## 3. The full drift identity

For \(X=(x_1,\ldots,x_k)\), put

\[
 D_a\Phi=u(x_a)\cdot\nabla_a\Phi+\nu\Delta_a\Phi,
\]

\[
 R_a\Phi(X)=\int K(y-x_a)\cdot
   \nabla_a\Phi(X^{a\leftarrow y})\,\mu(dy),
 \qquad A_k\Phi=\sum_{a=1}^k(D_a\Phi+R_a\Phi). \tag{5}
\]

The derivative in \(R_a\) is taken in the original slot before replacing that slot by \(y\). The free argument \(x_a\) of \(R_a\) is the new response variable. Define

\[
 B_k\Phi(X,z)=\sum_{a=1}^kK(x_a-z)\cdot\nabla_a\Phi(X),
 \qquad T_{ab}\Phi=K(x_a-x_b)\cdot\nabla_a\Phi. \tag{6}
\]

The labelled, uncompressed identity is

\[
\begin{split}
 dU_k[\Phi]={}&\left\{U_k[(\partial_t+A_k)\Phi]
                      +U_{k+1}[B_k\Phi]\right\}dt+dM_k^\Phi\\
 &+q\sum_{a\ne b}\sum_{B\subset\{a,b\}}
     U_{[k]\setminus B}[P_B(T_{ab}\Phi)]\,dt. \tag{7}
\end{split}
\]

For a symmetric \(\Phi\), define the following kernels. No symmetrization factor is hidden:

\[
 T_k\Phi(X)=\sum_{a<b}K(x_a-x_b)\cdot(\nabla_a-\nabla_b)\Phi(X), \tag{8}
\]

\[
 C_k\Phi(x,Z)=\int K(x-y)\cdot(\nabla_1-\nabla_2)
                     \Phi(x,y,Z)\,\mu(dy), \tag{9}
\]

\[
 Q_k\Phi(Z)=\iint K(x-y)\cdot(\nabla_1-\nabla_2)
                     \Phi(x,y,Z)\,\mu(dx)\mu(dy). \tag{10}
\]

Here \(C_k\Phi\) has \(k-1\) arguments and \(Q_k\Phi\) has \(k-2\). The notation \(Q_k\) is local to this reconstruction and denotes this explicit kernel, not a martingale quadratic variation. The symmetric form of (7) is

\[
\boxed{\begin{split}
 dU_k[\Phi]={}&U_k[(\partial_t+A_k)\Phi]dt+U_{k+1}[B_k\Phi]dt\\
 &+qU_k[T_k\Phi]dt
  +qk(k-1)U_{k-1}[C_k\Phi]dt\\
 &+q\binom{k}{2}U_{k-2}[Q_k\Phi]dt+dM_k^\Phi.
\end{split}} \tag{11}
\]

The last three terms are omitted at \(k=1\). An asymmetric \(B_k\Phi\) or \(C_k\Phi\) may be replaced by its ordinary average over permutations without changing its \(U\)-value.

### Proof of (7)

Apply smooth Itô calculus to each finite term in (1), retaining the derivative of every background measure. The common particle drift \(u\), particle diffusion \(\nu\Delta\), and the background equation combine to give
\(U_k[(\partial_t+\sum_aD_a)\Phi]\). This statement includes derivatives in slots integrated against \(\mu\): the weak background equation is exactly \(\partial_t\mu[f]=\mu[u\cdot\nabla f+\nu\Delta f]\).

For a term with particle-slot set \(A\), the residual force at a particle slot \(a\in A\) is

\[
 q\sum_{j\ne\iota(a)}K(X_{\iota(a)}-X_j)-(K*\mu)(X_{\iota(a)}).
\]

Split the particle sum into labels outside \(\iota(A)\) and labels \(\iota(b)\), \(b\in A\setminus\{a\}\). The first part, after adjoining a slot \(z\), contributes

\[
 F_{A\cup\{z\}}[P_{[k]\setminus A}(B_a\Phi)]
 -F_A[P_{([k]\setminus A)\cup\{z\}}(B_a\Phi)],
 \qquad B_a\Phi=K(x_a-z)\cdot\nabla_a\Phi. \tag{12}
\]

The second part is

\[
 q\sum_{b\in A\setminus\{a\}}F_A[P_{[k]\setminus A}(T_{ab}\Phi)]. \tag{13}
\]

There is no self-force: its value is \(K(0)=0\). The factor \(q\) in (13) survives because an already present particle label does not add another free summation.

For fixed \(a\), the signed sum of (12) over \(A\ni a\) is exactly the part of \(U_{[k]\cup\{z\}}[B_a\Phi]\) in which \(a\) is a particle slot. The omitted part, in which \(a\) is a background slot, is

\[
 -U_{([k]\setminus\{a\})\cup\{z\}}[P_a(B_a\Phi)].
\]

Therefore the signed sum of (12) is
\(U_{k+1}[B_a\Phi]+U_k[R_a\Phi]\), after relabelling \(z\) as \(a\) in the second term. This establishes the **positive** background response term and explains why it belongs to the full linearized operator rather than to an uncontrolled remainder.

For fixed ordered \((a,b)\), the signed sum of (13) is
\(qE_{[k],\{a,b\}}[T_{ab}\Phi]\). Formula (4) gives exactly the four terms in (7). All sums are finite, proving (7) for every \(k\), including \(k>N\).

### Coefficients in (11)

Oddness of \(K\) combines the two ordered terms \((a,b)\) and \((b,a)\) into the unordered-pair operator in (8). For each of the \(\binom{k}{2}\) unordered pairs, removal of either endpoint produces the same \(U_{k-1}[C_k\Phi]\), by symmetry of \(\Phi\) and relabelling. There are two such removals, giving \(2\binom{k}{2}=k(k-1)\). Removing both endpoints gives \(U_{k-2}[Q_k\Phi]\) once per unordered pair. These statements use no large-\(N\) simplification.

The diffusion creates no lower drift contraction in (7): within each factorial term, a given Brownian motion appears in at most one slot. Distinct labels have independent Brownian motions even when their coordinates coincide. The mixed Itô term encountered in the full-product convention (2) is exactly cancelled by the diagonal subtraction in that convention.

## 4. Martingale, including its normalization

For a fixed particle label \(i\), define the leave-one-label-out functional

\[
 U^{(-i)}_J[H]=\sum_{A\subset J}(-1)^{|J|-|A|}q^{|A|}
 \sum_{\iota:A\hookrightarrow[N]\setminus\{i\}}
 P_{J\setminus A}H((X_{\iota(a)})_{a\in A}). \tag{14}
\]

Its denominator is still \(N^{|A|}\), and its background is still \(\mu\). Differentiating (1) with respect to \(X_i\), and selecting the unique slot occupied by \(i\), gives

\[
 dM_k^\Phi=\sqrt{2\nu}\,q\sum_{i=1}^N\sum_{a=1}^k
 U^{(-i)}_{[k]\setminus\{a\}}
 [\nabla_a\Phi(X^{a\leftarrow X_i})]\cdot dW_i. \tag{15}
\]

For symmetric \(\Phi\), the relabelled summands agree, so

\[
 \boxed{\displaystyle dM_k^\Phi=\sqrt{2\nu}\,kq\sum_{i=1}^N
 U^{(-i)}_{k-1}[\nabla_1\Phi(X_i,\cdot)]\cdot dW_i.} \tag{16}
\]

Consequently the immediate, unexpanded bracket is

\[
 \frac{d\langle M_k^\Phi,M_\ell^\Psi\rangle_t}{dt}
 =2\nu k\ell q^2\sum_{i=1}^N
 U^{(-i)}_{k-1}[\nabla_1\Phi(X_i,\cdot)]\cdot
 U^{(-i)}_{\ell-1}[\nabla_1\Psi(X_i,\cdot)]. \tag{17}
\]

These are genuine square-integrable continuous martingales for the stated smooth data. For example, for symmetric \(\Phi\), each leave-one-out functional in (16) has absolute value at most \(2^{k-1}\|\nabla_1\Phi\|_\infty\), because the mass of each factorial measure is at most one. Thus

\[
 \frac{d\langle M_k^\Phi\rangle_t}{dt}
 \leq\frac{2\nu k^2 4^{k-1}}{N}\|\nabla_1\Phi_t\|_\infty^2. \tag{18}
\]

This bound establishes well-definedness. It does not provide cutoff-uniform bounds on a family of backward test kernels.

## 5. Every shared-label contraction in the bracket

Let \(I=[k]\) and \(J=[\ell]'\) be disjoint slot sets. A partial matching \(\mathfrak m\) is a bijection between a subset of \(I\) and a subset of \(J\); write \(p=|\mathfrak m|\). Identify the two variables on every matched edge. The quotient slot set \(V_{\mathfrak m}\) has
\(m=k+\ell-p\) slots. Its subset \(S_{\mathfrak m}\) of shared slots has size \(p\).

For a distinguished edge \(e=(a,b)\in\mathfrak m\), define

\[
 H_{\mathfrak m,e}
 =\operatorname{Diag}_{\mathfrak m}
       (\nabla_a\Phi\cdot\nabla_b\Psi). \tag{19}
\]

Differentiate the two original kernels **before** identifying variables. In particular, (19) is not the derivative of a product after identification. Integration of a shared slot means one integral against \(\mu\), not two.

The complete labelled formula is

\[
\boxed{\displaystyle
 \frac{d\langle M_k^\Phi,M_\ell^\Psi\rangle_t}{dt}
 =2\nu\sum_{p=1}^{\min(k,\ell)}q^p
 \sum_{\substack{\mathfrak m\ \text{partial matching}\\|\mathfrak m|=p}}
 \sum_{e\in\mathfrak m}\sum_{D\subset S_{\mathfrak m}}
 U_{V_{\mathfrak m}\setminus D}[P_DH_{\mathfrak m,e}].} \tag{20}
\]

The word “partial matching” in this formula has exactly the definition just given; all finite sums and every coefficient are explicit. The possible orders in a fixed \(p\)-row run from \(k+\ell-p\) down to \(k+\ell-2p\).

### Proof and enumeration

Expand the two original signed subset sums (1) before taking the Brownian bracket. Let \(A\subset I\) and \(B\subset J\) be their particle-slot sets. Particle labels are injective within each block. The equalities of labels between the two blocks therefore form a unique partial matching: no vertex can belong to two edges. A nonzero Brownian bracket chooses an edge of that matching, namely the two differentiated slots driven by the same Brownian motion. This is its distinguished edge.

Fix that matching and its distinguished edge. All other label values in the union must be distinct; otherwise the matching would have contained another edge. Thus the union of labels is an injection into the quotient slots occupied by particles. All \(p\) shared slots are forced particles. The original normalization satisfies

\[
 q^{|A|+|B|}=q^p q^{|A|+|B|-p},
\]

and the original sign is

\[
 (-1)^{k+\ell-|A|-|B|}
 =(-1)^{(k+\ell-p)-(|A|+|B|-p)}.
\]

It follows that this group of terms is precisely
\(2\nu q^pE_{V_{\mathfrak m},S_{\mathfrak m}}[H_{\mathfrak m,e}]\).
Apply (3). This proves (20), with no assumption that a quotient order is at most \(N\).

For symmetric kernels all choices of the matching and its distinguished edge give the same representative after relabelling, before choosing which shared slots to integrate. The number of matchings with a distinguished edge is

\[
 c_{k,\ell,p}
 =p\binom{k}{p}\binom{\ell}{p}p!
 =k\ell\binom{k-1}{p-1}\binom{\ell-1}{p-1}(p-1)!. \tag{21}
\]

The first expression chooses the two endpoint subsets, their bijection, and an edge. The second chooses the distinguished pair first and then the remaining \(p-1\) pairs. This also proves the equality of the expressions, independently of factorial simplification.

To give the fully compressed version, take shared variables \(z_1,\ldots,z_p\), with \(z_1\) the distinguished one, and separate unshared lists \(x\) and \(y\) of lengths \(k-p\) and \(\ell-p\). Set

\[
 H_p(z,x,y)=\nabla_1\Phi(z_1,\ldots,z_p,x)
                  \cdot\nabla_1\Psi(z_1,\ldots,z_p,y). \tag{22}
\]

For \(\epsilon\in\{0,1\}\) and \(0\leq r\leq p-1\), let \(P_{\epsilon,r}\) integrate \(z_2,\ldots,z_{r+1}\), and also \(z_1\) if \(\epsilon=1\), against \(\mu\). The shared variables other than \(z_1\) are symmetric, yielding

\[
\boxed{\displaystyle
 \frac{d\langle M_k^\Phi,M_\ell^\Psi\rangle_t}{dt}
 =2\nu\sum_{p=1}^{\min(k,\ell)}q^p c_{k,\ell,p}
 \sum_{\epsilon=0}^1\sum_{r=0}^{p-1}\binom{p-1}{r}
 U_{k+\ell-p-\epsilon-r}[P_{\epsilon,r}H_p].} \tag{23}
\]

There is no alternating sign in (20) or (23). Alternating signs remain inside the definition of \(U\); (3) accounts for their cancellation. Individual terms in these expansions need not be positive. Nonnegativity of a self-bracket follows from the sum of squares in (17), not from termwise positivity.

## 6. Low-order and degenerate checks

### One body, derived a second way

Directly subtract the weak background equation from the empirical Itô equation. Since \(K(0)=0\), the particle drift can be written \(u+K*(\eta-\mu)\). With \(\rho=\eta-\mu\), the interaction residual is

\[
 \iint K(x-y)\cdot\nabla f(x)\,\eta(dx)\rho(dy)
 =\rho[R_1f]+\langle\rho^{\otimes2},B_1f\rangle.
\]

The diagonal of \(B_1f\) vanishes, so (2) gives

\[
 dU_1[f]=\{U_1[(\partial_t+A_1)f]+U_2[B_1f]\}dt+dM_1^f.
\]

This agrees with (11), without using its subset proof. The bracket is

\[
 \frac{d\langle M_1^f,M_1^h\rangle_t}{dt}
 =2\nu q\{U_1[\nabla f\cdot\nabla h]+\mu[\nabla f\cdot\nabla h]\}
 =2\nu q\eta[\nabla f\cdot\nabla h]. \tag{24}
\]

### Pair and the next two orders

For \(k=2\), the lower drift terms in (11) are exactly

\[
 qU_2[T_2\Phi]+2qU_1[C_2\Phi]+qQ_2\Phi. \tag{25}
\]

For \(k=3\) they are \(qU_3[T_3\Phi]+6qU_2[C_3\Phi]+3qU_1[Q_3\Phi]\).
For \(k=4\) they are \(qU_4[T_4\Phi]+12qU_3[C_4\Phi]+6qU_2[Q_4\Phi]\).
The full drift also includes the displayed linear and upward terms in (11).

For two symmetric pair kernels, (23) has two rows:

\[
\begin{split}
 \frac{d\langle M_2^\Phi,M_2^\Psi\rangle_t}{dt}
 ={}&8\nu q\{U_3[H_1]+U_2[P_{z_1}H_1]\}\\
 &+8\nu q^2\{U_2[H_2]+U_1[P_{z_1}H_2]
                 +U_1[P_{z_2}H_2]+P_{z_1,z_2}H_2\}.
\end{split} \tag{26}
\]

The second row is the extra shared-label contraction. Dropping it would in general be false even at fixed smooth cutoff. If the pair statistic is normalized as \(P_N=U_2/2\), its martingale is \(M_2/2\), its cross-bracket with \(M_k\) is half the corresponding formula, and its self-bracket is one quarter of (26).

### Constant tests and orders larger than \(N\)

For the constant kernel on \(k\) slots,

\[
 c_k:=U_k[1]=\sum_{r=0}^{\min(k,N)}(-1)^{k-r}\binom{k}{r}\frac{(N)_r}{N^r},
 \qquad \sum_{k\geq0}\frac{c_kz^k}{k!}=e^{-z}(1+z/N)^N. \tag{27}
\]

In particular,

\[
 c_0=1,\quad c_1=0,\quad c_2=-q,\quad c_3=2q^2,
 \quad c_4=3q^2-6q^3.
\]

Every drift and martingale kernel above contains a derivative of the test, so both sides of the asserted evolution are zero for this test, although \(c_k\) generally is nonzero. For example, \(N=2,k=3\) gives \(U_3[1]=1/2\), while \(F_3=0\). The centered hierarchy must not be truncated at order \(N\).

There is a stronger check with one unused slot. For any kernel \(H\) on \([k-1]\), splitting the last slot into particle or background and counting its available labels gives

\[
 U_k[H\otimes1]=-q\left((k-1)U_{k-1}[H]
             +\sum_{a=1}^{k-1}U_{[k-1]\setminus\{a\}}[P_aH]\right). \tag{28}
\]

Indeed, if \(r\) other slots use particles, there are \(N-r\) available labels, so the two last-slot contributions sum to \(-rq\) times the original signed term. Counting \(r\) by its particle slots and applying (3) with one forced slot proves (28). For constants it yields \(c_k=-q(k-1)(c_{k-1}+c_{k-2})\), which also follows from (27).

When \(K=0\), all response, upward, and internal-force terms vanish, leaving the independent-diffusion drift \(U_k[(\partial_t+\sum_a(b\cdot\nabla_a+\nu\Delta_a))\Phi]\) and the unchanged Brownian bracket formulas. The proof and direct checker also allow coincident spatial coordinates without identifying their labels.

## 7. Exact independent finite checks

The supporting file is `VERIFICATION_CODE/round002_blind_selfcheck.py`. It uses only Python's standard library and exact pairs of rational numbers to represent Gaussian rationals. It does not numerically approximate derivatives or integrals, use random samples, or import a constructor implementation.

The microscopic side evaluates (1) by all subsets and all particle-label injections, differentiates those terms in particle coordinates, uses the original finite particle drift, and differentiates background Fourier moments from their PDE. The other side evaluates the separately implemented operator and matching expansions. Thus the comparison does not merely compare two printed forms of one implementation.

For reproducibility, use angular variables \(\theta=2\pi x\). The checker sets

\[
 \nu_\theta=3/7,\quad K_\theta(\theta)=\sin\theta+(1/7)\sin(2\theta),
 \quad b_\theta(\theta)=(1/3)\sin\theta+(1/5)\cos(2\theta),
\]

and initial density \(1+c\cos\theta\), \(c=0\) or \(1/2\), relative to normalized angular Haar measure. These are permitted smooth unit-torus data after taking
\(K_x(x)=K_\theta(2\pi x)/(2\pi)\), \(b_x(x)=b_\theta(2\pi x)/(2\pi)\), and \(\nu_x=\nu_\theta/(4\pi^2)\). The corresponding even mean-zero \(g\) and smooth periodic \(V\) are obtained by integration; no singular Riesz normalization is used. The PDE supplies the time derivative at this smooth positive initial density.

Particle phases are \((1,i)\), \((1,i,-1)\), or \((1,1)\). The last choice tests equal coordinates with different labels. Test kernels are explicitly generated real symmetric Fourier polynomials, including a tensor Fourier mode, and all operations are exact. The largest drift order is five and the largest bracket order is four in each block, with \(N=2,3\).

Command:

```text
python3 VERIFICATION_CODE/round002_blind_selfcheck.py > VERIFICATION_CODE/round002_blind_selfcheck_output.json
```

The command completed with exit code zero and output status **PASS**. It checked 20 exact drift equalities, 64 exact bracket equalities, 20 constant equalities, 204 matching-count equalities, and 21,845 finite-cancellation equalities. Python syntax parsing also passed. The noninteracting case is checked analytically above; it is not a separate execution row in this checker. Hashes of this report, the checker and its actual output are recorded in `ROUND_002_ALLORDER_RECONSTRUCTION_SHA256SUMS.txt` next to this report. The report is sealed only after this successful run.

## 8. Adversarial self-review and exact scope

The load-bearing potential failures checked in the derivation are the sign of the response from a background target; the factor \(N^{-1}\) for an already represented force label; the two distinct one-slot force removals; the single two-slot force removal; distinguishing particle-label equality from coordinate equality; differentiating before diagonal restriction; choosing one distinguished Brownian edge among all shared edges; integrating a shared background variable only once; and retaining centered orders above \(N\). Formulas (3), (12)--(13), and the equality-of-label matching proof resolve those points explicitly.

The reconstruction proves the finite smooth identities (7), (11), (15)--(17), and (20)--(23) from the model definitions. It does not certify an existing constructor statement, because no comparison has taken place. The computation is a self-check and a finite falsification attempt, not an independent audit or a substitute for the general proof.

No singular limit, cutoff-uniform backward-kernel estimate, centered residual estimate, Gaussian limit, finite critical truncation, Gibbs bridge, or local-equilibrium statement is asserted. In particular, the old energy-floor condition, full microscopically subcritical regime, and critical effective-coupling regime remain distinct; the identities themselves require none of those asymptotic conditions. The logarithmic normalization is not used. All canonical ledgers and frozen inputs remain unchanged. No commits, pushes, installations, or other-worktree edits were made by this worker.

After the output hashes are issued, this file is immutable. Any correction must be a separately named addendum or superseding report. The next action is the coordinator's comparison against the constructor output, with any discrepancy located in these numbered formulas.
