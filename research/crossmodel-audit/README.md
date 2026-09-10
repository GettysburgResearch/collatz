# Cross-model audit of recent Claude / Opus / Fable work

**Agent:** `gpt56-crossmodel-audit-01` (`GPT-5.6 Pro`)  
**Issue:** #71  
**Date:** 2026-07-27  
**Status:** adversarial audit packet; native claims retain their source-branch status unless an explicit correction says otherwise

## Frozen sources

```text
claude-01 symbolic-rewrite packet
  branch: claude/collatz-migration-math-osr370
  SHA:    407a788972a72da2fde59c19e9446e02647cc4f4

fable-01 diagonal-foundry and solution-cone packet
  branch: claude/collatz-repo-exploration-m2e5vp
  SHA:    0888a211f2703f5d3082e60fcbd0e8002b4b4650

fable-02 / Claude Opus foundations packet
  branch: claude/subagent-spawn-limits-ihpcc2
  SHA:    2cb80b4629ebfde5c8aaa3433c38e1382ea956b7
```

Model provenance was used only to locate the work. Every verdict below is based on the statement, proof, declared dependencies, and reproducible artifacts.

## Main findings

1. **Claude `L-0020` has a real proof gap but a clean repair.** The submitted proof averages reciprocal phases and silently drops the exact reciprocity error in the true Fourier phases. `L-7701` restores a fully exact block estimate with constant `7/10`, which is still strong enough for the intended frequency-block interface.
2. **Claude `T-0030` is not established as written.** It cites the gapped `L-0020`, routes through a now-superseded historical density-one assembly, and compresses downstream fair-window/minimal-survivor consequences that require their own review. The repaired block input is available; the complete assembly remains pending reconstruction.
3. **Fable foundry `T-9604` loses the diagonal.** Membership of a word in the unpaired family `{E(u0^infinity)}` does not prove that the same `u` is the binary expansion of the integer whose parity word was obtained. `L-7702` gives the exact paired graph criterion. The literal claim that this family is countable for every operator class is also false unless the class itself is countable.
4. **The solution-cone theorem files are better than their index.** `T-9703`, the actual finite-cardinality version of `T-9704`, `L-9705`, and the corrected `L-9708` reconstruct. But `CONE.md` drops the finiteness caveat from the cycle/component count and repeats the pre-correction `l2` slogan. `R-7702` records the documentation correction.
5. **Fable foundations contain substantial valid work.** The least-root extraction theorem, elementary cycle equations, the main `F=10^6` length-floor arithmetic, and the `L-9927` closure sieve survive this pass. `X-7701` independently reproduces the `10^6` floor, `m*(10^6)=2966`, the small `m=7..14` cycle census, and the complete 166-value `L-9927` list.
6. **`L-9918` overreads Parseval.** Its exact mean-square identities are correct. They do not imply that a Fourier sum is typically of order `sqrt(R)` or that `O(1)` values can occur only on density `O(1/R)`. The complete residue group is an exact counterexample. `R-7703` narrows the conclusion to the valid no-slack statement.
7. **Same-packet `PROVED` is not mislabelled under repository rules.** It denotes initial detailed review, not cross-model independent verification. The foundations packet states this boundary. Large enumerations and memory-bound phase-floor certificates therefore remain neutrally pending separate replay in this packet.
8. **Prior-art correction:** Fable `L-9918.1` already contains the architecture-wide bounded-least-root extraction dichotomy later rederived in `T-7801`. The latter must cite it branch-qualifiably; its signed single-chain packaging and expanding-affine countermodel remain distinct contributions.

## Audit boundary

This was a wide portfolio audit with deep reconstruction of the highest-impact global chains. It was not a byte-for-byte replay of every experiment or a line-by-line proof review of all 27 foundation claims. The permanent matrix names every deeply reviewed, partially replayed, and still-pending group explicitly.

No Collatz counterexample is claimed.
