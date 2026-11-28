# Finite kernel specification for the direct positive clock

This file is a finite restatement of QUADRATIC_CLOCK_PADE §§1–4 for the planned Lean development. It avoids constructing 2-adic numbers, infinite series or real analytic limits. The required objects are natural exponents, signed integers, rationals, odd-denominator valuations and finite words.

## Native input and affine tails

Let $x>0$ be an ordinary source, and let $t_j$ be the physical clock of its even input numbered $j$ starting at zero. Assume $t_j=a+j(b+1)+h\binom j2$ for $0\le j\le5s+2$ with $a,b\ge0$, $h,s\ge1$. Let $q=3^h/2^h$, $z=2^{b+1}/3^b$ and $p_l=z^l q^{-\binom l2}$. Put $y=-(x+1)(3/2)^a$, an integer since $a=v_2(x+1)$. For every observed $j$,
$$
 y-\sum_{l<j}p_l=-2^{t_j-a}3^{a-(t_j-j)}(T^{t_j}x+1).
$$
The terminal factor is odd. Thus the signed rational on the left has valuation **exactly** $t_j-a=j(b+1)+h\binom j2$. This is a finite affine identity, adjacent to the existing PinClock affine kernels. A rational with odd denominator is divisible by $2^d$ exactly when its integer numerator is; normalized fractions or an explicit odd common denominator both work.

## Coefficients and denominator-free implementation

Set $n=2s$, $m=s$, $N=n(n+m)$, $M=\binom m2$ and $E_k=\binom k2+km$. Write $q=q_1/q_2$, $z=z_1/z_2$ in lowest terms. For a subset $S\subseteq\{1,\ldots,n\}$ let $k=|S|$, $d=\sum_{j\in S}j$. Define
$$
 U(S,l)=(-1)^k z_1^{n+l-k}z_2^{m+k-l}
 q_1^{M+d+E_k-\binom l2}q_2^{N-d-E_k+\binom l2}
 \qquad(0\le l\le k+m).
$$
All exponents are natural numbers by $d\le kn-\binom k2$ and $\binom{k+m}2=E_k+M$. Put $B_k=\sum_{|S|=k}U(S,0)$, $B_*=\sum B_k$, $A_*=\sum_{S}\sum_{l\le k+m}U(S,l)$. Every $U(S,l)$ is an integer of absolute value at most $H(z)^{n+m}H(q)^{N+M}$. This gives the exact bound (6) in the main proof. Moreover $B_k p_l=\sum_{|S|=k}U(S,l)$ for these $l$.

For e.g. the algebra of cancellation one may also represent the same $B_k$ in the rationals as $D c_k z^{-k}q^{E_k}$, where $D=z_1^n z_2^m q_1^M q_2^N$ and $c_k$ is coefficient $k$ of $R(X)=\prod_{j=1}^n(1-q^jX)$. The degree bound is sharp, attained once for the $k$ largest distinct indices, so $v_2(c_k)=-h(kn-\binom k2)$. It follows $v_2(B_k)=(n-k)[b+1+h(n+m)]$, with $B_n$ an odd integer. This also proves that $B_*$ is odd, by a unique least valuation.

## No infinite sum in the Padé cancellation

Let $j_k=n+m+k+2$. The following is a finite rational identity:
$$
 B_*y-A_*=
 D\,R(q^{-(n+1)}) z^{n+m+1}q^{-\binom{n+m+1}2}
 +\sum_{k=0}^n B_k\left(y-\sum_{l<j_k}p_l\right).
$$
To prove it insert the finite tails, reindex $l=t+m+k$, and collect $t=1,\ldots,n+1$. The binomial identity for $\binom{m+k+t}2$ leaves $R(q^{-t})$ in the $t$th group. For $1\le t\le n$ its factor at $j=t$ is zero. For $t=n+1$ every factor $1-q^{j-t}$ is a dyadic unit and the displayed leading term has valuation
$$
 W=h(21s^2+3s)/2+(5s+1)(b+1).
$$
For the remaining term at $k$ use the native tail and the coefficient formula. More explicitly for $t=n+2$, $j_k=t+m+k$,
$$
 v_2(B_k p_{j_k})=v_2(D)+(t+m)(b+1)+h\binom{t+m}2
       +h\left[k(t-n)+\binom k2\right].
$$
This is at least $W+(b+1)+h(n+m+1)>W$. All $j_k\le 5s+2$ were assumed observed, so every physical tail is strictly above the leading valuation. This proves $v_2(B_*y-A_*)=W$, directly for the actual nonzero **integer**. The first margin (9) now follows with no agreement to an infinite reference.

## Physical cutoff using only the last observed even input

Let $K$ be the *last observed even index* in the matching window, and let $B=\log_2(x+1)$. For $K\le1$ or no zero, $L<8B$ by successive odd-run bounds. For $K\ge2$, $a\le B$, $b\le\gamma B$, $h\le\gamma^2B$, $\gamma=\log_23$. Even when the final run is incomplete:
$$
 L\le a+(K+1)(b+1)+h\binom{K+1}2.
$$
If $K\le11$, this gives $L<210B$ directly. Otherwise $s=\lfloor(K-2)/5\rfloor\ge2$, $5s+2\le K$, and $K+1\le5s+7\le9s$. Thus
$$
 L\le B+9bs+50hs^2,\quad
 \Delta_h hs^2+\Delta_b bs\le1+\gamma B,
 \quad \Delta_h>3/17,\ \Delta_b>4/17.
$$
It follows $L<B+284(1+\gamma B)<1000B$. This recovers exactly the manuscript's physical conclusion by finite statements alone.

The analytic logarithmic closing step can equivalently be packaged with integer powers and a final bit-length bound. The key finite division statement $2^W\mid B_*y-A_*$, $2^{W+1}\nmid B_*y-A_*$ and the coefficient bound work without logarithms.
