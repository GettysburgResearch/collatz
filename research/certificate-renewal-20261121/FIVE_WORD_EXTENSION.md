# Five transport through valuation-one and valuation-three prefixes

**PROPOSED elementary theorems and an exact finite coefficient certificate.**
The physical five-closure law remains open. This note enlarges its proved
certificate language and its contracting energy domain. The contraction
coefficient is weaker than PR166's coefficient on the smaller domain; the
advance is coverage, including new words beginning with valuations one
and three.

Let

\[
 T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
 \qquad U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n>0\text{ odd}),
\]

and let C be the actual basin of 1. Write \(I_a(q)=(2^a q-1)/3\) only
for a positive odd integer result, with a a positive integer. A word lists
exact accelerated division exponents in forward order. A repeated letter
\(2^{[r]}\) below means r copies of the exponent two, not exponentiation.

## Frozen sources and the new scope

| Source | Full SHA | Inspected path and dependence |
|---|---|---|
| PR157 | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, GCM-001/002: five-closure on certified odd ternary units is equivalent to full Collatz. `closing-attempts.md`, GCL-001/002: the unresolved rank-one family and uniform inverse-lift obstruction. |
| PR160 | `6d877e718f5ef9d57fe1830912c444359718747a` | `research/closure-attacks-20261120/merger/PHYSICAL_CERTIFICATE_BOUNDARY.md`, PC-002/003: a proportional return can increase height; repeating one expanding word has a valuation bound. No universal return-descent claim is made here. |
| PR162 | `2279da37ac612dbe049777354cdedb3c0aa03282` | `research/creative-closure-20261120/five_closure.md`, C5-001/002: the two-odd-step block `(2,b) -> (5,b-3)` and its complete supplied rank-two family. The block A below is inherited. |
| PR166 | `5996b9f525ca50978bc34f423192c36a87765bf3` | `research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`, FL1–FL4, and `LADDER_RENEWAL.md`: the complete valuation-two ladder, density 1/24 and subcritical renewal. Its ladder is included unchanged. |
| PR146 | `fd991063721e9c157d318e40bb20131762f7d750` | `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`: transport of every five comparison into a sufficient progression beginning `(1,3,3,3,3,3,3)`; and its smaller five comparisons for the surviving rank-five Mersenne family. `LEAST_FAILURE_SIEVE.md`: sparse sufficient adjacent tests and least-failure qualification. These were refreshed after the initial PR166 reading. |

The new results are the general extension identity FW2, seven additional
seed families, the complete compiler on their disjoint union, its density
23/384, and subcritical renewal on that larger domain. No priority beyond
these inspected repository statements is asserted. The source theorem
relating full five-closure to Collatz remains separately qualified; none
of the proofs below assumes five-closure.

## FW1. Exact correction decoding decides a fixed homogeneous block

For a prefix \(a=(a_1,\ldots,a_{p-1})\) of positive exponents, put

\[
 S(a)=\sum_{j=1}^{p-1}a_j,
 \qquad
 C(a)=\sum_{j=0}^{p-1}3^{p-1-j}2^{a_1+\cdots+a_j}.
\]

The empty sum in the exponent is zero. Appending a final exponent b gives

\[
 I_{a_1}\cdots I_{a_{p-1}}I_b(q)
   =\frac{2^{S(a)+b}q-C(a)}{3^p}.                         \tag{1}
\]

Suppose another prefix d of the same length satisfies

\[
 C(d)=5C(a),\qquad \Delta=S(d)-S(a),\qquad b-\Delta\ge1.
                                                                  \tag{2}
\]

For every legal positive source word \((a,b)\), with endpoint q,

\[
 5I_a I_b(q)=I_d I_{b-\Delta}(5q).                         \tag{3}
\]

Both ordinary paths have p odd inputs and the same shortcut clock
\(S(a)+b\). All target inverses are integral, positive and odd.

**Legality proof.** Equation (1) and (2) give an integer full inverse
numerator on the target arm. Reducing that numerator modulo three forces
the last inverse division to be integral. Divide and repeat to obtain
integrality at every inverse step. Every exponent is positive, so every
integral inverse output is odd. Starting at the positive odd endpoint 5q,
every such integral output is positive. Thus (3) is an ordinary physical
identity, not merely an equality of rational affine expressions.

For fixed p and a positive correction c there is at most one prefix d
with \(C(d)=c\). The following finite algorithm finds it or rejects:

1. If p=1, accept precisely c=1 and return the empty prefix.
2. For p>1, subtract \(3^{p-1}\). If the remainder R is not positive
   and even, reject. Otherwise its exact valuation is the first exponent
   \(d_1=v_2(R)\).
3. Replace c by \(R/2^{d_1}\), decrease p by one, and continue.

This is complete because after extracting \(2^{d_1}\), the remaining
correction is odd and has exactly the same form with one fewer term.
In particular, a fixed source word admits a homogeneous five transport
with the same odd count and clock exactly when the decoding of 5C(a)
succeeds and its last odd position is before that clock. Equality of
slopes already forces equal clocks and odd counts for any fixed-word
homogeneous identity on two distinct source values. The decoding statement
therefore does not omit a different fixed-word homogeneous choice.

## FW2. An unbounded extension of every suitable seed

Suppose a and d satisfy (2) with \(\Delta=3\) and the last entry c of d
is at least two. For every r>=1 define

\[
 a_r=(a,2^{[r]}),\qquad
 d_r=(d_1,\ldots,d_{p-2},c-1,2^{[r-1]},3).
\]

Then

\[
 C(d_r)=5C(a_r),\qquad S(d_r)-S(a_r)=3.                 \tag{4}
\]

Thus the block \((a_r,b)\), b>=4, transports to
\((d_r,b-3)\) for arbitrarily long two-runs.

For the one-letter extension let A=S(a), B=S(d)=A+3. Appending a two to
a gives correction \(3C(a)+2^{A+2}\). Replacing the last target exponent
c by c-1,3 gives

\[
 3\big(C(d)-2^B\big)+3\cdot2^{B-1}+2^{B+2}
 =3C(d)+\tfrac52 2^B
 =5\big(3C(a)+2^{A+2}\big).
\]

The new target last exponent is three, so the operation can be repeated
indefinitely. This proves (4) without extrapolating a finite replay.

## FW3. Eight disjoint source families

Use the following seeds. Row A and all its extensions are the existing
PR166 ladder; the other seven rows supply additional source cylinders.
An extendable seed permits any r>=0 in FW2, where r=0 means the original
seed. The remaining rows use r=0 only.

| Row | Source prefix a | Target prefix d | Minimum b | Extendable | C(a) |
|---|---|---|---:|---|---:|
| A | `(2)` | `(5)` | 4 | Yes | 7 |
| B | `(1,1,1)` | `(1,2,5)` | 6 | No | 65 |
| C | `(1,1,2)` | `(1,5,1)` | 4 | No | 73 |
| D | `(1,1,4)` | `(1,3,5)` | 4 | Yes | 121 |
| E | `(3,1,1,4)` | `(2,4,1,5)` | 4 | Yes | 1049 |
| F | `(2,1,1,4)` | `(3,2,1,5)` | 4 | Yes | 565 |
| G | `(3,1,1,2)` | `(2,4,3,1)` | 4 | No | 665 |
| H | `(2,1,1,2)` | `(3,2,3,1)` | 4 | No | 373 |

The table's corrections satisfy C(d)=5C(a) by direct integer arithmetic.
Row B has Delta=5 and every other row has Delta=3. FW1 and FW2 prove all
listed transports, including all b and all extension lengths.

Let H be the union of their initial-word cylinders, restricted to odd
positive ternary units. They are disjoint. Rows B,C,D begin respectively
`111`, `112`, `114`; E,G begin `3114`, `3112`; F,H begin `2114`, `2112`.
Row A starts with a nonempty two-run followed by an exponent at least
four. In an extended row the first exponent after its specified two-run
is at least four, so different run lengths are disjoint as well.

For a fixed prefix a and threshold m, the condition that the next exponent
is at least m is exactly the single binary residue

\[
 x\equiv-C(a)(3^p)^{-1}\pmod{2^{S(a)+m}}.                \tag{5}
\]

One can check the earlier exact exponents by reversing the integral full
word from the positive integer endpoint at clock S(a)+m; that endpoint
may be even, supplying additional terminal halvings. Thus its density
among odd integers, or among odd ternary units, is
\(2^{1-S(a)-m}\). The latter equality follows by the Chinese remainder
theorem, since (5) has a power-of-two modulus.

The contributions of A through H are respectively

\[
 \frac1{24},\ \frac1{256},\ \frac1{128},\ \frac1{384},\
 \frac1{3072},\ \frac1{1536},\ \frac1{1024},\ \frac1{512}.
\]

Each extendable row sums a geometric factor \(\sum_{r\ge0}4^{-r}=4/3\).
Its tail lies in one increasingly fine binary cylinder, whose density
and upper density tend to zero. Hence the infinite union has the natural
relative density

\[
 \boxed{\quad \operatorname{dens}_{\mathrm{odd},3\nmid}(H)
        =\frac{23}{384}.\quad}                          \tag{6}
\]

The former ladder contributes 16/384; the added cylinders contribute
7/384. This is a statement about the transport domain, not about the
density of known convergers or a complete cover.

### Every covered query has a smaller actual endpoint

For x in H let q be its endpoint after the identified block. Then

\[
 T^L(x)=q,\qquad T^L(5x)=5q,\qquad 3q\le x.             \tag{7}
\]

The endpoint is a positive odd ternary unit because it is an actual
positive odd successor. To see the height bound, row A has
\(I_2^rI_b(q)\ge I_b(q)\ge5q\), for r>=1,b>=4. For rows D,E,F the
additional two-run only increases the inverse source, because
\(I_2(v)\ge v\) for v>=1 and each outer inverse affine map is increasing.
At r=0 and minimum b, the lower bounds x/q obtained from (1) are
903/81, 7143/243 and 3531/243, respectively. Rows B,G similarly give
447/81 and 1383/243. Each exceeds three.

For row C, (5) is x=135 modulo256, so x>=135 and
\(q\le(81x+73)/256\le x/3\). For row H it is x=521 modulo1024, so
\(q\le(243x+373)/1024\le x/3\). This proves (7) everywhere on H.

Consequently a globally least failed five-closure antecedent cannot lie
in H: a failure at x would give a smaller certified q with a failure at
5q. This only excludes the stated domain from least failure.

## FW4. Complete compilation on the enlarged word language

Take a supplied complete first-hit certificate for x. If its exponent
word is a concatenation of the blocks in FW3, replace each block by its
target word and append the final exponent four, the edge 5 to 1. The
result is a complete first-hit certificate for 5x. If the source has p
odd inputs and shortcut clock N, the target has exactly p+1 and N+4.

Parsing is unambiguous by the disjoint-prefix argument. It consumes a
complete finite block on each iteration. Physical legality follows from
FW1 and composition on the actual endpoints. No target prefix can hit
1 early: its stated odd endpoint is 5q>=5, whereas U fixes 1. Source
prefixes similarly cannot hit 1 before a later exponent at least four.
Thus the output first-hit counts are exact, rather than merely upper
bounds from a padded certificate.

The empty certificate at x=1 produces the known word (4) for 5. A valid
input certificate outside the language returns `UNRESOLVED`; malformed
certificates are rejected. In particular the certificate (4) for x=5
remains outside this compiler. One is not entitled to use the compiler's
finite parsing termination as successful transformation on every input.

## FW5. The larger domain still contracts at exponent 21/25

Let f be any label in a metric space satisfying f(Tn)=f(n) on every
positive ordinary integer. Put

\[
 d_5(q)=d(f(5q),f(q)),\qquad s=21/25,
\]

and let E_s(X) be the sum of \(q^{-s}d_5(q)\) over odd ternary units
q<=X. Let R_s(X) be the same sum restricted to the complement of H.
Then

\[
 \boxed{E_s(X)\le R_s(X)+\frac{249}{250}E_s(X/3).}         \tag{8}
\]

In particular

\[
 \boxed{E_s(\infty)<\infty\iff R_s(\infty)<\infty,
 \qquad E_s(\infty)\le250R_s(\infty)
 \text{ when finite}.}                                 \tag{9}
\]

The key coefficient in (8) has a complete finite exact-arithmetic
certificate. Its derivation, unbounded tails and exhaustive domain are
spelled out next. It is not a statistic inferred from the 680 numerical
path replays in the accompanying checker.

### The full inverse fiber, including its unit guard

Fix a source prefix a with p odd inputs after appending b. Its inverse
sources for a fixed odd ternary unit q are

\[
 x_b=\frac{2^{S(a)+b}q-C(a)}{3^p},\qquad b\ge b_{\min}.
                                                                  \tag{10}
\]

Integrality requires
\(2^{S(a)+b}q=C(a)\pmod{3^p}\). The order of two modulo \(3^p\) is
\(P_p=2\cdot3^{p-1}\), so integral exponents form one progression.
The exact condition \(3\nmid x_b\) can remove members and must be retained
in the coefficient estimate. If its first member is a nonunit, the first
permitted member is at least one full period later.

The endpoint q=1 contributes zero because 5 reaches1. Every remaining
odd ternary-unit endpoint has q>=5. Since C(a)>0, the progression obeys
\(x_{b+jP_p}\ge2^{jP_p}x_b\). It follows that if b_0 is any valid lower
bound for the first permitted exponent, then the whole inverse fiber has

\[
 \sum_{b\text{ legal},\,3\nmid x_b}x_b^{-s}
 \le q^{-s}
 \left(\frac{3^p}{2^{S(a)+b_0}-C(a)/5}\right)^s
 \frac1{1-2^{-sP_p}}.                                  \tag{11}
\]

The bound remains valid if some nonunit later terms are included on the
right. All coefficients used below have a positive denominator and a
ratio strictly below one. The checker verifies this directly whenever
it evaluates the ratio; its very-small-term branch proves a stronger
bound before constructing a potentially huge power of two.

### A ternary residue cell supplies a safe b_0

A cell is q=Q modulo \(3^k\), with k>=5 and Q prime to three. Use
j=min(p,k) digits to find the least b>=b_min solving

\[
 2^{S(a)+b}Q=C(a)\pmod{3^j}.                            \tag{12}
\]

It is a lower bound for the true first exponent even if p>k. If p<k,
the cell also knows the residue modulo \(3^{p+1}\). When
\(2^{S(a)+b}Q-C(a)=0\pmod{3^{p+1}}\), the first integral source is
excluded by the unit guard, so replace b by b+P_p. This replacement is
safe for every q in the cell. These are the only deletions required in
the certificate; no source-specific numerical convergence is assumed.

### The entire tail in the two-run length

For the ladder use an empty stem P and r>=1. For D,E,F use the fixed
source stem in the table and r>=0. Thus all four families have words
\((P,2^{[r]},b)\), b>=4. Let the stem length be h, its total exponent
S, and write

\[
 I_P(z)=a_P z-b_P,\qquad a_P=2^S/3^h.
\]

Their values at z=1 are respectively 1,5/3,37/9,17/9, all positive.
The exact inverse source is

\[
 x=I_P(1)+a_P(4/3)^r(2^bq-4)/3.
\]

For r>=k, its integrality necessarily implies
\(q2^{b-2}=1\pmod{3^k}\). Let b_*>=4 be the least exponent satisfying
this condition on the cell. For q>=5 the source bound is

\[
 x\ge \frac{a_P}{3}(4/3)^r(2^{b_*}-4/5)q.
\]

For each r its actual exponent period is at least \(2\cdot3^k\).
Summing over every r>=k, and all its legal exponents, is therefore bounded
by q^-s times

\[
 \left(\frac{3}{a_P(2^{b_*}-4/5)}\right)^s
 \frac{(3/4)^{ks}}{1-(3/4)^s}
 \frac1{1-2^{-2s3^k}}.                                 \tag{13}
\]

This upper bound includes the entire infinite tail, with any incompatible
ternary digits or nonunit sources conservatively restored. For r<k,
use (11) separately. Use (11) for each of the four nonextendable rows as
well. Their sum is a proved column bound \(B(Q,k)\) on that cell.

### The complete exact coefficient certificate

The checker begins with all 162 unit residues modulo243. A cell whose
rational upper bound exceeds 249/250 is replaced by its three ternary
lifts. The only cells requiring subdivision are

| Depth k | Residue Q to subdivide |
|---:|---:|
| 5 | 61 |
| 6 | 547 |
| 7 | 547 |
| 8 | 4921 |
| 9 | 4921 |
| 10 | 44287 |
| 11 | 44287 |
| 12 | 398581 |
| 13 | 398581 |
| 14 | 3587227 |
| 15 | 3587227 |

These are the residues of 1/4 in the respective ternary moduli. Every
subdivision replaces one full congruence class by its three disjoint
children. The resulting 184 leaves, at depths at most16, are an exhaustive
disjoint cover of all positive odd ternary units by their ternary residues.
Their normalized residue mass sums exactly to2/3. Every leaf has
\(B(Q,k)<249/250\). The largest certified upper bound occurs at Q=205,
k=5. The exact list and rational values have the deterministic hash
reported by the checker.

There are no floating-point comparisons in this verification. For a
positive rational z<=1, `power_upper` returns an upper bound of z^(21/25)
with denominator \(10^{12}\), checking the integer inequality

\[
 c^{25}\operatorname{den}(z)^{21}
 \ge10^{300}\operatorname{num}(z)^{21}.
\]

It also checks the strict reverse inequality at c-1. Each geometric
factor uses
\(2^{-21P/25}\le2^{-\min(\lfloor21P/25\rfloor,160)}\).
For (13), replace \((3/4)^s\) by its rational upper bound; the function
\(g^k/(1-g)\) is increasing on (0,1).

The checker avoids constructing astronomically large powers in tiny
terms using a conservative exact branch. In (11), if
\(L=S+b\ge\max(\operatorname{bitlength}(C)+1,2p+201)\), then its ratio is
less than \(2^{-200}\), whose s-th power is at most \(2^{-168}<2^{-160}\).
The bound \(2^{-160}\) is then used before the geometric factor.
For (13), b>=2(h+1)+210 similarly bounds the ratio's s-th power by
\(2^{-160}\). These are upper bounds, never deletions or underflow zeros.

### Finish the energy proof with finite cutoffs

Each x in H has exactly one identified block and endpoint q. Ordinary
invariance gives d_5(x)=d_5(q), and (7) gives q<=X/3 whenever x<=X.
Summing the complete column bound just proved yields (8). Every cutoff
sum is finite and nonnegative. Replacing E_s(X/3) by E_s(X), subtracting
the finite 249E_s(X)/250, and then taking increasing cutoffs proves (9).
No subtraction of two infinite energies is used.

## What is still missing

Neither (8) nor (9) bounds the energy on the complement. The latest PR146
source makes this particularly concrete: its single sufficient five-test
progression begins with `(1,3,3,3,3,3,3)`, and is entirely outside H. Its
rank-five Mersenne construction also has a five antecedent beginning with
`(1,3)` for the stated exponents, so these new blocks do not settle that
family. A source beginning with valuation one is not automatically in a
new row; its following letters matter.

That PR146 theorem transports every supplied five comparison into its
omitted progression, injectively and with a fixed multiplicative height
bound. Thus proving five-closure on the present complement is still
equivalent to proving it everywhere. Its weighted consequence also says
that all five energy can be concentrated in that omitted progression up
to a fixed rescaling. Conversely the already covered 49-modulo-64 ladder
class carries all five comparisons by a larger inverse lift. Neither the
new coverage fraction nor the two complementary energy transfers is an
absolute energy bound.

The old rank-one certificate (2a) is still unresolved by this compiler.
PR157 reduces its five companion to `(5*9^(a-1)-1)/4`. No argument here
proves convergence of every member of that residual family. Nor does a
finite or countable concatenation of successful cylinders establish a
complete terminating selector without a proof that every required input
admits the next block.

The precise remaining sufficient step is finite s-energy on all of H's
complement, or a different complete certificate transformation. The
result supplies a broader ordinary-domain renewal with a checked strict
coefficient; it supplies neither of those missing global statements.

## Reproduction and evidence levels

Run `python -X utf8 -B check_five_word_extension.py` in this directory.
The same command with `-OO` retains every check. The output separately
records:

- 40 exact correction/extension instances, supporting the implementation
  of the unbounded algebraic proof;
- 680 bounded paired ordinary replays and28 successful complete compilers,
  including composed words, plus four malformed controls and the valid
  unresolved source5;
- the 184-leaf exact coefficient certificate with all tail bounds, which
  verifies the infinite inverse-column inequality through a finite
  exhaustive arithmetic cover.

The all-parameter ordinary identities follow from FW1–FW3, the compiler
from FW4, and the energy bound from (10)–(13) plus the exact coefficient
certificate. No finite target census is used as a universal convergence
proof, and no formal proof-assistant build is claimed.
