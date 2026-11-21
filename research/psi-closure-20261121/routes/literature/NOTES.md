# Route: literature and GRH check (21 Nov 2026)

**Evidence level: search-summary only.** About a dozen web searches and page summaries by
a delegated agent. No primary PDF was read in full. Every statement below must be re-fetched
from its source before it is cited as a theorem. Nothing here is a mathematical claim of
this repository.

## Outcome

Nothing found closes `OpenLemma` or its first layer (`∀ i, 3^i ∈ C`).

## Prior art for the closure criteria

| Source | What it gives (paraphrase) | Relation to the closure criteria |
|---|---|---|
| Andaloro, Fibonacci Quart. 38 (2000) | the class `1 mod 16` is a sufficient set | sufficiency of a class, not a closure equivalence |
| K. M. Monks, Proc. AMS 134 (2006) | every nonconstant arithmetic progression is sufficient | same type as above |
| Monks, Monks, Monks, Monks, arXiv:1204.3904 | strongly sufficient sets; every orbit meets `2 mod 9` | same type; formal definition of "strongly sufficient" not read |

No published statement was found that Collatz is equivalent to closure of the convergent
set under `n ↦ 3n`, `2n − 1`, `3n − 1` or an adjacent pair on a class. This is **not** a
novelty claim: Lagarias's annotated bibliographies and Wirsching's book were not checked.

## Explicit families and density

- No theorem found that every power of 3, every `2^a ± 1`, or any explicit exponential
  family with unbounded stopping time reaches 1.
- Tao (Forum Math. Pi 2022): almost all orbits, in logarithmic density, attain almost
  bounded values. Natural density 1 of the convergent set is not proved.
- Lau / AxiomProver, Hexagon preprint 2610.00249 (Oct 2026): explicit positive lower
  density, reported as Lean-formalized by the vendor. Not independently checked here.

## Conditional results

No GRH-, abc- or Artin-conditional theorem about Collatz cycles, divergence or density was
located. Digit-statistics results on `3^n` in base 2 (Dupuy–Weirich; Dimitrov–Howe) do not
control `T`-orbits of `3^n`, so no route from them to the first layer was found.

## The GRH announcement

Reported on 20 Nov 2026: Levent Alpöge (Anthropic) released a short note stating a belief
that a proof of the Riemann hypothesis was found working with Claude; a Lean development is
reported as the released artifact. Press reports conflict on whether the claim covers GRH.
Status per the press: not independently verified, not peer reviewed. The note itself was
not read. Whatever its status, no known conditional result turns GRH into `OpenLemma`.
