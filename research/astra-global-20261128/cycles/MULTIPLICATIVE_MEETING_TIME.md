# The critical date for meeting multiplicative dilates

Let $T(2m)=m$, $T(2m+1)=3m+2$, and fix positive integers $A,B$. For $n\ge1$ define the genuine first meeting horizon
\[
 H_{A,B}(n)=\min\{\max(s,u):s,u\ge0,\ T^s(An)=T^u(Bn)\},
\]
with $H=\infty$ if the two forward orbits are disjoint. Two *different* shortcut dates are allowed. Write $\kappa=\tfrac12\log(4/3)$ and $\mu=1/\kappa$. For an ordinary uniform $n\in I_X=(X,2X]$ the answer splits according to the rational multiplier group $\langle 2,3\rangle=\{2^a3^b:a,b\in\mathbb Z\}$.

* If $A/B\in\langle2,3\rangle$, then $H_{A,B}$ is tight. For every $h_X\to\infty$ the probability $\Pr(H_{A,B}>h_X)$ tends to zero. Quantitatively the limiting tails are $O_{A,B}(h^{-1/2})$.
* If $A/B\notin\langle2,3\rangle$, then for every $g_X/\sqrt{\log X}\to\infty$,
\[
          \Pr(H_{A,B}\le\mu\log X-g_X)\longrightarrow0.                 \tag{1}
\]
Under the separate fixed-minimum clock and minimum-tightness inputs one also has
\[
          \Pr(\mu\log X+g_X<H_{A,B}<\infty)\longrightarrow0.             \tag{2}
\]
Thus the entire mass of finite meetings is concentrated, in the tightness sense, in the critical square-root window, even when the two sources have another common component. These are absolute probability statements and require no positive lower bound on the mass of the finite meetings. The eventual co-component mass itself is unspecified.

The first assertion imports Leen's counted-pair merging theorem. The proof of (1) imports the source-qualified precritical binomial estimate for the **true** cumulative odd count and the published logarithmic linear-form bound of Matveev. An auxiliary pointwise floor consequence uses reciprocal packing on simple ordinary paths. These inputs and the additional inputs for (2) are distinguished below.

## The small multiplier group

For doubling, the orbits from $x,2x$ meet at respective dates zero and one. For tripling first take $x$ odd. The paths from $x,3x+1$ agree at the first date since both send to $(3x+1)/2$. Leen's neighbor theorem says that $3x,3x+1$ agree at date $t$ except on a set of binary cells modulo $2^t$ of relative size $O(t^{-1/2})$. The counted conclusion is stronger than needed here. Thus for almost all odd $x$ in a large octave the paths from $x,3x$ have met by $t\ge1$. This remains true with $x$ running through a fixed dilated odd progression: bounded fixed residue multiplicity and rounding cost $O_{A,B}(2^t/X)$ suffice. For even $x=2^v y$, first take $v$ common halvings at both sources. At ordinary fixed multiplier $x=Dn$, $v>h/2$ has probability $O_D(2^{-h/2}+X^{-1})$. For each fixed $h$ and each retained $v$, the odd part $y$ in the corresponding octave lies on a progression with odd step given by the odd part of $D$ times two. Its binary-cell multiplicity is at most two, independently of $v$. On sending $X\to\infty$ and using $t=\lfloor h/2\rfloor$, the limiting tail for $Dn,3Dn$ is $O_D(h^{-1/2})$. [Counted neighbor input, Paper 124/v1, equation (18) and its pair source](https://rstation.ai/problems/collatz/papers/124/v1)

For the stated ratio join $A$ and $B$ by a finite chain of positive integer multipliers in which neighbors differ by a factor of two or three. After common factors and denominators are cleared this uses only multiplication or division by the relevant primes, always at an integer; one may pass through the common prime-free part. If each neighboring pair admits a meeting with both dates at most $h$, the two ends admit one with both dates at most the number of links times $h$: at an intermediate orbit advance each partial meeting to the later of its two dates there, and append the resulting common suffix. The union bound gives the stated tight tail. A varying $h_X\to\infty$ follows by first taking any large fixed $h$.

## An arithmetic barrier valid for every individual meeting

Put $k_j(x)=\sum_{i<j}1_{T^i x\ {\rm odd}}$. The native positive offset, measured in initial-source units, is
\[
 T^s x=3^{k_s(x)}2^{-s}(x+E_s(x)),\qquad
 E_s(x)=\sum_{i<s:\,T^i x\ {\rm odd}}\frac{2^i}{3^{k_i(x)+1}}.          \tag{3}
\]
This follows by substitution at each even and odd step, including the zero offset at $s=0$. If $A/B\notin\langle2,3\rangle$, the real linear form
\[
 \Lambda=\log(A/B)+(k_s(An)-k_u(Bn))\log3-(s-u)\log2
\]
is never zero. For $s,u\le h$, the fixed positive rational bases in Matveev's theorem give
\[
                         |\Lambda|\ge c_{A,B}(2+h)^{-K_{A,B}}.           \tag{4}
\]
The constants may depend on both multipliers; the claim does not allow arbitrary growing primes. Applying the usual bound for the exponential form instead gives the same assertion by $|e^v-1|\le e|v|$ on $|v|\le1$. [Matveev, *An explicit lower bound for a homogeneous rational linear form in logarithms of algebraic numbers II*, Theorem 2.1 and the fixed-base consequence](https://doi.org/10.1070/IM2000v064n06ABEH000314)

At a meeting equation (3) bounds $|\Lambda|$ by $E_s(An)/(An)+E_u(Bn)/(Bn)$, since $\log(1+v)\le v$ for $v\ge0$. Each offset is at most $h/3$ times the largest $\exp(i\log2-k_i(x)\log3)$ through time $h$ on the relevant branch. Thus **every** meeting by $h\ge1$ forces
\[
        \max_{x\in\{An,Bn\}}\max_{0\le i\le h}
                   (i\log2-k_i(x)\log3)
                         \ge\log n-O_{A,B}(\log(2+h)).                  \tag{5}
\]
Even dropping the nonnegative grade in (5) gives $h\ge\log_2 n-O_{A,B}(\log\log n)$ for the first meeting, whenever the horizon is at most a constant times $\log n$; larger horizons already satisfy this basic bound.

An alternate pointwise consequence concerns true integer heights. Take a meeting pair minimizing $s+u$ among all pairs with both dates at most $h$. Each departed path segment has distinct states, since removing a repetition would preserve the common endpoint. If its two segments stay above $Y$, simple-path reciprocal packing gives $\sum_i 1/T^i x\ll Y^{-\sigma}$ on each for an absolute $\sigma>0$. The two physical logarithmic correction sums $\sum_{i<s,\,T^ix\text{ odd}}\log(1+1/(3T^ix))$ are therefore $O(Y^{-\sigma})$. Comparing the native multiplicative gains at the meeting bounds $|\Lambda|$ by the sum of these errors. By (4), at least one path has visited an ordinary state at most $O_{A,B}((2+h)^{K_{A,B}/\sigma})$ before or at a meeting by $h$. No averaging is used in this consequence. [Simple-path packing, Paper 28/v3, §8.1 (P3)](https://rstation.ai/problems/collatz/papers/28/v3)

An elementary uniform bound allows $A,B$ to vary. Put $e_s=3^{k_s}E_s$, the integer affine numerator offset. It satisfies $0\le e_s\le3^s-2^s$ by the recurrence $e_{i+1}=3^{1_{T^ix\text{ odd}}}e_i+1_{T^ix\text{ odd}}2^i$. At a meeting, divide the two cleared affine numerators by $2^{\min(s,u)}$. The coefficient of $n$ is a nonzero integer for every ratio outside $\langle2,3\rangle$. The absolute difference of the two nonnegative offsets is strictly below $3^{\max(s,u)}$: if $s\ge u$, each is at most $\max(3^s-2^s,2^{s-u}(3^u-2^u))<3^s$, and the other case is symmetric. Hence $n<3^{\max(s,u)}$ with no multiplier-dependent constant. In particular sources with a common factor $n\ge3^h$ and quotients in different $\langle2,3\rangle$ cosets have disjoint complete trajectories through date $h$.

## Uniformly before the critical date

The precritical count input is explicit. For a uniform genuine integer $x\le Y$, a given shortcut date $j$ and $G=\mu\log Y-j\ge1$, the total-variation distance from $k_j(x)$ to $\operatorname{Bin}(j,1/2)$ is at most
\[
           C_m(1+G)^{-m}+C\exp[-cG^2/(1+j)]                            \tag{6}
\]
for each fixed $m$. It is a one-date estimate on the true count **past the length of a complete binary source word**. Its proof uses signed native ternary transfer and a stopped fair size walk. It does not identify the whole original true parity path with iid fair bits. [PR 215, exact estimate (2), native count and true endpoint](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md)

Write $L=\log X$, $g=g_X$, $h=\lfloor\mu L-g\rfloor$. An empty or zero horizon is immediate. To prove (1) we may decrease $g$ to $\min(g,\mu L/2)$ so that the positive horizon is comparable to $L$. For each fixed $D\in\{A,B\}$, an exceptional-set probability for $Dn$, $n\in I_X$, is at most $2D+o(1)$ times the ordinary population probability for $x\le 2DX$. At this new scale $\log Y=L+O_D(1)$.

Let $b=\max(1,\lfloor\kappa g/(4\log2)\rfloor)$. Form a grid of intervals descending from $h$ in blocks of length $b$, truncating the last one at zero. If a date $i$ in a block with left edge $j$ satisfies (5), monotonicity $k_i\ge k_j$ implies
\[
             j\log2-k_j\log3\ \ge\ L-C_{A,B}\log(2+h)-b\log2.
\]
Its separation above the fair mean $\kappa j$ is at least $c_0(g+h-j)$ for large $X$, since $L-\kappa j=\kappa(g+h-j)+O(1)$ and $g\gg\sqrt L$. Under a binomial count at date $j$ Hoeffding bounds the required probability by $C\exp[-c_1(g+h-j)^2/(1+j)]$; the edge $j=0$ also satisfies this bound for its impossible event. Apply (6) at the corresponding fixed date and $Y=2DX$, whose gap $G$ differs from $g+h-j$ by $O_D(1)$. The resulting estimates sum over the grid to
\[
 C_{A,B,m}\sum_{r\ge0}\left[(g(1+r))^{-m}+
                \exp\{-c_2g^2(1+r)^2/L\}\right]=o(1)
\]
for $m>1$. The short last block adds at most a second instance at a comparable distance. The hypothesis $g/\sqrt L\to\infty$ suffices even if it tends to infinity very slowly. This proves (1) simultaneously for all candidate dates, using only the individual-date input (6). A finite family of fixed dilates in different $\langle2,3\rangle$ cosets consequently has disjoint *whole trajectory segments* up to this same precritical date, with probability tending to one. A union bound over its fixed pairs suffices.

## Upper tail for the finite meetings

For this claim take separately the natural tightness of the minimum of an ordinary orbit and the fixed-minimum-cell first-hit Gaussian in shortcut time, at mean $\mu\log X$ and scale a constant times $\sqrt{\log X}$. These are the inputs used in the linked moving-clock manuscript and its supporting critical law. In particular the time to the first minimum, restricted to any fixed minimum cell, exceeds $\mu\log X+g_X-O(1)$ with probability tending to zero when $g_X/\sqrt{\log X}\to\infty$. The conclusions hold on $n\le Y$ and thus give absolute exceptional-mass estimates on the fixed dilate samples $An,Bn$ by the same domination used for (6). [PR 215, minimum-cell and terminal-clock inputs](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/CRITICAL_CORRECTION.md) · [PR 215, fixed-root Gaussian and minimum truncation on actual components](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase2/MOVING_CLOCKS.md)

Fix $\varepsilon>0$. Minimum tightness lets us discard at most $\varepsilon+o(1)$ of the two-dilate sample so both full-orbit minima belong to a fixed finite set. For every ordered pair of minima in this set lying in the same eventual component, choose one pair of meeting dates for their genuine forward paths. Finitely many such choices give a finite common upper bound $J$. Two original sources meet eventually exactly when their minima have intersecting forward orbits. Outside the discarded set, every event with a finite meeting therefore has
\[
 H_{A,B}(n)\le J+\max(\text{first time to the minimum of }An,
                         \text{first time to the minimum of }Bn).
\]
The fixed-cell clock tail, summed over the finite set, bounds the probability of exceeding $\mu\log X+g_X$ by $\varepsilon+o(1)$. Let $\varepsilon\to0$. This proves (2), including the case of paths that eventually share an escaping ray. For any pair of multipliers the overcritical assertion still holds, but the small multiplier group already has the stronger tight first-meeting law.

For example the paths from $n,3n$ meet at a tight pair of dates, whereas for $n,5n$ an actual meeting, when it occurs, is confined in the stated absolute-mass sense to the critical window. Under universal convergence every pair from $n,5n$ ultimately meets and $H_{1,5}=\mu\log X+O_{\mathbb P}(\sqrt{\log X})$. Neither that convergence nor a limiting Gaussian law for the *pair* meeting time is an assumption of (1)–(2). The lower tail requires no minimum or ultimate-fate law.


Paper 233 studies early meetings when the starts are a semiprime product and its smaller prime, and permits the opposite arm to run without a deadline. Its leading coefficient comes from the early smaller prime on a variable-factor population. Here the ratio is fixed, the ordinary source $n$ grows on both arms, and the optimized maximum of both physical dates is the statistic. [Paper 233, §5 on early factor/product intersections](https://rstation.ai/problems/collatz/papers/233)

[Finite native affine and unequal-date checks](check_divisor_meetings.py) · [Recorded counts](../../../reports/astra-global-20261128/cycles/DIVISOR_MEETINGS.json)
