# Critical merger counts on arbitrary intervals of ordinary positive integers

Let \(t=\lfloor\log_2 N\rfloor\) and take \(s=s_N\ge1\), \(D=D_N\in\mathbb Z\). Let \(I\) be any interval of \(N\) consecutive positive integers on which \(3^s x+D>0\); one may also use the signed shortcut map without this last condition. For uniform \(x\in I\), compare the **actual** positive starting integers \(x,3^s x+D\) at the same native date \(t\). Put \(z=D/3^s\), \(\gamma=\log_2 3\) and \(b=1-\gamma/2=0.2075187496\ldots\).

* If \(s/\sqrt t\to\lambda\in(0,\infty)\) and \(\log(2+|z|)=o(t)\), then their probability of **numerical nonmerger** converges, uniformly in the interval position, to \(2\Phi(\sqrt2\lambda)-1\). In particular all offsets with normalized size \(N^{o(1)}\) are allowed.
* For every fixed \(\varepsilon>0\), if \(|z|\ge 2^{(b+\varepsilon)t}\), their probability of numerical merger is \(O_\varepsilon(N^{-c_\varepsilon})\) for some \(c_\varepsilon>0\). This second assertion is uniform in all \(s,D,I\) satisfying the size condition; the slope need not be at its critical value. Thus on genuine positive integers a large enough normalized real offset suppresses the critical merger profile.

The gap between subpolynomial offsets and the large-offset regime is left open. Both assertions concern a count over every interval, including changing intervals at very large origins, and give no claim about the later intersection of one specified pair.

## Upgrading the growing-level clock to subpolynomial normalized offsets

For a Haar-uniform base the [moving-level first-return proof](CRITICAL_TOWER_ENDPOINT_PROFILE.md) gives the displayed Brownian tail for its first zero-grade-difference time \(R\), uniformly along \(s/\sqrt t\to\lambda\), with arbitrary incoming offset. Only the final passage from that return to full canonical absorption \(A\) used a real-size condition. Leen's raw return bound gives, for fixed \(0<p<1\) and \(0<r<1\), \(\mathbb E|U|^p\le r^s|z|^p+C\) at the raw return offset \(U\). His stronger level-zero theorem “Uniform pair absorption” gives
\[
 \Pr_{0,U}(A>l)\le C\sqrt{(1+\log(1+|U|))/l}.
\]
By concavity, \(\mathbb E\log(1+|U|)\le p^{-1}\log(1+\mathbb E|U|^p)\), then Jensen for the square root gives
\[
                \Pr(A-R>l)\le C_p\sqrt{(1+\log(2+|z|))/l}.             \tag{1}
\]
Under the first assertion's hypothesis this is \(o(1)\) at each \(l=\lfloor\eta t\rfloor\), \(\eta>0\). The continuous first-return profile therefore also holds at full absorption. [Leen, *Exact rates in Collatz synchronization*, raw and coasted return moments, and uniform pair absorption](https://doi.org/10.5281/zenodo.23268751)

The canonical survival event at date \(j\) is a union of residues modulo \(2^j\). Its empirical probability on \(I\) at \(j=t-\lceil2\log_2(t+2)\rceil\) differs from its Haar probability by at most \(2^j/N\). At the two depths \(t,j\), for the same initial \(s,D\), the survival probabilities have the same limiting profile. The additional absorptions through \(t\) have empirical fraction at most \((1+2^t/N)\) times the Haar difference, which tends to zero. This proves the first conclusion for canonical absorption. [Leen, exact labelled cylinders](https://doi.org/10.5281/zenodo.23268755)

## Removing accidental numerical equalities uniformly in the offset

For a length-\(t\) parity word write its odd grade as \(g\) and its carry as \(C\ge0\). At its odd dates \(0\le u_1<\dots<u_g<t\),
\[
              C/3^g=\sum_{j=1}^g 2^{u_j}/3^j\le 2^{t-g}.                \tag{2}
\]
Indeed \(u_j\le t-g+j-1\), and the sum of \((2/3)^j\) over \(j\ge1\) is two. Two endpoint words with grades \(g_1,g_2\) and carries \(C_1,C_2\) give numerical equality just when
\[
   (3^{g_1}-3^{s+g_2})x=3^{g_2}D+C_2-C_1.                              \tag{3}
\]
If the slopes agree, equality is equality of the two affine functions on the whole source cylinder, which is canonical absorption by \(t\). If they differ, the absolute coefficient on the left is at least \((2/3)\max(3^{g_1},3^{s+g_2})\). For each of the \((t+1)^2\) possible grade pairs, all unequal-slope coincidences for which both grades are at least \(t/4\) are consequently within distance \(3\cdot2^{3t/4}\) of the single real center
\[
                          3^{g_2}D/(3^{g_1}-3^{s+g_2}).
\]
The size or sign of \(D\) changes the centers but does not change the length of these intervals.

For either arm the \(2^t\) source residues run once through all binary words of length \(t\) on a full residue period, since \(3^s\) is odd. For every word event its observed probability in any \(I\) is at most \((1+2^t/N)\) times its fair-bit probability. The low-grade exception costs \(O(e^{-ct})\) by Hoeffding. Counting the displayed real intervals, the total fraction of coincidences with unequal slopes is at most
\[
                   O(e^{-ct})+O((t+1)^2 2^{3t/4}/N)=O(N^{-c'})          \tag{4}
\]
for an absolute \(c'>0\), uniformly in all \(s,D,I\). This proves the first assertion for true numerical mergers.

Finally fix \(\delta>0\). Apart from probability \(O_\delta(t e^{-c_\delta t})\), each prefix of each arm satisfies \(|g_u-u/2|\le\delta t\) at all \(0\le u\le t\), by the same period majorant, Hoeffding, and a union bound. Just before its \(j\)-th odd date, \(j\ge u_j/2-\delta t\); therefore
\[
       C/3^g\le 2^{\gamma\delta t}\sum_{u=0}^{t-1}2^{bu}
                     \le C_0 2^{(b+\gamma\delta)t}.
\]
In an equal-slope numerical merger, (3) would force \(|D|/3^s\le C_1/3^{g_1}+C_2/3^{g_2}\). Choose \(\gamma\delta<\varepsilon/2\). The good-word estimate precludes this equality under the large-offset hypothesis for all sufficiently large \(N\). Combining its exceptional mass with (4) proves the second assertion. For example one can keep both inputs positive throughout by taking large positive integer offsets.
