# Exact ternary laws by cyclic geometric convolution

**PROPOSED implementation and arithmetic derivation; bounded tests, not a
forward-orbit distribution theorem.** This computes both the original
reference law and the square tilt in [INVERSE_PRESSURE.md](INVERSE_PRESSURE.md).

Fix b=2 or 4 and exponents with probability (b-1)b^-a. Let nu_(q,b) be the
law of Y_q modulo 3^q. For q=0 the law is concentrated on the only residue.
Its projectivity follows directly from the defining series: later summands
vanish at lower ternary precision. The affine recursion is

    nu_q = law of (3Y_(q-1)+1)/2^a mod3^q.

This is a law of an auxiliary model, not the empirical law of arbitrary sources.

## D1. Exact cyclic recurrence without truncating exponent tails

Put m=3^q, P=2*3^(q-1), and represent nu_(q-1) by integer numerators u_y and
a common denominator D. Two generates the units modulo m. Let r_y be the
unique discrete logarithm satisfying 2^(r_y)=3y+1 mod m, with 0<=r_y<P, and
put B_r=sum_(y:r_y=r) u_y. Set Q=b^P-1.

The total probability of an exponent a in a fixed nonzero residue class a_0
mod P, 1<=a_0<=P, is exactly

    (b-1)b^(P-a_0)/(b^P-1).

All infinitely many exponents in that class are summed, not cut off. Thus if
N_d/(D Q)=nu_q(2^d),

    N_0=(b-1) sum_r B_r b^((-r) mod P),
    N_(d+1)=b N_d-(b-1) B_((d+1) mod P) Q.          (1)

The subtraction corrects the single exponent that wraps from P-1 to zero.
One cyclic pass gives every unit probability; multiples of three have zero
mass. Exact closure N_P=N_0, nonnegativity, total mass and projectivity are
checked after every pass.

## D2. A convenient common denominator at every level

One may take

    D_q=b^(2*3^(q-1))-1, q>=1; D_0=1.               (2)

This need not be the reduced denominator of every entry. Since D_(q-1)
divides D_q, it remains to show D_(q-1) divides the numerator N_0 in (1).
The q=1 case is immediate. For q>=2 group y by its residue modulo 3^(q-2).
The discrete logarithms reduce modulo P/3, and powers of b reduce modulo
D_(q-1)=b^(P/3)-1. Projectivity says the grouped old numerators sum to
(D_(q-1)/D_(q-2)) times the corresponding level-(q-2) numerator. Therefore
N_0 modulo D_(q-1) is

    (D_(q-1)/D_(q-2)) times the preceding-level N_0.

By induction that preceding raw numerator is divisible by D_(q-2), proving
the claim. Divide (1) by D_(q-1) to get the implemented integer recurrence

    v_(d+1)=b v_d-(b-1)B_((d+1) mod P) D_q/D_(q-1).

The discrete logarithm table is built by successive multiplication by two;
no generic discrete-log search is used. There are O(3^q) big-integer additions
and multiplications by fixed b after building N_0. **This is not an O(3^q)
bit-complexity claim:** numerators and denominator have O(3^q) bits, and the
complete exact output itself has much larger bit size. Computing the initial
weighted sum naively also performs big-integer work at that scale.

## Executed validation

The standalone program computes both b=2 and b=4 for q=1,...,9. It verifies
all 59,046 residue entries across those 18 laws, with maximum modulus 19,683.
At q<=4 it compares every entry against a separate rational implementation
that explicitly sums all exponent congruence classes; 240 exact probabilities
are compared. The b=2, q=2 law has numerator vector

    (0,8,16,0,11,4,0,2,22), denominator 63,

matching the classical reference control used in the parent packet. Higher
levels are checked for mass, cyclic closure, nonnegativity and projectivity,
not against a second full high-depth implementation. Full numerator vectors
are hashed deterministically rather than committed as very large payloads.

Selected densities and finite-depth sums are recorded with rational outward
decimal enclosures. The square-tilted finite-depth sums are also compared
against independently computed, source-census all-depth upper bounds. This
cross-check uses a different indexing (forward source paths instead of residue
convolution). It does not make the two algorithms independent mathematical
review, and it does not prove any untested floating-point approximation.
