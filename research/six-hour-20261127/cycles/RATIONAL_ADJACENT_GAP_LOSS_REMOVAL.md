# A physical adjacent-gap census removes the multiplier loss at rational microscopic offsets

Consider primitive positive rational Collatz cycles of least odd period $P\to\infty$, common reduced denominator $d$ prime to six, physical maximal odd phase $X$, and canonical height at most one. Every positive valuation is allowed. Put $S=|\langle2,3\rangle_d|$ with $S=1$ at $d=1$, and assume $S=P^{o(1)}$. Write $A/P=a/q$ in lowest terms. The following bounds use no Subspace Theorem.

1. The physical exponent satisfies
$$
 \liminf\frac{\log X}{\log P}\ge\xi_0
 =1+\frac{\ln3}{\ln3+(2-\lambda)\ln(7/9)}
 =2.1049020798\ldots,\qquad \lambda=\log_2 3 .
$$
2. Under the published 2018 logarithmic bound, the mismatch fraction at **every** nonresonant lag $q\nmid h$ has global inferior limit strictly above $1/1000$. Under the separately quoted 2026 input $\mu(\lambda)\le3$, this global inferior limit is strictly above $1/55$. The earlier $1/36$ bound under that input still applies to its larger-offset or compatible-offset classes. In fact under the 2018 input alone, along any sequence for which the shorter rank offset divided by $q$ tends to zero, the mismatch fraction has inferior limit strictly above $1/55$ without multiplying it by a residue order.

These statements combine the exact compatible rank convexity and nonresonant physical entropy of the binary-energy author's two rational notes with the ordinary adjacent-gap drift census. The $g-1$ possible proper multiples of $q$ remain outside the lag assertion. No conclusion is made for unrestricted residue-group growth.

## Compatible physical gaps

Write $g=P/q$, $T=S/g$ and let $h_*$ be the unique compatible lag at rank offset $T$ supplied by RATIONAL_RESIDUE_RANK_CONVEXITY.md. Its hypotheses hold eventually since $S=P^{o(1)}$. In that note's normalization $K_i=2^{1-z_i}N_i$, $r_i=ia\bmod q$, define at any fixed $i$
$$
 V_j=2^{\lfloor(r_i+jT)/q\rfloor}K_{i+jh_*}/d\quad(j\ge0).
$$
The first difference $V_1-V_0$ is a positive integer. Every further second difference is the corresponding positive, normalized $T$-curvature multiplied by its entrance octave factor. Thus all these gaps are nondecreasing in $j$. For $n=\lfloor q/T\rfloor=\lfloor P/S\rfloor$ the octave factor at $n$ is at most two, so $V_n\le4X$. Summing the $n$ gaps gives
$$
 0<V_1-V_0\le 4X/n\le8XS/P .
$$
Across initial phases each value has multiplicity at most $S$ by the residue-progression convexity theorem.

Take $b$ least with $3^b>8XS/P$. Since $X\gg(P/S)^2$, this horizon tends to infinity. It is $O(\log P)$ along any bounded-exponent subsequence, and we may restrict to such subsequences for the lower bound. Exclude all terminal indices whose backward length-$b$ list, including both endpoints, meets ranks $[q-T,q)$. For each fixed date exactly $gT=S$ starts do so, hence at most $(b+1)S$ terminals are excluded. In every remaining window the two compared paths are in the fundamental octave at each simultaneous date and use the same mechanical divisor. Indeed their relative wrap can change only between a fundamental pair and a wrapped one. Upon dividing the raw gap recurrence by $d$, the normalized drift is the actual lowbit difference in $\{-1,0,1\}$. As in ADJACENT_GAP_PERIOD_EXCLUSION.md, a mechanical one forbids either direct reversal between nonzero signs. These edges are disjoint and there are at least $w=\lfloor(2-\theta)(b-1)\rfloor$ among the first $b-1$ edges. The possible drifts number at most $3^b(7/9)^w$ per schedule. The signed ternary terminal congruence determines its integer gap exactly. Thus
$$
 \frac{P-(b+1)S}{S}\le (b+1)3^b(7/9)^w .
$$
The $b+1$ schedules follow by cutting at chronological backward translates of the mechanical seam. Here $g\le S$, $q=P^{1-o(1)}$, $X\to\infty$, and the bounded-width geometric cap yields $\theta\to\lambda$. Taking logs with $S=P^{o(1)}$ proves the physical exponent $\xi_0$.

## Tiny incompatible offsets

For an arbitrary nonresonant lag let $t$ be the shorter residue rank offset. If $t/q\to0$, use that orientation. Its ambiguous fraction is at most $t/q=o(1)$. The rational signed entropy estimate (4) in RATIONAL_RANK_LAG_CONSUMERS.md applies to incompatible offsets as well: the terminal full-denominator residue costs at most $\log S$. Its physical height involves $Xt/q+P$ and its numerical multiplicity is $O(g[1+Pq^2/(Xt)])$. Write $\xi=\lim\log X/\log P$, $v=\lim\log t/\log P$ on a convergent subsequence. Now $\xi\ge\xi_0>2$, so this lower estimate applies even at $v=0$. If $\epsilon$ is a limiting mismatch fraction and $\epsilon\le1/55$, the conditional change-word entropy bound yields
$$
 H(\epsilon)+\epsilon\ln2\
 \ge \frac{\min(1,\xi+v-2)}{\xi+v-1}\ln3
 \ge\min\left((2-\lambda)\ln(9/7),\frac{\ln3}{M}\right).
$$
Here $H$ is binary entropy in nats. The function of $\xi+v$ increases below three and decreases above three. The lower endpoint is $\xi_0$, the upper endpoint is $M+1$, and $\xi_0-1=\ln3/[\ln3-(2-\lambda)\ln(9/7)]$ accounts for the first term.

Both target terms exceed $83/800$. For the first, $3^{200}<2^{317}$ gives $2-\lambda>83/200$ and $\ln(9/7)=2\operatorname{atanh}(1/8)>1/4$. For the second use $M<6$ and $\ln3>1$. On the other hand $H(1/55)+(\ln2)/55\le(1+\ln110)/55<83/800$. The last strict inequality follows by the exact rational comparison $\sum_{j=0}^{11}(753/160)^j/j!>110$. Entropy is increasing in the relevant interval, so compactness leaves a strict margin above $1/55$. When $t/q$ has a positive limit, the earlier two-orientation comparison gives the strict $1/1000$ or $1/36$ according to the input. Applying these cases to a subsequence realizing the global inferior limit proves the stated uniform bounds.

The 2018 logarithm input enters the compatible curvature theorem and the upper physical exponent. The 2026 source is needed only for its separately labeled macroscopic improvement. This is a written theorem. Its ordinary finite-period predecessor has separate exact certificate files.

- https://doi.org/10.22405/2226-8383-2018-19-1-15-25
- https://arxiv.org/html/2610.28079v1#S11
