# Session report — negative-phase coupling, padded towers, and renewal pressure

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21  
Starting hypothesis: The negative-template program should be resolved one shortcut step at a time. The intended structure was a finite negative phase together with one unbounded valuation or cycle-padding counter, rather than another flat collision alphabet.

## Approaches attempted

### 1. Exact synchronous coupling

Write an ordinary physical state as

\[
n=q-v,
\]

where \(-v\) is a moving ordinary negative reference state. Comparing the parity of \(q\) with the parity of \(v\) produced an exact four-case update for the pair \((q,v)\).

Even \(q\) keeps the physical orbit parity-aligned with the negative reference. Odd \(q\) is precisely a mismatch and sends the reference through a complementary branch.

### 2. Valuation acceleration

The exact valuation

\[
k=\nu_2(q)
\]

counts how long the physical trajectory shadows the negative phase before its first mismatch. Accelerating through these \(k\) synchronized steps gives a complete countable partition indexed by \(k\).

### 3. Negative-cycle padding

When the phase lies on a negative cycle, the valuation decomposes into a phase type modulo the cycle length plus a nonnegative padding counter. Every complete synchronized cycle circuit multiplies a return edge's real slope by the supercritical negative-cycle multiplier.

### 4. Complement-basin atlas

The complementary branch was computed at every phase of the negative eleven-cycle. After a bounded synchronized recovery, each complement phase enters either the same eleven-cycle or the negative three-cycle. Complements of the three-cycle then enter the negative fixed phase.

### 5. Prefix-code probability and thermodynamic pressure

A complete parity renewal code was examined simultaneously under fair parity measure and the Bernoulli measure with odd probability \(3/4\). This exposed the exact multiplier as a likelihood ratio and yielded two Kraft identities, mean multiplier one, and strictly negative typical logarithmic drift.

### 6. Routes considered but not promoted

- Directly treating all high-padding edges as a completed renewal grammar. The exact towers do not cover a forward-invariant ordinary set.
- Interpreting positive mean edge multiplier as typical growth. The Kraft calculation shows that complete coverage instead has negative typical log growth.
- Assuming the complement basin remains inside the eleven-cycle. Seven phase types descend to the negative three-cycle, and that cycle's complements descend to the fixed phase.

## New results

### T-0014 — Synchronous negative-phase coupling

For \(n=q-v\), with

\[
p=q\bmod2,
\qquad r=v\bmod2,
\qquad e=p\oplus r,
\]

one shortcut step is exactly

\[
q'=\frac{3^eq+p}{2},
\qquad
v'=\frac{3^ev+(2p-1)r}{2},
\]

and

\[
T(q-v)=q'-v'.
\]

If \(q\) is even, the phase follows its ordinary negative Collatz orbit. If \(q\) is odd, the phase takes the complementary branch.

The first mismatch after \(k=\nu_2(q)\) synchronized steps has a closed accelerated formula.

### T-0015 — Cycle-padded mismatch towers

A negative cycle of period \(\ell\), odd count \(a\), and multiplier

\[
\Lambda=3^a/2^\ell>1
\]

turns every fixed mismatch/recovery type into a countable geometric tower. Padding by \(t\) complete cycle circuits changes the edge multiplier by

\[
\lambda_t=\lambda_0\Lambda^t.
\]

Each tower consists of disjoint exact-valuation cylinders and becomes supercritical after finitely many padding levels.

### O-0008 — Complement-basin atlas

For the negative eleven-cycle, complement branches from seven phases enter the negative three-cycle at phase \(7\), while complements from four phases return to the eleven-cycle at phase \(34\).

From phase \(136\), the grouped base return systems are:

\[
T^9(q-136)=q'-7
\]

on seven residue classes modulo \(512\), with three odd steps, and

\[
T^{13}(q-136)=q'-34
\]

on four residue classes modulo \(8192\), with seven odd steps.

After cycle padding, these two families first become supercritical at levels \(45\) and \(21\), respectively.

### T-0016 — Collatz–Kraft martingale

For every complete binary prefix code,

\[
\sum_w2^{-|w|}=1
\]

and

\[
\sum_w\frac{3^{a(w)}}{4^{|w|}}=1.
\]

Thus, under fair cylinder probabilities,

\[
\mathbb E\left[\frac{3^{a(w)}}{2^{|w|}}\right]=1.
\]

The multiplier is exactly the likelihood ratio

\[
\frac{\mu_{3/4}([w])}{\mu_{1/2}([w])}.
\]

When the mean codeword length is finite,

\[
\mathbb E[\log\lambda]
=\frac12\log(3/4)\,\mathbb E[L]<0.
\]

Complete renewal coverage therefore has mean multiplier one but negative typical logarithmic drift. Every positive-growth survivor language is Haar-null.

The graph-directed pressure matrices

\[
\mathcal A_s(i,j)
=\sum_{e:i\to j}2^{-L_e}\lambda_e^s
\]

separate fair 2-adic coverage from real growth pressure.

### X-0008 — Exact verification

The experiment checks:

- the synchronous formula for \(1\le v\le300\), \(1\le q\le1000\);
- valuation acceleration for all selected negative-cycle phases and \(q<5000\);
- every complement-basin row;
- the first four padding levels for every phase type;
- direct physical Collatz iteration and signed displacement identities;
- the exact supercritical thresholds \(45\) and \(21\);
- the Kraft identities and negative log-drift formula on a nonuniform complete prefix code.

## Candidate counterexamples

None.

No finite starting integer is claimed to follow a closed infinite renewal grammar.

## Failed or blocked approaches

1. **High-padding edges as a finished solution.** Each edge family is exact and eventually expanding, but no invariant selection rule keeps one ordinary orbit in the accepted towers forever.
2. **Typical-growth interpretation.** Complete renewal coverage has negative typical logarithmic drift, despite mean multiplier one.
3. **Single-cycle closure.** Complement mismatches may descend through the hierarchy eleven-cycle → three-cycle → fixed phase.
4. **Coverage by finite supercritical returns.** The prior one-target obstruction remains; the new towers are countable rather than finite, but ordinary-boundary closure is still unproved.

## Potential errors audited

- Every coupled formula was checked against the physical state \(q-v\), not only symbolically.
- Exact valuation, not a lower bound, determines the synchronized shadow length.
- The recovery congruence is stated explicitly; failure creates another mismatch and is not silently ignored.
- The Kraft identities concern complete prefix partitions; they are not asserted for arbitrary incomplete libraries.
- Haar-null is not interpreted as empty.
- The graph pressure framework is a diagnostic and criterion, not an existence proof.

## Files changed

New:

- `claims/theorems/T-0014-synchronous-negative-phase-coupling.md`
- `claims/theorems/T-0015-cycle-padded-mismatch-towers.md`
- `claims/theorems/T-0016-collatz-kraft-martingale.md`
- `claims/observations/O-0008-negative-cycle-complement-atlas.md`
- `experiments/X-0008-cycle-coupling-kraft/README.md`
- `experiments/X-0008-cycle-coupling-kraft/run.py`
- `experiments/X-0008-cycle-coupling-kraft/results/summary.txt`
- this report

Corrected:

- `claims/theorems/T-0013-graph-directed-return-criterion.md`
- `claims/observations/O-0007-negative-136-cycle-chart.md`

Updated at session end:

- `CLAIMS.md`
- `CURRENT_STATE.md`
- `OPEN_PROBLEMS.md`
- `NEGATIVE_RESULTS.md`
- `CANDIDATES.md`
- `NOTATION.md`
- draft PR #3 and Issue #2 handoff

## Claims affected

Added:

- `T-0014`
- `T-0015`
- `T-0016`
- `O-0008`
- `X-0008`
- `Q-0014` through `Q-0016`

## Recommended next actions

### Primary route: finite phase plus padding stack

Use the finite complement-basin graph as control state and the cycle-padding integer as a stack symbol. Search for a substitution or pushdown rule that maps accepted high-padding edges to accepted high-padding edges and contains one explicit ordinary starting quotient.

### Pressure-directed search

For every candidate subgrammar, compute both

\[
\rho(\mathcal A_0)
\quad\text{and}\quad
\rho(\mathcal A_1).
\]

Reject large libraries that merely reproduce complete negative typical drift. Favor exceptional sublanguages with small fair mass, positive cycle growth, and a certifiable ordinary boundary.

### Multi-mismatch automaton

Extend the complement atlas beyond one mismatch. A failed synchronized recovery causes another mismatch; treating this as a transition rather than a failure may close a finite automaton over phase types.

### Ordinary-boundary criterion

The remaining nonlocal problem is to prove that a finitely generated exceptional language contains one finite ordinary integer rather than only a 2-adic path. This should be developed in parallel rather than postponed until the grammar is complete.

## Organizational improvement ideas

Add pressure data to future renewal-edge certificates:

```text
source phase
target phase
cylinder length
odd count
real multiplier
fair mass 2^-L
tilted mass 3^a/4^L
padding rule
ordinary-boundary status
```

No change to the repository operating model is proposed.
