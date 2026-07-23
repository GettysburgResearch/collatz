# Q-8501 — Construct one forever-defined ordinary primitive core

**Claim ID:** `Q-8501`  
**Status:** `OPEN`  
**Dependencies:** `L-8504`--`L-8507`, `T-8505`--`T-8508`  
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

## Equivalent top-boundary quotient target

`L-8506` places every legal current core in one of eight explicit ordinary blocks. `L-8507` proves that compatibility with a complete next block then reduces to exactly four residues of one ordinary top quotient:

\[
\boxed{
m=\rho_k+2^{11(t+33)}\ell
\longmapsto
m'=\sigma_k+3^G\ell,
}
\]

where `k` is the following target type, the ternary lift is forced, the four `rho_k` are distinct, and `sigma_k>=0`.

Thus a positive invariant may equivalently be written in either of two exact forms:

```text
primitive core form:
  high divisibility + six-bit gate;

top quotient form:
  one of four residues mod 2^(11(t+33))
  + exact multiplicative carry update.
```

From height `3760`, every noncanonical lift `ell>=1` strictly increases the top quotient. From height `3776`, `T-8508` gives

\[
\boxed{m'>2m.}
\]

The exceptional case is the canonical lift `ell=0`; it is now an explicitly isolated top-boundary event rather than hidden connector arithmetic.

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
3. equivalently, an all-time proof that the top quotient lands in one of the four `L-8507` residues at every step;
4. exact connector and physical tower replay;
5. proof of positivity at every intermediate state;
6. reconstruction of every intrinsic valuation/type marker;
7. the automatic core-growth conclusion
   \[
   C_n>2^{170n}C_0;
   \]
8. an independent verifier beginning only from the finite integer and rule.

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

A particularly sharp negative target is to prove that canonical lifts cannot recur indefinitely and that every noncanonical lift eventually misses all four next residues. No such theorem is currently supplied.

## Current narrowing

- `L-8502` removes the preloaded-inverse objection.
- `L-8503` and `T-8504` reduce the original connector system to one complement counter.
- `L-8504` removes trusted stage/type metadata and exposes the determinant-one physical marker.
- `L-8505` turns every connector into one exact `3^G C+1` Syracuse equation.
- `T-8507` removes all inverse/carry arithmetic from the runtime state.
- `L-8506` compiles every local state into eight exact ordinary blocks.
- `L-8507` reduces the complete next-stage compatibility to four residues with one type-independent modulus.
- `T-8508` proves every noncanonical top lift is uniformly refunded and eventually more than doubles.
- `T-8506` proves more than 170 bits of primitive-core growth per legal step.
- `T-8502` shows the completion set has Hausdorff dimension zero.
- `T-8503` excludes every eventually periodic type tail of minimal period at most `58`.
- `T-8505` excludes every eventual finite prime support.

The remaining object is one genuinely nonperiodic, fresh-prime-generating, top-boundary-carrying ordinary core orbit satisfying one explicit high binary divisibility and one six-bit gate at every step.
