# L-9815 — Exact successor gaps between survivor cylinders

Claim ID: `L-9815`  
Title: Survivor-cylinder successor gaps obey their own exact plateau and renewal law  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01` (formula and displayed orbit replay only)  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9812`; the exact finite cylinder formula restated below  
Scope: quantitative gaps between ordinary `64 -> 81` survivor starts  
Related counterexample candidates: none

## Definitions

Let `S_ell` be the nonnegative integers surviving at least `ell` induced chart
steps. For a binary word `u=(u_0,...,u_(ell-1))`, define its standard initial
cylinder representative by

\[
\alpha_\ell(u)
=
\left[
\sum_{j=0}^{\ell-1}
17u_j64^j81^{-(j+1)}
\right]_{64^\ell}.
\tag{1}
\]

These are the `2^ell` distinct representatives of `S_ell modulo 64^ell`.
For `Q>=1`, define the positive cyclic representative

\[
\langle x\rangle_Q^+
=
\begin{cases}
[x]_Q,&[x]_Q>0,\\
Q,&[x]_Q=0.
\end{cases}
\tag{2}
\]

For an ordinary `A>=0`, put

\[
\boxed{
D_\ell(A)
=\min_{u\in\{0,1\}^\ell}
\left\langle\alpha_\ell(u)-A\right\rangle_{64^\ell}^+.
}
\tag{3}
\]

## Statement

### 1. Exact successor and gap monotonicity

The integer

\[
\boxed{A+D_\ell(A)}
\tag{4}
\]

is exactly the least integer strictly larger than `A` that survives `ell`
steps. Moreover,

\[
\boxed{D_{\ell+1}(A)\ge D_\ell(A).}
\tag{5}
\]

### 2. Gap renewal law

Let

\[
B_\ell=A+D_\ell(A),
\qquad
E_\ell=T^\ell(B_\ell).
\tag{6}
\]

Then

\[
\boxed{
D_{\ell+1}(A)=D_\ell(A)
\iff
E_\ell\bmod64\in\{0,1\}.
}
\tag{7}
\]

Thus the successor gap has the same plateau/jump rule as the minimum survivor
in `L-9812`.

If `A=M_K` and `m_K` has a forbidden next residue, then

\[
\boxed{M_{K+1}=A+D_{K+1}(A).}
\tag{8}
\]

For every `ell<=K+1`, this yields the monotone lower bounds

\[
\boxed{M_{K+1}\ge A+D_\ell(A).}
\tag{9}
\]

In particular, the `+960` certificate in `L-9812` is exactly

\[
D_2(M_{46})=960.
\tag{10}
\]

### 3. Base-64 subtraction form

Write

\[
\alpha_\ell(u)=\sum_{j<\ell}p_j64^j,
\qquad
A\bmod64^\ell=\sum_{j<\ell}a_j64^j.
\tag{11}
\]

The digits of the positive cyclic difference are ordinary base-64 subtraction
digits:

\[
\boxed{
q_j\equiv p_j-a_j-b_j\pmod{64},
}
\tag{12}
\]

where `b_(j+1)=1` exactly when `p_j<a_j+b_j`. Minimizing (3) is therefore
lexicographic minimization of

\[
(q_{\ell-1},\ldots,q_0)
\tag{13}
\]

among the legal cylinder words, excluding the all-zero difference.

### 4. Exact meet-in-the-middle certificate method

Set

\[
g_j=17\cdot64^j81^{-(j+1)}\pmod{64^\ell}.
\tag{14}
\]

Split these generators into two halves. For each left subset sum `L`, put

\[
t=[A-L]_{64^\ell}.
\tag{15}
\]

In the sorted right-half subset sums, the first value strictly larger than `t`,
cyclically wrapping to the least value plus `64^ell`, gives the smallest
positive gap for that left half. The minimum over all left halves is exactly
`D_ell(A)`. This proves an exact method with

\[
O(2^{\lceil\ell/2\rceil}\log 2^{\lfloor\ell/2\rfloor})
\tag{16}
\]

time and `O(2^(floor(ell/2)))` storage.

### 5. Internal exact depth-47 result

An unfrozen exact run of the method in part 4 reports

\[
\boxed{
M_{47}
=99402651648084656958440378012632080125550281966624279112341154646188993.
}
\tag{17}
\]

Its chronological word is

```text
10111000011011000011110110100111011110001011110
```

and the displayed endpoint is

\[
\boxed{
m_{47}
=6393447153551689331942639550360611057613214810780972886950464545374060926528.
}
\tag{18}
\]

In particular,

\[
\boxed{M_{47}>2^{235}.}
\tag{19}
\]

The displayed word and endpoint have been independently replayed by the
integrating agent, but global minimality has not yet been independently
recomputed. Accordingly (17)--(19) remain `INTERNAL EXACT COMPUTATION`.

The exact endpoint residues imply the next two renewal facts without another
minimization:

\[
m_{47}\equiv0\pmod{64}
\Longrightarrow
\boxed{M_{48}=M_{47}},
\tag{20}
\]

while

\[
m_{48}
=8091706553713856810739903180925148369791724994894668810046681690239045860137
\equiv41\pmod{64},
\tag{21}
\]

so

\[
\boxed{M_{49}>M_{48}.}
\tag{22}
\]

## Proof

Every residue class in (1) contributes the increasing arithmetic progression

\[
\alpha_\ell(u)+64^\ell\mathbb Z_{\ge0}
\]

to `S_ell`. The least positive cyclic difference selects the first member of
that progression above `A`; minimizing over the words proves (4). Since
`S_(ell+1)` is a subset of `S_ell`, its next member above `A` cannot be closer,
proving (5).

The start `B_ell` already survives `ell` steps. It survives one more exactly
when its deterministic endpoint `E_ell` has residue `0` or `1 modulo 64`.
This is equivalent to the same start remaining the least successor at the next
depth, which proves (7). If `A=M_K` fails renewal, monotonicity of the minimum
excludes every depth-`K+1` survivor at or below `A`; (4) then gives (8), and
(5) gives (9).

Equations (12)--(13) are the standard subtraction-with-borrow algorithm written
from low to high base-64 digits. The meet-in-the-middle argument simply writes
every subset sum in (1) uniquely as `L+R`. For fixed `L`, the first cyclic
right sum after `[A-L]` minimizes the positive difference. Exhausting the left
sums therefore proves global minimality and the stated complexity.

For the internal result, direct exact replay verifies all 47 residue choices,
the final integer in (18), the reconstruction of (17) from (1), and
`M_47 mod81=39`. Its bit length is `236`, proving (19). Formula (7) then gives
(20)--(22). ∎

## Motivation

`L-9812` turned survivor-minimum growth into a legal-residue renewal question.
This lemma supplies the quantitative object at every failed renewal: the exact
distance to the next finite survivor cylinder. It also converts the search
from starting-room enumeration into a modular subset-sum successor problem.

## Dependency audit

- The cylinder formula (1) follows by iterating the exact chart recurrence and
  is stated explicitly.
- `L-9812` is used only to identify failed renewal of `M_K` and interpret the
  endpoint residues.
- The exact successor and meet-in-the-middle proofs do not depend on the
  depth-46 or depth-47 computation.
- Numerical minimality in (17) remains internal pending a frozen independent
  certificate; only the displayed orbit was independently replayed.

## Gap audit

- The exact method has square-root-exhaustive complexity and is not an
  asymptotic lower bound on `D_ell(A)`.
- Large finite gaps do not prove `M_K` diverges.
- The plateau `M_48=M_47` is compatible with eventual divergence.
- No nontrivial infinite survivor is constructed or universally excluded.

## Adversarial tests

- The positive representative in (2) is essential: a cylinder containing `A`
  contributes its next periodic copy, not a zero gap.
- `m_K<m_(K+1)<m_K+81^K` is valid only on a renewal plateau; across the
  depth-46 jump the minimizing room changes and the endpoint may decrease.
- The depth-47 word replay proves membership, not minimality.
- A lower prefix gap `D_ell(A)` is only a lower bound for the next deep minimum,
  not its exact value unless `ell=K+1`.

## Remaining uncertainty

A noncomputational lower bound on `D_ell(A)` is still missing. Small gaps mean
that the base-64 digits of `A` shadow a legal cylinder with a tightly constrained
borrow stream, suggesting a bridge to the carry-energy lemmas.

## Suggested next attack

Express bounded or subexponential successor gaps as long runs in the borrow
automaton, then combine the resulting digit constraints with `L-9803` or
`L-9805`. A theorem forcing a growing number of nonzero borrow/carry events
would convert the exact successor formula into an asymptotic minimum bound.
