# Brownian fluctuations on the true inverse tree of a fixed integer

**Proposed, source-qualified written theorem.** Use the shortcut and true natural predecessor-density law \(\mathsf Q_a\) of [the fixed-root inverse ray](NATURAL_INVERSE_RAY_EQUIDISTRIBUTION.md). The root \(a\) is any fixed positive transient integer prime to three. At depth \(k\), the law of the **entire ordered integer list** \((V_0,\ldots,V_k)\) is at total variation distance \(O_a(k^{-c})\), for some absolute \(c>0\), from the following source experiment. Put
\[
 z=e^{2k},\qquad Y=z^{1001/1000};
\]
choose an odd integer uniformly in \([Y,2Y)\), conditioned on its genuine shortcut path reaching \(a\), and read its last \(k\) native steps before first arrival in reverse. Every successful source has at least \(k\) incoming steps for large \(k\). If only arrivals by \(\lceil C k\rceil\) are counted, the resulting **finite** experiment still has total variation error \(o_a(1)\) for any \(C>2(1001/1000)\mu\), where \(\mu=2/\log(4/3)\). The stated polynomial approximation concerns uncensored successful sources.

Under \(\mathsf Q_a\), uniformly linearly interpolating on \(0\le t\le1\), one has the functional limit
\[
 \left(\frac{\log V_{\lfloor kt\rfloor}-(\lfloor kt\rfloor)/\mu}
                  {(\log3/2)\sqrt k}\right)_{0\le t\le1}
                       \Longrightarrow (B(t))_{0\le t\le1},              \tag{1}
\]
where \(B\) is a standard Brownian motion. This convergence is stable relative to the full inverse path: for every fixed bounded measurable path function \(H\), the limit of the expectation of \(H\) times a bounded continuous test of (1) is \(\mathbb E_a H\) times its Brownian expectation. In particular the same theorem holds after absolutely continuous changes of the inverse path law. Stability concerns each fixed \(H\), with no uniformity over varying path tests.

The outward odd-departure count \(N_j=\sum_{i=1}^j1_{V_i\text{ odd}}\) satisfies the same functional limit with normalization \((N_j-j/2)/(-\sqrt k/2)\), jointly with (1) with the **same** Brownian motion. At an odd root let \(D_j\) be the native depth of the \(j\)-th odd vertex after the root and \(Y_j=V_{D_j}\). The two odd-clock processes with components
\[
 \frac{D_{\lfloor kt\rfloor}-2\lfloor kt\rfloor}{\sqrt{2k}},\qquad
 \frac{\log Y_{\lfloor kt\rfloor}-\lfloor kt\rfloor\log(4/3)}
                        {\log2\,\sqrt{2k}}
\]
converge jointly to \((B,B)\). This applies to the natural and canonical genuine odd inverse laws at each nonperiodic odd unit, and to the canonical law at periodic odd units after its finite exit. Valbuena established the odd-height almost-sure speed, and Weaver identified equivalence of the two laws at transient roots. The imported functional limit is Leen's **forward** Brownian descent from varying ordinary sources jointly with the terminal fate. The use of uniform landing transport for the whole native suffix is needed to descend from that changing-source theorem to the actual fixed-root path law. [Valbuena, actual inverse clock](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/tao-basin-densities.tex) · [Weaver, Paper 12, §10.1](https://rstation.ai/problems/collatz/papers/12) · [Leen, Proposition Transport, Terminal Data, Arithmetic Progressions and Height Process](https://doi.org/10.5281/zenodo.23269488)

Weaver's Paper 175, §8, uses earlier counted passage estimates to couple successive odd source octaves at a shared landing on a geometric sequence of log scales, obtaining a natural first-hit ray on each positive-density minimum cell. Its proof establishes previous marginal gap frequencies and its §9 gives first-order odd cylinder information. That connection of actual inverse prefixes to shared landing points is prior. Here a single chosen reference octave approximates the full, prescribed native depth in total variation for an arbitrary eligible target and yields the stable Brownian process. [Weaver, Paper 175](https://rstation.ai/problems/collatz/papers/175)

## Transport of complete suffixes in total variation

For any real \(b\ge Y\), start from a uniform odd integer of \([b,2b)\). Let \(W\) be the first odd state at most \(z\), and give failed landings zero mass. Leen's Proposition *Transport* with frequency zero bounds the difference between its subprobability landing measures at \(b\) and \(Y\), on every test bounded by one, by \(O((\log z)^{-c})\). We retain this uniformity for arbitrary functions of the landing which inspect its later genuine trajectory.

At the reference source \(Y\), the probability of landing at \(W\le a2^k\) is exponentially small in \(k\). Here is a finite proof. Set \(L=\log z\) and \(m=\lfloor L/10\rfloor\). The first \(2m+1\) native bits have total variation error \(O(2^{2m+1}/Y)\) from a fixed initial one followed by independent fair bits, by the parity-class bijection. Through step \(2m\) all true states exceed \(Y2^{-2m}>a2^k\) for large \(k\). At date \(m\), relative to the initial state, the log height equals \(G_m\log3-m\log2+O(m2^{2m}/Y)\), where \(G_m\) counts odd departures. The mean expression is \(-m/\mu+O(1)\); since \(1/(10\mu)>1/1000\), a fixed binomial large-deviation bound implies the state there is at most \(z\) outside \(O(e^{-c_1k})\) of starts. The probability that all bits from \(m\) through \(2m\) are zero is also exponentially small. After date \(m\) its first odd state occurs through date \(2m\) and at most \(z\), since only halvings precede it. Thus with the same error the first odd landing by \(2m\) is above \(a2^k\). This proves the claim; also the initial values are larger than \(a2^k\), so at least \(k\) native steps are necessary to hit \(a\).

For any subset of native \(k\)-suffixes into \(a\), test \(W\) by the indicator that it reaches \(a\), that its own arrival takes at least \(k\) steps, and that its reversed suffix belongs to that subset. The observed submass is contained in the genuine successful suffix event, since \(a\) is transient. Any missed success forces an odd landing, and that landing is at most \(a2^k\): if the path from \(W\) to \(a\) takes fewer than \(k\) steps, use \(T(x)\ge x/2\); if the success predates \(W\), the target must be even, and successive halvings from \(a\le z\) give \(W\) equal to its odd part. A success at an odd target cannot occur before the first odd landing. No poor estimate of an undershoot on an arbitrary outer source is needed: apply *Transport* directly also to the indicator \(W\le a2^k\). At \(b\) the missed mass is therefore at most \(O_a(k^{-c})\) uniformly. The main suffix test has that same transport error, independently of the subset, and the reference missed mass is exponentially small.

For fixed \(k\), let \(b\to\infty\). Every possible suffix endpoint is at most \(2^k a\); its basin density is \(h(v)\) and the odd octave has the same limiting mass. Indeed the predicate of hitting a fixed vertex is a terminal label invariant above a fixed bound. Leen's terminal-data and progression results give this equality on odd starts; subtract odd initial intervals to obtain the odd-octave limit. Distinct endpoints have disjoint basins and each determines its whole word. Thus the limiting outer measure is \(h(a)\) times \(\mathsf Q_a\) at depth \(k\). The all-suffix test also shows the reference success probability equals \(h(a)+O_a(k^{-c})\). Division by this positive limiting constant proves total variation as stated. The source clock conditional on a genuine hit is \(\mu\log Y+O_{\Pr_a}(\sqrt{\log Y})\), by the original terminal-label theorem or by the bounded difference of minimum and target clocks proved below. At \(Y=e^{2(1001/1000)k}\), censoring beyond \(Ck\) discards \(o(1)\) conditional mass as claimed. For integer-only enumeration one can use precisely the odd integers between the indicated rounded endpoints.

## Reversing the true ordinary height profile

Write \(n\) for the reference sample, \(L_n=\log n\), \(\tau\) for its first minimum date, \(m(n)\) for the minimum and \(\tau_a\) for its first visit to \(a\) on success. There is a constant \(K_a\) with \(|\tau-\tau_a|\le K_a\) on every success. If the minimum occurs first, it is one of finitely many \(r\le a\) whose trajectory reaches \(a\); use the largest of their first arrival times. If the target occurs first, the minimum follows in at most the minimum time from \(a\). Thus \(\log m(n)\le\log a\) on these sources. True consecutive log heights differ by at most \(\log2\), so replacing a target endpoint by the minimum endpoint in any backwards evaluation changes the height by \(O_a(1)\), including the bounded part after the minimum.

Put \(c_*=\sigma/\mu\), \(\sigma^2=2(\log3)^2/\log^3(4/3)\), and \(\ell_n(i)=\log T^i n\). On the conditional reference sample Leen's height and terminal-label theorems give
\[
 D_n(s)=\frac{\ell_n(\lfloor s\tau\rfloor)-L_n+\lfloor s\tau\rfloor/\mu}
                         {c_*\sqrt{L_n}}
 \ \Longrightarrow B(s),\qquad
 \tau/(\mu L_n)\longrightarrow1
\]
in the uniform topology and probability, respectively. To see the source change explicitly, the height approximation by the published threshold process is in probability, hence persists on odd octaves and on successes of limiting positive mass. The threshold-process limit jointly independent of the target label holds on the odd progression by the original theorem and then on the octave by subtraction. Centering at \(\log n\) already applies there.

Let \(m_t=\lfloor kt\rfloor\). On \(\tau\ge k\), whose conditional probability tends to one, the exact endpoint difference gives
\[
 \frac{\ell_n(\tau-m_t)-m_t/\mu-\log m(n)}{c_*\sqrt{L_n}}
               =D_n(1-m_t/\tau)-D_n(1),                                 \tag{2}
\]
using the actual integer index \(\tau-m_t\) in \(D_n\). Since \(L_n/k\to\beta=2(1001/1000)\), the limit on the right is \(B(1-t/(\mu\beta))-B(1)\) uniformly in process law. This is Brownian motion in \(t\) scaled by \(1/\sqrt{\mu\beta}\). Multiplying (2) by \(c_*\sqrt{L_n/k}\) yields the coefficient \(\sigma/\mu^{3/2}=\log3/2\) in (1). Replacing \(\tau\) by \(\tau_a\) as above and using the whole-list total variation completes the deduction for the fixed-root law.

For every specified cylinder of finite inverse depth \(j\) and positive mass, the tail begins at its fixed endpoint under the very same natural inverse construction. That endpoint is transient and has positive density. The fixed initial \(j\) steps and a bounded date shift change the centered process uniformly by \(O_j(1/\sqrt k)\), since one log-height step has bounded size. Applying the proved theorem at this endpoint gives the same limit conditionally on the cylinder. Approximate any bounded measurable \(H\) in \(L^1\) by its depth-\(j\) conditional expectations to obtain stability. For arbitrary absolutely continuous probability changes first truncate their integrable Radon–Nikodym derivative.

Finally the exact native product on an outward ray is
\[
 \log V_j=\log a+j\log2-N_j\log3-
       \sum_{1\le i\le j:\,V_i\ {\rm odd}}\log(1+1/(3V_i)).
\]
The sum is bounded almost surely, since (1) in the companion [almost-sure height theorem](NATURAL_INVERSE_RAY_EQUIDISTRIBUTION.md) gives eventual exponential growth on that same ray. This proves the native count conclusion and its joint sign. At the \(j\)-th odd node \(N_{D_j}=j\) and \(D_j/j\to2\) almost surely. Uniform inversion on a bounded interval now gives \((D_{\lfloor kt\rfloor}-2\lfloor kt\rfloor)/\sqrt{2k}\Rightarrow B(t)\): for example apply the native count limit through \(3k\) steps, substitute \(D_{\lfloor kt\rfloor}/(3k)\to2t/3\) uniformly, and use Brownian time scaling. The same exact product at \(D_j\) gives the second odd component with its stated coefficient. The canonical fixed-root change of law follows from Weaver's absolute-continuity formula; a periodic canonical root leaves its cycle in a finite number of steps almost surely as in the companion proof.
