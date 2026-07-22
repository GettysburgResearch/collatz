# L-9892 -- Nested one-hot obstructions give unbounded exposed rank

Claim ID: `L-9892`
Title: Every survivor suffix has arbitrarily many lower zero-block competitors outside all predecessor phases
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-b`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9826`, `L-9881`, `L-9883`, `L-9885`, `L-9886`
Scope: one-hot exposing prefixes, delayed one-hot competitors, and the unrestricted finite-depth survivor order
Related counterexample candidates: none

## Setup

Fix

\[
m\ge1,
\qquad
v\in\{0,1\}^m,
\qquad
r=\alpha_m(v).
\tag{1}
\]

Write `w_n=0^(n-1)1` for the depth-`n` one-hot word of `L-9883`. Put

\[
O_M=\operatorname{ord}_{64^M}(81)=2^{6M-4}.
\tag{2}
\]

By `L-9881`, the powers of `81` modulo `64^M` are exactly the unit classes
congruent to one modulo 16, and (2) is their exact order.

## Statement 1 -- arbitrary lower rank outside the predecessor phase

For every `s,D>=1`, there are infinitely many depths

\[
\boxed{
n\equiv1\pmod4,
\qquad
n\not\equiv1\pmod {36},
}
\tag{3}
\]

such that `w_n v` is the exposed cylinder minimum of `L-9883`, but its
representative has at least `s` distinct lower global competitors. Every one
of those competitors

- first differs from `w_n v` after position `D`;
- has an exact zero terminal block of length `m`;
- is a pure power of 64 at depth `n+m`.

More exactly, choose `h_1>=m+2` in the unique class

\[
17\,81^{h_1-1}
\equiv17+64r
\pmod {64^{m+1}}.
\tag{4}
\]

Recursively define

\[
h_{i+1}=h_i+O_{m+h_i}
\qquad(1\le i<s).
\tag{5}
\]

For every `M>=1`, let `d_M` be the unique class modulo `O_M` with

\[
81^{d_M}\equiv17\pmod {64^M}.
\tag{6}
\]

Choose `n>h_s+D` in the class

\[
n\equiv h_s-1+d_{m+h_s}
\pmod {O_{m+h_s}}.
\tag{7}
\]

For `1<=i<=s`, define

\[
\omega_i
=0^{\,n-h_i}1\,0^{\,m+h_i-1}.
\tag{8}
\]

Then

\[
\boxed{
\alpha_{n+m}(w_nv)=A_*=64^{n-1},
\qquad
\alpha_{n+m}(\omega_i)=B_i=64^{n-h_i}.
}
\tag{9}
\]

The order is strict:

\[
\boxed{
B_s<\cdots<B_1<A_*,
\qquad
{B_i\over A_*}=64^{1-h_i}.
}
\tag{10}
\]

Thus the global rank of the exposed representative is unbounded along its
own exposing depth class, even after every legal-predecessor phase of
`L-9886` is excluded.

### Proof

The ratio `(17+64r)/17` is one modulo 16. The subgroup theorem quoted after
(2) therefore gives the unique class (4), and periods allow `h_1` to be as
large as needed. Every later increment in (5) is divisible by `O_(m+1)`, so
all `h_i` retain (4).

The discrete logarithms in (6) are compatible under reduction. Also, every
later increment `h_(j+1)-h_j` is divisible by each earlier `O_(m+h_i)`.
Therefore (7) implies, for every `i<=s`,

\[
\boxed{
17\,81^{-(n-h_i+1)}
\equiv1
\pmod {64^{m+h_i}}.
}
\tag{11}
\]

Combining (4) and (11) gives

\[
81^{-n}
\equiv(17+64r)^{-1}
\pmod {64^{m+1}}.
\tag{12}
\]

This is exactly the one-hot exposure congruence of `L-9883`, proving the
first identity in (9).

The exact cylinder formula of `L-9826` gives

\[
\begin{aligned}
\alpha_{n+m}(\omega_i)
&=64^{n-h_i}
 [17\,81^{-(n-h_i+1)}]_{64^{m+h_i}}\\
&=64^{n-h_i},
\end{aligned}
\tag{13}
\]

by (11). Its depth-`n` prefix already has representative `B_i`, so the final
`m` zeros leave it unchanged. By `L-9885`, this is an exact zero renewal
block, not only a congruence coincidence.

The sequence `h_i` is strictly increasing, proving (10). The condition
`n>h_s+D` makes every first difference occur after position `D`.

The exposure congruence (12) forces `n=1 mod4`. Adding multiples of the
power-of-two modulus `O_(m+h_s)` preserves every displayed condition and
cycles through every residue modulo 9. Infinitely many choices therefore
avoid `n=1 mod9`; together with `n=1 mod4`, these are exactly the choices in
(3). **QED**

## Statement 2 -- exact signed geometry

Every competitor in Statement 1 satisfies

\[
A_*-B_i
=64^{n-h_i}(64^{h_i-1}-1).
\tag{14}
\]

Consequently,

\[
\boxed{
v_2(A_*-B_i)=6(n-h_i),
\qquad
{A_*-B_i\over64^{n-h_i}}\equiv-1\pmod {64}.
}
\tag{15}
\]

Thus these failures can be simultaneously arbitrarily late in the word,
arbitrarily far below the exposed point, and arbitrarily numerous.

### Proof

Equation (14) follows from (9), and its parenthetical factor is odd. Since
`h_i>=2`, that factor is `-1 mod64`, proving (15). Increasing the initial
solution of (4), then choosing `n`, makes every ratio in (10) and every first
difference as small and as late as desired. **QED**

## Statement 3 -- the selected family is thin

Call a delay `h` admissible when it satisfies the exposure compatibility
condition (4). For one fixed admissible delay, the pure-power condition

\[
17\,81^{-(n-h+1)}\equiv1\pmod {64^{m+h}}
\tag{16}
\]

selects one refinement class modulo `O_(m+h)` inside the exposure class
modulo `O_(m+1)`. Its exact relative Haar density is

\[
\boxed{
{O_{m+1}\over O_{m+h}}=64^{1-h}.
}
\tag{17}
\]

Even if one unions these explicitly selected refinements over every
`h>=m+2`, the relative measure is at most

\[
\sum_{h\ge m+2}64^{1-h}
={64^{-m}\over63}.
\tag{18}
\]

Hence their complement in the 2-adic phase parameterization of the one-hot
exposing class has relative Haar measure at least

\[
\boxed{1-{64^{-m}\over63}>0.}
\tag{19}
\]

The rank obstruction is therefore arbitrarily severe on a thin selected phase
family. It does not prove universal failure at every exposing depth. In
particular, positive Haar measure in this 2-adic parameter space does not by
itself produce an ordinary integer depth outside the selected countable union;
(19) is not a natural-density statement. It also does not exclude other
one-hot coefficients or multi-hot competitors.

### Proof

Equation (17) follows directly from the exact orders in (2). The geometric
series gives (18), and the union bound gives (19). **QED**

## Statement 4 -- later-orbit mergers add no phases

The legal survivor map is globally injective:

\[
\boxed{T(64q+e)=81q+e,\qquad e\in\{0,1\}.}
\tag{20}
\]

Let

\[
A_j=T^j(A_*).
\tag{21}
\]

If an ordinary nonnegative legal point `B` has all the displayed iterates
defined and satisfies

\[
T^k(B)=A_j,
\tag{22}
\]

then exactly one of the following holds:

\[
k\le j
\Longrightarrow
B=A_{j-k}\ge A_*,
\tag{23}
\]

\[
k>j
\Longrightarrow
T^{k-j}(B)=A_*.
\tag{24}
\]

Thus a lower orbit merging into a later point is either already on the
forward one-hot trajectory or is a predecessor of `A_*`. The latter depths
are exactly the phase family classified by `L-9886`. Later-target mergers
create no new obstruction phases.

At the depths in Statement 1, which lie outside `n=1 mod36`, the competitors
`B_i` cannot merge into the candidate trajectory during any legal comparison
interval.

### Proof

Equality in (20) first determines `e` and then `q`, proving injectivity.
Apply injectivity `min(k,j)` times to (22). This gives (23) or (24).
The one-hot forward trajectory is increasing, while `L-9886` classifies every
finite legal predecessor of `A_*` inside `n=1 mod36`. **QED**

## What this advances

- `L-9886` produced one lower predecessor at arbitrarily deep exposures but
  only inside the one-step obstruction phase. Statement 1 gives unbounded
  lower rank at infinitely many depths outside that entire phase family.
- The failures occur after arbitrarily long common prefixes and have an exact
  signed difference unit, making them directly usable in survivor
  order-statistic and state-complexity arguments.
- The merger lemma closes the natural attempt to obtain additional phases by
  merging into a later point of the one-hot orbit.
- The density calculation sharply quarantines the result inside the 2-adic
  phase parameterization. It leaves a positive-Haar-measure complement but
  does not establish ordinary-depth or natural-density avoidance.

## Dependency audit

- `L-9826` supplies the exact cylinder formula and legal-map injectivity.
- `L-9881` supplies the exact order and subgroup generated by `81` modulo
  powers of 64.
- `L-9883` supplies the one-hot exposure congruence and cylinder-minimum
  interpretation.
- `L-9885` identifies the unchanged terminal zeros with a genuine zero
  renewal block.
- `L-9886` supplies the complete predecessor-phase exclusion used in
  Statement 4.
- No experiment or infinite-survival hypothesis is used.

## Gap audit

- The explicit pure-power family has small relative Haar measure and cannot
  decide the remaining 2-adic phase parameters in (19); that measure statement
  alone supplies no ordinary depth in the complement.
- The union bound concerns one selected refinement per delay. Other lower
  one-hot coefficients and multi-hot words are not counted.
- Unbounded finite-depth rank does not construct one ordinary infinite
  survivor or one fixed depth with infinitely many lower points.
- The result still does not identify the first positive block above the
  exposed point, so the global successor problem remains open.

## Adversarial checks

- The compatibility of (11) uses both nested logarithm classes and the large
  period in (5); reducing only (7) would not retain all earlier delays.
- The final `m` zeros are verified at depth `n`, not merely in the full
  length-`n+m` congruence.
- Adding the deepest period changes `n mod9` because that period is a power of
  two; it does not change `n mod4`.
- The exact density `64^(1-h)` is for the selected pure-power refinement at
  one fixed delay, not for all possible lower one-hot lifts.
- Statement 4 uses global injectivity only on legal chart points.

## Remaining uncertainty

Which lower zero-block words occur outside the selected refinements, and what
is the first positive centered block there? Pure-power delayed one-hot
witnesses and the Haar-measure bound alone cannot answer that question.

## Suggested next attack

For arbitrary `h`, put

\[
c_h
=[17\,81^{h-1}(17+64r)^{-1}]_{64^{m+1}}.
\tag{25}
\]

All lower one-hot zero-block lifts at that delay are characterized by

\[
[17\,81^{-(n-h+1)}]_{64^{m+h}}
=c_h+64^{m+1}q<64^{h-1},
\tag{26}
\]

with `0<=q<64^(h-m-2)`. Their fixed-`h` relative density is `64^(-m-1)`.
Determine correlations and ordinary-depth avoidance for these events across
`h`, then attack multi-hot competitors or the first positive block outside
the selected refinements.
