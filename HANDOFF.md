# Handoff: migrating this program to gfreund123/collatz

Everything lives on branch `claude/collatz-symbolic-rewrite-2x60pa` of
`gfreund123/math`, directory `collatz/`. All results are committed;
nothing exists only in chat.

## For the next session (with gfreund123/collatz as a source)

1. Clone/fetch this branch of `gfreund123/math`.
2. Copy the entire `collatz/` directory into the root of
   `gfreund123/collatz` (or `git subtree split -P collatz` on this
   branch to preserve the commit history, then merge that into the
   collatz repo).
3. Run the verification suite to confirm the transfer:
   every `experiments/*.py` should end `ALL CHECKS PASS` (or its
   documented summary line); logs regenerate into
   `experiments/results/`.
4. Commit with a message noting provenance (math repo, branch, HEAD
   hash).

## Reading order for any agent joining the program

1. `PAPER.md` — consolidated account; every claim cites its script.
2. `MINIMAL.md` — the minimal open statement (M1/M2/M3) and EQ.
3. `EQ.md` — state of the EQ attack (Theorems 7–10, what remains).
4. `RIGIDITY.md`, `H64.md`, `PROGRAM.md` — detailed proofs and the
   two constructions.
5. `PACKET-1.md` — the first work packet.

## Non-negotiable norms (proposed for the collatz repo)

1. **No claim without a verifying script** (exact arithmetic, committed,
   with a log in `experiments/results/`).
2. **One claims ledger** (claim → status → script → owner), read before
   starting any work.
3. **Adversarial review is a role**: each "proved" claim gets an agent
   assigned to break it. Cross-vendor preferred.
4. **Work happens in packets** (self-contained specs with falsifiable
   success criteria), claimed in the ledger.
5. Merge conflicts between agents are decided by scripts, not prose;
   dead ends are written up with the same rigor as successes; one
   notation file freezes definitions; one literature file tracks
   adjacent known results (Mahler Z-numbers, FLP, Cobham, LTE, SML,
   Gelfond–Schneider, Li–Sahlsten/Solomyak Fourier decay).
