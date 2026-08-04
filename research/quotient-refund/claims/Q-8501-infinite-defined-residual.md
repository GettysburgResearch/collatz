# Q-8501 — Construct one forever-defined ordinary primitive core

**Claim ID:** `Q-8501`  
**Status:** `OPEN`  
**Dependencies:** `L-8511`, `L-8512`, `T-8510`--`T-8513`  
**Full-objective role:** a positive solution is an unconditional Collatz counterexample

## Exact intrinsic target

Find one explicit finite state

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

and `C_0` a positive integer coprime to six, such that the decoder of `T-8507` is defined forever.

At state `(t,gamma,i,C)`, put

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\]

\[
X=3^GC+1.
\]

The exact all-time gates are

\[
\boxed{2^D\mid X}
\]

and, with `Y=X/2^D`,

\[
\boxed{[3^{\beta_i}Y]_{64}\in\{5,30,20,56\}.}
\]

The six-bit value gives the unique next type `j`,

\[
C'=Y/2^j,
\]

and the finite state becomes

\[
(t+16,\beta_i,j,C').
\]

No future type word, inverse tape, prime schedule, or completed stack is input.

## Equivalent Hensel-quotient target

`L-8512` gives the determinant-one coordinate

\[
C=a+2^Dq,
\qquad
Y=h+3^Gq,
\qquad
\begin{pmatrix}2^D&a\\3^G&h\end{pmatrix}
\in\operatorname{SL}_2(\mathbf Z).
\]

Put

\[
H_t=2^{11(t+33)}.
\]

At every step the four complete current-target/next-high-divisibility residues are

\[
\boxed{
q\equiv
\Lambda+U b_j
\pmod {H_t},
\qquad
b=(9,54,36,24),}
\]

for one odd unit `U`. The current physical target is automatic. Exactly one of the three free-lift classes modulo three is forbidden by source primitivity. For an allowed lift

\[
q=\varrho_j+H_t\ell,
\]

the exact next quotient is

\[
q'=\tau_j+3^G\ell.
\]

Thus a positive solution may equivalently be an inductive ordinary class for one changing-modulus Hensel quotient whose router is an affine copy of the fixed toll alphabet.

## Equivalent top-boundary target

For one compiled current block, `L-8507` gives

\[
\boxed{
m=\rho_k+H_t\ell
\longmapsto
m'=\sigma_k+3^G\ell.}
\]

`L-8509` splits the four residues into

```text
one common block of 11(t+33)-6 bits,
then four allowed six-bit cells.
```

`L-8510` gives one base-64 multiplier/carry update, and `L-8511` proves that after affine normalization its six-bit symbol is exactly the fixed physical type symbol `p_k` on both sides.

`T-8510` proves that every hypothetical infinite orbit becomes permanently refunded after finitely many connectors. `T-8513` proves that its current finite ordinary quotient then pays a complete future cylinder of linearly growing depth and retains a positive free quotient beyond it.

The remaining theorem is therefore exactly:

```text
ENTRY:
  one written integer reaches the permanent-refund regime;

ROUTING:
  its causally generated quotient content always equals
  the next common long residue and one legal normalized type symbol.
```

## Single-integer certificate

The intrinsic state corresponds to the one physical integer

\[
\boxed{
n_0=2^{11t_0+5+i_0}3^{\gamma_0}C_0-34.}
\]

Conversely, the factorization of `n_0+34` recovers all state coordinates:

- the binary valuation modulo `176` gives `i_0`;
- the full binary valuation gives `t_0`;
- the ternary valuation gives `gamma_0`;
- the remaining prime-to-six factor is `C_0`.

A final certificate may therefore contain one written integer, one finite inductive routing rule, and one verifier reconstructing all marks from the integer.

## Automatic consequences of a positive solution

No separate proof of these items would remain:

1. every connector and every intermediate shortcut-Collatz step is exact;
2. all physical states remain positive;
3. future types are determined causally;
4. consecutive primitive cores are coprime;
5. every primitive core gains more than `170` bits per connector;
6. canonical lifts disappear after a finite time;
7. the top quotient becomes permanently and acceleratingly refunded;
8. the current finite integer continually prepays an expanding exact future cylinder;
9. infinitely many globally new odd primes enter `n_n+34`;
10. the physical orbit is unbounded.

Hence one all-time routing invariant finishes the unconditional counterexample.

## Acceptance gate

A valid positive submission must contain:

1. the explicit integer `n_0` or equivalent intrinsic state;
2. a finite ordinary rule or inductive invariant proving every later route;
3. exact proof of both the dyadic and primitive gates;
4. canonical most-significant closure, not a fixed-modulus lasso;
5. an independent verifier beginning only from `n_0` and the finite rule.

A finite prefix, compatible `Z_2` point, periodic low-residue cycle, entropy surplus, or freely supplied future symbol sequence does not qualify.

## Negative completion target

Alternatively, prove that every finite intrinsic core eventually leaves the decoder domain. Such a theorem would close the whole linear-height quotient-refund escape class.

The canonical-run obstruction is no longer an open negative target: `T-8509` and `T-8510` already force eventual permanent refund. A negative theorem must now attack the permanently refunded affine fixed-alphabet router itself.

## Current frontier

The remaining object is one genuinely nonperiodic, fresh-prime-generating, top-boundary-carrying ordinary orbit satisfying a changing affine four-symbol Hensel cylinder forever. All drift, marker, canonical-run, and finite-stack-capacity obligations are closed inside the proposed packet.