# Compiling two signed reference cycles into ordinary certificate descent

**PROPOSED. Full Collatz convergence remains OPEN.** This note gives a
general, exact compiler for a family of ordinary certificate transformations.
It does not assume convergence of negative integers. The inputs to the
compiler are two supplied, finite rational calculations; the output is an
infinite arithmetic progression of positive ordinary parameters and a
strictly smaller parameter. Arbitrarily long supplied witnesses are accepted.

The two contractions in PR164 are instances of the construction. Six further
instances are exhibited, including a class whose parameters are divisible by
three. The common well-founded quantity is the ordinary parameter itself,
even though its source witness becomes longer. Neither this catalog nor the
whole compiler is proved to cover every required parameter.

## Sources and normalization

Use the accelerated map on positive odd integers

\[
 U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

Let \(E\) be the positive odd integers with a finite odd trajectory to 1,
equivalently the finite exponent witnesses of PR164. Write

\[
 X(M)=128M+1,\qquad Y(M)=64M+1,
 \qquad \mathcal C(M): X(M)\in E\Longrightarrow Y(M)\in E.
\]

The relevant domain of the full transfer question is \(M>0\), \(4\nmid M\).
The constructions below start on odd \(M\). They can land in different odd
residue classes modulo four.

* PR164, head `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`,
  [`continuation-negative.md`](https://github.com/GettysburgResearch/collatz/blob/6fa6b429870a9cd53cde0fc77ad64a3c3956199f/research/witness-closure-512-2026-11-20/continuation-negative.md),
  W512-070--072: the two earlier contractions, positive realization, and
  arbitrary-witness splicing. This note generalizes their reference-cycle
  construction; it does not claim those two examples as new.
* The same PR, [`continuation-descent.md`](https://github.com/GettysburgResearch/collatz/blob/6fa6b429870a9cd53cde0fc77ad64a3c3956199f/research/witness-closure-512-2026-11-20/continuation-descent.md),
  W512-060: a distinct positive-base-pair descent using a finite list of
  smaller P/Q premises. That result is not required for the proof below.
* PR146, head `fd991063721e9c157d318e40bb20131762f7d750`,
  [`LEAST_FAILURE_SIEVE.md`](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md):
  the sparse sufficient test and its surviving rank-five Mersenne family.
* PR163, head `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  [`REVERSE_CERTIFICATE_KERNEL.md`](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md),
  K3: the complete rank-five parametrization used as an adversarial case.

The full-conjecture equivalence is a pinned source dependency, not a new
claim or a new proof-assistant build in this note. The compiler theorem itself
uses only the elementary algebra proved below.

## NT1. The cycle equations determine a unique scale

For an odd rational number with odd denominator, a finite *reference word*
\([a_1,\ldots,a_r]\) means repeated algebraic updates
\(z\mapsto(3z+1)/2^{a_i}\), with the displayed exponent exactly the
2-adic valuation at each step. No infinite signed orbit is invoked.

The base pair at \(M=-1\) has the finite words

\[
 -127\xrightarrow{[2,2,2,1,2,4,5]}-1,
 \qquad
 -63\xrightarrow{[2,2,3,1,3,2]}-5.
\tag{1}
\]

The reference \(-1\) has the one-step word \([1]\) to itself, with
multiplier \(3/2\). The reference \(-5\) has the two-step word \([1,2]\)
to itself, with multiplier \(9/8\).

Now supply a negative rational \(m\) of odd numerator and denominator a
power of three, and exact reference words

\[
 128m+1\xrightarrow{w_s}-1,
 \qquad 64m+1\xrightarrow{w_t}-5.
\tag{2}
\]

Let \(r_s,r_t\) be their lengths and \(A_s,A_t\) their exponent sums.
Define

\[
 E_s=A_s-r_s-11,\qquad F_t=2A_t-3r_t-8,
 \qquad b=2E_s-F_t,\qquad a=3E_s-F_t.
\tag{3}
\]

Suppose \(a,b\ge0\), the denominator of \(m\) divides \(3^b\), and
\(2^a<3^b\). Set

\[
 L=2^a/3^b,\qquad M'=L(M+1)+m
     =\frac{2^aM+c}{3^b},\qquad c=2^a+3^bm\in\mathbb Z.
\tag{4}
\]

There are nonnegative numbers of the two reference cycles that can be
appended to the words in (1) and (2) so that their **affine endpoint
functions** agree on both arms under (4). Moreover, among scales of the
form \(2^a/3^b\), (3) is forced by this particular two-cycle matching.
This uniqueness concerns the specified terminal cycles and given prefixes;
it does not exclude other intermediate relations or cycles.

### Proof of the cycle equations

Put

\[
 \delta_s=r_s-7-b,\qquad
 \delta_t=(r_t-6-b)/2.
\tag{5}
\]

The second number is integral: (3) gives \(b\equiv r_t\pmod2\).
Append \(\max(\delta_s,0)\) copies of \([1]\) to the old source word
and \(\max(-\delta_s,0)\) copies to the new source word. Append
\(\max(\delta_t,0)\) copies of \([1,2]\) to the old target word and
\(\max(-\delta_t,0)\) copies to the new target word.

The reference constants agree by (1)--(2). Write \(\Delta=M+1\). The
old perturbations of the two inputs are \(128\Delta,64\Delta\), and the
new perturbations are \(128L\Delta,64L\Delta\). A word with \(r\)
odd inputs and exponent sum \(A\) multiplies a perturbation by
\(3^r/2^A\).

On the source arm, equality of slopes therefore requires

\[
 -b=7-r_s+\delta_s,
 \qquad a=A_s-18-\delta_s,
\]

or \(a-b=E_s\). On the target arm the corresponding equations are

\[
 -b=6-r_t+2\delta_t,
 \qquad a=A_t-13-3\delta_t,
\]

or \(2a-3b=F_t\). Solving the two linear equations gives exactly (3).
Choosing positive and negative parts as above makes every actual repetition
count nonnegative. This proves the assertion.

## NT2. Exact tail removal and ordinary realization

Put \(J(z)=4z+1\). For every positive odd \(z\),

\[
 3J(z)+1=4(3z+1),\qquad U(J(z))=U(z).
\tag{6}
\]

Hence positive odd \(z\) and \(J(z)\) have the same convergence status.

Two words with the same affine endpoint can first have their common
terminal exponent suffix removed. At the first unequal terminal exponents
\(u,v\), if \(u-v=2k\) is even, remove these terminal steps too. Their
new endpoints then satisfy

\[
 S=J^k(V)=4^kV+(4^k-1)/3.
\tag{7}
\]

For negative \(k\), this means \(V=J^{-k}(S)\). Both actual endpoints
will be positive odd integers. Formula (7) follows directly by solving
\((3S+1)/2^u=(3V+1)/2^v\). This tail removal often lowers the precision
needed to realize the reference words. It recovers the \(J^2\) device of
PR164 and also shortens its target words by a \(J\) device.

After optional tail removal, let the four retained exponent sums be
\(B_s,B'_s,B_t,B'_t\). It suffices initially to choose

\[
 K\ge\max\{2,B_s-6,B_t-5,B'_s-a-6,B'_t-a-5\}.
\tag{8}
\]

Increase \(K\), if necessary, until

\[
 2^a(2^K-1)+c>0,
 \qquad (3^b-2^a)(2^K-1)>c.
\tag{9}
\]

Such a finite \(K\) exists because \(2^a<3^b\). Require

\[
 M>0,\qquad M\equiv-1\pmod{2^K},\qquad
 M\equiv-c\,2^{-a}\pmod{3^b}.
\tag{10}
\]

Then \(M'\) in (4) is an odd positive integer strictly smaller than
\(M\), and all four retained words are exact ordinary prefixes. Thus

\[
 X(M)\in E\Longleftrightarrow X(M')\in E,
 \qquad
 Y(M)\in E\Longleftrightarrow Y(M')\in E,
\tag{11}
\]

and in particular \(\mathcal C(M)\Longleftrightarrow\mathcal C(M')\).

### Proof that every intermediate state is ordinary

Write \(M=-1+2^Kt\), \(t\ge1\). After a prefix with cumulative
exponent \(A_i\), an old source perturbation has 2-adic valuation
\(K+7-A_i\ge1\), and an old target perturbation has valuation
\(K+6-A_i\ge1\). The corresponding new-arm bounds are
\(a+K+7-A'_i\ge1\) and \(a+K+6-A'_i\ge1\).
All denominators here are odd. Thus each actual lifted endpoint is its
2-adically odd reference endpoint plus an even perturbation.

The congruence modulo \(3^b\) makes the new starting parameter integral.
Every starting value is positive. Inductively, the prescribed exponent
therefore divides \(3n+1\) exactly, the next endpoint is an odd integer,
and positivity is preserved. This proves legality, not just equality of
rational affine formulas. Conditions (9) prove \(0<M'<M\) for every
\(M\ge2^K-1\). Oddness of \(M'\) follows because it is an odd reference
\(m\) plus an even 2-adic perturbation. Finally (6)--(7) prove (11).

## NT3. A complete supplied witness is transported without a rank cap

Suppose retained source prefixes end at \(S=J^k(V)\), and a full
witness for the old source is supplied. Remove its forced prefix. Its
remaining exponent word is \([d,d_2,\ldots]\). Replace its first
exponent by \(d-2k\), then prepend the new source prefix. Formula (6)
proves that this is a witness for the new source. If the original witness
ended before the prescribed prefix or left an empty tail, first append
enough exponent-2 loops at 1. These are valid witnesses, and deterministic
trajectory uniqueness forces the prescribed prefix to agree. The adjusted
exponent is positive because it is the actual valuation at \(V\).

The same operation on the target arm works in either direction. Thus a
recursive solver can:

1. transform the entire supplied source witness to \(X(M')\);
2. invoke the smaller assertion \(\mathcal C(M')\);
3. transform any returned target witness back to \(Y(M)\).

No bound on the length or cumulative final exponent of the supplied or
returned witness is assumed. Switching among any number of compiled contracting
templates preserves the common strict rank \(M'<M\). It cannot produce
an infinite chain of successful recursive calls. It may, however, stop at
an uncovered parameter; that result must be **UNRESOLVED**, not success.

For the eight concrete templates below the retained prefixes all end above
1, so no padding is necessary. The source conversion changes the witness
length and total shortcut clock (the cumulative final exponent \(A_r\))
by \((+b,+a)\), while the child-target-to-parent conversion changes them
by \((-b,-a)\). The final letter of the exponent word is not what is
being counted here. These opposite changes express a
physical prefix replacement. They do not furnish a global bound on target
witness size.

## Eight exact instances

All rows have the common binary condition \(M\equiv-1\pmod{2048}\).
The ternary condition is \(M\equiv\rho\pmod{3^b}\), and
\(M'=(2^aM+c)/3^b\).

| Reference \(m\) | \(a\) | \(b\) | \(c\) | \(\rho\) | First \(M\) | First \(M'\) |
|---|---:|---:|---:|---:|---:|---:|
| \(-197/243\), PR164 | 7 | 5 | -69 | 48 | 292863 | 154265 |
| \(-29/27\), PR164 | 9 | 6 | -271 | 674 | 774143 | 543705 |
| \(-755/729\) | 9 | 6 | -243 | 486 | 980991 | 688981 |
| \(-1039/729\) | 11 | 7 | -1069 | 779 | 761855 | 713433 |
| \(-3125/2187\) | 11 | 7 | -1077 | 480 | 4052991 | 3795393 |
| \(-3101/2187\) | 11 | 7 | -1053 | 1377 | 3137535 | 2938121 |
| \(-3011/2187\) | 11 | 7 | -963 | 2007 | 3063807 | 2869079 |
| \(-1603/2187\) | 10 | 7 | -579 | 2100 | 3223551 | 1509335 |

The ternary cylinders in this table are disjoint. Their relative density
inside the common binary cylinder is
\(3^{-5}+2\cdot3^{-6}+5\cdot3^{-7}=20/2187\). This is an exact
coverage count for this finite catalog, not a density statement about all
successful templates or about all Collatz certificates.

### An explicit new positive table

For the third row put

\[
 M=1492992j+980991,\qquad M'=1048576j+688981,
 \qquad j\ge0.
\]

Here \(M'=(512M-243)/729\), \(0<M'<M\), and the exact ordinary
prefixes are:

| Start | Exponent word | Endpoint |
|---|---|---|
| \(X(M)\) | \([2,2,2,1,2,4]\) | \(17006112j+11174101\) |
| \(X(M')\) | \([2,2,2,1,1,1,2,1,1,3,3,7]\) | \(1062882j+698381\) |
| \(Y(M)\) | \([2,2,3,1]\) | \(30233088j+19865069\) |
| \(Y(M')\) | \([2,2,5,1,1,1,1,1,3,2]\) | \(7558272j+4966267\) |

The first endpoint is \(J^2\) of the second, and the third is \(J\)
of the fourth. At every prefix the constant endpoint is positive odd and
the coefficient of \(j\) is an even positive integer. These observations,
or the direct divisions in the companion replay, prove the table for every
\(j\), not merely for its first entry.

## The singular rank-five state is still unresolved

The current rank-five adversarial family has

\[
 e=119+162j,\quad P=2^e,\quad
 M=(8P-22)/243.
\tag{12}
\]

Its source reaches 1 in five odd inputs, while its target reaches \(P-1\).
The natural reference center is \(M_0=-22/243\). At that center the
upper reference follows \([2,2,2,5,1]\) to **zero**, while the lower
reference follows \([2,2,2,1,2]\) to \(-1\). The last upper division
is a finite algebraic shortcut step at a zero numerator, not an exact
accelerated odd valuation. For the actual positive lift it instead leaves
the power of two \(2^{e-2}\), which then halves to 1.

This source-zero/target-minus-one state is not a permitted input of NT1.
It cannot be silently treated as another odd reference cycle. In
particular, the supplied upper certificate does not resolve its target's
long shadow of \(-1\).

One can set up a separate candidate grammar: a new upper reference ending
at zero after \(d\) odd inputs, and a new lower reference ending at
\(-1\) with \(r_t\) odd inputs and exponent sum \(A_t\). Matching the
two arms would force

\[
 b=d-5,\qquad a=b+A_t-r_t-4.
\tag{13}
\]

Its integrality condition on the family (12) and strict inequality
\(2^a<3^b\) must both be checked. No construction covering the family
(12) is obtained from (13). This is not an exclusion theorem for that
grammar. Higher ranks, different reference cycles, and transformations not
based on this particular affine grammar remain available.

The precise global gap is therefore coverage: prove that every eligible
certified parameter reaches a certified base case or an applicable strict
descent, allowing the complete supplied witness to select the rule. The
eight-row catalog already leaves \(M=2047\) uncovered. Neither this
uncovered integer nor any failed template search is a Collatz counterexample.

## Executable evidence

`negative_template_compiler.py` checks both reference words and affine
slopes, performs the cycle synchronization and suffix removal, derives the
ordinary congruences, and validates all four ordinary affine tables for
each of the eight rows. It also reconstructs supplied witnesses in both
directions and checks terminal padding on four ordinary parameters per row.
The normal and optimized runs must agree. Its status explicitly retains
`full_claim: OPEN`.

The symbolic argument is the proof of each infinite progression. The
ordinary witness fixtures and malformed-input checks are finite evidence
for the implementation. Neither internal reconstruction nor repository
validation is a proof-assistant verification or external acceptance.
