# THM053 — first-collision exit measure of the killed attractive dual

2026-09-18 UTC. OPEN / UNAUDITED / VERSION_LOCKED. PO040. Auxiliary-law subgate; neither an original-flow collision assertion nor a critical-decay theorem. Fix every integerN>=2 and finite nu>0 in the precise coefficient-one d4 periodic Coulomb model of THM052. Use H=N^-1 sum_(i<j)g, c=4pi²,kappa=c(N-1), attractive maximal path dY=+gradH(Y)dt+sqrt(2nu)dW on Omega from iid Haar independent of noise, lifetime zeta. The process is killed at zeta and is not continued or given an entrance rule. For i<j, let m_ij be probability measure on the collision diagonal obtained by choosing one Haar point for the common i,j coordinate and independent Haar points for the otherN-2coordinates.

(A) The full drift has finite stopped lifetime action in first power, exactly

    E integral_0^zeta |gradH(Y_s)| ds = kappa^-1 integral_Omega |gradH(x)| dx < infinity.

The path has a limit Y_(zeta-) in the compact configuration torus almost surely. That limit is a collision configuration; this asserts no continuation beyond it. The norm is the full4N-coordinate Euclidean norm, not a sum of squared individual forces. The finite constants can depend onN,nu; no thermodynamic uniformity is stated.

(B) Almost surely precisely one unordered pair of coordinates coincides at that limiting configuration, and all other coordinates are distinct from one another and from that pair. Denote this unique pair by I. For every pair i<j and every bounded Borel function phi on(0,infinity) times (T4)^N,

    E[1_(I={i,j}) phi(zeta,Y_(zeta-))]
      =(2c/N) integral_0^infinity exp(-kappa t) integral phi(t,x) dm_ij(x) dt.

The same formula holds for nonnegative Borel functions, with extended expectations. Thus the lifetime is exponential of ratekappa, independent of(I,Y_(zeta-)); I is uniform among all N(N-1)/2 unordered pairs; conditional on I={i,j}, the terminal configuration has exact m_ij law. The exit-time density, unordered-pair coefficient2c/N and all marked conclusions are part of the claim. AtN2 there is only one pair. No point-start version is asserted.

Exact negation is any admitted finiteN,nu violating existence/integrability/limit in(A), uniqueness of the collision mark in(B), or the stated identity for any admitted test. A formal generator-adjoint or missing-boundary computation, a smooth-cutoff surrogate with no real collision, or an unproved simultaneous-collision exclusion is not a proof. The full distributional identity Delta H=kappa dx-(2c/N)sum_(i<j)m_ij must retain its atom and compensation. Existing killed-duality claim can be used only with its exact domain/source status or a reconstructed justification. Original THM046/PO033 remains OPEN; no corrected Gaussian/hierarchy theorem follows.
