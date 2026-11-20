# Source boundary for component-run placement

**Review scope:** exact hypotheses and the arithmetic compositions used by
COMPONENT_RUN_PLACEMENT.md. No complete independent verification of the
analytic renewal inputs is asserted.

## Pinned inputs

| Input | Pin | Claim used |
|---|---|---|
| Polynomial synchronization | PR146, 561d48a4d3a793a59b1cdf0406062ae1a6d47515, research/upper-bit-mergers/AFFINE_RAYS.md | A binary cylinder synchronizes a length-M interval at one common clock and odd count, with clock polynomial in M. |
| Pair compiler | Same head, research/upper-bit-mergers/PREFIX_COMPRESSION.md | Previously established ties survive further binary refinements. |
| Fixed-target routing | Paper48 v2, Theorem 8, equations (80)–(83) | The supplied ordinary unit can be routed into any unit ternary class with total valuation linear in precision. |
| First landing, inspected but not required | PR145, dd245a712f985909f541590e3f6c179b7ba011e4, research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md | Counts and physical windows for prescribed source cylinders. |

The [Paper48 primary page](https://rstation.ai/problems/collatz/papers/48)
identified itself as v2 when read. Its /v2 address failed retrieval.
The needed routing statement has effective but uncomputed constants,
and its proof imports Lemma 7 and earlier analytic estimates. The
bounded sample routes below do not verify that theorem.

## Synchronization quantifiers

The interval construction first reduces the number of distinct affine
profiles to \(O(\log M)\) in \(O(\log M)\) exposed binary digits.
At each reduction, the next free parameter bits are sampled uniformly.
Every arm has an odd coefficient in that parameter, which makes its
parity word uniform. A union bound controls the inherited error, and
a fractional moment controls the newly created affine remainders.
No independence between different arms is assumed.

The profile-count recurrence has the form

\[
K'\le C\left[(h+j+1)+(h+j+1)^{1/3}K^{2/3}\right].
\]

The source schedules \(j_l\) proportional to
\((3/4)^l\log M+\log\log M\). The cumulative bit cost is \(O(\log M)\);
the exponent \(2/3<3/4\) closes its profile-count induction. Merging
the remaining \(O(\log M)\) representatives increases the bit count
by a fixed factor per representative, yielding a polynomial final
clock. Every prior affine identity persists on the refined cell.

All slopes of an interval of translates are one. Equality of endpoint
slopes therefore forces equal clocks and equal odd counts, as required
by the composition lemma. The finite checker independently verifies
these identities for its four small templates by coefficient induction
for every lift. It does not instantiate the source's unspecified
polynomial constants.

## Why the first-landing result would also apply

The first-landing statement allows any fixed positive odd ternary-unit
target \(b\le M_0\), not only the target one. With a prescribed forward
valuation word of total \(A\), and a ternary source class of depth \(k\),
its wide-window hypothesis is

\[
X\ge C M_0\exp(C(A+k+1)).
\]

Its lower count is \(c(X/M_0)2^{-A}3^{-k}\), with sources in
\([X/4,X]\). Setting \(M_0=b\) is legitimate even for an anchor in a
hypothetical second component.

An arbitrary odd binary class modulo \(2^h\) is handled by following
the valuations forced by those bits until the first unresolved
valuation, then choosing its least possible value. This fixes at
most one additional source bit and gives a full valuation cylinder
of total at most \(h\) inside the chosen class. The measure loss is
at most a factor two. It does not replace a prescribed class by an
unrelated class. If an interval template starts in an even class,
one may condition on its odd neighbor and translate the resulting
start back by one.

The proof's bridge length is comparable to \(\log(X/M_0)\).
Writing \(J_w=3^L2^{-A}\), the bridge is chosen near the scale
\(J_wX\). The terminal congruence is imposed at precision \(k+L\);
the stated lower bound on \(X/M_0\) leaves that precision within
the available linear digit budget. Multiplying the bridge count
by the source-word factor gives exactly \(2^{-A}3^{-k}\).

The bridge retains a bounded real offset. A last predecessor \(s\)
of \(b\), of size comparable to \(M_0\), makes every earlier inverse
state exceed \(M_0\): every partial offset is bounded by the whole
offset, and its multiplier is bounded by three times that offset.
Thus the first low label really is \(b\). Deterministic recovery of
the valuations, and different first-landing times, prevent duplicate
counting across words and lengths.

This reconstruction checks the arithmetic downstream of the imported
fixed-total bridge floor. It does not independently establish that
floor or its analytic prerequisites.

## Why no mesoscopic claim is used in the new theorem

The shrinking-window version needs an additional rotation estimate
for \(\log_2 3\), with a stated width restriction of order
\((\log(X/M_0))^{-1/8.234}\). The later threshold-padding argument
removes the auxiliary condition \(M_0w\ge C\), but it does not
remove that physical width restriction.

Such windows remain far wider than a power of \(\log X\).
They therefore do not contradict the new lower bound for gaps
and cannot supply its missing opposing upper bound. The final
component-run theorem uses only existence of fixed-target routing
and an elementary height padding, so it imports none of these
counting or rotation estimates.

## Exact replay

Run:

From the repository root:

    python -B research/ordinary-merger-selection/verify_run_placement.py --output /tmp/collatz-run-placement-report.json

The checker verifies 14 all-lift affine identities, then constructs
16 ordinary blocks of lengths 2–5 reaching the supplied targets
1, 5, 7 and 31. All 56 starts replay to their targets at the claimed
common clocks. The actual capped searches examine 9,682 states in
total. Three altered-data controls are rejected.

The value 120 in that replay is a chosen padding/search budget for
these examples. It is not a computed value of the universal routing
constant. The examples deliberately include large ordinary sources,
so that positivity of the affine lift and the fixed-target quantifier
are exercised directly. Their eventual convergence is witnessed by
the printed finite paths.
