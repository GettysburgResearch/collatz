# Root review of complete cyclotomic value separation

Date: 2026-11-23. Source:
`research/lean-global-closure-20261121/risk25/CYCLOTOMIC_VALUE_SEPARATION_PROPOSED.md`,
SHA256 `a65775e58fff641dba07d36e622d38979e1a93268ddea0e5dd8e339ffc35021b`.

**VERIFIED as a written argument, with the stated fixed-logarithm and
ordinary-state-count inputs.** The original source's PROPOSED label is
preserved to retain its exact bytes. This review supplies a narrow
written-proof verdict for CV1--CV13; it is not a Lean formalization or a
complete-cycle exclusion.

I reconstructed the coefficient support argument first. A monic integer
factor P of degree k has |P(0)|=2^(ak/b), so b divides k. Since its roots
are closed under complex conjugation and have common modulus r,
X^k P(r^2/X)=P(0)P(X). Comparing paired nonzero coefficients forces
b to divide 2i. Thus P is a polynomial in X^(b/gcd(b,2)). The same
degree argument makes X^b-2^a irreducible, and Q(r)>0 prevents the
positive root from being cancelled. Its entire binomial therefore
survives in F_0.

After this reduction the normalized residual roots are roots of unity
over Q when b is odd, and over Q(sqrt(2)) when b is even. In the second
case the normalized degree is even and rationality of the original
polynomial gives f^sigma(Y)=f(-Y). The principal roots 1 and -1 can be
removed together.

I checked the orbit classification over Q(sqrt(2)). Orders not divisible
by eight have a single packet: a compatible lift of each unit residue
can be chosen with character (2/j)=+1 modulo eight. Orders divisible by
eight split into two packets of equal size. Each packet is closed under
complex conjugation. For orders divisible by sixteen, negation preserves
each packet whereas sigma exchanges them, so rational rescaling forces
both. Only orders 8m with m odd permit a single half packet.

For these exceptional packets, the unconditioned exponent progressions
1+8k and 7+8k have product at one equal to 2-sqrt(2); the other two
progressions give 2+sqrt(2). Partitioning exponents by gcd(j,m), and
using multiplicativity of the character, gives CV7 with its stated sign.
Character-weighted Moebius inversion gives CV8. For m>1, the full
cyclotomic value is one, and 2^omega(m)<=phi(m), so the smaller half
value is at least (1+sqrt(2))^(-phi(m)). For m=1 the two exact values
satisfy the same degree-based lower bound.

The paired-root identity CV3 is exact. Multiplying it over every full or
permitted half packet, and converting degrees back from Y to X, gives
the base sqrt(3r)*(1+sqrt(2))^(-1/b). Since r>3 and even b>=2, this
is bounded below by beta=3/sqrt(1+sqrt(2))>3/2. Odd b gives the
stronger base three. The positive principal binomial value contributes
3^b(e^L-1)>c_0 3^b b^(-K_0), by the same primary Matveev input
already checked in the core paper. This proves CV1 without the older
finite factor-gap certificate.

For actual integer cycles the independently reviewed global state count
gives a uniform upper bound on Lambda, and the reduced-clock bound gives
m<=C_m d^K. Applying lattice estimate RL9a then gives
M<=C d^K(3/2)^(d-1). Division yields CV13. The ratio's exponential
base is 2/sqrt(1+sqrt(2))>1. Combining with the power lower bound
on d also implies a stretched-exponential lower bound in the period
for D_pol/M, after increasing the absolute threshold.

This is an asymptotic necessary condition. It does not make D_pol a
reduced rational denominator. On a hypothetical integer cycle, the
full numerical gcd with Q_0(3) would still equal D_pol. No estimate
bounding that gcd by the maximum state has been proved, and the
retained denominator-five rational control shows why such an estimate
cannot be imported from rational-word geometry alone.
