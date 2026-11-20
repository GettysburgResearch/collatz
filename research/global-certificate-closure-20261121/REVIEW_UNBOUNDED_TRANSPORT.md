# Independent reconstruction of the unbounded first-one transport

**VERIFIED IN THE STATED SCOPE, as an internal mathematical review.**
This is not external referee acceptance, a proof-assistant verification,
or a proof of Collatz. The new claims remain proposed research.

The reviewed files are:

| File | SHA-256 |
|---|---|
| `UNBOUNDED_FIRST_ONE_TRANSPORT.md` | `24dfeff2089771c4ac03587bdb68a2cae6886399230dc38df2746f22092bcd23` |
| `check_unbounded_first_one_transport.py` | `8b5227e5579769aab6edf823fa6387c397ac17aa22f7a40ba360ddd906c1a2a4` |

## Unbounded identity and physical guards

I reconstructed the inverse maps independently. Set
`v=2^(b-3)q`, `z=(4/3)^(r-3)`, and write each side as a polynomial
in `z*v`, `z`, and 1. Exact equality of its three rational coefficients
proves both seed extensions for unrestricted r and b. In particular,
`I_1 I_1 I_4` has slope `64/27`, intercept `-19/27`, and value `5/3`
at 1. The source and target suffixes obey
`Q_a(5q)-1=(10/3)(S_a(q)-1)` for a=2,4. These identities verify UF4
without extrapolating a sampled run length.

The counts are r+4 on both arms, with clock `2r+b+a+2`. The source
correction is `(84+2^(a+2))4^r-27*3^r`, and the target correction is
five times that value. Divisibility of the full inverse numerator by
`3^(r+4)` forces all intermediate inverse divisions. Positive exponents
and positive odd endpoint 5q give positive odd states, none equal to one.
The same no-early-hit argument applies to the source prefix.

The cylinder modulus in UF6 includes the minimum last exponent four.
Its endpoint after only those four final clocks may be even; the proof
correctly takes the full actual last valuation to obtain the odd q.
The independent checker verifies 44 whole affine cylinders using ordinary
parity words, including slope and intercept rather than only sampled
integers. The displayed symbolic proof covers all run lengths.

The separating invariant `v2(3x-1)=2r+2` is correct. It proves the
disjointness across run lengths; the later exponent separates a=2,4.
The first two letters distinguish both new families from the older
renewable domains. The endpoint bound follows from
`q <= (2187/16384)x + 25/64` and the actual lower source bound x>=171.
The density sum, including control of the infinite tails, is valid.

## The inverse fiber is controlled by one ternary valuation

I separately rearranged the inverse equation to obtain

\[
3^{r+3}(3x-1)=4^r(2^{b+a+2}q-C_a).
\]

The factor `3x-1` is a ternary unit. Thus r is uniquely determined
by a fixed b,q,a, and r>=3 forces the one residue class of b modulo 486.
This uniqueness is essential: summing independently over all r would
discard the useful arithmetic dependence. The estimate in UF17 preserves
positivity, the actual endpoint lower bound, and the full infinite
geometric tail. Deleting nonunit sources and restricting the original
source cutoff can only reduce its nonnegative left side.

## Independent complete coefficient check

`review_unbounded_transport.py` imports no author checker. It builds
the unit groups modulo9,27,81,729, uses discrete logarithms to select
the least admissible exponents, and reconstructs the full credited
PR167 coefficient formula plus the two new fibers.

It verifies all 486 endpoint residues. Its fractional-power enclosures
use denominator `2^42`, independently of the author's decimal grid.
Every enclosure is certified by two adjacent integer twenty-fifth-power
comparisons. All denominators remain positive, and the complete upper
bounds are below 5/8 and 91/100. The normal and optimized reports are
identical.

The energy proof groups by actual ordinary endpoints and uses
`q<=x/3` on the entire combined domain. It does not interchange a
signed series or subtract infinite quantities. The finite-cutoff
subtraction and monotone limit giving UF22 are valid. The result keeps
the existing constants on a strictly larger domain; it does not bound
the remainder. No rigidity theorem or external density assumption is
needed for UF1--UF5 themselves.

## Compiler and latest-source boundaries

The explicit dictionary is prefix-disjoint. On its stated language,
consumption of the finite supplied certificate proves parsing
termination, and composition gives the exact first-hit counts p+1,N+4.
Valid unrecognized witnesses and malformed witnesses are distinct
outcomes. PR167's complete homogeneous recognizer is credited and is
strictly more general as a recognition architecture.

The final hard-prefix identity UF23 is proved and independently reviewed
in [NB1--NB3](NONHOMOGENEOUS_BOUNDARY.md). It is not absorbed by these
rewrites. The later [PR168 comparison](LATEST_TRANSPORT_COMPARISON.md)
likewise finds incomparable weighted domains, with no justified transfer
of numerical constants to a union. The older source pin in the theorem
is deliberate; the [source audit](SOURCES.md) records subsequent heads.

**First missing global inference:** neither universal nonhomogeneous
certificate conversion nor absolute summability of the uncovered energy
has been established. The correct local proofs and finite residue
certificate do not supply that inference.
