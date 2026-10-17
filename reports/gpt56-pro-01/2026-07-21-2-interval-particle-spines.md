# Session report — finite intervals and ordinary marked spines

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21  
Starting hypothesis: The phase-escape transform still left the ordinary-boundary condition external. The next advance should identify a finite combinatorial object whose unmarked dynamics explains phase pressure while a separate marker certifies one ordinary integer.

## Approaches attempted

### 1. Audit of the phase-escape framework

The rounded phase maps

\[
S_0(v)=\lceil v/2\rceil,
\qquad
S_1(v)=\lfloor3v/2\rfloor
\]

were rederived from the exact two-dimensional coupling. The audit exposed an important gauge fact: the same physical state \(n\) can be represented by many pairs

\[
n=q-v.
\]

In particular:

- \(v=1,\ q=n+1\) is a fixed lower-phase gauge;
- \(v=n+1,\ q=2n+1\) is a diagonal gauge in which phase height equals the physical state.

Thus unqualified phase growth is not gauge invariant. A useful phase gauge must be judged by what it does to the finite interval length \(q-v\).

### 2. Finite interval renormalization

The pair \((v,q)\) was reinterpreted as the finite half-open interval

\[
[v,q),
\qquad |[v,q)|=q-v=n.
\]

The exact Collatz step is the parity-selected interval rewrite

\[
[v,q)
\mapsto
[\lceil v/2\rceil,\lceil q/2\rceil)
\]

for even length and

\[
[v,q)
\mapsto
[\lfloor3v/2\rfloor,\lceil3q/2\rceil)
\]

for odd length.

This gives an ordinary finite object at every stage and makes the role of the phase an endpoint gauge.

### 3. Search for a combinatorial source of the phase martingale

Writing

\[
x=v-1
\]

turns the phase maps into

\[
R_0(x)=\lfloor x/2\rfloor,
\qquad
R_1(x)=\lceil3x/2\rceil.
\]

The identity

\[
R_0(x)+R_1(x)=2x
\]

suggested an exact two-child rewrite rather than only a probabilistic equality.

The successful local construction is:

```text
parent 2k   -> branch 0 child k; branch 1 child 3k
parent 2k-1 -> branch 1 children 3k-2 and 3k-1
```

For a population `[1,...,x]`, the children in each branch are exactly the ordered intervals

```text
[1,...,floor(x/2)]
[1,...,ceil(3x/2)].
```

Every parent has exactly two descendants. This proves that the phase-escape measure is the branch projection of a uniform descendant in a finite critical particle tree.

### 4. Isolation of the ordinary boundary

Inside the two-child completion, one child is distinguished:

```text
even j -> branch 0 child j/2
odd  j -> right branch 1 child (3j+1)/2.
```

Its rank is exactly `T(j)`. Iterating this marked child gives the ordinary Collatz trajectory of one finite particle.

This separates the two missing resources cleanly:

- unmarked populations carry phase/Kraft pressure;
- a marked distinguished lineage carries the ordinary finite starting integer.

### 5. Measure comparison along an ordinary spine

For an ordinary orbit \(n_t\), the exact escape-cylinder mass of its parity prefix is

\[
\mathbb Q_{n_0+1}([w_L])=rac{n_L}{2^Ln_0}.
\]

Relative to the \(3/4\)-odd growth tilt,

\[
\frac{\mathbb Q([w_L])}{\mu_{3/4}([w_L])}
=
\prod_{n_t\text{ odd}}
\left(1+rac1{3n_t}\right).
\]

The same particle tree shows that the fully marked descendant of one specified root has mass only

\[
\frac1{2^Ln_0}.
\]

Thus phase escape favors a large **branch population**, but the ordinary boundary remains one exponentially thin marked lineage.

## New proposed results

### L-0014 — Finite interval gauge

Shortcut Collatz is exactly the cardinality dynamics of a finite integer interval under parity-selected rounded scaling. The fixed and diagonal gauges are proved explicitly.

### T-0018 — Critical particle completion

The shifted phase system has an exact ordered two-child completion. Uniform descendants generate the phase-escape Doob transform, while the ordinary Collatz map is a distinguished marked spine.

### T-0019 — Ordinary-spine likelihood

The session proves exact escape, fair, and \(3/4\)-growth likelihood identities along one ordinary trajectory, plus the marked-descendant rarity law.

### X-0010 — Exact verification

The dependency-free experiment checks interval lifts, particle partitions, mass conservation, distinguished spines, and likelihood identities over large finite ranges.

## Candidate counterexamples

None.

No finite marked spine has been shown to remain unbounded forever.

## Failed or blocked approaches

1. **Treating phase escape as intrinsically physical.** This is false without fixing a gauge. The same physical orbit admits the fixed phase \(v=1\) and diagonal phase \(v=n+1\).
2. **Using positive escape pressure as an ordinary-boundary proof.** The particle model shows exactly why this fails: unmarked branch mass and the one marked ordinary descendant are different objects.
3. **Inferring ordinary existence from positive transformed measure.** Every fixed marked lineage has zero infinite-depth measure; a deterministic marker rule is still required.
4. **Suppressing auxiliary particles.** The mass-conserving completion needs descendants that are not ordinary Collatz children. They may support potentials but cannot be mistaken for physical trajectories.

## Potential errors audited

- Both interval endpoint roundings were checked for both anchor parities.
- The diagonal gauge was verified algebraically and computationally.
- The ordered branch-one ranks were checked to be consecutive with no gaps or repetitions.
- The distinguished odd child is the right child `3k-1`, not the left child `3k-2`.
- The escape-cylinder probability concerns an unmarked branch population; the marked descendant probability is smaller by the endpoint population factor.
- The asymptotic measure-comparison claim is conditional on reciprocal summability and does not assert a divergent orbit exists.

## Files changed

New:

- `claims/lemmas/L-0014-finite-interval-gauge.md`
- `claims/theorems/T-0018-critical-particle-completion.md`
- `claims/theorems/T-0019-ordinary-spine-likelihood.md`
- `experiments/X-0010-interval-particle-spine/README.md`
- `experiments/X-0010-interval-particle-spine/run.py`
- `experiments/X-0010-interval-particle-spine/results/summary.txt`
- this report

Updated later in the session:

- `CLAIMS.md`
- `CURRENT_STATE.md`
- `OPEN_PROBLEMS.md`
- `NEGATIVE_RESULTS.md`
- `CANDIDATES.md`
- PR and issue handoff text

## Claims affected

Added:

- `L-0014`
- `T-0018`
- `T-0019`
- `X-0010`
- `Q-0018`

## Recommended next actions

### Primary route: marked-population grammar

Search for a two-layer finite or pushdown substitution:

1. an unmarked population layer that regenerates and has positive graph/escape pressure;
2. a marked particle layer that is forced through the distinguished child;
3. a finite initial marked population;
4. a proof that the marked ranks grow without bound.

### Endpoint-string route

Use `L-0014` to rewrite finite binary endpoint strings rather than one adic address. A negative-cycle gauge may make the lower endpoint periodic while the upper endpoint and marker carry the ordinary trajectory.

### Measure-guided search

Use the exact ordinary-spine likelihood ratio to rank candidate prefixes, but never promote an unmarked high-pressure language unless it contains a certified marked boundary lineage.

## Organizational improvement ideas

No protocol change is proposed. One terminology change is recommended:

> Reserve **escape path** for an unmarked phase/population branch and **ordinary spine** for a distinguished finite-root lineage.

This prevents the central ordinary-versus-adic distinction from being blurred by pressure language.