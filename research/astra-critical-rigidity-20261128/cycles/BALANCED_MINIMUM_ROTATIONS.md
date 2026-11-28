# Large balanced-minimum ratio forces separation at every odd rotation

**PROPOSED.** A primitive positive rational Collatz cycle has odd states \(x_i=y_i/q\), common full reduced denominator \(q\), odd period \(p\), division exponents \(e_i\), total clock \(A=\sum e_i\), and minimum \(m\). For the same displayed clocks \((p,A)\) let \(m_{\rm bal}\) be the minimum of the positive rational cycle with balanced exponents
\[
  e_i^{\rm bal}=\lfloor(i+1)A/p\rfloor-\lfloor iA/p\rfloor,\qquad 0\le i<p .
\]
The balanced comparison may have smaller primitive period. Write \(s=s(\ell)\) for the number of unequal native exponents at a proper odd lag \(\ell\), and \(M=p/\gcd(\ell,p)\) for the order of that lag.

**Full rational denominators.** Fix \(\epsilon>0\). Along growing periods and minima, cycles with \(m/m_{\rm bal}\ge1/2+\epsilon\) satisfy, simultaneously at every proper lag,
\[
                  s(\ell)(\log_2 q+\log_2 p)\gg_\epsilon p.               \tag{1}
\]
Thus a bounded mismatch count gives an exponential lower bound on the *entire* reduced denominator for every such sequence, with no bound on the largest exponent, physical width or rotation order. Along sequences with \(s(\log q+\log p)=o(p)\), a fixed order \(M\) gives \(\limsup m/m_{\rm bal}\le1/M\), while orders tending to infinity give \(m/m_{\rm bal}\to0\).

**Ordinary cycles.** The written large-period implication with the classical two-logarithm estimate alone uses the same threshold \(1/2\). Using also the sparse-window theorem at the pinned PR213 source below, every fixed \(\epsilon>0\) gives
\[
 \frac m{m_{\rm bal}}\ge \frac{0.96355}{2}+\epsilon
  \quad\Longrightarrow\quad
       \min_{0<\ell<p}s(\ell)\gg_\epsilon p/\log p                         \tag{2}
\]
on sufficiently large positive primitive integer cycles. In the fixed-order counterpart, the upper bound on \(\limsup m/m_{\rm bal}\) is strictly below \(0.96355/M\). These are conditional restrictions on all rotations of one candidate. A low minimum compared to the balanced cycle remains possible. The unrestricted bound on the minimum ratio in PR213 was below \(0.96355\).

## The balanced comparison and a uniform height cap

Put \(\gamma=\log_2 3\), \(\lambda=\log2\) and \(\theta=A/p\). The exact positive lap product gives
\[
 \theta-\gamma=\frac1p\sum_i\log_2(1+(3x_i)^{-1}) .
\]
At growing minima, \(\theta\to\gamma\). The same clocks hold on the balanced cycle by its exact periodic realizer. The circular prefixes of every rotation of the floor exponents have sums equal to either the floor prefix at zero or that prefix plus one. The positive carry formula at each cut therefore gives all balanced states in \([m_{\rm bal},2m_{\rm bal})\), with the least value attained at the floor cut. This holds unchanged with repeated displayed phases. Since \(\theta\to\gamma\), the same lap product forces \(m_{\rm bal}\to\infty\).

On a genuine odd segment with all states at least \(m\), the angle \(\{\log_2(x/m)\}\) advances by \(\gamma+O(1/m)\) modulo one. The uniform empirical angular laws of the balanced cycles therefore converge to Haar. For each nonzero Fourier character, telescoping around the lap gives multiplication by \(e^{2\pi i k\gamma}\ne1\) up to \(O_k(1/m_{\rm bal})\), forcing its mean to zero. As the balanced heights occupy one octave, this gives
\[
 3\lambda m_{\rm bal}(\theta-\gamma)\longrightarrow
      \int_0^1 2^{-t}\,dt=\frac1{2\lambda}.
\]
The function on the circle has one jump and the limiting measure has no atom there. On the proposed cycle the analogous Taylor expansion gives
\[
         \frac{m}{m_{\rm bal}} =
           2\lambda\,\frac1p\sum_i m/x_i+o(1).                           \tag{3}
\]
The estimate is uniform in the maximum because all reciprocal heights are at most \(1/m\).

Theorem 1 of Bondareva, Luchin and Salikhov, used with integer coefficients \((A,-p,0)\), gives \(m\ll p^{5.116201}\) from \(0<A\log2-p\log3\le p/(3m)\) and \(A\asymp p\). This applies to positive rationals as well; denominators do not occur in their lap product. Use the single cutoff \(Y=p^7\) at all orders. It has \(m/Y=o(1)\). [BLS, Theorem 1, printed p. 18](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&option_lang=eng&paperid=619&what=fullt)

## The lowest track is a genuine orbit between rare joins

First fix an order \(M\), write \(d=p/M\), and suppose \(s(\log q+\log p)=o(p)\). In each base column \(r\bmod d\) put
\[
                       z_r=\min_{0\le j<M}x_{r+jd}.
\]
Let \(K\le s/2\) count the variable exponent columns. On a nonvariable column the map to the next column is the same positive-slope affine map on all \(M\) states. It sends the unique minimum to the next minimum, including the permuted cell labels at the wrap. Thus the cyclic list \(z_r\) has at most \(K\) joins that can fail its genuine ordinary or rational odd edge. The points in this list are pairwise distinct.

Apply the block argument of [rotation occupation](ROTATION_OCCUPATION.md), with \(T=\lfloor\log_2(qY)\rfloor\) (positive eventually). At most \(KT\) columns belong to common blocks of length at most \(T\). In each remaining column every state except possibly its minimum exceeds \(Y\). Consequently the exact inequalities are
\[
 0\le\sum_i m/x_i-\sum_r m/z_r
        \le (M-1)KT+(p-d)m/Y.                                           \tag{4}
\]
The normalized right side is \(o(1)\) after division by \(p\), since \(M\) is fixed. This controls the entire reciprocal occupation, including unbounded peaks.

At all but \(K\) of the \(d\) column steps the folded angles of \(z_r\) advance by \(\gamma+O(1/m)\). In the character argument the join error is at most \(2K/d\), which tends to zero. Their empirical angles converge to Haar. In particular
\[
 \frac1d\sum_r m/z_r\le\frac1d\sum_r2^{-\{\log_2(z_r/m)\}}
                     \longrightarrow\frac1{2\lambda}
\]
where the arrow concerns the upper sum. Equations (3) and (4) give the claimed bound \(1/M\), even when the total accumulated angular error of the entire physical lap is not known to tend to zero.

## The unbounded-order alternative

Now suppose \(M\to\infty\) and still \(s(\log q+\log p)=o(p)\). At every fixed \(J\ge2\), the unrestricted translate estimate (1) of [rotation occupation](ROTATION_OCCUPATION.md) gives
\[
 \limsup D_Y/p\le 1/J,\qquad D_Y=\#\{i:x_i\le Y\},
\]
because eventually \(J\le M\) and \(s\log(qY)=o(p)\). Taking arbitrarily large fixed \(J\) gives \(D_Y/p\to0\). Since \(p^{-1}\sum_i m/x_i\le D_Y/p +m/Y\), (3) gives \(m/m_{\rm bal}\to0\). No fixed-order remainder was taken to be uniform as \(M\) grew.

If (1) failed uniformly at arbitrarily large periods and minima, take a sequence with the left side divided by \(p\) tending to zero and choose its offending lags. The integer orders have a constant subsequence or a subsequence tending to infinity. Both contradict the lower margin above one-half. This gives the asserted positive constant as well as the fixed-mismatch denominator consequence.

## A stronger ordinary threshold by retaining the first and last physical states of each window

For a positive integer cycle, define \(G(x)=\lfloor\log_2(x/m)\rfloor\), \(f(x)=\{\log_2(x/m)\}\), and the bounded cost \(D(x)=(1-2^{-G(x)})2^{-f(x)}\). The cited PR213 finite-window proof gives the following *count* on the true cycle. For an absolute \(u>263/10000\), at most \(o(p)\) actual origins have mean \(D\)-cost at most \(u\) over the next \(n=\lceil\log_3 m\rceil+2\) observed odd states. It obtains \(u\) from the strict inequality
\[
             6u+\frac1{32}\log\!\left(\frac{209707481425}{34359738368}\right)
                          < \frac{\log3}{5.116201}.
\]
The source counts distinct ordinary origins after fixed trims, accounts for high endpoints, and verifies the positive transfer-operator bound in its finite certificate. Its stronger low-cost-window count, before averaging the whole cycle, is essential here. An average over the full cycle alone would not pass to selected phases. [PR213, exact source and finite bound](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/ODD_HEIGHT_PRESSURE.md) · [reciprocal-cost verifier at the same pin](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/check_odd_height_pressure.py)

On a fixed-order sequence with \(s\log p=o(p)\), the low-envelope word has at most \((n-1)K=o(d)\) length-\(n\) windows crossing a join. Every other window follows the actual ordinary orbit of its distinct initial phase for all \(n\) observed states. Hence only \(o(d)\) low-envelope origins can have mean cost at most \(u\). Averaging these overlapping windows around the \(d\)-cycle counts each selected cost exactly \(n\) times. Its mean \(D\)-cost has lower limit at least \(u\). By Haar convergence of the low-envelope angles,
\[
 \limsup\frac1d\sum_r m/z_r\le\frac1{2\lambda}-u .
\]
Combining with (3) and (4) gives an upper limit at most \((1-2\lambda u)/M<0.96355/M\). Growing least periods of ordinary positive cycles force growing minima because each fixed minimum specifies one deterministic orbit. The sequential order split above proves (2).

The numerical strengthening uses the pinned pressure certificate as a written dependency; the basic half-threshold and its full rational-denominator extension do not. Neither bound settles cycles with arbitrarily small balanced-minimum ratios and largely superpolynomial odd heights.

[Exact native controls](check_balanced_envelopes.py) · [Recorded counts](balanced_envelope_controls.json). The control checks 175 balanced references, including 80 imprimitive displays, the minimum-track joins and all retained physical windows, and 3,679 finite reciprocal-mass caps. The asymptotic constants use the written inputs above.
