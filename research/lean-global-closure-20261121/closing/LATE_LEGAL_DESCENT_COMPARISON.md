# Comparison with the refreshed legal source-surgery attempt

Date: 2026-11-22. This is a source-level comparison, not a Lean replay.

Read PR180 at `5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
`research/retained-source-attacks-20261122/LEGAL_DESCENT.md`.
The earlier repair note in this packet remains frozen at SHA256
`4e47174309ed0253458c7c1ad9e5ae20befd83e9c587616c6a3b2a048e31fb42`.

The new PR180 calculation and our target-tail attempt preserve different
parts of the physical data:

- PR180 retains a literal **source prefix** and deletes an interior source
  window. Its new source is
  \(q'=q+2^E(v-u)/3^i\), so \(3^i\mid v-u\) is necessary. Its joint
  record property \(q_j<q\) then limits nontrivial single-window deletion
  to positions with \(3^i<q\).
- Our calculation retains an actual **target suffix** after an arbitrarily
  edited initial part and attaches it to a certified safe source endpoint.
  The common tail forces \(2^{A-b}\mid x_b-y\). Its positive-state
  requirement and the original-target floor force \(o_b\ge r-2\).

These are complementary integrality restrictions, at the ternary and
dyadic sides respectively. Neither identifies a successful universal edit.

PR180's all-length gap-four replacement failure at endpoints
\(v\equiv7\pmod9\) is also an actual integer obstruction, rather than a
rational-shadow surrogate. Its subsequent signed-carry propagation allows
arbitrarily many changed earlier gaps. Within the stated nonnegative-power
regime the positive carry persists and gives

\[
S'=S-2^e c,\qquad c\ge1.
\]

Thus the exact original-target activation remains

\[
2S+1-t\ge2^{e+1}c.
\]

The full target odd surplus supplies no inequality of that sign. For
example, on the admissible upper residual boundary \(t=2S-1\), the
available slack is two, whereas \(2^{e+1}c\ge4\). Consequently **every**
repair of this stated positive-carry form fails to capture that unchanged
boundary target, regardless of the number of propagated edits. This is an
algebraic conditional observation; it does not assert that such a target
is bad or rule out an independent ordinary merger.

The all-certificate record control from our note remains unchanged as well:
for \(S=1092,t=2047\), every strictly lower-grade complete source is at
most 820, whose interval ceiling is 1641. Thus a source-only repair at a
strictly lower grade cannot activate that original target, even with an
arbitrarily complicated new word. That assertion uses PR185's pinned
all-word maximality proof, not a new certificate census.

**Conclusion:** the refreshed PR180 note does not supply the missing
activation inequality in our attempted repair. Its exact debt calculation
confirms the same unpaid numerical requirement for a different nonlocal
construction. Negative-power carry regimes, moving the common suffix,
simultaneous compensating windows, or later original-target mergers remain
outside both exclusions. No assertion that all possible surgery fails is
made.
