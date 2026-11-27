# First entrance and final upcrossing on the same ordinary sources

**Source-qualified written counterexample to a proposed reverse-transfer step.** Under the inputs below, a summable sequence of probabilities for the first downward landing can have a nonsummable sequence for the last upward crossing at the very same sets of departure integers. Every source used for the lower bound reaches one. A permanent departure, whose future stays above the ceiling, is a different event. No estimate here excludes it.

Use the shortcut map $T$, its next-odd map $U$, $R=81^j$, $d=\log_2 R$ and an integer ceiling $M=\lfloor d^D\rfloor$ with one sufficiently large fixed $D$. Sample an integer uniformly from $[7R,8R)$. The first downward label is the first shortcut value at most $M$. An upward crossing is an edge $q\to T(q)$ with $q\le M<T(q)$, labeled by its departure $q$. The **last upward crossing** is the chronologically last edge of this type if it exists. Undefined labels receive zero mass. A **permanent departure** is an upcrossing after which every iterate exceeds $M$.

There are sets $S_j\subset[.80M,.85M]$ of positive odd integers for which
$$
 \sum_j\Pr(\text{first downward label}\in S_j)<\infty,
 \qquad
 \sum_j\Pr(\text{last upward label}\in S_j,\ n\text{ reaches one})=\infty.       \tag{1}
$$
The selected final upcrossings occur after a first **odd** landing at a common lower ceiling $L=M(2/3)^k$ with $k=\lfloor1.4\log j\rfloor$ and natural logarithm. Their departures have actual ancestors below $L$ with $k$ successive valuations one. The lower bound concerns a subset of the marked targets relevant to sparse-prefix descent. Equation (1) compares the *same* target sets on the *same* head-source law; it does not assert that the whole sets of targets accessible to that prefix have summably small first-landing laws at this choice of $k$.

## A mark that retains the whole future

Write $\delta>0$ for the natural density of the basin of one. Set $B=M/2^h$ for a positive fixed integer $h$. For $y$ in an interval $I$ with endpoints $.90B+O(1)$ and $.95625B+O(1)$ let
$$
 f_M(y)=1_{\{y\text{ reaches one and }T^i(y)\le M\text{ for all }i\ge0\}}.
$$
The following estimates hold as $M\to\infty$ with $h$ fixed:
$$
 |I|^{-1}\sum_{y\in I} f_M(y)\ge \delta-O(2^{-h})-o(1).                       \tag{2}
$$
The coefficient in $O(2^{-h})$ is absolute. To verify this, let $t=\lfloor.4\log_2 B\rfloor$. On the complete binary grid of depth $t$, the shortcut parity bits are fair independent bits, so $Z_i=3^{p_i}2^{-i}$, where $p_i$ counts odd steps, is a nonnegative mean-one martingale. For every $y\in[.8B,1.1B]$ and $i\le t$, its intermediate states are at least $.8B/2^t$. The exact product for $T^i(y)$ thus gives $T^i(y)\le1.2B Z_i$ for all large $B$. The maximal inequality bounds the grid fraction that can exceed $M$ by $1.2\,2^{-h}$. Incomplete periods cost $O(2^t/B)$. Also $p_t\le .55t$ outside an exponentially small fraction of the grid, and there $T^t(y)\ll B2^{-t(1-.55\log_2 3)}<B^{.98}$. The return theorem in [RETURNS.md](../transfer/RETURNS.md) at source scale $B$, first barrier $B^{.98}$, and a fixed large $K$, bounds all subsequent values through the first $K$ passage by $B^{.98\cdot1.004}<M$, apart from a fraction $O_A((\log K)^{-A})+o(1)$. On convergent inputs the $K$ landing belongs to a finite set of convergent integers, whose entire futures have a finite cap depending only on $K$. First send $B$ to infinity and then $K$ to infinity. The interval has positive fixed proportional length, so its convergence-basin fraction tends to $\delta$. This proves (2).

We need (2) on one growing progression. For any odd $Q$ with $Q 2^t=o(B)$ and any $a\bmod Q$,
$$
 \frac{Q}{|I|}\sum_{y\in I,\ y\equiv a\ (Q)}f_M(y)
 \ge\frac1{|I|}\sum_{y\in I}f_M(y)
 -O\!\left(\sqrt{\frac{\log(2Q)}{t+1}}+2^{-h}+\frac{Q2^t}{B}\right).             \tag{3}
$$
The coefficient in (3) is independent of $h$. Here is the extension to this ceiling-sensitive label. For $0\le b<Q$, whenever $y,y+b$ fuse by time $t$ and both stay at most $M$ through that time, their two labels agree, since their futures coincide. The bad shifts are contained in binary residues of depth $t$ with grid fraction at most
$$ C\sqrt{\log(2Q)/(t+1)}+2.4\,2^{-h}. $$
The first summand is Leen’s uniform counted-pair estimate. For the two height tests use the martingale grid just proved for $y$ and its shift, with $y,y+b\in[.8B,1.1B]$ eventually. These grid tests use the maximal multipliers, so work on all lifts in the indicated interval. Write $F(y)=Q1_{y\equiv a\ (Q)}$. By CRT, the mean of $F(y+b)$ times each binary exceptional indicator over a full period $Q2^t$ equals the binary grid fraction. Covering $I$ by full periods costs at most one period's nonnegative mass beyond $|I|$ if started at the left endpoint. Replacing $\sum_I f_M(y)F(y)$ by $\sum_I f_M(y+b)F(y+b)$ costs $O(Q)$ since $b<Q$ and each endpoint interval contains at most one supported residue. Now replace $f_M(y+b)$ by $f_M(y)$ with the preceding error and average over $b$, using $Q^{-1}\sum_{b<Q}F(y+b)=1$. This proves (3). Only the finite-grid fusion input is imported. Exact invariance of the ceiling test has not been assumed.

## Actual excursions

Use integers $t_0=6u+3>0$ and set
$$
 z=4\,2^kt_0-1,\quad q=4\,3^kt_0-1,\quad r=6\,3^kt_0-1,\quad
 w=(9\,3^kt_0-1)/2 .
$$
Restrict $q$ to $[.80M,.85M]$ and take these $q$ for $S_j$. The $k$ shortcut steps from $z$ to $q$ are successive odd inputs and outputs. The following three shortcut states are $r$, $(3r+1)/2=2w$, and $w$. The first two exceed $M$ and $w=(9/8)(q+1)-1/2<M$. Thus the consecutive increasing states from $z$ cross $M$ precisely at $q\to r$. Since $z=(2/3)^k(q+1)-1$, we have $0<z\le L$ and $z\equiv-1\bmod3$.

The values of $w$ form an arithmetic progression of odd modulus $Q=3^{k+3}$, since $w=Q u+(Q-1)/2$. Impose $w=2^h y$. As two is invertible modulo $Q$, allowed $y$ form one residue modulo $Q$ in the interval $I$ used above, with a bijection to the retained $t_0$. Fix $h$ large enough to make the $2^{-h}$ errors in (2) and (3) smaller than $\delta/4$ in total. Then choose $D$ sufficiently large for the first-landing estimates below and to make the square-root error smaller than $\delta/4$. Indeed $\log Q/\log B\to1.4\log(3)/D$ and $Q2^t/B\to0$. Consequently $\gg B/3^k\gg_h M/3^k$ distinct $z$ yield $f_M(y)=1$. Each such excursion reaches one. After the edge $q\to r$, it returns below $M$ through $w$, takes $h$ halvings to $y$, and subsequently stays below $M$. Thus $q$ labels its actual last upward crossing.

Under Theorem 14 of [*First-landing bounds and canonical inverse laws*](https://rstation.ai/problems/collatz/papers/12/v1), for every $X\ge C L$ and every selected $z$, at least $cX/L$ positive odd sources in $(X/4,X]$ have first odd landing below or at $L$ equal to $z$. These source sets are pairwise disjoint. Choose $X=\epsilon R$ for a sufficiently small positive absolute constant to be specified next. The resulting lower count is $\gg X2^{-k}$.

**Transport into the requested head.** For each counted odd source $n$ set $m=n$ if it is a ternary unit and $m=4n+1$ otherwise. In the latter case $m$ is a unit with $U(m)=U(n)$. Both starting values exceed $M$. At a positive odd unit $v$ a positive odd unit predecessor $(2^a v-1)/3$ exists with $1\le a\le4$: the first admissible positive exponent is one or two, and the next admissible exponent gives the sibling $4x+1$ of the first result $x$. They cannot both be divisible by three. Iterate this choice to get $v_b$ with $U^b(v_b)=m$ for $0\le b\le B_0$. Uniformly at this fixed depth,
$$ \log_2 v_b=\log_2 m+A_b-b\log_2 3+O_{B_0}(1/m), $$
where $A_b$ is the integer sum of the chosen exponents. The finite error follows by expanding the inverse affine word with $a\le4$. Because $\log_2 3$ is irrational, choose one finite $B_0$ such that the first $B_0+1$ rotations can place every initial phase inside a fixed closed subarc of the interior of $[\log_2 7,\log_2 8]\bmod1$. Apply this to $\log_2(m/R)$; the vanishing error stays inside the full arc. Fix $\epsilon$ small enough that all $v_b<7R$ (each inverse step costs at most $16/3$ in height). Every $v_b\gg_{B_0,\epsilon}R>M$ and its intervening shortcut states before $m$ exceed $M$, since each intervening halving stops at its odd endpoint. Thus a nonnegative bounded dyadic shift puts $2^a v_b$ inside $[7R,8R)$ and preserves the selected lower landing and subsequent excursion. There is bounded multiplicity: from one head integer its odd part determines $v_b$, and $b\le B_0$ gives at most $B_0+1$ candidates $m$, each with at most two original $n$. An earlier shortcut crossing during the $m=4n+1$ replacement cannot affect the stated lower bound since the designated last upcrossing occurs after the eventual $z$ landing. The original head fraction marked by the last upcrossing is therefore $\gg 2^{-k}$.

For the upper estimate, $\#S_j\ll M3^{-k}$ since the modulus is $\asymp3^k$ and $D$ is large. The single-arm marginal proof in [HEAD_ROOTS.md, last section](../transfer/HEAD_ROOTS.md) at this very head bounds each regular first-landing atom by $O(\sqrt d(\log d)^{3/2}/M)$, with exceptional total mass $O_A(d^{-A})$. For the integer non-strict cutoff use strict threshold $M+1$ in the first-passage proof, which has the same bounds. Thus the first-downward probability is $O_A(\sqrt j(\log j)^{3/2}3^{-k}+j^{-A})$. Since $1.4\log 3-1/2>1$ whereas $1.4\log 2<1$, the upper series converges and the lower series diverges. This proves (1).

## Logical boundary and sources

The all-time ceiling mark distinguishes a final upcrossing followed by a return from the final departure *without* a return. At every fixed ceiling traversed by a genuinely escaping positive orbit the latter exists once the orbit has entered the interval. A bounded-source convergence series sees no such permanent departure. Positive predecessor density of a fixed escaping unit would push a fixed positive source mass onto that ray's permanent departure at each sufficiently high ceiling. A bound tending to zero just for these marked permanent departures would suffice for the escape branch. The estimates above allow that mass. They refute transporting level-summability for the ordinary last-upcrossing distribution without the additional fate mark. No nonstandard positive cycle is excluded.

The convergence-basin density and the written uniform relative landing and barrier inputs are identified in [RETURNS.md](../transfer/RETURNS.md). The physical marginal uses [PR197 at `578e43911f49d41ef610b368a89b5a1ec269e134`](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md). Leen's counted-pair inequality and finite grid convention are stated explicitly in [*Conditional clocks and source couplings*, equation (1) and Proposition 1](https://rstation.ai/problems/collatz/papers/13/v1). The uniform first-odd landing atom uses the assumptions recorded in paper 12, Theorem 14. These external developments were not rebuilt here. [BarrierExit.lean](BarrierExit.lean) checks only the three finite ascent, crossing, and halving identities, using Std with Lean 4.34.1.
