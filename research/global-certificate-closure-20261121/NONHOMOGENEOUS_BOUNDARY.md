# The exact remaining debt in a hard certificate language

**PROPOSED elementary identities and an architecture boundary.** This is
part of the attempted global completion, not a claim of nonconvergence.
It keeps the negative offset that a full certificate transformation must
handle. The positive results in this packet do not remove that offset.

The first-one/valuation-three pattern is motivated by PR146 at
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`. PR167 at
`e83cc8b35ad614c616df7c00318cc9645a174c34`,
`research/least-failure-closure-20261121/HOMOGENEOUS_FIVE_TRANSPORT.md`,
already gives the complete homogeneous recognizer and explicit missed
certificates. The stopping grade used below is the existing invariant in
PR150 `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
`research/pointwise-closure-20261120/LOCAL_CERTIFICATE_GRADE.md`, LC-1.
PR157's rank-one examples already rule out uniform target-rank bounds
in terms of source rank alone. No priority for that general obstruction,
the grade invariant, or the complete recognizer is claimed here.

Use the positive shortcut map T and the actual odd map
`U(n)=(3n+1)/2^v2(3n+1)`. A word specifies exact odd exponents. A superscript
on a letter denotes repetitions only when explicitly indicated.

## NB1. An exact affine debt, for every tail endpoint

Suppose the source has an actual positive odd prefix

\[
w=(1,\underbrace{3,\ldots,3}_{m\text{ letters}},b),
\qquad m\ge0,\quad b\ge4,
\]

from x to the positive odd endpoint q. Put

\[
p=m+2,\qquad L=3m+1+b,\qquad h=3m+4.
\]

The exact affine numerator is

\[
3^p x+B=2^Lq,\qquad
B=3^{m+1}+2\sum_{j=0}^m3^{m-j}8^j
 =\frac{3^{m+2}+2\cdot8^{m+1}}5.
\tag{NB1}
\]

The geometric-sum identity follows by multiplying the sum by `8-3=5`;
it holds for every m. In particular

\[
5B=3^p+2^h,
\qquad
\boxed{5x+1=2^h K,\quad
K=\frac{5\,2^{b-3}q-1}{3^p}.}
\tag{NB2}
\]

K is a positive odd integer. Integrality follows from (NB1), since
`3^p` is coprime to `2^h`; its numerator is positive odd. Consequently
`v2(5x+1)=h` exactly. For `0<=t<=h`, the actual shortcut orbit is

\[
T^t(5x)=2^{h-t}3^tK-1.
\tag{NB3}
\]

For `t<h` the input is odd and greater than one, so induction proves
every displayed step. At t=h the endpoint is positive even, also greater
than one. Thus

\[
\boxed{T^{3m+4}(5x)
 =3^{2m+2}(5\,2^{b-3}q-1)-1.}
\tag{NB4}
\]

The first h odd inputs are forced. This does not mean the first h
*accelerated* exponents are all one: the first h-1 are one, while the
h-th may include further even halvings after (NB4). Confusing these two
clocks would lose part of the actual target path.

An arbitrary supplied witness for q does not certify the right side of
(NB4). Neither the factor `3^(2m+2)` nor the negative offset has been
removed. This is the exact missing physical operation, rather than an
unspecified failure of a numerical search.

## NB2. Actual certified sources at every rank in this language

The language is not merely a collection of compatible finite prefixes.
For every m there are infinitely many odd ternary-unit x whose complete
first-hit certificate is exactly w with q=1.

Let p,h be as above, and set c=2 for even h and c=1 for odd h. Choose
the unique odd residue s modulo `2*3^p` such that

\[
5\,2^s\equiv1+c3^p\pmod{3^{p+1}},
\qquad s\ge1.
\tag{NB5}
\]

Such a residue exists because two generates the units modulo every
power of three. An elementary proof uses
`v3(4^(3^j)-1)=j+1`, obtained by cubing, together with `2=-1 mod3`.
The congruence modulo three forces s odd. Every positive representative
of this class is allowed. Put

\[
b=s+3,\qquad
K=(5\,2^s-1)/3^p,\qquad x=(2^hK-1)/5.
\tag{NB6}
\]

Equivalently, x is the integer `(2^L-B)/3^p` in (NB1). The latter
formula proves its integrality and oddness; the former gives `5x+1=2^hK`.
The original inverse word is integral at every intermediate division:
reduce its full numerator modulo three, divide, and repeat. The last
inverse `I_b(1)` exceeds one because b>=4, and every remaining integral
inverse is positive odd and cannot be one. Hence w is its actual
first-hit word, of rank p. The construction is entirely in positive
ordinary integers.

By (NB5), K=c modulo three. Our choice gives `2^hK=2 mod3`, and hence
`x=2 mod3`. The sources therefore satisfy the physical-five domain.
Increasing s through its period gives infinitely many distinct sources
at each rank p>=2. Their fivefold targets require at least `3p-2` odd
inputs before any possible first arrival at one. No assertion of such
an eventual arrival is made.

## NB3. No complete homogeneous compilation, even with terminal padding

For a convergent positive n let `g(n)=d(n)-2o(n)`, where d is its first
shortcut hitting clock and o its odd count. Padding with the cycle at one
leaves g unchanged. The elementary bound

\[
2^{g(n)}\le n
\tag{NB7}
\]

follows from the product identity
`2^d=n product(3+1/n_i)` over the odd inputs before the first hit.
Those odd inputs are at least three, so every factor is at most `10/3<4`.
If there are no odd inputs, n is a power of two and equality holds.

Take any source in NB2. If 5x converges, let E be the endpoint in (NB4).
The first h clocks all have odd input, so

\[
g(5x)=-h+g(E),\qquad g(x)=L-2p=m+b-3.
\]

By (NB4) with q=1 and (NB7),

\[
\boxed{
2^{g(5x)-g(x)}
\le\frac{E}{2^{h+g(x)}}
<\frac{45}{16}\left(\frac9{16}\right)^m<4.}
\tag{NB8}
\]

Thus `g(5x)-g(x)<2`. A homogeneous complete transport from x to 1
and from 5x to 5, with equal odd count and equal clock on both arms,
would instead give `g(5x)-g(x)=g(5)-g(1)=2`. This contradiction rules
it out. If 5x does not converge, no word to 5 exists either.

Therefore **every NB2 source is outside complete homogeneous compilation
from the terminal base 1**, even if arbitrary terminal cycles are appended
to its source certificate. This includes every consuming compiler made
only of homogeneous blocks and the final edge `5->1`, not just the
particular dictionaries in this packet. The conclusion is specific to
that architecture. Other terminal families, different clocks, different
odd counts, or a valid guarded induction remain possible.

## Completion status

The new unbounded first-one blocks in this packet are positive exact
transports, and their enlarged renewal domain has strict contraction.
NB1--NB3 show why those statements do not complete the hard language:
the target needs a different certificate resource pattern, and its
remaining shifted value has no certificate here. The arbitrary-tail
reverse descent separately handles a large final valuation; it does not
apply to every such residual. A proof of universal success for a
nonhomogeneous transformation, or an absolute bound on the uncovered
energy, is still missing.

`check_nonhomogeneous_boundary.py` checks the affine identity and actual
forced steps for varied positive odd endpoints, constructs actual
first-hit sources at ranks 2 through 10, and checks the exact rational
inequality behind (NB8). The formulas and elementary order argument prove
the infinite statements; the finite replay does not decide Collatz.
