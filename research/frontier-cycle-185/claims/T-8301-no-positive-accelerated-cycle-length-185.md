# T-8301 — No positive accelerated Collatz cycle has odd length 185

Claim ID: `T-8301`  
Title: Ordered-jump decoding excludes every nontrivial positive accelerated cycle of odd-state length 185  
Status: `PROPOSED`  
Authoring agent: `gpt56-cycle-02`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: Hercher's theorem that every nontrivial positive cycle has at least 92 local minima; branch-qualified `PR13/LIT-KTHM-0052` for the same dependency normalization and the length-184 frontier  
Scope: positive odd accelerated `3n+1` cycles with exactly 185 odd states  
Related counterexample candidates: none

## Statement

Let

\[
S(x)=\frac{3x+1}{2^{\nu_2(3x+1)}}
\]

be the accelerated Collatz map on positive odd integers. There is no nontrivial positive periodic orbit of `S` with exactly 185 odd states.

## Definitions

For a valuation word

\[
w=(a_0,\ldots,a_{184}),\qquad a_i\ge1,
\]

put

\[
A_j=\sum_{i<j}a_i,\qquad A=A_{185},
\]

and

\[
C(w)=\sum_{j=0}^{184}3^{184-j}2^{A_j},\qquad
D(w)=2^A-3^{185}.
\]

A positive cycle necessarily satisfies

\[
D(w)>0,\qquad C(w)=n_0D(w)
\]

for a positive integer `n_0`.

At a positive odd state greater than one,

```text
a_i=1  <=> the next odd state is larger,
a_i>=2 <=> the next odd state is smaller.
```

Call these letters ascents `A` and descents `D`.

## 1. Complete skeleton classification

By the external dependency, a nontrivial positive cycle has at least 92 local minima. A cyclic word of length 185 has at most 92 local minima because local minima and maxima alternate. Hence a hypothetical cycle of this length has exactly 92 local minima.

Its cyclic ascent/descent word therefore has exactly 184 changes and one equal adjacent pair. Up to cyclic rotation, precisely two skeletons remain.

### `AA` — unique doubled ascent

\[
w_{AA}=(1,1,b_0,1,b_1,\ldots,1,b_{91}),\qquad b_i\ge2.
\]

There are 93 ascents and 92 descents. Write

\[
b_i=2+c_i,\qquad c_i\ge0,
\qquad H=\sum_i c_i.
\]

The base valuation total is

\[
A^{(0)}_{AA}=277.
\]

Since

\[
2^{293}<3^{185}<2^{294},
\]

positivity of `D` forces

\[
H\ge17.
\]

### `DD` — unique doubled descent

\[
w_{DD}=(1,b_0,b_1,1,b_2,\ldots,1,b_{92}),\qquad b_i\ge2.
\]

There are 92 ascents and 93 descents. With the same notation, the base total is

\[
A^{(0)}_{DD}=278,
\]

and positivity forces

\[
H\ge16.
\]

These two families exhaust every possible positive length-185 cycle.

## 2. Ordered-jump identity

Fix either base skeleton. Let its variable descent positions be

\[
p_0<p_1<\cdots<p_{s-1},
\]

where `s=92` for `AA` and `s=93` for `DD`. Let `w^(0)` denote the word with every variable descent equal to two, and put

\[
C_0=C(w^{(0)}).
\]

For each variable position define its base suffix weight

\[
S_j=
\sum_{\ell>p_j}3^{184-\ell}2^{A^{(0)}_\ell}.
\]

The final variable is the final letter, so

\[
S_{s-1}=0.
\]

Every weak composition of the excess `H` is equivalently a nondecreasing sequence

\[
0\le j_0\le j_1\le\cdots\le j_{H-1}\le s-1,
\]

where the `r`th unit of excess is placed at variable `j_r`. Then

\[
\boxed{
C(w)=C_0+\sum_{r=0}^{H-1}2^rS_{j_r}.}
\tag{1}
\]

### Proof

Increasing one valuation at position `p_j` by one doubles every affine term strictly after that position, so its first incremental contribution is `S_j`. Apply the excess units in nondecreasing position order. Each earlier unit lies no later than the current one and has doubled the current suffix once. The `r`th incremental contribution is therefore `2^rS_(j_r)`. Summing proves (1). ∎

## 3. Strictly separated suffix valuations

For every nonfinal variable,

\[
\nu_2(S_j)=A^{(0)}_{p_j+1}.
\tag{2}
\]

Indeed, the first term in `S_j` has that valuation and every later positive term has larger valuation. Consequently the positive suffix valuations are strictly increasing with `j`.

This makes (1) losslessly decodable from its least `2`-adic term.

## 4. Unique multiplier decoder

Suppose a cycle exists and write

\[
C(w)=mD_H,
\qquad
D_H=2^{A^{(0)}+H}-3^{185},
\qquad m=n_0>0.
\]

Set

\[
R_0=mD_H-C_0.
\]

For `r=0,...,H-1`, if `R_r=0`, all remaining excess units must be assigned to the final variable, whose suffix weight is zero, and the decoder succeeds. Otherwise the first remaining term in (1) is uniquely least in `2`-adic valuation, so

\[
\nu_2(R_r)=r+\nu_2(S_{j_r}).
\tag{3}
\]

Equation (3) uniquely determines `j_r`. The decoder then requires the positions to be nondecreasing, subtracts

\[
2^rS_{j_r},
\]

and continues. An unavailable suffix valuation, a decreasing position, a negative remainder, or a nonzero terminal remainder proves that the multiplier cannot occur.

Thus each pair `(H,m)` has at most one candidate valuation word.

## 5. Uniform finite multiplier bounds

For fixed `H`, equation (1) gives

\[
C_0\le C(w)\le C_0+(2^H-1)S_0.
\]

Hence

\[
\left\lceil\frac{C_0}{D_H}\right\rceil
\le m\le
\left\lfloor\frac{C_0+(2^H-1)S_0}{D_H}\right\rfloor.
\tag{4}
\]

Writing `x=2^H`, the upper ratio has the form

\[
\frac{S_0x+(C_0-S_0)}{2^{A^{(0)}}x-3^{185}}.
\]

Its derivative in `x` has numerator

\[
-S_0 3^{185}-2^{A^{(0)}}(C_0-S_0)<0.
\]

Therefore the upper bound decreases with `H`. Exact integer evaluation at the first allowed height gives the uniform bounds

```text
AA: 1 <= m <= 539801,
DD: 1 <= m <= 566791.
```

The sharper lower bounds from (4) are used in the low-height scans.

## 6. Exact low-height scans

`X-8301` independently constructs both skeletons and exhausts every multiplier in (4) for

```text
AA: H=17,...,30,
DD: H=16,...,30.
```

No decoder succeeds.

The first scans are:

```text
AA, H=17: m=6,...,539801; 539796 multipliers; 0 solutions.
DD, H=16: m=10,...,566791; 566782 multipliers; 0 solutions.
```

All remaining displayed heights also have zero solutions. The canonical result records every stop reason, maximum decoder depth, and maximum inspected valuation.

## 7. One reference height controls every larger height

At reference height

\[
H_*=31,
\]

scan the full uniform multiplier ranges. Exact computation gives:

```text
AA:
  all 539801 multipliers fail by an unavailable suffix valuation;
  maximum decoded depth 18;
  maximum inspected remainder valuation 36.

DD:
  all 566791 multipliers fail by an unavailable suffix valuation;
  maximum decoded depth 19;
  maximum inspected remainder valuation 38.
```

For every `H>31`,

\[
D_H-D_{31}=2^{A^{(0)}}(2^H-2^{31})
\]

is divisible by

```text
AA: 2^(277+31)=2^308,
DD: 2^(278+31)=2^309.
```

Fix a multiplier in the appropriate uniform range and compare its decoder at `H` with the reference decoder. Initially their remainders differ by a multiple of `2^308` or `2^309`. As long as the reference decoder has not failed, both remainders have the same valuation because the reference valuations are at most 36 or 38. They therefore select the same suffix index and subtract the same term, preserving the high-divisibility difference. Induction carries the reference decoder to the same unavailable-valuation failure at height `H`.

Hence every height above 31 is excluded.

The low scans and the two stability classes cover all allowed excess heights. Therefore neither exhaustive skeleton admits a cycle. **QED**

## Dependency audit

- Hercher's local-minimum theorem supplies only the lower bound of 92 local minima.
- The cyclic skeleton classification is elementary and complete at length 185.
- The cycle equation is the standard accelerated affine identity.
- `X-8301` supplies the exact finite multiplier scans and frozen reference valuations.
- No unproved inference from finite depth to infinite height is made; the final passage is the explicit divisibility stability argument above.

## Gap audit

- This theorem excludes exactly odd-state length 185. It says nothing directly about length 186 or larger lengths.
- The external local-minimum theorem must be checked independently at its exact stated parameter.
- The theorem is computer-assisted at the finite scan step; the source and frozen output are committed.
- A zero result is not a counterexample. The project objective remains a positive cycle or an ordinary divergent orbit.

## Adversarial tests

- `run.py` checks the ordered-jump identity against direct affine constants on deterministic boundary assignments.
- `verify.py` is an independent implementation that does not import `run.py`; it checks 6,000 deterministic random ordered-jump instances and reconstructs every direct and reference scan.
- Both implementations require the reference failures to consist solely of unavailable suffix valuations before accepting the stability certificate.

## Remaining uncertainty

The arithmetic and decoder appear complete, but independent repository review is still required before status promotion.

## Suggested next attack

Apply the ordered-jump compiler to length 186. At that length the 93-minimum perfectly alternating skeleton and the 92-minimum one-defect skeletons form a finite cyclic family. Search them for an exact positive hit before converting another zero census into an exclusion theorem.
