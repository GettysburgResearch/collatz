# An ordinary stopping-time criterion at the Lagarias–Weiss tilt

For $1<s<2$ take independent positive geometric gaps with $p_s(e)=(2^s-1)2^{-se}$. Let $r_j$ denote the least positive odd representative modulo $3^j$ of the associated Syracuse affine residue at depth $j$. Define
\[
 M_j(s)=3^j\mathbb E_s[r_j^{-s}],\quad
 \beta_s=\log(2^s-1)-(s-1)\log3,\quad
 C_s=\frac{1+s\log3/\beta_s}{\log2}.
\]
Strict concavity and the zero endpoint values at $s=1,2$ give $\beta_s>0$. The input from Weaver 176, Theorem 3 (23), is an exact all-$s$ comparison and original escape-mass limit. Section 5.2 of that paper already identifies the quadratic exponential rate as the maximum of cycle retention and distinct-prefix source mass. It deduces a finite-cycle logarithmic repeat bound and a verified-floor cycle-exclusion implication at $s=2$. The following conditional result uses the *exponential rate* of the raw single-period quantity $M_j$. [Original tilted moments, including the prior fixed-$s$ and microscopic-tilt laws](https://rstation.ai/problems/collatz/papers/176)

Suppose
\[
                         \limsup_{j\to\infty}\frac1j\log M_j(s)\le0.     \tag{1}
\]
Then all positive trajectories eventually enter cycles, every cycle minimum obeys
\[
                   m\le [3(e^{\beta_s/s}-1)]^{-1},                    \tag{2}
\]
and only finitely many cycles occur. Write $J(x)$ for the number of odd-map steps from an odd $x$ until first reaching the union of these cycles. For every $0<r<\beta_s$,
\[
             \sum_{x\ge1\text{ odd}} x^{-s}e^{rJ(x)}<\infty .         \tag{3}
\]
Consequently the odd population through $X$ with $J(x)\ge t\log X$ has upper counting exponent at most $s-\beta_s t$ for $t\ge0$; a strictly negative exponent means the sets are empty at every sufficiently large $X$. The limsup of the first native cycle-entry time divided by $\log n$ is at most $C_s$. These are assertions about genuine positive source trajectories under the finite-quotient premise (1).

Two choices exclude every nontrivial cycle as well.

* At $s=9/8$ the minimum cap in (2) is less than $13$ and $C_s$ is approximately $62.82651$. Its geometric parameter $1-2^{-9/8}\approx0.541498$ lies inside Leen's established absolutely continuous range. Absolute continuity by itself does not give (1). [Leen, Theorem B and cited source version](https://zenodo.org/records/23268832) · [Precise parameter coverage](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase4/EXTENDED_TILTED_INTERVAL.md)
* Let $s_*$ maximize $\beta_s/s$ on $(1,2)$. It is unique, approximately $1.355090747$, and its geometric parameter $\theta_*=1-2^{-s_*}$ is characterized by $-\log\theta_*-[(1-\theta_*)/\theta_*]\log(1-\theta_*)=\log3$. The cycle cap is less than $9$, and $C_{s_*}\approx41.677647656$ is exactly the Lagarias–Weiss stochastic extremal native constant. Here (1) at that one parameter would prove Collatz together with the corresponding upper bound on the true extremal native stopping coefficient. Lagarias and Weiss prove the value for their independent random-walk and branching models. PR215 studies this same critical entropy parameter for inverse pressure, without the present least-positive-representative stopping conclusion. [Lagarias–Weiss, Theorem 2.1, (2.4)–(2.5), and (1.7)](https://doi.org/10.1214/aoap/1177005779) · [Critical supplied-target inverse pressure](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase5/UNIFORM_INVERSE_PRESSURE.md)

For either of these two parameters, (1) is **equivalent** to universal arrival at one **together with** (3) for the first odd arrival at one and every $0<r<\beta_s$. The sufficiency direction is a population exponential-moment criterion. A pointwise bound on the largest stopping coefficient alone is weaker than that summability statement.

## From the actual product to the stopping-time series

Put $f_j(x)=\prod_{i<j}3U^ix/(3U^ix+1)$ for the true odd map. The full positive-source $s$-moment is $Z_j(s)=\sum_{x\text{ odd}}f_j(x)^s/x^s$. Weaver's exact comparison is
\[
 0\le Z_j(s)-e^{-\beta_sj}M_j(s)
              \le 2^{-s}\zeta(s)(2^s-1)^{-j}.                          \tag{4}
\]
It comes from the ordinary positive-integer lifts of each ternary inverse word, adding the other positive odd representatives in its class. In particular the error decays strictly faster than $e^{-\beta_s j}$ for $s>1$. Therefore (1) is equivalent to $\sum_j e^{rj}Z_j(s)<\infty$ for every $0<r<\beta_s$: in one direction use (4) and an exponential majorant, and in the other bound each positive term by the sum and let $r\uparrow\beta_s$.

If any $x$ escaped, its simple-path survival factor would stay bounded below by the positive simple-path packing constant. Its single summand would preclude the last convergence. For a cycle with least odd value $m$, primitive odd length $p$ and lap product $f_p(m)$, evaluate that same series at depths $kp$ starting at $m$. It requires
\[
           \beta_s/s\ \le\ -p^{-1}\log f_p(m)
                 =p^{-1}\sum_{i<p}\log(1+1/(3U^im))
                 \le\log(1+1/(3m)).
\]
This proves (2). The equality case at $r=\beta_s$ is not needed. At the first cycle arrival all departed vertices before arrival are distinct, so $f_{J(x)}(x)\ge c>0$ with one absolute constant. Keeping that single positive term of the time-summed moment for each $x$ proves (3). It bounds the stated count by $C_{r,s}X^{s-rt}$. Taking $r\uparrow\beta_s$ gives the exponent and $\limsup J(x)/\log x\le s/\beta_s$. The exact native clock $t(x)$ at the first odd cycle arrival satisfies
\[
              t(x)\log2=J(x)\log3+\log x-\log U^{J(x)}x-\log f_{J(x)}(x).
\]
The endpoints lie in finitely many fixed cycles; the correction is bounded on the simple prefix. This gives $C_s$. Even starting values add their initial halvings, which have native coefficient $1/\log2<C_s$. Native entry into the cycle can precede its first odd entry by only a bounded terminal piece.

For $s=9/8$ the inequality $\beta_s/s>\log(40/39)$, sufficient for $m<13$, can be verified by $10905^8<2\cdot10000^8$ and $39^9(2\cdot10905-10000)^8>3\cdot40^9\cdot10000^8$. For the optimizer $\beta_{s_*}/s_*\ge\beta_{4/3}/(4/3)>\log(28/27)$ implies $m<9$. The latter follows using $1259^3<2\cdot1000^3$ and $27^4(2\cdot1259-1000)^3>3\cdot28^4\cdot1000^3$. The odd possible minima through twelve are covered by the true chains $3\to5\to1$, $7\to11\to17\to13\to5$ and $9\to7$, in addition to $1$ itself. Thus both parameter choices force the only cycle to be the known one.

Conversely, suppose all inputs reach one and (3) holds there. For $j\ge J(x)$ its subsequent lap has factor $3/4$ per odd step, so
\[
 \sum_{j\ge0}e^{rj} f_j(x)^s\le C_{r,s}e^{rJ(x)}
          \quad(0<r<\beta_s).
\]
Indeed $\beta_s<s\log(4/3)$ follows from $3(2^s-1)<4^s$. Summation using (3) and the positive direction of (4) recovers (1). PR215 previously related the supercritical *power* of its $s=2$ representative observable to finite-cycle logarithmic stopping. Our $s$ changes the underlying geometric law and the reciprocal exponent together within $(1,2)$, retaining the population series and the optimized coefficient. [PR215, precise earlier $s=2$-law power result](https://github.com/GettysburgResearch/collatz/blob/5845a208956bce43b80cf6b4adbadb849d35c15d/research/astra-nine-hour-20261128/escape/phase8/TILTED_ORDINARY_REPRESENTATIVE.md)

## Identification of the extremal constant

At the unique maximizer $s\beta'_s=\beta_s$ by strict concavity. Direct substitution at $\theta=1-2^{-s}$ gives the stated geometric entropy identity and $\beta_s/s=\log2/\theta-\log3$. Uniqueness follows also since $s\beta'_s-\beta_s$ strictly decreases and changes sign between one and two. Therefore $C_{s_*}=1/(\log2-\theta_*\log3)$. For the independent native Bernoulli log-drop model, the drift $1/C_{s_*}=\log2-\theta_*\log3$ corresponds to odd-bit fraction $\theta_*$. Its binomial rate is $I=\log2+\theta_*\log\theta_*+(1-\theta_*)\log(1-\theta_*)$. The geometric entropy equation is exactly $I=\log2-\theta_*\log3=1/C_{s_*}$. This is the large root of Lagarias–Weiss $C I(1/C)=1$. No stochastic-model conclusion is transferred to a deterministic ordinary input.

The least-representative bound (1) is open. At fixed $s$ the ordinary positive-source moment (4) already detects escape by its unrescaled limit. An exponential estimate there would additionally control long terminating inputs. In particular typical ternary regularity and near-optimal entropy at the annealed critical tilt do not bound the weight on the exceptionally small positive representatives tested in (1).

## A complementary lower bound from the critical inverse endpoint

Let $a_*=1/\theta_*$. If infinitely many genuine unit inverse words at target $1$ have odd length $j\to\infty$ and total $S\le(a_*+o(1))j$, then the actual terminating sources have native stopping coefficient at least $C_{s_*}$ on a subsequence. The additional hypothesis follows, for example, from the open equality $\Theta_\infty=\theta_*$ by PR215's uniform worst-target minimum-cost theorem (2). The existence of the inverse word at this single target suffices. [PR215, critical reverse entropy and the worst supplied integer, (2)](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase4/CRITICAL_REVERSE_ENTROPY.md)

Remove the $l$ complete laps at one after the source's first arrival. Each has odd length one and native cost two. Since $a_*<2$ and every other odd gap costs at least one, $j'=j-l\ge(2-a_*-o(1))j$. The remaining word has first-hit total $S'=S-2l\le(a_*+o(1))j'$. Its positive source $x$ satisfies $x\le2^{S'}/3^{j'}$. Necessarily $x\to\infty$ along a subsequence, since the first-hit odd lengths of every bounded set of terminating sources are bounded. Thus $\log x\le(a_*\log2-\log3+o(1))j'$. The actual native stopping identity gives $S'\log2\ge j'\log3+\log x$. Its resulting lower coefficient is exactly $C_{s_*}$. Together the critical inverse-cost equality and (1) at $s_*$ would therefore prove the sharp Lagarias–Weiss value for the original map, including its upper and lower sides. Both finite-quotient hypotheses are expressly open.

[Exact power and native-chain controls](check_tilted_stopping_caps.py) verify the two small-cycle exclusions. They do not verify either open finite-quotient premise.
