# T-8255 — All-repetition exclusion of two-pulse lifts of the two known negative cycles

**Claim ID:** `T-8255`  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-26  
**Issue:** #52; global-blocker context #55  
**Dependencies:** elementary accelerated Collatz affine algebra; the exact two-logarithm Matveev statement already recorded for `T-8202`; elementary continued-fraction facts  
**Scope:** exactly two positive valuation increases at distinct positions of an arbitrary repetition and rotation of either known ordinary negative accelerated Collatz cycle  
**Related counterexample candidates:** none

## Statement

Consider either primitive accelerated negative cycle

```text
P3  = (1,2),                 (A,k)=(3,2),
P11 = (1,1,1,2,1,1,4),      (A,k)=(11,7).
```

Repeat the chosen primitive word an arbitrary number `r>=1` of times, rotate it arbitrarily, choose two distinct positions, and increase the valuations at those positions by arbitrary integers

```text
d_1>=1,
d_2>=1.
```

Subject to independent reconstruction of the quoted Matveev theorem and its specialization, the resulting accelerated word cannot encode a nontrivial positive integral Collatz cycle.

The unique divisor hit over the entire two-family parameter space is

```text
P3, r=2, word (1,2,1,2),
positions 0 and 2,
d_1=d_2=1,

(1,2,1,2) -> (2,2,2,2),
n=1.
```

Thus the sole hit is the trivial accelerated Collatz cycle. No nontrivial positive cycle is produced by any two-pulse lift of either known negative cycle, for any repetition, gap, rotation, or pulse heights.

This removes the repetition bound from branch-qualified PR #51 `L-8001/X-8001` for the complete two-pulse class.

No divergent orbit, positive nontrivial cycle, or unconditional Collatz counterexample is constructed.

## Definitions

For one primitive cycle put

\[
U=2^A,
\qquad
Q=3^k,
\qquad
\eta=\log_2(Q/U)>0.
\]

After `r` repetitions and total pulse height

\[
t=d_1+d_2\ge2,
\]

the cycle denominator is

\[
\boxed{D=U^r2^t-Q^r.}
\tag{1}
\]

A positive accelerated cycle requires `D>0`. Define

\[
\Lambda=(Ar+t)\log2-kr\log3
       =(t-r\eta)\log2>0.
\tag{2}
\]

The negative states on the primitive cycles are

```text
P3:  -5,-7;
P11: -17,-25,-37,-55,-41,-61,-91.
```

Put

```text
c_* = 7   for P3,
c_* = 91  for P11.
```

## Proof

### 1. Exact normalized two-pulse correction

Rotate one pulse to position zero. Of the two oriented cyclic gaps, choose the shorter, and call it `g`. If the repeated word has length `kr`, then

\[
1\le g\le\left\lfloor{kr\over2}\right\rfloor.
\tag{3}
\]

Write

\[
X=2^{d_1},
\qquad
M=2^{d_2}.
\]

Let `z_j` be the negative states of the rotated repeated cycle and let

\[
S=\sum_{j=1}^{g}a_j.
\]

Define

\[
\mathfrak a=(-z_1)3^g,
\qquad
\mathfrak b=(-z_{g+1})2^S,
\qquad
\mathfrak c=\mathfrak a-\mathfrak b.
\tag{4}
\]

The unpulsed gap relation gives

\[
\mathfrak a>0,
\qquad
\mathfrak b>0,
\qquad
\mathfrak c>0,
\qquad
\mathfrak a=\mathfrak b+\mathfrak c.
\tag{5}
\]

A direct orbit-difference or numerator split gives the reduced pulse correction

\[
\boxed{
R=X(\mathfrak bM+\mathfrak c)-\mathfrak a.}
\tag{6}
\]

The full numerator differs from the negative baseline multiple of `D` by a factor coprime to `D` times `R`. Since `D` is odd and coprime to `3`, integrality is equivalent to

\[
\boxed{D\mid R.}
\tag{7}
\]

For completeness, the two one-variable eliminants are

\[
K(M)=Q^r(\mathfrak bM+\mathfrak c)-U^rM\mathfrak a,
\tag{8}
\]

\[
J(X)=U^r(X\mathfrak c-\mathfrak a)+\mathfrak bQ^r,
\tag{9}
\]

and the exact Bézout identities imply

\[
D\mid R
\iff D\mid K(M)
\iff D\mid J(X).
\tag{10}
\]

These are the branch-qualified `L-8001` eliminants, independently reconstructed by `X-8255` for every small row used below.

### 2. Gap-uniform exponential proximity

Because `M>=2`, one has `X<=2^(t-1)`. Using `(5)--(6)`,

\[
\begin{aligned}
0<R
&=\mathfrak b2^t+\mathfrak cX-\mathfrak a\\
&<\mathfrak b2^t+\mathfrak c2^{t-1}\\
&<\mathfrak a2^t.
\end{aligned}
\tag{11}
\]

If `(7)` holds with `D>0`, then `D<=R`. Since

\[
U^r2^t=Q^re^\Lambda,
\]

we obtain

\[
0<1-e^{-\Lambda}
={D\over U^r2^t}
\le {R\over U^r2^t}
< {\mathfrak a\over U^r}.
\tag{12}
\]

The first state after rotation is one of the finitely many primitive negative states, so by `(3)`

\[
\mathfrak a=(-z_1)3^g
\le c_*3^{\lfloor kr/2\rfloor}.
\tag{13}
\]

Therefore

\[
\boxed{
0<1-e^{-\Lambda}
<c_*{3^{\lfloor kr/2\rfloor}\over U^r}.}
\tag{14}
\]

For `P3` when `r>=3`, and for `P11` when `r>=2`, the right side is less than `1/2`. The elementary inequality

\[
-\log(1-x)<2x
\qquad(0<x<1/2)
\]

gives

\[
\boxed{
0<\Lambda
<2c_*{3^{\lfloor kr/2\rfloor}\over U^r}.}
\tag{15}
\]

This bound is uniform in the rotation, gap, and split of `t` between the two pulse heights. That is the decisive reduction.

### 3. Matveev removes all sufficiently large repetitions

Use the nonzero two-logarithm form

\[
\Lambda=(Ar+t)\log2-kr\log3.
\tag{16}
\]

In the exact Matveev normalization already recorded for `T-8202`, with degree one and two logarithms,

\[
K_2=2^{32}\log2\log3,
\]

and, once `Lambda<log 3`,

\[
\log\Lambda
\ge-K_2\bigl(1+\log(kr+1)\bigr).
\tag{17}
\]

From `(15)` and `floor(kr/2)<=kr/2`,

\[
\log\Lambda
<\log(2c_*)
-r\left(A\log2-{k\over2}\log3\right).
\tag{18}
\]

Hence every solution must satisfy

\[
r\left(A\log2-{k\over2}\log3\right)
<\log(2c_*)+K_2\bigl(1+\log(kr+1)\bigr).
\tag{19}
\]

`X-8255` verifies with exact rational logarithm intervals that `(19)` is impossible at and beyond:

| family | repetition cutoff | lower margin at cutoff | lower derivative at cutoff |
|---|---:|---:|---:|
| `P3` | `100,000,000,000` | `9,705,658,594.810496492978` | `0.948123076605365329` |
| `P11` | `25,000,000,000` | `6,546,362,814.894600712143` | `3.648651270195664299` |

The derivative is increasing thereafter. Therefore any divisor hit must have

```text
P3:  r < 100,000,000,000,
P11: r < 25,000,000,000.
```

The source theorem is the only non-elementary dependency in this step. The cutoff margins are exact rational interval certificates.

### 4. Legendre reduces every remaining repetition to convergents

Dividing `(15)` by `r log 2` gives

\[
0<{t\over r}-\eta
< {2c_*3^{\lfloor kr/2\rfloor}
   \over r\log2\,U^r}.
\tag{20}
\]

The exact certificate proves

\[
4c_*r3^{\lfloor kr/2\rfloor}<\log2\,U^r
\tag{21}
\]

for

```text
P3:  r>=6,
P11: r>=2.
```

The left-to-right ratio is uniformly decreasing: an upper bound for the ratio at consecutive `r` is `3/4` for `P3` and `81/1024` for `P11`.

Thus `(20)` implies

\[
0<{t\over r}-\eta<{1\over2r^2}.
\tag{22}
\]

Write the fraction in lowest terms:

\[
{t\over r}={p\over q},
\qquad
(r,t)=m(q,p).
\tag{23}
\]

Legendre's criterion shows that `p/q` is an upper continued-fraction convergent of `eta`. Since `r` lies below the Matveev cutoff, so does `q`.

The exact logarithm intervals have width below `2^-574` and certify all continued-fraction rows through the first denominator beyond each cutoff. There are 23 rows for `P3` and 15 for `P11`.

### 5. Seventeen convergent families vanish uniformly

Let `p/q` be one of the upper convergents and `q_+` the next convergent denominator. The standard complete-quotient identity gives

\[
p-q\eta>{1\over q+q_+}.
\tag{24}
\]

For a positive multiple `(r,t)=m(q,p)`,

\[
\Lambda=m(p-q\eta)\log2
>{\log2\over q+q_+}.
\tag{25}
\]

On the other hand, `(15)` gives

\[
\Lambda
<2c_*{3^{\lfloor kmq/2\rfloor}\over U^{mq}}.
\tag{26}
\]

The sequence on the right decreases with `m`. Indeed,

\[
{3^{\lfloor kq(m+1)/2\rfloor}/U^{q(m+1)}
 \over
 3^{\lfloor kqm/2\rfloor}/U^{qm}}
\le {3^{\lceil kq/2\rceil}\over U^q}<1
\tag{27}
\]

in both native families. It is therefore enough to test `m=1`.

Using `log 2>1/2`, equations `(25)--(26)` are incompatible whenever

\[
\boxed{
U^q>4c_*3^{\lfloor kq/2\rfloor}(q+q_+).}
\tag{28}
\]

Exact rational logarithm intervals verify `(28)` for:

```text
P3 upper convergents:
8/47,
26/153,
1269/7468,
4033/23734,
32377/190537,
916004/5390637,
10043667/59106470,
67557657/397573379,
559632586/3293409335,
11684726649/68764022656;

P11 upper convergents:
1/10,
2/21,
1496/15791,
18051/190537,
145913/1540182,
5380730/56796197,
1861294841/19646863616.
```

Each line excludes every positive multiple of that primitive convergent, not merely one repetition.

### 6. The sole exceptional convergent is impossible for two pulses

The only primitive row not covered by `(28)` is the first `P3` upper convergent

\[
{p\over q}={1\over5}.
\]

Then

\[
(r,t)=(5m,m).
\]

Because two distinct positive pulses are present, `t>=2`, so `m>=2`. Equation `(14)` becomes

\[
1-\left({59049\over65536}\right)^m
<7\left({3\over8}\right)^{5m}.
\tag{29}
\]

The left side increases with `m` and the right side decreases. At `m=2`, the left-minus-right margin is exactly

\[
\boxed{{806529523\over4294967296}>0.}
\tag{30}
\]

Therefore `(29)` is impossible for every `m>=2`. The case `m=1` has total pulse height one and is outside the two-pulse class; it is also covered by the small exact audit.

### 7. Complete exact audit of the non-Legendre range

The remaining repetitions are

```text
P3: 1<=r<=5,
P11: r=1.
```

For every primitive rotation and every shorter cyclic gap, `X-8255` reconstructs the two eliminants `(8)--(10)`, applies their proved all-size caps, enumerates every power-of-two pulse pair inside those caps, and replays every divisor hit physically.

Frozen totals:

| family | fixed packets | positive-denominator pulse pairs | eliminant identities | hits |
|---|---:|---:|---:|---:|
| `P3` | 30 | 609 | 1,218 | 1 trivial |
| `P11` | 21 | 289 | 578 | 0 |

The only hit is

\[
(1,2)^2\longmapsto(2,2)^2,
\qquad n=1.
\]

This completes the exclusion. ∎

## Relationship to the counterexample objective

This is a genuine exhaustive negative result for a strict infinite construction class:

```text
known negative baseline
+ arbitrary repetition
+ arbitrary rotation
+ arbitrary two distinct pulse positions
+ arbitrary positive pulse heights
```

The negative conclusion is genuinely weaker than the Collatz conjecture because positive cycles may lie outside this class. It does not merely increase a bounded search range; it closes every repetition and pulse height in the stated class.

Together with `L-8201` and `T-8202`, the negative-cycle pulse frontier is now:

```text
one pulse over all repetitions:
  source-conditionally closed;

two pulses over all repetitions:
  source-conditionally closed by T-8255;

arbitrary support at one fixed repeated word:
  finite by L-8201;

growing support with growing repetition:
  still open.
```

A future positive-cycle construction in this neighborhood must use at least three pulse positions whose support grows with the baseline architecture, change primitive block type, or leave coordinatewise upward pulsing of the two known negative cycles.

## Dependency audit

1. The two-pulse numerator reduction is proved in Sections 1–2 and independently replayed in `X-8255`; PR #51 `L-8001` is a consistency source.
2. The only external theorem is the exact Matveev lower bound already used by `T-8202`. The present substitution changes the exponential decay rate from `A log 2` to `A log 2-(k/2)log 3`.
3. Continued-fraction generation, cutoff margins, Legendre thresholds, primitive-row inequalities, the exceptional row, and all small cases are independently implemented twice.
4. Exact physical replay is performed for the sole divisor hit.

## Gap audit

- The theorem remains `PROPOSED / SOURCE-DEPENDENT` until the primary Matveev statement and both substitutions are independently reconstructed.
- The result covers exactly two distinct pulse locations. Three or more pulse positions are outside its scope.
- It covers only repetitions of the two known ordinary negative cycles, not a hypothetical undiscovered negative-cycle baseline.
- It does not eliminate mixed macro-block words or non-pulse valuation architectures.
- It proves no divergent-orbit statement and constructs no counterexample.
- The finite audit closes only the explicitly bounded non-Legendre range; the all-repetition conclusion comes from the analytic reduction.

## Adversarial tests

`X-8255` performs all of the following with exact arithmetic:

1. reconstructs both negative cycles, every primitive rotation, and every small repeated orbit;
2. checks the chain coefficients, their signs, and `a=b+c`;
3. checks both Sylvester/Bézout eliminants and their divisibility equivalence;
4. certifies the Matveev cutoff inequalities and positive derivatives;
5. certifies the Legendre thresholds and decreasing ratios;
6. certifies 38 continued-fraction rows;
7. rejects 17 ordinary upper-convergent families by `(28)` and the `1/5` family by `(30)`;
8. exhausts 898 positive-denominator small pulse pairs;
9. reconstructs and physically replays the unique trivial hit;
10. compares two standard-library implementations sharing no imported derivation module.

Frozen output:

```text
continued-fraction rows:             38
primitive upper families rejected:   18
nontrivial hits:                       0
trivial hits:                          1
master transcript:
b60b6c1e4564ac52a52749af8e19f854fb0f3de0c0a6269037e3f452b91278a8
```

## Remaining uncertainty

The native reduction and exact certificates have no known unresolved arithmetic step. The concentrated uncertainty is the precise primary-source Matveev formulation, inherited from `T-8202`, and independent review of the source constant and normalization.

## Suggested next attack

Do not return to larger two-pulse scans. The next exact negative-cycle target is:

```text
at least three pulse positions
+ support size allowed to grow with repetition
+ a multivariate resultant or mixed-height theorem uniform in support.
```

The direct ordinary-extraction target remains separate: decide one canonical least-root sequence rather than prescribe another infinite completion.
