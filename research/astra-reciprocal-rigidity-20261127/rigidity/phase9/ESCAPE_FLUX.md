# The logarithmic defect budget counts escaping components

Use the ordinary shortcut map on positive integers, with slopes $a(n)=1/2$ on even inputs and $a(n)=3/2$ on odd inputs. For a computable rational-valued function $0<u(n)\le1$, define
\[
 d_u(n)=\max\{0,\log(a(n)^2 u(n)/u(Tn))\},\qquad
 D_u(X)=\sum_{1\le n\le X}d_u(n).
\]
All logarithms in these quantities are natural. An escaping component is an equivalence class of escaping starts under eventual intersection of their forward orbits. This agrees with the weak component of the ordinary directed functional graph. The relation of eventual intersection is transitive and contains every individual edge. Conversely, forward intersection connects the two sources by a finite undirected path. A positive orbit either repeats and is bounded or is simple and tends to infinity, because every finite interval contains finitely many positive integers.

**Variational identity.** Let $c\in\{0,1,2,\ldots,\infty\}$ be the number of escaping components. Let $\mathcal U$ be the class of the above computable positive rational functions such that $d_u(n)\le 2\log3$ everywhere. Then
\[
 c=\min_{u\in\mathcal U}\liminf_{X\to\infty}\frac{D_u(X)}{2\log X}
  =\min_{u\in\mathcal U}\limsup_{X\to\infty}\frac{D_u(X)}{2\log X}.        \tag{1}
\]
If $c<\infty$, a single $u$ attains both minima with an ordinary limit. Its program may contain one fixed seed from each escaping component. The proof establishes existence of such a program conditional on that finite cardinality; it supplies neither the seeds nor a procedure to list them. The class is unconditionally nonempty, with the construction below usable without any information about the value of $c$.

For instance, a demonstrable bound $\liminf D_u(X)/(2\log X)<1$ for one computable positive bounded $u$ would exclude **all** escaping orbits. No such bound is established here. The formula counts escape components only. Contracting positive cycles, including any hypothetical nontrivial cycles, require a separate test.

## A lower bound from every independent ordinary trajectory

For a segment $x_j=T^j x_0$, set $A_t=\prod_{i<t}a(x_i)$. Its exact height identity gives
\[
 \log A_t=\log (x_t/x_0)-
     \sum_{i<t:\,x_i\ {\rm odd}}\log(1+1/(3x_i)).
\]
On every finite simple segment the last sum is at most $200/3$, by the written main-repository proof of the finite-path orbit-packing inequality T-A3-651, equations (1)–(2). This is a mathematical input to the asymptotic result; the finite Lean comparison does not formalize that estimate. Thus for each fixed escaping seed $s$ and its first index $t$ with $x_t\ge X>s$,
\[
 \sum_{i<t}d_u(x_i)\ \ge\ 2\log A_t+\log u(s)-\log u(x_t)
       \ \ge\ 2\log X-2\log s-400/3+\log u(s).                         \tag{2}
\]
All departures are distinct and below $X$. For $r$ escaping seeds in different components their paths are disjoint, so $D_u(X)\ge 2r\log X-O_{s_1,\ldots,s_r,u}(1)$. This proves the lower bound in (1), even for arbitrary positive $u\le1$ without computability or a uniform upper bound on $d_u$. If the global defect cap is $D>0$, these $r$ orbits require at least $(2r/D)\log X-O(1)$ distinct violating sites through $X$. [Finite-path reciprocal inequality T-A3-651](../../../astra-three-routes/pass3/FINITE_RECORDS.md)

## A finite stopping rule with a computable gate set

For a decidable set $E$ of ordinary integers, assume every escaping path eventually reaches $E$. Let $B_E(n)$ be the maximum of $A_t(n)$ up to and including first arrival at $E$, with the empty product $A_0=1$. If the path never reaches $E$, take the supremum over all times. In the latter case the path is eventually periodic by the assumption. A positive cycle has slope product strictly below one: multiplication of its physical height ratios gives the reciprocal of the positive product of $1+1/(3x)$ at its odd vertices, and a cycle consisting only of even vertices cannot occur. Thus the maximum is attained by the first repetition. Simulating until either event computes a positive rational $B_E(n)\ge1$.

Stopping immediately at $n\in E$ gives $B_E(n)=1$. At every other source, splitting off the first step gives the elementary optimal-stopping recurrence
\[
                  B_E(n)=\max(1,a(n)B_E(Tn)).                           \tag{3}
\]
Consequently $u_E=B_E^{-2}$ belongs to $(0,1]$ and has zero positive defect off $E$. At a gate $y$, if every future physical height through the next gate or during its gate-free tail is at most $H\ge y$, then $a(y)B_E(Ty)\le H/y$. Indeed every nonempty slope product from $y$ is at most its endpoint divided by $y$ by the height identity. Hence $d_{u_E}(y)\le2\log(H/y)$. This is a deterministic stopped maximum; splitting off its first action is the classical principle of dynamic programming. [Bellman, *The theory of dynamic programming* (1954)](https://doi.org/10.1090/S0002-9904-1954-09848-8)

## Unconditional sparse violations for a bounded computable function

Let $F:\mathbb N\to\mathbb N$ be any prescribed computable nondecreasing function tending to infinity, however slowly. Set $f(k)=\min(F(k),k)$ and choose a lower level $K\ge1$. At each level $k\ge K$, start every seed $i\le f(k)$ and record its first iterate $y\ge 2^k$, if it has one. Write $E_K$ for the union of the recorded integers. All starting seeds are strictly below the threshold. The search at a given level and seed ends after at most $2^k$ steps, because it crosses or repeats among the positive integers smaller than $2^k$. The last step before crossing is odd and gives
\[
                      2^k\le y< (3/2)2^k.                              \tag{4}
\]
These ranges for different levels are disjoint. To decide whether $y$ is a gate, use its own dyadic level and perform its finitely many threshold searches. In particular there are at most $f(k)$ gates in that whole octave. Each escaping seed is eventually included at every level and crosses each subsequent threshold. For any specified $n$, one may choose a level $k\ge K$ with $f(k)\ge n$; then the stopped-maximum computation at $n$ terminates within $2^k$ steps. Gate membership along that path is itself decidable by the preceding rule. These bounds assert total computability and can be extremely large.

A gate $y$ at level $k$ is the first crossing for some seed $i$ included both at $k$ and $k+1$. Since $y<2^{k+1}$, any later first crossing of $2^{k+1}$ by that seed is a marked gate and lies below $(3/2)2^{k+1}$. If the crossing never happens, that entire future stays below $2^{k+1}$. Either way the estimate after (3) gives $d_{u_{E_K}}(y)\le2\log3$. We have therefore constructed, unconditionally,
\[
 u_{E_K}\in\mathcal U,\qquad
 \#\{n\le X:d_{u_{E_K}}(n)>0\}\le\sum_{K\le k\le\log_2 X} f(k)
            =O\bigl((\log X)F(\lfloor\log_2X\rfloor)\bigr).            \tag{5}
\]
Since $f(k)\le k$, for every $s>0$,
\[
  \sum_{n\ge1}n^{-s}d_{u_{E_K}}(n)\le 2\log3\sum_{k\ge K}k2^{-sk}
                              \longrightarrow 0\quad(K\to\infty).     \tag{6}
\]
The finite work per vertex, the bounded edge deficit, and its arbitrarily small weighted mass are compatible with the possibility of a single escaping source. In particular, ambient power sparsity alone cannot prove one-edge positivity or its cumulative analogue on every fixed path.

Indeed $E_{K+1}\subseteq E_K$, and every fixed finite orbit segment is eventually below $2^K$. Thus $B_{E_K}(n)\uparrow\sup_{t\ge0}A_t(n)$, with the value infinity allowed. On bouncing through a bounded cycle the supremum is finite by strict cycle contraction. On an escaping orbit (2)'s height estimate gives $A_t(n)\to\infty$. Hence the decreasing limit of $u_{E_K}$ is positive **exactly** at bounded starts. It satisfies the limiting one-edge inequality everywhere, but it vanishes at every escaping start if any exist. This describes the precise positivity lost in forcing the ambient weighted deficit to disappear.

## Attaining the rate for a finite number of escaping components

Suppose $0<c<\infty$ and fix one seed $s_i$ in each escaping component. Use only these finitely many seeds, marking each one's first crossing $y_{i,k}$ of $2^k$ at all levels $k$ for which $2^k>s_i$. The membership test is finite and uses this fixed seed list. The gates on one chosen orbit increase strictly: (4) implies $y_{i,k}<2^{k+1}\le y_{i,k+1}$. Different chosen orbits never intersect. Any escaping ordinary start eventually merges into one of these tails and encounters gates. Thus (3) again computes a positive rational function on *every* ordinary source. In this construction its program can simply search to a gate or a repetition, without any prior termination time estimate.

Until the next gate from $y_{i,k}$, every physical height is at most $y_{i,k+1}$, by first passage. Hence
\[
           d_{u_E}(y_{i,k})\le2\log(y_{i,k+1}/y_{i,k})\le2\log3.
\]
For the gates through $X$ on this orbit, this bound telescopes. The next gate is at most $3X$ whenever the last counted one is at most $X$, and an orbit with no gate yet contributes zero. Thus the total for this orbit is at most $2\log X+O_{s_i}(1)$ and all other vertices outside the chosen gates contribute zero. Summing gives $D_{u_E}(X)\le2c\log X+O(1)$. With (2) this proves attainment and the claimed limit.

For $c=0$, take $E=\varnothing$. The program that waits for a repetition terminates on every input under this hypothesis, and (3) yields $D_{u_E}(X)=0$. For $c=\infty$, the lower bound for every finite $r$ forces the liminf to infinity for every $u\in\mathcal U$; (5) ensures the class has members in this case too. This finishes (1).

For a finite list of seeds one can also compute the number of distinct first crossings at each higher level. The count is nonincreasing once all seeds are below the initial threshold: every crossing at the next level comes through some crossing at the preceding one, and identical earlier crossing states have identical futures. A bounded seed ultimately supplies none. Seeds whose escaping paths merge supply the same crossing at every threshold above their finite pre-merger peaks. Thus the eventually constant value is exactly the number of escaping components represented in the finite list. There is no known effective common level at which this stabilization is certified for every list.

[Finite horizon and positivity review at PR 200](https://github.com/GettysburgResearch/collatz/pull/200) · [Source-specific positive mass and ordinary escape barriers at PR 201](https://github.com/GettysburgResearch/collatz/pull/201)
