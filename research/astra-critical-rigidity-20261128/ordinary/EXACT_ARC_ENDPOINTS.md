# Exact endpoint heights for open odd trajectories with a fixed mismatch budget

**PROPOSED written theorem.** Use the positive odd-map normalization of [the open-arc theorem](OPEN_ARC_MISMATCHES.md). At common odd dates $0\le t\le p$ the two positive odd numerators $y_{t,0},y_{t,1}$ over a common $q$ prime to six are distinct. There are at most a fixed $s$ mismatches between their $p$ native odd valuations. Allow any growth of $q$. Put $H_t=\log_2(\max(y_{t,0},y_{t,1})+q)$ and $h_t=\log_2(\min(y_{t,0},y_{t,1})+q)$. Uniformly in these open paths,
$$
      \liminf_{p\to\infty}\frac{H_0+h_p+4(s+1)\log_2 q}{p}\ge1.          \tag{1}
$$
Both dates in (1) are the supplied physical endpoints. Equivalently, for every fixed $s$ and $\epsilon>0$ there is a finite $C(s,\epsilon)$ such that, at **every** length,
$$
             (1-\epsilon)p\le H_0+h_p+4(s+1)\log_2q+C(s,\epsilon).       \tag{2}
$$
The finite constant is ineffective. Its dependence on the mismatch budget matters when adding inequalities from many arcs.

For example, on ordinary integer paths where **either** final odd state is bounded independently of $p$, (1) gives $\max_j y_{0,j}\ge2^{(1-o(1))p}$. The other final state can be arbitrarily large. More generally, if two (possibly independently timed) positive odd targets are supplied, one may stop the common comparison at the earlier **odd-clock** visit. Forward-incomparable targets ensure the odd states are distinct through that cut. The conclusion then applies whenever their common-prefix valuation mismatches stay bounded. It puts no upper bound on those mismatches for a general pair of target visitors.

## Why arbitrary endpoint ranks cost exactly the right number of forms

Use the stabilized dyadic field $K$, actual common carries $Z_i$, and physical endpoint vectors of the [open-arc proof](OPEN_ARC_MISMATCHES.md), now cutting the full supplied interval $[0,p]$. For a contrary family in (1), all initial and subsequent heights are $O(p)$ and $\log q=O(p)$. There are boundedly many division-sum differences, each $O(p)$, by the nonzero difference divisor on each common block. Select the adaptive post-mismatch cuts of (6) there, with at most $k=2(s+1)$ blocks. Let $0=t_0<\cdots<t_k=p$. Set
$$
   Y_j=y_{0,j},\quad W_j=2^{E_{k,j}}3^{-p}y_{p,j},\quad
   P_i=\langle Y_0,Y_1,Z_h:h\le i\rangle_K,\quad
   S_i=\langle W_0,W_1,Z_h:h>i\rangle_K .
$$
Every $P_i+S_i$ is the full space $V$; this follows by telescoping each actual partial path from both endpoints. The two true normalized partial numerators belong to its intersection at every cut.

Let $a=\dim\langle Y_0,Y_1\rangle_K$ and $b=\dim\langle W_0,W_1\rangle_K$. Both are in $\{1,2\}$. Choose independent sublists of the initial and terminal roots spanning their respective pairs. When $b=1$, choose the root corresponding to the **smaller final numerator**, passing to a subsequence to fix its label. The initial rank requires no special choice since all integer roots have ternary norm at most one. Every true numerator after the first date is a ternary unit even when an initial numerator is divisible by three.

As before, extend these bases greedily by carries in forward and reverse order, with indices $I,J$ and $r=\dim V$. Now $|I|=r-a$ and $|J|=r-b$. Their cumulative difference through cut $i$ is
$$
   \#(I\cap[1,i])-\#(J\cap[1,i])
          =\dim P_i-a-(r-\dim S_i)
          =\dim(P_i\cap S_i)-a.
$$
At the terminal endpoint this equals $b-a$. Discrete summation by parts therefore gives the exact identity
$$
\begin{aligned}
 \sum_{i\in I}t_i-\sum_{i\in J}t_i
   &=(b-a)p+\sum_{i<k}(t_{i+1}-t_i)[a-\dim(P_i\cap S_i)]\\
   &=(b-2)p+\sum_{i<k}(t_{i+1}-t_i)[2-\dim(P_i\cap S_i)].              \tag{3}
\end{aligned}
$$
For any fixed $\eta>0$, the last sum is at most $\eta p+o(p)$ on the adaptive partition. In each original interval of positive limiting length, choose a $K$-independent interior pair within its first $\eta$ fraction by testing two separated matching dates, both strictly after time zero. Then only the short initial piece can contribute positive loss. All intervals of length $o(p)$ together have negligible total; at every cut the intersection contains a positive normalized partial numerator. Neither endpoint needs to be moved.

At infinity and two each of the $b$ terminal roots costs $\log_2 y_{p,j}-\gamma p$, where $\gamma=\log_2 3$. The initial roots contribute at most zero at three. The prefix and suffix carry difference costs $\gamma(\sum_I t_i-\sum_J t_i)$. By (3) its boundary term combines with the terminal factor to give
$$
                        -b\gamma p+\gamma(b-2)p=-2\gamma p.
$$
The positive logarithmic terminal charge is at most $\log_2(y_{p,0}y_{p,1})$. The finite Laurent-translate completion, neutral ternary clearing factor, finite-dimensional heights and primitive normalization are those in the [arbitrary-cluster theorem](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md). The selected suffix carries have total logarithmic charge no larger than all carries.

With $\beta=\gamma-1$, their open maximum-envelope estimate is
$$
     \sum_i\log_2(qC_i)\le(\gamma+\beta)p+H_0-H_p+
                              2k\log_2 q+O_s(\log(p+1)).
$$
In particular the full product logarithm per core monomial is bounded above by
$$
       -p+H_0+h_p+4(s+1)\log_2q+\gamma\eta p+o_D(1)O_s(p)+o(p).
$$
Here the field/basis-dependent constant is fixed before taking the Laurent box size $D$ large. One can choose $\eta$, stabilize the basis, and then fix $D$ to make the last two fractional costs smaller than a supposed fixed deficit in (1). The rational $S$-adic Subspace Theorem contradicts the absence of a recurring fixed rational relation, as in the open-arc proof. This establishes (1); truncating the finitely many smaller lengths by a larger additive constant gives (2).

There is a stronger rank-one version along any stabilized family whose terminal ratio is in the same field $K$. Then the sole positive terminal charge is $\log_2\min_j y_{p,j}$. Retaining it exactly gives
$$
 \liminf\frac{H_0+\log_2\min_j y_{p,j}-H_p+4(s+1)\log_2q}{p}\ge1.       \tag{4}
$$
This hypothesis holds, for example, when the ordered pair of final numerators is fixed, or when their ratio is from a fixed finite set. Their normalizing-factor ratio is a power of two in $K$. The unconditional statement (1) requires no field-rank test on the data.

## Ordinary orbit growth and bounded-mismatch returns

For one fixed positive ordinary odd orbit $x_0,x_1,\ldots$ that is not eventually periodic, define its upper exponential growth rate in odd clocks by
$$
         \Lambda=\limsup_{t\to\infty}\frac{\log_2(x_t+1)}{t}
             =\gamma-\liminf_{t\to\infty}\frac{\sum_{i<t} e_i}{t}.
$$
Indeed the states are distinct positive integers, hence tend to infinity. The average of $\log_2(1+1/(3x_i))$ tends to zero, and summing the exact logarithmic recurrence gives the identity. In particular $0\le\Lambda\le\beta$.

Compare the first $p$ valuations with its own lag-$\ell$ word of the same length. Suppose their mismatch count remains bounded along a sequence $p\to\infty$. If $\ell/p\to A<\infty$, (1), the bound $H_0\le\max(\log_2(x_0+1),\log_2(x_\ell+1))$, and $h_p\le\log_2(x_p+1)$ yield
$$
                              1\le\Lambda(1+A).                         \tag{5}
$$
If $\ell$ stays bounded the initial term is $o(p)$; if it grows, the definition of $\Lambda$ bounds it by $(\Lambda+o(1))\ell+O(1)$. Together with $\Lambda\le\beta$, (5) gives the earlier explicit lag-ratio bound. If $\Lambda=0$, every bounded-mismatch recurrence along this fixed orbit has $\ell/p\to\infty$. The growth-rate formulation was suggested by the reference-arc lane. No particular growth rate for an unclassified orbit is assumed.

[Physical open-path controls](OPEN_ARC_CONTROLS.json) test the mixed terminal maximum cancellation. The [Lean kernel](BoundaryRanks.lean) proves (3) for actual finite-dimensional submodule ranks and bounds an intersection containing independent partial directions. Both public roots passed Lean 4.34.1 and the ordinary axiom inventory. The [finite rank replay](check_mismatch_partitions.py) exercises all four possible pairs of endpoint ranks, including both directions of rank change. The Subspace Theorem and its asymptotic application are written arguments.
