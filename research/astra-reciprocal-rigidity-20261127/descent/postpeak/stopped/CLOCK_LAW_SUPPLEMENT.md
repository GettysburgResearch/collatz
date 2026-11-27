# The complete first-meeting law in growing integer shells

Write \(H\) for the number of prescribed initial odd shortcuts, with the next bit free. For a positive source \(n\) on this cylinder, let \(\tau_H(n)=0\) if its original orbit meets any smaller positive source by original clock \(H\). Otherwise \(\tau_H(n)\) is the first further original index of such a meeting, possibly infinity. Every visitor clock is allowed. The comparison variable \(\tau\) uses independent fair post-ascent bits and the Haar ternary variable in the [stopped profile](PROFILE.md).

Let \(400\le H\le(\log_2 X)/120\), \(T=\lfloor H/6\rfloor-1\). Sample **uniformly from the actual integers** \(X\le n<2X\) with \(n=-1\bmod 2^H\). The joint law of the first \(T\) post-ascent bits and the complete value of \(\tau_H(n)\), including a possible infinite sample value, has total variation distance from the corresponding model law at most
\[
                     O\!\left(H^{-1/2}+H X^{-1/450}\right).            \tag{1}
\]
In particular it converges when \(H\to\infty\) anywhere in this range. The fixed-\(H\) ordinary source-density law separately has all its moments finite. Its full mean grows as \(\sqrt H\). The final section gives growing-shell moment statements for explicit polynomial truncations. These are written mathematical consequences of the cited results.

## Finite and unrestricted tests on a full binary subcylinder

Put \(B=H+T\le(\log_2X)/90\), \(J=\lfloor(\log_2X)/2\rfloor\). Fix a complete \(T\)-bit word and a prefix \(w\) of length \(j\le T\). The complete dyadic subcylinder has \(M=X/2^B+O(1)\gg X^{89/90}\) sources in the shell. Write \(f\) for the weight of \(w\), \(h=H+f\), \(R=C_w/2^j\). Its endpoint and gain are
\[
 Y=R+g_*(n+1),\qquad g_*=3^h/2^{H+j}>1 ,
\]
because \((3/2)^H>2^{H/2}\) and \(j\le H/6\). If \(w\) is nonmaximal, the explicit smaller visitor exists for every source. Assume henceforth that it is maximal, so the pointwise cone excludes all smaller visitors of grade at most \(h\). The prescribed subsequent \(T-j\) binary bits do not affect this exclusion.

For a legal reverse word of length \(d\le J\) and grade \(k>h\), write \(g=3^k/2^d\), \(D=g_*/g\), and let \(A\) be its forward affine numerator. Its inverse source is
\[
             m=D(n+1)+(2^dR-A)/3^k .
\]
It is positive, since actual legal inverse branches from positive integers remain positive. The equality \(D=1\) would force \(k=h\). Otherwise \(|1-D|\ge1/(2^{H+j}3^k)\). With \(0\le A\le3^d\), \(|R|\le(3/2)^j\), the condition
\[
                    n>2^B(3^J+2^J(3/2)^T)
\]
makes \(m<n\) exactly when \(g>g_*\). In the \(D<1\) direction use \(D<1\) for the one additive \(D\), and \(3^k\le3^J\); in the \(D>1\) direction the additive \(D\) is favorable. The condition holds uniformly for large \(X\), since \(3^J\le X^{4/5}\), \(2^J(3/2)^T\le X^{1/2+1/150}\), \(2^B\le X^{1/90}\).

Thus the finite-deadline event is a union of ternary classes modulo \(3^J\) in \(n\). In the final binary subcylinder it differs from its Haar probability by \(O(3^J/M)\). Here \(Y\) is Haar-uniform on \(R+3^h\mathbb Z_3\) when \(n\) is Haar-uniform in ternary coordinates. Conditioning on the extra \(T-j\) dyadic bits merely sets the spacing for the arithmetic progression sampled in this count.

There are two distinct truncation errors.

1. A true smaller visitor missed by the finite physical test gives a target whose **least** positive ancestor first arrives after \(J\), without going below itself. The map from \(n\) to \(Y\) is injective on this complete binary subcylinder. All targets and least ancestors lie below \(Z=4X(3/2)^B\ll X^{151/150}\). The uniform ordinary long-arrival estimate from the companion note bounds the relative count by \(O((Z2^{-J/25}+Z^{49/50})/M)\).
2. At a Haar-uniform unrestricted ternary target, a length-\(d\) reverse word of gain \(>1\) has more than \(d\log_3 2>5d/8\) odd steps, and its legality mass \(3^{-k}\) is below \(2^{-d}\). There are at most \(2^{d h_2(5/8)}\le2^{24d/25}\) candidate words, by the binary entropy bound. The probability of any such word at any \(d>J\) is \(O(2^{-J/25})\). Conditioning on the ball \(R+3^h\mathbb Z_3\) multiplies the upper bound by at most \(3^h\). This applies to the relevant larger-gain words because \(g_*>1\). The fixed-\(H\) all-clock transfer already identifies their higher-grade union with the complement of the physical protection probability \(p_{H,w}\).

The elementary entropy numbers and the first error are established in the earlier [uniform long-arrival estimate](../allclock/SCALED_TARGETS.md). Weaver's earlier finite-clock/all-visitor transfer and gain-word counting are the antecedents of these arguments. [Weaver 177/v1 §§7–8](https://rstation.ai/problems/collatz/papers/177/v1) · [Weaver 178/v1 §§1–2](https://rstation.ai/problems/collatz/papers/178/v1) · [Exact stopped-law identification](STOPPED_LAW.md)

The three resulting errors \(3^J/M,\ (Z2^{-J/25}+Z^{49/50})/M,\ 3^h2^{-J/25}\) are all \(O(X^{-1/450})\). In the second error the two exponents of \(X\) are \(-1/450\) and \(-53/22500\); in the third use \(3^h\le X^{4/225}\). In particular, uniformly in the *complete* \(T\)-word and every prefix length \(j\), its empirical conditional survival through \(j\) differs from \(p_{H,w}\) by \(O(X^{-1/450})\). This is two-sided. For nonmaximal words both probabilities vanish.

## Total variation, including the far tail

The earlier stopped law compares \(p_{H,w}\) with the model conditional survival at error
\(\epsilon_H=2^{5-H/24}+(2/3)2^{-\lfloor H/2\rfloor}\) uniformly on maximal prefixes. Taking consecutive differences gives the integer clock bins \(0,\ldots,T,>T\). On each full word their total variation discrepancy is \(O((T+1)(\epsilon_H+X^{-1/450}))\). The empirical full-word probabilities themselves have aggregate discrepancy \(O(2^B/X)\) from fair bits by dyadic rounding.

To expand the final bin into all remaining clock values, the additional total variation is bounded by the sum of the two unconditional tail masses. The model tail is \(O((T+1)^{-1/2})\). The actual shell tail is at most this order plus \(O(2^B/X)\), by the finite dyadic counted-sibling test from Leen and Weaver in the synchronization note. Its upper bounds allow even a sample source never meeting any smaller source. This proves (1). It does not infer a pointwise merger or a literal untruncated average over finite samples from convergence in total variation. [Synchronization estimate](SYNCHRONIZATION.md) · [Weaver 124/v1 Theorem 1](https://rstation.ai/problems/collatz/papers/124/v1)

## Full moments of the finite-height density law

Now take ordinary source-height density at fixed \(H\) first, and let \(\mu_H\) be the resulting complete probability mass function of \(\tau_H\). Weaver 178/v1, Theorem 1(a), gives the unconditioned natural-density survival \(d_s\ll\rho^s(s+1)^{-3/2}\) for first smaller meeting through original clock \(s\), where \(\rho=2^{h_2(\log_3 2)-1}\le2^{-1/25}\). Its original and visitor clocks have exactly the complete-orbit meaning used here. Conditioning on the initial odd cylinder therefore gives, for every fixed \(H,t\),
\[
                   \mu_H(\tau_H>t)\le 2^H d_{H+t}
                         \ll (2\rho)^H\rho^t .
\]
Every positive moment is finite for each fixed \(H\). For \(t\ge30H\), summation of this exponential bound with the polynomial moment factor costs \(O_a(1)\), in fact exponentially little as \(H\to\infty\). For \(t\le30H\) use the sibling upper \(O((t+1)^{-1/2})\); for \(t\le H/6-1\) use the matching all-visitors lower estimate. The tail-sum formula gives
\[
 \mathbb E_{\mu_H}[\tau_H^a]\ \asymp_a
 \begin{cases}
    \log H,& a=1/2,\\
    H^{a-1/2},& a>1/2 .
 \end{cases}
\]
For \(0<a<1/2\) these full moments converge to \(\mathbb E[\tau^a]\), by convergence in law and the uniform square-root tail. The limiting variable \(\tau\) itself has infinite moments for \(a\ge1/2\). In particular the **untruncated** first moment of \(\mu_H\) is \(\asymp\sqrt H\). [External unconditional first-meeting theorem](https://rstation.ai/problems/collatz/papers/178/v1) · [Conditional lower bound](SYNCHRONIZATION.md)

## Polynomial caps in the actual finite shell

Fix \(a>0\) and cap the actual waiting time at \(D_X=X^{1/(100a)}\). In the shell range of (1), with \(H\to\infty\), the empirical moment of \(\min(\tau_H,D_X)^a\) has the same respective orders \(\log H\) and \(H^{a-1/2}\) for \(a\ge1/2\); for \(0<a<1/2\) it converges to \(\mathbb E[\tau^a]\).

For the upper bound through \(30H\) the dyadic sibling test gives the square-root tail with additive rounding \(O(2^{H+t}/X)\), at most \(O(X^{-89/120})\) there. Past \(30H\) and up to \(k-H\), \(k=\lfloor\log_2 X\rfloor\), use Weaver 178/v1, Theorem 2's finite-sample upper on **all** starts below \(2X\), divided by the number \(\asymp X/2^H\) in the shell's ramp cylinder. This gives \(O(2^H\rho^{H+t})\), with exponentially small moment tail on this range. In particular the conditional mass still surviving through \(k-H\) is \(O(2^H2^{-k/25})=O(X^{-19/600})\). Its entire contribution up to the chosen cap is at most \(D_X^a O(X^{-19/600})=O(X^{-13/600})\). For large \(X\) the cap exceeds \(k\). The finite-shell lower bound through \(H/6-1\) gives the matching divergent orders. For \(a<1/2\), the part beyond any fixed threshold \(K\) and before \(30H\) is \(O_a((K+1)^{a-1/2})+o(1)\) in the moment tail, and the later parts vanish. Truncating first at \(K\) and using (1) gives the claimed convergence. No bound on untruncated empirical moments at fixed finite \(X\) is asserted. [Weaver 178/v1 Theorem 2](https://rstation.ai/problems/collatz/papers/178/v1)
