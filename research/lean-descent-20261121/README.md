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
`InverseReturn`. No re-verification of older research packets is claimed.
No GRH hypothesis is used in these theorems.

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
