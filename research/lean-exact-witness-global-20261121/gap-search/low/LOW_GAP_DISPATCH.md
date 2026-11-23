# Exact low-gap dispatcher checkpoint

Status: **partial conditional dispatcher; global closure unresolved**.
This uses the accelerated exponent gaps of the supplied source witness. It is
distinct from energy based on ordinary trajectory values.

## Source-word rank

Let an ordinary affine source prefix meet its child source prefix at their
common frontier, whose slope is odd. Group the ordinary forward moves into
partial accelerated gaps. If these words are

\[
A=(a_1,\ldots,a_k),\qquad B=(b_1,\ldots,b_l),
\]

and the actual frontier value has two-adic valuation \(\delta\), the complete
source words to its odd part are

\[
(a_1,\ldots,a_{k-1},a_k+\delta),\qquad
(b_1,\ldots,b_{l-1},b_l+\delta).
\]

An empty child prefix instead means that only the shared suffix remains after
normalizing its starting value. No last child gap is then inserted.

The generator cancels equal gap multiplicities and requires the largest
remaining differing gap to have greater multiplicity on the parent side, for
every \(\delta\ge0\). Once both variable final gaps exceed all fixed gaps, their
relative order is permanent; all earlier integer breakpoints are checked.

The separate replay uses the natural energy \(\sum C^a\). Its difference is
exactly

\[
\bigl(C^{a_k}-C^{b_l}\bigr)C^\delta
+\sum_{i<k}C^{a_i}-\sum_{j<l}C^{b_j}.
\]

For an empty child word, omit every child term. Nonnegative coefficient and
strictly positive value at \(\delta=0\) prove positivity for all \(\delta\ge0\).
The unchanged suffix cancels, so this handles any supplied witness, including
terminal padding. The affine prefixes have positive slopes and intercepts;
for parameter at least 1 no prefix value can be 1. Parameter 0 is listed as a
finite entrance exception and is not silently discharged.

All accepted replacements have at most 6 inserted gaps, so \(C=7\) suffices.
They also work with \(C=15\), the common base for the separately generated
high-gap catalogue with at most 14 inserted gaps. No comparison of the source
values or witness lengths is required.

## Finite search bound

Every ordinary affine component has a unique odd-slope frontier. An inverse
accelerated step with gap \(a\) sends \(x\) to \((2^a x-1)/3\), so it consumes
one factor 3 of the affine slope. The number of inverse odd steps is therefore
bounded by the initial slope's three-adic valuation.

At shared valuation 0, strict multiset decrease forces every inserted gap to be
at most the largest removed partial gap. These two bounds give a finite inverse
tree without a search depth cutoff. If a partial inserted word already fails
the multiset test, prepending further letters cannot improve it. The generator
keeps exact ordinary mergers as unconditional leaves.

This scope concerns a fixed whole affine cell, one F3/R3 query, common-frontier
source-prefix replacement and the displayed multiset order. It does not cover
arbitrary certificate transformations.

## Two universal source-word transitions

For an R3 obligation with known source \(3n\), a source word beginning
\((3,1,W)\) yields a child R3 obligation at

\[
n'=(3n+1)/2
\]

with known-source word \((3,W)\). Indeed, if
\(t=(9n+1)/8\), then \(3n'=4t+1\). The map \(J(t)=4t+1\) adds 2 to the
first source gap of \(t\), turning its initial 1 into 3. The parent desired
target takes one ordinary exponent 1 step to \(n'\). This deletes a gap 1 from
the known-source multiset, even when \(n'>n\). The child is generally outside
the deep-R3 domain, so its obligation must remain active in the dispatcher.

A source prefix \((3,4,W)\) instead reduces to F3 at the source tail \(u\).
The parent desired target takes the exact prefix \((1,1,1,2)\) to
\(J(3u)\). Thus F3 at \(u\), supplied with the untouched source word \(W\),
provides the target witness after a J lift and prefix insertion. Both removed
gaps disappear from the child source rank. This is a conditional transition,
not a proof that all F3 obligations hold.

For positive odd source multiples of 27, the earlier exact regular languages
\((2^k,4,b,W)\) and \((2^k,3,1^l,2,b,W)\) are proved in
[DIRECT_R_WORDS.md, DRW-004, equations (7)–(8)](https://github.com/GettysburgResearch/collatz/blob/b1503b7079c4ee549efccec6bbc77dbddfafed93/research/witness-global-closure-20261121/DIRECT_R_WORDS.md),
at commit `b1503b7079c4ee549efccec6bbc77dbddfafed93`. Here the superscripts
mean repeated letters. These are background results, are not used by the
87-row replay below, and do not cover all low-gap words.

## Replayed fixed-modulus result

Run:

```bash
python3 source_gap_frontier.py --M 288 --out /tmp/collatz-gap-frontier288.json
python3 -O source_gap_frontier.py --M 288 --out /tmp/collatz-gap-frontier288-optimized.json
```

The script is self-contained and uses only the Python standard library.
Both commands produce identical mathematical output and identical JSON bytes.

All 288 odd F3/R3 states were considered. The finite tree census examined 1,553
nodes and accepted 87 certificates: 18 ordinary mergers and 69 conditional
gap-energy replacements. There are 71 initially represented states. Dependency
pruning removes 43 and then 10, leaving 18 ordinary-merger states.

For the 16 deep-R3 cells, the first-source-gap coverage is:

| First source gap | Cells | Initially represented | Dependency-closed |
|---|---:|---:|---:|
| 1 | 8 | 1 | 0 |
| 2 | 4 | 0 | 0 |
| 3 | 2 | 1 | 0 |
| 4 | 1 | 1 | 1 |
| At least 5 | 1 | 0 | 0 |

For example, the cell \(n=288t+9\) remains uncovered by this fixed grammar.
Its known source \(3n\) has partial frontier word \((1,2,1,1)\). This is a
remaining dispatcher state, not a counterexample to the Collatz statement or
to a broader source-word transformation.

No modulus or depth escalation followed this checkpoint. A complete low-letter
state program and a complete high-letter cover remain unproved.
