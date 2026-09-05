# Scoped errata and pending replacement wording

This record implements the review boundary, not retroactive verification. Original proof files are retained byte-for-byte, including old wording. **The two replacement statements below are PROPOSED pending narrow independent review of this exact wording.** An unrestricted original is not accepted through an adjacent passing result.

## E-INTEGRATION-001 — positive-beta timed bootstrap

Source: PR88 `c28922fb6d1c070bf86a76192f40bc9ea3edd67c`, `research/external/mazur-2026/fixed-height-forward-power-saving.md`, MZ-FH-005. Review: [A, RA-021/022 and RP-A1](../../reports/prepublic-2026-09-05/reviewer-a/ACTION_MAP.md).

Proposed restriction: retain every original descent, fiber, scale and horizon hypothesis and require **beta>0** as well as `beta>max(1-D,1-delta/(1-r))` for the timed conclusion. A reconstructed the intended positive-beta range; the printed unrestricted nonpositive endpoint requires a separate argument.

A dyadic sum of `2^(j beta)` has the required upper-scale power for positive beta. At beta=0 it retains the number of shells; at negative beta a fixed small-source contribution is not bounded by a vanishing large-X power. This does not instantiate the missing survivor-specific fiber hypothesis. The intended crossing application below 0.901 remains conditional.

## E-INTEGRATION-002 — zero affine remainder before logarithms

Source: PR92 `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`, `research/astra-three-routes/pass2/SC_TAIL_AND_ECHO.md`, T-A3-453. Review: [B, F03](../../reports/prepublic-2026-09-05/reviewer-b/INTEGRATION_CHECKLIST.md).

Proposed guard: process `A_w=0` before the displayed logarithmic cutoff; use that cutoff only for `A_w>0`. Preserve all original positivity, integrality, displacement, full-denominator and prefix conditions.

A zero affine remainder has no odd contribution. A nonempty first coefficient-crossing word is therefore the one-letter word `0`. Its equation `A_w=D n+2^j d`, with `D=1`, `j=1`, `n>0` and `d>=0`, is impossible. Thus this no-descent displacement interval is empty, without evaluating the undefined zero logarithm. This is an endpoint repair, not an all-word ordinary exclusion theorem.

## E-INTEGRATION-003 — orbit terminology

The orbitwise counting and SC-tail summaries use **infinite distinct value set / non-eventually-periodic positive orbit**. A finite cycle repeated indefinitely is not an injective counting input. This is the scope retained by B for T-A3-403/451; neither the old periodic synthesis nor the SC*/FC* bridge is promoted.

## Software repairs are separate evidence

The affected active assertion-based verifier entry points reject optimized Python and authenticate preserved source bytes before delegation. PR88 regeneration uses a temporary directory and a uniquely named immutable report. Their implementation tests appear in [replay policy](../../docs/REPLAY_POLICY.md), not as independent review of a changed mathematical theorem.
