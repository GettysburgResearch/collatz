# Common-rank clock guards: supplied witnesses and padding

**Verdict: VERIFIED for the eight frozen template rows and their original
ordinary guards.** This is a scoped reconstruction of the clock semantics
needed by the new common-rank application, with a separate exact affine
table implementation. It is not a claim that the complete negative-template
splicing theorem has been formalized in Lean.

The common rank is

\[
P(n,d)=(n+1)(201/200)^d.
\]

Its actual well-foundedness and simultaneous induction are proved in
`CommonRank.lean`; the separate forcing lane reviews that proof. This note
addresses a different issue: whether the proposed recursive template call
really changes the **supplied ordinary clock** from `d` to `d+a`.

## Frozen input and exact replay

- PR168 head: `e4599b32e4b1a955ac9315d46782d4ad6a5db96c`.
- Source path: `research/closure-frontier-20261121/negative_template_compiler.py`.
- Source SHA-256: `16aab6efe1294a33c88f8b2fadae9d8060e68cc242eee18425aab7cfdcdd1745`.
- [Copied template inputs](common-rank-clock-inputs.json), SHA-256
  `86fd0b38b65c340e69d7a1e6a25643ef3da27e42432e3b4af14390cbc86ca842`.
- [Separate checker](check_common_rank_clocks.py).
- [Actual output](common-rank-clock-report.json), SHA-256
  `17d71896b4ea44e4d80685ff0075271f9276df2d25606c3f817051c481ded326`.

Both normal and optimized Python executions passed and emitted identical
bytes. The checker uses explicit failures, so optimization does not disable
its conditions. It checks 32 retained prefixes by exact constant/slope
arithmetic, not by sampling parameter values or searching for convergence.

## Why the original supplied clock is available

For each row, the checker reconstructs the least positive CRT parameter
`M0` and the progression increment. It then propagates an affine expression
`constant + slope*j`, `j>=0`, through every retained odd-step exponent.
At each step the constant is positive odd and the slope is even, proving
the same exact valuation over the whole progression.

All 32 retained endpoints have positive slopes and constant terms greater
than one. The smallest constant term is **208493**. Thus every retained
endpoint remains strictly above one for every allowed parameter.

The accelerated odd map fixes one. Consequently a supplied witness cannot
hit one before one of these forced prefixes ends, and its remaining tail
cannot be empty. The terminal padding allowed by the generic compiler is
therefore **unnecessary for these eight concrete rows**.

At endpoints related by `S=J^k(V)`, with `J(z)=4z+1`, the first remaining
odd-step exponent changes by `-2k`. In every row and on both arms the exact
integer check gives

\[
\sum\text{new prefix}-\sum\text{old prefix}-2k=a.
\]

Hence an old source witness of shortcut clock `d` produces a new source
witness of clock exactly `d+a`. The reverse compilation on the target arm
changes its returned clock by `-a`. These are total shortcut clocks, not
the final individual exponent or the number of odd inputs.

The checker also verifies the common-rank scale inequalities for all eight
rows, and the exact rational score guard for the expanding balanced example
`19483 -> 21091` at clock30. These numerical inequalities are separate from
the semantic prefix transport just described.

The ordinary value being scored must remain explicit. For a binary-source
goal it is `n=128M+1`, and the shifted-height guard is
`64c+3^b<2^a`. After conjugation to a psi-source goal it is instead
`n=81M+2=3m-1`, and the required guard is `27c+3^b<2^a`.
The checker verifies both guards for all eight rows. The equal seven-clock
source prefixes cancel in the composite conjugation; no claim that an
intermediate change of goal kind has zero cost is used.

## Limits that remain necessary

For a future template whose prescribed prefix might encounter one or leave
an empty tail, adding terminal loops changes the clock. A padded source
clock is `d+2j`, so a transported clock can be `d+2j+a`. Such padding cannot
be silently charged as zero: it increases `P`. That application must prove
the actual resulting strict score inequality, or first establish a no-padding
guard like the one above.

A common well-founded rank also does not supply an ordinary
least-counterexample floor. An unconditional `Basin(a)` goal is a different
semantic obligation from a closure query carrying a known source witness.
Even when `Basin(a)` is known, its existential witness clock has no automatic
bound that would make a certificate-bearing query score-small. Every such
transition requires its own sound implication and strict numerical guard.

The eight rows retain their original congruence, positivity and prefix
guards. No complete cover of all inputs, free conversion of goal kinds, or
new proof of `ResidualPsiClosure` follows from these checks.
