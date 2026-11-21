# Return dynamics after the forced narrow-band visit

Status: **OPEN** as a route to universal convergence. The work below does not
prove Collatz. Sources are frozen at PR #173,
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, especially
`research/lean-shell-cover/ForwardSection.lean`, `SectionDynamics.lean`, and
`RisingReturns.lean`.

The ordinary shortcut is `T(n)=n/2` on even inputs and `(3n+1)/2` on odd inputs.
A mark is an odd positive integer `n` satisfying

`(floor(log2 n)+1)*(n-2^floor(log2 n)) <= 70*2^floor(log2 n)`.

## The global closing attempt

For an odd orbit `x_0,...,x_p`, write `A_p` for the total number of divisions by
two in its `p` accelerated odd steps, and put

`E_p = sum_{i<p} log2(1+1/(3*x_i))`.

The exact real identity is

`log2(x_p)-log2(x_0) = p*log2(3)-A_p+E_p`.

If both endpoints are marks, write `log2(x_0)=d+theta` and
`log2(x_p)=e+eta`. Their defining inequalities bound `theta` and `eta` above
by `log2(1+70/(d+1))` and `log2(1+70/(e+1))`. Consequently

`e-d = p*log2(3)-A_p+E_p+theta-eta`.

This does give a restriction on near-integer approximations by `p*log2(3)`.
It does not determine the sign of `e-d`: the actual valuation sum `A_p` remains
the uncontrolled integer coordinate. A proof that the section forces enough
valuation across some complete sequence of returns is still missing.

I attempted to recover that coordinate from the long leading-zero gap supplied
by membership in the band and the trailing-one run that an increasing odd
prefix consumes. Two exact constructions below explain why the first proposed
forms of that rank do not close the argument.

## Every finite odd cylinder remains possible inside the band

For any `r<2^k` with `r` odd, and any threshold `B`, set

`s=k+B+1`, `d=2*s`, `n=2^d+r`.

Then `n>B`, `floor(log2 n)=d`, and `n` is marked. Indeed,

`(d+1)*r <= (2*s+1)*2^s <= 3*2^(2*s) <= 70*2^d`.

Moreover `n=r (mod 2^k)`. For every `j<=d` the exact affine identity is

`T^j(n) = 3^oddCount(r,j)*2^(d-j)+T^j(r)`.

For `j<d`, the extra term is even, so the complete first `k` parity word is
identical to the word at `r`. Its odd count is unchanged as well. The mark's
leading digits therefore cannot justify eliminating any fixed odd-source
parity cylinder. This is an ordinary positive-integer construction, not a
2-adic realization argument. Even-source cylinders are excluded because the
definition of a mark requires oddness.

`MarkedCylinders.lean` formalizes these assertions using the section definition
and the existing exact endpoint-shift identities. Lean 4.34.1 checked the file
with warnings treated as errors; its printed theorem dependencies contain only
`propext` and `Quot.sound`.

## A reset of the two proposed rank coordinates

The explicit numbers

`n=(2^525*3073-5)/3`, `m=2^512*3^11*3073-1`

are both marked, and `T^13(n)=m`. Their binary exponents are respectively
`535` and `541`. Further, `n=1 (mod 4)`, so `v2(n+1)=1`, whereas

`m+1=2^512*(3^11*3073)`

has exact 2-adic valuation `512`, since its displayed odd factor is odd.
Thus both binary exponent and trailing-one depth increase along an actual
finite trajectory whose endpoints are marks. Any claimed rank that is
coordinatewise nondecreasing in these two parameters and strictly decreases
at every marked return is incompatible with this trajectory: the induced
return dynamics captures its marked endpoint.

The arithmetic is recorded as one checked kernel-reduction theorem in
`MarkedResetWitness.lean`; its axiom report is empty. The core-only file uses
`decide`, never `native_decide`. This is a witness against an entire proposed
rank class, not a claim of an increasing infinite orbit. A companion agent
handles an unbounded first-return reset family, so that work is not duplicated
here.

## Cofinal collisions remove the monotonicity restriction

`BandCollision.lean` proves the stronger result described in
`EQUAL_FEATURE_COLLISIONS.md`: above every cutoff there is an actual nonconstant
finite path between two marks with the same binary exponent, both congruent
to one modulo four. Their trailing-one depths are both exactly one. The
construction also proves `(B+1)*2^t<=n`, ensuring that every intermediate state
through the endpoint clock stays above the cutoff.

Its dependencies are the source's proved rational-rotation approximation and
the companion `BandWord.lean` ordinary word/CRT construction. The full file
passes Lean 4.34.1 with warnings treated as errors and only the standard
`propext`, `Classical.choice`, and `Quot.sound` axioms.

Thus an arbitrary function of binary exponent and trailing-one depth cannot
strictly decrease at every section return beyond a finite exceptional range;
monotonicity of that function is unnecessary. The finite path begins and ends
at exactly the same feature pair. A rank that uses more information, or a
proof that groups a variable number of returns, is not excluded.

## Why the earlier expanding-return proof does not automatically iterate

The published increasing-first-return construction has an all-odd prefix of
length proportional to its binary exponent `d`. Its mark window has phase
width proportional to `1/d`. Basic rational-grid estimates only guarantee a
bounded number of visits in that prefix.

Trying to obtain `K` visits at multiples of one approximating denominator `q`
requires both `K*q<=d` and `K*|q*log2(3)-a|<=C/d`. Together these require

`K^2*q*|q*log2(3)-a|<=C`.

The supplied Dirichlet bound does not make the left side uniformly small for
arbitrary `K`. An assertion of arbitrarily many rising returns cannot be
deduced just by repeating the first-return argument. No such assertion is made.

## Remaining global obligation

A successful rank must accommodate all ordinary finite low-bit words and the
simultaneous size/trailing-run reset. A proof of eventual downward scale change
under the total section map is still absent. No hypothesis about that change
has been introduced as an axiom or promoted to a proved result.
