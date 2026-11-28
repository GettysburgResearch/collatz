# Unbounded ternary densities inside every compact real restriction

**Source-qualified written theorem.** Weaver's joint affine law has every finite ternary $L^q$ moment after a bounded real restriction, also at each exact central clock. Its essential supremum can nevertheless be infinite in every open unit cylinder, even when the real mark lies arbitrarily near zero. The proof builds distinct large first exponents with long critical continuations that fit successively inside the same trit cylinder. It uses Weaver's retained joint floor and the primary paper's balanced-word exit argument. [Weaver, Paper 9/v2, Theorems 16 and 18](https://rstation.ai/problems/collatz/papers/9) · [Weaver, Paper 12, Lemma 13 and Theorems 14–15](https://rstation.ai/problems/collatz/papers/12) · [Earlier maximum-multiplier peaks and critical-word dimension](LANDING_PROFILE_SPIKES.md).

Let $E_i$ be iid with $P(E_i=e)=2^{-e}$ for $e\ge1$. Put $S_i=\sum_{j=1}^i E_j$, $A_i=3^i2^{-S_i}$ and $B_i=\sum_{j=1}^iA_j/3$. Write $R=\lim B_i$ for the real limit and $Z=\lim B_i$ for the ternary limit. An inverse prefix $w$ acts through $F_w(u)=B_w+A_wu$ in both coordinates. Its ternary image is one depth-$|w|$ cylinder and its probability divided by that cylinder's Haar size is $A_w$. Normalize Haar on all of $\mathbb Z_3$. For a real interval $I$ set
\[
 K_{n,I}(z)=3^nP(B_n\in I,\ Z\equiv z\pmod{3^n}),\qquad
 K_{n,d,I}(z)=3^nP(B_n\in I,\ Z\equiv z\pmod{3^n}\mid S_n=d).
\]
Write $g_I$ for the density of $P(R\in I,Z\in dz)$ against ternary Haar.

For every nonempty open interval $I\subset(0,\infty)$, and also for $I=[0,K]$ for any $K>0$, the following hold.

1. Every nonempty unit ball has $\operatorname{ess\,sup}g_I=\infty$. On a common dense $G_\delta$ subset of the units, simultaneously for all such $I$,
\[
 K_{n,I}(z)\to\infty,\qquad
 \min_{|d-2n|\le c\sqrt n}K_{n,d,I}(z)\to\infty
                    \quad\text{for each fixed }0<c<2.                 \tag{1}
\]
The common set has Haar measure zero. Cylinder averages $\mathbb E(g_I\mid z\bmod3^n)$ also tend to infinity there. These statements concern cylinder averages and explicitly defined finite rows and require no choice of pointwise stationary density.
2. In every unit ball the simultaneous small-cap divergence locus in (1), over all $K>0$ and all $c<2$, has ternary Hausdorff dimension at least $H_2(\log_3 2)=0.949955\ldots$. For each fixed open $I$, the same lower dimension holds for its divergence locus in every unit ball.
3. For each $\epsilon>0$ and $N$ there is a unit cylinder on which every sufficiently large positive odd integer $y$ obeys
\[
  \#\{X/4<x\le X:\ x\text{ odd},\ \operatorname{Pass}_y(x)=y,
       \ R_{x\to y}\le\epsilon/y\}\ \ge\ N X/y.                       \tag{2}
\]
Here $R_{x\to y}$ is the base-two log correction up to first landing. All $X\ge C_{\epsilon,N}y$ are allowed. The cylinder can be placed in any prescribed unit ball. In particular (2) holds at arbitrarily large $y$ with $U(y)=1$. With $\nu_1$ the unnormalized natural minimum-cell $m=1$ law of the correction to that first minimum,
\[
                 \limsup_{t\downarrow0}\nu_1([0,t])/t=\infty.          \tag{3}
\]
Consequently even this terminating cell rules out a uniform $O(t)$ upper throughout a punctured neighborhood of the zero endpoint. It does not rule out a better-behaved subsequence, or supply an escape-dependent $t\log(1/t)$ lower on the terminating cell.

## Building one additional family in any prescribed cylinder

Let $\theta=\log_2 3$ and use $s_i=\lceil i\theta\rceil$, with positive consecutive gaps $e_i=s_i-s_{i-1}$. They are one or two. The critical prefix multipliers $a_i=3^i2^{-s_i}$ lie in $[1/2,1]$, including $a_0=1$. Its full ternary code is $\beta$. Start with a ball $z\equiv z_0\pmod{3^h}$ of units, $h\ge1$. Choose an arbitrarily large first exponent $E$, different from all earlier ones, satisfying
\[
                 2^E z_0\equiv1+3\beta\pmod{3^h}.                    \tag{4}
\]
Such exponents fill a nonempty progression since two generates the units modulo $3^h$. Put $\delta=3\,2^{-E}$. For $0<K\le1$, choose $p=\lfloor K/(8\delta)\rfloor>h+2$. Shrink to the nonempty ball
\[
                z\equiv2^{-E}(1+3\beta)\pmod{3^{p+1}}.               \tag{5}
\]
At each $0\le i<p$, follow the first $E$ and $i$ critical letters. The residual target $z_i$ is a unit since the next specified letter exists. Choose an alternative $f$ in a fixed bounded range $[3,L]$ such that $(2^f z_i-1)/3$ falls in the good unit cylinder $\mathcal C$ from Paper 12, Lemma 13. Primitivity modulo $3^{q+1}$, for $q$ the precision of $\mathcal C$, gives this choice. It may depend on the full target inside (5), always with the same bounded range. In the dimension construction below, where critical letters can be larger than two, increase $L$ by another period and choose $f$ unequal to the next letter. The resulting exits are prefix-free within this first-$E$ family, and different first exponents separate distinct families.

The exit prefix $w$ has $c_0\delta\le A_w\le C_0\delta$ and $B_w\le \delta(1+p+C_0)/3$. Its residual lies in $\mathcal C$. Lemma 13 gives constants $B_0,k_0,c_1>0$ and, at every compatible residual target, tail density
\[
 3^kP(B_k\le B_0,\ Z\equiv z'\bmod3^k,\ S_k=s)
                    \ge c_1\pi_k(s),\qquad |s-2k|\le2\sqrt k,         \tag{6}
\]
where $\pi_k$ is the negative-binomial total law. Choose $E$ large depending on $K,B_0$ before fixing $p$. Then $B_w+A_w B_0<K/2$ for every exit and $p\delta\ge K/16$. For $n$ exceeding the lengths of all these prefixes by a sufficiently large amount, sum (6) over the central tail totals. Each exit supplies at least $c_2 A_w$ to $K_{n,[0,K/2]}$. At any prescribed total $d$, it supplies at least
\[
       c_1 A_w\,\pi_{n-|w|}(d-S_w)/\pi_n(d)                          \tag{7}
\]
to the conditional density. For $|d-2n|\le c\sqrt n$, $c<2$, the numerator is within the retained band for all sufficiently large $n$ depending on the finite family. Uniformly in this band the ratio tends to one for each fixed prefix, by the negative-binomial local limit formula (equivalently by the factorial formula on finitely shifted totals). Only finitely many choices in (7) occur, including all the allowed $f$. Thus all sums have a lower bound $c_3 K$ per family, uniformly throughout (5) for all sufficiently large $n$ and every specified central total. The threshold may depend on the finite collection and $c$, not on deeper digits of $z$.

Repeat the construction inside the current ball with distinct $E$ until the sum exceeds any prescribed value $N$. For the stationary cap, on the independent tail event $R'\le1/3$ (of positive probability), $B_n\le K/2$ implies $R=B_n+A_nR'\le K$ because $A_n\le3B_n$. This proves the same eventual cylinder-average lower, after a fixed positive factor. By martingale convergence $g_{[0,K]}$ exceeds the lower bound almost everywhere in that ball. For each $N$, $K$ and $c$ the union of the successful open balls is dense in the unit set. Take countable intersections over integers $N$, reciprocal-integer $K$, and $c\uparrow2$ to obtain (1) for all caps. Fatou's lemma and $\int K_{n,[0,K]}\le1$ give Haar nullity of the divergence locus.

For a general open $I$ and given unit ball $V$, the full product support of the joint real/ternary law supplies a converging code with real offset in the interior of $I$ and address in $V$. At a sufficiently long finite prefix $v$, $B_v$ is in the interior and $F_v(\mathbb Z_3)$ is contained in $V$. Choose a small positive cap $K'$ with $B_v+[0,A_vK']\subset I$. Apply the foregoing construction to the residual address and map its successful balls by $F_v$. Multiplication of densities by $A_v$ and the fixed shift of $n,d$ preserve arbitrary divergence, using a slightly larger central-band constant below two for the residual when necessary. The same argument applies to stationary cylinder averages either directly by the affine recursion or the independent small remainder. Countably many rational open intervals suffice by inclusion. [Weaver, Paper 19, §9.1, equation (B7)](https://rstation.ai/problems/collatz/papers/19).

## Positive integers and the known terminating cell

Use the deterministic critical stream above. At a true positive odd $y$ in a successful ball and $y$ sufficiently large, all inverse prefixes are positive odd integers by residue compatibility. After the initial $E$ their values equal $(y-B_v)/A_v$, are strictly greater than $y$, and are comparable to $y/\delta$ uniformly over the critical segment and its side exit. Denote the side endpoint by $r$. It is a unit, and $U^{|w|}r=y$ with no earlier visit at or below $y$. Its path to $y$ has correction $-\log_2(1-B_w/y)\ll K/y$. The counted own-floor minorant in [the minimum endpoint proof](NATIVE_MINIMUM_ENDPOINT.md) supplies at least $cX/r$ source ancestors first landing at $r$ and having correction at most $b/r$ to that landing, whenever $X\ge C r$. Choose $K$ small compared with $\epsilon$, then all $\delta$ small compared with $K$. Their full arrival corrections at $y$ are at most $\epsilon/y$. Distinct exits give disjoint sets of original sources: the inverse word of the unique first landing on $y$ cannot start with two members of a prefix-free collection, also when $y$ is periodic. One family contributes $\gg KX/y$ from its $p$ side exits. Increase the finite number of families to prove (2), with source onset proportional to the largest $r/y$ of those finite families.

Primitivity gives arbitrarily large $e$ satisfying $2^e\equiv 1+3z_0\pmod{3^{h+1}}$ for any final unit ball $z_0\bmod3^h$. Then $y=(2^e-1)/3$ is a positive odd unit in that ball with $U(y)=1$. For $y>1$ the single extra step adds at most $1/(3y\ln2)$ to the positive correction and reaches the global minimum $1$ for the first time. The closed-interval weak limit on the minimum-one cell transfers the normalized counts, giving $\nu_1([0,(\epsilon+1/(3\ln2))/y])\gg N/y$. Sending $N$ and $y$ to infinity proves (3). This construction is compatible with any prescribed finite binary source residue for the general targets in (2), by the ordinary Chinese remainder theorem; the special direct-parent targets above obey their own binary restrictions.

## A large set of addresses with divergence at every positive cap

Fix a block size $l$ and $s<H_2(1/\theta)$. We can take $l$ large enough that there exists $s'>s$ with
\[
  M_l:=\min_{u=\lfloor l\theta\rfloor,\lceil l\theta\rceil}
                   {u-1\choose l-1}>3^{s'l}.                         \tag{8}
\]
This follows from Stirling's formula since $\theta\ln2=\ln3$. A free stream uses independent uniform $l$-letter compositions of the block totals $\lfloor j l\theta\rfloor-\lfloor(j-1)l\theta\rfloor$. All partial multipliers along such a stream are in $[c_l,C_l]$, by telescoping at block boundaries and the $O(l)$ clock range within a block. Its probability on any given length-$u$ word is at most $M_l^{-\lfloor u/l\rfloor}$. Its probability on any particular depth-$u$ ternary cylinder is at most
\[
                  C_l(u+1)3^{-s'u}.                                 \tag{9}
\]
Indeed $S_u-\theta u=O_l(1)$ and $B_u\le C_l u$. For a fixed allowed total $S$, the numerator $2^S B_u$ has a prescribed residue modulo $3^u$ and belongs to $[0,C_lu2^S]$. There are $O_l(u+1)$ choices. Each numerator and total determine all letters: removing the last term $3^{u-1}$ from the numerator gives $2^{E_u}$ times the preceding odd numerator, and the fixed total recovers the first gap. Summing over the $O_l(1)$ possible totals proves (9). The same bound holds for a stopped free stream of any fixed length at all precisions up to that length.

Starting inside any depth-$h_0$ unit cylinder, perform successive refinements, with $K_j=1/j$ at stage $j$. For each parent of precision $h$, choose a new $E$ satisfying (4) for the fixed ceiling word through $h-1$ letters. Keep exactly those $h-1$ ceiling letters after $E$, and then use a free stream for its remaining letters. With $\delta=3\,2^{-E}$, set $p=\lfloor K_j/(C_l^*\delta)\rfloor$, where $C_l^*$ is a sufficiently large constant depending only on the block multipliers and the fixed good-cylinder routing bound. Choose $E$ so large that $p\ge2h$, $\delta\ll_l K_j$, and $E$ differs from all earlier first exponents on this branch. The new precision is $p+1$. Give children their logical probabilities from the free stream, combining all words with the same ternary child. These finite refinements are consistent probability splittings. The initial congruence with the fixed $h-1$ letters imposes exactly the original depth-$h$ ball. The first free digit immediately specifies the next ternary digit since the map $F_{(E,e_1,\ldots,e_{h-1})}$ has ternary valuation $h$ in its linear part. Thus inside each parent, every relative depth-$u$ subball through the child precision has conditional mass at most the expression in (9). Deepening a selected child cannot change these shallower probabilities.

Every positive-mass child has at least one creating word. For that word, all of its critical partial multipliers after $E$ are within $[c'_l\delta,C'_l\delta]$ since the fixed front and the independent block product each have bounded gain. The positive-offset and side-exit arguments preceding (6) therefore hold with these fixed constants. The lower contribution per stage is $c'_l K_j$ at cap $K_j$ for all sufficiently large $n$, uniformly below the child, at every stated central total. All exits from different stages are disjoint owing to their distinct first exponents. For a point in the support and any fixed $K>0$, restrict to stages with $K_j\le K$. Their contributions sum arbitrarily high because $\sum_j K_j$ diverges, giving (1) on that support. The stationary averages satisfy the same conclusion by applying it first with cap $K/2$.

For the dimension bound, choose $s<s''<s'$ and bound (9) by $C_{l,s''}3^{-s''u}$. On any nested chain the parent precisions at least double. To bound the measure of a depth-$n$ cylinder, follow its completed parent refinements until the first child precision at least $n$, then use the within-parent prefix bound for the last step. All children of a particular parent have one common precision, so the chain is uniquely determined whenever a full refinement is crossed. With at most $1+\log_2(n+1)$ factors the resulting bound is $C_{l,s'',h_0}(n+1)^{C_{l,s''}}3^{-s''n}\ll_{l,s,s'',h_0}3^{-sn}$. The ternary mass distribution principle gives dimension at least $s$. Let $s$ vary up to $H_2(1/\theta)$. For a fixed open interval $I$ move a copy of the small-cap construction through the fixed prefix used above; a ternary similarity preserves its dimension. This lower bound does not identify the exact dimension of the full divergence locus.

For every fixed positive odd unit $m$ the same direct-parent construction solves $2^e m\equiv1+3z_0\pmod{3^{h+1}}$. Its large $y=(2^e m-1)/3$ take one genuine odd step to $m$, with the same extra log bound. Thus every fixed root's natural unnormalized first-arrival correction has infinite upper linear density at zero. If $m\in\mathcal M$, this lower bound holds inside its own global-minimum cell. In the stationary absolute-intercept variable, the natural correction $r$ transforms to $m(1-2^{-r})$ and its first-arrival survival weight is $2^{-r}$. The positive full stationary fibre dominates this weighted first-arrival submeasure up to its fixed normalizing factors. Hence each fixed positive odd unit's stationary fibre also has infinite upper linear density at absolute intercept zero. Paper 19, §9.2's periodic linear estimate concerns the opposite endpoint at intercept equal to the root. [First-arrival weighting and full-lap split](SPATIAL_TRACE_TAIL.md) · [Canonical integer fibre](https://rstation.ai/problems/collatz/papers/19).
