# Work Packets (current; supersedes PACKET-1.md)

Claim any packet by adding your name/date next to it in this file.

## P1 — Literature audit  [HIGHEST PRIORITY, blocks novelty claims]
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
