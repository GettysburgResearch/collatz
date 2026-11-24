# Primitive high rational cycles invisible at any fixed congruence precision

Date: 2026-11-23. Status: **PROPOSED written constructive theorem with completed scoped internal reconstruction review.** See the [review and exact source bindings](../../reports/2026-11-23-high-variance/CYCLE_REVIEW.md). Full positive-integer cycle exclusion remains OPEN.

This pass tried to turn the distinguished-ideal condition from PR185 into an unrestricted exclusion by testing a fixed collection of prime powers, then using positivity, a large cycle minimum and primitivity to eliminate every surviving word. The theorem below is an exact control against that step. It covers **every fixed modulus** coprime to six and arbitrarily large positive heights. It does not assert that all valuations at a fixed prime pass when tested to unlimited precision.

The construction is elementary. The only literature inspiration is the adjacent-transposition/rotation method in Knight's high-cycle argument; that argument excludes a special balanced cycle, whereas this construction deliberately introduces a controlled defect and retains the complete new denominator. No unproved cycle, GRH, or external analytic estimate is used.

## 1. Convention and theorem

For a binary shortcut word w of length L, with P ones at positions
0 <= d_0 < ... < d_(P-1) < L, define

\[
 C(w)=\sum_{i=0}^{P-1}2^{d_i}3^{P-1-i},\qquad
 D(w)=2^L-3^P.
\tag{1}
\]

Its affine composition is (3^P x+C(w))/2^L. If D(w)>0 and P>0,
the fixed point C(w)/D(w) and all its rotations are positive rational
shortcut-cycle states. The denominator D is odd and coprime to three.
At each rotation, its numerator is odd exactly when the first word bit
is one. Cancelling an odd common factor preserves this parity, so this
is a physical cycle for the usual extension of T to rationals with odd
reduced denominator.

**Theorem.** Given an integer M>=1 with gcd(M,6)=1, a real H>=0, and
any prime ell>=5 with ell not dividing M, there is an explicitly
constructible primitive word w such that:

1. D(w)>0 and 4L<7P;
2. every member of its positive rational cycle exceeds H;
3. M divides both D(w) and C(w);
4. ell divides D(w), but ell does not divide C(w).

In particular the cycle is nonintegral, its least shortcut period is L,
and every prescribed congruence test modulo a divisor of M sees the
correct distinguished evaluation C(w)=0 whenever D(w)=0. The surviving
extra prime ell explicitly witnesses failure of full denominator divisibility.

For a finite list of primes other than two and three and any prescribed
finite precisions, take M to be the product of those prime powers.
The statement is about **those specified precisions**. The construction
can have larger valuations in D than were prescribed; it does not claim
v_p(C)>=v_p(D) at every prime dividing M.

## 2. Parameters and a balanced base word

Let phi(1)=1, use the usual Euler totient otherwise, and put

\[
 t=\operatorname{lcm}(\varphi(M),\ell-1).
\]

Choose an integer q>=12 with q>216H, and define

\[
 a_0=\lfloor\log_2(3^q)\rfloor+1,
 \qquad a=t a_0,\qquad p=tq,\qquad \rho=p/a=q/a_0.
\tag{2}
\]

The integer a_0 is computed exactly as the bit length of 3^q; no
floating-point comparison is needed. Since 3^q is not a power of two,

\[
 3^q<2^{a_0}<2\,3^q.
\tag{3}
\]

For q>=12, 1/2<rho<2/3 and 4a<7p. Indeed a_0>q*log_2(3)>3q/2
by 9>8, while a_0<5q/3+1<2q. For the last inequality, use
log_2(3)<5/3, which follows from 27<32, and

\[
 a_0<q\log_2(3)+1<5q/3+1\le7q/4.
\]

Take a cyclic balanced mechanical word U of length a and weight p,
for example the word with bits

\[
 U_j=\lfloor(j+1)p/a\rfloor-\lfloor jp/a\rfloor.
\]

Every cyclic interval of length j has weight differing from rho*j by
strictly less than one. This follows directly by subtracting floors,
and remains true when the interval passes a cyclic boundary.

Because rho>1/2, U has no cyclic occurrence of 00. Let z=a-p be
its number of zeroes. If every cyclic gap between zeroes were at least
three, a>=3z would give rho>=2/3. Hence two consecutive zeroes are
separated by exactly one one. Their neighbours are ones, so U contains
10101. Rotate U so that these are its first five bits.

Define V by swapping positions 1 and 2:

\[
 U=10101\cdots,\qquad V=11001\cdots.
\tag{4}
\]

U and V have the same length and weight. The cyclic word V has exactly
one occurrence of 00, starting at position 2. All zero runs in either
word have length at most two; their first and last bits agree.
Only the second one moves, from position 2 to position 1. Thus the
**complete block carries** obey

\[
 \boxed{C(U)-C(V)=2\,3^{p-2}.}
\tag{5}
\]

This is a unit modulo every prime other than two and three.

## 3. Modulus payment and a deliberately retained obstruction

Euler's theorem and the choice of t give

\[
 2^a\equiv3^p\equiv1\pmod M,
 \qquad 2^a\equiv3^p\equiv1\pmod\ell.
\tag{6}
\]

For words A followed by B, the exact composition formula is

\[
 C(AB)=3^{|B|_1}C(A)+2^{|A|}C(B).
\tag{7}
\]

Consequently any concatenation of U and V has carry, modulo either
modulus in (6), equal to the sum of its individual block carries.

Equation (5) shows that the two quantities
C(U)+C(V) and 2C(U)+C(V) cannot both vanish modulo ell: subtracting
them would make C(U), then C(V), and then their unit difference zero.
Choose k in {1,2} such that

\[
 kC(U)+C(V)\not\equiv0\pmod\ell,
\]

and set

\[
 \boxed{w=U^{kM}V^M,\quad L=aM(k+1),\quad P=pM(k+1).}
\tag{8}
\]

The complete denominator is positive by (3). Its exponents are still
multiples of those in (6), so M*ell divides D(w). The complete carry is

\[
 C(w)\equiv M\bigl(kC(U)+C(V)\bigr)
 \pmod M\quad\text{and}\quad\pmod\ell.
\tag{9}
\]

The first residue is zero, while the second is nonzero because ell does
not divide M. This proves the exact simultaneous claims in the theorem.
After reducing C(w)/D(w), the prime ell still divides its denominator.
No factor of D is dropped from the test.

## 4. Primitivity is witnessed by one cyclic marker gap

There are exactly M occurrences of 00 in w, one in each V block.
Consecutive markers inside V^M are separated by a positions. The cyclic
gap passing through U^(kM) has length (kM+1)a and is uniquely longest.
Any rotational period of w preserves its set of 00 markers and their
cyclic distances. It must fix the marker immediately after this unique
longest gap, so its shift is zero modulo L. For M=1 the single marker
already gives the same conclusion. Thus w is primitive.

Because the rational shortcut map is deterministic and its actual parity
word is w, a smaller state period would give a smaller word period.
Therefore the rational cycle also has least state period L.

## 5. An explicit lower bound for every rational state

Let E(j) be the number of ones in the first j positions of w minus
rho*j. At a block boundary E=0. In U each prefix discrepancy lies in
(-1,1). Moving the second one one position earlier adds one only to the
prefix of length two. Hence, in every U or V block,

\[
 -1<E(j)<2.
\]

Subtracting two prefix discrepancies, including wraparound using
P=rho*L, gives for every cyclic interval of length j

\[
 \bigl|\#\text{ones}-\rho j\bigr|<3.
\tag{10}
\]

This holds for intervals longer than L too, by removing full periods.
No run of three zeroes occurs in w.

Put lambda=3^rho/2. Equation (3) implies 0<lambda<1 and
lambda^(a_0)=3^q/2^(a_0)>1/2. Also rho>1/2 implies
lambda^2>3/4. The finite geometric identity gives

\[
 1-\lambda^{a_0}
 =(1-\lambda)\sum_{j=0}^{a_0-1}\lambda^j
 > (1-\lambda)a_0/2.
\]

Since its left side is less than 1/2,

\[
 1-\lambda<1/a_0,\qquad 1-\lambda^3<3/a_0.
\tag{11}
\]

For any rational state x_i on the cycle, expand its preceding affine
recurrences. The homogeneous term tends to zero because the multiplier
over a full period is 3^P/2^L<1. Thus, with epsilon_j the periodic bits,

\[
 x_i=\frac12\sum_{j\ge1}\epsilon_{i-j}
       \frac{3^{\epsilon_{i-1}+\cdots+\epsilon_{i-j+1}}}{2^{j-1}}.
\tag{12}
\]

By (10), each term with epsilon_(i-j)=1 is at least
lambda^(j-1)/(2*3^3). Each group of three consecutive backwards bits
contains a one. Since lambda<1, its contribution to the weighted sum
is at least lambda^(3h+2). Summing those geometric groups yields

\[
 \boxed{x_i\ge\frac{\lambda^2}{54(1-\lambda^3)}
          >\frac{a_0}{216}>H.}
\tag{13}
\]

The last inequality uses a_0>q>216H. All inequalities refer to the
**same complete rational cycle** (8), not to changing finite words
chosen separately at each vertex.

For fixed M and ell, the construction has L<=6Mtq. Choosing
q=max(12,floor(216H)+1) gives an explicit linear-in-H period bound
with a modulus-dependent constant. This is not a claim about integer
cycle lengths.

## 5a. Quadratic height in the period along an infinite subsequence

There is a stronger conclusion for the **same fixed M and ell**. Let B>=1
be an integer and additionally require the exact integer inequality

\[
 2^{B a_0}<2\,3^{Bq}.
\tag{14}
\]

It says lambda^(B*a_0)>1/2. Repeat the geometric argument (11) with
B*a_0 in place of a_0; the discrepancy and backward-series arguments
are unchanged. Therefore

\[
 \boxed{\min_i x_i>\frac{B a_0}{216},\qquad
        \frac{\min_i x_i}{L}>\frac{B}{648Mt}.}
\tag{15}
\]

This strengthening has an integer-checkable additional hypothesis. It
does not introduce a floating-point closeness test into the construction.

To obtain infinitely many examples, write alpha=log_2(3), which is
irrational because no positive powers of two and three are equal. Its
upper continued-fraction convergents A/q have q tending to infinity and

\[
 0<A-q\alpha<1/q.
\tag{16}
\]

For completeness, the standard convergent recurrences give determinant
P_n Q_(n-1)-P_(n-1)Q_n=(-1)^(n-1). Writing the remaining continued-
fraction tail as alpha_(n+1) gives

\[
 \alpha-\frac{P_n}{Q_n}
 =\frac{(-1)^n}{Q_n(Q_n\alpha_{n+1}+Q_{n-1})}.
\]

Since alpha_(n+1) is greater than its integer part, the absolute error
is less than 1/(Q_n Q_(n+1))<=1/Q_n^2. Odd-indexed convergents lie
above alpha and their denominators are unbounded. This proves (16).
A primary author-written reference, read directly, is Burton Rosenberg,
*Continued fractions and the geometry of numbers* (2003), Lemmas 1--3,
PDF pages 2--3:
<https://www.cs.miami.edu/home/burt/learning/Workbook/special-topics/notes/continuedfract.pdf>.

For q>=12 in this upper subsequence, A=ceil(q*alpha)=a_0, and (16)
implies (14) with B=q. Since a_0<2q and L<=3Mt a_0, (15) gives

\[
 \boxed{\min_i x_i>\frac{a_0q}{216}
       >\frac{L^2}{3888 M^2t^2}.}
\tag{17}
\]

Thus, for every fixed M and ell in the theorem, infinitely many of the
constructed primitive nonintegral cycles pass the prescribed modulus
and have minimum at least a positive fixed multiple of the square of
their least period. In particular, their minimum/period ratio is
unbounded. Fixed-modulus divisibility, primitivity and an arbitrarily
large **linear** minimum-to-period threshold can hold simultaneously.
No unrestricted higher-power height growth is claimed.

## 6. What this attack settles and what it does not

The attempted shortcut was: retain the correct distinguished evaluation
at several primes to high fixed precision, require a primitive word,
exclude small positive values, and infer that the remaining full
zero-fiber is empty. The construction shows those conditions do not
supply that inference. Even the nontrivial-cycle cone 4L<7P and a
uniformly large minimum can coexist with all prescribed congruence
conditions. Equation (17) strengthens this to an unbounded
minimum/period ratio, keeping the modulus fixed.

The result does not rule out an adaptive arithmetic proof that finds a
new bad prime, or raises the precision at a previously selected prime as
a function of the whole word. Indeed this construction explicitly supplies
a bad prime ell. It also does not claim a positive integer cycle, an
escaping integer orbit, or an impossibility theorem for all sieves.

The unrestricted task remains to show, for every nontrivial candidate
word, failure of divisibility at some actual prime power of its complete
D. The fixed-prime norm route loses the distinguished fiber; the fixed-
precision correct-fiber route now has the explicit high primitive controls
above. Neither observation supplies a uniform all-word obstruction.

## 7. Provenance and evidence boundaries

The current exact source is PR185 at
`39ba48e6a8af781193e28c679ea8ab64663c3aa6`, path
`research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md`, Git blob
`5c9deff8147211d88794471fc1d6b6ab57d54069`. Its Sections 9--10 identify the
wrong-conjugate norm issue and retain ideals (ell^v,X-3). The new proof
above does not import that note as an unproved mathematical premise.

The contrasting all-word census is PR175 at
`8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`, path
`research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md`.
Its polynomial minimum bound does not assert that a fixed modulus decides
all words; no disagreement with that theorem is intended.

Primary literature consulted for the swap idea: Kevin Knight, *Collatz
high cycles do not exist*, Discrete Mathematics 349 (2026), article
114812, DOI <https://doi.org/10.1016/j.disc.2025.114812>. The publisher's
abstract and section previews were read. No unread full-text theorem
is used here. The direct identities and proofs above are self-contained.

The exact checker `cycle_ideal_control.py` constructs complete finite
controls, verifies every word bit on the rational cycle, and tests primitivity,
minimum height, both full divisibility statements, and the explicit bad
prime. It also realizes each finite word on a positive ordinary source.
Actual execution records and source bindings are collected in the
[replay and review packet](../../reports/2026-11-23-high-variance/).
Those executions are controls; the arbitrary-M,H statement is the written
proof, not a finite census or a Lean theorem.
