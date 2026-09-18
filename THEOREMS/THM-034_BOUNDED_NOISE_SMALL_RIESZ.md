# THM-034 — full bounded-diffusivity actual noise for small Riesz exponents

2026-09-18 UTC. ROOT PROVED_CANDIDATE / SELF_CHECKED at freeze. Fresh statement-only reconstruction and hostile review required. This is an additional sufficient range, not a change to the campaign mission or a claim about the cubic residual.

Fix integer d>=4, 0<s<2, finite T, smooth real terminal h and finite nu_*. For N>=2 and 0<nu<=nu_*, take the true homogeneous terminal-zero full pair inverse with both responses, the R7 weights w_q=w_1^q, actual singular particles from iid unit Haar independent of their Brownian drivers, zero external drift, K=-grad g, literal ordered deleted-pair P_N=U2/2 and mean-field centering. Set p=s+2, a=s/p, theta=1-s/d, beta=1/nu, b_N=min(beta,1), sigma_N^2=N b_N. Constants depend only on fixed displayed data and fixed kernel/weights, not N or selected nu.

For every fixed 1<q<min(d-2,d/2) with q<=s+1 and eta=s+1-q<2, prove

    sup_t |grad_pair Phi_t|/w_q
       <=C_q min(N^(eta/p),nu^(-eta/2)).

Here eta>=0 by hypothesis. No bounded-chi restriction is imposed. With q=p/2, prove for the genuine scaled actual corrector bracket

    Q_N<=C b_N min(N^a,nu^(-s/2))(N^-theta+nu).

The full conclusion is

    sup_(0<=nu<=nu_*) Q_N -> 0 as N->infinity.

At nu=0 define Q_N=0 directly from its noise coefficient. Uniformity includes nu depending arbitrarily on N; it does not rely on nu tending to zero or staying bounded away from zero. A quantitative sufficient bound, for all sufficiently large N, is

    Q_N<=C[ N^(a-theta)+N^(-(2-s)/(12p^2))
            +N^(-s/(4p(s+4)))+N^(-1/(2p))+N^(-2/p) ].

The actual leading scaled martingale bracket remains bounded and the expected integral of absolute scaled cross-variation tends uniformly to zero. Earlier fixed-N domain/particle results and the exact R10 energy floor and clipping theorem are conditional prerequisites as issued; their current unseen audit status is not an input.

Exact negation: an admitted fixed tuple and a sequence N->infinity, nu_N in[0,nu_*] violate a uniform stated bound or give positive limsup Q_N; or an admitted weighted estimate fails for every N/nu-independent constant. Required restrictions include d>=4, strict s<2, the actual homogeneous law, bounded nu, and the full pair inverse. No d=3, Coulomb, s=2 endpoint, unbounded diffusivity, general background, logarithmic interaction, cubic drift residual, higher hierarchy or fluctuation law follows. The old energy-floor, full microscopic subcritical and positive finite critical conditions retain their distinct exponents.
