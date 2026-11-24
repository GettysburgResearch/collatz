# The missing bridge after the literature pass

**Full Collatz remains open.** This pass tests how the literature can connect
the repository's results to a statement about every ordinary source. It
produces a broader written rigidity argument, checked algebraic interfaces,
and a sharp checked obstruction to one certificate strategy. The positive
analytic conclusion retains its source-qualified inputs; it is not a Lean
proof of convergence.

The three attacks were ordinary invariant labels and compact dynamics;
complete-certificate rewriting and inverse-tree integrality; and coefficient
stopping with the full affine correction. The
[source ledger](LITERATURE_SOURCES.json) also records the branches updated
after the preceding [145-PR reassessment](WHOLE_REPO_SYNTHESIS.md).

## 1. A broader regularity criterion

Use the ordinary shortcut map

\[
 T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
 \end{cases}
\]

For a bounded sequence `a`, write

\[
 L_X(a)=\frac1{H_X}\sum_{1\le n\le X}\frac{a(n)}n,
 \qquad H_X=\sum_{1\le n\le X}\frac1n.
\]

The [complete written argument](LITERATURE_RIGIDITY_BRIDGE.md) proves the
following, under its explicitly retained stationary-density inputs.
If `f` is an ordinary Boolean label with `f(Tn)=f(n)`, then for every fixed
real `theta` which is not an integer,

\[
 \boxed{L_X\bigl(f(n)e^{2\pi i\theta n}\bigr)\longrightarrow0.}
 \tag{1}
\]

This is an unweighted logarithmic statement about the original ordinary
integers. It is not a temporal average along one orbit. The general form
says that the label is asymptotically independent of each fixed finite
collection of congruence coordinates and real frequencies. The argument
does not establish existence of `lim L_X(f)`; a subsequential scalar can
depend on the subsequence.

For a nonconstant Boolean label, the earlier positive logarithmic
predecessor estimate then supplies one `epsilon_f>0` such that every fixed
real or complex trigonometric polynomial `P` satisfies

\[
 \boxed{\liminf_{X\to\infty} L_X(|f-P|)\ge\epsilon_f.}
 \tag{2}
\]

The constant is independent of the number and values of the frequencies
and of the coefficients. Clipping the real part of an approximant into
`[0,1]` cannot increase its distance from a Boolean label. The same
obstruction passes to the Besicovitch almost-periodic closure.

Consequently, **qualitative almost-periodic approximation of the basin-of-one
indicator would force full convergence**, under the stated analytic inputs.
Both periodic cycles and nonperiodic components are covered by this label
criterion. No approximation rate is required, and the frequencies need not
be rational. This weakens the sufficient regularity hypothesis in the
earlier [periodic-only theorem](PROFINITE_LABEL_RIGIDITY.md).

The quantifiers matter. An approximant is fixed before taking the cutoff
`X` to infinity. Its complexity may depend on the requested approximation
accuracy; it may not be chosen anew as an arbitrary lookup table at each
cutoff. Constructing the required approximants for the actual basin label
remains the missing step.

## 2. What makes the all-frequency proof work

The literature suggested an auxiliary compact group on which division by
both two and three is legitimate. For finitely many real frequencies,
use a finite residue factor coprime to six and copies of the compact group
whose character group is `Z[1/6]`. The latter is the six-solenoid. After
clearing rational denominators and choosing a rationally independent
frequency basis, ordinary integer sampling is equidistributed jointly
with every fixed binary and ternary residue coordinate.

The shortcut branches on the extra group are

\[
 F_0(z)=z/2,\qquad F_1(z)=(3z+w)/2.
\]

Each preserves Haar measure. Their common invariant functions are
translation-invariant: the equivalent identities under `2z` and `3z+w`
give equal values at `6z+w` and `6z+2w`. Since multiplication by six is
onto, this yields invariance under translation by `w`. That translation
has dense orbit in the chosen group.

[AffineRigidity.lean](AffineRigidity.lean) checks this algebraic step, its
continuous version, and the exact finite harmonic analogue. For an average
of two finite permutations, a sum of squares is used to prove separate
branch invariance. The module never treats a harmonic average as two
independent inequalities. See [the interface note](AFFINE_RIGIDITY.md).

The written measurable proof supplies the additional steps. A Bernoulli
conditional-expectation argument gives ergodicity of the extra affine
factor. Coupling with identical future parity symbols removes the initial
ternary coordinate. The stationary ternary density comes from Tao's
marginal fine-scale mixing and the previously audited atom-floor argument.

For the ordinary label, take subsequential limits of the **unweighted**
logarithmic empirical measures. Joint equidistribution dominates each limit
by full Haar measure. Exact changes of variables on the ordinary even and
odd branches imply invariance of its density under the nonsingular compact
shortcut map. The branch factors are exactly `1/2` and `3/2`, with the
odd image restricted to the ternary residue two.

Ergodicity makes that density constant on the stationary unit region.
The positive density floor transfers this to Haar measure on all ternary
units. Almost every binary input eventually has an odd step; this sends
every ternary nonunit into that unit region. Nonsingularity therefore
extends the same constant to full Haar measure. This proves (1) and its
finite-frequency version. The separate logarithmic predecessor input
prevents a separating Boolean label from having scalar zero or one,
yielding (2).

This route avoids assigning an arbitrary almost-everywhere stationary
density a value at an ordinary integer. It also avoids the newer joint-clock
positive-natural-density claim. Its analytic proof and precise input pins
are recorded separately from the Lean receipts.

## 3. A control that defeats the tempting entropy shortcut

Low complexity does not supply the missing approximation. The written note
constructs the explicit Boolean sequence

\[
 b(n)=\left\lfloor\sqrt{\lfloor\log_2 n\rfloor}\right\rfloor\pmod2.
\]

It is constant on the intervals
`[2^(j^2),2^((j+1)^2))`. It has linear word complexity `p_b(L)<=4L` and hence zero
topological entropy. Both colors have logarithmic density one half, while

\[
 L_X(|b(Tn)-b(n)|)\longrightarrow0.
\]

Nevertheless its logarithmic mean distance from every `[0,1]`-valued Bohr
almost-periodic sequence is exactly one half. The proof uses the growing
constant blocks and elementary exponential-sum bounds, not a numerical
experiment.

This is not a pointwise invariant Collatz label. It proves that zero entropy,
computability, positive color densities, and asymptotically vanishing
invariance error cannot by themselves manufacture the needed
almost-periodic approximations. Further use of the exact ordinary
functional equations is required.

## 4. A complete inverse-tree obstruction, with no prefix length cutoff

The certificate attack asks whether an arbitrarily long smaller-rank prefix
can always replace a troublesome front while preserving the supplied tail.
[LiteratureCertificate.lean](LiteratureCertificate.lean) gives a sharp
negative answer on an explicit family.

Put

\[
 u=729j+7,\quad q=3888j+37,\quad S=4q=15552j+148,
 \qquad M=13824j+130.
\]

Supply any complete odd-gap certificate `tail` for `u`. Every powered child
certificate with the same suffix, arbitrary initial even run, arbitrary
finite inserted prefix, and rank strictly smaller than the parent
`grades(2,4::tail)` satisfies

\[
 \boxed{S'\le M,\qquad9S'+14\le8S.}
 \tag{3}
\]

The maximum is attained by one initial even step and the prefix `[2,2,4]`.
The entire suffix cancels in the rank comparison. The remaining rank ideal
allows just two types of prefix: gaps at most three, or at most one four
with all other gaps at most two. Ordinary inverse-edge integrality closes
both trees after the explicitly classified nodes. This is an induction over
every finite prefix, not an unsuccessful finite-depth search.

Explicit power congruences produce arbitrarily large fully certified
parents. A further checked corollary quantifies over **every proposed
finite lookahead `K`**: some such parent has a wanted target in its original
interval whose first `K` shortcut states lie above the interval of every
lower-rank child retaining that suffix. The target is chosen in a long
initial odd run `2^K v-1`.

The source and target vary with `K`; no single infinite bad orbit is
constructed. The explicit unbounded family's suffix contains a large gap,
so this is not an unbounded family already wholly inside PR177's residual
alphabet-four normal form. Deeper suffix edits and asymmetric common-future
mergers remain available. The [complete note](LITERATURE_CERTIFICATE_BRIDGE.md)
also distinguishes this result from the other branches' fixed-clock
obstructions and successful variable-clock selectors.

## 5. Why the coefficient attack changed direction

The [coefficient literature audit](LITERATURE_COEFFICIENT_BRIDGE.md) checked
Korec's primary density theorem and a recent first-crossing preprint, then
compared them with the repository's exact correction and orbit-Mellin
work. Several initially attractive estimates were already known in that
scope. They were not added as nominally new proofs.

The obstruction remains the same exact inequality. If
`T^k(n)=C_k(n)(n+M_k)`, then ordinary descent requires
`n(1/C_k(n)-1)>M_k`. A coefficient drop alone does not pay the nonnegative
affine correction. The earlier checked finite coefficient alternative is
retained; the all-supercritical escape alternative has not been excluded.

## 6. Late repository connections and the next closing obligation

The late refresh found complementary developments in PR175, PR176, PR178,
PR180 and PR185; their exact observed heads are in
[LITERATURE_SOURCES.json](LITERATURE_SOURCES.json). Those PR descriptions
report global potential moments and antichain bounds, critical Abel
domination, an ordinary minimum-moment criterion, exact witness transport,
and variable-clock mergers. Their own source and execution qualifications
remain in force. This metadata reconciliation is not a new full audit of
all those proofs.

These developments do not yet supply almost-periodic regularity of an
ordinary component label, a complete successful certificate dispatcher,
or the retained-source estimate that forces absorption. The current pass
sharpens those alternatives: the analytic regularity condition is weaker
than before, while the certificate theorem rules out a whole class of
prefix-only repairs even when arbitrary prefix lengths are permitted.

The [execution and review report](../../reports/2026-11-21-dyadic-descent/literature/README.md)
separates the new Lean statements, their fresh dependency replay, the
written analytic proof, and repository integrity checks. The earlier
91-statement continuation remains unchanged.
