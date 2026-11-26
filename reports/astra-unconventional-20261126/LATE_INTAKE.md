# Intake scope and late cross-branch review

The pass began at `2026-11-26 18:44:58 UTC` on PR 195 commit `f192322f70073ba44bc9f98785a51c27a4da9ee5`. The [initial inventory](INTAKE.json) contains 169 returned pull-request metadata records. This is a repository-wide inventory and a selective reconstruction of relevant primary arguments, not a claim to have re-proved every historical theorem or replayed every corpus.

The first detailed intake pinned PR 192 at `0e313e2cd42cfce1275dbef6129ac13e9a49abd5`, PR 193 at `4cc06e7d8fdec923eed73a26b1e9d680c9f701d1`, PR 197 at `f74d2144275c3e1f9148b0b2997fecc7931ae7f5`, and PR 206 at `3729d84e00cf8794dab43fe2f500213b2b643f83`.

## Four heads changed during this pass

A second read fetched the actual Git trees below without checking them out over the working packet. Several branches independently use a directory with the same name; the full commit and path are therefore essential to the review identity.

| PR and frozen head | Primary paths and claims inspected | Narrow result |
| --- | --- | --- |
| [192](https://github.com/GettysburgResearch/collatz/pull/192), `1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca` | `research/astra-unconventional-20261126/adelic/GROWTH.md`, A6/A7; `descent/README.md`, inverse entry and §5; `descent/PAIRED.md`, cusp return | Local squareclass rank assumptions imply descent, but are not supplied on every orbit. Ordinary one-arm residue routing and paired cusp paths are distinct. The original 19-clock/8-odd payment still needs its prescribed second label and clock budget. The new packet's `PORTAL_BUDGET.md` supplies a separate obstruction to arbitrary-class payment and a scoped fixed-target density bound. |
| [193](https://github.com/GettysburgResearch/collatz/pull/193), `23b7d326a43feb21a827a9024fc24eb10d944338` | `research/astra-unconventional-20261126/README.md`; `arithmetic/MOVING_CENTERS.md`, (1)–(5) and two-window swap; `boundary/ALL_RECORDS.md`, object and quantifier scope | The root reconstructed the fixed-form Subspace Theorem reduction, primitive-gcd exception handling, actual adjacent-swap carry, and resulting long near-repetition restriction. Existence of enough such near-repetitions is absent. The full joint-window, entropy, trace and external analytic estimates were not all independently re-proved in this late read. |
| [200](https://github.com/GettysburgResearch/collatz/pull/200), `e14f3aed2037de90cd571ea8b7c1314222469920` | `research/unconventional-20261126/defects/CENTERED_DEFECT_RETURNS.md`, Theorems 1–2; `arithmetic/COUPLED_CYCLES.md`, J1; `operator/POWER_SPECTRUM.md`, O8 | The cycle agent reconstructed the fixed-template finite-rank-group argument using the stated Evertse–Schlickewei–Schmidt input, the paired rational construction and its denominator scope, and the specified Koopman spectrum. It separately replayed the pinned coupled control with output equality. None gives ordinary denominator-one exclusion or the required all-source return. Its Koopman space is distinct from this packet's forward-mass weighted \(\ell^1\) and rooted point-spectrum theorem. |
| [201](https://github.com/GettysburgResearch/collatz/pull/201), `3eb251fae9082fef33c047079a511d1c3f4c5969` | `research/unconventional-20261126/operator/HYBRID_DESCENT.md`, OP-D1–D3; `EXIT_GATES.md`, OP-G1–G2; `TERNARY_TRANSFER.md`, OP-T2 | The adelic agent and root independently reconstructed the mixed-root all-walk obstruction and ordinary finite-gate mass theorem. The agent checked the diagonal limits and compared them to the exact component-grade fibers. Early fixed sources retain positive atom mass even when later fibers concentrate. The mixed pair \((-1,1)\) is credited to this stronger upstream result. |

The PR 200 coupled-control replay is an agent execution, separate from the root's four saved control replays. Its source SHA-256 was `f768f54c2f5c35fcc4471f8d0a362f0e64745ff9079ee4fcc541e2df08893fa5`; it reported 23,009 sources and 653,953 transitions with exact output equality. No other upstream corpus or Lean build is implied by this event.

[Detailed PR 201 comparison and remaining gap](adelic/LATE_PR201.md)

## Literature actually used

The coordinating agent read Michael Rubinstein's [Waterloo report](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) and the linked [265-page working guide](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf). The report describes the Alpöge–Claude RH and Dirichlet-GRH formal development and independent checks. This pass did not rebuild that development. The guide itself distinguishes its thirteen remaining written hypotheses from inputs taken from the Lean proof.

The transferable mechanism tested here was quantitative integral lattice divisibility against an archimedean bound. Actual Collatz endpoint and internal-cut moment lattices were computed and proved to be full at the stated grades; native symmetric-power eigenline lattices have exactly their displayed denominator factors. No automorphic, motivic or algebraic structure was assumed merely by analogy.

Kunrui Yu's [1999 Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf) is used with rational 3-adic units to bound actual long matching words and postpeak work. Its hypotheses and primary theorem statement were checked, including the lack of a multiplicative-independence requirement and the nonzero-difference condition. The theorem itself remains external literature, not a Lean input proved in this pass. The root also checked the late PR 193 application of the classical finite-place Subspace Theorem to fixed forms; that does not assert an unproved moving-target version.

The improved consecutive-fiber and final pointed box-dimension statements invoke the explicitly pinned PR 146 synchronization estimate and rStation 48, formula (76). Their conditional deductions and parameter use were checked. The underlying analytic estimates were not independently reconstructed in full here and remain **SOURCE-QUALIFIED**. The elementary full-lattice, routing, pointed derived-set and concentration theorems do not depend on those stronger estimates.

## Review versus formal verification

The new written arguments were reconstructed at their saved file hashes; independent agent reviews supplement the coordinating agent's checks. This is internal mathematical review, not external peer review. The Lean and finite-replay receipts record separate executable events. A standard axiom inventory for a conditional convergence theorem does not discharge its ordinary merger, record-lock or cycle-exclusion hypotheses.
