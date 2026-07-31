# LIT-KTHM-0064 — All-repetition four-pulse exclusion over both native negative cycles

**Status:** `PROPOSED / SOURCE-AUDITED AT THE MATVEEV STEP / EXACT CERTIFICATE`  
**Native dependencies:** the standard accelerated-cycle numerator identity; PR #53 `L-8201`/PR #70 distributed-pulse normalization  
**External dependency:** `LIT-KTHM-0060`, specializing Matveev 2000, Corollary 2.3  
**Scope:** exactly four distinct upward valuation pulses of arbitrary positive heights over every repetition and rotation of

\[
P_3=(1,2),
\qquad
P_{11}=(1,1,1,2,1,1,4).
\]

**Counterexample status:** no nontrivial positive cycle is produced; one trivial lift to the cycle `1` is retained explicitly

## Theorem

Repeat either baseline an arbitrary positive number `r` of times, rotate it arbitrarily, choose exactly four distinct positions, and increase the four valuations by arbitrary positive integers.

Then the resulting accelerated valuation word is not the word of a nontrivial positive Collatz cycle.

For `P_3`, the sole positive-cycle hit is the trivial lift

\[
(1,2)^4\longmapsto(2,2,2,2,2,2,2,2),
\qquad n=1,
\]

obtained by adding one at each of the four valuation-one positions. For `P_{11}`, there is no positive-cycle hit.

## 1. Exact pulse identity

Let the repeated baseline have odd-state length `K=kr`, total valuation `Ar`, negative cycle states `z_j<0`, and largest absolute state at most `c_*`. After rotating immediately after a largest cyclic support gap, write

\[
0=p_1<p_2<p_3<p_4<K.
\]

The largest-gap choice gives

\[
\boxed{p_4\le\left\lfloor\frac{3kr}{4}\right\rfloor.}
\tag{1}
\]

Let the pulse heights be `d_i>=1`, put `X_i=2^{d_i}`, `P_i=X_1\cdots X_i`, and `t=d_1+\cdots+d_4`. Expanding the accelerated numerator and grouping the four prefix changes gives

\[
C_{\rm pulsed}-z_0D
=\sum_{i=1}^{4}W_i(X_i-1)P_{i-1},
\tag{2}
\]

where

\[
D=2^{Ar+t}-3^{kr},
\qquad
W_i=(-z_{p_i+1})3^{K-1-p_i}2^{A_{p_i+1}}.
\]

The ordinary segment identity between consecutive negative states gives

\[
W_1>W_2>W_3>W_4>0.
\]

Consequently, with `R` denoting the right-hand side of `(2)`,

\[
0<R<W_1\,2^t
\le c_*3^{\lfloor3kr/4\rfloor}2^t.
\tag{3}
\]

If a positive cycle exists, `D>0` and `D|R`. Put

\[
\Lambda=(Ar+t)\log2-kr\log3>0.
\]

Dividing `D<R` by `2^{Ar+t}` yields the universal four-pulse inequality

\[
\boxed{
0<1-e^{-\Lambda}
<c_*\frac{3^{\lfloor3kr/4\rfloor}}{2^{Ar}}.}
\tag{4}
\]

## 2. Small repetitions: a nontrivial positive-cycle product gate

For a nontrivial positive accelerated cycle all odd states satisfy `x_j>=3`. Multiplying

\[
2^{a_j}x_{j+1}=3x_j+1
\]

around the cycle gives

\[
2^{Ar+t}
=3^{kr}\prod_{j=0}^{kr-1}\left(1+\frac1{3x_j}\right)
\le3^{kr}\left(\frac{10}{9}\right)^{kr}.
\]

Since `t>=4`, a necessary condition is

\[
3^{kr}2^{Ar+4}\le10^{kr}.
\tag{5}
\]

Exact integer margins show that `(5)` fails for

```text
P3:  r=2,...,8;
P11: r=1,2,3.
```

This excludes every nontrivial cycle in those ranges. The `P3,r=4` all-two word is replayed separately and gives `n=1`.

## 3. Transition ranges

For `t>=4`, inequality `(4)` contradicts the exact lower bound from `t=4` whenever

\[
2^{Ar+4}-3^{kr}
\ge16c_*3^{\lfloor3kr/4\rfloor}.
\tag{6}
\]

The exact margins are positive for

```text
P3:  r=9,...,14;
P11: r=4.
```

Thus only `r>=15` for `P3` and `r>=5` for `P11` remain.

## 4. Legendre reduction

Once the right side of `(4)` is below `1/2`, one has

\[
0<\Lambda
<2c_*\frac{3^{\lfloor3kr/4\rfloor}}{2^{Ar}}.
\]

As `\log2>2/3`, the sufficient exact condition

\[
2^{Ar}>6c_*r3^{\lfloor3kr/4\rfloor}
\tag{7}
\]

implies

\[
0<\frac tr-\eta<\frac1{2r^2},
\qquad
\eta=\log_2\frac{3^k}{2^A}.
\tag{8}
\]

Hence the reduced fraction `t/r=p/q` is an upper continued-fraction convergent of `eta`.

The artifact proves `(7)` cofinally by residue classes:

```text
P3:  r>=15, period 2;
P11: r>=5,  period 4.
```

The exact period ratios are respectively

\[
\frac{459}{960}<1,
\qquad
\frac{94143178827}{87960930222080}<1.
\]

## 5. Matveev cutoffs

From `(4)` and `1-e^{-\Lambda}>\Lambda/2` for `0<\Lambda<1`,

\[
\Lambda
<2c_*\exp\left[-r\left(A\log2-\frac{3k}{4}\log3\right)\right].
\tag{9}
\]

The exponential rates are positive for both baselines. `LIT-KTHM-0060` gives

\[
\log\Lambda
>-748000000\log2\log3\,
\bigl(1+\log(kr+1)\bigr).
\tag{10}
\]

Exact rational log intervals prove that `(9)` and `(10)` are incompatible for

```text
P3:  r>=35,000,000,000;
P11: r>= 8,000,000,000.
```

The artifact records positive cutoff and derivative margins, so the contradiction persists beyond each cutoff.

## 6. Continued fractions below the cutoffs

Let `p/q` be an upper convergent and `q_+` the next convergent denominator. Every positive multiple `(r,t)=m(q,p)` is excluded if

\[
2^{Aq}
>4c_*3^{\lfloor3kq/4\rfloor}(q+q_+).
\tag{11}
\]

The exact continued-fraction transcript and every logarithmic margin are reconstructed independently.

For `P_{11}`, `(11)` holds for every upper convergent below the cutoff:

\[
\frac1{10},
\frac2{21},
\frac{1496}{15791},
\frac{18051}{190537},
\frac{145913}{1540182},
\frac{5380730}{56796197}.
\]

For `P_3`, it holds for every upper convergent below the cutoff except `1/5`. The ordinary rows begin

\[
\frac8{47},
\frac{26}{153},
\frac{1269}{7468},
\ldots,
\frac{559632586}{3293409335}.
\]

## 7. Exact exceptional `1/5` family

For `P_3`, the exceptional convergent has

\[
(r,t)=m(5,1).
\]

Four distinct positive pulses force `m=t>=4`. At `m=4`, exact arithmetic gives

\[
1-\left(\frac{59049}{65536}\right)^m
-7\frac{3^{\lfloor15m/2\rfloor}}{8^{5m}}
=
\frac{6266018807858022127}{18446744073709551616}>0.
\]

The right-hand term decreases by at most

\[
\frac{3^8}{8^5}=rac{6561}{32768}<1
\]

per increment of `m`, while the left-hand term increases. Thus every `m>=4` is excluded.

The ranges in Sections 2–7 are exhaustive, proving the theorem.

## Exact replay

```bash
python3 literature/experiments/LIT-X-0064-four-pulse-all-repetition/run.py \
  --check-results \
  literature/experiments/LIT-X-0064-four-pulse-all-repetition/results/canonical.json

python3 literature/experiments/LIT-X-0064-four-pulse-all-repetition/verify.py \
  literature/experiments/LIT-X-0064-four-pulse-all-repetition/results/canonical.json
```

The generator and verifier share no module. The frozen semantic digest is

```text
5efdd640ef15d261a263c923028397077d8166a01984ed365c4b859fac665b8c
```

## Applicability and dependency audit

- The Matveev source normalization is fully audited by `LIT-KTHM-0060`.
- The pulse numerator identity is elementary but should still receive an independent native reconstruction before status promotion.
- The proof permits arbitrary rotations, support positions, and positive pulse heights.
- The only use of positivity of a hypothetical cycle before the divisibility argument is the product bound in Section 2.
- The trivial cycle is not silently counted as a counterexample.

## Gap audit

- This excludes exactly four support positions, not support five or growing support.
- It treats upward pulses over only the two stated negative baselines.
- No statement about a general positive cycle follows.
- No divergent ordinary orbit or `K-####` candidate is produced.

## Next target

The same proof skeleton can be parameterized by support size `s`. The immediate next job is not a cap-box search: test the product/transition/Legendre/convergent inequalities at `s=5`, retaining exceptional convergents as explicit multiplier families. The full finite-decision envelope of `LIT-KTHM-0061` remains `s<=18` and `s<=117`, but exclusion is now complete through support four.
