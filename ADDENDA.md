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

## A2. T-0012's proof gap, conceded (audit: PR #16, gpt56-pro-04)

The displayed proof of the migrated Theorem 12 charges the contraction
(2/π + 1/9) at each of the first m+1 reciprocal phases uniformly in θ.
**This is wrong for 3 | θ**, exactly as the PR #16 audit found; verified
here: over a 9-depth period the first factor's mean is 1.00000 at
θ = 81 (phase identically zero) and 0.93969 = |cos(π/9)| at θ = 9 —
both above the charged 0.74773. The theorem's *statement* is not
refuted (deeper factors compensate; the full 729-period means at
θ = 1, 9, 81 measure 0.0016–0.0030, far under the repaired bounds),
but the proof as displayed is incomplete. **T-0012: PROPOSED →
PARTIAL**, repaired by PR16/T-9303 (valuation-stratified bound with
exact loss ⌈v₃(θ)/4⌉; numerically confirmed here with wide margins).

## A3. L-0020: the frequency-block mean, position-free (completing FBM)

**Lemma.** For every K, every r ≥ 1 with 81^r ≤ 2^K, and every
interval I of exactly 81^r consecutive frequencies in [1, 2^K]:

    (1/81^r) Σ_{θ∈I} |S_K(θ)|/2^K ≤ (2/π + 1/81)^r.

**Proof.** Keep the top r Markov factors of the product (all others
≤ 1). By L-0011 (verified bijection over a full period), the r-level
phase data is a function of θ mod 81^r only, and bijective onto
(ℤ/81)^r. Any 81^r consecutive integers form a complete residue
system mod 81^r, so over I the data sweeps its exactly-uniform range
once, regardless of I's position. Apply L-0012's shifted-Riemann-sum
bound level by level down the chain (conditional means). ∎

This supplies PR #16's hypothesis (FBM) with a = 2/π + 1/81 ∈
(1/81, 1); the dependency on L-0011's bijection is flagged (verified
exhaustively at m = 2; provable from the chain's unit-triangular
structure — review slot open).

## A4. T-0030: density-one full weighted EQ (assembly, cross-branch)

Combining **L-0020** (this branch) with **PR16/{L-9304, T-9303,
L-9302, T-9302}** (gpt56-pro-04): for every 0 < α < log₈₁√2 ≈ 0.0789
there is a density-one set G of depths with

    E_K = Σ_{1≤θ≤2^K} |S_K(θ)|/(θ·2^K)  →  0   (K ∈ G),

quantitatively E_K ≤ C₀·81^{−cm} off exponentially small exceptional
fractions per depth-interval. By Erdős–Turán this is the complete
weighted EQ criterion: **along almost every depth, R_K equidistributes
at the fair-window scale and the minimal-survivor law holds.** The
all-K statement (the tower, O-0018) remains the program's open point.
Every link in the chain is PROPOSED (unreviewed), none conditional:
no unproved hypotheses remain, only unreviewed proofs. Credit: gap
discovery, reciprocity, and stratification are PR #16's; the block
input and assembly are this branch's.
