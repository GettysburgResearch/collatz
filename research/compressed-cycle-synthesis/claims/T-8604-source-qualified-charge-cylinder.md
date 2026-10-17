# T-8604 — Source-qualified charge cylinder forces a 72-billion-state cycle floor

**Claim ID:** `T-8604`  
**Title:** The verified range below \(2^{71}\) forces enormous odd length and non-neutral support  
**Status:** `PROPOSED / SOURCE-QUALIFIED EXACT CERTIFICATE`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-23  
**Dependencies:** `L-8605`; `X-8612`; the branch-qualified external premise used by `PR12/L-9111` that every positive integer below \(2^{71}\) reaches the shortcut cycle \(\{1,2\}\)  
**Scope:** positive cycles of the accelerated odd Collatz map  
**Related counterexample candidates:** none

## 1. Statement

Assume the external verified-range premise

\[
\boxed{
1\le n<2^{71}
\quad\Longrightarrow\quad
n\text{ reaches the shortcut cycle }\{1,2\}.
}
\tag{H71}
\]

Then every nontrivial positive accelerated Collatz cycle has at least

\[
\boxed{
K_*=72,057,431,991
}
\tag{1}
\]

odd states.

If \(A\) is the total valuation and

\[
\chi=2k-A
\]

is the signed defect charge, then every such cycle also satisfies

\[
\boxed{
\chi\ge
C_*=29,906,536,378.
}
\tag{2}
\]

Consequently its number \(s\) of valuations different from \(2\) satisfies

\[
\boxed{
s\ge29,906,536,378.
}
\tag{3}
\]

The theorem is conditional only on `(H71)`. The Farey interval and all native
arithmetic are certified by `X-8612`.

## 2. Minimum-state input

Let

\[
n_0,\ldots,n_{k-1}
\]

be a nontrivial positive accelerated cycle and let

\[
m=\min_i n_i.
\]

Under `(H71)`, \(m\) cannot be below \(2^{71}\). Since every accelerated state
is odd and \(2^{71}\) is even,

\[
\boxed{
m\ge X:=2^{71}+1.
}
\tag{4}
\]

## 3. Exact charge cylinder

Multiplying the accelerated equations gives

\[
\frac{2^A}{3^k}
=
\prod_{i=0}^{k-1}
\left(1+\frac1{3n_i}\right).
\tag{5}
\]

Because \(n_i\ge X\),

\[
\frac{2^A}{3^k}
\le
\left(1+\frac1{3X}\right)^k.
\tag{6}
\]

Put

\[
\alpha=\log_2\frac43,
\qquad
\beta_X=\log_2\frac{4X}{3X+1}.
\tag{7}
\]

Since \(\chi=2k-A\), inequality `(6)` gives

\[
2^\chi
=
\frac{4^k}{2^A}
\ge
\left(\frac{4X}{3X+1}\right)^k,
\]

hence

\[
\boxed{
\frac{\chi}{k}\ge\beta_X.
}
\tag{8}
\]

The product in `(5)` is greater than one, so \(2^A>3^k\). Therefore

\[
\boxed{
\frac{\chi}{k}<\alpha.
}
\tag{9}
\]

Every cycle charge ratio lies in the extremely narrow one-sided cylinder

\[
\boxed{
\beta_X
\le
\frac{\chi}{k}
<
\alpha.
}
\tag{10}
\]

Its width is

\[
\alpha-\beta_X
=
\log_2\left(1+\frac1{3X}\right)
=
2.03668\ldots\times10^{-22}.
\tag{11}
\]

The decimal is explanatory only; the proof uses exact rational logarithm
bounds.

## 4. Farey-neighbor certificate

Put

\[
L=
\frac{2,733,776,749}{6,586,818,670},
\qquad
U=
\frac{27,172,759,629}{65,470,613,321}.
\tag{12}
\]

Their determinant is exactly

\[
27,172,759,629\cdot6,586,818,670
-
2,733,776,749\cdot65,470,613,321
=
\boxed{1}.
\tag{13}
\]

Their mediant is

\[
M=
\frac{29,906,536,378}{72,057,431,991}.
\tag{14}
\]

`X-8612` proves, with rational atanh-series enclosures for all logarithms,

\[
\boxed{
L<\beta_X<M<\alpha<U.
}
\tag{15}
\]

No floating-point comparison is used.

For completeness, if

\[
\frac ab<\frac pq<\frac cd,
\qquad
bc-ad=1,
\]

then

\[
q
=
d(pb-aq)+b(cq-pd)
\ge b+d.
\tag{16}
\]

Thus every reduced rational strictly between Farey neighbors \(a/b,c/d\) has
denominator at least \(b+d\).

Reduce \(\chi/k\) to lowest terms. By `(10)` and `(15)` it lies strictly
between \(L\) and \(U\), so its reduced denominator is at least

\[
6,586,818,670+65,470,613,321
=
72,057,431,991.
\]

The original denominator \(k\) is no smaller. This proves `(1)`.

The mediant itself lies inside the product cylinder, so the bound is sharp for
this two-endpoint Diophantine certificate. It is not an assertion that a cycle
exists at the endpoint.

## 5. Charge and support floors

The exact logarithm certificate also proves

\[
\frac{C_*-1}{K_*}<\beta_X.
\tag{17}
\]

For every \(k\ge K_*\), equations `(8)` and `(17)` give

\[
\chi
\ge
\beta_X k
\ge
\beta_X K_*
>
C_*-1.
\]

Since \(\chi\) is integral, \(\chi\ge C_*\), proving `(2)`.

Let \(p\) be the number of valuation-one positions. By `L-8605`,

\[
\chi
=
p-\sum_{a_i\ge3}(a_i-2)
\le p\le s.
\tag{18}
\]

Therefore \(s\ge\chi\ge C_*\), proving `(3)`.

## 6. Exact certificate

Run

```bash
python3 -B experiments/X-8612-defect-charge-cylinder/run.py \
  --output /tmp/X-8612.json \
  --check-results \
  experiments/X-8612-defect-charge-cylinder/results/canonical.json

python3 -B experiments/X-8612-defect-charge-cylinder/verify.py \
  experiments/X-8612-defect-charge-cylinder/results/canonical.json
```

The two implementations independently certify:

```text
Farey determinant:             1
odd-state floor:              72,057,431,991
signed-charge floor:          29,906,536,378
non-2 support floor:          29,906,536,378
packet-normal-form cases:     2,346
weighted-necklace cells:      77
```

## 7. Strategic consequence

The exact support-\(14\) through support-\(17\) computations remain useful
proof-producing compiler tests, but under `(H71)` they are far outside the
globally feasible positive-cycle region.

A full-denominator cycle search should now be organized by

\[
(k,\chi,\omega),
\qquad
\omega=s-\chi,
\]

not by small raw support. The product window fixes \(\chi/k\) inside `(10)`;
`L-8605` then compiles the residual finite packet slack \(\omega\).

## Source and gap audit

- The only external input is `(H71)`. The repository currently records it as a
  branch-qualified premise; this file does not independently re-run the
  \(2^{71}\) verification.
- If `(H71)` is changed, the same proof works with any certified minimum \(X\);
  only the logarithmic cylinder and Farey endpoints must be recomputed.
- This theorem excludes positive cycles below the stated length/support floors.
  It does not exclude divergent nonperiodic orbits.
- The exact Farey certificate is native and independently replayable.
