# Repeated finite-template tests on one ordinary record sequence

**Status — PROPOSED consequence of the adelic fixed-source theorem.**
This induction runs the [fixed-window Theorem A](../adelic/README.md)
over a growing number of coefficient-record blocks. All windows
come from one escaping positive ordinary source. The proof uses
the theorem with fixed budgets before passing to a second limit.

Fix a finite library $W$ of nonempty periodic native parity words and
a fixed integer $K$. For each genuine record block $i$, starting at
$q_i$, give any parse into at most $K$ exceptional intervals and
the complementary periodic pieces from $W$ in arbitrary phases.
Zero-length exceptions may switch the periodic template. Denote by
$s_i$ its total native clock and by $b_i$ the *sum* of exceptional
lengths. Write
$$
 S_l=\sum_{i<l}s_i,\qquad B_l=\sum_{i<l}b_i,\qquad
 H_l=\sum_{i<l}\log_2(q_i+1),\qquad \alpha=\log_2 3 .
$$

**Theorem T.** For every fixed finite library and per-record budget,
$$
 \limsup_{l\to\infty}\frac{S_l-\alpha B_l}{S_l+H_l}\le0.           \tag{T1}
$$
In particular along every subsequence with $S_l/H_l$ bounded away
from zero, $\liminf B_l/S_l\ge\log_3 2$ on that subsequence.
This applies whenever the elapsed odd time $k_l$ is bounded below
by a positive multiple of $l^2$ there. If $B_l=o(S_l)$, then
$$
              S_l=o(H_l),\qquad S_l=o(l\log(q_l+1)),\qquad
              k_l=o(l^2).                                         \tag{T2}
$$

*Proof.* Group $J$ successive record blocks into one window, with
$J$ any fixed positive integer. A group has at most $J(K+1)$
exceptional intervals after adding zero-length separators at
its internal record boundaries. By adelic Theorem A, for each
$\epsilon>0$ all sufficiently late such groups, starting at record
$i$, satisfy
$$
 (1-\epsilon)\sum_{j=i}^{i+J-1}s_j
       \le \log_2(q_i+1)+\alpha\sum_{j=i}^{i+J-1}b_j.              \tag{T3}
$$
Indeed if this failed along starts tending to infinity, the native
lengths would tend to infinity as well since $q_i\to\infty$. This
would directly contradict the fixed-budget theorem on that
sequence of ordinary windows. The constants need no uniformity in
$J$. Divide the first $l$ blocks backwards into full groups of
size $J$ and a bounded initial remainder. The strictly increasing
$q_i$ give $\log_2(q_i+1)\le J^{-1}\sum_{j=i}^{i+J-1}
\log_2(q_j+1)$ on every group. Summing (T3) gives
$$
 (1-\epsilon) S_l\le H_l/J+\alpha B_l+O_{J,\epsilon}(1).
$$
The constant includes all possibly early groups and can depend on
the ray, library and budget. Divide by $S_l+H_l$, send $l\to\infty$,
then $J\to\infty$ and $\epsilon\downarrow0$. This proves (T1).
For the first corollary divide the same finite bound by $S_l$
on the chosen subsequence. In addition $q_l\ll_{q_0}(3/2)^l$
by the full-orbit distortion estimate and the fact that every
record coefficient increases by at most $3/2$. Thus $H_l=O(l^2)$.
Since $k_l\le S_l\le\alpha k_l$, the remaining conclusions follow.

For the exact-template case $b_i=0$ throughout, the same grouping
also gives the normalized local statement
$$
       \frac1l\sum_{i<l}\frac{s_i}{\log_2(q_i+1)}\longrightarrow0. \tag{T4}
$$
Indeed the sum over any sufficiently late group of $J$ terms is
at most $1/(1-\epsilon)$ by (T3) and monotonicity of $q_i$.
Thus record blocks of native length at least $c\log_2(q_i+1)$
must have zero natural density in the record index, for every
$c>0$, if every block has this bounded template complexity.

There is a version without a supplied record partition. Include
single-letter words in $W$ so every finite path admits a parse, and
let $R(L)$ be the least number of exact periodic pieces covering
the first $L$ native bits. Write $X(L)=\max_{0\le i\le L}T^i(q_0)$.
Then on every positive escaping ordinary ray,
$$
                       \frac{R(L)\log_2(X(L)+1)}{L}\to\infty.       \tag{T5}
$$
To see this, partition an optimal parse into groups of at most $J$
pieces. The zero-exception case of the [finite two-ended bound
H](../adelic/README.md) gives each group length at most
$\log_2(X(L)+1)/(1-\epsilon)$ unless its endpoint is bounded in
terms of $J,W,\epsilon$. Such endpoints lie before a fixed native
time, since the actual ordinary trajectory escapes, so all groups
of the exceptional bounded-endpoint type together have length
$O_{J,W,\epsilon,q_0}(1)$. Also $R(L)\to\infty$; bounded $R(L)$
on a subsequence would make the entire growing prefix a single
fixed-budget window with fixed source and unbounded endpoint,
violating H. Consequently
$L\le(R(L)/J+1)\log_2(X(L)+1)/(1-\epsilon)+O(1)$.
First let $L\to\infty$, then $J\to\infty$, proving (T5).
At slow growth this height-sensitive bound complements the
adelic lane's stronger lower bound relative to $\log L$ at fast growth.

The [two-run symbolic example](ESCAPE_OF_MASS.md) with block lengths
$m_i=i+O(1)$ has $k_l\asymp l^2$. Its two constant odd-gap
runs correspond to at most two periodic native pieces. Thus (T2)
already excludes *every* positive ordinary realization of that
growth pattern, independently of the special marker divisibility
used there. The theorem also excludes examples with vanishing
exceptional fraction on the same scale. Slower first-ladder growth,
or a sufficient number of irregular letters, remains possible in
these necessary estimates.
