# The same densely occupied interval pattern above every prescribed ratio-five pair

**PROPOSED written theorem, conditional on the stated binary renewal result.** Both ordinary targets are prescribed. For all sufficiently large integers $N$ there exists a finite pattern $P_N\subseteq\{0,\ldots,N-1\}$, independent of the target, such that

$$
                        |P_N|\ge cN/\log N .
$$

For **every** positive odd $q$ prime to three there are arbitrarily large integer translations $b$ for which every $x\in b+P_N$ is a positive odd unit and the pair $(x,5x)$ reaches the prescribed pair $(q,5q)$. All sources in one translate have the same physical clock and the same odd count on both arms. Before a common suffix they have completed at least $c'\sqrt{\log N}$ positive ratio-five marks and have one common clock $e\asymp\log N$ with grade $p=e/2+O(\sqrt e)$. The first-arm real affine offset through the full clock can be made at most $1/2$. The constants are absolute. In particular no upper bound $o(N/\log N)$ valid on **all** intervals of length $N$ can hold for the ordinary ancestors of even one such prescribed pair.

The assertion measures the length of the interval containing the sources. Its position can be much greater than that length, and the appended common suffix can be much longer than the central prefix. This leaves fixed-height central pressure and universal convergence open.

Use the shortcut $T(2n)=n,\ T(2n+1)=3n+2$. At a mark, the first state is odd, the second is exactly five times the first, and the two counts of odd inputs since the initial odd source agree. The binary source input is Haar conditioned to begin odd. Our input R is PR146's result that the consecutive physical gaps $L$ between these marks are iid, with $c(1+t)^{-1/2}\le\Pr(L>t)\le C(1+t)^{-1/2}$. This is a result about binary inputs; ordinary targets enter separately in the final lift. PR195 previously counted symbolic central rows and gave a costly full-precision correction. Its round-seven short steering changed the fine ordinary target. The argument below bounds the real offset under the actual marked law, strengthens the central grade window, and retains the entire short-interval source pattern after routing it to each supplied pair. [PR146 at f431078244e868dc699fad011044f0d5e7f76437, first-return law and delays](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md) · [PR195 at 0e8a7f9f965416189b30b57b8aa818fbcb7757c7, round-six equations (4)–(6)](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round6/renewal/README.md) · [PR195, round-seven R7-R2 and R7-R3](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/renewal/README.md)

## Tight real offsets at renewal epochs

Between successive first-arm odd inputs the durations $g_j$ are iid with $\Pr(g_j=k)=2^{-k}$, $k\ge1$. The first-arm update on a real variable is $z\mapsto A_jz+B_j$, where $A_j=3\,2^{-g_j}$ and $B_j=2^{-g_j}$. The ordinary affine carry divided by the power of two is its value started at zero. For every $0<d<1$,

$$
 E A_j=1,\qquad a_d=E A_j^d<1.
$$

Strict concavity gives the inequality since $A_j$ is nonconstant. With $V_0=0,V_j=A_jV_{j-1}+B_j$, subadditivity and independence give $\sup_j E V_j^d\le E B_1^d/(1-a_d)$.

Let $M$ be the number of odd inputs in a complete marked gap. It is a stopping time in the geometric-letter filtration: those letters fix every first-arm bit up to the next odd sentinel and thereby determine every companion bit already consumed. A completed mark is exactly a return to the ratio and equal-count state at an odd sentinel. In particular $1\le M\le L$. For $0<\theta<d/3$, the product $S_j=(A_1\cdots A_j)^\theta$ is a nonnegative supermartingale. Stopping at $M\wedge n$, with $n\ge1$, gives $E S_{M\wedge n}\le E S_1=a_\theta<1$. Fatou gives $E S_M\le a_\theta$.

The terminal affine offset $V_M$ also satisfies $E V_M^\theta<\infty$, despite the infinite mean of $L$. On $2^k\le M<2^{k+1}$ use Hölder on the maximum of $V_j^\theta$ up to $2^{k+1}$. The $d$-moment of that maximum is at most the sum of the individual $d$-moments, $O(2^k)$. The event has probability $O(2^{-k/2})$ by R. Its contribution to $E V_M^\theta$ is therefore

$$
              O\big(2^{k\theta/d}2^{-k(1-\theta/d)/2}\big).
$$

This is summable. Finally the affine maps of different complete marked gaps are iid, since the unused geometric letters are fresh. If $Z_j$ is the real offset at the end of the $j$-th gap, subadditivity now yields

$$
       E Z_j^\theta\le a_\theta E Z_{j-1}^\theta+E V_M^\theta,
                 \qquad \sup_j E Z_j^\theta<\infty.                 \tag{1}
$$

This controls the offset at the actual renewal epoch, which has a different distribution from the offset at a deterministic clock.

## Counting a central marked row with bounded offset

Write $D_j=L_1+\cdots+L_j$. Choose a sufficiently small fixed $d_0>0$ and consider every integer $j\in[d_0\sqrt H,2d_0\sqrt H]$. R and a union bound on gaps exceeding $H$, followed by Markov on their truncated sum, give $\Pr(D_j>H)\le Cj/\sqrt H<1/8$. For fixed sufficiently small $\delta>0$, the probability $D_j<\delta H$ is at most $\Pr(L_i\le\delta H\text{ for all }i\le j)\le\exp(-c j/\sqrt{\delta H})<1/8$ for large $H$.

Let $p_t$ count first-arm odd inputs before physical clock $t$. After the fixed first odd bit, the parity bits are independent fair bits. The maximal second-moment inequality for centered partial sums gives $\Pr(\max_{t\le H}|p_t-t/2|>C_0\sqrt H)<1/8$ with an absolute $C_0$. By equation (1), choose an absolute $B\ge1$ with $\Pr(Z_j>B)<1/8$ uniformly in $j$. No independence between these four restrictions is used. For every indicated $j$, all four hold with probability at least $1/2$. Summing over $j$ counts at least $c\sqrt H$ good epochs in expectation.

The epochs on a single input have distinct clocks. There are $O(H^{3/2})$ possible clock/grade pairs in this window. Hence some row $(e,p)$, with $\delta H\le e\le H$ and $|p-e/2|\le C_0\sqrt H$, has word mass at least $c/H$. A chronological word of length $e$ beginning odd together with its terminal odd sentinel has mass exactly $2^{-e}$ under the odd-start law. Its carry, grade, earlier marks and mark number are determined by these bits. Thus there is a set of at least $c2^e/H$ distinct words with the asserted marks and real offset $0\le\beta_w\le B$.

## One pattern in the literal ordinary fibers of all prescribed pairs

Put $G=2^e/3^p$. The central window gives $c_1H\le\log G\le C_1H$ for all large $H$. Write $C_w=2^e\beta_w$. At a unit target $y$, a marked word gives exactly the inverse

$$
                        x_w=(2^e y-C_w)/3^p.
$$

Its legality at $y>B$ with unit source amounts to a congruence condition on $y\bmod 3^{p+1}$, with the odd sentinel supplied by odd $y$. Indeed the ordinary parity cylinder has step $2^e$ at its source and $3^p$ at its endpoint. The allowed endpoint class modulo $3^p$ is a unit since the last odd carry term is a power of two modulo three. Among its three lifts modulo $3^{p+1}$ exactly two give unit source. These two therefore have normalized unit-class mass $3^{-p}$. The companion follows the same binary cylinder and has endpoint $5y$ with grade $p$ by the marked relative state. Positivity follows from $y>B$. Averaging over the $2\cdot3^p$ unit residues gives a single class with at least $cG/H$ legal distinct words.

Choose any odd $y_0>B$ in that class. Distinct words give distinct positive sources; each source determines its own first-arm parity sequence. They all lie in $[G(y_0-B),Gy_0]$. Every larger odd target in this same fine class translates **all** these sources by the same integer $2^e(y-y_0)/3^p$, preserving all grades, both endpoints and source units. Given a large integer $N$, choose $H=\lceil C_2\log N\rceil$ with $C_2$ sufficiently large that $G\ge N$. Split the integer interval enclosing the sources into at most $1+\lceil (BG+1)/N\rceil$ intervals of $N$ consecutive integers, extending the last interval as necessary. One interval contains $\gg N/H\gg N/\log N$ sources. Subtract its left endpoint to obtain $P_N$.

For arbitrary $q$, choose $u\ge6$ such that

$$
        2^u q\equiv7+9y_0\pmod{3^{p+3}},\qquad y=(2^u q-7)/9>y_0 .
$$

Two generates the units modulo every power of three. This follows from its order two modulo three and $v_3(4^{3^j}-1)=j+1$ by successive cubing. There are arbitrarily large admissible $u$; $y$ is odd and in the required fine class. The elementary A branch sends $(y,5y)$ to $(q,5q)$ in $u$ steps with two odd inputs on each arm. Explicitly $y=64s+49$ for $s\ge0$ at all sufficiently large $u$, and the first six steps send the pair to $(9s+7,5(9s+7))=(2^{u-6}q,5\cdot2^{u-6}q)$. The remaining steps are common halvings. Thus the whole translated pattern has clock $e+u$, grades $p+2$, and total first-arm offset $(9\beta_w+7)/2^u\le1/2$ for sufficiently large $u$. The translations tend to infinity. [PR195 ordinary A branch, six-step physical verification](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round6/renewal/README.md) · [Std Lean proof of the physical simultaneous translation and suffix composition](PatternTransfer.lean)

A small exact example has $(e,p,y_0)=(18,7,1489)$. The three ordinary starts $178433,178469,178475$ and their fivefold companions have the prescribed equal-grade endpoints. Thus the pattern $\{0,36,42\}$ can be translated into every supplied pair's inverse tree by the same argument. For $q=1,5,7,11$ one may respectively take $u=6448,3995,30840,29007$ in the displayed congruence. The Lean theorem `examplePattern` checks the literal sources and the two-arm lift through any admissible router using ordinary natural-number trajectories.

### Many simultaneous arithmetic progressions

Fix $0<\epsilon<1$. For any large $N$ and any integer $1\le m\le N^{1-\epsilon}$, the common pattern contains $\gg N/\log N$ pairwise disjoint nontrivial three-term arithmetic progressions whose differences are multiples of $m$. These same progressions therefore occur above every supplied pair with the same count and clock in each translate. To prove it, take any subset of the pattern still having half its original size. Some residue class modulo $m$ has relative density $\gg1/\log N$. After rescaling, that class has length $L\asymp N/m\ge cN^\epsilon$. The Kelley–Meka progression-free density bound $\exp(-c'(\log L)^\eta)$ for an absolute $\eta>0$ is smaller than this density for all sufficiently large $N$. Remove the resulting three positions and repeat. The difference can be forced divisible by the prescribed modulus; the theorem does not fix the difference itself. [Kelley and Meka, *Strong Bounds for 3-Progressions*, main theorem](https://arxiv.org/abs/2302.05537)

## Why these intervals do not close the least-defect argument

If the supplied ratio-five pair has different component labels, every source in every translate has those same ordered labels. The prefix's center is $Gy$, and the actual source height includes the factor $y=(2^u q-7)/9$. The common dyadic suffix after clock six is already committed to the supplied pair. A theorem giving small representatives for most parents in a shell of *height* $X$ cannot be applied with $X$ replaced by the length $N$ of an arbitrarily positioned interval.

There is a quantitative obstruction even if one seeks the ordered **tripling** pair by a different ordinary routing. For $X\ge q>2B>0$, every $x\in[X,2X]$ landing at this $q$ on a first-arm row with $\beta\le B$ satisfies $x=G(q-\beta)$. Hence $G\le2X/(q-B)\le4X/q$, and at most $1+4BX/q$ integers can occur in the row. All clocks $e\le A\log X$ combined contribute at most $O_A((1+BX/q)(\log X)^2)$, before imposing any companion condition. At $X=q^c$ for fixed $c>1$ and $B\le q^{1-\epsilon}$ this is $o(X\exp(-C(\log X)^{1/3}))$ for every fixed $C$. Therefore even perfect control of the companion at *every* such bounded-offset row cannot overwhelm an ambient exceptional count of that size at a growing supplied first target. The inequality is a scale obstruction to this use of the rows and does not exclude large-offset paths, late clocks, different representatives of the same components, or an exceptional estimate conditional on the actual fiber.

For tripling, positive-clock landing at $(q,3q)$ from odd $(x,3x)$ is impossible because the upper path immediately becomes prime to three. PR195's common-future branch for two selected target classes avoids that obstruction. The iid recurrent mark law used above is for multiplier five. It gives no corresponding lower bound for an unabsorbed native tripling excursion ending in the desired component of $3q$. A positive ordinary unit $q$ reaching one with $3q$ failing to reach one remains unexcluded. [PR195, exact tripling obstruction](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/renewal/TRIPLING_FIBER.md) · [PR195, prescribed common future in two classes](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/reports/astra-global-closure-20261124/round7/arithmetic/TRIPLING_REVIEW.md)

The probability arguments and packing theorem are written proofs. Lean 4.34.1 with Std checked the two-arm translation, common-clock composition and span identity with warnings as errors. The explicit three-source router was checked in the same module. The six printed theorems report only `propext` and `Quot.sound`.
