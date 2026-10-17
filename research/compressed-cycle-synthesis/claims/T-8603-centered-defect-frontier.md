# T-8603 — Positive cycles require at least eighteen non-neutral valuations

**Claim ID:** `T-8603`  
**Title:** Exact centered-defect exclusion for support sizes seven through seventeen  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Dependencies:** elementary accelerated-cycle algebra; exact experiments `X-8603`, `X-8604`, `X-8608`, `X-8609`, `X-8610`, and `X-8611`  
**Scope:** positive cycles of the accelerated odd Collatz/Syracuse map  
**Related counterexample candidates:** none

## Statement

Let

\[
S(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}
\]

on positive odd integers. For a finite accelerated valuation word

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_j\ge1,
\]

call an index **neutral** when `a_j=2` and a **defect** when `a_j\ne2`.
Then no nontrivial positive exact `S`-cycle has exactly

\[
\boxed{s\in\{7,8,9,10,11,12,13,14,15,16,17\}}
\]

defects.

Equivalently, every nontrivial positive accelerated cycle has either at most
six defects or at least eighteen defects. Combined with the branch-qualified
proposed six-defect exclusion `PR34/L-9913`, the current proposed theorem chain
gives

\[
\boxed{\text{every nontrivial positive accelerated cycle has at least eighteen defects.}}
\]

The native statement of this file is the exact exclusion of support sizes seven
through seventeen. It does not silently promote the external branch claim.

## 1. Centered cycle equation

Put

\[
A_j=\sum_{i<j}a_i,\qquad A=A_k,
\]

\[
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},\qquad
D_w=2^A-3^k,\qquad E_w=C_w-D_w.
\tag{1}
\]

The usual accelerated cycle equation and its centered form are

\[
n_0D_w=C_w,
\qquad
(n_0-1)D_w=E_w.
\tag{2}
\]

A direct telescoping calculation gives

\[
\boxed{E_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j}).}
\tag{3}
\]

Thus every neutral valuation `2` contributes exactly zero to the centered
numerator. The centered one-step branch

\[
g_a(y)=\frac{3y+4-2^a}{2^a}
\tag{4}
\]

is increasing; deleting a neutral branch or lowering a valuation `a\ge3`
increases the replay on positive states. Since a nontrivial positive odd cycle
contains neither `1`, `3`, nor `5`, every centered cycle state satisfies
`y=n-1\ge6`. These facts yield the finite contraction classification used by
`X-8603` and `X-8604` through support thirteen.

## 2. Exact product cells at fixed support

For support `s`, let

\[
B=\sum_{a_j\ne2}a_j,
\qquad
R=\#\{j:a_j=2\}.
\]

Then the odd length and total dyadic exponent are

\[
k=s+R,
\qquad
A=B+2R.
\]

The least odd state in a nontrivial positive cycle is at least `7`. The exact
product formula therefore implies

\[
3^k<2^A\le\left(3+\frac17\right)^k=\left(\frac{22}{7}\right)^k,
\]

or equivalently

\[
\boxed{
3^{s+R}<2^{B+2R},
\qquad
2^{B+2R}7^{s+R}\le22^{s+R}.}
\tag{5}
\]

For each fixed support these exact integer inequalities leave finitely many
`(R,B)` cells without imposing any artificial upper bound on a defect value.
Every cyclic word can be rotated to begin at a defect and represented by

1. an ordered defect word of length `s`, with letters in `{1,3,4,...}` and sum
   `B`; and
2. a weak composition of `R` into `s` neutral gaps.

No defect value, zero gap, or gap distribution is omitted.

## 3. Exact affine join and replay gate

For finite valuation words `u` and `v`, affine composition gives

\[
\boxed{C_{uv}=3^{|v|}C_u+2^{A_u}C_v.}
\tag{6}
\]

At a fixed product cell the denominator

\[
D=2^{B+2R}-3^{s+R}
\]

is fixed and odd. After fixing the defect-sum and neutral-total split, equation
`(6)` makes a transformed meet-in-the-middle residue match exactly equivalent
to the necessary divisibility condition `D\mid C_w`.

A modular match is never accepted as a cycle. Every experiment regenerates the
full valuation word, computes the forced start `n_0=C_w/D`, checks positivity
and oddness, re-evaluates every advertised valuation
`\nu_2(3n+1)`, and verifies the exact return.

## 4. Supports seven through fifteen

The earlier exact packets give:

```text
X-8603 supports 7..12
contraction_classes=1082
enumerated_rows=2577878885
divisor_hits=0

X-8604 support 13
queries=64674409
hits=0

X-8608 support 14
windows=37
conceptual_words=50008555902
queries=62907549
hits=0

X-8609 support 15
windows=42
conceptual_words=355362127531
queries=126760223
hits=0
```

The support-fourteen and support-fifteen programs use the complete product
window `(5)` and therefore cover their full high-valuation alphabets.

## 5. Eureka: cyclic defect-necklace quotient

The first naive support-sixteen join became expensive because it carried every
rotation of a defect pattern separately. This multiplicity is unnecessary.
Every putative cyclic cycle can be rotated so that its defect word is the
lexicographically least rotation of its defect orbit. Rotating the cycle merely
rotates its neutral-gap vector, and the search already enumerates every gap
vector. Therefore it is lossless to retain one **defect necklace** and all
compatible gaps.

Formally, for a defect word `p=(p_0,...,p_{s-1})`, choose

\[
p=\min_{0\le j<s}(p_j,\ldots,p_{s-1},p_0,\ldots,p_{j-1}).
\tag{7}
\]

For any cycle represented by a rotation `q` of `p` with gaps `g`, rotate the
whole valuation word by the inverse defect rotation. The resulting word has
defect pattern `p`, a rotated gap vector `g'`, the same denominator, and a
cyclically conjugate exact orbit. Since all `g'` are enumerated, no cycle is
lost.

This quotient reduced the former support-sixteen bottleneck `(R,B)=(24,18)`
from tens of millions of redundant anchored states to a single defect necklace
and small gap-half tables.

## 6. Complete support-sixteen result — `X-8610`

`X-8610` uses the necklace quotient, an `8+8` affine split, and stores the
smaller transformed gap-half list at every neutral-total split. Exact coverage:

```text
windows=48
anchored_words=2216415791876
canonical_pattern_gap_instances=724990098067
stored_states=6134501
queries=543652557
formal_matches=0
exact_cycles=0
```

The independent Python verifier reconstructs all 48 product cells, applies
Burnside/explicit rotation checks to the defect necklaces, rebuilds every
coverage and half-state count, and directly enumerates the smallest cells.

Therefore no nontrivial positive accelerated cycle has exactly sixteen
defects.

## 7. Complete support-seventeen result — `X-8611`

`X-8611` generalizes the same construction to a `8+9` split. Since `17` is
prime, every nonconstant defect word has a full rotation orbit of size `17`;
the constant cases are handled explicitly. Large all-one cells are divided by
left-half neutral total, which changes neither the residue relation nor
coverage.

Exact coverage:

```text
windows=55
anchored_words=16071941097518
canonical_pattern_gap_instances=4856645105230
stored_states=17053060
queries=2471674701
formal_matches=0
exact_cycles=0
```

The independent verifier reconstructs all product windows, necklace counts,
conceptual and half-state counts, and directly exhausts the smallest cells.

Therefore no nontrivial positive accelerated cycle has exactly seventeen
defects.

## 8. Current boundary

The first unclosed defect layer is now support eighteen. The same product-window
and necklace compiler applies, but the largest all-one cells require further
sharding, external sorting, residue bucketing, or factorwise CRT compilation.
A resource boundary in support eighteen would not be evidence for a cycle.

## Dependency audit

- Equations `(1)` through `(4)` are elementary accelerated-cycle algebra.
- The floor `n\ge7` uses only `S(3)=5` and `S(5)=1`.
- The finite window `(5)` is the exact product formula with that floor.
- The join `(6)` is exact affine composition.
- The necklace quotient `(7)` uses only cyclic rotation invariance of the cycle
  equation and exhaustive enumeration of the rotated gap vector.
- Supports seven through seventeen depend on their named exact experiments.
- The corollary “at least eighteen defects” additionally cites the separate,
  branch-qualified proposed `PR34/L-9913` exclusion through six defects.

## Gap audit

- The six large computations still require independent repository
  reimplementation before promotion.
- Nothing here excludes support eighteen or larger.
- Nothing here addresses divergent nonperiodic orbits.
- Anchored conceptual counts and canonical quotient counts are reported
  separately; neither is presented as a number of stored states.
- No probabilistic inference is made from zero hits.

## Suggested next attack

1. Apply the necklace compiler to support eighteen with row-level checkpoints
   and neutral-split sharding.
2. Introduce a proof-producing prime-power/CRT prejoin for the largest rows,
   retaining exact full-modulus reconstruction for every survivor.
3. Compare the changing-modulus compiler with the quotient-refund map: both
   lanes now isolate ordinary divisibility, while refund already supplies
   positivity and exponential growth once defined forever.
