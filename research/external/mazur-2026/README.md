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
- [`synthesis-and-roadmap.md`](synthesis-and-roadmap.md) — the exact complementarity, why the two theorems do not yet combine automatically, and a proposed exponent-race bridge that would yield a complete Collatz proof under one new forward power-saving hypothesis.

## Import snapshot

- Imported against `main` commit `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- Import date: 2026-09-03.
- Every page of both supplied PDFs was read and visually inspected.
- A 57-check supplied-file integrity, provenance, and small-arithmetic replay passed; see [`local-check-report.json`](local-check-report.json).
- The full Lean builds and the 645,700,815-byte predecessor certificate payloads were **not** independently replayed in this repository import.

## Scientific placement

The predecessor theorem supplies **lower growth of an inverse basin**. The natural-density theorem supplies **forward descent for a density-one population**. The repository's resident `SC*` problem instead asks for a **fixed-source all-depth stopping theorem**, while `FC*` asks for a **complete first-crossing obstruction**. None of those quantifier shifts is automatic.

The most concrete combined target identified here is a fixed-threshold power-saving estimate. If the odd starts that fail to descend below a fixed height by logarithmic time could be bounded by `O_H(X^β)` for some `β < 0.901`, the predecessor theorem would contradict the existence of a least counterexample. The proof of that conditional bridge is given in the synthesis note; the needed forward power saving is open.
