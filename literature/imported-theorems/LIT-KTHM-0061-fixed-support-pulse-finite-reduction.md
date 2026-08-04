# LIT-KTHM-0061 — Every fixed pulse support below the critical density reduces to a finite exact decision

**Status:** `PROPOSED / BRANCH-QUALIFIED NATIVE COROLLARY; SOURCE-AUDITED LOGARITHMIC STEP`  
**Dependencies:** PR #53 `L-8201` fixed-cone resultant caps; the distributed-pulse identity reconstructed in PR #70; `LIT-KTHM-0060`  
**Scope:** upward valuation pulses over repetitions of the two known ordinary negative accelerated cycles  
**Counterexample status:** this is a finite-reduction theorem, not an exclusion or a positive-cycle certificate

## Statement

Let a primitive ordinary negative accelerated cycle have odd-state length `k`, total valuation `A`, and largest absolute state `c_*`. Repeat it `r` times and increase the valuations at exactly `s` distinct positions by arbitrary positive amounts.

If

\[
\boxed{
\Delta_s
:=A\log2-\frac{s-1}{s}k\log3>0,}
\tag{1}
\]

then there is an explicit finite repetition cutoff `R_s` such that every positive-cycle divisor hit has

\[
r<R_s.
\]

For each remaining repetition, PR #53 `L-8201` gives explicit finite caps on every pulse height. Hence the complete exactly-`s`-pulse class is decidable by a finite exact computation.

For the two native baselines:

\[
P3=(1,2),\qquad(A,k)=(3,2),
\]

condition `(1)` holds exactly for

\[
\boxed{s\le18,}
\tag{2}
\]

while for

\[
P11=(1,1,1,2,1,1,4),\qquad(A,k)=(11,7),
\]

it holds exactly for

\[
\boxed{s\le117.}
\tag{3}
\]

Thus the one-, two-, and three-pulse theorems are the first computed layers of a much larger finite-decision envelope.

## Proof of the repetition reduction

The `s` support points cut the repeated cycle of length `kr` into `s` positive cyclic gaps. Rotate the support point following a largest gap to position zero and write

\[
0=p_1<p_2<\cdots<p_s<kr.
\]

The final gap is at least `ceil(kr/s)`, so

\[
\boxed{
p_s\le\left\lfloor\frac{s-1}{s}kr\right\rfloor.}
\tag{4}
\]

The exact distributed-pulse identity has positive reduced weights and the chain form

\[
R=-w_1+
(w_1-w_2)P_1+
\cdots+
(w_{s-1}-w_s)P_{s-1}+w_sP_s,
\tag{5}
\]

where

\[
w_1>w_2>\cdots>w_s>0,
\qquad
P_i=2^{d_1+\cdots+d_i},
\qquad
P_s=2^t.
\]

All nonconstant coefficients in `(5)` are positive and sum to `w_1`; hence

\[
0<R<w_1 2^t.
\tag{6}
\]

The largest-gap normalization and the finite primitive negative-state list give

\[
w_1\le c_*3^{p_s}
\le c_*3^{\lfloor (s-1)kr/s\rfloor}.
\tag{7}
\]

The candidate denominator is

\[
D=2^{Ar+t}-3^{kr},
\]

and a positive divisor hit has `D|R`, so `D<=R`. Put

\[
\Lambda=(Ar+t)\log2-kr\log3>0.
\]

Dividing `(6)` by `2^{Ar+t}` gives

\[
0<1-e^{-\Lambda}
<c_*\frac{3^{\lfloor (s-1)kr/s\rfloor}}{2^{Ar}}.
\tag{8}
\]

When `(1)` holds, the right side decays exponentially in `r`; it is eventually below `1/2`, and then

\[
\Lambda
<2c_*\exp(-\Delta_s r).
\tag{9}
\]

`LIT-KTHM-0060` gives the incompatible lower bound

\[
\log\Lambda
>-748000000\log2\log3\,(1+\log(kr+1)).
\tag{10}
\]

The right side of `(9)` decays linearly in `r` after taking logarithms, whereas `(10)` decays only logarithmically. Therefore all sufficiently large `r` are impossible, and an explicit cutoff is obtained by solving one monotone inequality.

For each `r<R_s`, there are finitely many supports. `L-8201` proves a nonzero one-variable resultant for every pulse coordinate and an explicit coordinate cap. The remaining search is finite.

## Exact support thresholds

Condition `(1)` is equivalent to

\[
s<\frac{k\log3}{k\log3-A\log2}.
\tag{11}
\]

The exact rational logarithm intervals in `LIT-X-0060` certify

\[
18<\frac{2\log3}{2\log3-3\log2}<19
\]

and

\[
117<\frac{7\log3}{7\log3-11\log2}<118.
\]

This proves `(2)`–`(3)`.

## What this changes

Before this reduction, the repository had complete all-repetition calculations only at support one, two, and three. The exact logical frontier is now:

```text
P3:
  support 1..18 -> finite exact decision in principle;
  support >=19 -> this largest-gap/Matveev rate no longer closes.

P11:
  support 1..117 -> finite exact decision in principle;
  support >=118 -> this rate no longer closes.
```

This is an architecture-level narrowing. It identifies a genuine density threshold rather than merely asking for “more pulses.”

## Applicability and dependency audit

- The proof is conditional on the native distributed-pulse identity and monotone reduced weights.
- `L-8201` is needed for finite height caps after the repetition cutoff.
- The Matveev step is source-audited by `LIT-KTHM-0060`.
- The theorem does not assert that the finite boxes are computationally small.
- It does not apply to mixed baselines or downward pulse changes.

## Gap audit

- Supports `4..18` and `4..117` have not been exhaustively replayed.
- At and above the critical support density, the exponent in `(9)` is nonpositive and this proof gives no cutoff.
- A finite reduction is not a Collatz proof or disproof.
- Zero resultants would require separate treatment, although `L-8201` rules them out in its fixed-cone setting.

## Suggested next attack

Do not launch blind support-by-support scans. First generalize the Legendre/convergent layer of `T-8260` symbolically in `s`, so that the Matveev cutoff collapses to a small transition range. Then use `L-8201` only on the surviving finite packets. The first uncomputed target is support four.
