# A power-saving exceptional set for the sharp pressure scale

**FS-016/017: PROPOSED, pending independent review.** This quantitative
argument uses the shortcut map $T$, ordinary finite parity cylinders,
and deterministic first returns to a height interval. No external
predecessor-density theorem is used. It counts exceptional *targets*.
The individual first returns may receive many sources.

## FS-016. All comparable first hits use a short clock off a power-sparse set

For all sufficiently large $X$, all but $O(X^{1-1/20000})$ integers
$t\in[X,2X]$ have the following simultaneous property. For every positive
$x\le X^{1+1/10000}$ that reaches $t$, its first visit to $t$ is within
$M=\lfloor(\log_2 X)/2\rfloor$ shortcut steps. Neither $x$ nor $t$ is
required to be odd in this claim.

Write $h=\log_2 X$ and put

$$
 B=X^{1-1/10000},\quad W=X^{1+1/10000},\quad
 Y=X^{1+1/100},\quad K=\lfloor9h/1000\rfloor .
$$

For $V\ge B$, let $\mathcal S_j(B,V)$ consist of positive integer
$u\le V$ with $T^i(u)\ge B$ for all $0\le i\le j$. If
$\log_2(V/B)\le j/25$ and $X$ is large enough that
$\log_2(3+1/B)<8/5$, these starters must have at least $3j/5$ odd bits.
Indeed $B\le T^j(u)\le V(3+1/B)^q/2^j$. The parity bijection and the
fair-binomial Hoeffding bound give

$$
 |\mathcal S_j(B,V)|\le(V+2^j)\exp(-j/50).
$$

Apply this first at $(j,V)=(M,Y)$ and then at $(K,W)$.
Here $\log_2(Y/B)=0.0101h$, $\log_2(W/B)=0.0002h$,
$M\ge0.49h$, and $K\ge0.0089h$ eventually, so both conditions hold.
Also $2^M\le Y$ and $2^K\le W$.

Take a path from $x\le W$ to a shell target $t$ with first-hit clock
$\ell>M$. If it visits a state below $B$, take its *last* such state.
The next state $u$ is at most $2B$ by $T(n)\le2n$. If the path reaches
$t$ from $u$ in at most $M$ steps, there are $O(B(M+1))$ possible
targets in this case: enumerate the possible $u$ and their first $M+1$
positions. Otherwise start the remaining long segment at $u$. When
there was no low visit, start at $u=x$. Thus we have a segment of length
$l>M$ starting at $u\le W$, staying at least $B$, and ending at $t$.

Look exactly $M$ clocks before the end, at $w=T^{l-M}(u)$. If $w\le Y$,
then $w\in\mathcal S_M(B,Y)$, and $t=T^M(w)$ is a single determined
endpoint. If $w>Y$, take the last state $v\le2X$ between $u$ and $w$,
or take $v=u$ if none exists. Then $v\le W$. From $v$ the orbit
reaches above $Y$ before its next visit to $[1,2X]$ (if $v>2X$, before
its first such visit). This upwards crossing takes more than $K$ steps
because $2^K W<Y$. In particular $v\in\mathcal S_K(B,W)$. Define the
reentry associated to $v$ to be its first state at most $2X$ after
first crossing above $Y$. This depends only on $v$, and for the path
being counted occurs after $w$, within the final $M$ steps. So $v$
can account for at most $M+1$ possible $t$, its reentry and the next
$M$ forward positions. This count handles arbitrarily many earlier
excursions.

The total exceptional count is at most

$$
 O(B(M+1))+|\mathcal S_M(B,Y)|+(M+1)|\mathcal S_K(B,W)|.
$$

Using $\log 2<0.7$, the exponents of $X$ in the two survivor terms
before the logarithmic factor are at most
$1.01-0.49/(50\cdot0.7)$ and
$1.0001-0.0089/(50\cdot0.7)$. Both are strictly below $1-0.0001$.
The low-exit term is $O(X^{1-0.0001}\log X)$.
This proves FS-016 with the stated reserve.

## FS-017. First-hit pressure in the good target population

Use the odd first-hit pressure $H_2$ and $F=H_2/t^2$ of
[FS-014](PRESSURE_LAW.md). For any fixed $\delta>0$,

$$
 \#\{t\in[X,2X]\ {\rm odd}: F(t)>t^{-2+\delta}\}
   =O_\delta\!\left(X^{1-\min(1/20000,\delta/2)}\right).
$$

To see this, discard the exceptional targets in FS-016. Every first-hit
source $x\le W$ of a remaining odd $t$ is accounted for by some
valuation word of total $A\le M$; first hitting an odd target from an
odd source costs exactly $A$ shortcut steps. Enlarge the sum to *all*
legal words with at most $M$ odd letters, including the empty word.
Each length-$q$ word is legal on one ternary residue class modulo $3^q$.
Since $3^M=X^{(\log_2 3)/2+o(1)}<X$, this class occurs at most $3X/3^q$
times in the shell (dropping the odd restriction only enlarges the
count). For each $q$ the sum of squared derivative weights times
$3^{-q}$ over **all** words is exactly one:

$$
 \sum_{a_1,\ldots,a_q\ge1}3^{-q}
        \left(3^q/2^{a_1+\cdots+a_q}\right)^2=1 .
$$

Thus the sum of the near-source pressures over good odd targets is
at most $3X(M+1)$. For a source $x>W$, take the first odd state
$y\le2X$ on its trajectory if one exists. Every good shell target this
source visits is reached from that $y\le W$ in at most $M$ shortcut
steps. There are at most $M+1$ such targets per source. Since each
first-hit derivative obeys $J_0(x,t)\le t/x$, the sum of far-source
pressures on good targets is at most
$4X^2(M+1)\sum_{x>W}x^{-2}=O(X^{1-1/10000}\log X)$.
Consequently the full $H_2$ sum on the retained targets is
$O(X\log X)$. Markov's inequality and the discarded count give the
claim. This estimates the population off the bad set and does not
bound its untruncated contribution to the full mean.

## Fixed-component boundary

On a hypothetical escaping component, any fixed odd $b$ and its later
odd target $t_j$ satisfy $B_b\subseteq B_{t_j}$. The source-qualified
positive-density theorem would give $\#(B_{t_j}\cap[1,t_j])\ge c_b t_j$
with a constant and cutoff uniform in $j$. This follows from inclusion
of the *same* basin, independently of the individual constants for
the $t_j$. Thus a pointwise sublinear cap on comparable ancestors of
every large target would exclude such escape. FS-016 does not give one.
Its high-excursion estimate counts a reentry once even if a positive
density of initial sources funnels into that single reentry. A thin
sequence of such targets is compatible with the exceptional-count bound.
