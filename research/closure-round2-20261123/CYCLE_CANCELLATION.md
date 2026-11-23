# Attack on numerical cancellation: full-quotient defects and zero-fibre packing

Date: 2026-11-23. Status: **OPEN closing attempt with proved finite arithmetic
and counting deductions. No unrestricted integer-cycle exclusion.**

The target in this pass is the actual numerical gcd, after all common
polynomial factors have been removed. This note does not add another
rational countermodel or fixed word-template exclusion. It tries to convert
whole-word carry transport and the dependent family of cyclic rotations
into the strict zero-fibre bound needed for closure. The resulting
injections are valid, but their counts remain too large.

## 1. Updated sources and exact target

Throughout, take integers 1<=p<A and a binary shortcut word w of length A
and weight p, with one positions d_i. Use the complete carry and denominator

\[
 C(w)=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i},\qquad D=2^A-3^p>0.
\tag{1}
\]

Let Z(A,p) be the set of all such words with D dividing C(w), and let
N_0=|Z(A,p)|. Every word in Z gives an actual positive integer cycle.
A primitive A-cycle supplies A distinct rotations in Z, so N_0<A is a
sufficient exclusion target for that pair. Repetitions of a shorter cycle
must not be counted as A distinct rotations.

The new PR185 theorem at
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md`
(blob `54b6f161d8a8ce81c32fed6c6166807d5c9f8445`), proves growth of
D_pol after polynomial gcd cancellation. It explicitly leaves the numerical
quantity gcd(D_pol,Q_0(3)) open. Its principal-fibre control
`PRINCIPAL_FIBER_CONTROL.md` (blob
`c749ad8f97cd9585a9b251129a79a880ff46d965`) shows that even a surviving
principal factor can cancel completely at the correct evaluation.

The new PR178 head `2169884b64871b448cda16c7d74a0d5914ed870b`,
`research/high-variance-20261123/cycles/MOVING_PRIME_CYCLE_ATTEMPT.md`
(blob `f71374314dbf2193aa82ed493eadbcd223a97e6c`), constructs primitive
high rational cycles integral at **every prime in a prescribed finite set**.
That local statement is stronger than the preceding PR182 fixed-precision
construction. Its balanced full-denominator unit identity, credited there
to the earlier PR185 observation, is also formalized at that head.
The present attack therefore keeps the complete, word-dependent D.

## 2. Exact transport of the numerical gcd under one moving letter

Write two complete words, of the same length and weight, as

\[
 w=u\,0^h1\,v,\qquad w'=u\,10^h\,v,
 \qquad h\ge1.
\]

All earlier and later bits are retained. Chronological concatenation gives

\[
 \boxed{C(w)-C(w')=2^{|u|}3^{|v|_1}(2^h-1).}
\tag{2}
\]

Since gcd(D,6)=1, if D divides C(w), then

\[
 \boxed{\gcd(D,C(w'))=\gcd(D,2^h-1),\qquad
 \operatorname{den}_{\rm red}\frac{C(w')}{D}
   =\frac{D}{\gcd(D,2^h-1)}.}
\tag{3}
\]

The identity concerns the entire numerical denominator, including every
prime power, rather than a norm or a fixed set of primes. For h=1 the
neighbor has full reduced denominator D. This does not by itself bound
the numerical cancellation remaining after polynomial gcd removal; no
claim about gcd(D_pol,Q_0(3)) is inferred from the transport law. More generally, for one adjacent
swap without assuming either carry is divisible by D,

\[
 \gcd\bigl(\gcd(D,C(w)),\gcd(D,C(w'))\bigr)=1,
\quad
 \gcd(D,C(w))\gcd(D,C(w'))\mid D.
\tag{4}
\]

Proof: any common divisor in (4) divides D and the 2,3-unit difference in
(2), hence is one. Equation (3) is gcd invariance under subtraction,
followed by removal of a factor coprime to D. These are elementary
consequences of the complete adjacent-swap identity, not an independent
transcendence result. No external novelty or priority claim is made for
these identities; their role here is to test a possible global counting
argument.

For D>1, the attempted balancing argument cannot transport integrality
through adjacent exchanges: integrality is lost immediately, and no
nontrivial divisor of D cancels from the neighboring carry. For D=1,
the neighbor remains integral, as the exact formula requires. The next question was whether the simultaneous loss around all
cyclic rotations forces more distinct neighboring words than exist.

## 3. A global disjoint-neighborhood injection

Assume A>=5 and

\[
 \boxed{D>2\,3^{\lfloor A/2\rfloor}.}
\tag{5}
\]

For a word z with A bits and p ones, let o_i count the ones strictly
before cut i. In Z/DZ define the units

\[
 a_i=2^i3^{-o_i}\quad(0\le i<A).
\]

**Cut separation.** The a_i are pairwise distinct even up to sign.

To prove this, compare distinct cuts along the shorter cyclic arc, of
length 1<=h<=floor(A/2), containing r ones with 0<=r<=h. The full
relation 2^A=3^p modulo D permits wraparound, so the ratio of the two
cut units is 2^h3^(-r). Equality up to sign would imply

\[
 D\mid 2^h-3^r\quad\text{or}\quad D\mid2^h+3^r.
\]

These are nonzero integers: equality of a positive power of two and a
power of three is impossible. Their absolute values are at most
2*3^floor(A/2), contradicting (5).

Now form the graph whose vertices are all binomial(A,p) words; an edge
exchanges unequal bits at two neighboring **cyclic** positions. Its
degree t(z) is the number of cyclic changes of bit in z.

**Packing theorem.** Under (5), the closed neighborhoods of the words
in Z(A,p) are pairwise disjoint. Consequently

\[
 \boxed{\sum_{w\in Z(A,p)}(1+t(w))\le {A\choose p}.}
\tag{6}
\]

Here are the details needed for the cyclic cut. First, two zero words
cannot be adjacent: rotate their common swapped positions away from the
end of the displayed word and use the unit difference (2) with h=1.
Rotation preserves the zero fibre, because a cycle can start at any of
its states. Second, suppose a word z were adjacent to two different zero
words at distinct cuts. Since A>=5, choose a new origin outside the at
most four positions touched by those two swaps. Both exchanges are now
internal. Relative to this common z, their carry displacements have the
form

\[
 \pm 3^{p-1}a_i,\qquad \pm 3^{p-1}a_j.
\]

Both must cancel the same C(z) modulo D. As 3 is a unit, this contradicts
cut separation. Thus no vertex belongs to two closed neighborhoods.
Counting them gives (6).

In particular N_0<=binomial(A,p)/(1+min_(w in Z)t(w)) when Z is
nonempty. No independence between rotations or between prime divisors is
assumed. The bound is valid but remains far above N_0<A.

## 4. A stronger window injection, still insufficient

There is a second exact injection with no hypothesis (5). Let 1<=h<=A
and assume

\[
 D>3^h.
\tag{7}
\]

Fix a contiguous cyclic window of h positions. **A zero word is determined
by its bits outside this window.**

Indeed rotate the window to be internal, and suppose two zero words are
u v s and u v' s with |v|=|v'|=h. Since their complete weights agree,
|v|_1=|v'|_1. Their carry difference is

\[
 C(uvs)-C(uv's)=2^{|u|}3^{|s|_1}\bigl(C(v)-C(v')\bigr).
\]

Thus D divides C(v)-C(v'). Every h-bit carry lies between zero and
3^h-2^h: replacing a zero by a one in the chronological recurrence
C_(j+1)=3^(epsilon_j)C_j+epsilon_j 2^j only increases the carry,
and the all-ones word has carry 3^h-2^h. Equation (7) therefore forces
C(v)=C(v'). The pair (odd count,carry) determines a finite word of a
specified length. To see this, the parity of the carry gives the first
bit; after it is removed, the suffix odd count is known and the recursion
C(b::v)=3^(|v|_1)b+2C(v) recovers the suffix carry. Induction recovers
every bit. Hence v=v'.

It follows that

\[
 \boxed{N_0\le
 \sum_{r=\max(0,p-h)}^{\min(p,A-h)}{A-h\choose r}
 \le2^{A-h}.}
\tag{8}
\]

This is an injection into ordered complementary bit strings; it includes
the requested full zero-fibre, not only one cycle or a collection of
independently chosen witnesses. Nevertheless its strongest h is on the
scale log_3(D), at most A*log_3(2). The resulting complementary word has
linear length approximately (1-log_3(2))*A, rather than logarithmic length.
The bound therefore remains exponential in A, and the earlier PR175
cycle-minimum census already gives a stronger asymptotic polynomial
bound under its stated logarithmic-form input. Equation (8) is not claimed
as an improvement over that census.

For a concrete comparison, at (A,p)=(13,8), D=1631 and h=6 satisfy
(7). The looser last bound in (8) permits 128 words, whereas primitive-cycle exclusion
needs fewer than 13. This example illustrates the size of the remaining
counting gap; it is not a claim that 128 zero words actually occur.

**First unsupported step.** To get N_0<A from this route, one would need
a substantially stronger global disjointness/expansion statement for
long edit paths, or reconstruction from a sufficiently short complement.
The local unit differences do not supply either. For several edits, the
carry changes are signed sums of units that can have nontrivial common
divisors with D. Cyclic rotations give dependent zero words, not additional
independent congruences. Treating the local injections as globally
injective would assume the needed conclusion.

## 5. Testing a moving-target gcd theorem at the actual normalization

For coprime A,p, PR178's balanced unit permits another exact view of the
same obstruction. Choose u in (Z/DZ)^* with u^p=2 and u^A=3, and set
v=u^(-1). For an arbitrary word define

\[
 b_i=\lfloor Ai/p\rfloor,\quad e_i=d_i-b_i,\quad
 e_*=\min_i e_i.
\]

For the unique i with r=Ai mod p, put c_r=2^(e_i-e_*). These are
positive integer powers of two. Since pd_i-Ai=-r+pe_i,

\[
 C(w)=3^{p-1}2^{e_*}P(v),\qquad
 P(V)=\sum_{r=0}^{p-1}c_rV^r
\quad\text{in Z/DZ}.
\]

Negative e_* causes no loss: two is a unit in this quotient. Because
v^p=1/2, the explicit unit identity

\[
 2(1-v)(1+v+\cdots+v^{p-1})=1
\]

gives

\[
 \boxed{D\mid C(w)\ \Longleftrightarrow\ H(v)=0,\qquad
 H(V)=2c_0-c_{p-1}+2\sum_{r=1}^{p-1}(c_r-c_{r-1})V^r.}
\tag{9}
\]

For a balanced word all c_r=1, so H=1 and divisibility is impossible
when D>1. For an arbitrary legal word, the coefficient differences in
this **residue order** have no established uniformly bounded support,
degree or height. Original word legality constrains neighboring d_i in
the chronological order; it does not erase the permutation r=Ai mod p.
Equation (9) keeps the correct full quotient, but is not itself a new
cycle exclusion or a bound for the numerical gcd. For gcd(A,p)>1 it
cannot be used by retaining only the principal factor; all components
must still be treated.

The literature attack was to use the moving-target version of the
Subspace/gcd theorem. Grieve--Wang, *Greatest common divisors with moving
targets and consequences for linear recurrence sequences*, Theorem 1.2,
requires fixed polynomial degrees and coefficients of small height
relative to the moving S-unit arguments. Its alternative also retains
exceptional subgroup configurations; it is not an unconditional small-gcd
statement at every moving point. The theorem statement and height
conventions were read directly in the primary author preprint, pages 2
and 7: <https://arxiv.org/pdf/1902.09109>.

Three attempted encodings failed their stated requirements:

- Directly evaluating F_0,Q_0 at the fixed point 3 has no growing argument
  height and allows growing degree and coefficient height.
- Introducing every summand 2^(d_i)3^(p-1-i) as an S-unit coordinate makes
  the number of coordinates grow with p, so this is no fixed-dimensional
  application.
- Introducing the complete C as one extra coordinate does not preserve
  the S-unit hypothesis. For an odd starting word, C is odd and its last
  one term shows C is not divisible by three. Its prime factors outside
  {2,3} carry log C of numerator height; it is not supplied as a small
  outside-prime perturbation of a {2,3}-unit.

The fixed-polynomial Corvaja--Zannier Theorem 1 was also read in its primary
paper, <https://arxiv.org/pdf/math/0311030>, pages 1--2. It has fixed
coprime polynomials, a fixed finitely generated torus group and an
exceptional algebraic locus. It does not remove the growing-description
or exceptional-locus obligations above. No general gcd theorem is
imported as an unproved universal Collatz premise.

## 6. Evidence and result of the attack

Equations (2)--(9) have written proofs above. The complete carry definition
and concatenation theorem are imported from the previously audited
`research/high-variance-20261123/CycleWordAlgebra.lean`. The new
`CycleCancellation.lean` formalizes the moving-one carry identity, the
positive-denominator two/three coprimalities, the exact numerical gcd
transport, and the full-denominator and adjacent-swap consumers. The
full-denominator consumer derives the needed coprimalities from this
word's own denominator rather than assuming them separately.

The author's compilation with Lean 4.34.1 and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` passed with warnings treated
as errors. Its public-declaration axiom audit used only `propext`,
`Classical.choice` and `Quot.sound`; it introduced no new axioms. These
finite arithmetic statements do not formalize the graph counting,
cyclic-window injection, normalization or literature application.

`cycle_cancellation_controls.py` supplies a small independent arithmetic
replay: position-sum and chronological affine carries, actual ordinary
parity/closure for repetitions of the known 2 -> 1 -> 2 cycle, and exact
rational reduction of the neighboring carry. At A=12, p=6, D=3367,
the repeated source has C=6734, while two contextual adjacent swaps have
carries 6491 and 6302; both neighboring reduced denominators are 3367.
The D=1 control explicitly remains integral. A separate h=3 control
uses the abstract modulus 7, with carries 56 and 35 and common gcd 7;
that modulus is not mislabeled as the word's full cycle denominator.
Corrupted source carry, neighboring carry and modulus controls are
rejected. Both normal and optimized Python replay passed for these exact
controls. No extra large finite census was used to infer absence of all
cycles.

This pass did not produce the full numerical-cancellation obstruction.
It reached actual whole-fibre injections, kept every denominator factor,
and identified the exact step that does not follow from local transport.
The unresolved target remains D_pol not dividing Q_0(3), or a different
argument forcing N_0<A, for every nontrivial primitive integer-cycle
candidate.
