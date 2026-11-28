# Joint first-landing clocks and physical labels at arbitrary source separation

**Source-qualified written theorem.** The complete joint local template and circular total-variation formula (1)–(2) in [the mesoscopic clock theorem](MESOSCOPIC_LANDING_CLOCK.md) hold whenever $B\to\infty$ and $v=\log(X/B)\to\infty$, with no bound on the growth of either parameter relative to the other. They hold for actual uniform positive odds and also for all positive starts in the original octave $[X,2X)$, recording the entire shortcut clock to the first odd landing. The proof uses [PR195, signed ordinary initial trit cancellation with exact native total, (3)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md) and the mesoscopic theorem. The scalar renewal setup follows [PR213, relative landing](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md). Here the exact moving **time** is kept as an output coordinate and matched across every scale. In particular the result does not follow simply by applying the older unmarked relative estimate to the pair of observables.

With $D=\log(4/3)$, $P=\log3$, $b=\log2$, $\mu=D/2$, put $\sigma^2=P^2/(4\mu^3)$ and let $f_s$ be the continuous Gaussian density with mean $s/\mu$ and variance $\sigma^2s$, evaluated at an integer date. If $W(r)=P e^r1_{[0,b)}(r)$ periodically modulo $P$, the conclusion for arbitrarily large separation is
\[
 p_{B,X}(y,t)\ \simeq\ \frac2B g(y/B,y) f_v(t) W(tb+\log(y/B)-v).    \tag{1}
\]
Precisely, for every $\epsilon>0$ the fixed template $g$ can be chosen so that the limsup of the sum of all absolute discrepancies, including cemetery, is below $\epsilon$. This is a statement on individual integer labels and dates. The limiting variation distance for the source dilation $X\mapsto e^cX$ is the circular translate discrepancy in the mesoscopic theorem, for every fixed $c$.

## A one-step estimate that preserves both coordinates

Take the shortcut $T(n)=n/2$ on even $n$ and $(3n+1)/2$ on odd $n$. Let $A(n)$ denote the pair of true first odd label $\le B$ and its shortcut time, or the single cemetery state. Denote by $S$ the operator shifting every finite clock by one and fixing cemetery. For all positive starts write the vector with raw normalization
\[
             F_v=(Be^v)^{-1}\sum_{Be^v\le n<2Be^v}\delta_{A(n)}.
\]
It differs in sum norm from the uniformly normalized law by $O((Be^v)^{-1})$ for $Be^v\gg1$. At every sufficiently large $v$, uniformly in $B$ and for every fixed $A>0$,
\[
   \left\|F_v-\tfrac12 S F_{v-b}-\tfrac12 S F_{v+P-b}\right\|_1
                  \ll_A (1+v)^{-A}.                                  \tag{2}
\]

Here is the marked source argument. On any odd source interval $I\subseteq[Z,2Z]$, with $w=\log(Z/B)$ large, take $k=\lfloor c w\rfloor$ for a sufficiently small fixed $c$. Then $k\le(\log_2 Z)/32$ and $Z2^{-4k}\ge B e^{w/2}$. For any mean-zero function $\psi$ on $\mathbb Z/3$ of modulus at most one, the input (3) of PR195 bounds by $O_A(k^{-A})$ the sum norm of $\sum_{n\in I}\psi(n) f_k(n)\delta_{(s,z)}/n$ at the literal odd endpoint $z=U^k(n)$ and accumulated division total $s$. The restriction $s>4k$ has unsigned reciprocal mass $O(e^{-c'k}+2^{4k+1}/Z)$ by parity counting. Before or at this short prefix every good state is above $B$, and $1-f_k(n)\ll k/(Z2^{-4k})$. Send each $(s,z)$ to the true first odd landing of $z$, adding $s$ to its remaining native time and fixing cemetery on failure. The deterministic map contracts mass norm. On the good sources this is precisely $A(n)$, with its initial time included. Thus the signed measure with weights $1/n$ at $A(n)$ is $O_A(w^{-A})$ on every subinterval. Partial summation removes $1/n$, giving the same bound for the weights $1/Z$. All parity estimates used here are statements about high starting odd integers.

On all positive integers split off the exact initial $2^a$ for each start. The source trit function becomes $\psi(2^a n)$ on odds, still centered, and the time gets the additional $a$; the law on failure stays at cemetery. For $ab\le w/2$ the remaining scale has logarithmic separation at least $w/2$, and after its natural normalization the prefactor is $2^{-a}$. The other coasts have total mass $O(e^{-c w}+Z^{-1})$, since all those inputs are divisible by the first excluded power of two. This proves the same centered-trit estimate for $A(n)$ on any high octave or subinterval of it with all starts.

In the raw sum defining $F_v$, each source must take a step because $n>B$. The even contribution is exactly $S F_{v-b}/2$. The odd image $m=(3n+1)/2$ runs over the class $m\equiv2\pmod3$ in an interval obtained by shifting $[3Be^v/2,3Be^v)$ by $1/2$. The endpoint error is $O((Be^v)^{-1})$. Replacing this class indicator by $1/3$ via the all-positive centered-trit estimate gives $S F_{v+P-b}/2$, proving (2).

## Stop the scale recursion in a mesoscopic range

Let $X_i=b-P B_i$ for independent fair bits $B_i\in\{0,1\}$, let $Z_n=\sum_{i=1}^n X_i$, and note $\mathbb E X_i=\mu>0$. This auxiliary walk evolves the logarithmic **source scale** in (2). Choose
\[
     R=\min(v/2,\sqrt{\log B}),\qquad H=v-R,\qquad
     Q=\min\{n:Z_n\ge H\},\qquad s=v-Z_Q.
\]
Both $R,H$ tend to infinity, $R=o(\log B)$ and $R-b<s\le R$. The strong law gives $Q<\infty$ almost surely. Iterating (2) and stopping at $Q$ yields
\[
                  \|F_v-\mathbb E S^Q F_s\|_1\ll_A R^{1-A}
                                                    \quad(A>1).        \tag{3}
\]
Indeed the expected number of visits of a positive-drift walk to any specified interval of length one is bounded by an absolute constant, uniformly in its initial state. After its first visit, the conditional probability of revisiting after $n$ more steps is at most $\Pr(|Z_n|\le1)$, summable in $n$ by a Chernoff bound on the bounded increments. Charge $(1+v-Z_i)^{-A}$ before $Q$ on successive unit intervals in $[R,\infty)$. For formal iteration stop first at $Q\wedge N$ and then send $N\to\infty$; the discarded measure on $Q>N$ tends to zero since the shapes there have uniformly bounded mass. This proves (3).

The mesoscopic theorem holds also for $F_s$ with all positive starts. Its normalized law is the sum over initial even coasts $a$, with weight $2^{-a-1}+O((Be^s)^{-1})$ for any fixed $a$, of the odd laws at separation $s-ab$ and the extra clock $a$. The phase stays exactly $(t-a)b+\log u-(s-ab)=tb+\log u-s$. For each fixed $a$ the translated Gaussian differs in sum norm from $f_s$ by $o(1)$. Truncate the geometric coast tail at a large fixed $a$ and then pass to the limit. The mesoscopic estimate is uniform for $s\in[R-b,R]$ by its sequential formulation. Substitute it into (3). The phase at total date $t$ stays the same on every auxiliary path, because
\[
    (t-Q)b+\log u-s=tb+\log u-v-P\sum_{i\le Q}B_i.
\]
In the obtained template the only remaining scalar factor is $\mathbb E[f_s(t-Q)1_{t\ge Q}]$. Replacing this by $\mathbb E f_R(t-Q)$ in sum norm costs $o(1)$: $s-R$ is bounded uniformly, the Gaussian means and standard deviations vary by bounded and $O(R^{-1/2})$ amounts respectively, and the negative-date Gaussian tails vanish. Multiplication by $W$ has bounded norm and the sampled template has bounded total mass. It suffices to prove
\[
       \sum_{t\in\mathbb Z}|\mathbb E f_R(t-Q)-f_{H+R}(t)|\to0
                     \qquad(H,R\to\infty).                            \tag{4}
\]

## Fluctuations of the auxiliary crossing and the Gaussian convolution

Write $K_q=\sum_{i\le q} B_i$. At a first crossing at date $q$, $Z_q-H=\xi$ lies in $[0,b)$; for fixed $q$ there is at most one eligible $K_q$ and $\xi=(qb-H)\bmod P$. Define the bounded periodic Riemann-integrable function
\[
 V(\xi)=\frac P\mu 1_{[0,b)}(\xi)\Pr(\inf_{i\ge1} Z_i>\xi),
                  \qquad 0\le\xi<P.
\]
The probability factor is monotone on the indicated interval. We claim
\[
        \sum_q|\Pr(Q=q)- f_H(q)V(qb-H)|\to0 .                          \tag{5}
\]
For $|q-H/\mu|\le M\sqrt H$ and eligible $k=K_q$, one has $|k-q/2|\ll_M\sqrt q$. Conditional on $K_q=k$, a first crossing at $q$ is precisely the event that all sums of the last $i$ increments in reverse order exceed $\xi$, $1\le i\le q$. For $i=q$ the condition holds automatically once $H>0$. The first $l=\lfloor q^{1/8}\rfloor$ reversed bits have law tending in total variation to iid fair bits, uniformly over these central totals. Indeed sampling them without replacement from $k$ ones and $q-k$ zeros differs from independent sampling with success probability $k/q$ by $O(l^2/q)$; changing to probability $1/2$ costs $O_M(l/\sqrt q)$. The unconditional probability of any reversed sum at $i>l$ falling to $b$ or less is $O(e^{-cl})$, and conditioning on $K_q=k$ costs at most $O_M(\sqrt q)$. The infinite iid comparison has the same exponentially small tail. Hence the conditional first-crossing probability differs from $\Pr(\inf_{i\ge1}Z_i>\xi)$ by $o_M(1)$, uniformly even at discontinuities in $\xi$.

For the eligible $k$, one has $k-q/2=(\mu q-H-\xi)/P$. The binomial local central limit estimate gives $\Pr(K_q=k)=(P/\mu) f_H(q)+o_M(q^{-1/2})$ uniformly in the same window. If the phase lies outside $[0,b)$ the true mass and $V$ both vanish. Sum the errors over that window. The probability of its complement is $O(M^{-2})+o(1)$ by the same one-sided maximal and terminal Chebyshev bounds as in the mesoscopic crossing, and the bounded $V$ has Gaussian tails there. This proves (5). Gaussian equidistribution on the circle of length $P$, for the irrational rotation by $b$, now gives $\int V\,dm_P=1$ by summing (5). The equidistribution is uniform in translations: nonconstant Fourier modes have bounded partial sums and the variation of a normalized Gaussian of growing width tends to zero. Approximation from above and below extends this result to bounded Riemann-integrable functions, including the monotone factor in $V$.

Convolve (5) with the positive Gaussian values $f_R$ on the integer lattice, whose sum tends to one uniformly for $R\to\infty$. For fixed $t$, the product $f_H(q)f_R(t-q)$ equals $f_{H+R}(t)$ times a normalized Gaussian in $q$ with variance $\sigma^2 HR/(H+R)$ and a center depending on $t$. That variance tends to infinity when both $H,R$ do. The same Gaussian equidistribution is uniform in that center and in the translate $-H$. Thus the convolution of $f_H(q)V(qb-H)$ with $f_R$ equals $f_{H+R}(t)(1+o(1))$, uniformly in $t$. Summing proves (4), regardless of the relative rates at which $H,R$ grow.

This establishes (1) for all positive starts. For the odd uniform octave, subtract its even contributions before normalizing. In raw form the odd law with weight $2/(Be^v)$ is $2F_v-SF_{v-b}$ exactly for $v$ large. The second phase agrees with the first, its translated Gaussian has vanishing sum-norm discrepancy, and the true odd normalization changes the vector by $O((Be^v)^{-1})$. This proves the assertion for odd starts too. The mesoscopic circular-translation argument then applies verbatim and gives the stated comparison for every fixed dilation. The theorem retains the clock-phase obstruction on the way *into* the floor; the subsequent last exit of an escaping orbit depends on the future of its actual integer landing label.


## Explicit octave discrepancies

For $\delta=c\bmod P\in[0,P)$ the overlap integral divides into the ordinary and wrapped intersections of the intervals $[0,b)$ and $[\delta,\delta+b)$ modulo $P$. On the first the smaller profile is $P e^{r-\delta}$, giving overlap $(2e^{-\delta}-1)_+$. On the wrapped intersection the smaller profile is $P e^r$, giving $((2/3)e^\delta-1)_+$. Hence the limiting joint variation distance on two complete source octaves is
\[
          1-(2e^{-\delta}-1)_+-((2/3)e^\delta-1)_+ .                  \tag{6}
\]
The respective distances for source dilations $2,3,4,5$ are $2/3,0,1/2,31/45$. The maximum is $3-4/\sqrt3$ at $\delta=P/2$: in the two-sided overlap region this follows by minimizing $2e^{-\delta}+(2/3)e^\delta$, and the one-sided regions are monotone. The nonzero overlap for complete octaves is compatible with the disjointness example for much narrower separated source intervals.

[Finite exact controls](check_global_landing_clock.py) test the raw native time split, chronological and reversed auxiliary crossings, the clock phase cocycle, the balanced unit-side exits and the full-octave discrepancy integral. The [receipt](../../../reports/astra-global-20261128/escape/GLOBAL_LANDING_CLOCK_CHECKS.json) uses bounded words and does not certify the analytic inputs.
