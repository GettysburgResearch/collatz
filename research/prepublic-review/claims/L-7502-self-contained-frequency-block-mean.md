# L-7502 — Self-contained true-phase frequency-block mean

**Claim ID:** `L-7502`  
**Status:** `PROPOSED` pending independent review  
**Authoring agent:** `gpt56-breakthrough-01`  
**Created:** 2026-08-01  
**Starting commit:** `2183dc7e66162684e464913a4ae1a222b41b30f3`  
**Frozen source interfaces:** Claude Fourier product at `407a788972a72da2fde59c19e9446e02647cc4f4`; exact phase reciprocity PR #16 `L-9304` at `87478352e65c7b816dfc8b3b30894b71fb50f662`  
**Scope:** the `64 -> 81` Fourier product and positive frequencies used in PR #72 `L-7701`  
**Related candidates:** none

## Status boundary

This is a new proposed strengthening found during the pre-public review of PR #72. It is not used to retroactively verify Claude `L-0020`, PR #72 `L-7701`, or any downstream equidistribution theorem. Each frozen source keeps its own review status.

## Statement

Let `S_K(theta)` be the exact Fourier product of the Claude `64 -> 81` survivor set. Let `r>=1`, assume

\[
81^r\le 2^K,
\]

and let `I` be any interval of exactly `81^r` consecutive positive frequencies contained in `[1,2^K]`. Then

\[
\boxed{
\frac1{81^r}\sum_{\theta\in I}
\frac{|S_K(\theta)|}{2^K}
\le \left(\frac7{10}\right)^r.}
\]

The proof does not use Claude's submitted shifted-cosine estimate `2/pi+1/81`. It uses only the elementary bounded-variation estimate

\[
\frac1{81}\sum_{j=0}^{80}
\left|\cos\!\left(\pi\frac{j+\phi}{81}ight)\right|
\le \frac2\pi+\frac2{81}
<\frac7{10},
\]

with arguments interpreted modulo one.

## 1. Uniform reciprocal digits

For `0<=t<r`, let `q_t(theta)` be the reciprocal residue from PR #16 `L-9304`, reduced modulo `81^(t+1)`, and put

\[
y_t(\theta)=q_t(\theta)/81^{t+1}.
\]

As `theta` runs through any complete residue system modulo `81^r`, the terminal residue `q_(r-1)(theta)` is uniform modulo `81^r`, because multiplication by `-17*64^(r-1-K)` is a unit.

The chain satisfies

\[
q_{t+1}\equiv64q_t\pmod {81^{t+1}}.
\]

Consequently the coordinates

\[
q_0,
\qquad
j_t=\frac{q_{t+1}-64q_t}{81^{t+1}}\pmod {81}
\quad(0\le t<r-1)
\]

are a triangular bijective encoding of `q_(r-1)`. They are therefore uniform and independent in `Z/81Z`. Conditionally on the past, the next phase runs once through a shifted complete `81`-point grid modulo one.

## 2. Elementary one-level average

Put

\[
f(x)=|\cos(\pi x)|,
\]

viewed as a one-periodic function. On `[0,1]`,

\[
\int_0^1f(x)\,dx=2/\pi,
\qquad
\operatorname{Var}_{[0,1]}(f)=2.
\]

For any shifted complete grid, choose one sample point in each interval

\[
[j/81,(j+1)/81].
\]

On an interval `J`, a sample value is at most the interval average plus `Var_J(f)`. Summing the 81 inequalities gives

\[
\frac1{81}\sum_{j=0}^{80}f(x_j)
\le
\int_0^1f(x)\,dx+rac{\operatorname{Var}(f)}{81}
=rac2\pi+rac2{81}.
\]

Iterated conditional averaging therefore yields

\[
\frac1{81^r}
\sum_{\theta\in I}
\prod_{t<r}|\cos(\pi y_t(\theta))|
\le a_0^r,
\qquad
a_0:=\frac2\pi+rac2{81}.
\]

Using `3<pi<4`,

\[
\frac12<a_0<\frac{56}{81}<\frac7{10}.
\]

## 3. Reciprocity hypothesis and true-phase error

Let

\[
x_t(\theta)=z_{K,t}(\theta)/64^{K-t}
\]

be the true phase. PR #16 `L-9304` requires

\[
17\theta<64^{K-t}.
\]

This holds for every `theta<=2^K` and `t<r`. Indeed, `81^r<=2^K` and `81>64` imply `6r<K`. Hence

\[
64^{K-t}\ge64^{K-r+1}
>17\,2^K
\ge17\theta.
\]

The exact reciprocity identity is therefore available at every retained level:

\[
x_t-y_t=rac{17\theta}{81^{t+1}64^{K-t}}.
\]

Since `|cos(pi x)|` is `pi`-Lipschitz and all factors lie in `[0,1]`, product telescoping gives

\[
\left|
\prod_{t<r}|\cos(\pi x_t)|
-
\prod_{t<r}|\cos(\pi y_t)|
\right|
\le
\pi\sum_{t<r}|x_t-y_t|.
\]

The geometric sum satisfies

\[
\sum_{t<r}|x_t-y_t|
<\frac{\theta}{64^K}
\le\frac1{32^K}.
\]

Thus the mean true product is at most

\[
a_0^r+4/32^K.
\]

## 4. Absorbing the error below `7/10`

The feasibility condition with `r>=1` forces `K>=7`. Moreover

\[
\frac7{10}-a_0
>
\frac7{10}-\frac{56}{81}
=rac7{810}.
\]

Because `a_0>1/2` and `r<=K`,

\[
\left(\frac7{10}\right)^r-a_0^r
>
\frac7{810}\,2^{-(r-1)}
\ge
\frac7{810}\,2^{-(K-1)}
>
\frac4{32^K}.
\]

Therefore

\[
a_0^r+4/32^K
<
(7/10)^r,
\]

which proves the stated true-phase block mean. ∎

## Dependency audit

- The exact Fourier product and the reciprocal identity are frozen branch-qualified inputs.
- The reciprocal-digit bijection is reconstructed above from the unit congruence.
- The one-level cosine bound is proved directly from total variation; Claude `L-0012` is not used.
- The reciprocity hypothesis omitted from PR #72 `L-7701` is checked explicitly.
- No finite computation is load-bearing.

## Gap audit

- This proves only the local frequency-block mean.
- It does not verify the density-one shell assembly, Erdős–Turán transfer, minimal-survivor consequence, or the all-depth ordinary-integer intersection.
- It does not alter the status of any frozen source theorem.
- The exact Fourier-product and reciprocity inputs still retain their own branch statuses.

## Suggested review

1. Check the triangular reciprocal-digit bijection.
2. Check the shifted-grid total-variation estimate.
3. Check `6r<K` and the `L-9304` representative hypothesis.
4. Check the final error-gap inequality at the first feasible `K=7`.
