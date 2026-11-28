# Positive Hamming density for genuine parity paths of multiplicative dilates

Let $T(2m)=m$ and $T(2m+1)=3m+2$, also on $\mathbb Z_2$. For fixed positive **odd** integers $A,B$ write $H_t$ for the number of unequal departure parities among the first $t$ steps from $An$ and $Bn$. Write $D_t=k_t(An)-k_t(Bn)$ for their cumulative odd-count difference. If $A/B\notin3^{\mathbb Z}$, then under Haar $n\in\mathbb Z_2$,
\[
      \liminf_{t\to\infty} H_t/t\ge
       \begin{cases}
         2/7,& A/B\equiv5,7\pmod8,\\
         2/9,& A/B\equiv1,3\pmod8 .
       \end{cases} \qquad\text{almost surely}.                          \tag{1}
\]
Every next mixed sign is truly fair, but the two full parity words share their source and are not independent. At the intrinsic clock $H_t$, $D_t$ runs through a genuine simple symmetric walk. In particular its iterated-logarithm upper and lower limits in that clock are $1$ and $-1$. On ordinary octaves with $t=t(X)\to\infty$ and $2^t=o(X)$, the lower bound (1) minus any fixed $\varepsilon>0$ holds with probability tending to one. In the opposite odd multiplier group $A/B\in3^{\mathbb Z}$, the two paths eventually coincide at equal dates for Haar-almost every source under the counted-pair synchronization input, hence $H_t/t\to0$ there.

The outside-group assertion uses exact native branch arithmetic, an elementary periodic random-walk estimate, and the classical $2$-adic logarithm bound specified below. The latter is unnecessary for the $5,7$ residue classes, including the pair $n,5n$. Previous work already identifies the fair zero-or-signed grade increment for translated pairs and studies the long return time to grade zero, including resets at fusion. Here the unequal multiplier slopes prevent fusion almost surely and give a linear lower bound in the physical clock. [Paper 194, mixed departures and stopped cylinders](https://rstation.ai/problems/collatz/papers/194) · [PR 212, grade martingale for translated-source return pressure](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/merger/PRIMITIVE_PRESSURE.md)

## Mixed dates and the waiting time

Reveal the binary source bits in increasing order. Conditional on $n\equiv r\bmod 2^t$, write $n=r+2^t u$ with fresh Haar $u$. The two physical states at date $t$ are
\[
           c+A3^{k_t(Ar)}u,\qquad e+B3^{k_t(Br)}u
\]
with $c=T^t(Ar)$ and $e=T^t(Br)$. The two slopes are odd. Thus whether this departure has mixed parities is measurable *before* revealing the next bit; if mixed, this fresh bit selects a fair sign for $D_{t+1}-D_t$. Otherwise the increment is zero. These assertions also hold at any finite bit-prefix stopping time by partition into its disjoint cylinders.

At the time just after the $j$th mixed departure (time zero for $j=0$), let $S_j$ denote the current grade difference. The state difference is affine in the fresh tail, with nonzero slope of valuation
\[
                       v(S_j)=v_2(A3^{S_j}-B).
\]
Negative exponents are odd rational units and cause no change of valuation when cleared. Since $A/B\notin3^{\mathbb Z}$, this slope never vanishes; a zero state difference has conditional probability zero. The number of successive common departures before the next mixed one is exactly the valuation of the state difference. Indeed a common edge multiplies their difference by $1/2$ or $3/2$. If the intercept is not divisible by $2^{v(S_j)}$, that waiting time is a fixed smaller valuation. Otherwise the valuation equals $v(S_j)$ plus the valuation of a fresh Haar integer, with mean one and variance two. Hence there are infinitely many mixed departures almost surely; their fair signs make $(S_j)$ a simple symmetric walk from zero. If $W_j$ is the number of physical steps to and including the next mixed departure, then
\[
 \mathbb E(W_j\mid\mathcal F_j)\le2+v(S_j),\qquad
       \operatorname{Var}(W_j\mid\mathcal F_j)\le2,                      \tag{2}
\]
where $\mathcal F_j$ here is the history just after the $j$th mixed departure. The geometric conditional description determines the waiting length, and the new sign is fair at the subsequent mixed date. Thus $W_j-\mathbb E(W_j\mid\mathcal F_j)$ are martingale differences with uniformly bounded second moment. Their averages tend to zero almost surely by the martingale strong law (or square summability after division by $j+1$).

## A valuation sampled at the embedded walk

For odd $A/B\equiv5,7\bmod8$, $v(d)$ is either one or two and alternates between them as the integer $d$ changes parity: no power of three is $5$ or $7$ modulo eight, and one exponent parity matches the target modulo four. Since $S_j\equiv j\bmod2$, the mean along these dates tends exactly to $3/2$.

For $A/B\equiv1,3\bmod8$, the average along the embedded walk tends to $5/2$ almost surely. First, for each $k\ge3$ the solutions of $v(d)\ge k$ form one residue modulo $q_k=2^{k-2}$. The modulo-$2^k$ order of $3$ is $q_k$, as follows from $v_2(3^{2^r}-1)=r+2$ for $r\ge1$. Its powers are exactly the units congruent to one or three modulo eight, by the matching cardinalities. For $k=1$ all exponents qualify; for $k=2$ exactly one parity does. The sum of the uniform residue frequencies of these level sets is $1+1/2+\sum_{k\ge3}2^{-(k-2)}=5/2$.

A growing cutoff needs a bound on the exceptional high valuations at ordinary *integer* exponents. Bugeaud and Laurent's Theorem 3 gives
\[
                         v(d)\ll_{A,B}(\log(2+|d|))^2.                    \tag{3}
\]
For $d>0$ take the multiplicatively independent odd rational units $3,B/A$ in the theorem, exponents $d,1$, and prime two. For $d<0$ clear the odd unit $3^d$ and use $3,A/B$. Multiplicative dependence would force the positive rational $A/B$ to be an integral power of $3$, by unique prime factorization. The remaining exponent zero has fixed finite valuation. No uniformity in growing $A,B$ is claimed. [Bugeaud–Laurent, *Minoration effective de la distance p-adique entre puissances de nombres algébriques*, Theorem 3, pp. 4–5 of the authors' text](https://irma.math.unistra.fr/~bugeaud/travaux/logpadicdef.pdf)

Here are details transferring the residue averages through the unbounded function $v$. For a function $f$ on $\mathbb Z/q$ and the simple-walk transition $P$, one can solve $(I-P)h=f-\bar f$ with $\|h\|_\infty\le Cq^2\|f\|_\infty$. Indeed the equation for successive differences of $h$ has right-hand side $-2(f-\bar f)$ with period sum zero; summing once gives differences bounded by $O(q\|f\|_\infty)$, adjusted to have average zero, and summing again gives the stated bound. Telescoping along $S_j$ leaves two endpoints plus bounded martingale differences, so
\[
  \mathbb E\left|m^{-1}\sum_{j<m} f(S_j)-\bar f\right|^2
                        \ll q^4\|f\|_\infty^2/m.                        \tag{4}
\]
No aperiodicity is needed for this time-average estimate.

Let $K=\lfloor(\log_2 m)/16\rfloor$ and $q=2^{K-2}$ for large $m$. The truncated function $f=\min(v,K)$ is periodic with this period, and its uniform mean tends to $5/2$. By (4) its empirical mean differs by $o(1)$ almost surely along every fixed geometric sequence of integer sample sizes $m=\lfloor(1+\delta)^i\rfloor$ with $\delta>0$, by Chebyshev and Borel–Cantelli. The indicator of $v\ge K$ has uniform mean $1/q$. Again by (4), outside a summable exceptional sequence its empirical frequency is at most $1/q+m^{-1/16}$. Since $|S_j|\le m$, (3) bounds the empirical high-valuation excess by $O_{A,B}((\log m)^2(1/q+m^{-1/16}))=o(1)$ along that sequence. The partial sums of $v$ are nonnegative and increasing. Taking countably many $\delta\downarrow0$ and bracketing between adjacent endpoints now proves the claimed almost-sure mean for all $m$.

Writing $\tau_m=\sum_{j<m}W_j$, equation (2) gives $\limsup\tau_m/m\le2+3/2$ or $2+5/2$, respectively. Inverting this increasing clock gives (1), including intermediate physical dates just before the next mixed departure. The ordinary finite-horizon conclusions use that the full parity pair to date $t$ is a function of $n\bmod2^t$, whose octave law has TV error $O(2^t/X)$ relative to Haar.

## Exact grade covariance

Each individual grade is $\operatorname{Bin}(t,1/2)$ under Haar, by binary parity cylinders and the fact that the odd source multiplier preserves Haar. The conditional variance of the difference increment is the indicator of a mixed date, so
\[
 \mathbb E D_t^2=\mathbb E H_t,\qquad
 \operatorname{Corr}(k_t(An),k_t(Bn))=1-2\mathbb E H_t/t.                \tag{5}
\]
Fatou's lemma in (1) therefore gives limiting upper correlations $3/7$ in the first residue classes and $5/9$ in the second. Formula (5) is exact for the finite Haar cylinder model. For unnormalized moment transfer from ordinary octaves at a moving horizon, the rounding error for $D_t^2/t$ is $O(t2^t/X)$ using the trivial bound $|D_t|\le t$. Thus that moment statement, for example, follows at all $t\le(1-\varepsilon)\log_2 X$. The Hamming fraction and fixed-probability excursion tests only require $2^t=o(X)$.

For a ratio that is an integral power of three, the small-group proof in [the physical meeting dichotomy](MULTIPLICATIVE_MEETING_TIME.md) uses same-date meetings for each tripling after common initial halvings. Its fixed-date limiting Haar failure is $O_{A,B}(h^{-1/2})$. Increasing the date proves eventual same-state agreement almost surely, after which all later parities are equal. Outside this group, (1) and the classical law of the iterated logarithm for $(S_j)$ describe fluctuation at the intrinsic Hamming clock. The subsequent [dyadic line-incidence theorem](MULTIPLIER_BERNOULLI_JOINING.md) identifies the limiting mixed speed as one half and proves independent Brownian grade limits for every fixed finite family of pairwise nonsmooth multipliers.

[MixedParity.lean](MixedParity.lean) proves the exact native affine-cylinder lift, equality of the two child grades before the next bit, complementarity of the two child departure parities, and both two-child grade-sum and square-sum formulas. These finite statements even allow fixed nonnegative intercepts at both odd-multiplier sources. The source imports the actual shortcut run and odd count from the earlier finite kernel. Its five public theorem environments compile under the pinned Lean 4.34.1 strict settings and use only propositional extensionality and quotient soundness. The Haar stopping, periodic occupation estimates and logarithmic-form input above are written mathematics. [Exact finite Haar sums and residue counts](check_prime_variation.py) · [Recorded counts](../../../reports/astra-global-20261128/cycles/PRIME_VARIATION.json)
