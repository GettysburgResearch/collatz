# Focused five-ray investigation

This packet studies the actual ordinary five-ray merger question
\(t\sim5t+1\), equivalent to full Collatz in the pinned PR #146 source. It does
**not** establish that universal merger, exclude divergent orbits, or resolve
all positive cycles.

| File | Established scope |
|---|---|
| [PAIRED_RETURNS.md](PAIRED_RETURNS.md) | All-time ternary target obstruction for synchronous returns; two exact descending six-step families; an expanding **first** nine-step return on every \(512v+287\), with no cross-arm meeting through clock 9; a third smaller-question rule obtained by reversing that expanding return; a terminating guard that explicitly permits unresolved outcomes. |
| [check_paired_returns.py](check_paired_returns.py) | Exact affine certificates and ordinary guard. Run without arguments for its bounded checks, or use `--start 410 --clock 9` to see a certified reduction with an unresolved terminal question. |
| [FINITE_CLOCK_BARRIER.md](FINITE_CLOCK_BARRIER.md) | An elementary interval where all \(N\) questions remain unanswered at the compression clock; a source-qualified natural-shell theorem showing that almost all pairs remain unanswered even at clocks approaching \((1+\tfrac12\log_2 3)\log_2 t\). |
| [check_finite_clock_barrier.py](check_finite_clock_barrier.py) | Exact bounded replays and arithmetic margins. Its enormous effective asymptotic threshold is proved symbolically, not enumerated. |
| [search_paired_returns.cpp](search_paired_returns.cpp) | Exploratory exhaustive enumeration through a supplied bit depth, at most 26. A run through 24 was performed. This search is not a universal return or convergence proof. |
| [paired_return_cones_24.tsv](paired_return_cones_24.tsv) | 178 selected finite return witnesses from that bounded run, with tab delimiters. Their image cones have union measure \(11842/59049\); this selected data is not a complete branch classification. |

The key new control is that an actual return does not by itself imply descent:
\[
 (512v+287,\,2560v+1436)
   \xrightarrow[6\text{ odd inputs each}]{9\text{ shortcut steps}}
 (729v+410,\,3645v+2051),\qquad v\ge0.
\]
There is no earlier synchronous five-ray return and no cross-arm meeting at
any two clocks at most 9. Conversely, reversing this certificate legitimately
reduces the question at \(729v+410\) to the smaller one at \(512v+287\).

The target obstruction is also all-time: every nontrivial synchronous return
lands at a parameter congruent to 2 modulo three. Every nontrivial fixed-word
affine return valid at two parameters is automatically synchronous and balanced.
This blocks uniform inverse-return branching from targets in the other two
ternary classes. It does not prove that arbitrary forward adaptive coverage is
impossible or that any positive pair never meets.

The conditional final section of `PAIRED_RETURNS.md` reconstructs what would
follow from proving five-ray mergers for every parameter prime to three.
It displays the additional universal equality that remains missing. Its small
valuation model refutes an inference using only two scaling identities; it is
not a counterexample model of full ordinary Collatz dynamics.

## Sources and checks

The source head is PR #146,
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`, especially
`research/upper-bit-mergers/AFFINE_RAYS.md`, `EVENTUAL_FIVE_RAY.md`, and
`THREE_RAY.md`. PR #149 at `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
`research/forward-inverse-defect/CLOSURE_BOUNDARY.md`, was consulted for its
ordinary-versus-selected-inverse scope boundary. The all-time return results
require only elementary arithmetic and the definitions.

The finite-clock shell theorem additionally imports Baker--Wüstholz. Its
constant was checked in the primary-author publisher excerpt linked in that
proof. It is not reproduced from an unsourced numeric approximation.

Run the two exact checkers with ordinary Python. Both reject `python -O`,
because optimized execution would disable their assertions. The C++ exploration
is separate and is not needed to replay the mathematical certificates.

The exploratory run compiled the source with `g++ -O3 -std=c++17` and invoked
the resulting executable with argument `24`. It was run through Python
`subprocess.run`, capturing both output streams. Standard output consists of
rows `new h source target q residue inverse_expands`; standard error records
counts, and the current version also records growing-return examples.
The TSV is selected data, not raw standard output. Its extraction sorted the
reported discovery rows by `(q, residue, h)` and kept a row only if no previously
kept `(j, residue mod 3^j)`, with `1 <= j <= q`, already covered its cone. This
gave 178 rows. Every saved row is a finite affine witness that can be replayed
individually; no completeness claim about all return branches is needed or made.

The remaining closure obligation concerns **every positive ordinary input**:
an actual merger for each retained five-ray question, or a universally available
strict reduction to a smaller such question. The source's sublinear count of
distinct labels and the component's arbitrarily long consecutive runs do not
establish that obligation; the finite-clock packet demonstrates the missing
weight quantitatively on ordinary examples.
