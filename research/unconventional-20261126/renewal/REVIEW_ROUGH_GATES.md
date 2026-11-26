# Independent review of the square-root budget at true record gates

**Verdict — verified.** I checked
[ROUGH_LOG_GATES.md](../operator/ROUGH_LOG_GATES.md) at SHA-256
119009343083c886caa5e465c08c9bcce47aa13dff76772ca0afa25d697e1a7a.
The weight is the **incoming** complete-record roof at the marked
physical endpoint. Conditioning the outgoing edge on a bad terminal
integer would require carrying this convention through the indexing.

* The logarithmic coefficient at odd record states is strictly
  increasing, as are their physical values since $x_k/M_k$ is
  increasing. The records below binary log-height $\sqrt N$ form
  one initial interval of the record chain, whose telescoping
  incoming weight is at most $\sqrt N+O_{x_0}(1)$. There is no
  multiplication of this term by the number of records.
* A higher bad terminal has one selected prime valuation whose
  log-size is at least $c\sqrt N$; the ceiling choice still works
  if the prime itself exceeds this scale. Consecutive qualifying
  record marks less than $c'\sqrt N$ clocks apart give a zero
  shifted return numerator by its real size and exact divisibility.
  There are at most $1+O(\sqrt N)$ separated groups for each fixed
  shift and selected prime, uniformly over adaptive prime choices.
* Backwards dyadic integrality reconstructs the true signed parity
  word after a zero return. A pair of true strict records has
  superunit net multiplier, positive carry and odd endpoint. Thus
  its reference is on a negative signed odd cycle. A full period
  immediately before its endpoint has strictly smaller coefficient
  at every earlier odd clock than that terminal value. Otherwise
  the physical later record would have failed the identical
  coefficient comparison. Still earlier periods shrink by the
  inverse of the positive superunit multiplier. This identifies
  the **terminal phase itself** as a signed coefficient-record phase.
* Each short-gap group is a concatenation of such exact returns to
  this same phase. From its first mark onward the first strict
  subsequent crossing depends only on the signed word, since that
  first physical mark was already a global record. Every interior
  incoming and outgoing intermediate full ladder is consequently
  the correct signed one. The distances to the immediately
  preceding and following signed record phases are bounded by a
  primitive period. After discarding fixed-length margins at the
  two ends, all three physical centers therefore have the required
  fixed past and future. Two-adic matching uses future letters and
  ternary matching uses sufficient odd grade from the past, with
  the true rotated signed phase as reference. This verifies the
  previous/current/next precision claimed in OP-G9.
* There are only boundedly many discarded marks per margin, even
  when a group contains many qualifying returns. Their incoming
  roofs have uniform upper bound $\log_2(3/2)$. Summation over the
  finite shifts and bounded-size prime pool proves the absolute
  exceptional mass bound. Multiple violations at one terminal
  can be union-bounded for the specified unprotected shifts.
* On super-square-root horizons, after normalization the fixed
  precision neighborhoods exhaust the finite union of exact
  signed edges terminating at the specified shifts. The full-law
  domination follows by simultaneous weak limits tested against
  nonnegative continuous functions. The $v>0$ refinement follows
  by applying the native-count C1 bound before weighting. If the
  full law gives one of these signed cycles an atom, the argument
  imposes a support constraint on exceptional submass there; it
  does not convert that submass into a whole component of the atom.

The comparison with the native numerical peak is only a bounded
additive discrepancy. In the proof above every selected heavy
mark is still an actual coefficient record. A statement selecting
individual numerical gate states would require the separate
transport of their marks.
