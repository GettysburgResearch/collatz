# All-prefix clock counts and visits to a fixed odd value

**Status.** The complete-row estimates below are proposed written theorems. Lean checks the fixed-gate injection. Escape remains open.

For the forward-clock test of PR 206, requiring failure at every prefix costs one extra inverse power of the depth compared to failure at the final prefix alone. This applies to a complete progression of ordinary starting values, even after fixing the exact gap history of a supplied source. In the reverse direction, a given odd value can be reached at a failing clock at only a small fraction of odd depths. This bound includes cycles and uses no renewal assumption.

## 1. How often a given gate can occur

Use the ordinary shortcut map $T$, with even step $x/2$ and odd step $(3x+1)/2$. Let $p=p_t(x)$ count odd inputs before time $t$. For a positive odd gate $g$, count positive source/clock pairs $(x,t)$ satisfying

$$
T^t x=g,\qquad (2^t)^6\le (p+1)(3^p)^6,\qquad p\le N .
$$

Every qualifying accelerated odd return is included. Initial even sources and time zero are also allowed. Put $B=\lceil(N+1)^{1/6}\rceil$. The total number of pairs, over **all** positive sources and all shortcut clocks, is at most

$$
                         6g^2 B. \tag{1}
$$

For a nonperiodic $g$ it is at most $gB$. Consequently at most $O_g(N^{1/6})$ depths up to $N$ admit any such visit. For sufficiently large $N$, partitioning $[N/2,N]$ around the occupied depths gives an interval of $\gg_g N^{5/6}$ consecutive unoccupied depths.

Let $v$ count visits to $g$ strictly before the specified clock. Each departure from $g$ contributes the exact factor $(3g+1)/(3g)$ to the ordinary product distortion, and the other factors are at least one. Hence

$$
 (3g+1)^v 3^p x\le (3g)^v 2^t g .
$$

The failing clock gives $2^t\le B3^p$. Cancelling $3^p$ yields

$$
 (3g+1)^v x\le B(3g)^v g. \tag{2}
$$

With $m=3g$, Bernoulli’s inequality gives $(1+1/m)^m\ge2$, so $2^{\lfloor v/m\rfloor}x\le Bg$. Encode a qualifying pair by

$$
       \left(v\bmod m,\ 2^{\lfloor v/m\rfloor}(2x-1)\right).
$$

The first coordinate has $3g$ choices. The second is strictly below $2Bg$. The odd part and the 2-adic valuation of the second recover $x$ and the quotient. The first recovers the remainder, hence $v$. For fixed $x$, distinct visits to $g$ have distinct $v$. The bounding rectangle proves (1). If $g$ is nonperiodic, each source visits it at most once, and (2) gives $x\le Bg$.

[GateVisits.lean](GateVisits.lean) proves the marked product, (2), the dyadic budget, the bounds on both coordinates and injectivity on actual visits. It imports the resident shortcut iteration and its count of odd inputs.

## 2. The exact forward population

Put $\mu=\log_2 3$, $c=1/(6\log 2)$, $b_j=c\log(j+1)$ and $H(j)=\lfloor\mu j+b_j\rfloor$. Unmarked logarithms are natural. For arbitrary $m\ge0$ and positive odd $d$, take the $2^{H(n)}$ ordinary starting values

$$
                       2(m+di)+1,\qquad 0\le i<2^{H(n)}.
$$

Let $S_j$ sum the first $j$ actual odd gaps, and let $P_n$ be the fraction with $S_j\le H(j)$ for **every** $1\le j\le n$. This is exactly failure of every strict test of PR 206 through $n$. Define

$$
 p=1/\mu,\quad r=1-p,\quad \lambda=\log(1/(2r)),\quad
 \rho=(r/p)e^{\lambda\mu},\quad \kappa=c\lambda.
$$

Uniformly in both the offset and the stride,

$$
 P_n\asymp \rho^n n^{-3/2+\kappa},
 \qquad \rho=0.946504577\ldots,\quad \kappa=0.073005443\ldots. \tag{3}
$$

Testing only $S_n\le H(n)$ gives a fraction $\asymp\rho^n n^{-1/2+\kappa}$. The power $\kappa$ retains the polynomial slack in the actual crossing predicate.

**Ordinary realization.** A word of positive gaps with total $s$ specifies exactly one odd residue modulo $2^{s+1}$. For a single gap, solve $3x+1=2^e y$ backwards using invertibility of $3$ modulo the new power of two and odd $y$. Applying this recursively to the odd target residue fixes the source residue and ensures that every valuation is exact. Since the stride $d$ is odd, each word with $s\le H(n)$ thus has fraction $2^{-s}$ in this row. The words are disjoint. We can calculate the finite row fraction by summing probabilities for independent geometric gaps with $\Pr(E=e)=2^{-e}$, $e\ge1$. This identification is solely a count of complete ordinary cylinders.

**Change of measure.** Under the tilted law $Q(E=e)=p r^{e-1}$, the mean is $\mu$. Put $Y_j=S_j-\mu j$. For a depth-$n$ word, the ratio of its ordinary row weight to its $Q$-probability is $\rho^n e^{\lambda Y_n}$. The centered increments have finite variance and span one on their translated lattice. One side is bounded, and the other has a geometric tail.

**Upper bound.** A centered walk with this increment law or its reflection, started at $z\ge0$, remains nonnegative for $k$ steps with probability $\le C(1+z)/\sqrt k$. For $z<L=\sqrt k$, stop at the first exit from $[0,L)$. The overshoots on either exit side have uniformly bounded conditional first and second moments, by geometric memorylessness and the bounded opposite step. A sufficiently long run of one fixed upward step forces exit, so the exit time has finite mean for fixed $L$. Stopping the position gives an upper-exit probability at most $(z+C)/L$. Stopping its square minus elapsed time times the variance gives mean exit time $O(L(z+1))$ using that upper-exit bound. Both stops follow by truncation, since pre-exit positions are bounded and exit overshoots have bounded second moments. Surviving $k$ steps requires upper exit or remaining in the strip through $k$. Markov’s inequality gives the stated bound. If $z\ge L$ the bound is immediate.

For the curved boundary set $X_j=-Y_j$, $\tau=\inf\{j:X_j+b_j<0\}$. Comparison through $j$ with constant boundary $-b_j$ first gives $Q(\tau>j)\ll(1+b_j)/\sqrt j$. Stop the centered walk at $\tau\wedge j$ and sum the deterministic increments of $b$ up to that time. Using the bounded conditional mean of the overshoot at failure gives

$$
 E_Q[(X_j+b_j)1_{\{\tau>j\}}]\le C+
       \sum_{i=1}^j (b_i-b_{i-1})Q(\tau\ge i)=O(1).
$$

The sum converges by the preliminary bound. Starting at $k=\lfloor j/2\rfloor$, compare the remaining block with boundary $-b_j$. Since $b_j-b_k=O(1)$, the flat bound and the preceding expectation give $Q(\tau>j)\ll j^{-1/2}$.

Split $n$ into three blocks of lengths differing by at most one. For a specified terminal integer $s\le H(n)$ put $z=\mu n+b_n-s$. The first block must survive the curved bound. On the reversed last block the partial sums of the centered increments must stay at least $-z$, since $Y_{n-i}\le b_{n-i}\le b_n$. Its flat constraint costs at most $C(1+z)/\sqrt n$. Conditional on both outer blocks, the middle sum must take a specified lattice value of probability at most $C/\sqrt n$, by the local CLT or Stirling’s formula at the negative binomial mode. Independence of the disjoint blocks under $Q$ gives

$$
 Q(\tau>n,S_n=s)\le C(1+z)n^{-3/2}.
$$

Multiply by $\rho^n e^{\lambda(b_n-z)}$ and sum the convergent series over the unit-spaced $z\ge0$. This proves the upper half of (3).

**Lower bound.** Choose $k=\lfloor n/2\rfloor$, $s=\lfloor\mu n+b_k\rfloor$ and $y=s-\mu n$. Require all first-half centered sums to be strictly negative, and all reversed second-half centered sums to be strictly positive. If the combined endpoint is $y$, each intermediate centered sum in the second half is at most $y\le b_k$, so both conditions suffice. Sum over attainable first-half endpoints $u\in[-2\sqrt n,-\sqrt n]$. Each such lattice point makes $y-u$ attainable for the reversed second half for all sufficiently large $n$: the required integer sums lie in their respective supports, which contain every integer above the block length. The two positive endpoints $-u$ and $y-u$ lie in compact subintervals of the positive diffusive range when divided by their respective standard deviations. Theorem 2 of Caravenna gives conditional atom probabilities $\gg1/\sqrt n$ there for the walks conditioned to have strictly positive partial sums. Both increment signs meet its span-one and finite-variance hypotheses. [Caravenna, lattice conditioned local limit theorem](https://arxiv.org/pdf/math/0406182)

For either sign, the strict-survival probability itself is $\gg1/\sqrt n$. Take one fixed positive first step and then stop on lower failure or at upper level $L=K\sqrt n$. From the resulting fixed $z_0>0$, optional stopping and the upper overshoot bound give probability at least $z_0/(L+C)$ of upper exit. If that occurs before the deadline, Kolmogorov’s maximal inequality gives probability at least $1-n\sigma^2/L^2$ to survive the remaining clocks. If it occurs later, survival through the deadline is already assured. Choose $K$ large. Nonempty centered partial sums cannot equal zero since $\mu$ is irrational. Each of the two joint constrained atom probabilities is therefore $\gg1/n$. There are $\gg\sqrt n$ matching points. Multiplying and summing gives probability $\gg n^{-3/2}$ at the chosen endpoint, where $e^{\lambda y}\asymp n^\kappa$. This proves (3). The one-cut estimate uses the unconstrained lattice local CLT with the same exponential sum, taking $s=H(n)$ for the lower bound.

**Keeping the source’s past.** Fix one positive odd source $a$ with a given admissible history of its first $j$ gaps and total $s_0=S_j(a)$. Among representatives in the complete row with that exact history, the fraction of continuations missing the next $h$ tests is

$$
                    \asymp_{a,j}\rho^h h^{-3/2+\kappa},\qquad h\to\infty. \tag{4}
$$

The conditional masses are $2^{-s}$ for the added clock $s$, since the prescribed cylinder has mass $2^{-s_0}$. The new centered boundary at continuation depth $i$ is $\mu j-s_0+b_{j+i}$. Its initial value is nonnegative. It increases logarithmically, has bounded increment over each large doubling interval and gives the same convergent stopped sum with an added fixed initial term. In the lower proof use the value of this boundary at the split. Its tilt contributes $h^\kappa$ up to constants depending on the fixed prefix.

For exact arithmetic, initialize $C_{j,s_0}=1$ and all other entries to zero. Then

$$
 C_{i,t}=1_{\{t\le H(i)\}}\sum_{v<t} C_{i-1,v}.
$$

The conditional count is $\sum_t C_{n,t}2^{H(n)-t}$ out of $2^{H(n)-s_0}$ representatives. All these representatives have the same past as the supplied $a$.

## 3. Combining the two bounds at one original gate

The all-prefix test yields a stronger estimate on the **same source/clock pairs**, if the start is odd and the counted endpoint is an actual odd return. Keep only pairs for which every odd-return test through that endpoint fails. For each fixed positive odd $g$, the number through grade $N$ is

$$
 O_g\!\left(\frac{(N+1)^{\theta/6}}{(\log(2+N))^\eta}\right),\qquad
 \theta=1+\frac{\log\rho}{\mu\log 2}=0.949955527\ldots,\quad
 \eta=\frac32-\kappa-\frac{1-\theta}{6}=1.41865\ldots . \tag{5}
$$

This counts pairs with repeated visits included. To see the ordinary short-interval consequence of (3), take $h$ maximal with $2^{H(h)}\le L$ for $L\ge2$. Since $H(h+1)-H(h)$ is bounded, an interval of $L$ consecutive odd representatives lies in a bounded number of complete rows at horizon $h$. Also $\log L=\mu h\log 2+(\log h)/6+O(1)$ for large $L$. Thus the number missing the first $h$ cuts is at most $C L^\theta(\log(2L))^{-\eta}$. Enlarging $C$ covers the finite small cases. This bound also works for odd strides in the index.

For a pair counted in (5), let $j=\lfloor v/(3g)\rfloor$. Equation (2) gives $x\le X_j=\lfloor Bg\,2^{-j}\rfloor$. At each $j$ there are at most $3g$ allowable visit ranks for a given $x$. Terms with $X_j=0$ are empty. Choose $h_*$ as above for $L=\max(2,Bg)$. The total number of pairs of grade below $h_*$ is $O_g((h_*+1)^{1/6})$ by (1) with the smaller budget. For every remaining pair the full history survives, in particular, the horizon selected for $L=\max(2,X_j)$. The odd sources up to $X_j$ lie in an interval of at most this many representatives. Summing their bound over the possible ranks costs at most

$$
 Cg\sum_{j:\,X_j\ge1} X_j^\theta(\log(2X_j))^{-\eta}
 \ \ll\ g(Bg)^\theta(\log(2Bg))^{-\eta}.
$$

For the sum with $j\le(\log_2(Bg))/2$ the logarithms are comparable and the powers form a geometric sequence. The rest is $O((Bg)^{\theta/2})$ by the same geometric sum without logarithmic saving. For fixed $g$ the early-grade cost is absorbed for large $N$. Substituting $B=\lceil(N+1)^{1/6}\rceil$ proves (5). No renewal floor or conditional distribution at the endpoint is used.

## 4. The attempted pointwise contradiction

Assume a divergent positive trajectory. Its odd values tend to infinity. Choose one actual tail minimum $a$ after its first odd return. The descent-or-cycle theorem of PR 206 implies this $a$ misses every clock test. For every $n$, it belongs to the population in (3), and for each fixed past it belongs to (4). Once $2^{S_j(a)+1}>a$, this $a$ is the least positive representative of its own gap cylinder. With increasing precision the same integer keeps choosing the lift of quotient zero. The lower and upper bounds on the complete population sample every lift; their number of failures grows exponentially. The first unsupported step is excluding that distinguished quotient-zero representative at some future depth.

Trying to force its exclusion by many predecessors at the same $a$ has a quantitative obstacle. Most inverse depths have no original satisfying even the terminal cut at $a$, by (1). The balanced sources of PR 207 have $S_b=2b$, which crosses the matched cut. Appending a suffix changes both the absolute grade and available clock budget. The escaping source gives a witness at every depth at the **moving** gate $q_n=U^n(a)$. Equation (1) concerns a fixed $g$ and its constant grows with $g$. A lower bound for unfiltered legal predecessors gives no matching count of qualifying originals at these moving gates.

**Selecting a last crossing after the balanced prefix.** There is a way to turn these predecessors into actual nevercrossers. It exhibits an exact collapse in multiplicity. Write $A_i$ for the clock from $g$ to $q_i=U^i(g)$, $R_i=2^{A_i}/3^i$ and $G_n=(4/3)^n$. For *every* original $x$ in the row of grade $n$ and clock $2n$ ending at $g$, its cut after $i$ more gaps crosses precisely when

$$
                    (G_n R_i)^6>n+i+1. \tag{6}
$$

This is an equality of events for every $i$, point by point. Every original has the same future from the supplied $g$ and has spent the same two clocks. Suppose $g$ is on the escaping ray. Its product distortion $D_i$ is bounded, so $R_i=gD_i/q_i\to0$. For $n\ge1$ the cut $i=0$ crosses. Hence (6) has a largest index $i_n$. Set $k=n+i_n$ and $y_n=q_{i_n}$. At every $j>0$, comparison of the strictly crossed cut with the subsequent failed cut gives

$$
     (k+1)\big(2^{S_j(y_n)}\big)^6
        <(k+j+1)(3^j)^6 .
$$

Since $k+j+1\le(k+1)(j+1)$, this proves that the **ordinary value $y_n$ misses all its own tests**. In particular the map taking each balanced original to its last-crossing state has image size exactly one whenever the row is nonempty, regardless of its size. The kernel statements $\,\mathtt{common\_gate\_all\_tests}$ and $\mathtt{suffix\_misses}$ in [GateVisits.lean](GateVisits.lean) check the common native-clock predicates and the actual-suffix reset. The calculation uses no comparison between different source laws.

Varying the balance depth gives distinct outputs on a known scale. As $R_{i+1}\ge(2/3)R_i$, failure of the very next cut gives
$$
    (k+1)^{1/6}<G_nR_{i_n}\le (3/2)(k+2)^{1/6}. \tag{7}
$$
The indices $i_n$ are nondecreasing, and $i_{n+2}\ge i_n+1$. Indeed a crossing at $(n,i)$ persists at $(n+1,i)$ because $(4/3)^6>2$. It persists at $(n+2,i+1)$ because $(32/27)^6>5/2\ge(n+i+4)/(n+i+1)$ for $n\ge1$. This reasoning defines the selected points from the escaping ray alone; when the inverse floor supplies balanced originals it identifies their common output. Thus the first $M$ balanced depth parameters produce at least $\lceil M/2\rceil$ genuinely distinct nevercrossing values. From (7) each is at most $g(\sup_iD_i)G_M$. This concrete logarithmic lower count in the height ceiling leaves room under the upper count in (3). The exponentially many originals at each fixed balance depth cannot be counted as additional outputs.

**Several clocks and gates on the same original.** Suppose $x$ reaches $g$ at grade $n$ and physical clock $t$, then the second gate $q_j=U^j(g)$ at $(n+j,t+A_j)$. At $q_{j+\ell}$ the second representation of the original test has ratio

$$
 \frac{2^{t+A_j}}{3^{n+j}}\,
 \frac{2^{A_{j+\ell}-A_j}}{3^\ell}
       = \frac{2^t}{3^n}R_{j+\ell},
$$

and both representations have denominator parameter $n+j+\ell+1$ in the sixth-power inequality. Thus the original tests after the second gate are literally the suffix of the same list. Every gate observed at or before the last crossing selects that same output. Every later gate has no crossing left to select. Two gates reached from a genuinely common positive source lie on a single ordered orbit. Conditioning on both gives no independent last-crossing experiment.

Alternatively one can vary $(n,t)$ at a single nonperiodic $g$. Distinct such rows have disjoint originals, since an ordinary start cannot visit $g$ twice. Each row contributes at most one selected output at or after that gate. For $1\le n\le M$ and $|t-2n|\le\sqrt n$, there are $O(M^{3/2})$ possible row labels, independently of the number of originals supplied in each row. This is an upper on the number of different selected outputs and gives no localization into a smaller translated row.

PR 197 puts several physical *query values* for a shared coarse parent on one binary grid. That construction preserves the parent distribution and the shared bits. Its different query values do not come with a proof that they are successive forward states of one ordinary starting integer. If one imposes that extra condition, the identity above applies; if one keeps the different query sites, an estimate on their joint last-crossing outputs and their source multiplicities is still required. The pinned grid upper $o(d^{-3})$ at its original selection remains open. [PR 197, joint grid and actual labels](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/source-progress/GRID_TRANSFER.md)

One can instead select the minimum of the multiplicative coefficient inside each inverse history, hoping that it occurs on a different incoming branch. Choose $g$ least among positive ordinary divergent starts; it is odd because an even start immediately halves. Every earlier state $y$ on a path reaching $g$ is divergent and satisfies $y\ge g$. On its nonempty suffix to $g$ the inverse coefficient is $2^s/3^k=D_{y\to g}\,y/g>1$. Strictness follows from $y>g$ since the divergent state $g$ cannot repeat on this path. Thus the multiplicative coefficient at $g$ is strictly below the coefficient at each earlier state of the branch. Its eventual global minimum is consequently on the common future of $g$, even when entrance clocks differ. Selecting a different minimum before branches merge at higher gates would require a lower bound on the actual pre-merge excursions of those newly selected originals. The inverse floor counts paths but contains no such event.

Weaver’s new record-increment theorem was tested on the same supplied trajectory. With $x_t=T^t x_0$, the distinct-state reciprocal estimate bounds $D_t=\prod_{i<t,\;x_i\ {\rm odd}}(1+1/(3x_i))$. Thus $3^{p_t}2^{-t}=x_t/(x_0D_t)\to\infty$. There is a last global coefficient minimum. Restarting at its actual date gives every positive-length relative coefficient strictly above one: equality would require $2^t=3^p$. This tail has no consecutive decreasing coefficient records to which Theorem 5 could apply. Sparsity of differences between records supplies no first future record here. [Weaver, paper 224 v1, Theorem 5](https://rstation.ai/problems/collatz/papers/224) · [Resident orbitwise boundaries](../../integrated/orbitwise-boundaries/README.md)

## Reproduction and source boundary

The clock and depth come from PR 206. PR 208 gives the prior terminal-cut bound and a finite all-prefix recursion. PR 207’s joint central-row lower floor is source-qualified and is not needed for (1)–(4). Equations (3) and (4) are written arguments, including the cited lattice local limit theorem. [PR 206, b2b56b9](https://github.com/GettysburgResearch/collatz/tree/b2b56b94175174a680a296478f16c619a8828972/research/clock-itineraries) · [PR 208, 72635b2](https://github.com/GettysburgResearch/collatz/tree/72635b2a3af2f5b6cbf4eeff7ce1c89b6e6a5f7f/research/openai-machinery-20261125/clock) · [PR 207, b56c4dc](https://github.com/GettysburgResearch/collatz/tree/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124)

From the repository root using Lean 4.34.1, run

```sh
obj=$(mktemp -d)
lean -o "$obj/EscapeCore.olean" research/astra-universal-descent-20261124/EscapeCore.lean
LEAN_PATH="$obj" lean -DwarningAsError=true research/astra-closure-20261125/escape/GateVisits.lean
python -B research/astra-closure-20261125/escape/check_rows.py
```

The exact Python comparison covers 63 combinations of horizon, prescribed prefix, offset and odd stride through depth eight. The additional depth-512 recurrence is illustrative. The kernel audit for the injection uses only `propext`, `Classical.choice` and `Quot.sound`.
