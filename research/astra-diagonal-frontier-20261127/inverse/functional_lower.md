# Brownian paths in the fixed-root inverse fluctuation cluster set

Let $a$ be any fixed positive odd ternary unit. Under its canonical ordinary inverse path law $P_{h,a}$ let $D_j=S_j-2j$ be the centered sum of the physical inverse gaps, with $D_0=0$. Define $Z_n\in C[0,1]$ by linearly interpolating $D_j/\sqrt{n\log\log n}$ at $j/n$, for $n\ge3$. Under the averaged joint Syracuse mixing assumption (J) of Weaver's Paper 211 and the inputs to the fixed-root inverse upper bound, almost surely the uniform subsequential cluster set of $Z_n$ contains
\[
 \mathcal K=\left\{f:\ f(0)=0,\ f\text{ absolutely continuous},\quad
                            \int_0^1|f'(t)|^2\,dt\le4\right\}.       \tag{1}
\]
The same result holds under the natural entrance law $Q_a$ at any nonperiodic such $a$. In particular
\[
 \limsup_n\frac{D_n}{\sqrt{n\log\log n}}\ge2,\qquad
 \liminf_n\frac{D_n}{\sqrt{n\log\log n}}\le-2 .
\]
The proof gives a lower inclusion at each supplied root. The normalization is that of fair geometric gaps, whose variance is two. [Weaver, Paper 211 v1, Appendices A–B](https://rstation.ai/problems/collatz/papers/211/v1) · [Fixed-root ordinary path estimates, commit aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) · [Earlier fixed-root lower fluctuations and stopped-trial construction](inverse_fluctuation_lower.md).

## A uniform prefactor on any fixed Gaussian window

There is an absolute $c>0$ with the following property. For each fixed real $u$, for all sufficiently large block lengths $b$ depending on $u$, and every positive odd unit $y$, there is a family of ordinary inverse words from $y$ with unit endpoints, all of length $b$, such that
\[
 |D_b-u\sqrt b|\le2\sqrt b,\qquad
 \max_{i\le b}|D_i|\le(|u|+7)\sqrt b,\qquad
             \sum_w3^b2^{-S_b(w)}\ge c\exp[-(|u|+1)^2/4].           \tag{2}
\]
The same $c$ works for every fixed $u$. A compact bound on all $u$ can be fixed before selecting a common block onset.

Here are the details of this uniformity extension of the monitored bridge argument. The favorable cylinder and $g_M\ge p_*/2$ there for all $M\ge M_0$ are fixed by Paper 211, (B.2)–(B.3), at the central endpoint zero, before choosing the final window or monitor. In Appendix A the fixed-window calculation (A.4) gives summable $e_i(C)$ for every fixed central bound $C$. These errors can have constants depending arbitrarily on $C$. Their tails tend to zero, while the lower bound on $g_M$ from (B.3) still holds on the same cylinder at arbitrarily large $M$.

Run the mesh proof (B.4)–(B.6) on the compact endpoint range $|x|=|s-2b|/\sqrt b\le C$. Conditional composition convergence and Gaussian-ratio bounds at the fixed base hold on every such compact range by the same Stirling formula and bridge argument (B.4). The old-prefix probability truncation in (B.5) may use a $C,M$-dependent bound. The positive-window lower bound $\pi_b(s)\gg_C b^{-1/2}$ suffices for every late-lift, short-interval and switch error in §B.3 to be relatively $o_C(1)$. The early deletion and lift errors use $e_i(C)$ from (A.4). The bounded monitor at each mesh date is covered by (A.6) at any fixed cutoff. Use symmetric monitor coefficient $C+3$ and final coefficient $C+4$. A centered variance-two Brownian bridge has positive probability $p$ to stay strictly between $-2$ and $2$. Translating it by the line $t x$ with $|x|\le C$ gives monitor probability at least this same $p$. Thus (B.6) bounds the normalized mass below on the cylinder by $3p_*p/4$ up to its tail and depth errors. Choose $M$ large at the fixed $C$ and then the depth large; the surviving prefactor is absolute. The bounded spreading gap of §B.4 uses only that fixed favorable cylinder, and its unit-density multiplier is at least $3\cdot2^{-V}$ with absolute $V$. Its $O_V(1)$ shift is absorbed by one more fixed unit of strip slack and an enlarged central window. Hence the lower prefactor on arbitrary unit residues is absolute, even as the onset depends on the chosen compact interval. This use of (J) does not assert a joint limit with $C$ growing with $b$.

Apply the result on the band $|x-u|\le1/2$. Summing the exact fair geometric total masses over this band converges to the integral of the variance-two Gaussian density there, which is at least $c'\exp[-(|u|+1)^2/4]$. Congruence at an actual positive root makes every step integral and positive. Repair any terminal multiple of three by increasing the last gap by two, with at most two provisional words per final word and a weight loss of at most four. This consumes at most two units of strip and endpoint slack at a large block length. The constants in (2) accommodate these changes. [Paper 211 v1, §§2.1 and B.2–B.4](https://rstation.ai/problems/collatz/papers/211/v1).

## A uniform trial for a fixed polygonal path

First let $f$ be piecewise linear from zero, with slopes $s_1,\ldots,s_r$ on successive time intervals of lengths $d_i>0$, $\sum_i d_i=1$ and $E=\sum_i d_i s_i^2<4$. Fix an approximation tolerance $e>0$. Choose a large constant $A$ to be specified. Let $k\to\infty$, and fix an integer $L\ge1$ before the trial. Put
\[
       m=\lfloor(\log k)/A^2\rfloor,\quad
       b=\lfloor L2^k/m\rfloor,\quad N=mb .
\]
Use nonnegative integers $m_i$ with $\sum_i m_i=m$ and $m_i=d_i m+O_r(1)$. For successive groups of $m_i$ blocks require (2) with $u=A s_i$. The lower cutoffs in (2) are attained for all large $k$ because the list of slopes, $A$ and $L$ are fixed. Every qualifying increment profile $D'_j$ from the beginning of this trial, interpolated on $[0,1]$, satisfies
\[
   \sup_{0\le t\le1}\left|
       \frac{D'_{Nt}}{\sqrt{N\log k}}-f(t)\right|
                       \le 2/A+o_{A,L,f}(1).                        \tag{3}
\]
Indeed, accumulated endpoint errors cost at most $2m\sqrt b/\sqrt{N\log k}\to2/A$. The center contributed by one block differs from the desired slope divided by $m$ by the factor $A\sqrt{m/\log k}\to1$. The finite rounding of the piece boundaries costs $O_f(1/m)$. Within one block the discrepancy is at most $(A\max|s_i|+7)/\sqrt{m\log k}=o(1)$ on this scale, and the variation of $f$ across one block vanishes as well.

The actual conditional probability of the whole trial from a positive unit $y$ is at least
\[
   \frac{\alpha}{h(y)}\prod_i
        \left(c\exp[-(A|s_i|+1)^2/4]\right)^{m_i},                 \tag{4}
\]
where $\alpha$ is the absolute positive trace floor. The full inverse word has a single terminal factor $h(\mathrm{end})/h(y)$, and the unnormalized contributions (2) multiply on the true ordinary tree. The exponent of $k$ in the negative logarithm of the product tends to
\[
                  E/4+O_f(1/A)+O(\log(1/c)/A^2).
\]
Take $A$ sufficiently large that this is below one and $2/A<e/4$. There is a fixed $p<1$ such that (4) is at least $(\alpha/h(y))k^{-p}$ at every large $k$. Neither the telescoping comparison nor the compact-window bound uses independent exponents at the supplied root.

## Realization on one physical inverse path

The low-trace occupancy result and stopped conditional Borel–Cantelli argument of the earlier note apply unchanged. In more detail, for almost every path the indices $k$ of dyadic epochs $[2^k,2^{k+1})$ containing a time with $h(X_j)\le8$ have positive upper density. This follows from Paper 12's full-event Cesàro identity (29) for $\rho_1/h$, with harmonic partial summation. The sum of $k^{-p}$ over occupied epochs diverges for $p<1$. Stop each trial at its first such $T_k$ in the epoch, omitting it when there is none. More precisely $T_k$ is the time at which the trial starts. On occupied epochs (4) gives the conditional probability lower bound $(\alpha/8)k^{-p}$. For each fixed $L$, split $k$ into a fixed number of residue classes so that consecutive possible trial intervals $[T_k,T_k+N]$ in the same class are disjoint. The conditional martingale Borel–Cantelli lemma, applied as in the earlier note, gives infinitely many complete successes almost surely. Intersect over all integers $L$ before allowing $L$ to depend on the path. [Weaver, Paper 12 v1, Lemma 8, equation (29)](https://rstation.ai/problems/collatz/papers/12/v1).

On a path satisfying the fixed-root upper bound, all the old centered values for $j\le T_k$ are bounded by $C_\omega\sqrt{2^k\log k}$ for large $k$. At a successful terminal date $n_k=T_k+N$, the pretrial scale therefore costs $O(C_\omega/\sqrt L)$ uniformly on the entire earlier segment. The earlier segment occupies a time fraction at most $2/(L+o(1))$; the affine time change on the later segment changes any argument of $f$ by at most this same bound. Its effect vanishes with large $L$ by uniform continuity. The normalization ratio $\sqrt{N\log k}/\sqrt{n_k\log\log n_k}$ differs from one by $O(1/L)+o_L(1)$. Combining with (3), choose a large integer $L$ so the prehistory, time-change and normalization errors together are below $e/2$ for all sufficiently large successes. The resulting calendars have $\|Z_{n_k}-f\|_\infty<e$ infinitely often.

Take a countable dense collection of rational polygonal paths with energies strictly below four and all rational positive tolerances. Every path in (1) is a uniform limit of these paths. For instance, take fine polygonal interpolants of $f$, whose energies are at most the original energy by Cauchy–Schwarz, contract slightly toward zero, and perturb the finitely many vertices and breakpoints rationally within the strict energy margin. On the countable probability-one intersection, a diagonal choice of strictly increasing horizons realizes every such uniform limit. Bounded equivalence of the full inverse path laws at nonperiodic roots transfers the result to $Q_a$. This argument asserts cluster points and does not require relative compactness of the entire sequence of rescaled paths.
