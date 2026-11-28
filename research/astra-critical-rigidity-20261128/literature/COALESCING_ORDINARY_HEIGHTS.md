# Coalescing Brownian paths from actual families of Collatz integers

Let \(T\) be the shortcut map, \(t=\lfloor\log_2 N\rfloor\), \(\gamma=\log_2 3\), and \(b=1-\gamma/2\). Fix \(d\). For each \(N\), take nonnegative integer exponents and integer offsets such that
\[
   s_i/\sqrt t\longrightarrow a_i,\qquad
   0\le a_1<\cdots<a_d<\infty,\qquad
   \max_i\log(2+|D_i|/3^{s_i})=o(t).
\]
Choose \(x\) uniformly in any interval of \(N\) consecutive positive integers on which every \(x_i=3^{s_i}x+D_i\) is positive. Write \(g_i(k)\) for the actual odd count of \(x_i\) up to native shortcut date \(k\). Linearly interpolate each process between its displayed mesh values. Both families
\[
  W_i(k/t)=\frac{s_i+g_i(k)-k/2}{\sqrt t},\qquad
  Y_i(k/t)=\frac{\log_2(T^k x_i)-\log_2 x+bk}{\gamma\sqrt t},
     \quad 0\le k\le t,                                                    \tag{1}
\]
converge jointly in \(C([0,1])^{2d}\) to two copies of the **same** finite system of coalescing Brownian paths started at \(a_1,\dots,a_d\). Each distinct path moves with variance rate \(1/4\). Before any two live paths meet, they move as independent Brownian motions, and paths that meet stay together. The convergence holds along every choice of the interval positions.

Jointly with (1), all actual first numerical meeting times divided by \(t\), capped at 1, converge to the correspondingly capped Brownian meeting times. At every fixed positive observation time through 1, the actual partition by equality converges jointly with the paths to its Brownian partition. For instance at time 1 the limiting probability that three specified arms are all distinct is
\[
    H(a_2-a_1)+H(a_3-a_2)-H(a_3-a_1),\qquad H(y)=2\Phi(\sqrt2 y)-1.        \tag{2}
\]
The population is sampled from genuine positive integers. The theorem does not require randomizing their subsequent arithmetic. The interval length determines the time horizon, so the assertion gives no limit along the future of one fixed integer.

## The binary filtration and the two-particle clocks

First take \(x\) Haar-uniform in \(\mathbb Z_2\), and let \(\mathcal F_k\) reveal \(x\bmod 2^k\). On either next lift of this residue, the current value of each arm changes by an odd multiple of the new fair bit, using its current word slope \(3^{s_i+g_i(k)}/2^k\). Thus each centered parity bit equals the same fresh fair sign times a predictable sign, divided by two. The step processes in (1) using grades are martingales. Writing \(M_{ij}(k)\) for the number of differing departure bits in the first \(k\) dates, their predictable covariations are exactly
\[
 \langle W_i,W_j\rangle(k/t)=\frac{k-2M_{ij}(k)}{4t},\qquad
 \langle W_i\rangle(k/t)=\frac{k}{4t}.                                  \tag{3}
\]
The indicators of disagreement are predictable even though the individual bits are fresh.

For \(i<j\), the initial pair based at the Haar coordinate \(x_i\) has slope \(3^{s_j-s_i}\) and integer offset \(D_j-3^{s_j-s_i}D_i\). Its normalized offset has magnitude at most
\(3^{s_i}(|D_j|/3^{s_j}+|D_i|/3^{s_i})\), with logarithm \(o(t)\) after adding two. Let \(R_{ij}\) be its first zero of the signed adjusted grade difference, and \(A_{ij}\) the first date of equal affine maps, equivalently equal grades adjusted by the initial exponents and identical physical affine output on the source cylinder. All times herein are stopping times of the joint filtration. The [moving-level native clock, equation (3)](CRITICAL_TOWER_ENDPOINT_PROFILE.md) and [post-return bound, equation (1)](ORDINARY_AFFINE_INTERVAL_PROFILE.md) give
\[
     (A_{ij}-R_{ij})/t=o_{\mathbb P}(1),\qquad
     \sup_{k\le t}\frac{|2M_{ij}(k\wedge R_{ij})-(k\wedge R_{ij})|}{t}
                    =o_{\mathbb P}(1).                                    \tag{4}
\]
These inputs are derived from Leen's physical holding and return laws. For the second conclusion let \(\sigma_h\) be the physical date of the \(h\)-th mixed direction, killed at the mixed index \(K\) of the first zero. The cited clock gives \(|\sigma_{h\wedge K}-2(h\wedge K)|=o_{\mathbb P}(t)\) at each deterministic \(h\le t+1\), in triangular-array form. On a fixed mesh of spacing \(\eta t\) the maximum satisfies the same bound. Monotonicity and the Lipschitz bound for \(2(h\wedge K)\) give the uniform maximum over all \(h\le t+1\) by taking \(\eta\downarrow0\). Inverting between successive mixed directions gives the second assertion of (4), including intervals ending in a hold. The odd-level entrance in that clock argument discards at most one mixed direction and \(o_{\mathbb P}(t)\) raw dates. The post-return delay estimate uses the original pair before this entrance. After \(A_{ij}\) all successive bits agree. Together (3) and (4) give the uniform-in-time estimate
\[
  \langle W_i,W_j\rangle(u)=\tfrac14[u-u\wedge(R_{ij}/t)]+o_{\mathbb P}(1).
                                                                               \tag{5}
\]
There are only finitely many pairs. [Leen, *Exact rates in Collatz synchronization*, uniform pair absorption, return moment and physical clock](https://doi.org/10.5281/zenodo.23268751)

## Identification of the full joint path

Each single arm has independent fair bits under Haar by the invertible parity coding. Its centered walk is tight after the scaling in (1), for example by the fourth-moment bound for sums of independent signs. This gives joint tightness for the fixed number of arms. Include in the joint limit the adapted, bounded, 1-Lipschitz processes \(u\mapsto u\wedge(R_{ij}/t)\), rounded to their last mesh point for past measurability as needed. Any subsequential limit has their form \(u\wedge\rho_{ij}\) for \(0\le\rho_{ij}\le1\). The discrete martingale identities for \(W_i\) and \(W_iW_j-\langle W_i,W_j\rangle\) pass to the limit against bounded continuous functions of the past of these joint processes. Fourth moments of all single-arm maxima are uniformly bounded by the fourth-moment maximal inequality. Mesh interpolation changes the positions by at most \(1/(2\sqrt t)\). Consequently the limit processes \(V_i\) are continuous martingales in their joint filtration augmented by these **past** clock observations, with brackets (5) and \([V_i](u)=u/4\).

Up to \(R_{ij}\) the signed grade difference of arms \(j,i\) is nonnegative and at a finite return it is zero. After \(A_{ij}\) it is zero forever. During the intervening \(o_{\mathbb P}(t)\) times, the tight moduli of continuity of the two walks make the maximum absolute scaled difference \(o_{\mathbb P}(1)\). Therefore \(V_j-V_i\) is a nonnegative martingale, zero at \(\rho_{ij}\) if \(\rho_{ij}<1\) and thereafter. At its first zero it must stay zero by optional sampling and nonnegativity. Its bracket up to \(u\) is exactly \((u\wedge\rho_{ij})/2\); hence its first meeting capped at 1 equals \(\rho_{ij}\). This argument also handles a first zero that disappears under a naive hitting-time continuous-mapping argument.

These martingale identities characterize the finite coalescing Brownian system. Up to the first meeting, the vector has zero cross-brackets and diagonal brackets \(u/4\). On a product extension, continue the stopped vector with independent Brownian increments of rate \(1/4\) beyond that stopping time. Its brackets are then those of an independent Brownian vector on the whole interval by Lévy's characterization, so the law up to the first meeting is determined. At the stopping time identify equal positions. Conditional on its past the same argument applies to the surviving distinct coordinates up to their next meeting. Optional sampling justifies the restarted martingale identities, and each meeting decreases their number. This proves uniqueness and the full convergence. The finite process is the classical finite-point motion of the Arratia flow. [Fontes, Isopi, Newman and Ravishankar, *The Brownian web: characterization and convergence*](https://arxiv.org/abs/math/0311254)

## Transfer to actual positive integers and true log heights

All the joint histories through \(j=t-\lceil2\log_2(t+2)\rceil\) are functions of one residue \(x\bmod 2^j\). Its empirical distribution on any interval of length \(N\) is within \(2^j/N=o(1)\) in total variation of uniform. Shortening and freezing the walks at \(j/t\) changes their sup norm by \(O((t-j)/\sqrt t)=o(1)\); truncating the scaled return and absorption times there changes their capped values by at most \((t-j)/t=o(1)\). Thus the preceding joint convergence transfers to ordinary inputs.

An unequal-slope numerical coincidence stays unequal in slope forever: from that date onward identical physical values take identical steps. At date \(t\) its defining equation in the original \(x\) has coefficient \(3^{s_i+g_i}-3^{s_j+g_j}\), and right side \(3^{g_j}D_j-3^{g_i}D_i+C_j-C_i\) for nonnegative true word carries \(C_i,C_j\). On typical words both terminal grades are at least \(t/4\). The [bounded-carry argument](ORDINARY_AFFINE_INTERVAL_PROFILE.md) puts \(x\) within \(3\cdot 2^{3t/4}\) of a fixed real center for each of \((t+1)^2\) grade pairs. Here \(s_i,s_j\ge0\); the nonzero coefficient dominates two thirds of the larger full slope. The low-grade exception has exponentially small empirical fraction by the full residue-period majorant. Thus with probability \(1-o(1)\), every pair's first numerical meeting agrees with canonical absorption up to date \(t\). To recover the partition *at* time 1, observe also that \(\Pr(A_{ij}>t)\to H(a_j-a_i)\) by the first-return law and its post-return estimate, using the same shortened/full cylinder sandwich as in the affine interval theorem. Equivalently, the probability of a merger in the last \(\eta t\) tends to zero as \(\eta\downarrow0\), uniformly after the limit in \(t\); positive meeting times of a Brownian pair have continuous laws. The same argument handles any fixed finite collection of positive dates. For (2) the two neighboring equality events intersect precisely in outer equality in the noncrossing limit; inclusion–exclusion gives the formula.

Write \(C_{i,k}\) for the prefix carry. With empirical probability \(1-o(1)\), all fixed arms and all their prefixes have \(|g_i(k)-k/2|\le\delta t\) by a union bound and the full-period fair-bit majorant. The sum of normalized odd contributions then gives \(C_{i,k}/3^{g_i(k)}\le C2^{(b+\gamma\delta)t}\) simultaneously. Remove \(x<N^{3/4}\), costing at most \(N^{-1/4}\) in any interval. Take fixed \(\delta>0\) so small that \(b+\gamma\delta<3/4\). The exact affine formula becomes
\[
  T^k x_i=2^{-k}3^{s_i+g_i(k)}x
       \left(1+\frac{D_i/3^{s_i}+C_{i,k}/3^{s_i+g_i(k)}}{x}\right).
\]
Uniformly through all dates its parenthesis is \(1+o(1)\) on this event. This proves the joint real-height claim in (1).

A single-arm Brownian path limit and pre-minimum trajectory laws have earlier sources. Leen also gives conditional path laws for late adjacent pairs; Weaver gives selected physical clocks and actual-source couplings. The present conclusion uses a joint martingale identification for a finite family with separated initial levels of order \(\sqrt t\), and an empirical law of their actual log heights on every interval. It concerns finitely many prescribed arms. [Leen, *Brownian motion in Collatz orbits*](https://doi.org/10.5281/zenodo.23252395) · [Leen, *Late synchronization and the geometry of Collatz families*](https://doi.org/10.5281/zenodo.23268753) · [Weaver, *Conditional clocks and source couplings for Collatz synchronization*, Paper 13](https://rstation.ai/problems/collatz/papers/13/v1)
