# Independent written review of the bounded-birth partition

**Scope.** Independently reconstructed the stronger carry partition proposed in this session and its consequences for finite-window entropy and counting. Status is verified as written mathematics conditional on the specified actual-scalar and sliding-window results. The present note supplies no Lean kernel verification. The input mean estimates and ordinary parity-prefix compression are PR189, exact head a0be70b1ffa075cbc50755ac76036108c028d120. [Sliding-window mean estimates](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/FINITE_PHASE_ENTROPY.md) · [Global occupation setup](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/README.md)

Fix $0<x<1/2$, $D=(1-x)/(1-2x)$, $\lambda=1+Dx$ and $f(0)=1$, $f(i)=Dx^i$ for $i>0$. Summing the geometric series gives $\sum_{i\ge0} f(i)=D$. The exact positive-gap restriction at a digit $b$ and incoming carry $c$ is $0\le d\le b+3c-1$. Let $K_bf(c)=x^c\sum_d f(d)$ over the allowed successors. For $c>0$, $K_bf(c)\le Dx^c=f(c)$. At $c=0$ the three row bounds are $1,\lambda,1+D(x+x^2)$ respectively, and the third is at most $\lambda^2$ since their difference equals $Dx+(D^2-D)x^2$. Thus $K_bf\le\lambda^{b-1} f$ pointwise.

For a word of length $m$, digit sum $B$, sum the product of the nonnegative operators over the initial state. Since $f(c)\ge x^c$, the partition weighted by the sum of all $m+1$ carries is at most $D\lambda^{B-m}$. For the version counting only the first $m$ carries, apply the same proof to the first $m-1$ edges, bounded by the same expression because $b_{m-1}-1\ge0$. This truncation is essential in obtaining the stated global occupation exponent without charging the terminal carry twice.

Choose $x=u^2$, where $u$ is the positive solution in $(0.58,0.59)$ to $u(1+D(u^2)u^2)=1$. The function on the left is strictly increasing there, and this is the root of $u^5+u^3-2u^2-u+1=0$. Then $\lambda=1/u$ and $\log(1/x)=2\log\lambda$. Conditional Gibbs entropy on the actual canonical word gives
$$
 H(K\mid B_{\rm word})\le (2C+2E_{\rm end}+\mathbf E B-m)\log\lambda+\log D.
$$
PR189's fixed-source sliding-window bounds give $2C+\mathbf E B\le\alpha m+O_q(R)$ and $E_{\rm end}=O_q(1)$, with $\alpha=\log_2 3$. The gap word is a function of the canonical word and the carries, so its conditional entropy cost per actual window is at most $(\alpha-1)\log\lambda$, up to the same boundary error. Its normalized coefficient is $0.285859533495646\ldots$. No rationality or finite phase universe is needed for this statement.

For global counting set $m=\lfloor\log_3(X/8)\rfloor$ and $K=\lfloor\log_2 X\rfloor$. When the binary clock $A<K$ the physical endpoint satisfies $q'\le 2\,3^m X/2^A$, and its carry is at most $(2\alpha m-A)/3+O(1)$. If $C$ is now the sum of the first $m$ carries and $B$ the canonical digit sum, the exact telescoping identity $A+k_m=B+2C+k_0$ gives $C\le(A+\alpha m)/3-B/2+O(1)$. The truncated partition therefore bounds the count for any one starting phase by
$$
 O(1)\exp\!\left[\bigl(2(A+\alpha m)/3-m\bigr)\log\lambda\right].
$$
The cancellation of $B$ uses $\log(1/x)=2\log\lambda$. Once the $m$ carries and $A$ are fixed, the telescope recovers $k_m$ and all gaps. The other count is by positive compositions of $A$ into $m$ parts. Each gap word contributes at most $X/2^A$ sources since $A<K$ and its ending odd bit fixes one class modulo $2^{A+1}$.

Writing $a=A/m$, the normalized composition exponent increases up to $a=23/20$ and the weighted exponent decreases thereafter. Their respective values at this split are $0.679755060262293\ldots$ and $0.676765182498803\ldots$. The strict margins absorb $O(\log X)$ clock choices. For $A\ge K$ the endpoint is below $X/2$ via the full affine carry bound. An injection of the forward map restricted to the specified set makes its $m$-fold iterate an injection, enabling the single $F(X/2)$ charge. With at most $L$ phases, iteration gives $F(X)=O(LX^{0.68})$. For a fixed injective orbit with subexponential canonical language the bound also follows, with a constant and threshold depending on that orbit. No proof of such phase complexity for an arbitrary orbit is supplied.

The separately constructed integer tree demonstrates exactly where the high-clock charge fails if one enlarges the count to a full basin.
