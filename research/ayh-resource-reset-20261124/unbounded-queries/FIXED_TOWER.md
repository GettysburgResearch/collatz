# What a merger can transport on a fixed tower

Write $T$ for the shortcut map, $P_i(x)$ for its number of odd inputs through $i$ steps, and $C(x)$ for reaching 1.

## A pointwise clock bound for the entire cone of smaller bases

Fix $z$ coprime to 6. For **every** $0<w<z$, arbitrary ranks $r,s$, and independent clocks $i,j\le H$, suppose $T^i(3^r z)=T^j(3^s w)$. Set $p=r+P_i(3^r z)$ and $q=s+P_j(3^s w)$. Then

$$
3^p<6^H.
$$

If $p\ge H$, then $q<H$, $j<i$, and $3^p<2^{i-j}3^q$. In this case even $3^{p+1}<6^H$. Taking $H=i=j$, an equal-clock merger requires $p<i$. Every reverse defect is 17 modulo 48, so these restrictions apply to the unchanged least defect, all positive smaller bases, and every comparison rank. The comparison starts at $3^s w$. A separately unbounded power of two multiplying the comparison start is outside this statement if it survives the comparison clock.

For the proof write $2^iT^i(x)=3^{P_i(x)}x+b_i$, where $0\le b_i\le3^i-2^i$ by induction. Align both denominators at $2^H$. Set $A=2^{H-i}3^p$ and $B=2^{H-j}3^q$. The meeting gives $Az+e=Bw+f$, where $0\le e,f<3^H$. If $p,q\ge H$, reduction modulo $3^H$ gives $e=f$. Thus $Az=Bw$ and coprimality of $z$ to $B$ forces $z\mid w$, contradicting $0<w<z$. If $p\ge H>q$, then $A\ge3^H$. The alternative $B\le A$ gives $Bw+f<Aw+A\le Az$, another contradiction. Hence $A<B$, forcing $j<i$ and the strict slope inequality. Multiplication by 3 and $q+1\le H$ give the sharpened bound. For a single positive base on both arms, if both total grades are at least $H$, the identical remainder argument gives $A=B$. Uniqueness of the powers of two and three then yields $i=j$ and $p=q$. [Lean proof](TowerLowerCone.lean)

**What this says about PR206’s actual endpoint.** The reviewed certificate gives a common endpoint at 1381 clocks for 513 consecutive vertices beginning at a selected rank $m$ on the given odd tower. In the family congruent to 1 modulo 8, $d+P_{1381}(3^{m+d}z)=660$ for $0\le d\le512$. Multiplication by 3 carries a defect $z\equiv17\pmod{48}$ through residues 1 and 3 modulo 8, so its construction uses this family. At $m\ge721$, the common endpoint cannot equal the clock-1381 iterate of **any** $3^s w$ with $0<w<z$. At $m\ge1592$, it cannot equal such an iterate at **any** clock up to 1381, since $3^{2252}<6^{1381}\le3^{2253}$. The clock exclusion from the displayed grade is kernel checked. The numerical family and its grades are sourced to the pinned upstream theorem. Thus arbitrarily late blocks provably miss this particular leastness comparison at their supplied clock. Continuing the paths longer remains possible. [PR206 merger source](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontierMergers.lean)

PR195’s Theorem 2 allows arbitrarily long repetitions from a finite bank of powered words on each arm and excludes certificates at infinitely many ranks. The result here covers every rank and every physical word, with an explicit cost in the maximum clock. PR195’s other finiteness theorem concerns equivalence classes with a common clock and equal total grade. A finite class may lie inside a much larger basin. Its full class-finiteness proof is a written upstream result. [PR195 arithmetic packet](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/arithmetic/README.md)

## Exactly what reflects back to the source

For every $z>0$, if $3^r=1+2^H k$ and $k>3\cdot2^H$, then for all $i,j\le H$,

$$
T^i(3^r z)=T^j(3^{r+1}z)
\quad\Longleftrightarrow\quad
i=j,\quad T^i(z)=T^j(3z),\quad P_i(z)=1+P_j(3z).
$$

Put $K=kz$. The shifted endpoint values are $2^{H-i}3^{P_i(z)}K+T^i(z)$ and $2^{H-j}3^{1+P_j(3z)}K+T^j(3z)$. Both remainders are below $K$ since $T^i(x)\le2^i x$. A meeting equates remainders and coefficients, which forces the displayed conditions. They conversely imply a meeting. For $H\ge3$, successive squaring gives $3^{2^{H-2}}\equiv1\pmod{2^H}$. Thus all sufficiently large multiples $r$ of $2^{H-2}$ qualify, specifically whenever $3^r>1+3\cdot4^H$. A reverse defect at $z$ gives disjoint ordinary segments through $H$ on this entire rank progression of its own tower. [Lean proof](FixedTowerReflection.lean)

## An exact delayed merger at the convergent control 17

The original values 17 and 51 reach 1 in 9 and 17 clocks, respectively. At clock 17 their endpoints and odd counts agree. A compensated common-clock merger would require one extra lower-arm odd input. Such an equality persists once obtained and is incompatible with the equal counts and common tail. Thus precisely the same disjoint-return condition holds at this known convergent original edge for every horizon.

For every odd $H=17+2n$ and every rank cutoff $L$, there is a rank $r\ge L$, a multiple of $2^{H-2}$, at which the first **asynchronous deadline** for $3^r17$ and $3^{r+1}17$ is exactly $H+5$. That is, no independently chosen clocks $i,j\le H+4$ give a meeting, and both arms meet at clock $H+5$.

At time $H$ the unshifted endpoints are 1 and the odd counts are equal to a value $p$. Write $3^r=1+2^H k$. The lifted endpoints at $H$ are $a+1,3a+1$, where $a=17\cdot3^p k$. Choose $a\equiv5\pmod{32}$. This is possible cofinally: $3^{2^{H-2}}=1+2^H c$ with $c$ odd, and raising this identity to exponent $u$ gives $k\equiv cu\pmod{32}$ since $32\mid2^H$. An odd multiplier is invertible modulo 32. The entire progression of such $u$ remains available above any cutoff.

Write $a=32v+5$. From time $H$, the pairs at the next four clocks are $(16v+3,48v+8)$, $(24v+5,24v+4)$, $(36v+8,12v+2)$ and $(18v+4,6v+1)$, with distinct entries in every pair. At the fifth clock both entries are $9v+2$. The preceding reflection result excludes all meetings through $H$. Take $r\ge H+4$. The high-rank merger result already shows that any meeting through $H+4$ must be synchronous, proving the exact deadline. Direct ordinary-integer replay finds first deadlines 22 and 24 at ranks 360448 and 3276800, respectively. These are genuine meetings. The common endpoint’s basin need not be known. [Construction](DelayedTowerMerger.lean)

## What remains unresolved

For a **hypothetical actual defect** PR146’s written constructive repair yields a further source-qualified consequence. In every binary prefix of the defect it finds a subclass on which the pair has a common-clock merger. High returning ranks on the same tower attain that subclass, since powers of 3 cover the extensions of each accessible odd residue modulo 8. If the original prefix requests enough bits to enforce the disjointness theorem above, these genuine mergers occur after the chosen horizon. Agreement at some nearby phases and arbitrarily long delays at returning phases therefore do not exclude disagreement at rank zero. [PR146 affine classification](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md) · [PR206 rotation](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontierRotation.lean)

There is also a source-qualified restriction on the possibility that all later ranks are good. For a convergent rank $r$ let $t_r$ be a hit at 1, $p_r=P_{t_r}(3^rz)$, and $S_r=2(r+p_r)-t_r$. An additional two clocks on the cycle add one odd step, so the score is independent of the chosen hit. A compensated merger preserves the score. On the other hand $2T(x)\le4^{x\bmod2}x$ gives $S_r\ge r\log_2(4/3)-\log_2 z$. If all ranks from 1 onward converge, telescoping from rank 1 to $N$ forces a positive net increase linear in $N$. The source-qualified PR146/206 finite upper estimate leaves only $O(N/\sqrt{\log N})$ possible unmerged edges at deadline $\lfloor\log_2 N\rfloor$. Discarding the first $O(\log N)$ ranks ensures that every remaining merger at that horizon is compensated. Hence among the exceptional edges (including the discarded initial ranks) the maximum upward score jump is at least a constant times $\sqrt{\log N}$ for all sufficiently large $N$ at that fixed source. A score jump can occur between two good vertices. [PR146 finite upper estimate](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md) · [PR206 fixed-tower transfer](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontier.md)

Furstenberg’s circle result concerns closed invariant sets for commuting multiplications. No circle factor preserving the two specified ordinary basin labels was constructed. Tao’s theorem quantifies over almost every starting integer in logarithmic density; one geometric tower has bounded reciprocal mass and logarithmic density zero. Neither supplies a change at a prescribed returning phase. [Furstenberg, 1967](https://math.ucsd.edu/~asalehig/F_Disjointness.pdf) · [Tao, *Almost all orbits of the Collatz map attain almost bounded values*](https://arxiv.org/abs/1909.03562)

**Open.** There is still no proof that an actual change at the least defect forces a change within every 512-edge window on that tower, or that an unrestricted ordinary comparison leads to a smaller reverse defect. The first theorem limits the clocks a smaller-base comparison can use. The second identifies exactly which bounded meetings reflect back to the original source.
