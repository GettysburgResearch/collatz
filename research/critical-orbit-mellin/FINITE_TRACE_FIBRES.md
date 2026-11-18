# Singularity of the real inverse fibre at every finite ternary trace

**PROPOSED, source-qualified.** Write $b(t)=\lim_q L^q1(t)$ for the mean-one pointwise trace and $\lambda$ for ternary Haar probability. At every unit $t\in\mathbb Z_3$ with $b(t)<\infty$, the canonical inverse walk has transitions $J_a b(s)/b(t)$ to $s=(2^at-1)/3$ on legal letters, $J_a=3/2^a$. The law of its real offset
$$
 B_0=\sum_{i\ge1}3^{i-1}2^{-(a_1+\cdots+a_i)}
$$
is purely singular to Lebesgue measure. This includes every finite-trace irrational phase. The [ordinary integer result](../terminal-residue/SINGULAR_FIBRES.md) is prior in this repository. Here its argument applies at every finite trace using a uniform lower bound for joint observation probabilities and requires no fixed-root almost-sure word law. The external inputs are the stationary joint singularity of [paper 19](https://rstation.ai/problems/collatz/papers/19/v2), the [every-depth trace and local-test convergence](../native-pressure-20261118/EVERY-DEPTH.md), and the positive bounded-offset mass in [paper 12](https://rstation.ai/problems/collatz/papers/12/v1).

Since $b=L b$ at finite-trace points, all visited phases have finite trace and are units almost surely. The [sibling estimate](RECORD_POLE_RIGIDITY.md) bounds every partial real offset at a finite root in terms of $b(t)$, hence $B_0$ is finite along every legal infinite path there. Define $F_t$ to be $b(t)$ times its law, and $B_q$ the analogous real series starting at the ancestor $X_q$. Let $\Sigma$ be the stationary joint law of the real and ternary offsets of a single iid geometric inverse word.

## A lower bound after arbitrary path restriction

There are absolute $C,c>0$ with $F_s([0,C])\ge c$ at every finite-trace unit $s$. The [bounded-real floor proof](../terminal-residue/ENDPOINT_ODOMETER.md) extends verbatim: the finite selected word event (paper 12, equation (39), summed over its central totals) depends on the indicated ternary digits and the word's real offset. For a nonordinary phase choose a positive odd representative at the required ternary precision. The terminal unit constraint needs at most one extra ternary digit; increasing the last exponent by two replaces a nonunit child $x$ by $4x+1$, a unit, with bounded multiplicity and a factor four cost. The uniform lower bound on $b$ for unit children gives $b(s)\Pr_s(B_0^{[q]}\le C_0)\ge c_0$ on the selected cylinder. The events decrease to $\{B_0\le C_0\}$. A bounded first exponent reaches that cylinder from every unit and the resulting child remains a finite-trace phase. This proves the asserted full-unit floor.

For every such starting $t$, every open bounded interval $I\subset(0,\infty)$, every ternary cylinder $D$, and every measurable path event $E$,
$$
 \liminf_{q\to\infty}\Pr_t(E,\ B_q\in I,\ X_q\in D)
 \ \ge c'\Pr_t(E)\,\Sigma(I\times D)                                      \tag{1}
$$
with $c'>0$ absolute. First take $E$ equal to the full space. Fix $m$ at least the precision of $D$ and any finite family of length-$m$ inverse words $w$ satisfying $\beta_w+J_w[0,C]\subset I$. At a finite-trace phase $s$ in $D$ each compatible word with unit child contributes at least $cJ_w$ to $F_s(I)$. Sum these disjoint contributions, setting the sum to zero outside $D$. The resulting local function $f$ satisfies $f(s)\le {\bf1}_D(s)F_s(I)$ on the finite-trace unit states. On nonunit states the lower function also vanishes, since it includes a nonempty legal prefix (take $m\ge1$). Transfer gives
$$
 \Pr_t(B_q\in I,X_q\in D)\ge L^q f(t)/b(t)\longrightarrow\lambda(f).
$$
For a compatible word the target lies in a single depth-$m$ unit ball, and two of its three lifts at depth $m+1$ have unit child. Therefore its Haar integral contribution is $(2c/3)2^{-\sum a_i}$ when the ball lies in $D$. Increase the finite family at this fixed length to all qualifying words. Under the iid geometric word the real offsets $\beta_w$ converge almost surely to the stationary real series, $J_w\to0$ almost surely, and the target's first $m$ ternary digits are already determined. Taking $m\to\infty$ and using Fatou proves (1) for the full event. The same absolute coefficient holds for every finite-trace root. On any fixed prefix cylinder the future process restarts at such a root, so multiplying by its probability proves (1) for that cylinder and then for finite disjoint unions. Approximate arbitrary $E$ in path probability by finite unions of cylinders to obtain (1).

## Contradiction to joint singularity

If the fibre at $t$ has a nonzero absolutely continuous component, choose a Borel set of positive probability on which its restricted real law is bounded by $K$ times Lebesgue measure. Let $E$ be the corresponding path event. For each prefix word to $X_q\in D$, its subsequent tail in $I$ puts $B_0$ in the affine interval $\beta_w+J_w I$. Hence
$$
 \Pr_t(E,B_q\in I,X_q\in D)\le K|I|L^q{\bf1}_D(t)\longrightarrow K|I|b(t)\lambda(D).
$$
Combine with (1). The joint stationary law would be dominated by a finite multiple of Lebesgue times Haar on intervals times ternary cylinders, hence on all Borel sets. This contradicts its established joint singularity. The proof transfers that singularity to each finite-trace root individually. It gives a lower bound on moving tail observations, without asserting their every-depth weak convergence.

## Compact null support at finite trace

For every finite-trace unit $t$, the closure of the real offsets of **all** its legal infinite codes is exactly $\operatorname{supp}F_t$; it is compact and Lebesgue-null. This extends the [positive integer support result](../terminal-residue/SUPPORT.md). Compactness follows from the uniform bound on $B_0$ at this fixed $t$. We give the mass lower bound proving the closure and nullity assertions.

First $F_s([0,\varepsilon])\gg\varepsilon$ for $0<\varepsilon\le1$, uniformly at all finite-trace units $s$. Choose an exponent $a$ within six above $\max(1,\lceil\log_2((1+3C)/\varepsilon)\rceil)$ sending $s$ to a unit child. The bounded-real floor there puts mass at least $cJ_a\gg\varepsilon$ in this interval on returning to $s$.

Consider any finite prefix with unit terminal phase of any legal infinite code at $t$. Write $r=\beta_w=\sum_{j=1}^kP_j/3$, $r_i=\sum_{j\le i}P_j/3$, $d_i=r-r_{i-1}$ for $i\le k+1$. For each $j\ge i$, the changed-unit sibling from the [record-pole estimate](RECORD_POLE_RIGIDITY.md) gives mass $\gg P_j$ within $O(d_i)$ of $r$, by the bounded-real floor. These departure events are disjoint. Thus $F_t([r-C_1d_i,r+C_1d_i])\gg d_i$. Given $0<\varepsilon\le1$, if $r\le\varepsilon$ use the small real floor at $t$. Otherwise choose $i$ with $d_i>\varepsilon\ge d_{i+1}$. If $d_{i+1}\ge\varepsilon/2$, the last estimate suffices. Otherwise $P_i/3=d_i-d_{i+1}>\varepsilon/2$; at the original phase after $i$ letters use its small real floor with argument $\varepsilon/P_i<1$. This contributes $\gg\varepsilon$ within $2\varepsilon$ of $r$, since $|r_i-r|\le\varepsilon$. We have proved, with absolute constants,
$$
 F_t([r-C_2\varepsilon,r+C_2\varepsilon])\ge c_2\varepsilon .
$$
The estimate extends by closure to every possible infinite offset and its closure, as the partial sums on that code converge. Hence each such point belongs to the support; the opposite inclusion follows since the law is carried by these codes' image up to null sets. Every support point has positive upper symmetric Lebesgue derivative of $F_t$, while that derivative vanishes Lebesgue-almost everywhere by the pure singularity just proved. The whole compact support has Lebesgue measure zero.

## Full dimension of bounded legal offsets at every phase

At **every** ternary unit $t$ there is a bounded set of real offsets of legal infinite codes of Hausdorff dimension one. At each finite-trace $t$ its compact null fibre support therefore has Hausdorff dimension one. This is a statement about the support and does not identify the lower dimension of the full probability measure at all such phases.

Here are the inputs to a uniform real Cantor construction. With $q$ sufficiently large and $A=2q$, every unit phase $s$ admits at least
$$
 c(4/3)^q/\sqrt q
$$
distinct legal length-$q$ inverse words of this clock, with offset $\beta_w\le B$ and unit child, for absolute $B,c$. Indeed at the selected mark of [paper 12, Lemma 7, (39)](https://rstation.ai/problems/collatz/papers/12/v1) retain its stated bounded real offset and central total. One additional ternary digit suffices to prescribe a unit child: take the spatial target residue for $\beta_w$ equal to $s-3^q2^{-A}$ modulo $3^{q+1}$. To reach the selected mark from any unit insert one bounded outer exponent, as in the [central total spreading calculation](../native-pressure-20261118/EVERY-DEPTH.md). Its bounded clock shift keeps the remaining total within the required central range, and it changes the real cutoff by only a fixed factor. The resulting normalized word mass is $\gg\Pr(S_q=2q)\gg1/\sqrt q$; each word contributes $J=(3/4)^q$. Irrational targets obey the very same finite cylinder statement.

At a fixed total, $2^A\beta_w$ is an integer and distinct words have distinct such numerators, by recovering the last exponent from its dyadic valuation after subtracting $3^{q-1}$ and then iterating. All numerators lie in the class $2^A s\bmod3^q$, so distinct offsets are separated by at least $J$. At every unit node select a fixed number $M_q\gg J^{-1}/\sqrt q$ of its available words with offsets separated by at least $(2B+2)J$, by keeping a fixed fraction of the sorted points. Repeat from each selected unit child. All continuation offsets lie in $[0,B/(1-J)]\subset[0,2B]$ for large $q$. The constructed nested sibling real intervals therefore have a gap at least $J$ in their parent's scale, contraction exactly $J$, and at least $M_q$ children independently of the node. The uniform child measure gives dimension at least $\log M_q/(-\log J)$, by the elementary mass distribution bound on these separated levels. Fix a common $B$ and let $q\to\infty$; the resulting sets are all in $[0,2B]$ and their dimensions approach one, proving the claim.
