# Independent reconstruction review: positive actual-return charges

**Verdict: VERIFIED at the stated deduction boundaries, with inherited
source qualifications retained.** This is a separate agent's mathematical
reconstruction and bounded implementation comparison. It is not an external
review, a formal verification, a proof of the required closing estimate,
or a resolution of Collatz. No mathematical correction was required for
the frozen files below.

## Frozen files and source interfaces

| File | SHA-256 |
| --- | --- |
| `research/global-closure-20261120/transport.md` | `5b1559d09ae81107416b44e97fd8b93a7a60d0f334746e3b2c94ab314d6c9649` |
| `experiments/global_closure_transport.py` | `68e74e13aa3ebf7aaeef743dcbcd9a06216f349a4c65af8cf703a3eea20d3d83` |
| `reports/2026-11-20-global-closure/transport-report.json` | `e4a3a274584d5656980e093946e1a61f1dc27059d7947b53143572d81a84b779` |

The review read PR #152 at
`2391a9c1e4a7f77233b951d2eb6da92e76652e7c`,
`research/gemini-global-closure-20261120/ACTUAL_TRANSPORT.md`, AT2--AT3
(Git blob `20c8ba3b7c5858999f6a25db93c3118bc7fe9ff2`), and
`FIXED_SOURCE_DRIFT.md`
(Git blob `fef8f0ea429479f468ae34bd5d198ec47a7ca7a5`). The exact map,
rank, quarter-safe guard, return endpoint convention, and original input
agree with these sources. Their stated inherited moving-rank qualifications
are not enlarged by this review.

The interval theorem was read in PR #153 at
`eb04a5d79020cefa0ba46794095b5766c5ff66a4`,
`research/fixed-integer-descent/drift.md`, FID-DRIFT-001/002/005. The local
source SHA-256 matches the manuscript's pin:
`d73a93d8a803996bde7b15f33e307d28385c8ffe2f9b99f449dfea35140c3338`.
Its domain is a simple **forward ordinary shortcut path**, not a
predecessor basin. Its bounds apply to translated integer intervals;
the recursive envelope and its constants retain the source's scope.

## Claim-by-claim reconstruction

### GCT-001 — VERIFIED from the pinned additive return budget

The proof applies the pointwise inequality
`psi(Bu)<=psi(u)+log(6)` to the same original source at each return.
Since `psi>0`, reciprocation gives the required lower bound on its
occupation charge. Merging adds source weights and does not remove the
contribution of any never-absorbed original atom. The decreasing-integrand
comparison gives the displayed logarithmic lower bound with the correct
factor `1/log(6)`.

Fatou's lemma applies to a nonnegative countable source sum, so no finite
initial psi-moment is needed. The surviving mass limit follows by dominated
convergence of survival indicators against the summable original input.
Full support makes any one never-absorbed atom have positive mass.
Nontrivial cycles are included in this same argument; the proof does not
discard their repeated visits. The passage back to ordinary shortcut
orbits correctly uses total finite accelerations and the impossibility
of an infinite quarter-safe rank descent.

The upper bound `G_N=o(log N)` remains an unproved sufficient condition.
The manuscript does not treat `O(log N)` as enough, or claim equivalence
with the previous signed-drift target.

### GCT-002 — VERIFIED, including complete source tails

For sources above `M`, the fixed input has total mass at most `1/(M+1)`.
Each of its first `N` retained occupations has charge at most `1/psi_*`.
This proves the entire omitted-original-source bound, including any
subsequent mergers or changes of endpoint size. It is not an endpoint
truncation. With `M=N` the error is bounded, hence is `o(log N)`; the
triangular-array equivalence is therefore valid. The same argument proves
the stated more general cutoff condition.

### GCT-003 — VERIFIED as a separate deterministic control

The odd part `q` is fixed along every surviving doubling step, and its
finite chain length `L(q)=2^(q^3)` therefore gives absorption for every
individual ordinary source. The proper rank, additive gauge bound, and
translated-interval count are valid. At the chosen horizon `N=L(q)`, the
single original atom at `q` contributes at least the amount in (12).
The estimate `psi_0(q2^j)<3+log N` and the denominator bound `4q^8` have
the correct direction. The resulting lower bound diverges along these
horizons despite absorption of every source.

This is a control for the specified abstract interfaces and source
weights. The manuscript explicitly does not identify its doubling edges
as Collatz edges. It validly blocks the claimed *necessity* of the Green
condition from those interfaces alone; it does not disprove that condition
for the actual Collatz return.

### GCT-004 — VERIFIED with the source interval theorem

An individual nonperiodic `B` state is visited at most once. In an
eventually periodic shortcut orbit, the preperiod and one cycle traversal
form a finite simple shortcut prefix containing every distinct value ever
visited. Otherwise any finite selection of actual return endpoints is
contained in a sufficiently long simple shortcut prefix. This justifies
the interval theorem for return endpoints even though return lengths and
safe excursions depend on the actual history.

Deleting the periodic states of `B` is essential: a periodic endpoint
can have infinitely many visits. After that explicit deletion, Tonelli's
theorem sums the per-source bound without any assumption about the number
of predecessors or merging. The counting-function integral gives
`10s/(s-29/30)` and, at `s=1`, exactly `300`; the height-tail exponent
has the correct sign. For real cutoffs one may use the integer lower
endpoint `ceil(H_0)`, which is no larger than the manuscript's counting
upper bound.

The bounded Poisson corrector exists as its convergent nonnegative series,
and shifting that series proves the coboundary identity, including killed
and periodic endpoints. No procedure deciding the periodic set or computing
the infinite series is inferred. The original-source tail follows from
its uniform bound. The squaring control correctly separates finite
reciprocal-height charge from the much larger reciprocal-psi charge.

## Implementation review and executed evidence

The frozen default replay was regenerated with:

```sh
python -X utf8 -B experiments/global_closure_transport.py --compare reports/2026-11-20-global-closure/transport-report.json
```

It passed with 2,941 unsafe sources through 64 returns; 3,475 distinct
actual return edges; 9,117 physical acceleration words; 25,037 shortcut
edges; 122,729 translated-window checks; and 3,475 exact rational
reciprocal-height coboundaries. The maximum physical value was 4,076,810.
This repeats the reported bounded experiment; it does not extend its domain.

An independently written comparison is saved as
[`arithmetic-transport-independent.py`](arithmetic-transport-independent.py),
with its executed receipt in
[`arithmetic-transport-independent.json`](arithmetic-transport-independent.json).
It reconstructs acceleration by greedily replaying the physical parity word,
without using the author's affine endpoint or repetition-count formula.
It calculates the rank over the source-qualified modes plus additional
finite modes, reconstructs the unsafe return, and transports exact
`Fraction` weights from the original sources. Every merger preserves
those weights until killing.

The independent scope is every unsafe source through 512 and 32 returns:
183 original sources, 565 rank inputs, 562 physical accelerations,
211 actual return edges, and 1,548 accepted physical shortcut edges.
Exact mass conservation holds at all 32 horizons. At horizons
`1,2,4,8,16,32`, its exact-weight functional enclosures fit inside the
author's intervals; carrier counts and complete source-tail bounds agree.

For this numerical comparison, the author's logarithm interval routine is
reused **after a separate algebraic audit**, rather than claimed as an
independent reimplementation. The audit checked range reduction, positive
atanh terms, the remainder
`9/[4(2T+1)3^(2T+1)]`, sign reversal of interval endpoints for negative
binary exponents, monotone nested logarithms, reciprocal endpoint reversal,
and every outward integer rounding. The author's separate rational-series
checks are also part of the executed default replay.

The integer checker uses explicit `require` gates rather than removable
Python assertions. The finite window checker evaluates the one-pass
envelope from the source; the stronger recursive envelope in the written
theorem remains source-qualified, not newly exhaustively enumerated here.

## Remaining uncertainty

The review verifies these deductions and finite implementations at the
frozen bytes. It does not prove the reciprocal-psi upper estimate, exclude
any previously unexcluded nontrivial cycle, or replace the inherited
rank and interval source proofs with formal verification. The gap stated
in section 7 of the manuscript is still the global closing obligation.
