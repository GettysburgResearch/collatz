# T-8405 — No C-finite top-boundary certificate

Claim ID: `T-8405`  
Title: An ordinary six-branch survivor quotient cannot satisfy an eventual integer linear recurrence  
Status: `PROPOSED / EXACT METHOD BOUNDARY`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-23  
Dependencies: `L-8406`, `T-8404`  
Scope: the exact ordinary quotient of the six-branch pulse chart  
Related counterexample candidates: none

## 1. Coarse quotient dynamics

Write one physical boundary in its branch cylinder as

\[
 h_n=Mq_n+d_{i_n},
 \qquad
 M=2^{19},
 \qquad
 i_n\in\{0,\ldots,5\}.
 \tag{1}
\]

`L-8406` gives the deterministic partial update

\[
 \boxed{
 Mq_{n+1}=Nq_n+e_{i_n}-d_{i_{n+1}},
 \qquad N=3^{12}.}
 \tag{2}
\]

For a fixed pair `(i,j)`, legality is one residue

\[
 q_n\equiv\rho_{ij}\pmod M.
 \tag{3}
\]

The 36 residues belonging to one fixed source type are distinct.  Therefore the pair

```text
(current type i_n, q_n mod M)
```

uniquely determines the next type whenever the chart is defined.

## 2. Periodic quotient residues force a periodic branch code

Assume that `q_n mod M` is eventually periodic, with period `P` after some index.  Augment the current type by the phase `n mod P`.  The update is then a deterministic map on the finite set

```text
{0,...,5} x Z/PZ.
```

Every forward orbit of this finite deterministic system is eventually periodic.  Hence

\[
 \boxed{
 q_n\bmod M\hbox{ eventually periodic}
 \Longrightarrow
 i_n\hbox{ eventually periodic}.}
 \tag{4}
\]

By `T-8404`, an eventually periodic branch code cannot be the code of a positive ordinary infinite survivor: its `2`-adic completion is one rational number whose real evaluation is nonpositive.

Thus

\[
 \boxed{
 \text{every positive ordinary survivor has non-eventually-periodic}
 \ (q_n\bmod M).}
 \tag{5}
\]

## 3. C-finite sequences are excluded

Suppose, for contradiction, that the ordinary quotient is eventually C-finite.  Then there are fixed integers

```text
c_0,...,c_(s-1)
```

and an index `n_0` such that

\[
 q_{n+s}=c_{s-1}q_{n+s-1}+\cdots+c_0q_n
 \tag{6}
\]

for every `n>=n_0`.

Modulo `M`, the state vector

\[
 (q_n,\ldots,q_{n+s-1})\pmod M
 \tag{7}
\]

belongs to a finite set and evolves deterministically.  It is therefore eventually periodic, so `q_n mod M` is eventually periodic.  This contradicts `(5)`.

Consequently

\[
 \boxed{
 \text{the top quotient of an ordinary infinite survivor is not
 eventually C-finite over the integers}.}
 \tag{8}
\]

## 4. Certificate classes removed

The same argument excludes every proposed top-boundary formula that would make `q_n` eventually satisfy a fixed integer linear recurrence, including:

- polynomial sequences;
- ordinary exponential-polynomial sequences;
- sequences with a rational ordinary generating function;
- fixed companion-matrix or fixed linear-register updates;
- any finite list of such sequences after an eventually periodic selector.

It also excludes a proof architecture whose only unbounded coordinate is C-finite and whose remaining control is finite.

## 5. Why this matters

The result removes the most natural closed-form attempt after `L-8407`.  A successful existence proof cannot prescribe the top boundary by one fixed linear recurrence and then check the low nineteen-bit cells.  It must use genuinely nonlinear arithmetic, changing recurrence data, unbounded memory beyond a C-finite register, or an equivalent fresh-prime/top-boundary mechanism.

This agrees with the independent fresh-prime diagnosis in the larger linear-refund architecture: an ordinary survivor must continually manufacture new arithmetic content rather than remain inside one fixed finite-prime or fixed linear library.

## Gap audit

- Non-C-finite does not mean nonexistent.
- The theorem does not exclude nonlinear recurrences, stacks, changing moduli, or several interacting unbounded registers.
- It proves no finite survival bound.
- It supplies no ordinary survivor and no Collatz counterexample.
