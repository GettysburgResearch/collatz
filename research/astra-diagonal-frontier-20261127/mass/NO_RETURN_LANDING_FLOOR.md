# A uniform fixed-root lower bound with all reverse prefixes constrained

Fix the positive odd Collatz map \(U(v)=(3v+1)/2^{v_2(3v+1)}\). On the way back from a specified odd unit \(z\) write \(E_i\) for the *actual* inverse gaps and \(S_j=\sum_{i=1}^j E_i\). There are absolute constants \(c>0,C\ge4\) such that for every ordinary odd \(z\ge1\) coprime to 3, every \(M\ge z\), and every \(X\ge CM\), at least \(cX/M\) distinct odd integers \(v\in(X/4,X]\) first land at \(z\) below \(M\) and satisfy
\[
             S_j>\tfrac74j+\log_2(M/z)
          \qquad(1\le j\le J),                                        \tag{1}
\]
where \(J\) is their odd travel time to \(z\). In particular *each earlier physical site* fails the \(7/4\) forward gate on its own suffix ending at \(z\). This result uses the selected words in the proof of Weaver's first-landing lower bound. The displayed first-landing probability in that paper, without its selected-word construction, does not imply (1).

For the first-permanent-entry law \(\mu\) this gives
\[
   \mu(\{z\})\ge c'/z \qquad\text{at every permanently passing odd unit }z. \tag{2}
\]
Periodic permanent targets are included. For every nonperiodic odd unit \(z\), with \(d_z\) its relative natural predecessor density and \(Q_z\) the natural inverse entrance law, the stronger reserve profile holds:
\[
 d_z Q_z\!\left(S_j-\tfrac74j>b\ \text{for every }j\ge1\right)
       \ge (c'/z)\,2^{-b}\qquad(b\ge0).                               \tag{3}
\]
In particular the all-time absence-of-record probability \(q_z\) at reserve zero has \(d_zq_z\ge c'/z\). This proves a lower bound for the constrained physical law at every specified nonperiodic ordinary unit. A strong first-landing floor or full-measure inverse mean-two theorem taken separately gives no such all-prefix lower bound for this slope.

## The retained word and the deterministic barrier

Use the actual subdensity \(H_{k,d}\) in Weaver's Appendix A, equation (60), verified there on a fixed unit cylinder \(\mathcal C=y+3^q\mathbb Z_3\) for \(|d-2k|\le2\sqrt k\). It contains complete selected blocks of lengths \(b_i\) and then a free terminal segment of length \(<2b_j\), where \(j\) denotes the next block. With \(b_0=10^6\), \(b_{i+1}=b_i+\lfloor b_i/100\rfloor\), a selected complete block has total \(D_i\) within \(\lceil b_i^{3/5}\rceil\) of \(2b_i\). Since \(b_i\ge10^6\), the tolerance is at most \(b_i/100\); for example \(b^{3/5}+1\le b/100\) on that range. A selected word also has \(A_t=3^t2^{-S_t}\le R_0=16^{b_0}\) for every prefix and the increasing affine offsets \(B_t=\tfrac13\sum_{i=1}^t A_i\le B_0=2^{b_0+1}+16^{b_0}\). At the favorable ternary cylinder its unnormalized central-slice mass, multiplied by \(3^k\), is at least \(c_0\Pr(S_k=d)\) for every sufficiently large \(k\). The gap law used to count words here is the independent geometric measure, in inverse order. The conclusion below concerns distinct ordinary integers. [Weaver, Paper 12, Lemma 13 and Appendix A, equations (51), (58), (60)](https://rstation.ai/problems/collatz/papers/12).

For a prefix ending inside the next selected block or the final free part, put \(d_i=\sum_{\ell<i}b_\ell\) and let \(0\le u\le2b_i\) be the length used in that next part. By telescoping growth \(b_i\le b_0+d_i/100\). Every gap is at least one. The cumulative total \(T_{d_i+u}\) on this selected word therefore satisfies
\[
 T_{d_i+u}-\tfrac74(d_i+u)
   \ge (1.99-\tfrac74)d_i-\tfrac34 u
   \ge 0.225d_i-\tfrac32 b_0 \ge -\tfrac32 b_0.                     \tag{4}
\]
This argument covers partial early blocks, free final words and empty prefixes. [SelectedBlockBarrier.lean](SelectedBlockBarrier.lean) checks extension of the two completed-block invariants, (4), payment by a single initial gap and the failing-suffix implication.

Choose a fixed \(K\ge\max(R_0,B_0+1,1)\). Let \(e_{\min}\) be the least integer for which \(2^{e_{\min}}z\ge6KM\). Since 2 generates the units modulo \(3^{q+1}\), within the next \(2\cdot3^q\) integers one can choose \(e\ge e_{\min}\) with \(2^e z\equiv1+3y\bmod3^{q+1}\). Its direct physical preimage \(r=(2^ez-1)/3\) is positive odd, lies in the unit cylinder \(\mathcal C\), and satisfies
\[
       2KM-\tfrac13\le r<C_bM,\qquad r>2B_0,\quad r-B_0>R_0M
\]
for an absolute \(C_b\). Crucially \(e\ge\log_2(M/z)+\log_2(6K)\), where \(\log_2(6K)>\tfrac32b_0+\tfrac74\). This is already guaranteed by the published choice \(R_0=16^{b_0}\). First take the actual inverse edge \(z\leftarrow r\), then the selected word starting at \(r\). Inequality (4) gives \(e+T_t>\tfrac74(t+1)+\log_2(M/z)\) at *every* resulting backward prefix. The order here matters. A gap appended at the remote source would not pay the initial debt.

An eligible word of total \(d\) and odd length \(k\) has integral inverse states \(x_i=(r-B_i)/A_i>(r-B_0)/R_0>M\); the actual parities and valuations follow from the affine congruence at \(r\). Thus \(z\) is the first forward landing at or below \(M\). Set \(\theta=\log_23,\ \beta=2-\theta,\ L=\log_2(X/r)\). Use integers \(|k-L/\beta|\le h\sqrt L\) for a small absolute \(h\), and \(d_k=\lfloor L+k\theta\rfloor\), giving \(L-1<d_k-k\theta\le L\). For large absolute \(L\), these totals lie within \(2\sqrt k\) of \(2k\). The geometric negative-binomial local estimate gives \(\Pr(S_k=d_k)\gg L^{-1/2}\), over \(\gg\sqrt L\) depths. On each such slice the equal geometric weights \(2^{-d_k}\) give at least \(c_0(2^{d_k}/3^k)\Pr(S_k=d_k)\ge(c_0X/(2r))\Pr(S_k=d_k)\) words. Each gives its own ordinary \(x_k\in(X/4,X]\) because \(r/2<r-B_k\le r\). Fixed-depth collisions are impossible by deterministic forward iteration. Distinct depths give distinct first-landing times, also for periodic \(z\). Summing and using \(r<C_b M\) proves (1) for \(X\ge CM\) with absolute \(C\).

## Natural entrance mass and prefix-free amplification

Take \(M=z\) in (1). When \(z\) is permanent, every earlier site fails a finite gate, so \(F(v)=z\) on those distinct sources. Divide by the number of odd integers through \(X\) and let \(X\to\infty\), using the countable first-entry law. This gives (2) regardless of possible periodicity.

For (3), take \(M=z2^b\). At any fixed depth \(m\), the counted sources have \(J>m\) once \(X\) is large, since \(J=1+k\) and \(k\) lies in the preceding central window. Use the fixed-depth conditional natural entrance law of a nonperiodic unit \(z\), summing over its countable cylinder partition, to conclude
\[
   d_z Q_z(S_j-\tfrac74j>b,\ 1\le j\le m)\ge c'/(z2^b).
\]
The right side does not depend on \(m\). Continuity from above gives (3). This is not a replacement of the ordinary law by its stationary transform. The estimate on conditional mass retains its \(d_z\) denominator.

There is a positive amplification for every prefix-free family \(\mathcal A\) of concrete ordinary unit inverse words at a fixed nonperiodic \(z\) that are strictly above the \(7/4\) line at all their positive prefixes. Write \(x_w\) for the ordinary terminal ancestor of \(w\). Continuing each word at \(x_w\) by the zero-reserve event in (3) stays strictly above the same line from \(z\). The family's cylinders are disjoint and have natural mass \(d_{x_w}/d_z\). Hence
\[
             d_z q_z\ \ge\ c'\sum_{w\in\mathcal A}{1\over x_w}.       \tag{5}
\]
Take a supremum over finite antichains or use countable additivity. In particular, on an escaping ray and for every fixed \(A>0\), the [relative sparse-passage law](RELATIVE_SPARSE_PASSAGE.md) imposes
\[
 \sum_{\substack{z\ {\rm permanent\ on\ that\ ray}\\z\ge M}}
    \sup_{\mathcal A\text{ at }z}\sum_{w\in\mathcal A}1/x_w
    \ll_{A}(\log M)^{-A}.
\]
No antichains exceeding the latter bounds on any hypothetical escaping ray have been constructed. With only the empty word (5) charges \(1/z\). Even the sum of \(1/z\) over *all* large permanent roots already has a power-saving tail by the PR201 ordinary sparsity estimate. The reciprocal lower bound proves positive mass for every permanent unit but does not by itself contradict escape or exclude cycles.
