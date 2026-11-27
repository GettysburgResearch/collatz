# An exact rational finite-sum proposal for the full ordinary problem

**Status: a fully explicit sufficient assertion and a compiled conditional
consumer. The assertion is open; this is not a proof of Collatz.**

Let `U` be the actual accelerated map on positive odd integers and
`e(x)=v₂(3x+1)`. Assign the positive rational coefficient

\[
 c_e=\frac{134}{25}\left(\frac5{14}\right)^e,
 \qquad
 W_k(x)=\prod_{i=0}^{k-1}c_{e(U^i x)}.
\]

The empty product is one. For natural `K,H,y`, define the completely finite,
computable rational number

\[
 R_{K,H}(y)=\sum_{k=0}^{K}
    \sum_{\substack{1\le x\le H\\x\text{ odd}\\U^kx=y}}W_k(x).
                                                               \tag{1}
\]

Every term follows the true orbit of an ordinary integer. Repeated visits,
including the known fixed odd state 1, are counted separately. There are no
chosen inverse probabilities or assumed stopping times in this definition.

The proposed assertion is

\[
 \boxed{\exists C\in\mathbb Q\ \forall K,H\in\mathbb N\ \forall y>0
   \text{ odd},\qquad R_{K,H}(y)^2\le C y^3.}                    \tag{2}
\]

`FiniteGreenBound` in [RationalGreen.lean](RationalGreen.lean) is exactly (2).
Its final theorem `finite_green_bound_implies_collatz` concludes that every
positive natural number reaches 1 under the usual full map, whose odd step is
`3*n+1` and whose even step is `n/2`. It does **not** provide a witness for (2).

## Why this particular rational weight

For a gap word of length `k` and total clock `S`, the product is
`(134/25)^k*(5/14)^S`. Give its legal ternary ball its usual Haar mass `3^-k`.
The sum over all words at depth `k`, integrated over ternary Haar measure, is
exactly `(134/135)^k`, because

\[
 \frac{1}{3}\sum_{e\ge1}c_e
 =\frac{134}{25}\frac{5/14}{3(1-5/14)}=\frac{134}{135}.
\]

Thus the associated positive infinite ternary Green series has Haar integral
**135**. Its restriction to positive odd integers is the increasing limit of
(1) as both cutoffs tend to infinity. The identification uses the elementary
fact that every legal inverse word at a positive odd integer reconstructs a
positive odd source and all its actual intermediate gaps; conversely every
such ordinary path supplies its legal word. The Haar argument is a written
calculation. The two exact rational identities behind it are checked in Lean;
the infinite integral is not formalized here.

The arithmetic margin is also exact:

\[
 c_e^2 2^{3e}
 =\left(\frac{134}{25}\right)^2\left(\frac{50}{49}\right)^e
 \ge27\left(\frac{25}{24}\right)^2\qquad(e\ge1).
\]

If `2^e*y=3*x+1` and `x>=13`, it follows that

\[
 \frac{201}{200}\,y^3\le c_e^2x^3.                            \tag{3}
\]

At the worst permitted endpoint `x=13`, the sharper squared growth factor is
`9862333/9800000`, greater than `201/200`. The known cycle at 1 has coefficient
`c₂=67/98<1`; it is not accidentally excluded by the construction.

## The complete conditional descent argument

Fix an actual positive odd source `a`. Its first `k` steps supply a term in
`R_{k,a}(U^k a)`. Positivity and (2) bound

\[
 v_k=\frac{W_k(a)^2}{(U^ka)^3}\le C.
\]

If every state were at least 13, (3) would give
`v_(k+1)>=(201/200)*v_k` for all `k`, while `v₀=1/a³>0`. This contradicts the
upper bound. Thus the orbit reaches an odd state below 13. Lean verifies the
actual full-map trajectories from 1, 3, 5, 7, 9 and 11 to 1, and the exact
halving transport from every positive natural number to its odd part.

[PotentialAssembly.lean](PotentialAssembly.lean) separately records the
generic positive bounded potential argument and its transport to the full
Collatz statement. [RationalGreen.lean](RationalGreen.lean) then proves the
coefficient inequalities, defines the actual finite sums, includes each
specified path as one of their nonnegative terms, and completes the preceding
argument. Neither theorem imports an axiom named Collatz or introduces an
unproved theorem as a Lean axiom. The unresolved mathematical requirement is
the explicit premise (2).

## The strength of the proposed bound

The small Haar integral does not imply (2): positive ordinary integers form a
countable Haar-null set. The [fixed time-tilt analysis](../global/TILTED_GREEN.md)
also exhibits a dense collection of nonintegral dyadic centers at which the
infinite Green series is infinite. A local upper envelope on real/ternary
neighborhoods cannot establish the desired ordinary restriction.

There is a second substantive qualification. Put

\[
 p=\log_2(14/5),\qquad t_*=(134/25)/3^p>1.
\]

Then `c_e=t_*(3/2^e)^p`, exactly. On a terminating source `x`, keep its first
hit of 1 at odd time `k`. The simple-path reciprocal floor, when invoked with
the cited uniform packing input, gives `f_k(x)>=c>0`, and hence

\[
 G(1)\ge t_*^k(c/x)^p.
\]

Finiteness of this single value already forces

\[
 k\le\frac{p}{\log t_*}\log x+O(1),
 \qquad \frac{p}{\log t_*}\simeq31.56735.
\]

This is a uniform logarithmic **odd-step** first-hitting bound over all
terminating sources, an additional unresolved quantitative statement. The
finite gate (2) is therefore presented as a sufficient proposal, without
claiming equivalence to Collatz. Weaver's [Paper 222 §7.9](https://rstation.ai/problems/collatz/papers/222)
records the corresponding distinction for another exponential tail law;
[Paper 127](https://rstation.ai/problems/collatz/papers/127) supplies large fixed
shortcut-time ratios, not a family refuting every logarithmic constant.
The new prefix-dependent adaptive construction is being pursued specifically
to avoid imposing this extra fixed time tilt.

The formal result is useful only with its premise visible. Proving that
premise, or proving the ordinary bound for the adaptive replacement, remains
the main task.
