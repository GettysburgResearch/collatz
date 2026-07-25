```text
Claim ID:            T-6121
Title:               Uniform density gate: every fixed macro-block chart has survivor density
                     at most 2^-N, and chart confinement forces rigid odd-step density
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        L-6105(a)
Scope:               ALL fixed macro-block charts of the shortcut Collatz map, not just the
                     six-branch chart
Related counterexample candidates: none; constrains all of them
```

## Definitions

A **(k,q) macro-block chart** is: an integer `q >= 1`, an integer `1 <= k <= q`, and a set
`W` of parity words of length `q` with exactly `k` ones, each beginning with `1`. A positive
odd integer `n` is *chart-legal for N steps* if its shortcut-Collatz parity word of length
`qN` is a concatenation `w_0 w_1 ... w_{N-1}` of words from `W` such that each block starts at
an odd number. Write `D = |W|`, `Q = 2^q`. The chart is **expanding** when `3^k > 2^q`.

The six-branch chart of T-6101 is the `(12,19)` chart with
`W = { (110)^(5-i) 1010 (110)^i : i = 0..5 }`, `D = 6`.

## Statement

**(a) Digit ceiling.** `D <= C(q-1, k-1) <= 2^(q-1)`. Hence for **every** macro-block chart

```text
D / Q  <=  1/2.
```

**(b) Survivor density.** The set of `n` that are chart-legal for `N` steps is a union of at
most `D^N` residue classes modulo `2^(qN)`, of natural density at most `(D/Q)^N <= 2^-N`. The
all-time chart-legal set in `Z_2` is a compact set of Haar measure `0` and Hausdorff dimension
at most `log D / (q log 2) <= 1 - 1/q < 1`.

**(c) Density rigidity.** If `n` is chart-legal for `N` steps then its parity word of length
`qN` has exactly `kN` ones. Hence the odd-step density of the trajectory equals `k/q` exactly
at every multiple of `q`, and deviates from `k/q` by at most `q/j` at step `j`. An all-time
chart-legal `n` therefore has an orbit whose odd-step density **converges to the fixed
rational `k/q` with discrepancy `O(1/j)`**.

**(d) Consequence for the positive program.** Being chart-confined is strictly stronger than
diverging. A divergent Collatz orbit need only satisfy
`liminf (odd-step density) > log 2 / log 3`; a chart-confined orbit must additionally pin the
density to one rational `k/q` forever, with bounded discrepancy, using only `D` of the
`C(q-1,k-1)` available blocks.

## Proof

**(a)** A parity word of length `q` with `k` ones and first letter `1` is determined by the
positions of the remaining `k-1` ones among the remaining `q-1` places, so there are
`C(q-1,k-1)` of them, and `W` is a subset. `C(q-1,k-1) <= sum_j C(q-1,j) = 2^(q-1)`. Dividing
by `Q = 2^q` gives `D/Q <= 1/2`. `QED`

**(b)** By the Terras bijection (L-6100 in T-6101), each word of length `qN` corresponds to
exactly one residue class mod `2^(qN)`; the legal words are among the `D^N` concatenations,
so at most `D^N` classes occur (exactly `D^N` when every concatenation is realisable at odd
numbers, as in the six-branch chart by L-6105(a)). Density and dimension follow, using
`D <= 2^(q-1)` for the final bound. `QED`

**(c)** Each block contributes exactly `k` ones in `q` letters, so after `N` blocks there are
`kN` ones in `qN` letters. For `j = qN + s` with `0 <= s < q`, the count of ones is between
`kN` and `kN + s`, so the density lies within `q/j` of `k/q`. `QED`

**(d)** Immediate from (c). `QED`

## Motivation

This is the uniform version of what X-6110 measured in one chart, and it is the reason the
same wall has been hit in every positive lane of this project. Three consequences worth
stating plainly:

1. **No chart can be "dense enough".** One might hope to rescue the positive program by
   enlarging the digit set until survivors become plentiful. (a) forbids it: the density is at
   most `1/2` per step for *any* macro-block chart, and for expanding charts it is far
   smaller. For `(12,19)` the maximum is `C(18,11)/2^19 = 31824/524288 = 0.0607`; the
   six-branch chart uses `6/524288 = 1.14e-5`, a further factor of `5304`.
2. **Every fixed chart is heuristically ordinarily empty.** The expected number of positive
   integers `<= X` surviving `N` steps is `X (D/Q)^N -> 0`, so the expected number of all-time
   seeds is `0` for every chart, and remains `0` after summing over the countably many charts.
   This is precisely the classical heuristic for the Collatz conjecture; a positive
   construction inside a fixed chart is fighting it head-on with no leverage.
3. **Chart-confined divergence is the wrong target.** By (d), the architectures pursued in
   this project ask for an orbit far more rigid than a mere counterexample. If a divergent
   orbit exists, there is no reason for it to have asymptotically constant odd-step density,
   let alone one realised by finitely many fixed blocks.

## Gap audit

* *Is (a) tight?* Not for expanding charts; there `k/q > log2/log3 = 0.6309`, so
  `C(q-1,k-1) ~ 2^((q-1)H(k/q))/sqrt(.)` with `H(0.63) = 0.9506 < 1`, and the density decays
  like `2^(-c q)` with `c > 0`. The uniform bound `1/2` is stated because it is unconditional
  and needs no asymptotics.
* *Does (b) prove emptiness?* **No.** Measure zero and dimension `< 1` are compatible with
  containing integers (e.g. the set `{n : n = 1 mod 4}` has positive density, but a Cantor set
  of measure zero such as the all-time legal set can still contain integers — nothing here
  excludes it). (b) supports a heuristic, not a theorem. This is the same honest gap as
  C-6111 and must not be overstated.
* *Does (c) assume blocks start at odd numbers?* Yes, by definition of the chart; T-6101's
  converse remark shows this is automatic once the next block begins with `1`.
* *Does this apply to non-block architectures?* Not directly. Charts with variable block
  length, or with a growing digit set, are outside the definition. That was the only escape
  route this theorem left open, and it has since been **closed by T-6131**, which proves the
  same conclusion for every divergence-targeting architecture whatsoever by bounding the
  dimension of the target set itself at `H_2(log2/log3) = 0.94996`.

## Adversarial tests

* `(12,19)`: `C(18,11) = 31824`, computed; `31824/2^19 = 0.0607` matches the claimed ceiling.
* Six-branch: predicted class count `6^N` at depth `N` matched exactly by enumeration at
  depths 1-4 (6, 36, 216, 1296) in X-6110.
* Predicted least-root growth `(Q/D)^N = 87381^N` versus measured `99380^N` over 16 exact
  levels: exponent agreement to 1.13%.

## Suggested next attack

Resolved: T-6131 shows no architecture escapes, by bounding the dimension of the divergence
target itself. T-6121 remains the sharper statement *within* fixed macro-block charts (its
`D/Q <= 1/2` and the exact `D^N` class count are what X-6110's search algorithm relies on),
but the universal statement to cite going forward is T-6131.
