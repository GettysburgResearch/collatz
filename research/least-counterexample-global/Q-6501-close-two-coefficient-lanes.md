# Q-6501 — Close both least-counterexample coefficient lanes

**Claim ID:** `Q-6501`  
**Title:** Eliminate the zero-rate supercritical cusp and every finite first-crossing cylinder  
**Status:** **OPEN / GLOBAL BLOCKER**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `D-6501`, `L-6501`--`L-6504`, `T-6501`--`T-6506`, `R-6501`; branch-qualified PR #76--#77

## Exact target

After independent reconstruction of the branch-qualified dependencies, prove both statements below.

# Lane A — exclude the zero-rate, sparse-return, supercritical ordinary cusp

There is no positive integer `n` whose actual shortcut-Collatz orbit satisfies

\[
D_k=q_k-{\log2\over\log3}k\ge0
\qquad(k\ge0).
\tag{A}
\]

The current packet proves that any such ordinary orbit must satisfy all of the following.

## 1. Divergence and correction control

\[
T^k(n)\to+\infty,
\]

\[
P_k\le e^{7/9}k^{1/9},
\qquad
T^k(n)=n3^{D_k}P_k.
\]

## 2. Logarithmic mean bank and records

\[
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O_n(1),
\]

\[
\max_{k\le K}3^{D_k}
\ge {K^{8/9}\over ne^{5/3+o(1)}}.
\]

## 3. Sparse fixed-band returns

For every fixed `H`,

\[
\#\{k<K:D_k\le H\}=O_{n,H}(K^{1/9}),
\]

so `D_k -> infinity` in natural density one.

## 4. Critical relative recurrence

The source-qualified López--Stoll theorem forces

\[
\liminf_{k\to\infty}{D_k\over k}=0.
\]

Therefore there are arbitrarily late times with

\[
\log T^k(n)=o(k).
\]

The path has high logarithmic average bank but repeatedly approaches the zero linear-drift boundary.

## 5. Simultaneous canonical-boundary collapse

Along a subsequence of cusp times, the canonical parity-cylinder boundaries are

\[
r_k=n,
\qquad
s_k=T^k(n),
\]

with

\[
{\log r_k\over k}\to0,
\qquad
{\log s_k\over q_k}\to0.
\]

Thus the exact remaining arithmetic object is a sequence of all-prefix-supercritical words with simultaneous zero-rate `2`-adic source and `3`-adic endpoint representatives.

## 6. Infinite-stopping tail-minimum ladder

The same orbit generates tail minima

\[
h_0<h_1<h_2<\cdots,
\]

with

\[
h_{i+1}\le(3h_i+1)/2,
\]

infinite ordinary stopping time, and coefficient-stopping depths tending to infinity.

## What would close Lane A

Sufficient outcomes include:

1. a canonical-boundary uncertainty theorem proving that every sufficiently long all-prefix-supercritical word has a source or endpoint height rate bounded away from the simultaneous zero-rate corner;
2. a weaker quantitative lower bound incompatible with `L-6504`;
3. a pointwise orbit-mixing theorem forcing some coefficient-subcritical prefix on the same ordinary trajectory;
4. an inverse-tree/minimality theorem showing that the tail-minimum ladder creates a smaller counterexample;
5. a complete `2`--`3` product-formula obstruction for the canonical source/end pair.

## What does **not** close Lane A

`R-6501` constructs an explicit binary word satisfying

\[
D_k\ge0,
\quad
\text{mean }D\ge(8/9)\log_3k-O(1),
\quad
3^{D_k}\gg k^{8/9},
\]

with only finitely many visits to each fixed low band and with `D_k/k -> 0`.

Every finite prefix has positive ordinary representatives and the complete word has a compatible `2`-adic realization. Hence the scalar conditions, finite compatibility, and completion alone cannot imply exclusion. A proof must use ordinary canonical-boundary arithmetic.

# Lane B — exclude all finite first crossings

For every first-crossing parity word `w`, use the exact data of `L-6502`:

\[
x=r_w+2^j t,
\]

\[
T^j(x)=y_w+3^q t,
\]

\[
0\le t\le
H_w=\left\lfloor{y_w-r_w\over2^j-3^q}\right\rfloor.
\]

Prove that no member of this finite list can be a least positive counterexample.

Sufficient global outcomes include:

1. a uniform verified-range bound on all listed starts;
2. a cofinal lower bound on `r_w` exceeding the paradoxical ceiling;
3. a theorem forcing one later descent for every listed start;
4. for periodic words, complete whole-denominator cycle nondivisibility and exact replay.

`T-6505` already excludes bounded-bank, low-complexity cofinal crossing families. PR #83 closes a one-pulse near-return class. High-bank, high-complexity, multi-pulse and mixed-block families remain.

Another finite set of crossing lengths or continued-fraction cells does not close Lane B.

# Why this is exhaustive

If Collatz is false, choose a least positive counterexample.

- If its coefficient never crosses below one, it belongs to Lane A.
- If the crossing is finite, its first crossing belongs to Lane B.
- If the orbit is eventually periodic, rotate the nontrivial positive cycle to its minimum; one period belongs to Lane B.

There is no third positive ordinary failure mode.

# What would count as a proof of Collatz

A complete packet must provide:

1. independent reconstruction of the imported least-counterexample and coefficient-stopping gates;
2. an unconditional exclusion of the zero-rate Lane-A cusp;
3. an unconditional cofinal exclusion of Lane B, including positive cycles;
4. no invocation of a prescribed parity directive or nonordinary completion;
5. exact handling of every positive integer above the verified range.

# Current status

The four scalar Lane-A estimates requested in the latest attack have **not** been converted into a contradiction. `R-6501` proves that they cannot be sufficient by themselves.

The genuine progress is that ordinary Lane A is now localized to one sharper boundary:

```text
all-prefix nonnegative real drift
+ logarithmic mean bank
+ sparse fixed-band returns
+ critical liminf drift
+ zero-rate canonical source
+ zero-rate canonical endpoint.
```

No theorem currently proves that boundary empty. No proof of Collatz and no counterexample is claimed.
