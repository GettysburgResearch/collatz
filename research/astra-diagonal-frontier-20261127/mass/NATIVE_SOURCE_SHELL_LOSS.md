# Seven-step loss on the original binary source shells

Let \(T(x)=x/2\) for even \(x\), \(T(x)=(3x+1)/2\) for odd \(x\). Count its odd departures by \(q_j(x)\) through the first \(j\) shortcut steps. Put \(\rho=4/7\). The native gate \(W_K\) requires \(q_j\ge\rho j\) for every \(1\le j\le K\). Let \(P_K\) be its probability under fair independent parity bits, or equivalently its fraction among the principal representatives \(1,\ldots,2^K\). Every surviving representative is odd when \(K\ge1\). For \(s\ge0\) integral let \(I_{K,s}=[2^{K-s-1},2^{K-s})\); inclusion of the right endpoint instead of the left makes no difference for the large \(K\) and ranges here, as the endpoints are even.

There are positive constants \(C_0,\ldots,C_6\), \(\gamma=2^{H_2(4/7)-1}<1\), and an absolute \(\epsilon>0\) such that uniformly for all nonnegative integers \(s,b\) with \(s+b\le\epsilon\log_2 K\),
\[
 \frac{\displaystyle\sum_{m\in I_{K,s},\ W_{K+b}(m)}1/m}
      {\displaystyle\sum_{m\in I_{K,s},\ W_K(m)}1/m}
  =(1+o(1))\,\frac{P_{K+b}}{P_K}
  =(1+o(1))\,\gamma^b
      \frac{C_{(K+b)\bmod7}}{C_{K\bmod7}}.                              \tag{1}
\]
In particular the same original atoms in **every one of these shells** lose fraction \(1-\gamma^7+o(1)\) in the next seven actual steps, taking \(s+7\le\epsilon\log_2 K\). Any nonempty union of the allowed shells obeys the same ratio, even if the union depends on \(K\). A source in \(I_{K,s}\) first became principal at native bit time \(K-s\), except for powers of two, so these include exact ages of order \(\log K\). All sums use the original reciprocal \(1/m\). The start is never replaced after survival.

The main estimate is polynomial discrepancy, independent of real-source R4 or subspace-theorem inputs. For the uniform distribution on all passing words at \(K\) let \(m(w)\) be their ordinary principal source. There is an absolute \(c>0\) such that
\[
 \sup_{I\ \mathrm{circle\ interval}}
 \left|\Pr(m(w)/2^K\in I\mid W_K)-|I|\right|\le C K^{-c}.              \tag{2}
\]
The same upper bound holds for the **expected conditional discrepancy** after recording the entire word except the orientation of designated exchanges described below. Thus any bounded test of that record transfers to a source interval of length \(z\) with additive conditional error \(O(K^{-c}/z)\). This estimate still leaves the exponentially small normalized position of a fixed ordinary start outside its scope.

## The entire accepted law and its periodic gate constants

Under fair bits put \(Q_j=\sum_{i<j}w_i\). Every length-\(K\) bit word determines one integer residue modulo \(2^K\). For the acceptance criterion \(7Q_j-4j\ge0\), [Baxter, Example 3, pp. 741–742](https://msp.org/pjm/1960/10-3/pjm-v10-n3-p01-s.pdf) gives the formal one-sided identity
\[
 \sum_{K\ge0}P_K z^K
  =\exp\!\left(\sum_{j\ge1}\frac{z^j}{j}
                    \Pr(\operatorname{Bin}(j,1/2)\ge\rho j)\right).
                                                                         \tag{3}
\]
Apply the weak-side version to the walk \(4j-7Q_j\); ties are accepted. For \(r=j\bmod7\), Stirling's formula and successive binomial ratios give
\[
 a_j:=\gamma^{-j}j^{-1}\Pr(\operatorname{Bin}(j,1/2)\ge\rho j)
       \sim c_r j^{-3/2},\qquad a_0=0,
\]
with \(c_r=[2\pi\rho(1-\rho)]^{-1/2}(3/4)^{\lceil \rho j\rceil-\rho j}/(1-3/4)>0\). Indeed the ratio of the next binomial atom to the current one is decreasing above \(\lceil\rho j\rceil\), tends to \(3/4\) there, and is uniformly bounded away from one for all large \(j\). This justifies the geometric tail factor.

For each fixed \(v\ge1\), at \(j\bmod7=r\),
\[
 \lim_{j\to\infty}j^{3/2}(a^{*v})_j
     =v\sum_{i\ge0}(a^{*(v-1)})_i c_{(r-i)\bmod7}.
\]
When one summand is at least \(j-L\), its index is unique for \(j>2L\), giving this sum truncated to \(i\le L\). In the remainder one summand is at least \(j/v\) and the others total at least \(L\). Since \(a_j\ll (1+j)^{-3/2}\) its contribution after multiplication by \(j^{3/2}\) is at most \(O_v(\sum_{i\ge L}(a^{*(v-1)})_i)\), which tends to zero with \(L\). The \(v=1\) case is immediate, with the zeroth convolution the unit atom. Splitting at \(j/2\) gives \(u*u\ll u\) for \(u_j=(1+j)^{-3/2}\). Thus all these scaled convolutions are bounded by \(C^v\), allowing termwise passage in the exponential series (3) with its \(1/v!\). Consequently
\[
 P_K\sim C_{K\bmod7}\gamma^K K^{-3/2},\quad
 C_r=\sum_{i\ge0}g_i c_{(r-i)\bmod7},\quad
 \sum g_i z^i=\exp\left(\sum a_j z^j\right).
                                                                         \tag{4}
\]
All seven constants are positive and finite. Only the lower bound \(P_K\gg\gamma^K K^{-3/2}\), also obtainable by a single cyclic rotation, is needed for (2).

## Exchanging two legal words at the same position

At aligned positions \(4t,\ldots,4t+3\), exchange \(1101\) and \(1110\). Both pass every local prefix from a nonnegative initial debt, both add \(5\) to \(7q-4j\), and both have three odd departures. Let \(\mathcal R\) record all other chunks exactly, mark either of these two words by a single symbol, and retain the final incomplete chunk exactly. Every orientation of the marks has the same fair mass, has the same complete-block counts, and passes exactly when one does. Conditional on \(\mathcal R,W_K\) the orientations are independent fair bits. The probability law before this recording is conditioned **only on \(W_K\)**, not on any exact endpoint count.

Set \(r=Q_K,\ a_t=Q_{4t}\) and \(Y=T^K(m)\). For a word on its actual principal source one has
\[
 2^K Y=3^r m+
       \sum_{\{i:w_i=1\}}2^i3^{r-Q_{i+1}},\qquad
 0\le \frac{Y}{3^r}-\frac{m}{2^K}
   =\sum_{\{i:w_i=1\}}2^{i-K}3^{-Q_{i+1}}\ll 3^{-\rho K}.              \tag{5}
\]
The inequality uses \(Q_{i+1}\ge\rho(i+1)\) and the fact \(2/3^\rho>1\). This normalization uses actual real positive heights. To compute the characteristic function of \(Y/3^r\bmod1\), reduce the integer identity modulo \(3^r\), where division by \(2^K\) denotes its ternary modular inverse. Exchanging the oriented third odd position in the chunk changes the integer numerator by \(2^{4t+2}3^{r-a_t-3}\), up to sign. For frequency \(l\ge1\) the phase increment is therefore the class
\[
 \theta_t=
 \frac{[\,l\,2^{4t+2}(2^K)^{-1}\,]_{3^{a_t+3}}}{3^{a_t+3}}
 \quad\bmod1 .                                                          \tag{6}
\]
The brackets mean an **integer residue**, not the ordinary real power \(2^{-K}\). Although \(r\) may vary between records, it cancels in (6) for each individual record. The conditional characteristic magnitude is
\(\prod_{t\ {\rm marked}}|\cos(\pi\theta_t)|\). In particular the flag defined by \(\|\theta_t\|\ge1/98\), called good here, depends only on the counts **before** the chunk and the fixed \(K,l\).

There is a fixed lower bound on the chance to mark at every full chunk given any surviving past in the \(W_K\)-conditioned sequential law. If the current debt is \(d\ge0\) and \(R\) positions remain, let \(p_R(d)\) be fair survival from there. Each of the two words has conditional probability \(p_{R-4}(d+5)/(16p_R(d))\ge1/16\) for \(R\ge4\). Monotonicity in initial debt and in permitted horizon proves the inequality. Thus at a predictable good chunk the factor \(Z_t\), equal to \(|\cos(\pi\theta_t)|\) when marked and one otherwise, has conditional expectation at most
\[
       \vartheta=1-(1-\cos(\pi/98))/8<1.
\]
At every other chunk \(Z_t\le1\). The product of the \(Z_t\)'s divided by \(\vartheta\) at each predictable good chunk is a nonnegative supermartingale of initial value one. For any integer \(g\ge0\), the expected product is at most \(\vartheta^g+\Pr(\#\mathrm{good}<g\mid W_K)\). This use of the sequential law does not condition on the future positions of the marks or on their final number.

## Many large phases from the slope gap

Use \(1\le l\le K^2\). For consecutive full chunk starts the classes satisfy
\[
              3^{a_{t+1}-a_t}\theta_{t+1}\equiv16\theta_t\pmod1.       \tag{7}
\]
If both centered representatives have absolute value below \(1/98\), the integer discrepancy in (7) has absolute value at most \((81+16)/98<1\), hence it vanishes. Along a run of small phases with \(L\) edges, their absolute values grow by the exact real factor \(2^{4L}3^{-(a_{t+L}-a_t)}\).

With \(W_K\)-conditional probability \(1-O(K^{-10})\), every underlying bit interval of length at least \(10000\log(2K)\) has an odd proportion at most \(3/5\). Indeed under independent Bernoulli\((4/7)\) bits, Hoeffding's bound for each interval is \(\exp(-2L_{\rm bit}/35^2)\), and there are at most \(K^2\) intervals. On \(W_K\) the fair-to-tilted probability ratio is at most \(\gamma^K\), since \(Q_K-\rho K\ge0\). Dividing by \(P_K\gg\gamma^K K^{-3/2}\) gives the claimed error. This device only bounds the exceptional set of complete words under the original conditional law.

For sufficiently large \(K\) set \(t_0=\lceil10000\log(2K)\rceil\). At every full chunk start \(t\ge t_0\), \(a_t\ge4\rho t\) and \(3^{a_t+3}>K^2\ge l\). Thus (6) is nonzero even if \(3\mid l\), and
\(\|\theta_t\|\ge3^{-(a_t+3)}\ge3^{-(4t+3)}\). If \(4L\ge10000\log(2K)\) and the entire run is small, the good interval-count event gives
\[
       3^{-(4t+3)}2^{4(1-(3/5)\log_2 3)L}\le1.
\]
Since \(3^5<2^8\), the coefficient \(1-(3/5)\log_2 3\) exceeds \(1/25\), and hence \(L<40t+30\). A shorter run has \(L\le t\). Starting at \(t_0\), advance over a run of small vertices and the next good vertex, or just the next good vertex when the run is empty. Each advance multiplies the index by at most \(44\), including a final truncated run, for all sufficiently large \(K\). Therefore at least \((\log K)/(2\log44)\) good chunk starts occur before \(K/4\) for every sufficiently large \(K\), on the stated event. Floors affect this bound by at most a constant before increasing the onset.

The expected absolute value of the conditional endpoint characteristic function is now \(O(K^{-c_1})\) for \(c_1=-\log\vartheta/(2\log44)>0\), uniformly for \(1\le l\le K^2\); the exceptional probability is absorbed. The bound \(1-\cos(\pi/98)\ge2/98^2\) gives \(c_1>3\cdot10^{-6}\). Equation (5) transfers the same estimate to the original source characteristic function with additional error \(O(K^2 3^{-\rho K})\). Applying the Erdős–Turán interval discrepancy inequality conditionally on the record, with cutoff \(K^2\), and then taking expectation costs only \(O(\log K)\) in the Fourier bound. This gives (2), for example with \(c=10^{-6}\). For a record event \(A\), multiply the conditional discrepancy inequality by \(1_A\) before averaging. Comparison of \(\Pr(A,\ m/2^K\in I\mid W_K)\) with \(|I|\Pr(A\mid W_K)\), then division by the interval probability, gives the asserted total variation transfer with an adjusted absolute constant when \(|I|\) exceeds twice the discrepancy.

## Bringing back the original first moment

For \(0<z_1<z_2\le1\), (2) and one partial summation give
\[
 \sum_{\substack{2^Kz_1\le m<2^Kz_2\\W_K(m)}}\frac1m
       =P_K\left(\log(z_2/z_1)+O(K^{-c}/z_1)\right).                   \tag{8}
\]
Here the factor \(P_K\) is exact because there are \(2^KP_K\) accepted representatives, while \(1/m=2^{-K}(m/2^K)^{-1}\). The half-open endpoint convention causes at most the same discrepancy error.

For an age-\(s\) shell use \(z_1=2^{-s-1},z_2=2^{-s}\). At depth \(K+b\) the **identical interval of ordinary integers** has instead \(z'_1=2^{-s-b-1},z'_2=2^{-s-b}\). These starts are also principal at \(K+b\); no new physical representatives inside the selected shell are introduced by increasing the bit clock. The logarithmic integrals are both \(\log2\). Taking any \(0<\epsilon<c\) gives relative errors \(O(K^{-(c-\epsilon)})=o(1)\) uniformly. Equation (4) then gives (1), since \(b=O(\log K)=o(K)\). At fixed or increasing \(b\) divisible by seven the periodic constants cancel. Finite residual tails through these delays are consequently bounded by a constant times \(\gamma^b\); no infinite-time expectation is inferred.

## Comparison and remaining range

[Paper 87, Theorem 1 and Corollary 2a](https://rstation.ai/problems/collatz/papers/87) previously used the same \(1101/1110\) exchange, conditional record cancellation and S-unit estimates for the coefficient-survival gate at odd frequency \(\log_32\), with a different quantitative conductor bound. [Paper 107, §§2–3](https://rstation.ai/problems/collatz/papers/107) also uses a predictable-product estimate for a run-count stop. The new feature here is the normalized **ternary** endpoint implementation of the full native \(4/7\)-gate source discrepancy. Its strictly subcritical odd frequency gives elementary positive growth across small-phase runs. At the coefficient threshold this particular growth factor vanishes. [The earlier eight-letter and switched-family result](PRINCIPAL_TERMINAL_LEAKAGE.md) used this orientation for a selected odd-gap family. Equation (2) holds on the entire native parity gate, and (1) compares the original weighted sources on the identical physical interval at both deadlines. [Paper 28, §7.11](https://rstation.ai/problems/collatz/papers/28) gives strong real-source upper concentration on linear precision bands for a differently tilted critical word law; no such theorem is used here.

For a fixed ordinary \(m\) and growing \(K\), its birth age is \(K-\lceil\log_2 m\rceil\). It eventually exceeds the shell range in (1). Extending a positive relative loss to that full old population would require information at normalized source positions of order \(2^{-K}\), as well as control that survives the \(1/m\) weight. Neither (2)'s polynomial absolute error nor its source-preserving shell comparison supplies this.

The [finite arithmetic replay](check_native_shells.py) checks every passing source at four test horizons and each available oriented exchange in those rows. It includes 10,622 complete passing rows and 5,759 exact swaps. [Retained finite counts](native_shell_checks.json)

## A stronger range from the tilted holding-walk estimate

There is a separate source-qualified strengthening. For some absolute \(c_*>0\), (2) improves to
\[
               D_K\ll\exp[-c_*(\log K)^2],                              \tag{9}
\]
and (1) holds uniformly throughout \(s+b\le c'(\log K)^2\) for some positive \(c'\). This uses the **nonnegative geometric discount** in [Paper 50, §§2 and 4, equations (5)–(9) and (22)](https://rstation.ai/problems/collatz/papers/50). The earlier, elementary estimate (2) does not require that input. The stronger expected conditional discrepancy below uses a different record based on pairs of gaps; it does not assert the stronger rate for the earlier four-bit record.

Every accepted parity word starts with a one. Writing the native word as \(10^{g_1-1}\cdots10^{g_r-1}\) gives positive gaps of exact total \(K\). This encoding includes the final trailing zeros and permits \(T^K m\) to be even. In reverse order let \(e_1,\ldots,e_r\) be the same gaps, with sums \(E_j\). The exact modular endpoint representation from (5) is
\[
      Y\equiv \sum_{i=1}^r 3^{i-1}2^{-E_i}\pmod{3^r}.                   \tag{10}
\]
For a frequency \(1\le l\le \exp((\log K)^2)\), write \(l=3^v l'\) with \(3\nmid l'\), and use conductor \(d=r-v\). For all sufficiently large \(K\), \(d\ge\rho K-O((\log K)^2)\gg K\). Only the first \(d\) reverse gaps enter this reduced character.

Pair the reverse gaps from the endpoint, up to \(\lfloor d/2\rfloor\). For the moment fix \(l\). A held pair has total three, and its orientation swaps \(1,2\) with \(2,1\). In the reverse numerator in (10) its character phase difference is exactly
\[
       l'\,3^{2j-2}2^{1-E_{2j}}/3^d\pmod1
\]
for pair \(j\), using ternary inversion. This is the white-point phase in (5) of Paper 50. Keep both orientations when the **chronological** entering native debt \(7(r-2j)-4(K-E_{2j})\) is at least one. Both orientations then pass if one does: the lower intermediate debt in these two native length-three words is the initial debt minus one, while the final debt is the initial debt plus two. If the entering debt is zero, retain the actual orientation. Other pairs and any unused letters may be completely recorded. The pair totals fix the entering debts and cumulative phase arguments even after several swaps. Thus under the original \(W_K\) law, the eligible held orientations are independent fair choices conditional on this record and \(r\).

A frequency-independent record suffices as well. Use all \(\lfloor r/2\rfloor\) pairs with the same debt rule, recording any final singleton. For a reduced conductor \(d\), the additional eligible pairs beyond the first \(\lfloor d/2\rfloor\) only multiply the conditional characteristic magnitude by factors at most one. This includes a pair straddling the last effective gap when \(d\) is odd; drop its factor. The record and its admissible choices are now common to all frequencies, as needed for conditional discrepancy.

Let \(N_{\rm w}\) count white held pairs in the first \(\lfloor d/2\rfloor\) pairs as in Paper 50, relative to its primitive frequency \(l'\). Let \(V\) be the number of native zero-debt dates in \([0,K)\) on this accepted word. Every omitted held pair accounts for a distinct such date, since its chronological entering time is \(K-E_{2j}\). For the fixed sufficiently small parameter of the primary theorem and its discount \(\beta_0>0\), the conditional Fourier product is bounded by
\[
            \exp[-\beta_0(N_{\rm w}-V)].
\]
More precisely one can use \(1\) as a second upper bound. The paper's (7) uses precisely the cosine attenuation of total-three white pairs, and not cancellation between different pair-total environments.

In native Bernoulli\((\rho)\) bits, every new excursion from debt zero can return to zero while surviving only if its first bit is a one. Consequently, by the strong Markov property at successive zero visits,
\[
       \Pr(V>L\mid W_K)\ll K^{3/2}\rho^{L-1}\quad(L\ge1)               \tag{11}
\]
under the fair conditional law, using the same \(\gamma^K/P_K\) change-of-law bound as before. Under iid positive geometric gaps of parameter \(\rho=4/7<\log_32\), Paper 50's induction for the nonnegative discount gives
\[
         \mathbb E_\rho \exp(-\beta_0 N_{\rm w})
                    \ll \exp[-c_0(\log d)^2]                            \tag{12}
\]
uniformly over primitive \(l'\). Specifically (7) defines that discount, (8) its renewal recursion, and the bound for the recursion in §4 yielding (22) is optimized immediately after (22). It is this stronger proof input that is used; a bound only on the absolute value of a complex Fourier expectation would not justify dropping the gate.

For each fixed \(r\), the iid \(r\)-gap probability of any word of total \(K\) is \(\rho^r(1-\rho)^{K-r}\). The fair weight \(2^{-K}\) divided by this probability is at most \(\gamma^K\) when \(r\ge\rho K\). Reverse order leaves the iid law unchanged. The **nonnegative** quantity in (12) can therefore be summed first over actual accepted words at that fixed \(r,K\), then upper bounded by the full iid expectation, including all totals and paths. Dividing by \(P_K\) and summing over the at most \(K\) counts \(r\), we obtain
\[
       \mathbb E[\exp(-\beta_0 N_{\rm w})\mid W_K]
               \ll K^{5/2}\exp[-c_2(\log K)^2].
\]
Here \(N_{\rm w}\) is the count for the \(r\) and reduced conductor of the actual word. Choose \(L=\lfloor \eta(\log K)^2\rfloor\) with \(0<\beta_0\eta<c_2/2\). On \(V\le L\) the discrepancy-product cost for the erased boundary exchanges is at most \(e^{\beta_0L}\). On the complement (11) is already \(\ll\exp[-c_3(\log K)^2]\). Thus the expected conditional characteristic magnitude of the endpoint has this form uniformly through the stated frequencies. Equation (5) transfers it to the source, at exponentially negligible cost. Conditional Erdős–Turán with cutoff \(\lfloor\exp((\log K)^2)\rfloor\) costs only \(O((\log K)^2)\), proving (9) and its expectation over this gap-pair record. Finally apply (8) using (9) at both actual deadlines; \(2^{s+b}\) is absorbed by the error under the stated small constant \(c'\).

This grants the seven-step law for genuine, growing native ages of order \((\log K)^2\). Even that age is \(o(K)\), so it does not evaluate the contribution of an individual source that was already principal at a fixed depth.
