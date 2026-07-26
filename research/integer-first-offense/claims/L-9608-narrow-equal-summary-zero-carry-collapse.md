# L-9608 — Narrow equal-summary alphabets have zero cycle carry

**Claim ID:** `L-9608`
**Status:** `PROPOSED`
**Agent:** `gpt56-pro-04`
**Issue:** #46
**Date:** 2026-07-26
**Dependencies:** elementary affine-block composition
**Related claims:** `L-9607`
**Scope:** finite alphabets of contracting affine blocks with one common multiplier and divisor

## 1. Statement

Fix integers

\[
0<P<Q
\]

and a finite nonempty set of integer constants

\[
\mathcal C=\{C_1,\ldots,C_s\}.
\]

For every `i`, let the corresponding affine block be

\[
Qx'=Px+C_i.
\tag{1}
\]

Put

\[
C_- = \min_i C_i,
\qquad
C_+ = \max_i C_i,
\qquad
W=C_+-C_-.
\tag{2}
\]

Assume the alphabet is **narrow**:

\[
\boxed{W<Q.}
\tag{3}
\]

Suppose a finite word

\[
i_0i_1\cdots i_{R-1}
\]

has an integral cycle at its block boundaries:

\[
Qx_{t+1}=Px_t+C_{i_t}
\qquad(0\le t<R),
\]

with

\[
x_R=x_0=n\in\mathbf Z.
\tag{4}
\]

Then

\[
\boxed{x_t=n\quad(0\le t\le R)}
\tag{5}
\]

and

\[
\boxed{C_{i_t}=(Q-P)n\quad(0\le t<R).}
\tag{6}
\]

Consequently:

1. every selected block constant is the same;
2. if the constants in `C` are distinct, the block word is constant;
3. if no `C_i` is divisible by `Q-P`, no integral cycle exists at all;
4. if exactly one constant is divisible by `Q-P`, every integral cycle is the fixed point of that one block.

This conclusion holds for **all repetition lengths** and every ordering of the block alphabet.

## 2. Proof

Iterating `(1)` around the proposed cycle gives

\[
Q^Rn=P^Rn+
\sum_{t=0}^{R-1}
P^{R-1-t}Q^tC_{i_t}.
\tag{7}
\]

Since

\[
Q^R-P^R
=(Q-P)
\sum_{t=0}^{R-1}P^{R-1-t}Q^t,
\tag{8}
\]

we obtain

\[
(Q-P)n
=
\frac{
\sum_{t=0}^{R-1}P^{R-1-t}Q^tC_{i_t}
}{
\sum_{t=0}^{R-1}P^{R-1-t}Q^t
}.
\tag{9}
\]

The right side is a convex combination of the selected constants. Hence

\[
C_-\le (Q-P)n\le C_+.
\tag{10}
\]

Now inspect the first edge. From `(1)` and `x_0=n`,

\[
Q(x_1-n)=C_{i_0}-(Q-P)n.
\tag{11}
\]

The right side is divisible by `Q`. By `(10)`, its absolute value is at most

\[
C_+-C_-=W<Q.
\]

The only multiple of `Q` in that interval is zero. Therefore

\[
x_1=n,
\qquad
C_{i_0}=(Q-P)n.
\tag{12}
\]

Apply the same argument to the next edge. Since `x_1=n`, equation `(11)` repeats with `i_1`, forcing

\[
x_2=n,
\qquad
C_{i_1}=(Q-P)n.
\]

Induction proves `(5)` and `(6)`. The four consequences are immediate. ∎

## 3. Interpretation

The theorem says that a contracting equal-summary grammar cannot transport a nonzero integer carry around a cycle when its complete constant alphabet fits inside one divisor-width interval.

The full denominator is not attacked factor by factor. Instead, integrality of the first returned edge forces a multiple of `Q` whose Archimedean size is strictly below `Q`; it must vanish. Every later edge then vanishes in the same way.

Thus the entire arbitrary repetition axis collapses to the primitive one-block fixed points.

## 4. Relationship to `L-9607`

`L-9607` treats two equal-summary constants through the geometric factor

\[
G_R={Q^R-P^R\over Q-P}
\]

and obtains an all-or-none conclusion under a coprimality hypothesis.

`L-9608` is complementary:

- it permits an arbitrary finite alphabet, not only two constants;
- it requires no factorization or coprimality with `G_R`;
- it uses the Archimedean width hypothesis `W<Q`;
- it proves the stronger statewise conclusion that every block-boundary carry is zero.

Neither theorem contains the other in full.

## 5. Gap audit

- The strict inequality `W<Q` is load-bearing. At width at least `Q`, nonzero multiples of `Q` can occur in `(11)`.
- The theorem is for common `P,Q`; scale-varying summaries are outside scope.
- It excludes cycles, not aperiodic divergent paths.
- Intermediate physical legality is unnecessary for the negative conclusion: no coarse integral affine cycle exists, so no exact physical subcycle exists.
- No Collatz conjecture conclusion is asserted outside a separately identified block alphabet.

## 6. Adversarial checks

1. The weights in `(9)` are strictly positive because `P,Q>0`.
2. The average in `(9)` uses the complete denominator identity, not a selected proper factor.
3. The proof does not assume the cycle states are ordered or monotone.
4. Duplicate constants are harmless: the theorem forces one affine map, though multiple labels may name it.
5. If `W=Q`, the argument no longer excludes `C_i-(Q-P)n=\pm Q`; strictness cannot be weakened for free.

## 7. Suggested use

For any fixed-weight pulse or repair alphabet:

1. compute its common `(P,Q)`;
2. determine the exact minimum and maximum affine constants;
3. test `C_+-C_-<Q` symbolically;
4. reduce every all-repetition cycle question to the primitive block fixed points.
