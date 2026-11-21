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

## Checkpoint 2: one order for both recursive moves

[MIXED_CERTIFICATE_DESCENT.md](MIXED_CERTIFICATE_DESCENT.md) and the standalone
[Mathlib module](mathlib/MixedCertificate.lean) prove that source-prefix
consumption and the two longer height-descending replacements of PR169
decrease the same well-founded multiset order. Both infinite affine families
are checked for every natural parameter, including their actual upper and
lower ordinary paths. A finite-rule induction kernel exposes complete rule
coverage as an explicit hypothesis; no such coverage theorem is supplied.

The core project also contains a uniform exponent recursion in
[MersenneRecursion.lean](lean/Collatz/MersenneRecursion.lean): every even
Mersenne exponent at least two folds into the preceding odd exponent. This
reduces part of the terminal multiplier family by actual ordinary moves.

[EXACT_FORWARD_FLOOR.md](EXACT_FORWARD_FLOOR.md) records the full floor proof
and exact multiplier transport. [TERMINAL_FIVE_NORMALIZATION.md](TERMINAL_FIVE_NORMALIZATION.md)
gives the component-preserving asynchronous normalization and the stronger
rank-minimal version, with the precise two repair conditions still open.

## Checkpoint 3: an unbounded reset and a complete arithmetic moment

[VALUATION_RESET_GRAMMAR.md](VALUATION_RESET_GRAMMAR.md) gives a source
replacement with an arbitrarily long middle loop. Under explicit ordinary
integer equations, the new core module
[UnboundedReset.lean](lean/Collatz/UnboundedReset.lean) proves

\[
T^{\ell+17}(m)=P/4,\qquad T^{\ell+16}(2m-1)=P-1,
\qquad T^j(m)<P/2\quad(0\le j\le\ell+17).
\]

Thus the single old source step `P/2 -> P/4` can be replaced by the entire
longer prefix, and a failed parent comparison would produce a smaller failed
comparison. All paths, every intermediate-state bound and the arbitrary-tail
certificate splice are checked in Lean. The power-of-two specialization has
a valuation-selected loop length; its normalized-unit guard is not universal.

The Mathlib module also now proves that its two affine replacements construct
actual complete supplied hitting certificates with strictly smaller measures.
This makes the common-suffix argument explicit inside the kernel.

[PRIMITIVE_SURVIVAL.md](PRIMITIVE_SURVIVAL.md) and
[PrimitiveSurvival.lean](mathlib/PrimitiveSurvival.lean) build the complete
ordinary source partition directly from positive valuation words. With the
precisely defined primitive-source moment `B_q`, Lean proves

\[
A_q=B_q+R_q,\qquad
0\le R_q\le\frac{\zeta(4)}{16}\,15^{-q},\qquad
\mathrm{FullCollatz}\iff B_q\longrightarrow0.
\]

Here `A_q` weighs the original positive odd sources that have not reached one,
using their fixed weight `n^(-4)`. Every valuation and every higher lift is
included. This criterion detects nontrivial cycles as well as divergent
orbits. **The decay of `B_q` is not proved.** The attempted absorption estimate
and the precise failed inference are in [FLUX_ATTEMPT.md](FLUX_ATTEMPT.md).

[question_primitive_source_moment.txt](question_primitive_source_moment.txt)
is a self-contained arithmetic handoff without orbit terminology. The
restricted same-family folding obstruction is recorded separately in
[MERSENNE_FOLD_INVARIANT.md](MERSENNE_FOLD_INVARIANT.md), as a written argument.

## Continuing attacks

The remaining work is to supply complete rules for the shared order, including
the terminal multiplier states, or to prove an arithmetic survival estimate
sensitive to both divergent trajectories and nontrivial cycles. The common
order's applicability to the two given families is now proved; all-input
coverage remains a separate open assertion.

This checkpoint does not rerun all earlier research packets. It compiles the new modules and the imports actually needed by them, prints the principal theorem dependencies, and runs the repository's required structural gate at the published checkpoint.

## Provenance and evidence

[SOURCES.md](SOURCES.md) freezes the source heads used to select the attack. [The execution report](../../reports/2026-11-21-lean-global-resolvent/README.md) records actual Lean commands, exact file hashes and publication identities. No `sorry` or new unproved axiom is used by the compiled modules. A theorem whose type assumes a closing condition is not presented as unconditional convergence.
