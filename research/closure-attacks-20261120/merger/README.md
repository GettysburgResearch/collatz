# Multiplicative-five merger attack

**Collatz remains unresolved.** This packet isolates one smaller physical
target and tests actual certificate transport for that target.

- [Single-multiplier theorem](SINGLE_MULTIPLIER.md): `x ~ 5x` for every
  positive odd ternary unit is already equivalent to full convergence.
  Thus the older restricted five-ray criterion needs only the slice
  `t=4x`; its unbounded `5*3^i` family and the auxiliary tripling law are
  unnecessary. The later PR157 already proves a stronger one-way basin
  criterion on this slice. This is a short independently derived proof
  of its symmetric corollary, not a strengthening of that latest result.
  The hypothesis itself remains open.
- [Physical return and carry analysis](PHYSICAL_CERTIFICATE_BOUNDARY.md):
  exact variable-word necessity, an infinite family whose first same-clock ratio-five
  return increases the odd parameter, a valuation rank that proves repeated
  use of any one expanding return word terminates, and the exact carry left
  by an attempted wild-semigroup compiler. Arbitrary return switching and
  all-source success remain open.

`check_single_multiplier.py` proves the displayed path identities and
descent inequalities on every affine lift of the 320 ternary-unit cells
modulo 480, keeping (M5) calls explicit. `check_physical_returns.py` verifies
the unbounded affine return family and the exact valuation conjugacy, with
small finite controls for its repeated-word construction. Reports are
`single_multiplier_report.json` and `physical_returns_report.json`.
Normal and `-OO` execution produced byte-identical reports in this task.
Neither replay establishes the missing all-source ordinary mergers.

[REVIEW_ARITHMETIC.md](REVIEW_ARITHMETIC.md) records this agent's independent
exact-byte review of the adjacent arithmetic packet. Its mathematical
reconstruction, fresh source replay, and separate integer-only clock checks
are distinguished from external acceptance and from finite evidence.
