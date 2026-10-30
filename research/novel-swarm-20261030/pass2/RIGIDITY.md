# Finite-dimensional and all-base automatic invariant rigidity

**PROPOSED; self-audited, not independently reviewed or formally verified.**
This is a new written reconstruction, not a recovery of the unavailable first
swarm's artifacts. No external priority claim is made. The supplied proofs do
not assume that all positive Collatz trajectories converge.

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n. An
**invariant** is a function f on positive integers satisfying f(T(n))=f(n).
In particular f(2n)=f(n). The domain is the original integer source, not time
along one trajectory. Nothing below excludes a finite-state *parity itinerary*
by silently applying a theorem about a source-indexed invariant.

## R1. Finite monochromatic intervals, with a constructive arithmetic proof

For every positive K there are integers r>=0, L>=0, q>=0, E>0 and K legal
length-L parity words such that, for every h>=0 and 1<=i<=K,

    T^L(r+i+2^L h) = E+3^q h.                         (1)

Thus every invariant has monochromatic intervals of arbitrarily large finite
length. The color and component may depend on K. No endpoint in (1) is assumed
to converge to 1.

This is a specialization of the finite-family compiler in PR #132, ACS-002/003,
not a new assertion of finite-family merger existence. Here is the arithmetic
needed independently of that manuscript's other results.

At a pair (3^d y+b,y), d>0, select the following parities on y:

| Condition | Selected y parity | Upper/lower words | New (d,b) |
|---|---|---|---|
| b even and nonzero | even | 0 / 0 | (d,b/2) |
| b odd | odd | 0 / 1 | (d-1,(b-3^(d-1))/2) |
| b=0 | odd | 1 / 1 | (d,(1-3^d)/2) |

The zero case creates a nonzero intercept. Halve even nonzero intercepts until
odd, then reduce d. This terminates at d=0. For a nonzero constant gap g,
orient the larger value first. The following guards finish the construction:

| Gap | Lower-source guard | Upper/lower words | New gap |
|---|---|---|---|
| even | even | 0 / 0 | g/2 |
| 1 mod 4, g>1 | 1 mod 4 | 01 / 10 | (3g+1)/4 |
| 3 mod 4 | 2 mod 4 | 10 / 01 | (3g-1)/4 |
| 1 | 4 mod 8 | 100 / 001 | 0 |

For b<0 swap source labels before and after the gap calculation. Every
nonterminal stage reduces g-1 by a factor at most 3/4. These are literal affine
identities, including their guards, not choices available to a fixed input.

Every successive parity choice pulls back to exactly one additional dyadic
source digit: after j shortcut steps the current coefficient is an odd integer
divided by 2^j. The compiler therefore gives one nonempty dyadic cylinder and
two equal-length words merging each chart. Direct word composition gives

    3^(q_upper) 3^d = 3^(q_lower),
    3^(q_upper) b + C_upper = C_lower,

where 2^L T_w(x)=3^(#ones(w)) x+C_w.

To merge a finite collection, maintain forms 3^(q_i) h+B_i after a common
clock and source refinement. Choose two unequal forms; orient their slopes so
q_upper>=q_lower and use the chart just proved. Its lower-coordinate guard
pulls back through an odd coefficient to a dyadic guard on h. Apply that same
source refinement and the same number of actual shortcut steps to every arm.
Previously equal forms stay equal and the selected two become equal. The
number of distinct forms strictly decreases. Starting with h+i, i=1,...,K,
proves (1). All starting values and all actual intermediate values are positive.

## R2. Every component reaches every dyadic leading-digit interval

For every positive source n and positive integer b, some integer in n's
undirected Collatz component lies in

    C_b = union_(k>=0) [b 2^k,(b+1)2^k) intersect Z.   (2)

Moreover there are arbitrarily large such integers. Only actual finite
forward/inverse paths are used.

First move n to an odd value v. If 3 divides v, replace v by its next odd
iterate; that result is a unit modulo three. Starting with x_0=v, construct
positive odd inverse states

    x_(j+1) = (2^(a_j) x_j - 1)/3.

When x_j=2 mod3 choose a_j from {3,5,7}; when x_j=1 mod3 choose it from
{4,6,8}. All three choices give integers; their numerators cycle through the
three relevant residues modulo nine. Exactly one gives a multiple of three
as quotient. Choose either of the other two. Hence each x_j stays an odd
ternary unit, U(x_(j+1))=x_j with the specified exact valuation, and
x_(j+1)>=2x_j. This is a constructive inverse ladder.

Let c=log_2(3), A_j=sum_(i<j) a_i. Then

    log_2 x_j = A_j - jc + theta_j,
    theta_j = log_2 v + sum_(i<j) log_2(1-1/(2^(a_i)x_i)).

The correction series converges absolutely, since a_i>=3 and x_i>=2^i v.
Thus modulo one, log_2 x_j is the irrational rotation -jc plus a convergent
perturbation. Irrationality follows from 2^u != 3^v for positive integers u,v.
Every tail of an irrational rotation is dense, and a perturbation tending to
zero retains visits to the interior of every nonempty interval. Consequently
these inverse states visit the logarithmic interval corresponding to (2), at
arbitrarily large heights. This proves R2.

The project already studies residue-locked inverse ladders and logarithmic
phase geometry in PR #137. This short proof supplies the precise cone-access
statement required here; it does not claim discovery of that general method.

## R3. A finite-dimensional zero block propagates through an entire cone

Let g(n)=u M_(b_l)...M_(b_0) v be a D-dimensional linear representation over
an arbitrary field, using the canonical most-significant-first binary digits
of n. Suppose g(2n)=g(n) for all positive n. If g is zero on

    [b 2^L,(b+1)2^L) intersect Z,

with b>=1 and L>=D-1, then it is zero on the entire cone C_b.

Put r=u M_(digits of b). For every word w of length at most L, append enough
zero digits to reach length L. Repeated doubling invariance then gives
r M_w v=0. Define

    V_j = span{M_w v : |w|<=j}.

The increasing sequence satisfies
V_(j+1)=V_j+M_0 V_j+M_1 V_j. Once it stabilizes it is stable forever. If v!=0,
it starts with dimension one and therefore V_(D-1) is the full reachable
column space; if v=0 the conclusion is immediate. The row r annihilates that
space, hence every suffix word, proving the claim. No spectral radius,
positivity of matrices, characteristic-zero assumption, or leading-zero
convention is needed.

The D-1 observation length cannot be reduced for this linear-algebra lemma
alone: take M_0=I, M_1 the nilpotent shift e_j -> e_(j+1), v=e_1, r=e_D^T.
Words of length at most D-2 vanish, while the all-one word of length D-1 does
not. This control concerns the lemma, not a Collatz invariant.

## R4. Binary finite-dimensional invariants are constant

**Theorem.** Every Collatz invariant admitting a finite-dimensional binary
linear representation over a field is constant on the positive integers.

Let its dimension be d>=1. By R1 there is a monochromatic interval of length
2^(d+1), with value c. Every interval of that length contains an aligned block
[b 2^d,(b+1)2^d) with b>=1. Subtracting the constant c gives a representation
of f-c of dimension at most d+1. R3 makes f=c on C_b. R2 connects every source
to C_b by actual Collatz edges, so invariance gives f(n)=c for all n>0.

In particular, finite-rank binary linear representations cannot distinguish
positive components. This includes finite binary-kernel span whenever it is
expressed by its usual digit-transition representation; the theorem is stated
in the explicit matrix form so that no convention about regular sequences is
required. Reversing a digit-reading convention transposes matrices and reverses
products and gives the same class of scalar representations.

This proof can also refute a specified nonconstant representation over an
effectively computable field: either doubling invariance fails (decidable by
finite-dimensional equivalence), a finite merger path from R1 violates
invariance, or an R2 ladder from a differently colored source reaches the
constant cone and exposes a violated edge. The last search is guaranteed to
terminate by R2 but no practical uniform running-time bound is claimed.

## R5. Automatic invariants in every integer base are constant

**Theorem.** For every integer B>=2, a finite-valued B-automatic Collatz
invariant is constant on positive integers.

Take a most-significant-first DFAO with D states. By R1 choose a monochromatic
interval long enough to contain an aligned base-B block
[b B^L,(b+1)B^L), b>=1, L>=2^D. A length 2 B^L interval suffices. Let s be the
state after reading the canonical digits of b. The subsets

    S_j = {delta(s,w): w has length j}

evolve by one deterministic map on at most 2^D subsets. Thus by time L they
are on a periodic orbit, of some period p>=1. All states in S_L output the
same color c; so the same is true on every block

    [b B^(L+kp),(b+1)B^(L+kp)), k>=0.                  (3)

If B is not a power of two, log(2)/log(B^p) is irrational. The doubling orbit
n 2^a of any positive n therefore visits (3), by irrational rotation on the
logarithmic circle of circumference p log B. Taking a sufficiently large
visit ensures k>=0. Doubling preserves the invariant, so f(n)=c.

If B=2^r, R2 first provides a component member
x in [b 2^j,(b+1)2^j). Choose k sufficiently large that r(L+kp)>=j and double
x exactly r(L+kp)-j times. The result belongs to (3) and stays in the same
component. Again f(n)=c. These two cases cover every integer base.

## R6. Algebraic generating-function consequence

Let F be a finite field of characteristic p and let f:N->F satisfy the
Collatz invariant equation for positive n; f(0) is unconstrained. The
Christol--Kamae--Mendes France--Rauzy theorem identifies algebraic power series
over F(z) with automatic coefficient sequences in characteristic p. R5 gives

    sum_(n>=0) f(n) z^n is algebraic over F(z)
      iff f(n)=c for every n>0
      iff the series is f(0)+c z/(1-z).               (4)

The external theorem is used only for this corollary. Reference: G. Christol,
T. Kamae, M. Mendes France, G. Rauzy, *Suites algebriques, automates et
substitutions*, Bull. Soc. Math. France 108 (1980), 401--419, Theorem 1,
Section 5, p.406; DOI 10.24033/bsmf.1926.
Primary article: https://www.numdam.org/article/BSMF_1980__108__401_0.pdf .
The parsed theorem and the reading-direction discussion on p.406 were checked;
the web PDF screenshot attempt failed, so no visual-page verification is claimed.

For example, the actual convergence indicator 1_{n reaches 1} is invariant.
If Collatz is false, that indicator must have infinite binary linear rank, must
be nonautomatic in every integer base, and its series over every finite field
must be transcendental. Conversely, establishing any one of the relevant
finite-complexity hypotheses would prove Collatz. **No such hypothesis has
been proved for the actual indicator.** This is a rigorous complexity
obstruction and a conditional route, not a resolution.

## Evidence and boundaries

The checker constructs and verifies whole-progression certificates for K=1
through 128; independently replays chart lifts and inverse ladders; exhausts
specified small DFAO classes; and checks finite-field observability examples.
Those tests are implementation evidence, not substitutes for the proofs above.
They do not establish automaticity, algebraicity, finite rank, or convergence
for arbitrary sources. Neither an external novelty audit nor independent
mathematical acceptance is claimed.
