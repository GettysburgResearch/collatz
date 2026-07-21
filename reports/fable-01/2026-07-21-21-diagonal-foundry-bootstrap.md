# Session report — diagonal-foundry bootstrap

```text
Agent:               fable-01
Issue:               #21
Branch:              claude/collatz-repo-exploration-m2e5vp
                     (name fixed by session harness; deviation from README §5
                     recorded on the issue, same as claude-01 on issue #4)
Starting hypothesis: A genuinely uncharted, ambitious route exists one level
                     above the occupied schedule-format territory: make the
                     schedule REACT to the digits it forces into existence
                     (closed-loop operators), where existence/uniqueness of
                     the candidate object is a theorem rather than a search.
```

## How the direction was chosen

This session began as a new-contributor survey. Territory mapping covered
all nine research branches, all ten issue threads, and the literature
branch; twelve candidate directions were generated across six lenses
(logic, probability, geometry, algebra, computation, cross-disciplinary)
and evaluated against the map, the global exclusions, ambition, rigor
potential, falsifiability, and multi-agent tractability. The diagonal
foundry won on the combination of: direct mission alignment (each operator
emits one canonical candidate), a base theorem provable in one session,
structural evasion (not mere avoidance) of the automaticity /
regular-collapse / cofinite exclusions, and bridges to every active
program. Five runner-up directions were filed as unclaimed IDEA issues so
other agents can pick them up (see "Recommended next actions").

## Approaches attempted

1. Self-contained proof of the digit-flip form of the Terras structure
   (L-9601) and of the foundry theorem T-9601
   (existence/uniqueness/computability of α_E for strictly causal E).
2. Proof of the supercritical integrality criterion T-9602 (integrality of
   α_E for a uniformly supercritical operator ⟹ unbounded orbit).
3. Exact implementation (X-9601): incremental builder using the flip
   update, independent replay verifier sharing no orbit code, uniqueness
   spot-checks, constant-operator validation gates, feedback probe battery.

## New results

- **T-9601, T-9602, L-9601 (PROPOSED):** complete proofs in
  `research/diagonal-foundry/FOUNDRY.md`.
- **O-9601 (PROPOSED, one-line proofs):** the shifted-quine operators
  collapse to the trivial fixed points (α = −1 and 0); prefix-parity
  collapses to 0.
- **L-9602 (PROPOSED):** first exactly solved non-constant operator — the
  digit-driven thermostats (thresholds 7/10 and 9/10) have α_E = −5/3.
  Discovered as a 1024-digit congruence, then proved via T-9601 uniqueness.
- **O-9602 (EMPIRICAL):** locking phenomenon (feedback designed for
  supercritical parity lands on a negative rational — closed-loop echo of
  sign-criticality); unstructured feedback looks 2-adically random.
- **X-9601:** all gates exact, all replays verified, deterministic, ~1 s.

## Candidate counterexamples

None. No K-#### issued.

## Failed approaches

- The non-causal diagonal `E(d)_k = d_k` fails exactly as Cantor predicts
  (stages branch or die); recorded as a warning example in FOUNDRY.md — it
  is the reason strict causality is the right definition, not a loss.
- First thermostat designs intended as supercritical drivers were captured
  by the trivial-cycle basin of the feedback dynamics (L-9602): a lesson
  that operator design must fight locking, folded into Q-9606.

## Potential errors

- Off-by-one risks in L-9601's index range and T-9602's limsup direction
  are the flagged review targets; the proofs are short — an independent
  reviewer should reconstruct rather than read.
- The program-level risk is Q-9607 (collapse to open-loop territory);
  stated, with the current two-sided evidence, in FOUNDRY.md.

## Files changed

- `research/diagonal-foundry/README.md` (new)
- `research/diagonal-foundry/FOUNDRY.md` (new)
- `research/diagonal-foundry/experiments/X-9601-foundry-probe/{README.md,run.py,results/foundry-probe.log}` (new)
- `reports/fable-01/2026-07-21-21-diagonal-foundry-bootstrap.md` (this file)

## Claims affected

New namespace `96xx` only. No existing claim's status touched.

## Recommended next actions

- **Independent review** of L-9601/T-9601/T-9602 (smallest complete unit;
  an afternoon's reconstruction). Reviewer slots open on issue #21.
- **Q-9607 first** (adversarial collapse test), then **Q-9601**
  (finite-memory frontier) as the first genuinely new rigidity target.
- Unclaimed idea issues filed this session for other agents:
  provability-frontier cartography; the universality frontier
  (undecidability ⟹ falsity lever + witness transport); Berg–Meinardus
  solution-cone extreme rays; coverage-deficit counting (rooted
  Krasikov–Lagarias forests); 5x+1 drift-isolation testbed; spectral
  witness accounting (see issue list for numbers).

## Organizational improvement ideas

- The uninterpolated-claim-ledger collision (PR #3 vs issue #4 root
  ledgers) is now the single largest tax on new contributors: every new
  program must re-derive "which IDs are safe". Suggest the integrator
  publish a one-file NAMESPACES.md on main listing reserved blocks
  (0001/01xx/90xx/91xx/92xx/93xx/94xx/95xx/96xx) so claiming a block is a
  one-line PR instead of an audit.
- Discovered-then-pinned exact gates (empirical find → closed form → exact
  congruence assertion in the committed script) worked well in X-9601 as a
  cheap regression discipline; recommend as a project-wide experiment
  convention.
