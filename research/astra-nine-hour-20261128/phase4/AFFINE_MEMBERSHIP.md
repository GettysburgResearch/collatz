# Exact affine-word membership is already decidable

The general semigroup-membership search can be narrowed substantially.
Membership in the particular two-generator rational affine monoid arising
from Collatz is an elementary, uniquely decodable problem. The outstanding
problem is whether some member sends a supplied integer to one. These are
different quantified questions, even though both are expressed with the
same two matrices.

This is an elementary restatement of the classical finite parity-word
coding, with a direct decoder and a connected Lean kernel. No priority is
claimed for uniqueness of parity cylinders.

## A deterministic decoder

Read a binary word chronologically, using f_0(x)=x/2 and
f_1(x)=(3x+1)/2 without imposing parity guards. Its resulting affine map is

\[
       f_w(x)=\frac{A_w x+C_w}{2^{|w|}},\qquad A_w=3^{\#1(w)}.
\]

For a first letter b and remaining word v,

\[
 A_{bv}=3^b A_v,\qquad C_{bv}=b A_v+2C_v.                 \tag{1}
\]

Since A_v is odd, the parity of C_{bv} is exactly b. Thus the first
letter and the remaining affine code are recovered by

\[
\begin{array}{c|c|c}
C\bmod2& A_{\rm next}&C_{\rm next}\\\hline
0&A&C/2\\
1&A/3&(C-A/3)/2.
\end{array}                                               \tag{2}
\]

Perform exactly t steps, and verify the reconstructed word's exact scale
and offset against the supplied code (t,A,C). An invalid intermediate
division can instead be rejected immediately. The verified version is
particularly simple to formalize: the raw candidate uses natural division
and truncated subtraction, while the final exact check rejects every
invalid encoding.

The Lean file proves raw round-trip recovery, exact output length,
soundness, completeness, and injectivity of the triple (length, scale,
offset). These statements connect directly to the earlier
[integral-endpoint legality theorem](../AffineReachability.lean).
[Formal decoder](AffineWordDecoder.lean)

Now consider a supplied rational affine matrix with bottom row (0,1) and
top row (a,b). If a is nonpositive or b is negative, reject it. Write a in
lowest positive terms. Its denominator must be a power 2^t, since every
A_w is odd. This determines t uniquely. Its numerator supplies A, and
2^t b must be a nonnegative integer C. Apply (2) and the final check. The
test accepts exactly the matrices in the monoid, and the accepted word is
unique. In particular the monoid is free on its two displayed generators.

The running time is polynomial in the ordinary binary input length. The
number of decoding steps is t, bounded by the input denominator's bit
length. The arithmetic operands and the reconstructed code have bit
length bounded by a polynomial in the input length. This complexity
observation is written mathematics; the Lean kernel proves correctness,
not a machine cost model.

Fixed-matrix membership therefore needs no new general decision theorem.
By contrast, vector reachability from (n,1) to (1,1) asks for **some**
accepted matrix whose a n+b equals one. Its denominator 2^t is not supplied
and its length t has no known universal bound. The integral-endpoint
theorem makes this precisely ordinary convergence of the supplied n.
The ability to recognize each candidate matrix does not decide the
existential search over all candidate lengths.

## The exact interface of flat rational matrix sets

Diekert, Potapov and Semukhin prove decidability for flat rational sets
over GL(2,Z), including Boolean combinations. A flat expression is a finite
union of products L_0 g_1 L_1 ... g_k L_k with fixed rational matrices g_i
and rational subsets L_i of GL(2,Z). In such an expression every L_i has
determinant of absolute value one. The whole set consequently has only
finitely many determinant magnitudes. Our affine monoid contains f_0^t
of determinant 2^{-t} for every t, so it is not a flat rational set of this
specified kind. This directly rules out applying that theorem to the
unmodified two-generator monoid. It does not exclude a new encoding into
another decision problem, which would require its own correctness proof.
[Primary 2024 SIAM article, definition of flat sets and Corollary 6.7](https://researchonline.ljmu.ac.uk/id/eprint/24543/1/2024SIAMfinal_submittion.pdf)

## A precise finite-automaton obstruction

Dhiman and Pandey prove that the complete forward reachability relation
for the classical map is not recognizable by a finite automaton in base
three. Their June 2026 manuscript gives a first-order extraction of powers
of two from the full relation and applies Cobham's theorem. Its argument
does not assume the Collatz conjecture.
[Primary manuscript, Theorem 2](https://arxiv.org/pdf/2602.06066)

For the classical map, a shorter extraction suffices. If R(x,z) means
that z occurs in x's forward orbit, then on positive integers

\[
 x\text{ is a power of two}\quad\Longleftrightarrow\quad
   \forall z\,[R(x,z)\land z\text{ odd}\ \Longrightarrow z=1]. \tag{3}
\]

A power of two halves into the cycle 1,2, whose only odd state is one.
Conversely, write x=2^a m with m odd. Its first a steps reach m, so the
right side forces m=1. This is merely a simplified extraction for the
same published obstruction. It is not a new nondefinability theorem.
Since parity and order are definable using addition, a base-b automatic
full relation would make powers of two base-b automatic. Cobham rules
this out whenever b is multiplicatively independent of two, including
every base that is not itself a power of two.

The same short extraction works for the entire published family of odd
q,d with q+d=2^s: one maps to 2^{s-1}, and its cycle again has only one
odd state. Thus the same argument applies in every radix multiplicatively
independent of two for each of those maps, not just its radix q.

This does not rule out a finite-state sufficient termination certificate,
nor does it prove undecidability of reachability. It also supplies no
obstruction at bases 2^k. The manuscript's discussion in Section 8, PDF
page 7, describes constant
multiplication by an odd q as unrecognizable in base two; that particular
sentence is incorrect, because multiplication by a fixed integer is
definable by repeated addition and is recognizable in every integer base.
The extraction proof of its stated base-q theorem does not use that
sentence.

## Exact finite controls

The checker constructs affine matrices independently by chronological
fraction arithmetic, decodes every word through length fourteen and
checks uniqueness. It then exhausts complete scale-and-offset boxes
through length five, comparing decoder acceptance with literal word
enumeration. The tested malformed rational matrices cover signs,
non-dyadic slopes, incompatible offsets and integer nonidentity slopes.
The scope is finite arithmetic, not a bound on unrestricted reachability.
[Checker](check_affine_decoder.py)
