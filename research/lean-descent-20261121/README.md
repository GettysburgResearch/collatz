# Lean attack on full Collatz by a finite odd-step budget

**Checkpoint status: OPEN. Full Collatz is not proved.** The main route is an
explicit finite arithmetic assertion at every positive input, with a complete
Lean proof that this assertion implies the full conjecture. The universal
assertion remains a hypothesis in the displayed theorem type. There are no
added axioms or `sorry` proofs.

This packet uses the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

## The direct route to the full theorem

For one fixed ordinary input `n`, track its actual orbit and four integers:
`A=3^p`, `D=2^t`, the number `p` of odd inputs, and the affine remainder `B`.
Lean proves at every clock

\[
             D\,T^t(n)=An+B.
\]

At an even step, `D` doubles. At an odd step, `A` triples, `D` doubles,
`B` becomes `3B+D`, and `p` increases by one. If all earlier coefficients
`A/D` are at least `1/2`, Lean proves the integer inequality

\[
                         3B\le2pA.
\]

Consequently a first strict crossing `2A<D` with `2p<=3n` gives `B<=An`
and hence

\[
              T^t(n)=\frac{An+B}{D}<n.
\]

Strong induction on the actual positive input now gives full Collatz. It
handles nontrivial cycles and divergent trajectories together: either kind
of counterexample would have a least positive starting value, and that value
cannot admit the certified strict descent.

The remaining assertion is:

\[
\boxed{\quad\forall n>1\quad\text{the first crossing }2^t>2\cdot3^{p_t(n)}
\text{ exists with }2p_t(n)\le3n.\quad}
\]

This is `CollatzHalfCrossing.HalfBudget`, explicitly **OPEN**. It is a
sufficient condition, not an asserted equivalent reformulation of Collatz.
No proof here deduces its uniform linear budget from eventual convergence.
The [completion attempt](HALF_BUDGET_ATTACK.md) records the precise canonical-root
inequality tried, its ordinary-integrality requirement, and the remaining
fixed-source branch.

### One bounded test per input

Any witness to the displayed assertion occurs by clock `3n+2`. Indeed, the
previous coefficient has `2^(t-1)<=2*3^p<=2^(2p+1)`, and the odd count has not
decreased. The separate `BudgetCheck.lean` module proves this clock bound and
gives an exact bounded search. Its soundness and completeness are formal:

```lean
def UniversalBudgetCheck : Prop :=
  ∀ n, 1 < n → budgetCheck n = true

theorem collatz_of_universal_budget_check
    (h : UniversalBudgetCheck) : ∀ n, 0 < n → Basin n
```

The missing proof is `h`. This type does not declare `h` as an axiom.
The test follows the original integer and stops at its first crossing; it
does not replace the input with changing finite witnesses or a 2-adic point.

For the exact fixture `n=27`, the first crossing is at clock 65 with 40 odd
inputs and ordinary endpoint 10. The budget is `80<=81`. `Examples.lean`
checks these numbers in the kernel. The base `n=1` fails this proposed budget
and is correctly handled separately by induction. Finite fixtures do not
establish universal acceptance.

### The weaker unit-only target

`UnitBudget.lean` proves that it is enough for the test to pass on `n` not
divisible by three. The ordinary orbit stays within that domain, so the
strict-descent induction closes there; ordinary moves then extend convergence
to every positive integer. The strongest global theorem in this packet is

```lean
def UnitBudgetCheck : Prop :=
  ∀ n, 1 < n → n % 3 ≠ 0 → budgetCheck n = true

theorem collatz_of_unit_budget (H : UnitBudgetCheck) :
  ∀ n, 0 < n → Basin n
```

`UnitBudgetCheck` remains OPEN. This theorem does not infer the quantitative
budget for inputs divisible by three. In a unit-only induction, a smaller
inverse source must itself be a unit or have a separately supplied budget.

## A complete shadow for the other global route

PR 174 reduces Collatz to a sparse reverse-closure implication for
`m` and `3m-1`. The new `CrossShadow.lean` keeps the integer relation

\[
 ax-by=d,\qquad
 a'=3^f a,\quad b'=3^e b,\quad
 2d'=3^{e+f}d+3^f ae-3^e bf,
\]

where `e,f` are the current parities. It proves exact iteration even when the
relative odd count changes sign. Starting at `(a,b,d)=(3,1,1)`, a supplied
certificate `T^t(3m-1)=1` yields the terminal equation

\[
                  3^{q+1}T^t(m)=3^p+d_t.
\]

The terminal inequality needed for ordinary descent is formalized with its
hypothesis intact. A tempting completion is false: for `m=82=27*3+1`,
the member arm 245 first reaches 1 at clock 16, while 82 reaches 233 at that
clock. Lean verifies the exact counterexample. Negative terminal debt alone
also fails to imply descent. See [the attack and exact boundary](CROSS_SHADOW_ATTACK.md).

## Mixed forward and inverse certificates

### General unequal-clock transfer

`BudgetTransfer.lean` supplies one formal rule for arbitrary ordinary prefixes
`x -> z` and `n -> z`, at possibly different clocks. Write `M,D,p` for each
prefix's multiplier, denominator, and odd count. If the source prefix from
`x` has not yet crossed one half, and

\[
 M_nD_x\le M_xD_n,\qquad 3x+2p_n\le3n+2p_x,
\]

then a supplied budget at `x` transfers to `n`. Lean proves the exact
composition, cancellation, odd-cost bound, and extraction of the first
crossing. These guards are checked on the actual ordinary paths; a basin
equivalence alone is not treated as a budget certificate.

### An unbounded inverse ladder

For arbitrary natural `r,s,u` and positive `v` satisfying

\[
 3^s v=4^r u+2,\qquad 2^{s+2r}<3^{s+r},
\]

put `x=2^s v-1` and `q=3^r u+1`. `TernaryLadder.lean` proves

\[
 T^{s+2r}(x)=q,\qquad p_{s+2r}(x)=s+r,\qquad 0<x<q.
\]

It also proves that every prefix coefficient is at least one. Thus a budget
at the smaller source transfers to `q`, for unbounded block lengths. The
word consists of `s` odd shortcuts followed by `r` odd/even pairs.

The source-unit issue has a formal repair. Under the stronger inequality

\[
               3\,2^{s+2r}<2\,3^{s+r},\qquad s>0,
\]

spend the first odd step and use `y=2^(s-1)*(3v)-1`. This is automatically
`2 mod 3`, is positive and smaller than `q`, and the remaining prefix still
expands. The unit-only induction can therefore use it. For example,
`111 -> 167 -> 251 -> 377 -> 566 -> 283` supplies the smaller unit `167`
for `283`, despite the original source being divisible by three.

The [unbounded ladder proof and domain](TERNARY_LADDER.md) explain both
versions. **A covering construction for every remaining unit has not been
proved.** The general merger theorem and this infinite ladder do not silently
assert such coverage.

### A paired five-return progression

`InverseReturn.lean` proves, for every `t>=0`,

\[
\begin{aligned}
x&=131072t+127657<q=177147t+172534,\\
T^{17}(x)&=q, &T^{17}(5x)&=5q.
\end{aligned}
\]

This is an expanding forward word and a contracting inverse comparison.
It excludes an entire ternary progression from being a least failed-five
source. A written coefficient calculation also transfers the proposed
half-crossing budget from `x` to `q`; that budget transfer is not yet a Lean
declaration. The [short note](INVERSE_RETURN.md) records the exact word and
the reason a complete induction must mix forward and inverse moves.

## Source pins and attribution

The latest source refresh for this checkpoint used:

| Source | Frozen head | Use |
|---|---|---|
| PR 174 | `7034109ed60a26bc49824e1ed43c239ceca81194` | Dependency-free Lean base, closure theorem and shadow route |
| PR 173 | `a09eb47197cd99f218b3fa013c681df65ea0f69a` | Read the global interval criterion and its exact remaining survivor bound |
| PR 146 | `f431078244e868dc699fad011044f0d5e7f76437` | Read latest return-clock and terminal characterization |
| PR 172 | `b22d94240f3d44a04231508e5dfe9a4947a57125` | Read current certificate-completion scope |
| PR 171 | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | Earlier paired-return results and full-kernel pressure boundary |

`Collatz/ReverseBasin146.lean`, `Collatz/Closure.lean`, and
`Collatz/Shadow.lean` are copied without changes from PR 174's pinned project.
That project credits its reverse-basin source to PR 146 at
`e238c63a5d57f96bb063b7472498d1977df51951`, with its documented Lean-core shim.
The new modules are `HalfCrossing`, `BudgetCheck`, `CrossShadow`, and
`InverseReturn`, followed by `BudgetTransfer`, `UnitBudget`, and
`TernaryLadder` at checkpoint two. No re-verification of older research packets is claimed.
No GRH hypothesis is used in these theorems.

The live refresh during this pass also recorded PR 173 at
`cccf14d13250d3f98ef9b01ddbd304d11294e603` (new octave mixing and packing
criteria), PR 174 at `011b89e5362ea89427c2704e5e6c1f434e860da0` (the formal
base is unchanged), PR 175 at `ad513f1ea609ed47dbcf997df0f09c16557264ee`
(relative parity barrier), PR 176 at `bff01093f3eb073216f9ec610130d16067fcc1fd`,
PR 177 at `fe58c189b619d2983940b19a50f1b12798f5651f`, and PR 178 at
`7e40cb5e09f4ed84b96eebf1d2e3fe43fdadf862`. Their current interfaces were
considered for the closing argument; no theorem from these later heads is
imported into this Lean development. In particular, the exact dyadic square
mixing identity is not used to assume fresh parity blocks along a fixed
ordinary trajectory.

## Build and evidence

The project is dependency-free and pinned to Lean 4.34.1:

```bash
cd research/lean-descent-20261121/lean
lake build
lake env lean -DwarningAsError=true Audit.lean
lake env lean -DwarningAsError=true Examples.lean
```

`Audit.lean` prints the actual global theorem types, retaining their open
hypotheses, and the axiom dependencies of the principal results. Build
receipts and publication checkpoints are recorded in the PR description.
Repository-integrity validation is distinct from Lean verification.
The actual first remote checkpoint is `4bf2675bcc78b42a3f17c0dd826e1dfcc4c8f35b`;
its [Lean receipt](../../reports/2026-11-21-lean-descent/checkpoint1-lean.json)
and [clean-checkout receipt](../../reports/2026-11-21-lean-descent/checkpoint1-validation.json)
are preserved. Later checkpoint validation identifies its own exact head.
