# Session report — Lane-A critical-boundary attack

**Agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Issue:** #78  
**Draft PR:** #80  
**Branch:** `agent/gpt56-positive-02/least-counterexample-global`  
**Date:** 2026-07-31

## Requested target

Exclude a positive ordinary orbit satisfying

\[
D_k\ge0\quad\forall k,
\]

\[
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O_n(1),
\]

\[
\max_{k\le K}3^{D_k}\gtrsim_nK^{8/9},
\]

and

\[
\#\{k<K:D_k\le H\}=O_{n,H}(K^{1/9})
\quad\forall H.
\]

## Outcome

The full ordinary orbit was **not excluded**.

The pass proved that the displayed scalar profile is internally consistent even after requiring:

- one genuine binary parity word;
- all-prefix coefficient supercriticality;
- exact finite parity-cylinder realizability at every depth;
- one compatible `2`-adic completion;
- the rational critical-density condition `D_k/k -> 0`.

Therefore no valid proof can derive ordinary nonexistence from those scalar estimates alone.

This is recorded as `R-6501`, with explicit prefix counts

\[
q_k=\left\lceil
{\log2\over\log3}k
+{8\over9}\log_3\left({k+2\over2}\right)
\right\rceil.
\]

The increments are exactly binary because the defining real increment is positive and strictly below one.

## New ordinary-only consequences

### `L-6503` — tail-minimum ladder

Every positive divergent orbit generates infinitely many starts `h_i` with infinite ordinary stopping time and

\[
h_i<h_{i+1}\le(3h_i+1)/2.
\]

Their coefficient-stopping depths tend to infinity. Thus a Lane-A orbit is not an isolated exceptional integer; it creates a multiplicatively `3/2`-syndetic ladder of increasingly deep infinite-stopping starts.

### `T-6506` — source-qualified critical density

López--Stoll Theorem 1 implies that a rational `2`-adic integer with a divergent noncyclic orbit must satisfy

\[
\liminf q_k/k={\log2\over\log3}.
\]

Hence an ordinary Lane-A orbit obeys

\[
\liminf D_k/k=0.
\]

Combining this with the exact correction product gives a subsequence

\[
\log T^k(n)=o(k).
\]

So the surviving path has logarithmically growing mean bank and density-one bank escape, yet returns arbitrarily late to subexponential physical height in elapsed time.

### `L-6504` — simultaneous canonical-boundary collapse

At the subexponential cusp times, the actual finite parity word has canonical representatives

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

This identifies the exact remaining Lane-A object: an all-prefix-supercritical exponent code occupying the simultaneous zero-rate `2`-adic source / `3`-adic endpoint corner.

## Latest literature digested

1. **López--Stoll, arXiv:2101.12747.** Supplies the rational critical-density equality used in `T-6506`.
2. **Kramer, arXiv:2607.10041.** Supplies a `2`--`3`--infinity diagnostic and necessary zero residue rates for fixed ordinary roots. It does not prove the missing canonical-boundary lower bound.
3. **Chang, arXiv:2603.25753.** Closes map-level balance but explicitly leaves pointwise orbit-level one-bit mixing open.
4. **Rozier--Terracol, arXiv:2502.00948v5 / Discrete Mathematics 349 (2026), 115167.** Remains the live paradoxical-sequence source; global finiteness remains conjectural.
5. **Angeltveit, arXiv:2602.10466.** Improves finite verification and necessary constraints, not the one exceptional orbit.

## Exact first invalid inference

The failed implication is now explicit:

```text
finite compatibility
+ compatible 2-adic path
+ D_k >= 0
+ mean D >= (8/9) log_3 k - O(1)
+ polynomial coefficient records
+ sparse fixed-band returns
+ critical liminf drift
--------------------------------
no positive ordinary realization.
```

`R-6501` satisfies every premise except the unproved ordinary realization. The missing statement is exactly the latter.

## New exact closing target

Prove a canonical-boundary uncertainty theorem for all-prefix-supercritical words. One sufficient form is:

\[
\max\left\{
{\log r(w)\over |w|},
{\log s(w)\over q(w)}
\right\}\ge\varepsilon
\]

for one fixed `epsilon>0` and every sufficiently long word.

`L-6504` shows that an ordinary Lane-A path would violate this along a subsequence.

A weaker lower envelope incompatible with simultaneous zero rates would also suffice.

## Candidate status

None. No Collatz proof, counterexample, positive cycle, or `K-####` object is claimed.

## Files added in this wave

```text
research/least-counterexample-global/claims/L-6503-tail-minimum-syndetic-ladder.md
research/least-counterexample-global/claims/T-6506-critical-density-subexponential-cusp.md
research/least-counterexample-global/claims/L-6504-two-boundary-cusp-subsequence.md
research/least-counterexample-global/claims/R-6501-scalar-profile-does-not-imply-exclusion.md
reports/gpt56-positive-02/2026-07-31-78-lane-a-critical-boundary.md
```

The README, inventory, literature audit, and `Q-6501` were updated accordingly.

## Recommended next action

Attack only the simultaneous canonical-boundary corner. More scalar drift, record, or density estimates cannot close Lane A without a theorem tying them to the same finite ordinary source.
