# Finite certificates with arbitrary odd denominators

Read [FINITE_RATIONAL_CERTIFICATE.md](FINITE_RATIONAL_CERTIFICATE.md).

For one actual positive source and a supplied rational complementary
candidate `a/q`, with `q` any positive odd integer, an explicit finite
number of parity tests now suffices to force eventual periodicity.
The proof controls excursions outside the finite numerator interval
`[-q,q]`, then uses a repeated numerator and a finite parity window
to force a repeated ordinary state. Zero and negative numerators are
included. The eventual period is at most `2q` by the independently
proved complementary-denominator capacity bound.

The seven numerical core lemmas are Lean checked. The complete finite
certificate and its cycle consumer are reviewed written arguments.
Constructing a candidate that funds its own horizon for every positive
input remains open; the larger denominator class also leaves
nontrivial-cycle exclusion as a separate obligation.
