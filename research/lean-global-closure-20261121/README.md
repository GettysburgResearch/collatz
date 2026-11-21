# Lean attempts at universal Collatz closure

**Status: OPEN. No complete proof of Collatz is claimed.** This project targets
the universal closing step, with machine-checked intermediate results and
explicit hypotheses. The map is the ordinary shortcut map

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

## Compiled results

### An obstruction valid at every finite window width

[`CollatzGlobalClosure/LocalProfileObstruction.lean`](CollatzGlobalClosure/LocalProfileObstruction.lean)
constructs, for **every** binary window width and **every** size threshold,
positive odd integers `n > m > 1`, with `n` above that threshold, satisfying

\[
3n+1=4m,\qquad H_r(n)=H_r(m).
\]

Here `H_r` records the entire zero-padded binary-window histogram of width
`r+1`. It follows that **any function** of one fixed-width histogram,
including a nonlinear function with an arbitrary preordered codomain,
cannot be a strict rank for every accelerated odd Collatz step. Arbitrarily
many small exceptions do not fix this obstruction. This is a constructive
infinite-family theorem, independent of numerical synthesis searches.
The [construction and scope](LOCAL_PROFILE_OBSTRUCTION.md) retain the
distinction from ranks that depend on positions or on blocks of steps.

### Deterministic relative parity

[`CollatzGlobalClosure/RelativeParityBarrier.lean`](CollatzGlobalClosure/RelativeParityBarrier.lean)
proves, for every positive orbit that never hits one and every clock `t`,

\[
2^{4t}\le 2^{7p_t}n^4,
\]

where `p_t` counts its actual odd inputs before clock `t`. This covers both
divergence and hypothetical nontrivial cycles. It then proves a finite
source-relative convergence certificate and the exact equivalence

\[
\texttt{ForwardFiveClosure}\iff\texttt{RelativeBudgetReturns}.
\]

The right-hand statement is **not proved**. It is a defined proposition,
not a new axiom. The [proof note](RELATIVE_PARITY_ROUTE.md) gives its complete
quantifiers, the elementary estimates, and the first unsupported step in
the attempted deterministic completion. No novelty claim is made for the
elementary parity estimate.

## Build

The project pins Lean **4.34.1** and mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. From this directory:

```sh
lake exe cache get Mathlib/Tactic.lean Mathlib/FieldTheory/Finite/Basic.lean Mathlib/Data/Nat/Digits/Lemmas.lean
lake build
```

`lakefile.toml` treats warnings as errors. The relative-parity declarations
and the two principal profile theorems print their axiom dependencies. Only Lean's standard
`propext`, `Classical.choice`, and `Quot.sound` occur. The source contains
no `sorry`, custom axiom, `native_decide`, or unsafe proof mechanism.
The actual package execution is recorded in
[`checkpoint-build.json`](../../reports/lean-global-closure-20261121/checkpoint-build.json)
and [`checkpoint2-build.json`](../../reports/lean-global-closure-20261121/checkpoint2-build.json).
This execution proves the stated implications; it does not establish their
open universal hypothesis.

## Latest source interfaces considered

These are exact investigation pins, not unproved premises imported into the
Lean kernel. Older work is not re-audited by this checkpoint.

| Source | Exact head | Interface used for the research attempt |
|---|---|---|
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `f431078244e868dc699fad011044f0d5e7f76437` | Whole-interval synchronization; certified terminal sources; finite directed five-closure interface |
| [PR173](https://github.com/GettysburgResearch/collatz/pull/173) | `8596fdfd4d6378b57f83d843e94a206f45604b1b` | Lean predecessor fans in narrow multiplicative shells |
| [PR171](https://github.com/GettysburgResearch/collatz/pull/171) | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | Paired section recurrence and the distinction between Haar recurrence and supplied ordinary sources |
| [PR164](https://github.com/GettysburgResearch/collatz/pull/164) | `9582df78eb4d768eb748d3cf367ba97582308a52` | Witness-relative rewrites for the direct `27m -> 9m` closure problem |
| [PR172](https://github.com/GettysburgResearch/collatz/pull/172) | `b22d94240f3d44a04231508e5dfe9a4947a57125` | Prior pass's global certificate attempts and explicit remaining obligations |

The active universal attempts are deterministic relative parity, adaptive
endpoint steering for synchronized intervals, and a rank that retains
nonlocal binary/ternary structure. An incomplete search or a conditional
closing lemma will not be labeled a proof of the full theorem.
