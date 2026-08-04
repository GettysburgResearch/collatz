# Literature audit wave 9 — restricted minimal words and effective logarithmic closure

**Agent:** `gpt56-pro-03`  
**Date:** 2026-07-29  
**Issue:** #7  
**Draft PR:** #13  
**Counterexample status:** none

## Objective

Re-read the newest global-blocker and constructive work, locate external mathematics that directly bears on the remaining ordinary-root and full-denominator questions, derive exact native consequences, and push them without promoting any native theorem.

## Main result 1 — exact approximate-multiplication identification

The six-branch chart is exactly the Dubickas–Mossinghoff partial map

```text
x -> ceil(P*x/Q) when x mod Q lies in S;
STOP otherwise,
```

with

```text
P=3^12,
Q=2^19,
S={294912,331776,438784,297024,6472,466033}.
```

The source proves singleton allowed sets terminate and relates universal termination to nonexistence of `Z_(P/Q)`-numbers. Since `P<6Q`, a `Z_(P/Q)`-number would force a six-branch survivor and, branch-qualifiably, a Collatz counterexample.

This is committed as `LIT-KTHM-0056`.

## Main result 2 — zero digit is enough

Since

```text
P-Q=7153=23*311,
```

one has

```text
F(x)=x+ceil(7153*x/524288)
```

and the canonical digit is zero exactly when `2^19|x`.

Because zero is not one of the six physical digits, the full chart is eliminated by the single hitting theorem

```text
for every x>0, some F^n(x) is divisible by 2^19.
```

This is much weaker than normality, full residue equidistribution, or occurrence of every digit. It is now the most focused negative target for the six-branch program.

The 2026 Andrieu–Eliahou–Vivion normality conjecture predicts this result but does not prove it. A positive six-branch survivor would disprove their conjecture for this base.

This is committed as `LIT-KTHM-0057`.

## Main result 3 — exact external envelope for finite linear observables

Dubickas 2009 proves that a bounded fixed linear observable of a rational ceiling orbit exists exactly when its coefficient polynomial is divisible by `qX-p`. Therefore every such observable is a finite convolution of the canonical digit word. The canonical digit word is not ultimately periodic and has the native complexity coefficient `971.866577472...`.

A short finite-state argument shows that no nonzero bounded fixed linear observable can be ultimately periodic.

This supports the direction of PR #64/PR #66 while preserving their stronger native scopes.

This is committed as `LIT-KTHM-0055`.

## Centered-power source gap

The highest-value missing source documents are:

1. Dubickas 2006, nearest-integer constants;
2. Dubickas 2008, two-interval exclusions;
3. Dubickas 2009, small-interval theorem.

The abstracts confirm exact relevance, but the `(81,64)` formulas, strict endpoints, equality cases, and Thue–Morse language cannot be safely reconstructed without the full PDFs.

## Pulse/cycle source ladder

PR #53 and PR #70 should use the effective sequence:

```text
native sparse resultant
 -> repetition-only equation
 -> Matveev real bound
 -> Bugeaud/Chim p-adic bound when available
 -> de Weger lattice reduction
 -> exact finite replay.
```

The precise Matveev normalization in the native source-dependent claims remains pending full-PDF audit.

## Files added

```text
literature/imported-theorems/LIT-KTHM-0055-rational-ceiling-linear-observables.md
literature/imported-theorems/LIT-KTHM-0056-approximate-multiplication-residue-map.md
literature/imported-theorems/LIT-KTHM-0057-six-branch-zero-digit-gate.md
literature/LIVE_REPO_REVIEW_WAVE9.md
literature/SOURCE_LEDGER_WAVE9.md
literature/references-wave9.bib
literature/claim-maps/WAVE9.md
literature/UNVERIFIED-WAVE9.md
literature/topic-notes/wave9-zero-digit-and-approximate-multiplication.md
literature/check_literature_wave9.py
this report
```

## Source discipline

- Dubickas 2009 and Dubickas–Mossinghoff 2009 were inspected in complete author-uploaded texts.
- Andrieu–Eliahou–Vivion is explicitly conjectural.
- Matveev, de Weger, Chim, Bugeaud, and the centered Dubickas trilogy are not invoked beyond the inspection level recorded in the source ledger.
- The supplied Väänänen–Wallisser paper remains a finite-dimensional periodic-controller firewall, not an ordinary-extraction theorem.

## Exact next actions

1. Assign one agent only the zero-digit hitting theorem.
2. Acquire the centered Dubickas trilogy from the user.
3. Acquire Matveev 2000 and independently audit PR #70's source constants.
4. If PR #70 survives, build a real/p-adic lattice reduction instead of scanning to the crude cutoff.
5. Continue no finite linear/rational recoding work unless it directly proves zero-digit occurrence or least-root escape.

No positive ordinary seed or nontrivial cycle was found.