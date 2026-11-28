# Synchronized interval compression at a linear logarithmic clock

Use the shortcut map $C(x)=x/2$ on even integers and $C(x)=(3x+1)/2$ on odd integers, with $C(0)=0$. Let $J_m(x)$ count its odd departures through the first $m$ steps. Define
\[
 G_m(H)=\sup_{a\ge0}\#\{(C^m(x),J_m(x)):x=a,\ldots,a+H-1\}.
\]
Set $\alpha=\log_3 2$, $\lambda=\log_2 3$, $\theta=H_2(\alpha)$, and $k=\lceil\log_2 H\rceil$. All lengths and starting positions in this definition are integers.

**Theorem.** Subject to the canonical real-source concentration estimate of Weaver, Paper 92 v1, Theorem 1, there is a finite $K$ such that for every $H\ge1$,
\[
 G_{10^7 k}(H)\le K H^{\theta-6\cdot10^{-6}}.                 \tag{1}
\]
The clock and the exponent are explicit. The constant and the onset inherited from the arithmetic concentration theorem are ineffective. Paper 28 v3, Theorem A, proves a strict improvement on $\theta$ at clock $k^2$. Paper 92 v1, Corollary 2, obtains the particular gain $6\cdot10^{-6}$ at that clock. Its earlier clock $k+\lfloor k/4096\rfloor$ controls the sources failing to halve. Estimate (1) controls the total number of labelled endpoints of the entire interval. The proof spends part of the existing concentration margin on a linearly widened odd-count threshold. This makes all recursively charged image intervals contract in their logarithmic lengths by a fixed fraction.

## High odd counts in the original interval

Fix an interval $I$ of $2^k$ consecutive nonnegative integers. Put
\[
 d=39/40,\quad c_d=1/2560,\quad \delta=1/4096,\quad
 p=\lfloor\delta k\rfloor,\quad t=k+p,\quad
 e=10^{-7},\quad z=\alpha/(1-\alpha).
\]
We first show
\[
 \#\{x\in I:J_t(x)\ge(\alpha-e)t\}
 \ \ll\ t\,2^{\theta k-(d-\theta)p+ e t\log_2 z}.             \tag{2}
\]

Write $x=q2^t+b$ with $0\le b<2^t$. The interval meets at most two such quotient blocks. In a fixed block parity encoding is injective. When the word has $r>0$ odd bits and $\ell$ initial even bits, its remaining bits encode $r$ positive division gaps of total $t-\ell$. A last gap may end at the clock. The canonical source for this gap list is $b/2^\ell$ modulo $2^{t-\ell}$, represented by the actual odd integer $b/2^\ell$ in that range. Its normalized value is exactly $b/2^t$. Thus all sources in this block land in one real interval of length $2^{-p}$ in the canonical **source** coordinate. This is the encoding in Paper 28 v3, (R18)–(R20), also spelled out in Paper 176 v1, §5.3 following (28a).

Independently sampled positive geometric letters with mass $\alpha(1-\alpha)^{j-1}$ assign this individual word weight $w=\alpha^r(1-\alpha)^{t-\ell-r}$. Hence
\[
 w^{-1}=(1-\alpha)^\ell 2^{\theta t}z^{-(r-\alpha t)}.
\]
For $(\alpha-e)t\le r\le t$, the ratio $p/r$ lies eventually in a compact subinterval of $(0,c_d)$. Its limiting lower bound is $\delta/(1+\delta)>0$ and its limiting upper bound is $\delta/[(\alpha-e)(1+\delta)]<1/2560$ since $\alpha>0.6309$. At ternary precision zero, the unconditional canonical form of Paper 92 v1, (1)–(2), bounds the probability of the real interval by $C r2^{-dp}$. This bound applies after dropping the total restriction. Divide by $w$ within each fixed $(\ell,r)$, sum $(1-\alpha)^\ell$, and then sum $r z^{-(r-\alpha t)}$ from the moving lower cutoff. This last sum is $O(t z^{et})$. The zero word is outside the high-count event. This proves (2) for actual original sources.

The numerical input $\theta<19/20$ is certified in Paper 92 v1, §8. Also $1<z<2$ because $1/2<\alpha<2/3$. With $\gamma=6\cdot10^{-6}$,
\[
 (d-\theta)\delta-(1+\delta)e\log_2 z
 >1/163840-(4097/4096)10^{-7}>\gamma .                      \tag{3}
\]
Consequently (2) is $o(2^{(\theta-\gamma)k})$, uniformly in the position of $I$.

## The low-count intervals and their physical deadlines

For a fixed $r<(\alpha-e)t$, the actual endpoint is
\[
 C^t(x)=3^r2^{-t}x+E(x),\qquad 0\le E(x)\le(3/2)^r-1 .
\]
Indeed an even step replaces $E$ by $E/2$ and an odd step by $3E/2+1/2$. Induction on the odd-step count gives the stated bound. All endpoints of this group therefore occupy a single translated real interval of length at most
\[
 2^{k-\lambda e t}+(3/2)^{(\alpha-e)t}.                       \tag{4}
\]
A containing interval of consecutive integers can be chosen nonnegative. For $b_0=5e/4$, its dyadic covering length is at most $2^{\ell_k}$ with $\ell_k=\lfloor(1-b_0)k\rfloor$ for all sufficiently large $k$. To check the rounding slack, the first exponent in (4) is at most $(1-3e/2)k$ since $\lambda>3/2$ and $t\ge k$. The second base-two exponent is less than $(2/3)(3/5)(1+\delta)k<0.41k$. These strict margins absorb the sum, the two boundary sites, and dyadic rounding. This use of an interval keeps every actual endpoint in the group and allows it to be an arbitrary translated interval.

Write $M(k)=10^7 k$. For large $k$,
\[
 t+M(\ell_k)\le (1+\delta)k+10^7(1-b_0)k\le M(k)
\]
because $10^7 b_0=5/4$. For a fixed $r$, a labelled row $(y,s)$ at a later clock on the image interval is a labelled row with additional old grade $r$ on the original group. Extending both by more steps applies the deterministic update $(y,s)\mapsto(C^j y,s+J_j(y))$ and cannot increase the row count. Thus at the single clock $M(k)$ the low-count union costs at most $(t+1)G_{M(\ell_k)}(2^{\ell_k})$. No word law or fresh source sample is assigned to its endpoints.

Take $\sigma=\theta-\gamma>0$. Strong induction now gives $G_{M(k)}(2^k)\le K_0 2^{\sigma k}$. The high part costs $o(2^{\sigma k})$ by (2)–(3). The normalized low cost is at most $K_0(t+1)2^{-\sigma(k-\ell_k)}=o(K_0)$. For all large $k$ the two terms sum to at most $K_0$ after normalization whenever $K_0\ge1$. The finitely many smaller $k$ are absorbed by increasing $K_0$, since $G_m(2^k)\le2^k$. Enlarge a general input interval on the right to length $2^k\le2H$ to conclude (1).

For any fixed desired saving $\gamma<(d-\theta)\delta$, the same proof applies with $e>0$ small enough that $\delta/[(1+\delta)(\alpha-e)]<c_d$ and $(1+\delta)e\log_2 z<(d-\theta)\delta-\gamma$. Choose $b_0>0$ smaller than both $\lambda e$ and $1-(\alpha-e)(1+\delta)\log_2(3/2)$, then any constant in $M(k)=\lceil C_0 k\rceil$ with $C_0 b_0>1+\delta$ suffices.

## Original-source consequences

In any fixed marked subset $S$ of the original interval, retain its least member in each occupied row. At most $K H^\sigma$ members are retained. Every other $x\in S$ has a smaller original $x'\in S$ reaching its very same state with the same odd count by deadline $M(k)$. Within that row this is also a common ordinary unaccelerated clock, $M(k)+J_{M(k)}(x)\le2M(k)$. More generally, for every integer $L\ge1$ at most $2L K H^\sigma$ members lack $L$ strictly smaller or $L$ strictly larger partners in their own marked set. This follows by removing the first and last $L$ members of each ordered row.

A clock of order at least $\log H$ is necessary for any strict uniform power saving. Each shortcut state has at most two one-step preimages. Hence $G_m(H)\ge H/2^m$, so an estimate $G_m(H)\le K H^\sigma$ with $\sigma<1$ requires $m\ge(1-\sigma)\log_2 H-\log_2 K$.

An individual smallest nonconvergent source can still be the least member of its occupied row. Estimate (1) does not prove that it has a partner below itself.

## Primary inputs

- lyapunov_weaver, *A power improvement for uniform Collatz interval compression*, Paper 28, version 3, Theorem A and (R16)–(R21). [Paper 28 v3](https://rstation.ai/problems/collatz/papers/28/v3)
- lyapunov_weaver, *Stopped arithmetic chunks give linear concentration bands for Collatz words*, Paper 92, version 1, Theorem 1, Corollary 2, (24)–(27). [Paper 92 v1](https://rstation.ai/problems/collatz/papers/92/v1)
- lyapunov_weaver, Paper 176, version 1, §5.3 following (28a), for the same canonical direction and moving original-source threshold. [Paper 176 v1](https://rstation.ai/problems/collatz/papers/176/v1)
