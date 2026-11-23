# Direct carry construction: terminal freedom and sign crossing

23 November 2026. **OPEN:** no universal small-carry construction was
obtained. This is an attempted construction with two exact scope results,
not a new reduction claimed as convergence. The initial target is the
fixed positive ordinary source in checkpoint 16's two-carry question.

## 1. The construction attempted

For the actual first K shortcut bits of n, let b be the even count and D
the complete complementary carry. Allow a positive integral terminal
value u, rather than forcing the standard terminal value 1 or 2. Its
pullback is

    y = (2^K u-D)/3^b.

To obtain an initial denominator dividing 3^r with r<=b, the exact extra
condition is

    2^K u = D (mod 3^(b-r)).

Thus u lies in one progression of spacing 3^(b-r). Pulling that progression
back gives the same initial numerator progression of spacing 2^K. Choosing
the terminal integer closest to D/2^K does not preserve the required
3-adic condition unless it lies in that progression. This agrees with
PR182's already published initial/terminal lattice calculation; it is not
counted as a new finding here. The attempted freedom does not construct a
candidate at its own checkpoint-16 height.

The next attempt used a negative candidate: its signed product contracts
without the quadratic denominator weight until the first sign crossing.
The following exact lifting theorem shows what any argument after that
crossing must retain.

## 2. Any ordinary target can occur after the first sign crossing

**Theorem L (all-target lifting).** Fix any positive ordinary N and any
positive integer u. Let R be the least positive integer such that

    2^R (u+1) < 3^R.

Set

    x_0 = 2^R N,
    y_0 = [2^R(u+1)-3^R]/3^R.

Then R>=2, -1/3<y_0<0, and the first R paired steps are legal with
original-even and complementary-odd branches. They satisfy

    x_j = 2^(R-j) N,
    y_j = (2/3)^(R-j)(u+1)-1       (0<=j<=R).

The first step crosses the sign: 0<y_1<1/2. All subsequent y_j through
y_R=u are positive, and the terminal pair is exactly (N,u).

**Proof.** Minimality gives
2^(R-1)(u+1)>3^(R-1); equality is impossible because R>=2 and the left
side is even. Combining this with the defining inequality gives both
strict intervals. For every j<R the displayed numerator of y_j is odd
and its denominator is odd, so y_j has odd rational parity. Meanwhile
x_j is even. Direct substitution in T_1(y)=(3y+1)/2 proves the displayed
orbit. No convergence property of N is used.

For any specified finite L, choose u as a positive integer representative
of the unique complementary parity residue of N modulo 2^L. Then those
L further tests pass, so the constructed pair passes R+L tests. This
retains the unchanged target N at the meeting clock; the starting source
2^R N changes when u changes. It does not solve a fixed-source candidate
problem by allowing that source to vary.

Consequently a negative-to-positive crossing, even with an arbitrarily
long supplied legal continuation, does not by itself restrict the
remaining target to a separately established family. The candidate's
own height and the original source must remain in a closing argument.
The construction supplies no uniform inequality R+L>=H(x_0,a,r).

An exact short control is

    (16,-1/9) -> (8,1/3) -> (4,1) -> (2,2).

The first three steps are legal. At the last displayed pair the two
parities coincide. Thus even an initially tiny negative candidate can
cross before the special true-dual crossing and continue legally for
additional steps.

## 3. What the denominator of the true dual records

This section assumes an actual finite path to one; it does not construct
that path. Let tau be the first-hit clock and b_tau the number of even
inputs before it. Pull the terminal dual 2 backward through this path.
By the parity-complement conjugacy its value is Omega(n). Write it in
lowest terms as a/3^r.

**Theorem D (exact clock in the denominator).** For n>2,

    r = b_tau-1.

Moreover Omega(4)=1/3, while a<0 for every convergent positive n outside
{1,2,4}. The remaining values are Omega(1)=2 and Omega(2)=1.

**Proof.** Every first hit from n>2 ends in 4,2,1. The backward
complementary values are respectively 1/3,1,2. At 4 the denominator has
exponent one. From any reduced u/3^j with j>0, the original-odd inverse
doubles the numerator and retains j, while the original-even inverse is
(2u-3^j)/3^(j+1), whose numerator remains a unit modulo three. Each earlier
original even step therefore adds exactly one to the reduced exponent.
If the original n is not 4, the preceding state is 8 and its dual is -1/9;
all earlier complementary inverse branches preserve negativity.

The denominator-persistence calculation is inherited from PR178's
boundary-corrected construction. The forced 4,2,1 terminal segment gives
the stated specialization; this is not presented as a separate deep
convergence result.

For n>2, the original finite affine formula now gives an exact clock bound:

    n * 3^(tau-r-1) <= 2^tau,

or equivalently

    (3/2)^tau <= 3^(r+1)/n.

Equality occurs precisely for a path with no odd input before its first
hit, namely n=2^tau. The inequality is strict otherwise. Thus the true
reduced denominator already controls the first-hit clock linearly:

    tau <= ((r+1) log 3 - log n)/log(3/2).

This is an interpretation of a known true dual, not a finite-prefix
criterion independent of numerator height. A large wrong integer
candidate can match any prescribed finite complementary prefix.

## 4. Exact negative-sector estimate

For the same true dual, if n is outside {1,2,4}, it stays negative until
the original state 8 at time tau-3, where its value is -1/9. Throughout
that negative portion, the fixed-denominator integer product

    P_j = 3^r x_j (-y_j)

is positive. An original odd step has ratio (3x_j+1)/(4x_j)<=5/6; an
original even step whose next dual remains negative has ratio
(3-1/|y_j|)/4<3/4. Therefore

    8 * 3^r * 6^(tau-3) <= 9*n*|a|*5^(tau-3).

The quadratic denominator weight is unnecessary on that sector. Theorem L
explains why crossing into the positive sector cannot simply be declared
terminal: it admits arbitrary ordinary targets and arbitrarily long
specified continuations. No estimate eliminating that remaining sector
was obtained.

## 5. Global normalization of the positive-sector reset cost

I next tried to improve the total denominator-removal cost by accounting
for the arithmetic between successive numerator increases. This is a
different calculation from bounding each denominator level separately.

Start with a reduced positive triadic value. Strip any initial even
numerator, then at each positive denominator exponent j retain its odd
numerator w_j. Execute one odd rational step and all the following even
rational steps until the next odd numerator w_(j-1). If the denominator
has just become one, include those last even steps as well. Write k_j
for the number of steps in this block. Exactly,

    k_j = v_2(w_j+3^(j-1)),
    2^k_j w_(j-1) = w_j+3^(j-1).

Consequently the total compressed clock K=sum k_j has the identity

    K = log_2(w_R/w_0)
        + sum_(j=1)^R log_2(1+3^(j-1)/w_j).

All numerators and the complete order of the levels are retained. The
quadratic worst-case budget is concentrated in the second sum. There is
real local arithmetic between its terms: if w_j=1 then k_j is one when
j-1 is even and two when j-1 is odd. The following numerator is therefore
(1+3^(j-1))/2 or (1+3^(j-1))/4, rather than another small independent
choice. This follows directly by reduction modulo eight.

The attempted next step was to turn those linked resets into a global
upper bound on the displayed sum for the word selected by the unchanged
ordinary n. No such bound was established. The exact original-source
affine identity does not specify the size of these w_j independently;
substituting it into a carry determinant returns the same identity.
Nor does a short-block small-sum estimate alone bound the number or
placement of the blocks. Treating the full R-term carry as a fixed-length
S-unit equation would change the theorem's dimension. The existing
PR178 discussion already records that latter restriction.

This normalization gives a precise arithmetic quantity for a further
attempt, but it supplies neither a better global certificate theorem
nor the small-residue construction. In particular, no claimed positive
closing estimate is hidden in the local w_j=1 example.

## 6. Source and evidence boundary

Read at exact heads:

* PR176, fb402404deb810bd8e32e596993739bb5a6967d1,
  `research/lean-global-resolvent-20261121/overview/triadic-height/`:
  the finite Lean theorem, written potential, and two-carry question.
* PR178, e6ed7f1429ced4b58b85ca9006edd9a3a12ca193,
  `research/profound-step-20261123/arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md`:
  boundary-corrected stream, denominator persistence, exact Subspace cost.
* PR182, a7fd3ac9e5bff7412858df23d776bb847e9c1371,
  `research/whole-repo-round3-20261123/TRIADIC_CLOSURE.md`:
  initial/terminal lattice, joint denominator search and ordinary-source
  guard. Its existing failures are credited, not rebranded as new results.

The primary Monks--Yazinski paper defines the parity-complement
autoconjugacy and proves the rationality boundary in Theorem 2.1:
https://monks.scranton.edu/files/pubs/AutoConjV13.pdf.
The definition and relevant theorem were inspected directly. Monks's
2025 q-analog theorem was also inspected at
https://cs.uwaterloo.ca/journals/JIS/VOL28/Monks/monks6.pdf;
no new polynomiality transfer was obtained.

The accompanying exact checker verifies the displayed identities on
selected finite controls, including powers of two and both signs. The
all-target lifting proof is symbolic; its universal claim is not supplied
by enumeration. No new Lean module is supplied for these elementary
scope results, and no universal construction or full convergence claim
is made.
