# The supercritical return experiment at true Collatz gates

Let $\mathcal P$ be the strict future parity gate, $D=\log(4/3)$, and $d_1$ the ordinary density of the predecessor basin of $1$. A return means passage from one member of $\mathcal P$ to the next one on its genuine positive shortcut path. Missing returns have a cemetery symbol. From ordinary $\mathcal P\cap[X,2X)$, the limiting probability of completing $a=a(X)$ successive returns is
\[
 \begin{cases}
 1-d_1(1-e^{-t^2/2}),&
          a/\sqrt{2\log X/D}\to t\in[0,\infty),\\
 1-d_1,& a/\sqrt{\log X}\to\infty.
 \end{cases}                                                           \tag{1}
\]
Thus success in the second regime measures the entire counterexample density, including possible nontrivial cycles. Every return outcome through $a$ returns or through the absorbing alternative $1$ is determined by an actual trajectory of at most $C(\log(2X)+a)$ shortcut steps. The gate membership tests on this trajectory are separately finite by the exact parity record bound. The limiting identification (1) uses the source-qualified physical laws in [sharp gate sampling](SHARP_TRUE_GATE_SAMPLING.md).

## Uniform singularity of the supercritical word law

There is a finite deterministic estimate for every distribution supported on $\mathcal P\cap[1,2X]$, for every $a\ge1$. The total variation distance between its first $a$ complete return words (including cemetery) and $a$ independent Catalan excursion words is at least
\[
                 1-2\exp[-c a^2/(\log(2X)+a)]                         \tag{2}
\]
for an absolute $c>0$. This estimate needs no assumptions on the fate or density of the starting set.

Indeed, if the returns are completed in $q$ odd and $s$ shortcut departures, the suffix-floor level goes up exactly $a$, so $s=2q-a$. All these odd departures have values $v\ge3$, since the cycle $1,2$ contains no true gate. The odd affine product to the endpoint $y$ satisfies
\[
 1\le y=n\,3^q2^{-s}\prod_v(1+1/(3v))
      \le n\,2^a(5/6)^q .
\]
Therefore $q\le H=(\log(2X)+a\log2)/\log(6/5)$. This same bound applies to the prefix stopped at $1$ before $a$ returns: both endpoints have $g=0$ and its surplus is the number of gate departures, at most $a$. Starting from a gate, the next gate or $1$ occurs in finite time by the balanced-return argument, including on an escaping orbit. Hence the full experiment always stops and $s\le2H$. To perform the ancillary exact test at all visited sites, a single extended native prefix still suffices: the visited heights up to $2H$ are at most $(3/2)^{2H}(2X+1)$, and the additional parity-record lookahead at every site is bounded by a constant times the logarithm of that common maximum. [Actual gate transitions and effective record horizon](../cycles/RARE_ODD_ASCENTS.md)

For a fair independent Catalan word, reverse the $2q-1$ signed shortcut letters to get a simple symmetric walk's segment before its first hit of $+1$. The internal partial sums of that reversal are at most zero, since the unreversed positive prefixes have values at least one. Each word has exactly its fair native probability $2^{1-2q}$. Concatenating $a$ independent segments therefore gives the random walk up to its first hit of $a$, by independence after each first hit. Under that law $\sum q_i\le H$ implies a hit of $a$ within $2H$ fair ticks. The exponential maximal inequality for the walk bounds this probability by $2\exp(-a^2/(4H+2))$. The event “some return is missing or the completed odd length is at most $H$” has true probability one. This proves (2). In [the subcritical Palm law](TRUE_GATE_PALM_WORDS.md) the same word total variation tends to zero for $a=o(\sqrt{\log X})$ in each positive-mass component. Equation (2) rules out extending an independent-word comparison above the square-root scale even when one conditions on a hypothetical escaping component.

## Gate count on entry into the known cycle

Sample a start uniformly among $\mathcal P\cap B_1\cap[X,2X)$ and let $\tau$ be its first native visit to $1$. The exact gate count $G$ of departures before $\tau$ equals $b_\tau$ because $g(1)=g(n)=0$. Then
\[
 \frac{G}{\sqrt{2\log X/D}}\ \Longrightarrow\ R,
       \qquad \Pr(R>t)=e^{-t^2/2}\quad(t\ge0).                        \tag{3}
\]
Here is the retained terminal statistic required to justify conditioning on the rare gate. At a physical output $y$ in the middle-block argument proving sharp sampling, retain not only $g(y)$ but also $b_{\tau_y}(y)$ on $B_1$, with $\tau_y$ the actual first hit of $1$. For ordinary starts in this basin the two marks divided by $\sqrt{2\log Y/D}$ converge to $(-\min B,B_1^{\rm BM})$ for standard Brownian motion on $[0,1]$. This is exactly the incoming physical path and its future floor at the terminal supplied root; $B_1^{\rm BM}$ here denotes the Brownian endpoint. The same law holds at fixed ternary residue, including the restriction that $y$ is odd. Indeed neighboring starts fuse within $o(\sqrt{\log Y})$ dates off a set of proportion $o(1)$ by the counted merger. If their first hits occur after this date, their remaining path is identical, and both terminal surpluses differ by $o(\sqrt{\log Y})$. Early target visits cost $o(1)$. The half-normal floor marks have the same fixed-shift bound. Natural octaves extend to fixed proportional intervals as in the sharp theorem. The joint limiting cumulative distribution is continuous because both marginals are continuous, so convergence is uniform over the two thresholds. The $L^1$ finite-trit approximation to $\rho_m$ again keeps this limit in the physical tests.

At actual initial surplus $z$, middle centered total $w$, add the terminal test $z-w+b_{\tau_y}(y)\le t\sqrt{2\log X/D}$ to the existing test $g(y)<z-w$. It involves only the true output marks after the two complete blocks. The pair-minimum full-column estimate, endpoint strip bracketing, compact clock tail removal and core-word conditional bridge proof are unchanged. The final Brownian comparison is a fair geometric walk of $N=\lfloor\log X/D\rfloor$ odd gaps, required to remain strictly positive and to finish at height at most $t\sqrt{2N}$. Indeed its last independent Brownian motion supplies its negative minimum and terminal value jointly, with the same restriction and total surplus. All boundary tests have limiting mass zero; the independent initial Rayleigh height also has a continuous distribution. The strict ballot formula $\pi_N(s)(2N-s)_+/N$ in the sharp proof yields precisely the Rayleigh endpoint conditional on survival. This proves (3) including the physical output's dependence between its future deficit and endpoint. The argument does not infer a conditional weak limit merely from an unconditioned Brownian approximation to a probability tending to zero.

Exactly $G-1$ further returns are possible from a starting gate in $B_1$; the initial site is already its first gate and $1$ is not a gate. In every other component there are infinitely many future gates. On an escaping orbit this follows from the positive lower asymptotic gate frequency. On any different odd cycle of period $p$ all its odd values are at least $3$, and its total shortcut count $s$ satisfies $2^s=\prod_{i<p}(3+1/x_i)\le(10/3)^p<4^p$. Its positive centered increment $2p-s$ over one lap is the integer number of true gate departures there, by the suffix-floor cocycle; visiting the cycle guarantees infinitely many. Finally [sharp gate sampling](SHARP_TRUE_GATE_SAMPLING.md) gives mass $d_1$ to $B_1$ under the gate sampler. Combining these facts proves (1), using tightness from (3) at the endpoint $t=\infty$. Equation (2) gives no corresponding upper bound for success: it forces even successful real words into a region rare under the independent excursion law.
