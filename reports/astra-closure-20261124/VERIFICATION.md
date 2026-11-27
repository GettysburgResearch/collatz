# Verification of the global-arithmetic and passage checkpoint

The new packet is `research/astra-closure-20261124/`. **Nineteen public arithmetic declarations passed official Lean 4.34.1** with `-j1 -DwarningAsError=true` and an axiom query for each declaration. Only `propext`, `Classical.choice` and `Quot.sound` were accepted. There were no admitted proofs or extra mathematical axioms in these declarations.

| Module | Public declarations | Formal scope |
| --- | ---: | --- |
| `arithmetic/MountainReturns.lean` | 6 | Complete signed carry, least-valuation noncancellation, ternary square estimate, common-carry divisor, primitive target under stated arithmetic hypotheses, exceptional dyadic rounding |
| `descent/Repayment.lean` | 5 | All-later-visitor factorization, inverse length inequality, rational source-budget transport, all-ones identity/divisibility, critical-arm repayment exclusion |
| `transfer/PhysicalReturn.lean` | 5 | Actual shortcut affine lift, unique affine collision, unbounded suffix, finite cap for bounded roots, exact finite product-marginal counting |
| `boundary/BarrierExit.lean` | 3 | Exact ascent, three crossing/return steps, arbitrary halving run |

The first three modules were compiled together. The boundary module was added and independently compiled after its source was frozen; the receipt includes both runs and verifies the first three source hashes were unchanged. The reproduction driver includes all four. Audited copies append fully qualified axiom queries, preserve the original proof bytes and have their own recorded hashes.

[LEAN_AND_CONTROLS.json](LEAN_AND_CONTROLS.json) records every command, result, source hash and audited-copy hash. The four adjacent compiler logs preserve the transitive inventories.

## Finite arithmetic controls

Each program was run normally and with Python optimization enabled. All six executions passed; paired standard output agreed exactly. Their explicit requirements remain active under optimization.

| Program | Recorded coverage |
| --- | --- |
| `arithmetic/check.py` | 5,000 exact mountain windows; 4,571 high-entry nondegenerate tuples, including 294 low terminal cases; 5,215 power starts; 4,095 exact necessary rounding exclusions |
| `descent/check.py` | 16 complete ternary-period versus physical-forward-visit comparisons, at shortcut deadlines 5 and 7, two budgets and four overlapping prefix families |
| `transfer/controls.py` | 165,726 binary head residue profiles; 81 recovered clock pairs at 253-bit head inputs, with 43 equal roots |

These are finite controls for arithmetic interfaces. They neither certify the analytic theorems nor extrapolate to universal convergence.

## Independent reconstruction and scope

Four written reviews are in the packet:

- `transfer/REVIEW_ARITHMETIC.md` checks Mahler, the full signed nondegeneracy argument, joint ESS rank, first-small-valley splitting and Evertse's numerical-gcd application.
- `arithmetic/REVIEW_HEAD_ROOTS.md` checks the ballot lower bound, asynchronous collision count, clock decoding, stopped-prefix estimates and original-source marginal multiplicities. It identified a necessary timely-population normalization; the correction and counterexample are retained.
- `transfer/REVIEW_DESCENT.md` checks every-clock repayment, the renewal bound, ordinary floors and two-arm counting. It also proves the uniform finite-cutoff estimate and its actual-root consequence.
- `transfer/REVIEW_BOUNDARY.md` checks the future ceiling mark, CRT progression law, actual excursion, head transport and the two distinct series exponents.

Each review identifies exact target hashes. [ROOT_REVIEW.md](ROOT_REVIEW.md) records the coordinator's separate reconstruction and the new latest-source comparison. [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) binds the complete scientific packet; [LATEST_HEADS.json](LATEST_HEADS.json) binds the repository intake.

The Mahler, Subspace, ESS, renewal, probability, density and all-time arguments remain written mathematics. Recent first-passage/fusion/barrier inputs remain source-qualified. No claim is made that the nineteen declarations formalize these infinite theorems or prove Collatz.

Earlier proof bundles and external formalization libraries were not rebuilt. Clean complete-checkout repository validation is a separate integrity gate, with its receipt recorded after the scientific commit. It does not verify mathematics.

The actual published scientific commit `b579defec53bb791ddbe2b6e07382cbb079ba8fc`, tree `33594eec89da3eaeb19ae4f6347efe29edaea8ee`, passed all five default integrity commands in a fresh, complete, clean 446-file checkout. [Publication record](PUBLISHED_CHECKPOINT.md) · [Exact checkout receipt](PUBLISHED_CHECKOUT.json).
