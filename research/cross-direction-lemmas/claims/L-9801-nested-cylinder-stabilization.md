# L-9801 — Ordinary stabilization for canonical nested cylinders

Claim ID: `L-9801`  
Title: Canonical nested cylinders realize an ordinary nonnegative integer exactly by eventual stabilization  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01-p`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: compatible residue cylinders with growing nested moduli  
Related counterexample candidates: none

## Definitions

A **canonical representative modulo** `Q` is the unique representative in
`[0,Q)`. A residue sequence `(R_k mod Q_k)` is **compatible** when
`Q_k | Q_(k+1)` and `R_(k+1)=R_k mod Q_k`. Its inverse-limit point has an
**ordinary nonnegative realization** if one integer `A>=0` has residue `R_k`
modulo `Q_k` for every `k`. The representatives **eventually stabilize** when
`R_k` is constant for all sufficiently large `k`.

## Statement

Let

\[
1\le Q_0\mid Q_1\mid Q_2\mid\cdots,
\qquad Q_k\longrightarrow\infty,
\]

and let `R_k` be the canonical representatives of a compatible residue
sequence:

\[
0\le R_k<Q_k,
\qquad
R_{k+1}\equiv R_k\pmod{Q_k}.
\tag{1}
\]

Then the following hold.

### 1. Mixed-radix monotonicity

For every `k` there is a unique integer `a_k` such that

\[
R_{k+1}=R_k+a_kQ_k,
\qquad
0\le a_k<\frac{Q_{k+1}}{Q_k}.
\tag{2}
\]

In particular, `(R_k)` is nondecreasing.

### 2. Ordinary realization criterion

The compatible inverse-limit point is represented by an ordinary
nonnegative integer `A` if and only if `R_k` eventually stabilizes. In that
case the stable value is `A`.

Equivalently,

\[
\bigcap_{k\ge0}
\{n\in\mathbb Z_{\ge0}:n\equiv R_k\pmod{Q_k}\}
\ne\varnothing
\tag{3}
\]

if and only if `(R_k)` is eventually constant; when nonempty, the
intersection is a singleton.

### 3. Equivalent finite tests

The following are equivalent:

1. the inverse-limit point is an ordinary nonnegative integer;
2. `R_k` eventually stabilizes;
3. `a_k=0` for all sufficiently large `k`;
4. the nondecreasing integer sequence `(R_k)` is bounded.

When `Q_k=p^{e_k}` for one prime `p` with `e_k -> infinity`, the inverse-limit
point is the unique element of `Z_p` having residues `R_k`. The criterion above
then distinguishes an ordinary nonnegative integer inside `Z_p` from a merely
`p`-adic point.

## Proof

Compatibility in (1) makes `R_{k+1}-R_k` an integer multiple of `Q_k`, so
there is a unique integer `a_k` satisfying the equality in (2). If `a_k<0`,
then

\[
R_{k+1}\le R_k-Q_k<0,
\]

contrary to the canonical range for `R_{k+1}`. Hence `a_k>=0`. Also

\[
a_kQ_k=R_{k+1}-R_k<Q_{k+1},
\]

which gives the upper bound in (2). This proves part 1.

Suppose an ordinary `A>=0` has all the displayed residues. Choose `k_0` with
`Q_{k_0}>A`. For every `k>=k_0`, the canonical representative of `A` modulo
`Q_k` is `A` itself, so `R_k=A`. Thus ordinary realization implies eventual
stabilization.

Conversely, if `R_k=A` for every `k>=k_0`, compatibility shows that the same
ordinary integer `A` satisfies every earlier congruence as well. It therefore
represents the inverse-limit point and belongs to (3).

If two nonnegative integers `A` and `B` belonged to (3), every `Q_k` would
divide `A-B`. Since `Q_k -> infinity`, this forces `A=B`. The intersection is
therefore a singleton whenever it is nonempty.

Equation (2) shows that eventual stabilization is equivalent to eventual
vanishing of `a_k`. A bounded nondecreasing sequence of integers is eventually
constant, and an eventually constant sequence is bounded. This proves all
equivalences in part 3. The `p`-adic specialization is the standard inverse
limit description of `Z_p`. ∎

## Motivation

This lemma is the common ordinary-realization checkpoint for several active
directions:

- the H-frontier uses least exact-cylinder representatives `Pi(w)` and
  eventual zero carry;
- PR #20 uses least initial survivor-cylinder representatives `R_K` and
  extension blocks;
- PR #3 uses compatible connector and residual cylinders generated at
  increasing precision.

In each case, arbitrarily long finite realizations or a unique completion
point are strictly weaker than an ordinary infinite trajectory.

## Dependency audit

No Collatz-specific claim is used. Only elementary divisibility, canonical
residue representatives, and monotonicity of bounded integer sequences enter
the proof.

## Gap audit

- The lemma does not prove stabilization or non-stabilization for any active
  directive.
- A noncanonical choice of representatives need not be monotone; canonical
  ranges are essential.
- The statement concerns nonnegative integers. Negative ordinary integers use
  centered or complementary representatives and need a separately stated
  convention.
- A large modulus, large representative, or large archimedean bit budget says
  nothing by itself about eventual stabilization.

## Adversarial tests

- `R_k=A` with `Q_k>A` is the stabilizing case.
- `R_k=Q_k-1` is compatible and represents `-1` in a prime-adic inverse
  limit, but it does not stabilize and correctly fails the nonnegative
  criterion.
- The binary prefixes `R_k=sum_{j<k} b_j 2^j` stabilize exactly when the digit
  stream has only finitely many `1` bits.

## Remaining uncertainty

None in the abstract lemma. Its usefulness in a given program depends on
proving that the program's finite cylinders are compatible and canonically
represented.

## Suggested next attack

For each active cylinder construction, derive an exact recurrence for its
digits `a_k`. A counterexample route must make those digits eventually zero;
an obstruction route must force infinitely many nonzero digits.
