# A finite triadic certificate with one amortized height budget

Checkpoint 16, 23 November 2026. **Full Collatz remains OPEN.** The strongest
new result is a Lean-checked finite closing theorem for one fixed signed
triadic candidate. A single integer potential pays for every denominator
drop, removing the earlier multiplication of numerator height by denominator
exponent. The universal construction of a successful candidate remains open.

This checkpoint pursued four coordinated attacks: that construction,
entropy rigidity for the actual boundary law, complete numerical cycle
cancellation, and the common pressure maximum's optimal ancestry. The
last three did not produce a closing estimate. Their precise attempts and
an exact obstruction to the balanced-word bridge are retained below.

## 1. The concrete finite theorem

Use the ordinary shortcut map `T(n)=n/2` for even n and `(3n+1)/2` for odd n.
Fix an ordinary positive integer n and a single rational candidate `a/3^r`,
where a is any signed integer and r is nonnegative. Define

\[
 F(r)=\prod_{j=0}^{r-1}(1+3^j),\qquad
 B=n\max(1,|a|)F(r),\qquad E=\operatorname{bl}(B),\qquad H=9E+1.
\]

Here `bl(B)` is the least positive E for which `B<2^E`; equivalently it is
`1+Nat.log 2 B` for positive B. Run the literal paired trajectory specified
in the [complete proof](TRIADIC_AMORTIZED_BUDGET.md). At each step the
candidate must have parity opposite to the original orbit's current state.

**If the first H tests all pass, the original orbit reaches 1 by H.**
This is a finite premise, with the horizon computed from the unchanged
initial source and candidate. There is no all-time compatibility premise,
cycle-exclusion premise, or presumed drift estimate.

The main formal declaration is

```text
CollatzTriadicBudget.finite_triadic_height_certificate
```

in [TriadicAmortizedBudget.lean](lean/TriadicAmortizedBudget.lean). It
computes E, checks the explicit finite compatibility premise, and concludes
that the literal ordinary orbit reaches one. All 22 new theorem declarations
and four definitions are covered by [the audit](lean/TriadicAmortizedAudit.lean).
The exact paired-state dependency is copied unchanged from PR178 at
`4e204f54136c79cf8c9393b34e3330594f99ae0a`; its source hash is bound in
[SOURCES.json](SOURCES.json).

### What changed in the proof

At state `(x,w,r)`, with candidate `w/3^r`, use one potential

\[
                         P=x|w|F(r).
\]

An ordinary odd nonterminal step contracts P by at least a factor `5/6`.
An ordinary even step at positive denominator exponent contracts it by at
least `1/4`, even when the numerator grows or changes sign. At denominator
zero the only tie is `w=1`; the next compatible nonterminal step contracts.
Thus every two nonzero nonterminal steps contract by `5/6`, and eight
steps strictly halve the positive integer potential. A zero numerator has
its own finite divisibility bound, paid by the same initial height. Both
the zero case and the finite horizon are included in the Lean theorem.

Since

\[
 \log_2F(r)=\tfrac12r(r-1)\log_2 3+O(1),
\]

the new sufficient horizon is

\[
                 O(\log n+\log\max(1,|a|)+r^2).
\]

The preceding PR178 horizon was
`8 bl(n)+(9r+8) bl(max(1,|a|,3^r))+2`.
The new numerator-height cost is additive. Either certificate may be used
when its numerical horizon is shorter; no pointwise improvement for every
parameter choice is claimed.

## 2. The arithmetic construction still needed

For the actual first K shortcut bits `e_i`, let `b_K` count even inputs and
let the complete complementary carry be

\[
 D_0=0,\qquad D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i.
\]

It is enough to construct, for every fixed positive n, signed a and
nonnegative r and K such that

\[
 K\ge9\operatorname{bl}\bigl(n\max(1,|a|)F(r)\bigr)+1,
 \qquad 2^K\mid 3^{b_K}a+3^rD_K.
\]

The endpoint congruence forces every preceding complementary parity by
inverting that same affine word over rationals with odd denominators.
This congruence bridge and the logarithmic asymptotic are independently
reviewed written arguments. The Lean capstone takes the finite literal
parity checks as its premise; it does not formalize the endpoint-congruence
bridge or construct a candidate.

The [standalone two-carry question](TWO_CARRY_CONSTRUCTION_QUESTION.txt)
states the construction entirely in finite integer arithmetic. Its first
divisibility condition retains the original positive input; its second
retains the complete complementary carry. A universal proof would settle
the full convergence statement. The question is a handoff target, not a
solved lemma or an independently weaker problem.

The construction attempt tested coupled carries, rational reconstruction,
and the polynomial conjugacy in Monks's 2025 q-analog paper. For that
conjugacy the polynomial degree is exactly the first-hit clock, when
convergence is already known. No independent polynomiality theorem or
sufficient small-residue estimate was obtained.

## 3. What the other full attacks established

| Attack | Result of this pass | Remaining closing step |
|---|---|---|
| Actual-boundary entropy | [Exact graph-directed equation and source-law analysis](BOUNDARY_RIGIDITY_ATTEMPT.md). The high-trace part has mass tending to one uniformly over the moving inverse clock. A fixed nondegenerate independent reference has a linear relative-entropy cost. These are explicitly credited corollaries of existing retracing identities. | Prove the critical collision upper bound on that same actual high-trace law, or supply a valid convolution/scenery structure and its quantitative transfer. |
| Common pressure maximum | [Every later target inherits an all-depth coefficient optimum](OPTIMAL_ANCESTOR_BALANCE.md), directly from PR182's root. An exact ordinary control shows that such an optimum does not force balance. | Use a genuinely infinite property or an admissibility-preserving arithmetic comparison to defeat the actual optimal ray. |
| Complete cycle denominator | [Tao's additive cubes, affine-walk cutoff and extremal words](FULL_CYCLE_LITERATURE_ATTEMPT.md) were tested against the unchanged full denominator. | Bound the actual complete-carry zero fibre strongly enough to exclude all rotations of a primitive cycle. |

The optimizer control is particularly concrete: source 31 is the unique
coefficient maximizer over **every** positive odd unit ancestor at **every**
depth for each target in

\[
31\to47\to71\to107\to161\to121\to91.
\]

Yet the shortcut word `11111010` is unbalanced. At the last target,
`91/32=728/256<729/256` excludes every source at least 32 at once; ten
explicit smaller-source trajectories complete the proof. The example
converges and makes no claim about an infinite escaping ray. A separate
fixed-target control shows that balancing the gaps `(1,2,3)` to `(2,2,2)`
changes the integer source 11 into `283/27`.

## 4. Literature and evidence boundaries

The primary statements inspected include Monks--Yazinski's autoconjugacy
theorem, Monks's polynomial q-analog theorem, Hochman's inverse entropy
theorems, Hochman--Shmerkin's separate-invariance projection theorem,
Tao's Littlewood--Offord discussion, and the stated extremal-word objective.
The attempt notes give exact URLs and access scope. None of these sources
is silently promoted into the missing Collatz construction, independence,
or numerical-cancellation assertion.

The [execution and review record](../../../../reports/2026-11-23-triadic-height/README.md)
records fresh strict Lean compilation, the exhaustive new-declaration axiom
audit, exact finite controls, and source hashes. Its independent written
review covers the signed numerator, zero entry, finite zero tail, and
endpoint-congruence consumer. The repository gate is a separate integrity
check. No historical research corpus or expensive prior census was rerun.

Earlier work remains in [checkpoint 15](../integer-boundary/README.md).
