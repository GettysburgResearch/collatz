# Independent scoped review of the stationary collision argument

Reviewer: arithmetic-minimum lane, 2026-11-23.

Scope: `COLLISION_CORE.md`, Sections 3--5, as read in the shared working tree.
This was a mathematical challenge of the new argument, not a replay of the
historical dependency graph or a claim to have formalized its probability
theory.

Reviewed file SHA-256 after the inverse-law source-path correction:
`12d5f897b830c9d4deff794c3d42f99cf330244be4eafe6a4c716fd5db353e7c`.

No gap was found in the following steps.

1. **The stationary lift retains the selected source law.** For fixed word
   length, the bounded total-gap expectation gives tightness on a countable
   discrete alphabet. A diagonal extraction therefore loses no probability
   mass. Deleting either end of a word changes only boundedly many sampled
   endpoints, yielding both consistency and stationarity. The finite ternary
   coding identity is exact; its pushforward preserves the already selected
   ternary time-limit marginal.
2. **The entropy dichotomy is exhaustive.** One strict finite-block Shannon
   deficit persists by stationary subadditivity. If no finite block has a
   deficit, relative-entropy equality against the positive-integer geometric
   product law forces every block to be exactly that product law. Its
   nonuniform one-letter distribution has strictly smaller collision entropy
   than Shannon entropy. No existence of a collision entropy rate is used.
3. **The remainder in (18) is covered.** When `m>=k`, the last remainder of
   length less than `k` is a projection of the final consecutive `k`-block
   contained in the sampled `m`-word. That block's endpoint interval is
   contained in the full `k`-word sampling interval with exactly the stated
   mixture proportion. Entropy concavity and the chain rule yield the bound.
4. **Countable-alphabet entropy continuity is justified.** With fixed `k`,
   the partition function for the cost `sum gaps` is finite for every
   positive parameter. The displayed Gibbs estimate makes entropy tails
   uniformly small by choosing that parameter first and then the cost cutoff.
   A mere appeal to total variation would not suffice; the written argument
   supplies the needed additional control.

The extension to moving resolutions `m=o(M)` is consequently justified in
the finite-deficit case along the extracted source subsequence. The paper
correctly does not infer the same moving-resolution conclusion from a merely
iid fixed-block limit. A same-limit upper collision estimate is still needed
for escape exclusion; this review supplies no such estimate.
