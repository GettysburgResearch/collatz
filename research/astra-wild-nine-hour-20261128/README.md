# Nine-hour independent attacks on global Collatz obstructions

**Active exploratory research. Collatz remains unresolved.** This pass began on November 28, 2026, at 09:08:39 UTC, with the requested endpoint 18:08:39 UTC. Three Astra 6.2 agents at ultra work independently with broad repository context; the coordinator reviews, connects, and publishes the results. Finished lanes will be restarted during the pass.

The purpose is to attack complete arguments that could rule out every exceptional positive source or every complete nontrivial positive cycle. The initial directions are provisional: complete-cycle arithmetic, component-color rigidity, outside machinery, and the critical inverse-control endpoint. They are not a commitment to small improvements within those architectures. A promising closure will take priority over the allocation.

## Source and evidence policy

The integrated base is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Current science also lives in open PRs, especially #211–#218. The [intake](../../reports/astra-wild-nine-hour-20261128/INTAKE.json) freezes the returned metadata. Concurrent passes #217 and #218 are separate work and will be credited where used. Earlier source claims do not become verified merely by being cited here.

Written arguments, locally compiled Lean, externally reported Lean, exact finite checks, and unproved premises will be labeled separately. Source-dependent asymptotics retain their quantifiers. Every ordinary-source claim keeps one fixed positive integer; completions and moving finite witnesses are distinguished. Cycle claims retain the entire denominator and primitive-period conditions.

## Organization

- `arithmetic/`: independently chosen arithmetic and complete-cycle attacks.
- `dynamics/`: independently chosen dynamical and component arguments.
- `outside/`: outside mechanisms developed into mathematical attacks.
- `coordinator/`: independent synthesis, critical endpoint attacks, and connected kernels.
- `reports/astra-wild-nine-hour-20261128/`: source pins, review, actual verification, and checkpoint ledger.

## Checkpoint 1

The [exact native affine-branch spectrum](arithmetic/AFFINE_BRANCH_SPECTRUM.md) supplies the matching lower exponential rate for every prescribed odd-grade sequence. Its total exponent is the previously known upper exponent, approximately 0.9654. Leen's ternary entropy theorem is the named external input. The result also applies to the known multiple basins of the minus-sign map, so this spectrum alone does not close positive Collatz.

The [ordinary colour construction](dynamics/ORDINARY_COLOUR_OBSTRUCTION.md) has density one half, exact doubling invariance, and very small disagreement under every fixed rational affine comparison. Its colour survives the actual strictly precritical Collatz trajectory for almost every original start, while a positive proportion eventually crosses a true colour defect. It isolates the missing exact propagation and late-height information in an averaged component argument.

The [coordinator's review](../../reports/astra-wild-nine-hour-20261128/CHECKPOINT_01_REVIEW.md) reconstructs both proofs and separates inherited results from new deductions. Two Lean modules and five public roots were rebuilt and audited locally; the infinite analytic statements remain written, with their source qualifications. The [full metadata refresh](../../reports/astra-wild-nine-hour-20261128/SOURCE_REFRESH_01.json) records all 155 open PRs returned at 09:21 UTC.

The opening intake commit was an organizational record, not a mathematical checkpoint. The nine-hour research pass continues.

