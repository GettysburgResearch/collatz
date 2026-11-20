# Independent review of the two-macro normalization

Reviewed `agent_boundary_upper/TWO_MACRO_NORMALIZATION.md` and
`agent_boundary_upper/check_two_macro_normalization.py` after the original
expanding-return packet was finalized.

**Conclusion: no mathematical issue found.** This is an exact equivalence
of existence of infinite positive schedules with a restricted integer
ceiling orbit. It is not an all-source exclusion theorem, and the note
accurately explains why excluding that subsystem would not close the
least-counterexample argument.

## Points checked independently

1. `Delta=2^9*3^14`, the two constant identities, and the shared binary and
   ternary congruences are correct. On an infinite path, each term after the
   first is both an endpoint and a continuing safe source. That conjunction
   supplies the full congruence modulo Delta. Its normalized value is
   positive because every continuing source exceeds `a_star`.
2. Substitution gives `M b_next=K b+c+epsilon` exactly. Conversely,
   `a=a_star+Delta*b` and the next reconstructed a are positive even integers.
   The exact affine equation therefore forces
   `K*a+C_epsilon=0 modulo 2M`. Oddness of K selects exactly the certified
   safe residue. Since that residue lies strictly between 0 and 2M, a positive
   representative has a nonnegative cylinder parameter. No extra parity
   assumption is missing from the converse.
3. Because `0<c<c+1<M`, an integral normalized step is precisely the ceiling
   step, with one of the stated two remainders. The finite-word terminal
   congruence has a unique source class modulo `M^h`. Reducing it modulo M
   forces the first integral step; division by M and induction force every
   subsequent step. Positive representatives stay positive.
4. The real limit and its tail are correct:
   `beta=lambda^(-n)*b_n` tends to a positive limit, and
   `beta*lambda^n-b_n` belongs to `[c/D,(c+1)/D]`, strictly inside `(0,1)`.
   The fractional-part conclusion follows. In the 2-adic limit the remaining
   endpoint has valuation at least `38n` and vanishes; in the real limit it
   tends to beta, not zero. Thus simultaneous convergence does not identify
   the two limits. The interval condition is correctly labeled necessary,
   not sufficient for the exact two-digit recurrence.
5. The relevance qualification is essential and correct: the known convergent
   physical X arm already excludes infinitely many unchanged expanding
   returns in the intended least-failure setup. Permanent avoidance of useful
   sections remains outside the restricted ceiling-map problem.

The provided exact checker passed on its stated 126 finite digit words and
642 macro steps. It was replayed from an unchanged copy in this review
directory so its report-writing behavior did not modify the author's files.
The current checker writes its report beside `__file__`; making its default
stdout-only would be a publication hygiene improvement, not a mathematical
correction. No broader numerical search was performed.

The external primary-source citation was handled separately by the root
reviewer. The mathematical normalization and conclusions reviewed here use
no conjectural equidistribution input.
