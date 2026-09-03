# Mazur 2026 Collatz advances

> **Status: EXTERNAL SOURCE-QUALIFIED; LOCALLY AUDITED (PARTIAL).** Collatz remains unsolved. These works are not resident proofs of the conjecture and are not added to the canonical claim registry by this import.

This packet imports and analyzes two complementary July 2026 works by Lech Mazur:

1. **Certified exponent-0.90 lower bounds for Collatz predecessor sets** — an inverse-tree theorem for every fixed target not divisible by three.
2. **Natural-density almost-bounded Collatz orbits in logarithmic time** — a forward typical-orbit theorem with ordinary natural density and explicit logarithmic clocks.

The supplied PDFs are indexed by exact fingerprint in [`papers/`](papers/); their binaries are not redistributed because no license was supplied. Machine-readable provenance and evidence boundaries are in [`sources.json`](sources.json); [`check_import.py`](check_import.py) verifies the recorded source metadata and small exact-arithmetic surface, and rechecks supplied PDF bytes when invoked with `--pdf-dir`.

## Read in this order

- [`CLAIM_MATRIX.md`](CLAIM_MATRIX.md) — claim-by-claim status and non-claims.
- [`predecessor-x090.md`](predecessor-x090.md) — theorem, proof architecture, trust boundary, repository relation, and improvement program.
- [`natural-density-log-time.md`](natural-density-log-time.md) — theorem, transport mechanism, clocks, limitations, and improvement program.
- [`synthesis-and-roadmap.md`](synthesis-and-roadmap.md) — the exact complementarity, why the two theorems do not yet combine automatically, and a proposed exponent-race bridge.
- [`fixed-height-forward-power-saving.md`](fixed-height-forward-power-saving.md) — a theorem-development pass on the missing forward estimate: a sharper `H=1` reduction, an unconditional `X^0.949955...` Lane-A prefix bound, an exact exponent-loss audit, and a killed-pullback criterion identifying the remaining quantitative input.

## Import snapshot

- Imported against `main` commit `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- Import date: 2026-09-03.
- Every page of both supplied PDFs was read and visually inspected.
- A 57-check supplied-file integrity, provenance, and small-arithmetic replay passed; see [`local-check-report.json`](local-check-report.json).
- The full Lean builds and the 645,700,815-byte predecessor certificate payloads were **not** independently replayed in this repository import.
- The fixed-height continuation has its own numerical regression report at [`fixed-height-check-report.json`](fixed-height-check-report.json); that report is not proof evidence.

## Scientific placement

The predecessor theorem supplies **lower growth of an inverse basin**. The natural-density theorem supplies **forward descent for a density-one population**. The repository's resident `SC*` problem instead asks for a **fixed-source all-depth stopping theorem**, while `FC*` asks for a **complete first-crossing obstruction**. None of those quantifier shifts is automatic.

The fixed-height continuation sharpens the combined target. It is enough to control the single floor `H=1`: if Collatz is false, the predecessor theorem forces at least `X^0.901/(1+log_2 X)` odd starts below `X` to avoid `1` for every finite clock. Therefore an upper bound `B_1(X;C)=O(X^beta)` with `beta<0.901` would close the conjecture. The continuation proves only a restricted coefficient-supercritical prefix estimate with exponent `0.949955...`; the full fixed-height theorem remains open.
