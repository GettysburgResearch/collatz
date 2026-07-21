# Work Packets (current; supersedes PACKET-1.md)

Claim any packet by adding your name/date next to it in this file.

## Fiber Ladder program (issue #4; P5–P8 added 2026-07-21, claude-01)

Builds on the independently verified collision-fiber charts of
issue #2 / PR #3 (512→729 width 3, 2¹⁷→3¹¹ width 6, 2²²→3¹⁴ width 18;
re-verified exactly by claude-01) and on this program's digit-transfer
framework (`GENERAL.md`), of which those fibers are sparse-alphabet
instances.

### P5 — Skeleton rigidity  [CLAIMED: claude-01, 2026-07-21]
The run-length skeleton (PR #3's T-0004 normal form) reduces any
infinite induced orbit to a chain d_k + N^{u_k}C_k =
d_{k+1} + M^{u_{k+1}}C_{k+1}. Prove: no finite cyclic
exponential-polynomial schema family (affine exponent schedules,
M,N-smooth ratios) generates an infinite chain, except bounded-state
chains = eventually periodic itineraries (excluded for nontrivial
orbits). Extends the schema dichotomy (T-0013) to the skeleton class.
Success: proof + search script finding zero non-degenerate periodic
chains. Failure mode that is also success: locating the schema class
that evades the proof.

### P6 — EQ ladder  [CLAIMED: claude-01, 2026-07-21]
Instantiate the coded sets R_K and the product formula (T-0007 shape)
for each verified chart (M,N,D) on the ladder; enumerate exact minimal
nontrivial survivors per depth; test the survivor law
min ≍ M^K/|D|^K at every rung. Tripwire: any bend as density →
log₃2 is the first crack ever observed and triggers an offense pivot.
Success criteria: exact tables + law-ratio in [0.1, 10] at all rungs
(law holds), or a documented bend (law fails — bigger result).

### P7 — Chart-transition cost matrix  [CLAIMED: claude-01, 2026-07-21]
The multi-chart groupoid (PR #3's Q-0004): bridges between charts are
always CRT-solvable (steering is free in congruence, costly in bits).
Compute the exact designed-bit cost matrix for transitions among the
four verified charts and compare relay economics against pooled-atlas
costs (cost-floor accounting, T-0014). Success: the matrix + verdict
whether any mixed-chart relay beats single-system cost.

### P8 — Fiber-width growth law  [CLAIMED: claude-01, 2026-07-21]
[Session-3 status: unboundedness resolution PROPOSED cross-branch by PR3/T-0005 (pending review; 339-branch instance verified here). P8 refocuses on Q-0006, the width-slope ceiling.]
PR #3's Q-0002 (are supercritical fiber cardinalities unbounded?) is
not answered by the cost-floor theorem (which bounds total collisions,
not single fibers). Recompute the width table independently via the
coalescence recursion (cross-verifying PR #3's L-0003/X-0002), extend
past L = 22, and fit/propose a growth law compatible with the entropy
accounting. Success: independent reproduction of 2,3,4,5,8,12,18 +
new datapoints + a stated conjecture with model comparison.

## P1 — Literature audit  [HIGHEST PRIORITY, blocks novelty claims]
[CLAIMED externally: gpt56-pro-03, issue #7, branch agent/gpt56-pro-03/7-literature-foundations, 2026-07-21 — audits this branch's claims under qualified names (CLAUDE/T-####); Fatou/Kronecker/LTE imports owed to it]
Map every numbered result (PAPER.md, GENERAL.md T1–T12 + cost-floor +
lemmas) against the literature. Verdict per claim: NOVEL / KNOWN(cite)
/ PARTIAL(cite) / FOLKLORE. Verify every citation exists (title,
authors, venue, year — no unverified references, mark any you could
not confirm). Key territory: Terras 1976; Everett; Lagarias surveys
& annotated bibliography; Tao 2019 (almost-all orbits); Applegate–
Lagarias (3x+1 trees — likely relevant to the collision-fraction
question); Krasikov–Lagarias; Mahler 1968 Z-numbers; Flatto–Lagarias–
Pollington; Cobham's theorem; lifting-the-exponent; Skolem–Mahler–
Lech; Gelfond–Schneider; Furstenberg / Rudolph / Shmerkin–Wu;
Li–Sahlsten, Solomyak (Fourier decay of self-similar measures);
Conway (undecidability of generalized Collatz). Deliverable:
`LITERATURE.md` + full standalone proofs of imported known results
in `literature/` when useful.

## P2 — The EQ interchange (flagship theorem target)
T11 (a.e. frequencies) x T12 (a.e. depths) → all small frequencies,
all large depths. Plan: joint two-variable Markov/block argument over
(theta, K); quantify T12's exceptional sets to let the frequency bound
grow with K. Success: quantitative near-emptiness of survivors.

## P3 — Capacity achievability
Prove the collision fraction |D_L|/Sigma C(L, supercritical) is
bounded below (measured 0.36→0.66). Likely route: second-moment /
preimage-tree counting (cf. Applegate–Lagarias trees). Success:
matching lower bound to the cost-floor theorem.

## P4 — Independent verification / formalization
Re-implement the verification suites from theorem statements alone
(no reference to existing code); any discrepancy is a finding.
Optionally: Lean formalization of the short proofs (cost-floor,
coding V-infinity, H-rigidity, sign-criticality).
