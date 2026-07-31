# T-6602 — divergent orbits have an all-supercritical two-place tangent

**Claim ID:** `T-6602`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6601`; elementary parity-cylinder bijection  
**Scope:** positive shortcut-Collatz trajectories tending to `+infinity`  

## Statement

Let

\[
x_k=T^k(n)
\]

be a positive ordinary orbit satisfying

\[
x_k\longrightarrow+\infty.
\tag{1}
\]

Then there are increasing indices `s_i` and values

\[
h_i=x_{s_i}
\]

with all of the following properties.

1. **Tail-minimum property**
   \[
   T^m(h_i)\ge h_i
   \qquad(m\ge0).
   \tag{2}
   \]
2. **Archimedean escape**
   \[
   h_i\longrightarrow+\infty.
   \tag{3}
   \]
3. **Coefficient-depth escape**
   \[
   \boxed{\tau(h_i)\longrightarrow\infty.}
   \tag{4}
   \]
4. **Orbit-supported supercritical tangent**  
   There is an infinite binary word
   \[
   v=(v_0,v_1,\ldots)
   \]
   and a subsequence of the `h_i` such that, for every `L`, infinitely many of those ordinary tail minima have first `L` parity bits equal to `v_0\ldots v_{L-1}`, and
   \[
   \boxed{3^{q_L(v)}\ge2^L\qquad(L\ge1).}
   \tag{5}
   \]
5. **Two-place convergence**  
   Let `xi in Z_2` be the unique 2-adic integer with parity word `v`. A further diagonal subsequence satisfies
   \[
   h_{i_j}\longrightarrow\xi\quad\text{in }\mathbf Z_2,
   \qquad
   h_{i_j}\longrightarrow+\infty\quad\text{in }\mathbf R.
   \tag{6}
   \]

Thus divergence creates an exact all-prefix-supercritical tangent, but its ordinary realizers escape at the Archimedean place.

## Proof

### 1. Tail minima

Because `(1)` holds, every tail

\[
\{x_k:k\ge r\}
\]

has a least value. Choose `s_0` at the global tail minimum and recursively choose `s_(i+1)>s_i` at the least value of the tail beginning after `s_i`.

A trajectory tending to infinity cannot repeat a value, since a repetition would make it eventually periodic. Therefore the selected values are strictly increasing. This proves `(2)` and `(3)`.

In particular,

\[
t(h_i)=\infty.
\]

### 2. Coefficient depth

Fix `L`. By `(3)`, eventually `h_i>H_L`. Applying `T-6601` to `(2)` gives

\[
\tau(h_i)>L
\]

for every sufficiently large `i`. Since `L` was arbitrary, `(4)` follows.

### 3. Compact tangent word

Let `p_i` be the infinite parity sequence of the orbit starting from `h_i`. The compact product space

\[
\{0,1\}^{\mathbf N}
\]

contains a convergent subsequence, say `p_(i_j)->v`.

Product convergence means that for every fixed `L`, all sufficiently late `p_(i_j)` have exactly the prefix `v_0...v_(L-1)`. By `(4)`, their first `L` coefficients are all at least one. The coefficient depends only on that finite parity prefix, so `(5)` follows.

By thinning the subsequence in the usual nested-cylinder construction, every finite prefix of `v` occurs at infinitely many of the selected wave minima.

### 4. The 2-adic tangent

The finite parity-vector bijection gives one residue modulo `2^L` for every length-`L` word. The compatible residues of the prefixes of `v` select one unique `xi in Z_2`.

Choose the diagonal subsequence so that `h_(i_j)` agrees with `v` for at least `j` parity steps. Then

\[
h_{i_j}\equiv\xi\pmod{2^j},
\]

which proves 2-adic convergence. Real divergence is inherited from `(3)`. This proves `(6)`. ∎

## Relationship to PR #76 and PR #77

The least-counterexample gate of PR #76 uses minimality only to obtain a no-descent start above the verified floor. Every sufficiently late `h_i` has those same properties. Thus the Farey gate, once independently verified, applies branch-qualifiably to every such wave minimum, not only to the globally least counterexample.

PR #77 shows that a positive ordinary realization of the tangent word `(5)` would tend to `+infinity`. `T-6602` shows why this still does not finish the proof: compactness may select a genuine 2-adic tangent while its actual ordinary realizers move to infinity.

## Gap audit

- The theorem assumes a divergent orbit; it is a necessary-structure theorem, not a nondivergence proof.
- The 2-adic tangent `xi` need not be an ordinary integer.
- If `xi` is a positive ordinary integer, it is itself a coefficient-supercritical divergent counterexample; the theorem supplies no contradiction.
- If `xi` is nonordinary, it is an orbit-supported completion ghost.
- Positive entropy, branching, or pointwise growth does not supply the missing Archimedean bound.
