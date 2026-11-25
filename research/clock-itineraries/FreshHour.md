# November 25 follow-up on the Collatz proof

**The global statement remains open.** For the shortcut map, 23 is the first clock at which every positive odd target coprime to three occurs as the common image of $23+32t$ and its triple. The parameter depends on the target. A second theorem routes every such target through 513 consecutive powers of three at each sufficiently late clock. A route to a chosen target concerns a constructed source. The missing convergence statement concerns every prescribed source. [Sharp pair theorem](PairCover.md) · [513-rank theorem and finite-count equivalence](CommonClocks.md)

## Three tests of the remaining gap

* **Descent.** In every sufficiently high packet of $2^{80(R+H+1)}$ consecutive parameters of a prescribed mixed progression, at least half generate whole subprogressions on which every rank through $R$ falls below its base at the common clock $H+80(R+H+1)$. A convergent source at rank 512 can nevertheless avoid every lower-base merger through $10^{243}$ steps on both paths. A method using these refinements must still control a particular hypothetical least bad source. [Tower proofs](HourTower.md)
* **Escape.** A hypothetical nonrepeating ray with bounded historical drawdown and unbounded gaps between records supplies an aperiodic limiting gap sequence with an irrational ternary coordinate. The general pointwise drawdown estimate is open. [Escape proofs](HourEscape.md)
* **Cycles.** In a sequence of positive cycles whose odd heights occupy a fixed multiplicative strip and whose minima tend to infinity, rational accumulation is excluded separately at two and three, at every choice of phase. Positive gap sizes and periods are unrestricted. Actual convergent paths also realize arbitrarily deep centered windows in a factor-two strip. Excluding cycles requires information about the complete return. [Rational exclusions](mathlib/HourEscapeBinaryWindows.lean) · [Ordinary paths and explicit cutoffs](HourCycle.md)

## Fresh sources examined

These six research threads add to the [fifty earlier PRs](FiftyPRs.md). The links freeze the revisions used here.

| PR | Contribution considered |
|---:|---|
| 192 | Bounded-cycle inverse optimization and the distinction between a constructed merger and a hit for a supplied source. [Proposal](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/FINAL_PROPOSAL.md) |
| 193 | Nineteen odd steps in a residue merger and finite Fourier constraints. [Research packet](https://github.com/GettysburgResearch/collatz/blob/aa0b01234735683b413098b81afdf764de503730/research/astra-closure-20261125/README.md) |
| 195 | Large prime factors across a cycle and quantitative bounded-lag arithmetic for orbit mergers. [Round 12](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/README.md) |
| 197 | Paired rational reference trajectories, ternary rescue, and delay at simultaneous checkpoints. [Paired reductions](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/paired-reductions/README.md) |
| 201 | A two-gap inverse router, thin-band escape constraints, and a new critical-record renewal calculation. [Earlier revision](https://github.com/GettysburgResearch/collatz/tree/02fb390a76fb2ffb00fee612649ca23a82d99d31/research/killed-green-head-closure-20261124) · [Renewal update](https://github.com/GettysburgResearch/collatz/blob/94ce06ccbd312ccd0ce4450b567cc514a2f0b54a/research/killed-green-head-closure-20261124/record-renewal/README.md) |
| 210 | Rational residues on critical record limits and the arithmetic hypotheses for turning a limiting word into an ordinary trace. [Record rigidity](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md) |

We compiled the original source bytes of `ThinBand.lean`, `RecordRenewal.lean`, and `CriticalRecordRigidity.lean` using native Lean 4.34.1 and the pinned Mathlib cache. Their 23 printed axiom reports contain only standard Lean axioms. The original sources emit linter warnings. These checks cover the formal declarations in those files. The adjoining papers contain further arguments. The November 24 Elsenhans paper also treats computations for individual very large inputs and makes its fast complexity estimate conditional on a quantitative convergence hypothesis. [Elsenhans, *Numerical verification of the Collatz conjecture for billion digit random numbers*](https://link.springer.com/article/10.1007/s40993-026-00811-5)

## Later updates during the hour

A second sweep found substantive changes on five heads. PR 192 constructs the exact smaller source $1121+48\cdot3^8a$ for a comparison from $89585+48\cdot2^{19}a$, saving 19 clock steps and eight odd steps. Its chains vary the source. PR 195 uses the earlier 1379-step certificate to synchronize finite banks of parents on refinements of its particular progression. It retains a merger obligation for a prescribed defect. [PR 192 proposal](https://github.com/GettysburgResearch/collatz/blob/0e313e2cd42cfce1275dbef6129ac13e9a49abd5/research/astra-literature-closure-20261125/FINAL_PROPOSAL.md) · [PR 195 finite-bank theorem](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md)

PR 193 gives a written $S$-adic Subspace Theorem lower bound for the outside-prime part of an ordinary carry times the starting height, uniformly over supplied sources. Its Lean files cover the finite identities and certificates. PR 197 obtains arbitrarily large savings on cofinal parameter families using the signed cycle through $-17$ and $-55$. PR 200 studies the onset time of fixed-ray traces and conditional Fourier cancellation. A quantitative transfer to all ordinary positive sources remains open. [PR 193 carry result](https://github.com/GettysburgResearch/collatz/blob/4cc06e7d8fdec923eed73a26b1e9d680c9f701d1/research/astra-multiple-attacks-20261125/README.md) · [PR 197 unbounded savings](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/unbounded-queries/README.md) · [PR 200 trace onset](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md)

A written argument in this packet gives $O_\theta(X^\theta)$ visits below $X$ on every finite simple odd path whenever $\theta>h(\log_2 3)/\log 3\approx0.9499555$. The estimate is uniform in the path. Its proof uses counting and induction and has not been formalized. [Height count proof and prior bounds](HourCycleOccupation.md)

## Rebuilding this packet

Use Lean 4.34.1 and a Mathlib checkout at `d13f23b723b8a846827a245b89c10fc7d3f11612` with its matching binary cache. The command below rebuilds every local Lean module into a new temporary directory, checks every printed axiom report, and writes the source hashes and module counts to a receipt. Adjust the paths to the installed toolchain and Mathlib.

```sh
python check_fresh_lean.py --lean /path/to/lean --mathlib /path/to/mathlib4 --receipt verification.json
python pair_fiber_replay.py
```
