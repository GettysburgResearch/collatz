# A rotational exclusion for arbitrary contracting words

**Status.** Proposed written theorems with exact bounded replay. The analytic
step uses PR177, head 25bf9b95a9404998e8e55aa401773488cd3dd4b8,
`research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md`,
(TS7), a source-qualified application of Matveev's Corollary 2.3
(DOI 10.1070/IM2000v064n06ABEH000314, [primary PDF](https://www.mathnet.ru/links/ece4aa0032f96dfaf141673d5dc77324/im314_eng.pdf)). The Lean file checks the finite algebraic cores; the uniform analytic estimate and all-period classification are written proofs.
The elementary carry and common-denominator setup comes from PR191,
37b3916633cd32a0c173b20bb18ec3a7ec290a63,
`research/two-sided-cycle-packing-20261124/README.md`, sections 1--2.
The first theorem applies at arbitrary bit positions, with no block dictionary.

## 1. Whole-period common factors

Use the shortcut map and write a primitive positive cycle of rational numbers
in lowest terms with common odd denominator d. Let its bit period be A and its
odd count p, and set D=2^A-3^p>0. For an m-bit word v with odd positions
t_0<...<t_(q-1) let C_v=sum_j 2^{t_j}3^{q-1-j}. For a whole-period
word v at initial state x the closure is Dx=C_v. Distinct rotations at
different positions in a primitive cycle have distinct states, by determinism.

**R1.** If two different rotations agree on a cyclic interval of L bits,
cut immediately after that interval to write the two rotations as vw and v'w
with common suffix w and complementary words of length m=A-L and equal count q.
Then
```
D/gcd(D,C_v-C_v') divides d,
D <= d |C_v-C_v'| <= d (2^{m-q}-1)(3^q-2^q) < d 3^m.
```
Indeed C_{vw}=3^{#1(w)}C_v+2^m C_w. Subtract the two closing equations,
clear d, and use gcd(D,3)=1. The distinct starting states give unequal
carries. The extrema for a q-odd m-bit word are 3^q-2^q and
2^{m-q}(3^q-2^q), by t_j between j and j+m-q. This proves all claims.
The fixed interval may cross the original choice of cyclic origin.

**R2.** Every primitive nonstandard positive ordinary cycle has distinct
cyclic factors of length ceil(A/2)-1 at all its A starting positions.
In particular, every nonidentity shift changes at least four parity bits.

The arithmetic estimate below gives D>3^{floor(A/2)+1} for A>=17.
A repeated factor of the stated length would contradict R1 with d=1.
If a shift changes exactly two bits, the remaining matching bits occupy
two (possibly empty) cyclic runs, one of length at least ceil((A-2)/2).
Hamming distance is even for two rotations of the same weight. Distance
zero is excluded by primitivity. For A<=16 a direct enumeration below
shows the only positive integer words are alternating repetitions of 10.

### Explicit uniform period-gap estimate

For 17<=A<512, exact integer comparison over 82,202 contracting pairs is
given in controls.py. For 512<=A<10^13, write theta=log(3)/log(2).
An exact Farey enclosure is
```
83130157078217/52449289519716 < theta < 18340740190704/11571718688839.
```
To reproduce the inequalities, bound log(x), x in {2,3}, by truncating
2 sum z^{2j+1}/(2j+1) at j=127 for z=(x-1)/(x+1), with positive error
less than 2z^257/(257(1-z²)). The two endpoint fractions have determinant
one and both denominators exceed 10^13. Every fraction in their open
interval in lowest terms has denominator at least the sum of theirs
(by expressing its numerator-denominator vector as a positive integral
combination of the two endpoint vectors). Since A/p>theta and p<=A,
A/p strictly exceeds the upper fraction U/V. Thus
Lambda=A log2-p log3>log(2)/V>2^-46. For lambda>0,
1-e^{-lambda} >= min(1,lambda)/2, e.g. by e^{lambda}>=1+lambda.
Consequently D=2^A(1-e^{-Lambda})>2^{A-47}. For A>=512,
(4/3)^A >=(4/3)^512 >9*2^94 by integer calculation, giving
2^{A-47}>3^{A/2+1}.

For A>=T=10^13, pinned (TS7) gives log|Lambda|>-5*10^9(1+log A).
Since log(2/sqrt(3))=log(4/3)/2>1/8, it suffices that
A/8 > log 6 + 5*10^9(1+log A). This holds at T (log 10<3 and log 6<2)
and the difference has positive derivative 1/8-5*10^9/A thereafter.
Thus D>2^{A-1} exp(-5*10^9(1+log A))>3^{A/2+1}.

The small-period enumeration iterates all 131,070 binary words of lengths
1 through 16. Among 112,892 positive-carry contracting words, exactly 16
have D dividing C, and each is cyclically alternating. This enumeration
checks the literal closing condition for all ordinary cycles of these lengths.

More generally (TS7) and R1 give the asymptotic bound
L < (1-log(2)/log(3))A + [log(2d)+5*10^9(1+log A)]/log(3).
Without a theorem forcing an arbitrary cycle to contain such long matching
factors, this exclusion cannot rule out all nonstandard cycles. Nor does
a cycle exclusion address ordinary divergence.

## 2. A transposition divisor for equal-clock blocks

**R3.** Partition a rational positive cycle into r>=3 blocks of fixed
length a and fixed positive count b; write N=2^a, M=3^b, so N>M.
Suppose a cyclic shift by whole blocks preserves every position except
that it interchanges two distinct block carries, with absolute difference
E>0 at positions i<j, numbered from zero. Set h=j-i, g=gcd(r,h), and
K=(N^r-M^r)/(N^g-M^g). Then
```
K/gcd(K,E) divides d,       K>N^{r-g}>=N²>E.
```
Each shifted initial state has integral numerator over the common d.
The difference of whole-word carries is, up to sign,
E N^i M^{r-1-j}(N^h-M^h). Subtract the two whole-cycle closing equations.
The monomial is a unit modulo N^r-M^r, giving
N^r-M^r | d E (N^h-M^h). By Euclid's algorithm on exponents,
gcd(N^h-M^h,N^r-M^r)=N^g-M^g, so K divides dE.
The geometric sum for K strictly exceeds its first term N^{r-g},
and g<=r/2 gives r-g>=2. The carry range is at most
(2^{a-b}-1)(3^b-2^b)<NM<N². This excludes ordinary realization.
For ordinary integers the exclusion overlaps PR191 TCP-3's no-reuse
conclusion; the explicit large denominator divisor and the elementary
proof are additional. No hypothesis about coprimality of r and h occurs.

## Replay

Run `python controls.py` in this directory (standard library). It checks
the Farey-log enclosure, all indicated finite period comparisons, all short
word closures, 13,066 actual rational rotations for R1, and 5,908 small transpositions against their actual reduced
denominators. These counts are bounded controls, not tests of a universal
orbit. Both normal Python and python -O replayed all guards. Dropping d in R1 fails for 001 versus 010: D=d=5 and delta=2. Using two different positions in the nonprimitive word 1010 can give identical states and hence zero difference.

For Hamming-two primitive rational cycles, R1 and (TS7) also give

    d > (2/sqrt(3))^A exp(-5*10^9(1+log A))/6.

This asymptotic denominator bound has no block dictionary hypothesis.
