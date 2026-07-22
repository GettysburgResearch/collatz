# L-8701 — Monotonicity, chart invariant, and bounded carry

**Claim ID:** `L-8701`  
**Type:** lemma  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Dependencies:** `D-8701`  
**Scope:** every legal ordinary forced-tail step

## Statement

For every legal step

\[
(B,e)\longmapsto(B',e')
\]
of `D-8701`:

1. the residue
   \[
   \boxed{B+4e\pmod{17}}
   \tag{1}
   \]
   is invariant;
2. if `B>0`, then
   \[
   \boxed{B'>B;}
   \tag{2}
   \]
3. the base-64 transducer carry after its first column lies in `{0,...,17}`.

Consequently, any positive ordinary infinite forced tail is automatically divergent.

## Proof

Reducing

\[
64B'=81B+e-e'
\]
modulo `17` and using `64≡81≡13 (mod 17)` gives

\[
13(B'-B)\equiv e-e'\pmod{17}.
\]

Since `13^{-1}≡4 (mod 17)`, equation `(1)` follows.

For monotonicity, inspect the three exact branches. If `B=64Q`, then

\[
B'-B=17Q,
\]
which is positive for `B>0`. On the switching branches,

\[
(64Q+15,1)\mapsto(81Q+19,0)
\]
gives difference `17Q+4`, while

\[
(64Q+49,0)\mapsto(81Q+62,1)
\]
gives difference `17Q+13`. Both are positive.

For the carry bound, after the initial column one has

\[
0\le a_j,a_{j-1}\le63,
\qquad 0\le k_j\le17.
\]

Hence

\[
0\le17a_j+a_{j-1}+k_j\le1151<18\cdot64,
\]
so `k_{j+1}<=17`. The initial offsets `0,19,62` also produce a first outgoing carry at most `17`.

## Interpretation

The invariant is the ordinary chart class: if `A=64B+e`, then

\[
A\equiv13(B+4e)\pmod{17}.
\]

Monotonicity means the constructive problem needs only nontermination; unboundedness follows automatically. It does not prove that a positive infinite path exists.
