# Integer agreement in the real and 3-adic numen forces a genuine cycle

Date: 2026-11-23. Written infinite theorem; no assertion that nontrivial cycles have been excluded.

## Main statement

Let $z\in\mathbb Z_2$ have infinitely many one-digits at positions
$d_1<d_2<\cdots$, and put

\[
S_k=\sum_{i=1}^k3^{i-1}2^{-(d_i+1)}.
\]

Suppose the 3-adic limit is a positive odd integer $q$:

\[
\lim_{k\to\infty}^{\mathbb Q_3}S_k=q\in\mathbb N,
\qquad q\text{ odd}.                                      \tag{1}
\]

Then the same series converges in the real numbers to a number
$B(z)$ with $0<B(z)\le q$. More precisely:

1. $B(z)=q$ if and only if the inverse itinerary specified by $z$ stays forever in the actual shortcut cycle containing $q$.
2. In that case $z$ is purely periodic as a binary 2-adic code. In particular it is rational.
3. If $q$ is not a periodic point, then the following uniform strict gap holds for **every** such code:

\[
\boxed{q-B(z)\ge q\exp(-200/3)>0.}                         \tag{2}
\]

If $q$ is periodic but the inverse path leaves the cycle after a finite prefix, the gap is again strictly positive, with the finite prefix product retained explicitly below. There is no uniform gap over all those exit times, because arbitrarily many initial laps can make the prefix product arbitrarily small.

This is a corrected two-place statement. It does not infer a forward divergent orbit from an irrational input. A nonperiodic positive integer may enter the known cycle, or could escape; (2) applies to either case. It also does not rule out an unknown positive cycle: such a cycle would satisfy the equality alternative.

The elementary finite-cylinder estimate used below comes from PR177 at `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`, Section 1. No canonical measure, predecessor-population, entropy, mixing, or stationarity assumption enters. The extension to arbitrary inverse rays and its consequence for simultaneous numen values are the deduction here; no claim of global historical priority is made.

## 1. Every tail is an actual positive odd integer

Set $A_i=d_i+1$, $A_0=0$, and $e_i=A_i-A_{i-1}\ge1$.
Writing (1) after the first $i$ one-digits gives

\[
q_i=\frac{2^{A_i}}{3^i}(q-S_i),\qquad q_0=q,
\]

and

\[
3q_i+1=2^{e_i}q_{i-1}.                                   \tag{3}
\]

The remaining infinite-one tail shows $q_i\in\mathbb Z_3^\times$:
after normalization its first term is a power of two in the denominator and every subsequent term is divisible by three. On the other hand, the rational expression for $q_i$ has denominator dividing $3^i$. A rational number of this form in $\mathbb Z_3$ is an ordinary integer. Thus all $q_i$ are ordinary integers.

Starting from $q_0\ge1$, equation (3) shows $q_i>0$; as an integer it is at least one. Its numerator $2^{e_i}q_{i-1}-1$ is odd, so $q_i$ is odd. Unit status has already excluded divisibility by three. Since $q_{i-1}$ is odd, (3) also gives the **exact** valuation

\[
v_2(3q_i+1)=e_i,\qquad U(q_i)=q_{i-1}.
\]

No approximate congruence or independent residue representative replaces this ordinary inverse path.

## 2. A summable bound on any simple inverse path

Let $q_0,q_1,\ldots$ be an inverse path of distinct positive odd integers with $U(q_i)=q_{i-1}$. We claim

\[
\boxed{\#\{i\ge0:q_i\le X\}\le5X^{39/40}\quad(X\ge1),}
\qquad
\boxed{\sum_{i\ge0}q_i^{-1}\le200.}                       \tag{4}
\]

For clarity, the form of the finite-cylinder input needed here is this: for
$r=\lfloor(3/5)\log_2X\rfloor$, a collection of actual starting states at most $X$ on which $U^r$ is injective has cardinality at most $4X^{39/40}$. The cited proof uses one exact residue modulo $2^{A+1}$ for each length-$r$ gap word of total $A$, splits at $\lfloor5r/3\rfloor$, and counts the distinct ordinary endpoints in the high-total part. It does not require the starting collection to be a complete forward orbit.

Delete the first $r$ vertices of our inverse path. On the remaining vertices, $U^r(q_i)=q_{i-r}$ is injective, by distinctness. Hence

\[
\#\{i:q_i\le X\}\le r+4X^{39/40}.
\]

If $r=0$ this proves the desired estimate immediately. Otherwise
$r\le2^r\le X^{3/5}\le X^{39/40}$, proving the first inequality in (4).
The same argument covers a finite distinct inverse segment: if it has at most $r$ vertices, all of them lie among the deleted vertices.

By the elementary counting-integral identity and Tonelli,

\[
\sum_i\frac1{q_i}
=\int_1^\infty\#\{i:q_i\le t\}\frac{dt}{t^2}
\le5\int_1^\infty t^{-41/40}\,dt=200.
\]

This counts separated visits across high excursions as well: no contiguous-height-window assumption has been used.

## 3. The exact real remainder

Define

\[
\lambda(x)=\frac{3x}{3x+1}.
\]

Equation (3) telescopes, for every $k$, to

\[
\boxed{q-S_k=\frac{3^kq_k}{2^{A_k}}
=q\prod_{i=1}^k\lambda(q_i).}                            \tag{5}
\]

All factors lie in $(0,1)$, so $S_k$ is increasing and bounded above by $q$. The real limit $B(z)$ therefore exists without an extra convergence hypothesis.

On a simple inverse path, (4) and $\log(1+t)\le t$ give

\[
\prod_{i=1}^k\lambda(q_i)
=\exp\left(-\sum_{i=1}^k\log(1+(3q_i)^{-1})\right)
\ge\exp(-200/3).
\]

Pass to the limit in (5). This proves the uniform real remainder bound (2) whenever the path is simple.

## 4. Repetition, cycle exits, and equality

If an inverse path repeats a state, say $q_j=q_k$ with $j<k$, then
$U^{k-j}(q_k)=q_j=q_k$, so that state is periodic. Applying $U^j$ shows that $q_0$ is on the same cycle. Thus an inverse path rooted at a nonperiodic $q$ is automatically simple, proving (2) in the stated form.

Suppose instead that $q$ lies on a cycle. At each cycle vertex exactly one odd predecessor is in that same cycle. Following those predecessors forever makes $q_i$ periodic and bounded. The product in (5) then tends to zero, since each lap multiplies it by a fixed number strictly between zero and one. Therefore $B(z)=q$.

If the inverse path leaves the cycle at $q_J$, with $J\ge1$, it can never subsequently reenter a cycle. Any cycle encountered farther backward would have a forward iterate equal to $q$, and would therefore have to be the original cycle, forcing $q_J$ into it as well. Its tail is consequently simple. Applying (4) to that tail gives, for the original root,

\[
q-B(z)\ge
q\left(\prod_{i=1}^{J-1}\lambda(q_i)\right)
\exp(-200/3)>0.                                         \tag{6}
\]

We have included $q_J$ and its successors in the simple-tail sum, so the prefix in (6) stops at $J-1$. This retains every earlier cycle lap exactly.

Hence equality holds precisely for the inverse path that never leaves the cycle. Its odd gaps repeat, so the chronological inverse binary code repeats a finite block from its first digit. This proves pure periodicity and rationality, completing the theorem.

## 5. What the result does and does not supply

A positive ordinary integer in the numen's 3-adic image need not be periodic; `NUMEN_INVERSE_FIBER.md` constructs many such inputs even for known terminating sources. By contrast, simultaneous agreement of the real and 3-adic sums at the same positive odd integer forces an actual periodic itinerary. The proof makes the real tail quantitatively visible instead of assigning a value from one completion to the other.

For a periodic word, the common value is the usual full-denominator rational fixed point. The unresolved step is still to exclude integer values for every nontrivial positive primitive word. Neither the strict real gap for nonperiodic roots nor the full residual polynomial denominator bound establishes that exclusion. The equality alternative must not be removed by assuming that an arbitrary ordinary root is nonperiodic.

No new quantitative Tauberian contraction follows merely from (2): the root itself must first be known nonperiodic, and the periodic branch supplies exactly the zero real remainder which the theorem allows. The uniform gap is therefore a valid classification tool, not an unconditional no-cycle estimate.
