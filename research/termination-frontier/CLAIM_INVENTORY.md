# Noncanonical claim inventory: termination frontier

This inventory permanently reserves the identifiers used below in the
`*-9000` range for issue #5. It is not the repository's canonical `CLAIMS.md`.
An integrator should index or alias these stable identifiers after the competing
bootstrap branches settle, without silently renumbering them.

Only `L-9001` and `R-9001` contain complete arguments in this port. Their status
is `PROPOSED`, not `PROVED`, until repository review. All stronger legacy results
listed in the companion README are provenance and may not be cited as proved
dependencies.

---

## L-9001: Canonical match heights are unbounded

**Claim ID:** L-9001
**Title:** Canonical match heights are unbounded for the binary--ternary swap
**Status:** PROPOSED
**Authoring agent:** `gpt56-termination-01`
**Reviewing agents:** none in this repository
**Created:** 2026-07-21
**Last updated:** 2026-07-21
**Dependencies:** definition of the standard match lift; the rule `ae -> ea`
**Scope:** standard global match bounds for string rewriting
**Related counterexample candidates:** none

### Statement

Give each symbol an initial height 0. In the standard match lift, an application
of `ae -> ea` to `a_i e_j` labels both new right-hand symbols with

$$
 h=1+\min(i,j),
$$

while symbols outside the redex retain their heights. Then for every `n >= 1`
there is a lifted derivation

$$
 c_0a_0^ne_0^nd_0\;\longrightarrow^*\;
 c_0e_1e_2\cdots e_n\,a_na_{n-1}\cdots a_1d_0.
$$

Consequently the standard match height is unbounded on derivations starting
from canonical mixed-radix strings. In particular, no ordinary finite global
match bound proves termination of the full Collatz string-rewrite system.

### Definitions

Subscripts are match heights, not extra alphabet symbols. A *canonical string*
here means a delimiter-bounded word of the form `c a^n e^n d`, which is within
the syntactic family used by the mixed-radix system. A global match bound `B`
would bound every height in every lifted derivation by `B`.

### Motivation

Match bounds are a standard termination technique. This claim identifies an
exact reason the ordinary version cannot close the AYH system, so future work
must add relative phases, semantic information, context, or a different
encoding.

### Proof

Ignore the unchanged delimiters. We prove by induction on `k`, for
`0 <= k <= n`, that `a_0^n e_0^n` rewrites to

$$
 e_1e_2\cdots e_k\,
 a_k^{\,n-k+1}a_{k-1}a_{k-2}\cdots a_1\,
 e_0^{\,n-k},                                      \tag{1}
$$

where for `k=0` the displayed word is interpreted as `a_0^n e_0^n`.

The base case is immediate. Suppose (1) holds for `k<n`. Move the leftmost
remaining `e_0` leftward across the block

$$
 a_k^{\,n-k+1}a_{k-1}\cdots a_1.
$$

When `k=0`, moving `e_0` across all `n` copies of `a_0` creates a travelling
`e_1` and `n` copies of `a_1`, giving (1) for `k=1`.

Now take `1 <= k < n`. From right to left, the crossing order is
`a_1,a_2,...,a_{k-1}`, followed by the `n-k+1` copies of `a_k`; the first list
is empty when `k=1`. Crossing `a_r e_{r-1}` creates `e_r a_r`, so after the
first list the travelling symbol has height `k-1`. Its first crossing with the
rightmost `a_k` creates `e_k a_k`. There remain `n-k` copies of `a_k`;
crossing the first creates height `k+1`, and all later crossings preserve height
`k+1` because `1 + min(k,k+1) = k+1`. Thus they create exactly `n-k` copies
of `a_{k+1}`. The resulting word is (1) with `k+1`.

At `k=n`, (1) is

$$
 e_1e_2\cdots e_n a_na_{n-1}\cdots a_1,
$$

which contains height `n`. Since `n` is arbitrary, no finite global bound
exists. The derivation uses a rule of the full system, so adding the other rules
cannot remove these reachable lifted derivations. QED.

### Dependency audit

The proof uses only the match-lift definition and `ae -> ea`. It does not use
Collatz convergence, a parity heuristic, or termination of another subsystem.

### Gap audit

- The conclusion is about the ordinary global match-bound criterion, not every
  method containing the words “match bound.”
- Unbounded match height does not imply a nonterminating rewrite sequence.
- The argument gives one family of legal derivations; it makes no claim about a
  preferred rewrite strategy.
- If a tool uses a different annotation update than `1 + min`, this theorem
  must not be applied without proving equivalence of conventions.

### Adversarial tests

For `n=1`, `a_0e_0 -> e_1a_1`. For `n=2`:

```text
a0 a0 e0 e0
-> a0 e1 a1 e0
-> e1 a1 a1 e0
-> e1 a1 e1 a1
-> e1 e2 a2 a1
```

Both match the formula.

### Remaining uncertainty

The mathematical induction is complete for the stated lift. A reviewer should
confirm that the intended external match-bound tool uses precisely this
annotation convention before importing the result into a tool-specific ledger.

### Suggested next attack

Try a relative or semantically labelled match bound whose measure discounts the
forced carry-sorting family rather than raising the global annotation ceiling.

---

## R-9001: Weak-component membership does not imply a cycle-minimum bound

**Claim ID:** R-9001
**Title:** Refutation of the cycle-minimum inference from weak connectivity
**Status:** PROPOSED
**Authoring agent:** `gpt56-termination-01`
**Reviewing agents:** none in this repository
**Created:** 2026-07-21
**Last updated:** 2026-07-21
**Dependencies:** definitions of a functional graph, weak component, and cycle
**Scope:** logical inference used in inverse-tree and cycle inequalities
**Related counterexample candidates:** any hypothetical nontrivial Collatz cycle

### Statement

Let the vertices of a functional graph lie in a totally ordered set (in
particular, they may be positive integers). Let `Gamma` be a directed cycle and
let `W` be its weak component. Write

$$
 m_W=\min W,\qquad m_\Gamma=\min\Gamma
$$

when the minima exist. For a vertex `y` in `W`, weak-component membership alone
implies only `y >= m_W`; it does not imply `y >= m_Gamma`. Therefore any
Collatz cycle argument that obtains a sibling bound `y >= m_Gamma` solely from
weak connectivity has an unsupported inference.

### Definitions

A functional graph has one outgoing edge from every vertex. Its weak components
are the connected components after edge directions are forgotten. A sibling or
inverse-tree vertex may lie in the same weak component as a cycle without lying
on the cycle.

### Motivation

Several real-inequality attacks on hypothetical cycles compare off-cycle
siblings with the least cycle state. This comparison is attractive but does not
follow from the minimality notion actually available for a whole component.

### Proof / refutation

The inequality `y >= m_W` is the definition of `m_W`. Since `Gamma` is a subset
of `W`, one has `m_W <= m_Gamma`, but there is no implication in the reverse
direction.

A two-vertex functional graph is a complete countermodel to the proposed
inference: let the vertices be `{1,2}`, with edges `1 -> 2` and `2 -> 2`. The
cycle is `Gamma={2}`, the weak component is `W={1,2}`, and the off-cycle vertex
`y=1` satisfies

$$
 y=m_W=1<2=m_\Gamma.
$$

Thus connectivity alone cannot prove the cycle-minimum bound. QED.

### Dependency audit

No property of Collatz dynamics is used. This is deliberately a logical
refutation: a Collatz-specific lemma could still establish the stronger bound,
but it would require additional arithmetic proof.

### Gap audit

- The countermodel is not claimed to be a Collatz component.
- The result does not prove that a hypothetical Collatz cycle has a smaller
  off-cycle sibling.
- It refutes only derivations whose sole premise is weak-component membership.

### Adversarial tests

If `W=Gamma`, then `m_W=m_Gamma`; this special case does not rescue the general
inference. Adding any in-tree vertex below the cycle minimum reproduces the
countermodel.

### Remaining uncertainty

None for the stated graph-theoretic implication. Any application must be
checked to see whether it uses extra Collatz-specific hypotheses.

### Suggested next attack

For a proposed cycle, derive sibling bounds directly from the exact inverse map
and divisibility constraints. Keep `m_W` and `m_Gamma` as distinct parameters
unless their equality is proved.

---

## Q-9001: Multi-state natural selector frontier

**Claim ID:** Q-9001
**Title:** Can a genuinely multi-state selector complete the natural interpretation?
**Status:** IDEA
**Authoring agent:** `gpt56-termination-01`
**Reviewing agents:** none
**Created:** 2026-07-21
**Last updated:** 2026-07-21
**Dependencies:** prior natural-matrix provenance in the companion README
**Scope:** full AYH mixed-radix system
**Related counterexample candidates:** none

### Statement

Determine whether the surviving three-state target selector can be connected
through an intermediate block with at least two genuinely interacting states so
that every AYH rule is weakly oriented and at least one required rule is strict.
If not, prove a block-flux or Farkas-style obstruction covering all such blocks.

### Definitions

“Genuinely interacting” excludes a direct affine return, a one-state path, dead
transients, and a block triangular decomposition into those already reported
cases.

### Motivation

This is the first natural-matrix mechanism not covered by the prior collapse
arguments; larger blind coefficient sweeps do not isolate it.

### Proof or construction

Open question; none is claimed.

### Dependency audit

The claim that smaller cases collapse is provenance only in this branch and
must be imported before a negative solution can cite it.

### Gap audit

The existence of a finite satisfying model would still require a complete,
independently checked termination certificate and an audit of strictness,
monotonicity, contexts, and all eleven rules.

### Adversarial tests

First recover the three-state tuple model and reproduce the known one-state
Farkas circuit exactly; this is a dependency check, not a parameter sweep.

### Remaining uncertainty

Both existence and impossibility are open in this packet.

### Suggested next attack

Encode symbolic block-sum flux for a two-state strongly connected intermediate
block before choosing numerical coefficient bounds.

---

## Q-9002: Arctic interacting transient return

**Claim ID:** Q-9002
**Title:** Can an interacting transient return carry strict marked visibility?
**Status:** IDEA
**Authoring agent:** `gpt56-termination-01`
**Reviewing agents:** none
**Created:** 2026-07-21
**Last updated:** 2026-07-21
**Dependencies:** prior arctic critical-saturation provenance in the companion README
**Scope:** arctic interpretations of the AYH system
**Related counterexample candidates:** none

### Statement

Determine whether a transient strongly connected return that interacts with the
critical `PQ/QP` core can make a marked rule strict while preserving all weak
orientations. Alternatively prove a saturation theorem that propagates
critical exactness through every such return.

### Definitions

An interacting return must re-enter and influence the critical core; a dead
escape edge or a support-only latch does not qualify.

### Motivation

Prior bounded searches were unsatisfiable but support-only models survived.
This question isolates the mathematical distinction that another bounded sweep
would not resolve.

### Proof or construction

Open question; none is claimed.

### Dependency audit

The prior UNSAT figures and critical-saturation theorem are historical
provenance until their artifacts are imported.

### Gap audit

A support graph alone does not verify tropical weights, strict coefficient
orders, or context closure. A bounded UNSAT result cannot prove impossibility in
arbitrary dimension.

### Adversarial tests

Require any candidate to exhibit the exact critical cycle, transient return,
marked coefficient, and strict inequality; then check all rule inequalities
symbolically.

### Remaining uncertainty

Both existence and impossibility are open in this packet.

### Suggested next attack

Search first for a symbolic conservation law on return flows; use solver
synthesis only to distinguish concrete alternatives suggested by that law.
