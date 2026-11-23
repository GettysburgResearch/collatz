# One weighted product pays for every triadic denominator drop

**Status:** a new finite sufficient certificate for the full convergence
claim; construction of a certificate for every positive source remains open.
This note builds on PR178 at
`4e204f54136c79cf8c9393b34e3330594f99ae0a`, especially
`research/global-closure-20261123/duality/TRIADIC_RANK.md`.

The new point is an amortized product that removes the multiplication of
the candidate numerator height by its denominator exponent. There is one
potential across both signs and all denominator levels. No new cycle
exclusion assumption or probability law enters.

## 1. Exact paired states and the product

Write the shortcut map as `T(x)=x/2` on even inputs and `(3x+1)/2` on odd
inputs. A complementary triadic candidate is one fixed signed rational
`a/3^r`. The paired integer state is `(x,w,r)`, with represented rational
`y=w/3^r` and opposite parities of `x` and `w`. Its exact transitions are

| Original parity | New original state | New numerator | New exponent |
|---|---:|---:|---:|
| odd | `(3x+1)/2` | `w/2` | `r` |
| even, `r>0` | `x/2` | `(w+3^(r-1))/2` | `r-1` |
| even, `r=0` | `x/2` | `(3w+1)/2` | `0` |

These equations are used only while the actual parity test passes.
Lowest terms are unnecessary. Define the integer denominator weight

\[
 F(0)=1,\qquad F(r)=\prod_{j=0}^{r-1}(1+3^j),\qquad
 P(x,w,r)=x|w|F(r).
\]

Suppose `x>1` and `w!=0`.

**Original odd step.** An odd positive `x>1` is at least 3. Hence

\[
 \frac{P'}P=\frac{3x+1}{4x}\le\frac56.
\]

**Original even step, positive denominator exponent.** Put `r=j+1`.
The triangle inequality and `|w|>=1` give

\[
 2|w'|=|w+3^j|\le|w|+3^j\le|w|(1+3^j).
\]

Since `F(j+1)=(1+3^j)F(j)` and `x'=x/2`,

\[
                         P'\le\frac14P.                 \tag{1}
\]

This pays for the entire possible numerator increase at a denominator
drop. It includes negative numerators and negative-to-positive crossings.

**Original even step, exponent zero.** Here

\[
 \frac{P'}P=\frac{|3w+1|}{4|w|}.
\]

If `w<0`, the ratio is at most `3/4`. If positive odd `w!=1`, then
`w>=3`, and the ratio is at most `5/6`. The single remaining case is
`w=1`, for which `w'=2` and `P'=P`. If the next parity test also passes,
the next original state is odd. Unless that state is 1, the next step
contracts by at least `5/6`.

Thus `P` never increases at a nonterminal, nonzero step; every two such
consecutive steps contract by `5/6`. Four two-step blocks give

\[
 P_{i+8}\le(5/6)^4P_i<\tfrac12P_i,                      \tag{2}
\]

because `2*5^4=1250<1296=6^4`. No denominator clock has to be charged
separately from this product.

## 2. The zero numerator is included

Starting from `w!=0`, a zero numerator can only be created by the even
positive-denominator branch: immediately before it, `w=-3^j`, and
`x'=x/2`. For an original state `x>1`,

\[
               x'+1\le x\le x|w|F(j+1)=P.               \tag{3}
\]

Once the numerator is zero, a passed parity test forces an original odd
step and keeps that numerator zero. If there are `L` subsequent passed
steps, the fixed integer at zero entry satisfies

\[
                             2^L\mid x'+1.               \tag{4}
\]

This follows from `2(x_{i+1}+1)=3(x_i+1)` and coprimality of 2 and 3.
The finite zero tail therefore consumes at most the binary length of the
same preceding product. It is not an unexamined exceptional trajectory.

## 3. A smaller sufficient horizon

For a positive integer `m`, let `bl(m)` be the least positive `E` with
`m<2^E`. For one original input `n>0` and one candidate `(a,r)`, set

\[
 B=n\max(1,|a|)F(r),\qquad E=\operatorname{bl}(B),\qquad
                         H=9E+1.                         \tag{5}
\]

**Finite paired theorem.** If the first `H` actual complementary parity
tests all pass, then the original orbit reaches 1 by clock `H`.

Here is the complete clock argument. Assume it has not reached 1. If
`a=0`, (4) at the initial state contradicts `n+1<=2^E<2^H`.
Otherwise, if no zero numerator occurs by clock `8E`, applying (2) `E`
times gives a positive integer product below 1. Hence a first zero occurs
at a clock `j` with `1<=j<=8E`. Every earlier product is at most
`P_0=B`. By (3), `x_j+1<=B<2^E`. There are at least
`H-j>=E+1` further passed steps. Equation (4) makes the strictly positive
integer `x_j+1<2^E` divisible by `2^(E+1)`, a contradiction.

The convenient factor 9 leaves a separate zero-tail allowance; the
weighted-product gain does not depend on optimizing this factor.

Let `e_i=T^i(n) mod2` be the original actual word, `b_i` its even count,
and let the complete complementary carry satisfy

\[
 D_0=0,\qquad D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i.
\]

The same inverse-word argument as PR178 gives a finite arithmetic
certificate:

\[
                  2^H\mid3^{b_H}a+3^rD_H                \tag{6}
\]

implies that all `H` parity tests pass. Therefore (6), at the horizon (5),
forces the original `n` to reach 1. Pulling back the literal affine word
from its terminal odd-denominator rational proves legality at every
prefix, so no endpoint-only substitution is used.

## 4. Exact height gain and the remaining construction

The weight has the exact logarithmic form

\[
 \log_2F(r)=\frac{r(r-1)}2\log_2 3
       +\sum_{j=0}^{r-1}\log_2(1+3^{-j}).                 \tag{7}
\]

The last sum is less than 2: its `j=0` term is 1, and for `j>=1`,
`log_2(1+3^-j) <=3^-j/ln2`, whose sum is `1/(2ln2)<1`.
Consequently

\[
 H=O\bigl(\log n+\log\max(1,|a|)+r^2\bigr).
\]

The preceding certificate used
`8 bl(n)+(9r+8) bl(max(1,|a|,3^r))+2`.
Its numerator-height term was multiplied by `r`. The present term is
additive; its leading quadratic denominator cost is half that of the
naive independent-level budget before the final constant. The old
certificate remains available when its numerical horizon is smaller.

The remaining full-strength task is still to construct `K,a,r` from each
fixed positive `n` such that

\[
 K\ge9\operatorname{bl}\bigl(n\max(1,|a|)F(r)\bigr)+1,
 \qquad 2^K\mid3^{b_K}a+3^rD_K.                         \tag{8}
\]

Unrestricted centered residues do not achieve this height. The universal
construction was attempted through the original/complementary carry
pair and through rational reconstruction, but no sufficient small-residue
estimate was obtained. This checkpoint improves the exact certificate
window; it does not assert a witness in that window.

## 5. Literature that motivated the attempted construction

Monks–Yazinski, *The autoconjugacy of the 3x+1 function*,
[primary paper](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Theorem 2.1, supplies the rational complementary-parity framework.
The triadic specialization and prior finite horizon are credited to
PR178 above.

Monks's 2025
[q-analog paper](https://cs.uwaterloo.ca/journals/JIS/VOL28/Monks/monks6.pdf),
Theorem 5 and Conjecture 6, prompted an attempted polynomial construction.
For its map with `A=1`, `B=1+q^2`, direct inverse iteration gives

\[
 H_n(q)=(1+q^2)\sum_{i\ge0}e_iq^i\quad\text{in }\mathbb F_2[[q]].
\]

Its coefficients are `e_i+e_(i-2)` with missing negative-index bits zero.
For a positive integer whose first hit of 1 is at clock `tau`, this
polynomial has degree exactly `tau`: at `tau=0,1` this is direct; if
`tau>=2`, its two preceding states are 4 and 2, so the coefficient at
`tau` is 1 and every later coefficient is zero. Thus polynomiality did
not supply an independent shorter certificate or a universal triadic
candidate. This observation is a direct reconstruction, not a claim of
priority for the conjugacy.

No general 2-adic rationality, automaticity of every integer orbit,
algebraic-series coherence, or unrestricted approximation theorem is
assumed in the weighted-product proof.

## 6. Verification scope

The companion Lean module proves the new integer potential and its
finite contraction consequences against the exact `TriadicStep`
constructors copied unchanged from the pinned PR178 dependency. The
precise declaration and execution inventory is supplied separately.
The full height-dependent congruence-to-convergence argument above is
written mathematics unless explicitly included in that inventory.

Exact controls use the same complete paired rules, both signs, zero
entry, the integral tie, several large denominator drops, and actual
finite candidates. They do not test the universal existence assertion
(8). This note makes no full Collatz claim.
