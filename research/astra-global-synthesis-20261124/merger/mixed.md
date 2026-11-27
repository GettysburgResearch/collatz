# One ordinary comparison for arbitrary singleton/pair mixtures

**Status: complete conditional ordinary-path theorem checked in Lean.**
The theorem is `Collatz.MixedPaid.mixed_descent` in
[MixedPaid.lean](MixedPaid.lean). It does not assert universal Collatz
convergence or existence of an infinite positive input path of the type
under consideration.

Use the positive shortcut map `T`, with `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`. At positive odd block boundaries, light `L`
means the two exact odd gaps `(2,1)` and paid `P` means `(1,4)`:

\[
8q'=9q+7\quad(L),\qquad32q'=9q+5\quad(P).
\]

The intermediate odd values are `(3q+1)/4` and `(3q+1)/2`, respectively.

## Statement with the original floor retained

Suppose one fixed ordinary infinite input consists of `L` and `P`
blocks, with every paid cluster having length one or two and at least
three lights between successive clusters. The input can start anywhere
inside a light run or paid cluster. For every block boundary `q_j`,
there is a positive odd ordinary integer `m` such that

\[
m<q_j,\qquad
m<\begin{cases}(3q_j+1)/4&\text{on }L,\\
                 (3q_j+1)/2&\text{on }P,\end{cases}
\qquad T^k(m)\ne1\text{ for every }k\ge0.
\]

Thus the globally least positive nonconverger cannot itself be a
boundary or intermediate of such a supplied infinite input. Singleton
and pair clusters can be mixed arbitrarily and nonperiodically; all
light-run lengths at least three are allowed. There is no upper bound
on those lengths. A smaller nonconverger need not follow the same
language, and the comparison need not merge with the original orbit.
Merely reaching this language later at a larger value does not by
itself beat an earlier original floor.

## The seven-state comparison

Number the phases as a free light, the beginning of the last three
lights before a cluster, two remaining lights, one light before a
singleton, one light before a pair, the first paid block of a pair,
and the last paid block. The allowed transitions are

\[
\begin{gathered}
\mathrm{free}\longrightarrow\mathrm{free}\text{ or }\mathrm{begin},\quad
\mathrm{begin}\longrightarrow\mathrm{two},\\
\mathrm{two}\longrightarrow\mathrm{oneSingle}\text{ or }\mathrm{onePair},\quad
\mathrm{oneSingle}\longrightarrow\mathrm{last},\\
\mathrm{onePair}\longrightarrow\mathrm{pairLead}\longrightarrow\mathrm{last},
\quad\mathrm{last}\longrightarrow\mathrm{free}\text{ or }\mathrm{begin}.
\end{gathered}
\]

At a phase `s` and boundary `q`, put `y=N_s(q)/256`. The table gives
the complete numerator and target affine equation. The bit string is
the actual input parity at each successive shortcut step, with 1 odd
and 0 even.

| Phase | Source block | Numerator `N_s(q)` | Target equation | Literal target bits |
|---|---|---|---|---|
| free | L | `183q+1` | `8y'=9y+5` | `110` |
| begin | L | `183q+1` | `8y'=27y+19` | `111` |
| two | L | `549q+131` | `8y'=9y+10` | `011` |
| oneSingle | L | `549q-13` | `8y'=3y+4` | `001` |
| onePair | L | `549q-13` | `8y'=9y+10` | `011` |
| pairLead | P | `549q-175` | `32y'=3y+1` | `10000` |
| last | P | `183q-37` | `32y'=9y+5` | `11000` |

All these target states are ordinary integers on the supplied path.
Some are even; the proof concerns the literal shortcut map throughout.
Each target block takes the same three or five shortcut clocks as its
source block, while its number of odd steps can differ.

### Integrality from the same input's future edges

Two successive source equations, with their odd endpoints, imply
`q_j >= 17` at every boundary. Checking the odd integers below 17
against the two possible next block equations proves this elementary
bound; it is also an `omega` lemma in Lean. In particular all subtractions
in the table have their ordinary integer meaning.

Write `w_s` for 8 or 32, and `m_s,c_s` for the multiplier and carry
in the target equation. Every allowed transition satisfies the exact
identity

\[
w_sN_t(q')=m_sN_s(q)+256c_s.
\]

Every `m_s` is odd and every `w_s` is divisible by eight. Apply this
identity backwards along the next three actual edges. The first edge
gives divisibility by eight, the next by 64, and the third by 256.
Consequently `256` divides `N_s(q_j)` at **every** position of this
same fixed input. Dividing the identity gives the target equation in
the table with ordinary natural-number endpoints. No limiting 2-adic
source is used in this proof.

### The equations give literal ordinary paths

The seven equations force the source residue of `y` to be, respectively,
`3,7,6,4,6` modulo eight, or `21,3` modulo 32. Substituting those
residues into `T` gives exactly the displayed bit strings and target
endpoints. Thus every row describes a literal 3- or 5-clock ordinary
path, not only a rational affine identity.

All target boundary values exceed two, by the numerator table and
`q_j >= 17`. Their cumulative shortcut times tend to infinity. If a
target orbit hit 1, all later values would belong to the cycle `{1,2}`,
contradicting its later boundary values. This proves that every `y_j`
is a nonconverger. The same argument applied to the source block
equations proves that every `q_j` is a nonconverger.

## Strict comparison with both odd positions

At a free or begin phase, take

\[
m=y=\frac{183q+1}{256}.
\]

Its row forces oddness, and it is positive and strictly below both
`q` and `(3q+1)/4`. For the other phases use a future boundary of the
original input, already known to be a nonconverger:

* At a paid phase, the next boundary is `(9q+5)/32` and is below both
  `q` and its larger intermediate `(3q+1)/2`.
* With one light before the next paid block, the boundary immediately
  after that paid block is `(81q+103)/256`.
* With two lights before it, that boundary is
  `(729q+1391)/2048`.

For `q >= 17`, the last two expressions are strictly below both `q`
and `(3q+1)/4`. These are the two exact finite inequalities `drop1`
and `drop2` in the Lean proof. The chosen boundaries are positive and
odd. This covers every phase, including all permitted initial partial
fragments, without requiring the comparison slope at the other phases
to be below one.

## Raw input statement and formal scope

The final Lean theorem takes Boolean block labels `p : Nat -> Bool`,
ordinary boundaries `q : Nat -> Nat`, and the following local rules:

* `P P` is followed by `L`;
* `P L` is followed by two more `L`'s;
* every boundary is odd and obeys its exact `L` or `P` equation.

Four labels, the present one and the next three, determine the phase.
The theorem constructs this phase track internally and concludes with
one `m` below both floors and the literal predicate
`Bad m := forall k, iter k m != 1`. Its hypotheses do not include a
smaller partner, a supplied comparison orbit, or a convergence oracle.
The Lean file imports only `Std` and contains no admitted claim.

The conditional theorem addresses every actual infinite input satisfying
these hypotheses. It does not prove those hypotheses hold on every
nonconvergent source, and it does not supply an infinite ordinary
realization of an arbitrary symbolic input word.

## Discovery and relation to the earlier obstruction

The coordinating search used the free chart `y=lambda(q+7)-5` and
tested exact signed seeds over the whole tile, permitting changed
target odd counts. The slope `lambda=183/256` gives the two seeds

\[
-31187/2187\quad(LLLP),\qquad
-928747/19683\quad(LLLPP).
\]

Their signed shortcut paths reach `-5` after respectively `(14,8)`
and `(19,10)` shortcut-clock/odd-count pairs. These match the complete
source tiles, so the outgoing slope is unchanged. Decomposing these
paths gives the table above. The final proof replaces this search
criterion with exact ordinary integrality, parity, and floor lemmas.

PP3 in [the earlier paired note](proof.md) restricts preparation on
each light block to two target odd visits with a common slope. Here
the begin block has three odd visits, the oneSingle block has one,
and intermediate slopes change from `183/256` to `549/256`. This is
outside that template. The selected mixed rule also subsumes the
earlier paired-only language with four intervening lights and the
six-separated singleton language at the PR192 source pin. Their
separate proofs and finite-reset statements are preserved.

Paid clusters of length three or more, one- or two-light separations,
and arbitrary odd-gap sequences remain outside this theorem. There
is no universal language-coverage claim.

## Replay and source attribution

[mixed_check.py](mixed_check.py) constructs legal ordinary input
cylinders independently of the comparison table, follows literal `T`
on the comparison, and checks both strict floors. Its normal and
optimized runs cover 581 phase paths, including 233 containing both
cluster types, 12,782 comparison edges and 12,782 simultaneous floor
checks. These finite examples supplement the all-time conditional
Lean theorem; they do not prove its infinite hypotheses are realized.

The normalization and prior singleton comparison are pinned in
[proof.md](proof.md). Generic iteration, parity and unbounded-boundary
lemmas adapt PR192's `descent_Separated.lean` at
`d2081d1cd2410e6004eaee9f9b13c5553afaf3f4`. The seven-state coefficients,
raw mixed-language theorem, and strict comparisons above are the new
construction in this checkpoint.
