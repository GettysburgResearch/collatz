# A dyadic companion for the biased parity series

**PROPOSED written theorem.** For the ordinary shortcut map, rationality of a single dyadic scalar is equivalent to eventual periodicity. Membership of this scalar in $\mathbb Z[1/3]$ is equivalent to hitting 1. The latter implication uses a finite integral companion check. The scalar exists at every binary argument without any convergence hypothesis. Its universal membership in $\mathbb Z[1/3]$ remains open.

Use $T(x)=x/2$ on even inputs and $T(x)=(3x+1)/2$ on odd inputs, on $\mathbb Z_2$. Let $e_i=T^i(x)\bmod2$, $p_i=\sum_{j<i}e_j$, and $A_i=2^{i+p_i}/3^i$. Define
\[
 D(x)=\sum_{i\ge0}e_iA_i\in\mathbb Z_2,\qquad
 B_k(x)=\sum_{i<k}e_iA_i\in\mathbb Q.
\]
Every term at clock $i\ge k$ is divisible by $2^k$ in $\mathbb Z_2$, uniformly in the input. The finite prefix is locally constant, so this defines a continuous function. The finite sums can also be evaluated over the reals. The identity $3(A_{i+1}-A_i)=-A_i+2e_iA_i$ gives $2D(x)=\sum_{i\ge0}A_i-3$ over $\mathbb Q_2$. The weights use the physical clock, including even steps.

## Rational values force eventual periodicity

The finite splitting identity gives
\[
 D(x)=B_k(x)+A_k(x)D(T^kx).
\]
In particular $D(2x)=\frac23D(x)$, and at an odd input $D(x)=1+\frac43D(Tx)$. An even input therefore has an even companion, and an odd input has companion equal to 1 modulo four. Given an actual companion $d=D(x)$, its future and all future physical parities are determined by
\[
 d'=\frac{3d}{2}\quad(d\text{ even}),\qquad
 d'=\frac{3(d-1)}4\quad(d\equiv1\bmod4).
\]
The residue $3\bmod4$ cannot occur.

Suppose $n>0$ is ordinary and not eventually periodic. Its forward states $x_i=T^i n$ are distinct and tend to infinity. This orbit does not hit 1. The high-prefix theorem at the pinned source below gives $A_k^5\ge (256/243)^k/n^3$. Thus $A_k\to\infty$, and the finite identity $2B_k=3A_k-3+\sum_{i<k} A_i$ gives $B_k\to\infty$ over the reals.

If $d_0=D(n)$ is rational, the branch recurrences make all $d_i=D(x_i)$ rational with reduced denominators dividing the initial odd denominator. Indeed the $d_i$ lie in $\mathbb Z_2$, and the equations divide only by powers of two. The equality $d_i=(d_0-B_i)/A_i$ holds in $\mathbb Q$ at every clock. It follows that $d_i<0$ eventually. Write $w_i=-d_i/3>0$ on this tail. The $w_i$ have bounded denominators and satisfy
\[
 w_{i+1}=\frac{3w_i}{2}\quad(x_i\text{ even}),\qquad
 w_{i+1}=\frac{3w_i+1}{4}\quad(x_i\text{ odd}).
\]

The $w_i$ cannot repeat. Equal companions give the same complete parity sequence by the deterministic recurrence. Sources sharing $k$ parity bits differ by a multiple of $2^k$. Indeed subtract their affine endpoint formulas $2^k T^k x=3^{p_k}x+C$, with identical $p_k,C$. Equality at all depths gives equality of the two ordinary sources, contrary to distinctness. A sequence of distinct positive rationals with bounded denominators tends to infinity. In particular eventually $x_i\ge20$ and $w_i\ge64$.

The even-step factor of $x_i^2w_i^3$ is $27/32$. Its odd-step factor satisfies
\[
 \frac{(3+1/x_i)^2(3+1/w_i)^3}{256}
 \le \frac{61^2\,193^3}{20^2\,64^3\,256}
 =\frac{26750481097}{26843545600}<1.
\]
Both branches contract by a common strict factor at every sufficiently late clock. Their product tends to zero while $x_i,w_i\to\infty$, a contradiction. This proves rationality implies eventual periodicity. Conversely an eventually periodic physical orbit gives a finite preperiod and a geometric period in the dyadic series. The period multiplier $2^{L+p}/3^L$ is strictly 2-adically contracting for $L>0$, so the geometric sum is rational.

## Triadic values force the standard cycle

When $d_0\in\mathbb Z[1/3]$, every step consumes at least one remaining denominator factor of three, and division by two or four is legal in $\mathbb Z_2$. Once the denominator is one, each next result is an integer divisible by three. Suppose $n$ never hits one. All its positive physical states stay at least 20 by checked finite convergence below 20, and $B_k\to\infty$ as above. Some tail carries positive integers $w_i=-d_i/3$. Applying the strict product decrease on that tail forces some $w_i<64$, since positive integer heights have a minimum. At a legal step, even physical parity requires $w_i$ even, and odd physical parity requires $w_i=1\bmod4$. The recurrences then determine the next $w_i$. For $2\le w_i<64$ the exact calculation in the Lean module reaches the forbidden residue $3\bmod4$ within 17 steps. At $w_i=1$ every remaining physical input would be odd: the companion stays at one and the even formula is not integral. An all-odd path from positive ordinary $x$ is impossible since $2^k(T^k x+1)=3^k(x+1)$ would imply $2^k\mid x+1$ for every $k$.

Conversely $D(1)=9$ by the two-step multiplier $8/9$. Finite backward substitution propagates membership in $\mathbb Z[1/3]$ to every positive start that hits one. For general rational $D(n)$ the residual denominator can put the small $w_i$ on a strictly finer grid, beyond the integral computation. The conclusion in that case is eventual periodicity.

## A finite linear representation in binary digits fails

One route to universal rationality would be a finite-dimensional binary digit representation over $\mathbb Q$ with rational initial data. Such a representation would give finite-dimensional span over $\mathbb Q_2$ of the sequences $n\mapsto D(2^j n+r)$, $0\le r<2^j$, by multiplying the fixed digit matrices. In fact that span is infinite-dimensional.

If $x\equiv z\bmod2^j$, their first $j$ branches agree. Finite splitting gives
\[
 D(x)-D(z)\in2^{j+p_j(z)}\mathbb Z_2.
\]
At any positive ordinary $z$, $p_j(z)\to\infty$ since eventual all-even input would force a positive integer to be divisible by every power of two. Thus all dyadic difference quotients of $D$ tend to zero at each such $z$. At zero $D(0)=0$. For all $p,j\ge0$,
\[
 \frac{D(2^j3^p)-D(0)}{2^j}=3^{-j}D(3^p).
\]
The right side has binary norm one because $3^p$ is odd.

The functions $1$ and $x\mapsto D(3^p x-1)$, $p\ge0$, are linearly independent over $\mathbb Q_2$ on $\mathbb Z_2$. In a putative finite relation choose the least $p$ with a nonzero coefficient of the indicated function. Take the difference between $x=3^{-p}+2^j$ and $3^{-p}$, divided by $2^j$. The $p$ term has fixed nonzero norm. Each higher $q$ gives a difference quotient at the positive ordinary $3^{q-p}-1$ with a fixed unit increment factor $3^q$, and tends to zero. The ultrametric triangle inequality contradicts the relation. The constant alone is independent.

The all-odd section has the exact form
\[
 D(2^p(n+1)-1)=\sum_{i<p}(4/3)^i+(4/3)^pD(3^p(n+1)-1).
\]
Translating the variable by one gives the same independence on the dense set of nonnegative ordinary inputs by continuity. Even the all-ones sections, with constants adjoined, have infinite rank. This excludes the stated linear scheme. It does not classify the arithmetic of $D(n)$ at any given positive ordinary input.

## Scope and pins

The base is GettysburgResearch/collatz, PR182, commit `a30402b7849c437edf245974d9f436d1f105e08e`. The high physical prefix estimate comes from `research/high-variance-closure-20261124/continuation/lean/BiasedParity.lean`, theorem `geometricTerm`. The finite floor is `QuarterShift.below_twenty` in `research/high-variance-closure-20261124/lean/QuarterShift.lean`. The older real scalar in `research/scalar-rigidity-round9-20261123/ACTUAL_SCALAR_LAW.md`, Section 1, is the accelerated gap sum $\sum_j v_2(3q_j+1)/3^{j+1}$. Its triadic criterion was already proved. The present dyadic scalar uses a different series and a different partial map. The bivariate height classifies all its rational values.

The `DyadicCompanion.lean` core treats the ordinary integer equations with denominators cleared. The dyadic series, rationality equivalence, and infinite linear rank are written proofs. Proving $D(n)\in\mathbb Z[1/3]$ for every positive ordinary $n$ would settle the physical convergence problem. That arithmetic construction remains missing.
