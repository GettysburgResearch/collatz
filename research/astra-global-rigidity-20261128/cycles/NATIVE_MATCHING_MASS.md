# How much of a full native rotation can lie in its longest matching runs?

Let \(y_i\) be a primitive positive **ordinary integer** cycle of odd period \(p\), and let \(P\) count its rising departures, those with \(a_i=v_2(3y_i+1)=1\). For a proper lag \(0<r<p\), a matching run is a circular interval of departures on which \(a_i=a_{i+r}\). Write \(L_k(r)\) for the sum of the \(k\) largest maximal matching-run lengths, using all runs if there are fewer. Write \(\gamma=\log_2 3\), \(\beta=\log_2(3/2)\). Then for each fixed \(k\), along growing least periods,
\[
       \max_{0<r<p}\ \gamma L_k(r)\ \le\ 2\beta P+o_k(p).             \tag{1}
\]
Thus every native rotation leaves at least \((1-2\beta/\gamma-o_k(1))p\) sites outside **any fixed number of its exact matching runs**. The constant is approximately \(0.26186\); fewer rises increase the lower bound. The remaining sites may themselves lie in a growing number of shorter matching runs. In particular (1) does not assert a positive Hamming mismatch density. The theorem allows arbitrarily many mismatches and arbitrary division sizes. On the shortcut clock different arithmetic and rates apply.

The proof uses the fixed-place construction of [native rotation separation](NATIVE_ROTATION_SEPARATION.md). We give its needed restriction to selected matching intervals and a multiple-lap argument which removes the small-lag and boundary losses. The sources are actual positive integers throughout.

## A selection estimate on two adjacent native words

Consider two adjacent native words of length \(d\to\infty\), at dates \([0,d)\) and \([d,2d)\), with positive odd states \(y_t\). Assume \(y_t\ne y_{t+d}\) for all \(0\le t<d\), \(\log_2(y_0+1)=o(d)\), and \(S_{2d}=O(d)\). Other state repetitions are allowed. Select a bounded number of disjoint intervals \([b_j,c_j)\subset[0,d)\) on each of which the two copies match exactly. Let \(L=\sum (c_j-b_j)\), and let \(P_{2d}\) count rises in the whole \(2d\)-departure window. Then
\[
                        \gamma L\le \beta P_{2d}+o(d).                 \tag{2}
\]
There is no restriction on the two words outside the selected intervals. For ordinary positive paths the clock bound follows from \(2^{S_{2d}}=y_0\prod_{t<2d}(3+1/y_t)/y_{2d}\le y_0 4^{2d}\), including paths with repetitions. The separate source inequalities assure the native differences are nonzero on the selected intervals; distinctness of all \(2d\) departures played no further role in the argument once the clock bound was available.

For details, on a putative positive linear violation pass to the same scaled sequence field as in the native separation proof, with scale \(d\). Discard selected intervals of vanishing normalized length and put \(b_j^*=\lim b_j/d\), \(c_j^*=\lim c_j/d\), and \(e_j=\lim v_3(y_{b_j}-y_{b_j+d})/d\). All are finite by the ordinary forward growth bound. The projections of \([b_j^*-e_j,c_j^*]\) on \(\mathbb R/\mathbb Z\) cover the selected limiting intervals, whose union has measure \(\lim L/d\). Group by common effective start modulo one, taking a longest representative from each group. Their unprojected lengths have sum at least \(\lim L/d\). Choose one internal terminal date \(t_j\) per representative with normalized date arbitrarily close to its right endpoint, avoiding the finitely many prohibited valuation residue classes. With \(g_j=v_3(y_{t_j}-y_{t_j+d})\) this gives \(\lim\sum g_j/d\ge \lim L/d-\epsilon\). A positive linear violation has positive limiting selected length, so the construction uses at least one representative.

Use \(B_t=2^{S_t}3^{-t}\), \(H_t=B_ty_t\) and \(\lambda_j=B_{t_j+d}/B_{t_j}=2^{u_j}3^{-d}\), with \(u_j=O(d)\). The pure dyadic fixed-place estimate gives integral normalized ternary valuations on \(\mathbb Q(\lambda_j)\), exactly as there. The distinct normalized residue classes of \(H_{t_j}\) and \(H_{t_j}-\lambda_j^{-1}H_{t_j+d}\) imply endpoint independence over this field, even when a physical integer appears at unrelated dates. The translated finite boxes and the ternary replacements give the same total saving at least \(\gamma(1-\delta)\sum g_j\) per average box row.

There is a sharper ordinary chronological charge in this setting. On \([a,b)\) let \(P[a,b)\) count rises. For each \(a\le i<b\),
\[
 \frac{B_i}{B_b}=\prod_{i\le j<b}\frac{3}{2^{a_j}}
       \le (3/2)^{P[a,b)}.
\]
At every nonrise this factor is at most \(3/4\). Similarly \(y_t+1\le(3/2)^{P[0,t)}(y_0+1)\): a rise multiplies \(y+1\) by \(3/2\), and a nonrise does not increase \(y\). By the exact chronological sum formula for \(H_b-H_a\), the product in one real-differenced row is at most
\[
       (y_0+1)(2d)^{2k'-1}(3/2)^{P_{2d}},
\]
where \(k'\) is the bounded number of representatives. Its base-two logarithm is \(\beta P_{2d}+o(d)\). Under a fixed linear violation of (2), taking \(\epsilon,\delta\) sufficiently small yields an exponentially small product of the fixed forms. The same rational Subspace Theorem contradicts the established endpoint independence. This proves (2).

## Lifting a proper lag through many actual laps

To prove (1), assume a sequence violates it by a fixed multiple of \(p\). Rotate each cycle to begin at its least odd value, which has logarithm \(O(\log p)\) by the classical two-log bound used in the main proof. Fix an arbitrary positive integer \(K\). Instead of comparing paths \(r\) steps apart, use
\[
                               d=Kp+r.
\]
This is the same physical rotation at every departure. Every pair \(y_t,y_{t+d}\) is distinct because \(r\) is proper. The window extends through actual repeated laps; its other repetitions are permitted in (2). All the chosen \(k\) circular runs lift to matching intervals on \([0,Kp)\subset[0,d)\), splitting at lap boundaries when necessary. This gives at most \(2Kk\) intervals with total length exactly \(K L_k(r)\). Also \(P_{2d}\le(2K+2)P\), since \(2d\le(2K+2)p\). The integer \(K\) and hence the interval budget remain fixed while \(p\to\infty\). Using \(d\asymp_K p\), (2) implies
\[
                  \gamma L_k(r)\le (2+2/K)\beta P+o_{k,K}(p).
\]
Take the limit superior along the alleged violating sequence, using \(P\le p\), and then let \(K\to\infty\). This proves (1), uniformly in the originally selected proper lag. The order of limits uses fixed-dimensional Subspace Theorems only. Distinctness of paired physical states is indispensable. At lag zero modulo the period all protected differences vanish.

Weaver 174 bounds the share of rises in the largest constant-exponent-one runs on an ordinary path, including a joint result with selected high-exponent departures. The present runs can instead have arbitrary internal valuation words, and agreement is between different phases of the same actual cycle. [Weaver, *How rising steps are distributed in odd Collatz trajectories*, Theorems 2 and 5](https://rstation.ai/problems/collatz/papers/174)
