# Uncancelled prime factors on every consecutive pair of ordinary ramps

Fix a finite set of primes $S$ containing 2 and 3. For a positive integer $m$ put $m_{S^c}=m/\prod_{p\in S}p^{v_p(m)}$. For a positive odd input $x$, factor $x+1=2^s3^h\beta$ with $(\beta,6)=1$. Write $N=3^{s+h}\beta$. The $s$ actual odd shortcuts take $x$ to $N-1$. Put $v=2^{v_2(N-1)}\ge2$. The following halvings reach the odd integer $x'=(N-1)/v$. Factor $x'+1=2^{s'}3^{h'}\beta'$ in the same way. Define the coprime positive integers $U,V$ by
$$
                \frac UV=\frac{\beta'_{S^c}}{\beta_{S^c}}.
$$

**For every $\epsilon>0$ there is a constant $c_{S,\epsilon}>0$ such that every supplied positive odd $x$ satisfies**
$$
                        UV^3\ \ge c_{S,\epsilon}N^{1-\epsilon}.       \tag{1}
$$
In particular $\max(U,V)\gg_{S,\epsilon}(x+1)^{1/4-\epsilon}$. The constants from this proof are ineffective. For any one fixed reduced outside-$S$ ratio only finitely many starting values $x$ are possible. There is no restriction on the two original cofactors or on their common part.

### Two applications of the rational subspace theorem

We use the $S$-adic subspace theorem of Schmidt and Schlickewei in dimension two. Include the real place in the set of places. At each place choose two independent rational linear forms. For each $\delta>0$ their product of absolute values at a primitive integer vector of maximum norm $D$ is at least $cD^{-\delta}$ whenever none of the evaluated forms vanishes. Indeed all exceptions to the lower bound with $c=1$ lie on finitely many proper rational lines. Each line contains at most two primitive integer vectors. Absorb their finitely many positive products by reducing $c$; this argument does not compute $c$. The forms below are fixed independently of the source. [Schlickewei, *On linear forms with algebraic coefficients and Diophantine equations*](https://doi.org/10.1016/0022-314X(77)90073-7) · [Varjú, *Times 2, 3 mod Q*, Theorem 5, precise rational formulation](https://publications.hse.ru/pubs/share/direct/809451625.pdf)

Set $W=x'+1$ and $R=vW=N+v-1$. Then $N<R<2N$ because $v\mid N-1$. Put $g=\gcd(N,R)$. The outside-$S$ parts of $R/g,N/g$ are exactly $U,V$, respectively. Apply the theorem to the primitive vector $(R/g,N/g)$ with forms $(X-Y,Y)$ at the real place and $(X,Y)$ at each prime in $S$. Every evaluated form is nonzero. Using $|p|_p=p^{-1}$, the product is
$$
  \frac{(R-N)N}{g^2}\prod_{p\in S}|(R/g)(N/g)|_p
   =\frac{v-1}{R}\,UV < \frac{UV}{W}.
$$
Since $D=R/g<2N$, this proves $W\ll_{S,\delta}N^\delta UV$, even when the primitive vector is constant on an infinite family of inputs.

For the second application the primitive vector is $(N,1)$. Use $(X-Y,Y)$ at 2 and $(X,Y)$ at infinity and all other primes in $S$. Now $N\ge3$ is odd and $v$ is the *exact* 2-part of $N-1$, so the product is precisely $N_{S^c}/v$. Thus $v\ll_{S,\delta}N^\delta N_{S^c}$. Write $N_{S^c}=GV$, $R_{S^c}=GU$; by construction $G=\gcd(N_{S^c},R_{S^c})$ and $GU\mid W$. It follows that
$$
       N_{S^c}\le WV/U\ll_{S,\delta}N^\delta V^2,
       \qquad v\ll_{S,\delta}N^{2\delta}V^2.
$$
Multiplying this bound by the one for $W$ gives $N<vW\ll_{S,\delta}N^{3\delta}UV^3$. Take $\delta=\epsilon/3$. Also $N=(3/2)^s(x+1)\ge x+1$. These calculations prove (1).

### Direction of transfer on an escaping trajectory

Run these successive complete ramps on any fixed escaping ordinary trajectory, after its initial even steps. Every finite start has a finite maximal odd run and a finite halving run, so there are infinitely many such pairs. Index quantities by $i$ starting at zero, with next cofactor $\beta_{i+1}$. Along this trajectory $x_i\to\infty$ and $N_i\to\infty$. Since $\log U_i-\log V_i=\log\beta_{i+1,S^c}-\log\beta_{i,S^c}$, summation of (1) gives
$$
  4\sum_{i<k}\log U_i\ \ge (1-\epsilon)\sum_{i<k}\log N_i
       +k\log c_{S,\epsilon}-3\log\beta_{0,S^c}.
$$
The mean of $\log N_i$ goes to infinity. First send $k\to\infty$ and then $\epsilon\downarrow0$ to obtain
$$
           \liminf_{k\to\infty}\frac{\sum_{i<k}\log U_i}
              {\sum_{i<k}\log N_i}\ \ge\ \tfrac14.                    \tag{2}
$$
For each $0<\theta<1/4$, the lower fraction of total $\log N_i$ weight on indices with $U_i\ge N_i^\theta$ is at least $(1/4-\theta)/(1-\theta)$, because $1\le U_i\le W_i\le N_i$. In particular every such ray has infinitely many transitions inserting this much prime mass outside any one prescribed finite pool. The same telescoping calculation on a full cycle lap drops the initial-cofactor term exactly. For a single transition a large $V$ can account for (1). Even a large $U$ can come from increasing a prime valuation that was already positive. The weighted fraction in (2) is over the crests of the actual supplied orbit and need not be its unweighted frequency of shortcuts.

The earlier bounded adjacent-core result used an explicit finite classification. The new bound allows arbitrary common factors, arbitrary individual core sizes, and removal of every fixed finite prime set. In a different direction Paper 138 controls long-run multiplicative rank for unshifted odd states; it does not give (1) for this pair of shifted cores. Each pair still follows one forward trajectory, so large uncancelled factors certify no visit to a smaller source by themselves. [Consecutive-core classification](ADJACENT_RAMP_CORES.md) · [Paper 138](https://rstation.ai/problems/collatz/papers/138)

The [integer checker](check_reduced_core_transport.py) verifies both exact local-product identities on 65,536 odd starts for each of three fixed prime pools, and the telescoping identity on supplied ordinary trajectories. It also checks an infinite family's formula at selected parameters: for `f=6m+2`, `N=5·2^f+1` and `x=2N/3−1`, the next odd ramp start is 5 and the inserted part `U` is one. Thus the individual lower bound cannot be restated as a numerator-only claim. [Exact controls](reduced_core_transport_controls.json)

[CoreTransport.lean](CoreTransport.lean) formalizes the algebra combining the two numerical upper bounds and the complete product telescoping identity. Its analytic upper bounds are explicit hypotheses; the Subspace Theorem and the resulting asymptotic inequalities are written inputs, not formal axioms. The companion [retention theorem](CORE_RETENTION.md) treats the common prime part and gives a separate three-variable consequence.
