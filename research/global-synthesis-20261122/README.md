# Global synthesis: independent cycle exponents, escape moments, and complete tails

**22 November 2026. Full Collatz remains OPEN.** This continuation starts
from PR178 at `be5696cc45a95ad1903802b08ba1dc3ebba66930` and the refreshed
repository-wide research map. It develops three globally quantified
extensions of the latest work. None of the unresolved final estimates is
installed as a Lean axiom.

## What this pass establishes

| Route | New conclusion | Evidence and boundary |
|---|---|---|
| Cycle arithmetic | Every supplied product `V1^e1 ... Vr^er` of fixed parity blocks admits effective classification over **all independent nonnegative exponents**. The concrete odd-gap family `P^a Q^b`, `P=(1,1,4,1,1,1,2)`, `Q=(2)`, has no positive cycle for any `a,b>=1`. | Written proof using the explicitly specialized Matveev theorem; seven checked Lean statements for the integer resource, Farey obstruction, and complete finite denominator cases; exact rational certificate. No finite list of block schemas is shown to cover all cycles. |
| Ordinary source mass | Under the pinned uniform predecessor-population input, **one escaping ordinary orbit** forces `sum_{n<=X} m(n) >= c1 X log X` and `sum_{n<=X} m(n)/n >= c2 (log X)^2` for sufficiently large `X`, with explicit constants and onset. | Independently reviewed conditional written proof. Two Lean statements check finite source accounting with the population premises explicit. The required sublogarithmic upper mean is unproved; cycles remain separate. |
| Complete source certificates | Every supplied certified odd unit root `q` and every `N>=q` admit a literal-tail predecessor in `N<p<16N/3`, using at most `C(N)` inverse letters in `{1,2,3,4}` and at most `4C(N)` shortcut clocks. | Eleven checked Lean statements, preserving the actual map, supplied tail, and first-crossing bound. This quantitatively strengthens the existing alphabet-four selector; the low-grade successful dispatcher remains open. |

The detailed proofs are [ARITHMETIC_CLOSURE.md](ARITHMETIC_CLOSURE.md),
[ORDINARY_MASS.md](ORDINARY_MASS.md), and
[GLOBAL_MERGERS.md](GLOBAL_MERGERS.md). The
[execution and review record](../../reports/2026-11-22-global-synthesis/README.md)
separates kernel checks, rational certificate checks, written deductions,
and imported analytic hypotheses.

The separate [closing refresh](LATE_REFRESH.md) reconciles four branches
that advanced during this execution. In particular, PR183 independently
published an overlapping generic independent-exponent classification
before our mathematical commit; the note records that attribution and the
distinct concrete two-parameter exclusion here. Its new source inspection
does not change the frozen proof inputs or add to the Lean audit count.
The late [tail-capture composition](TAIL_CAPTURE_BRIDGE.md) supplies
successful whole-interval rules at retained roots congruent to one modulo
81 or 729, under the specified complete-source certificate hypotheses.
It is a separately reviewed written proof with exact example replays.

## 1. The arithmetic enlargement is over the whole exponent lattice

The preceding PR185 theorem handled one-parameter families whose block
exponents were affine functions of a common parameter. Here the exponents
can vary independently and at unrelated rates.

For a block `Vi`, compute its length `Li`, odd count `si`, affine correction
`Ci`, and signed denominator `Di=2^Li-3^si`. Set

\[
K=\max_i(|D_i|+C_i),\qquad B=2\sum_i C_i,\qquad C=2^{32}.
\]

If a repeated block does not fix its incoming ordinary state `xi`, its
entire repetition clock `mi` satisfies

\[
2^{m_i}\mid D_i x_i-C_i,\qquad
2^{m_i}\le K(x_i+1).
\]

Actual forward height transport then pays for every block from the same
original state:

\[
2^L\le[K(x_0+1)]^{2^r-1}.
\]

A suitable cyclic rotation bounds `x0` through the whole cycle denominator.
The explicit two-logarithm estimate turns this into

\[
L\le H=\left[2^{r+1}(K+2B+2C)\right]^2.
\]

Zero defects are handled separately: they identify a cycle already realized
by one of the fixed blocks. Those cycles are replayed and classified, never
assumed trivial. This produces a terminating classification algorithm and
an effective semilinear description of the exponent vectors that realize
the resulting finite cycle list.

For the concrete `P^aQ^b` application, the proof goes further than a huge
theoretical cutoff. An exact rational interval around `log(3)/log(2)` excludes
every `a>=16`; an elementary inequality excludes `b>=a`. Exactly 105 pairs
remain. Twenty have a nonpositive cycle denominator, and the other 85 fail
divisibility by the full positive denominator. These 105 cases are checked
both by an independently composed Python certificate and by Lean's kernel
`decide`. The all-exponent coverage argument and the external logarithmic
theorem remain written mathematics.

The unbounded-description issue is retained explicitly. For a fixed
dictionary of blocks, increasingly long primitive cycles would require
increasingly long repeated-block descriptions. The present proof gives a
quantitative lower bound on that description length; it does not bound it
from above for all possible cycles.

## 2. One escape would force a macroscopic ordinary first moment

Let `m(n)` be the least actual future odd value of the odd unit `n`. The
population input is the precise source-qualified statement

\[
\#\{n\le X:n\text{ is an odd unit and reaches }a\}
\ge cX/a\qquad(X\ge C_0a),
\]

with absolute `c>0` and `C0>=1`, as pinned in the proof note. This input is
not a new formal theorem of this packet.

One injective orbit provides increasing suffix minima `tj` with
`tj+1 <= (t0+1)(3/2)^j`. At each minimum, choose a small off-orbit parent,
then the least ordinary root `rj` of its basin. These basins are disjoint,
their roots obey a common geometric upper bound, and every original source
in the chosen basin satisfies `m(n)>=3 rj/64`.

Consequently, if `R=(64/3)(t0+1)` and `X>=C0 R`,

\[
\frac1X\sum_{\substack{n\le X\\ n\text{ odd unit}}}m(n)
\ge\frac{3c}{64\log(3/2)}\log\frac{X}{C_0R},
\]

\[
\sum_{\substack{n\le X\\ n\text{ odd unit}}}\frac{m(n)}n
\ge\frac{3c}{128\log(3/2)}
\left(\log\frac{X}{C_0R}\right)^2.
\]

Only finitely many basins are used at each source cutoff. There is no
exchange of an infinite sum with a density limit. The same argument gives
fixed-truncation first-moment bounds with the truncation fixed before
`X` tends to infinity.

Thus even `liminf_X sum m(n)/(X log X)=0` would eliminate all escaping
orbits. We tried to obtain this from the newest ordinary harmonic flow.
Its weighted moments and collision contraction retain the source correctly,
but do not control the minimum or the extra moving height factor. The note
records this exact failure rather than claiming the upper estimate.

## 3. A bounded-cost selector with the complete tail retained

The six-row selector from PR177 already supplies a legal inverse letter
in `{1,2,3,4}` at every positive odd ternary unit. This pass makes its
cofinality quantitative. For a supplied complete certificate, the ordinary
first hitting time of one strictly increases along the selected inverse
chain, so its vertices are distinct. Pigeonhole gives the first crossing
above `N` within

\[
C(N)=\left\lfloor\frac{N+5}{6}\right\rfloor+
\left\lfloor\frac{N+1}{6}\right\rfloor
\]

inverse edges. The last exact edge gives `3p<16N`; concatenation preserves
the original literal tail.

The attempted next step was to replace a grade-four gap using the entire
alphabet-three inverse graph. Its six unit residue classes have outdegrees
`(1,2,1,1,0,1)`, so their mean is exactly one. The repeated-gap-two portions
have an exact valuation budget, but branching can restart that budget.
The proof also classifies an entire symbolic family: if
`q0=1+3^h u`, with `h>=1` and positive even `u=2 mod 3`, its whole
alphabet-three inverse graph is the single chain
`qj=1+4^j 3^(h-j)u`, ending at a nonunit leaf. The roots
`q=(4^(1+2*3^h)-1)/3` give a fully certified example at every such depth.
Thus universal cofinal alphabet-three replacement on every literal tail is
false. These supplied tails have large gaps, so the family leaves a
selective strategy on the residual alphabet-four language open. The
classification is written arithmetic; the finite graph examples remain
separate computational controls.

## 4. Repository-wide reassessment and current dependencies

The fresh inventory contains **145 PRs, 122 open PRs, 40 issues, and 159
branches**, with main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The [snapshot](../../reports/2026-11-22-global-synthesis/SOURCE_REFRESH.json)
records the metadata. This is a complete available metadata inventory and
a selective mathematical synthesis, not a line-by-line proof audit of every
branch.

| Current source | Contribution used in choosing the new attacks |
|---|---|
| Main research map, integrated source/extraction/transport packets and scoped errata | Preserve one ordinary source, actual legality, whole denominators, and the distinction between formal checks and analytic acceptance. |
| PR173 and PR176 | Forced shrinking-band entry, the faster polylogarithmic entrance route, inverse contact criterion, and the exact paid literal-cut envelope. These already establish substantial quantitative infrastructure. |
| PR177, PR180, PR183, PR184, PR185 | Complete-source rank, alphabet-four coverage, physical erasure and independent-clock mergers, blocked normal forms, and the unbounded literal carry language. These identify the remaining successful-selector requirement. |
| PR175, PR180, PR185 | Canonical potential moments, ordinary harmonicization, exact retained-source transport, and the positive energy carried by a hypothetical escape. These distinguish bounded reference energy from absorption. |
| PR182 | Ordinary Fourier cancellation and the Besicovitch regularity sufficient condition. The required regularity is not constructed by that condition. |
| PR185 and PR186 | Effective fixed-schema cycle arithmetic and the literature's exact theorem interfaces. These motivate the independent-exponent theorem and its exact tail certificate. |
| Previous PR178 packets | Source collision budget, physical tail barrier, ordinary-renewal construction, and Abel antichain bounds. These are retained with their original receipts. |

Every imported exploratory claim retains the exact head and file given in
the relevant proof note. None is promoted into the accepted main baseline.
This packet changes no existing claim registry, historical proof receipt,
workflow, or integration status.

## Reproduction

The [Lean build](lean/build.sh) requires Lean 4.34.1 and the existing pinned
Mathlib checkout `d13f23b723b8a846827a245b89c10fc7d3f11612`. It rebuilds
the one required frozen `ShellCover` import, all new modules, and the public
theorem audits. It installs no dependencies and makes no network requests.

The exact arithmetic checker is
`python -X utf8 -B research/global-synthesis-20261122/certificates/independent_pq_verify.py --self-test`.
The supplied-certificate selector and finite graph controls are reproduced by
`python -X utf8 -B research/global-synthesis-20261122/inverse_alphabet_selector.py --replay`.
The generic classification theorem is not accompanied by a search up to its
astronomical bound. Its concrete application uses the small certified
finite remainder described above.
