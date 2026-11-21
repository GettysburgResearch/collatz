# Simultaneous Collatz returns for a growing interval

**PROPOSED.** Write $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. A profile at clock $h$ records the ordinary endpoint and the number of odd inputs before that clock. On a binary class these two entries specify the entire affine endpoint as the initial parameter varies.

**Theorem.** Take all $M$ consecutive starts $x+i$, $0\le i<M$, and all $M$ companions $5(x+i)$. There is a binary class of depth at most $C\log^2(2M)$ on which, at the same clock, every first arm has profile $(z,p)$ and every companion has profile $(5z,p)$. The endpoint $z$ varies with the lift. In fact the clock by which a random binary input has seen this event has median of order $\log^2(2M)$ for $M\ge2$. These are absolute constants. Every realized finite word works on its entire ordinary positive residue class.

For a fixed arithmetic progression for the first index and any specified $q\ge1$ coprime to six, one can further arrange $z=q$ and $5z=5q$, with the last index at most
$$
                 q\exp\!\left(\exp(C_m\log^2(2M))\right).             \tag{1}
$$
The additional clocks used to prescribe $q$ are outside the median estimate. This quantifies the height cost of packing an entire block into the comparison at one supplied integer.

## Compressing a random block of affine profiles

Use uniform independent low binary digits of $x$. At clock $h$, write $x=r+2^h w$ with $0\le r<2^h$. Each current arm is
$$
                     b3^{p_i}(w+U)+e_i,\qquad b\in\{1,5\},
$$
where $U$ is common and $e_i\ge0$. Initially $U=0$, $e_i=bi$. Within each group retain one representative for each distinct profile. Coincident profiles persist at every later clock. Write $K_h$ for the combined representative count and $S_h$ for the sum of $\sqrt{e_i}$ over these representatives, counting the two groups separately.

On exposing another $j$ digits $v$ of $w$, an arm gains $l$ odd inputs and has ordinary affine remainder $R$. The new common center is $(v+U)/2^j$ and its error is $3^l2^{-j} e_i+R$. Each individual arm sees independent fair parity bits conditional on the old class, because its free slope is odd. The error updates one bit at a time by $e'=(3^\epsilon e+\epsilon)/2$. Consequently
$$
 \mathbb E(S_{h+j}\mid\text{old class})\le \rho^j S_h+C K_h,
 \qquad \rho=(1+\sqrt3)/(2\sqrt2)<1.                                 \tag{2}
$$
Indeed the expected square root contracts by $\rho$ and receives a bounded additive term at each step. Retaining one copy of equal profiles can only reduce the final sum.

For any $B\ge1$ and any realized class, those representatives with $e_i\le B$ have at most $\lfloor B\rfloor+1$ integer endpoints per group and per odd count. The rest cost at least $\sqrt B$ each in the sum. Hence
$$
                 K_h\le 2(h+1)(B+1)+S_h/\sqrt B.                    \tag{3}
$$
These expectation inequalities avoid conditioning on a sequence of unusually favorable digit blocks. They strengthen the earlier deterministic thinning construction. [Earlier profile bound](AFFINE_RAYS.md#a-polynomial-synchronization-time-for-a-whole-interval)

Here are details of the iteration. Put $P=\lceil\log_2(2M)\rceil$, $\nu=3/4$, $a_l=\nu^l P$, $Q_l=P2^{a_l}$, also using $a_{-1}=P/\nu$. In round $l$ expose $j_l=\lceil D a_l\rceil$ digits. Stop at the first $r$ with $a_r\le1$. Total exposed length is at most $C_D P$. Choose the absolute $D$ large enough that $\rho^{j_0}M^{3/2}\le Q_0$ and $\rho^{j_l}Q_{l-1}\le Q_l$ for every round. Denote the two expectations after $l$ rounds by $k_l,s_l$. Initially $k_0=2M$ and $s_0=O(M^{3/2})$.

There is an absolute $A$ such that $k_l\le A Q_l$ throughout and $s_{l+1}\le 2CA Q_l$ with $C\ge1$ as in (2), enlarged for the initial bound. To see the induction explicitly, also choose $D$ so that $\rho^{j_l}Q_{l-1}\le Q_l/2$ for $l<r$ (where $a_l>1$). Then (2) gives the asserted bound on $s_{l+1}$. In (3) take $B=\max(1,(s_{l+1}/P)^{2/3})$. This gives
$$
 k_{l+1}\le C'_D(P+P^{1/3}s_{l+1}^{2/3})
          \le C''_D(1+A^{2/3})P2^{(2/3)a_l}\le A Q_{l+1}
$$
by choosing $A$ sufficiently large after $D$. The first round uses $s_0$ directly. Since $a_{r-1}\le1/\nu$, at a deterministic $h=O(P)$ both $\mathbb E K_h$ and $\mathbb E S_h$ are $O(P)$.

## A sharp clock scale for coalescence within the two groups

At this $h$ sort the surviving profiles in each group by nondecreasing odd count. Consecutive representatives with counts $p,p+s$ have endpoints $X,Y=3^s X+d$ with $s\ge0$, $d\in\mathbb Z$ and
$$
                          |d|/3^s\le e_X+e_Y.
$$
On fresh digits $X$ is binary uniform since its parameter slope is odd. The equal-slope absorption estimate gives the conditional probability that this edge has yet to tie both counts and endpoints after $u$ more steps as at most $C(1+s+\sqrt{|d|/3^s})/\sqrt u$. In its oriented process a reversal exchanges the two arms, and absorption means equality of affine forms. This is stronger than merely encountering the same number at one point. [Oriented absorption estimate](GROWING_ADDITIVE_GAPS.md#reaching-a-small-normalized-offset)

The $s$ terms telescope to at most $2h$ across both lists. Each representative contributes to at most two neighboring errors. Taking a union bound and then expectation shows that the first time $G$ at which each group has just one profile obeys
$$
             \Pr(G>n)\le C\min(1,P/\sqrt n).                         \tag{4}
$$
Here one uses $n-h\ge n/2$ when $n\ge2h$ and enlarges the constant for the smaller clocks. The two surviving groups need not yet have endpoint ratio five.

There is a matching lower bound for $M\ge2$. Put $b=\lfloor\log_2 M\rfloor$. After exposing the first $b$ digits, the consecutive starts include one congruent to zero and one congruent to $-1$ modulo $2^b$. Their first $b$ parities are all zero and all one respectively, giving a count difference $b$. From that point their signed count difference has increments zero or a fair sign, with the choice to hold or jump determined before the fresh bit. One can supply an independent sequence of fair signs at jumps. A simple walk from $b$ stays positive through $n$ signs with probability at least $c\min(1,b/\sqrt n)$ by reflection. On this event the pair has yet to tie. For $n<b$, a tie of the whole group would persist to $b$ and contradict the two displayed counts. This proves the matching order in (4). For a median lower bound take $u\le c_0 b^2$ more steps after clock $b$. The probability of hitting zero is at most $u/b^2$ by the martingale maximal inequality for the independent sign walk. Small $b$ is covered by $G\ge b$. [Reflection bound](THREE_RAY_CLOCKS.md#avoiding-level-zero)

## Returning both lists to a prescribed pair

Let $J$ be the first clock at which both groups have tied and the reference pair has equal counts and exact ratio five. The next estimate controls the entire waiting-time distribution up to a logarithmic factor,
$$
 c\min(1,P/\sqrt n)\le \Pr(J>n)
 \le C\min\!\left(1,\frac{P}{\sqrt n}\left[1+\log_+(n/P^2)\right]\right),
 \quad M\ge2.                                                         \tag{5}
$$
Here $\log_+ t=\max(0,\log t)$. The lower bound follows from $J\ge G$. For the upper bound assume $n\ge4P^2$ and stop the common source-bit filtration at $S=G\wedge\lfloor n/2\rfloor$. The reference signed level $k$ is a martingale for this filtration. Up to clock $P^2$ the expected absolute stopped level is at most $P$ by its conditional variance bound of one per step. On a subsequent dyadic segment $[t,2t]$, the expected absolute increment of the stopped level is at most $\Pr(S>t)\sqrt t=O(P)$. To see this, condition at $t$ and apply the second-moment bound for at most $t$ further steps on the event $S>t$. Summing yields
$$
             \mathbb E|k_S|\ll P[1+\log(n/P^2)].
$$
Likewise $\mathbb E\sqrt{1+S}\ll P[1+\log(n/P^2)]$ by integrating (4). From (1a) in the companion note, the conditional probability of missing the root for the remaining $n-S$ steps is bounded by $C(1+|k_S|+\sqrt{\log(2+R_S)})/\sqrt n$. Its final numerator term is deterministically $O(\sqrt{1+S})$. On $G\le\lfloor n/2\rfloor$ any such root ties the two lists as required. Adding $\Pr(G>\lfloor n/2\rfloor)$ proves (5). The same proof works with $S=\max(G,v)\wedge\lfloor n/2\rfloor$ for any fixed delay $v$, with constants depending on $v$. [Reference-root hitting estimate](FIVE_RETURN_CLOCK_AND_TERMINALS.md#the-first-return-tail)

Taking $n$ a sufficiently large absolute multiple of $P^2$ makes the right side of (5) smaller than one half. The median lower bound for $G$ thus completes the sharp median statement for $J$. There is a uniform ordinary consequence. In every interval of $N$ consecutive possible first indices, if $\log(2M)=o(\sqrt{\log N})$, all but $o(N)$ first indices synchronize the two full lists by clock $\lfloor\log_2 N\rfloor$. Indeed the test through $n$ is periodic modulo $2^n$. At this choice of $n$ any such interval is covered by two periods, and (5) tends to zero.

For any fixed initial congruence modulo $2^v$, the probability of failure conditional on it is at most $2^v$ times the unconditional failure bound. Thus some such prefix gives the required joint class at clock $H=O_v(P^2)$, which may be taken at least $v$. Once a joint return has occurred, arbitrary extra steps can lose the reference ratio, so take the successful clock itself. If it occurs before $v$, first require a reference return at or after $v$ using the delayed form of (5). The final free-parameter slope of the first arm is $3^p$ with $p\le H$.

For a full modulus $m$, now impose its odd part and apply the exact modular construction already proved for ratio-five returns. Its steering modulo the factor of $m$ prime to six and its short terminal preparation use $O_m(1)$ clocks. The final first-arm values run through $z_0+3^{P'}m' t$ with $P'\le H+O_m(1)$ and $m'$ fixed and coprime to six. A final doubling exponent $b$ giving $2^b q$ in this progression has a period $O_m(3^{P'})$. On the canonical binary representative the endpoint and modulus have logarithms $O_m(H+1)$ by the ordinary affine formula. One can therefore take a nonnegative lift with $b=O_m(3^{P'}+H+1)$. Substitution in the source progression and addition of the $M-1$ shifts prove (1). All intermediate identities hold on positive integers. [Prescribed endpoint construction, section 2](FIVE_RETURN_IN_EVERY_CLASS.md#2-prescribing-the-two-endpoints-and-the-full-arithmetic-progression)


The height and clock controls also give **many disjoint blocks landing at each specified pair**. Fix an odd ternary unit $q_0$. The two-child inverse construction in the earlier comparison theorem gives at least $c_{q_0} Z^\beta$ different odd ternary units $q\le Z$ that reach $q_0$ with equal-count ratio-five returns. Here $\beta=1/\log_2(2^{23}/9)>0$. In brief, the children $(2^L q-7)/9$ use the length-six return and final halvings. Two choices of $L\le23$ give ternary units and the common parent is uniquely recovered by two odd steps. One fixed tree level therefore supplies the stated number of distinct inputs, even if paths from different levels overlap. [Exact two-child construction](FIVE_RETURN_IN_EVERY_CLASS.md#3-simultaneous-blocks-and-the-gap-to-a-proof)

Take $M=\lfloor\exp(c_m\sqrt{\log\log X})\rfloor$ with $c_m>0$ sufficiently small. The height factor $K_m(M)$ on the right of (1) is then $X^{o(1)}$. The clock to each intermediate target $q$ is at most $H+O_m(1)+b\le\exp(O_m(\log^2(2M)))=X^{o(1)}$, uniformly in $q$. Apply (1) to the tree inputs $q\le X/K_m(M)$. Each resulting first index has at most one intermediate target at a given clock, so it is counted at most $X^{o(1)}$ times. Among those distinct blocks, greedy selection keeps at least one in every $2M-1$ as pairwise disjoint. Thus at least $X^{\beta-o(1)}$ **disjoint** blocks of this growing length occur below every sufficiently large $X$ in the chosen progression of first indices. Each block reaches the *same* supplied pair $q_0,5q_0$ on all its arms. The clock may vary across blocks.
## A criterion for the full conjecture

Let $C$ consist of the starts that reach one. Write $F_m(X)$ for the longest consecutive block in $[1,X]$ on which $x\in C$ and $5x\notin C$ at every index, with the first index in any one fixed residue class modulo $m$. Put $F_m(X)=0$ when no block exists. If Collatz fails, the global five-closure criterion gives one positive $q$ coprime to six with $q\in C$ and $5q\notin C$. Inverting (1) with this *fixed* $q$ yields, for all sufficiently large $X$,
$$
                F_m(X)\ge \exp(c_m\sqrt{\log\log X}).
$$
In particular, a zero lower limit of $\log(1+F_m(X))/\sqrt{\log\log X}$ even for one progression would settle the conjecture. The same necessary lower growth holds for the longest consecutive block all of whose starts fail to reach one, by taking as the first-arm target a ternary unit in any nonconvergent component. Such a unit is obtained by removing powers of two, taking an odd step, and removing powers of two again. These unconditional implications quantify the size of the blocks any counterexample must produce. Proving the opposing upper bound for the actual basin, or proving five-closure at every terminal in the companion note, remains open. [Five-closure equivalence, GCM-002](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md)

The [exact replay](check_whole_interval_returns.py) verifies complete block profiles at sizes 2, 5, 12 and 24, including their total odd counts and two independent positive lifts of each class. Equations (1)–(5) are analytical claims for unbounded sizes.
