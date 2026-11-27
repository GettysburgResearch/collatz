# A small positive one-site perturbation retaining the Gaussian input laws

**Countermodel for inference from the population laws.** Given a finite height cutoff \(H\) and \(\epsilon>0\), one can change the ordinary shortcut map at exactly one odd site \(a>H\). Its new successor exceeds the genuine successor by strictly less than a relative \(\epsilon\). Its one-step log correction \(\log(2T'(a)/(3a))\) is strictly positive and can be made smaller than \(\epsilon\). The altered map has a second positive cycle entirely above \(H\), with a strictly positive but arbitrarily small average affine correction. Every sufficiently high first-landing label is unchanged pointwise. The every-fixed-target Gaussian arrival law continues to hold with its corresponding actual basin density. Both cycles attract positive natural populations under the same source imports used for the genuine map.

This strengthens the earlier example that changed the odd successor to the gate itself. Here the changed odd step grows the input, its log correction retains the genuine positive sign, and all computations concern actual positive integer sources on the modified map. This is a countermodel to a proposed implication, with the arithmetic change given explicitly. [PR211, one-site fixed-point construction](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/ONE_SITE_MUTANT.md)

## An exact ordinary path returning to the gate

Choose \(q\ge1\), \(P>q\) with
\[
                3/2<r=2^P/3^q<(3/2)(1+\delta)
\]
for an arbitrarily small fixed \(\delta>0\). These pairs exist with arbitrarily large \(q\) since \(\log_2 3\) is irrational and its positive integer multiples are dense modulo one. Take \(P\) the smallest integer strictly above \(q\log_2 3+\log_2(3/2)\), choosing the fractional part sufficiently close to one.

The powers of four run through the \(3^q\) residues congruent to one modulo three in \(\mathbb Z/3^{q+1}\mathbb Z\). Indeed \(v_3(4^{3^i}-1)=i+1\) by the binomial expansion or the elementary lifting identity for the cube. Choose arbitrarily large \(k\) so that the odd gate
\[
     a=(4^k-1)/3\equiv -2^{q-P}\pmod{3^q}.
\]
The negative power of two means its modular inverse. In particular \(3\nmid a\). Its genuine successor is \(2^{2k-1}\), followed by even divisions and then the known cycle. Define the positive odd integer
\[
       b=2^q\frac{2^{P-q}a+1}{3^q}-1
          =ra+(2/3)^q-1 .
\]
For \(k\) large one has \(b>(3a+1)/2\), and \(b/((3a+1)/2)\to 2r/3\). Choose \(\delta\) sufficiently small that this relative change and \(\log(2b/(3a))\) meet the stated requirements. The altered map agrees with the genuine one off \(a\) and sets \(T'(a)=b\).

For the odd shortcut, \(T(x)+1=(3/2)(x+1)\). The integer \(b+1\) has exact two-adic valuation \(q\), since \(2^{P-q}a+1\) is odd. Thus \(b\) takes exactly \(q\) consecutive genuine odd steps to \(2^{P-q}a\), then \(P-q\) even steps to \(a\). Its odd sites increase strictly from \(b>a\), and its intervening positive even sites exceed \(a\). They are all distinct, so the new cycle has minimal period \(P+1\), exactly \(q+1\) odd departures, and minimum \(a\). Its average exact log correction is
\[
    A'=\log2-\frac{q+1}{P+1}\log3
            =\frac{\log(2r/3)}{P+1}>0 .
\]
All even updates and all other odd updates remain exactly genuine. By decreasing \(\delta\) one can impose the elementary odd-step upper ratio \(2T'(x)/x\le 10/3\) at every \(x\ge3\). Increasing \(k\) protects any fixed finite list of preverified trajectories.

## Which population laws survive

Write \(C_a\) for the new cycle, \(S\) for the finite union of \(C_a\) and the full genuine future of \(a\), and \(P(y),\tau_y\) for genuine ancestors and first-hit clocks. Every orbit is unchanged until the first visit to \(a\). The two futures then remain in their respective finite subsets of \(S\). An original odd or even source is allowed in each statement.

- If \(y\notin S\), its ancestors and their first-hit clocks are identical. The ancestors of \(a\) and their clocks are also unchanged. If \(y\in C_a\setminus\{a\}\), its genuine future reaches \(a\) in a fixed time and its genuine predecessors satisfy \(P(y)\subset P(a)\). The new basin is \(P(a)\). On \(P(y)\) use the unchanged first visit to \(y\), and on \(P(a)\setminus P(y)\) use \(\tau_a+\tau'_y(a)\). The restricted timed count for \(\tau_a\) on \(P(y)\) equals the timed count for \(\tau_y\) with the fixed added time \(\tau_a(y)\).
- A genuine future site \(y\in S\setminus C_a\) has \(P(a)\subset P(y)\). No source visiting both can hit \(y\) before \(a\), because \(y\) never reaches \(a\) on its genuine path. Its modified basin is therefore exactly \(P(y)\setminus P(a)\). The times on the retained basin are unchanged, and the deleted timed count is \(\tau_a+\tau_y(a)\) on \(P(a)\). The two finite futures intersect only at \(a\): the genuine future after \(a\) consists of powers of two, and every even site of the new future contains the factor \(a>1\).
- Apply the genuine every-target formula (A.8) to these finite sums and differences. A fixed additive clock shift preserves the Gaussian limit by continuity. For each fixed target the modified law is exactly \(d'_y\Phi(z)\) in the same normalization, with \(d'_y\) its actual modified basin density. Select another gate \(a'=(4^\ell-1)/3\) with \(3\nmid\ell\), large enough that its genuine future passes through every power of two in the true future of \(a\). The two genuine gates never see each other and their basins are disjoint. All sources in \(P(a')\) still reach the known cycle. Positivity of both \(P(a)\) and \(P(a')\) follows from the positive-predecessor input. In particular all previously positive fixed-target densities remain positive, also for the affected powers of two. [Population inputs and shortcut conventions](CRITICAL_CORRECTION.md)
- If the two orbits of a source ever diverge, both forward heights after that time belong to \(S\). Thus the supremum over **all times** of the absolute difference of their log heights is bounded by a constant depending only on the chosen gate. The density-one macroscopic log-height theorem therefore transfers. Every altered minimum is either the genuine one on a source never visiting \(a\), or at most \(a\). Minimum tightness transfers as well.
- For every \(R\ge a\), the first odd state at most \(R\), including failure, is identical on every integer for the two maps. Reaching the changed odd site already constitutes a landing. For \(R<a\), each changed source lies in \(P(a)\) and its resulting small-cutoff label can be compared using its first fixed-target tests. Only the exact high-cutoff agreement is needed in the two-scale theorem.
- The complete first-meeting clock of the earlier packet is identical for all starts above \(\max S\). Before entry in \(S\), each visited state's ancestors are identical. At entry, the state itself supplies a smaller visitor, since it is below the original source. If no entry occurs, all tested ancestors and both full source paths agree forever. At any fixed bounded time, all ordinary parity-window densities are identical too, because only finitely many sources can hit the altered gate by that time.

On a simple path the altered log correction has the genuine harmonic upper bound plus a constant, since a departure from \(a\) can occur only once. On repeated laps all odd-site log corrections are strictly positive; the nontrivial cycle mean may be made arbitrarily small. Consequently the new map obeys the source hypotheses and arithmetic estimates used for the full critical-window derivation. It gives strict loss in the lower Gaussian tail test even though its first-landing law at every sufficiently large scale is pointwise the original one. Any argument that evaluated this test from those data alone would also apply to this countermodel. A proof of saturation for the genuine map needs an input that distinguishes its exact update at the changed site.
