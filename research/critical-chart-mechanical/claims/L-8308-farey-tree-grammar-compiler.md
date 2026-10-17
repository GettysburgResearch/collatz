# L-8308 — The full Farey sibling-swap grammar has exact modular and real compilers

Claim ID: `L-8308`  
Status: `PROPOSED / EXACT HIERARCHICAL-GRAMMAR COMPILER`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8302`, `L-8304`, `L-8305`, branch-qualified `PR45/L-8403`  
Scope: the recursive Farey/Christoffel parse of the lower critical mechanical run word  
Related counterexample candidates: none

## 1. Farey parse

For coprime integers

\[
0<p<q,
\tag{1}
\]

let `L(p,q)` be the lower binary mechanical word. Let `b` be the inverse of `p modulo q` in `{1,...,q-1}` and put

\[
a={pb-1\over q},
\qquad
(c,d)=(p-a,q-b).
\tag{2}
\]

Then

\[
pb-qa=1,
\qquad
p=a+c,
\qquad
q=b+d,
\tag{3}
\]

and the two fractions are Farey neighbors. With their natural order,

\[
\boxed{L(p,q)=L(a,b)L(c,d).}
\tag{4}
\]

The leaves are

```text
L(0,1)=0,
L(1,1)=1.
```

Equation `(4)` recursively gives a full binary parse tree with `q` leaves.

## 2. Hierarchical sibling-swap grammar

Define `G(p,q)` recursively:

- `G(0,1)={0}` and `G(1,1)={1}`;
- for the Farey parents `x=(a,b)` and `y=(c,d)`, a word belongs to `G(p,q)` exactly when it has one of the forms

\[
uv
\quad\hbox{or}\quad
vu,
\tag{5}
\]

with

\[
u\in G(x),
\qquad
v\in G(y).
\tag{6}
\]

Thus every internal occurrence may retain or reverse its two recursively repaired children. Choices at repeated occurrences are independent. Different choice assignments are allowed to produce the same terminal word; the grammar is a set of words, not a claim of injective derivations.

Every word in `G(p,q)` has length `q` and weight `p`. For the critical run parameters

```text
p = 236,838,463,643,
q = 267,629,447,755,
```

all words therefore expand through `L-8304` to accelerated words with the same

```text
k = 3,149,971,404,836,
A = 4,992,586,555,009,
D = 2^A-3^k.
```

## 3. Exact modular compiler

Fix a modulus `M`. For a run word `w`, let

\[
\Sigma_M(w)=(P_w,Q_w,C_w)\pmod M
\tag{7}
\]

be its accelerated affine summary, so chronological concatenation obeys

\[
(P,Q,C)_{uv}
=
(P_uP_v,Q_uQ_v,P_vC_u+Q_uC_v)\pmod M.
\tag{8}
\]

For a node `x`, let

\[
\mathcal C_M(x)
=
\{C_w\pmod M:w\in G(x)\}.
\tag{9}
\]

The multipliers `P_x,Q_x` are fixed by the node counts. If `x` has Farey children `y,z`, then

\[
\boxed{
\begin{aligned}
\mathcal C_M(x)
={}&\{P_zc_y+Q_yc_z:c_y\in\mathcal C_M(y),c_z\in\mathcal C_M(z)\}\\
&\cup
\{P_yc_z+Q_zc_y:c_y\in\mathcal C_M(y),c_z\in\mathcal C_M(z)\}
\pmod M.
\end{aligned}}
\tag{10}
\]

Memoizing `(10)` by the rational node gives an exact finite compiler. Reusing a memoized set does not couple repeated occurrences: each parent cross-product independently chooses one member for each child occurrence.

## 4. Exact directed real envelope

Normalize each run word to

\[
F_w(x)=r_wx+t_w,
\tag{11}
\]

where `r_w` is fixed by the node counts and positive. Let

\[
I(x)=[\ell_x,u_x]
\tag{12}
\]

be the minimum and maximum translations over `G(x)`.

For children `y,z`, positivity gives the exact endpoint recursion

\[
\boxed{
\ell_x
=
\min\{r_z\ell_y+\ell_z,
       r_y\ell_z+\ell_y\},}
\tag{13}
\]

\[
\boxed{
u_x
=
\max\{r_zu_y+u_z,
       r_yu_z+u_y\}.}
\tag{14}
\]

The endpoint choices are attainable because the two child grammars are independent. Hence `[ell_x,u_x]` is the exact convex envelope of the translation set, not merely a heuristic interval.

When `r_x<1`, every fixed point in the node grammar lies in

\[
\boxed{
J(x)=
\left[{\ell_x\over1-r_x},{u_x\over1-r_x}\right].}
\tag{15}
\]

Using directed decimal or rational-ball arithmetic at every operation gives a proof-carrying enclosure.

## 5. Ordinary quotient-cylinder decision

Assume `D` is odd and fix `M=2^B`. For the root grammar, every integral fixed point `N=C_w/D` must satisfy

\[
\boxed{
N\equiv C_wD^{-1}\pmod {2^B}.}
\tag{16}
\]

The modular compiler `(10)` gives the exact finite set

\[
\mathcal Q_B
=
\{cD^{-1}\pmod {2^B}:c\in\mathcal C_{2^B}(p,q)\}.
\tag{17}
\]

If the real envelope satisfies

\[
0<J(p,q)<2^B,
\tag{18}
\]

then the grammar contains an integral fixed point if and only if

\[
\boxed{
\mathcal Q_B
\cap
(\mathbf Z\cap J(p,q))
e\varnothing.}
\tag{19}
\]

This decides the complete ordinary equation over the entire recursive grammar. It uses no factorization of `D` and no enumeration of the expanded words.

## 6. Proof audit

- Equation `(4)` is the lower-Christoffel Farey concatenation, also reflected in local `L-8302`.
- Equations `(8)` and `(10)` are exact affine concatenation.
- Equations `(13)`–`(14)` follow from positive linear coefficients and independently attainable child extrema.
- Equation `(16)` is ordinary division modulo a power of two, valid because `D` is odd.
- Under `(18)`, each residue has at most one possible ordinary representative, proving `(19)`.

## 7. Computational realization

`X-8306` implements `(10)` and `(13)`–`(19)` independently at

\[
B=314
\]

for the full critical root. A separately written verifier reconstructs the same grammar from the Farey-parent equation `(2)`.

## 8. Gap audit

- `G(p,q)` is a large hierarchical grammar, but not the set of every binary word of length `q` and weight `p`.
- The compiler decides one frozen critical shape, not every continued-fraction shape.
- A positive result at a modular precision without the real condition `(18)` would still be insufficient.
- No cycle or infinite chart path is asserted in this lemma.

## 9. Suggested next attack

Apply the same compiler to a union of neighboring critical convergents and to grammars allowing controlled shape changes. A quotient residue entering the real window is not yet a cycle, but it reduces the complete search to the corresponding exact residual circuit and full valuation replay.
