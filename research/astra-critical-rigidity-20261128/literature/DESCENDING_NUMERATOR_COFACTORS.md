# Almost every denominator level in every long window has a large numerator cofactor

Fix finite prime sets \(P,S\), with \(2,3\in P\). Let \(q\ge1\) be any integer coprime to six, supported on \(S\). Its size may vary without bound. Start the rational shortcut map at any reduced signed fraction \(b/(q3^n)\), \(n\ge1\). At each level \(h=n,n-1,\ldots,1\) denote by \(u_h\) its signed **odd** numerator, in lowest terms, immediately before the odd departure that changes its denominator from \(q3^h\) to \(q3^{h-1}\). Write \(b_P(v)\) for the positive factor of \(|v|\) supported outside \(P\), with multiplicities.

For every \(0<\delta<1\) and \(\epsilon>0\) there exists \(C_{P,S,\delta,\epsilon}\) such that in **each** consecutive window of \(w\) levels in \([1,n]\),
\[
 \#\left\{h\text{ in the window}: b_P(u_h)\le(q3^h)^{1-\delta}\right\}
                                      \le\epsilon w+C_{P,S,\delta,\epsilon}.  \tag{1}
\]
Thus the exceptional proportion tends uniformly to zero as \(w\to\infty\), even for varying signed sources, denominator sizes and positions of the window. In particular this holds throughout the positive \(q=1\) arithmetic landing model and every moving subwindow of it. The estimate counts odd departures, one per denominator level. It gives no \(O(n\log n)\) upper bound for the number of intervening native dates. The [physical construction of the positive landing test](../ordinary/POSITIVE_DESCENDING_INTERVALS.md) relates that separate question to the maximal unmatched integer clock.

The proof below uses just the [signed chronological Subspace estimate (3)](../ordinary/SPARSE_DISCREPANCY_BLOCKS.md), positivity of the descending impulses, and divisibility at one prime at a time. Its constants inherit the ineffectivity of the Subspace estimate. In contrast to a general positive-level pair, this descent has only one sign of impulse, and all observed endpoints are odd.

## Integer formulas on the physical rational orbit

Reduction preserves coprimality of the numerator to \(q\) at every step. For \(h>1\) the odd update replaces \(u\) by \((u+q3^{h-1})/2\), still a ternary unit, and even steps halve the numerator. An exact zero before the denominator loses its last factor of three would require \(u=-q3^{h-1}\), precluded by coprimality to \(q3\). At \(h=1,q=1,u=-1\) the landing can be zero, after all our marked dates. At a positive level a nonzero integer numerator takes only finitely many even halvings before an odd departure. This proves the existence and nonvanishing of all listed \(u_h\), for either initial sign.

Suppose an interval begins at \(u_h\) and ends at \(u_{h-k}\), where \(1\le k\le m\) and \(h-k\ge1\). Denote its native duration by \(d\) and its \(k\) odd dates by \(0=t_0<t_1<\cdots<t_{k-1}<d\), relative to its start. Then
\[
 2^d u_{h-k}-u_h
    =q3^{h-k}V,\qquad
 V=\sum_{i=0}^{k-1}2^{t_i}3^{k-1-i}>0,\qquad
                   V\le m2^d3^m.                                      \tag{2}
\]
All intermediate normalized numerators are nonzero. Thus every strictly earlier native cut of the sum with both endpoints restored is nonzero, since the partial sum through the previous step is the intermediate numerator times the corresponding power of two. Apply the chronological estimate with \(P'=P\cup S\) and \(\kappa=2\). Its pure terms have odd part \(q3^{h-1-i}\) supported on \(P'\). The two endpoint dyadic valuations vanish. Consequently
\[
         d\le 2\log_2[b_{P'}(u_h)b_{P'}(u_{h-k})]+C_{m,P'}.           \tag{3}
\]
We need only \(b_{P'}(u)\le b_P(u)\); primes in \(S\) not dividing the particular \(q\) cause no problem. The coefficient two in (3) is independent of \(m\) and \(q\).

## A bounded count in a fixed packet, independent of its length

Put \(X_h=\log_2(q3^h)\). In a packet of \(m\) consecutive levels, all \(X\)'s differ by at most \(m\log_2 3\). The following counts hold whenever all \(X\)'s in the packet exceed a threshold depending on \(m,P,S,\delta\), uniformly in the source.

Consider first the real-small marks with \(|u_h|\le(q3^h)^{1-\delta/2}\). A negative such input makes the next state positive once the threshold is large, because its magnitude is less than \(q3^{h-1}\). Positivity then persists, so at most one such negative mark occurs. Between two positive real-small marks the initial odd injection gives
\[
                 2^d u_{h-k}\ge q3^{h-1}
                  \quad\Longrightarrow\quad d\ge(\delta/2)X_h-\log_2 3.
\]
If there are two or more positive real-small marks, the whole distance from the first to the last is at most \(4X_h+C_{m,P'}\) by (3). Consecutive selected dates are separated by at least \(\delta X_h/4\) for sufficiently large initial \(X_h\), even allowing variation across the packet. One may therefore bound the number of real-small marks by \(3+\lceil20/\delta\rceil\), independently of \(m\).

For any remaining mark counted on the left of (1), some fixed prime \(\ell\in P\) satisfies
\[
                v_\ell(u_h)\log_2\ell\ge\alpha X_h,\qquad
                                \alpha=\delta/(2|P|).
\]
Here \(\ell\nmid6q\), because the marked numerator is prime to \(6q\). For each such \(\ell\) select marks satisfying this valuation condition and the original bound on \(b_P(u_h)\). If two of them bound an interval as in (2), the \(\ell\)-part of \(V\) is at least \(2^{\alpha X_{h-k}}\), since \(\ell\nmid q3\). On the other hand \(\log_2 V\le d+O_m(1)\). Consequently successive selected marks are at least \(\alpha X_h/2\) native dates apart in the sufficiently high packet, measured against its first level. By (3) the full first-to-last distance is at most \(4X_h+C_{m,P'}\). This bounds their count by \(2+\lceil10/\alpha\rceil\) for each \(\ell\), regardless of \(m\). The argument used the common positive sum \(V\), including when the endpoints have opposite signs.

Let \(B=3+\lceil20/\delta\rceil+|P|(2+\lceil10/\alpha\rceil)\). For every fixed \(m\), every sufficiently high \(m\)-level packet has at most \(B\) bad marks. Partition any window into consecutive packets of length \(m\) and one possible remainder. The number of levels in packets below its fixed threshold is bounded in terms of that threshold and \(m\), because \(X_h\ge h\log_2 3\). Count the remainder by \(m\) and the other packets by \(Bw/m\). Choosing \(m>B/\epsilon\) proves (1). In particular, setting \(m=B+1\) shows that every such packet above its corresponding finite threshold contains at least one mark of the claimed cofactor height. The prime pool and the requested exponent are fixed before the limit.
