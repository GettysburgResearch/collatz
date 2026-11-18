# The real-offset fibre has no finite endpoint density at any supplied integer unit

**Proposed, source-qualified.** Use additive ternary Haar probability $\lambda$, the stationary geometric inverse series in the real and ternary completions with joint law $\Sigma$, and its canonical ternary density $h$ in the normalization $\int h\,d\lambda=1$. For a positive integer $t$ coprime to $3$, let $F_t$ be the unnormalized real-offset law of its canonical inverse walk, of total mass $h(t)$. Then $F_t([0,r])/r$ cannot have a finite limit as $r\downarrow0$. The assertion also holds after division by $h(t)$. The argument does not rule out a bounded lower limit, or prove that the upper limit is infinite.

In fact no vague subsequential limit of $r^{-1} F_t(r\,du)$ on $(0,1)$ can have density bounded by a constant on an entire interval $(0,\eta)$. The proof uses the positive retained-word floor in paper 12 and pure singularity of the stationary **joint** law from paper 19. It does not require a singular real marginal, or any assumption on the forward orbit of $t$. [Paper 12 v1, Lemma 13](https://rstation.ai/problems/collatz/papers/12/v1) · [Paper 19 v2, joint singularity and integer real fibres](https://rstation.ai/problems/collatz/papers/19/v2)

## The first exponent and the bounded-real floor

For the unit-compatible exponent $e$ write $x=(2^e t-1)/3$, $J_e=3/2^e$ and $b_e=2^{-e}$. The transition to an integer unit child $x$ has probability $J_e h(x)/h(t)$. This is paper 19's odd-root law. It also defines a walk at every positive **even** ternary unit $t$: the ordinary trace is finite, positive and satisfies $Lh=h$ there, so the probabilities sum to one, and all children are positive odd integers. Nonunit children have zero harmonic weight. The harmless constant between the local normalization and the present $h$ cancels from all transitions. The real offset satisfies $B=b_e+J_e B'$ after the first step. It exists on all integer codes by monotonicity and the finite identity $t=b_w+J_wx_w$; in particular $B>0$ on every infinite path. [Harmonicity at odd and even positive roots, §2](../native-pressure-20261118/CANONICAL-RETURN.md) · [Paper 19 v2, (B3)–(B5), (F2)](https://rstation.ai/problems/collatz/papers/19/v2)

For every $k\ge0$ and Borel $I\subset(0,1]$ one has exactly
$$
 2^k F_t(2^{-k}I)=F_{2^k t}(I).                                      \tag{1}
$$
If $2^kB\le1$ then $e>k$, since $b_e\ge2^{-k}$ for $e\le k$ and the residual offset is strictly positive. Replace $e$ by $e-k$ at $2^kt$: it gives exactly the same integer child, multiplies $b_e,J_e$ by $2^k$, and leaves the remaining walk unchanged. Summing the unnormalized transition laws proves (1).

There exist absolute $C,c>0$ such that
$$
 F_t([0,C])\ge c                                                     \tag{2}
$$
for every positive integer unit. Here are details needed for the uniformity. For a word of length $q$, write $A_j=3^j2^{-S_j}$ for its multiplier through $j$ letters with total $S_j$, and $B_j=\frac13\sum_{i=1}^j A_i$. Paper 12, (39), gives a fixed unit cylinder $V$ and absolute $B_0,c_0$ such that at each sufficiently large $q$ and every odd integer $v\in V$, the sum of $A_q$ among legal words with $B_q\le B_0$ is at least $c_0$. Indeed sum (39) over central totals $|S_q-2q|\le2\sqrt q$, whose geometric probability is bounded below (variance $2q$). A word with a terminal nonunit integer can be changed by increasing its last exponent by two. Its endpoint becomes $4x_q+1$, a unit, its multiplier is divided by four, its last positive offset summand decreases, and this operation is injective on the modified words. Including the unmodified unit words gives multiplicity at most two. Their total multiplier is therefore still bounded below. By the absolute positive harmonic floor at unit children and the telescoping prefix probabilities, $h(v)\Pr_v(B_q\le B_0)\ge c_1$. These events decrease in $q$, proving $F_v([0,B_0])\ge c_1$. Finally for any initial $t$ choose a uniformly bounded $e\ge1$ for which $(2^e t-1)/3$ lies in $V$. This uses that $2$ generates the units modulo $3^{d+1}$, where $d$ is the precision of $V$; the chosen compatible child is an odd positive integer. Its prefix has multiplier bounded below, and $2^{-e}(1+3B_0)$ is bounded above uniformly. This proves (2).

## Long consecutive stretches of the dyadic orbit dominate the joint stationary law

Write $m_\times=(3/2)\lambda$ on ternary units for normalized Haar there. For any ternary residue cylinder $D$ in the units and open bounded interval $I\subset(0,\infty)$, the following lower estimate is uniform in the starting time of the average:
$$
 \liminf_{N\to\infty}\inf_{d\ge0}\frac1N
 \sum_{k=d}^{d+N-1}{\bf1}_D(2^kt)F_{2^kt}(I)\ \ge c\,\Sigma(I\times D).       \tag{3}
$$
In fact for any fixed word $w$ of length $q$ at least the precision of $D$, if $B_q+A_q[0,C]\subset I$, its cylinder contributes at least $c A_q$ to $F_y(I)$ whenever $y$ is compatible and the child $x_q$ is a unit, by (2). These path cylinders at a fixed depth are disjoint. Its ternary legality fixes one residue modulo $3^q$, necessarily a unit. The three lifts modulo $3^{q+1}$ give the three distinct child residues modulo $3$ since $x_q=(y-B_q)/A_q$. Thus exactly two lifts are eligible, of combined $m_\times$-mass $3^{-q}$. The target condition $D$ either retains both or neither. The values $y=2^kt$ enumerate the units modulo $3^{q+1}$ periodically, with the same limiting frequencies uniformly over all consecutive blocks of length $N\to\infty$. Apply this count first to a finite family of words; then increase the family by positivity. Each resulting weight $A_q3^{-q}=2^{-S_q}$ is precisely the iid geometric word probability. The condition $D$ then reads $Z\in D$ on the infinite iid continuation. Under this law $A_q\to0$ and $B_q\to B$ almost surely. If $B\in I$, eventually $B_q+A_q[0,C]\subset I$. Fatou's inequality now yields (3).

## A bounded-density tangent would contradict joint singularity

Suppose along some $r_i\downarrow0$ the rescaled measures $r_i^{-1}F_t(r_i\,du)$ converge vaguely on $(0,1)$ to a locally finite measure bounded by $M\,du$ on $(0,\eta)$, $0<\eta\le1$. Select integers $k_i\to\infty$ with $v_i=2^{k_i}r_i\in(1/2,1]$, passing to a subsequence with $v_i\to v\in[1/2,1]$. For every open interval $I$ with closure in $(0,\eta/2)$ and each fixed $j\ge0$, (1) gives
$$
 F_{2^{k_i+j}t}(I)=2^jv_i\,[r_i^{-1}F_t(r_i\,du)](2^{-j}I/v_i).
$$
The moving endpoints converge to points strictly inside $(0,\eta)$. Using slightly enlarged compact intervals and then decreasing them proves $\limsup_i F_{2^{k_i+j}t}(I)\le M|I|$. For each fixed $N$ use this at the finitely many $0\le j<N$, then let $N\to\infty$. Uniform frequencies of $2^kt$ in $D$ give an upper bound $M|I|m_\times(D)$ for the resulting block averages. Equation (3) supplies the lower bound $c\Sigma(I\times D)$. The rectangle inequality implies $\Sigma\ll du\,dm_\times$ on $(0,\eta/2)\times\mathbb Z_3^\times$, by dyadic interval partitions and regularity. This portion of $\Sigma$ has positive mass: take the first geometric exponent sufficiently large and an independent finite real tail bounded by a fixed constant. Joint pure singularity from paper 19 is a contradiction. In particular, a finite limit $F_t([0,r])/r\to C'$ would give the excluded tangent $C'\,du$ by subtracting the cumulative values at the two ends of each interval.
