# Uniform negative-nine returns and a source-clock constraint

## Proved positive result

`lean/Collatz/LowGapGlobal.lean` proves an unbounded return theorem for every
complete supplied odd-source certificate. Write the common active interval
as

\[
I(s,t):\quad 0<t\le2s+1,
\]

and retain the existing complete-source grade

\[
\Gamma(e;W)=
([2e+1]\text{ if }e>0\text{, otherwise }[])
\mathbin{++}\operatorname{map}(2\cdot,W).
\]

The hypotheses below are the existing lower-rank interval induction
hypotheses for the supplied source. The new theorems construct successful
queries inside that interval; they do not assume a new active-domain
coverage statement.

**Uniform affine cone.** Given any complete certificate for the odd source
\(q\), every target satisfying

\[
0<t\le9q+3,\qquad t\equiv q+3\pmod4
\]

returns through a strictly lower complete-source grade. In particular, the
negative-nine carry \(9q-1\) returns for every such source. There is no
bound on the source, its certificate length, or any supplied exponent.

**Positive-nine returns.** For the target \(9q+2\), the complete source
prefix may be either

\[
[1]\quad\text{or}\quad[2,1],
\]

followed by an entirely arbitrary supplied tail. These are genuine ordinary
target transports followed by lower-rank interval queries. The literal tail
is retained at the specified split, and subsequent source steps consume its
actual initial entries.

The formal theorem names are:

- `CollatzLowGapGlobal.odd_source_cap`
- `CollatzLowGapGlobal.nine_lattice_return`
- `CollatzLowGapGlobal.negative_nine_return`
- `CollatzLowGapGlobal.positive_nine_first_one`
- `CollatzLowGapGlobal.positive_nine_two_one`

The module passed Lean 4.34.1 with `-DwarningAsError=true`. It imports only
the existing `LowIntervalRefinement` module and adds no axioms or admitted
proofs.

## Why the return is uniform

For a nonterminal odd source \(q\), its first ordinary shortcut step is

\[
T(q)=\frac{3q+1}{2}.
\]

The existing `ordinary_step` theorem supplies the actual complete child
certificate and proves its strict grade decrease. Its interval ceiling is

\[
2T(q)+1=3q+2.
\]

Thus any positive target at most \(3q+2\) is already a successful query.
The source \(q=1\) uses the previously proved finite terminal base.

For the larger cone, split only on \(q\bmod4\):

| Source phase | Forced target divisibility | Target bound after division | Source steps |
| --- | --- | --- | --- |
| \(q\equiv1\pmod4\) | \(4\mid t\) | \(t/4\le3q+2\) | One |
| \(q\equiv3\pmod4\) | \(t\equiv2\pmod4\) | \(t/2\le3T(q)\) | Two |

In the second row, \(T(q)\) is itself odd, so the same odd-source cap
applies to its inherited complete certificate. The two strict grade
decreases compose. Division of an even target preserves its ordinary basin
membership. This proves the cone at all source sizes and all witness
lengths.

For a source beginning with gap one, write

\[
3q+1=2u.
\]

The positive-nine target has the exact ordinary step

\[
9q+2=6u-1\longmapsto9u-1.
\]

The last value is in the returned cone for the complete certified source
\(u\). Deleting the literal first source gap makes its whole inherited
rank strictly smaller than the original rank.

For source prefix \([2,1]\), splitting the supplied witness gives

\[
9q+7=8u.
\]

The target uses the exact positive-gap prefix \([1,2]\):

\[
9q+2\xrightarrow{[1,2]}9u-5.
\]

Indeed, \(9(9q+2)+5=8(9u-5)\). The endpoint is positive and satisfies
\(9u-5\equiv u+3\pmod4\), so the same cone closes it. The compiler
verifies integral ordinary prefix legality, not merely a rational identity.

## Relation to the latest carry language

The comparison source is PR185 at
`276be8154f4e867acc0230466b34d9cb224aacf5`, specifically
`research/whole-repo-closure-20261122/CARRY_LANGUAGE.md` and its accompanying
`CarryLanguage.lean`. That packet proves the supplied-source language

\[
1\,\{2,3\}^{*}\,2\,1
\]

for the positive-nine carry. It tracks negative-one intercepts at the same
total clock as a selected source prefix. The new return removes all
restrictions after the initial gap one. It does so by allowing additional
target halvings and advancing the actual source once or twice, using the
existing complete-source rank at the end of the block. No unrestricted
certificate is obtained from an earlier target query and then reused as if
its grade were controlled.

The additional prefix \([2,1]\) follows from the same affine cone with
intercept minus five. The general positive-nine carry on source prefixes
starting with two but not covered here, or starting with three or four,
is not asserted to be closed. The complete global interval dispatcher also
remains unproved.

## Exact obstruction to an unrestricted source-clock override

The separate executable `gap-search/high/clock_rank_cycle.py` preserves a
concrete cycle that any proposed hybrid rank must avoid. Fix the target
\(t=73\). The following are complete, unpadded source witnesses; the
clock is their exact first shortcut hitting time of one.

| Source | Initial even run | Complete odd-gap word | Clock |
| --- | --- | --- | --- |
| 77 | 0 | \([3,3,1,2,3,4]\) | 16 |
| 116 | 2 | \([3,1,2,3,4]\) | 15 |
| 176 | 4 | \([1,2,3,4]\) | 14 |
| 272 | 4 | \([2,3,4]\) | 13 |
| 416 | 5 | \([3,4]\) | 12 |
| 640 | 7 | \([4]\) | 11 |
| 1024 | 10 | \([]\) | 10 |

Each of the six downward table moves increases the known ordinary source
and decreases its exact source clock by one. The fixed target remains
inside every source interval. After the first ordinary odd step, these
moves apply the next odd operation ahead of the source's retained even run.

There is then a valid alphabet-four return from source 1024 to source 77,
preserving the empty literal suffix. Its grade comparison is

\[
[6,6,2,4,6,8]<[21],
\]

and its source still exceeds the chosen target: \(77>73\). Thus this
last edge satisfies even the cofinal construction's stronger chosen-source
bound, not only the active interval condition.

Consequently, the union of **all** these source-clock overrides and
**all** such lower-grade cofinal resets contains a directed cycle at one
fixed target. No well-founded relation can orient every edge of that union
downwards. This excludes the unrestricted hybrid proposal; it does not
exclude a target-dependent selection, a smaller allowed set of clock
overrides, or the target-changing returns proved above.

The executable independently checks every odd edge, every ordinary step,
the exact first hitting clocks, the strict source increases, the final
highest-changed-grade comparison, the unchanged suffix, and all fixed-target
interval bounds. Its checks stay active under `python -O`. This exact
cycle is a finite obstruction witness, not a finite census used to infer
universal behavior.
