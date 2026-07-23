# T-8603 — Positive cycles require at least sixteen non-neutral valuations

**Claim ID:** `T-8603`  
**Title:** Exact centered-defect exclusion for support sizes seven through fifteen  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Dependencies:** elementary accelerated-cycle algebra; exact experiments `X-8603`, `X-8604`, `X-8608`, and `X-8609`  
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
\boxed{s\in\{7,8,9,10,11,12,13,14,15\}}
\]

defects.

Equivalently, every nontrivial positive accelerated cycle has either at most
six defects or at least sixteen defects. Combined with the branch-qualified
proposed six-defect exclusion `PR34/L-9913`, the current proposed theorem chain
gives

\[
\boxed{\text{every nontrivial positive accelerated cycle has at least sixteen defects.}}
\]

The native statement of this file is the exact exclusion of support sizes seven
through fifteen. It does not silently promote the external branch claim.

## 1. Centering at the trivial fixed point

For the word `w`, put

\[
A_j=\sum_{i<j}a_i,\qquad A=A_k,
\]

\[
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},\qquad
D_w=2^A-3^k,\qquad E_w=C_w-D_w.
\tag{1}
\]

The accelerated cycle equation is

\[
n_0D_w=C_w.
\tag{2}
\]

Subtracting the trivial fixed state `1` gives

\[
(n_0-1)D_w=E_w.
\tag{3}
\]

A direct telescoping calculation yields

\[
\boxed{E_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}(4-2^{a_j}).}
\tag{4}
\]

Thus every neutral valuation `2` disappears from the centered numerator.

The centered one-step branch is

\[
g_a(y)=\frac{3y+4-2^a}{2^a}.
\tag{5}
\]

For `y>0`, deleting `g_2(y)=3y/4` increases every later replay. If
`a\ge c\ge3`, then

\[
g_c(y)-g_a(y)=(2^{-c}-2^{-a})(3y+4)>0,
\]

so lowering a high valuation also increases replay. Every `g_a` is increasing.
A nontrivial positive odd cycle contains neither `1`, `3`, nor `5`; hence every
cycle state is at least `7` and every centered state satisfies `y=n-1\ge6`.

These monotonicities drive the complete finite classification through support
thirteen and remain useful as pruning at larger support.

## 2. Supports seven through thirteen

For supports `7` through `13`, contraction at centered floor `6` reduces every
possible defect multiset to a finite survivor list. Rotating a largest neutral
gap to the end gives

\[
D_R=2^B4^R-3^s3^R,
\qquad
E_w=3^tE_u,
\]

with `t` the terminal largest gap and `u` the core before that gap. Since
`gcd(D_R,3)=1`, a positive exact cycle requires

\[
D_R>0,\qquad D_R\mid E_u,\qquad E_u\ge2D_R.
\tag{6}
\]

A positive-term rearrangement bound makes every surviving defect type finite.
`X-8603` performs a lossless maximum-height dynamic program followed by direct
enumeration for supports seven through twelve. `X-8604` uses an exact affine
meet-in-the-middle residue join at support thirteen.

Frozen results:

```text
X-8603 supports 7..12
contraction_classes=1082
enumerated_rows=2577878885
explicit_cases=421
dp_pruned_cases=512
divisor_hits=0

X-8604 support 13
contraction_classes=1018
patterns=4746
pattern_rows=136508
dp_pruned=109188
left_states=64869934
right_states=64869934
queries=64674409
hits=0
```

No divisor hit reached the exact valuation-replay gate.

## 3. Finite product windows for supports fourteen and fifteen

The support-fourteen contraction classifier has unbounded high-valuation
families, so `X-8608` and `X-8609` do not impose a finite high-letter alphabet.
Instead they use the exact cycle product window.

Let `s` be the defect support, let

\[
B=\sum_{a_j\ne2}a_j,
\qquad
R=\#\{j:a_j=2\}.
\]

Then

\[
k=s+R,
\qquad
A=B+2R.
\]

The least odd state in a nontrivial positive cycle is at least `7`. The exact
product formula therefore gives

\[
3^k<2^A\le\left(3+\frac17\right)^k=\left(\frac{22}{7}\right)^k.
\tag{7}
\]

Equivalently, every candidate cell satisfies the integer inequalities

\[
\boxed{
3^{s+R}<2^{B+2R},
\qquad
2^{B+2R}7^{s+R}\le22^{s+R}.}
\tag{8}
\]

For fixed `s`, these inequalities leave only finitely many `(R,B)` cells.
Within a cell, every cyclic word can be rotated to begin at a defect and is
represented by

- an ordered defect word of length `s` over `{1,3,4,...}` with sum `B`; and
- a weak composition of `R` into `s` neutral gaps.

No defect value or gap distribution is omitted.

## 4. Exact affine join

For any finite valuation word `v`, let `m_v`, `A_v`, and `C_v` denote its
length, valuation sum, and affine constant. Concatenation satisfies

\[
\boxed{C_{uv}=3^{m_v}C_u+2^{A_u}C_v.}
\tag{9}
\]

For one fixed product cell, the denominator

\[
D=2^{B+2R}-3^{s+R}
\]

is fixed and odd. Splitting the defect/gap representation into two halves fixes
the two join multipliers once the half defect sum and half neutral total are
fixed. Sorting one transformed residue list and querying the exact complementary
residue is therefore equivalent to testing `D\mid C_w` for every represented
word.

A modular match is not accepted as a cycle. Both programs regenerate the full
valuation word, compute the forced start `n_0=C_w/D`, and replay every exact
valuation and the return before reporting a hit.

## 5. Complete support-fourteen result

`X-8608` uses a `7+7` defect split. Exact coverage:

```text
windows=37
conceptual_words=50008555902
left_states=62907549
right_states=62907549
queries=62907549
hits=0
```

The independent Python audit reconstructs all product cells and state counts
and directly enumerates the smallest neutral totals. The authoring replay also
agrees byte-for-byte with the frozen canonical output.

Therefore no nontrivial positive accelerated cycle has exactly fourteen
defects.

## 6. Complete support-fifteen result

`X-8609` uses a `7+8` defect split. Moduli above 64 bits use exact two-limb
Montgomery reduction; any match is regenerated with arbitrary-precision
integers before replay.

The computation was frozen in six neutral-total chunks. Combined exact
coverage is

```text
windows=42
conceptual_words=355362127531
left_states=126760223
right_states=475187506
queries=126760223
hits=0
```

The independent Python audit reconstructs all 42 cells, every conceptual and
half-state count, and directly enumerates the smallest cells.

Therefore no nontrivial positive accelerated cycle has exactly fifteen
defects.

## 7. Exact first open layer

The minimal unclosed defect support is now sixteen. For support sixteen the same
product inequalities leave a finite cell set, but the current `8+8` join grows
substantially at the first large 66-bit row. The first unfinished cell in the
current scout is

\[
\boxed{R=24,\qquad B=18.}
\]

A timeout or resource limit in that row is not evidence for or against a cycle.
It is the exact next computational target.

## Dependency audit

- Equations `(1)` through `(5)` are elementary accelerated-cycle algebra.
- The floor `n\ge7` uses only `S(3)=5` and `S(5)=1`.
- The finite window `(8)` is the exact product formula with that floor.
- The join `(9)` is exact affine composition.
- The support-seven-through-thirteen conclusion depends on `X-8603` and
  `X-8604`.
- The support-fourteen and support-fifteen conclusions depend on `X-8608` and
  `X-8609` respectively.
- The corollary “at least sixteen defects” additionally cites the separate,
  branch-qualified proposed `PR34/L-9913` exclusion through six defects.

## Gap audit

- The four large exact computations still require independent repository
  reimplementation before promotion.
- Nothing here excludes support sixteen or larger.
- Nothing here addresses divergent nonperiodic orbits.
- Conceptual word counts are coverage counts; stored states are reported
  separately.
- No probabilistic inference is made from zero hits.

## Adversarial tests

- Every experiment contains a dormant hit path that reconstructs the complete
  word and performs exact valuation replay.
- `X-8608/verify.py` and `X-8609/verify.py` independently reconstruct windows
  and counts and directly enumerate the smallest cells.
- Both C++ programs were replayed in the authoring environment against their
  frozen canonical outputs.

## Suggested next attack

1. Complete support sixteen beginning with `(R,B)=(24,18)` using an `8+8`
   external merge, residue bucketing, or factorwise CRT join.
2. Route every modular hit immediately to exact reconstruction rather than
   accumulating near-candidates.
3. In parallel, compare the same changing-modulus residue compiler with the
   quotient-refund counter’s most-significant divisibility condition; both
   lanes now isolate ordinary integrality as their sole missing gate.
