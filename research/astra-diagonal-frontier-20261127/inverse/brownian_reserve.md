# Critical inverse persistence and a near-linear no-return floor

Fix a positive odd integer $a$ prime to three. In an actual inverse word from $a$, write $S_j$ for the sum of its first $j$ positive odd gaps, read outward. All intermediate and terminal integers must be ternary units. Define
\[
 W_\epsilon(a,n)=
 \sum_{\substack{|w|=n\\ S_j(w)>(2-\epsilon)j\ (1\le j\le n)}}
                    3^n2^{-S_n(w)} .
\]
These are geometric weights on one supplied integer tree. Let $m_\epsilon(n)=\inf_a W_\epsilon(a,n)$ over the ordinary roots just specified.

Under the averaged joint Syracuse mixing input (J) used by Weaver in Paper 211 v1, the critical persistence exponent is
\[
              \lim_{n\to\infty}\frac{\log m_0(n)}{\log n}=-\frac12 .   \tag{1}
\]
Moreover, writing $l_\epsilon=\liminf_{n\to\infty}m_\epsilon(n)$ and $u_\epsilon=\limsup_{n\to\infty}m_\epsilon(n)$, for every $\delta>0$ there are positive constants $c_\delta,C$ such that
\[
       c_\delta\epsilon^{1+\delta}\le l_\epsilon\le u_\epsilon
                               \le C\epsilon\qquad(0<\epsilon\le1/8).  \tag{2}
\]
Consequently the logarithms of both extreme quantities divided by $\log\epsilon$ tend to one as $\epsilon\downarrow0$. In the upper bounds the minimizing root can change with the horizon. No upper rate at any individually specified ordinary root follows from this averaging.

There are two direct ordinary consequences. For every nonperiodic unit $a$, relative natural predecessor density $d_a$, and natural reverse entrance law $Q_a$,
\[
\begin{split}
 d_a Q_a(S_j>2j,\ 1\le j\le n)&\ge c_\delta a^{-1}(n+1)^{-1/2-\delta},\\
 d_a Q_a(S_j>(2-\epsilon)j,\ \hbox{every }j\ge1)
                         &\ge c_\delta a^{-1}\epsilon^{1+\delta}.       \tag{3}
\end{split}
\]
At every unit $a$, periodic or otherwise, for $M\ge a$, $0<\epsilon\le1/8$, and $\log(X/M)\ge C_\delta\epsilon^{-2}\log^2(2/\epsilon)$, at least $c_\delta\epsilon^{1+\delta}X/M$ positive odd unit sources in $(X/4,X]$ have their first odd landing at or below $M$ precisely at $a$. Each path takes $O_\delta(1+\log X)$ shortcuts. Its reverse prefixes satisfy $S_j-(2-\epsilon)j>\log_2(M/a)$. The finite-height result also uses the refined fixed-total floor in the companion calculation. [Weaver, *Parity discrepancy before the first Collatz visit to 1*, Paper 211 v1, 23 November 2026, Appendices A–B and §2.1](https://rstation.ai/problems/collatz/papers/211/v1) · [Companion reserve and octave argument](reserve_bootstrap.md) · [Fixed-total selection with a uniform reserve loss](all_slope_no_return.md).

## A one-sided version of the monitored bridge minorant

For fair independent geometric letters of mass $2^{-e}$, put $D_j=S_j-2j$, $\pi_n(s)=2^{-s}\binom{s-1}{n-1}$ and $\beta_n=\sum_{j=1}^n3^{j-1}2^{-S_j}$. There exists an absolute $c_0>0$ such that for each fixed $0<b\le1$, every sufficiently large $n$ depending on $b$, every unit residue $r\bmod 3^n$ and every integer $s$ with $x=(s-2n)/\sqrt n\in[1/4,1/3]$,
\[
 3^n\Pr\{\beta_n=r\pmod {3^n},\ S_n=s,\ \min_{j\le n}D_j>-b\sqrt n\}
                         \ge c_0 b\,\pi_n(s).                         \tag{4}
\]
The input Proposition B.1 concerns a two-sided strip. Here is the modification to its monitored proof, where independence of $c_0$ from $b$ matters. Normalize the left side by $\pi_n(s)$ and call it $F^-_{n,b}(r,s)$. The favorable cylinder and the unmonitored prefix densities $g_M$ satisfying $g_M\ge p_*/2$ there come from (B.2)–(B.3) before choosing a boundary. Fix $0<v<b$ and take the initial mesh in (B.3's proof, §B.3) with mesh spacing $h=\lfloor n^{3/4}\rfloor$. At each mesh date $p$, including the endpoint, require $D_p\ge-v\sqrt n$. Section B.2's conditioned-composition invariance principle (B.4) also holds with any fixed actual prefix. Its minimum has no atom at $-v$. For $x> -v$ the reflection formula for the variance-two bridge gives the survival probability
\[
                  P^-_v(x)=1-\exp[-v(v+x)] .                         \tag{5}
\]
Indeed it is one minus the ratio of the reflected Gaussian endpoint density at $x+2v$ to that at $x$. Uniformity on a fixed compact interval of positive endpoints follows by subsequences and continuity in $x,v$. These are exactly the base convergence hypotheses of (B.5), so its right-hand profile becomes $g_M P^-_v(x)$.

For specificity let $e=(b-v)/8$ and $\ell=\lfloor n^{1/4}\rfloor$. At precision $p-\ell$, switch each nonterminal check to $D_{p-2\ell}\ge-(v+e)\sqrt n$. Keep the original two-sided increment test on every interval of length at most $2h$ inside each selected block and final tail, with threshold $e\sqrt n$. The monitored mixing estimate (A.6) holds for arbitrary tests of the centered sums at the indicated dates. Grouping in (A.7) uses only the prefix total, so its translate at each future date is still the same within a group. The early coarse lifts and the later one-digit lifts keep their stated bounds. A switch can lose a word only if the two sums differ by more than $e\sqrt n$, precisely the same absolute increment test as in §B.3. The union of its short-interval failures has cost $O(n^2\exp[-c_e n^{1/4}])$ per block before the source's grouped bounds. The original summable deletion errors $e_i$ and total normalized $o(1)$ switch and late-lift errors therefore still apply. Between consecutive retained checks at most four long selected blocks and the final tail contribute increments of absolute value at most $e\sqrt n$ each. The shorter selected blocks together contribute $O(\sqrt{h\log h})=o(\sqrt n)$. Since $v+6e<b$, every retained intermediate date satisfies the strict one-sided boundary. This gives (B.6) with $F^-$ and $P^-_v$ on every compact subinterval of $(0,1)$, including a neighborhood of $[1/4,1/3]$.

First take $n\to\infty$ at fixed prehistory index $M$, then $M\to\infty$ using $\sum e_i<\infty$, then $v\uparrow b$. The cylinder minorant has an absolute prefactor independent of $b$. For spreading to all unit residues, §B.4 prepends a bounded exponent of size $\le V$ at the fixed cylinder depth. It multiplies the normalized density by $\ge3\cdot2^{-V}$. Its shift in the residual centered endpoint is $O_V(n^{-1/2})$, so the endpoint remains in that larger compact positive interval. A fixed width slack absorbs the shift of every partial sum, and the ratio of central total probabilities tends uniformly to one. Taking away the slack after the depth limit again gives an absolute prefactor. For $x\in[1/4,1/3]$ and $0<b\le1$, (5) is bounded below by an absolute constant times $b$. Enlarging the onset separately for each fixed $b$ proves (4). This step imports no assertion uniform in a width varying with depth.

On a supplied ordinary unit $y$, the congruence in (4) makes the full word and all its prefixes integral. Iterating $(2^e z-1)/3$ on positive odd inputs gives positive odd outputs whenever integral. A subsequent integral inverse forces its input to be a ternary unit. When the last output is divisible by three, increase only the last letter by two, changing that endpoint to $4z+1$ and making it a unit. This can only raise the last centered sum, costs at most a factor four in geometric weight, and has at most two preimages on the full set of words being repaired. Thus it costs at most a factor eight overall. Summing (4) over the displayed band of totals gives an absolute $c_1>0$ such that the aggregate physical weight is at least $c_1b$. The lower endpoint gain is at least $\sqrt n/4$ and the final gain is at most $\sqrt n/3+2$.

## Buying a multiplicative increase in reserve

Choose a fixed integer $J\ge8$ before selecting a block length. At reserve $R\ge R_0(J)$ take $n_R=\lfloor J^2R^2\rfloor$ and $b=1/(2J)$ in (4). The maximum possible loss of centered reserve is $R/2$. The terminal gain is at least $JR/5$, so the new lower reserve is $R'=(1+J/5)R$. The retained unnormalized physical mass is at least $c_2/J$ with $0<c_2<1$ absolute. The same bounds apply to a $2-\epsilon$ reserve, since its increment gets the additional nonnegative term $\epsilon n_R$. At every step the block length and the lower reserve are common across all paths. Since $J$ is fixed, a single $R_0(J)$ covers its width-dependent shell onset at every later stage.

Write $g=1+J/5$. A bounded initial unit gap at a supplied $a$ buys $R_0(J)$ units of strict reserve at weight $c_J>0$. If the threshold is $M\ge a$, choose that gap in a bounded-width interval above $\log_2(M/a)+A+R_0(J)+2$, instead, at weight $\ge c_Ja/M$. Here $A$ is the absolute strict-height margin of the companion argument. Upon reaching a requested lower reserve $K$, the number of stages is at most $1+\log(K/R_0)/\log g$ when $K>R_0$, and zero otherwise. By multiplication of (4) on the real tree, the retained weight apart from the initial bridge is at least
\[
          c_J(1+K)^{-\alpha_J},\qquad
                 \alpha_J=\frac{\log(J/c_2)}{\log(1+J/5)}
                                  \longrightarrow1.               \tag{6}
\]
The total number of letters before the last stage ends is $O_J(1+K^2)$ by the geometric sum of the deterministic block lengths. The same bound holds for its total gap sum apart from the initial threshold bridge. These bounds also hold with $K$ replaced by the lower reserve actually attained along the geometric schedule.

For (2), take $K=C\epsilon^{-1}\log(2/\epsilon)$ plus a fixed margin, enough to fund every prefix of the final selected family by the companion all-slope bound. At each funded terminal take one bounded bridge into the favorable cylinder, large enough to exceed the absolute offset cutoff $4F+4$. Given any sufficiently large common target horizon $n$, the remaining number of letters $t$ is independent of the endpoint. Sum the refined fixed-total floor at length $t$ over a central window of $\asymp\sqrt t$ totals, prescribing the extra terminal unit digit. The resulting unnormalized weight is bounded below by one absolute constant. Thus (6) is a uniform lower bound up to absolute factors for $m_\epsilon(n)$ at all sufficiently large $n$. For any $\delta>0$ choose $J$ so that $\alpha_J<1+\delta/2$; the logarithm in $K$ is then absorbed into $\epsilon^{-\delta/2}$. This proves the lower bound in (2). For the finite octave count, use instead the final assembly and strict height estimate of the companion reserve argument. Each common-depth terminal $y$ contributes $\gg X/y$, their reciprocal heights satisfy the same telescope, and first landing at $a$ distinguishes all complete routes. The onset $C_\delta\epsilon^{-2}\log^2(2/\epsilon)$ in log height accommodates the entire funded prehistory.

For the critical lower bound fix $J$. Let $R_i=R_0g^i$, and let $N_i$ include the initial gap and all completed stages through reserve $R_i$. There is $C_J$ with $N_i\le C_J R_i^2$ for every $i$. At fixed large calendar horizon $n$, choose the last $i$ with $R_i\le \sqrt{n/(2C_J)}$. Then $N_i\le n/2$ and $R_i\ge c_J\sqrt n$. The last $t=n-N_i\in[n/2,n]$ letters can be chosen using (4) at one fixed width $b_J\le c_J/2$, small enough that the possible loss is at most $R_i/2$. They have weight $\gg_J1$. Formula (6), or the exact number $i=\log(R_i/R_0)/\log g$ of completed stages, now gives $m_0(n)\gg_J n^{-\alpha_J/2}$. This proves the desired critical lower bound after increasing $J$. For bounded $n$ needed in (3), any prescribed finite horizon has a positive uniform weight floor, for example by choosing at each step a legal unit child at exponent between $3$ and $8$.

## The upper comparison and the ordinary natural law

Average $a$ over a complete set of positive odd unit representatives modulo $3^{n+1}$. For each fixed $n$-gap word, integrality and a unit endpoint pick exactly two of the $2\cdot3^n$ unit residues. The resulting average of $W_\epsilon$ is therefore the independent geometric probability of its prefix conditions. This equality follows first for finite total cutoffs, then by monotone convergence. In particular it is an upper bound for the infimum.

Realize the independent gaps as the interarrival times of successes in independent fair bits. If the first $n$ completed gaps all obey the critical strict condition, the simple symmetric walk with increments $+1$ at failures and $-1$ at successes is strictly positive from native time one through the $n$th success, hence at least through time $n$. The reflection principle gives strict survival through $n$ with probability $O(n^{-1/2})$. This proves the other half of (1).

At positive $\epsilon$, survival at every completed gap is strict survival after time zero of the native walk with increments $1$ and $-1+\epsilon$ of equal probability. Its first step must be $1$. The positive zero $s_\epsilon$ of $(e^{-s}+e^{(1-\epsilon)s})/2=1$ satisfies $s_\epsilon=O(\epsilon)$ by Taylor expansion at zero, uniformly for $0<\epsilon\le1/8$. Start the walk at height one. Stopping its exponential martingale at the first nonpositive height gives $e^{-s_\epsilon}\le e^{s_\epsilon}\Pr(\text{hit})$, since overshoot is at most one and on an infinite surviving path the walk tends to infinity by positive drift. The stopped martingale is bounded. Thus infinite survival is at most $1-e^{-2s_\epsilon}=O(\epsilon)$. The finite geometric survival probabilities decrease to that value, proving the last inequality of (2).

At a nonperiodic root $a$ the natural mass of each depth-$n$ unit predecessor cylinder ending in $y$ is $d_y/d_a$. Distinct endpoints at fixed depth give disjoint cylinders. The reciprocal predecessor lower bound $d_y\ge c/y$ and the actual height inequality $y\le 2^{S_n}3^{-n}a$ therefore give $d_aQ_a(\text{strict survival through }n)\ge c W_\epsilon(a,n)/a$. This proves both lines of (3), using continuity from above at fixed $a,\epsilon$ for the second. In particular the critical canonical law also has the lower comparison $P_{h,a}(\text{survival through }n)\ge cW_0(a,n)/h(a)$ from its terminal trace floor. The fixed-root iterated-logarithm theorem gives eventual critical failure almost surely. [Canonical ordinary inverse paths at commit aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) · [Fixed-root lower fluctuations](inverse_fluctuation_lower.md).

For a fixed nonperiodic $a$, let $T=\inf\{j\ge1:S_j\le2j\}$. Under $Q_a$ it is almost surely finite by the cited fixed-root lower fluctuation theorem, while $\mathbb E_{Q_a}[T^q]=\infty$ for every $q>1/2$. Choose $0<\delta<q-1/2$ in (3) and use the discrete tail-sum formula for the $q$th moment. The same conclusion holds for the canonical law at every fixed positive odd unit under the trace-floor and fixed-root fluctuation inputs. These estimates do not determine the moment of order exactly $1/2$.
