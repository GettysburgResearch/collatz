# Paired ordinary reductions and the final remaining obligation

**Collatz remains OPEN.** This pass gives new strictly smaller ordinary queries, proves limits on several proposed ways to make those queries universal, and assembles the results in a final Lean proposal with the missing theorem exposed. It does not prove universal convergence.

The main positive result reaches a rank-three family that the preceding uniform search could not handle: thirteen rational-reference rules exclude **17 parameter classes for m modulo 19,683** in the exponent family j=11+162m. A separate finite word bank excludes **55 of the 256 candidate residue classes modulo 12,288**, at every upper rank. These are exact source-specific certificates. Neither fraction measures how much of the Collatz conjecture is solved.

The fresh root build compiled **41 mathematical modules and three audit modules** from source, including twelve new mathematical modules. There were 49 successful compiler invocations, including five final recompiles after three trailing-whitespace removals. The three public audits cover exactly **204 non-private theorems, 52 new**, with dependencies contained in `propext`, `Classical.choice`, and `Quot.sound`. Independent mathematical reviews and exact finite replays accompany the proofs. [Execution and review record](../../../reports/ayh-resource-reset-20261124/paired-reductions/README.md).

## Map and induction target

Throughout, one clock means one application of

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Let \(C(n)\) mean that this ordinary positive orbit reaches 1. The previous [reverse-17 reduction](../directed-return/Residue17Closure.lean) proves that universal convergence is equivalent to the absence of a reverse defect

\[
z\equiv17\pmod{48},\qquad C(3z),\qquad\neg C(z).
\]

If any defect exists, choose its least ordinary value \(z\). The unconditional [bounded-return theorem](../closing-proposal/QuantitativeReturn.lean) takes every positive nonconvergent input \(x\) to a defect at most \(2^{40}x\). Thus either an equivalent lower input below \(z/2^{40}\), or a new smaller defect query \(w<z\), contradicts leastness. The second option needs no factor \(2^{40}\): it must prove both \(C(w)\leftrightarrow C(z)\) and \(C(3w)\).

This is the useful change of induction parameter. A smaller query can have a more complicated upper certificate. The proof orders queries by their ordinary value; it does not require the upper odd count to decrease.

## 1. Rational references supply new smaller queries

The difficult family has

\[
j=11+162m,\qquad81z+271=2^{j+7},\qquad T^7z=2^j-1.
\]

Its upper triple has a three-odd certificate. The signed rational reference \(a=-271/81\) reaches \(-1\) after seven clocks with four odd inputs, while \(3a\) reaches zero after nine clocks with three odd inputs. These references describe exact affine words on a positive source when the required binary precision is present.

Choose a second reference \(b=-B/3^d\), whose lower word reaches \(-1\) after \(s\) clocks and whose upper word reaches zero two clocks later. The checked rows give an actual positive integer \(w\) satisfying

\[
3^d w=2^{j+s}-B,\qquad
T^s w=T^7z=2^j-1,\qquad
T^{s+2}(3w)=2^{j-2},
\]

with \(w\equiv17\pmod{48}\) and \(w<z\). The common lower value proves \(C(w)\leftrightarrow C(z)\), and the upper power of two proves \(C(3w)\). This excludes the supplied \(z\) as a least defect.

[MersenneTwoCenter.lean](MersenneTwoCenter.lean), `progress` and `least_excluded`, prove thirteen full progressions. Two have period \(6561\), and eleven have period \(19683\); they give seventeen disjoint classes at the common period. For example,

\[
m=5903+6561t,\quad d=12,\quad B=2692031,\quad s=18
\]

works for every natural \(t\), with no bound on the original source. The independent replay checks both the first and next member of all thirteen progressions by direct ordinary iteration, including an exponent \(j=5{,}350{,}871\). The all-parameter result comes from the Lean proof, not these samples.

[SignedCycleDilation.lean](SignedCycleDilation.lean) also proves a general paired lift from a common signed reference, including the explicit \(-1183\) contraction. [DifferentCycleAnchors.lean](DifferentCycleAnchors.lean) aligns distinct references \(-1807\) and \(-127\), giving

\[
z+1807=1610612736t,\qquad w+127=75497472t.
\]

The displacement ratio is \(3/64\), and both lower and upper basin labels agree. The lower and upper arms may enter different signed cycles. The complete derivations, row data, and exact limitations are in [SIGNED_ROUTES.md](SIGNED_ROUTES.md).

## 2. A finite reduction bank valid at every upper rank

[GuardedResidueCover.lean](GuardedResidueCover.lean) contains sixteen literal affine word certificates. Eleven join the two original arms by ordinary paths. Five also use a tripling query only after proving that its input is a smaller positive residue-17 candidate. Such a query is justified by leastness at that smaller input.

The kernel computes the exact census: **55 of 256** possibilities for \(z\equiv17\pmod{48}\) modulo \(12288\) are excluded. The remaining 201 classes are not declared safe. In particular, the difficult family in Section 1 lies in the uncovered class \(3233\pmod{12288}\); its new rational-reference certificates add a different kind of progress.

## 3. Exact restrictions on a surviving least defect

[OddClockFloor.lean](OddClockFloor.lean) kernel-checks convergence for the integers 1 through 2719, then proves a multiplicative bound along any positive nonconvergent orbit. If \(q\) is its actual odd count through clock \(h\), then for every \(B\le2720\),

\[
B^q2^hT^h(x)\le(3B+1)^q x.
\]

Together with the uncorrected lower bound, this gives exact equivalences on such an orbit:

\[
2^{40}T^{1024}(x)<x\quad\Longleftrightarrow\quad q\le620,
\]

and, when \(x=3^r w\) with \(w>0\),

\[
T^{1024}(x)<w\quad\Longleftrightarrow\quad q+r\le646.
\]

[DefectClockFloor.lean](DefectClockFloor.lean) attaches this to the original least defect. A survivor must have at least 621 odd inputs in its first 1024 clocks and must satisfy

\[
B^q2^h\le(3B+1)^q2^{40}
\]

at every clock and every \(B\le2720\). These statements have no lower size cutoff on the nonconvergent source. A small fraction of a complete parity grid passes the necessary test; this does not rule out an individual exceptional source.

The latest tower results in PRs 192, 195, 208 and 209 were compared at frozen heads. Their tower exponent \(r\), actual upper first-hit odd count \(R\), and ordinary comparison clocks are distinct quantities. Selected simultaneous success for many tower exponents supplies no universal certificate at an arbitrary fixed base. The exact source and claim comparison is in [TECHNICAL_NOTE.md](TECHNICAL_NOTE.md) and [SOURCES.json](SOURCES.json).

A second live refresh before publication found new heads for PRs 192, 195 and 206. The new PR206 theorem is stronger than selected-base success: for **every fixed odd base** and every starting rank, it finds a later block of 513 consecutive tower vertices with a common endpoint after 1381 clocks. Its offset may be as large as \(2^{1379}\), and the endpoint is below the first vertex of that later block. It does not place the endpoint below the original base. Its recurrence criterion still requires a rank-zero basin disagreement to recur in every 512-edge window. Our least reverse defect supplies the initial disagreement, but no result supplies that recurrence. The new PR192 height slice misses both displayed difficult families at its required threshold; the new PR195 whole-denominator criterion still requires exclusion of every admissible nontrivial cycle word. [Live source comparison](../../../reports/ayh-resource-reset-20261124/paired-reductions/LIVE_SOURCE_SYNTHESIS.md).

## 4. What the attempts to make the construction universal established

### Upper rank cannot determine a forward stopping deadline

[FixedRankDeadlines.lean](FixedRankDeadlines.lean), `no_rank_deadline`, proves that for every fixed \(R\ge3\), every deadline \(H\), and every size cutoff \(L\), there is a single ordinary \(z\ge L\) whose triple **first** reaches 1 with exactly \(R\) odd inputs, but whose lower orbit has an arbitrarily long expanding odd prefix after clock seven. More precisely, for some \(q\ge H\),

\[
z\le128T^i(z)\qquad(0\le i\le7+q).
\]

Consequently, no deadline depending only on \(R\) can guarantee the required forward drop. A clock depending on the actual source or a different ordinary merger remains possible. These constructed examples are not claimed to diverge.

### The specified rational-center language misses an ordinary source

At \(m=0\), the source in Section 1 is \(z=3233\). [CenterPhaseObstruction.lean](CenterPhaseObstruction.lean) proves that none of the 67 smaller positive candidates \(w\equiv17\pmod{48}\) ever reaches any of the twelve target phases

\[
2^{11-u}3^u-1,\qquad0\le u\le11.
\]

The result quantifies over every clock. The finite kernel computation reaches 1 and then uses the proved \(1,2\) cycle to exclude every later clock. It therefore rules out all denominator depths within that particular phase-aligned smaller-query mechanism at this source. The parent itself converges in 107 clocks, so this is a failed coverage claim, not a Collatz counterexample.

A separate **written** theorem, with an independently reviewed proof and a kernel-checked final contradiction, controls arbitrarily large sources: if \(3^k\mid m>0\), a valid shrinking rational-center query must use denominator exponent \(d\ge k+5\), or at least twelve extra lower odd inputs after denominator clearance. All thirteen positive rows have zero such extra inputs. [CENTER_PHASE_OBSTRUCTION.md](CENTER_PHASE_OBSTRUCTION.md) states the exact normalization and scope. A growing-depth or longer-word search is not excluded.

### The two checkpoint comparisons need genuinely more information

For the other rank-three Mersenne row, the earlier least-defect argument forces two bad checkpoints with ternary exponents q,s below the first bad Mersenne exponent j. [CheckpointUnitExit.lean](CheckpointUnitExit.lean) proves their exact normalized exits and their attachment to earlier ordinary Mersenne trajectories. The full simultaneous-delay argument is a **written**, independently reviewed proof in [SIMULTANEOUS_CHECKPOINT_DELAY.md](SIMULTANEOUS_CHECKPOINT_DELAY.md).

For \(v\ge128\), \(v\equiv4\pmod{27}\), \(d=v_2(v)>0\), put \(W=3^{2v}\). There are 32 known-good earlier Mersenne trajectories associated with \(W^i-1\), \(1\le i\le32\). The **written** theorem in [THIRTY_TWO_ORDINARY_COMPARISONS.md](THIRTY_TWO_ORDINARY_COMPARISONS.md) proves that, through \(v\) clocks from a normalized bad checkpoint and \(v\) clocks after a comparator's peak, only its matching degree, 21 or 22, can meet it; the comparison clock is forced. Every one of the 32 initial ascents is also excluded through \(v\) source clocks. The much larger menu reduces to two possible comparisons over this range. Both can succeed at particular supplied sources; no guaranteed success for every fixed cofactor was found.

The earlier ternary rescue bank still applies to some of these same parents. [ShadowTernaryDigits.lean](ShadowTernaryDigits.lean) proves that the special binary family visits every ternary residue. [ShadowTernaryRescue.lean](ShadowTernaryRescue.lean) attaches an existing rescue progression to the exact supplied parent. It does not increase the earlier bank's 1000-of-59049 coverage count.

## 5. Aaronson–Yolcu–Heule and the choice of next theorem

[Yolcu, Aaronson and Heule](https://emreyolcu.com/research/rewriting-collatz.pdf) motivate the exact mixed-base word approach: termination of their full system would settle Collatz. A new primary-source check of [Nashida's matrix-interpretation barriers](https://github.com/harappa/collatz-arctic-interpretation-barriers/tree/de961be6671b2084ae0189a3572b674c60788456) reinforces a specific limitation: the specified natural-number and arctic matrix interpretations, in arbitrary dimension and under their stated admissibility conditions, cannot make the required progress on the full system. That external repository was inspected, not rebuilt here. Its scope does not exclude general rational, real, polynomial, lexicographic, or transformed-system methods.

The positive paired queries above use exact word identities, ordinary positivity and a smaller ordinary input. They avoid needing one of those static interpretations. Their missing ingredient is a **well-founded, source-specific extension rule**: on a surviving source, either produce a valid smaller query or prove that a prescribed search measure decreases until such a query is reached. Merely solving the abstract cycle-alignment equations, finding success on arbitrarily large other sources, or obtaining a small exceptional proportion does not supply that rule.

## 6. Final Lean proposal and first unproved step

[ClosingProposal.lean](ClosingProposal.lean) gathers every proved exclusion into `SurvivingCase z j`. It requires the same least reverse defect, an actual upper hit of rank at least three, avoidance of the previous tail and Mersenne cases, avoidance of all newly proved query cases, and the exact clock constraints above.

The final interface is:

```lean
def RemainingExclusion : Prop :=
  ∀ z j : Nat, SurvivingCase z j → False

theorem collatz_from_remaining
    (remaining : RemainingExclusion) : UniversalConvergence

theorem collatz_iff_remaining :
  UniversalConvergence ↔ RemainingExclusion
```

Both the consumer and equivalence are proved and audited. **`RemainingExclusion` is unproved.** It is the first unsupported step in a complete proof. The file adds no axiom asserting it, and no density or selected-source result is silently substituted for it.

## Reproduction and evidence boundaries

Use Lean **4.34.1**, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. With `LEAN` pointing to that compiler and `LEAN_PATH` containing the pinned Mathlib dependency objects, run:

```sh
bash research/ayh-resource-reset-20261124/paired-reductions/check_lean.sh
```

The script creates a fresh temporary directory and rebuilds every repository-local dependency before use. The actual run in this pass was split into the recorded baseline, new-module, final-assembly and formatting batches; their paths, hashes, outputs and timings are retained separately. The last batch recompiles two modules after trailing-whitespace removal and their affected closing consumers. The six finite replay programs passed both normal and optimized Python execution with matching outputs. Details, independent reviews and hash manifests are in the [report directory](../../../reports/ayh-resource-reset-20261124/paired-reductions/README.md). Repository integrity validation is a separate clean-checkout event, recorded against the published commit in PR197.
