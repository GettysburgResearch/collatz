# An explicit coefficient with an ineffective period threshold

The proof of [native rotation separation](NATIVE_ROTATION_SEPARATION.md) also retains the coefficient of the actual source and denominator. Put \(\gamma=\log_2 3\), \(\beta=\gamma-1\), and \(\kappa=\gamma-2\beta=2-\gamma=\log_2(4/3)>0\). All logarithms here have base two.

For positive native paths whose \(2r\) departures are distinct and whose adjacent length-\(r\) division words differ at most \(s\) times, with \(s\) fixed,
\[
        \liminf_{r\to\infty}
        \frac{\log(y_0+q)+(2s+1)\log q}{r}\ \ge\ \kappa.               \tag{1}
\]
In particular \(\liminf\log(y_0+q)/r\ge \kappa/(2s+2)\). At \(q=1\) the stronger lower coefficient is **independent** of the fixed mismatch cutoff: \(\liminf\log(y_0+1)/r\ge\kappa\). The onset can depend on \(s\) in both statements.

Indeed, suppose the numerator in (1) is at most \((\kappa-\eta)r\) infinitely often, with \(\eta>0\). Then \(\log(y_0+q)=O(r)\), enough for every individual height, halving and effective-start bound in Sections 1–3 of the proof. In Section 4 the exact chronological row estimate is
\[
      2\beta r+\log(y_0+q)+(2k-1)\log q+O_s(\log(2r)),
\]
where the number of retained classes satisfies \(1\le k\le s+1\). Thus the row exponent is at most \((\gamma-\eta)r+O_s(\log(2r))\). Choose the terminal-date and box losses with \(\gamma(1-\delta)(1-\epsilon)>\gamma-\eta/2\). The same fixed rational forms give a contradiction. This proves (1).

For cyclic words, let \(z=\log q\), \(p\) be the native period, and set
\[
                  \rho_s=\frac{1}{4\cdot16^{s+1}}.
\]
For every family of primitive positive rational cycles with some native rotation of at most \(s\) mismatches,
\[
        \liminf_{p\to\infty}\frac{z}{p}
           \ \ge\ \frac{\kappa}{2s+2}\,\rho_s.                         \tag{2}
\]
To verify (2), suppose a sequence violates it by a fixed amount. At the minimum, the usual two-log bound in the main proof gives \(\log(y_0+q)\le z+O(\log p)\). Choose the smaller lag \(1\le r\le p/2\); retain a subsequence on which \(r/p\) converges. If its limit is at least \(\rho_s\), (1) implies (2). Otherwise eventually \(P=\max(1,r,\lceil\log(y_0+q)\rceil)\le\rho_s p\). Among \(s+1\) successive intervals \([u,16u)\) with \(u=16^jP\), \(0\le j\le s\), one contains no mismatched departure. All lie before \(p/2\). A repeated length \(R=r\lfloor 15u/(2r)\rfloor\) satisfies \(R\ge 15u/2-r\ge 13u/2\), and its two distinct sources give
\[
          (1-\beta)R\le\log(y_u+q)\le (1+\beta)u.
\]
This is impossible: \(\beta<3/5\) follows from \((3/2)^5<2^3\), so \((1-\beta)(13/2)>13/5>1+\beta\). This proves (2).

The exponent in (2) is explicit. For any strictly smaller positive coefficient the resulting eventual inequality has an ineffective period threshold. No effective lower function of period for the ordinary-cycle mismatch count follows from this proof.
