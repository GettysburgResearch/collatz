# Positive-population tests of the native entropy budget on one supplied ray

R6 asks for fair-coin large-deviation upper bounds for the first \(\lfloor\kappa\log_2N\rfloor\) shortcut parity letters of uniform \(n\le N\). We give true lower populations forced by the future of any one supplied positive integer. These remain meaningful when an upper estimate pays a subpower additive counting error, or when it is required only at thresholds with a positive fair counting exponent. The argument uses the actual continuation at that integer. It proves no unconditional upper bound on its odd frequency. [Polson–Sokolov R6 at the book pin](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex#L783-L785)

Write \(\theta=\log_2 3\), \(D=1-\theta/2\), \(\kappa_*=1/D\), \(I(x)=1-H_2(x)\), \(F_\kappa(x)=1-\kappa I(x)\). Let \(u\) be any limit of \(Q_m(a)/m\) along an increasing sequence for one fixed actual positive source \(a\). We may replace it by a fixed subsequent positive odd ternary unit, since a finite shift leaves this set of limits unchanged.

## An unbiased prefix already detects every violation of the literal one-source cutoff

Fix \(\kappa>1\) and \(0<\rho<\min(1,\kappa/\kappa_*)\). There is a sequence \(N_i\to\infty\) along which at least \(N_i^{\rho+o(1)}\) ordinary starts have full type tending to
\[
           p(\rho)=\frac{\kappa_*\rho}{2\kappa}
                    +\left(1-\frac{\kappa_*\rho}{\kappa}\right)u.       \tag{1}
\]
More precisely the assertion holds in every fixed neighborhood of \(p(\rho)\), with a positive target-dependent multiple of \(N_i^\rho\) starts.

Choose \(\log_2N_i=m_i/(\kappa-\kappa_*\rho)+O(1/N_i)\) for the specified tail subsequence. Within the proportional octave of \(n\asymp N_i^\rho\) in the positive-density first-hit basin of \(a\), first visit occurs at \(\kappa_*\rho\log_2 N_i+o_{\Pr}(\log N_i)\) and the prehit odd fraction tends to one half. These are the fixed-target natural clock theorem and its exact height identity. The residual clock differs from \(m_i\) by \(o_{\Pr}(\log N_i)\), over which the absolute possible cost in the count is at most that clock difference. This proves (1). [Fixed ordinary first-hit law and its analytic premises](../mass/FIXED_BASIN_NATIVE_WINDOW.md)

Suppose the postulated R6 upper holds even only at upper thresholds \(v>1/2\) where \(F_\kappa(v)>0\), in the form \(\#\{n\le N:Q_t(n)\ge vt\}\le N^{F_\kappa(v)+o(1)}\). For \(1<\kappa\le\kappa_*\) it follows for every supplied \(a\) that
\[
           \limsup_m Q_m(a)/m\le I_+^{-1}(1/\kappa),                  \tag{2}
\]
where the inverse uses \([1/2,1]\). Indeed if \(F_\kappa(u)<0\), then \(p(\rho)\) decreases continuously from \(u\) to \(1/2\) as \(\rho\) increases to \(\kappa/\kappa_*\). At the crossing where \(F_\kappa(p(\rho))=0\), one already has \(\rho>0\). Move slightly beyond it and take \(v<p(\rho)\) sufficiently close that \(0<F_\kappa(v)<\rho\), violating the stipulated estimate. If the R6 upper is imposed even when its predicted count is \(o(1)\), (2) has a simpler proof by using the single start \(a\). The content of (1)–(2) is that an anomalous fixed start forces a polynomial population even at an interior threshold where the fair population is itself polynomial.

## Exact-date inverse rows within a macroscopic source range

For a more localized test choose \(b\in(0.21,1/2)\), \(\alpha=(1-\theta b)^{-1}<\kappa\), and put
\[
      p_b=\frac{\alpha b+(\kappa-\alpha)u}{\kappa}.
\]
In every fixed neighborhood of \(p_b\), along a sequence of scales there are at least
\[
                 N^{\,1-\alpha I(b)-o(1)}                              \tag{3}
\]
ordinary starts. These have one identical native prefix date \(h\) and one identical odd count \(j\) at their visit to \(a\). Whenever \(a>1\) they lie in a fixed proportional interval at height \(N\). A further fixed shift to a unit \(a>1\) is available for any orbit with an upper-type anomaly, since the eventual \(1,2\) cycle has limit \(1/2\).

Take \(h_i=\lfloor\alpha m_i/(\kappa-\alpha)\rfloor\), \(j_i=\lfloor b h_i\rfloor\), \(N_i=\lceil a2^{h_i}3^{-j_i}\rceil\). Then \(\log_2N_i=h_i/\alpha+O_a(1)\), and the full clock leaves \(m_i+O_a(1)\) actual further steps. The supplied-state tilted exact-row theorem at this \(j_i,h_i\) yields \(\ge2^{h_iH_2(b)-j_i\theta-o(h_i)}\) distinct positive odd unit sources. The retained real inverse offset belongs to \([0,1]\), so each start is between \((a-1)2^{h_i}3^{-j_i}\) and \(a2^{h_i}3^{-j_i}\). This is a visit at a specified time, sufficient even for a periodic target. Substitution gives (3). The cited rate upper is for a minimum over supplied states; only its uniform lower is used here. [PR215 exact supplied positive rows, eq. (1)](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase4/TILTED_ENTROPY_TRANSFER.md) · [Certified parameter range and dependencies](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase4/EXTENDED_TILTED_INTERVAL.md)

At \(\kappa=\kappa_*\), this macroscopic-source test implies \(u\le 2/\theta-1/2=0.7618595\ldots\) under fair upper estimates near type \(1/2\). Indeed set \(e=1/2-b>0\), \(c=1/\theta-1/2\). Then \((\kappa_*-\alpha)/\alpha=e/c\) and
\[
                 p_b-\tfrac12=(\alpha/\kappa_*)e[(u-1/2)/c-1].
\]
The fair upper at thresholds tending to \(p_b>1/2\) requires \(\kappa_*I(p_b)\le\alpha I(b)\) by (3). Use \(I(1/2+x)=2x^2/\log2+O(x^4)\) and send \(e\downarrow0\). Whenever \(u>1/2+c\), this implies \((u-1/2)/c-1\le1\); the smaller \(u\) satisfy the claimed cap directly. At \(u=1/2+2c\) the inequality is valid for every \(b\) in this argument, because \(p_b-1/2=(\alpha/\kappa_*)e\) and convexity gives \(I(p_b)\le(\alpha/\kappa_*)I(1/2+e)\).

At the critical clock the all-threshold one-source cap in (2) is approximately \(0.76153\), slightly stronger numerically. The macroscopic-source argument uses only near-central **fixed** types, arbitrarily close to \(1/2\), and sources comparable in size to the cutoff. Neither conclusion reaches \(\log_3 2=0.63093\ldots\), the necessary lower limiting frequency of an escaping path. For \(\kappa>\kappa_*\) the separate supercritical law already shows that even an ordinary weak law of large numbers decides convergence under its positive-basin inputs. The scale-rounded number 4.82 in the book is slightly larger than the exact \(\kappa_*=4.81884\ldots\). [Prior critical and supercritical full-source criterion](../mass/CRITICAL_NATIVE_COUNT.md)
