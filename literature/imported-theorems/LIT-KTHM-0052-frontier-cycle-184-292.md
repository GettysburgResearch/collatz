# LIT-KTHM-0052 — No positive accelerated Collatz cycle has odd length `184`

**Type:** exact native arithmetic theorem with a finite decoder, stability proof, and replay artifact.  
**Maps to:** issue #9, issue #41, `SYN/L-9904`, and the first accelerated length capable of escaping the published `91`-local-minimum exclusion.  
**External input:** Hercher's theorem that a nontrivial positive Collatz cycle has at least `92` local minima.

## 1. Why length `184` is the first local-minimum frontier

Let

```text
S(x)=(3x+1)/2^a,
a=v_2(3x+1),
```

be the odd accelerated Collatz map on a positive odd state `x>1`. Then

```text
a=1   -> S(x)>x,
a>=2  -> S(x)<x.                                         (1)
```

Indeed, `(3x+1)/2>x`, while `(3x+1)/4<x` for `x>1`.

Along a cyclic sequence, local minima and local maxima alternate. Hence an accelerated word of odd-state length `k` has at most `floor(k/2)` local minima. Hercher excludes every nontrivial positive cycle with at most `91` local minima, so

```text
k>=184                                                   (2)
```

is necessary before an accelerated word can even accommodate the first unexcluded count of `92` local minima.

At `k=184`, any hypothetical nontrivial cycle must therefore have **exactly** `92` local minima. Equality in the alternating-minima bound forces the ascent/descent pattern to alternate. After a cyclic rotation, its valuation word has the form

```text
w=(1,b_0,1,b_1,...,1,b_91),
b_i>=2.                                                  (3)
```

Thus the family below contains every possible positive accelerated cycle of odd length `184`.

## 2. Total valuation and excess mass

Put

```text
A=sum_i(1+b_i),
H=A-276,
c_i=b_i-2.                                              (4)
```

Then

```text
c_i>=0,
sum_i c_i=H.                                            (5)
```

A positive cycle requires

```text
D_H=2^A-3^184>0.                                        (6)
```

The exact comparison

```text
2^291<3^184<2^292                                       (7)
```

shows that `(6)` forces

```text
A>=292,
H>=16.                                                   (8)
```

## 3. Ninety-two two-step blocks

The pair of accelerated valuations `(1,2+c_i)` acts by

```text
boxed:
2^[3+c_i]x_(i+1)=9x_i+5.                                (9)
```

Let

```text
u_j=sum_(i<j)c_i,
E_j=3j+u_j,
0<=j<=92.                                               (10)
```

Composing the `92` blocks gives

```text
2^[276+H]x_92=9^92x_0+5S_H(c),                          (11)
```

where

```text
S_H(c)=sum_(j=0)^91 9^(91-j)2^(E_j).                    (12)
```

Since `9^92=3^184`, a cycle requires

```text
D_H divides 5S_H(c),
D_H=2^[276+H]-9^92.                                     (13)
```

Only this necessary divisibility condition is used below. No converse or intermediate-valuation assumption is needed for the exclusion.

## 4. Telescoping to `H` ordered unit jumps

Define

```text
Q_j=9^(92-j)8^j,
0<=j<=92.                                               (14)
```

Then

```text
Q_j-Q_(j+1)=9^(91-j)8^j.                                (15)
```

Using `u_0=0` and `u_92=H`, summation by parts gives

```text
S_H(c)=J_H(c)-D_H,                                      (16)
```

where

```text
J_H(c)=sum_(j=1)^92 (2^[u_j]-2^[u_(j-1)])Q_j.           (17)
```

Resolve each jump `u_j-u_(j-1)=c_(j-1)` into unit increments. There are unique nondecreasing positions

```text
1<=j_0<=j_1<=...<=j_(H-1)<=92                           (18)
```

such that

```text
boxed:
J_H(c)=sum_(r=0)^(H-1)2^rQ_(j_r).                       (19)
```

Conversely, every sequence `(18)` determines one weak composition `(5)`.

Put

```text
g_H=gcd(D_H,5),
D'_H=D_H/g_H.                                           (20)
```

Modulo `5`, one has

```text
D_H congruent to 2^H-1 mod5,                            (21)
```

because `8^92 congruent to 9^92 congruent to1 mod5`. Hence

```text
g_H=5  iff H congruent to0 mod4,
g_H=1  otherwise.                                      (22)
```

Equations `(13)` and `(16)` imply

```text
boxed:
D'_H divides J_H(c).                                    (23)
```

Therefore there is a positive integer multiplier `m` satisfying

```text
boxed:
sum_(r=0)^(H-1)2^rQ_(j_r)=mD'_H.                       (24)
```

## 5. Uniform finite multiplier bounds

The sequence `Q_j` is strictly decreasing. Therefore

```text
(2^H-1)Q_92<=J_H(c)<=(2^H-1)Q_1.                       (25)
```

For fixed `g in {1,5}`, the upper ratio

```text
g(2^H-1)Q_1/(2^H Q_92-Q_0)                             (26)
```

strictly decreases with `H`, because `Q_0>Q_92`.

The first positive-denominator height in the `g=5` class is `H=16`; the first in the `g=1` class is `H=17`. Exact evaluation gives the universal bounds

```text
g_H=5 -> 1<=m<=1005828,
g_H=1 -> 1<=m<=73778.                                   (27)
```

The sharper lower endpoints are used in the small exact scans, but are not needed for the uniform theorem.

## 6. The valuation decoder

Fix `H`, `m`, and suppose `(24)` holds. After removing the first `r` jump terms, put

```text
R_r=sum_(s=r)^(H-1)2^sQ_(j_s).                          (28)
```

The `s`th term has exact binary valuation

```text
v_2(2^sQ_(j_s))=s+3j_s.                                 (29)
```

Since the positions are nondecreasing, every term with `s>r` has valuation strictly larger than `r+3j_r`. Hence the first remaining term is the unique term of least valuation and

```text
boxed:
j_r=(v_2(R_r)-r)/3.                                    (30)
```

Thus a fixed multiplier `m` has at most one candidate jump sequence. Starting with

```text
R_0=mD'_H,                                               (31)
```

the exact decoder repeatedly:

1. computes `v_2(R_r)`;
2. requires `(v_2(R_r)-r)/3` to be an integer in `[1,92]`;
3. requires the positions to remain nondecreasing;
4. subtracts `2^rQ_(j_r)`; and
5. after `H` steps, requires zero remainder.

Failure of any check proves that multiplier impossible.

## 7. Direct scans at `H=16,...,20`

The proof artifact

```text
literature/experiments/LIT-X-0052-frontier-cycle/run.py
```

performs exact standard-library scans at the first five heights. It finds no solution:

```text
H  A    multiplier interval      eligible decodes  maximum depth  solutions
16 292  23 ... 1,005,828              71,843            16          0
17 293   2 ...    73,778               5,269            15          0
18 294   2 ...    56,036               4,003            15          0
19 295   2 ...    50,021               3,573            15          0
20 296   6 ...   237,369              16,955            17          0
```

At `H=16`, the denominator factors completely and squarefreely as

```text
2^292-3^184 =
5 * 11 * 13 * 17 * 83 * 89 * 179 * 1097 * 1301
  * 2963 * 4547 * 5113 * 13457 * 28697 * 1626211
  * 192491569 * 177790780231 * 314328249709
  * 167385996821689.                                    (32)
```

Every displayed factor is prime, and the largest has `48` bits. The exact factorization is independently checked by deterministic Miller--Rabin tests valid below `2^64` and by multiplication.

## 8. Stability for every larger height

The remaining infinitely many values of `H` split into the two gcd classes in `(22)`.

### 8.1 The `g_H=1` class

Use the reference height

```text
H_*=501.                                                 (33)
```

The decoder scans every eligible `m<=73778`. All `5,269` eligible multipliers fail a valuation-modulo-`3` check after at most `15` decoded positions. Across the full reference scan, every inspected remainder has

```text
v_2(R_r)<=31.                                           (34)
```

For any other `H>=21` with `g_H=1`,

```text
D'_H-D'_(501)=(2^H-2^501)Q_92.                          (35)
```

Every multiplier surviving the initial decoder filter has `v_2(m)>=3`. Therefore

```text
v_2(m(D'_H-D'_(501)))
 >=21+276+3
 =300.                                                   (36)
```

As long as the same jump terms are subtracted, the two decoder remainders differ by a multiple of `2^300`. Since the reference valuation never exceeds `31`, both decoders have the same valuation, choose the same jump position, and preserve the same difference. Induction carries the reference failure to every such `H`.

### 8.2 The `g_H=5` class

Use the reference height

```text
H_*=500.                                                 (37)
```

The decoder scans every eligible `m<=1005828`. All `71,844` eligible multipliers fail a valuation-modulo-`3` check after at most `20` decoded positions. Every inspected remainder has

```text
v_2(R_r)<=42.                                           (38)
```

For any other `H>=24` divisible by `4`,

```text
D'_H-D'_(500)=(2^H-2^500)Q_92/5.                        (39)
```

Again `v_2(m)>=3`, so

```text
v_2(m(D'_H-D'_(500)))
 >=24+276+3
 =303.                                                   (40)
```

The same induction, now using `42<303`, transfers the reference failure to every height in this class.

The direct scans at `H=16,...,20` and the two stability classes cover every `H>=16`.

## 9. Exact replay

Run

```bash
python3 literature/experiments/LIT-X-0052-frontier-cycle/run.py \
  --check-results \
  literature/experiments/LIT-X-0052-frontier-cycle/results/canonical.json
```

The two stable-class transcript digests are

```text
g_H=1:
e7b965827614c319335e925782b8533690e3ba3827ba6a47674e4de44edc9702

g_H=5:
b7ddde20ce910d6597d64bb3f7238a67ecab3f279f5583eef1ec5e2c9c8c687e.
```

The `H=16` transcript digest is

```text
c8449fe7c2d15679df8bb4d68ecd376c68b2995ef033e87fd2063447f5cde58d.
```

The canonical JSON records all five direct scans, both reference scans, the valuation margins, and the factorization check.

## 10. Theorem

```text
boxed:
There is no nontrivial positive accelerated Collatz cycle
with odd-state length k=184.                             (41)
```

### Proof

A hypothetical length-`184` cycle has at least `92` local minima by Hercher and at most `92` by alternation. Hence it has the form `(3)`. Positivity of its cycle denominator forces `H>=16`. Its necessary divisibility condition gives `(24)`. The direct and stability decoder arguments exclude `(24)` for every `H>=16`. Contradiction. QED.

## 11. Scope and literature boundary

This theorem is an exact project-level cycle exclusion and a reusable decoder for alternating-minimum families. Stronger lower bounds for other cycle parameters may already imply larger global exclusions; no novelty claim is made here without a separate full literature comparison.

The theorem does not exclude accelerated lengths `k>=185`, divergent orbits, or the Collatz conjecture.