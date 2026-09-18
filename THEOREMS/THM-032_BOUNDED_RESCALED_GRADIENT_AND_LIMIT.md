# THM-032 — uniform spatial bounds and full-kernel limit at bounded rescaled diffusivity

2026-09-18 UTC. PROVED_CANDIDATE / SELF_CHECKED at submission. Exact scope of sealed TASK063 Sections1–8, with the diagnostic and exclusions in Sections9–10 preserved. No actual-law tail implication is claimed.

Fix d>=3,0<s<=d-2,T finite,L finite,smooth real terminal h,unit Haar,zero external drift,mu=1 and the frozen K=-grad g. For every N>=2 and0<=nu<=L N^(-2/(s+2)), use the existing symmetric terminal-zero bounded Borel full inverse Phi^(N,nu), with both exact compensated responses and the actual backward Fourier test f^nu. Fixed positive periodic weights w_s,w_(s+1) equal the respective inverse powers of distance near the diagonal.

Prove uniformly in N,nu and t:

    sup_(x!=y) |Phi_t^(N,nu)|/w_s + sup_(x!=y)|grad_pair Phi_t^(N,nu)|/w_(s+1) <= C.

The same full inverse has jointly continuous off-diagonal value and spatial first derivatives, which are its global weak derivatives. Its Haar W1,1 norm is uniformly bounded. Its contracted first gradient A_t(x)=integral grad_x Phi_t(x,y)dy is continuous, uniformly bounded, and is the classical gradient of the value projection.

Let R be the full response and J_t^0 the source of the actual zero-diffusion Fourier test. Define

    Phi_t^0=integral_0^(T-t) exp(r R) J_(t+r)^0 dr.

Prove this is the unique solution of the response-only terminal equation in the uniformly weighted-value class from the complete report. It is symmetric, continuous with continuous spatial derivatives off diagonal, a global weak W1,1 representative, and need not be bounded at the diagonal. The exponential and time equation have the exact weighted-space meanings stated in the report.

As N->infinity, prove uniformly over0<=nu<=L N^(-2/(s+2)) and0<=t<=T: Phi^(N,nu)->Phi^0 in C1(H) for every compact H strictly off the diagonal, and in global Haar W1,1. Contracted values and first gradients converge uniformly in t,x,nu. No common exceptional set over all noise parameters is required; every claimed supremum/norm must have its stated quantifiers and justified passage.

Exact negation: admitted fixed data and a bounded-rescaled-diffusion sequence violate a uniform bound, actual/weak derivative or contraction assertion, or either stated convergence. Include T=0,L=0,nu=0,Coulomb compensation and both response coefficients1. No H1 conclusion from the displayed weight, diagonal trace, weighted-supremum convergence near the shrinking diagonal, second/time-derivative convergence, actual evolved bracket, residual, fluctuation law or hierarchy closure. Every microscopic critical sequence eventually lies in a bounded-rescaled-diffusion class; general full subcriticality is not replaced by that auxiliary condition.
