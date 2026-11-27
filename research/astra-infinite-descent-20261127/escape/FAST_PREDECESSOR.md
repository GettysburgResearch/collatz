# A fast predecessor in every relative interval

Let $T$ be the shortcut map, $y$ any positive odd integer coprime to three, and $\alpha=\log_2 3$. For $D\ge1$, let $\Delta_D$ be the largest circular gap among $\{-j\alpha\bmod 1:0\le j\le D\}$. For $L\ge3$ put

$$
 A=y2^{L+3+6D},\qquad
 \nu=-\log_2(1-8/(5\,2^L y)).
$$

**Finite interval theorem.** For every $Z\ge A$ and $\log_2(1+\delta)>\Delta_D+\nu$, there is an integer $z\in[Z,(1+\delta)Z)$ coprime to three whose first visit to $y$ uses some $j\le D$ odd departures and a shortcut time $t$ with

$$
    0\le t-\log_2(z/y)-j\alpha\le\nu.                              \tag{1}
$$

Every shortcut state through that hit is at most $(3z+1)/2$. The starting integer may be even. For fixed $\delta>0$ the excess over the fastest possible time $\log_2(z/y)$ is bounded independently of $y,Z$. This result uses elementary finite inverse branches and irrational rotation. No predecessor-density result enters. The moving-target complement below gives the limiting largest gap of the full set of bounded-grade sources.

## A row of actual positive ancestors

For a positive odd unit $v$ and $E\ge1$, among the four exponents $e=E,\ldots,E+3$ at least one has $2^e v\bmod9$ equal to $4$ or $7$. Check the six possible residues of $2^Ev\bmod9$. Then $w=(2^e v-1)/3$ is a positive odd unit. The first shortcut step from $w$ gives $2^{e-1}v$ and the following $e-1$ halvings give $v$. Exactly one departure is odd.

Start from $v_0=y$. Use $E=L$ for the first inverse edge and $E=3$ for subsequent edges. Write $v_j$ for the resulting ancestor, $S_j=\sum_{i\le j}e_i$ and $S_0=0$. Every $v_j$ is an actual positive odd unit. The odd nodes strictly increase with $j$, because $e_i\ge3$. The forward segment from $v_j$ first visits $y$ exactly at $S_j$ with $j$ odd departures, since every prior odd is larger than $y$ and the intermediate even states are positive multiples of the next odd. For $j\ge1$,

$$
  S_j\le L+3+6(j-1),\qquad
  3^jv_j+B_j=2^{S_j}y,\qquad
  5\,2^L B_j+2^L3^j\le8\,2^{S_j}.                                 \tag{2}
$$

At $j=1$ use $B_1=1$. A further step with exponent $e\ge3$ gives $B_{j+1}=2^e B_j+3^j$. In the last inequality's numerator the new two contributions of size $2^L3^j$ have coefficient $5+3=8\le2^e$. This proves the invariant. In particular

$$
 \log_2(v_j/y)=S_j-j\alpha-\ell_j,\qquad 0\le\ell_j\le\nu.
$$

Use $v_0=y,\ell_0=0$. Since $v_j\le A\le Z$, lift each $v_j$ by a unique nonnegative power of two into $[Z,2Z)$. Its log phase stays the same. Any arc of length greater than $\Delta_D+\nu$ contains a lifted phase. Indeed the ideal phases form a net of largest gap $\Delta_D$, and each representative has moved to the left by at most $\nu$. Apply this to the arc starting at $\log_2(Z/y)$ and ending at $\log_2((1+\delta)Z/y)$. For $\delta\ge1$ use the whole octave. If the lift is $z=2^r v_j$, then $t=r+S_j$ and the first-hit and odd-count claims follow. Every intermediate even state on an odd edge is bounded by the immediate odd image $(3v_i+1)/2$, and the leading even coast is bounded by $z$. This proves (1).

The Lean code checks the unit choice, the actual shortcut steps, the count and both integer bounds in (2). [InverseSpreading.lean](InverseSpreading.lean)

## All bounded-grade sources and a sharp moving-target limit

For fixed $X\ge A$, let $\Theta(y,X,D)$ be the phases $\log_2(z/y)\bmod1$ of **all** $z\in[X,2X)$ with an actual visit to $y$ using at most $D$ odd departures. Let $G(\Theta)$ denote its largest circular gap. If $((3/2)^D-1)/y<1$, put

$$
 \nu_*=-\log_2\left(1-\frac{(3/2)^D-1}{y}\right).
$$

Then

$$
    \Delta_D-\nu_* \ \le G(\Theta(y,X,D))\le\Delta_D+\nu.            \tag{3}
$$

The upper bound follows from the constructed row. For the lower, every actual prefix at time $t$, grade $q$ has the numerator identity $2^t T^t z=3^qz+B$. Its additive height satisfies $B/2^t+1\le(3/2)^q$. For an even departure the height of the prior offset is halved; for an odd departure the height plus one is multiplied by $3/2$. Induction starts at one. Thus at a hit on $y$, $\log_2(z/y)\bmod1$ is the ideal point $-q\alpha$ moved to the left by at most $\nu_*$. Within the largest ideal gap, at most a right-hand portion of length $\nu_*$ can then contain actual phases. This proves (3), including vacuous negative lower bounds. The all-prefix integer inequality is checked as *grade_defect*.

For fixed $D,L$ the gap tends to $\Delta_D$ as $y\to\infty$ through odd units, uniformly over all octaves $[X,2X)$ with $X\ge A$. The conclusion also holds with vanishing error for varying $D$ when $(3/2)^D=o(y)$. In particular $\Delta_D\ge1/(D+1)$. A uniform theorem in moving $y$ that assumes only a budget of $D$ odd inputs cannot guarantee a source in windows much narrower than that relative scale. The first-hit version of (3) holds as well, since the explicit row consists of first hits and the lower bound applies to every hit.

## Clock and interval choices

Irrationality of $\log_2 3$ follows from unique factorization. A finite initial segment of the rotation covers the circle at every prescribed mesh. Given $0<\delta\le1/2$, choose $D$ so that $\Delta_D<\tfrac12\log_2(1+\delta)$ and $L\ge3$ so that $\nu<\tfrac12\log_2(1+\delta)$ even at $y=1$. This proves the all-target, all-location theorem for fixed $\delta$ with a uniform threshold $Z/y$.

For explicit shrinking widths, write $q_m$ for the convergent denominators of $\alpha$. Each consecutive block of $q_m$ rotation points is within $1/q_m$ pointwise of a translated permuted grid of mesh $1/q_m$, so its largest gap is at most $3/q_m$. An entirely elementary lower bound $|b\log3-a\log2|\gg3^{-b}$ for a nearest integer $a$ gives $q_{m+1}\ll 3^{q_m}$. It follows that $\Delta_D\ll1/\log(2+D)$. Along $D=q_m$ one instead has $\Delta_D\ll D^{-1}$.

Wu and Wang's Theorem 1 on three-term linear forms in $1,\log2,\log3$ implies $\|j\alpha\|\gg_\kappa j^{-\kappa}$ for every $\kappa>4.1163051$, by setting the constant coefficient to zero. This is exactly the primary-source input used in PR205. For the first denominator $q_m\ge C/\delta$, its predecessor is less than $C/\delta$ and $q_m\ll_\kappa\delta^{-\kappa}$. It suffices in (1) to take $D\ll_\kappa\delta^{-\kappa}$ and $L=O(1+\log(1/\delta))$. Hence for every $\sigma<1/4.1163051$ and all sufficiently large $Z/y$, there is a visitor in every window of relative width $(\log(Z/y))^{-\sigma}$. Its time exceeds $\log_2(z/y)$ by a sublinear power of $\log(Z/y)$. On the unbounded bands $Cq_m\le\log_2(Z/y)\le2Cq_m$ for a large absolute $C$, width $O(1/\log(Z/y))$ suffices by taking $D=q_m$. The order on these bands is sharp in the moving-target sense of (3). [Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) · [PR205, pinned commit and short-window transfer](https://github.com/GettysburgResearch/collatz/pull/205)

PR205 and its PR201/203 inputs already give linearly many first-hit sources in thinner-than-fixed relative windows, with mixed digits and prescribed clock residues. Its fixed-target, all-location width exponent at fixed clock modulus is $1/(2\cdot4.1163051)$, and its favorable bands have $\log X$ of order $q_m^2$. Their construction counts central total-valuation histories. Here the tradeoff concerns one near-fastest actual source, a number of odd departures chosen across a range of order $\log(Z/y)$, and constants uniform over all odd unit targets. The rank-one phase argument with the all-prefix upper inclusion also identifies the worst moving-target mesh. Finite fixed-length rotation nets in other Collatz orbit-placement constructions appear in Weaver's paper 222. [Weaver, *The order of odd Collatz states within a factor of two*](https://rstation.ai/problems/collatz/papers/222)

## Distance from the forward problem

An actual predecessor at some point of every specified source interval does not select the integer at that interval's endpoint. At $Z=2^J$ even the favorable guaranteed width in this result is of order $2^J/J$. This exceeds the available all-member synchronization lengths. No density input is needed for this gap statement, and no averaging across starting values makes the actual designated pair meet.
