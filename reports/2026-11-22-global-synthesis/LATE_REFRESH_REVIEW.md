# Review of the separate late refresh and capture composition

**22 November 2026. Full Collatz remains OPEN.**

## Scope and source qualification

The late refresh inspects PR175, PR180, PR182 and PR183 at the exact
heads in [LATE_SOURCE_REFRESH.json](LATE_SOURCE_REFRESH.json). It does
not replay their Lean modules or upgrade their analytic source inputs.
The original scientific execution remains commit
2eb1006fba0128006f09fa4279202334f61a233a, with twenty new public Lean
statements and the original three receipts.

An independent arithmetic reader reconstructed the parallel generic
classification and checked the chronology, polynomial-label scope, and
real-growth-exponent obstruction. An independent analytic reader checked
the return-reference parameters, Green constant and exponent, source
domain, and moving-height limitations.

Two qualifications identified during that review were applied:

- The Green estimates explicitly use nonperiodic odd ternary units and
  killing on first entrance into any periodic orbit; the fixed-depth
  density assertion uses finite p greater than one.
- The finite-period profile hypothesis is convergence of the normalized
  difference to zero, which allows zero coefficients. Its conclusion
  excludes nonzero leading profiles, not all upper majorants.

PR183's independent generic block-exponent classification has earlier
recorded repository publication. The attribution is explicit. The
inspected late changes do not include the concrete all-a,b P^aQ^b
exclusion and its certificate in this packet.

## New written composition

[TAIL_CAPTURE_BRIDGE.md](../../research/global-synthesis-20261122/TAIL_CAPTURE_BRIDGE.md)
was derived by the merger reader and independently reconstructed by the
arithmetic reader and the lead. The checked core is:

1. Exact positive odd inverse chain
   q_j=1+4^j*3^(h-j)*v, with 3*q_(j+1)+1=4*q_j.
2. Actual complete certificate for the new source 8*(1+4^h*v), with
   initial even run three and h gap twos before the identical supplied
   tail.
3. The existing PoweredTrace and IntervalHyp allow a ternary-nonunit
   initial odd core.
4. For an old initial even run at most three and a consumed prefix of
   maximum gap four containing a four, the greatest changed grade is
   eight and its multiplicity strictly decreases.
5. The new source captures every positive actual target endpoint at
   most 16*(1+4^h*v)+1, under the same lower-grade induction hypothesis.
6. For a single consumed gap four, initial even run two and h>=4,
   the replacement source exceeds the original source. The same holds
   for initial even run three and h>=6. These cover the entire original
   intervals at target clock zero.

The gap-two trace itself is inherited elementary arithmetic, also present
as WitnessGlobal.twos_trace. The new written conclusion is the capture
composition and the whole-interval comparison.

**Verdict:** the written conditional capture rule and its two
whole-original-interval corollaries follow from the explicit hypotheses.
No conclusion is made about coverage of every remaining certificate
query. These are not additional compiled Lean declarations.

## Actual finite execution

The lead independently replayed the complete supplied tails, exact gap
valuations, target paths, grade comparison and full literal-cut maximum.
The permanent control is
[tail_capture_replay.py](../../research/global-synthesis-20261122/tail_capture_replay.py).
It uses explicit checks that remain active under optimized Python.

The script was run under ordinary and optimized Python. Both executions
passed and produced byte-identical
[late-capture-fixtures.json](late-capture-fixtures.json). The controls
include the two full certificate examples, the actual small and
below-source target paths, and sixteen parameter instances through
h=128. They verify compatibility; they do not replace the arbitrary-h
written argument.

| Reviewed or executed object | SHA256 |
|---|---|
| Final reconciliation note after scope fixes | 256df74b16e68ef8f29cc7ebdd0a29555074655f33816d4150014d9b3783345c |
| Written capture composition | 96fbaf71e5760636bf619e27f2be8ca3a84a3c3a5b836f292d27bc0417e371c8 |
| Executed compatibility script | fe7d47227f883777567344bcf05af8db9c538589fa7a0172538c3a85ce3bb773 |
| Identical output from both modes | 3247fe534d31bbd5b59ff99bf3b04b81e71f38cd7f22007f824ea79f89d6e2fd |

All original compiled modules, exact arithmetic certificate inputs and
reviewed mathematical notes remain unchanged. The only earlier tracked
files modified by this follow-up are the scientific and report README
pointers. Repository integrity on the eventual commit is a separate
execution and does not certify the written theorem.
