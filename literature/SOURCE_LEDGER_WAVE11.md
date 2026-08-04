# Source ledger — literature audit wave 11

Only located or user-supplied sources are listed. Source theorem, native reduction, and exact computation remain separate.

## S89 — Matveev weighted coefficient parameter

**Record:** E. M. Matveev, *An Explicit Lower Bound for a Homogeneous Rational Linear Form in the Logarithms of Algebraic Numbers. II*, Izvestiya: Mathematics 64 (2000), 1217–1269.

**Inspected:** complete user-supplied English PDF, especially equations `(1.3)`, `(1.4)`, Corollary 2.3, and the height definitions.

**Wave-11 correction:** the native estimate

\[
B<kr+1
\]

uses Matveev's weighted parameter `B` from `(1.3)`, not the coarser `B*` from `(1.4)`. The numerical pulse certificates had used the correct value `kr+1`; only the explanatory label was wrong. `LIT-KTHM-0060` has been corrected.

## S90 — verified positive-cycle floor

**Records:**

1. David Barina, 2025 verification of the Collatz conjecture below `2^71`.
2. Ahmed Ansari, 2025 recursively sufficient extension used in PR #76 to obtain
   \[
   N_*=4\cdot3^{44}+2.
   \]

**Inspected in this wave:** repository source audit and primary metadata; the distributed `2^71` computation was not rerun.

**Native use:** `LIT-KTHM-0065` uses only the consequence that every member of a nontrivial positive cycle exceeds `N_*`.

**Status caution:** `SOURCE-QUALIFIED`. Independent review should reconstruct the exact Ansari implication and preserve the computational provenance of the Barina floor.

## S91 — Dubickas centered-power trilogy

**Records:** Dubickas 2006, 2008, 2009 as listed in `SOURCE_LEDGER_WAVE10.md`.

**Inspected:** complete user-supplied PDFs.

**Wave-11 use:** no new scalar bound beyond Wave 10. The source consequences remain side constraints for PR #16/PR #67; they do not prove ordinary appended-block nonstabilization.

## S92 — Bugeaud and Chim finite-place logarithmic forms

**Records:** Bugeaud 2002; Chim 2025.

**Inspected:** complete user-supplied PDFs.

**Wave-11 use:** proposal for the first support-density barrier. Both theorems bound valuations of genuine two-term logarithmic forms under explicit unit, principal-unit, and multiplicative-independence hypotheses. They do not automatically apply to a multi-term pulse resultant.

The required native bridge is:

```text
identify a denominator prime l >= 5;
reduce one pulse resultant modulo l to a genuine two-term form;
verify unit/principal-unit hypotheses;
prove the resulting logarithmic valuation bound is below v_l(D).
```

No such fresh-prime incompatibility has yet been proved.

## Cautions

- `LIT-KTHM-0065` is a native synthesis, not a theorem quoted from one paper.
- Its Matveev step is source-audited.
- Its verified-floor step is source-qualified.
- Its pulse identity and divisor reduction remain native proposed dependencies.
- The exact replay certifies all rational/logarithmic inequalities after those interfaces.
- No source listed here proves a standard Collatz counterexample or the full conjecture.