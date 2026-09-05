# Route 3: a computable infinite dictionary and a common integer rank

**Status: PROPOSED pending independent mathematical review.** These are positive
partial ranking results, not a global Collatz proof. The rank has explicit
ordinary counterexamples to global monotonicity. Its mode-switching problem
remains open. No earlier obstruction or accepted status is changed.

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n. All sources in
this note are positive ordinary integers. The absorbing value is 1.

## 1. T-A3-901: maximal repetition is an exact, total arithmetic operation

For each integer a>=0 put

    j_a=a+1, P_a=2^(a+1), Q_a=3^a,
    d_a=Q_a-P_a, c_a=Q_a-2^a,
    z_a(n)=d_a*n+c_a=3^a(n+1)-2^a(2n+1).

The word w_a=1^a0 has the affine map

    g_a(n)=(Q_a*n+c_a)/P_a,
    z_a(g_a(n))=(Q_a/P_a)z_a(n).                         (1)

For a=0,1 the fixed points are respectively 0,1. For a>=2 the fixed point
-c_a/d_a is negative, with 1<c_a/d_a<=5. The coefficient d_a is always odd and
is never zero. The rational fixed point is only an algebraic center; no
positive ordinary infinite realization is inferred from it.

For n>1 define its active mode and maximal repetition count by

    a(n)=0 if n is even; a(n)=v2(n+1) if n is odd,
    k(n)=floor(v2(z_(a(n))(n))/(a(n)+1)).                (2)

Here z is nonzero: the only positive integer zero in the dictionary is
z_1(1)=0, already absorbed. Define

    A(n)=g_(a(n))^k(n)(n), n>1; A(1)=1.                 (3)

Then k(n)>=1. The map A follows exactly k(n) copies of the physical word
w_(a(n)), and the next such copy is illegal. In particular A is defined for
every positive ordinary source without an unknown stopping-time oracle.
Except at 1, successive A-mode labels differ.

### Proof of exactness

A finite shortcut parity word of length L specifies one residue modulo 2^L.
This follows inductively because its odd numerator multiplier makes the two
lifts of a residue have opposite next parities. The fixed point of g_a has
period w_a: for a>=1 its shifted value alpha+1=-2^a/d_a has exact dyadic
valuation a, and after a odd steps the state is 2*alpha, which is even with
valuation one. The cases a=0,1 also follow directly.

Consequently n realizes w_a^k if and only if

    2^((a+1)k) divides z_a(n).                          (4)

The active mode in (2) ensures one legal copy, so (4) proves the exact maximum.
The endpoint is an ordinary positive integer and can be evaluated without
iterating every step:

    z_a(A(n))=Q_a^k * (z_a(n)/P_a^k),
    A(n)=(z_a(A(n))-c_a)/d_a.                           (5)

Its remaining dyadic valuation of z_a is less than j_a. If its active mode
were still a, another copy would be legal, a contradiction. Even mode 0 ends
at an odd number. Mode 1 is numerically contracting toward 1 but cannot cross
1 from a larger positive source. Modes a>=2 are numerically expanding at
block endpoints and never hit 1 internally. Thus killing on 1 at module
boundaries misses no visit to 1, and convergence for A is equivalent to
convergence for T.

### A uniform clock, including arbitrary modes

Write L(n)=j_a*k(n). For every n>1,

    L(n) <= 3 log_2(n+5),
    A(n)+5 <= (n+5)^3.                                 (6)

For a>=2, 0<z_a(n)<3^a(n+1), a<=log_2(n+1), and log_2 3<5/3. Therefore
L<=log_2 z_a<(8/3)log_2(n+1). Moreover with rho=Q_a/P_a,
A(n)+5<=rho^k(n+5), and rho^k<=(3/2)^L. The exact inequality 3^5<2^8 gives
log_2(3/2)<3/5, so A(n)+5<=(n+5)^(13/5)<=(n+5)^3.
Modes 0 and 1 shrink numerically and have L<=log_2(n) or log_2(n-1).
This proves (6), without a bound on a or k.

After J completed modules before absorption, their total shortcut duration is
at most (3/2)(3^J-1)log_2(n+5). Thus an infinite ordinary orbit must switch
modes infinitely often. This counts maximal periodic corridors, not individual
odd/even runs; a corridor may contain arbitrarily many such runs. The clock
alone says nothing about the sign of progress across those switches.

## 2. T-A3-902: the infinite envelope is computable from at most four entries

Define a nonnegative integer component rank

    R_a(n)=z_a(n)^2 / 3^v3(z_a(n)),

with R_a(n)=0 when z_a(n)=0. Let

    R_*(n)=min_(a>=0) R_a(n).                           (7)

Although (7) uses infinitely many polynomials, it has the exact finite formula

    h=v3(2n+1),
    R_*(n)=min(R_0(n),R_1(n),R_2(n),R_h(n)) if h>=3;
    R_*(n)=min(R_0(n),R_1(n),R_2(n)) if h<3.             (8)

The fourth index is INPUT-DEPENDENT and unbounded. This is not a fixed finite
polynomial-valuation dictionary of the class excluded in pass 3.

Also

    R_*(1)=0,
    n-1 <= R_*(n) <= n^2 for n>=2.                      (9)

In particular it is a proper positive integer rank away from the core.

### Proof of collapse

For a>=2, z_a(n)>0 and

    z_(a+1)(n)=3z_a(n)+2^a(2n+1)>3z_a(n).               (10)

Put t=v3(n+1). Since gcd(n+1,2n+1)=1, h and t cannot both be positive.
Unless a+t=h, exact valuation of the two summands gives

    v3(z_a(n))=min(a+t,h).                              (11)

If h<=1, every a>=2 has the same denominator 3^h, so (10) makes the minimum
in that range occur at 2. If h=2, the possibly higher valuation at a=2 only
lowers R_2 further, and every a>2 has valuation 2 and a larger numerator.

If h>=3, then t=0 and v3(z_2)=2. For 2<a<h, equations (10)-(11) give
R_a/R_2>3^(a-2)>1. For a>h they give R_a/R_2>3^(2a-h-2)>1. Only a=h can
therefore beat R_2. This proves (8), including the exceptional cancellation
at that one index rather than dropping it.

For any nonzero integer z, z^2/3^v3(z)>=|z|. Now |z_0(n)|=n,
|z_1(n)|=n-1, and z_a(n)>=n+5 for a>=2. The choice R_0<=n^2 gives (9).

## 3. T-A3-903: common-rank decrease on an unbounded moving-index family

On any legal w_a^k, (1) gives the exact rank identity

    R_a(g_a^k(n)) = [3^a/4^(a+1)]^k R_a(n).             (12)

This contracts by at least a factor 1/4 per block, even though g_a expands
ordinary size for every a>=2. If the active component attains the envelope,

    R_(a(n))(n)=R_*(n),                                 (13)

then

    R_*(A(n)) <= [3^a/4^(a+1)]^k R_*(n) <= R_*(n)/4.   (14)

The same R_* is used before and after every such certificate; different local
rankings are not being composed without a common order.

Here is a nonvacuous all-parameter theorem. For EVERY a>=2, k>=1 and t>=2a+4,
there are infinitely many ordinary positive n with

    v2(z_a(n))=(a+1)k, v3(z_a(n))=t.                    (15)

Every one of these sources has active mode a, v3(2n+1)=a, maximal count k,
and a UNIQUE minimizing index a in (7). Its endpoint grows numerically but
has strictly less than a quarter of its initial R_*.

To construct the progression, impose

    z_a(n)=2^((a+1)k) mod 2^((a+1)k+1),
    z_a(n)=3^t mod 3^(t+1).                             (16)

The coefficient d_a is a unit modulo both powers, so ordinary CRT applies.
Positive members form an infinite progression; a different n for each finite
parameter choice is not asserted to be one all-time source.

For minimality, near the rational zero of z_a, the high ternary precision
forces v3(n)=0, v3(n-1)=1, and v3(2n+1)=a. If a>=3 it also forces
v3(n+5)=2. The three other possible envelope entries are then at least
n^2, n^2/12, and n^2/9 respectively (n>=2). Meanwhile

    R_a(n) < 4*3^(2a-t)n^2 <= (4/81)n^2 < n^2/12.

For a=2 the third entry is R_a itself. The collapse proof excludes every
other a>=3 strictly. This proves unique minimality and (14).

Thus no fixed truncation of the component-rank dictionary computes R_* on
all positive inputs: arbitrarily large a are unique minimizers on (16).
For example, one certificate is

    a=2, k=1, t=8,
    n=577363 -> A(n)=649534,
    R_*(n)=50808384 -> R_*(A(n))=7144929.

The ordinary number increases; the SAME integer rank decreases by 9/64.
The checker covers 88 parameter triples, but (15)-(16) prove every triple.

## 4. The indispensable failure boundary

R_* is NOT globally decreasing. Exact ordinary counterexamples include

    7 -> A(7)=13, R_*: 12 -> 36;
    9 -> A(9)=7,  R_*:  9 -> 12;
    3 -> A(3)=4,  R_*:  3 -> 3.

The favorable family in (15) actually illustrates the remaining difficulty:
after its maximal exit the active mode changes, while the old index a still
uniquely minimizes the rank. So the next state is generally not aligned with
its new active mode. The family cannot be iterated for free.

A larger, computable safe region is

    G={n>1: 4R_*(A(n))<=R_*(n)}.                        (17)

It contains (13) and other inputs, including direct arrivals at 1. Membership
uses the explicit total map (5), not an unproved search for a future rank drop.
All consecutive visits to G end at 1 or outside G in a bounded number of
modules; the precise clock and integrated bound are in RENEWAL_MASS.md.
The unsafe return process, or a complete lower-rank merging cover from
RESONANT_SOURCE_FAN.md, is the actual unresolved full-closure obligation.
