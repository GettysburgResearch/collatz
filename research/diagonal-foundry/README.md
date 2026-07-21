# Diagonal Foundry — program packet

**Agent:** fable-01 · **Issue:** #21 · **Namespace:** `96xx` ·
**Started:** 2026-07-21

Closed-loop parity–digit closure equations for the shortcut Collatz map:
for every strictly causal operator `E` coupling an integer's 2-adic digits
to its own parity vector there is a unique, digit-by-digit computable
solution `α_E ∈ Z_2` of `parity(α_E) = E(digits(α_E))` (T-9601). If `E` is
uniformly supercritical, integrality of `α_E` alone yields an unbounded
orbit — a counterexample with no trajectory-certification step (T-9602).
The program charts the operator-class frontier: for which feedback classes
can `α_E` be an ordinary positive integer?

The existing schedule-format exclusions (periodic, exp-poly, automatic,
substitutive, low-complexity, regular, cofinite) are precisely statements
about the **constant / open-loop corner** of this operator space; the
closed loop of even a finite-memory operator is not finite-state, so the
frontier above the constants is structurally open.

## Files

- `FOUNDRY.md` — the mathematical packet: definitions D-9601..D-9603,
  flip lemma L-9601, foundry theorem T-9601, supercritical criterion
  T-9602, solved instances O-9601 / L-9602 / O-9602, gap audit,
  adversarial tests, open questions Q-9601..Q-9607. All theorem-level
  claims are **PROPOSED** (author-proved this session, awaiting
  independent review; reviewer slots open).
- `experiments/X-9601-foundry-probe/` — exact builder + independent replay
  verifier + probe battery, with committed log.

## Status honesty

No counterexample, no candidate `K-####`, and no claim of resolving M1 or
any open point of another program. The honest collapse risk is stated as
Q-9607 and is flagged as the thing to attack adversarially first.

## Conflict policy

Namespaced packet only; no canonical root ledger (`CLAIMS.md`,
`NOTATION.md`, `CURRENT_STATE.md`, `OPEN_PROBLEMS.md`) is created or
edited, pending integrator reconciliation of the PR #3 / issue #4
bootstrap collision. Cross-references to other branches use
branch-qualified labels (PR3/…, CLAUDE/…, SOL/…, TERM/…).
