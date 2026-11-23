# Independent review of the endpoint-retaining renewal argument

Reviewer: cycle literature lane. Date: 23 November 2026.

**Reviewed source:**
`../atomic/ORDINARY_RENEWAL_AND_RETAINED_ENDPOINT.md`

**Exact SHA-256:**
`6bb1ea3812806af2c799fa22a43d7384647e6c2b288813ead185301f78ecd1f9`

**Scope:** equations (7)--(20b), (25)--(38), and the full-odd-domain
corollary (39)--(43), conditional on the explicitly retained positive
pressure function and finite harmonic probability in (1)--(3).

**Verdict: PASS for this written scope.** No new verification of the
earlier existence/positivity theorem for that hypothetical escaping
component, external literature proof, or infinite Lean formalization is
claimed.

The following calculations were reconstructed independently:

- `S^j` is an ordinary bijection onto the stated high-valuation set.
  Atomwise scaling yields normalized mass `t^j`, geometric renewal, and
  the conditional pushforward without a missing normalizing factor.
- The ternary orbit length is exactly `3^(K-1)` in a fixed class modulo
  three. Finite-period counting proves the cylinder and bounded-endpoint
  test estimates. The unchanged second marginal is `U_*mu`; tightness on
  its discrete ordinary space justifies the joint weak limit. The binary
  collapse and the correlated valuation-phase lift preserve that label.
- On a legal inverse branch, the change of variables from normalized
  class Haar to normalized unit Haar contributes `2/3`. Summing even or
  odd exponents gives exactly the two displayed beta constants; their
  half-sum is `rho(s)`. This yields the finite ternary Green integral.
- Actual predecessor atom identities give the future-occupation formula
  and `U_*mu=(P_s1)mu`. The positive minimum of `P_s1` therefore retains
  the infinite Green integral in the ordinary endpoint coordinate.
- Expanding the source density square gives `t^(-min(i,j))`, with
  multiplicity `2(J-k)-1`. Reindexing proves both L2 bounds. For arbitrary
  averaging weights, one retained ordinary atom bounds each congruence
  class of averaging times, places at least half the mass in `C_k`, and
  yields the displayed Holder lower bound with the correct exponent.
- On the explicitly enlarged odd domain, the new probability is
  renormalized rather than identified with `mu`. The symmetry `4n+1`
  has period `3^K`, giving full ternary Haar independent of the retained
  ordinary endpoint. The full-domain operator permits parents divisible
  by three, has no branches at roots divisible by three, and satisfies
  `m3 P_s^+ = rho(s) m3` with the factor `1/3` for additive Haar.

No conclusion excluding an ordinary escaping atom follows from these
calculations, and the source does not claim one. In particular, its two
Green-integral coordinates and its two orders of limits are kept distinct.

One nonmathematical wording clarification was suggested: the introduction's
phrase “the original atomic law” should identify the unchanged **next-state
law `U_*mu`**, so that it cannot be mistaken for equality with `mu` itself.
The displayed equations already have the correct law. Any subsequent
edit must receive its own hash binding; this report reviews only the bytes
identified above.
