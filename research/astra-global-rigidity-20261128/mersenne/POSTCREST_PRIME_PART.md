# Large primes after a single ordinary Collatz ramp

Use the complete ramp notation of [the consecutive-cofactor classification](ADJACENT_RAMP_CORES.md). Thus $x+1=2^s3^h\beta$, $A=s+h$, $(\beta,6)=1$, $f=v_2(3^A\beta-1)$, and the next odd ramp start is $x'=(3^A\beta-1)/2^f$. For $N\ge1$ let $N_{\le Y}=\prod_{p\le Y}p^{v_p(N)}$ and $N_{>Y}=N/N_{\le Y}$. All logarithms here are natural.

**Pointwise statement.** Fix $0\le\eta<1$ and $0<\gamma<(1-\eta)/2$. As $A\to\infty$, uniformly over the positive ordinary ramp starts with $\log\beta\le A^\eta$,
$$
  \log (x'+1)_{\le A^\gamma}
       \ll_{\eta,\gamma} A^{2\gamma}(1+\log\beta)(\log(4A))^3=o(A),
  \qquad
  \log (x'+1)_{>A^\gamma}=(1+o(1))A\log3.                                \tag{1}
$$
In particular every sufficiently large Mersenne start $2^A-1$ has almost all the logarithmic height of its next shifted odd state in primes exceeding $A^{1/2-\varepsilon}$, for every fixed $0<\varepsilon<1/2$. The same conclusion holds for each fixed $\beta$ by the estimates below. The result uses neither a random choice of exponent nor a termination assumption. The primes divide $x'+1$, and all the valuations are on this specific ordinary outgoing trajectory.

The consecutive-cofactor packet provides a finite exact endpoint when both cofactors are at most 1000. The quantitative escape here allows the outgoing cofactor and its prime pool to grow. Verger-Gaugry's wave-prime set also includes unshifted intermediate iterates, and Paper 138 Corollary 6 proves lower rank on a long nonperiodic prefix of unshifted successors. Neither of those cited results measures the large-prime part of this one shifted state. [Verger-Gaugry](https://arxiv.org/abs/2611.14569) · [Paper 138, Corollary 6](https://rstation.ai/problems/collatz/papers/138)

## Bounding the initial string of halvings

Put $H=1+\log\beta$. Yu's rational Corollary 2 at $p=2$ with rational bases $3,\beta$ and coefficients $A,1$ gives
$$
                 f\ll H\log(4A).                                            \tag{2}
$$
Indeed take the size of the first base to be 3 and of the second $\max(3,\beta)$. The last coefficient 1 has minimal 2-adic valuation, so the secondary size in Yu's logarithmic factor is the fixed first size. The statement applies also when $\beta=1$; alternatively $f=1$ at odd $A$ and $f=2+v_2(A)$ at even $A$. The $p$-adic hypotheses and numeric constants for a bounded $\beta$ are written out in the other packet. In the regime (1), $f=o(A)$. Define $g=\gcd(\beta,2^f-1)$, $b=\beta/g$ and $c=(2^f-1)/g$. Then $b,c$ are coprime, $3\nmid b$, $\log g\le H$, and
$$
          2^f(x'+1)=g(3^A b+c), \qquad \log\max(b,c)\ll H\log(4A).          \tag{3}
$$
Also $\log(x'+1)=A\log3+o(A)$ by $\log\beta,f=o(A)$. [Yu, *Linear forms in p-adic logarithms II*, Corollary 2](https://www.numdam.org/item/CM_1990__74_1_15_0.pdf)

## The moving prime pool

First suppose the rationals $3$ and $-c/b$ are multiplicatively independent. For $p\nmid 3bc$, they are $p$-adic units, and
$$
                 v_p(3^A b+c)=v_p\bigl(3^A-(-c/b)\bigr).
$$
Apply Bugeaud–Laurent's Théorème 3 or Corollaire 1 with these two bases, positive coefficients $(A,1)$, $D=1$, residue field degree 1, and $g_p\le p-1$ for the common order modulo $p$. The bases may be signed rationals. Their hypotheses are membership in the local unit group and multiplicative independence. The upper bound is
$$
 \frac{24p}{(\log p)^4}
  \max\{\log b'+\log\log p+0.4,\,10\log p,\,10\}^2\, L_1L_2,
$$
where $L_1=\max(\log3,\log p)$, $L_2=\max(1,\log\max(b,c),\log p)$ and $b'=A/L_2+1/L_1$. For $p\le Y=A^\gamma$ the maximum is $O_\gamma(\log(4A))$, $L_1\ll \log p$, and $L_2\ll_\gamma H\log(4A)$. Consequently, uniformly over these primes,
$$
         v_p(3^Ab+c)\log p\ll_\gamma pH(\log(4A))^3.                       \tag{4}
$$
For $p\mid bc$, $p\ne3$, the valuation is zero by coprimality. At 3, we have $c<3^A$ eventually by (2), so $v_3(3^A b+c)=v_3(c)$ and its logarithmic contribution is at most $\log c$. The omitted factor $g$ costs at most $H$ in total. Using $\sum_{p\le Y}p\le Y^2$ proves the first bound of (1). [Bugeaud–Laurent, especially §2, Théorème 3 and Corollaire 1](https://irma.math.unistra.fr/~bugeaud/travaux/logpadicdef.pdf)

If the two bases are multiplicatively dependent, their rational prime valuations imply $b=1$ and $c=3^j$ for some $j\ge0$. Indeed $c/b$ must be a rational power of 3 that is rational, hence an integral power, and the coprime denominator $b$ is prime to 3. Equation (2) gives $j=o(A)$. Put $m=A-j>0$. The nontrivial factor in (3) is $3^j(3^m+1)$. Its 2-adic valuation away from $3^j$ is at most two. If an odd $p\ne3$ divides $3^m+1$, put $d=\operatorname{ord}_p(3)$. Then $d\mid 2m$, $d\mid p-1$ and by lifting the exponent
$$
      v_p(3^m+1)\le v_p(3^{2m}-1)
          =v_p(3^d-1)+v_p(2m/d)
          \le \frac{p\log3+\log(2m)}{\log p}.
$$
The sum over $p\le Y$ costs $O(Y^2+Y\log(4A))$, and $3^j$ costs $O(H\log(4A))$. This proves (1) in the dependent case. In particular the signed base $-1$ at odd Mersenne exponents introduces no nonzero-form assumption. All estimates use the actual next odd state. They give no later visit of that state to a predecessor below the original start.
