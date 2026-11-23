# A complete-certificate attack with arbitrary target phases

**Status: the universal Collatz closure remains OPEN.** The new positive results
are a complete rule for every power-of-two source in the common induction, and
a Lean compiler for arbitrary finite, asynchronous source and target words.
Both preserve the entire supplied convergence certificate and decrease the
same well-founded multiset used by PR177. A successful choice of words for
every remaining nonterminal query has not been proved.

The map is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Write `Basin(n)` for finite ordinary convergence to one and
\(\psi(n)=2n-1\). All inputs and all constructed endpoints in the mathematical
theorems are ordinary natural numbers. No probability, 2-adic realization,
finite search cutoff, or conjectural axiom is an input to the compiler.

## 1. What the source comparison selected

The relevant complete-witness sources were read at these exact heads:

| Source | Head | Actual files and interface inspected |
|---|---|---|
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | `research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md` and `WHOLE_INTERVAL_SYNCHRONIZATION.md`: finite terminal deadline and arbitrary block synchronization, with a remaining pointwise terminal comparison. |
| PR147 | `b74b2d466f58844a742a6ed6bcdf06844269f361` | `research/robust-inverse-credit/PROOF.md`, `README.md`, and `MERGER_AND_HEIGHT.md`: the inverse compiler consumes prescribed ternary factors; it does not provide a forward source rank or a prescribed component merger. |
| PR164 | `9582df78eb4d768eb748d3cf367ba97582308a52` | `research/witness-global-closure-20261121/DIRECT_R_WORDS.md`, `README.md`, and `POSITIVE_RENEWAL.md`: exact full-tail rewrites, least-failure restrictions, and still-unbounded Mersenne terminal families. |
| PR174 | `c92cd473de3b85ceb945702a726d2eb7350a6af8` | `research/psi-closure-20261121/routes/layers/Layers.lean`, `routes/pow3/Pow3Families.lean`, and the closure foundation: arbitrary-exponent normalization already exposes the powers-of-three terminal problem. |
| PR177 | `00a611094043afeb256d6532b477c0709e8ed270` | `research/lean-exact-witness-global-20261121/lean/Collatz/{GapMultiset,GapComparison,GapHandoffs,LowGapToPsi,UnboundedGapReset}.lean` and `UNBOUNDED_GAP_REWRITES.md`: actual common rank, full-tail splices, and incomplete arithmetic guards. |
| PR181 | `5f03d809b4495802971211ef13ff905f741d700d` | `research/lean-global-target-20261121/closure/README.md` and `UNPAID_EXIT.md`: repeated expanding returns have a finite charge budget, but exhausting it does not force a paying exit. |

These are interfaces from actual scientific files, not deductions from PR
titles. The only imported mathematical dependencies of `CollatzGlobalClosure/AsynchronousReset.lean` are
the eight unchanged PR177 Lean files listed in the provenance manifest.

The synthesis is to permit independent target clocks and arbitrary actual
parent-target phases while retaining one complete source certificate and one
multiset order. It avoids treating a ratio-five paired return as a psi return.
It also avoids treating inverse padding as a rank decrease: prepending a word
retains every old gap multiplicity, and does not change the endpoint on which
an interior reset guard depends. An actual deletion or reduction of an old
grade is necessary.

## 2. Every terminal power-of-two source now has a valid rule

`CollatzGlobalClosure/TerminalReset.lean` handles **every** parent source \(2^e\), including
arbitrary supplied terminal padding `Certificate(1,tail)`.

For \(e\ge4\), choose the powered child source

\[
m=3\,2^{e-1}.
\]

The explicit ordinary odd path \(3\to5\to1\) has gap word \((1,4)\).
Consequently the complete child certificate has initial even run \(e-1\)
and the exact odd word \((1,4)\mathbin{\Vert}\mathrm{tail}\). Its grades are

\[
\{2e-1,2,8\}\uplus 2\,\mathrm{tail},
\]

whereas the parent grades are \(\{2e+1\}\uplus2\,\mathrm{tail}\).
Every newly inserted grade is strictly below \(2e+1\), even at \(e=4\).
The parent target takes one actual odd shortcut step:

\[
T(2^{e+1}-1)=3\,2^e-1=2m-1.
\]

Thus the lower-ranked child psi query reconstructs the parent query. The
child source is larger by a factor \(3/2\), and its supplied source clock is
four steps longer; the common multiset still decreases. The four small
exponents \(e=0,1,2,3\) close by literal paths from \(1,3,7,15\) of ordinary
lengths \(0,5,11,12\), respectively.

The theorem `terminal_case` is the complete terminal-source **induction
step**. It calls the psi conclusion on a smaller complete certificate. It
does not independently prove convergence of all Mersenne numbers, because
the nonterminal child cases of the simultaneous dispatcher remain open.
There is no remaining unbounded terminal power-of-two family to exclude in
that dispatcher.

The general theorem `power_transfer` permits any \(0<j\le e\) for which a
complete certificate of \(3^j\), with all gaps at most \(e\), is supplied.
It transfers to powered child \(3^j2^{e-j}\), retaining all terminal padding.
The all-exponent terminal rule above needs only the fixed certificate of
three; it assumes no theorem about arbitrary powers of three.

## 3. The arbitrary three-word compiler

For a positive-gap word \(W\), let \(|W|\) be its length, \(B(W)\) its sum, and
\(C(W)\) its standard affine correction. A legal path from \(n\) to \(z\)
satisfies

\[
3^{|W|}n+C(W)=2^{B(W)}z.
\]

PR177's `word_path_of_identity` proves the converse with every intermediate
integer guard. The new `word_path_identity` proves the forward direction for
the literal word-path representation.

Let the parent source be \(S=2^e q\), with \(e>0\), and retain a supplied
complete odd certificate `Certificate(q,tail)`. Choose any finite words:

- \(W\): a proposed child-source path from \(m\) to the same \(q\);
- \(V\): a proposed child-target path from \(2m-1\) to an endpoint \(z\);
- \(P\): an **actual parent-target path** from \(2S-1\) to the same \(z\).

Put

\[
p=|W|,\quad d=|P|,\quad B=B(W),\quad K=B(V),\quad F=B(P).
\]

The exact compatibility conditions are

\[
|V|=p+d,\qquad K+e=B+F,
\tag{A1}
\]

\[
\begin{aligned}
2^F C(V)+2^K3^d
={}&2^F\bigl(3^{p+d}+2\,3^d C(W)\bigr)+2^K C(P),
\end{aligned}
\tag{A2}
\]

and every gap in \(W\) is at most \(e\). Require \(m>0\) and the exact source
identity

\[
3^p m+C(W)=2^B q.
\tag{A3}
\]

**Lean theorem `three_word_whole_witness`.** Under A1--A3 and the supplied
actual parent path, the compiler produces

\[
\operatorname{Certificate}(m,W\mathbin{\Vert}\mathrm{tail}),
\qquad
\operatorname{Basin}(2m-1)\iff\operatorname{Basin}(2S-1),
\tag{A4}
\]

and a strict decrease in the common complete-certificate rank.

That rank is the multiset

\[
\Gamma(e;\mathrm{tail})=
\{2e+1\}\uplus\{2a:a\in\mathrm{tail}\}
\quad(e>0).
\]

The child replaces the single grade \(2e+1\) by the finite multiset
\(\{2a:a\in W\}\), all of whose entries are at most \(2e\). The entire
supplied tail cancels literally. The inserted length, child integer, and
both target clocks have no fixed upper bound.

### Why the target word is ordinary

Multiply the child target affine expression by \(2^F\), add \(2^K3^d\),
and apply A2. Use A3 and \(2^F2^B=2^K2^e\), which follows from A1. The result
is \(2^K\) times the parent target affine expression plus \(2^K3^d\).
The actual parent path supplies its endpoint equation. Cancel the equal
addends and the positive factor \(2^F\); this proves

\[
3^{|V|}(2m-1)+C(V)=2^K z.
\]

`word_path_of_identity` then forces every child-target division. The theorem
does not assume that a formal affine endpoint is already an ordinary path.

### An explicit path beyond the initial odd run

The compiler includes the checked choice

\[
e=1,\qquad W=(),\qquad V=(2,2),\qquad P=(1,4).
\]

For every \(t\ge0\), put \(q=8t+1\). The child target \(16t+1\) and parent
target \(32t+3\) merge at \(9t+1\), after four and five ordinary steps,
respectively. Given any complete certificate for \(q\), the child retains it
unchanged and deletes the parent's initial even grade. The parent phase goes
past its initial odd run. This is a concrete use of the enlarged interface;
the familiar local descent itself is not presented as a new global theorem.

## 4. The first-odd-run specialization and its full boundary

The specialization `whole_witness_reset` permits any \(0\le j\le e+1\) and
uses the parent target's actual initial odd run to

\[
3^j2^{e+1-j}q-1.
\]

Its simpler exact word conditions are

\[
|V|=|W|+j,\quad B(V)+e=B(W)+j,
\quad C(V)+2^{B(V)}=2\,3^j C(W)+3^{|W|+j}.
\tag{A5}
\]

One explicitly checked unbounded-exponent family is

\[
W=(1,2,7,e),\quad V=(6,1,1,2,1),\quad e\ge7,
\]

with guard

\[
81m+1093=1024S.
\]

It retains any supplied odd tail of \(S=2^e q\). Its child source can be
larger, while the complete witness decreases. This example instantiates
the universal compiler; its ternary cell is not a full selector.

There is also a kernel-checked all-word boundary, rather than a failed finite
probe. Every complete certificate whose gaps are at most three represents
one: backward induction from one permits only the gap-two self-loop. Hence
a parent source \(S=8\), with \(e=3,q=1\), could only produce child source
\(m=1\) in A5. The child target one remains in \(\{1,2\}\), whereas the parent
target fifteen has the first-run endpoints

\[
15,\ 23,\ 35,\ 53,\ 80.
\]

`no_first_run_reset_for_eight` proves that no pair of words of **any finite
length** satisfies this specialization for that parent. Fifteen does
converge; this is a boundary of the first-run, odd-child grammar. The
three-word compiler removes the restriction to that parent phase, and
`CollatzGlobalClosure/TerminalReset.lean` supplies the complete terminal-source case using a
powered child when needed. The remaining dispatcher coverage is still open.

## 5. What the exact search says

`search/async_reset_search.cpp` enumerates every odd binary source cylinder through ordinary
source clock 29, for the specialization \(j=1\). It permits independent target
clocks \(1\le k\le h\) and requires the source prefix to stop immediately
after an odd input. If its source count/correction are \(p,C\) and target
count/correction are \(p+1,D\), the exact condition is

\[
D+2^k=6C+3^{p+1}.
\]

Set \(\delta=h-k+1\). The parent guard is

\[
S\equiv C2^{-(k-1)}\pmod{3^p}.
\]

After appending the parent's remaining halvings, the new final source gap is
\(e-\delta+1\). All earlier gaps and \(\delta\) must be at most \(e\).

The run at budget 22 found 429,188 compatible finite cylinders and retained
5,828 nonnested ternary cells. Their exact relative measure among ternary
units is

\[
\frac{14463505}{129140163}=0.111998503517453\ldots.
\]

Every retained row actually requires prior gap at most 16 and \(\delta\le4\).
The largest positive-child threshold is
\(2020210285/67108864<31\). Thus all these local rows are usable at every
parent even valuation \(e\ge16\), whenever their guard holds.

The independent Python replay reconstructs all correction formulas, both
ordinary paths, the exact source splice, disjointness, and two positive
ordinary lifts per row. Both normal and optimized Python checked 11,656
lifts at \(e=16\) with identical results. These checks are finite evidence
about the generated rows; the unbounded compiler is the Lean theorem.
The source-clock search does not cover arbitrary parent-target phases.

## 6. The first unproved step in the full attempt

The missing claim is an actual complete dispatcher: for **every** activated
source/target comparison and every supplied complete source certificate,
produce a proved terminal case or a sound comparison with a strictly smaller
complete certificate. The terminal power-of-two case is now fully covered.
The three-word compiler supplies a much broader class of nonterminal rules,
but does not choose such a rule for every remaining input.

In the even-source psi branch, the specific open task is to choose legal
\(P,W,V,m,z\) satisfying A1--A3 and the gap bound, or provide another valid
terminal/recursive rule. Guard coverage, parent-phase legality, and child
activation all remain necessary. For the full mixed induction, the remaining
odd-source and alternate-shape cases must also be covered in that same rank.
The finite 11.2% guard union supplies no inference about the remaining fixed
ordinary parents. Inverse-tree density and arbitrary padding do not supply
the missing selector.

## 7. Lean and reproduction

The new files are `CollatzGlobalClosure/AsynchronousReset.lean` and `CollatzGlobalClosure/TerminalReset.lean`. Their imports
are eight byte-preserved core Lean files from PR177; no Mathlib is needed. Lean 4.34.1 with
`-DwarningAsError=true` checks the compiler, exact specializations, complete
rank decrease, and the all-word first-run boundary. The audited declarations
use only standard `propext`, `Classical.choice`, and `Quot.sound`, with some
smaller subsets. No `sorry`, `native_decide`, or conjectural axiom is used.

`build_wide.py` performs a fresh build of this continuation and writes exact source hashes,
commands, exit codes, and the axiom output in the chosen receipt:

```sh
python -B build_wide.py --lean /path/to/lean-4.34.1/bin/lean \
  --output /fresh/build --receipt /fresh/build.json
```

It compiles the eight dependencies in this order before `CollatzGlobalClosure/AsynchronousReset.lean`
and `CollatzGlobalClosure/TerminalReset.lean`:

```text
ReverseBasin146 Closure Witness DirectedInduction WitnessEnergy
SourceWitness GapMultiset UnboundedGapReset
```

To regenerate and replay the finite search output:

```sh
g++ -O3 -std=c++17 search/async_reset_search.cpp -o /tmp/search_async
/tmp/search_async 29 22 > /tmp/async_29.csv
python -B search/replay_async_reset.py /tmp/async_29.csv 16
python -O -B search/replay_async_reset.py /tmp/async_29.csv 16
```

The fresh build receipt and source hashes are process evidence. Repository
integrity checking is separate and does not prove the global closure.
