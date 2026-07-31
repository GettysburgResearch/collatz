# T-6608 — the coefficient corridor gives an exact entropy-return certificate

**Claim ID:** `T-6608`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6604`; elementary binomial counting  
**Scope:** every finite first-coefficient-crossing word  

## 1. Setup

Let

\[
v=(v_0,\ldots,v_{j-1})
\]

be a first coefficient-crossing parity word, and write

\[
S_t=\sum_{r=0}^{t-1}v_r,
\qquad
\alpha={\log2\over\log3},
\qquad
D_t=S_t-\alpha t.
\]

Thus

\[
0\le D_t\le B
\qquad(0\le t<j),
\tag{1}
\]

where

\[
B=\max_{0\le t<j}D_t,
\]

while `D_j<0`.

Put

\[
q=S_j,
\qquad
\lambda=j\log2-q\log3>0.
\tag{2}
\]

For `1<=L<=j-1`, define the exact corridor word count

\[
\boxed{
\mathcal N(L,B)
=
\sum_{s=s_-(L,B)}^{s_+(L,B)}\binom Ls,}
\tag{3}
\]

where

\[
s_-(L,B)=\max\{0,\lceil\alpha L-B\rceil\},
\qquad
s_+(L,B)=\min\{L,\lfloor\alpha L+B\rfloor\}.
\tag{4}
\]

## 2. Every proper factor lies in the corridor

Consider a length-`L` factor beginning at

\[
0\le a\le j-1-L.
\]

Its number of ones is

\[
S_{a+L}-S_a
=
\alpha L+D_{a+L}-D_a.
\tag{5}
\]

Both endpoints are proper prefixes, so `(1)` gives

\[
\alpha L-B
\le
S_{a+L}-S_a
\le
\alpha L+B.
\tag{6}
\]

Therefore every such factor is one of the `N(L,B)` binary words counted in `(3)`.

There are exactly

\[
j-L
\]

proper factor starts.

## 3. Exact return criterion

If

\[
\boxed{j-L>\mathcal N(L,B),}
\tag{7}
\]

then two proper starts carry the same length-`L` factor.

If their physical states are equal, the segment already contains a positive cycle.

If their physical states are distinct and the endpoint does not descend, `T-6604` forces

\[
\boxed{
2^L+1
<
3^B\left({j\over\lambda}+{j\over2}\right).}
\tag{8}
\]

Consequently the two exact inequalities

\[
\boxed{
\begin{aligned}
j-L&>\mathcal N(L,B),\\
2^L+1&\ge
3^B\left({j\over\lambda}+{j\over2}\right)
\end{aligned}}
\tag{9}
\]

exclude every acyclic ordinary no-descent realization of the word.

No symbolic factor enumeration, Baker theorem, or asymptotic estimate is required.

## 4. Canonical Box-2 consumer

Let `r^+(v)` be the least positive parity-cylinder representative. If the canonical descent target fails, then `r^+(v)` itself is an ordinary no-descent realization at the crossing.

Thus `(9)` is a proof-producing sufficient certificate for

\[
r^+(v)>{A_v\over2^j-3^q},
\]

outside the positive-cycle alternative.

The required inputs are finite and exact:

```text
j and q;
the maximum bank B of the word;
one factor length L;
a directed lower interval for lambda;
the binomial count N(L,B).
```

## 5. Necessary bank inequality for a target failure

Suppose `(7)` holds and no physical state repeats. Rearranging `(8)` gives

\[
\boxed{
B>
\log_3\left(
{2^L+1\over j/\lambda+j/2}
\right).}
\tag{10}
\]

Hence every canonical target failure must carry enough coefficient bank to pay for each recurrence forced by the corridor count.

Taking the maximum over all `L` satisfying `(7)` gives the implicit exact lower bound

\[
\boxed{
B>
\max_{\substack{1\le L<j\\ j-L>\mathcal N(L,B)}}
\log_3\left(
{2^L+1\over j/\lambda+j/2}
\right).}
\tag{11}
\]

The occurrence of `B` on both sides is deliberate: `(11)` is a finite monotone fixed-point test for the allowed bank.

## 6. Entropy relaxation

For asymptotic use, standard binomial estimates may replace `(3)` by

\[
\mathcal N(L,B)
\le
(2B+2)
2^{L H_2(\alpha+B/L)}
\tag{12}
\]

whenever `alpha+B/L<=1/2` is replaced by the appropriate monotone side around the maximum binomial coefficient; a symmetric formulation using

\[
\max_{|x-\alpha|\le B/L}H_2(x)
\]

is always valid.

This yields source-free asymptotic recurrence criteria for sublinear corridors. The exact theorem, however, is `(3)--(9)` and avoids all entropy-approximation conventions.

## 7. Composition with the mechanical packet

- `T-6605/T-6606` force recurrence from a small mechanical swap budget.
- `T-6608` forces recurrence directly from a narrow coefficient corridor, even when the word is far from mechanical.
- `T-6607/L-6602` isolate the remaining wrap quotient when recurrence is insufficient.

A surviving canonical target failure must therefore be simultaneously:

```text
wide-corridor enough to defeat the binomial return count;
large-swap enough to defeat the mechanical return count;
and wrapped into the short dangerous defect window.
```

## 8. Gap audit

- A wide bank can make `N(L,B)=2^L`, eliminating the return conclusion.
- For logarithmic `L`, the dyadic return may be too short to beat an exceptionally small `lambda`.
- A repeated physical state is handed to the cycle lane rather than excluded here.
- The theorem supplies an exact finite certificate and a bank lower bound, not a universal contradiction.
