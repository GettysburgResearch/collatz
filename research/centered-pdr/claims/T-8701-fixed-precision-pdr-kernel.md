# T-8701 — Exact fixed-precision PDR kernel

**Claim ID:** `T-8701`  
**Type:** theorem  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Dependencies:** `D-8701`; elementary modular-cylinder algebra  
**Scope:** every dyadic precision `64^d`, `d>=1`

## 1. Existential modular graph

Fix `d>=1`. Let `G_d` have states

\[
(b,e),
\qquad 0\le b<64^d,
\qquad e\in\{0,1\},
\]
whose low digit is legal in `D-8701`.

There is an edge labelled `h in {0,...,63}` from `(b,e)` to `(b',e')` when the ordinary lift

\[
B=b+h64^d
\]
has one exact legal forced step and its target is congruent to `b'` modulo `64^d`.

Let `K_d` be the greatest existential safety kernel: the set of states from which `G_d` admits an infinite directed path.

## 2. Cylinder states

For a binary word

\[
w=e_0e_1\cdots e_d,
\]
let `R_d(w)` be the unique residue modulo `64^d` for which

\[
64B_{j+1}=81B_j+e_j-e_{j+1}
\]
is integral through the first `d` transitions. Explicitly,

\[
\boxed{
R_d(w)
\equiv
-\sum_{j=0}^{d-1}
(e_j-e_{j+1})64^j81^{-(j+1)}
\pmod{64^d}.}
\tag{1}
\]

Define

\[
C_d=
\left\{
(R_d(w),e_0):w\in\{0,1\}^{d+1}
\right\}.
\tag{2}
\]

## 3. The theorem

For every `d>=1`,

\[
\boxed{K_d=C_d.}
\tag{3}
\]

The word-to-state map in `(2)` is injective, so

\[
\boxed{|K_d|=2^{d+1}.}
\tag{4}
\]

Under this identification, the two internal kernel edges are exactly

\[
\boxed{
e_0e_1\cdots e_d
\longrightarrow
e_1\cdots e_d a,
\qquad a\in\{0,1\}.}
\tag{5}
\]

Thus the kernel is the binary de Bruijn graph on words of length `d+1`.

## 4. Proof

### Injectivity

Given `(R_d(w),e_0)`, the low residue and current digit determine `e_1` uniquely by the legal-branch table. The resulting integer quotient determines `e_2`, and so on for `d` steps. Therefore two words producing the same state are equal.

### `C_d` is invariant

Fix `w=e_0...e_d` and append `a`. Nestedness gives one digit `h` with

\[
R_{d+1}(wa)=R_d(w)+h64^d,
\qquad0\le h<64.
\]

Starting from this lift and taking one exact step leaves an integer satisfying the suffix itinerary

\[
e_1...e_da
\]
for `d` further transitions. Its residue modulo `64^d` is therefore `R_d(e_1...e_da)`. This is precisely edge `(5)`. Hence every cylinder state has two successors inside `C_d`, so `C_d subseteq K_d`.

### No other state admits an infinite path

Two lifts congruent modulo `64^d` differ by `h64^d`. After one homogeneous update their targets differ by

\[
81h64^{d-1}.
\]

Therefore the target modulo `64^{d-1}` is independent of the chosen high block `h`. More generally, the first `d` forced decisions of an ordinary lift are determined solely by its initial residue modulo `64^d`.

An infinite path in `G_d` supplies at least `d` successive legal decisions. By the preceding precision-loss observation, its initial residue therefore realizes one actual word `e_0...e_d` through `d` integral transitions. It equals the unique cylinder residue `R_d(w)`, and the initial state lies in `C_d`. Thus `K_d subseteq C_d`, proving `(3)`.

## 5. Periodic ghost representation

Repeat a word `w` of length `d+1` periodically. Its unique `2`-adic nearest-integer completion has the same first `d` integrality constraints, so its reduction modulo `64^d` is `R_d(w)`. Hence every fixed-precision kernel state has a periodic `2`-adic lasso representative.

This last observation is used in `R-8701`; it does not make the lasso an ordinary integer.

## Verification

`X-8701` constructs the full ambient graphs through precision three, independently computes their greatest fixed points, verifies the de Bruijn edges and periodic-ghost crosswalk, and checks cylinder injectivity through precision fifteen. The computation is corroboration only; the proof above is uniform in `d`.
