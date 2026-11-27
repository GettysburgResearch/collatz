# Forward visits, ordered anchors, and a summable cost on the full synchronous classes

**PROPOSED written theorems. Collatz remains OPEN.** Work on positive ordinary integers. The shortcut map halves even inputs and sends odd inputs to $(3n+1)/2$. Write $U$ for the odd map removing the full power of two from $3n+1$. The clocks below are odd clocks. All states after the first odd step are coprime to three; $U(1)=1$.

PR197's critical marks are the odd $x$ with $d=\lfloor\log_2 x\rfloor$, $e=v_2(3x+1)$, and
$$
(d+1)(x-2^d)\le70\,2^d,\qquad d+1\le5e\le d+8.
$$
Write $B$ for this set. PR197 shows that arbitrarily high elements of $B$ reach each fixed ternary-unit target. Here we place $U(B)$ **on the forward orbit from each fixed start**, reduce its fibers, and track successive reductions on that original orbit. The amplitudes lost in the reductions have finite sum on an escaping orbit.

## 1. An explicit lift of the target seen on the forward orbit

For any odd ternary unit $y>1$ there is a unique $k\ge0$ with $3\cdot2^k<y<6\cdot2^k$. Of the two consecutive integers
$$
e\in\{\lfloor k/4\rfloor+1,\ \lfloor k/4\rfloor+2\},
$$
take the unique one with $2^e y\equiv1\pmod3$. Then $x=(2^e y-1)/3$ is positive odd, $U(x)=y$, and $d=e+k$. Indeed integrality and the strict lower bound give $x\ge2^{e+k}$, and the upper bound gives $x<2^{e+k+1}$. Now $k+1\le4e\le k+8$. Conversely, for this $y$ every odd lift has $d=e+k$, and this pair exhausts the possibilities for the critical strip. Thus membership in $U(B)$ is one integer test on $y$: check the mark on this unique lift. The point $y=1$ is handled separately.

**Forward entrance theorem.** From any positive odd ternary unit $n$, either 1 or $U(B)$ is visited in fewer than $2\sqrt n$ odd steps. For an arbitrary positive start first strip twos and take one odd step if necessary.

Use PR173's actual-trajectory theorem `steer` with its allowed real phase $\theta_0=\log_2 3$. In fewer than $\sqrt n$ odd steps it gives a $y<n/4$ or
$$
0\le \delta=\log_2 y-(\log_2 3+z),\qquad (h+1)\delta\le35,
\quad h=\lfloor\log_2 y\rfloor,\ z\in\mathbb Z .
$$
On a drop restart at the strictly smaller positive odd state. The geometric series in the square roots is less than $2\sqrt n$. Consider the second alternative. For $y>1$ the lift above has $k\le h-1$ and $d+1\le5k/4+3\le(5h+7)/4$. If $h\le54$, then $d+1\le70$ and the mark holds on the entire octave. If $h\ge55$, then $0\le\delta<1$ and $z=k$ (equality at the lower endpoint is impossible for a unit). By convexity $2^\delta-1\le\delta$ on this interval. Hence
$$
0\le (x-2^d)/2^d\le(y-3\cdot2^k)/(3\cdot2^k)
=2^\delta-1\le\delta.
$$
Since $d+1\le2(h+1)$, this proves the mark without a buffer assumption at the lower edge.

## 2. A decidable section and anchors on one original orbit

For each legal $k,e$ let $I_{k,e}$ be the finite set of direct targets $y$ whose lift above belongs to $B$ with those parameters. Use $H_d=(d+2)^3$, $d=e+k$. Partition this set by $U^{H_d}(y)$. Keep the least target $v$ in each nonempty fiber, and let $S$ be their unique critical lifts $r$. A finite octave enumeration decides membership. In the notation of a given $y\in U(B)$, write $r(y)$ for its chosen lift, $v(y)=U(r(y))$, and $A(r)=U^{H_d}(U(r))$. Thus $v(y)\le y$, $A(r(y))=U^{H_d}(y)$, and
$$
0\le y-v(y)\le 70\cdot3\cdot2^k/(d+1)+2^{-e}.
$$
This last bound follows from the upper marked endpoint in $I_{k,e}$ and its strict lower endpoint. In particular the relative gap is $O(1/\log y)$.

To enter, follow the **given** odd orbit to the first eligible $y\in U(B)\cup\{1\}$. Stop at 1; otherwise record $r(y)$ and advance on that same orbit to $A(r(y))$. To take a positive return from a recorded $r$, begin at $U(A(r))$, take the first eligible target $y'$, and either stop at 1 or record $r'=r(y')$. If this first hit took $j$ steps from $U(A(r))$, then
$$
A(r')=U^{1+j+H_{d'}}(A(r)).
$$
Every anchor is on the original forward orbit at a strictly increasing time. The amount of search between anchors, excluding the prescribed synchronization block, satisfies the forward entrance bound. The sequence of recorded marks is a deterministic map on $S\cup\{1\}$, with 1 absorbing. A start reaches 1 if and only if its recorded chain stops at 1. In particular, universal convergence is equivalent to convergence on $S$ and to termination of this deterministic return from every recorded source. If the original odd orbit is injective, its recorded minima are **all different**, because equality would repeat their anchors on that same orbit. Thus an escaping orbit forces infinitely many nonconvergent residual minima, even with the reduction always choosing the least member of the relevant fiber. A bounded nonconvergent orbit gives a recurring chain of representatives anchored on its actual cycle. This conclusion is separate from the size estimate.

The union size has the strict improvement
$$
\sum_{r\in S}r^{-4\theta/5}<\infty,\qquad
\theta=H_2(\log 2/\log 3).
$$
For each $d$ there are at most two choices of $e$ and $k=d-e=4d/5+O(1)$. Each $I_{k,e}$ lies in an integer interval of length $O(2^k/(d+1)+1)$. By PR193's uniform finite-clock packing theorem, the number of distinct terminal images after $H_d$ is at most $C2^{\theta k}/d^{\theta+1/2}$ for large $d$. One can apply the theorem to an enclosing interval of length comparable to $2^k/d$ to bound its logarithmic factor on both sides. Its required clock $O((\log L)^2)$ is below $H_d$ eventually. Summing the octave bounds after multiplication by $2^{-4\theta d/5}$ proves the claim since $\theta+1/2>1$. This counts endpoints after the physical first drop. It uses neither independence of sieves nor a growth estimate for the whole basin.

## 3. Uniform correction budget on whole synchronous classes

Fix an injective positive odd orbit $q_i=U^i(q_0)$, $i\ge0$. Let $C_i$ be all positive odd $z$ with $U^t(z)=U^t(q_i)$ for some $t\ge0$, at equal odd clocks on both arms. The map $U$ sends $C_i$ into $C_{i+1}$. A synchronous merger between members of $C_i,C_j$ implies $i=j$, by advancing past their original merger times and using injectivity of the orbit. Consequently the set of class minima $m_i=\min C_i$ is a transversal to which PR193's packing bound applies. Put
$$
c_i=\log_2(1+1/(3m_i)),\qquad D_i=\sum_{h\ge i}c_h.
$$
Then $\sum_i c_i<\infty$. Indeed the dyadic interval $[2^a,2^{a+1})$ contains at most $O(2^{\theta a}/\sqrt{a+1})$ minima. Each contributes $O(2^{-a})$. If every representative is above a fixed floor $F\ge2$, the total is $O(F^{\theta-1}/\sqrt{\log F})$. This applies in particular with the least positive nonconvergent source as a common floor (with “above” read as “at least”). Regardless of the floor, $D_i\to0$ on the fixed orbit.

Write $c(z)=\log_2(1+1/(3z))$. For every $z\in C_i$ and **all** its future times, $c(U^s z)\le c_{i+s}$. For $u,v\in C_i$ merging after $H$ odd steps let $E_u,E_v$ denote the sums of their actual valuations on these segments. Telescoping the two logarithmic recursions gives
$$
\log_2(u/v)-(E_u-E_v)
=\sum_{s<H}\big[c(U^s v)-c(U^s u)\big]. \tag{1}
$$
The right side has absolute value at most $\sum_{i\le h<i+H}c_h\le D_i$, **uniformly over the entire classes and the merger times**. The same bound holds for the distance of the logarithmic ratio of any two members of $C_i$ to the nearest integer. It shrinks to zero even for alternative ordinary sources of unbounded height.

Apply (1) to the disjoint forward segments from each selected $y=q_i$ to its anchor, paired with the alternate arm from $v(y)$. Put $b_i=\log_2(y/v(y))\ge0$. The disjoint intervals give
$$
\sum_{\text{recorded }i}\big|b_i-(E_y-E_{v(y)})\big|\le D_0<\infty. \tag{2}
$$
An injective positive integer orbit tends to infinity, so the distance estimate of Section 2 gives $b_i\to0$. Each right-hand error in (1) also tends to zero. Integrality forces $E_y=E_{v(y)}$ at every sufficiently late recorded visit. In particular
$$
\sum_{\text{recorded }i}\log_2\frac{y}{v(y)}<\infty .
$$
This controls the cumulative gain from replacing a target on one fixed escaping orbit by its least physical representative, through all repeated returns. It also works with any family of disjoint synchronized replacement segments admitting relative gaps tending to zero. No branch switches into a new uncontrolled measure.

The same mechanism gives a second exact obstruction to escape. For any disjoint stretches of a proposed injective orbit and any alternative ordinary representatives merging at their terminal odd clock, a divergent sum of distances of their log height ratios to the nearest integer is impossible. If one could force such a divergent sum on the nonconvergent orbit, its escape would be excluded. In particular it would suffice to force nonsummable positive compression on the recorded first visits. The present bounds allow infinitely many zero or summably small gains. The basin lower count does not exclude this: many backward sources may enter one synchronous class, and its smallest target can equal the actual visit. The analogous summability argument does not count repeated laps of a finite cycle. A proof that every finite cycle enters 1 or that every nonconvergent initial source yields contradictory gains remains **OPEN**.

## 4. The true least unit representatives obey an exact bounded-clock recurrence

Restart the injective orbit after one odd step, so every $q_i$ is a ternary unit. Put $n_i=\min\{z\in C_i:3\nmid z\}$, distinct from the unrestricted minima $m_i$ used for the uniform budget. Write $e_i=v_2(3n_i+1)$. For a unit $y$ let $b(y)$ be the smallest positive exponent producing a ternary-unit odd predecessor $p(y)=(2^{b(y)}y-1)/3$. Direct reduction modulo nine gives

| $y\bmod 9$ | 1 | 2 | 4 | 5 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|
| $b(y)$ | 2 | 1 | 2 | 3 | 4 | 1 |

Set $b_i=b(n_{i+1})$. Since $U(n_i)\in C_{i+1}$ is a unit, $n_{i+1}\le U(n_i)$. Also $p(n_{i+1})\in C_i$: its next step synchronizes with $q_{i+1}=U(q_i)$, so adding one initial clock gives a synchronous merger with $q_i$. As this predecessor is a unit, $n_i\le p(n_{i+1})$. Consequently
$$
2^{e_i}n_{i+1}\ \le\ 3n_i+1\ \le\ 2^{b_i}n_{i+1}. \tag{3}
$$
Thus $1\le e_i\le b_i\le4$ for every index, and $e_i=b_i$ forces $U(n_i)=n_{i+1}$. The minimum also satisfies $n_i=p(U(n_i))$, since a smaller legal unit lift of its actual successor would be in $C_i$.

Define the real height
$$
M(z)=z\,2^{L(z)},\qquad L(z)=\sum_{s\ge0} c(U^s z),\qquad z\in C_i.
$$
The sum converges uniformly on $C_i$, with $0<L(z)\le D_i$. It satisfies $M(Uz)=3M(z)/2^{v_2(3z+1)}$. If two members of $C_i$ merge, iterating this identity gives an *exact* integral power of two for their corrected-height ratio. Set $M_i=M(n_i)$. There is therefore a unique integer $a_i$ with
$$
M_{i+1}=3M_i/2^{a_i},\qquad n_i<M_i\le 2^{D_i}n_i. \tag{4}
$$
When $D_i<1$, $M_i$ is the least corrected height among the units in $C_i$: a strictly smaller corrected height must be at most $M_i/2<n_i$, whereas every unit representative $z$ has $M(z)>z\ge n_i$. The point $U(n_i)$ gives $2^{-e_i}3M_i\ge M_{i+1}$ whenever $D_{i+1}<1$. Likewise the point $p(n_{i+1})$ gives $2^{b_i}M_{i+1}/3\ge M_i$ whenever $D_i<1$. In particular, **at every sufficiently late index**
$$
1\le e_i\le a_i\le b_i\le4. \tag{5}
$$
This derivation compares the least ordinary representatives on both sides of a real orbit edge. No choice of an indefinitely changing test source is involved.

For example, from any index $J$ beyond this threshold, $\sum_{i=J}^{J+N-1}a_i\le N\log_2 3+\log_2 M_J$ by (4) and $M_{J+N}>1$. Hence at least $(2-\log_2 3)N-\log_2 M_J$ indices have $a_i=e_i=1$. At these indices $U(n_i)$ and $n_{i+1}$ occupy exactly the same corrected height. Equal corrected height does not force equality of ordinary integers. For $t\equiv4\bmod6$, the two distinct positive units $483+256t$ and $469+256t$ reach the same odd value $17+9t$ after two odd steps with the same total valuation eight. Their respective intermediate odd states are $725+384t$ and $11+6t$. For general $t\ge0$, their common endpoint is the odd part of $17+9t$ and their common total valuation is $8+v_2(17+9t)$. This verifies the ordinary multiplicity of such equal-clock fibers irrespective of their eventual fate. It establishes neither an escaping realization of infinitely many resets nor that these two sources are the minima of their classes.

The remaining question in this normal form is whether the actual unit minima and their ordinary residues can continue indefinitely with (3)–(5) and the summable class budget. The forced density of exponent one is compatible with binary-clock growth, and no argument here rules out infinitely many small strict replacements or an actual least-source tail with no replacements.

### Integer gap on the original orbit and a multi-step inverse test

Fix $J$ with $D_J<1$. On the given orbit, at every $i\ge J$ the number
$$
\ell_i=\log_2(M(q_i)/M_i)
$$
is a **nonnegative integer**. Indeed $q_i$ is a unit in the same class as $n_i$, their heights differ by an integral power of two, and $M_i$ is the minimum corrected height. The two multiplicative recurrences give the exact law
$$
\ell_{i+1}=\ell_i+a_i-v_2(3q_i+1).
$$
A valuation above four therefore requires a previously positive integer gap. The normalized gap zero asserts equality of corrected heights only. If the orbit has gap zero from $i$ onwards, then all its future valuations are exactly $a_i,a_{i+1},\ldots$ and are at most four. At most one unit in $C_i$ can stay at the minimum corrected height at every future time: two such sources share this entire valuation word, hence agree modulo $2^{1+\sum_{t=i}^{i+h-1}a_t}$ for every $h$, forcing equality as ordinary integers. This says nothing about how many sources can attain a single minimum at one time.

More generally let $A(i,h)=\sum_{t=i}^{i+h-1}a_t$ and let $E_h(z)$ be the total valuation in the next $h$ odd steps from $z$. At every $i\ge J$,
$$
E_h(n_i)\ \le\ A(i,h)\ \le\
\min_{\substack{z\ \mathrm{positive\ odd\ unit}\\U^h(z)=n_{i+h}}}E_h(z). \tag{6}
$$
The left inequality uses the corrected height of the actual endpoint $U^h(n_i)\in C_{i+h}$, which is at least $M_{i+h}$. On the right, every indicated predecessor belongs to $C_i$ by appending the finite synchronous merger of $n_{i+h}$ with $q_{i+h}$. Its corrected height is $2^{E_h(z)}M_{i+h}/3^h\ge M_i$. The minimum exists because iterating the short unit predecessor produces at least one such $z$. Both sides concern the same ordinary classes, with no replacement of a transported distribution by a fresh one. Formula (6) compares total clocks, not cardinalities of predecessor sets. Neither a bound on $\ell_i$ preventing replenishment nor a violation of (6) for some actual minimum has been established.

## Dependencies and formal scope

- PR173, `fa0c9e2a2851e6324391e39c17afcb5913185aec`, `research/lean-shell-cover/ForwardSection.lean`, theorem `steer`. The hypothesis is a positive odd start and its center is an arbitrary real. We use its actual forward visits at the center $\log_2 3$.
- PR197, `2fb1f11c959e35eba875338833d84969222dc089`, `research/ayh-resource-reset-20261124/positive-section/CRITICAL_SECTION.md`, supplies the critical-mark definition and the backward-cofinality comparison. The forward lift and entrance proof above are independent of that cofinality argument.
- PR193, `c6cb5e66516a86c33a757154983bbddc822510de`, `research/astra-universal-descent-20261124/escape.md`, §§1a–1b, supplies the written finite-clock and all-time translated packing estimates. PR182, `9b02334f27ff59694a91fe7f018e0aaabad7620b`, `research/astra-round13-20261124/LATEST_BAND.md`, previously selected minima among all marks at source scale with a finite critical-power sum at exponent $\theta$.
- [ForwardAnchors.lean](ForwardAnchors.lean) formalizes the integer critical lift with its physical equation and size, the exact integer mark implication, the moving-clock anchor identity and admissibility of arbitrary variable-delay spliced representatives. The same file proves the integral, denominator-cleared product identity for two actual merging arms behind (1), the short legal ternary-unit predecessor, and the exact two-sided inequality (3). The real steering application, section enumeration, packing and infinite sums are written proofs.
