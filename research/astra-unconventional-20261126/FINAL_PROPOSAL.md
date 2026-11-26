# Final proposal: closed arithmetic, open global premises

**OPEN — no full Collatz proof is claimed.** The new ordinary-family return theorems and exact routing theorem are closed formal results. The universal convergence implications remain conditional. This document identifies the precise boundary so the fresh kernel build cannot be mistaken for a proof of the conjecture.

## The existing ordinary merger target

The retained, rebuilt statement is:

```lean
theorem final_proposal (remaining : FrontierMerger) :
    ∀ n : Nat, 0 < n → Good n :=
  universal_iff_frontier_merger.mpr remaining
```

This is the actual theorem in [round eleven's FinalProposal.lean](../astra-global-closure-20261124/round11/formal/FinalProposal.lean), not a newly assumed axiom. The definition of [FrontierMerger](../astra-global-closure-20261124/round10/vendor/SmoothCore.lean) quantifies over every positive odd ternary-unit base \(w\), positive exponent \(r\), and positive odd \(a\) with
\[
 3^rw+1=2^{m+1}a.
\]
On the surviving explicitly specified arithmetic cases, it requires an actual ordinary merger
\[
 T^h(3^rw)=T^k(3^jb),\qquad
 b>0,\qquad b<w\ \text{or}\ (b=w\text{ and }j<r).
\]
The arithmetic guards are
\[
 2^{m+1}\le3^r\quad\text{or}\quad 3^{m+1}a\equiv1,11\pmod{16},
\]
and, when \(r\ge2\), \(3^rw\not\equiv85\pmod{512}\). The exact Lean definition governs these quantifiers and normalizations. The two clocks \(h,k\) are unrestricted and need not agree.

**First unsupported step:** producing this smaller-base or earlier-exponent merger for every supplied surviving tuple. Constructing arbitrarily many examples, selecting a new base after selecting a word, or routing every residue from a very high predecessor does not discharge it.

## What the thirteen new formal families discharge

Write
\[
 \mathcal F(z)=\forall n>0,\;2^{40}n<z\Longrightarrow\operatorname{Good}(n).
\]
The theorem `PhaseFamilies.closed_families`, together with its base, upper-word and canonical-family declarations, proves \(\mathcal F(z_t)\Rightarrow\operatorname{Good}(z_t)\) for all thirteen parameter rows in [PHASE_RETURN.md](renormalization/PHASE_RETURN.md). This is a statement about each supplied ordinary integer in those infinite families, not a changing-witness density claim.

The deduction from a *least canonical reverse disagreement* uses the separately pinned quantitative-return theorem to supply \(\mathcal F(z)\). That source implication is written/reviewed upstream; the new Lean theorem exposes the floor as a hypothesis. No declaration claims that the listed families exhaust all canonical disagreements.

On the bounded bad-cycle alternative, a new exact minimum comparison gives \(s\ge1+(3/4)^r(z-1)\), where \(r=v_3(s-1)\in\{2,3,4,5\}\). Using the stronger floor and smaller canonical return identities, the three-odd upper-hit case has no survivor when \(r=2\); at \(r=3,4,5\) only \(e=6\) remains. The new Lean modules prove the conditional floor, divisibility capture, contracting prefixes, and exact smaller canonical returns. The upstream identification of the bounded branch and the final long-ramp assembly are written deductions. [Precise bounded reduction](renormalization/BOUNDED_RANK_THREE.md)

The remaining \(e=6\) family has
\[
 j=11+162m,\qquad x=2^j-1,\qquad z=(128x-143)/81.
\]
In the remaining bounded case, \(M_j=x\) is the first bad Mersenne and \(3M_j\) is good. Its residue \(31\bmod48\) prevents the smaller raw disagreement from immediately contradicting canonical leastness. The new all-clock first-entry optimization and fixed postpeak bounds apply to possible competitors. They do not construct the needed small competitor at every such supplied \(m\). Upper odd counts beyond three and the first-crossing alternative remain open. The rank-two deadline and synchronized-grade rules already fail on ordinary convergent data. No universal selector based on those rules is proposed.

The separately reviewed [finite-cover theorem](renormalization/FINITE_COVER_BARRIER.md) further excludes a finite cover of this row by the specified fixed-word floor and canonical-query tests. Its all-word reduction is written mathematics; the resulting complete finite classification is independently replayed. It explicitly permits an unbounded selector terminating at each ordinary exponent while failing at the nonordinary ternary limit. Thus it refines the missing construction, without asserting impossibility of a full Collatz proof.

The [positive-Haar extension](renormalization/HAAR_BARRIER.md) shows that these exceptional ternary parameters form a positive-measure set in every sufficiently small ball about 590. The proof uses an exact finite ordinary replay through 5,900,000 and a written inverse-branch first-passage estimate. It rules out identifying all nonterminating ternary controls with finitely many rational points, but supplies no ordinary counterexample and does not decide whether an unbounded selector terminates at every ordinary exponent.

## A possible fixed-component contradiction and its absent construction

Suppose \(C(3y)\) is witnessed at clock \(H_0\) with \(p_0\) odds, while the lower orbit of \(y\) is nonperiodic. If, for arbitrarily large \(g\), there were a positive \(u\) satisfying both
\[
 \begin{aligned}
 T^{h_1}u&=T^{h_1}y,&g+P_{h_1}(u)&=P_{h_1}(y),\\
 T^{h_2}(3u)&=T^{h_2}(3y),&g+P_{h_2}(3u)&=P_{h_2}(3y),
 \end{aligned}
\]
then the exact source-height laws would give
\[
 (4/3)^g\le 3U(y)4^{p_0}/2^{H_0},
\]
an impossibility for unbounded \(g\). The two arms may use different clocks; within each arm the merger and augmented odd grade are synchronized as displayed.

This is a concrete sufficient mechanism for excluding an escaping lower in that disagreement. **The simultaneous-reset existence theorem is not proved.** Existing profinite routing, canonical upper insertions, full signed moment lattices, and labels of coalescing components do not imply the two displayed exact equalities. The ordinary source-minimum laws show why repairing the clocks after the fact can be expensive.

The bounded branch has separate new constraints: a global minimum, good neighbors, oriented tripling pairs, and restrictions on competing inverse clocks. Rational controls show the tested local numerical conditions can coexist, but are not claimed as ordinary counterexamples. No contradiction eliminates every ordinary candidate cycle.

## The retained critical-record consumer

The second rebuilt full-domain implication is

```lean
theorem collatz_of_record_lock_and_cycles
    (lock : RecordLock) (cycles : CycleExclusion) :
    ∀ x : ℤ, 0 < x → ∃ t : ℕ, run 1 t x = 1
```

[Exact definitions and proof](../astra-global-closure-20261124/round13/critical/CriticalRecordRigidity.lean)

`RecordLock` requires every nonperiodic positive source, after one finite shift, to match the actual parity itinerary of one fixed negative rational numerator model at **all** future clocks. `CycleExclusion` requires every positive periodic source to reach one. Neither input is established here. The finite congruence transport and impossibility of an infinite negative match are closed; choosing one rational shadow valid for all time remains open.

The sparse-correction control does not refute `RecordLock`, because it changes the unit carry. It demonstrates that the listed finite/profinite approximations alone cannot justify that inference. The exact pointed spectrum and minimum profile of a hypothetical ordinary escape retain the unit carry and one supplied component, but they produce no contradiction. In particular, a limiting profinite object need not retain the critical average of moving ordinary starting points.

## Decision after the three-hour research pass

The publishable output is the verified finite and formal progress, the independently reconstructed written theorems with their stated hypotheses, and a precise reduction of the remaining alternatives. A full proof would still require either the ordinary `FrontierMerger`, both critical-record inputs, or another complete argument addressing ordinary escape and nontrivial ordinary cycles.

The full moment lattice and the explicit essential spectral disk are useful exclusions of specified proof mechanisms. They are not impossibility theorems for every determinant method, every function space, or every future Collatz approach. The source-qualified analytic estimates remain labeled as such. No missing premise is replaced with an axiom, a finite search, or a probabilistic average.
