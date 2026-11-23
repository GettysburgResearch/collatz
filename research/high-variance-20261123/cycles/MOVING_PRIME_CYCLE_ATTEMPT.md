# The moving-prime requirement in the complete cycle denominator

**23 November 2026. Status: written theorem about a failed global
cycle-exclusion route; no unrestricted positive-cycle exclusion.**

The attempted closing step was to retain PR185's distinguished
evaluation ideal at enough ordinary primes, combine those local tests
with a large positive real floor, and use a uniform local-to-global
argument. The result below makes the quantifier obstruction exact.

> For every finite set of primes S and every real H>0, there are
> primitive positive rational Collatz cycles whose every state exceeds
> H, whose every state is integral at every prime in S, and whose every
> state has the same reduced denominator D>1. Their shortcut length A
> and odd-step count p satisfy gcd(A,p)=1 and the strict cycle cone
> 2^A>3^p and 4A<7p.

Thus no fixed finite inventory of distinguished-prime tests, even
together with an arbitrarily large real floor, excludes all the
nonintegral rational cycles that imitate an integer cycle at those
places. The construction does **not** refute an adaptive test whose
prime set depends on the full word or contains every factor of D.
The integer-cycle problem still asks for all of those factors at once.

The proof uses a full-denominator modular inverse for balanced words.
The fact that balanced words have an S-unit numerator in the coprime
number-field lift is credited prior PR185 work. Here that observation
is made into an explicit modular identity, then combined with a
simultaneous all-finite-prime, all-real-floor construction. No general
historical novelty claim is made.

## 1. Exact map, words, and denominator

Extend the shortcut Collatz map to rational numbers with odd reduced
denominator: a rational is even or odd according to its numerator
modulo two, and
\[
T(x)=
\begin{cases}
x/2,&x\text{ even},\\
(3x+1)/2,&x\text{ odd}.
\end{cases}
\]
All uses of this rational extension are explicit. A rational cycle
constructed here is not an ordinary positive integer orbit.

Fix integers A,p with 1<=p<A and gcd(A,p)=1. Define
\[
d_i=\left\lfloor\frac{Ai}{p}\right\rfloor
\quad(0\le i<p),\qquad
D=2^A-3^p,\qquad
C=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i}.
\tag{1}
\]
Assume D>0. The positions d_i are distinct, begin at zero, and lie
below A. Write d_p=A and let g_i=d_(i+1)-d_i be the positive odd gaps.

The rational fixed point of this word is C/D. For a cyclic shift
starting at odd position i, extend d_(i+p)=d_i+A and put
\[
a_{i,j}=d_{i+j}-d_i,\quad
C_i=\sum_{j=0}^{p-1}2^{a_{i,j}}3^{p-1-j},\quad
q_i=C_i/D.
\tag{2}
\]
Direct index shifting gives
\[
2^{g_i}C_{i+1}=3C_i+D,\qquad
2^{g_i}q_{i+1}=3q_i+1.
\tag{3}
\]
Each C_i is odd: its first summand is odd and all the others are even.
D is odd. Thus q_i is odd in the rational extension, and (3) has the
exact 2-adic valuation g_i. The word is a literal rational Collatz
cycle, not only a formal affine fixed point.

## 2. An inverse modulo the entire denominator

### Balanced numerator lemma

For the word (1),
\[
\boxed{\gcd(C,D)=1.}
\tag{4}
\]

**Proof.** Work in R=Z/DZ. Both 2 and 3 are units. Choose integers r,s
with pr+As=1 and set u=2^r 3^s in R. The full congruence
2^A=3^p gives
\[
u^p=2,\qquad u^A=3.
\tag{5}
\]
For example,
u^p=2^(pr)3^(ps)=2^(pr+As)=2; negative exponents are powers of
units, so they discard no prime factor.

The integers
\[
m_i=pd_i-Ai
\]
are exactly 0,-1,...,-(p-1), each once: they are the negatives of
the residues Ai modulo p, and multiplication by A permutes those
residues. Consequently
\[
3^{1-p}C
 =\sum_{i<p}u^{m_i}
 =u^{1-p}\sum_{j=0}^{p-1}u^j.
\tag{6}
\]
The geometric identity and (5) give
\[
(u-1)\sum_{j=0}^{p-1}u^j=u^p-1=1.
\tag{7}
\]
In particular the geometric sum is a unit even if R has zero divisors.
Combining (6)--(7) exhibits the explicit inverse
\[
\boxed{
C\,(u-1)u^{p-1}3^{1-p}=1
\quad\text{in }\mathbb Z/D\mathbb Z.
}
\tag{8}
\]
This proves (4) without replacing the distinguished quotient by a
norm or discarding a component. The proof also works for D=1; the
construction below ensures D>1. ∎

Since the multipliers 2 and 3 in (3) are units modulo D,
gcd(C_i,D)=gcd(C,D)=1 for every i. All odd states therefore have
**full reduced denominator D**. The intervening shortcut states are
positive powers of two times the next odd state, so their reduced
denominator is also D.

This explicitly excludes every coprime balanced word with D>1 as an
integer cycle. It is a structured family already implicit in the
credited balanced S-unit observation; it is not claimed as unrestricted
cycle progress.

## 3. A uniform real floor for all rotations

Write
\[
B=2^A/3^p>1.
\]
Differences of floors satisfy
\[
a_{i,j}>\frac{Aj}{p}-1,
\]
including cyclicly wrapped indices. Hence
\[
\frac{2^{a_{i,j}}}{3^j}>
\frac12\,B^{j/p}\ge\frac12.
\]
Summing (2) yields
\[
\frac{C_i}{3^p}>\frac p6,
\qquad
\boxed{q_i>\frac{p}{6(B-1)}}
\quad\text{for every }i.
\tag{9}
\]
The estimate is simultaneous over all cyclic shifts; it is not a
bound only on one selected fixed point.

Every intermediate shortcut state between q_i and q_(i+1) is a
nonnegative power of two times q_(i+1). Thus (9) is also a lower
bound for the **entire** shortcut cycle.

## 4. Avoid any prescribed finite set of denominator primes

Let S be a finite set of primes. Choose an even positive integer L
divisible by ell-1 for every odd ell in S, for example the least common
multiple of 2 and those ell-1.

There are arbitrarily large primes p with p=1 mod L. Only this special
progression is needed, and it has an elementary cyclotomic proof:
given any finite list of primes, take an integer z>=3 divisible by L
and by every prime on the list. A prime divisor ell of Phi_L(z)
divides neither z nor L because Phi_L(0)=1. Since X^L-1 is squarefree
modulo ell, the order of z modulo ell is exactly L. Therefore
ell=1 mod L and ell is absent from the list. Also Phi_L(z)>1,
as follows from its complex roots having absolute value one. This
proves the required infinitude without a quantitative prime estimate.

For such a prime p, let b be the least positive integer satisfying
2^(Lb)>3^p, and define
\[
A=L(b+1).
\tag{10}
\]
Then
\[
2^L<B=2^A/3^p<2^{2L}.
\tag{11}
\]
For the upper bound, minimality gives 2^(L(b-1))<=3^p; equality is
impossible because the bases have different prime support.

For all sufficiently large p,
\[
p<A<2p,\qquad 4A<7p.
\tag{12}
\]
For an elementary quantitative check, 3^5<2^8 gives
A<(8/5)p+2L. Taking p>14L implies both inequalities in (12);
A>p follows from 2^A>3^p>2^p.
Since p is prime and p<A<2p, gcd(A,p)=1.

For each odd ell in S, Fermat's theorem and the chosen congruences give
\[
D=2^A-3^p\equiv1-3=-2\pmod\ell.
\tag{13}
\]
For ell=3 the same expression follows directly from 3^p=0 mod3
and even A. For ell=2, D is odd. Therefore
\[
\boxed{\gcd(D,\prod_{\ell\in S}\ell)=1.}
\tag{14}
\]
Together with (4), every rational state has denominator D and is
integral at every prime in S.

Equation (11) also gives
\[
D>(2^L-1)3^p>1,\qquad
\min_{\text{entire cycle}}x>
\frac{p}{6(2^{2L}-1)}.
\tag{15}
\]
Choose p in the progression larger than both 14L and
6H(2^(2L)-1). This proves the required real floor.

Finally the parity word is primitive. If it were a repetition of
r>1 identical shorter words, r would divide both its length A and
its number p of odd letters. This contradicts gcd(A,p)=1. Its actual
rational shortcut period is therefore exactly A.

Equations (4), (12), (14), and (15) prove the theorem in the opening
paragraph.

## 5. What happened to the attempted closing argument

The intended inference was to replace the whole denominator test by
a bounded set of primewise distinguished-ideal tests, while retaining
the same positive-cycle cone and a strong real minimum restriction.
The construction defeats that inference for **every fixed finite
prime set and every fixed real floor**.

Taking S_k to contain the first k primes and H_k=k gives a sequence
of primitive rational cycles with minimum tending to infinity.
For each fixed prime, every sufficiently late cycle is integral at
that prime. Each cycle nevertheless has a nontrivial reduced
denominator. The sources and periods vary with k; this is not one
fixed ordinary integer acquiring an infinite orbit.

In particular:

- An argument over all ordinary primes remains exact and is not
  contradicted by this construction.
- A word-dependent finite sieve can still inspect all factors of
  its actual D. This construction does not show such a sieve
  cannot be effective.
- Positivity and an arbitrarily high real floor do not repair the
  replacement of that word-dependent set by a fixed finite set.
- The balanced family has gcd(C,D)=1, so **every** prime divisor of
  D witnesses nonintegrality. The obstruction witnesses can all
  be forced outside any prescribed fixed inventory.

For a general word, the normalization in (6) instead has coefficients
that are powers of two multiplying the distinct residue powers of u.
Multiplying by u-1 gives their coefficient differences, not the
constant one in (7). Those differences can have arbitrary length and
sign pattern as the word varies. Neither positivity of the original
word nor its primitivity supplies the needed full-denominator unit
identity for that polynomial. The attempted extension therefore
stops at this precise step.

We also examined the cyclic integer system with diagonal entries
2^g and cyclic off-diagonal entries -3. Its determinant is D, and
its cokernel is cyclic of order D: the maximal-minor gcd divides
both a power of two and a power of three. The all-ones forcing
class has order D/gcd(C,D). This retains the right arithmetic
information, but does not produce a new strict class obstruction.
Its real solution is positive for every word in the positive
cone, so a real convex-separation argument alone cannot remove
the nonintegral cycles above. No bare reformulation is counted
as a closing theorem.

The remaining unrestricted task is a word-dependent obstruction at
the actual distinguished ideal of at least one prime power dividing
D, or another argument that excludes the integer cycle directly.
No such universal obstruction was obtained.

## Sources and formalization boundary

- PR185 at 39ba48e6a8af781193e28c679ea8ab64663c3aa6,
  [CYCLOTOMIC_ZERO_FIBER.md](https://github.com/GettysburgResearch/collatz/blob/39ba48e6a8af781193e28c679ea8ab64663c3aa6/research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md),
  Sections 2, 9 and 10: balanced S-unit observation, the
  distinguished-ideal counterexample, and exact rotation-unit
  dependence. Its blob is 5c9deff8147211d88794471fc1d6b6ab57d54069.
- The proof here retains the complete D throughout. It does not
  use a field norm as a substitute, GRH, a cycle search bound,
  or an unproved distribution theorem for denominator primes.
- The infinite selection of primes, actual rational realization,
  primitive period and simultaneous real-floor result are written
  mathematics. Any finite Lean module supplied alongside this
  note has its own explicit hypotheses and audit scope; it does
  not certify these further deductions automatically.
