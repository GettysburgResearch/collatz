# Rigidity of polynomially decaying infinite digit scores for Collatz parity

Let $p\ge2$ be an integer radix and $D\ge0$ a fixed integer. Let $\mathcal A=\{0,\ldots,p-1\}$ and $\mathcal X=(\mathcal A\cup\{\bot,\top\})^{\mathbb Z}$. The shift is $(Sx)_i=x_{i+1}$. For an observable $g:\mathcal X\to\mathbb R$, write
$$
 \operatorname{var}_r g=\sup\{|g(x)-g(y)|:x_i=y_i\text{ for }|i|\le r\} .
$$
Fix bounded observables $g_0,\ldots,g_D$ with a common decay exponent $P$ satisfying
$$
 \operatorname{var}_r g_j\le C(1+r)^{-P},\qquad P>2+\frac{D(D+3)}2. \tag{1}
$$
The constant and exponent may depend on the proposed ranking function. This includes exponentially decaying dependence on the digits in either direction. The displayed threshold is sufficient; no optimality is asserted.

Represent a positive integer $n$ by $z(n)\in\mathcal X$, with its canonical digits in positions $0,\ldots,L-1$ from least to most significant, $\bot$ to their left, and $\top$ to their right. Let $b$ be any bounded real function of the whole integer. Then
$$
 F(n)=b(n)+\sum_{i=0}^{L-1}\sum_{k=0}^D i^k g_k(S^iz(n)) \tag{2}
$$
has the following rigidity property. If both actual parity branches have finite upper drift allowances above a fixed floor, then $F(n)=\gamma L(n)+O(1)$ for some real $\gamma$. In particular, a lower-bounded function of the form (2) cannot simultaneously satisfy $F(n/2)-F(n)\le a$ at every sufficiently large even $n$ for some finite $a$, and satisfy $F((3n+1)/2)-F(n)\le-\varepsilon$ at every sufficiently large odd $n$ for some $\varepsilon>0$. Without a lower bound, functions satisfying these two drift conditions exist exactly when $a\ge\varepsilon\log 2/\log(3/2)$. The assertion permits true infinite memory; it does not follow from a fixed finite truncation of (2), whose accumulated error can grow like $L^{D+1}$.

## 1. From the actual edges to a full-support maximizing measure

Throughout a degree-$d$ induction let all current observables satisfy a variation bound with exponent $P_d>2$. On the pure digit shift $\mathcal A^{\mathbb Z}$ let $B=g_d$. If $\nu$ is any non-atomic $M_p$-invariant circle probability, denote by $\Lambda_B(\nu)$ the integral of $B$ against the two-sided stationary digit law induced by $\nu$, reversing the leading-digit orientation to match (2). Its cylinder probabilities are the stationary consecutive-digit probabilities of $\nu$. This defines the two-sided law by consistency. A bounded continuous observable on the pure digit shift is uniformly approximable by window functions.

For $U\sim\nu$, $X_L=\lfloor p^L U\rfloor$, fixed integral multiplier $c\ge1$ and offset $q\ge0$, the limit of $L^{-d-1}\mathbb E F(cX_L+q)$ is $\Lambda_B((M_c)_*\nu)/(d+1)$. Indeed approximate each padded observable uniformly within $\delta$ by a radius-$r$ function on $\mathcal X$ (fix an extension of each radius-$r$ block). The total normalized approximation error is $O_{d,c,q}(\delta)$ uniformly for large $L$, and the leading integrals differ by at most $\delta$. Apply Lemma 1 of `../root/DIGIT_POLYNOMIAL_RANKING.md` to this finite observable, then send $\delta$ to zero. Approximation applies to the evaluation limit; it makes no assertion that finite truncations themselves satisfy the ranking inequalities.

The actual even and odd edges now give the same invariant-integral inequalities as Section 2 of that manuscript. For $p$ not a power of two the even edges and the equidistribution theorem yield $\Lambda_B(\mathrm{Leb})\ge\Lambda_B(\mu)$ for every stationary positive finite-order Markov digit law. When $p=2^k$, use the odd identity $T(2x+1)=3x+2$, commute the two circle multipliers $k$ times, and apply equidistribution for $p$ and $3^k$ to get the opposite inequality. Passing the equidistribution limit for $B$ follows from the corresponding finite-window statement by uniform approximation. [Hochman, Theorem 1.1](https://arxiv.org/html/2103.08938v2) · [Wren, paper 98, Lemmas 2–3](https://rstation.ai/problems/collatz/papers/98).

These Markov laws approximate the integral against every stationary law $\lambda$ on the pure digit shift. Fix any block length, mix its stationary block frequencies under $\lambda$ with an arbitrarily small positive uniform fraction, and use the resulting strictly positive circulation as the block law of its associated finite-order Markov chain. All statistics on those blocks converge back to their values under $\lambda$ as the uniform fraction vanishes. Increase the block length and use the uniform approximation of $B$. Reversing time causes no restriction on the class of stationary digit laws. Thus uniform Bernoulli measure maximizes the integral of $B$, or maximizes that of $-B$ in the opposite case.

## 2. Exact cohomology with a controlled modulus of continuity

We give the argument and its variation estimates to keep track of degree reduction. A full-support maximizing measure forcing cohomology to a constant for regular observables is a classical conclusion of ergodic optimization. [Jenkinson, Mauldin and Urbański, *Ergodic optimization for countable alphabet subshifts of finite type*, introductory finite-shift comparison](https://webspace.maths.qmul.ac.uk/o.m.jenkinson/countable24.pdf).

On $\mathcal A^{\mathbb Z}$, write $x^+$ for $x$ with every coordinate $j<0$ replaced by zero. Set
$$
 h_1(x)=\sum_{n\ge0}[B(S^nx)-B(S^nx^+)].
$$
Each summand is $O((n+1)^{-P_d})$ because the two sequences agree at all coordinates $j\ge-n$. If $x,x'$ agree on $[-r,r]$, the differences of their summands for $n\le r/2$ are $O((1+r/2)^{-P_d})$ each, and the remaining sum is $O((1+r)^{1-P_d})$ in absolute value. Hence $h_1$ is bounded with variation $O((1+r)^{1-P_d})$. The function $g=B-h_1+h_1\circ S$ depends only on the one-sided future: expansion gives
$$
 g(x)=B(x^+)+\sum_{n\ge1}\big[B(S^n x^+)-B(S^{n-1}(Sx)^+)\big].
$$
It has the same $O((1+r)^{1-P_d})$ variation on matching one-sided prefixes (use the common fixed past when measuring its variation). Its extremal stationary average $\beta$ is unchanged by this bounded coboundary.

After changing sign if necessary, all stationary integrals of $g$ are at most $\beta$, with equality for uniform Bernoulli measure. On one-sided digit strings define
$$
 u(x)=\sup_{n\ge0,\ w\in\mathcal A^n}\sum_{j=0}^{n-1}[g(S^j(wx))-\beta].
$$
Here $wx$ is concatenation. This supremum is bounded. For a nonempty word $w$ replace $wx$ by the infinite repetition of $w$; at time $j$ they share their first $n-j$ digits. The change of the sum is at most a constant times $\sum_{h\ge1}(1+h)^{1-P_d}<\infty$ since $P_d>2$. The sum on the periodic orbit is nonpositive. The empty word supplies zero. If $x,x'$ share their first $r$ digits, the difference of each candidate sum is $O(\sum_{h\ge1}(r+h)^{1-P_d})=O((1+r)^{2-P_d})$, uniformly in $w,n$. This bound passes to $u$.

Extending any prehistory of $y$ by its first symbol gives $u(Sy)\ge u(y)+g(y)-\beta$. The nonnegative continuous slack has integral zero under the full-support maximizing measure, hence vanishes at every $y$. Undo the first cohomology and any sign change. We have the exact identity on all pure-digit sequences
$$
 B=\beta+h\circ S-h,\qquad \operatorname{var}_r h=O((1+r)^{2-P_d}). \tag{3}
$$
Here $h$ on the two-sided shift is obtained from $u-h_1$, with the sign adjusted when the original measure minimizes $B$. This step is stronger than merely knowing extremality of the Bernoulli average for a continuous observable.

## 3. Both infinite sentinel tails

Write $P_0:\mathcal X\to\mathcal A^{\mathbb Z}$ for the coordinatewise map replacing either sentinel by digit zero, and $R:\mathcal X\to\mathcal X$ for the one replacing only $\bot$ by zero. Both commute with $S$. At every padded sequence split
$$
 g_d(z)=g_d(P_0z)+[g_d(z)-g_d(Rz)]+[g_d(Rz)-g_d(P_0z)]. \tag{4}
$$
At $S^iz(n)$ the middle term is $O((1+i)^{-P_d})$. Its contribution after multiplication by $i^d$ and summation is uniformly bounded whenever $P_d>d+1$.

For the last term, write $t=t(n)$ for the top-to-bottom digit string of the numeral continued by zeros forever, so $t_0\ne0$. Define $\Delta_m(t)$ to be the difference between the two evaluations of $g_d$ at a position $m\ge0$ places below its first digit, with the semi-infinite digits $t$ beneath the upper boundary, and with every position above the upper boundary set respectively to $\top$ and to zero. This agrees exactly with the last difference in (4) at $i=L-1-m$ whenever $m<L$. One has $|\Delta_m|\ll(1+m)^{-P_d}$. For $0\le k\le d$ introduce
$$
 H_k(t)=\sum_{m\ge0}(1+m)^k\Delta_m(t).
$$
The series are uniformly absolutely convergent if $P_d>d+1$. If two leading strings share their first $r$ digits, the summands for $m\le r/2$ change by at most $O((1+m)^k(1+r/2)^{-P_d})$ (enlarging constants for small $r$). For $m>r/2$ use absolute decay. Thus the variation of $H_k$ is $O((1+r)^{k+1-P_d})$.

Expanding the polynomial in $L-1-m$ and extending its sum to $m\ge0$ gives
$$
 \sum_{i<L} i^d[g_d(RS^iz)-g_d(P_0S^iz)]
 =\sum_{k=0}^d {d\choose k}(-1)^k L^{d-k}H_k(t)+O(1). \tag{5}
$$
The omitted tail of the unexpanded polynomial has absolute sum at most $C\sum_{m\ge L}(1+m)^d(1+m)^{-P_d}$, uniformly bounded. This establishes (5) for the canonical zero-continuations without imposing any inequalities on the terminator digits.

Apply (3) to the first term of (4). For $d\ge1$, summation by parts on all positions with $h_i=h(S^iP_0z)$ gives
$$
 \sum_{i<L}i^d(h_{i+1}-h_i)=(L-1)^d h_L-
       \sum_{i=1}^{L-1}[i^d-(i-1)^d]h_i. \tag{6}
$$
The bulk term is an allowed degree-$d-1$ score: composing $h$ with $P_0$ preserves its variation bound, and adding the missing $i=0$ contribution changes a bounded term. The endpoint $h_L$ is a function of the leading digits $t$ with variation $O((1+r)^{2-P_d})$, since the sequence centered just above the top contains zeros to its upper side and $t$ to its lower side.

Equations (5)–(6) give exactly
$$
 F(n)=\beta\sum_{i<L}i^d+L^d H(t(n))+G(n), \tag{7}
$$
where $H$ is continuous on the compact one-sided leading-digit space, and $G$ has the form (2) of degree at most $d-1$ with variation exponent at least $P_d-(d+1)$. To see the class closure explicitly, each remaining top term is a polynomial of degree at most $d-1$ in $L$ times a leading-digit function with this regularity. Store it at $i=L-1$ by multiplying the corresponding leading-digit observable by the indicator that the center is genuine and the next upper coordinate is $\top$. Evaluate its leading digits by reading coordinates $0,-1,-2,\ldots$ with all sentinels replaced by zero, and evaluate the polynomial at $i+1$. Leading-digit functions may be extended to strings with first digit zero by a bounded constant there, a clopen part of the space. This defines a global padded observable of the stated variation. All bounds are uniform in the numeral. The factor $d+1$ covers both the loss of two orders in the bulk cohomology and the loss of $k+1$ orders in (5). The induction maintains $P_d>2+d(d+3)/2$, because subtracting $d+1$ leaves the same strict margin at degree $d-1$. This guarantees $P_d>2$ and $P_d>d+1$ whenever they are used.

## 4. The mantissa, degree descent and the last odd path

Let $v=\log_p(3/2)$ and use the real mantissa coordinate $u=\log_p n-(L-1)$. Except at the countably many nonunique expansion points, the map sending a real mantissa to its leading-digit string is continuous into the symbolic product. The function $H$ composed with this map is bounded and measurable. For almost every $u$ and any prescribed leading depth $r$, choose a fixed open mantissa interval around $p^u$ such that the source and its $3/2$ multiple stay inside their respective first-$r$ leading-digit cells and have a constant length change $m=\lfloor u+v\rfloor$. The fixed additive $1/2$ on the actual odd edge preserves these cells for all sufficiently large lengths upon shrinking the interval away from its endpoints.

For the degree-$d-1$ function $G$, average over the actual odd $n$ in this mantissa interval at length $L$. The normalized expected difference $\mathbb E[G(Tn)-G(n)]/L^d$ tends to zero. Uniformly approximate its finitely many observables by finite-window observables with error $\delta$; the total normalized error is $O_d(\delta)$, while the finite-window progression count of Section 4 of the companion gives $O_{I,r}(L^{-1})$ for each fixed approximation. Take $L\to\infty$ and then $\delta\downarrow0$. The input $n$ and its image both remain actual integers throughout.

Divide the odd drift inequality by $L^d$ in (7), using $\sum_{i<L+m}i^d-\sum_{i<L}i^d=mL^d+O(L^{d-1})$. The possible variation of $H$ on the two leading cells tends to zero when the prescribed depth $r\to\infty$. Consequently
$$
 \beta\lfloor u+v\rfloor+H(t(\{u+v\}))-H(t(u))\le0\quad\text{for almost every }u,
$$
where $t(u)$ is the leading string of $p^u$. Integration gives $\beta v\le0$. On the actual even branch $n=2m\mapsto m$, the same argument uses the constant image stride one, source stride two, and rotation $v_e=-\log_p 2$. Its integrated inequality gives $\beta v_e\le0$. Opposite signs force $\beta=0$ independently of any global lower bound. The inequality is now equality almost everywhere, and the irrational rotation by $v$ makes $H(t(u))$ constant almost everywhere. The pushforward distribution of uniform $u$ under the leading-digit map has full support on the space of strings having a nonzero first digit: every valid finite leading cylinder has an interval of mantissas of positive length. Since $H$ is symbolically continuous, it is the same constant on **all** these strings, including terminating expansions. Its multiple of $L^d$ in (7) is stored as the unweighted sum of the differences $(i+1)^d-i^d$. This reduces the degree without altering $F$.

Starting from (1), the total regularity loss in these positive-degree steps is at most $\sum_{d=1}^D(d+1)=D(D+3)/2$. At each step the available $P_d$ exceeds both $2$ and $d+1$; the final degree-zero exponent still exceeds two. At degree zero the exact coboundary (3) telescopes to a bounded contribution. Both boundary tails in (4) have uniformly bounded sums. Thus $F(n)=\gamma L(n)+O(1)$. The $J$ actual odd departures from $2^J-1$ end at $3^J-1$. The resulting difference divided by $J$ tends to $\gamma\log_p(3/2)$, which must be at most $-\varepsilon$. A lower bound would force $\gamma\ge0$, giving a contradiction. For an arbitrary score, applying the even allowance to the $J$ steps from $2^J z$ to fixed $z$ above the threshold gives $-\gamma\log_p 2\le a$. Combining the two constraints gives the claimed necessary tradeoff. Conversely $F(n)=-c\log n$, where $\varepsilon/\log(3/2)\le c\le a/\log2$, has even increment $c\log2$ and odd increment $-c\log(3/2+1/(2n))\le-\varepsilon$. It is of the form (2) since it differs by a bounded function from $-c(\log p)L$.

This is a written infinite-context extension of `../root/DIGIT_POLYNOMIAL_RANKING.md`. It uses the same classical equidistribution theorem and actual integer progression count, and an explicit bounded-subaction argument to track losses in the modulus of continuity. The three finite cyclic-transport Lean modules in this directory are independent of this argument. No polynomial-time or universal-program ranking obstruction follows merely from the conditions on the digit observables.
