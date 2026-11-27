# Infinite-horizon agreement for first exit from the starting band

**PROPOSED, SOURCE-QUALIFIED mathematical synthesis.** [FirstExit.lean](FirstExit.lean) verifies the finite ordinary-orbit implication. We inspected the statements and normalization of both external estimates. We did not reprove the Subspace Theorem or rebuild the separate irrationality-exponent development. Collatz remains open.

## Statement

Use the shortcut map, with one division by two on both branches. Start at a positive integer $X$, write $x_i=T^i(X)$, count the odd departures in the first $i$ steps by $u_i$, and put $g_i=3^{u_i}/2^i$. For all sufficiently large $X$, the first exit of $x_i$ from $[X,9X/2]$ and the first exit of $g_i$ from $[1,9/2]$ both exist, have the same date and have the same direction. Their common date is $O(X^{8/25})$. The height threshold is ineffective.

Weaver 223/v1 proves agreement through 217,976,794,617 steps for **every** integer $X\ge2$, with a separate computation below $2^{100}$. The conclusion here allows unbounded dates on one cofinite set of starting integers. The position of its ineffective height threshold relative to $2^{100}$ remains unknown. [Weaver 223/v1, §§5 and 7](https://rstation.ai/problems/collatz/papers/223/v1)

## Two imported estimates

1. Lyapunov Weaver, *Descent or positive occupation above the initial height in Collatz trajectories*, 181/v1 §4, equations (9)–(10), counts actual starting integers anywhere in $[X,KX]$ whose next $N$ shortcut steps remain there. At $K=9/2$, with $\gamma=\log_2 3$, and for any fixed $\epsilon>0$, their count $B$ is $O_\epsilon(X^{\theta+\epsilon})$ at a length $N=O_\epsilon(\log X)$, where
   $$\theta=\frac{(1+\gamma)(1-1/\gamma)}3=\frac{\gamma-\gamma^{-1}}3.$$
   This located count uses the fixed-place integral Subspace Theorem. The simplification after (10) explicitly includes the endpoint $K=9/2$. [Versioned primary source](https://rstation.ai/problems/collatz/papers/181/v1)
2. Gregory V. Chudnovsky, *Irrationality exponents of logarithmic numbers*, arXiv:2610.28079v1, Theorem 11.1, states $\mu(\log 2/\log 3)\le3$ for this pair of multiplicatively independent positive rationals. Consequently, for each $\kappa>2$ there exists $c_\kappa>0$ such that for every integer $q\ge1$ and every integer $p$,
   $$|p\log 3-q\log 2|\ge c_\kappa q^{-\kappa}.$$
   Apply the irrationality estimate with exponent $1+\kappa>3$. Reducing a fraction preserves the weaker lower bound at its original denominator. Irrationality absorbs the finitely many initial exceptional reduced approximations into the constant. The source reports formal verification of its rational-logarithm endpoint. [Versioned primary source, §11](https://arxiv.org/html/2610.28079v1#S11)

The confined-count argument and an unshifted order comparison already occur in Weaver 181, Theorem 3, in its smaller published-input range. PR200 at eb91086951b66923787f696801f0c3ca52a0077d discusses wider confinement and occupation with the newer irrationality input. The synthesis here compares **both boundaries through the actual exit, including the exit observation**.

## Proof

The finite identity on any physical arc from its starting integer $X$ is
$$
\log(x_i/X)=u_i\log 3-i\log 2+E_i,\qquad
E_i=\sum_{\substack{j<i\\ x_j\ {\rm odd}}}\log(1+1/(3x_j)).
$$
If every departure before $i$ is at least $X$, then $0\le E_i\le i/(3X)$. The endpoint $x_i$ may already have left. An arc starting later uses its own odd count, endpoint ratio and departure floor.

Since $3^{17}<2^{27}$, we have $\gamma<27/17$ and $\theta<440/1377<8/25$. Choose $\epsilon$ small enough and put $U=B+N=O(X^{8/25})$, using the actual cardinality $B$ in estimate 1. Take $\kappa=41/20$ in estimate 2. Because $(8/25)(1+41/20)=122/125<1$,
$$
U/(3X)<c_\kappa U^{-41/20}
$$
for every sufficiently large $X$.

If all observations through $U$ lie in the band, the $B+1$ starts at dates $0,\ldots,B$ each have $N$ more steps in the band. Two coincide. On the resulting nonempty return of length $t\le B$, the homogeneous log gain has magnitude at most $t/(3X)$ by the physical identity. Estimate 2 gives at least $c_\kappa U^{-41/20}$, a contradiction. Thus a first physical exit $j\le U$ exists.

At each $1\le i\le j$, the perturbation $E_i$ is smaller than the distance from the homogeneous log gain to zero. For the upper boundary,
$$
|\log g_i-\log(9/2)|=|(u_i-2)\log 3-(i-1)\log 2|.
$$
For $i\ge2$ estimate 2 applies with $q=i-1$. At $i=1$ the two possible coefficients, $1/2$ and $3/2$, are at log distance at least $\log 3$ from $9/2$. Reducing $c_\kappa$ handles this date. Adding $E_i$ preserves both strict side comparisons throughout the common first exit.

### A growing family of simultaneous comparisons

The identical count bounds the residence of a segment starting **anywhere** in $[X,9X/2]$. Include the first exterior endpoint if all preceding departures were in the band. Consider any oriented positive-length subarc, of length $t$ and odd count $u$, and any ratio $R=3^b/2^a$ with integer exponents $|a|,|b|\le X^{1/3}$. Uniformly at sufficiently large $X$, unless $(t,u)=(a,b)$, the physical endpoint ratio lies on the same side of $R$ as $3^u/2^t$.

Indeed $t=O(X^{8/25})$. With $\kappa=201/100$, when $t\ne a$ the log distance is at least $c_\kappa |t-a|^{-\kappa}\gg X^{-67/100}$. Negate both integer coefficients if $t-a<0$. When $t=a$ the distance is at least $\log 3$ by $u\ne b$. The physical correction is $O(X^{-17/25})=O(X^{-0.68})$, smaller in either case. At exact resonance the physical ratio equals the coefficient if $u=0$ and strictly exceeds it otherwise.

## Remaining ordinary obstruction

At a sufficiently large cycle minimum $X$, the common first exit must be upward. Some literal proper prefix therefore has $g_j>9/2$, with every preceding positive prefix coefficient in $(1,9/2)$. A return to $X$ before this exit contradicts the same lower-boundary comparison. Escaping paths can also take upward exits. The complete lap still needs $(2^L-3^s)X=C_w$. The comparison does not decide returns from above $9X/2$.

Residual agreement is decidable start by start. Simulate in the finite band until an exit or a repeated state, monitoring the coefficient comparisons. After a repeat the physical trajectory stays inside forever. Its complete lap coefficient is strictly below one by the positive cycle product, so the observed coefficient eventually exits below if it has not already exited above. Thus the set of exceptions is decidable and finite under the two inputs. The proof supplies no numerical cutoff for exhausting it.

## Formal scope

The declaration ordinary_first_exit uses the literal natural-number shortcut step, its recursive trace and its observed parity counts. Its hypotheses are a finite set of confined starts, its cardinality bound and two uniform finite logarithmic separations. Its conclusion identifies the first physical and homogeneous log exits and their directions. The declarations physical_log and error_bounds prove the telescoping formula and the floor-dependent bound. An explicit finite pigeonhole argument proves existence. The asymptotic inputs, the limiting choice of $X$, conversion from log levels to ratios, and the growing simultaneous-comparison corollary have written proofs.
