# Session report — session 3: solution-cone lemma swarm (issue #24)

```text
Agent:               fable-01
Issue:               #24 (claimed this session; owner's #1-ranked unclaimed direction)
Branch:              claude/collatz-repo-exploration-m2e5vp
Starting hypothesis: The coefficient-operator seed in the issue #24 ranking
                     comment decomposes into ~12 small, independently
                     provable results; a parallel prover swarm with dual
                     adversarial verification can produce a large packet in
                     one pass.
```

## Approaches attempted

12 parallel prover agents, one precisely-scoped target each, with a
designed verification stage (2 adversarial verifiers per proof + repair
round). Targets chosen to give the program: exact operator foundations
(L-9701), the load-bearing equivalence (T-9701), cone geometry (T-9702),
a spectral reformulation (T-9703), measure-side duality (T-9704), a
faithful Hilbert home (L-9705, L-9708), the canonical functional equation
(L-9706), growth transfer (L-9707), computational anchors (X-9701,
X-9702), and literature positioning (M-9701).

## New results (ALL UNREVIEWED DRAFTS — see caveat below)

Headlines beyond the issue's seed:

- **T-9703 (spectral trichotomy):** Collatz ⟺ the unit-circle point
  spectrum of F on ℓ∞ is exactly {±1}; any single unit eigenvalue that is
  not a root of unity ⟺ a divergent orbit exists.
- **T-9704 (count dichotomy):** dim Fix(F|ℓ∞) = #components vs
  dim Fix(P|ℓ¹) = #cycles; divergence ⟺ strict inequality.
- **L-9708 (space-selection theorem):** Fix(F|ℓ²(w)) is spanned by the
  indicators of components with w-summable mass — unweighted ℓ² is blind
  (dim 0 unconditionally), summable weights are faithful.
- **L-9705:** F*F is diagonal on the weighted spaces, giving the exact
  operator norm and a separable-Hilbert formulation of the conjecture.

## CRITICAL PROCESS CAVEAT (recorded per §17.1: never conceal uncertainty)

The verification stage of the swarm did not run: all 24 verifier agents
failed on a session usage limit after the 12 provers completed. The
workflow's internal "CONFIRMED" labels were vacuous (empty verdict lists)
and were discarded during integration. What was salvaged in this pass:
the integrator ran all 12 committed verification snippets locally —
all pass (finite consistency only). `VERIFICATION.md` records the exact
state and the reviewer entry points. Every claim is PROPOSED at most and
flagged UNREVIEWED in its file header.

## Candidate counterexamples

None. No K-#### issued.

## Failed approaches

The full prove→verify→repair pipeline as a single pass — killed by an
external resource limit, not by the mathematics. The prover outputs are
cached (workflow run wf_c6b5dadd-96f) so the verification stage can be
resumed exactly when capacity allows.

## Files changed

- `research/solution-cone/{README.md, CONE.md, VERIFICATION.md}`
- `research/solution-cone/claims/{L-9701,T-9701,T-9702,T-9703,T-9704,L-9705,L-9706,L-9707,L-9708,X-9701,X-9702,M-9701}.md`
- `research/solution-cone/experiments/snippets/*.py` + `results/*.log`
- this report

## Claims affected

New 97xx namespace only. Nothing promoted; nothing outside the packet
touched.

## Recommended next actions

1. Re-run the cached verification stage (resume wf_c6b5dadd-96f) or,
   better, independent human/agent review starting with T-9703's
   depth-cocycle argument and T-9704's conservativity step.
2. Audit M-9701's attributions under the issue #7 protocol.
3. The mathematical next step is Q-9707 (separation problem) — transport
   the ℓ∞-spectral separation of T-9703 into the disk/Hilbert setting
   fixed by L-9705/L-9708.

## Organizational improvement ideas

A verification stage that silently produces zero verdicts must not be
interpretable as "no objections": pipelines should distinguish
"verified: no objections" from "verification absent". This packet's
integration enforced that manually; recommend it as an explicit norm for
any future agent-swarm methodology (M-idea for the integrator).
