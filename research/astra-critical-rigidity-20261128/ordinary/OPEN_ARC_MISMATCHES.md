# A height bound at interior dates of two open trajectories with few valuation mismatches

**PROPOSED written theorem.** Fix a nonnegative integer $s$ and $0<\theta<1$. Consider any growing family of pairs of positive odd trajectories with $p\to\infty$ ordinary **odd** steps each. At each common odd clock through $p$ the two states are distinct. At most $s$ of the $p$ pairs of native valuations disagree. The two trajectories need not meet prescribed targets, return to their origins, or belong to the same component.

More generally let their states be represented by odd positive integer numerators $y_{t,0},y_{t,1}$ over a common denominator $q$ prime to six, with $\log_2 q=o(p)$. Their actual equations are $2^{e_{t,j}}y_{t+1,j}=3y_{t,j}+q$, where $e_{t,j}=v_2(3y_{t,j}+q)\ge1$. The ordinary integer case has $q=1$. Put
$$
 H_t=\log_2(\max(y_{t,0},y_{t,1})+q),\qquad
 h_t=\log_2(\min(y_{t,0},y_{t,1})+q).
$$
Then
$$
             \liminf_{p\to\infty}
             \frac{H_0+h_{\lfloor\theta p\rfloor}}p\ \ge\ \theta .         \tag{1}
$$
Thus low initial height forces *both* trajectories to be exponentially high at each specified interior fraction of their odd clocks. In particular, with $\gamma=\log_2 3$ and $\beta=\gamma-1$,
$$
   \liminf_{p\to\infty}\frac{\log_2[(y_{0,0}+q)(y_{0,1}+q)]}p
                               \ \ge\ 1-\beta=2-\log_2 3.                  \tag{2}
$$
The leading constants in (1) and (2) are independent of the fixed mismatch budget. The asymptotic onset is ineffective and may depend on that budget.

## A consequence on a single ordinary orbit

Let $x_0,x_1,\ldots$ be the odd states of any fixed positive ordinary orbit which is not eventually periodic. Compare its first $p$ native valuations to the $p$ starting at its own lag $\ell\ge1$. On every family with $p\to\infty$ and bounded Hamming mismatch count,
$$
                         \liminf\frac{\ell}{p}
                \ \ge\ \frac{2-\log_2 3}{\log_2 3-1}>0.709.                \tag{3}
$$
Indeed synchronized state equality would imply a repeated ordinary odd state. Every odd step satisfies $x_{i+1}+1\le (3/2)(x_i+1)$, so the initial logarithm in (2) is at most $2\log_2(x_0+1)+\beta\ell$. Likewise $h_{\lfloor\theta p\rfloor}\le h_0+\beta\theta p$, which derives (2) from (1) by taking $\theta\uparrow1$. This excludes bounded-mismatch approximate prefix cubes of growing lengths, and applies throughout the regime $\ell\le p/2$. Exact agreement permits the stronger elementary bound $\liminf\ell/p\ge1/\beta$ by dividing the initial nonzero difference by the common power of two. Neither consequence asserts eventual periodicity of all positive orbits.

## Common carries on an open path

We use the field and the two chronological bases in the [arbitrary-cluster rotation theorem](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md), with two new boundary terms. Assume (1) fails with a fixed deficit $\delta>0$ on a subsequence. Then $H_0=O(p)$, both full trajectories have logarithmic height $O(p)$, and all total division exponents are $O(p)$. Partition at the at most $s$ post-mismatch dates. Within each common block include the smaller last exponent in the common division sum $B$. The difference of its two actual affine equations gives $2^B\mid y_{\rm high}-y_{\rm low}\ne0$ at its start. Thus each $B=O(p)$. The at most $s$ unmatched last excesses are each $O(p)$ because $2^{e_{t,j}}\le3y_{t,j}+q$. This proves the stated total bound. The same divisibility applies after inserting any additional cuts.

On an interval between such cuts of odd length $L$, let $F_j$ be the common division sum through its first $j<L$ edges. Its shared positive carry is
$$
                        C=\sum_{j=0}^{L-1}3^{L-1-j}2^{F_j},
                        \qquad (C,6)=1.
$$
On the higher starting track, all edges before the last agree with the other track. Their increasing common affine maps preserve the order. In particular the higher state at every date used by $F_j$ is the *physical maximum* at that date. Since its starting numerator $M\ge2^B$ and $F_j\le B$, the normalized affine correction on this track, through any $h<L$, is at most
$$
      1+\frac qM\sum_{j<h}2^{F_j}3^{-j-1}\le1+q/2 .
$$
Consequently $F_h-\gamma h\le H_{\rm start}-H_{{\rm start}+h}+
\log_2(1+q)+\log_2(1+q/2)$. Also
$\log_2 C\le\gamma L+\log_2 L+\max_{h<L}(F_h-\gamma h)$. All the selected drops within different blocks charge disjoint subintervals of the **single** maximum envelope $H$. At every native odd date, including a mismatch, $H_{t+1}-H_t\le\beta$. Along any open cut-to-cut arc of length $P$ its total downward variation is at most $\beta P+H_{\rm start}-H_{\rm end}$. We obtain, at every fixed bound on the number of blocks,
$$
  \sum_i\log_2(qC_i)\le (\gamma+\beta)P+H_{\rm start}-H_{\rm end}+o(p).  \tag{4}
$$
The error accounts for a bounded number of terms $O(\log p+\log(1+q))$. This estimate permits a different higher track on different blocks. The single envelope is well-defined at the switching edges.

## Choosing two independent boundary pairs

For the full path put $a(t)=\sum_{u<t}(e_{u,1}-e_{u,0})$. This sequence has at most $s+1$ distinct cumulative values, all $O(p)$. After stabilizing their incidence pattern and integer combinations on a subsequence, use the field $K=\mathbb Q(T_1,\ldots,T_n)$ generated by a complementary lattice of the dyadic powers. As proved in the [dyadic-field lemma](../cycles/SEPARATED_ROTATION_DENOMINATORS.md), every nonzero fixed $f\in K$ has $v_3(f)=o(p)$, and distinct Laurent monomials are rational-linearly independent on every further infinite subsequence. The proof uses Evertse's inequality for a nonvanishing sum of a fixed number of $S$-units. Stabilize all $K$-relations among each finite list of pairs and carries by the countable diagonal procedure of the rotation theorem. [Evertse, Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

On any interval $[u,v)$ of agreeing departures the nonzero differences $d_t=y_{t,1}-y_{t,0}$ satisfy $2^{F}d_v=3^{v-u}d_u$. After the first date all actual numerators are ternary units, since $q$ is prime to 3. If the two states at a date are dependent over $K$, their ratio is in $K$ and differs from 1. Hence $v_3(d_t)=o(p)$. Two such dependent pairs cannot occur in one common interval at dates separated by a fixed positive multiple of $p$.

Choose $\eta>0$ much smaller than $\delta$, $\theta$ and $1-\theta$. In each of the windows $[1,\eta p]$ and $[\lfloor\theta p\rfloor, (\theta+\eta)p]$ take $4s+8$ equally spaced candidates up to integer rounding. After removing candidates on mismatch departures, two candidates in each window lie in one common run at distance comparable to $p$. Stabilize the candidate relations and select an independent pair in each window. Call the two dates $u,v$ respectively, $P=v-u$. Both initial and terminal pairs are now independent over the same field on the stabilized subsequence. We have
$$
  P\ge (\theta-\eta)p-O(1),\quad H_u\le H_0+\beta\eta p+O(1),\quad
                h_v\le h_{\lfloor\theta p\rfloor}+\beta\eta p+O(1).       \tag{5}
$$
The terminal window lies **forward** from the stated interior date. No restriction on an individual downward jump is used.

## The two open boundary forms

Cut $[u,v]$ at the post-mismatches and at a time mesh of fixed size $N$. Use relative cuts $0=t_0<\cdots<t_k=P$ and actual cumulative exponents $E_{i,j}$ since $u$. Let
$$
 Z_i=qC_i2^{E_{i-1,0}}3^{-t_i},\qquad
 W_j=2^{E_{k,j}}3^{-P}y_{v,j},\qquad Y_j=y_{u,j}.
$$
The two terminal vectors $W_0,W_1$ are independent over $K$ because the ratio of their normalizing factors belongs to $K$. Telescoping the genuine two partial paths gives
$$
 R_{i,j}=Y_j+\sum_{b\le i}2^{E_{b-1,j}-E_{b-1,0}} Z_b
        =W_j-\sum_{b>i}2^{E_{b-1,j}-E_{b-1,0}} Z_b
        =2^{E_{i,j}}3^{-t_i}y_{u+t_i,j}.
$$
In particular both initial and terminal root pairs span two dimensions. Apply the [prefix and suffix basis argument](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md) to these identities. For details, greedily extend the two initial roots by carries in forward order (indices $I$), and the terminal roots by carries in reverse order (indices $J$). At any cut the prefix and suffix spans contain both $R_{i,j}$. Their normalized ratio differs from the ratio of the actual numerators by an element of $K$. Summation by parts gives
$$
 \sum_{i\in I}t_i-\sum_{i\in J}t_i
  =\sum_{i<k}(t_{i+1}-t_i)(2-\dim(P_i\cap S_i))
  \le(2s+2)(P/N+1).
$$
Here $P_i,S_i$ are the two cut spans. Inside each common run at most one nonboundary mesh pair is dependent, by the ternary difference bound. Post-mismatch cuts account for at most $s$ additional terms.

Use the suffix basis at infinity and two and the prefix basis at three, clearing field denominators in the latter forms. The finite Laurent-translate construction in the same proof supplies fixed rational forms on a fixed Euclidean dimension, with no nonzero rational coordinate relation recurring. In the two-place product each terminal form costs $\log_2 y_{v,j}-\gamma P$, while each suffix carry costs $\log_2(qC_i)-\gamma t_i$. At three the two initial roots have norm one and each prefix carry has logarithmic norm $\gamma t_i$. The translate-boundary fraction vanishes as the fixed box size $D$ grows after choosing $N$. Thus the base-two logarithm of the full product, divided by the translation-box cardinality, is at most
$$
 \log_2(y_{v,0}y_{v,1})-2\gamma P+\sum_i\log_2(qC_i)
      +\gamma(2s+2)(P/N+1)+o_D(1)O_{s,N}(p)+o(p).
$$
By (4) the sum of the first three terms is at most
$$
  -P+H_u+h_v+o(p),
$$
since $\log_2(y_{v,0}y_{v,1})\le H_v+h_v$ and $\gamma-\beta=1$. Equations (5) and the supposed deficit in (1) give a negative margin after choosing $\eta$. Next fix $N$ large, stabilize all necessary relations for that mesh, and finally fix $D$ large. The product is exponentially small in $p$ on this subsequence. The cleared primitive coordinates have height $2^{O(p)}$ at all these fixed choices, and their only clearing denominators are two and three. The rational $S$-adic Subspace Theorem forces a recurring fixed rational dependence, the desired contradiction. [Schlickewei's original theorem](https://doi.org/10.1016/0022-314X(77)90073-7)

## Larger denominators and finite controls

Allow an arbitrary common $q$ prime to six, and keep the same fixed $s,\theta$. The same argument yields
$$
  \liminf\frac{H_0+h_{\lfloor\theta p\rfloor}+4(s+1)\log_2 q}{p}
                \ge \theta .                                                  \tag{6}
$$
A violating subsequence has $H_0=O(p)$ and $\log q=O(p)$, sufficient for the height and field construction. In place of the uniform mesh, apply the [adaptive partition](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md) on the open arc between the selected boundary pairs. There are at most $s+1$ post-mismatch intervals. In each interval with positive limiting relative length insert one independent pair within its first $\epsilon$ fraction, using two separated candidates. Intervals of length $o(p)$ require no extra cut. The signed rank loss is at most $\epsilon p+o(p)$ and $k\le 2(s+1)$.

The sharpened shifted height bound on the higher track is
$$
  2^{F_h}(y_h+q)3^{-h}
  = M+q\left(\sum_{j<h}2^{F_j}3^{-j-1}+2^{F_h}3^{-h}\right)
  \le M(1+q).
$$
Indeed each dyadic power in parentheses is at most $M$ and the sum of its geometric coefficients is $(1+3^{-h})/2\le1$. Hence the carry bound (4) gains at most $2k\log_2q+O(k\log(p+1))$ beyond its explicit envelope terms, since each block contributes $\log_2 q+\log_2(1+q)$. In the final product this costs at most $4(s+1)\log_2q+o(p)$. The two boundary selections, terminal maximum cancellation and Subspace Theorem now prove (6). The discrepancy counts are fixed before taking limits in all three versions.

The [physical replay](check_open_arcs.py) sums each open-track affine ledger using exact rational arithmetic. It checks different total division sums, switches of the higher track, and the multiplicative open-boundary identity that cancels the terminal maximum. Cases reaching equality are truncated before the first common state. They include direct lag comparisons on six fixed ordinary orbits. [Integer receipts](OPEN_ARC_CONTROLS.json)

The conclusions concern the heights required for two ordinary trajectories to have long nearly equal valuation words. The general convergence and divergent-trajectory questions remain open.
