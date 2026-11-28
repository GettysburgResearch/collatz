# The closed matched-code exponent governs every native residence length in a range of widths

**Proposed written theorem.** Fix \(2<R<4\). Put \(\gamma=\log_23,\ \eta=\log_2(R/2),\ a=\gamma-1,\ f=(\eta-a)_+,\ s=\eta-2f\), and set
\[
 t=\gamma^{-1}\max\{3(s+\gamma f)/5,\ 9s/16+5\gamma f/8\},
 \qquad r=\min\{0.5753\,\eta/\gamma,\ t\}.
\]
The [matched Sidon theorem](MATCHED_SIDON_CODES.md) bounds the ratio of log period to log minimum by \(r\) for ordinary cycles in this width. Here the same bound applies to **every length of a distinct open run**, with a width-dependent Diophantine condition: if \(\mu(\log_23)\le\mu_0<\infty\) and \((\mu_0+1)r\le1\), then every run of \(T\) distinct positive ordinary odd Collatz states in \([M,RM]\) satisfies
\[
                              T\le M^{r+o(1)}.                           \tag{1}
\]
No repetition of a reduced-rank pattern is assumed. With the classical published \(\mu_0=5.116201\) this applies through \(R=2.73292\ldots\) (the root \(r=1/6.116201\)); under the imported \(\mu_0=3\) it applies through \(R=3.28052\ldots\) (the root \(r=1/4\)). At \(R=3\) the resulting exponent is \(0.21232612\ldots\) under the latter hypothesis. For every sufficiently small fixed \(\eta>0\), even classical finite measure suffices for the bound \(T\le M^{(0.5753/\gamma)\eta+o(1)}\). The limit \(M\to\infty\) is taken first at fixed width. [Classical BLS Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Log-ratio import and audit scope](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

More generally if \(\mu_0 r<1\), every such run has exponent at most
\[
 \limsup \frac{\log T}{\log M}\le
    \max\left\{r,\
        \min\left(\frac{(\mu_0+3)r-1}{2},
                  \frac{4t+\mu_0 r-1}{3}\right)\right\}.              \tag{2}
\]
In the second branch of (2) the collision estimate with coefficient \(1/4\) is only needed where this improves the first branch; its application in this regime is detailed below. As \(R\uparrow4,\ \mu_0=3\), this recovers the [uniform subfour residence theorem](UNIFORM_SUBFOUR_RESIDENCE.md). Weaver's physical source count gives a different bound including an exit correction for separated visits. The narrow-width source entropy for arbitrary realizable prefixes and the exact factor-two endpoint are treated in the [open source entropy note](../literature/CONFINED_SOURCE_ENTROPY.md) and [Weaver 222/v1](https://rstation.ai/problems/collatz/papers/222/v1), respectively.

## The actual restricted alphabet on each open grid

On any of the spatially short samples of [the one-sheet proof](CONFINED_CONVERGENT_GAPS.md) or [the all-sheet proof](UNIFORM_SUBFOUR_RESIDENCE.md), use \(v=(1-\eta)/2,\ L=2^{1-v}M\) in the common floor \(F_i=\lfloor\log_2(V_i/L)\rfloor\). It lies strictly between \(RM/2\) and \(2M\). On \(n=\lceil\log_3(32RM)\rceil+3\) forward edges all selected normalized labels lie within a relative \(o(1)\) of the base \(L2^{z_i}\), \(z_i=\{\log_2(V_i/L)\}\), uniformly in the sampled column and date. The true binary tags lie in \(\{1,2\}\). If a row includes both options, its base label is within relative \(o(1)\) of \([2M,RM]\), hence \(z_i\) lies in \(I=[v-o(1),v+\eta+o(1)]\). Retain all rows in this enlarged interval, including any constant ones. Every discarded coordinate is common to every word. Over this coding horizon \(z_i\) differs modulo one from \(z_0+i\gamma\) by \(O_R(n/M)\), uniformly; the actual winding differs from that of this rotation only near a boundary of vanishing width. Irrational rotation averaging is uniform over \(z_0\). The retained row fraction tends to \(\eta\).

Match each winding-one retained row with a retained successor, except at the last row. These disjoint pairs have asymptotic density \(f\): in the limiting intercept coordinate the departure and its shift by \(a\) must both lie in \(I\) without wrapping, a condition of length \((\eta-a)_+\). On the matched pair the genuine positive native valuation rules out the single descending tag configuration. This leaves \(sn+o(n)\) binary singletons and \(fn+o(n)\) ternary coordinates. All endpoint and moving-boundary exceptions are \(o(n)\). Thus any subsample whose initial physical label sums are Sidon has size \(\le M^{r+o(1)}\). For the mixed branch, the exact native divisor turns equal coordinatewise pair outputs into equal initial physical label sums, as in the cited matched-code theorem. For the \(0.5753\) branch, use the original binary integer-sum code upper bound on the \(\eta n+o(n)\) active rows. [Cohen–Litsyn–Zémor, Theorem 1, author manuscript and statement in the two-grade theorem](TWO_GRADE_SIDON.md)

## Last denominator and the collision cost

Write \(\lambda=\lim\log T/\log M\) along a subsequence and assume \(\lambda>r\). Weaver's uniform sub-four bound still gives \(\lambda\le v_*<1/2\). For the convergent \(h/b\) with \(b\le T<b'\), the one-sheet argument proves \(b\le M^{r+o(1)}\) as follows. In a putative counterexample use \(U_0=b/(\log M)^3\) up to a fixed constant, so all reduced ranks are distinct and \(4U_0<b\). The native Frobenius comparison and temporal rectangle identity in that proof give area \(O(b^2 U_0/M)\). Its published sampling argument retains a Sidon population of size
\[
                   b\,M^{-o(1)}(1+b^3/M)^{-1/3}.
\]
The width-dependent alphabet just established applies to these same actual sources. Hence \(\alpha-(3\alpha-1)_+/3\le r\) for \(\alpha=\lim\log b/\log M\). As \(r<1/3\), this implies \(\alpha\le r\). The proof needs only \(b\le T\) and \(T^2=o(M)\) to fit the native sample and its dyadic deadline. If \(b\) is already subpolynomial in \(M\) the desired inequality is automatic.

Let \(\xi=\lim\log b'/\log M\), after taking a further subsequence. The irrationality measure gives \(b'\le b^{\mu_0-1+o(1)}\), so \(\alpha+\xi\le\mu_0r<1\) and the limits are finite. The [all-sheet area and fiber argument](UNIFORM_SUBFOUR_RESIDENCE.md) now bounds the total count of nontrivial equal-pair-sum collisions on a population \(K=M^{\lambda-o(1)}\) of actual folded labels by \(K M^{z+o(1)}\), where
\[
                           z=\max\{0,3\lambda-1,\lambda+\alpha+\xi-1\}.
\]
In applying that argument we use \(U=T/(\log M)^{10}\). The hypothesis \(\lambda>r\ge\alpha\) gives polynomial sheet length \(T/b\); \(U/b'\to0\) follows directly from \(T<b'\), so the stronger next-convergent gap used in its original regime is unnecessary. All other comparison estimates use \(bU/M=o(1)\), \(bb'=o(M)\), \(T\le b'\) and the fixed band margins. The strict-convex fiber theorem is therefore applicable.

For the generic separation bound, remove collisions with a random subsample. If there are at most \(K d\) four-distinct equal-sum edges, the number of nonconstant three-term progressions is at most \(K+\sqrt{2K^2d}\), by the repeated-center argument in [the controlled-collision proof](REPEATED_ADDITIVE_PACKINGS.md). Taking \(d=M^{z+o(1)}\ge1\) and keeping vertices with probability a small constant times \(d^{-1/3}\), the expected counts of remaining four-edges and three-edges together are at most half the expected retained population. Delete one member of each. This supplies a Sidon subset of size \(\gg Kd^{-1/3}\) obeying the actual restricted alphabet bound. Thus
\[
                           \lambda\le r+z/3.                            \tag{3}
\]
If \(z=0\) this contradicts \(\lambda>r\), and if \(z=3\lambda-1\) it would give \(1/3\le r\). Consequently \(z=\lambda+\alpha+\xi-1>0\). In particular \(z<\lambda\), as required for a nonempty prefix in the controlled-collision proof. Applying that proof directly to the two retained alphabet sizes gives \(\lambda\le t+z/4\): its two nonempty-prefix branches have coefficients \(1/5,1/4\), respectively, and their constant terms are bounded by \(t\). Substitution of \(\alpha+\xi\le\mu_0r\) in this inequality and (3) proves (2). Under \((\mu_0+1)r\le1\), the first fraction in (2) is at most \(r\), proving (1) including equality at the threshold.
