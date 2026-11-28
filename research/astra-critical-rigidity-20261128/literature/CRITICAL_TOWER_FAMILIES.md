# Critical families of powers and the size of an actual endpoint fibre

Keep the towers, notation, full cutoff \(t=\lfloor\log_2 N\rfloor\), fixed \(c,M\), and arbitrary exponent origin of the [critical endpoint profile](CRITICAL_TOWER_ENDPOINT_PROFILE.md). The probability below is the fraction of the \(N\) consecutive exponent starts under consideration. Let \(k/\sqrt t\to\lambda\in(0,\infty)\). Write \(p(\lambda)=2[1-\Phi(\sqrt2\lambda)]=\operatorname{erfc}(\lambda)\) for the limiting probability the two outer endpoints coincide. All conclusions are uniform over interval origins and the two tower directions.

1. For any deterministic set \(I_N\subseteq\{0,\ldots,k\}\) containing both endpoints and of cardinality \(o(\sqrt t)\), the probability that **all of its marked tower members** have the same actual value at date \(t\) tends to \(p(\lambda)\). The positions may vary arbitrarily with \(N\).
2. When both outer endpoints at date \(t\) agree, let \(B_N\) count the intervening members **of the entire consecutive block** which miss that value. Put \(B_N=0\) otherwise. For every \(H\ge2\),
\[
          \limsup_{N\to\infty}\sup_a\Pr(B_N>H)\ll_{c,M,\lambda}H^{-2/3}.
                                                                            \tag{1}
\]
Since \(p(\lambda)>0\), the number missing is tight also conditionally on actual outer endpoint fusion. An exact entire-block success probability at positive critical \(\lambda\) is not obtained by setting \(H=0\).
3. For the actual numerical endpoint multiplicities \(m_y=\#\{a\le n<a+N:T^t(X_n^\pm)=y\}\) one has
\[
                 \frac{\sum_y m_y^2}{N\sqrt t}\longrightarrow\frac2{\sqrt\pi}.
                                                                            \tag{2}
\]
Thus the mean size of the fibre seen by a uniformly sampled exponent is asymptotic to \(2\sqrt{t/\pi}\). The number of distinct endpoints has lower bound \((\sqrt\pi/2-o(1))N/\sqrt t\), strengthening the lower constant from the [single-grade count](DISTINCT_TOWER_ENDPOINTS.md).

An exact finite instance separates full-block from endpoint fusion. At native date 16 the five consecutive inputs \(3^{19},\ldots,3^{23}\) have respective values \(116357384,116357384,349072151,3141649355,116357384\). The two outer paths have synchronized while two interior paths have different endpoints.

## A return-to-zero order argument

Work first on a full Haar base \(x\) and the affine family \(x_i=c+3^i(x-c)\), \(0\le i\le k\). In the descending tower the indices are read in the other direction, taking the largest denominator index as \(x_0\). The adjusted grade at date \(u\) is \(L_i(u)=i+g_u(x_i)\), where \(g_u\) counts actual odd inputs. For \(i<j\) write \(R_{ij}\) for the first equality of those two adjusted grades, and \(A_{ij}\) for canonical absorption. Before its first equality, the signed difference \(L_j-L_i\) is positive and changes by at most one per date. Hence, on \(R_{0k}\le v\), for each \(0<i<k\),
\[
                   R_{0i}\le v\quad\hbox{or}\quad R_{ik}\le v.           \tag{3}
\]
Indeed, otherwise both strict inequalities would persist at the date where the two outer adjusted grades meet. This elementary fact concerns the relative grades; it does not presume order of real orbit values.

For any affine pair in this family its canonical initial level is the exponent gap \(r\), its offset is \((1-3^r)c\), and its first base is Haar since multiplication by an odd power of three preserves that measure. Leen's [raw return moment and remaining-absorption estimate](https://doi.org/10.5281/zenodo.23268751) give, uniformly over all such pairs and gaps,
\[
                         \Pr(A_{ij}-R_{ij}>l)\le C_c/\sqrt l .           \tag{4}
\]
Indeed \(|(1-3^r)c|/3^r\le |c|\), the return offset has uniformly bounded fractional moment, and the remaining tail from it at level zero is at most \(C(1+|D|^p)/\sqrt l\). When the initial Haar law is conditioned on the fixed pair of cosets used by the actual tower, every event probability in (4) grows by at most the fixed reciprocal mass of that set. No conditioning on a selected crossing or on successful outer fusion is needed.

Fix \(0<\delta<1/2\), and put \(v=\lfloor(1-\delta)t\rfloor\). If \(A_{0k}\le v\), then (3) holds for every interior mark. If that mark is missing at \(t\), one of the two comparisons in (3) has reached zero by \(v\) but has failed to absorb by \(t\). Its contribution has unconditional probability at most \(2C_{c,M}/\sqrt{t-v}\). More formally these restricted events, with both dates bounded by \(t\), are unions of depth-\(t\) cylinders. Synchronized canonical pairs remain synchronized at all subsequent dates. The conditional Haar bound for any such union transfers to the uniform exponent interval with factor at most \(1+P_t/N\le2\), even when the intervening index and endpoints move. Unequal-slope coincidences of the outer pair on special actual inputs cost only \(O_{c,M}(t+1)/N\).

By the critical profile at deadlines \(v,t\) (the same proof uses \(v\le t\) and \(k/\sqrt v\to\lambda/\sqrt{1-\delta}\)), the upper limiting probability of an outer absorption in \((v,t]\) is at most a fixed multiple of
\[
        p(\lambda)-p(\lambda/\sqrt{1-\delta})=O_\lambda(\delta).
\]
Equivalently use the conditional Haar difference of the two nested events and the empirical full-period majorant. Summing (4) over \(o(\sqrt t)\) marked indices gives \(o_\delta(1)\); then let \(\delta\downarrow0\). Together with the matching outer upper bound this proves assertion 1. For the full consecutive block, the early-outer probability multiplied by the conditional expected number missing, equivalently the expectation restricted to that early event, is at most \(O_{c,M,\lambda}(\delta^{-1/2})\). Markov and the late-outer bound give \(O(\delta+H^{-1}\delta^{-1/2})\). Taking \(\delta\) proportional to \(H^{-2/3}\), capped below \(1/2\), proves (1).

## Counting actual equal pairs

The left numerator of (2) counts ordered pairs of exponents with the same actual endpoint, including the diagonal. For lag \(k\) in \([\varepsilon\sqrt t,L\sqrt t]\), the fraction of agreeing endpoint pairs converges to \(p(k/\sqrt t)\) uniformly in the lag and in the exponent origin, for every fixed \(0<\varepsilon<L\). Otherwise extract a subsequence along which \(k/\sqrt t\) converges in that compact interval and apply the continuous critical profile. Discarding at most \(k\) terminal indices changes each fraction by at most \(k/N\) when forming pairs internal to the interval. Lags below \(\varepsilon\sqrt t\) have total unordered contribution at most \(\varepsilon N\sqrt t\).

For larger lags through \(t\), the [two-arm grade bound](TERNARY_TOWER_SYNCHRONIZATION.md) is at most \(C_M\exp[-k^2/(2t)]+O_{c,M}(t/N)\). The summed additive error and interval-end losses are \(O_{c,M}(t^2)\). Two exponent indices above \(C_{c,M}(t+1)\) cannot coincide at a lag beyond \(t\), since numerical equality then requires a grade difference equal to the lag. In particular, in every actual endpoint fibre the indices above that cutoff have diameter at most \(t\), hence number at most \(t+1\). The \(O_{c,M}(t+1)\) indices below the cutoff contribute only \(O_{c,M}(t^2)\) equal pairs in total including all their arbitrarily distant high partners. This avoids paying for a possible exceptional coincidence separately at each of the \(N\) lags.

After division by \(N\sqrt t\), let \(\varepsilon\downarrow0\) and \(L\to\infty\). The Gaussian envelope pays the omitted high lags, and the compact Riemann sums give \(\int_0^\infty p(u)du=1/\sqrt\pi\). There are two orders per positive lag, and the diagonal \(N\) contributes \(o(N\sqrt t)\). This proves (2). Finally Cauchy–Schwarz gives \(\#\{y:m_y>0\}\ge N^2/\sum_y m_y^2\).
