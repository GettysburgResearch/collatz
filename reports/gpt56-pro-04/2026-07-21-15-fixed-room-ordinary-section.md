# Agent report — fixed-room ordinary-section theorem attempt

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Requested objective

Attempt the decisive theorem that no infinite itinerary can simultaneously:

1. supply the symbolic novelty required by ordinary-code repetition rigidity;
2. preserve ordinary integrality at every shift;
3. remain in the bounded real companion section;
4. avoid both repetition-height and reciprocal carry-height contradictions.

The universal contradiction did not close. The session did close one misleading route, derive an exact ordinary-section equivalence, discover an exact dual minimum formula, and compute the exact first nontrivial depth-46 survivor above `2^227`.

## 1. The two criticality constants are one mechanism

PR #20's repetition obstruction and PR #16's reciprocal phase-carry obstruction contain the same constant

\[
\kappa
=
\frac1{\log_{64}81-1}
=
\frac{\log64}{\log(81/64)}.
\]

The initial hypothesis was that satisfying both constraints might overspend one information budget. Exact reconstruction shows otherwise.

## 2. `L-9311`: repetition is an orbit-difference zero-carry chain

Let `A_k` be the ordinary integral tail orbit of a hypothetical survivor. If equal length-`ell` factors begin at `r<t`, define

\[
D_i=A_{r+i}-A_{t+i}.
\]

During the common factor,

\[
\boxed{64D_{i+1}=81D_i.}
\]

Hence

\[
D_i=64^{\ell-i}81^iu
\]

for one nonzero integer `u`. Therefore

\[
64^\ell
\le A_t-A_r
<
(81/64)^{t-r}A_r,
\]

which gives

\[
\ell
<
(\log_{64}81-1)(t-r)+\log_{64}A_r.
\]

This independently reconstructs PR #20's local repetition theorem. The repetition and reciprocal-carry inequalities are two completion-height bounds on different zero-carry cocycles.

`R-9302` records the method closure: matching `kappa` values are not opposing budgets, so their numerical comparison cannot prove nonexistence.

## 3. `T-9313`: the fixed-room invariant

For a hypothetical ordinary room

\[
A=\Phi(\varepsilon),
\]

let `A_j` be its ordinary tail after `j` digits and define

\[
P_j
=
17\sum_{t=0}^{j-1}
\varepsilon_t81^{j-1-t}64^t.
\]

Iteration gives

\[
\boxed{81^jA=64^jA_j+P_j.}
\]

The quotient is the same fixed integer `A` at every depth.

Reverse the past word. Its triadic coordinate lies in `C_j`, and `A_j mod81^j` is exactly that coordinate. The future word simultaneously puts `A_j` in the infinite survivor attractor.

The bounded real companion gives

\[
\boxed{
(81/64)^j(A-1)+1
\le A_j
\le(81/64)^jA.
}
\]

Conversely, coherent ordinary integers satisfying the fixed-room equations reconstruct the tail recurrence and the original survivor series in `Z_2`. This is an exact equivalence.

## 4. Exact finite duality

Let

\[
m_j=\min(C_j\setminus\{0,1\})
\]

and

\[
M_j=\min(R_j\setminus\{0,1\}).
\]

For `c in C_j`, reverse its low-to-high word into chronological survivor order. The fixed-room formula gives

\[
A(c)
=
\frac{64^jc+P_j}{81^j}
=
c(64/81)^j+X_j,
\]

where the nontrivial finite real prefix satisfies

\[
0<X_j<1.
\]

Since `A(c)` is integral,

\[
\boxed{A(c)=\lceil c(64/81)^j\rceil.}
\]

The word maps are bijective, so

\[
\boxed{
M_j
=
\left\lceil m_j(64/81)^j\right\rceil.
}
\]

This is an exact minimum-survivor identity, not merely a lower bound.

The sequence `M_j` is nondecreasing because `R_(j+1) subset R_j` as ordinary finite survivor sets. The ordinary-section problem is equivalent to

\[
\boxed{M_j\to\infty.}
\]

## 5. `X-9303`: exact depth-46 minimum

The class set is a modular subset-sum system. `X-9303` uses a `23+23` meet-in-the-middle split:

1. enumerate and sort `2^23` exact right-half sums;
2. scan `2^23` left-half sums in Gray-code order;
3. test the nearest admissible modular complement on both sides of the wrap point;
4. exclude the trivial classes `0,1`;
5. reconstruct a minimizing word;
6. reverse it into chronological order;
7. reconstruct the starting room;
8. replay all 46 survivor steps;
9. compare independently with full enumeration through depth 16.

The exact triadic minimum is

\[
m_{46}
=
13995580641937679806861747515838198945935546006963182029787326398035667034.
\]

A low-to-high minimizing word is

```text
1101110101010000110011100000101001011110110110
```

and the chronological word is

```text
0110110111101001010000011100110000101010111011
```

The exact starting room is

\[
\boxed{
M_{46}
=
275396778563393867136351926990265018601508986973296055235244496661568
>2^{227}.
}
\]

Direct replay ends at the class `m_46` after exactly 46 valid induced steps.

Frozen digest:

```text
f2c4dd9b0c436c9450c03424b27d80366865f54bb8c286944a35047d0662c9bc
```

## 6. `T-9314`: bounded ordinary-section exclusion

Every infinite ordinary survivor belongs to every finite survivor set `R_j`. Therefore it is at least `M_46` unless it is one of the two trivial rooms `0,1`.

Consequently there is no nontrivial ordinary survivor room in

\[
2\le A\le2^{227}.
\]

This is a genuine ordinary-section exclusion, not a finite-set discrepancy consequence. It remains finite.

## 7. Why the universal theorem remains open

The exact remaining statement is

\[
M_j\to\infty.
\]

The computation gives one large monotone checkpoint but not asymptotic divergence. A bounded nondecreasing sequence of finite minimum survivors would eventually stabilize, producing one fixed ordinary room with arbitrarily long valid prefixes and hence an infinite itinerary.

No current invariant rules out that stabilization universally.

The likely sharper object is the least **extendible** depth-`j` survivor: finite validity alone includes words with no infinite continuation.

## 8. Files added

- `research/adelic-cusp/claims/L-9311-orbit-difference-carry-duality.md`
- `research/adelic-cusp/claims/T-9313-fixed-room-past-future-equivalence.md`
- `research/adelic-cusp/claims/T-9314-bounded-ordinary-room-exclusion.md`
- `research/adelic-cusp/claims/R-9302-naive-complexity-carry-incompatibility.md`
- `research/adelic-cusp/ORDINARY_SECTION.md`
- `experiments/X-9303-fixed-room-cantor-minimum/README.md`
- `experiments/X-9303-fixed-room-cantor-minimum/run.py`
- `experiments/X-9303-fixed-room-cantor-minimum/results/canonical.json`
- this report

Updated:

- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/claims/Q-9302-two-place-room-cusp.md`
- PR #16 metadata and cross-program comments

## 9. Claim effects

Added:

- `L-9311` — `PROPOSED`;
- `T-9313`, `T-9314` — `PROPOSED`;
- `R-9302` — `PROPOSED`;
- `O-9303`, `X-9303` — internal exact finite computation.

No issue-#4 or PR #20 claim is promoted or altered.

## 10. Review priorities

1. Reconstruct the fixed-room identity and converse in `T-9313`.
2. Check the reversed-word indexing in the `C_j` congruence.
3. Check the exact ceiling transform `A(c)=ceil(c(64/81)^j)`.
4. Check that this transform preserves minima.
5. Replay `X-9303`, especially modular wrap handling and exclusion of `0,1`.
6. Reconstruct the direct survivor replay at depth 46.
7. Reconstruct `L-9311` and confirm the local repetition inequality.
8. Confirm that `R-9302` refutes only the naive comparison route.

## 11. Highest-value next theorem

Prove that the monotone exact minima

\[
M_j=\min(R_j\setminus\{0,1\})
\]

tend to infinity.

A promising route is to classify extendible children of low finite survivors and prove that every bounded branch eventually dies. An equivalent active-cylinder route is to prove that the appended nested-cylinder blocks cannot become eventually zero along a positive coherent itinerary.

## Status boundary

This session did not prove universal ordinary-section nonintersection. It did derive the exact equivalence and minimum duality, close one misleading proof route, and compute an exact ordinary-section exclusion through `2^227`.

No ordinary survivor, divergent Collatz seed, nontrivial cycle, or resolution is claimed.
