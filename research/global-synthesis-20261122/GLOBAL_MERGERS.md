# Global merger and complete-witness closure attempt

**Full Collatz closure remains OPEN.** This pass follows the current
unbounded source-word program through its last grade, rather than extending
a fixed binary residue table. It obtains an explicit height-and-clock
version of the certified alphabet-four predecessor construction. The
attempt to spend the final gap-four grade reaches a separate, unresolved
ordinary inverse-tree membership problem.

The ordinary shortcut map is `T(n)=n/2` for even `n`, and `(3*n+1)/2`
for odd `n`. A gap `a` records the exact positive odd edge
`3*p+1=2^a*q`. A physical merger has two independent ordinary clocks.

## 1. Exact source heads inspected

| PR and head | Source interface used |
|---|---|
| PR177, `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | `research/lean-exact-witness-global-20261121/BOUNDED_GAP_ATTACK.md`, `LOW_INTERVAL_REFINEMENT.md`, `UNBOUNDED_GAP_REWRITES.md`, `PSI_SUFFIX_ATTACK.md`, `MERGER_RETAINED_EVEN.md`, and `lean/Collatz/BoundedGapCofinal.lean`: literal-tail alphabet-four cofinality, one complete-source multiset, and the explicit low-interval obligation. |
| PR176, `8aeb843bba254f065743b6fa277a70906b51d520` | `research/lean-global-resolvent-20261121/overview/parallel/SOURCE_ENVELOPE.md` and `CONTACT_CAPTURE_SYNTHESIS.md`: exact attained source envelope over paid literal cuts, independent-clock merger interface, and a still-open actual contact estimate. |
| PR180, `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `research/lean-wide-pass-20261122/WITNESS_SYNTHESIS.md`: arbitrary dyadic physical erasure compiled into the same complete-source order, and the remaining carry pair `(r,9*r+2)`. |
| PR185, `276be8154f4e867acc0230466b34d9cb224aacf5` | `research/whole-repo-closure-20261122/CARRY_LANGUAGE.md`: the literal-source language `1 {2,3}* 2 1`, with exact target endpoint one below the retained source endpoint. |
| PR183, `907a540943090968bc683b1b9246208e9053c1f8` | `research/literature-closing-20261121/mergers/CONSTRUCTIVE_NORMAL_FORM.md`: one matrix rank, complete blocked grammar, physical `f11` erasures, and the open all-normal-form erasure cover. |
| PR178, `be5696cc45a95ad1903802b08ba1dc3ebba66930` | Existing `research/reframe-20261121/UNIVERSAL_MERGERS.md` and `research/literature-reframe-20261122/PHYSICAL_MERGERS.md`: marked prefix inheritance and the unequal-clock physical tail barrier. These are retained, not repeated as new results. |

These are source inspections at the displayed heads. The new local Lean
module is checked separately; this note does not claim a new replay of all
five upstream projects.

## 2. An explicit all-bound alphabet-four selector

Fix a positive odd ternary unit `q` carrying its actual complete odd tail
`tau`, and let `N >= q`. Reuse exactly PR177's six-row inverse selector:

| `q mod 18` | gap `a` | selected predecessor, with `q=18v+r` |
|---:|---:|---:|
| 1 | 4 | `96v+5` |
| 5 | 3 | `48v+13` |
| 7 | 4 | `96v+37` |
| 11 | 3 | `48v+29` |
| 13 | 2 | `24v+17` |
| 17 | 1 | `12v+11` |

Each output is an odd ternary unit greater than one and satisfies
`3*p+1=2^a*q`, with `1<=a<=4`. In particular, the source-one row takes
`5 -> 1`, not a repeated terminal self-loop.

Let `C(N)` be the number of positive odd ternary units at most `N`:

\[
C(N)=\left\lfloor\frac{N+5}{6}\right\rfloor+
     \left\lfloor\frac{N+1}{6}\right\rfloor.
\]

The new quantitative conclusion is

\[
\boxed{N<p,\qquad 3p<16N,\qquad
       |W|\le C(N),\qquad \sum W\le4C(N),}
\tag{G1}
\]

where every letter of `W` is in `{1,2,3,4}` and the complete source
certificate is literally `W ++ tau`. Thus the predecessor lies in a fixed
multiplicative window and has an explicit finite prefix-clock budget.
There is no unspecified basin-clock bound and no search cutoff in this
selector. The supplied tail is unchanged.

**Proof.** Iterate the selected inverse edge. Every selected vertex reaches
the preceding vertex through a nonterminal ordinary path: the starting
odd vertex exceeds one, and all intermediate values are positive even
integers. Therefore the least ordinary hitting time of one strictly
increases at each inverse edge. The selected vertices are pairwise
distinct. Among the first `C(N)+1` vertices, one must exceed `N`; all
vertices are positive odd ternary units. Stop at the first crossing.
Its predecessor is at most `N`, so its edge gives
`3*p+1 <= 16*N`, hence the height bound in (G1). The number of edges is
at most `C(N)` and each costs at most four ordinary clocks. Reverse the
selected edge labels to obtain the forward word `W`, then concatenate the
unchanged supplied tail.

This argument strengthens PR177's `cofinal_predecessors` quantitatively;
the inverse table and its alphabet threshold are credited to that source.
The formal theorem uses `C(N)` as the cardinality of the displayed finite
set. The elementary floor formula above is an exact count of residues one
and five modulo six. The explicit selector implementation checks that
count, every positive edge, the retained tail, the window, and the clock.

**Formal status:** `lean/QuantitativeInverseSelector.lean` compiled with
Lean 4.34.1 and `-j1 -DwarningAsError=true`. Its strongest public theorem is
`CollatzShell.QuantitativeInverseSelector.bounded_window_literal_tail`.
The companion audit checks all eleven public theorems, whose axioms are
subsets of `propext`, `Classical.choice`, and `Quot.sound`. The module imports
the existing `ShellCover` ordinary map; it defines no replacement dynamics.
The final clean-checkout publication replay remains a separate event.

## 3. Attempt to remove the last grade

The common source rank is

\[
\Gamma(e;A)=\bigl(\{2e+1\}\text{ if }e>0\bigr)
             \uplus\{2a:a\in A\}.
\]

At the largest changed grade, multiplicity must decrease. One removed gap
at least five pays for any finite four-letter prefix. An initial even run
at least four does likewise. The explicit window in (G1) now bounds that
replacement's height and prefix clock, but leaves the rank payment exactly
as in PR177.

To spend a gap **four** by the same mechanism, the inserted prefix would
need gaps at most three. This motivates the full inverse graph

\[
I_a(q)=(2^a q-1)/3,\qquad a\in\{1,2,3\},
\]

retaining positive odd ordinary vertices. A ternary-nonunit child is a
terminal leaf. On unit input residues `(1,2,4,5,7,8)` modulo nine, the
unit-child outdegrees are exactly `(1,2,1,1,0,1)`. Their mean is **one**.
There is no subcritical counting contraction available from that table.

Consecutive exponent-two edges can be eliminated exactly:

\[
q_j-1=(4/3)^j(q_0-1).
\tag{G2}
\]

For `q_0 != 1`, the number of consecutive integral edges of this kind is
at most `v_3(q_0-1)`. At `q_0=1`, it is the terminal fixed loop. However,
gap-one/gap-three branching can start a new valuation episode. Summing
the individual episode bounds does not establish a global finite bound.

### A complete symbolic extinction family

There is an exact all-depth class, rather than only a residue census.
Let `h>=1`, let `u>0` be even with `u=2 mod 3`, and set

\[
q_0=1+3^h u,\qquad
q_j=1+4^j3^{h-j}u\quad(0\le j\le h).
\tag{G3}
\]

The **entire** ordinary cap-three predecessor graph of `q_0` is the single
chain `q_0,q_1,...,q_h`. Each edge has gap two, each vertex before the last
is a unit, and the last vertex is divisible by three and has no odd
predecessor. Its largest vertex is exactly `1+4^h*u`.

For `j<h`, the input `q_j` is one modulo three. Integrality of
`(2^a*q_j-1)/3` with `1<=a<=3` forces the even exponent `a=2`, and direct
substitution gives `q_{j+1}`. At `j=h`, the residue is `1+u=0 mod3`, so
no exponent yields an integral odd predecessor. Strict increase follows
from (G2). This proves the full graph description for every `h,u`, with
no convergence assumption on the root and no finite graph search.

More generally, for any odd `q_0>1` with `q_0=1 mod3`, write
`q_0-1=3^h*u` with `3` not dividing `u`. Its entire first valuation block
is (G3). If `u=2 mod3`, it ends at the leaf just proved; if `u=1 mod3`, it
ends at a branching input two modulo three. The latter case is exactly
where this symbolic classification stops.

For a supplied complete certificate at a root in the finite-chain class,
every cap-three source replacement has been classified, including its
maximum height and the exact retained tail. A replacement above a requested
bound `N` exists within this class exactly when `N<1+4^h*u`. This can be
used to extend a literal-cut envelope by a proved finite inverse-prefix
envelope. It cannot be promoted to cofinality when `N` is larger. This
classification is a written arithmetic theorem; it is not included among
the eleven new Lean declarations.

### Certified roots with every prescribed finite cap-three depth

The finite-chain obstruction occurs on an explicit growing family of
fully certified ordinary roots. For every `h>=1`, put

\[
k=1+2\cdot3^h,\qquad q=\frac{4^k-1}{3}.
\tag{G4}
\]

The single odd gap `2k` takes `q` to one. Moreover `q-1=3^h*u`, where
`u` is positive, even, and two modulo three, so G3 classifies its entire
cap-three predecessor graph at arbitrary depth `h`.

Here is a direct divisibility proof, without an assumed valuation formula.
Define `A_h=4^(3^h)`. Induction gives

\[
A_h=1+3^{h+1}v_h,\qquad v_h\equiv1\pmod3.
\]

The initial case is `v_0=1`. Cubing `A_h` gives the integer recurrence

\[
v_{h+1}=v_h+3^{h+1}v_h^2+3^{2h+1}v_h^3,
\]

which preserves that residue. Since `k-1=2*3^h`,

\[
q-1=\frac{4(A_h^2-1)}3
     =3^h\,[4v_h(A_h+1)].
\]

The bracket is the desired `u`, and its residue is two. Therefore every
cap-three predecessor of this certified `q` is at most `1+4^h*u`.
This refutes a universal cofinal cap-three literal-tail replacement even
on an unbounded family of actual supplied certificates. The tails in G4
contain the large gap `2k`; they do **not** refute a selective strategy on
the remaining alphabet-four source language. No assertion about a failed
Collatz orbit follows from this finite inverse-graph obstruction.

The executable finite explorations found complete finite cap-three trees
for roots `5,31,37,101`, of respectively `16,28,808,524` ordinary vertices
and maximal inverse depths `7,15,80,92`. These include nonunit leaves.
They are independently reproducible finite closures, not evidence of an
all-root extinction theorem. In particular, the root `37` reaches values
with 48 binary digits before its finite tree closes; local real-height
monotonicity is unavailable.

The first unsupported step of the attempted grade-four replacement is
now precise: prove sufficient cofinal cap-three ancestry for every tail
that needs it, or prove and exploit a complete finite alternative. Neither
critical branching counts nor the finite examples give either statement.
At the terminal tail `q=1`, cap-three ancestry consists only of one, so
cofinal replacement there is explicitly impossible. A complete strategy
must use target motion or another valid source rewrite at that boundary.

## 4. Compatibility with the other new global interfaces

The literal-cut envelope of PR176 is maximal only over literal prefix
deletion plus a replacement initial even run. It does not dominate every
cap-three inverse prefix. A successful cap-three source replacement could
therefore enlarge that envelope, but its existence and its height must be
proved on the same supplied tail.

The PR185 carry language consumes a complete prefix, lowers the source
grade, and reaches the active interval through `u-1`. Its states `D_1`
and `D_2` do not form a total machine: an initial source gap at least two,
an internal gap four, or `D_2` followed by gap one can leave that machine.
Replacing the target intercept to force it back would change the target
whose convergence must be proved. No such substitution is made here.

The mixed-base rank in PR183 belongs to a different program. Its rightmost
blocked pair proposes

\[
n=3^k(6q+1)+r,\qquad m=3^k(2q)+r,
\qquad0\le r<3^k.
\]

The rank and ordinary value both decrease under the proposed erasure.
The identity `n=3m+1` holds exactly when `2r=3^k-1`; the known odd-length
all-ones suffix family then gives an actual one-clock merger. For general
ternary suffixes, the carry is instead `3^k-2r`, which can be positive
or negative and is not automatically the ordinary `+1` carry.
Thus the two-state carry language cannot simply be attached to every
mixed-base erasure. A common physical endpoint remains necessary.

The current positive synthesis is therefore an explicit, bounded-cost
all-input selector **within the already certified high-grade domain**,
plus a sharply identified last-grade arithmetic problem. It does not
prove `LowIntervalStep`, a universal physical merger, or full Collatz.

## 5. Primary literature considered in this attempt

The historical relation of restricted least inverse branches to Mahler's
`Z`-number problem is discussed in entry 14 of Lagarias's
[*Annotated Bibliography (1963–1999)*, arXiv:math/0309224v13](https://arxiv.org/pdf/math/0309224v13),
read directly here. That entry describes the partially defined branches
`(4n-1)/3` and `(2n-1)/3` and an avoidance question for multiples of three.
This is a bibliographic account of Banerji's work, not an imported solution
of the integer avoidance problem; the terminal root-one loop is separately
retained in our graph.
A current primary public note, *Exact avoidance in the Collatz inverse
graph with exponents at most four* (4 November 2026),
<https://rstation.ai/problems/collatz/papers/96>, explicitly leaves
positive-integer membership in its forced survivor open. Its target,
alphabet, and exceptional completion set differ from cap-three extinction.
It was inspected to locate the arithmetic boundary; its proof and finite
certificates are **not imported** as established inputs to this Lean work.

The earlier Monks arithmetic-progression sufficiency and the
Yolcu–Aaronson–Heule mixed-base interpretation remain attributed through
the exact source packets above. Neither predecessor sufficiency nor an
independently decreasing rewrite rank supplies the absent universal
source-and-target selector.

## 6. Execution and formal scope

```sh
python -X utf8 -B research/global-synthesis-20261122/inverse_alphabet_selector.py \
  --replay --output selector-replay.json
python -X utf8 -O -B research/global-synthesis-20261122/inverse_alphabet_selector.py \
  --replay --output selector-optimized-replay.json
```

Both executions returned identical JSON. The twelve supplied-certificate
fixtures use roots `1,5,37,85`, including an inherited tail with gap eight,
at thresholds up to `2^256`. The longest selected prefix in those fixtures
has 244 odd edges and 643 ordinary clocks. These numbers describe the
finite replay only. The arbitrary-threshold, arbitrary-tail conclusion is
the Lean theorem (G1), with its explicit premises.

The four cap-three explorations additionally replay every legal inverse
edge out of every retained vertex and confirm that the finite sets are
closed. Their vertex hashes are recorded by the script. Those are complete
finite graph computations, not an all-positive-root extinction proof.
The script also checks fifteen G3 instances through depth 128 and five
fully certified G4 instances through `h=5`, including their exact one-gap
tails. These are finite replays of the separate written all-parameter
proofs, not additional Lean declarations.

The eleven public theorem declarations are `selected_spec`, `odd_gap_path`,
`odd_gap_nonterminal`, `firstTime_increases`, `GapPath.append`, `GapPath.run`,
`GapPath.start_odd`, `walk_path`, `walk_injective`,
`crosses_within_window_card`, and `bounded_window_literal_tail`, in namespace
`CollatzShell.QuantitativeInverseSelector`. The first is the attributed
six-row selector replay; the new quantitative conclusion uses the
nonterminal first-hit comparison, injectivity, and attained first crossing.
