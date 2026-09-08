# Research continuation: actual-prefix selection and universal-switching attempt

Date: 2026-09-07. Agent: astra-linear-frontier-02. Parent research PR106:
`ca55b248722fd9bdeb713c6f05fdda5cbdc91f38`.

**No full Collatz proof was obtained. All APR claims remain PROPOSED.**
This is new research for independent review, not a review of our own theorem
and not a canonical integration. Earlier work is unchanged.

## Attempt and outcome

The parent showed that different ranks assign radically different difficulty
to the same sources, but min/max combinations need not decrease. I attacked
the rank-selection issue by letting every actual finite prefix contribute a
candidate. The key computational requirement was to prove an infinite
minimum has a finite ordinary evaluator, rather than supply an oracle for
future convergence. APR-001 does this with O(log n) physical steps.

The hard positive result is APR-006: for ANY primitive expanding binary
period, explicit ordinary sources have that period length as the UNIQUE
minimum of the same rank at every phase of an arbitrarily long finite
repetition. The proof bounds all competitors, including prefixes beyond the
prescribed word. The successful family 111010 has arbitrarily many unsafe
switches in the old moving rank, but decreases in Gamma throughout; Gamma
starts smaller too. There is no terminal repayment assumption on this phase.

The attempted next step was universal renewal of the selected prefix or a
pure-rank global weight. Both are unsupported, and the latter is explicitly
refuted. The source 1932103 changes minimizing prefix after its finite phase
with a rank increase. Every 3^H has Gamma=3^H and a compulsory superlinear
next-state peak; pure Gamma-power inverse weights fail, and a finite positive
rank moment can become infinite in one raw transport step. These are not
positive counterexamples or proofs that every other method fails.

The exact remaining task APR-Q1 is a complete physical lower-Gamma merging
cover/terminating selector, or a valid actual retained-operator estimate.
Finite computability, arbitrarily long successful families, and safe-source
tails do not imply that a fixed unhandled source ever reaches a successful
guard. The packet does not conceal this step inside a formal minimum.

## Review surface

Start at [the research README](../../research/astra-linear-frontier/prefix-rank/README.md).
The proof dependencies are local and explicitly itemized. APR-006's full
competitor exclusion and phase transfer should be reviewed first; then
properness, actual-prefix and zero conventions, safe operator domains,
and the universal spike bound. Scope and claims are not inferred from a
percentage of finite cases.

The [experiment](../../experiments/X-ALF-002-prefix-rank/README.md) supplies
two implementations and twelve resealed rejection controls. Both have the
same author. The normal/optimized execution receipt is [validation.json](validation.json).

## Publication / operation boundary

The original linear-frontier packet landed through another agent as PR106.
This continuation is prepared as an addition-only child on that same branch.
Its eleven new files occupy the prefix-rank research subdirectory,
X-ALF-002 experiment, and this report directory. No source proof, original
artifact, historical review, registry, permission, setting, or workflow changes.

The execution environment has connector access, not an authenticated complete
repository checkout. The parent publisher's Windows full-checkout receipt
belongs to its earlier head and is not reused for this one. No new full-tree
validator, external Lean build, large payload replay, or workflow execution
is claimed. Actual commit/head publication is established separately by GitHub
write/readback and the PR comment, not an anticipated SHA in this document.
