# Lean attack on global certificate closure

**Active proof attempt; full Collatz remains OPEN.** The objective is to discharge a universal closing statement in Lean. This packet records compiled checkpoints while that argument is pursued. An equivalence with convergence is a reduction, not a proof of convergence.

Use the ordinary shortcut map `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`. `Basin n` means that an actual finite iterate reaches one. All sources are ordinary positive integers.

## Checkpoint 1: exact global floor and unrestricted terminal normalization

The dependency-free Lean project in [lean/](lean/) builds with Lean 4.34.1:

```sh
cd research/lean-global-resolvent-20261121/lean
lake build
lake env lean -DwarningAsError=true Audit.lean
```

The project reuses the three pinned core modules of PR174 and adds the following new modules. The imported closure hypothesis is never silently supplied as a proof.

### Exact least-failure geometry

[LeastForwardFailure.lean](lean/Collatz/LeastForwardFailure.lean) defines a failed forward closure at `m` by `m>0`, `Basin m`, and `not Basin (2m-1)`. A least such `m` is exactly the parent of the globally least bad integer `2m-1`. Every positive integer below `2m-1` therefore converges, with no multiplicative loss in that floor.

The least parent is even. Writing `m=2t`, the remaining configuration is precisely

\[
\neg\operatorname{Basin}(9t-1),\qquad
\forall\,0<n<4t-1,\quad\operatorname{Basin}(n).
\]

Lean proves full convergence equivalent to excluding this exact configuration, and also equivalent to closure of the basin under `t -> 9t-1`. Neither closing assertion is proved here.

The module also transports the unrestricted `3x-1` closure question across any supplied actual odd edge `3x+1=2^a t`:

\[
\operatorname{Basin}(3x-1)
\Longleftrightarrow
\operatorname{Basin}(3^{a-1}t-1).
\]

The higher ternary multiplier remains part of the obligation. It is not treated as an already valid basin operation.

### Terminal normalization without matching clocks or ranks

[TerminalFive.lean](lean/Collatz/TerminalFive.lean) proves that every failed five-pair has a source-rank-minimal representative `q` for which

\[
q\in C,\qquad 5q\notin C,\qquad
5T^s(q)\in C\quad(s>0).
\]

This forbids asynchronous proportional returns from the bad target to five times any later source endpoint. No balanced-clock or equal-odd-count restriction is imposed. The proof is induction on an actual supplied source hitting clock; it does not require a numerical upper bound on a last return.

The same module gives an exact pair of arithmetic repair obligations equivalent to forward-five closure. Both retain two known ordinary antecedents, `u` and `5u`, before asking for `5u-1` or `5u-2` on their respective stated congruence domains. The file definitions and theorem types give the exact guards. These repair obligations remain open.

## Continuing attacks

The parallel work is attempting to combine source-prefix consumption with witness transformations that increase length but decrease numerical height, and to obtain an arithmetic estimate sensitive to both divergent trajectories and nontrivial cycles. A proposed common order is the multiset order on the ordinary states of the supplied source certificate. Its applicability and all-input coverage must be proved separately; a well-founded order by itself does not furnish a rule at every state.

This checkpoint does not rerun all earlier research packets. It compiles the new modules and the imports actually needed by them, prints the principal theorem dependencies, and runs the repository's required structural gate at the published checkpoint.

## Provenance and evidence

[SOURCES.md](SOURCES.md) freezes the source heads used to select the attack. [The execution report](../../reports/2026-11-21-lean-global-resolvent/README.md) records actual Lean commands, exact file hashes and publication identities. No `sorry` or new unproved axiom is used by the compiled modules. A theorem whose type assumes a closing condition is not presented as unconditional convergence.
