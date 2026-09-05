# Route 2 continuation — actual SC tails and complete return continuations

**Status: PROPOSED pending independent mathematical review.** No proof of SC*,
no exclusion of every positive cycle, and no all-word return obstruction is
claimed. The new bridge is a separately proved local statement; it does not
promote or overwrite the repository's source-qualified SC*/FC* synthesis.

## 1. T-A3-451 — every infinite orbit contains an actual all-supercritical tail

For the shortcut T, let C_k(n)=3^(q_k(n))/2^k and C_0=1. The orbitwise Mellin
argument in [ORBIT_MELLIN.md](ORBIT_MELLIN.md), Section 4, proves

    an infinite positive orbit implies C_k(n) -> infinity.

Thus the sequence C_k(n) attains its global minimum at some finite index r.
For y=T^r(n), coefficient concatenation gives

    C_t(y)=C_(r+t)(n)/C_r(n) >= 1 for every t>=0.          (1)

This is one actual positive integer on the original orbit, not changing
finite-depth representatives. The source need not be the value minimum and
r is not claimed effectively bounded.

### Exact qualitative closure split

The following are equivalent:

    SC*: every positive integer has a coefficient-subcritical prefix;
    every positive orbit is eventually periodic.                         (2)

For the forward implication, an infinite orbit would give y in (1), violating
SC*. Conversely, a positive periodic tail has period coefficient c<1:
its exact product formula is 1=c product_odd(1+1/(3x)), and a positive cycle
must have an odd state. After a fixed preperiod, repeated periods multiply
the source coefficient by powers of c. Eventually it is below one.

Consequently the following complete-proof target is sufficient:

    SC* + no nontrivial positive integer cycle => Collatz.                (3)

This avoids demanding that every first-crossing non-descent word be impossible.
The new implication is a reduction, not a solution of either remaining premise.
Nontrivial cycles cannot be dropped from (3): they satisfy SC* themselves.

The older PR #80 L-6503 establishes a ladder of value minima whose finite
coefficient-stopping depths tend to infinity, explicitly without an actual
infinite coefficient-stopping source. Equation (1) supplies that stronger
source conclusion via the finite correction product. Its qualitative
coefficient-escape input has prior literature discussion and is not claimed
novel; the exact source-pinned distinction is in SOURCES_AND_REVIEW.md.

## 2. L-A3-452 — the extracted source is close to a value minimum

Start an infinite orbit at its attained value minimum n, and choose r as above.
Since C_r<=C_0=1, the explicit product estimate gives

    n <= y=T^r(n) <= n exp((160/3)n^(-1/40)).              (4)

In particular, the displacement from the value minimum to an actual SC-infinite
source is at most

    n [exp((160/3)n^(-1/40))-1] = O(n^(39/40)).            (5)

For n>=(160/3)^40, the elementary inequality exp(u)-1<=2u for 0<=u<=1 gives
the explicit upper bound (320/3)n^(39/40). This threshold is enormous; it is
not advertised as a practical verified floor. The improved invariant-set
exponent gives O(n^(19/20)) with non-explicit uniform constants.

This is a bound on the **location** of an extracted ordinary source. It says
nothing about how many steps are needed to reach it. It therefore does not
prove the moving stopping-time box in the existing cofinal-envelope program.

For an all-supercritical source n, the affine formula keeps its orbit above n.
The period argument in Section 1 rules out eventual periodicity, so the orbit
is infinite (the resident IC-SC-001 already proves full divergence). In the affine formula
2^k x_k=3^(q_k)n+A_k,

    0 <= A_k/3^(q_k)
       = n(P_k-1)
       <= n[exp((160/3)n^(-1/40))-1]                     (6)

for every k. This is a uniformly bounded real normalized correction, at one
fixed source. It must not be confused with its different 2-adic limiting sum;
no integrality contradiction follows from identifying the two completions.

## 3. T-A3-453 — every finite continuation is one interval and one CRT class

Let w be a first coefficient-crossing shortcut word of length j, weight q and
affine constant A. Put P=2^j, Q=3^q, D=P-Q>0. For a formal non-descent write

    r=(A-Pd)/D, y=r+d=(A-Qd)/D,
    d integer, 0<=d<A/P.                                (7)

The case d=0 remains present. For an ordinary source, integrality is exactly

    d = A P^(-1) mod D.                                 (8)

For D=1 this is the unrestricted congruence. Since P and D are coprime, the
inverse exists for every other D. This is the whole denominator, not one of
its prime factors.

Take any continuation word u of length t with affine data (P_u,Q_u,A_u),
P_u=2^t, Q_u=3^(weight u). Let b_u be its canonical source residue modulo P_u.
The endpoint y realizes u exactly when

    d = Q^(-1)(A-D b_u) mod P_u.                         (9)

Indeed D and Q are odd, so (9) is precisely (A-Qd)/D=b_u mod P_u. The original
word w is also realized whenever (7) is an ordinary integer: modulo P,
Q r+A=0, and shortcut parity-cylinder bijectivity applies.

At the end of u, ordinary no descent relative to r is equivalent to

    (P P_u-Q Q_u)d >= (P_u-Q_u)A-D A_u.                  (10)

Derive this by multiplying T_u(y)-r by the positive number D P_u.
There is **no assumption that P P_u-Q Q_u is positive**. A positive coefficient
gives a lower bound on d, a negative coefficient gives an upper bound, and a
zero coefficient gives a tautology or an empty set according to its right side.
Use (10) at every prefix of u to require no intermediate descent.

Thus a complete finite continuation test consists of:

- the interval 0<=d<A/P intersected with the prefix half-lines (10);
- one CRT residue modulo D*2^t, combining (8) and (9).

This is lossless in both directions for positive ordinary sources. Conversely,
an integer d satisfying all these conditions yields r>0, legal w and u,
and no descent on u; proper prefixes of w are supercritical and hence also
stay above r. The source and endpoint cannot be chosen independently.

At t>=ceil(log_2 ceil(A/P)), even the dyadic continuation residue alone leaves
at most one integer displacement in the initial interval. This is uniqueness
of the retained displacement, not a guarantee of rejection or termination.
There is no assumption of fresh parity bits after the source is fixed.

## 4. Exact finite offense and a rational countermodel

The new finite compiler exhausts the same 12,449 first-crossing words through
length 21 as the parent. There are 9,779 formal positive integer displacements
with positive rational sources. Literal rational continuation for at most 2j
additional shortcut steps rejects 9,381, leaving 398. The old first-echo test
rejects 6,431 of the same pairs. The full-denominator integer-source count is
still zero in this positive-displacement family.

The experiment therefore demonstrates a stronger arithmetic prefilter, not
9,381 newly excluded integer counterexamples. It also retains every formal
zero-displacement cycle: 12,448 words have A>0, and only the trivial word 10
has an integer source in this finite range.

There is an exact reason not to infer an all-rational continuation theorem.
For

    w=1101101100, P=1024, Q=729, A=1085, D=295, d=1,
    r=61/295, y=356/295,

the positive rational orbit has no descent below r, forever. With the odd
common denominator 295, its numerators have the finite preperiod

    61,239,506,253,527,938,469,851,1424,712,356,178,89

followed by the period

    281,569,1001,1649,2621,4079,6266,3133,4847,7418,
    3709,5711,8714,4357,6683,10172,5086,2543,3962,1981,
    3119,4826,2413,3767,5798,2899,4496,2248,1124,562.

For an even numerator v the next numerator is v/2; for an odd numerator it
is (3v+295)/2. The last one maps to 281. All listed numerators are at least
61, and the first crossing and displacement are exact. This is a finite
certificate of a rational no-descent tail, **not an ordinary Collatz orbit**.
Equation (8) fails: D does not divide A-Pd=61. Hence any proposed proof using
only real no-descent and arbitrarily many rational parity echoes is refuted
by this example. Ordinary integrality is indispensable.

## 5. Remaining offense on this route

Keep both legitimate targets active: prove source escape for SC*, and exploit
(8)-(10) to exclude ordinary cycles or relevant near-returns. The tail bridge
shows that all divergent failures already feed SC*, even if a least value
minimum first crosses its coefficient. The continuation compiler supplies
additional exact information without assuming descent occurs at that first
crossing. Neither target is proved by the finite corpus or the rational
countermodel. No existing theorem status is changed.
