# T-0039 — Two-block room exclusion criterion

Claim ID: `T-0039`  
Title: Every eventual room requires an allowed six-bit output directly above a zero six-bit input cell at every late scale  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0025`, `L-0033`, `T-0033`, `T-0037`  
Scope: stabilized phase-`-34` three-symbol addresses  
Related counterexample candidates: none

## The two adjacent Hensel blocks

For a three-symbol prefix `(a,b,c)`, retain the lifted address

\[
\widehat\rho_m(a,b,c)
=ho_m(a,b,c)+M_mh_m(a,b,c)
\tag{1}
\]

from `L-0033`, where

\[
0\le\rho_m<M_m,
\qquad
0\le h_m<64.
\]

Define the top input-cell block

\[
\boxed{
q_m(a,b,c)
=\left\lfloor{64\rho_m(a,b,c)\over M_m}\right\rfloor
\in\{0,\ldots,63\}.}
\tag{2}
\]

Thus the twelve bits straddling the modulus boundary are

```text
lower block: q_m  = top six bits of rho_m below M_m;
upper block: h_m  = six-bit Hensel lift above M_m.
```

The canonical output type exists exactly when

\[
[-N_mh_m]_{64}\in\{5,30,20,56\}.
\tag{3}
\]

## Statement 1 — eventual rooms require the zero lower block

For every fixed room `C > 0`, there is `m_C` such that

\[
\boxed{C H_m<{M_m\over64}}
\qquad(m\ge m_C).
\tag{4}
\]

Consequently, if `C` supports an eventual ordinary trajectory, then at every
sufficiently late scale its three-symbol prefix satisfies simultaneously

\[
\boxed{q_m(a,b,c)=0}
\tag{5}
\]

and the allowed-output condition (3).

### Proof

The upper bound `log_2(3)<65/41` gives

\[
\log_2 H_m
<{1083\over41}2^m+{1024\over41}m.
\]

On the other hand,

\[
\log_2{M_m\over64}
={4257\over128}2^m+27.
\]

Their leading-coefficient difference is

\[
{4257\over128}-{1083\over41}
={35913\over5248}>0.
\]

This proves (4).  A room boundary is the least address by `L-0033/(14)`, so
`rho_m= floor(C H_m)<M_m/64`, which is equivalent to (5).  The output must be a
valid next tower type, giving (3). ∎

## Statement 2 — exact cofinal exclusion criterion

Define

\[
\mathfrak Z_m
=
\left\{
(a,b,c):
q_m(a,b,c)=0,
\ [-N_mh_m(a,b,c)]_{64}\in\{5,30,20,56\}
\right\}.
\tag{6}
\]

Then

\[
\boxed{
\mathscr C=\varnothing
\quad\Longleftrightarrow\quad
\text{no coherent infinite room path passes through }\mathfrak Z_m
\text{ at every sufficiently late scale}.}
\tag{7}
\]

In particular, either of the following sufficient conditions excludes every
room:

1. `mathfrak Z_m` is empty for a cofinal sequence of scales;
2. the exact overlap graph between `mathfrak Z_m` and `mathfrak Z_(m+1)` is empty
   for a cofinal sequence of scales.

### Proof

The forward implication is tautological.  Conversely, an eventual room supplies
its unique three-symbol prefix at every late scale.  Statement 1 puts that
prefix in `mathfrak Z_m`, and the fixed real room supplies coherence between
successive scales.  The two sufficient conditions therefore contradict room
existence. ∎

## Statement 3 — bounded exact audit

An exact lifted-inverse evaluation gives

\[
\boxed{\mathfrak Z_m=\varnothing}
\qquad(12\le m\le19).
\tag{8}
\]

Equivalently, throughout this audited range every prefix that passes the
allowed-output filter has

\[
\boxed{\rho_m(a,b,c)\ge {M_m\over64}.}
\tag{9}
\]

The minimum survivor-address bit gaps below the full modulus are

```text
m                 12 13 14 15 16 17 18 19
U_m-bit_length      5  0  1  1  2  1  1  0
```

where a gap of five still places the address above `M_m/64`.

Equation (8) is `EMPIRICAL` finite verification, not the infinite theorem.
`X-0017` contains the portable audit through scale 14; an independent GMP
implementation used during authoring extended the same integer formulas
through scale 19.

## Why this is the current atomic frontier

Earlier formulations involved:

- 256 tower symbols;
- a full stage correction of millions of bits;
- a free ordinary quotient;
- or a 1024-state triple-seam graph.

After `T-0031`, `L-0033`, and the present theorem, room existence first requires
one twelve-bit boundary pattern:

```text
[ allowed six-bit output lift h_m ]
[ zero six-bit input cell q_m       ]
```

at every late scale.

The lower block is an ordinary completion-height demand.  The upper block is a
Hensel output-type demand.  They are adjacent bits of the same exact modular
inverse.  A proof that this pair never occurs cofinally closes the entire fixed
corrected-stage architecture.

## Gap audit

- Finite emptiness through scale 19 does not prove cofinal emptiness.
- The high moving bits are not controlled by the stable low 2-adic limit of the
  normalized inverse.
- An actual source-specific Newton carry can transport new high bits; an
  abstract finite-state argument is insufficient.
- No counterexample or universal Collatz conclusion is claimed.