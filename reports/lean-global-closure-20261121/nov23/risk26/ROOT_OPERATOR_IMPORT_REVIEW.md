# Root reconstruction of the operator theorem used in UB7

23 November 2026. **VERIFIED at written-proof scope for the import below.**

Source: PR180, commit `7cfd911d35382d9d3bc988060ba88ade78a4267e`,
`research/closing-step-20261123/GLOBAL_CONSTRUCTION.md`, Sections 1--3,
especially Theorem 1 and equations (8), (10)--(13). This review covers
the critical-disc meromorphy, classification by actual positive cycles,
and simplicity of the operator poles. It is not a new Lean build or an
audit of every later section in that document.

## Meromorphy in the actual stated space

The space is X with norm sup_n |f(n)|/n. Conjugating by f(n)=n*h(n)
makes K a weighted composition operator on bounded functions with
weight a(n)=1/2+e(n)/(6n). Its difference from (1/2) times composition
by T is compact: truncate the rows at M and the norm of the remaining
diagonal multiplier tends to zero. Equivalently, use the source's
finite-rank truncation and finite matrix inverse on |z|<1/q_M. These
discs exhaust |z|<2. Analytic Fredholm theory, or the finite matrix
identity displayed in the source, gives meromorphy with finite-rank
polar parts there. No unspecified weighted completion is substituted
for X.

## Actual cycles exhaust the eigenvectors outside radius one half

Fix |lambda|>1/2. On a positive nonperiodic ordinary orbit, states are
distinct and tend to infinity. Eventually a(n)<q<|lambda|, so iteration
of the eigenvector relation bounds the normalized eigenfunction at its
initial state by a fixed constant times (q/|lambda|)^k. It must vanish.

On an actual cycle of shortcut length A and odd count p, multiplying
the same relation gives lambda^A=3^(-p). Conversely, a compatible
cycle amplitude extends backwards uniquely to its whole basin.
That extension is in X: choose M with q_M<|lambda|. Before entering
the cycle, an ordinary path cannot repeat, so it visits at most M
states at or below M. The remaining normalized transport factors are
at most q_M/|lambda|<1. The finitely many small-state factors give one
uniform bound, independent of the backward starting point.

Only finitely many cycles are compatible with a fixed such lambda.
Each must intersect the finite set [1,M], since otherwise the product
of its normalized weights would have modulus strictly smaller than
|lambda|^A. Distinct cycles cannot share a state. Thus the eigenspace
is exactly the finite collection of compatible cycle amplitudes.

## No hidden Jordan chains

Restriction to a compatible cycle is a finite weighted permutation
matrix. Its characteristic equation is t^A=3^(-p), whose roots are
simple. An eigenvector in the range of K-lambda I would therefore
restrict to zero on every compatible cycle. The preceding eigenvector
classification would then make it zero everywhere. Hence no nonzero
generalized eigenvector chain of length two exists; longer chains are
excluded as well. In the Fredholm region this makes every operator
resolvent pole simple.

The eigenvectors live on actual ordinary basins. A separate finite
matrix introduced by the truncation can have presentation artifacts,
but those do not add poles to the full resolvent once its kernel has
been classified. A particular forcing coordinate may cancel a genuine
operator pole; UB7 concerns the full resolvent and does not assume
that every pole survives in every scalar coordinate.

## Consequence used in this packet

At each interior cycle pole, the grouped factor constructed in UB5 has
an analytic zero. The simple finite-rank principal part is therefore
removed by multiplication, yielding UB7 on |z|<2. Overlapping cycle
root groups only increase the zero multiplicity and cause no defect.
This argument establishes no continuation across the boundary circle
and no absence of unknown cycles.
