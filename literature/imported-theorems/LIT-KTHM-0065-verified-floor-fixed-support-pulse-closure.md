# LIT-KTHM-0065 — Verified-floor closure of every fixed pulse support below the density threshold

**Status:** `PROPOSED / SOURCE-QUALIFIED AT THE VERIFIED FLOOR / SOURCE-AUDITED AT THE MATVEEV STEP / EXACT CERTIFICATE`  
**Native dependencies:** PR #53 `L-8201` fixed-cone pulse resultants and the distributed-pulse identity reconstructed in PR #70  
**External dependencies:** Barina 2025 verification below `2^71`; Ansari 2025 recursive-sufficiency extension as used in PR #76 `T-6701`; `LIT-KTHM-0060` (Matveev 2000, Corollary 2.3)  
**Scope:** arbitrary repetitions, rotations, distinct pulse positions, and positive pulse heights over the two known ordinary negative accelerated cycles  
**Counterexample status:** no nontrivial positive cycle is produced

## Theorem

Let

\[
P_3=(1,2),
\qquad (A,k,c_*)=(3,2,7),
\]

and

\[
P_{11}=(1,1,1,2,1,1,4),
\qquad (A,k,c_*)=(11,7,91).
\]

Repeat one primitive word `r>=1` times, rotate arbitrarily, choose exactly `s`
distinct positions, and increase the valuations at those positions by arbitrary
positive integers.

Then:

\[
\boxed{
P_3:\quad 1\le s\le18
\Longrightarrow
\text{no nontrivial positive Collatz cycle};
}
\]

\[
\boxed{
P_{11}:\quad 1\le s\le117
\Longrightarrow
\text{no positive Collatz cycle}.
}
\]

For `P3` the only positive-cycle hits are the trivial representations

\[
(1,2)^s\longmapsto(2)^{2s},
\qquad n=1,
\]

obtained at repetition `r=s` by adding one at every valuation-one position.
For `P11` even this trivial lift is impossible because the primitive word
contains a valuation `4`, which upward pulses cannot reduce to `2`.

The bounds `18` and `117` are the exact positive-rate limits of this proof:

\[
2^{3\cdot18}>3^{2\cdot17},
\qquad
2^{3\cdot19}<3^{2\cdot18},
\]

and

\[
2^{11\cdot117}>3^{7\cdot116},
\qquad
2^{11\cdot118}<3^{7\cdot117}.
\]

Thus supports `19` and `118` are the first layers not covered by the
largest-gap exponential-decay mechanism.

## 1. General fixed-support pulse inequality

Put

\[
N=kr.
\]

After rotating immediately after a largest cyclic support gap, write

\[
0=p_1<p_2<\cdots<p_s<N.
\]

The largest gap has length at least `ceil(N/s)`, so

\[
\boxed{
p_s\le
N-\left\lceil\frac Ns\right\rceil
=
\left\lfloor\frac{s-1}{s}kr\right\rfloor.
}
\tag{1}
\]

Let the pulse heights be `d_i>=1`, put

\[
X_i=2^{d_i},
\qquad
t=d_1+\cdots+d_s,
\]

and let

\[
D=2^{Ar+t}-3^{kr}.
\]

The distributed-pulse identity, after removing the exterior factor coprime to
`D`, gives one positive reduced correction `R` satisfying

\[
D\mid R
\tag{2}
\]

for every integral pulsed cycle and

\[
0<R<c_*\,3^{p_s}2^t.
\tag{3}
\]

If the cycle is positive then `D>0`, so `(2)--(3)` imply

\[
D\le R.
\]

Define

\[
\Lambda=(Ar+t)\log2-kr\log3>0.
\]

Dividing by `2^(Ar+t)` gives

\[
\boxed{
0<1-e^{-\Lambda}
<
c_*\frac{
3^{\lfloor (s-1)kr/s\rfloor}
}{
2^{Ar}
}.
}
\tag{4}
\]

This is the only point where the pulse-position geometry enters.

## 2. A second approximation from the verified cycle floor

Use the branch-qualified verified range from PR #76:

\[
N_*=4\cdot3^{44}+2
=
3\,939\,083\,608\,734\,444\,931\,526.
\]

Every odd state in a nontrivial positive cycle is greater than `N_*`.
Multiplying the accelerated equations

\[
2^{a_j}x_{j+1}=3x_j+1
\]

around the cycle yields

\[
e^\Lambda
=
\prod_{j=0}^{kr-1}
\left(1+\frac1{3x_j}\right).
\]

Therefore

\[
\boxed{
0<\Lambda
<
\frac{kr}{3N_*}.
}
\tag{5}
\]

Put

\[
\eta=\log_2\frac{3^k}{2^A}.
\]

Since

\[
\frac tr-\eta=\frac{\Lambda}{r\log2},
\]

equation `(5)` gives

\[
0<\frac tr-\eta
<
\frac{k}{3N_*\log2}
<
\frac{k}{2N_*},
\tag{6}
\]

using `log 2>2/3`.

For every `r<=10^6`,

\[
kr^2<N_*,
\]

so `(6)` implies

\[
0<\frac tr-\eta<\frac1{2r^2}.
\tag{7}
\]

## 3. Pulse decay supplies Legendre for every larger repetition

For `r>=10^6`, use `(4)` at the largest admitted support. The exact certificate
proves

\[
6c_*r\,
3^{\lfloor(s_{\max}-1)kr/s_{\max}\rfloor}
<
2^{Ar}
\tag{8}
\]

for every `r>=10^6`, with

\[
s_{\max}=18\quad(P_3),
\qquad
s_{\max}=117\quad(P_{11}).
\]

The proof checks one base value in each residue class modulo `s_max`; over one
complete residue period the left/right ratio is multiplied by

\[
\frac{r+s_{\max}}r
\frac{3^{(s_{\max}-1)k}}{2^{As_{\max}}}
<1.
\]

Since the exponent in `(8)` is nondecreasing in `s`, the same inequality holds
for every smaller support.

Inequality `(8)` makes the right side of `(4)` smaller than `1/(6r)`, hence
smaller than `1/2`. Thus

\[
\Lambda<2c_*
\frac{
3^{\lfloor(s-1)kr/s\rfloor}
}{
2^{Ar}
}.
\]

After division by `r log 2`, `(8)` gives again

\[
0<\frac tr-\eta<\frac1{2r^2}.
\tag{9}
\]

Combining Sections 2 and 3:

\[
\boxed{
\text{for every repetition }r,
\text{ the reduced fraction }t/r=p/q
\text{ is an upper convergent of }\eta.
}
\tag{10}
\]

## 4. Matveev gives a finite convergent list

For fixed support `s`, put

\[
\beta_s=
A\log2-\frac{s-1}{s}k\log3.
\]

At the maximal supports,

\[
\beta_{18}>0
\quad(P_3),
\qquad
\beta_{117}>0
\quad(P_{11}).
\]

Equation `(4)` gives, once its right side is below `1/2`,

\[
\Lambda
<
2c_*e^{-\beta_s r}.
\tag{11}
\]

The source-audited specialization of Matveev 2000 gives

\[
\log\Lambda
>
-748000000\log2\log3
\left(1+\log(kr+1)\right).
\tag{12}
\]

The weighted coefficient parameter is below `kr+1` because
`\Lambda<log3`.

Exact rational logarithm intervals certify that `(11)--(12)` are incompatible
for

```text
P3, every s<=18:
    r >= 5,000,000,000,000;

P11, every s<=117:
    r >= 400,000,000,000,000.
```

The certificate records a positive margin and positive derivative at each
cutoff. Hence every candidate upper convergent has denominator below the
corresponding cutoff.

## 5. Two complementary ways to reject a convergent family

Let `p/q` be one of the finitely many upper convergents and write

\[
(r,t)=m(q,p).
\]

Put

\[
\lambda_0
=
(Aq+p)\log2-kq\log3>0,
\]

so

\[
\Lambda=m\lambda_0.
\]

### 5.1 Verified-floor rejection

Equation `(5)` implies

\[
m\lambda_0
<
\frac{k\,mq}{3N_*}.
\]

After cancelling `m`, every candidate must satisfy

\[
\boxed{
\lambda_0<\frac{kq}{3N_*}.
}
\tag{13}
\]

Thus the exact opposite inequality excludes every multiple of the convergent,
independently of support positions and pulse heights.

### 5.2 Pulse-comparison rejection

Let `q_+` be the next convergent denominator. The complete-quotient identity
gives

\[
\lambda_0
>
\frac{\log2}{q+q_+}
>
\frac1{2(q+q_+)}.
\tag{14}
\]

At the maximal support, if

\[
\boxed{
2^{Aq}
>
4c_*
3^{\lfloor(s_{\max}-1)kq/s_{\max}\rfloor}
(q+q_+)
}
\tag{15}
\]

and

\[
2^{Aq}>
3^{\lceil(s_{\max}-1)kq/s_{\max}\rceil},
\tag{16}
\]

then the upper bound in `(11)` decreases with `m`, and its value at `m=1`
is already below the lower bound `(14)`. Hence every positive multiple is
excluded. Again, validity at the maximal support implies validity at every
smaller support.

## 6. Complete exact convergent coverage

`LIT-X-0065` resolves the continued fractions using rational intervals and
checks every upper convergent below the Matveev cutoffs.

For `P3`, there are twelve relevant upper convergents:

```text
1/5, 8/47, 26/153:
    rejected by the verified-floor inequality;

1269/7468 through 559632586/3293409335:
    rejected by both methods;

11684726649/68764022656,
395601808308/2328096542299:
    rejected by pulse comparison.
```

Coverage totals:

```text
verified-floor only:  3
pulse-comparison only: 2
both:                  7
total:                12
```

For `P11`, there are eleven:

```text
1/10, 2/21, 1496/15791, 18051/190537:
    rejected by the verified-floor inequality;

145913/1540182, 5380730/56796197:
    rejected by both methods;

1861294841/19646863616
through
18925801838545/199770954797019:
    rejected by pulse comparison.
```

Coverage totals:

```text
verified-floor only:  4
pulse-comparison only: 5
both:                  2
total:                11
```

Every possible nontrivial positive cycle lies in one of these convergent
families, and every family is excluded. This proves the theorem. ∎

## Exact replay

```bash
python3 literature/experiments/LIT-X-0065-verified-floor-fixed-support/run.py \
  --check-results \
  literature/experiments/LIT-X-0065-verified-floor-fixed-support/results/canonical.json

python3 literature/experiments/LIT-X-0065-verified-floor-fixed-support/verify.py \
  literature/experiments/LIT-X-0065-verified-floor-fixed-support/results/canonical.json
```

The generator and verifier share no author module.

Frozen semantic digest:

```text
7844793b1bf9e1f4f2fe4c20792d4bc408d0e1e4c1ba196917d1a5d7f919b20f
```

## Why this gains ground

This is not another finite pulse-height scan. It combines four independent
resources:

```text
fixed-support largest-gap decay;
the ordinary verified cycle floor;
Matveev's effective real logarithmic bound;
complete continued-fraction and resultant reduction.
```

The verified floor handles precisely the short convergents where the
largest-gap comparison is weakest. The pulse comparison handles the late,
exceptionally accurate convergents where the verified-floor estimate is too
weak.

Together they close every fixed support for which the largest-gap decay rate
is positive.

## Applicability audit

- The Barina/Ansari floor is imported branch-qualifiably and is not rerun here.
- The Matveev normalization is fully source-audited in `LIT-KTHM-0060`.
- The pulse correction and exact divisor equivalence remain native proposed
  dependencies requiring independent mathematical reconstruction.
- The exact certificate independently reconstructs all inequalities and
  continued-fraction rows after those interfaces.
- The theorem treats upward pulses over only the two stated negative cycles.
- It does not cover support growing beyond `18` or `117`, mixed baselines,
  arbitrary valuation words, or divergent nonperiodic orbits.

## Exact next frontier

The first uncovered layers are

```text
P3:  support 19;
P11: support 118.
```

At those supports

\[
A\log2-\frac{s-1}{s}k\log3<0,
\]

so largest-gap decay no longer bounds the repetition. A further extension
must exploit a new source of cancellation or prime divisibility, such as:

```text
a denominator/resultant fresh-prime incompatibility;
a multi-gap rather than largest-gap estimate;
a full-support density theorem;
or a mixed-baseline normal form.
```