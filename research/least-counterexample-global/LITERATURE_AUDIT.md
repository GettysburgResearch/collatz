# Latest-literature audit for the least-counterexample proof attack

**Agent:** `gpt56-positive-02`  
**Date:** 2026-07-31  
**Issue:** #78  
**Status:** source-positioning audit; no source theorem is promoted automatically

## 1. Rozier--Terracol is the live paradoxical-sequence source

Olivier Rozier and Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948v5, now has journal reference

```text
Discrete Mathematics 349 (2026), 115167.
```

Its relevant contributions are:

- the exact distinction between coefficient contraction and actual descent;
- the paradoxical-sequence framework;
- harmonic-mean restrictions on paradoxical segments;
- the observation that a counterexample with infinite stopping time generates infinitely many paradoxical segments;
- the conjectural finiteness of nontrivial paradoxical behavior.

The paper does **not** prove that paradoxical sequences are finite. Therefore it does not close Lane B.

Native `T-6502` uses the same exact correction product, but adds the ordinary distinct-source specialization needed by a least-counterexample or one-period cycle segment.

## 2. The May 2026 Niu note is withdrawn

Tong Niu, arXiv:2605.13886, is marked withdrawn in version 2. The withdrawal comment says that Rozier--Terracol v4 already contains the relevant enumeration and seven `(j,q)` pairs, and that the additional mediant observation follows routinely from their data.

Accordingly:

```text
arXiv:2605.13886 is not used as an independent load-bearing theorem.
```

Any useful parity-cylinder formula is reconstructed directly or cited to Terras/Everett/Rozier--Terracol instead.

## 3. Angeltveit improves finite verification, not exceptional-orbit elimination

Vigleik Angeltveit, arXiv:2602.10466, gives a faster exact algorithm for verifying all starts below `2^N`, with less than a factor-two additional running time per added bit according to the abstract.

PR #76 also imports an all-prefix ballot/descent constraint from the paper. That constraint is valuable for narrowing a least counterexample, but it remains a necessary condition. A finite verification algorithm, however efficient, does not by itself prove that one unbounded exceptional orbit cannot exist.

The source theorem and the repository specialization should be independently reconstructed before status promotion.

## 4. Chang isolates an orbit-mixing statement but does not prove it

Edward Y. Chang, arXiv:2603.25753, proves a map-level balance theorem for compressed odd-to-odd residues and reduces the remaining bias to one orbit-level bit observed at sparse burst-ending times.

This is a useful localization:

```text
map-level residue balance is closed;
pointwise orbit-level mixing remains open.
```

A map-level count cannot be substituted for balance along the one orbit of a least counterexample. To become a Collatz proof, the paper's remaining one-bit mixing statement must be proved for every positive orbit or at least for a hypothetical least counterexample.

## 5. Almost-all descent theorems do not remove one least counterexample

Terras--Everett density theorems, Tao's almost-bounded theorem, and later quantitative refinements are genuine global distribution results. Their exceptional sets may have density zero while still containing one orbit. No inspected theorem couples those average bounds to the exact nested parity cylinders of a least counterexample strongly enough to force emptiness.

They may become decisive only after an architecture-specific statement turns one counterexample into too many independent exceptional integers.

## 6. Current repository frontier

The newest positive-direction repository work is issue #75 and draft PRs #76--#77:

```text
least counterexample:
  tau = infinity and the orbit tends to +infinity,

or

  finite first coefficient crossing
  tau >= 217,976,794,617.
```

The present packet advances that frontier without adding a finite search:

- `L-6501`: ordinary distinctness and prime-to-six arithmetic bound the total odd-step correction by `e^(7/9) k^(1/9)`;
- `T-6501`: all-time supercritical coefficient records must grow at least as `r^(8/9)` at record times;
- `T-6502`: every acyclic no-descent crossing satisfies a cofinal logarithmic harmonic window;
- `L-6502`: every first-crossing word has a complete exact finite list of ordinary no-descent starts.

## 7. Honest literature conclusion

No current source inspected on 2026-07-31 supplies a proof of Collatz or a theorem that silently closes either exhaustive lane.

The most credible remaining global targets are now:

1. **Lane A:** prove that an ordinary parity cylinder cannot sustain the unbounded coefficient-record law of `T-6501` forever;
2. **Lane B:** prove a cofinal lower bound on the canonical least representative `r_w`, or a uniform bound on the exact finite lists in `L-6502`;
3. **cycles:** force the complete positive-cycle denominator equality and replay, rather than accumulating proper-factor hits.

Map balance, almost-all descent, finite verification, and paradoxical-sequence enumeration are supporting inputs. None may be promoted to the missing pointwise theorem.
