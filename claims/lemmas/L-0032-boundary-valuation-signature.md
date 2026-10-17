# L-0032 — Exact 2-adic/3-adic valuation signature of every scaled boundary

Claim ID: `L-0032`  
Title: The current tower type is the binary valuation of the scaled tail and the previous type is its ternary valuation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0031`  
Scope: every positive ordinary boundary in the stabilized phase-34 tower system  
Related counterexample candidates: none

## Type table

Use the scaled-tail constants of `L-0031`:

| type `i` | `p_i` | `b_i` | `alpha_i=v_2(p_i)` | `beta_i=v_3(b_i)` |
|---:|---:|---:|---:|---:|
| 0 | 5  | 9  | 0 | 2 |
| 1 | 30 | 54 | 1 | 3 |
| 2 | 20 | 36 | 2 | 2 |
| 3 | 56 | 24 | 3 | 1 |

At one boundary,

\[
W_n=p_{i_n}+64h_n,
\tag{1}
\]

and one local step is

\[
2^{11(t_{n+1}+1)}W_{n+1}
=
3^{7(t_n+1)}W_n+b_{i_n}.
\tag{2}
\]

## Statement

### 1. Current binary signature

\[
\boxed{
v_2(W_n)=\alpha_{i_n}.}
\tag{3}
\]

Thus the current tower type is recovered from the exact binary valuation:

\[
\boxed{
i_n=\alpha^{-1}(v_2(W_n)).}
\tag{4}
\]

### 2. Outgoing ternary signature

\[
\boxed{
v_3(W_{n+1})=\beta_{i_n}.}
\tag{5}
\]

Thus the preceding tower type is constrained by the exact ternary valuation of
the next boundary.

### 3. Uniformly bounded `2`- and `3`-parts

Every scaled boundary satisfies

\[
\boxed{0\le v_2(W_n)\le3,}
\tag{6}
\]

and, after the first transition,

\[
\boxed{1\le v_3(W_n)\le3.}
\tag{7}
\]

All unbounded arithmetic complexity of `W_n` therefore lies in primes outside
`{2,3}`.

### 4. Signature-compatible transition graph

A type transition `i -> j` can occur only when

\[
\boxed{
v_2(W_n)=\alpha_i,
\qquad
v_3(W_{n+1})=\beta_i,
\qquad
v_2(W_{n+1})=\alpha_j.}
\tag{8}
\]

The four symbolic types are therefore ordinary adelic signatures, not arbitrary
labels.

## Proof

Because

\[
W_n=p_{i_n}+64h_n
\]

and `v_2(p_i)=alpha_i<6`, the second summand has strictly larger binary
valuation. Therefore

\[
v_2(W_n)=v_2(p_{i_n})=\alpha_{i_n},
\]

proving (3)--(4) and (6).

For the ternary valuation, the first term on the right side of (2) has

\[
v_3\left(3^{7(t_n+1)}W_n\right)
\ge7(t_n+1).
\]

The toll has valuation

\[
v_3(b_{i_n})=\beta_{i_n}\le3.
\]

The two valuations are unequal, so the valuation of their sum is the smaller
one:

\[
v_3\left(3^{7(t_n+1)}W_n+b_{i_n}\right)
=\beta_{i_n}.
\]

The left multiplier in (2) is a power of two and hence a 3-adic unit. This proves
(5) and (7). Equation (8) combines the two conclusions. ∎

## Strategic meaning

`T-0032` proves that an infinite ordinary path needs infinitely many fresh
primes. The present lemma locates those primes exactly: they cannot hide in
growing powers of two or three, whose valuations remain in the finite sets

```text
v_2 in {0,1,2,3}
v_3 in {1,2,3}.
```

This also strengthens the fixed-room approximation in `T-0033`. After reducing

\[
{W_m2^{e_m}\over3^{a_m}}
\]

to lowest terms, the removed power of three is at most `3^3`, while the numerator
retains the full power `2^(e_m+alpha_i)`.

That is the native input for a two-place Ridout-type approximation theorem.

## Gap audit

- Bounded `2`- and `3`-valuations do not bound the remaining prime support.
- The lemma does not show that every signature transition is realizable.
- It does not construct or exclude a cap-stitch tail.

## Adversarial tests

`X-0016` checks the two valuations on every exact boundary in its canonical
finite connector chains.