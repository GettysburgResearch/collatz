# Final report: three-hour proof pass

**Status: no full Collatz proof and no maximal median collision lower bound.** This pass produced a source-qualified semiprime sufficiency theorem, a simpler one-copy criterion that would settle full convergence, positive evaluation before its critical window, and concrete imports and limitations of the factoring work. All analytic dependencies and formal scopes remain explicit.

Requested interval: November 28, 2026, 08:52:20–11:52:20 UTC, or 10:52:20–13:52:20 in Jerusalem. Final publication and remote verification conclude the interval. The work is published in [Collatz PR217](https://github.com/GettysburgResearch/collatz/pull/217), stacked on PR214 at `504d29d399efa941a62006d1ea4635385ce6bb5f`. The final PR receipt records the published head and frozen validation tree; the report does not attempt a self-referential commit hash.

## 1. What would now settle the critical question

Use the native shortcut map, and let
\[
 \nu=\log2-\tfrac12\log3,\qquad
 h_X=\lfloor\log X/\nu\rfloor,\qquad
 W_X(n)=\frac{2(a_{h_X}(n)-h_X/2)}{\sqrt{h_X}},
\]
where the source is uniform on the positive integers through \(X\), and \(a_h\) is its actual number of odd departures. Let \(b\) denote the natural density of the known convergent basin. The [minimum-only argument](collision/CRITICAL_TAIL_WITHOUT_PACKING.md) proves
\[
 \limsup_X\Pr(W_X\le-z)
 \le b\Phi(-z)+(1-b)\Phi(-z/r_*),\qquad z>0,
\]
with
\[
 \beta_3=\frac{\log2}{\log(10/3)},\qquad
 r_*=\frac{\log2-\beta_3\log3}{\nu}\approx0.42170026<1.
\]
It follows that the single estimate
\[
 \boxed{\quad\liminf_X\Pr(W_X\le-z)\ge\Phi(-z)
 \quad\text{for one fixed }z>0\quad}
\]
would force \(b=1\), and the named positive-predecessor theorem would then give full Collatz. **The boxed lower bound remains unproved.** The upper-gap implication uses the source-qualified joint minimum/clock law; it is not an unconditional replacement for that external input.

The simplification is substantive. Before the first global minimum, departed states are distinct, so the exact logarithmic correction is at most \((1+\log h)/3\). After an actual minimum \(m\), every state stays at least \(m\), and the native product gives
\[
 2^t\le(3+1/m)^{a_t}.
\]
A bad minimum is odd and at least three, giving \(2^t3^{a_t}\le10^{a_t}\). These finite facts control every bad future, including a hypothetical escaping one. No orbit-packing estimate, full height-process limit, phase equidistribution or classification of hypothetical cycles is needed for this upper gap. The stronger [exact cycle-mixture description](arithmetic/CRITICAL_GRADE_TAIL.md) retains its extra packing input.

The [stationary transfer](factoring/STATIONARY_COLLISION_CONSUMER.md) moves the entire actual grade/endpoint law with error \(O(\log X/X)\), uniformly in the observation clock. Its one-copy selector has exact mass \(\rho_X=X/2^{h_X}\). The boxed problem is therefore equivalent, up to the controlled transfer error, to the relative lower estimate
\[
 \Pr\!\left(K=1,\ A_{h_X}\le
 \left\lfloor h_X/2-z\sqrt{h_X}/2\right\rfloor\right)
 \ge[\Phi(-z)-o(1)]\rho_X.
\]
This removes endpoint labels and the two-copy probability scale from the sufficient target. It does not remove the correlation between the selector and the odd grade.

The original [collision endpoint theorem](COLLISION_THRESHOLD.md) remains intact:
\[
 \frac18-L\ge\frac{b(1-b)}4.
\]
Its countable-series formulation includes arbitrary nonperiodic mass. The Lean kernel verifies the exact maximal-mass equivalence, not the missing assertion \(L\ge1/8\).

## 2. A semiprime family sufficient for full convergence

The [semiprime sufficiency theorem](SEMIPRIME_SUFFICIENCY.md) concerns
\[
 \mathcal S=\{pq:p<q\text{ prime},\ \log(pq)<p\le\log^2(pq)\}.
\]
Uniformly over actual Collatz component unions, it transfers positive ordinary density to positive relative density within this sparse family. The error is paid on the \(X/\log X\) semiprime scale, using the unconditional Matomäki–Teräväinen short-interval supply theorem, actual pair-fusion cylinders, and Brun–Titchmarsh control of failing residues. Combined with positive predecessors, convergence of every member of \(\mathcal S\), or upper relative convergence density one within \(\mathcal S\), is equivalent to full Collatz.

The [representative theorem](SEMIPRIME_REPRESENTATIVES.md) supplies a concrete integer-testable subfamily: for \(n=pq\) of bit length \(B\), require \(B<p\) and \(4p\le B^2\). Every positive source has a finite genuine merger with a member of this subfamily. An explicitly terminating dovetail finds the two paths, with no uniform runtime bound asserted. Seven certificates contain 214 independently replayed native edges.

The factorization problem on this family is already easy: the small factor is polynomial in the input bit length. The missing theorem is dynamical convergence or descent of these semiprimes. This reduction does not remove RH from the different ordered-prime-product independence theorem in Paper233. Earlier sparse sufficient sets are credited to their prior sources.

## 3. What was positively evaluated, and where it stops

The [moving precritical theorem](factoring/PRECRITICAL_STATIONARY_EVALUATION.md) gives an actual relative evaluation of the selected grade distribution. For every deterministic \(w_X\to\infty\) with \(w_X=o(\sqrt{\log X})\), put
\[
 h=\lfloor\nu^{-1}\log X-w_X\sqrt{\log X}\rfloor.
\]
The normalized grade tends to a standard Gaussian, and the corresponding stationary selected probability equals \([\Phi(-z)+o(1)]X/2^h\). The source is the directly inspected uniform full height-process theorem, with endpoint continuity and the preminimum harmonic correction supplied explicitly. There is no rate claim or estimate relative to a growing Gaussian tail.

Inside a fixed critical window, the preminimum contribution is exactly \((\Phi(t)-\Phi(u))_+\). Below \(t=u\), that contribution is zero, and the desired lower estimate concerns the actual postminimum continuation. The finite [association counterexample](arithmetic/STATIONARY_GRADE_ANTICORRELATION.md), checked by two methods on 100,000 native sources, rules out an all-scale positive-association shortcut. It does not disprove the critical asymptotic target.

The [near-fair tilt ledger](arithmetic/FINAL_TILT_ATTEMPT_LEDGER.md) retains the source window and controls the transfer error at the rare-event scale, including the improved negative-tilt error. It leaves an ordinary exponential moment unevaluated. A change of measure therefore identifies another precise consumer without settling its sign or limit.

## 4. Actual imports from the factoring repository

The [aggregate transfer](factoring/AGGREGATE_PROFILE_TRANSFER.md) imports the general prime-power Cartier machinery from factoring PR234. A constant matrix retains odd grade, ternary residue and real carry moments. Its cost is polynomial in the numerical conductor, moment degree and precision; a polynomial-time evaluator in the bit length of the full conductor is not proved.

The [resolvent reduction](factoring/JOINT_RESOLVENT_WINDOW.md) encodes the entire ordinary source window using a logarithmic-squared number of specified complex resolvent queries. The [stationary reduction](factoring/CONDUCTOR_AND_STATIONARY_TRANSFER.md) provides exact integer recovery from a sufficiently accurate biased joint trace. Neither result discards the growing ternary conductor or the real window. Evaluating the required trace remains the load-bearing task.

The final source intake includes the new [arbitrary-corank Fourier evaluator](factoring/CHECKPOINT004_FOURIER_IMPORT.md) in factoring PR365 at head `c9034e4b6a814f624ae38a976ff49ada333158d3`. Its fourth-power local tensor computation is real, but the squarefree local precision does not supply a growing \(3^a\) conductor. Conditioning on the graph label needed by the proposed consumer also prevents reuse of an unconditional average-corank estimate. For the direct Boolean encoding, the graph is injective and unweighted phase averaging erases cross-word interference. These are specific import failures, not impossibility claims about every future encoding.

The [concurrent-interface report](RECENT_CONCURRENT_INTERFACES.md) also integrates source-level findings from Collatz PR218 (signed postcritical flux), PR220 (factor-passage clocks on the sufficient semiprime family), and PR219 (native affine rectangles). It supplies an exact stationary scalar for the signed flux target. None of those inspected inputs proves the needed full joint-window lower bound.

## 5. Routes ruled out with explicit scope

The [single-edge calibration](collision/ONE_EDGE_COLLISION_SPLIT.md) preserves the relevant limiting descent data while changing the collision constant. Thus those data alone cannot close the native arithmetic question. The [actual multiplier rigidity](factoring/MULTIPLIER_CERTIFICATE_RIGIDITY.md) and [high-state spectral bounds](arithmetic/HIGH_STATE_AND_PROFILE_OBSTRUCTIONS.md) constrain proposed short arithmetic merger samplers.

The [Green-tail defect](arithmetic/ANCHOR_GREEN_TAIL_DEFECT.md) identifies the uniform truncation defect with the largest weighted escaping-component Green mass. The [atomic](arithmetic/ATOMIC_ANCHOR_MAJORANT_OBSTRUCTION.md) and [critically damped atomic](arithmetic/CRITICAL_DAMPED_ANCHOR_OBSTRUCTION.md) obstructions close the specified summable atomic majorant classes. Non-atomic real-dependent potentials remain outside those results. The [selected-grade ledger](collision/SELECTED_GRADE_ATTEMPT_LOG.md) shows that identical future words contribute only the vanishing diagonal collision scale.

The dyadic zero-one argument is explicitly credited as prior Paper212. Boundary-energy and single-edge finite controls are not presented as new universal convergence theorems.

## 6. Verification and publication scope

The pass has **74 distinct public theorem roots in twelve Lean modules**, each freshly compiled and separately imported for type and axiom auditing under Lean4.34.1. The final [binding receipt](../../reports/astra-collision-factor-bridge-20261128/final-lean-bindings.json) binds all current sources and reproduction runners to the complete successful audit logs and named root inventories. Only `propext`, `Classical.choice` and `Quot.sound` occur across the packet. The last four-root [MinimumProduct kernel](arithmetic/MinimumProduct.lean) uses only `propext` and `Quot.sound` and retains explicit finite lower-state hypotheses.

Pinned compiled dependencies were reused. This is not a cold dependency rebuild or an independent LeanChecker replay. The analytic source theorems, asymptotic deductions and universal-convergence implications remain written proofs with external inputs. The [positive-predecessor dependency audit](PREDECESSOR_DEPENDENCY_AUDIT.md) reports an incomplete compatibility probe and does not count the external theorem as freshly verified.

Seven scientific checkpoints preserve the work incrementally. Each publication uses the complete frozen repository integrity gate and a matching remote tree, with an expected-parent update and fresh PR-head verification. Checkpoint receipts bind the validator outputs; the final PR description records the last frozen tree and validation result. The checkpoint table in [README](README.md) distinguishes new formal roots and finite experiments from source-qualified mathematics.

The best next proof obligation is the one-copy critical negative-grade lower bound in section1. The best arithmetic alternative is a genuine convergence theorem for the explicitly sufficient semiprime family. Both address the full conjecture; neither was settled during this pass.
