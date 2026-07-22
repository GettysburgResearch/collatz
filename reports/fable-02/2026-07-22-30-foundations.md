# Session report — fable-02 — foundations packet (99xx)

```text
Agent:    fable-02 (coordinator), with prover sub-agents fable-02-p1…p7 and
          verifier sub-agents fable-02-v1…v9 (each a separate context)
Issue:    #30
Branch:   claude/subagent-spawn-limits-ihpcc2 (harness-designated; §5 deviation noted in #30)
Session:  2026-07-21 ~21:00Z → 2026-07-22 morning (one session-limit outage mid-run,
          ~23:5xZ–00:10Z; all interrupted agents resumed after reset)
```

## Starting hypothesis

The classical load-bearing lemmas of Collatz research (Terras bijection, iteration formula,
cycle Diophantine constraints, divergence density threshold, preimage/sieve structure) could
be proved completely in-repo, adversarially reviewed, and packaged so every active direction
can cite a common proved substrate instead of literature imports or per-branch re-derivations.

## Approaches attempted

Parallel prover sub-agents, each given a precisely pre-stated lemma with a suggested proof
route and orders to correct-and-flag any error in the coordinator's statements; each finished
file then reviewed by a separate adversarial verifier sub-agent (independent reconstruction +
independent exact-arithmetic refutation attempts, per README §13). Waves: 7 lemmas → 5 more
assigned to successful provers → verification. Late in the session the repository owner
directed that remaining verifications be skipped to conserve credits; files affected stay
PROPOSED for an external cross-model review pass.

## New results (see research/foundations/FOUNDATIONS.md for the full index)

PROVED (author + passed in-repo adversarial review): L-9902 (Terras bijection),
L-9903 (iteration formula, sharp remainder bounds), L-9904 (2-adic conjugacy; realization;
the boxed integrality-obstruction theorem), L-9905 (cycle equation; product formula),
L-9906 (no nontrivial cycles with m ≤ 6 odd terms, elementary), L-9907 (divergence ⟹
liminf parity density ≥ log₃2; converse; integer-only pigeonhole with precise caveats),
L-9909 (preimage tree; minimal-counterexample sieve; exact survivor classes mod 2⁸),
L-9901 (C/T/S equivalences + orbit trichotomy), L-9911 (conditional minimal-counterexample
structure theorem).

PROPOSED (complete proofs, not yet reviewed; external cross-model pass planned by owner):
L-9908 (stopping-time density with float-free certified rate), L-9910 (Legendre criterion;
certified CF digits of log₂3; convergent constraints on cycle shape), L-9912 (cycle exponent
statistics; bonus eliminations m ∈ {7,9,12}; K singletons), L-9914 (census lower bound
(1/5)x^{3/10} via mod-9-controlled preimage tree).

## Candidate counterexamples

None proposed, none found. Nothing in this packet asserts either resolution of the conjecture.

## Failed approaches / corrections worth recording

- Coordinator sketch errors caught and corrected by provers (flagged inline in the files):
  L-9910.4(i)'s "forces x_min < 1" (corrected route: x_min < 2 ⟹ x_min = 1 ⟹ trivial);
  L-9907.3's claim that the pigeonhole fails "in Q" (it survives for single odd-denominator
  rational orbits; genuine failure modes are Z₂∖Q points and non-orbit symbolic sequences);
  L-9912.5's dictionary example (a = 3 ⟺ x ≡ 13 mod 16, not 5 mod 16).
- Verifier-found defects, all minor, fixed and documented in-file: a k = 0 quantifier edge in
  L-9907's (2.4); scope/wording items in L-9905, L-9903.
- No elementary counting upper bound on the exponent-1 fraction in cycles exists (recorded
  with structural reason as Q-9912-A) — attempts to force one were abandoned honestly.

## Potential errors (where reviewers should look hardest)

Each file's "Remaining uncertainty" section lists its own pressure points. Packet-level:
the load-bearing finite computations (L-9906's 1763-case enumeration, L-9909's n ≤ 10⁶
sweep, L-9910's big-integer CF certificates, L-9908's integer certificates) have been run
exactly and, where PROVED, independently re-implemented — but a third, external re-execution
is cheap and worthwhile; L-9910's largest certificates (16.8M-bit comparisons) are
machine-checked only; the four PROPOSED-without-review files await any adversarial pass.

## Files changed

research/foundations/: NOTATION.md, FOUNDATIONS.md, L-9901…L-9912, L-9914 (13 claim files);
reports/fable-02/2026-07-22-30-foundations.md (this report). No canonical root ledger touched.

## Claims affected

D-9901…D-9910 (definitions); L-9901…L-9912, L-9914 (new, statuses as above);
Q-9902, Q-9904, Q-9912-A (new open questions).

## Recommended next actions

1. External review pass over the six PROPOSED files (owner has one planned).
2. m = 8, K = 13: enumerate the 792 exponent compositions (settles the smallest open
   cycle length; L-9912's bonus makes this the natural next elementary step).
3. L-9913 (suggested, unclaimed): Eliahou-style cycle-length lower bound from L-9905 +
   L-9910's certified convergents + a verified sweep floor.
4. Extend L-9906's template with a larger verified floor (m ≤ 29 reachable per its notes).
5. Cross-link: issue #21 can now cite L-9902 as the requested independent reconstruction;
   issue #25 can build on L-9909/L-9911/L-9914's closure + root-independent counting.

## Organizational improvement ideas

- The prover/verifier split (separate contexts, verifier must re-derive and re-compute from
  statements alone) caught real defects cheaply; recommend it as the default for proof files.
- Pre-stating lemmas with suggested routes plus a standing "correct-and-flag" instruction
  produced several fixes of the coordinator's own errors — better than trusting top-down
  statements.
- Claim-ID namespacing (99xx) and packet isolation again avoided all cross-branch conflicts;
  the convention deserves promotion into README §7 once an integrator consolidates.
- Load-bearing finite computations should always ship as in-file code + verbatim output with
  their exact logical role stated (this packet's convention; propose repo-wide adoption).
```text
HANDOFF FROM: fable-02
HANDOFF TO: any (external review pass planned by owner)
CURRENT CLAIM OR CANDIDATE: L-9908/10/12, L-9914 awaiting review; other 9 PROVED
BLOCKING STEP: independent review of the four PROPOSED files
FILES TO READ: research/foundations/FOUNDATIONS.md first, then per-file
FAILED ATTEMPTS: see "Failed approaches" above
MOST PROMISING NEXT MOVE: m = 8 / K = 13 enumeration; then L-9913
MAIN RISK: treating PROPOSED compound corollaries (m ∈ {7,9,12} eliminations) as settled
POSSIBLE ORGANIZATIONAL IMPROVEMENT: adopt prover/verifier split repo-wide
```
