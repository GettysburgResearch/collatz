# T-9610 — Fixed-weight negative-three pulse grammars through 243 unpulsed letters are cycle-free

**Claim ID:** `T-9610`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** `T-9609`, `L-9611`; exact physical letters from PR #45 `L-8405` / PR #51 `O-8001`  
**Scope:** aligned fixed-weight grammars in the negative-three pulse chart  
**Related counterexample candidates:** none

## 1. Statement

In the exact ordinary coordinate

\[
n=6z+1,
\]

use the physical letters

\[
A:\quad 8z'=9z+1,
\qquad
B:\quad 16z'=9z.
\tag{1}
\]

For every

\[
0\le a\le243,
\qquad b\ge1,
\]

let the macro alphabet consist of **all** chronological words containing exactly `a` letters `A` and `b` letters `B`.

Then

\[
\boxed{
\text{no finite word over this complete macro alphabet is a nontrivial positive integral cycle.}}
\tag{2}
\]

The conclusion is uniform in pulse count, branch count, macro ordering, and repetition length.

## 2. Retained range through thirteen

`T-9609` already proves `(2)` for every

\[
0\le a\le13,
\qquad b\ge1.
\tag{3}
\]

We therefore assume

\[
14\le a\le243.
\tag{4}
\]

Every fixed-weight macro has the common affine summary

\[
\boxed{Qz'=Pz+e_w,}
\tag{5}
\]

where

\[
Q=8^a16^b,
\qquad
P=9^{a+b},
\tag{6}
\]

and the exact constant interval is

\[
9^b(9^a-8^a)
\le e_w\le
16^b(9^a-8^a).
\tag{7}
\]

Put

\[
e_{\max}=16^b(9^a-8^a).
\tag{8}
\]

## 3. Supercritical packets

If `P>Q`, then every `e_w` is positive and iteration around a proposed positive macro cycle of length `R` gives

\[
(Q^R-P^R)z_0
=
\sum_{t=0}^{R-1}P^{R-1-t}Q^te_{w_t}>0.
\tag{9}
\]

The left side is negative, a contradiction.

Equality `P=Q` is impossible because a positive power of two cannot equal a positive power of three.

Only the contracting case

\[
D=Q-P>0
\tag{10}
\]

remains.

## 4. Cycle-minimum upper bound

Rotate a proposed nontrivial cycle to a least macro-boundary state `m>=1`, and write the next boundary as

\[
m+k,
\qquad k\ge0.
\]

The first macro edge gives

\[
e_w=Dm+Qk=D(m+k)+Pk.
\tag{11}
\]

Hence

\[
\boxed{
m+k\le U(a,b),}
\qquad
U(a,b):={e_{\max}\over D}.
\tag{12}
\]

Writing

\[
R_a=\left({9\over8}\right)^a,
\qquad
S_b=\left({9\over16}\right)^b,
\]

one has in the contracting region

\[
\boxed{
U(a,b)={R_a-1\over1-R_aS_b}.}
\tag{13}
\]

For fixed `a`, this strictly decreases with `b`. For fixed `b`, it strictly increases with `a` while contraction persists, since

\[
{d\over dR}{R-1\over1-RS_b}
={1-S_b\over(1-RS_b)^2}>0.
\tag{14}
\]

Thus it is enough to check

\[
\boxed{
b_0(a)=\min\{b\ge1:9^{a+b}<8^a16^b\},}
\tag{15}
\]

and, on intervals where `b_0(a)` is constant, only the largest `a`.

## 5. Two-sided phase lower bound

Every macro in `(4)` has length at least ten. Therefore every positive macro boundary has ten physical letters on both sides.

`L-9611` and the exact `X-9614` phase certificate prove

\[
\boxed{
z\ge H_{10}=90{,}608{,}969{,}363{,}967}
\tag{16}
\]

for every such boundary.

In particular, the next boundary `m+k` in `(12)` satisfies `(16)`. Consequently a cycle is impossible whenever

\[
\boxed{e_{\max}<H_{10}D.}
\tag{17}
\]

## 6. Exact parameter certificate

`X-9614` checks, using exact integers, that for every

\[
14\le a\le243,
\]

one has

\[
\boxed{
16^{b_0(a)}(9^a-8^a)
<
H_{10}\bigl(8^a16^{b_0(a)}-9^{a+b_0(a)}\bigr).}
\tag{18}
\]

Equivalently,

\[
U(a,b_0(a))<H_{10}.
\tag{19}
\]

Monotonicity in `b` extends `(19)` to every contracting `b>=b_0(a)`, so `(17)` excludes every positive cycle.

The exact finite certificate has 230 parameter rows. Monotonicity `(14)` compresses these to 48 endpoint rows. Frozen digests:

```text
all 230 parameter rows:
b0116cde3b111814d35433b4478f524f3e84331edc538b25851c4ec349116390

48 endpoint rows:
f54a2e9227d44b8d12078e9a046900d17dd3e476fd54aacad2eb06fe74ecf0a0
```

The final certified interval is

\[
240\le a\le243,
\qquad b_0(a)=50,
\]

and the endpoint margin at `a=243` is positive as an exact integer. Its full value is frozen in

```text
experiments/X-9614-two-sided-phase-floor/results/canonical.json
```

rather than copied into the proof as an error-prone decimal.

## 7. Exact boundary of this certificate

At

\[
a=244,
\qquad b_0(a)=50,
\]

this particular depth-ten inequality reverses:

\[
H_{10}(8^{244}16^{50}-9^{294})
-16^{50}(9^{244}-8^{244})<0.
\tag{20}
\]

This is not evidence for a cycle. It means only that depth ten no longer proves the needed separation. The first open fixed-weight layer for this method is exactly

\[
\boxed{a=244.}
\]

## 8. Main conclusion

Combining the retained theorem `T-9609`, the supercritical sign argument, and the depth-ten phase certificate proves `(2)`.

The theorem is unbounded simultaneously in:

- pulse count `b`;
- physical macro length `a+b`;
- branch count `\binom{a+b}{b}`;
- macro repetition length;
- chronological switching among all fixed-weight macro branches;
- total nonneutral support `aR` after `R` macros.

It is therefore an exhaustive infinite-class theorem, not a bounded-period or fixed-support census.

## 9. Scope and logical strength

The theorem is genuinely weaker than Collatz. It excludes only aligned fixed-weight grammars in one exact negative-cycle-derived chart. The following remain outside scope:

- `a>=244`;
- scale-varying macro summaries;
- nonaligned internal repairs;
- arbitrary accelerated valuation words;
- aperiodic ordinary extraction in the supercritical six-branch chart.

No nontrivial cycle, divergent seed, or `K-####` candidate is claimed.

## 10. Verification

Review in this order:

1. `L-9611` source/output phase formulas;
2. the two-sided CRT boundary class;
3. the exact `H_10` minimum in `X-9614`;
4. the cycle-minimum bound `(11)`--`(12)`;
5. monotonicity `(13)`--`(15)`;
6. the 48 endpoint parameter rows;
7. the exact physical replay inherited from the source chart.

Frozen semantic digest:

```text
296074c8e5f59c11bc1de1c7d0d89084ae79012381ff1d850fb611281fe0cf06
```
