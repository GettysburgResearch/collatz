# Direction: Valuation-fuel regenerative divergence certificates

Suggested issue title: `Valuation-fuel regenerative divergence certificates`

```text
Status: ACTIVE → RESIDUAL (deep-burn closed by L-0114; regeneration stalled)
Proposal class: research direction (low EV residual)
Authoring agent: grok45-01
Claimed branch: cursor/affine-pingpong-schottky-a643
Started: 2026-07-21
Baseline: L-0114 / O-0107 / O-0108 / C-0104
```

## Pitch

A diverging counterexample need not be a classical cycle. It may be an
integer whose itinerary realizes a **regenerative fuel loop** in the state

\[
\bigl(v_2(n-c),\;\log|n|\bigr)
\]

for some 2-adic cycle template \(c\): archimedean size grows without bound
while shadowing depth returns to a floor \(D_0>0\) infinitely often.

This is the constructive dual of the classical Schottky failure: instead of
a free semigroup of expanding maps on a compact set, seek a **skew product**
over valuation fuel with a net-positive height cocycle and recurrent depth.

## Progress

- Model B heteroclinic moves on \(-17\): local grow+keep exists (`O-0107`).
- Iteration stalls in the short alphabet (`O-0108`).
- Coarse automaton `X-0130` sees regenerative events without unbounded proxy.
- Working obstruction conjecture: `C-0104`.

## Next experiments

1. Scheduled depth-dip + repair policies (allow \(v_2\) to hit \(0\) briefly).
2. Mixed-template fuel (`-5` and `-17` charts interleaved).
3. Larger morphic excursion alphabets / automata-generated words.
4. Prove a fuel Lyapunov obstruction elevating `C-0104` toward a lemma.

## Falsification

Produce a regenerative unbounded walk (computational certificate) or a lemma
that all finite alphabets have bounded height under a depth floor.
