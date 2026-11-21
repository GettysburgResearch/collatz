# Deep-machinery guide: research and review scope

Date: 22 November 2026. Scientific entrypoint:
[literature/deep-machinery-20261122](../../literature/deep-machinery-20261122/README.md).

## What was actually done

- Read the repository entrypoints, research map, integrated status and
  scoped errata, contribution rules, and replay policy.
- Froze the accepted baseline and ten relevant exploratory PR heads.
  Checked that all 31 file locations in `REPO_SOURCES.json` exist at their
  recorded commits. This is a path/identity check, not a compiler replay.
- Researched three specialist streams in parallel: analysis/entropy,
  arithmetic/logic, and dynamics/operators/termination. Added a separate
  rigidity and long-shot synthesis anchored to the exact repo interfaces.
- Consolidated 58 chapter citation records into 56 main unique works,
  plus a separately consulted Vojta author exposition: 57 works total.
  `SOURCES.json` records primary URLs, versions, theorem locations, and
  the actual inspection level. Indexed statements, author restatements,
  recent source-qualified papers, and abstract-only leads are distinct.
- Had another researcher check the new quantitative deductions and the
  chapter-to-task implications. The review reconstructed the algebra and
  hypothesis boundaries; it was not just agreement with a summary.

## Mathematical cross-checks and resulting fixes

| Item | What the second check covered | Remaining boundary |
|---|---|---|
| Proposed polylogarithmic visit clock | Dirichlet denominator lower bound; perturbation and height product; quarter-size restarts; telescoped shortcut clock including initial even prefix | Explicit logarithmic constants, effective threshold, rounding and formalization are still required |
| Retained-atom Lp deduction | Holder-conjugate exponent; finite fourth logarithmic moment; dyadic harmonic divergence; distinct endpoints | The required transported-density estimate is OPEN; cycles are not excluded |
| Occupation certificate | Killed adjoint inequality and telescoping; initial mass at 1 handled separately | No suitable universal potential has been constructed |
| Fixed-floor rate comparison | Least failed source is odd; a unit target lies between m and 2m; lower-density comparison; strict exponent thresholds | Recent population inputs remain source-qualified; the uniform upper tail and effective remaining range are OPEN |
| Fixed-block recurrence quotient | Torsion-free source root group; simple-denominator polynomial factor argument; fixed schema and denominator conditions | Theorem statements checked through primary indexed text; full proof not audited; classification and coverage are OPEN |
| Rigidity and arithmetic dynamics | Exact multiplier restrictions; finite-index/decomposition scope; reducibility; map and interpolation hypotheses | No suitable source-preserving rigidity representation is constructed |

Precision corrections incorporated into the guide include:

- a survivor is **not eventually periodic** when distinctness is needed;
- the Lp statement uses `1 < p < infinity`;
- the occupation sum adds the initial atom at 1 when the full measure is used;
- the offset composition names the valuation sum of the last block;
- the odd-start fixed-floor comparison explains initial powers of two;
- the solenoid definition includes connectedness and finite-rank dual;
- Rudolph's relatively prime multipliers are at least 2;
- the general solenoid conclusion retains finite-index restriction and
  finite ergodic decomposition;
- the operator-renewal summary includes its nonzero mean-operator condition;
- large early norms are not described as a refutation of an asymptotic bound;
- all source-reported formalization claims retain their replay boundaries.

No statement in this report certifies Collatz, promotes an exploratory
packet to the accepted baseline, or supplies the missing global estimates.
In particular, the newest four #183 Lean scripts were reported pending
compiler replay at the inspected head. No external or repository Lean
project was rebuilt for this literature contribution.

## Repository execution boundary

The publication PR records the actual final commit, changed paths, and the
result of `python -X utf8 -B tools/validate.py` on a clean complete checkout
of that commit. Its JSON execution receipt is generated outside the tested
checkout, as required by replay policy. The PR also records the final
remote readback. Treat only those recorded execution results as executed;
this methodology note is not a substitute for a receipt.

The validator checks repository structure and frozen identities. It does
not check the mathematics in this guide. No new expensive search,
optimization result, Lean theorem, or bounded Collatz verification is
claimed by this documentation-only contribution.
