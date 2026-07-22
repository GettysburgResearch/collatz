# Q-8501 — Construct one forever-defined ordinary primitive core

**Claim ID:** `Q-8501`  
**Status:** `OPEN`  
**Dependencies:** `L-8504`, `L-8505`, `T-8505`--`T-8507`  
**Full-objective role:** a positive solution is an unconditional Collatz counterexample

## Exact target

Find one explicit finite intrinsic state

\[
(t_0,\gamma_0,i_0,C_0),
\]

with

\[
16\mid t_0,
\qquad
t_0\ge3744,
\qquad
\gamma_0\in\{1,2,3\},
\qquad
i_0\in\{0,1,2,3\},
\]

and `C_0` a positive integer coprime to six, such that the primitive-core decoder of `T-8507` is defined for every future step.

At state `(t,gamma,i,C)`, set

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\]

\[
X=3^G C+1.
\]

The all-time obligations are exactly

\[
\boxed{2^D\mid X}
\]

and, after `Y=X/2^D`,

\[
\boxed{[3^{\beta_i}Y]_{64}\in\{5,30,20,56\}.}
\]

The six-bit value gives the unique next type `j`, the next core is `C'=Y/2^j`, and the finite state updates to

\[
(t+16,\beta_i,j,C').
\]

No connector inverse, carry tape, future type word, or completed `2`-adic address is input to this map.

## Single-integer certificate

The intrinsic state corresponds to the one physical positive integer

\[
\boxed{
n_0=2^{11t_0+5+i_0}3^{\gamma_0}C_0-34.}
\]

Conversely, the factorization of `n_0+34` recovers all four state coordinates:

- the binary valuation modulo `176` gives `i_0`;
- the full binary valuation gives `t_0`;
- the ternary valuation gives `gamma_0`;
- the remaining prime-to-six factor is `C_0`.

A final certificate may therefore consist of one written integer, one finite inductive rule, and one independent verifier that reconstructs the entire state from the integer.

## Positive completion certificate

A valid submission must contain:

1. the explicit integer `n_0` or equivalent intrinsic state;
2. a finite ordinary rule or inductive invariant proving both decoder gates recur forever;
3. exact connector and physical tower replay;
4. proof of positivity at every intermediate state;
5. reconstruction of every intrinsic valuation/type marker;
6. the automatic core-growth conclusion
   \[
   C_n>2^{170n}C_0;
   \]
7. an independent verifier beginning only from the finite integer and rule.

Then `T-8507` gives one explicit positive ordinary Collatz counterexample.

## Necessary arithmetic renewal

Any positive solution must satisfy `T-8505`:

- every boundary has a nontrivial prime-to-six core;
- consecutive cores are coprime;
- the complete core is replaced at every connector;
- every fixed finite prime set is escaped infinitely often;
- infinitely many globally new odd primes divide `n_n+34`.

Thus the invariant cannot be a finite-prime multiplicative library, a bounded catalogue of prime-supported templates, or an ultimately periodic fixed-rank schema. It must causally manufacture the exact rapidly growing coprime core required by the next moving binary cylinder.

## Negative completion target

Alternatively, prove that every finite intrinsic core eventually leaves the decoder domain. Such a theorem would close the entire linear-height quotient-refund escape class.

## Current narrowing

- `L-8502` removes the preloaded-inverse objection.
- `L-8503` and `T-8504` reduce the original connector system to one complement counter.
- `L-8504` removes trusted stage/type metadata and exposes the determinant-one physical marker.
- `L-8505` turns every connector into one exact `3^G C+1` Syracuse equation.
- `T-8507` removes all inverse/carry arithmetic from the runtime state.
- `T-8506` proves more than 170 bits of primitive-core growth per legal step.
- `T-8502` shows the completion set has Hausdorff dimension zero.
- `T-8503` excludes every eventually periodic type tail of minimal period at most `58`.
- `T-8505` excludes every eventual finite prime support.

The remaining object is one genuinely nonperiodic, fresh-prime-generating, unbounded-state ordinary core orbit satisfying one explicit high binary divisibility and one six-bit gate at every step.
