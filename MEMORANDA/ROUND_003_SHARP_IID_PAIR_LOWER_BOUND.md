# Round 003: a rare-pair lower bound and sharp initial iid criterion

2026-09-17. Root Astra Ultra construction, following the two sealed iid reports. Mathematical status PROVED_CANDIDATE; audit SELF_CHECKED only until a separate referee issues a verdict. This is a new claim, THM-019, not a retroactive strengthening of either constructor's report. THM-017 is reserved for the separately assigned internal-pair transport model; THM-018 for the independent reconstruction's separate L1 upper bound.

The claim concerns only the bare mean-zero torus Riesz pair under initial iid Haar preparation, not the actual backward corrector or singular interacting law. No stable law or critical dynamic theorem is asserted. The root may not certify this construction.

## 1. Exact assertion and prerequisites

Fix an integer d>=1 and d/2<s<d. Use the coefficient-one local Riesz representative g proved from the frozen heat/Fourier normalization in the sealed collision report (hash 9e39bf83b9f8073bf5d31f33bdc26a31af563af5fe5316ed5399ea1d48eff8f4). Let X_1,...,X_N be iid Haar and

    P_N[g] = N^(-2) sum_(i<j) g(X_i-X_j),  N>=2.

For all sufficiently large N there exist positive finite constants a,p,C depending only on d,s such that, with u_N=N^(2s/d-2),

    P{P_N[g] >= a u_N} >= p,
    ap u_N <= E|P_N[g]| <= C u_N.                    (1)

Consequently, for every positive beta_N, b_N=min(beta_N,1), sigma_N=sqrt(N b_N), and A_N=b_N N^(4s/d-3),

    sigma_N P_N[g] -> 0 in probability
    if and only if A_N -> 0,

and the same condition is equivalent to convergence to zero in L1. If A_N is unbounded along a subsequence, the scaled family is not tight. If A_N is bounded, the L1 upper bound implies tightness. These are assertions about the diagnostic pair statistic, not the campaign's full fluctuation field.

Exact negation: fixed admissible d,s and an iid Haar sequence violate one of (1) or its stated consequences. We prove (1) using a second-moment bound for a close-pair count, a centered truncated pair variance, and the positive principal singularity. There is no inference from an infinite untruncated variance.

The needed proved local facts are: g has zero mean, is integrable, and there exist R in (0,1/4) and constants C_tau,C_V>0 such that for 0<r<R,

    g(z) >= (1/2)|z|^(-s) for 0<|z|<R,
    0 < tau_r := integral_(|z|<r) g(z) dz <= C_tau r^(d-s),
    V_r := ||g 1_(|z|>=r) + tau_r||_2^2
             <= C_V r^(d-2s).                     (2)

These follow from g(z)=|z|^(-s)+a smooth local remainder and polar integration. Choose R small enough that the bounded remainder has absolute value at most |z|^(-s)/2 inside R. The outer fixed-region squared integral is finite; since d-2s<0, it can be absorbed into the displayed V bound after enlarging C_V. The existing collision report proves these facts without an external source theorem. The exact iid canonical-pair variance is (N-1)V_r/(2N^3), as separately reconstructed in both reports.

## 2. A close pair has a fixed positive probability at the minimum-distance scale

For N large enough that R_N=N^(-2/d)<R, fix delta in (0,1), to be chosen below, and let Z_N count the unordered pairs at distance less than delta R_N. Write M=N(N-1)/2, let v_d be the Euclidean unit-ball volume, and let

    q_N=v_d delta^d/N^2,
    m_N=E Z_N=M q_N.

The torus balls are embedded because delta R_N<R<1/4. Any two distinct pair indicators are independent in pairs. Disjoint pairs use independent labels. If the pairs share one label, conditioning on that uniform label gives independent remaining positions and the same constant conditional ball probability q_N; thus their joint expectation is q_N^2. Mutual independence of all pair events is neither true nor required.

It follows that

    E Z_N^2 = m_N + M(M-1) q_N^2 <= m_N+m_N^2.

Cauchy--Schwarz applied to Z_N 1_(Z_N>0) gives

    P(Z_N>0) >= m_N^2/E Z_N^2 >= m_N/(1+m_N).

For N>=2, v_d delta^d/4 <= m_N <= v_d delta^d/2. Therefore

    P(Z_N>0) >= c_0 delta^d,
    c_0 := v_d/[4(1+v_d/2)] > 0.                 (3)

This is an elementary fixed positive lower bound for a fixed delta; it does not invoke a Poisson or extreme-value limit.

## 3. Separate the positive inner contribution from the outer fluctuation

Define the centered outer kernel k_R=g 1_(|z|>=R_N)+tau_(R_N). It has mean zero, so P_N[k_R] is the canonical deleted pair. The identity, on every configuration without collisions, is

    P_N[g] = P_N[k_R]
             + N^(-2) sum_(i<j) g(X_i-X_j) 1_(dist<R_N)
             - (N-1) tau_(R_N)/(2N).            (4)

All terms in the inner sum are nonnegative by (2). On {Z_N>0}, at least one of them is at least (1/2)(delta R_N)^(-s). Since N^(-2)R_N^(-s)=R_N^(d-s)=u_N, (2) and (4) give

    P_N[g] >= P_N[k_R]
                 + (delta^(-s)/2-C_tau/2)u_N.   (5)

Choose delta small enough that delta^(-s)>=2 C_tau. Then the last deterministic coefficient is at least delta^(-s)/4. The outer variance satisfies

    Var(P_N[k_R]) = (N-1)V_(R_N)/(2N^3)
                      <= (C_V/2)u_N^2.          (6)

Chebyshev therefore gives

    P{P_N[k_R] < -delta^(-s)u_N/8}
                      <= 32 C_V delta^(2s).     (7)

Because 2s>d, delta can be chosen, once and for all, small enough to satisfy both the preceding mean condition and

    32 C_V delta^(2s) <= (c_0/2)delta^d.

For example any positive delta<1 with delta^(-s)>=max(1,2 C_tau) and delta^(2s-d)<=c_0/(64 C_V) works. No relation between the outer event and the close-pair event is presumed. Subtract the probability in (7) from (3), and use (5). This proves

    P{P_N[g] >= delta^(-s)u_N/8}
                      >= (c_0/2)delta^d.        (8)

Thus a=delta^(-s)/8 and p=c_0 delta^d/2 prove the first part of (1); ap u_N is the corresponding lower bound on the first absolute moment. Constants depend only on the fixed d,s and its fixed Riesz kernel. They are independent of N and beta_N.

## 4. Matching first-absolute-moment upper bound

This section recomputes an elementary upper bound; the independent statement-only route has separately announced the same consequence and must seal its own proof before comparison.

Let l_R=g 1_(|z|<R_N)-tau_(R_N), so g=k_R+l_R and both kernels are mean zero. The canonical outer pair has, by (6),

    E|P_N[k_R]| <= sqrt(C_V/2) u_N.

The inner kernel is integrable, though generally not square-integrable. Its L1 norm is at most 2 tau_(R_N), since g is positive within this ball. Directly summing the absolute values of the unordered pair evaluations gives

    E|P_N[l_R]| <= (N-1)||l_R||_1/(2N)
                    <= tau_(R_N) <= C_tau u_N.

The triangle inequality proves the second upper bound in (1) with C=sqrt(C_V/2)+C_tau. It holds for all sufficiently large N, without first assuming any asymptotic temperature condition. No covariance expansion of an infinite-variance random variable occurs.

## 5. Necessary and sufficient condition, and exact scope

Multiplying (1) and (8) by sigma_N gives

    ap sqrt(A_N) <= E|sigma_N P_N[g]| <= C sqrt(A_N),
    P{sigma_N P_N[g] >= a sqrt(A_N)} >= p.        (9)

If A_N->0, the upper bound proves L1, hence probability, convergence to zero. If A_N does not tend to zero, a subsequence has A_N>=epsilon>0. On that subsequence the probability of exceeding a sqrt(epsilon)/2 is at least p, contradicting probability convergence to zero. This proves the equivalence with no uniform-integrability assumption.

If A_N is unbounded along a subsequence, for every fixed threshold L the lower event in (9) eventually exceeds L along that subsequence, with probability at least p. No uniform tightness bound with error less than p is then possible. If A_N is bounded, the upper bound and Markov's inequality give tightness for all sufficiently large N; the finitely many initial integrable random variables do not affect tightness of the sequence.

In particular at sqrt(N) scale, s<3d/4 gives vanishing (the case s<=d/2 was already proved separately); s=3d/4 gives a tight sequence that does not tend to zero; and s>3d/4 gives a non-tight sequence. No limiting distribution at the boundary is identified here. For the frozen microscopic critical beta_N~lambda N^(1-s/d), b_N is eventually one, but these diagnostic conclusions are not a theorem about the actual full critical fluctuation observable or its corrector.

The counterexample to vanishing is a probability lower bound for the bare iid pair, not a failed variance test. The missing actual backward-kernel estimate is untouched; its internal transport may change the singularity. TASK-025 explicitly tests that possibility in a separately declared solvable model. No positive-time law, response/diffusion estimate, field tightness, logarithmic case or singular model-comparison gate is closed by the present result.
