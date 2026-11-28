# Two-sided transport between odd runs

**PROPOSED, written proof.** Two positive shifted heights may each have an odd run spending a macroscopic fraction of its bit length. This note bounds the intervening ordinary trajectory. Its transient word and number of even events are unrestricted. An absolute effective estimate uses the reduced ratio of two odd cofactors. A separate Subspace Theorem estimate permits arbitrary unrelated cofactors with a qualitative onset.

## 1. Shifted affine difference at both endpoints

Use the shortcut map and write $z=x+1$. At an odd input, $z\mapsto3z/2$; at an even input, $z\mapsto(z+1)/2$. Choose two disjoint positive runs of odds on one actual orbit, each ending at the next even input, and starting after an even input or at the initial source. Their starting shifted heights are $2^g q$ and $2^{g'}q'$, with $q,q'$ positive odd and $g,g'\ge1$. Count from the end of the first run, at shifted height $3^gq$, up to the start of the second. This gap contains $s$ odd inputs and $h\ge1$ evens; $r=s+h$ excludes both displayed runs. Affine unrolling gives
$$
 X=2^{r+g'}q'=Y+E,\qquad Y=3^{g+s}q,\qquad
 0<E\le3^s(2^h-1)<3^s2^h. \tag{1}
$$
Indeed the carry starts at zero and evolves to $3E$ on an odd step and $E+2^t$ on an even step at gap time $t$. For fixed totals, exchanging an odd-even pair for an even-odd pair increases the carry by $2^t$ before the common later steps. Thus all evens first maximize it, with carry $3^s(2^h-1)$. Positivity follows from $h\ge1$.

## 2. An effective estimate for every pair, including a shared unbounded cofactor

Put $\gamma=\log_2 3$, $c=\log_2(3/2)$, $H=\max(q,q')/\gcd(q,q')$ and $T=2+r+g+g'$. There is an absolute effective constant $C$ for which
$$
 \boxed{\quad h\ge \log_2(3^g q)-C\log_2(2H)\log_2 T,\qquad
 c s\ge\log_2(2^{g'}q')-C\log_2(2H)\log_2 T.\quad} \tag{2}
$$
For the proof use the nonzero, positive real linear form
$$
 \Lambda=\log(X/Y)=(r+g')\log2-(g+s)\log3+\log(q'/q).
$$
For $q\ne q'$ apply Matveev's Corollary 2.3 to the three positive rationals $2,3,q'/q$ in $\mathbb Q$, with the real logarithms, $D=1$, and the integer coefficients displayed. The general corollary requires nonvanishing; the rational bases may be multiplicatively dependent. Take $A_1=\max(\log2,0.16)$, $A_2=\max(\log3,0.16)$, $A_3=\max(\log H,0.16)$ in (2.4), and $B^*\le T$ in (1.4). The rational logarithmic height of $q'/q$ is $\log H$ and bounds the absolute logarithm. If $q=q'$ omit the third logarithm and use the two-logarithm case. The corollary yields $-\log\Lambda\le C'\log(2H)\log T$. When $0<\Lambda<1$, $E/X=1-e^{-\Lambda}\ge\Lambda/2$; when $\Lambda\ge1$, $E/X\ge1-e^{-1}$. In both cases $\log_2(X/E)\le C\log_2(2H)\log_2 T$. Combining with (1), first using $Y\le X$ and then using $X$ directly, proves both inequalities. [E. M. Matveev, *Izvestiya Mathematics* 64 (2000), Corollary 2.3, equations (1.4), (2.4) and (2.6)](https://doi.org/10.1070/IM2000v064n06ABEH000314).

For a return to the same odd cofactor, $H=1$ even if that cofactor grows across examples. If both starts are Mersenne integers ($q=q'=1$), then
$$
 h\ge\gamma g-O(\log T),\qquad s\ge g'/c-O(\log T).
$$
In particular, reaching a second Mersenne of at least the original bit length requires $r\ge(\gamma+1/c)g-O(\log T)$. Along a family with $g\to\infty$ and $\log T=o(g)$, this forces positive linear costs in both counters. An unrestricted destination need not have small reduced cofactor ratio, and an actual Mersenne need not ever reach a second large Mersenne.

## 3. Qualitative uniform bound at arbitrary cofactor ratio

For a finite set $S$ of primes containing 2 and 3, write $[z]_{S^c}=\prod_{p\notin S}p^{v_p(z)}$ for the part of a positive integer supported outside $S$. For every $\epsilon>0$ there is $c_{S,\epsilon}>0$ such that all positive integers $X>Y$ satisfy
$$
 (X-Y)[X]_{S^c}[Y]_{S^c}\ge c_{S,\epsilon} X^{1-\epsilon}. \tag{3}
$$
No effectiveness claim is needed. For $0<\epsilon<1$, suppose there are arbitrarily large $X$ with the left side less than $X^{1-\epsilon}$. At infinity take the independent forms $X-Y,Y$; at each $p\in S$ take the two coordinates. The product over these places is exactly the left side divided by $X$. Dividing coordinates by $d=\gcd(X,Y)$ multiplies that product by $[d]_{S^c}^{-2}\le1$. The primitive height is at most $X$. The Subspace Theorem puts the primitive pairs in finitely many rational lines. Yet $(X-Y)/X<X^{-\epsilon}$ tends to zero, so $Y/X\to1$ with $Y/X<1$. A finite list of ratios cannot do so. The finitely many remaining small $X$ can be included in the constant. Larger $\epsilon$ follow immediately. This proves (3). [Evertse and Ferretti, *Annals of Mathematics* (2013), rational specialization of the Subspace Theorem](https://doi.org/10.4007/annals.2013.177.2.4).

More generally take any interval of $r$ actual steps containing an even input, with shifted endpoints $z,\tilde z$ and $s$ odd inputs. Then $X=2^r\tilde z$, $Y=3^s z$ have outside parts $[\tilde z]_{S^c},[z]_{S^c}$, and (3) controls their product with their exact positive carry $E=X-Y$. In (1), one may bound the outside parts by $q,q'$. With $B=\log_2(2^g q)$ and $B'=\log_2(2^{g'}q')$, taking logs gives
$$
 g+g'\le B+c s+\epsilon(r+B')+O_{S,\epsilon}(1). \tag{4}
$$
Here the sharp upper bound $\log_2 E<h+\gamma s=r+c s$ from (1) accounts for the term $c s$. Also
$$
 B'\ge B+c g+\gamma s-r,\qquad B'\le \gamma B+c r.
$$
The first inequality follows from $X\ge Y$ and the second from the fact that an odd input multiplies the shifted state by $3/2$ and an even input does not increase it.

Suppose $g\ge\delta B$ and $g'\ge\delta B'$ for some fixed $0<\delta\le1$, along a family with $B\to\infty$. Substituting these bounds in (4) shows
$$
 (2\delta+c\delta^2-1)B
 \le \delta h+c(1-\delta)s+o(B+r). \tag{5}
$$
Precisely, the limit superior of the positive excess divided by $B+r$ is zero: first take the limit for fixed $\epsilon$, then let it tend to zero. If $\delta>1/(1+\sqrt{\gamma})$, the left coefficient is positive and $c(1-\delta)<\delta$. Along any subsequence where $r/B$ stays bounded, (5) gives
$$
 \liminf\frac rB\ \ge\ 2+c\delta-\frac1\delta. \tag{6}
$$
The same statement holds for the full family because the subsequences with unbounded ratio cannot lower a finite limit inferior. In particular, two distinct half-bit odd runs require a gap of at least $(0.292481\ldots-o(1))B$ additional shortcut steps, counted after the first odd run and before the second. The estimates above describe repeated bursts and cofactor transport; trajectories with frequent shorter runs remain possible.
