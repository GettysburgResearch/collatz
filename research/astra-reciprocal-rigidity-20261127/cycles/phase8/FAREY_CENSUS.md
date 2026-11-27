# Counting all reduced denominators in one parity cylinder

Set $p=\log_3 2$, $h_*=H_2(p)$, $\beta=3/2-h_*$, and $L(x)=1+\log x$ for $x\ge1$. Let $d_{\min}(n)$ be the minimum full reduced denominator among nonzero signed rational shortcut cycles of least physical period $n$, with infinity allowed for an empty family. Define

$$
 \theta_F=\frac{1}{2h_*},\qquad
 \lambda_F=\frac{3/2-h_*}{2h_*}=\frac32\theta_F-\frac12.
$$

**Theorem.** For each fixed $\lambda<\lambda_F$, the set of physical periods satisfying

$$
                   d_{\min}(n)>n^{\theta_F}L(n)^\lambda               \tag{1}
$$

has natural density one. In particular $\theta_F>10/19$ and $\lambda=11/38$ is admissible. This theorem applies to every word shape, both signs and true least periods. It does not rule out one exceptional ordinary cycle.

The joint count below replaces the separate-denominator sum of [ENDPOINT_CENSUS.md](ENDPOINT_CENSUS.md). Its uniform ballot estimate, positive-prefix charge and shrinking-arc count are retained. Two elementary observations supply the larger exponent. Distinct small-denominator rationals in a bounded interval separate in the native dyadic parity code. The full above-floor excursion includes time spent coming down from the peak.

## Simultaneous parity separation

Fix a common sign, $D\ge1$, and consider reduced magnitudes $a/d,b/e$ with odd $d,e\le D$ in an interval of width $X$. If their first $t$ parity bits agree then

$$
                             2^t\mid ae-bd .
$$

Indeed the magnitude formula for that prescribed word is $2^t y_t=3^q y_0\pm C$, where the affine intercept is the same for both starts and $3^q$ is odd. Subtraction in the rationals of odd denominator gives the stated divisibility of the integer cross difference. Distinct values have $0<|ae-bd|\le deX\le D^2X$. Thus if $2^t>D^2X$, at most one such rational phase can realize a given word, **across the entire denominator range**. A shared reduced rational has the same future; as a periodic phase it belongs to only one true cycle.

For a fixed cutoff $D$ use the same $M=B=\lceil100L(D)\rceil$ on all its denominators. Let
$$
     \alpha=\frac{\log(2/(1+1/(2B)))}{\log(3+1/M)},\qquad
     \alpha_0=\frac{\log2}{\log(3+1/M)},\qquad c_M=(3+1/M)/2 .
$$
The estimates (2) and (4) in the preceding proof give the uniform $O(2^{ht}(1+t)^{-3/2})$ count of words whose every prefix has odd count at least $\alpha'j-a_0$, with $\alpha'$ either slope, $0\le a_0\le1$ and $h=H_2(\alpha')$. Here $3/5\le\alpha'\le p$, $h\le H_2(3/5)<1$ and $h-h_*=O(1/L(D))$. Consequently $(D^2)^{h-h_*}$ and $M^{h-h_*}$ are bounded by absolute constants. All following estimates are uniform for $D\ge1$.

## High minima across all denominators

On each cycle of minimum magnitude at least $M$, the nonnegative future-minimum charges have total at least its full logarithmic gap $g_C=|n_C\log2-u_C\log3|$. A positive charge at $y$ is at most $(B+1/2)/y$ and its parity prefixes all have odd count at least $\alpha j$. This holds for either sign, with the same constants, by the earlier charge calculation.

For all $y\le X$, $X\ge M$, take $t=\lfloor\log_2(D^2X)\rfloor+1$. The simultaneous separation and ballot bound give at most $O((D^2X)^h/L(D^2X)^{3/2})$ such charged phases per sign. Sum their charge bounds over shells $[2^jM,2^{j+1}M)$. Since $h=H_2(\alpha)$ stays uniformly below one, the shell sum converges and gives

$$
 \sum_{\substack{C:d_C\le D\\\min_i |x_i|\ge M}}g_C
   \ll \frac{B D^{2h}M^{h-1}}{L(D^2M)^{3/2}}
   \ll \frac{D^{2h_*}}{L(D)^\beta}.                                 \tag{2}
$$

The sum includes both signs, counts true cycles once and has no period or maximum-height cutoff. The source of the $D^{2h_*}$ factor is one joint parity count.

## The entire high excursion

Fix $N\le n_C\le2N$, $1\le d_C\le D\le N^{11/20}$ and assume the minimum is below $M$. Let $Y$ be the maximum magnitude of the cycle. It has $n_C$ distinct positive magnitude numerators at its one reduced denominator, so $Y\ge N/D$. Uniformly in the stated range this exceeds $2M$ for all sufficiently large $N$.

Within the cyclic excursion containing such a peak, choose the first state $z\ge M$ after the last crossing up from below $M$ before the peak. It satisfies $z\le(3M+1)/2\le2M$. After the peak choose the last state $z'$ before the next visit below $M$. It satisfies $z'<2M$, since on either sign every magnitude step from $y\ge M$ has next magnitude at least $y/2$. This includes the reflected negative odd step $(3y-1)/2$ since $M\ge100$. All states from $z$ through $z'$ are at least $M$. Their growth in any one step is at most the factor $c_M$.

Let $\ell$ be the number of physical steps from $z$ to $z'$ through the chosen peak. The portions up to and after the peak give separate contributions:
$$
 \ell\ \ge\ \log_{c_M}\!\frac{Y}{2M}+\log_2\!\frac{Y}{2M}
       \ \ge\ \frac83\log_2\!\frac{N}{2MD}.                          \tag{3}
$$
For the second inequality, $c_M\le301/200<2^{3/5}$, since $(301/200)^5<8$. The choice of a true excursion, including its return below the floor, is essential to the second term in (3).

Set $t=\lfloor\log_2(2MD^2)\rfloor+1$. Throughout $D\le N^{11/20}$ and $M=O(L(N))$, (3) is at least $(6/5)\log_2N-O(\log L(N))$, whereas $t\le(11/10)\log_2N+O(\log L(N))$. Thus all $t$ steps from $z$ fit above the floor, uniformly for large $N$. Starting with $z\le2M$ and ending at any of the first $t$ steps at magnitude at least $M$, the signed step-ratio upper bound gives
$$
        \frac12\le (3+1/M)^q 2^{-j},\qquad
        q\ge\alpha_0(j-1)\ge\alpha_0j-1,\qquad 1\le j\le t .
$$
Every qualifying cycle supplies a witness $z\in[M,2M]$. Assign one per cycle. Distinct cycles of one sign supply distinct rational phases even when their denominators differ. The simultaneous separation gives at most one for each permitted $t$-bit word. Applying the uniform ballot estimate to this full prefix condition yields
$$
 \#\{C:N\le n_C\le2N,\ d_C\le D,\ \min_i |x_i|<M\}
       \ll \frac{(D^2M)^{H_2(\alpha_0)}}{L(D^2M)^{3/2}}
       \ll \frac{D^{2h_*}}{L(D)^\beta}.                              \tag{4}
$$
The harmless factor of two counts both signs. This estimate imposes no lower bound on $g_C$.

## Density of the retained least periods

Adding (2) divided by $b>0$ to (4) gives the count with multiplicity
$$
 \#\{C:N\le n_C\le2N,\ d_C\le D,\ g_C\ge b\}
       \ll (1+b^{-1})\,\frac{D^{2h_*}}{L(D)^\beta},\qquad
                 1\le D\le N^{11/20}.                                 \tag{5}
$$

The desired cutoff $D=C_\lambda N^{\theta_F}L(N)^\lambda$ fits this range for large $N$, with $C_\lambda$ chosen to cover the dyadic interval in (1). Indeed $p<2/3$ and $3^{12}>2^{19}$ give $h_*>H_2(2/3)=\log_2 3-2/3>11/12$. Hence $\theta_F<6/11<11/20$. Taking $b=L(N)^{-\eta}$ with $0<\eta<\beta-2h_*\lambda$ makes (5) $o(N)$. Every smaller gap requires $\|np\|<b/\log3$. Irrational equidistribution bounds the number of such **period values** in $[N,2N]$ by $o(N)$: use any fixed arc containing the shrinking arc and then shrink the fixed arc. The dyadic conclusion gives natural density one in (1).

The exact entropy comparison $h_*<19/20$ in the initial proof gives $\theta_F>10/19$ and $\lambda_F>(3/2)(10/19)-1/2=11/38$. All conclusions are written proofs, with the earlier finite charge and Gronwall lemmas kernel-checked as described in [ASCENT_CENSUS.md](ASCENT_CENSUS.md). No logarithm-separation estimate or finite ordinary verification floor enters this argument.
