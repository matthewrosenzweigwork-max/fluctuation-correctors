# Round023 — a static threshold obstruction to an energy-only source estimate

2026-09-18 UTC. ROOT CONSTRUCTION / SELF_CHECKED / VERSION_LOCKED. Entire THM045 and its exact negation are frozen separately. This concerns a precisely specified static class. It does not produce a counterexample to iid-prepared singular dynamics, a Gaussian limit, or the higher-corrector mission. Root is exposed to the earlier campaign and cannot certify this construction independently.

## 1. Kernel and statistic at the four-dimensional Coulomb threshold

Work on T^4 with Haar mass one and the exact THM045 normalization. The full R4 heat proof, at d=4,s=2, gives

    g(x)=4 pi^2 integral_0^infinity [p_t(x)-1]dt,
    g_hat(k)=|k|^-2 (k!=0), g_hat(0)=0,
    g(x)=|x|^-2+H(x) locally, H smooth and even,
    div K=4 pi^2(delta_0-dx), K=-grad g.

The local expansion and compactness away from zero imply |D^j g(x)|<=C_j(1+dist(x,0)^(-2-j)) for every fixed j. In particular K is Haar L1. For every smooth h the symmetrized J_h is bounded in absolute value by C_h(1+dist(x,y)^-2), hence is genuinely Haar integrable. Integrating K by parts against a smooth test uses the full compensated divergence measure, and gives

    j_h(x):=integral J_h(x,y)dy=-4 pi^2(h(x)-integral h),
    integral j_h=0.

For h=cos(4pi x_1) the literal original statistic is therefore

    P_N[J_h]=(2N^2)^-1 sum_(i!=j)J_h(x_i,x_j)+4pi^2 eta_N[h].       (1.1)

No singular diagonal value is assigned. All subsequent configurations stay a positive distance from collisions at each fixed N.

## 2. The lattice regular part is strictly negative

Write H0=H(0). Subtract the central Euclidean heat kernel before letting x tend to zero in the R4 formula. The nonzero image sum at small times is exponentially small after multiplication by any fixed inverse power of t. At large times, p_t(0)-1 decays exponentially and the Euclidean kernel is integrable since dimension4. These majorants justify the limit and yield

    H0=4pi^2 integral_0^infinity [p_t(0)-1-(4pi t)^-2]dt
      =pi integral_0^infinity [Theta(v)^4-1-v^-2]dv,               (2.1)
    Theta(v)=sum_(n in Z) exp(-pi v n^2), v=4pi t.

Both the Fourier and the image expression of the same periodic Gaussian give Theta(v)=v^-1/2 Theta(1/v); thus no additional summation theorem is imported. Substituting v=1/u in the portion(0,1) shows that the two portions of (2.1) are equal. Nonnegative termwise integration on(1,infinity) then gives

    H0=2pi [sum_(k in Z^4\{0}) exp(-pi|k|^2)/(pi|k|^2)-1].       (2.2)

Here is an explicit strict bound. Since pi>3 and the first nine nonnegative Taylor terms of exp(3) already exceed20, exp(-pi)<1/20 and exp(-3pi)<1/8000. For n>=1, n^2>=1+3(n-1). Consequently

    Theta(1)<1+2(1/20)/(1-1/8000)=8799/7999,
    2*8799^4<3*7999^4.

It follows that Theta(1)^4-1<1/2. Since |k|^2>=1 for nonzero integer k, the positive sum in (2.2) is less than1/(2pi)<1/6. In particular

    H0<-5pi/3<0.                                                (2.3)

The proof needs only negativity, not an asserted optimal lattice energy or a numerical evaluation of H0.

## 3. Exact grid energy and uniform deformation estimates

Let G_m=(m^-1 Z/Z)^4, N=m^4, m>=5. The distributional Fourier coefficients of sum_(y in G_m)g(x-y) vanish except at frequencies mk, where they equal m^4|mk|^-2=m^2|k|^-2. Thus

    sum_(y in G_m)g(x-y)=m^2 g(mx)                              (3.1)

as distributions. Both sides are smooth away from G_m, so the equality holds pointwise there. Let x approach0, subtracting the identical |x|^-2 singularity. Equation(3.1) gives

    sum_(y in G_m,y!=0)g(y)=(m^2-1)H0,
    H_N(G_m)=(1/2)(m^2-1)H0.                                  (3.2)

Every grid particle has zero force: the displacement multiset is invariant under z->-z, K is odd, and points satisfying z=-z on the torus have K(z)=0. Therefore the first derivative of grid energy vanishes in every smooth deformation direction.

Use v(x)=sin(2pi x_1)e_1 and T_epsilon(x)=x+epsilon v(x) modulo the torus. Choose epsilon0>0 with epsilon0 Lip(v)<1/4. The first-coordinate derivative stays positive, and the periodic lift has degree one; hence T_epsilon is a smooth torus diffeomorphism for |epsilon|<=epsilon0. Shortest-distance triangle inequalities, applied also to every lift, give

    (1-Lip(v)|epsilon|)dist(x,y)
       <=dist(T_epsilon x,T_epsilon y)
       <=(1+Lip(v)|epsilon|)dist(x,y).                         (3.3)

Represent x-y by a shortest lift. Then |v(x)-v(y)|<=Lip(v)dist(x,y). Differentiating the pair energy twice along this linear-in-epsilon deformation gives

    |partial_epsilon^2 g(T_epsilon x-T_epsilon y)|
       <=C(1+dist(x,y)^-2).                                  (3.4)

All constants in this section are independent of m,epsilon. The needed grid bound is

    (1/N)sum_(z in G_m,z!=0)(1+dist(z,0)^-2)<=C.                (3.5)

Indeed choose representatives j with |j_l|<=m/2. The number with n<=|j|<n+1 is at most C(n+1)^3, by covering their disjoint unit cubes by a thick annulus in R^4. Thus m^-4 sum_(0<|j|<=Cm)(|j|/m)^-2<=C, with the finitely small shells included. The same argument gives the useful uniform tail

    (1/N)sum_(0<dist(z,0)<=delta)dist(z,0)^-2<=C delta^2         (3.6)

for delta>=1/m, and zero for delta<1/m. Boundary choices of shortest representatives only affect the fixed constants.

Equations(3.4)–(3.5) imply |d^2 H_N(T_epsilon G_m)/d epsilon^2|<=C_E N. Together with the zero first derivative and(3.2), for epsilon=a/m,

    H_N(T_(a/m)G_m)<=(H0/2)(m^2-1)+(C_E/2)a^2 m^2.

Choose once a>0 so small that a<=epsilon0 and (C_E/2)a^2<=|H0|/8. Since m>=5, this is at most -c_E m^2 for a fixed c_E>0. Equation(3.3) also gives minimum pair distance at least3/(4m). This construction does not presume an actual dynamical evolution of the grid.

## 4. Second-order source expansion with a uniform remainder

Let F_m(epsilon)=P_N[J_h](T_epsilon G_m), with the exact expression(1.1). For j=0,1,2,3,

    |partial_epsilon^j J_h(T_epsilon x,T_epsilon y)|
       <=C(1+dist(x,y)^-2).                                  (4.1)

To justify this uniformly, an l-th epsilon derivative of K contributes D^l K evaluated at the deformed displacement times l factors v(x)-v(y). Its size is at most C dist(x,y)^-3. Each remaining derivative of the gradient difference is a difference of values of the smooth function D^(j-l+1)h(T_epsilon x)[v(x)^(j-l)] at x and y; its Lipschitz norm is uniformly bounded, so its magnitude is at most C dist(x,y). The product has precisely the bound(4.1). Smooth far-field terms are harmless. Formula(3.5), and the smooth row in(1.1), give sup_m,|epsilon|<=epsilon0 |F_m'''(epsilon)|<infinity.

At zero, F_m(0)=0 and F_m'(0)=0 for every m>=5. Here is an exact frequency argument which includes the row. The undeformed statistic is a translation-covariant linear functional of h. Relabeling the full grid by a in G_m leaves it unchanged, while replacing h(x) by h(x+a) multiplies a complex test of frequency k by exp(2pi i k.a). The nonzero frequencies of h are +/-2e_1, so its undeformed statistic vanishes. The first variation is bilinear in h and v, translation covariant under simultaneous translation of those two inputs. Its frequencies are +/-2e_1 plus +/-e_1, namely +/-e_1,+/-3e_1. None is in m Z^4 for m>=5. Averaging the simultaneous translates over G_m therefore proves the first variation vanishes, including the differentiated row term. This argument uses only a finite sum and smooth differentiation away from the grid diagonal.

For fixed epsilon, define the continuum comparison with independent x,y Haar:

    F_infty(epsilon)=(1/2)integral J_h(T_epsilon x,T_epsilon y)dxdy
                       +4pi^2 integral h(T_epsilon x)dx.

It is three times differentiable by(4.1) and Haar integrability. The off-diagonal grid Riemann sums for its second derivative at zero converge to the continuum integral. Explicitly, remove dist(x,y)<delta using(3.6) and its Haar integral counterpart, both bounded by C delta^2. On the remaining compact region the differentiated integrand is continuous; a continuous cutoff can be inserted, and usual product-grid Riemann sums converge. Let delta decrease to zero. The row Riemann sums converge directly. Therefore

    F_m''(0)->F_infty''(0).                                  (4.2)

Let mu_epsilon=(T_epsilon)#dx and rho_epsilon=mu_epsilon-dx. The inverse function and change-of-variables formula, with uniformly positive Jacobian, imply in every fixed C^j norm

    rho_epsilon(x)=-epsilon div v(x)+O(epsilon^2)
                 =-2pi epsilon cos(2pi x_1)+O(epsilon^2).       (4.3)

The same expansion follows directly by differentiating the identity T_epsilon^-1(T_epsilon x)=x and the reciprocal Jacobian, so no weak-to-strong density inference is used. Since K is L1 and the densities/tests smooth, the original row subtraction gives the exact equality

    F_infty(epsilon)=(1/2)integral J_h(x,y)rho_epsilon(x)rho_epsilon(y)dxdy
                    =integral rho_epsilon grad h.(K*rho_epsilon).    (4.4)

For rho=A cos(theta), theta=2pi x_1, coefficient g_hat(e_1)=1 gives K*rho=2pi A sin(theta)e_1. Also grad h=-4pi sin(2theta)e_1. Since integral cos(theta)sin(theta)sin(2theta)=1/4, (4.4) equals -2pi^2 A^2. Substituting A=-2pi epsilon in(4.3), with the bilinear L-infinity bound supplied by K in L1, yields

    F_infty(epsilon)=-8pi^4 epsilon^2+O(epsilon^3),
    F_infty''(0)=-16pi^4.                                    (4.5)

Uniform Taylor remainder and(4.2) now prove the discrete limit at the moving deformation scale, rather than assuming a continuum approximation uniform in that scale:

    m^2 F_m(a/m)=(a^2/2)F_m''(0)+O(a^3/m)->-8pi^4 a^2.        (4.6)

This order of arguments is essential: a zeroth-order grid Riemann-sum convergence would not by itself control the m^2-scaled error.

## 5. Exact Haar/exchangeable law and positive absolute limit

Start with the deformed grid configurations of Sections3–4. Add one uniform common translation Y in T^4 and a uniform random permutation of the N labels. The resulting law is exchangeable and common-translation invariant, with exactly Haar one-body marginals. Energy and minimum separation are unchanged. It is initially an atomic-orbit law, which will be smoothed in Section6.

For any configuration x, common translation satisfies P_N[J_h](x+Y)=P_N[J_(h(.+Y))](x), because K uses only displacements and Haar is translation invariant. Put h_c=cos(4pi x_1),h_s=sin(4pi x_1), and C=P_N[J_hc](x),S=P_N[J_hs](x). Consequently the translated statistic is C cos(4pi Y_1)-S sin(4pi Y_1), and

    E_Y|P_N[J_hc](x+Y)|=(2/pi)sqrt(C^2+S^2).                  (5.1)

The deformed grid is invariant under inversion x->-x since v is odd. K is odd and grad h_s is even, so the raw h_s source changes sign under inversion; its row h_s also changes sign. Therefore S=0 for that grid, while C=F_m(a/m). Equations(4.6) and(5.1), with sqrt(N)=m^2, give exactly

    sqrt(N)E|P_N[J_h]|->16pi^3 a^2>0.                        (5.2)

The signed expectation is zero by common translation. Its vanishing does not imply the absolute estimate in(5.2) vanishes.

## 6. Bounded smooth N-body densities without changing the limit

The assertion requires smooth densities, not just the preceding orbit law. For each m, the deformed grid has minimum separation at least3/(4m), and H_N<=-c_E m^2. On a compact sufficiently small product neighborhood of this configuration, energy and both C,S in(5.1) are continuous because there are no collisions. Choose a positive delta_m<1/(16m) so that arbitrary individual displacements of size at most delta_m preserve

    minimum separation>=1/(2m),
    H_N<=-(c_E/2)m^2,
    |C-F_m(a/m)|+|S|<=m^-3.                                 (6.1)

Such a delta_m exists by uniform continuity at each finite-dimensional compact neighborhood. No lower bound on delta_m uniform in m or uniform density estimate is asserted or needed. Choose a nonnegative C-infinity probability bump supported in the ball of radius delta_m, and displace each labelled grid point by an independent draw. Then independently add common Haar translation and randomize the labels as in Section5.

The product bump has a bounded smooth density on (T^4)^N. Translation averaging and the finite permutation average preserve smoothness, nonnegativity, unit mass and boundedness at each fixed N: all derivatives can be passed through the compact translation integral using their fixed-N finite suprema. The resulting F_N is exchangeable and common-translation invariant, hence has exact one-body Haar marginals. All configurations in its support, including closure points, obey(6.1), since those inequalities were imposed on a closed product neighborhood and are invariant under translations/permutations.

The Euclidean norm is Lipschitz with constant one. Thus (6.1) and(5.1) change the expected absolute source, relative to the unsmoothed orbit law, by at most (2/pi)m^-3. Multiplication by m^2 makes the change tend to zero. Equation(5.2) remains exact. With c=min(1/2,c_E/2), all support/energy requirements of THM045 follow for every sufficiently large m, with the same fixed a,c.

Every random source is bounded for each fixed N because its support stays away from collisions. Haar source/background contractions were justified before constructing the law. No singular regularization, diagonal extension, stochastic generator claim or unproved limiting integrability has been used.

## 7. Falsification checks and exact logical consequence

The proof route was challenged at the sign of H0, the grid self subtraction, first-variation selection, the strength of the moving-scale Riemann approximation, scalar/row coefficients, random-translation centering, and smooth-density support. Equations(2.1)–(2.3) prove the sign without a guessed lattice-energy value. Equation(3.2) subtracts the identical coefficient-one singularity. The derivative identities eliminate lower-order lattice errors before the m^-1 deformation is inserted. Uniform third derivatives and the integrable differentiated diagonal tail supply the quantitative moving-scale passage. Formula(5.1) keeps signed and absolute expectations distinct. Section6 completes the density requirement with an error strictly smaller than m^-2.

The new supporting exact diagnostic tests the integer/Taylor theta bounds, grid Fourier selection, the continuum coefficient via rational Fourier algebra, all deleted/Haar factors in an exactly solvable smooth probe, and explicit mutations. Those finite calculations cannot establish the infinite-lattice sign, continuum singular Riemann limit or smooth law construction; these are proved above and require two fresh independent gates.

If accepted, THM045 shows that exact Haar one-body centering, exchangeability, bounded smooth finite-N densities, microscopic separation and even a pointwise strictly negative energy of the sharp floor order do not alone imply sqrt(N) E|P_N[J_h]|->0 at d4,s2. The deterministic/energy-only estimate has order one there. It does not imply failure of an integrated source estimate, nor failure for the actual iid-prepared evolved law: the constructed static laws are not claimed to be those laws. Additional dynamical/correlation/corrector information remains a legitimate route for the campaign. None of the three beta/lambda regimes, normalizations or larger scientific targets is changed.

Executed supporting diagnostic:1549 exact assertions across24 categories;10 detecting coefficient/scale mutations. A smooth two-mode Fourier pullback independently matches the density calculation. No finite test certifies the singular analytic construction. Fresh independent gates remain pending.
