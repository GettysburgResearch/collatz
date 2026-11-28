# A finite positive Hausdorff gauge for the full nonmerging set

Use the canonical states and physical shortcut clock of [the critical-gauge result](CRITICAL_MERGER_HAUSDORFF.md). For a fixed integer state \(z=(s,D)\) let \(E_z\subset\mathbb Z_2\) consist of the bases whose adjusted pair never absorbs. Leen's harmonic capacity is \(h(z)=s+\mathbb E_z M\), where \(M\) counts level-zero departures. For large integer \(t\) take
\[
       \psi(2^{-t})=2^{-t}\sqrt{t\log\log t}.
\]
Only the large-depth values matter in the dyadic metric. There are absolute constants \(0<c<C<\infty\) such that
\[
                  c h(z)\ \le\ \mathcal H^\psi(E_z)\ \le\ C h(z).       \tag{1}
\]
The result applies to the whole survivor, including histories of zero probability under the capacity law. In particular it gives a finite positive measure for the nonmerging bases of \((x,3x)\) and for the restriction to odd bases. Removing exceptional physical coincidences of unequal slopes changes the set by at most countably many points. Any gauge whose ratio to \(\psi\) tends to zero gives zero measure, and one whose ratio tends to infinity gives infinite measure on every live starting state. No universal ordinary source assertion follows.

## Imported facts about positive excursions

Let \(R\) be the first return to zero from a fixed positive level. A genuine excursion begins just after a level-zero departure; its initial level is one. Include the initial positive excursion with its actual starting level \(s\), when present. We use the following written results of Leen in addition to the cylinder and capacity identities.

* The physical tail satisfies \(\mathbb P_{j,D}(R>n)\le Cj/\sqrt n\) for all positive levels \(j\) and all integer offsets \(D\). The total time outside positive excursions before absorption has finite mean from each fixed integer state. These are the fixed-return lemma's uniform envelope and the boundary coast estimates. [Exact rates, October 9, 2026](https://doi.org/10.5281/zenodo.23268751)
* From a level-zero state of offset \(d\), \(\mathbb E\exp(\lambda_\alpha M)\le C_\alpha(1+|d|^\alpha)\) for any fixed \(0<\alpha<1\) and some \(\lambda_\alpha>0\). From a fixed positive state the offset of its first return has finite \(\alpha\)-moment. Conditioning there gives a finite exponential moment for \(M\) at every fixed integer state. [Late synchronization, “Exponential moments of all departures”](https://doi.org/10.5281/zenodo.23268753) · [Exact rates, return moments](https://doi.org/10.5281/zenodo.23268751)
* At positive level \(j\), equal-parity holding steps keep the level fixed. The next mixed step raises or lowers the level by one with equal Haar probabilities. Its waiting time, counting the mixed step, is stochastically bounded above by \(v_2(3^j-1)+G\), with \(G\) a geometric variable on \(1,2,\ldots\) of success probability \(1/2\). In the six-row kernel, an offset valuation below \(v_2(3^j-1)\) decreases by one at either holding branch. Above or at that threshold a fair trial has at least probability one half to drop below it. Once the offset is odd the next step is mixed. This proves the conditional stochastic bound uniformly in the arriving offset. [Quantitative synchronization, “Holding times and the level walk”](https://doi.org/10.5281/zenodo.23268755)

Treat a positive excursion killed at zero as having level zero forever after killing. Its level is a nonnegative martingale under Haar. Weighting each labelled history by the terminal level divided by its initial positive level \(s\) defines its infinite probability law \(Q^\uparrow_{s,D}\). It stays positive. Holding branches are unchanged. At successive mixed steps, the embedded levels \(J_i\) start at \(s\) and move from \(j\) up and down with probabilities \((j+1)/(2j)\) and \((j-1)/(2j)\). This follows by conditioning at the first mixed move: its wait has the preceding uniform tail, the next fair direction is tilted by \((j\pm1)/j\), and those two weights average one. In particular the same conditional holding bound holds under \(Q^\uparrow\). Let \(\sigma_n\) be the physical date just after the \(n\)-th mixed move.

## An upper tail for the physical clock under the infinite law

For some absolute \(C_0,C_1\), every \(n\) sufficiently large with \(s\le n\), and every initial offset,
\[
                 Q^\uparrow_{s,D}(\sigma_n>C_0n)\le C_1 n^{-3}.         \tag{2}
\]
For the embedded walk, its length-\(n\) law is a simple symmetric walk from \(s\), killed on reaching zero, tilted by its terminal position divided by \(s\). The Radon–Nikodym factor against the unrestricted simple walk is at most \((s+n)/s\le n+1\).

For a free walk \(Y_i\) on \(\mathbb Z\), write \(L_n(m)=\sum_{i<n}\mathbf 1_{m\mid Y_i}\). On residues modulo \(m\), the centered function \(\mathbf 1_{x=0}-1/m\) has the form \((I-P)f\), \(P\) the simple-walk transition operator, with \(|f(x+1)-f(x)|\le2\) and oscillation at most \(2m\). Indeed the successive differences of \(f\) change by \(-2(\mathbf 1_{x=0}-1/m)\) around one period. Choose their additive constant to give them mean zero, then sum them to obtain a periodic \(f\). The accumulated centered count is the difference of two endpoint values plus a martingale with increments bounded by two. Azuma's inequality therefore gives, simultaneously at all \(m=2^k\le n^{1/4}\),
\[
            |L_n(m)-n/m|\le 2m+C\sqrt{n\log n}
\]
except on free probability \(O(n^{-6})\), on choosing absolute \(C\) large enough. The terminal tilt above changes the exception to \(O(n^{-5})\).

On a retained positive walk \(1\le J_i\le2n\). Sum the occupancy bounds for powers of two through \(m_*=2^{\lfloor\log_2(n)/4\rfloor}\). All remaining valuation levels contribute at most \(\log_2(2n)L_n(m_*)=o(n)\). Thus \(\sum_{i<n} v_2(J_i)\le n+o(n)\) on the retained event. The holding allowance satisfies \(v_2(3^j-1)\le2+v_2(j)\). Conditional geometric domination gives a fixed finite exponential moment for the positive part of each wait minus this allowance. Iterated conditioning and exponential Markov bound the sum of these positive parts by \(C'n\) outside \(O(e^{-cn})\). This proves (2) with absolute constants. Independence of waits across successive levels is unnecessary.

## A quantitative chance of crossing a high boundary in one surviving excursion

There are absolute constants \(a,c,\eta>0\) such that, for fixed positive initial level \(s\), uniformly over \(D\), at all sufficiently large \(t\) with \(s\le t^{9/10}/2\),
\[
\begin{split}
 Q^\uparrow_{s,D}\{s_u<a\sqrt{u\log\log u}\text{ for all integer }t^{9/10}\le u\le t/4\}
                    &\le C\exp[-c(\log t)^\eta].                        \tag{3}
\end{split}
\]
In (3), \(s_u\) refers to raw time. Use mixed epochs \(n=2^j\) from \(2t^{9/10}\) to \(t/(4C_0)\). These supply a positive multiple of \(\log t\) disjoint direction blocks \((n/2,n]\) for large \(t\). The embedded transition has up probability at least one half. Coupling each direction to a fresh fair sign by a uniform random number gives conditional probability at least \(c j^{-1/2}\) that
\[
                         J_n\ge b\sqrt{n\log j},
\]
for an absolute sufficiently small \(b>0\). Indeed the fair sum over \(n/2\) signs exceeds that threshold with this lower bound. To check it directly, sum its binomial probabilities over the admissible-parity sites in \([b\sqrt{n\log j}, b\sqrt{n\log j}+\sqrt n]\). Stirling's inequalities give each a lower bound \(c n^{-1/2}\exp[-C(b\sqrt{\log j}+1)^2]\); the cubic remainder is bounded here since \(n=2^j\). Reducing \(b\) makes the summed bound at least \(c j^{-1/2}\) for large \(j\). Coupling works after every starting level because \(J_{n/2}>0\). The probability of missing every direction-block opportunity is at most \(\prod_j(1-c j^{-1/2})\le C\exp[-c'\sqrt{\log t}]\). By (2), except on \(O(t^{-2})\), every physical epoch under consideration lies between \(n\) and \(C_0 n\). On this event a successful block gives a physical exceedance in (3), with \(a\) chosen small relative to \(b/\sqrt{C_0}\). This proves (3).

For a Haar excursion originating at raw time zero, (3) also bounds the probability of surviving its first \(t/2\) physical steps without a high level at those interior dates. Condition at local time \(\lfloor t/4\rfloor\). Leen's uniform first-return tail bounds the remaining survival probability by \(C s_{\lfloor t/4\rfloor}/\sqrt t\), with zero contribution if already killed. Integrate this actual level tilt. The resulting bound is
\[
                  Cs\,t^{-1/2}\exp[-c(\log t)^\eta].                   \tag{4}
\]
Changing strict inequalities or fixed integer roundings has no effect if the tested high threshold is reduced by a fixed factor.

## Paying all residual live cylinders

At an arbitrary fixed live starting state write \(I\) for all the positive excursion intervals before eventual Haar absorption. Include the initial positive interval when applicable. Their count is at most \(M+1\); the expected sum of their initial levels is \(h(z)\). Write \(B_0\) for the total number of raw steps before absorption outside those positive excursion intervals, including boundary coasts and any departure steps not counted in an interval. The boundary coast estimates and the finite mean of \(M\) give \(\mathbb E_z B_0<\infty\). Put \(u=t^{7/10}\). Three exceptional events together have Haar probability \(o_z(1/\sqrt{t\log\log t})\):

1. \(M>C_z\log t\), by the fixed-state exponential moment.
2. \(B_0>t^{4/5}\), by Markov's inequality.
3. At least two intervals in \(I\) have length greater than \(u\). The probability that any one is long is \(O_z(u^{-1/2})\), by summing the uniform first-return bounds at the actual entries. On a later entry an earlier completed long interval is known. Charging each later index once, its conditional chance to be long is at most \(C/\sqrt u\) because every later interval starts at level one. Hence the probability of two longs is at most
\[
  C u^{-1/2}\mathbb E_z[(M+1)\mathbf1_{\{\mathrm{some\ long}\}}]
               \ll_z u^{-1/2} (u^{-1/2})^{3/4}=O_z(t^{-49/80}),
\]
using the fourth moment. The exponent \(49/80\) exceeds \(1/2\).

Outside these events, if the pair is still live at \(t\), precisely one interval must account for at least \(t-t^{4/5}-(C_z\log t+1)t^{7/10}\) elapsed steps by date \(t\). Its starting date \(k\) is at most \(t^{4/5}+(C_z\log t+1)t^{7/10}<t^{17/20}\). The interval survives its first \(t/2\) steps. For each local time \(t^{9/10}\le v\le t/4\), its global date satisfies \(v\le k+v\le2v\). Thus if the global level stays below \(a'\sqrt{w\log\log w}\) for all dates \(n_0\le w\le t\), (4) applies with \(a'\) sufficiently smaller than \(a\), for each fixed \(n_0\) and all large \(t\). Sum (4) at all possible labelled entries with their Haar weights, including the initial term of weight \(s\). The resulting factor is \(h(z)\). Consequently
\[
 \sqrt{t\log\log t}\ \mathbb P_z\{A>t,\ s_w<a'\sqrt{w\log\log w}
                         \text{ for all }n_0\le w\le t\}\longrightarrow0.    \tag{5}
\]
This is an estimate for the whole unresolved finite-level cover, beyond the almost-sure statement under a changed probability law.

Stop all cylinders after depth \(n_0\) when their first high level is attained. Their weights under the capacity law are \(2^{-w}h(z_w)/h(z)\ge a'\psi(2^{-w})/h(z)\), so their total gauge cost is at most \(h(z)/a'\). Fill all remaining live cylinders at level \(t\). Their total cost tends to zero by (5). First take \(t\to\infty\), then \(n_0\to\infty\), proving the upper bound of (1).

## Positive measure and the complement of the critical case

For completeness, in one immortal positive excursion the maximum embedded level through \(n\) moves has, for \(H\ge4s+4\), a tail \(Q^\uparrow(\max_{i\le n}J_i\ge H)\le C\exp[-c H^2/n]\). Stop at level \(H\): the density against the killed fair walk then is \(H/s\). To reach \(H\), that walk must first hit \(\lfloor H/2\rfloor\) before zero, an event of probability \(s/\lfloor H/2\rfloor\), and then gain the remaining distance within \(n\) steps. The free maximum obeys the usual reflection or exponential-martingale bound. Multiplication proves the stated tail. At \(n=2^j\) choose \(H=C_2\sqrt{2^j\log j}\), with \(C_2\) an absolute sufficiently large constant, and use Borel–Cantelli. Holding does not raise the level, and the number of mixed moves is at most the raw clock. It follows that \(s_t\le C_3\sqrt{t\log\log t}\) eventually \(Q^\uparrow\)-almost surely, with absolute \(C_3\). On the subset where the inequality holds for every \(t\ge n_0\), all intersecting cylinders at such depths have \(Q^\uparrow\)-mass at most \(C_3\psi(2^{-t})/s\). For large \(n_0\) this subset has mass at least one half. The mass distribution bound gives at least \(s/(2C_3)\) Hausdorff measure to the bases whose first positive excursion lasts forever.

In the full process take this forever-positive subset at each possible genuine departure, and also at the initial positive excursion if present. These sets are Borel and disjoint: an infinite positive excursion has a unique start. Extending a fixed labelled word of length \(k\) acts on binary cylinders by a similarity of factor \(2^{-k}\). The gauge satisfies \(\psi(2^{-(n+k)})/\psi(2^{-n})\to2^{-k}\), so each fixed departure contributes at least its Haar cylinder mass times the absolute one-level lower constant. Countable additivity gives the lower bound \(ch(z)\). The odd restriction on \((x,3x)\) is its first odd cylinder followed by the live state \((1,-1)\). This completes (1). The positive-excursion lower bound and the critical power transition were developed jointly with the ordinary lane. This deduction imports the stated pair-process results, without relying on a physical-clock law of the iterated logarithm or rebuilding their Lean sources.
