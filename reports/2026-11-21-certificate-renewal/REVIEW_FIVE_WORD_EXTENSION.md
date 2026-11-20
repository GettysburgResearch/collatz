# Independent review: enlarged five-word transport and renewal

**Verdict: VERIFIED for FW1–FW5 at the exact local file hashes below.** This is a mathematical and arithmetic-code review by a separate agent, not a formal proof-assistant build or approval of all neighboring source PRs.

Reviewed files:

- `FIVE_WORD_EXTENSION.md`: SHA-256 `1969be619e2fe2b42fd2cad65d0bc0a50eb0f2c008154a652dfdf4934ebb9461`.
- `check_five_word_extension.py`: SHA-256 `7648405fc2446f3ac857e23e79bb9923fca7e8b919ca31185d4977c80e0c7232`.

## Ordinary identities and domain

I independently reconstructed the full inverse-word formula and the successive divisibility argument. Full numerator integrality forces each inverse division; a positive odd endpoint and positive exponents make every integral inverse output positive odd. The correction-decoding recursion is unique because the remaining correction after its leading term is removed has exact two-adic valuation equal to the first exponent.

The extension identity is valid for every run length. For one extension, lowering the last target exponent by one and appending three changes its correction to `3 C(d) + 5·2^(S(a)+2)`, precisely five times the new source correction. Its new final entry is three, so induction is legitimate. This proof does not depend on the forty replayed extension instances.

The eight initial-word families are pairwise disjoint, including variable two-runs. I recalculated each density and their sum `23/384`. The tail in a run length is contained in an increasingly fine fixed-prefix binary cylinder, which justifies natural density of the countable union. The ternary-unit restriction does not change relative binary-cylinder densities by CRT.

I checked `3q<=x` separately on all rows. The two rows C and H require their actual minimum source residues; the weaker estimate obtained by inserting the possibly unrealizable endpoint `q=1` would not suffice for C. The note correctly uses the residue guards. The complete compiler consumes finite disjoint blocks, preserves each block's physical clock, and appends the actual edge `5 -> 1`. It rejects malformed first-hit words and retains `UNRESOLVED` for valid uncovered inputs.

## Full inverse-column estimate

The following points are essential and are correctly retained:

1. The endpoint `q=1` has zero five defect. Every remaining positive odd ternary unit is at least five, so the denominator replacement `C/q <= C/5` has the stated direction.
2. On a cell with too few ternary digits, the first exponent found from the weaker congruence is a lower bound for the actual first exponent. It is still valid to use the full actual exponent period in the geometric factor, because the full legal progression starts no earlier than that lower bound.
3. When the cell knows one additional ternary digit and the first integral source is a multiple of three, skipping that first exponent is valid uniformly on the cell. Later forbidden sources may be restored on the upper-bound side.
4. The exact correction for a stem followed by a two-run gives the positive term `I_P(1)` plus an explicit `(4/3)^r` term. Dropping the former is an upper bound for inverse weight. For `r>=k`, integrality forces the displayed weak exponent congruence modulo `3^k`; the actual exponent period is at least `2·3^k`. Thus the two independent geometric sums cover every omitted run length and every omitted exponent.
5. All fractional powers are bounded from above by an integer-verified rational. Rounding the geometric exponent down, or increasing gamma in `gamma^k/(1-gamma)`, also enlarges the bound. The tiny-term branches use positive upper bounds, not numerical zero; their stated clock thresholds imply powers strictly smaller than `2^-160`.

The residue algorithm begins with every unit class modulo 243 and replaces a class only by its three disjoint children. Its 184 leaves therefore cover the entire unit domain, not merely sampled residues. The exact upper bound is below `249/250` on every leaf. The resulting finite-cutoff renewal inequality and `E_s <=250 R_s` follow without subtracting infinite sums.

## Executed replay

I ran the exact checker independently in normal and `-OO` Python. Both exited zero with empty stderr and identical stdout SHA-256:

`2fb03f2fb1865d633e0517d8ac96818732bb7c71d8e49b93cabfc537a6d21c72`.

The output reports 680 paired ordinary replays, 28 complete certificate compilations, four rejected malformed controls, and the complete 184-leaf coefficient certificate. Execution details are in `review-five-execution.json`; the exact normal and optimized outputs are retained separately.

## Review boundary

This verdict covers FW1–FW5 and their mathematical relation to the reviewed checker. It does not verify the independently cited latest PR146 sufficient-progression theorem, the external predecessor-density input, or any implication from finite complement energy to full Collatz beyond the explicitly cited source boundary. In particular the contraction estimate does not bound the complement energy or provide a complete certificate selector. The coverage increase is real; universal convergence remains unproved.
