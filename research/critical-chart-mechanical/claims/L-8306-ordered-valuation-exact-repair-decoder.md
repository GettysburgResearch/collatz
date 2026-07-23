# L-8306 — Ordered local repairs admit a lossless exact-integer decoder

Claim ID: `L-8306`  
Status: `PROPOSED / EXACT CONSTRUCTIVE REDUCTION`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8302`, `L-8305`; for positive-cycle replay, branch-qualified `PR34/L-9904` or local `T-8302`  
Scope: a finite family of pairwise-disjoint local replacements whose numerator deltas have strictly increasing dyadic valuations  
Related counterexample candidates: none; a decoder hit would immediately create one after exact replay

## 1. Exact repair grammar

Fix one accelerated or paired-chart word with complete denominator

\[
D=2^A-3^k>0
\]

and affine numerator `C_0`.  Freeze pairwise-disjoint legal replacements

\[
\mathcal R=(R_0,R_1,\ldots,R_{m-1}).
\]

Applying replacement `R_j` changes the numerator by an exact nonzero integer

\[
\Delta_j=\varepsilon_j2^{v_j}u_j,
\qquad
\varepsilon_j\in\{-1,+1\},
\qquad
u_2(u_j)=0.
\tag{1}
\]

Assume

\[
\boxed{v_0<v_1<\cdots<v_{m-1}.}
\tag{2}
\]

For a binary selection vector `x=(x_0,...,x_(m-1))`, the repaired numerator is

\[
C(x)=C_0+\sum_{j=0}^{m-1}x_j\Delta_j.
\tag{3}
\]

The replacements are disjoint, so every selection vector is one valid word with the same `(A,k,D)`.

## 2. Lossless dyadic decoder

Fix an ordinary integer candidate `N` and put

\[
T_N=ND-C_0.
\tag{4}
\]

The exact cycle equation `C(x)=ND` is equivalent to

\[
\sum_jx_j\Delta_j=T_N.
\tag{5}
\]

Define a residual `R_0=T_N`.  At stage `j`, perform the following deterministic rule.

```text
if R_j=0:
    x_j=0;
    R_(j+1)=0;

else if v_2(R_j)<v_j:
    reject;

else if v_2(R_j)=v_j:
    x_j=1;
    R_(j+1)=R_j-Delta_j;

else:
    x_j=0;
    R_(j+1)=R_j.
```

### Theorem 1 — exact uniqueness

There exists a selection vector satisfying `(5)` if and only if the decoder reaches

\[
R_m=0
\tag{6}
\]

without rejecting.  When it exists, the selection vector is unique.

### Proof

Suppose a solution exists and inspect the least undecided index `j`.  Every future delta is divisible by

\[
2^{v_{j+1}},
\]

and hence by `2^(v_j+1)`.  Therefore, modulo `2^(v_j+1)`, the remaining equation is

\[
R_j\equiv x_j\Delta_j\pmod {2^{v_j+1}}.
\tag{7}
\]

The right side is zero when `x_j=0` and has exact valuation `v_j` when `x_j=1`.  Thus:

- valuation below `v_j` is impossible;
- valuation exactly `v_j` forces `x_j=1`;
- valuation above `v_j` forces `x_j=0`.

This is exactly the decoder rule.  Subtracting the forced term preserves the equation for the remaining suffix.  Induction proves that every solution follows the decoder and is unique.  Conversely, if the decoder ends at zero, summing its performed subtractions gives `(5)`. **QED**

## 3. Finite ordinary quotient window

The full family has the rigorous real enclosure

\[
L=
\frac{C_0+\sum_j\min(0,\Delta_j)}D,
\qquad
U=
\frac{C_0+\sum_j\max(0,\Delta_j)}D.
\tag{8}
\]

Every repaired fixed point `C(x)/D` lies in `[L,U]`.  Consequently an integral cycle in the frozen grammar must use one of the finitely many candidates

\[
\boxed{
N\in\mathbf Z\cap[L,U].}
\tag{9}
\]

Applying Theorem 1 to every integer in `(9)` gives a complete proof-producing decision procedure for the entire `2^m` repair family.

This requires neither a factorization of `D` nor enumeration of the selections.  A hit supplies the exact identity

\[
C(x)=ND.
\]

Branch-qualified `PR34/L-9904` then gives positive integral replay with every advertised valuation.  In the paired-chart specialization, local `T-8302` gives the physical seed directly.

## 4. Circuit form

For trillion-symbol words, `T_N`, the deltas, and the residuals need not be expanded as decimal integers.  They may be retained as exact signed exponential circuits.

At stage `j`, the forced decision depends only on the residual modulo

\[
2^{v_j+1}.
\]

After a subtraction, the next stage needs precision only through `2^(v_(j+1)+1)`.  Thus a verifier may increase dyadic precision monotonically and retain a sparse circuit for the final exact-zero check.

No floating-point or probable equality is permitted.  The last condition `R_m=0` is an ordinary exact circuit identity.

## 5. Application to the critical run grammar

In `L-8305`, a neighboring unequal run transposition beginning after prefix dyadic exponent `E_j` has

\[
\Delta_j
=\pm7\,2^{16+E_j}3^{b_j}.
\tag{10}
\]

Along disjoint sites ordered from left to right, the prefix exponent is strictly increasing.  Hence

\[
\nu_2(\Delta_j)=16+E_j
\]

satisfies `(2)` automatically.

Therefore the full disjoint run-transposition grammar—far beyond the 80-site proper-factor experiments `X-8302` and `X-8303`—is not a generic subset-sum problem.  For each ordinary quotient candidate it has at most one possible repair word, recovered digit by digit from the exact residual.

The same conclusion holds for the symbol-level adjacent swaps in PR #45 and local `L-8302`: their delta valuations are the strictly increasing prefix valuation plus the local smaller letter.

## 6. Why this is stronger than a modular join

A modular repair proves only

\[
C(x)\equiv0\pmod M
\]

for a proper divisor `M|D`.  The decoder instead targets

\[
\boxed{C(x)=ND}
\]

for an ordinary integer selected by the real quotient window.  It simultaneously enforces every prime-power digit of the complete denominator and the Archimedean quotient.

The prime-power quotient cylinders of `L-8303` remain useful early rejection filters, but they are no longer the terminal certificate.

## 7. Gap audit

- The theorem decides a frozen disjoint-replacement grammar, not all words with the same `(A,k)`.
- The integer window `(9)` may still contain many candidates; a separate exact bound or interval computation is needed.
- Overlapping replacements do not form the independent binary grammar `(3)` and require a different normal form.
- A decoder failure is a negative result only for the declared site family.
- No decoder hit, positive cycle, infinite chart path, or Collatz counterexample is asserted in this lemma.

## 8. Suggested next attack

1. Generate the complete canonical disjoint Farey/run site family through the full Euclidean hierarchy.
2. Compute the rigorous quotient interval `(8)` as an affine interval circuit.
3. Decode every integer in `(9)` directly against `T_N=ND-C_0`.
4. Route any hit immediately to independent exact valuation and shortcut-Collatz replay.
5. If the whole hierarchy fails, record the resulting complete grammar exclusion rather than another proper-factor census.
