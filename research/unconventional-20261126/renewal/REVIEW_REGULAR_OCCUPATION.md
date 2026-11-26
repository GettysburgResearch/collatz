# Independent review of the conservative regular log-height sector

**Verdict — VERIFIED at the stated pin.**
[REGULAR_OCCUPATION.md](../operator/REGULAR_OCCUPATION.md),
SHA-256 016949d85c512c229043fbe7be50188deb140b84c15d01cc72315845e720ba43.
I checked the compulsory law, edge normalization and compactification
against [GATE_SUSPENSION.md](../operator/GATE_SUSPENSION.md). The
claimed transverse measure may be infinite and the regular sector
may have zero mass.

* For each fixed translation time $t$, the continuous interval
  sample before and after translation differs only on endpoint
  time windows of total length at most $2t$ on the uniform
  interval of length $A_n$. Joint weak subsequences therefore
  have the same two one-mark marginals. The fractional age is
  independent uniform conditional on the edge even if the edge
  limit lies on the compactification boundary. At a *regular*
  initial dyadic phase a finite succession of positive roofs
  already covers the allotted forward time. Those blocks are
  locally forced by a finite native parity cylinder, and exact
  boundary coincidence has conditional age probability zero.
  The marked future then passes by continuity along just these
  finitely many labels. Regularity is preserved forward, so
  stationarity of the full pair marginals leaves no compensating
  influx into the regular sector from its complement. This
  justifies restricting the finite suspension measure even though
  the regular set itself need not be clopen.
* In height coordinates its measure is $(\lambda/a)(dv)\,dh$.
  A finite forward time crosses finitely many boundaries on this
  sector because the genuine roof series diverges. For $a\ge\delta$
  on a marked set $B$, time in the last $\epsilon<\delta$ of each
  interval differs from $\epsilon$ times its departure count by
  at most two partial endpoint contributions. Invariance gives
  expected occupied time $T\epsilon\pi(B)$, while integer-time
  additivity gives expected departure count $T\mu(B)$. Divide
  by $T$ before exhausting by $\{a\ge1/j\}$; these sets have
  $\pi$-mass at most $j\lambda(1)$. Counts in $B$ and $F^{-1}B$
  differ by at most one over any long observation, so their mean
  intensities agree also for infinite-mass sets by monotone
  exhaustion. No division of the original boundary mass by a
  zero roof is involved.
* Recurrence for the time-one map on the finite suspension
  returns almost every point above each positive-$\pi$ set to
  its marked intervals infinitely often. Each interval has
  bounded duration; finitely many boundary advances cannot
  account for such returns. Since interval heights have positive
  length and their base progression is deterministic, this
  proves conservativity of the base. A mere equality of
  $\sigma$-finite base marginals would have been insufficient.
* For a dyadic atom, recurrence of that coordinate gives a
  genuine closed record word of positive total roof. Its fixed
  point is a negative rational dyadic unit integral at three.
  On its finite collection of phases the finite suspension
  remains invariant. A long log-time shift traverses at least
  $t/\log(3/2)-O(1)$ whole blocks and thus contracts even the
  least favorable ternary difference to zero. The ternary
  conditional law is the diagonal one.
* For a ternary atom, countability of the atom set and of the
  label alphabet permits discarding all null transitions. The
  affine maps are injective, so atomic transitions are confined
  to that sector in both directions. Conservativity of each
  positive labeled arrow supplies a realization returning to
  that arrow; its intervening itinerary is a finite closed walk
  of genuine positive-mass arrows. Fixed points at all rotated
  phases are rational signed odd units, and the exact rational
  gaps between them are their genuine gaps. The first strict
  upcrossing in the forward signed itinerary is unique. Thus
  every arrow is on a deterministic cycle and the true dyadic
  address follows this whole future. Uniqueness of the dyadic
  parity code identifies the local pair.
* On a cycle, rotation in its continuous phase modulo its total
  roof and in the translated real phase modulo $\log2$ has no
  nonconstant invariant character: the ratio of periods is
  $m\log_2 3-S$, which is irrational. Product Haar on this
  two-torus implies the stated independence and roof-proportional
  phase masses. For a positive rational with infinite coefficient
  records, unboundedness of their heights follows also from
  fixed-denominator positive-path distortion in PR210: otherwise
  the positive distinct numerator path could not escape, while
  a positive cycle has only finitely many coefficient records.

There is a short direct check specifically for atoms of the *full*
probability on the rational diagonal. A rational diagonal phase
$u$ is a negative signed periodic record phase by PR210. Fix one
edge $u\to u'$ in its deterministic cycle. In a sufficiently
small dyadic neighborhood of $u$ the next two record labels, and
hence their positive roofs $a(u),a(u')$, are locally constant.
Restrict the empirical starts to shrinking joint neighborhoods
of $(u,u)$ and transport their counts to the next phase. Their
circle marks are translated by $a(u)$. Nonnegative tests and
shrinking neighborhoods yield for the finite circle atom measures
$$
 \lambda_{u'}/a(u')\ \ge\
       (\operatorname{rot}_{a(u)})_*(\lambda_u/a(u)).
$$
For rigor one may first take open start neighborhoods whose
closures are sent inside a fixed closed terminal neighborhood,
approximate nonnegative continuous circle tests there, and use
portmanteau before shrinking the terminal neighborhoods to their
intersection. Boundary indices have negligible bounded roof
relative to $A_n$. Summing the comparisons cyclically forces
equality at every phase. The total rotation is irrational
relative to $\log2$, giving Haar and roof weights again. If the
full start law is supported on the rational diagonal, its
roof-weighted alphabet is automatically tight: every starting
dyadic limit from unbounded labels lacks a finite upcrossing,
whereas every rational diagonal phase here has one. This latter
support observation does not imply finite total raw boundary rate.

The [fixed-source stress tests](LOG_HEIGHT_MODEL.md) show why the
regular-sector rigidity still requires new ordinary arithmetic.
A symbolic law can place its entire normalized height on a
signed diagonal Haar cycle while retaining a rare off-diagonal
cluster and an irrational initial dyadic address.
