# Certified exponent-0.90 predecessor bounds

> **Import verdict: EXTERNAL SOURCE-QUALIFIED; no contradiction found in a full-paper structural audit.** The public checked source is stronger evidence than the manuscript alone, but this repository has not independently rebuilt the Lean closure or replayed the two large payloads.

## Exact theorem surface

For

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

let

\[
\pi_a(x)=\#\{1\le n\le x:T^j(n)=a\text{ for some }j\ge0\}.
\]

For every fixed positive target `a` with `3 ∤ a`, the paper proves:

\[
\pi_a(x)\ge C_a x^{901/1000}
\]

for some `C_a>0` and all sufficiently large `x`, and therefore

\[
\pi_a(x)\ge x^{9/10}
\]

for all sufficiently large `x`. The second statement spends the `1/1000` exponent reserve to absorb the unknown positive constant.

Targets divisible by three are correctly excluded: their only predecessors are the dyadic chain `2^r a`, so their predecessor count is only logarithmic. The final target-reduction argument covers both residue classes modulo three and periodic targets without assuming Collatz convergence.

## What is genuinely new in the proof architecture

The result is not merely a level increase from 15 to 18. It solves an analytic termination problem caused by the advanced `D3` shift `log_2(3)-1>0`.

The proof pipeline is:

1. bounded-predecessor envelopes and the Krasikov–Lagarias difference system;
2. a positive level-18 feasible vector for the no-truncation coefficient program at `lambda=2^(901/1000)`;
3. history-sensitive expansion of nonnegative shifted terms;
4. deletion of dominated lifts, retaining every ordinary survivor;
5. an adaptive fallback chosen from a bounded potential only when all three lifts are dominated;
6. a syndetic irrational-rotation obstruction excluding an infinite legal expansion path;
7. a time-local critical pruning that follows the lift attaining the actual functional minimum;
8. choice-valued retarded induction and transfer from envelopes to every eligible target.

The conceptual innovation is the separation of two roles that a single fixed branch could not safely serve:

- the **full normal form** carries coefficient validity and contains a nonempty family at every auxiliary minimum;
- the **time-local critical pruning** carries the functional inequality by selecting actual minima at the current `(residue,time)`.

Dominated lifts cannot be critical minima because positivity plus path monotonicity would force a strict inequality opposite to the monotonicity of the same envelope. This is the key interface that lets the certificate-selected fallback coexist with function-dependent minimizers.

## Finite certificate surface

At level 18 there are `3^17 = 129,140,163` principal states.

### Coefficient vector

The exact integer formulation uses

```text
Q  = 268435456
A  = 76981049
B1 = 207142911
B3 = 386810365
```

and checks one row per principal state. The imported local checker confirms the three exact coefficient-direction inequalities and the three worked rows in the appendix. The source reports:

```text
rows checked:        129,140,163
failed rows:         0
minimum weight:      1,048,576
maximum weight:      1,859,404,226
minimum row margin:  4,147,742,755
payload bytes:       516,560,652
payload SHA-256:     fc96181c552398be8bbc4c0a47482a53c4ff847059bf7fd4b9be11837ca7c34c
```

### Adaptive potential

The potential takes values in `{0,...,34}`. Along principal motion the adjusted height `H=3s+P` does not increase; along a certificate-selected fallback auxiliary edge it falls by

\[
\delta=5-3\log_2 3>0.
\]

The source reports:

```text
transition inequalities: 215,233,605
failed inequalities:     0
payload bytes:            129,140,163
payload SHA-256:          778584ce7635639ab2a0c7de766f81e8f551b0a52f96ca51eb2bb128c3248f52
```

Nonzero fallback choices are sparse but real: the reported lift counts are `42,561,920`, `484,085`, and `716`. That sparsity is mathematically suggestive: the exceptional states that defeat the globally fixed lift-zero rule may have a compressible 3-adic or automata description.

## Termination argument audit

The most delicate paper-level step is the passage from the bounded potential to global expansion termination.

- Ordinary-survivor records with the same residue have nonincreasing exact shifts by the history-dominance rule.
- Between records, every fallback auxiliary edge consumes at least `delta` of adjusted height, while expanded nodes have nonnegative shift and potential.
- Therefore record-free intervals have uniformly bounded auxiliary length; the record set is forward-syndetic.
- The record shifts have the form `n log_2(3)-q_n` and are classwise antitone over finitely many residue colors.
- The syndetic irrational-rotation lemma rules out such an infinite colored sequence.
- Finite branching plus the absence of infinite paths yields finite normal forms.

The logical interfaces are coherent, and the public formalization reportedly covers the analytic chain. The import found no paper-level quantifier reversal between existence of normal forms, a uniform shift interval, time-local choice, and the retarded induction.

## Trust and reproducibility boundary

The manuscript names worktree commit

```text
0bb368e3b51b980ef5c3b33bb86316e3001c37ac
```

while the public ProofAtlas release identifies immutable checked-source commit

```text
5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f
```

as authoritative for the accepted theorem declarations.

The theorem cone uses standard classical axioms plus two explicitly disclosed generated `native_decide` assertions for the LP and potential checks. Separate exact Python and C++ replays are reported. This is a reasonable layered certificate design, but it is not kernel-only computation and was not independently replayed here.

## Exact limitations

- `901/1000` is feasible, not proved optimal at level 18.
- No infeasibility result is given for a larger exponent or for any neighboring level.
- The potential is a level-specific table, not a uniform construction in `k`.
- The finite normal forms are proved to exist but are not materialized, so the common retardation depth, the prefactor, and target thresholds are not numerically extracted.
- Predecessor abundance is a population statement. It neither controls a fixed forward source nor proves that the predecessor set has positive density.
- The theorem gives no direct `SC*`, `FC*`, ordinary-extraction, or all-orbit conclusion.

## Repository crosswalk

### `SC*`

The resident coefficient-stopping packet fixes one source and asks whether every sufficiently long physical prefix crosses below coefficient one. The predecessor theorem instead fixes a target and counts many sources over all depths. The quantifiers point in opposite directions; no direct implication is available.

The adaptive elimination technique may nevertheless be reusable. Its strongest transferable interface is:

```text
positive feasible coefficients
+ bounded state-dependent fallback potential
+ history domination
=> uniformly retarded time-local choice witnesses.
```

A source-conditioned analogue on the SC surplus/valuation state space would be genuinely relevant.

### Ordinary extraction

The finite potential is a certificate over a complete residue space, not an ordinary positive all-depth seed. It does not cross the repository's extraction firewall. Conversely, its successful use of history and state-dependent choice is evidence that bounded residue-only controllers can be too rigid while modestly enriched adaptive state can succeed analytically.

### Periodic tails and `FC*`

The all-target transfer includes periodic targets, but it does not test complete denominators or exclude cycles. It supplies inverse basin size, not the exact cycle equation.

## Improvement program

### P1. Certify level-18 optimality or a sharper feasible exponent

Run primal and dual exact programs. A dual certificate would distinguish “search stopped” from “level-18 optimum reached.” Search rational exponents on both sides of `0.901`, then preserve the first exact separating dual witness.

### P2. Classify the exceptional adaptive lifts

In each auxiliary family, nonzero selectors occupy `484,801` of `43,046,721` rows, about `1.13%`; lift two appears only `716` times. Recover those indices, inspect their base-three suffixes and transition neighborhoods, and test whether the selector is generated by a short transducer plus a bounded defect counter. A structural classification could replace 129 million potential bytes with a theorem.

### P3. Build a recursive potential family

Search for a relation between level `k` and level `k+3`, since the successful step from 15 to 18 multiplies the state space by 27. Candidate forms include:

- a digit-local base potential plus sparse correction states;
- a max-plus or Bellman fixed point with a level-independent local rule;
- a cohomological potential on the 3-adic inverse-branch graph;
- a finite core with one unbounded carry, consistent with the repository's representation firewalls.

A uniform `P_k` with a fixed fallback loss would convert repeated finite achievements into a structural theorem.

### P4. Materialize and compress normal forms

Memoize the history quotient needed by dominance, enumerate the finite normal forms, and record the maximal terminal depth and shift interval. This would make `nu`, `Delta`, `C_a`, and a target threshold explicit. Hash-addressed DAGs or proof-producing compressed tries should avoid expanding identical subtrees repeatedly.

### P5. Prove an asymptotic LP theorem

The central inverse-density target is not simply another isolated exponent. Prove either:

\[
\lambda_k\to2
\]

for feasible no-truncation bases, giving `x^(1-epsilon)` for every `epsilon>0`, or a stronger positive-density predecessor theorem. A renormalization or subadditivity law across levels would be more valuable than brute-force scaling alone.

### P6. Join the forward exponent race

The synthesis note proves that predecessor exponent `gamma` beats any fixed-height forward bad-set exponent `beta<gamma`. With the current `gamma=0.901`, a forward estimate `O_H(X^beta)` for any `beta<0.901` would close Collatz. Higher inverse exponents relax the required forward power saving.
