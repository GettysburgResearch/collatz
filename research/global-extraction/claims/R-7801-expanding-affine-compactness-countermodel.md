# R-7801 — Expanding affine finite compatibility does not imply ordinary extraction

**Claim ID:** `R-7801`  
**Type:** refutation / architecture boundary  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-global-01`  
**Created:** 2026-07-25  
**Dependencies:** elementary congruence algebra; `T-7801` only for interpretation  
**Scope:** nonautonomous odd-over-dyadic affine systems  
**Related counterexample candidates:** none

## Refuted inference

The following implication is false, even with arbitrarily strong expansion:

```text
every finite prefix has infinitely many positive ordinary realizations
+ the finite cylinders are nested and select one infinite compatible point
+ every legal finite step is exact, integral, positive, and expanding
+ the odd multiplier dominates the dyadic divisor by an arbitrarily large factor
=> one ordinary integer realizes the infinite path.
```

The conclusion requires an archimedean extraction theorem. It does not follow from the listed local properties.

## Universal construction theorem

Let

\[
q_n=2^{e_n}\ge2,
\qquad
M_0=1,
\qquad
M_{n+1}=M_nq_n.
\]

Choose mixed-radix digits

\[
0\le d_n<q_n
\]

that are neither eventually zero nor eventually equal to `q_n-1`. Define

\[
R_0=0,
\qquad
R_{n+1}=R_n+d_nM_n.
\tag{1}
\]

Thus

\[
0\le R_n<M_n,
\qquad
R_{n+1}\equiv R_n\pmod {M_n}.
\]

Let `(Lambda_n)` be any prescribed sequence of positive real numbers. There exist:

- positive odd integers `A_n` with
  \[
  A_n>\Lambda_n q_n;
  \]
- integers
  \[
  0\le b_n<q_n;
  \]

such that the deterministic affine maps

\[
\boxed{
F_n(x)=\frac{A_nx+b_n}{q_n}}
\tag{2}
\]

have all of the following properties.

1. **Exact finite-cylinder equivalence.** An initial integer `x_0` follows the first `N` maps integrally if and only if
   \[
   x_0\equiv R_N\pmod {M_N}.
   \tag{3}
   \]
2. **Infinite positive realization at every finite depth.** For every `N`, infinitely many positive integers follow the first `N` maps integrally.
3. **Positivity.** Every integral trajectory beginning at a positive integer remains positive.
4. **Arbitrarily prescribed expansion.** Every legal positive step satisfies
   \[
   F_n(x)>\Lambda_n x.
   \tag{4}
   \]
5. **No ordinary infinite realization.** No integer `x_0\in Z` follows every map integrally.

In particular, the expansion factors `Lambda_n` may tend to infinity arbitrarily rapidly.

## Construction and proof

We construct the maps together with the composed affine numerators.

Put

\[
P_0=1,
\qquad
C_0=0.
\]

Suppose `P_n,C_n` have been chosen so that the first `n` maps compose to

\[
x_n=\frac{P_nx_0+C_n}{M_n},
\tag{5}
\]

with

\[
P_n\text{ odd},
\qquad
C_n\equiv-P_nR_n\pmod {M_n}.
\tag{6}
\]

Choose any positive odd integer

\[
A_n>\Lambda_nq_n.
\]

Because

\[
R_{n+1}\equiv R_n\pmod {M_n}
\]

and `(6)` holds, the integer

\[
E_n=
-\frac{A_n(P_nR_{n+1}+C_n)}{M_n}
\tag{7}
\]

is well defined. Choose `b_n` to be its canonical residue modulo `q_n`:

\[
0\le b_n<q_n,
\qquad
b_n\equiv E_n\pmod {q_n}.
\tag{8}
\]

Define

\[
P_{n+1}=A_nP_n,
\]

\[
C_{n+1}=A_nC_n+b_nM_n.
\tag{9}
\]

Then

\[
F_n(x_n)
=
\frac{A_n(P_nx_0+C_n)+b_nM_n}{M_nq_n}
=
\frac{P_{n+1}x_0+C_{n+1}}{M_{n+1}},
\]

so `(5)` propagates.

By `(7)--(9)`,

\[
C_{n+1}+P_{n+1}R_{n+1}
\equiv0\pmod {M_nq_n},
\]

which is `(6)` at level `n+1`.

Since every `A_j` is odd, `P_N` is invertible modulo the dyadic modulus `M_N`. Therefore

\[
M_N\mid P_Nx_0+C_N
\quad\Longleftrightarrow\quad
x_0\equiv R_N\pmod {M_N}.
\]

This proves `(3)`. Compatibility of the residue chain then shows that the first `N` composed states are all integral exactly for that same cylinder.

For every `N`, the integers

\[
x_0=R_N+tM_N,
\qquad t=1,2,3,\ldots,
\]

are positive finite-prefix realizations. This proves property 2.

If a legal state `x` is positive, then

\[
F_n(x)=\frac{A_nx+b_n}{q_n}>0
\]

because `A_n>0` and `b_n>=0`. Moreover,

\[
F_n(x)
\ge\frac{A_n}{q_n}x
>\Lambda_nx.
\]

This proves properties 3 and 4.

If one ordinary integer followed every map, `(3)` would make it realize every nested cylinder `R_N mod M_N`. The digits were chosen neither eventually zero nor eventually maximal. By the signed criterion of `T-7801`, the selected inverse-limit point is neither a nonnegative nor a negative ordinary integer. This proves property 5. ∎

## Concrete one-bit example

Take

\[
q_n=2,
\qquad
d_n=n\bmod2.
\]

The selected binary completion has alternating digits

```text
0,1,0,1,0,1,...
```

and is neither eventually zero nor eventually one. Every finite binary prefix has infinitely many positive ordinary representatives, but the unique `2`-adic completion is not in `Z`.

The theorem decorates this same chain with any desired odd multipliers and any desired finite-step expansion factors.

## Consequences for current Collatz architectures

The result does not refute an architecture-specific Collatz theorem. It refutes a **proof schema**.

Once exact physical replay has been proved, the remaining existence question is still whether one initial ordinary integer lies in every pulled-back cylinder. Physical replay is a conditional conjugacy: it tells us what happens if such an integer exists, not that it exists.

Therefore none of the following, alone or in any combination that uses only their local content, can prove ordinary extraction:

- every finite word or path has positive representatives;
- a nonempty compact inverse-limit path set;
- a unique `2`-adic completion;
- large odd-over-dyadic expansion;
- quotient doubling or permanent refund after entry;
- positive core growth;
- finite branching, SCCs, or modular lassos;
- Haar-nullness, positive dimension, or entropy estimates;
- fresh-prime turnover conditional on an infinite path.

A successful proof must add information not present in this countermodel—for example:

```text
bounded canonical least representatives;
a global ranking contradiction forcing exit;
a completion-height theorem forcing eventual zero blocks;
an exact ordinary invariant with one explicit initialization;
or a full-denominator finite cycle equality.
```

## Why this is an exhaustive architecture-level negative result

Every nonautonomous odd-over-dyadic affine system whose finite-prefix legality is encoded only by nested congruence classes admits the countermodel mechanism above. Thus there is no universal compactness-plus-refund extraction theorem at that level of abstraction.

Any positive theorem for PR #45, PR #49, PR #51, the H renewal counter, or a centered cylinder must use a source-specific global relation beyond their shared affine/cylinder/refund skeleton.

## Gap audit

- The constructed maps are not claimed to be Collatz blocks.
- Accordingly, the theorem does not eliminate any specific Collatz subsystem.
- It eliminates only arguments that treat the common affine/cylinder/refund properties as sufficient for ordinary existence.
- A special identity in one architecture may still force bounded representatives; that is precisely the remaining legitimate target.