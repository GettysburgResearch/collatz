# Mixed descent: the exact loop and a guarded escape

## The full-proof idea tested

A balanced five return can increase its ordinary source while shortening
a supplied source certificate. Its inverse can decrease ordinary size while
lengthening that certificate. It was tempting to alternate these two moves,
normalizing after each inverse step, and prove termination by a richer rank.
The exact normalizer allows this proposal to be tested on all words.

Write `R(n,t)` for a common-clock return from `(n,5n)` to `(q,5q)` with
equal odd-input counts. Let `L(n,d)` be the last such return in clocks
`0,...,d`, and define the finite certificate normalization

\[
\mathcal N(n,d)=\bigl(T^{L(n,d)}(n),\ d-L(n,d)\bigr).
\]

A finite residual `(q,d)` has no positive balanced return through clock
`d`. If `T^d(q)=1` is supplied, it is also a residual source certificate.
The no-return predicate itself does not assume that hit certificate.

## RT1. Suffix cancellation

If `R(n,s)` holds, then for every `t>=0`,

\[
R(n,s+t)\quad\Longleftrightarrow\quad R(T^s(n),t).
\]

The ordinary endpoint equality follows by composition of finite iterates.
Odd-input counts add under the same composition, and the equal prefix
counts cancel. This is an exact equivalence, not merely concatenation
closure or a finite experimental observation.

Lean: `balanced_five_suffix_iff` in
[`Retraction.lean`](lean/CollatzGlobal/Retraction.lean).

## RT2. Every balanced inverse extension retracts exactly

Suppose `R(n,s)`, put `q=T^s(n)`, and assume `(q,d)` is a finite residual.
Then

\[
\boxed{L(n,s+d)=s,\qquad \mathcal N(n,s+d)=(q,d).}
\]

The first equality uses RT1: a later return at `s+t`, with `0<t<=d`,
would give a forbidden residual return. The incoming word already gives a
return at `s`, so it is exactly the last one. There is no restriction on
the size of `n`, the length `s`, or any earlier returns.

In particular, selecting a smaller inverse ancestor of a finite residual
and applying complete last-return normalization sends the certificate
back to precisely the original residual. The composite does not expose
a new residual obligation.

Lean: `lastReturn_of_residual_endpoint` and
`normalize_inverse_extension`.

## RT3. The scope of the rank obstruction

For a rank depending on the ordinary source and remaining clock, the two
operations above form a directed two-cycle. **No rank valued in any
well-founded relation can strictly decrease on both of those operations.**
This includes ordinal and lexicographic ranks, not just a fixed linear
combination of size and clock.

Lean proves this at arbitrary universe and relation through
`wellFounded_no_two_cycle` and `no_wellFounded_rank_both_ways`.

The state qualification is essential. This does not exclude a proof
system carrying additional history, phase, or auxiliary obligations; a
system that permits one operation to increase rank; or a selector that
rejects one of the two directions. It does not exclude asymmetric witness
rewrites that change the return geometry while preserving the required
target implication.

The [separate reconstruction review](../../reports/2026-11-21-lean-global/RETRACTION_REVIEW.md)
pins the exact Lean source and checks these boundaries.

## A positive guarded synthesis

The [common-rank construction](COMMON_RANK.md) takes the last option
seriously. Its score on a convergent source with supplied clock is

\[
P(n,d)=(n+1)(201/200)^d.
\]

Lean proves this order well-founded on all natural source/clock pairs.
A forward return consuming `t` clocks is admitted only when
`(q+1)200^t<(n+1)201^t`. The actual increasing-source return
`19483 -> 21091` in thirty clocks passes. Its inverse fails the guard,
so the retraction cycle is not admitted.

More significantly, all eight frozen negative-reference templates also
decrease this same score while adding their exact positive number of
source clocks. Fixed ordinary prefixes conjugate those templates into
the psi goal type, where guarded psi returns and the templates can be
interleaved. This avoids conflating a five goal with a binary reverse
goal, and avoids treating padding or a change of goal kind as free.

The result is a common termination argument for the admitted, sound
moves. **A rule selecting a successful move or a complete target
certificate on every remaining psi residual is still missing.** The
[coverage attempt](COVERAGE_ATTEMPT.md) examines that concrete obligation.

None of these conclusions uses a hypothetical GRH theorem. The proofs
do not turn a probability-one parity statement into an ordinary-input
statement, and do not assume that a terminating partial compiler succeeds
on every input.
