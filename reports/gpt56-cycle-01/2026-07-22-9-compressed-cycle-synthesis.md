# Session report — compressed positive-cycle synthesis

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Date:** 2026-07-22

## Starting hypothesis

A full unconditional Collatz disproof is most plausibly obtained from an integer-first finite certificate: a nontrivial positive cycle or a finite automaton sanctuary. The session therefore prioritized proof-producing finite objects instead of extending unqualified 2-adic or finite-prefix survivors.

## Repository state read

The startup audit read the root operating protocol, the global counterexample map, the `99xx` foundations packet, the active centered/H/collision branches, and issue #9. The strongest reusable inputs were:

- the reviewed affine cycle equation and product formula `L-9905`;
- the proposed exponent-window analysis `L-9912`;
- the exact warning that symbolic compatibility does not imply ordinary integrality;
- the global map's identification of positive cycles and finite sanctuaries as the shortest finite-certificate routes.

## Approaches attempted

### 1. Full positive-cycle windows

A proof-producing meet-in-the-middle enumerator was built from the exact affine monoid. It derives every `(m,K)` window with integer inequalities and covers every positive exponent composition in those windows.

**Result:** all windows through `m=27` are empty. This becomes `T-8602` / `X-8601`.

### 2. First upper-convergent low-complexity shape

At `(m,K)=(41,65)`, exact searches covered all binary valuation words and every word with one exponent above two.

**Result:** zero divisibility matches among `35,548,596,168,868` words. This is `X-8602`; unrestricted compositions remain open.

### 3. Compressed negative-cycle/refund grammars

Exploratory exact searches combined the known negative-cycle valuation blocks with exponent-2 refund blocks. Complete frozen subfamilies included:

- 145,008,513 interleavings of 35 seven-term negative-cycle blocks and 8 refund blocks;
- 164,068,870,680 interleavings of 10 two-term negative-cycle blocks, 10 seven-term blocks, and 7 refund blocks;
- 348,024,877,200 interleavings in the `(m,K)=(94,149)` refinement with token counts `(12,9,7)`.

All had zero divisibility matches. These runs were exploratory and are not promoted to theorem files in this packet because their grammar selection is ad hoc.

### 4. Periodic congruence sanctuaries

The finite-modulus search led to a general proof rather than a larger census. Sink-component period halving reduces every invariant modulus to its odd part. On the odd part, the forward affine generators `2x` and `3x+1` provide:

- a translation-by-one commutator on the factor coprime to six;
- a universal reset to `1` on the power-of-three factor.

**Result:** every nonempty bare congruence sanctuary contains `1`. This becomes `T-8601`.

### 5. Lift-qualified centered survivor continuation

The prior class-6 correction was extended from depth 46 to depth 48. The exact least class-6 state at depth 48 is

```text
2058345563356755928201470321791581267096577184563271133449970057619956673
```

with chart word

```text
101101101001001000000011000010001101000010110100
```

Its lifted positive Collatz seed is

```text
9807411213641013540254064474418710743224867761742644812320445568659793551
```

It exits after 48 chart blocks and reaches `1` after 1,425 shortcut steps. This is exact finite evidence and is not a counterexample.

### 6. Autoconjugacy probe

The parity-complement autoconjugacy was evaluated modulo `2^128` for negative starts through `-1,000,000`. No image stabilized to a positive integer below `2^64`. This is a bounded probe only and was not committed as a claim.

## New results

- `T-8601` (`PROPOSED`): no nonempty bare periodic congruence sanctuary can avoid `1`.
- `T-8602` (`PROPOSED`): no nontrivial positive Syracuse cycle has at most 27 odd terms.
- `X-8602` (`EMPIRICAL`, exact finite): zero low-complexity matches at `(41,65)` across 35.5 trillion words.

## Candidate counterexamples

None.

No object found in this session satisfies all of:

1. one explicit positive integer;
2. exact physical Collatz transitions for every time;
3. a proof of nontermination, divergence, or nontrivial periodicity.

## Failed approaches and what they rule out

- Raw extension of centered survivor depth produced another terminating seed.
- Bare periodic congruence sanctuaries are now ruled out in full generality.
- Small and medium positive-cycle windows through 27 odd terms are exhausted.
- Several natural negative-cycle/refund compressed grammars are exhausted, but only within their declared token counts.

## Potential errors requiring review

- `T-8601`: independently reconstruct the sink-period-halving step and the order of composition in the affine commutator.
- `T-8602`: independently implement the left/right composition join rather than copying the submitted code.
- Confirm that the repository's `m` nomenclature stays separated from external local-minimum counts.

## Files changed

- `research/compressed-cycle-synthesis/README.md`
- theorem/experiment files under `research/compressed-cycle-synthesis/claims/`
- `experiments/X-8601-cycle-window-exhaustion/`
- `experiments/X-8602-65-41-low-complexity/`
- this report

## Recommended next actions

1. Independently review `T-8601`; if correct, remove every bare modular sanctuary synthesis lane.
2. Independently replay `X-8601` and promote `T-8602` only after a fresh implementation agrees.
3. For a constructive cycle search, use a grammar with a compositional proof certificate and enough unbounded state to escape fixed low-complexity token families.
4. For a sanctuary, retain genuine canonical-word boundary memory; a residue modulus alone is impossible.
5. Continue class-6 work only through a theorem about eventual appended-block stabilization, not by treating another finite depth as evidence of an infinite orbit.

## Organizational improvement

Finite counterexample searches should publish two separate counters:

- the number of conceptual objects covered;
- the number of stored or streamed meet-in-the-middle states.

This prevents accidental reporting of `2^m` when a fixed-total constraint reduces the actual word count, and makes completeness audits much easier.
