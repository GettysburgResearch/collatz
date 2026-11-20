# Independent review of the Mersenne predecessor-witness depth theorem

**VERDICT: VERIFIED for W1–W2 at the frozen manuscript below.**
The result excludes a uniformly bounded number of odd inputs for a specified
cheaper-predecessor construction. It does not exclude source-dependent
algorithms, general ordinary walks, or Collatz itself.

The reviewed file is `agent_deep_reverse/MERSENNE_WITNESS_DEPTH.md`, SHA-256
`25f16035aece8873c0b3fd9101552b8aaafea78a90478ecd6f9caa67e999176f`.
Its mathematical proof was reconstructed independently. The separate checker
`check_mersenne_depth_review.py` imports no author code. Normal and `-OO`
executions produced byte-identical reports `mersenne-depth-review-normal.json`
and `mersenne-depth-review-optimized.json`.

## W1: the rational center is used algebraically

Write an inverse word as `I_a(v)=(2^a*v-1)/3`, with positive exponents and
endpoint `Y'(P)=2^A*P/3^q-D/3^q`, where `D>0`. At `P_*=11/4`, the starting
value is `7/4`, a ternary unit congruent to 1 modulo 3. Ternary integrality
of the first inverse therefore forces its exponent to be even and at least
2; this also clears the denominator 4. Its output is a positive integer.
Every subsequent integral inverse output remains a positive integer.

No ordinary parity or least-source guard is applied to the rational center.
For example, its first integral output may be the even integer 2. The proof
correctly uses integrality, positivity, affine slope, and congruence only.

If the upper slope `lambda=2^(A+1)/3^q` is at most `1024/243`, the integer
center endpoint `V` obeys

`1<=V<(512/243)*(11/4)=1408/243<6`.

The lower binary eligibility condition is
`Y'(2^e)=65,129,193 (mod256)`. For the actual exponents `e>=119`, its
residue is the constant term `-D*3^(-q)` modulo 256. At the center,

`V=-D*3^(-q)+11*2^(A-2)*3^(-q)`.

For `A>=10`, the last term vanishes modulo 256, contradicting `1<=V<=5`.
For `A=8,9`, reducing modulo 64 gives `V=1`. For `2<=A<=7`, it instead
gives `v2(V-1)=A-2`; among `1<=V<=5` this leaves only `A=2,3,4`.
The manuscript's complete direct enumeration of those three totals is
correct. In particular `(2)` has constant binary residue 41 modulo 64;
`(2,1)` has center endpoint 1, violating the required finite valuation;
and the total-four words are nonintegral or have center endpoint 9.

An integral inverse word from `7/4` to 1 must start `(2,1)` and then use
only exponent-two loops at 1. Indeed an inverse landing at 1 comes from 1
with exponent 2 or from 2 with exponent 1. Removing terminal loops leaves
the second case. An inverse from a positive integer cannot land at 2,
because it would require `2^a*v=7`; the 2 must therefore be the first
output from `7/4`. Thus `A=2q-1`. Among `A=8,9`, only `A=9,q=5` survives,
with the word `(2,1,2,2,2)` and

`Y'(P)=(512P-1165)/243`.

Its upper is exactly the original `X=(1024P-2573)/243`, with no strict
saving. This proves the all-word W1 statement; the argument is not a
finite search extrapolation.

As a separate finite audit, the independent checker enumerates all 510
positive compositions with total exponent from 2 through 9. It reconstructs
their affine maps and center states directly, verifies the inverse-word
intercept identity, and finds exactly the displayed eligible cheap word.

## W2: actual-source lifting and the numerical-height issue

For each `H>=5`, choose an arbitrarily large exponent in `e=119 (mod162)`
with `4*2^e=11 (mod3^H)` and `e>=4H+11`. Existence follows from
`2^119=11/4 (mod243)` and `v3(2^162-1)=5`: the powers of `2^162` generate
all units congruent to one modulo 243 at each higher ternary precision.
The lift determines one residue class for the progression parameter modulo
`3^(H-5)`, giving infinitely many ordinary exponents.

If a legal ordinary inverse word has depth `q<=H`, then each center prefix
is ternarily integral as well. After `i` inverses, its difference from the
actual prefix is `2^(A_i)*(2^e-11/4)/3^i`, still ternarily integral for
`i<=H`. The center's first output clears its denominator 4, so W1 applies.
Depth zero is separately ineligible because `2^e-1=255 (mod256)`.

The proof must still rule out a word whose affine slope is larger but whose
negative intercept makes its particular ordinary endpoint smaller. The
manuscript does this correctly. Its exact formula is

`Y'=(2^A/3^q)*(P-E)`,
`E=1+sum_{i=1}^q 3^(i-1)/2^(A_i) <= (3/2)^q`,

since `A_i>=i` and the resulting geometric sum is exact at equality.
The independent checker verifies both the identity and inequality directly
for all 510 small-total words, using fractions and affine composition.

For `lambda>lambda_0=1024/243`, put both fractions over
`3^max(q,5)`, with integer numerators `m>b`. Then

`lambda/(lambda-lambda_0)=m/(m-b)<=b+1<=1025*3^q`.

This holds also for `q<5`; the common numerator `b` is then simply 1024.
Since `P>=2^(4H+11)>1025*9^H`, the inequalities `q<=H` and
`E<=(3/2)^q` imply

`(lambda-lambda_0)*P>lambda*E`.

Hence `2Y'-1-X` is positive, including its remaining positive constant
`2573/243-1`. A strict numerical saving must therefore have
`lambda<=lambda_0`. W1 then leaves only the exact original upper, which
again is not a strict saving. This closes the slope/intercept gap for all
words, not only words of bounded total exponent.

The claimed representative bound
`e<=max(119,4H+11)+162*3^(H-5)` is valid, since consecutive solutions differ
by exactly the final period. It gives the stated logarithmic lower bound
on needed depth along a family of varying ordinary sources. It does not
assert that any fixed positive source has no finite successful witness.

## Further independent checks and the unsuccessful recursion

The checker independently lifts the exponent through precisions 5 to 16.
For depths 5 through 9 it exhausts the positive integral center tree up to
the exact total-exponent cap forced by `lambda<=lambda_0`. The five trees
contain 19, 26, 51, 70, and 124 nonempty nodes, respectively. At each actual
lifted source, the only eligible cheap word is the original one, and its
upper height equals `X`. Larger slopes are covered by the general argument
above, not silently omitted from the theorem. A further 618 exact finite
fraction comparisons audit the slope-separation formula.

The proposed precision-spending identity is also correct:
`I_2^i(Y)=1+(4/3)^i*(Y-1)` through the available ternary precision. Every
nonzero repetition raises the associated upper height above `X` and makes
the lower value 1 modulo 256, outside the allowed binary classes. At the
exit, one ternary residue has no odd predecessor; the other permits an
exponent-one inverse. The revised manuscript correctly notes that one
repetition followed by that inverse can repay height, while the leading
factor remains above one after at least two repetitions. No uniform
repayment theorem is inferred from those observations.

The scope qualifications are necessary: the theorem concerns ordinary
predecessors ending exactly at the prescribed Mersenne and counts odd
inputs. It is not a lower bound for arbitrary undirected ordinary walks,
and it does not block an algorithm whose depth depends on its actual
source or certificate.
