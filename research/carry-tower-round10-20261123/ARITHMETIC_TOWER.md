# An arithmetic exclusion for sparse automatic carry scripts

23 November 2026. Published parent PR182:
`c369ae3c426ec6aaf9a280ec9578b9910c2147d5`.

**Status: PROPOSED written theorems with finite arithmetic controls.
The specified automatic scripts have no rational 2-adic physical
source. Collatz and the full denominator-eight exclusion remain OPEN.**

Round nine produced bounded, positive, nonperiodic automatic gap
sequences whose discounted sum is exactly 7/8, and positive ordinary
realizations of every finite prefix. Here an ordinary height argument
excludes one fixed positive source for four explicit families of such
scripts, with a finite mismatch budget. A second elementary argument
shows their unique 2-adic physical completions are irrational. The
latter keeps a rational candidate's ordinary numerator height and its
binary valuation in the same finite equation.

## 1. Exact sources and normalization

Use the positive odd map `U(q)=(3q+1)/2^g`, where
`g=v_2(3q+1)`. The parent inputs are:

| Source at the full parent head | Claims used | Git blob |
| --- | --- | --- |
| `research/scalar-rigidity-round9-20261123/ARITHMETIC_RIGIDITY.md` | R9-A2: arbitrary binary two-block script has scalar 7/8; R9-A3: complete terminal-odd cylinders | `2c872eb9818be062e9444fde91555ba4e1e7230f` |
| `research/scalar-rigidity-round9-20261123/CARRY_RETURN.md` | Literal maps and domains in (3) | `0b0d2ff63339522689f9984aad1bae3ab63d9e08` |

Let the unpaid block L have actual odd gaps `(2,1)` and the paid
block P have gaps `(1,4)`. Their complete maps are

\[
L(q)=\frac{9q+7}{8},\quad q\equiv9\pmod{16};\qquad
P(q)=\frac{9q+5}{32},\quad q\equiv3\pmod{64}.
\tag{1}
\]

A script is a binary sequence s, with `s_j=0` selecting L and
`s_j=1` selecting P at block index j. The odd-gap sequence is

\[
g_{2j}=2-s_j,\qquad g_{2j+1}=1+3s_j.
\tag{2}
\]

Every script has discounted gap sum 7/8. Its candidate carries at
the block boundaries are zero, and its intermediate carries are
`s_j`, hence at most one. These are symbolic facts; no ordinary
infinite realization is supplied by them.

For an actual finite realization write `X_j=q_(2j)+7`. Keeping the
additive constants in (1) gives the single exact equation

\[
\boxed{8\,4^{s_j}X_{j+1}=9X_j+166s_j.}
\tag{3}
\]

## 2. A finite window for every positive ordinary source

**R10-A1 (same-source window).** Suppose one positive odd source q
actually follows a finite L/P script. If m consecutive unpaid blocks
start at block j, then

\[
\boxed{2^{3m+1}8^j\le9^j(q+7).}
\tag{4}
\]

**Proof.** At every positive ordinary block boundary `X>=8`.
The unpaid map is `X'=9X/8`. The paid map is
`X'=9X/32+83/16`, which is at most `9X/8` because
`27X>=166`. Thus

\[
8^jX_j\le9^jX_0.
\tag{5}
\]

Across the m unpaid blocks,
`8^m X_(j+m)=9^m X_j`. The endpoint is a positive odd ordinary
state, so `X_(j+m)` is even. Since `9^m` is odd, this forces
`2^(3m+1)` to divide the positive integer `X_j`; in particular
`2^(3m+1)<=X_j`. Combining with (5) proves (4), including m=0.

The equivalent logarithmic bound is

\[
3m+1\le\log_2(q+7)+j\log_2(9/8).
\tag{6}
\]

This is a finite statement about the unchanged actual source. It
does not assume `h(q)=7/8`, eventual convergence, or the existence
of an infinite script realization. Merely bounding the carries
does not imply that every possible script violates this window.

## 3. A rational numerator cannot support an excessively sparse script

Let the paid positions be an infinite increasing sequence
`t_0<t_1<...` of nonnegative integers. Put

\[
F_s=\sum_{r\ge0}4^r(8/9)^{t_r}\quad\text{in }\mathbb Q_2.
\tag{7}
\]

The term valuations are `2r+3t_r`, strictly increasing to infinity,
so this 2-adic sum exists. No real convergence is needed here.

Iterating (3) backwards over n blocks gives, with
`S_n=sum_(j<n)s_j`,

\[
X_0=(8/9)^n4^{S_n}X_n
       -\frac{166}{9}\sum_{j<n}s_j(8/9)^j4^{S_j}.
\tag{8}
\]

The complete finite cylinders have one compatible odd 2-adic
source. Since their endpoint shifted coordinate is even, the first
term in (8) tends to zero 2-adically. Its unique physical completion
therefore is

\[
\boxed{q_*=-7-\frac{166}{9}F_s.}
\tag{9}
\]

This identity also holds for any rational source with odd denominator
that were to follow the infinite script: every rational odd state
has even shifted coordinate, so the same boundary term vanishes.

**R10-A2 (lacunary arithmetic obstruction).** If

\[
\limsup_{R\to\infty}\frac{8^{t_{R+1}}}{9^{t_R}}=\infty,
\tag{10}
\]

then `F_s` and `q_*` are irrational elements of `Q_2`. In particular,
the script has no rational physical source of either sign, and no
positive ordinary infinite source.

**Proof.** Suppose `F_s=a/b` in lowest terms. The sum is 2-adically
integral, so b is odd; take b positive and put `H=|a|+b`.
For each R write the partial sum as `N_R/D_R`, where

\[
D_R=9^{t_R},\qquad
N_R=\sum_{r=0}^R4^r8^{t_r}9^{t_R-t_r}.
\tag{11}
\]

The next omitted term has strictly lower binary valuation than
every later term. Consequently

\[
v_2(aD_R-bN_R)=2(R+1)+3t_{R+1}.
\tag{12}
\]

The integer in (12) is nonzero. On the other hand,
`0<N_R<4^(R+1)D_R`, because each `(8/9)^(t_r)<=1` and
`sum_(r<=R)4^r<4^(R+1)`. Hence

\[
4^{R+1}8^{t_{R+1}}
\le|aD_R-bN_R|
<H4^{R+1}9^{t_R}.
\tag{13}
\]

Thus a rational value would require `8^(t_(R+1))/9^(t_R)<H`
for every R, contradicting (10). Multiplication by the nonzero
rational `166/9` and translation by -7 preserve irrationality.

A convenient sufficient condition is that, for some fixed
`epsilon>0`, infinitely many consecutive paid positions satisfy

\[
\frac{t_{R+1}}{t_R}\ge\log_8 9+\epsilon
\quad(t_R>0).
\tag{14}
\]

The obstruction is an exact rational-height test for this script
family. It is not an assertion that a general automatic word has
such gaps, or that every bounded carry sequence is irrational.

## 4. Four automatic families, all with scalar 7/8 and no rational source

For a fixed integer k>=1, select P precisely at the positive indices
whose binary expansion has at most k one-bits. All other blocks are L.
A finite automaton recognizes this set by counting one-bits up to k
and retaining a separate zero-input state. The script is nonperiodic:
it has infinitely many paid blocks and arbitrarily long unpaid runs.

**R10-A3.** For each `k=1,2,3,4`, this automatic script has bounded
candidate carries, positive bounded gaps, and discounted value 7/8,
but its physical 2-adic completion is irrational. Every finite
prefix still has positive ordinary realizations.

For every `h=2^n`, the paid positions

\[
(2^k-1)h\quad\text{and}\quad2^kh
\tag{15}
\]

are consecutive: an integer strictly between them has the same k
leading one-bits as the left endpoint and at least one additional
one-bit below them. The ratio in (10) along these pairs is

\[
\left(\frac{8^{2^k}}{9^{2^k-1}}\right)^h.
\tag{16}
\]

For k<=4 its base exceeds one. The weakest case k=4 follows from
`8^16=2^48>3^30=9^15`, equivalently `256>243` raised to the sixth
power. Therefore R10-A2 applies. The finite ordinary realization is
exactly R9-A3 at each finite depth; it does not contradict the
irrational completion.

For k=1, paid positions are `1,2,4,8,...`, the specific round-nine
example. Writing

\[
F(z)=\sum_{r\ge0}4^rz^{2^r},
\qquad F(z)=z+4F(z^2),
\tag{17}
\]

its completion is `-7-(166/9)F(8/9)` in `Q_2`. The functional
identity explains a Mahler-type connection, but the irrationality
proof above imports no Mahler value theorem. Although the series
also converges in the real embedding, the two values are not
identified.

The displayed gap test does not extend to all k: at k=5,
`8^32<9^31`, so (16) decreases. This is a precise limit of the
present argument, not a rational or ordinary realization at k=5.

## 5. An explicit mismatch budget for each fixed positive source

**R10-A4 (effective positive-source exclusion).** Fix `1<=k<=4`
and a positive odd source q. Let

\[
B=\operatorname{bl}(q+7),\qquad C_k=35-2^{k+1}>0,
\]

and choose h to be the least power of two satisfying

\[
C_kh\ge11B+24.
\tag{18}
\]

Then q cannot match all the first `2^(k+1)h` odd gaps of the
specified automatic script. The first differing actual odd gap
occurs within this finite budget.

| k | C_k | Odd-gap budget |
| --- | ---: | ---: |
| 1 | 31 | 4h |
| 2 | 27 | 8h |
| 3 | 19 | 16h |
| 4 | 3 | 32h |

**Proof.** If those gaps matched, (15) would provide an actual
unpaid run of length `m=h-1` starting at
`j=(2^k-1)h+1`, entirely inside the first `2^kh` blocks.
Use (4), raise both sides to the eleventh power, and use

`9^11=31381059609<34359738368=2^35`,

together with `q+7<2^B`. Comparing integer powers of two gives

\[
33m+11<2j+11B.
\]

Substitution yields `C_kh<11B+24`, contradicting (18).
All quantities in the budget are finite integers. Here B>=4 and
h>1. Since h is the least such power of two, the budget is less than

\[
\frac{2^{k+2}(11B+24)}{C_k}.
\tag{19}
\]

The construction addresses a prescribed script, not every ordinary
orbit with scalar 7/8. A finite steering prefix can be handled by
applying the same theorem to its actual positive endpoint, without
identifying that endpoint with the original source.

## 6. Literature boundary and the remaining arithmetic step

Mahler's primary paper [*An unsolved problem on the powers of 3/2*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6416420BFE33A5DDC3DAB6EA358C2B0B/S1446788700005371a.pdf/div-class-title-an-unsolved-problem-on-the-powers-of-3-2-a-href-fn01-ref-type-fn-a-div.pdf)
(1968), Sections 2--3 and equations (7)--(10), was directly inspected.
It writes the same symbolic series in real and 2-adic senses with
different resulting coordinates. Its Section 6 also distinguishes
a necessary indefinitely continuable integer algorithm from a
sufficient Z-number criterion. These are relevant warnings against
equating the two values of (17) or promoting finite cylinder legality
to an ordinary infinite source. No Z-number nonexistence theorem
is assumed here.

Eliahou and Verger-Gaugry's [*The number system in rational base 3/2
and the 3x+1 problem*](https://arxiv.org/html/2504.13716v1)
(2025), Proposition 3.1 and Corollary 3.2, were inspected in the
authors' preprint. They identify an odd shortcut step with appending
one digit in the rational-base representation. Their Section 4
leaves its further global questions open. The present shifted
two-block equation is an elementary grouped ordinary equation;
it does not identify our redundant discounted carries with the
paper's normalized rational-base digits. No general periodicity
theorem for automatic Collatz scripts is imported.

`arithmetic_tower_controls.py` replays complete ordinary cylinders,
the exact shifted equations and windows, the four automatic gap
families, the supplied-source mismatch budgets, and finite valuation
and height controls for (11)--(13). These tests corroborate the
written proofs and remain active under optimized Python.
`ArithmeticTower.lean` proves twelve finite declarations: both block
replays through an odd intermediate state, both shifted identities,
the height inequality and its finite iteration, the unpaid-run
identity and full binary divisor, the same-source window, and the
exponent, four-family budget, and exact boundary comparisons. The binary-index run
identification and infinite 2-adic irrationality argument remain
written mathematics.

The companion tower lane treats arbitrary paid excursions and their
actual cumulative valuation budget. The present theorem instead
excludes explicit scripts and all rational values for a quantitative
lacunarity class. **First unsupported step:** force an arbitrary
actual low-phase source to enter this excluded class, or exclude
the remaining scripts without that sparsity condition. Bounded
carries, automaticity alone, and rationality of the discounted
scalar do not supply such an implication here.
