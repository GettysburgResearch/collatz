# T-6601 — finite coefficient thresholds for infinite-stopping starts

**Claim ID:** `T-6601`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** elementary shortcut-Collatz affine algebra only  
**Scope:** positive ordinary integers with infinite ordinary stopping time  

## Definitions

Use the shortcut map

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

For a binary parity word

\[
w=(v_0,\ldots,v_{k-1})\in\{0,1\}^k,
\qquad q(w)=\sum_{i=0}^{k-1}v_i,
\]

put

\[
A_w=\sum_{i=0}^{k-1}
 v_i\,3^{q(w)-q_{i+1}(w)}2^i,
\qquad
q_{i+1}(w)=\sum_{r=0}^{i}v_r.
\]

Every integer following `w` for `k` shortcut steps satisfies

\[
\boxed{
T^k(x)=\frac{3^{q(w)}x+A_w}{2^k}
      =C_wx+E_w,}
\]

where

\[
C_w=\frac{3^{q(w)}}{2^k},
\qquad
E_w=\frac{A_w}{2^k}\ge0.
\]

If `C_w<1`, define its no-descent height

\[
\Theta(w)=\frac{E_w}{1-C_w}
         =\frac{A_w}{2^k-3^{q(w)}}.
\]

For `L>=1`, define the exact finite threshold

\[
\boxed{
H_L=
\max_{1\le k\le L}
\max_{\substack{w\in\{0,1\}^k\\ C_w<1}}
\Theta(w).}
\tag{1}
\]

The set in `(1)` is finite and nonempty.

For a positive integer `x`, let

\[
t(x)=\min\{k\ge1:T^k(x)<x\},
\]

and

\[
\tau(x)=\min\{k\ge1:3^{q_k(x)}/2^k<1\},
\]

with either value equal to `infinity` when no such `k` exists.

## Theorem

If

\[
t(x)=\infty
\qquad\text{and}\qquad
x>H_L,
\]

then

\[
\boxed{\tau(x)>L.}
\tag{2}
\]

Equivalently, every prefix through length `L` is coefficient-supercritical:

\[
3^{q_k(x)}\ge2^k
\qquad(1\le k\le L).
\]

## Proof

Suppose instead that `tau(x)<=L`, and put `k=tau(x)`. Let `w` be the actual length-`k` parity prefix of `x`. Then `C_w<1`.

Since `t(x)=infinity`, its endpoint does not descend:

\[
T^k(x)\ge x.
\]

Using the affine formula,

\[
C_wx+E_w\ge x,
\]

hence

\[
x\le\frac{E_w}{1-C_w}=\Theta(w)\le H_L.
\]

This contradicts `x>H_L`, proving `(2)`. ∎

## Exact meaning

`H_L` is not an empirical frontier. It is the largest rational fixed-point height among **all** subcritical shortcut parity words of length at most `L`.

Consequently, an ordinary start with infinite stopping time can have a short coefficient crossing only while it lies below one explicit finite height.

## Source-qualified quantitative corollary

Rozier--Terracol record Ellison's lower bound, in the subcritical case and at sufficiently large exponents,

\[
2^k-3^q>2^k e^{-k/10}.
\]

At a first coefficient crossing, every preceding coefficient is at least one. Each odd additive contribution to the final remainder is therefore less than `1/2`, so

\[
E_w<q/2<k/2.
\]

Thus an infinite-stopping start `x` with a sufficiently large finite first crossing `k` satisfies

\[
x<\frac{k}{2}e^{k/10}.
\]

Equivalently,

\[
\boxed{k>10W(x/5),}
\]

where `W` is the Lambert function. This source-qualified estimate is much weaker than the current Farey gate for starts above the verified range, but it makes the escape `tau(x)->infinity` quantitative without a finite search.

## Gap audit

- The theorem does not prove that any fixed `x` has finite coefficient stopping time.
- The thresholds `H_L` may grow without bound; proving they eventually dominate every ordinary infinite-stopping root is exactly the missing global theorem.
- A compatible infinite parity word is not promoted to an ordinary integer.
- The Lambert-W corollary depends on the exact Ellison normalization quoted by Rozier--Terracol; the elementary theorem does not.
