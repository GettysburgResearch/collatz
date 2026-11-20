# PR170 comparison: carry four and terminal phase

**Frozen latest-source cutoff for this pass:** PR170,
`656063d5efa0f5708356ab2563a4348d39bae013`.

The exact files read in full were
`research/global-forcing-20261121/certificates/CARRY_COMPILER.md` and
`research/global-forcing-20261121/energy/TERMINAL_PHASE.md`.

**Outcome:** the carry-four family is a useful new explicit unbounded
transport. Its completed blocks still belong to the existing homogeneous
architecture. The terminal-phase theorem gives a broader architecture
obstruction that should be credited in any new terminal-one specialization.
Neither file proves the missing global closure. No frozen UF proof,
checker, or report was changed.

## 1. What the carry-four construction actually adds

With

\[
E=(2,1,1,1,2,1,7),\qquad F=(3,6,1,2,1,1,1),
\]

the source and target enter the state `(y,5y+4)`. The correction identity
is `B(F)-5B(E)=4*2^15`, with `B(E)=3709` and `B(F)=149617`.
The next source valuation-one step preserves the affine carry exactly:

\[
U(5y+4)=5U(y)+4.
\]

The exit `(3,b)` on the source, `b>=2`, corresponds to `(4,b-1)` on the
target and returns to the proportional pair `(q,5q)`. Thus every full block

\[
E\,1^r\,(3,b)\quad\longmapsto\quad F\,1^r\,(4,b-1)
\]

has the same `r+9` odd inputs and the same clock `r+b+18`. Its explicit
unit first-hit witnesses exist at every rank at least nine.

This gives an explicit mechanism for arbitrarily long valuation-one runs
inside a nonzero comparison state. It is different from our UF1 families
`(1,2^r,1,a,b)`, `a=2,4`. The carry entry starts `(2,1)`, our new families
start `(1,2)`, and the old PR166 ladder requires its initial run of twos
to be followed by an exponent at least four. These displayed block families
are distinct.

However, a completed carry block still satisfies `B(target)=5B(source)`
and preserves both total resources. Consequently the entire block is
already accepted by the complete decoder of PR167 HT1/HT2 and PR168
FR1/FR3. A nonzero state inside a block does not, by itself, escape that
architecture when the block returns to the same proportional endpoint.

PR170's separate `(1,1,1,b)` block is the existing row classified in
PR167 and repeated in PR168. Our UF attribution already credits that row
to PR167, so no correction to our novelty statement is needed.

### Height requires separate accounting

The carry family does not uniformly decrease from source to endpoint.
Its source-to-endpoint leading factor is
`3^(r+9)/2^(r+b+18)`, which can exceed one. Therefore our UF endpoint
bound `q<=x/7` and our inverse-fiber renewal cannot be transferred to it.

A precise possible use in the other direction follows from its own
formula. At `r=10,b=2`,

\[
x=\frac{2^{30}q-1351\,3^{15}-2^{26}}{3^{19}},
\qquad 2^{30}<3^{19}.
\]

Hence every positive integral ordinary realization has `x<q`. If `q`
were a five failure and this inverse source were a ternary unit, the two
ordinary arms would produce the smaller failure `x`: its convergence is
certified by the source path to the known `q`. This is a legitimate
endpoint-class descent, conditional on the full inverse guards. It does
not cover arbitrary `q`; neither congruence coverage nor a global
well-founded return follows from this one identity.

## 2. The terminal-phase statement is broader than a terminal-one test

PR170 credits the established stopping grade from PR146,

\[
H(n)=\tau(n)-2r(n),\qquad
\Delta(x)=H(5x)-H(x),
\]

where the grades are defined when the corresponding ordinary paths
converge. Its TP1 applies to actual ordinary edges in either direction.
For a native affine path of slope `3^j/2^k`, the grade change is `k-2j`.
Two whole-family paths sending `(x,5x)` to `(q(x),5q(x))` have equal
native slopes, and unique factorization forces equal signed `j,k`.
Therefore they preserve `Delta`, even with reverse edges, unequal path
lengths, adaptive choices, and an infinite dictionary.

TP2 consequently excludes completeness with **any terminal parameter set
whose certified phases are bounded below**, not just terminal parameter 1
and not just a fixed finite block dictionary. Every finite certified
terminal library meets that bounded-below condition.

The proof uses the already known one-step sources
`x_a=(4^a-1)/3`, with `a>=2` and `3` not dividing `a`. Their five multiples
have at least `2a-1` odd inputs before a possible first hit. Conditional on
target convergence, the actual orbit product gives

\[
2^{\Delta(x_a)}<\frac{20}{3}(5/6)^{2a-1},\qquad
\Delta(x_a)<(13-2a)/4.
\]

If a purported compiler succeeded, its terminal certificate would first
establish target convergence, making the grades valid. Their preservation
would then contradict the terminal lower bound. Thus no convergence of
the entire target family is assumed in the obstruction.

The carry-four completed blocks, all our UF blocks, and the earlier
balanced dictionaries preserve this same phase. PR170 explicitly leaves
open exits with different comparisons, singleton ordinary certificates,
or terminal classes with unbounded phase, provided a new coverage and
termination proof is supplied.

## 3. Consequence for the root's NB3 and for closure

The root's NB3 hard-prefix/terminal-1 argument should be described as a
quantitative application of the existing grade, with the general grade
credited to PR146 and the broader bounded-below terminal-library theorem
credited to PR170 TP1--TP2. A new exact hard-prefix calculation or bound
can remain a separately stated specialization; the phase invariant and
general terminal-library obstruction should not be presented as newly
discovered there.

The carry construction does not transform the hard negative state into
its positive carry four. In particular the remaining target

\[
3^{2m+2}(5\,2^{b-3}q-1)-1
\]

is not absorbed by the displayed entry/loop/exit. The carry theorem assumes
the specific actual entry word `E` and a specified exit. It does not show
that an arbitrary supplied certificate reaches either guard.

The phase obstruction also does not refute an energy proof supported on
hypothetical nonzero defects: it is invoked after a successful compiler
would establish convergence, and the explicit certified examples have
zero defect. It supplies no absolute upper bound on untreated energy.

There is therefore no closing implication to import from these two files.
The useful additions are the explicit carry mechanism and the precisely
broader statement about permitted terminal libraries.

## Frozen UF snapshot

The completed transport proof remains SHA-256
`24dfeff2089771c4ac03587bdb68a2cae6886399230dc38df2746f22092bcd23`.
Its checker remains
`8b5227e5579769aab6edf823fa6387c397ac17aa22f7a40ba360ddd906c1a2a4`,
and its normal/optimized report remains
`2ba847fc1f42a6fcb23978583fa6563e2c2c3d1ec18061532134dcb66a029ece`.
No PR170 numerical or energy constant is imported into those files.
