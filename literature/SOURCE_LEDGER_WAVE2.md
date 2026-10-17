# Source ledger — wave 2

Only sources actually located during this pass are listed. `Full text` means the paper/manuscript itself was inspected; `metadata/abstract` means only the official or author-hosted bibliographic surface was inspected. The relation column is deliberately conservative.

| Key | Located source | Inspection | What it supports | What it does not support |
|---|---|---|---|---|
| `AkiyamaFrougnySakarovitch2008` | Shigeki Akiyama, Christiane Frougny, Jacques Sakarovitch, *Powers of rationals modulo 1 and rational base number systems*, Israel Journal of Mathematics 168 (2008), 53–91 | bibliographic metadata / manuscript surface located | genuine rational-base numeration and powers-mod-one context for PR #3 | does not identify the repo's signed cylinder-selected renewal language with the canonical `p/q` representation language |
| `Karp1978` | Richard M. Karp, *A characterization of the minimum cycle mean in a digraph*, Discrete Mathematics 23 (1978), 309–311 | bibliographic metadata located | cycle-mean algorithms and the finite potential framework near `PR3/T-0013` | does not construct arithmetic Collatz edges or an invariant survivor |
| `MauldinWilliams1988` | R. Daniel Mauldin, S. C. Williams, *Hausdorff dimension in graph directed constructions*, Transactions of the AMS 309 (1988), 811–829, DOI `10.1090/S0002-9947-1988-0961615-4` | official metadata located | graph-directed compact attractor context | does not prove ordinary-integer membership or deterministic Collatz selection |
| `Hutchinson1981` | John E. Hutchinson, *Fractals and self similarity*, Indiana University Mathematics Journal 30 (1981), 713–747 | bibliographic/full-text surface located | contraction/IFS fixed-point theorem | not an arithmetic realization theorem |
| `CaucalRispal2025` | Didier Caucal, Cyril Rispal, synchronized-transducer treatment relevant to Collatz, DOI `10.1007/978-3-031-81202-6_8` | publisher metadata located | modern transducer context for PR #12 | does not produce a regular sanctuary |
| `ShallitWilson` | Jeffrey Shallit, D. Wilson, *The 3x+1 problem and finite automata*, author-hosted PDF `https://cs.uwaterloo.ca/~shallit/Papers/wilson.pdf` | manuscript located | finite-automata treatment of Collatz-adjacent structure | not a forward-invariant sanctuary theorem |
| `Barina2025` | David Barina, published Collatz verification paper, DOI `10.1007/s11227-025-07337-0` | publisher metadata located | the external finite verification frontier used only for PR #12 search pruning | does not enter the sanctuary certificate itself; exact strict range wording must be copied from the paper |
| `GeserHofbauerWaldmann2004` | Alfons Geser, Dieter Hofbauer, Johannes Waldmann, *Match-bounded string rewriting systems*, Applicable Algebra in Engineering, Communication and Computing 15 (2004), 149–171 | publisher/search metadata located | scope of the match-bounded termination method | unbounded one-convention match height does not refute other termination methods |
| `Eliahou1993` | Shalom Eliahou, *The 3x+1 problem: new lower bounds on nontrivial cycle lengths*, Discrete Mathematics 118 (1993), 45–56 | bibliographic metadata located | classical exact cycle arithmetic and lower-bound context | not a substitute for replaying a compressed solver output |
| `SimonsDeWeger2005` | John L. Simons, Benne de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arithmetica 117 (2005), 51–70 | paper metadata/full-text surface located | rigorous cycle-bound framework | its parameter conventions must be matched exactly before pruning a search |
| `Hercher2022` | Jan Hercher, *There are no Collatz m-cycles with m <= 91*, arXiv `2201.00406` | arXiv manuscript located | current local-minimum cycle frontier cited by issue #9 | `m` is not the accelerated odd-step count |
| `SterinWoods2020` | reverse cellular-automaton formulation by Sterin and Woods, arXiv `2007.06979` | arXiv manuscript/metadata located | alternative compressed reachability context | not an existence theorem for a positive cycle |

## Verification discipline

- Exact theorem imports in wave 2 are mostly supplied with complete elementary proofs, so they do not depend on uninspected proof text.
- A source's presence in this ledger never upgrades a native claim.
- When a title/venue is not needed for a load-bearing theorem, the suite records it as context rather than pretending to have checked a numbered theorem.
- The Barina range, Hercher parameter, and any tool-specific match annotation must be copied exactly by the branch that uses them.