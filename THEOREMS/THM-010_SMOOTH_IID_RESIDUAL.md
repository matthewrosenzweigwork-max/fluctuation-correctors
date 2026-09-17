# THM-010 — fixed-smooth iid corrector residual

Version 1.0, 2026-09-17. Mathematical status PROVED_CANDIDATE; audit status SELF_CHECKED at submission. Frozen statement for independent comparison and hostile review. Later verdicts belong in the theorem ledger; do not rewrite this submitted card.

## Statement and negation

Use exactly the fixed-smooth gradient diffusion, probability reference, iid initial law, mean-field centering, ordered distinct-label N^k normalization, full backward one-body and pair operators, and uniform C^(4d+12) hypotheses in TASKS/ACTIVE/PO-001_RESIDUAL.md. For every N>=2 and beta>0 set sigma=sqrt(N) min(sqrt(beta),1), P=U_2/2, and F=C Phi with averaged six-term symmetrization.

There are finite constants independent of N,beta, explicitly in MEMORANDA/ROUND_002_COUPLING.md (2.1)–(2.4), such that

- E|P[Phi_0]| <= I/N;
- E integral_0^T |U_3[C Phi_t]| dt <= T C_3/N^(3/2);
- E[M_Phi]_T <= 2 T H^2/(beta N^2);
- E TV_[0,T]([M_f,M_Phi]) <= 2 T L_f H/(beta N^(3/2)).

Consequently the first two quantities multiplied by sigma and the latter two multiplied by sigma^2 vanish for every temperature sequence beta_N>0. The lower drift contractions have integrated absolute size at most 5 T d kappa_0 A_1/N. The quantities are absolute estimates under the actual interacting law, not signed mean cancellation or an evolved iid assumption.

Exact negation: permitted data and parameters violate one stated estimate with its displayed constants, or a permitted sequence satisfying the uniform norms has nonvanishing limsup for one of the scaled targets. The constructor proof excludes this negation using empirical negative-Sobolev moments and exact diagonal deletion. A separate independent construction/comparison is pending at submission.

## Dependencies, limitations, and proof

Fixed finite horizon, fixed smooth even g and smooth V, Brownian motions independent of the iid initial positions, and deterministic smooth backward tests as in the task. The proof does not require uniform derivatives of the background beyond the task's assumptions and in fact displays a weaker sufficient test regularity, but this card does not amend the frozen target.

Proof: MEMORANDA/ROUND_002_COUPLING.md, especially (4.9), (5.2), (5.5), (6.1), and (7.7). New root lemma MEMORANDA/ROUND_002_UNIFORM_SMOOTH_DATA.md separately qualifies the uniform norm assumption for fixed smooth data; it requires its own review and is not silently folded into this submitted theorem.

This is the fixed-smooth iid subclaim of PO-001. Its singular version, other preparations, critical power counting, limiting covariance and law, field/path tightness, and cutoff/model comparison remain separate. No old energy-floor exponent or microscopic-coupling exponent changes. No private or unverified literature theorem is used.
