# A rederived valuation-one block, a short renewal proof, and a rank-two residual

**PROPOSED. Full forward-five closure and Collatz remain OPEN.**
All paths below are ordinary positive integer trajectories for the shortcut
map T(n)=n/2 on even inputs and T(n)=(3n+1)/2 on odd inputs. Let U be its
odd acceleration and write I_a(q)=(2^a q-1)/3 only when the result is a
positive odd integer. A word lists exact accelerated division exponents.

## Source comparison

**Latest-head correction to the initial comparison.** During final review,
PR168 at `e4599b32e4b1a955ac9315d46782d4ad6a5db96c`,
`research/closure-frontier-20261121/FIVE_RETURN_LANGUAGE.md`, FR1--FR4,
and PR169 at `6cb9bfdc828f91576066b0e4a099d47d8144e915`,
`research/certificate-renewal-20261121/FIVE_WORD_EXTENSION.md`, FW1--FW5,
were found and read. PR168 already contains the exact triple-one block,
its cylinder, its closed first-hit family, and a strictly larger complete
balanced-word recognizer. PR169 contains the same block as row B in a
different larger grammar. Accordingly V1 and V2 below are independent
rederivations and checks of those results, not new transport families.

V3 provides a short proof with only two endpoint classes for the smaller
A+B union. Its cutoff X/6 is specific to that smaller union. PR168 proves
the stronger coefficient 903/1000 on a larger domain with cutoff X/2,
and PR169 proves coefficient 249/250 on another larger domain with cutoff
X/3. V3 is a table-free cross-check, not an improvement in coverage or in
the strongest known coefficient. V4's explicit rank-two residual was not
found in these inspected main proofs or their closing-attempt ledgers.
This is a repository-source comparison, not a literature priority claim.

The additional refresh PR167 at
`e83cc8b35ad614c616df7c00318cc9645a174c34`,
`research/least-failure-closure-20261121/EXPANDED_FIVE_RENEWAL.md`,
ER1--ER3, also contains the same triple-one block. Its larger domain has
relative density 85/1536 and a joint 21/25 coefficient 91/100, with cutoff
X/3. This reinforces the independent-rederivation status of V1--V3.

PR166 at `5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
FL1--FL3, gives the complete family of initial blocks `(2 repeated r times,b)`,
r>=1,b>=4. Its `LADDER_RENEWAL.md` proves subcritical renewal on their
disjoint union. The older r=1 block is credited there to PR162.

The latest PR146 at `fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`, localizes
the entire five problem into a sufficient residue class whose words start
`(1,3,3,3,3,3,3)`. Its Mersenne construction likewise leaves a first
valuation-one obligation. The new block below starts with three ones;
it does not settle that particular one-followed-by-threes obligation.

PR164 at `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`,
`research/witness-closure-512-2026-11-20/README.md`,
`continuation-descent.md`, `continuation-negative.md`, and
`continuation-j.md` supplies additional complete-witness transformations
for the different companion (x+1)/2. They were inspected for overlap and
do not furnish an unstated premise for the identity below.

## V1. Rechecking an ordinary first-valuation-one block

For every legal source word `(1,1,1,b)` from x to q, with b>=6,

\[
\boxed{5I_1^3I_b(q)=I_1I_2I_5I_{b-5}(5q).}                \tag{1}
\]

Both arms have four odd inputs and shortcut clock L=b+3. Thus

\[
T^L(x)=q,\qquad T^L(5x)=5q.                              \tag{2}
\]

**Proof.** The source has odd positions 0,1,2,3 and affine correction

\[
B=27+18+12+8=65,
\qquad x=(2^{b+3}q-65)/81.
\]

The target positions are 0,1,3,8; their correction is
`27+18+24+256=325=5B`. Its full inverse numerator is consequently
`2^(b+3)(5q)-325=81(5x)`. All its exponents are positive when b>=6.
Reduction modulo three and induction through the reversed word prove
integrality of every inverse division. Each resulting integer is odd
and positive. Starting from 5q>=5, no such inverse output can be one:
I_a(u)=1 would require 2^a u=4 with odd u>1. The source prefix also
avoids one, since I_b(q)>=21q for b>=6 and the displayed source
formula gives x>q; the three I_1 inverse steps decrease down to x.
This proves actual path legality
and the first-hit assertions, not just the affine equation.

The exact source domain is

\[
\boxed{x\equiv271\pmod{512}.}                            \tag{3}
\]

Indeed the first four source exponents impose
`81x+65=0 mod512`. Its unique binary residue is 271; conversely that
residue gives the exact first three exponents one and a fourth exponent
at least six. The endpoint q is an odd ternary unit and

\[
q\le(81x+65)/512\le x/6,
\]

because every positive source in (3) has x>=271. This cylinder is
disjoint from every prior FL3 cylinder: its first exponent is one,
whereas theirs is two. Its relative density among odd ternary units
is 1/256.

One literal example is

    271 -> 407 -> 611 -> 917 -> 43,
    1355 -> 2033 -> 1525 -> 143 -> 215=5*43,

with exponent words `(1,1,1,6)` and `(1,2,5,1)` and clock nine.

## V2. Rechecking complete certificate composition on the A+B language

Let a supplied complete first-hit word belong to the language generated
by the two kinds of blocks

    A: (2 repeated r times,b), r>=1,b>=4;
    B: (1,1,1,b), b>=6.

Use FL1 for A and (1) for B, then append the known edge 5->1 of
exponent four. This produces a complete first-hit certificate for 5x.
Every block preserves its odd count and shortcut clock, so the target
has exactly one more odd input and four more shortcut steps than x.
The parsing is unambiguous: the first letter selects the block type,
and a run of twos or the required triple of ones selects its end.
The compiler consumes a finite supplied word; it does not assume a
future stopping-time bound. Valid unsupported words remain UNRESOLVED.

An explicit closed family, already present in PR168 FR2, is

\[
x_k=(2^{54k+31}-65)/81,\qquad k\ge0.
\]

Its exact source word is `(1,1,1,54k+28)` and its exact target word is
`(1,2,5,54k+23,4)`. Integrality follows from `2^31=65 mod81` and
`2^54=1 mod81`. The same inverse-legality argument proves every
intermediate value, and no earlier hit occurs. Moreover x_k=2k mod3,
so k not divisible by three supplies the ternary-unit members.

Let H be the disjoint union of all old FL3 cylinders and the new B
cylinder, restricted to odd ternary units. Its relative density is

\[
\frac1{24}+\frac1{256}=\frac{35}{768}.
\]

This is the density of the whole initial-block domain, not a claim that
every input there has a complete word in the compiler language.

## V3. The whole enlarged domain still contracts at exponent .84

Let f be any ordinary T-invariant metric label and
`d_5(q)=d(f(5q),f(q))`. For s=21/25 define

\[
E(X)=\sum_{\substack{q\le X\\q\text{ odd},\ 3\nmid q}}
q^{-s}d_5(q),
\qquad
R(X)=\sum_{\substack{q\le X,\ q\notin H\\q\text{ odd},\ 3\nmid q}}
q^{-s}d_5(q).
\]

Then

\[
\boxed{E(X)\le R(X)+\kappa E(X/6),\qquad
\kappa=\frac{405749}{424576}<1.}                           \tag{4}
\]

Consequently full energy is finite if and only if the uncovered energy
is finite, with

\[
E(\infty)\le\frac{424576}{18827}R(\infty)
\quad\text{when }R(\infty)<\infty.                       \tag{5}
\]

The joint endpoint congruences are important here. Adding the earlier
coarse .84 coefficient to a separate coarse bound on the B-cylinder
would not establish contraction.

### Complete inverse-fiber bounds

Fix an odd ternary-unit endpoint q. For an A-block with run length r,
its sources are

\[
x_b=(2^{2r+b}q-B_r)/3^{r+1},\quad B_r=4^{r+1}-3^{r+1},
\]

with b>=4 in one progression modulo `P_r=2*3^r`; unit guards can
delete sources. Since B_r>0, successive sources grow by at least
the factor `2^P_r`. For B-blocks,

\[
y_b=(2^{b+3}q-65)/81,
\]

with b>=6 in one progression modulo54, and successive sources grow
by at least 2^54. These progressions follow from the exact orders of
two modulo the corresponding powers of three.

The contributions at q are d_5(q) times these complete positive
inverse-fiber sums. There are no duplicate source inputs: r is fixed
by the initial A-word, and the B-cylinder is disjoint from all A-cylinders.

The endpoint q=1 contributes zero because 5 reaches1. For other
endpoints q>=5, write t=(3/4)^s. We use the exact bounds

\[
t<393/500<4/5,\quad 64^{-s}<1/32,\quad
7^{-s}<1/5,\quad (5/52)^s<1/7,\quad (81/499)^s<1/4.
\tag{6}
\]

Each fractional-power comparison in this proof is an integer
comparison after raising to the positive power25.

### Case A: q is not seven modulo27

Every A-block with r>=2 has b>=5. A legal b=4 would require
`4q=1 mod3^(r+1)`, hence q=7 mod27, contrary to the case condition.

For r=1, FL3 gives x_b>=7q and progression period6. Its total
normalized inverse weight is less than `32/155` by (6).

For r>=2 and b>=5,

\[
x_b\ge(52/5)(4/3)^r q.
\]

Using q>=5, this follows from
`x_b=1+(4/3)^r(2^bq-4)/3`. Since P_r>=18, (6) gives

\[
\sum_{r\ge2}\sum_b(q/x_b)^s
<\frac17\frac{(4/5)^2}{1-4/5}\frac{32}{31}
=\frac{512}{1085}.
\]

Every B-block has y_b>=(499/81)q from b>=6 and q>=5. Its normalized
fiber sum is less than `(1/4)(32/31)=8/31`. Thus the complete combined
coefficient in this case is less than

\[
\frac{32}{155}+\frac{512}{1085}+\frac8{31}
=\frac{1016}{1085}<\kappa.                               \tag{7}
\]

### Case B: q is seven modulo27

The endpoint q=7 also has zero defect: both7 and35 have explicit ordinary
paths to1. Every remaining positive odd q in this class is at least61.
Therefore every A-block satisfies

\[
x_b\ge(324/61)(4/3)^r q.
\]

The exact bound `(61/324)^s<1/4`, together with (6), gives the complete
A contribution less than

\[
\frac14\frac{393}{107}\frac{32}{31}=\frac{3144}{3317}.
\]

For the B-block, integrality modulo27 gives
`2^(b+3)*7=65 mod27`, or `2^(b+3)=17 mod27`. The order is18 and
`2^15=17 mod27`, so b=12 mod18. In particular b>=12. Hence

\[
y_b\ge(32755/81)q.
\]

We have `(81/32755)^s<1/129` and `2^(-54s)<1/129`. Summing the full
period54 progression bounds its contribution by `1/128`. Combining,

\[
\frac{3144}{3317}+\frac1{128}
=\frac{405749}{424576}=\kappa<1.                         \tag{8}
\]

The source cutoffs are q<=x/7 for A and q<=x/6 for B. Summing the
preceding bounds over q<=X/6 proves (4). At finite X, E(X/6)<=E(X),
so subtracting the finite quantity kappa E(X) proves (5) by monotone
limits. No subtraction of infinite sums is used.

For reference, the harmonic case also contracts on this enlarged union:
the earlier A coefficient16/21 plus the B coefficient
`1/[6(1-2^-54)]` is less than14/15. The subcritical proof above is the
two-class residue argument; the newer PR168 and PR169 bounds cover larger
domains as specified in the source comparison.

## V4. A different first-valuation-one family remains a genuine residual

For k>=0 put

\[
z_k=(2^{6k+5}-5)/9.
\]

It has the exact first-hit source word `(1,6k+4)`, and z_k=2k mod3.
The target has the unconditional finite identity

\[
\boxed{T^{6k+8}(5z_k)=\frac{5(3^{4k+2}-1)}8=:w_k.}       \tag{9}
\]

Before this endpoint the target has exactly4k+4 odd inputs and every
intermediate value exceeds1. The endpoint w_k is an odd integer at
least5. Therefore any eventual first-hit target certificate must have
at least4k+5 odd inputs, although the source rank is exactly two.

To prove (9), two odd shortcut steps give
`T^2(5z_k)=5*2^(6k+3)-5`. The negative-five shadow block sends
`-5+2^e c` to `-5+9*2^(e-3)c` in three shortcut steps, with two odd
inputs, whenever e>=4 and c is positive odd. Apply it 2k times to
reach `40*81^k-5`. Three more shortcut steps give
`45*81^k-5=5(3^(4k+2)-1)`, which has exact two-adic valuation three.
Three halvings now give w_k. The explicit formulas prove positivity
and the odd counts throughout.

This is a first-letter-one version of the already known general
rank-expansion boundary in PR157 `closing-attempts.md`, not a claim
that source-rank-only bounds were previously possible. It gives the
precise residual on the new domain. Convergence of every w_k is not
proved. For k=1 the supplied source is227 and its multiplied companion
reaches455 at clock14; the A+B compiler correctly leaves `(1,10)`
unresolved.

## V5. No balanced return on a one-then-threes prefix

For every integer r>=0 and every positive b, the source word

\[
w=(1,\underbrace{3,\ldots,3}_{r\text{ letters}},b)
\]

has no balanced five-return word. Here balanced means the target has the
same odd count and shortcut clock and satisfies the affine identity
`5I_w(q)=I_v(5q)` on its ordinary source cylinder. This specializes the
complete correction decoder of PR168 FR1 and PR169 FW1 to the prefix
that occurs in the critical PR146 Mersenne comparison.

**Proof.** Put p=r+2. The source correction is

\[
B=3^{r+1}+2\sum_{j=0}^r3^{r-j}8^j
 =\frac{3^{r+2}+2^{3r+4}}5.
\]

A balanced target would have correction
`M_0=5B=3^p+2^(3r+4)`. Decode the target odd positions by subtracting
the leading power of three and dividing by the exact power of two in
the remainder. At step j, for 0<=j<=p-2,

\[
M_j=3^{p-j}+2^{3r+4-j},\qquad
M_j-3^{p-1-j}
 =2\left(3^{p-1-j}+2^{3r+3-j}\right).
\]

The parenthesis is odd, so every one of these divisions has exact
exponent one. The final normalized remainder is therefore

\[
M_{p-1}=3+2^{2r+3}>1.
\]

For a correction with exactly p terms it must instead equal one.
This contradiction proves the assertion, independently of b. The
argument excludes this specified balanced prefix architecture; it does
not exclude a longer prefix after further source exponents have changed,
different terminal projections, or a rank-changing complete certificate.

The stronger two-antecedent route also has an exact elementary form.
For an odd ternary unit q with first exponent one put u=U(q). Then
u is odd, `u=2 mod3`, and `u!=5 mod9`; conversely these conditions give
`q=(2u-1)/3`. Ordinary one-step identities give

\[
q\in C\iff u\in C,\qquad
5q\in C\iff5u-2\in C.
\]

Thus the proposed implication from `q in C` and `5U(q) in C` to
`5q in C` is precisely the still unproved implication from `u,5u in C`
to `5u-2 in C` on this domain. The much smaller known representatives
for u and5u in the special least-failure construction do not by
themselves supply a certificate for the minus-two component.

## Attempted completion and remaining gap

The A+B compiler consumes some genuine first-valuation-one
blocks, including arbitrary concatenations with the unbounded A-ladders.
The short joint energy proof controls their entire source union at exponent
.84. These transport families are already included in the refreshed PR168
and PR169 sources. It does not prove that every known terminating source word can be
parsed into these blocks, nor that every uncovered failure reaches them
along a defect-preserving smaller-source path.

In PR146's special Mersenne comparison, the source word instead starts
with one followed by a long run of threes. Its source is near the
rational fixed value1/5 after the first step; the multiplied companion
has a long Mersenne ascent. The known convergence of q and5U(q) does
not yet supply a certificate for5q. The V1 block does not match that
word and is not silently used there.

No bound on R(infinity) is obtained, and the full theorem remains OPEN.
No GRH input is needed for V1--V5. All claimed unbounded statements
rest on the proofs above; the separate program provides finite literal
and exact rational verification only.
