# Unbounded first-one five transport and a valuation-controlled renewal

**PROPOSED elementary results; the universal five implication and Collatz remain open.**

This note gives two unbounded physical transport families beginning with
valuation one, proves their complete binary cylinders, and bounds their
inverse fibers by a ternary valuation argument. They can be added to the
entire renewable domain of PR167 while retaining its constants `5/8` and
`91/100`. These are explicit additional families inside PR167's homogeneous
recognizer, not a new complete certificate architecture.

## Exact source pins and attribution

* PR166, `5996b9f525ca50978bc34f423192c36a87765bf3`,
  `research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`:
  the arbitrary valuation-two ladder and its consuming compiler.
* The same PR, `LADDER_RENEWAL.md`: inverse-fiber summation and the original
  ladder renewal.
* PR167, `e83cc8b35ad614c616df7c00318cc9645a174c34`,
  `research/least-failure-closure-20261121/HOMOGENEOUS_FIVE_TRANSPORT.md`:
  the complete correction decoder, maximality over homogeneous dictionaries,
  and all three first-one four-input families. In particular the block
  `(1,1,1,b)` below was independently found during this pass but is credited
  to the already published complete classification.
* The same PR, `EXPANDED_FIVE_RENEWAL.md`: the full old domain, its correlated
  endpoint-residue coefficient `Gamma_s`, and the constants `5/8`, `91/100`.
* The same PR, `HOMOGENEOUS_LOCALIZATION.md`: a homogeneous prefix preserves
  complete homogeneous recognizability of the supplied endpoint certificate.
* PR146, `fd991063721e9c157d318e40bb20131762f7d750`,
  `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`: the hard
  first-one/valuation-three boundary and prescribed-endpoint localization.

No external analytic theorem is used in the results proved here. Any later
rigidity consequence of finite five energy retains the source qualifications
in PR163 and PR167. In particular, the renewal below does not supply the
missing finite energy of its uncovered sources.

Write `T(n)=n/2` on positive even integers and `(3n+1)/2` on positive odd
integers. Write `U(n)=(3n+1)/2^v2(3n+1)` on positive odd integers. An exponent
word lists the successive exact division exponents of `U`. On rationals set
`I_a(z)=(2^a z-1)/3` for algebraic calculations; an ordinary inverse step
requires a positive odd integral output.

## UF1. Two unbounded first-one blocks

For every `r>=3` and `b>=4`, the following are actual paired transports
whenever their source words are actual positive odd paths from `x` to `q`:

| Source word | Target word from `5x` to `5q` |
|---|---|
| `(1,2^r,1,2,b)` | `(1,1,4,2^(r-3),3,3,1,b-3)` |
| `(1,2^r,1,4,b)` | `(1,1,4,2^(r-3),3,1,5,b-3)` |

Here `2^r` denotes `r` consecutive letters equal to two. Both words have
`p=r+4` odd inputs. For the row indexed by `a=2` or `a=4`, both clocks are

\[
L=2r+b+a+2.
\tag{UF1}
\]

Thus `T^L(x)=q` and `T^L(5x)=5q`. The source ranks in these blocks are
unbounded, and each source begins with valuation one followed by an
arbitrarily long run of twos. None is an initial PR166 ladder block or one
of PR167's four-input first-one blocks.

### A seed-centered derivation

Put `J=I_2` and `R=I_1 I_1 I_4`, where composition is in forward-word order.
Then

\[
J^r(z)=1+(4/3)^r(z-1),\qquad R(1)=5/3,
\qquad R(z)=5/3+(64/27)(z-1).
\tag{UF2}
\]

Let `S_a=I_1 I_a I_b`, and let

\[
Q_2=I_3I_3I_1I_{b-3},\qquad
Q_4=I_3I_1I_5I_{b-3}.
\]

Directly,

\[
\boxed{Q_a(5q)-1=(10/3)(S_a(q)-1).}
\tag{UF3}
\]

For clarity, `S_2(q)=(2^(b+3)q-23)/27` and
`S_4(q)=(2^(b+5)q-47)/27`. The corrections of `Q_2` and `Q_4` are
respectively `419` and `659`; their clocks are `b+4` and `b+6`.
Consequently `B(Q_a)+81=10(B(S_a)+27)`, and their leading numerators
also agree in (UF3).

Using (UF2)--(UF3), for every `r>=3`,

\[
\begin{aligned}
R J^{r-3}Q_a(5q)
 &=\frac53+\frac{64}{27}(4/3)^{r-3}\frac{10}{3}(S_a(q)-1)\\
 &=\frac53+\frac{10}{3}(4/3)^r(S_a(q)-1)\\
 &=5I_1J^rS_a(q).
\end{aligned}
\tag{UF4}
\]

This is also a reusable extension principle: **any** algebraic pair
`S,Q` satisfying (UF3) gives (UF4), provided the displayed counts and
positive integer inverse guards are supplied. No assertion that every
suffix admits such a pair is made.

### Ordinary legality

For a word with `p` odd inputs, clock `L`, and correction `B`, its inverse
formula is `(2^L q-B)/3^p`. The two source corrections in UF1 are

\[
B_{r,a}=C_a4^r-27\,3^r,
\qquad C_2=100,\quad C_4=148.
\tag{UF5}
\]

Equation (UF4) says that the target correction is `5B_{r,a}`. Since the
source is integral, the full target numerator equals `3^(r+4)(5x)`.
Reducing modulo three, then dividing and repeating, proves integrality
of each successive inverse step. Every target exponent is positive,
including `b-3`, so the inverse states are odd. Starting at `5q>=5`,
each integral inverse is positive. An inverse of an odd value greater
than one cannot equal one, since `2^a v=4` would be required. Thus no
target state in the block is one.

The source also avoids one before its endpoint. Indeed `I_b(q)>=5` for
`b>=4,q>=1`; every integral inner inverse before the final `q` is greater
than one. The subsequent `I_2` steps preserve strict inequality, and an
`I_1` step on an odd input cannot output one. Therefore the words are
ordinary paths with exact valuations, not just rational identities.

## UF2. Whole cylinders, strict smaller endpoints, and density

For `a in {2,4}`, `r>=3`, define

\[
M_{r,a}=2^{2r+a+6},\qquad
\rho_{r,a}=-B_{r,a}(3^{r+4})^{-1}\pmod {M_{r,a}}.
\tag{UF6}
\]

The inverse here is only modulo a power of two and always exists. The
**entire** source cylinder for the corresponding UF1 block is

\[
\boxed{x=\rho_{r,a}\pmod {M_{r,a}}.}
\tag{UF7}
\]

The first few residues provide exact controls:

| `a` | `r` | Cylinder |
|---:|---:|---|
| 2 | 3 | `16299 mod16384` |
| 2 | 4 | `50859 mod65536` |
| 2 | 5 | `96939 mod262144` |
| 4 | 3 | `39851 mod65536` |
| 4 | 4 | `169643 mod262144` |
| 4 | 5 | `342699 mod1048576` |

To prove (UF7), prescribe the first `r+3` exact exponents
`(1,2^r,1,a)` and require at least four divisions at the next odd input.
Reversing these specified shortcut parities modulo their required power
of two gives one odd residue modulo `M_{r,a}`. The full inverse identity
at clock `2r+a+6` gives exactly (UF6). Conversely the same reverse parity
calculation on that residue forces the earlier exponents exactly and the
last exponent at least four. Taking the full last valuation yields the
odd endpoint `q` used in UF1.

There is a useful independent separating invariant. If `u=U(x)` after
the first valuation-one step, then `u=I_2^r(z)` and the next odd value
`z` has valuation one. Therefore `z=3 mod4` and

\[
v_2(u-1)=2r+1,\qquad
\boxed{v_2(3x-1)=2r+2.}
\tag{UF8}
\]

Different `r` cylinders are disjoint. At fixed `r`, the exact later
exponent `a` separates the two rows. Their initial pattern `(1,2,...)`
separates them from all three PR167 four-input rows, which start `(1,1)`;
their first exponent separates them from the PR166 ladder, which starts
with two.

Every UF1 endpoint satisfies

\[
\boxed{q\le x/7<x.}
\tag{UF9}
\]

Indeed (UF5) gives

\[
q=\frac{3^{r+4}x+B_{r,a}}{2^{2r+b+a+2}}
\le\frac{2187}{16384}x+\frac{25}{64}.
\]

The largest coefficients occur at `r=3,b=4,a=2`; dropping the negative
term in `B_{r,a}` only enlarges this bound. The right side is at most
`x/7` for `1075x>=44800`, in particular for `x>=43`. By (UF8), these
positive sources satisfy `3x=1 mod256`, and the least positive solution
is `x=171`. This proves (UF9) uniformly.

Their densities among all positive integers sum to

\[
\sum_{r\ge3}(2^{-2r-8}+2^{-2r-10})
=\frac1{12288}+\frac1{49152}
=\frac5{49152}.
\tag{UF10}
\]

The infinite tails are contained in `3x=1 mod2^(2R+2)` by (UF8), whose
density tends to zero as `R` tends to infinity. This justifies the infinite
sum of cylinder densities. Imposing the ternary-unit guard gives relative
density `5/24576` among odd ternary units, by the Chinese remainder theorem.
With the full PR167 domain, the relative density becomes

\[
\boxed{85/1536+5/24576=455/8192.}
\tag{UF11}
\]

If a least failed antecedent of the physical implication
`x in C =>5x in C` exists, it belongs to none of these cylinders. Otherwise
UF1 transports it to a smaller positive odd ternary-unit `q in C`, while
`5q` has the same nonconvergent label as `5x`, contradicting minimality.
This is a least-five-failure statement, not an assertion that knowledge of
one convergent `x` certifies every smaller integer.

## UF3. A consuming compiler, with its existing maximal recognizer credited

Let the dictionary contain:

1. Every credited PR166 block `(2^r,b)`, `r>=1,b>=4`.
2. All three credited PR167 blocks `(1,1,a,b)`, `a=1,2,4`, with the
   corresponding last-exponent thresholds `6,4,4`.
3. Both UF1 families for every `r>=3,b>=4`.

The block source patterns are prefix-disjoint. A source beginning in two
has a unique maximal run of twos; a source beginning `(1,1)` has one of
the three fixed four-input patterns; a source beginning `(1,2)` has a
unique maximal following run of twos and one of the two UF1 endings.
Hence concatenations admit a direct left-to-right consuming parser.

Given an actual complete first-hit witness whose word is a concatenation
of these blocks, replace each block by its target word and append the
single exponent four, the known edge `5->1`. Every block transports its
actual endpoint to exactly five times that endpoint. The parser consumes
a positive finite number of source letters each time, and thus terminates
from the supplied certificate length. No target prefix visits one before
the final edge. If the source has odd count `p` and clock `N`, the output
therefore has exactly

\[
\boxed{\omega(5x)=p+1,\qquad\tau(5x)=N+4.}
\tag{UF12}
\]

For source `x=1`, the empty source word yields `(4)`. Malformed witnesses
are rejected separately from valid witnesses outside this block language,
which return `UNRESOLVED`.

PR167 HT2 already proves that its one-shot decoder includes every such
homogeneous consuming compiler, even for an infinite adaptive dictionary.
The compiler here is a convenient explicit language and a verification
control, **not** a stronger complete recognition architecture. In
particular PR167's localization-cancellation theorem continues to apply.

Each fixed `r,a` also yields an unconditional infinite first-hit family.
Set `q=1`, choose the unique class of `b` modulo `2*3^(r+3)` satisfying
`2^(2r+b+a+2)=B_{r,a} mod3^(r+4)`, and take every `b>=4` in it. The
existence and uniqueness of that class follow from the fact that two is
a primitive root modulo a power of three. Each such input has the exact
source rank `r+4` and target rank `r+5`. A source ternary-unit restriction
can be imposed afterward; the ordinary convergence identity itself does
not need it.

## UF4. A valuation-controlled inverse-fiber bound

Let `f` be any metric-valued ordinary `T`-invariant label, and put
`e(x)=d(f(5x),f(x))`. As in the pinned PR167 source, `e(1)=0`, so a
nonzero endpoint contribution has odd ternary-unit `q>=5`.

The central additional observation is

\[
\boxed{3^{r+3}(3x-1)
 =4^r\left(2^{b+a+2}q-C_a\right).}
\tag{UF13}
\]

Since `3x-1` is a ternary unit, actual integral sources satisfy

\[
\boxed{v_3(2^{b+a+2}q-C_a)=r+3.}
\tag{UF14}
\]

For each fixed `a,q,b`, this determines **at most one** `r`. In particular
one must not bound these inverse fibers by a separate independent sum over
every run length if the exact valuation can instead be retained.

Since `r>=3`, (UF14) requires

\[
2^{b+a+2}q=C_a\pmod {729}.
\tag{UF15}
\]

Two has order `486` modulo `729`, so for fixed `a,q` the eligible `b` occupy
one residue class modulo `486`. For completeness, the elementary order
claim follows from `v_3(4^(3^j)-1)=j+1`, proved by expanding the next cube;
the order of four is `3^(k-1)` modulo `3^k`, and the odd powers of two
are `-1 mod3`.

Fix a unit residue `c mod729`, let `q_c` be its least odd representative
at least five, and let `b_a(c)>=4` be the least solution of (UF15). Set

\[
H_a(c)=\frac{81(3/4)^3}
 {2^{b_a(c)+a+2}-C_a/q_c}.
\tag{UF16}
\]

All denominators are positive. Rearranging (UF13),

\[
x=\frac13+(4/3)^r\frac{2^{b+a+2}q-C_a}{81}.
\]

For `b=b_a(c)+486j`, `q>=q_c`, and `r>=3`, this gives

\[
q/x\le H_a(c)\,2^{-486j}.
\tag{UF17}
\]

To check the geometric comparison, the denominator
`2^(b_a+a+2+486j)-C_a/q_c` is at least `2^(486j)` times its value
at `j=0`. Together with uniqueness of `r` for each `b`, this proves the
complete all-run estimate, for every `s>0`,

\[
\boxed{\sum_{x\text{ in UF1 row }a\atop x\mapsto q}(q/x)^s
 \le\frac{H_a(c)^s}{1-2^{-486s}}.}
\tag{UF18}
\]

Discarding sources divisible by three, or sources above a finite cutoff,
only improves the inequality. No convergence, independence, random parity,
or initial energy assumption enters this bound.

## UF5. Strictly enlarged renewable domain at the existing constants

Let `H_old` be the full domain of PR167 ER1: the complete PR166 ladder and
all three four-input first-one cylinders. Let `H_new` add every UF1
cylinder. Let

\[
E_s(X)=\sum_{0<x\le X\atop x\text{ odd},\,3\nmid x}x^{-s}e(x),
\qquad
R_s^{new}(X)=\sum_{0<x\le X\atop x\notin H_{new},\ x\text{ odd},\,3\nmid x}
x^{-s}e(x).
\]

Write `Gamma_s(d)` for the explicit old fiber bound in PR167 ER2,
equation (10), where `d=q mod81`. Its full formula and every coefficient
are independently reconstructed in the accompanying checker. For each
of the 486 unit residues `c mod729`, define

\[
\Lambda_s(c)=\Gamma_s(c\bmod81)
 +\frac{H_2(c)^s+H_4(c)^s}{1-2^{-486s}}.
\tag{UF19}
\]

The finite exact certificate verifies

\[
\boxed{\Lambda_1(c)<5/8,\qquad
\Lambda_{21/25}(c)<91/100\quad\text{for every }c.}
\tag{UF20}
\]

This is a complete finite residue calculation for the specified rational
coefficients, not a finite search over Collatz starts. Harmonic comparisons
are rational. For exponent `21/25`, every required rational power is
enclosed above on a `10^-9` grid by integer twenty-fifth-power comparisons.
Upper bounds enter positive numerators and `1-upper` denominators. The
checker emits all 486 rows and the exact maximum upper bounds; it uses no
floating point in the certificate.

Every old endpoint has `q<=x/3`, and every new UF1 endpoint has `q<=x/7`.
Grouping finite-cutoff sums by their actual endpoint, using physical
equality `e(x)=e(q)`, (UF18), and (UF20), proves

\[
\boxed{E_1(X)\le R_1^{new}(X)+\frac58E_1(X/3),}
\qquad
\boxed{E_{21/25}(X)\le R_{21/25}^{new}(X)
                      +\frac{91}{100}E_{21/25}(X/3).}
\tag{UF21}
\]

The constants and cutoff factor are the existing PR167 ones; the domain
is strictly larger, by all the unbounded first-one families. In particular
this is not advertised as an improvement of the numerical contraction
constant. The important additional fiber fact is (UF14).

At finite cutoffs, `E_s(X/3)<=E_s(X)` permits subtraction. Monotone limits
then show that the full energy is finite exactly when its new remainder
is finite, and in that case

\[
E_1(\infty)\le(8/3)R_1^{new}(\infty),\qquad
E_{21/25}(\infty)\le(100/9)R_{21/25}^{new}(\infty).
\tag{UF22}
\]

## The remaining physical boundary

The new words begin `(1,2,...)`. They do not consume the hard
`(1,3^m,b)` prefix localized in the pinned PR146 work. For that latter
prefix, with `p=m+2`, `L=3m+1+b`, the exact source correction satisfies

\[
5B=3^p+2^{3p-2},\qquad
5x+1=\frac{2^{3m+4}(5\,2^{b-3}q-1)}{3^{m+2}}.
\]

For `b>=4`, its target has `v2(5x+1)=3m+4`, and after those shortcut
steps its actual value is

\[
\boxed{T^{3m+4}(5x)
 =3^{2m+2}(5\,2^{b-3}q-1)-1.}
\tag{UF23}
\]

The factor `3^(2m+2)` and the negative offset are not absorbed by UF1 or
by the supplied `q` certificate. Source and target do not have the same
odd-step resources at this boundary. PR167 already proves that adding a
homogeneous localization prefix cannot repair an unrecognized endpoint
certificate. Its rank-one source obstruction and examples with different
target clocks likewise survive the enlarged dictionary.

Nor does (UF21) bound the new remainder from above. A contractive renewal
is not a finite-energy proof until its uncovered charge is controlled.
The actual remaining obligation is a valid nonhomogeneous certificate
transformation or an all-source upper bound for that remainder. Neither
is established here. No full Collatz proof is claimed.

## Verification scope

`check_unbounded_first_one_transport.py` independently reconstructs source
and target corrections, replays actual odd maps on integral sources,
checks all the displayed cylinder controls and selected lifts, compiles
mixed complete first-hit witnesses, and verifies all 486 coefficient rows
with exact rational/integer arithmetic. It imports no previous checker.
Failures are explicit and remain active under optimized Python. Corrupted
target words, malformed source witnesses, and valid unresolved witnesses
are distinct controls. The universal claims rest on the proofs above;
finite replay is implementation evidence and verification of the finite
coefficient certificate.
