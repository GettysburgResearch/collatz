# T-0042 — Full-offset gadgets exist at every precision and have a causal branch compiler

Claim ID: `T-0042`  
Title: Arbitrary-precision full-offset collision gadgets and causal correlated selectors from fixed-weight unit representation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-23  
Dependencies: `L-0037`, `L-0010`, `T-0041`  
Scope: finite collision-code construction at every requested precision  
Related counterexample candidates: none

## 1. Unconditional full-offset gadget for every `b`

Fix `b>=1` and put

\[
P=2b,
\qquad
G_b=3^{2b}-3^b.
\tag{1}
\]

Choose one unit signature, for example

\[
\beta=1.
\]

For each

\[
d\in\mathbb Z/3^b\mathbb Z,
\]

apply `L-0037` with weight `b`, precision `2b`, and target

\[
\boxed{y_d=1+3^bd\pmod {3^{2b}}.}
\tag{2}
\]

Pad every resulting word with high zero symbols to common length `G_b`.  Call
the word `v_d`.

Then

\[
\boxed{B(v_d)\equiv1+3^bd\pmod {3^{2b}}.}
\tag{3}
\]

In particular,

\[
B(v_d)\equiv1\pmod {3^b},
\]

and relative to `v_0`,

\[
\boxed{
{B(v_d)-B(v_0)\over3^b}
\equiv d\pmod {3^b}.}
\tag{4}
\]

Thus a full-offset gadget exists for **every** `b`, including

\[
\boxed{b=176.}
\]

The construction is unconditional and finite.  Its common length is very large;
it is not the linear `6b` or `18b` efficiency conjecture.

## 2. Causal branch algorithm

The branch `v_d` is generated from the current finite correction request `d`
by the recursive algorithm `Rep(b,2b,1+3^bd)` of `L-0037`.

No future collision word, infinite `3`-adic expansion, or compactness choice is
used.  At every recursive level the algorithm:

1. evaluates one already constructed finite prefix modulo a power of three;
2. forms one unit target;
3. lifts one discrete logarithm by three-way tests; and
4. writes one new finite odd position.

Therefore the full-offset branch selector is a total causal arithmetic
function

\[
\boxed{
\operatorname{Compile}_b:
\mathbb Z/3^b\mathbb Z
\longrightarrow
\{\text{finite weight-}b\text{ parity words}\}.}
\tag{5}
\]

## 3. Correlation with a current dyadic request

Let `u_x` be the length-`2b`, weight-`b` dyadic-prefix word of `L-0010`, indexed
by

\[
x\in\mathbb Z/2^b\mathbb Z.
\]

Fix `u_0`.  From the **current finite request** `x`, compute

\[
\boxed{
d_x
\equiv
-2^{-2b}\bigl(B(u_x)-B(u_0)\bigr)
\pmod {3^b}.}
\tag{6}
\]

Then compute `v_(d_x)` by (5) and output

\[
\boxed{w_x=u_xv_{d_x}.}
\tag{7}
\]

Exactly as in `T-0041`, the constants of all `w_x` are congruent modulo
`3^(2b)`, while their inverse-root residues cover every class modulo `2^b`.
Hence

\[
\boxed{
\operatorname{Select}_b(x)=w_x}
\tag{8}
\]

is a causal complete-`b`-bit collision selector.

In particular, if an ordinary refund state computes a required finite block

\[
x=\chi(t,i,k)\pmod {2^{176}},
\]

then `Select_176(x)` produces the corresponding collision branch using only the
current values `(t,i,k)` and ordinary finite arithmetic.  Future type symbols
are not supplied to the compiler.

## 4. Exact size at `b=176`

The suffix gadget has

\[
\boxed{
G_{176}=3^{352}-3^{176}}
\tag{9}
\]

available positions and weight `176`.  The correlated core has common length

\[
\boxed{
2\cdot176+G_{176}}
\tag{10}
\]

and weight `352`.

This is an explicit finite construction, but its length has `558` binary bits.
It proves all-precision availability and causal orientation; it does **not**
solve the efficiency problem required for a practical finite macro-tile.

For comparison:

- `O-0012` gives exact length-`6b` gadgets through `b=6`;
- `L-0036` proves all-`b` structured uniformity through two surplus ternary
  digits at length `18b`;
- the still-open efficient target is `O(b)` length with all `b` surplus digits.

## 5. What is and is not oriented

Equation (8) resolves the branch-selection ambiguity at the arithmetic-code
level:

```text
current finite correction request
  -> unique finite dyadic prefix
  -> unique ternary correction target
  -> finite collision branch.
```

It does not assert that an already written ordinary Collatz integer lies in the
complete `2^(2b+G_b)` parity cylinder of that branch.  Low-block selection and
canonical most-significant closure are different statements.  `L-0038` records
the exact ordinary anchoring and stabilization boundary.

## 6. Proof

Equation (3) is `L-0037` applied to every unit target in (2).  Equations (3)--(4)
are the definition of a full-offset gadget.  The causal statement follows from
the explicit recursive compiler.

For the correlated code, the concatenation identity gives

\[
B(u_xv_{d_x})
=
3^bB(u_x)+2^{2b}B(v_{d_x}).
\]

Subtract the reference and divide by `3^b`.  Equations (4) and (6) make the
result zero modulo `3^b`, proving common precision `2b`.  Modulo `2^b`, the
suffix term vanishes and the constants reduce to

\[
B(w_x)\equiv3^bB(u_x)\pmod {2^b}.
\]

The inverse roots are therefore

\[
-3^{-b}B(u_x)\pmod {2^b},
\]

which form a complete residue system by `L-0010`. ∎

## Verification

`X-0020`:

- exhaustively reconstructs every unit target for `1 <= a <= P <= 8`;
- exhaustively constructs all full-offset branches through `b=6`;
- compiles representative `b=176`, precision-`352` targets;
- checks representative causal correlated-selector branches at `b=176`.

## Gap audit

- The theorem proves tasks (1) and the arithmetic part of task (2) using an
  explicit but exponential-length construction.
- It does not prove that the efficient length-`18b` terminal map is surjective
  modulo `3^(2b)`.
- A collision branch selected from the current counter may still fail the full
  ordinary parity-cylinder and top-boundary tests.
- No all-time refund invariant, explicit counterexample integer, or canonical
  most-significant closure is claimed.