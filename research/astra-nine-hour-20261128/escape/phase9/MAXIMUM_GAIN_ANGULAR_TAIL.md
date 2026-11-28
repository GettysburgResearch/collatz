# Exact tail and angular law of the greatest legal gain

For a ternary point \(z\), let \(G(z)\) be the supremum of the forward affine multipliers over all finite shortcut inverse words legal at \(z\), including the empty gain one. This maximizes over the entire allowed tree at a supplied point. Papers 177–178 give \(m(G>t)\le t^{-2}\) under ternary Haar probability \(m\), and Paper 207, §3, uses the real multiplier shell of Paper 146 to prove \(m(G>t)\gg t^{-2}\). These earlier conclusions concern exactly this \(G\). [Weaver 177](https://rstation.ai/problems/collatz/papers/177) · [Weaver 207, §3, equations (3)–(4) and the maximum-gain subsection](https://rstation.ai/problems/collatz/papers/207/v1)

**Source-qualified sharpening.** For \(\sigma\) the tilted stationary ternary law with independent gaps of probabilities \(p_e=3/4^e\),
\[
              t^2\,1_{\{G>t\}}\,dm\ \Longrightarrow\ \kappa_G\sigma,
                  \qquad 0<\kappa_G\le1.                             \tag{1}
\]
The scalar constant has the interaction formula below. At positive ordinary integers the same function satisfies \(G(y)/y\to0\) as \(y\to\infty\) exactly when every positive ordinary orbit is bounded. The stationary angular law in (1) does not control the pointwise ordinary criterion.

## Branch overlap and the scalar constant

An inverse word that ends in an even inverse has its gain reduced by that final step. Thus maximizers may be sought among words ending in an odd inverse, which group into accelerated letters. Put \(a_e=3/2^e,\ F_e(x)=(3x+1)/2^e\) and
\[
    u_e(z)=a_e 1_{F_e\mathbb Z_3}(z)G(F_e^{-1}z),\qquad
    G(z)=\max(1,\sup_e u_e(z)).
\]
The Haar Jacobian of \(F_e\) is \(1/3\). With \(\rho\) the original stationary density and \(b_e=a_e1_{F_e\mathbb Z_3}\rho\circ F_e^{-1}\), we first have \(G\le C(1+\rho)\) almost everywhere. Indeed for each fixed word \(w\) whose terminal inverse argument is a unit, positivity of the stationary transfer gives \(\rho\ge a_w\rho\circ F_w^{-1}\ge\alpha a_w\) on its cylinder at such points, using the unit floor of [the individual-increment proof](INDIVIDUAL_COLLISION_INCREMENTS.md). If that final argument is nonunit, drop the last accelerated letter: its preceding argument is a unit as an image of some \(F_e\), and the dropped gain is at most \(3/2\). For a one-letter word the empty prefix suffices for this bound. Countably many branch inequalities can be enforced simultaneously almost everywhere.

It follows that \(u_e\le C(a_e1_{F_e\mathbb Z_3}+b_e)\) almost everywhere. Because \(\sum_e a_e=3\), \(\int\rho=1\), and \(\sum_e b_e=\rho\), the distinct-branch integral is finite:
\[
                  \int\sum_{e\ne f}u_e u_f\,dm<\infty .              \tag{2}
\]
The only term requiring an input beyond first moments is \(\int\sum_{e\ne f} b_e b_f<\infty\), supplied by Paper 146, (19)–(22). In particular the \(u_e\) are summable almost surely and their nonzero maximum is attained. [Weaver 146, §8, equations (19)–(25)](https://rstation.ai/problems/collatz/papers/146/v1)

Write \(T(s)=m(G>s)\), \(g(s)=T(s)-\tfrac13\sum_eT(s/a_e)\). Its integrable signed interaction satisfies
\[
 \int_0^\infty s|g(s)|\,ds<\infty,\qquad
 \int_0^\infty s g(s)\,ds
      = \tfrac12\int\left[G(z)^2-\sum_e u_e(z)^2\right]dm(z).        \tag{3}
\]
The bracket is one integrable signed function. At each point, subtract the sum of branch indicators from the indicator of their maximum, and add the base-one contribution. The \(s\,ds\) integral of the absolute difference is at most \(1/2\) plus half the sum of squares of the nonmaximal entries. Each such square is at most its product with the maximum, so (2) gives Fubini and (3).

Now \(f(x)=e^{2x}T(e^x)\) obeys
\[
   f(x)=e^{2x}g(e^x)+(\nu*f)(x),\qquad
       \nu=\sum_e(3/4^e)\delta_{\log3-e\log2}.
\]
This is the same scalar renewal kernel as for the density tail in Paper 146, with the different max interaction (3). For clarity, \(f\) is bounded by the known crossing upper bound and vanishes at \(-\infty\); \(e^{2x}g(e^x)\in L^1\). The lazy version \((\delta_0+\nu)/2\) is nonlattice since its support generates \(\log2,\log3\) with irrational ratio. Its mean is half \(\mu=\log3-\tfrac43\log2>0\). Exponential smoothing makes the forcing directly Riemann integrable; the two-sided key renewal theorem gives the smoothed limit \(\mu^{-1}\int_0^\infty s g(s)\,ds\). Monotonicity of \(T\) removes smoothing as in Paper 146, (23)–(25), proving
\[
     \lim_{t\to\infty}t^2T(t)=
       \kappa_G=\frac1{2\mu}\int\left(G^2-\sum_eu_e^2\right)dm .
\]
The two-sided order from Paper 207 ensures strict positivity, and the first-crossing upper bound gives \(\kappa_G\le1\). No numerical value of this constant is claimed.

## Conditioning the large gain

For \(\eta_t=t^2 1_{\{G>t\}}dm\), when \(t>1\) the event is the union of the branch exceedances \(u_e>t\). The difference between their summed measures and the union has total mass at most \(t^2\sum_{e<f}m(u_e>t,u_f>t)=o(1)\), by dominated convergence from (2). With pushforward denoted by a subscript \(*\),
\[
               \left\|\eta_t-\sum_e p_e(F_e)_*\eta_{t/a_e}
                    \right\|_{\rm TV}=o(1).
\]
Iterate a fixed \(r\) times. The intermediate thresholds stay at least \(t/(3/2)^r\), and all the coefficients have total one, so the accumulated error tends to zero. Each \(F_w\) of depth \(r\) maps \(\mathbb Z_3\) into one depth-\(r\) cylinder; on that finite partition only the scalar masses of \(\eta_{t/a_w}\) remain. These approach \(\kappa_G\) uniformly over the attained thresholds. The iid probabilities \(p(w)\) of the resulting cylinders form \(\sigma\bmod3^r\). All fixed partitions together prove (1).

## The ordinary diagonal

At every positive integer \(y\) the ternary legality test reconstructs positive, parity-correct ordinary inverse words. A shortcut path \(x\to y\) with multiplier \(a_w\) satisfies
\[
             a_w/y=f_w(x)/x,\qquad
             f_w(x)=\prod_{\text{odd departures }v}3v/(3v+1)\le1 .
\]
Consequently \(G(y)/y\ge\epsilon\) with strict margin requires a predecessor \(x\le1/\epsilon\). If all positive orbits are bounded, the union of the forward trajectories of any such finite set of sources is finite, so \(G(y)/y\to0\). Conversely on a supplied escape from \(x\), \(f_w(x)\downarrow f_\infty(x)>0\) by orbit-set sparsity. Taking subsequent targets on this trajectory gives a positive lower limit. More precisely on a cofinal escaping ray in component \(C\),
\[
              G(y)/y\longrightarrow
                 \max_{x\in C} f_\infty(x)/x .
\]
Indeed restrict to \(x\le M\) with error at most \(1/M\) in the supremum. Each fixed \(x\in C\) reaches every sufficiently late target on the ray through a unique finite path, whereas sources outside \(C\) never do. Pass to the limit over that finite set and then let \(M\to\infty\). The positive supremum is attained because \(f_\infty(x)/x\le1/x\). Suprema also make the statement valid without finite attainment in a symbolic tree. [Uniform simple-path correction bound](../phase4/HARMONIC_SOURCE_PHASE.md)
