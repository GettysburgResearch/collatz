# A height bound for finite simple trajectories at the entropy threshold

**PROPOSED.** Let \(x_0,\ldots,x_{m-1}\) be distinct positive integers with \(T(x_i)=x_{i+1}\) for \(i+1<m\), where \(T\) is the shortcut Collatz map. Let \(M=\max_i x_i\), \(p=\log_3 2\), and \(h=H_2(p)\). There are absolute positive constants \(c,C\) such that, for \(M\ge2\),
\[
 m\le C M^h\exp\{-c(\log M)^{1/3}\}.                       \tag{1}
\]
The theorem also applies to one period of a cycle. On any infinite distinct orbit, its prefix maxima therefore satisfy, for all large \(k\),
\[
 \max_{0\le i<k}x_i
 \ \ge\ k^{1/h}\exp\{c'(\log k)^{1/3}\}
\]
with an absolute \(c'>0\). This conclusion concerns maxima over time. An unbounded orbit can return to values below earlier records.

## The height cap confines the walk

Put \(L=\lfloor\log_2 M\rfloor\), \(w=\delta L^{1/3}\), and \(Y=M e^{-w}\), where a fixed, sufficiently small \(\delta>0\) is chosen below. It suffices to work at large \(M\). The [critical count for finite segments](CRITICAL_MOMENT.md) bounds the number of states at most \(Y\) by \(O(Y^h)\). At most \((L+1)O(Y^h)\) starts have a visit at most \(Y\) in their next \(L\) steps, counting the source itself and only steps inside the segment. Indeed, each low state has at most one predecessor at each given time lag in the indexed segment. Discard these starts and the last \(L\) positions. Every remaining length-\(L\) window lies wholly in \((Y,M]\).

Let \(q_t\) count the odd inputs in this window's first \(t\) steps and write \(D_t=q_t-pt\). With \(x\) its first value, the shortcut affine identity reads \(T^t(x)=3^{D_t}x+E_t\) with \(0\le E_t\le(3/2)^L-1\). For large \(M\) the latter bound is below \(Y/2\). The window thus satisfies
\[
 \frac{Y}{2M}\le 3^{D_t}\le\frac{M}{Y}
 \qquad (0\le t\le L).
\]
In particular \(|D_t|\le W=(w+\log 2)/\log 3\).

## Counting words in a strip

Under the Bernoulli law with parameter \(p\) the centered walk \(Z_t\) has increments \(B-p\). Its largest one-point probability after \(s\) steps is at most \(C_p/\sqrt s\). From any starting position inside \([-W,W]\), the probability of lying there after \(s=\lceil A(W+1)^2\rceil\) steps is at most \((2W+2)C_p/\sqrt s\le1/2\), for fixed large \(A\). Apply this estimate to consecutive independent blocks. The probability of staying in the strip for \(L\) steps is at most
\[
 2^{-\lfloor L/s\rfloor}\le 2\exp\{-c_0 L/(W+1)^2\}
\]
for a fixed \(c_0>0\). Each strip word has probability \(2^{-hL}\exp(\lambda D_L)\), \(\lambda=\log(p/(1-p))\). Its inverse weight is at most \(2^{hL}e^{\lambda W}\). Each word accounts for at most two sources \(x\le M\) by the parity cylinder modulo \(2^L\).

The total count is bounded by
\[
 L+O((L+1)M^h e^{-hw})
  +O\!\left(M^h\exp\{\lambda W-c_0 L/(W+1)^2\}\right).
\]
For sufficiently large \(L\), \(W+1\le C_1\delta L^{1/3}\), where \(C_1\) is absolute. Choose \(\delta>0\) so that \(c_0/(C_1\delta)^2>2\lambda C_1\delta\). Both exponential factors then save \(\exp(-c L^{1/3})\) after decreasing \(c\) to absorb the polynomial. This proves (1). To invert it use \(M\ge k\) for a prefix of \(k\) distinct integers.

## Scope and remaining obstruction

The common height cap applies for every time inside the chosen segment. To bound all visits below a fixed \(X\) on an unbounded trajectory, intervening states may exceed \(X\) by an arbitrary factor. In that case the upper strip bound used here requires a larger cap. The exponent \(1/3\) arises by balancing the low-state cost \(\exp(-hw)\) against the centered-walk confinement cost \(\exp(-cL/w^2)\). This balance gives no fixed power saving below \(h\).
