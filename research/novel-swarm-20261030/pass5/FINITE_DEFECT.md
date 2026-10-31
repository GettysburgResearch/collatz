# Finite defective edges: a complete automatic normal form

**FD1--FD4: PROPOSED, self-audited; no independent mathematical acceptance.**
Use the shortcut map T(n)=n/2 for even positive n and (3n+1)/2 for odd n.
The hypothesis in this file is exact: f(T(n))=f(n) for every n>=N, for one
fixed integer N>=1. It does not mean small average error, density-one equality,
or an invariance test on finitely many sampled integers.

An automatic function is produced by a finite deterministic automaton with
output (DFAO), reading the canonical most-significant-first base-B digits of
its positive integer input. Outputs may be any finite set. Put K=ceil(N/2).

## FD1. High monochromatic intervals

For every L0 and floor N, an eventually invariant function has a
monochromatic interval of at least L0 consecutive positive integers, lying
above N. Its color need not be known or be the color of the component of 1.

We use the fixed-family merger compiler in PR132, ACS-002/003, reproduced
in pass2/RIGIDITY.md R1, at the exact source pins in README.md. The extra
point here is that all physical edges of its finite certificate can be kept
above N. For clarity, the arithmetic existence argument is reconstructed.

For a chart (3^d y+b,y), d>0, these controlled parity choices give equal-clock
chart transitions:

| Intercept | Choose y | New (d,b) |
|---|---|---|
| Nonzero even b | even; words 0/0 | (d,b/2) |
| Odd b | odd; words 0/1 | (d-1,(b-3^(d-1))/2) |
| b=0 | odd; words 1/1 | (d,(1-3^d)/2) |

The zero case first creates a nonzero intercept. Repeated halving then reaches
an odd intercept and decreases d. At d=0 orient the larger value first and
write its positive gap as g. A nonterminal gap decreases by these rules:

| Gap | Lower-source residue | Upper/lower words | New gap |
|---|---|---|---|
| even | even | 0/0 | g/2 |
| 1 mod 4, g>1 | 1 mod 4 | 01/10 | (3g+1)/4 |
| 3 mod 4 | 2 mod 4 | 10/01 | (3g-1)/4 |
| 1 | 4 mod 8 | 100/001 | 0 |

For nonterminal odd g, the quantity g-1 decreases by at least the factor 3/4.
These are literal affine identities. Each next prescribed parity pulls back
to an additional dyadic input digit because the current numerator's source
coefficient is odd. The construction chooses a subprogression; it does NOT
choose the parity of a previously fixed input.

For finitely many arms h+i, maintain a common refinement and common clock.
Their current forms have slopes that are powers of three. The chart compiler
merges any chosen unequal pair. Refining the same source parameter and
advancing all arms preserves earlier equalities. The number of distinct
forms decreases, so after finitely many stages all arms coincide. Thus there
are r,L,E,q with

    T^L(r+i+2^L h)=E+3^q h,  1<=i<=L0,

on an unbounded positive progression of h. At each of the finitely many
intermediate clocks the state is an affine function of h with positive
slope. Increasing h therefore puts EVERY state on EVERY arm above N. Exact
invariance along these actual high edges proves FD1. No source is assumed to
converge, and no asymptotic stopping-time claim enters.

## FD2. Cone access without crossing the floor

For every positive x with 3 not dividing x, an actual inverse path whose
states all stay >=x reaches arbitrarily large members of every dyadic
leading-digit cone

    C_b = union_{j>=0} [b*2^j,(b+1)*2^j),  b>=1.

At a current ternary unit x choose a in {3,5,7} when x=2 mod3, or in
{4,6,8} when x=1 mod3. All three values make y=(2^a x-1)/3 integral and odd;
exactly one makes y a multiple of three, because the choices cycle through
the relevant three residues modulo nine. Choose either other value. Then

    y>=2x,   3 does not divide y,   T^a(y)=x.

Every physical intermediate state is at least x. The initial x is allowed
to be EVEN: in that case this is a raw shortcut path, not a claimed single
odd-to-odd U edge. Later inverse states are odd.

Iterate to x_j. If A_j is the accumulated sum of a's, then

    log_2 x_j = A_j-j log_2 3+theta_j,
    theta_j=log_2 x_0+sum_{i<j}log_2(1-1/(2^{a_i}x_i)).

Since x_i>=2^i x_0 and a_i>=3, theta_j has a finite limit. The fractional
parts of -j log_2 3 form an irrational rotation; every tail visits the interior
of every nonempty arc. Adding a convergent error preserves that property.
The arcs corresponding to C_b therefore supply arbitrarily large required
visits. Every connecting path stays above its initial source. This is the
high-floor extension of parent R2, not a new discovery of inverse-ladder
logarithmic phase geometry.

## FD3. Exact classification

Let f be B-automatic and invariant on every edge with source >=N.

**Case I: B is not a power of two.** There is one value c such that

    f(n)=c for EVERY n>=K.

The finitely many values at 1<=n<K are unrestricted.

**Case II: B=2^r for an integer r>=1.** There are values c and c_m, one for
each positive odd multiple m of three with m<N, such that, for n>=K,

    f(n)=c_m  if n=2^j m for one of these m and j>=0;
    f(n)=c    otherwise.

Again, the values below K are unrestricted. Only the portion of each dyadic
ray at or above K is assigned c_m; its lower portion may carry arbitrary
individual values.

### Proof

Let the DFAO have D states. Fix L>=2^D and apply FD1 to an interval of length
at least 2B^L, sufficiently high to contain an aligned block
[bB^L,(b+1)B^L), with b>=1. Let s be the state after the digits of b. The
sets S_j of states reachable from s by all suffixes of exactly j digits
evolve under the map S -> union_d delta_d(S). There are at most 2^D subsets.
By time L this sequence is periodic, with some period p>=1. Every state in
S_L outputs a common color c, so f=c on all blocks

    [b B^{L+kp},(b+1)B^{L+kp}),  k>=0.                (1)

If B is not a power of two, log 2/log(B^p) is irrational. The doubling orbit
of every n>=N visits (1), by density of the logarithmic rotation; choose a
large visit so that k>=0. All doubling edges have source >=N. Therefore
f(n)=c for n>=N.

If B=2^r, start with n>=N and 3 not dividing n. FD2 connects n, without
leaving the high region, to x in [b2^j,(b+1)2^j). Choose k large enough that
r(L+kp)>=j, and double x exactly r(L+kp)-j times. This enters (1), so f(n)=c.
If 3 divides n but its odd part m is at least N, halve to m and take its odd
shortcut edge. Its new value (3m+1)/2 is greater than m and a ternary unit.
The same conclusion follows. The only high sources not covered are the
rays with odd m<N and 3|m. Doubling invariance makes each such high ray
monochromatic, with its own possibly different value.

Finally, every n>=K satisfies 2n>=N, so the edge 2n -> n equates its value
to a high doubling lift. This extends the description from n>=N to n>=K,
including the truncated portions of the exceptional rays.

### Sufficiency and sharpness

Every function of the displayed form is invariant on all edges with source
>=N. An even edge preserves odd part. An odd source n>=N is not exceptional,
and its image (3n+1)/2 is a ternary unit, so both values are c. Every image of
a source >=N is at least K; therefore values below K are unconstrained.

The described functions are automatic in the specified bases. A finite
initial table is automatic in every base. In binary, an exceptional ray is
the canonical binary word of m followed by any number of zeros, with a finite
lower truncation; finite unions are regular. Grouping binary digits in blocks
of r, with the shorter first block handled by initial states, gives a base-2^r
automaton. There are only finitely many labels, so output tables suffice.

For example f(n)=1_{oddpart(n)=3} has its only defective Collatz edge at n=3.
It is nonconstant and invariant for every source >=4. Removing the rays
would make the theorem false. Conversely, truncating this ray to a finite
base-three table cannot make it invariant at all later sources; the checker
exports an actual violated edge for that control.

At N=1 the exceptional list and the small region are empty. FD3 recovers
parent R5: every all-base automatic exact Collatz invariant is constant.
The new statement is the finite-defect classification and high-floor proof;
parent global rigidity is explicitly credited.

## FD4. Reversible finite machines cannot hide defects near the origin

If every digit transition of the DFAO is a permutation, eventual Collatz
invariance already forces f constant on ALL positive integers.

On a finite set, the monoid generated by permutations is a group. All states
reachable from the initial state form a single group orbit, and every one
is reachable by a canonical positive word: prepend a positive power of the
nonzero digit 1 whose permutation is the identity. A reachable output color
has a target state. From each reachable state a word of length at most some
fixed L reaches that target. Append such a word to every canonical prefix
of length ell. Distinct prefixes give distinct integers with that color,
all below B^{ell+L}; hence a nonempty color has positive upper natural density.

By FD3 every color different from c is confined to finitely many points and
finitely many dyadic rays, a set with O(log X) members below X. Such a color
has upper density zero, a contradiction. This also removes possible small
exceptions below K. Permutations are essential; the sharp ray/table machines
are not reversible.

## Evidence boundaries

The producer exhausts 7,176 labeled DFAOs in four specified base/state classes
at three floors. Its finite arithmetic-product searches decide each model
on the entire positive integer domain, not on a sampled source interval.
Every accepted model is compared to the normal form by exact automaton
product equivalence. The separate verifier checks the exported positive
closure certificates and negative witnesses, not the entire census again.
Neither those checks nor this manuscript establish any automaticity property
of the actual convergence indicator. No Collatz component is globally
excluded without the finite-state hypothesis.
