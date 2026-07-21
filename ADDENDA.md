# Proof addenda to migrated documents

Post-migration completions of proofs that the migrated documents
asserted with only partial written support. Each entry names its
target claim; the ledger row points here. Migrated documents are not
edited; this file is the append-only home for their completions.

## A1. Exact multiplicative orders (completes T-0019, `H64.md`)

**Claim (as asserted).** `ord(64 mod 81^k) = 9·81^{k−1}` for all
`k ≥ 1` ("no Wieferich luck"; level-k gadget length `9·81^{k−1}`), and
dually `ord(81 mod 2^j) = 2^{j−4}` for `j ≥ 5`.

**Proof.** Both are lifting-the-exponent computations — the same lemma
already used quantitatively by Theorem 5 (supply isometry).

*3-adic side.* `64 ≡ 1 (mod 9)` with `v₃(64 − 1) = v₃(63) = 2`. For
`p = 3` and `3 | a − 1`, LTE gives `v₃(a^n − 1) = v₃(a−1) + v₃(n)`;
hence `v₃(64^n − 1) = 2 + v₃(n)`. The order of 64 modulo `3^m`
(`m ≥ 2`) is the least `n` with `2 + v₃(n) ≥ m`, i.e. `n = 3^{m−2}`.
With `81^k = 3^{4k}`:

    ord(64 mod 81^k) = 3^{4k−2} = 9·81^{k−1}   for every k ≥ 1. ∎

*2-adic side.* `v₂(81 − 1) = v₂(80) = 4`, `v₂(81 + 1) = 1`. For odd
`n`, `v₂(81^n − 1) = 4 < j` (any `j ≥ 5`); for even `n`, LTE at
`p = 2` gives `v₂(81^n − 1) = v₂(80) + v₂(82) + v₂(n) − 1 =
4 + v₂(n)`. The least `n` with `4 + v₂(n) ≥ j` is `n = 2^{j−4}`:

    ord(81 mod 2^j) = 2^{j−4}   for every j ≥ 5. ∎

Consistency check: Theorem 5's isometry constant is the same
computation at `n = 4d`: `v₂(81^{4d} − 1) = 4 + v₂(4d) = 6 + v₂(d)`.
Consequences as stated in `H64.md`: every tower level exists, no
coincidence collapses gadget lengths, and `k = 1` recovers the carry
nine-cycle order. External import: LTE (audit under P1, issue #7).

Ledger effect: **T-0019 PARTIAL → PROPOSED** (complete written proof;
independent review still pending like all PROPOSED entries).
