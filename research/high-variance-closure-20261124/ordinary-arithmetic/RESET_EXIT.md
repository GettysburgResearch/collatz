# Unbounded losses on the last wrapped marked edge

**Status.** Written counterexample for the proposed score `R_*` at base commit `a30402b7849c437edf245974d9f436d1f105e08e`. It works for **every** allowed choice of separated cutoffs in `research/high-variance-closure-20261124/continuation/MULTISCALE_CLOSURE.md` and every positive summable weight sequence for which the clock sum is finite on all positive inputs. Level one alone has unbounded uncompensated refill on genuine nonperiodic ordinary edges. A signed repair below pays every marked loss and quantifies its sacrifice on unmarked steps. Collatz remains open.

Use the shortcut $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. Take the original selector $S$, cutoffs $B_j$, seeds $A_j=S\cap[B_j,\infty)$, wrapped marks $M_l$, first-hit clocks $t_l$, weights $w_l>0$, $W_l=\sum_{k\ge l}w_k$, $G=\sum_lw_lt_l$ and the proper ancestor toll $b_*$ from the cited construction. In particular $B_j\ge2^{j^2}$. The proof uses the cited separation of distinct virtual starts by more than four times the larger level. The small-cycle and unit kills are retained throughout.

## Two facts about ordinary ancestors and the selector

Write $p(x)=\mathbf1_{x\notin M_1}$. At any positive $z$ with unique positive predecessor $x$, splitting incoming paths according to whether they have length zero gives

$$
b_*(z)=\min\{z,b_*(x)+p(x)\}.
$$

For every $x\equiv8\pmod {18}$ with $x\ge26$, $z=x/2\equiv1\pmod3$ has exactly this unique predecessor. The positive odd number $m=(4x-5)/9$ has the two odd steps $m\mapsto(2x-1)/3\mapsto x$. Thus $b_*(x)\le m+2\le x/2$. At any such **marked** $x$ one has the exact equality $b_*(z)=b_*(x)$, independently of the rest of the incoming tree.

The original selector outputs its input at every sufficiently large $s=7\cdot3^a+C$ with $1\le C\le\sqrt{s}$, uniformly over these offsets. To see this, let $t$ be the deepest window containing $s$ at clock zero, within the selector's depth limit. For large $s$, this is the largest nonnegative integer satisfying $C<3^{a-t}$. It is below the limit $D=\lfloor\log_2 s\rfloor$, since $C\ge1$ and $a<D$. Maximality gives $3^{-t}\le3C/3^a=O(s^{-1/2})$, so all points in $W_t$ are within $O(s^{-1/2})$ of the anchor in circular phase. If a second actual state $T^k s$ were in $W_t$ for $1\le k\le H(s)\le\sqrt{\log_2 s}$, then

$$
\|k\log_3 2\|\le O(s^{-1/2})+ O(H(s)2^{H(s)}/s).
$$

Here the second term sums the actual phase errors at odd clocks, each at a state at least $s/2^{H(s)}$. On the other hand, for integer $r$ nearest $k\log_3 2$, the different integers $2^k,3^r$ are at most $2\cdot2^k$. The mean-value estimate for the logarithm gives $\|k\log_3 2\|\ge (2\log3)^{-1}2^{-k}$. This is larger than the displayed upper bound uniformly over those $k$ once $s$ is large. Thus clock zero wins, even when deeper windows at other clocks are allowed. In particular $s\in S$. No equidistribution rate is required.

## Clean intervals for every allowed bank

Define $C_j^{\rm cut}=\min_{k\ge j} B_k/3^k$ and $D_j=\log C_j^{\rm cut}$. The minimum exists, and $D_j\ge j^2\log 2-j\log 3$ for large $j$. Fix $0<c<\log(4/3)$. Infinitely many $j$ satisfy $D_{j+1}-D_j>(\log3+c)j$. Otherwise summing the opposite bound eventually gives $D_j\le(\log3+c)j^2/2+O(j)$, contradicting the lower bound. At these indices $C_j^{\rm cut}=B_j/3^j$ since the minimum strictly increases, whence

$$
C_{j+1}^{\rm cut}>B_j e^{cj}.
$$

In particular an interval with large multiplicative width is available even when the prescribed cutoffs sometimes bunch together. For each sufficiently large such $j$, take the least $a\ge0$ for which $A=7\cdot3^a\ge B_j$, so $B_j\le A<3B_j$. Choose $2j\le d\le2j+5$ such that $r=d-j+1\equiv1\pmod6$. Let $C$ be the least strictly positive residue satisfying $A+C\equiv 13\cdot2^d\pmod{18\cdot2^d}$, and put

$$
s=A+C=2^d u,\qquad s'=3s+2^d=2^d(3u+1).
$$

Here $u\equiv13\pmod {18}$, and $s'=7\cdot3^{a+1}+(3C+2^d)$. Both positive offsets are at most $55\cdot2^d\le \sqrt{B_j}$ eventually. Both seeds lie in $[B_j,10B_j)$, with their values plus one strictly less than $C_{j+1}^{\rm cut}$ eventually. The selector result marks both seeds at clock zero, giving level $j$ starts on both actual trajectories.

The first $d$ clocks of both are even, their states at clock $d$ are $u$ and $3u+1$, and their clock $d+1$ endpoints coincide. The two clock-$d$ states are distinct. A deterministic map sends distinct periodic states to distinct states, since its restriction to any finite union of cycles is a permutation. Consequently at least one of these two clock-$d$ states is nonperiodic. Every state in its actual trajectory from clock zero through $d$ is then nonperiodic. This holds regardless of whether the common endpoint is itself on a cycle.

## Exact level-one exits

Choose the branch from the preceding paragraph and denote its trajectory $X_i$, with seed $q=X_0\in\{s,s'\}$. Extend it to negative indices by $X_{-k}=2^k q$. Any witness $X_i=T^e(v)$ from an ordinary seed $v\in A_h$ with $0\le e\le h-l$ at level $l\ge1$ gives a virtual start at $t=i-e$ of level $h$. The separation theorem applies on this extended path by shifting to a starting time at or before $0,t$. In particular it includes witnesses on different incoming branches, and requires no uniqueness of a seed.

For $0\le i\le2j$ one has $|i-e|\le\max(2j,h)$. Comparison with the given level $j$ start at zero forces $t=0$. In that case $T^e(v)=T^e(q)$, so

$$
 B_h\le v\le 2^e T^e(q)\le 3^e(q+1)\le3^h(q+1).
$$

As $q+1<C_{j+1}^{\rm cut}$, necessarily $h\le j$. Also $e=i$, giving $l\le h-i\le j-i$. Conversely the seed $q\in A_j$ itself witnesses level $j-i$ at every $0\le i<j$. With $J(x)=\max(\{l:x\in M_l\}\cup\{0\})$, this proves precisely

$$
J(X_i)=j-i\quad(0\le i<j),\qquad J(X_i)=0\quad(j\le i\le2j).
$$

Now put $x=X_{j-1}$. On either candidate branch $x$ is respectively $2^r u$ or $2^r(3u+1)$, even and congruent to $2\cdot4=8\pmod9$. Thus $x\equiv8\pmod {18}$ and $b_*(x)=b_*(Tx)$. The selected branch has no periodic state through $2j\le d$. There is no mark, unit or finite-cycle kill on $X_j,\ldots,X_{2j}$, so $t_1(Tx)\ge j+1$. The **exact** nonperiodic debit gives

$$
 R_*(x)-R_*(Tx)=4\bigl(W_2-w_1 t_1(Tx)\bigr)
 \le4W_2-4w_1(j+1)\longrightarrow-\infty.
$$

Thus the proposed finite proper score has unbounded one-edge **increases** at the same level on arbitrarily large ordinary inputs. The comparison uses one genuinely nonperiodic branch at each $j$, without deciding which branch by solving its eventual fate. Different $j$'s give different large witnesses. No single divergent trajectory is constructed.

The conclusion extends to every finite signed ancestor price $b_c(z)=\inf_{T^k(m)=z}(m+\sum_{i<k}c(T^im))$ with $|c|\le K$, assuming the infimum is finite at the tested nodes. Splitting at the unique incoming edge gives the same Bellman equality with $c(x)$ in place of $p(x)$, even if the infimum is unattained. Since $b_c(x)+c(x)\le (4x-5)/9+3K < x/2$ eventually, $b_c(x)-b_c(Tx)=-c(x)$ stays bounded. Any fixed finite scalar multiple of such a toll fails to pay the displayed level-one losses. This extension concerns the stated linear ancestor starting price and bounded edge charges.

## An unbounded signed price that pays every refill

Bounded signed charges fail on the preceding examples. It pays the full actual refill on **every** marked edge and quantifies the leftover cost on unmarked edges. The resulting proper total score still has genuine increasing unmarked edges.

Let $D(x)=K+\log(x+1)$ with a sufficiently large fixed $K>e$, and set $v(x)=1/(D(x)\log D(x))$. Define the signed residual $c(x)=v(x)(1-3\mathbf1_{M_1}(x))$. Uniformly on every ordinary finite path $X_i=T^i(m)$ there is an absolute effective $C_0$ with

$$
 \sum_{i<k}c(X_i)\ \ge\ \tfrac1{10}\sum_{i<k}v(X_i)-C_0. \tag{1}
$$

For the proof, extend the trajectory to negative times by doubling. At each virtual start $t$ let $h$ be the maximal level of any of its records. This maximum exists because $X_t+1\ge B_h/3^h$, so $h\le C(1+\sqrt{\log(X_t+1)})$ for an absolute effective $C$. All its marked observations lie in $[t,t+h)$. Assign the longer interval $[t,t+4h)$ to this start. These assigned intervals are disjoint by separation. On one interval the logarithmic height changes from its initial value by at most $4h\log 2$, in either direction. By choosing $K$ large once and for all, the ratio of the largest to the smallest $v$ on every such interval is at most $6/5$. Indeed the relative change of $D$ is at most $4C\log 2(1+\sqrt{x})/(K+x)$ with $x=\log(X_t+1)$, uniformly tending to zero as $K\to\infty$. The logarithm in the extra factor of $v$ also has relative variation tending uniformly to zero. Thus the marked sites carry at most $3/10$ of the $v$-mass on a complete assigned interval. The sum of $c=v-3v\mathbf1_{M_1}$ there is at least one tenth of its $v$-mass. Outside assigned intervals every site is unmarked. At most two cut intervals touch the ends of a finite segment. Each has uniformly bounded entire $v$-mass, since it is at most $4h(6/5)v(X_t)$. This proves formula (1), including for segments that start inside a block witnessed on a different predecessor branch.

Define an infimum over literal finite ordinary paths by

$$
 R^{\dagger}(n)=\inf_{T^k(m)=n}\left[m+4G(m)+\sum_{i<k}c(T^im)\right],
 \qquad \beta(n)=R^{\dagger}(n)-4G(n).
$$

Here $G\ge0$ is finite as hypothesized. The empty path gives a finite upper bound. By formula (1) every candidate is at least $m-C_0+\frac1{10}\sum v$. For each $m$, the sum of $v(T^im)$ diverges, because $D(T^im)\le D(m)+i\log(3/2)$ and the series with terms $1/[(a+bi)\log(a+bi)]$ diverges. Thus a fixed upper cost cuts down both $m$ and $k$ to finite sets, and $R^{\dagger}$ is finite, bounded below and proper. These bounds give effective search ranges. When $G$ is computable with the canonical weights, the finite minimum of computable reals is computable without deciding ties. Adding one fixed constant would make the total score nonnegative.

Telescoping $4G$ shows that $\beta$ is exactly the signed ancestor price with starting price $m$ and edge charge $4(G(x)-G(Tx))+c(x)$. In particular those charges include the actual, possibly unbounded, negative reset term. Extending one path gives the unconditional inequalities

$$
 R^{\dagger}(n)-R^{\dagger}(Tn)\ge
 \begin{cases}
 2v(n), & n\in M_1,\\
 -v(n), & n\notin M_1.
 \end{cases}
$$

This includes periodic sources. The proof uses no upper bound substituted for an exact nonperiodic debit. On each marked edge $\beta(n)-\beta(Tn)\ge 4(G(Tn)-G(n))+2v(n)$. It pays the entire refill, including the unbounded examples above. On unmarked edges the allowed loss $v(n)=o(1/\log n)$ is smaller than the preceding physical target. Its sum still diverges on every infinite positive path. The properness statement concerns $R^{\dagger}$. Separate properness of $\beta$ is not required for it.

For the canonical clocks satisfying $G(n)=O(1+\sqrt{\log(n+1)})$, increasing unmarked edges actually occur. On the same increasing sequence of clean indices take $x=X_{j+5}$ with $j\ge6$. This is an unmarked even source still congruent to $8\pmod {18}$, since six more halvings after $X_{j-1}$ preserve the displayed residue at the new source. Let $z=x/2$. The unique-parent recurrence now reads $R^{\dagger}(z)=\min\{z+4G(z), R^{\dagger}(x)+c(x)\}$. For $m=(4x-5)/9$ its two-odd-step path gives $R^{\dagger}(x)+c(x)\le m+4G(m)+3\sup v<z$ for large $x$. The signed residual is positive on this unmarked edge. Hence $R^{\dagger}(Tx)-R^{\dagger}(x)=v(x)>0$ exactly. The signed construction shifts the loss to a smaller size and a different set of dates, and supplies no all-orbit descent or exclusion of a nonstandard cycle.

**Evidence.** `lean/ResetAncestor.lean` formalizes the ancestor Bellman identity, the equal-toll congruence, the delayed collision and the nonperiodic branch disjunction. The selector self-return, clean-tail argument, virtual-start transfer, unbounded refill and signed repair are written proofs. `checks/reset_exit_control.py` tests exact selector outputs and collision arithmetic for six synthetic source-size parameters. It does not instantiate the full wrapped bank.
