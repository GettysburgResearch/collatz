# Hamming distance from every nonidentity rotation of an ordinary cycle

**PROPOSED, with a source-qualified logarithmic-form input.** Let a primitive
positive ordinary shortcut Collatz cycle have length L. Every nonidentity
rotation of its parity word must differ in at least

    (ln L - O(ln ln L)) / ln(log_2 3)

positions as L grows. The constants are uniform in the cycle and shift.
The only primitive positive cycle admitting a rotation with exactly two
mismatches is the trivial cycle through 1 and 2. These restrictions apply
to every word arrangement. They leave open cycles with larger rotational
distances and leave divergent trajectories open.

## Setup and elementary estimates

Write x_i for the L distinct positive ordinary phases, b_i for their parity,
q for the number of ones, and m for the least phase. Indices wrap modulo L.
Use the shortcut T(x)=x/2 on evens and T(x)=(3x+1)/2 on odds. A positive
cycle has q>0, and multiplying its individual step ratios gives

    lambda = L ln 2 - q ln 3 = sum_(b_i=1) ln(1+1/(3 x_i)) > 0.
    m <= q/(3 lambda).

The correction product exp(lambda) is at most q+1. Indeed, sort the q
distinct odd phases increasingly; the j-th is at least j, and the product
of 1+1/j from 1 to q telescopes. The argument uses a single primitive tour.

For a fixed shift 0<r<L let d be the Hamming distance between b and its
rotation by r. It is even and positive. If it vanished, the parity schedule
would have period gcd(r,L); the associated repeated affine block has the
same unique fixed point as the whole word, contradicting primitivity.
Let a_i count the ones in b_i,...,b_(i+r-1). Its increments are
a_(i+1)-a_i=b_(i+r)-b_i. There are d/2 increases and d/2 decreases, so
its oscillation is at most d/2. Since its cyclic mean is rq/L, the exact
r-step product bounds every phase ratio by

    x_(i+r)/x_i <= 3^(a_i-rq/L) exp(-r lambda/L) exp(lambda)
                 <= 3^(d/2) (q+1).

Cut at x_0=m. The two aligned starting values x_0 and x_r thus obey

    log_2(1+max(x_0,x_r)) <= Z,
    Z = log_2(1 + m (q+1) 3^(d/2)).

## An elementary exact distance inequality

Put gamma=log_2(3/2) and c=1+gamma=log_2 3. Then

    L <= (Z+1) (c^(d+1)-1)/gamma.                             (1)

To prove this, follow both trajectories from the cut. They are distinct at
every offset because r is a nonidentity shift of a primitive ordinary cycle.
An agreeing run of h parity bits at offset t forces 2^h to divide the
difference of the two states there: the affine difference after that run
is 3^a times their initial difference divided by 2^h, where a is the common
odd count. Thus h is at most the base-two logarithm of the larger current
state plus one (and in fact at most its base-two logarithm). At each step,
T(x)+1 <= (3/2)(x+1), so h <= Z+gamma t.
An agreeing run and its next mismatch therefore advance elapsed time from
t to at most c t + Z + 1. Split the itinerary into d such pieces and the
possibly empty final agreeing run. Iterating this upper bound from t=0
proves (1), including consecutive mismatches.

For L>=2, Proposition 6.3 in Rozier and Terracol, quoting Rhin, gives the
nonzero natural-log form lambda >= L^(-13.3). Its height here is
max(L,q)=L. Thus m <= L^(14.3)/3 and, for example,

    Z <= 1 + 16 log_2 L + (d/2) log_2 3.

If d >= 3 ln L, the stated asymptotic bound already holds since
3 ln(c)>1. Otherwise Z=O(ln L). Taking natural logarithms in (1) then
yields d >= (ln L - O(ln ln L))/ln c. For the first inequality (1),
one may instead use the actual m or the displayed actual lambda directly,
without the imported theorem.

## Peeling a common factor, and the two-mismatch classification

For any length-l binary word u with k ones, write C(u) for its affine
numerator, so the prescribed endpoint is (3^k x+C(u))/2^l.
Composition gives C(uv)=3^ones(v) C(u)+2^|u| C(v). A cycle rotation w
starting at phase x has C(w)=D x with the full D=2^L-3^q>0.

If two distinct phases begin with a common factor f, let u,v be their
complementary words of length L-|f|. Then u and v have the same weight,
and subtraction gives

    D (x_i-x_j) = 2^|f| (C(u)-C(v)).
    D divides C(u)-C(v) != 0.                                (2)

The full D is odd; there is no loss from canceling 2^|f|. For any core
of length l, 0<=C(u)<=3^l-2^l: the all-ones word gives the maximum, as
can be seen by composing the two affine branches on a nonnegative formal
input zero. Consequently D < 3^(L-|f|).

If the rotation has exactly two mismatches, the two complementary agreeing
runs have total length L-2. Their longer length is at least ceil((L-2)/2).
Equation (2) therefore requires

    0 < D < 3^(floor(L/2)+1).                                 (3)

For L>=1024 the imported logarithmic estimate gives
D=2^L(1-exp(-lambda)) >= 2^(L-1) L^(-14). This uses monotonicity and
1-exp(-t)>=t/2 for 0<=t<=1. At L=1024 exact integer comparison gives
(2/sqrt(3))^L > 6 L^14. The ratio of the left side to the right side
increases thereafter, since (1+1/L)^14 <= (1025/1024)^14 < 2/sqrt(3).
These last comparisons can both be checked after squaring and clearing
denominators. Thus D>3^(floor(L/2)+1), contradicting (3).

For 2<=L<1024 the [exact checker](check.py) compares (3) for every weight.
Only periods 2,3,4,5,6,7,8,10,12,13 and 16 survive. For each surviving
length and weight it enumerates *every* parity word by physical iteration
from the representatives 0,...,2^L-1, reconstructs its affine numerator,
and tests the entire D. Each positive integral quotient is physically
replayed. All hits are repetitions or rotations of the trivial (1,2)
cycle. Its primitive parity word does have Hamming distance two from its
one-step rotation.

## Evidence and remaining problem

The checker also tests the phase-ratio and common-factor arithmetic on
finite positive rational realizers. A mixed rational cycle 10/7,5/7,11/7,
20/7 has a rotation with two mismatches. Distinct integer phases and their
dyadic spacing matter in the proof. A rational formal cycle need not meet
the integral spacing in (1) or the divisibility in (2).

The full-period estimates above do not bound the number of mismatches
from above for a candidate cycle. A proof of a conflicting universal upper
bound, or a different obstruction for the large-distance words, remains
missing.

The logarithmic input is an external theorem. We inspected the v5 PDF,
Proposition 6.3 and its displayed specialization to u_0=0, u_1=L, u_2=-q.
We have not independently reconstructed Rhin's Padé proof. PDF SHA-256
`cd1bbb1b6fd659ff36c105cb3a0fb7de727a22c2a7e6c61f864c7e7bb2a21883`.
[O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v5](https://arxiv.org/pdf/2502.00948v5).
For the repository's periodic-word setup see the
[periodic tails packet](../integrated/periodic-tails/README.md), based here
on main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
