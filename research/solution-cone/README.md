# Solution cone — program packet

**Agent:** fable-01 · **Issue:** #24 · **Namespace:** `97xx` ·
**Started:** 2026-07-21 (claimed after the owner's independent ranking
placed #24 first among unclaimed directions)

The pullback operator `F` on coefficient sequences, `(Fa)_m = a_{T(m)}`
(shortcut map `T` on `N_0`, `T(0) = 0`), makes the Collatz conjecture a
statement about a fixed-point space: fixed sequences are exactly those
constant on the weak components of the functional graph, so the
conjecture says `dim Fix(F) = 2` in any faithful coefficient space.
This packet develops the surrounding theory as many small, independently
verified results: exact operator norms and adjoints, the component
theorem, extreme rays of the nonnegative fixed cone, the unit-circle
point-spectrum dichotomy, pushforward/pullback duality (cycles vs
components), faithful weighted Hilbert settings, the canonical
single-valued functional equation, radial-growth transfer, and the
Hilbert-blindness no-go with an exact faithfulness criterion.

Production protocol for this packet: each result was drafted by a
dedicated prover agent, adversarially reviewed by two independent
verifier agents (one reconstructing the proof from the statement alone,
one attempting refutation with executable finite checks and 3n−1
controls), and repaired-and-rechecked when objections arose. Per README
§7 the statuses below still enter as **PROPOSED** at strongest — the
swarm's internal verification does not count as the repository's
independent review, and the per-claim verification trail is recorded in
`VERIFICATION.md` so reviewers can target the weakest links directly.

## Files

- `CONE.md` — the results, one section per claim, with complete proofs,
  gap audits, and statuses.
- `VERIFICATION.md` — the adversarial-review trail per claim (verdicts,
  objections raised, repairs made).
- `experiments/` — the computational experiments (X-9701 identity
  checker and truncated-kernel accounting; X-9702 spectral/duality
  experiments on the 3n−1 control map), with exact code and committed
  logs.

## Conflict policy

Namespaced packet; no canonical root ledgers touched; cross-references
branch-qualified. Literature attributions are provisional pending the
issue #7 verification culture (see M-9701 positioning note).
