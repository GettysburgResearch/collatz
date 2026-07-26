# T-8260 — All-repetition exclusion of three-pulse lifts of the two known negative cycles

**Claim ID:** `T-8260`  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Authoring agent:** `gpt56-sol-04`  
**Reviewing agents:** none yet  
**Created:** 2026-07-26  
**Issue:** #52  
**Dependencies:** elementary accelerated Collatz affine algebra; the
L-8201 resultant/Bézout argument reconstructed below; elementary
continued-fraction facts; the exact two-logarithm Matveev statement recorded
for `T-8202` and `T-8255`  
**Scope:** exactly three positive valuation increases at distinct positions of
an arbitrary repetition and rotation of either known ordinary negative
accelerated Collatz cycle

## Statement and status split

Let

```text
P3  = (1,2),                 (A,k)=(3,2),
P11 = (1,1,1,2,1,1,4),      (A,k)=(11,7).
```

Repeat either primitive word any number `r>=1` of times, rotate it arbitrarily,
choose exactly three distinct positions, and increase their valuations by
arbitrary integers `d1,d2,d3>=1`.

Two conclusions must be distinguished.

1. **Proved finite computation.** For `P3` at `r=2,3` and `P11` at `r=1`,
   every support, primitive rotation, and arbitrary positive height triple is
   exhausted using exact nonzero resultant caps.  The sole divisor hit is

   ```text
   P3, r=3, support (0,2,4), heights (1,1,1):
   (1,2)^3 -> (2,2,2,2,2,2),  n=1.
   ```

   `P3,r=1` has only two positions and is structurally outside the class.

2. **Conditional all-repetition conclusion.** Subject to independent
   reconstruction of the quoted Matveev theorem and its normalization, those
   are the only repetitions that require finite height enumeration.
   Consequently no exactly-three-pulse lift in the full stated class encodes a
   nontrivial positive integral Collatz cycle.

The second conclusion remains `PROPOSED / SOURCE-DEPENDENT`.  The finite
computation and every native inequality after the quoted logarithmic-form
bound are independently replayable and do not inherit that source status.

No divergent orbit, nontrivial positive cycle, or unconditional Collatz
counterexample is constructed.

## 1. Largest-gap normalization

For a repeated word of length

\[
N=kr,
\]

the three support points cut the cyclic index set into positive gaps
`g1,g2,g3` with sum `N`.  Rotate the support point following a largest gap to
position zero.  With a fixed lexicographic tie rule, write the normalized
support as

\[
0=p_1<p_2<p_3<N.
\]

The final gap is `N-p3=max(g1,g2,g3)`.  Since the largest of three positive
integers summing to `N` is at least `ceil(N/3)`,

\[
\boxed{p_3\le N-\lceil N/3\rceil=\lfloor2N/3\rfloor.}
\tag{1}
\]

Rotations of a repeated primitive word reduce to the `k` primitive rotations.
`X-8260` explicitly maps all 293 raw rotation/support configurations in the
finite range to 45 normalized packets and verifies that every primitive
rotation occurs.

## 2. Exact distributed-pulse correction

Let the normalized repeated word be

\[
w=(a_0,\ldots,a_{N-1}),\qquad
B_j=\sum_{h<j}a_h,
\]

and let `z_j` be its ordinary negative cycle states.  Put

\[
\mathcal U=2^{Ar},\qquad \mathcal Q=3^{kr},
\qquad X_i=2^{d_i},\qquad P_i=X_1\cdots X_i.
\]

For the perturbed total pulse

\[
t=d_1+d_2+d_3,
\]

the denominator is

\[
\boxed{D=\mathcal U2^t-\mathcal Q.}
\tag{2}
\]

The full L-8201 pulse weights share the factor

\[
G=2^{a_0}3^{N-1-p_3}.
\]

Since `D` is odd and is not divisible by `3`,

\[
\gcd(D,G)=1.
\tag{3}
\]

After removing `G`, define

\[
\begin{aligned}
w_1&=(-z_1)3^{p_3},\\
w_2&=(-z_{p_2+1})3^{p_3-p_2}2^{B_{p_2+1}-a_0},\\
w_3&=(-z_{p_3+1})2^{B_{p_3+1}-a_0}.
\end{aligned}
\tag{4}
\]

The affine segment identity between successive support positions gives

\[
w_1>w_2>w_3>0.
\tag{5}
\]

Equivalently, each difference is a positive accelerated segment numerator.
The reduced distributed-pulse correction is

\[
\begin{aligned}
R={}&w_1(X_1-1)
  +w_2X_1(X_2-1)
  +w_3X_1X_2(X_3-1)\\
={}&-w_1+(w_1-w_2)X_1+(w_2-w_3)X_1X_2+w_3X_1X_2X_3.
\end{aligned}
\tag{6}
\]

If `C_b` is the standard affine numerator of the pulsed word and `z_0` is the
negative baseline state, direct affine subtraction gives

\[
\boxed{C_b-z_0D=GR.}
\tag{7}
\]

Thus

\[
\boxed{D\mid C_b\iff D\mid R.}
\tag{8}
\]

`X-8260` checks (4)--(8), including `C_b-z_0D=GR`, for every finite tuple.

## 3. Uniform exponential proximity

Formula (6) is a positive pulse sum, so `R>0`.  Its three nonconstant
coefficients are positive and sum to `w1`.  Since each partial product is at
most `X1X2X3=2^t`,

\[
0<R<w_1\,2^t.
\tag{9}
\]

The first post-rotation state is one of the primitive negative states, whose
absolute value is at most

```text
c_* = 7   for P3,
c_* = 91  for P11.
```

By (1) and (4),

\[
w_1\le c_*3^{\lfloor2kr/3\rfloor}.
\tag{10}
\]

Define

\[
\Lambda=(Ar+t)\log2-kr\log3>0.
\tag{11}
\]

If `D|R`, then `D<=R`; dividing (2) and (9) by
`\mathcal U2^t` yields

\[
\boxed{
0<1-e^{-\Lambda}
<c_*{3^{\lfloor2kr/3\rfloor}\over2^{Ar}}.}
\tag{12}
\]

Exact integer residue-class certificates prove that the right side is below
`1/2` for

```text
P3:  r>=4,
P11: r>=2.
```

Using `-log(1-x)<2x` on those ranges gives

\[
\boxed{
0<\Lambda
<2c_*{3^{\lfloor2kr/3\rfloor}\over2^{Ar}}.}
\tag{13}
\]

The effective exponential rates are positive:

\[
A\log2-\frac{2k}{3}\log3>0
\tag{14}
\]

for both primitive families.

## 4. Source-dependent Matveev cutoff

Use the nonzero two-logarithm form

\[
\Lambda=(Ar+t)\log2-kr\log3.
\tag{15}
\]

In the exact Matveev convention inherited from `T-8202`,

\[
K_2=2^{32}\log2\log3.
\]

Once `Lambda<log3`, its normalized coefficient parameter satisfies
`B<kr+1`, and the quoted theorem gives

\[
\log\Lambda\ge-K_2(1+\log(kr+1)).
\tag{16}
\]

Equation (13), with
`\lfloor2kr/3\rfloor\le2kr/3`, gives

\[
\log\Lambda
<\log(2c_*)-
r\left(A\log2-\frac{2k}{3}\log3\right).
\tag{17}
\]

Combining the bounds produces a necessary inequality.  Exact rational
logarithm intervals certify its failure at and beyond:

| family | cutoff | cutoff margin | derivative margin |
|---|---:|---:|---:|
| `P3` | `200,000,000,000` | `32,280,745,255.142788801272` | `0.598272068585801669` |
| `P11` | `50,000,000,000` | `34,680,525,975.148380266802` | `2.432349286228691192` |

The derivative is increasing thereafter.  Separate exact margins certify
`Lambda<1<log3` before (16) is used.

This is the sole non-elementary source boundary.  The primary Matveev
statement has not been reconstructed line by line in this work, so no
unconditional all-repetition status is asserted.

## 5. Legendre ranges and transition repetitions

Divide (13) by `r log2`:

\[
0<{t\over r}-\eta
<
{2c_*3^{\lfloor2kr/3\rfloor}
\over r\log2\,2^{Ar}},
\qquad
\eta=\log_2(3^k/2^A).
\tag{18}
\]

The inequality

\[
4c_*r3^{\lfloor2kr/3\rfloor}<\log2\,2^{Ar}
\tag{19}
\]

is certified in each residue class modulo three beginning at

```text
P3:  r=10,
P11: r=3.
```

For `P3`, the first three lower margins are

```text
r=10:    297,850,677.954893017873
r=11:  4,480,934,491.639144142991
r=12: 33,169,013,293.113153143929
```

For `P11`, they are

```text
r=3:          731,086,795.639144142991
r=4:   11,629,889,924,588.967204846029
r=5:   24,801,918,487,196,296.835524669335
```

The certified three-step ratios are below one, so (19) persists.  Hence

\[
0<{t\over r}-\eta<{1\over2r^2}.
\tag{20}
\]

After reducing `t/r=p/q`, Legendre's criterion makes `p/q` an upper
continued-fraction convergent of `eta`.

Exactly three positive pulses also give `t>=3`.  Before the Legendre ranges,
the lower bound

\[
\Lambda\ge(Ar+3)\log2-kr\log3
\tag{21}
\]

exceeds (13) by the following certified margins:

| family | repetitions | smallest listed margin |
|---|---|---:|
| `P3` | `4,5,6,7,8,9` | `0.777742992804302110` |
| `P11` | `2` | `1.094019166218095102` |

Therefore the only repetitions not analytically rejected are

```text
P3:  r=2,3,
P11: r=1.
```

## 6. Continued fractions and the exceptional `1/5` row

The exact atanh-series intervals for `eta` have widths below `2^-576` for P3
and `2^-574` for P11.  They certify all 38 continued-fraction rows through
the first denominator beyond the Matveev cutoffs.

If `p/q` is an upper convergent and `q_+` is the next convergent denominator,
the complete-quotient identity gives

\[
p-q\eta>{1\over q+q_+}.
\tag{22}
\]

For a multiple `(r,t)=m(q,p)`,

\[
\Lambda>{\log2\over q+q_+}.
\tag{23}
\]

The right side of (13) decreases with `m`; `X-8260` certifies the logarithmic
decay margin separately for every row.  It is enough to check `m=1`, where
(13) and (23) are incompatible if

\[
\boxed{
2^{Aq}>
4c_*3^{\lfloor2kq/3\rfloor}(q+q_+).}
\tag{24}
\]

Exact rational log margins certify (24) for ten P3 upper rows and all seven
P11 upper rows.  The only exception is the first P3 row

\[
{p\over q}={1\over5}.
\]

Here `(r,t)=(5m,m)`.  Three distinct positive pulses force `m=t>=3`, and
(12) becomes

\[
1-\left({59049\over65536}\right)^m
<
7{3^{\lfloor20m/3\rfloor}\over8^{5m}}.
\tag{25}
\]

The left side increases with `m`; the right side decreases, with one-step
ratio at most `3^7/8^5`.  At `m=3`, left minus right is exactly

\[
\boxed{
{75388584689551\over281474976710656}>0.}
\tag{26}
\]

Thus every `m>=3` is impossible.

## 7. Exact coordinate caps and finite exhaustion

For one normalized packet write

\[
R=\sum_{j=0}^{3}c_jP_j,
\qquad
(c_0,c_1,c_2,c_3)
=(-w_1,w_1-w_2,w_2-w_3,w_3).
\tag{27}
\]

For coordinate `i=1,2,3`, define `R_i^-`, `R_i^+`, and `S_i` exactly as in
L-8201, but using the reduced coefficients.  The reduced eliminant is

\[
E_i=\mathcal U S_iR_i^-+\mathcal QR_i^+.
\tag{28}
\]

Direct expansion gives the Bézout identity

\[
\boxed{\mathcal U S_iR-R_i^+D=E_i.}
\tag{29}
\]

Since `D` is odd,

\[
D\mid R\iff D\mid E_i.
\tag{30}
\]

The reduced coefficient valuations are

\[
\nu_2(c_i)=B_{p_i+1}-a_0.
\tag{31}
\]

In (28), `\mathcal Qc_i` is the unique term of least `2`-adic valuation, so

\[
\boxed{\nu_2(E_i)=B_{p_i+1}-a_0;}
\tag{32}
\]

in particular, `E_i` cannot vanish.

Put

\[
\Lambda_i=
\mathcal U\sum_{j<i}|c_j|
+\mathcal Q\sum_{j\ge i}|c_j|.
\tag{33}
\]

The product of the two other pulse variables is at least four.  The L-8201
norm argument, now reconstructed for `R`, gives every divisor hit the cap

\[
\boxed{
X_i\le
\left\lfloor{4\Lambda_i+\mathcal Q\over4\mathcal U}\right\rfloor.}
\tag{34}
\]

`X-8260` compiles (34) for every normalized packet, enumerates every
power-of-two coordinate in all 45 resulting boxes, and checks (27)--(34) on
every tuple.

Frozen finite totals:

| family/range | normalized packets | capped height tuples |
|---|---:|---:|
| `P3, r=2` | 2 | 559 |
| `P3, r=3` | 8 | 4,336 |
| `P11, r=1` | 35 | 48,913 |
| **total** | **45** | **53,808** |

There are `161,424` exact resultant identities.  Every tuple also checks
`C_b-z_0D=GR`.  The sole divisor hit has

```text
D=R=3367,
C_b=3367,
n=C_b/D=1,
word=(2,2,2,2,2,2).
```

It closes under exact valuation replay.  There are no nontrivial hits. ∎

## Invalid scout premise

PR #51 `X-8002` is useful corroboration but is not an arbitrary-height
exhaustion.  For each repetition it scans pulse compositions only at the
least total pulse making `D>0` and the next three totals.  Therefore the
premise

> “X-8002 found no nontrivial hit, so all three-pulse heights are excluded”

is invalid.  Arbitrary heights are closed here only by the nonvanishing
coordinate caps (28)--(34), followed by complete cap-box enumeration.

`X-8002` did independently see the same trivial `r=3` hit in its bounded
window.

## Dependency audit

1. The distributed-pulse formula, common-factor removal, and `C_b-z_0D=GR`
   identity are derived above and replayed for every finite tuple.
2. The L-8201 resultant, valuation, and cap argument is reconstructed in
   reduced coordinates; it is not invoked as an opaque software dependency.
3. Largest-gap normalization, transition margins, continued fractions,
   candidate-family decay, the exceptional row, and finite enumeration are
   implemented independently in `run.py` and `verify.py`.
4. The exact Matveev theorem formulation is the sole external
   non-elementary dependency.

## Gap audit

- The all-repetition theorem remains `PROPOSED / SOURCE-DEPENDENT` until the
  primary Matveev statement and substitution are independently reconstructed.
- The proved finite computation does not depend on Matveev.
- The result covers exactly three distinct pulse locations, not four or a
  support size growing with repetition.
- It covers only repetitions of the two known ordinary negative cycles.
- It proves no divergent-orbit statement and no global Collatz result.
- Agreement of two standard-library programs is not independent mathematical
  peer review.

## Adversarial verification

`X-8260` provides:

1. exact rational interval certificates for every analytic margin;
2. all 38 certified continued-fraction rows and all 18 primitive upper
   families;
3. an explicit `1/5` exceptional certificate;
4. a normalization transcript covering all raw supports and primitive
   rotations;
5. packet-level reduced weights, coefficients, valuations, norms, and caps;
6. one compressed transcript row for every finite height tuple;
7. independent reconstruction that imports no author module;
8. exact replay of every hit;
9. transcript-tampering regression tests.

Frozen master transcript:

```text
3ecc48c9b33c99f9395cb61e28fed61ad9cd8f5ed48b3eac246a97cc1f7655cc
```
