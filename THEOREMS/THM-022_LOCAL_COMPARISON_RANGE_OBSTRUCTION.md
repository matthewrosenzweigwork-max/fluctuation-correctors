# THM-022 — obstruction to the coefficient-one local radial comparison

2026-09-17. PROVED_CANDIDATE / HOSTILE_REVIEW_PASS (fresh AUD022) / VERSION_LOCKED. Fresh blind reconstruction pending. Proof is the separately corrected V2, hash faa668b30ee77d4826348412c85a936bbbafba22873e9b566d4db788a05fdb95. V1 is preserved as failed Taylor-constant provenance. This card includes the explicit annulus and logical wording qualifications in the separate erratum; it does not alter the proof.

Fix integer d>=1, 0<s<d with s>d-2, N>=2, nu>0, z0 nonzero, and 0<a<r0=|z0|<R<infinity. On D={a<|z|<R}, use the process with generator L=2nu Delta+(2s/N)|z|^-s-2 z.grad, stopped/killed at first annular exit rho. Let j=s|z|^-s and

    F(tau,r)=N/4[(r^(s+2)+2s(s+2)tau/N)^(2/(s+2))-r^2].

For every such fixed tuple there is tau0>0 such that for all 0<tau<tau0,

    E_z0 integral_0^(tau wedge rho) j(Z_h) dh > F(tau,r0).

The time may depend on every fixed parameter and the annulus. No uniform time over these data is claimed. This assertion disproves the coefficient-one extension, and is stronger than its logical negation.

Exact negation of this universally quantified assertion: there exists an admissible tuple for which every epsilon>0 admits tau in (0,epsilon) with the displayed strict inequality false. Equality of stopped path laws and a nonnegative subsequent source would give the same obstruction for any existing global realization; existence is not included. No different majorant, full pair inverse, evolved-law estimate, critical theorem or logarithmic case is disproved.
