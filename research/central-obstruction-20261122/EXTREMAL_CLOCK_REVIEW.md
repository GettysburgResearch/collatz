# Independent review: extremal-source clock counterexample

2026-11-22. **Verdict: PASS. No mathematical correction required.**

Reviewed the all-certificate argument against the literal baseline
`GradeDrop`, `sourceGrades`, `PoweredTrace`, `GapTrace`,
`low_complete_is_one`, and `single_four_language`. Independently checked
the two exact source traces, grade multiplicities, source clock, and target
orbit. As requested, no Lean recompile was performed; the coordinating
agent's fresh publication replay supplies that check.

## Frozen inputs

| File | SHA256 |
|---|---|
| `central_escape/EXTREMAL_SOURCE_CLOCK_FAILURE.md` | `e60e0744d5d9d88f2f417050aff2cd73c1f1831815ccedb365f9311912cb9ded` |
| `central_escape/ExtremalSourceClock.lean` | `83da6bb58074c104221e27e58c0726289bf4ef324d9cd31f50ceba1d49bd668e` |
| Baseline `WitnessSynthesis.lean` | `8bee9e1caa0c914d77f0a37f86bbd6caa5dbd27be607c7d03783e7463219cadd` |
| Baseline `WitnessGlobal.lean` | `37cc56085ad5d9e3a313af3f9e7dd3d041a697cda199db42eb452e321164a4e6` |

The baseline paths are under
`collatz_central_20261122/research/whole-repo-closure-20261122/lean/vendor/`.

## Why the global maxima are proved without a cutoff

The repository relation is exactly

\[
\operatorname{GradeDrop}(g',g)\iff
\exists a:\operatorname{count}_{g'}(a)<\operatorname{count}_{g}(a)
\ \text{and}\ 
\forall b>a:\operatorname{count}_{g'}(b)=\operatorname{count}_{g}(b).
\]

Its grades are the optional initial odd grade `2e+1`, followed by twice
each odd-source valuation. Thus the note correctly uses multiplicities
and equality of multisets, not list order.

For the displayed `G`, any complete certificate at smaller or equal
grade has no grade above eight, hence no gap above four and `e<=3`.
There is at most one gap four. With no gap four,
`low_complete_is_one` forces the odd source to be one, giving powered
source at most eight. With one gap four, the grade-eight multiplicity
matches `G`; an initial exponent three would create a larger grade-seven
multiplicity, so `e<=2`.

Splitting at the unique four is legitimate for arbitrary word length.
The remaining low-gap complete suffix starts at one, and every such
suffix consists solely of twos. The previously proved
`single_four_language` therefore applies with arbitrary padding. Its
source set has largest member `273`, with every other member at most
`205`. Consequently all complete powered sources at grade at most `G`
are at most `4*273=1092`, and the displayed certificate attains this.

For the strict maximum, the only possible powered source above `820`
is `q=273,e=2`. Every complete `GapTrace` has odd intermediate states:
a nonempty next edge forces its input odd, and the terminal endpoint is
one. Hence each gap is the exact valuation, and the complete trajectory
from 273 is forced up to first arrival at one. Every certificate is the
displayed word followed by arbitrary twos. With `e=2`, zero padding has
grade `G`; positive padding raises the grade-four count with every higher
count unchanged. Neither is strictly below `G`. Initial exponents zero
or one give sources at most `546`, including arbitrary padding. All
other one-four sources are at most `4*205=820`. The given 820 certificate
is strictly smaller at grade four, so **820 is the attained global strict
maximum**. No finite census or unproved bound on padding is used.

## Independent exact arithmetic

The independently replayed odd trajectory is

\[
273\to205\to77\to29\to11\to17\to13\to5\to1,
\]

with exact gaps `[2,3,3,3,1,2,3,4]`. Its grade counts are
`{8:1,6:4,5:1,4:2,2:1}`. The 820 certificate removes the first gap,
decreasing only the grade-four count from two to one.

Direct shortcut iteration independently confirmed

\[
T^{23}(1092)=1,\qquad T^{23}(2047)=283763,
\]

\[
\min_{1\le j\le57}T^j(2047)=2134>2047,
\qquad T^{58}(2047)=1067<2047.
\]

The new-interval assertion is strict and correct:
`1641=2*820+1 < 2047 <= 2*1092+1=2185`.
The Lean declaration over `Fin 57` covers exactly clocks 1 through 57;
the endpoint declaration supplies clock 58. The all-word maximality
argument is properly labelled written, rather than included in the eight
new finite Lean declarations.

## Scope

This disproves the proposed universal full-interval descent bound by the
maximal source's own clock. It does not address a larger allowed target
clock, all merger policies, or the narrower psi-head-three target family.
In particular, `2047=8q-1` would require `q=256`, which is not an odd
source of the residual class `q=256j+173`. The note explicitly preserves
that distinction. No changes were made to the author's files.
