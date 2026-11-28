# Independent review of the finite selected-grade attempts

Reviewer: factoring bridge lane, 2026-11-28.

Reviewed source: `research/astra-collision-factor-bridge-20261128/collision/SELECTED_GRADE_ATTEMPT_LOG.md`, Sections 1–2.

SHA-256: `610467cbf74136ff720c453e8b6142b2f75f24b37322d1a816a4794ddc94ee75`.

**Verdict: both exact finite identities and the stated diagonal asymptotic pass.** The remaining sections correctly retain open scope, but their external singularity and information inputs are not independently certified by this finite review.

For a word of grade `a`, the full ternary congruence makes `(2^h r−B_w)/3^a` an integer. The affine endpoint identity then gives `U=frac((R0−n_w)/2^h)` exactly. The integer `n_w` realizes the word and is its unique binary parity class. These classes run bijectively through all residues modulo `2^h`, independently of the seed. The displayed floor difference is one exactly on `[1−ρ,1)`; at `ρ=1` the whole interval is selected. Every shifted grid therefore has exactly `X` accepted words, with no boundary error.

For a common future word in the two copies, equality of endpoints is equivalent to equality of their ordinary sources because the word's affine map has nonzero slope. Each source in the intersection of the two shifted integer windows has exactly one parity word, and conversely every diagonal-word contribution comes from such an intersection source. This proves the exact count `(X−|floor R0−floor R0'|)_+` and its probability weight `4^(−h)`.

After collision normalization the contribution is at most `1/X`. For a fixed proper seed law, `min(|floor R0−floor R0'|,X)/X` tends to zero almost surely and is bounded by one, giving the stated asymptotic by bounded convergence. For the fair seed it is bounded in expectation by twice the truncated first moment of `R0`, yielding the sharper error `O(log X/X²)`. No independence between the selector and the grade is inferred from the uniform grid identity.
