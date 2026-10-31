# Whole-integer-domain certificates for finite quotient models

**EC1--EC3: PROPOSED, self-audited.** The finite graph is an exact decision
procedure for a SUPPLIED finite-state model. It is not a finite-state model
of all Collatz trajectories, nor a universal convergence test.

## EC1. Two affine relations decide all high Collatz edges

Let f be produced by a base-B DFAO with S states. For a fixed N>=1, the
identities f(T(n))=f(n) for every n>=N are equivalent to

    f(2u)=f(u)       for every u>=ceil(N/2),
    f(3u+1)=f(u)     for every odd u>=N.               (1)

Necessity uses the even edge 2u -> u, then the two edges
u -> (3u+1)/2 <- 3u+1. Both sources of the latter comparison are >=N.
For sufficiency, the first relation converts the second into the required
odd edge. If a relation fails, it supplies an actual violated T edge: 2u
for the first, and either u or 3u+1 for the second. The executable reads
both output values to choose that actual source; it never reports only a
failure of a nonphysical symbolic relation.

### A most-significant-first carry graph

Consider f(mu+c)=f(u), with m=2,c=0 or m=3,c=1, subject to a lower threshold
h and, for the second relation, odd u. Pad the input word with leading zeros
so that it has the same length as the canonical output word for mu+c. The
output's first digit must be nonzero. Canonical input evaluation starts at
its first nonzero digit, not at the padding zeros.

If d is the next input digit and e the output digit, upper carry a and lower
carry b satisfy

    e = m*d+b-B*a,  0<=a,b<=m.                        (2)

Read from the most significant side, starting with upper carry 0, and require
terminal carry c. The admissible carry range contains every ordinary
multiplication/addition carry: the bottom carry is c<=m, and the recurrence
cannot exceed m. Conversely, summing (2) with place values shows that every
accepted path satisfies output=mu+c exactly.

A product state consists of: input DFAO state, output DFAO state, current
carry, input parity, and min(current input prefix,h). A special state -1 on
each DFAO side means that the canonical representation has not yet started.
Once started, leading-zero suppression stops. Reading d updates parity to
(B*parity+d) mod2 and the threshold counter to min(h,B*cap+d).

Accept only when the input is positive, cap=h, terminal carry=c, and the
parity guard holds. A differing output label is a violating input. Starting
from (-1,-1,0,0,0), breadth-first search either finds such a path or exhausts
a FINITE graph. Exhaustion checks (1) for every integer, not just inputs
whose digits appeared in a numerical sample.

There are at most

    D = 8*(S+1)^2*(N+1)                              (3)

states in either search: at most four carries, two parity values and
N+1 capped prefixes. A shortest violating path has fewer than D transitions;
its output word represents the actual source 2u or 3u+1, or bounds u above.
Thus every failure has an actual violated T edge at a source

    n < B^D.                                        (4)

This deliberately loose bound is different from parent pass3's sharper
4d-dimensional LINEAR observability bound. Here S is the number of finite
states AFTER specialization, and can grow exponentially with the number
of polynomial variables. The search is polynomial in S, N and B, not in
log N, polynomial degree or the input description length. No useful bound
on a separating finite quotient for arbitrary commutative coefficients is
claimed.

### Exported certificates

A positive certificate lists a finite set containing the initial state,
closed under every allowed digit/carry transition, with no unequal-label
accepting state. Closure of an over-approximation suffices; minimality and
BFS order are not required. A negative certificate gives a literal positive
source, its raw shortcut image and unequal labels, with the optional
arithmetic digit path explaining how it was found.

The producer enumerates the lower carry in (2). The standalone verifier
instead enumerates both digits d,e and solves for the unique lower carry.
It reconstructs raw T edges directly. It imports neither producer code nor
repository kernels. This is implementation diversity by the same author,
not independent mathematical peer review.

## EC2. Sound finite specialization, and its one-way boundary

For a rational polynomial machine, all coefficients and initial coordinates
lie in Z[1/D0] for a finite integer D0. Select a prime p not dividing D0.
The reduced machine is finite, with at most p^d states. Every modular
violated edge proves a rational violated edge, because exact equality over
Z[1/D0] would survive reduction.

To ensure that a violation exists, preserve a specified nonzero difference
of rational outputs: also avoid the numerator of that difference. Under a
global-invariance target any unequal pair suffices, by AR2. For invariance
above N, the pair must violate the normal form in AR3; an unequal pair on
two permissible exceptional rays need NOT produce a high violation. For
polynomial automorphisms any unequal pair suffices, by AR4.

A constant or invariant quotient is NOT a positive certificate of rational
invariance. The control f(n)=2n reduces to zero modulo 2, but its rational
edge 2 -> 1 has values 4 and 2. The complete finite graph properly accepts
the quotient and the report retains the rational violation. Likewise,
nilpotents may require finite rings rather than fields for separation.

For explicitly given rational coefficients, primes preserving a supplied
unequal pair can be found by exact arithmetic. For arbitrary abstract
commutative rings, AR1 is an existence theorem; no uniform effective
representation of the ring or quotient-search algorithm is assumed.

## EC3. Delayed polynomial defects, without scanning the source interval

Take one rational state x, initial value 0, every digit update x -> x+1,
and polynomial output

    H(x)=binom(x,K)=x(x-1)...(x-K+1)/K!.

The state equals the digit length. With B=2 and K=512, use prime 521,
which does not divide K!. The graph finds the literal violated edge

    n=2^511,   T(n)=2^510,   f(n)=1,   f(T(n))=0.

The producer retains 3,575 visited product states, rather than enumerating
the 154-decimal-digit source interval. This is an example of an effective
refuter, not a hard-to-verify new Collatz trajectory: the final witness
itself is an elementary even edge. Smaller binary K=64 and ternary K=128
controls test the same implementation under different bases and primes.

The other nonlinear checks include x -> x^2+d, coupled quadratic updates,
and reversible Henon maps (x,y) -> (y,x+y^2+d). Their inverse is
(u,v) -> (v-u^2-d,u), so reduction really does preserve reversibility.
The latter models are tested at floor N=32, not merely globally.

## Actual finite coverage

The producer exhausts all labeled binary-output DFAOs with initial state 0
in these classes: (base,states)=(2,2),(3,2),(4,2),(2,3). This is 7,176 models.
Each is checked at floors 1,4,8, giving 21,528 whole-domain graph decisions.
For every accepted model, a separate automaton-product traversal checks
exact equality to its classified normal form on all canonical positive words.

Seven selected DFAO certificates, 33 polynomial quotient models, a bad-prime
control and a nilpotent control are exported. The standalone verifier
reconstructs those certificates, but does not independently re-enumerate the
full 7,176-model census. Its mutation suite tests thirteen direct semantic,
type, closure and duplicate-JSON failures, not independently resealed
full-corpus mutations. Precise final counts and hashes are in the receipt.

No bound here applies directly to the unknown convergence indicator without
a supplied finite model. Finding a large counterexample to a guessed model
is not finding a counterexample to Collatz.
