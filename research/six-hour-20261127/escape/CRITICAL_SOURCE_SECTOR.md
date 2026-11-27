# A critical population of bounded real rational sources detects precisely escape

Let \(T(x)=x/2\) at an even numerator and \(T(x)=(3x+1)/2\) at an odd numerator for positive rationals of odd reduced denominator. Let \(g_i\) count the first \(i\) odd departures. Set
\[
 p=\log_3 2,\quad K=K_n=\lceil pn\rceil,\quad Q=2^n,\quad q=3^K,
 \quad W_j=\{2^i\le3^{g_i}\text{ for every }i\le j\}.                 \tag{1}
\]
Take \(n\ge1\). Use every integer numerator \(Q/2\le a<13Q/2\) coprime to 6 with the fixed denominator \(q\). In particular \(1/6<a/q<13/2\): the original rationals themselves lie in one bounded real interval at every depth. Let \(D_{n,L}\) count these sources passing \(W_{n+L}\) on their actual trajectory and put \(P_{n,L}=D_{n,L}/D_{n,0}\).

**Written theorem.** Condition uniformly on the sources counted by \(D_{n,0}\) and write \(z=T^n(a/q)\). Every \(z\) is a positive ordinary integer. For \(R\ge2\),
\[
 \sup_{n\ge1}\Pr(z\ge R)\ll (1+\log R)R^{-\beta},
 \qquad \beta=\log_3\frac p{1-p}.                                     \tag{2}
\]
In particular all moments of order \(0<s<\beta\) are uniformly bounded. This estimate holds without hypotheses on eventual Collatz behavior, even though there are passing words at zero final excess with unbounded real affine offset.

On the cited simple-orbit reciprocal packing estimate for the escape implication, the following are equivalent:
\[
 \begin{aligned}
 &\text{every positive ordinary trajectory is eventually periodic};\\
 &\lim_{L\to\infty}\sup_{n\ge1}P_{n,L}=0;\\
 &\lim_{L\to\infty}\liminf_{n\to\infty}P_{n,L}=0.                       \tag{3}
 \end{aligned}
\]
A single escaping positive integer would give \(\liminf_{n\to\infty}\inf_{L\ge0}P_{n,L}>0\). In (3) every finite positive cycle, including a hypothetical nontrivial cycle, lies on the vanishing side. The [earlier fixed 5/8 sector](RATIONAL_SOURCE_SECTOR.md) uses real starting heights growing with depth and detects both kinds of counterexample. At the critical value (1), the tightness proof needs a bound on the time spent near the gate and the lift onto a given escaping orbit needs control of the physical intercept.

## Physical words and the critical offset

For a binary word of length \(t\), write its bits \(e_i\), its prefix grades \(g_i=\sum_{j<i}e_j\), and
\[
 C_t=\sum_{i<t:e_i=1}2^i3^{g_t-g_{i+1}},\qquad
         2^tT^t(a/q)=3^{g_t}a/q+C_t.                                 \tag{4}
\]
Every word specifies one dyadic source residue modulo \(2^t\). At \(t=n\) let \(g_n=K+k\); then \(k\ge0\), and the exact terminal is
\[
             z={3^k a+C_n\over Q}.                                    \tag{5}
\]
A passing word starts odd, and the six consecutive numerator lifts of its residue in the stated half-open interval are odd. Since \(3\nmid Q\), exactly four are prime to three. Thus \(D_{n,0}\) is four times the number of gated words. The numerator congruence in (4) makes (5) an integer. No terminal probability is substituted for the source counting measure.

Write \(R_i=g_i-pi\) and \(V_n=\sum_{i=0}^n3^{-R_i}\). Directly from (4),
\[
 0\le {C_n\over Q3^k}
   ={3^K\over Q}\sum_{i<n:e_i=1}{2^i\over3^{g_{i+1}}}
   ={3^K\over3Q}\sum_{i<n:e_i=1}3^{-R_i}\le V_n,\qquad
 z\le3^k(13/2+V_n).                                                    \tag{6}
\]
The mechanical word with grades \(g_i=\lceil pi\rceil\) passes the gate and has \(k=0\). At each of its odd departures \(3^{-R_i}\ge1/3\), so \(C_n/Q\ge K/9\). A deterministic bounded-offset argument at critical slope would fail already on this word.

## A marked ballot estimate

All counting estimates below are proved here. The auxiliary independent-bit measure is used to count words, and then removed exactly. Uniformly in \(r\in[3/5,7/10]\), take iid bits of mean \(r\) and the centered walk with increments \(e_i-r\). Let \(G_t(x,y)\) be the probability of going from \(x\ge0\) to \(y\ge0\) in \(t\) ticks while staying nonnegative, with zero probability for inadmissible lattice points. Setting \(d_t=(t+1)^{-3/2}\), we first have
\[
                 G_t(x,y)\le C(x+1)(y+1)d_t.                          \tag{7}
\]
For one-sided survival to \(t\), stop on first exit from \([0,M)\) with \(M=1+\sqrt t\). The overshoots are at most one. For \(x<M\), the quadratic \((s+1)(M+1-s)\) has expected decrement \(r(1-r)\ge 1/5\) before exit, and is nonnegative before and at exit. Truncation gives \(\mathbb E\tau\le5(x+1)(M+1)\). The stopped linear martingale gives upper-exit probability at most \((x+1)/(M+1)\). Hence survival is \(O((x+1)/\sqrt{t+1})\), also for reversed signs and for \(x\ge M\). For the unconstrained middle block the binomial maximal atom is \(O((t+1)^{-1/2})\) uniformly; Fourier inversion and \(|1-r+re^{iu}|^2=1-4r(1-r)\sin^2(u/2)\) give this by a Gaussian integral on \([-\pi,\pi]\). Split into three blocks of comparable length, requiring forward survival of the first and reverse survival from \(y\) of the last. Conditional on both outer increments, the middle sum is fixed. Their three bounds multiply to (7). Bounded lengths, including \(t=0\), are covered by increasing \(C\).

For a walk from zero let \(L_n=\sum_{i=0}^n3^{-S_i}\) with \(S_i=g_i-ri\). There are absolute \(c,C'>0\) satisfying
\[
 \mathbb E_r[e^{cL_n};\ \min_{i\le n} S_i\ge0,\ S_n=y]
              \le C'(1+y)d_n.                                        \tag{8}
\]
Indeed, order the \(h\) marked times in \(L_n^h\), allowing ties at cost at most \(h!\). Split the constrained walk at all the marks and use (7) on its \(h+1\) segments, including zero-length segments. At each marked time the nonnegative heights run through a translate of the integers; the sum of \((1+s)^23^{-s}\) over that lattice is bounded by an absolute constant. The remaining factor from the terminal is \(1+y\). The convolution estimate \(\sum_{i=0}^n d_i d_{n-i}\le C_0d_n\) follows by splitting at \(n/2\) and summing \(d_i\). Iteration bounds the marked moment by \(h!C_1^{h+1}(1+y)d_n\). Summing its exponential generating function for \(c<1/C_1\) proves (8).

For \(r=p\), put \(\delta_n=K-pn\in[0,1)\), \(\lambda=(1-p)/p<1\). Every word ending at excess \(k\) has tilted probability \(2^{-nH_2(p)}\lambda^{-(k+\delta_n)}\). The total number of passing words is \(\asymp2^{nH_2(p)}d_n\). The upper bound is (7) after summing \((1+k)\lambda^k\). For the lower bound, rotate a grade-\(K\) word at the minimum of its centered partial sums for slope \(K/n\); the rotated word stays above this slope, hence passes (1). Each rotated word has at most \(n\) preimages. The near-central binomial coefficient \(\binom{n}{K}\asymp 2^{nH_2(p)}n^{-1/2}\) follows from Stirling, uniformly for the bounded rounding error. Equation (8) and the exact four lifts now give
\[
      \Pr(k=j,\ V_n>v)\le C_2(1+j)\lambda^j e^{-cv}
                   \quad(j\ge0,\ v\ge0),                             \tag{9}
\]
where \(V_n\ge1\). To infer (2), split at \(j_0=\lfloor\log_3R\rfloor\). The mass with \(j\ge j_0\) is \(O((1+j_0)\lambda^{j_0})\). For \(j=j_0-u<j_0\), (6) and (9) give the same quantity times \(O(\lambda^{-u}\exp(-c3^u))\), adjusting the constant for the fixed \(13/2\) and the first few \(u\). This sums, proving the uniform ordinary endpoint bound.

## Periodic states and the converse positive lift

After (5), the continuation gate is \(g_i(z)-pi+k+\delta_n\ge0\) for all \(i\le L\). Every positive shortcut cycle of length \(s\) and grade \(u\) has \(3^u<2^s\). There is at least one odd departure, so its intercept in (4) is strictly positive, and (4) returns to the same positive integer. Thus its grade deficit grows linearly over repeated laps and defeats every fixed finite slack, also after a finite transient. Under eventual periodicity of all integer orbits, all \(z\le R\) fail after a common additional finite clock, uniformly in \(n\), since (5) gives \(z\ge3^k/2\). The complement costs (2). Send \(R\to\infty\) to obtain the middle condition in (3).

Suppose instead that some positive orbit escapes. An unbounded nonperiodic orbit on the positive integers tends to infinity, since infinitely many returns to a finite set would repeat a state. On every simple orbit the reciprocal sum over its odd states is finite by the ordinary orbit interval-packing bound, so the forward product \(\rho_y=\prod_v(1+1/(3v))\) over future odd departures from a sufficiently late point \(y\) is at most two. Choose \(y\) so late that all its future states are at least 16. We may choose it arbitrarily large subject to these conditions. If \(g_i(y)\) is its actual grade, real telescoping gives
\[
     2^iT^i y=y3^{g_i(y)}\prod_{v\text{ odd before }i}(1+1/(3v)).
                                                                         \tag{10}
\]
Choose the unique integer \(h\) with \(29/8\le y/2^h<29/4\). Then (10) implies \(2^i\le 2^h3^{g_i(y)}\) at every future clock since \(2(y/2^h)<16\). Fix this point and \(h\) before sending \(n\to\infty\). The choices of \(y,h\) below may be made after all absolute constants have been fixed. [Simple-orbit reciprocal packing, Paper 175, (B) and its stated input](https://rstation.ai/problems/collatz/papers/175)

The point \(y\) will be the terminal at the **earlier** time \(t=n-h\), at grade exactly \(K\). It need not equal the ordinary terminal \(z=T^h y\) at time \(n\). To produce many sources hitting \(y\), take an initial run of \(b\) ones, a middle word of length \(m=n-h-b-8\) and grade \(l=K-b-5\), and one of the fixed terminal blocks
\[
                  v_4=11111000,\qquad v_3=11110100.
\]
Here \(b\) is one absolute integer selected below. Choose \(y\) sufficiently late that \(h\ge b+16\), which ensures \(r=l/m\ge p\) for all sufficiently large \(n\), with \(r\to p\). For the middle word require all prefixes above slope \(r\), and take
\[
  C_{\rm mid}/3^l=\sum_{i<m:e_i=1}2^i/3^{g_{i+1}}\le C_*             \tag{11}
\]
with a universal \(C_*\). There are \(\gg\binom{m}{l}/m\) such words uniformly for \(r\in[3/5,7/10]\) with \(r\ge p\). Indeed at slope \(r=l/m\) cyclic rotation gives probability \(\gg d_m\) of the nonnegative bridge ending at zero. The central binomial atom of this tilted walk is \(\gg1/\sqrt{m+1}\) uniformly by Stirling. Dividing (8) at \(y=0\) by that lower bound for the bridge event, at least half those bridges have \(L_m\le C_*\) with a universal \(C_*\). Since \(r\ge p\), \(2^i/3^{g_i}\le3^{-(g_i-ri)}\), giving (11).

Choose \(b\) such that \((1-p)b>8\) and \((2/3)^b(C_*+256)<1/32\). The initial run contributes exactly \(1-(2/3)^b\) to \(C_t/3^K\). The middle contribution is at most \((2/3)^b C_*\). The last eight bits contribute at most \((2/3)^b(2^m/3^l)255\le (2/3)^b255\). Thus for either terminal block
\[
             31/32\le C_t/3^K\le33/32.                                \tag{12}
\]
The first run and the middle stay above the critical gate; their accumulated surplus is at least \((1-p)b\), enough for the fixed last eight bits. The exact numerator at this earlier terminal is
\[
       a=2^{n-h}y-C_t,\qquad {a\over Q}={y\over2^h}
                         - {q\over Q}\,{C_t\over3^K}.                 \tag{13}
\]
Using \(1\le q/Q<3\), (12) and the choice of \(h\), this belongs to \([1/2,13/2)\). At the last odd position \(i\) of the length-\(t\) word, zero-based, \(t-i=4\) or 3 according to the displayed terminal block. Since \(C_t\equiv2^i\bmod3\), choose \(v_3\) if \(y\equiv1\bmod3\) and \(v_4\) otherwise to obtain \(3\nmid a\). Also \(a\) is odd since the word starts odd. The backward binary affine branches \(v\mapsto2v\) and \(v\mapsto(2v-1)/3\) over odd denominators force the indicated departure bits. All intermediate values are positive because the full inverse gives the positive source (13) and each prescribed forward affine branch preserves positivity.

At the earlier landing the bank is \(K-pt=\delta_n+ph\), enough for the full future word by (10). Different middle words give different numerators by determinism. For fixed \(h,b\), cancelling factorials gives
\[
 {\binom{n-h-b-8}{K-b-5}\over\binom nK}
          \longrightarrow p^{b+5}(1-p)^{h+3}>0 .
\]
The word lower bound (11), the four-lift upper bound on \(D_{n,0}\), and \(m/n\to1\) give \(\liminf_n\inf_L P_{n,L}>0\). The absolute construction constants do not give a uniform positive lower fraction over escaping starting points; it depends on the selected late \(y\). This proves (3).

## The corresponding ordinary binary harmonic test

Use the exact gate (1) in the [binary harmonic construction](../BINARY_PREFIX_CRITERION.md). At length \(n\) sum \(1/r\) over the ordinary integers \(1\le r<2^n\) passing all prefixes. As in its stopped-shell proof, the union over depths has \(O(X^{H_2(p)})\) members through height \(X\). Their reciprocals are summable, so dominated convergence gives in the limit the sum of \(1/r\) over actual ordinary starts passing (1) forever. Each eventual cycle fails (1) by its strict lap deficit. On any escaping orbit the cumulative surplus in logarithms is
\[
       g_i\log 3-i\log2=\log(T^i y/y)-\log\rho_{y,i}\to+\infty
\]
by (10) and simple-orbit reciprocal packing. It attains a global minimum at a finite clock; the tail following that clock passes the exact critical gate forever. Hence this harmonic sum tends to zero exactly when no ordinary orbit escapes. It does not count a possible nontrivial periodic orbit. A small critical mass at one depth excludes persistent starts of a given bounded height. An escaping start with that bound may first attain its global surplus minimum later at a larger integer.

The [Lean interfaces](CriticalSourceSector.lean) prove the exact integer critical-grade equivalence, denominator interval, finite suffix comparison, strict positive lap deficit, exhaustion of any fixed natural slack over repeated laps, and concatenation of a prepaid integer debt. The ballot estimates, positive population transfer and infinite conclusions are written proofs. The [integer controls](check_critical_source_sector.py) reconstruct every passing word at depths 5, 8, 12, 16 and 20, scan the complete original rational population through depth 12, check the mechanical offsets at depths through 2048, and execute three positive reduced lifts through their earlier landing at depth 457. The recorded finite tests impose no eventual fate condition. [Retained output](CRITICAL_SECTOR_CONTROLS.json)
