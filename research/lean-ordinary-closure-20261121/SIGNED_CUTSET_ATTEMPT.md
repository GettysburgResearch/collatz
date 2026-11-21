# Final global closing attempt: actual-support first-entry congestion

**Outcome:** no global closure or finite-energy bound was proved. The
following conditional argument identifies the exact unsupported
inference in this attempted use of first-defect cutsets.

Write `C` for the ordinary basin of one,
`Y(j)=64j+1`, and `X(j)=128j+1`. Suppose `j` is an actual failed directed
comparison:

\[
Y(j)\notin C,\qquad X(j)\in C.
\]

The argument also applies if `j` belongs to CI4's retained set. It uses
the real basin indicator, not a freely prescribed array of charges.

Choose a positive ternary unit `q` in the ordinary component of `Y(j)`.
Such a unit exists: remove powers of two and, if necessary, take the next
ordinary step from an odd multiple of three. Ordinary edges in either
direction preserve the basin label. Thus `q` and the whole ordinary
connection from `q` to `Y(j)` are outside `C`.

The newly proved predecessor logarithmic-density theorem gives a
constant `c_q>0` and a cutoff beyond which

\[
\sum_{\substack{n\le H\\\exists t,\ T^t(n)=q}}\frac1n
\ge c_q\log H.
\]

For each such source `n`, choose the following legal augmented path:

1. Follow its ordinary orbit to `q`.
2. Follow the fixed ordinary connection from `q` to `Y(j)`, allowing
   ordinary edges in either direction as in the comparison graph.
3. Traverse the single directed comparison `Y(j) → X(j)`.
4. Follow an actual ordinary certificate from `X(j)` to one, whose
   existence is part of the failed-comparison premise.

Every vertex before step 3 is outside `C`; every vertex after it is
inside `C`. Consequently this is an actual-label first-entry path with
exactly one nonzero comparison increment, at `j`.

If `F_H(j)` is the reciprocal source mass routed through that query by
these chosen paths, then

\[
\boxed{F_H(j)\ge c_q\log H\longrightarrow\infty,
\qquad \text{the query's harmonic cut weight is }1/j.}
\]

Thus truncating a path at its first basin entry removes later sign
changes, but does not turn its input occupation mass into a uniformly
bounded multiple of the cut's harmonic weight. Even a single actual
failed retained query can carry unbounded reciprocal input mass under
legal first-entry routing. Signed telescoping cannot discard this
positive mass; completing paths into closed circulations introduces
oppositely oriented crossings rather than an upper bound on absolute
energy.

**Scope:** this construction concerns arbitrary chosen legal augmented
paths. It does **not** show that CI4's particular canonical compiler has
this congestion, and does not refute a future support-sensitive bound
for that compiler. The unsupported step would be to infer such a bound
from first-entry selection, actual basin support, and retained-set
summability alone. Controlling that specific routing, or obtaining a
different quantitative cancellation that bounds absolute energy, remains
unproved.
