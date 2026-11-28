# A maximum over rational approximants for ordinary Collatz descent

**PROPOSED, written proof.** Throughout, $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. A time counts one application of this shortcut map. The uniform estimate in Section 4 is open.

## 1. An inequality equivalent to reaching 1

Let $s_k(x)$ count odd inputs at times $0,\ldots,k-1$, including $s_0=0$. Set $M_k(x)=(17/32)^k3^{s_k(x)}$ and $W(x)=\sup_{k\ge0}M_k(x)$. The factor $17/16$ introduces a margin into the usual linear multiplier.

**Proposition 1.** For each positive integer $n$, $W(n)<\infty$ if and only if the orbit of $n$ reaches 1.

After the first visit to 1, every two steps multiply $M_k$ by $3(17/32)^2=867/1024<1$. Conversely, suppose the orbit stays at least 7. Its odd steps introduce the affine correction $1+1/(3T^j n)\le22/21$. An even step has correction one. This gives

$$
  7\le T^k(n)\le n(352/357)^k M_k(n).
$$

A bounded $M_k$ is impossible. Each member of $\{1,\ldots,6\}$ reaches 1 by direct iteration, completing the proof.

Under Haar probability on the 2-adic integers, the parity symbols are independent fair bits. At depth $k$, this follows by induction because adding $2^k$ to the start preserves the first $k$ symbols and adds the odd integer $3^{s_k}$ to the $k$-th state. Thus $M_k^{1/2}$ is a nonnegative supermartingale, because

$$
 \sqrt{17/32}(1+\sqrt3)/2<1.
$$

Squaring and simplifying gives $34\sqrt3<60$. Stopping at the first crossing up to time $K$ and letting $K$ increase yields $\Pr(W\ge A)\le A^{-1/2}$ for $A>1$, using a limit from below if the supremum is approached without attainment. This probability estimate concerns random 2-adic starts. Proposition 1 concerns each ordinary integer.

## 2. The rational approximants

For a finite parity word $w$, prepend it to an infinite string of ones. Its unique 2-adic initial value $r_w$ is obtained by taking the inverse branches $z\mapsto2z$ and $z\mapsto(2z-1)/3$ in reverse time from $-1$. Both give the required parities over the 2-adics. Each $r_w$ is a negative rational of odd denominator. Appending a one to $w$ leaves $r_w$ unchanged.

Write $e=E(w)$ for the number of zeros. For $0\le j<e$, let $u_j$ count the ones preceding the $(j+1)$-st zero, so $0\le u_0\le\cdots\le u_{e-1}$. Under the change $z\mapsto -z-1$, the inverse branches become $v\mapsto 2v+1$ and $v\mapsto(2/3)v$. Expanding their composition gives

$$
 -r_w=1+\sum_{j=0}^{e-1}2^j(2/3)^{u_j}, \qquad 1\le -r_w\le2^e.
$$

Every such tuple occurs, including the empty tuple at $e=0$.

Set $a=\log_2(51/32)>0$, $b=\log_2 3$. For $x\in\mathbb Z_2$ put $v_2(0)=+\infty$.

**Proposition 2.** The following identity holds in the extended real numbers.

$$
 \log_2 W(x)=\sup_{w}\{a\,v_2(x-r_w)-b E(w)\}.
$$

Two distinct initial values have identical parity words for exactly $v_2$ of their difference many steps. This follows by multiplying their difference by $1/2$ or $3/2$ at each shared branch. Let $\ell=v_2(x-r_w)<\infty$. At most $E(w)$ zeros occur in those $\ell$ shared symbols. Therefore $a\ell-bE(w)\le\log_2 M_\ell(x)$. Conversely, the actual length-$k$ word of $x$ gives $\ell\ge k$ with $E(w)=k-s_k(x)$. If $x=r_w$, the eventual all-ones orbit gives both sides $+\infty$. These arguments include $k=0$ and the empty word.

## 3. Unique maximizer at each arity

Fix a positive integer $n$. For an $e$-tuple define

$$
 C_e(u)= n+1+\sum_{j<e} 2^j(2/3)^{u_j},\qquad
 D_e(n)=\max_u v_2(C_e(u)).
$$

Start with $C_0=n+1$. Recursively set

$$
 u_e=v_2(C_e)-e,\qquad C_{e+1}=C_e+2^e(2/3)^{u_e}.
$$

**Proposition 3.** The recursion exists for every $e$, generates nonnegative nondecreasing $u_e$, and yields the unique maximizing tuple at each arity. Moreover $D_e=e+u_e$.

The new summand has the same 2-adic valuation as $C_e$ and odd denominator. The next valuation rises by at least one. This proves the monotonicity and positivity assertions by induction. For a competing tuple, take the first index $j$ at which it differs. The partial sum then has valuation equal to the smaller of $j+u_j$ and the competing $j+u'_j$. All later contributions have larger valuation than that smaller value. The final competing valuation is at most $j+u_j$, strictly below that of the greedy $e$-tuple. Positivity of the real summands excludes vanishing $C_e$.

The bound $C_{e+1}\le n+2^{e+1}$ and its common denominator $3^{u_e}$ give an a priori estimate valid for all arities,

$$
 u_{e+1}\le (\log_2 3)\,u_e+\log_2(1+n/2^{e+1}).
$$

In particular finite arity admits an effective bound without an initial exponent cutoff.

The quantity $D_e$ is the time index of the $(e+1)$-st even input of the actual shortcut orbit of $n$, starting the clock at zero. Indeed the word ending in the $e$-th zero has length $e+u_{e-1}$ when $e>0$. Its length is at most $D_e=e+u_e$. Thus the common prefix of length $D_e$ has exactly $e$ zeros. Its next symbol is an even input of $n$, the first disagreement with the rational approximant. The case $e=0$ follows from $D_0=v_2(n+1)$.

## 4. The remaining arithmetic inequality

The propositions yield the pointwise equivalence

$$
 n\text{ reaches }1
 \quad\Longleftrightarrow\quad
 \sup_{e\ge0}\{aD_e(n)-be\}<\infty.
$$

For each positive integer $n$ one needs $D_e(n)\le (b/a)e+O_n(1)$ uniformly in the number of summands. Here $b/a$ is approximately $2.36$. The unique maximizing tuples and the elementary recurrence restrict every arity, but the recurrence permits exponential growth. Fixed-dimensional estimates for sums of units and Haar-almost-everywhere finiteness leave this pointwise estimate open.

The [fixed-arity theorem](SPARSE_APPROXIMATION.md) gives subexponential depth at every fixed source, and the [post-burst result](MERSENNE_POST_BURST.md) treats a growing number of even events for long initial runs. The [ranking analysis](RANKING_OBSTRUCTIONS.md) treats the replacement of the infinite maximum by finitely many local observations and by a summable series of valuations. The [literature map](PRIMARY_SOURCES.md) records the hypotheses of related results.
