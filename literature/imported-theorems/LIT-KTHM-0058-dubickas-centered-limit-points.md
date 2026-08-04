# LIT-KTHM-0058 — Exact Dubickas limit-point bounds and the four-phase `81/64` lift

**Status:** `KNOWN — EXACT SOURCE + EXACT NATIVE COROLLARY`  
**Primary source:** Artūras Dubickas, *On the Distance from a Rational Power to the Nearest Integer*, Journal of Number Theory 117 (2006), 222–239, Theorems 3 and 4  
**Source inspection:** complete PDF, including the definitions on pp. 224–225, Theorem 4 on p. 226, and the proof of Theorem 3 on pp. 236–237  
**Native interfaces:** PR #16 `T-9315/T-9317`, PR #67 centered height renewal  
**Counterexample status:** no ordinary survivor or Collatz counterexample is claimed

## Source theorem

For `0<r<1`, define

\[
T(r)=\prod_{m\ge0}(1-r^{2^m}),
\qquad
E(r)=\frac{1-(1-r)T(r)}{2r}.
\tag{1}
\]

Dubickas proves that if `p>q>=1` are coprime and `xi` is nonzero, then

\[
\limsup_{n\to\infty}
\left\|\xi\left(\frac pq\right)^n\right\|
\ge \frac{E(q/p)}p.
\tag{2}
\]

The theorem also gives an explicit small limit point. The load-bearing input for the repository is `(2)`.

The source derives `(2)` from a sharp theorem on tails of non-ultimately-periodic integer sequences. If `s_n` is such a sequence, then infinitely many tails satisfy

\[
\left|s_l+s_{l+1}r+s_{l+2}r^2+\cdots\right|>E(r)-\varepsilon.
\tag{3}
\]

The source exhibits sharp extremal sequences through the Thue–Morse word. This is an extremal real-tail theorem, not an ordinary-integer extraction theorem.

## Direct `(81,64)` specialization

Taking `(p,q)=(81,64)` gives

\[
\boxed{
\limsup_n\left\|\xi(81/64)^n\right\|
\ge \rho_{81/64}:=\frac{E(64/81)}{81}.}
\tag{4}
\]

The exact interval computation in `LIT-X-0058` gives

\[
0.007747163838833358349215
<\rho_{81/64}<
0.007747163838833358349216.
\tag{5}
\]

The native centered radius is

\[
\frac1{81}=0.012345679012345679\ldots,
\]

so the direct scalar theorem is strictly subcritical.

## Stronger four-phase corollary

Assume a hypothetical centered orbit is written

\[
\xi(81/64)^n=B_n+u_n,
\qquad B_n\in\mathbb Z,
\qquad |u_n|\le\frac1{81}.
\tag{6}
\]

Use

\[
81/64=(3/2)^4
\]

and apply the source theorem for `3/2` to `8xi`. For `j=0,1,2,3`,

\[
8\xi(3/2)^{4n+j}
=2^{3-j}3^jB_n+8(3/2)^ju_n.
\tag{7}
\]

The first term is an integer. Therefore the four phasewise distance bounds are

\[
\frac8{81},\qquad \frac4{27},\qquad \frac2{9},\qquad \frac13.
\tag{8}
\]

For `3/2`, Dubickas's constant is

\[
\rho_{3/2}=\frac{3-T(2/3)}{12}
=0.238117558418513716\ldots .
\tag{9}
\]

Because `T(2/3)<1/3`, one has

\[
\rho_{3/2}>2/9.
\]

Hence every subsequence realizing the source lower limit must eventually lie in phase `j=3`. In that phase, `(7)` gives the exact identity

\[
\left\|8\xi(3/2)^{4n+3}\right\|=27|u_n|.
\]

Consequently

\[
\boxed{
\limsup_{n\to\infty}|u_n|
\ge
\frac{3-T(2/3)}{324}.}
\tag{10}
\]

The exact interval is

\[
0.008819168830315322822179
<\frac{3-T(2/3)}{324}<
0.008819168830315322822180.
\tag{11}
\]

This strictly improves `(5)`, while remaining below `1/81`.

## Strategic meaning

The full PDFs settle the previous source ambiguity:

```text
source scalar constant at 81/64:
  exact and subcritical;

four-phase use of 81/64=(3/2)^4:
  gives a stronger exact lower limit;

remaining obstruction:
  ordinary arithmetic stabilization, not a missing scalar estimate.
```

Thus another search for a slightly better one-dimensional limit-point constant is unlikely to close PR #16 or PR #67. A decisive theorem must use the integer cylinder, appended blocks, renewal quotient, or an equality/near-extremal language theorem substantially stronger than `(2)`.

## Applicability audit

- The source assumes only `xi!=0`; no irrationality hypothesis is needed because `q>1`.
- The source theorem concerns real distances to the nearest integer and does not assert integrality of the nearest integers.
- The four-phase argument is an exact native corollary, not a statement printed in the paper.
- The strict inequality `rho_(3/2)>2/9` follows from the first product factor `T(2/3)<1/3`.
- Equality cases for arbitrary rational `p/q` are not classified by the source theorem.

## Gap audit

- The lower bound `(10)` leaves positive slack to `1/81`.
- The sharp Thue–Morse construction in the source is for the unrestricted integer-tail theorem; it does not say every near-extremal centered orbit is Thue–Morse.
- No contradiction with an all-time centered orbit follows.
- No ordinary seed is constructed.

## Exact artifact

```bash
python3 literature/experiments/LIT-X-0058-centered-dubickas/run.py \
  --check-results \
  literature/experiments/LIT-X-0058-centered-dubickas/results/canonical.json
```
