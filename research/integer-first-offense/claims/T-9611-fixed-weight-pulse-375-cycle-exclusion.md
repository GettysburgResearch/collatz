# T-9611 — Fixed-weight negative-three pulse grammars through 375 unpulsed letters are cycle-free

**Claim ID:** `T-9611`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** `T-9610`, `L-9611`; exact physical letters from PR #45 `L-8405` / PR #51 `O-8001`  
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
0\le a\le375,
\qquad b\ge1,
\]

let the macro alphabet contain every chronological word with exactly `a` letters `A` and `b` letters `B`.

Then

\[
\boxed{
\text{no finite word over this complete macro alphabet is a nontrivial positive integral cycle.}}
\tag{2}
\]

The conclusion is uniform in pulse count, branch count, chronological macro ordering, and repetition length.

## 2. Retained range through 243

`T-9610` proves `(2)` for every

\[
0\le a\le243,
\qquad b\ge1.
\tag{3}
\]

We therefore assume

\[
244\le a\le375.
\tag{4}
\]

Every fixed-weight macro has common affine data

\[
Qz'=Pz+e_w,
\qquad
Q=8^a16^b,
\qquad
P=9^{a+b},
\tag{5}
\]

with

\[
0<e_w\le e_{\max}=16^b(9^a-8^a).
\tag{6}
\]

## 3. Supercritical packets

If `P>Q`, then iteration around a proposed positive macro cycle of length `R` gives

\[
(Q^R-P^R)z_0
=
\sum_{t=0}^{R-1}P^{R-1-t}Q^te_{w_t}>0,
\tag{7}
\]

while the left side is negative. Thus no positive cycle exists.

There is no equality case because a positive power of two cannot equal a positive power of three.

It remains to treat

\[
D=Q-P>0.
\tag{8}
\]

## 4. Cycle-minimum upper bound

Rotate a proposed nontrivial cycle to a minimum boundary `m>=1`, and write the next boundary as `m+k`, `k>=0`. The first macro edge gives

\[
e_w=Dm+Qk=D(m+k)+Pk.
\tag{9}
\]

Consequently

\[
\boxed{m+k\le U(a,b),}
\qquad
U(a,b):={e_{\max}\over D}.
\tag{10}
\]

Writing

\[
R_a=\left({9\over8}\right)^a,
\qquad
S_b=\left({9\over16}\right)^b,
\]

one has

\[
U(a,b)={R_a-1\over1-R_aS_b}.
\tag{11}
\]

For fixed `a`, this decreases strictly with `b`. For fixed `b`, it increases strictly with `a` while contraction persists, because

\[
{d\over dR}{R-1\over1-RS_b}
={1-S_b\over(1-RS_b)^2}>0.
\tag{12}
\]

Therefore it is enough to check the least contracting pulse count

\[
b_0(a)=\min\{b\ge1:9^{a+b}<8^a16^b\}
\tag{13}
\]

and one largest `a` in each interval on which `b_0(a)` is constant.

## 5. Exact depth-fifteen phase floor

Every macro in `(4)` has at least fifteen physical letters on both sides of every cyclic macro boundary.

`L-9611` defines the two-sided phase floor, and the independent `X-9615` reconstructions prove

\[
\boxed{H_{15}=874{,}917{,}472{,}129{,}210{,}216{,}448.}
\tag{14}
\]

The unique minimizing ordered phase pair is

```text
past suffix   BAAABBBBBBABAAA
future prefix BBBAABAABABAAAA
```

with

\[
\begin{aligned}
\sigma(BAAABBBBBBABAAA)
  &=195{,}256{,}963{,}146{,}815
    &&\pmod{205{,}891{,}132{,}094{,}649},\\
\rho(BBBAABAABABAAAA)
  &=920{,}720{,}130{,}273{,}280
    &&\pmod{2{,}251{,}799{,}813{,}685{,}248}.
\end{aligned}
\tag{15}
\]

Hence every positive macro boundary in `(4)` satisfies

\[
\boxed{z\ge H_{15}.}
\tag{16}
\]

Combining `(10)` and `(16)`, every contracting packet is excluded once

\[
\boxed{e_{\max}<H_{15}D.}
\tag{17}
\]

## 6. Exact parameter certificate

`X-9615` independently checks `(17)` for every

\[
244\le a\le375
\]

at `b=b_0(a)`. There are 132 exact parameter rows. Monotonicity `(11)`--`(13)` compresses the proof to 28 interval endpoints.

Frozen parameter digests:

```text
all 132 rows:
d41faff63b5db9fef5ac8a4e826b6b1bd07092abbd2ba3966c6f88ac3d3ce3bc

28 endpoint rows:
11f4aa4c2c893a95450f167b2189bbf24725110de9b3217aff68b6076f8e102e
```

Thus `(17)` holds for every contracting `b>=b_0(a)` in the range `(4)`. Together with the supercritical sign argument, this proves `(2)`.

## 7. Exact method boundary

At

\[
a=376,
\qquad b_0(a)=77,
\]

this particular depth-fifteen inequality reverses:

\[
H_{15}\bigl(8^{376}16^{77}-9^{453}\bigr)
-16^{77}(9^{376}-8^{376})<0.
\tag{18}
\]

This does not produce or suggest a cycle. It states only that the depth-fifteen phase floor is no longer large enough for the direct height comparison. The first open fixed-weight layer for this certificate is

\[
\boxed{a=376.}
\]

## 8. Exact finite certificate

The depth-fifteen phase computation contains

\[
2^{15}=32{,}768
\]

past suffixes and the same number of future prefixes, hence

\[
\boxed{4^{15}=1{,}073{,}741{,}824}
\]

ordered CRT phase pairs.

Two separately implemented C++ programs reconstruct the complete table:

- the generator uses the closed affine constant formula;
- the verifier builds every source cylinder by iterative local residue lifting.

Both also reconstruct all parameter signs through `a=375` and the first failure at `a=376`.

Frozen aggregate checks:

```text
minimum multiplicity: 1
aggregate sum mod 2^64: 694153015195832603
aggregate xor:          7571253252837843397
```

## 9. Strength and scope

The theorem is unbounded simultaneously in:

- pulse count `b`;
- physical macro length `a+b`;
- branch count `\binom{a+b}{b}`;
- macro repetition length;
- chronological switching among all fixed-weight macro branches;
- total nonneutral support `aR` after `R` macros.

It is still strictly weaker than Collatz. It does not cover:

- `a>=376`;
- scale-varying macro summaries;
- nonaligned internal repairs;
- arbitrary accelerated valuation words;
- the separate aperiodic ordinary-extraction problem in the supercritical six-branch chart.

No nontrivial cycle, divergent seed, or `K-####` candidate is claimed.

## 10. Verification

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9615-depth15-phase-floor/run.cpp \
  -o /tmp/x9615-run

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-9615-depth15-phase-floor/verify.cpp \
  -o /tmp/x9615-verify

/tmp/x9615-run --check-results \
  experiments/X-9615-depth15-phase-floor/results/canonical.json

/tmp/x9615-verify \
  experiments/X-9615-depth15-phase-floor/results/canonical.json
```

Expected output:

```text
X-9615 canonical results match
all independent X-9615 depth-15 phase checks passed
```
