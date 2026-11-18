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
