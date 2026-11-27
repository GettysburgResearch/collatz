# Finite integer labels in dyadic equidistribution of the joint law

Let \(X=(R,Z)\) have the stationary real and ternary affine law for the fair shortcut maps. Use the compact group \(S=(\mathbb R\times\mathbb Q_3)/\operatorname{diag}\mathbb Z[1/3]\), with fundamental domain \([0,1)\times\mathbb Z_3\), quotient map \(\pi\), normalized Haar probability \(m_S\), and the metric of Weaver’s quotient theorem. On its cover with lattice \(m\operatorname{diag}\mathbb Z[1/3]\), where \(m\) is a positive integer prime to three, integer diagonals retain their labels modulo \(m\). Dividing both coordinates by \(m\) identifies this cover with \(S\).

The dyadically expanded measure on this identified cover satisfies
\[
 W_1\!\left(\mathcal L\big(\pi(2^n X/m)\big),m_S\right)
   \ll \frac{\sqrt{\log(n+2)+\log m}}{(n+1)^{1/4}}.                 \tag{1}
\]
There is also a bound retaining the physical unit intervals in the original cover. In the identified fundamental domain let \(\mathcal P_{m,r}\) record the real bin of width \(1/(m3^r)\) and the ternary residue at depth \(r\). It records both the unit-interval label in \([0,m)\) and the extra real resolution \(3^{-r}\) there. For an integer \(t\ge1\), put \(k=r+\lceil\log_3 m\rceil+t\). Provided \(k\le n/4\),
\[
 \left\|\mathcal P_{m,r}\mathcal L\big(\pi(2^n X/m)\big)
              -\mathcal P_{m,r}m_S\right\|_{\rm TV}
 \ll \sqrt{\frac{k(\log(n+2)+\log m)}{\sqrt{n+1}}}+3^{-t}.          \tag{2}
\]
In particular the labels and any fixed extra resolution become asymptotically uniform for \(\log m=o(n^{1/4})\). This extends the argument for \(m=1\) in [Weaver 19, §10.6, (Q1)–(Q6)](https://rstation.ai/problems/collatz/papers/19).

To prove the estimates, use the original unprojected stationarity and a fair native word \(w\) of length \(n\). Iteration gives
\[
 2^n X\ \overset{\rm law}=3^{J(w)}X'+B(w),
\]
where \(B(w)\) is an integer diagonal, \(J(w)\) is the odd count with the binomial law \(\operatorname{Bin}(n,1/2)\), and \(X'\) is independent with the law of \(X\). The translation by \(B(w)/m\) on \(S\) is an isometry. No independence of \(J(w)\) and \(B(w)\) is required.

Let \(\delta_i\ge0\) be the single-digit conditional entropy deficits of the successive ternary digits of \(\{R/m\}\), relative to \(\log3\). They satisfy
\[
 \sum_{i\le N}\delta_i\le C\log(N+2)+\log m .
\]
Indeed an interval of real length \(3^{-N}\) for \(R/m\) has probability at most \(C m3^{-N}(N+1)\) by the real concentration estimate (Q7); when \(m3^{-N}>1\) this bound holds trivially. The entropy of the full integer cell index is at least minus the logarithm of its maximum probability. Removing \(\lfloor R/m\rfloor=\lfloor\lfloor R\rfloor/m\rfloor\) costs at most the finite entropy of \(\lfloor R\rfloor\), from the fractional moment used in (Q4).

For \(j\ge k\), let \(\lambda_j=\mathcal L(\pi(3^j X'/m))\). Since \(Z/m\in\mathbb Z_3\), the two depth-\(k\) cell coordinates in the ordinary ternary grid \(\mathcal Q_k\) are the \(2k\) successive real digits from \(j-k+1\) through \(j+k\), with the lower-coordinate block negated modulo \(3^k\). Thus the grid entropy deficit is at most the sum of those single-digit deficits. For \(j<k\), use the trivial bound \(2k\log3\). Since \(J\) has maximum atom \(O((n+1)^{-1/2})\), its lower tail below \(n/4\) is exponentially small, and each index can occur in at most \(2k\) of the windows, one obtains
\[
 \mathbb E_J D_{\rm KL}(\mathcal Q_k\lambda_J\Vert\mathcal Q_k m_S)
 \ll \frac{k(\log(n+2)+\log m)}{\sqrt{n+1}}
 \qquad(1\le k\le n/4).
\]
This estimates the average of the unmixed deficits, which matters since the translations can depend on the count. Pinsker’s inequality, Jensen’s inequality, and the nested-cell Lipschitz approximation from (Q2) bound \(\mathbb E_J W_1(\lambda_J,m_S)\) by the right side of (1). Isometric translation and convexity then prove (1).

For (2), translation by \(B(w)/m\) permutes the cells of \(\mathcal P_{m,r}\) exactly. The carry into the ternary residue is constant on each real bin. For any union of these cells, approximate from inside and outside by unions of \(\mathcal Q_k\) cells. The two approximations differ in Haar mass by \(O(m3^{r-k})\), by counting the real boundary intervals; the ternary cells refine exactly. Therefore its probability under \(\lambda_j\) differs from Haar by \(O(m3^{r-k})+\|\mathcal Q_k\lambda_j-\mathcal Q_km_S\|_{\rm TV}\). Average, use the permutations, and insert the preceding entropy estimate to obtain (2).

These are written deductions for the specified stationary word law from the cited concentration, finite-entropy and stationarity inputs. Even on this cover, estimating a fixed original arithmetic fibre at ternary depth \(d\) requires relative control on a mass of order \(3^{-d}\) at a fixed root. Neither (1) nor (2) supplies that relative control at the Poisson clock \(n\asymp d\). For the special dyadic choice \(m=2^s\le2^n\), the identified measure in (1) is exactly the ordinary quotient law at time \(n-s\). At \(s=n\) it is the original singular stationary quotient law, independently of \(n\). This gives an explicit limit to an unqualified uniform-cover Haar claim.
