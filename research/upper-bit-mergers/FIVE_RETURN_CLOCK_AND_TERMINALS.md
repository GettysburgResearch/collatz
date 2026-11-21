# The first ratio-five return and the last ordinary return

**PROPOSED.** Let $T$ be the shortcut Collatz map. At clock $t$ put $X_t=T^t(x)$, $Y_t=T^t(5x)$, with odd-input counts $p_X(t),p_Y(t)$. A **root** means $Y_t=5X_t$ and $p_Y(t)=p_X(t)$. Both conditions matter. We obtain a sharp first-return tail under binary Haar input and an effective last-return deadline on each ordinary input supplied with a path to one. Together they identify a sparse ordinary set on which the full forward-five implication is equivalent to Collatz.

## The first-return tail

The state is $(k,c)$ with $k=p_Y-p_X$, $c=Y-5\,3^kX$. Its origin is a root. Binary Haar input means that every length-$n$ source parity word has probability $2^{-n}$. From the full-state estimates (S4), (S6), (S8)–(S11) of PR 171 and the signed-state control in PR 146 we prove
$$
             c_0 n^{-1/2}\le \Pr_{(0,0)}(\tau^+>n)\le C_0 n^{-1/2},\qquad n\ge1,       \tag{1}
$$
where $\tau^+$ is the first positive root time. The same order holds conditional on $x$ odd. In particular the positive moments of $\tau^+$ are finite exactly for orders below $1/2$. [Full-state estimates, S4–S11](https://github.com/GettysburgResearch/collatz/blob/2bd243b3e05eaa5543adeb2894637b053c9662ca/research/adaptive-closure-20261121/AFFINE_SECTION_RECURRENCE.md) · [Signed-state control, section 1](https://github.com/GettysburgResearch/collatz/blob/66970775e4bdc945a68308e37a8eb028ebde42d2/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md)

For the proof sample the chain every three clocks. Write
$$
 R=\sqrt{|c|/(1+5\,3^k)},\quad
 g(k)=(10^6+k^2)^{-1},\quad V=\log(10^6+k^2)+g(k)R/100,\quad W=|k|+V.
$$
The skeleton difference $\Delta k$ has conditional mean zero, magnitude at most three and conditional variance at least $1/4$. For $|k|\ge3$ its sign cannot cross strictly in three steps, so the conditional drift of $|k|$ is zero. For $|k|\le2$ this drift is at most three. Outside the finite set $F=\{|k|\le2003, R\le10^{11}\}$ the drift of $W$ is nonpositive. At large $|k|$ this follows from (S10)–(S11), and at $|k|\le2$ with $R>10^{11}$ the upper bound
$$
       3+3/1000+g(k)(-2R/25+211/100)/100
$$
is negative. Finiteness follows from the state lattice $c\in 3^{-\max(0,-k)}\mathbb Z$. On $F$ the positive drift has a finite upper bound $B$.

Every state in $F$ has a fixed parity word to the root by the control theorem. Its integer offset there is $3^{\max(0,-k)}c$. Pad with zero bits at the root to one common length $3L\ge3$. At each skeleton visit to $F$ there is therefore probability at least $\epsilon=2^{-3L}$ of hitting the root on the skeleton within $L$ skeleton steps. Start a trial on the first visit and then at the first visit at least $L$ steps after the previous trial start, provided the root has yet to be hit. The expected number of trials is at most $1/\epsilon$, and each trial accounts for at most $L$ pre-hit visits to $F$. This bounds the total expected number of such visits even if the chain is killed earlier.

From a nonroot state $z$, stop the skeleton on reaching the root or $|k|\ge A$. Denote this time by $\sigma$. For $|k_0|<A$, finite-time stopped drift identities give
$$
 \mathbb E W_{\sigma\wedge j}\le D_z=W(z)+BL/\epsilon,\qquad
 \tfrac14\mathbb E(\sigma\wedge j)
 \le\mathbb E k_{\sigma\wedge j}^2-k_0^2\le (A+3)D_z.
$$
The second inequality uses the uniform conditional variance, bounded overshoot and $W\ge |k|$. Exiting before the root by time $j$ costs probability at most $D_z/A$. Survival inside the strip up to $j$ costs at most $4(A+3)D_z/j$. Take $A=\lceil\sqrt j\rceil+1$. For initial $|k_0|\ge A$ the resulting bound is already trivial. Including clocks between skeleton samples gives for any state the ordinary first-hit bound $C(1+W(z))/\sqrt n$, with time zero allowed. From the root, first take one prescribed or random step and apply this bound to the resulting finite list of states. This proves the upper bound in (1).

For a lower bound condition on an odd first step. The first two carries are $-2$ and then either $-1$ or $-5$, with level zero. At the third step the level is $+1$ or $-1$ and no earlier positive root has occurred. At each subsequent step the choice to jump is predictable and the sign at a jump is fair. Supply independent signs at jumps and extend the sequence with unused independent signs when needed. The probability the associated simple random walk avoids zero for $n$ signs is at least $c/\sqrt n$ by reflection. It then also avoids zero for the actual number of jumps in the next $n$ clocks. This proves (1), with the small clocks covered directly. [Reflection argument](THREE_RAY_CLOCKS.md#avoiding-level-zero)

We will also use a version less sensitive to large carries. From (S6), after $b=\lceil C\log(2+R_0)\rceil$ steps one has $\mathbb E R_b=O(1)$ for sufficiently large absolute $C$. The level martingale gives $\mathbb E|k_b|\le |k_0|+\sqrt b$ by its bounded increments. Since $W\ll1+|k|+R$, applying the preceding hitting estimate at $b$ gives
$$
 \Pr_z(\tau>n)\ll (1+|k_0|+\sqrt{\log(2+R_0)})/\sqrt n.             \tag{1a}
$$
If $n<2b$ the right side already dominates a constant. This first-hit version allows time zero. From the root, (S5) also gives the deterministic bound $\log(2+R_t)=O(t+1)$ on every word by iterating $R_{t+1}\le\sqrt{3/2}\,R_t+1$.

## Delays, shrink factors and ordinary intervals

Mark a root when its source endpoint is odd. Conditional on the initial source being odd, clock zero is marked. The gaps $L$ between consecutive marks are independent with one common law. Indeed the odd bit revealed by a mark is prescribed. All later bits are fresh. After leaving that mark the first positive root has the conditional tail (1). Wait there for the first odd bit, with any intervening zero bits keeping the section at its root. This adds a geometric waiting time with fresh bits. Thus $\Pr(L>n)\asymp(1+n)^{-1/2}$. Regeneration can equivalently be recorded just after the bit of each marked clock has been consumed.

Let $u_j$ be the probability that $j$ is marked, including $u_0=1$. Then
$$
                          \sum_{0\le j<H}u_j\asymp\sqrt H\qquad(H\ge1).
$$
For the upper bound, the renewal generating function at $z=e^{-1/H}$ equals $(1-\mathbb E z^L)^{-1}$. Its denominator is at least $(1-e^{-1})\Pr(L\ge H)$. For the lower bound, take $l=\lfloor c\sqrt H\rfloor$ gaps. The chance any exceeds $H$ is $O(c)$ and the expected sum with gaps truncated to $H$ is $O(l\sqrt H)$. For small absolute $c$ the $l$th mark occurs before $H$ with probability at least $1/2$. The initial mark covers bounded $H$.

For $1\le H\le n/2$ the probability of no mark in $[H,n]$ is exactly $\sum_{j<H}u_j\Pr(L>n-j)\asymp\sqrt{H/n}$, by partitioning according to the last mark. For $H>n/2$ the same lower bound up to constants follows by monotonicity from $H=\lfloor n/2\rfloor$, and the upper bound is one.

For $0<\theta\le1$, call a mark at $j$ a slope success if $3^{p_X(j)}2^{-j}\le\theta/2$. The probability there is no such success during $[H,n]$ has order
$$
        \min\!\left(1,\sqrt{(1+H+\log(1/\theta))/n}\right).          \tag{2}
$$
Indeed no such mark can occur before $\log_2(2/\theta)$. For the upper bound choose $K=\max(H,\lceil C\log(2/\theta)\rceil)$ so that $3^{3j/5}2^{-j}\le\theta/2$ for $j\ge K$. If $K>n/2$ a constant upper bound suffices. Otherwise a bad last mark at $j\ge K$ requires $p_X(j)>3j/5$, with probability $O(e^{-a j})$ by the binomial tail (conditioning on an odd first bit costs at most two). Given a mark there, the next gap is independent of its prefix. The sum of $O(e^{-aj})\Pr(L>n-j)$ for $j\ge K$ is $O(1/\sqrt n)$ by splitting at $n/2$. Combine with the bound for last mark below $K$.

There is also an ordinary version of (2). In any interval of $N$ consecutive positive integers restrict to odd $x$ coprime to three. Put $n=\lfloor\log_2 N\rfloor-4\ge1$. The fraction with no root in $[H,n]$ having odd endpoint $y\le\theta x$ has the order in (2), uniformly for $1\le H\le n$. The binary part of any marked prefix test through $n$ has period $2^{n+1}$. Combined with the ternary condition the period is $3\cdot2^{n+1}\le N$, so counts are comparable with absolute constants to the corresponding periodic densities. For the lower bound an ordinary endpoint satisfies $T^j x\ge2^{-j}x$, so a success requires a mark at $j\ge\log_2(1/\theta)$ as well as $j\ge H$. For the upper bound the affine remainder for $j\le n$ is at most $(3/2)^n-1$, by one-step induction. A slope success implies $y\le\theta x$ as soon as $x\ge2(3/2)^n/\theta$. If $\theta\ge N^{-1/10}$, the discarded fraction is $O(N^{\log_2(3/2)+1/10-1})=O(1/\sqrt n)$. For smaller $\theta$ the right side of (2) is bounded below by an absolute constant. The matched bounds refer to this finite-clock certificate and count equality.

## A computable terminal comparison for every certified source

Let $x$ be any positive integer with a supplied ordinary path to one. Set $d$ equal to its first-hit clock and $p=p_X(d)$. Every root along this particular pair occurs by
$$
                             d+\min(2p,120).                            \tag{3}
$$
In particular (3) requires no convergence input about $5x$.

If a root occurs at $t\ge d$, its source is one or two and its target is five or ten. The target path through $t$ is simple, since a repeat would trap its future in a cycle, while its endpoint reaches one and lies outside the $1,2$ cycle. For either arm multiply the odd-step corrections $1+1/(3v)$ over its odd inputs $v$ before $t$. In the exact product formula the initial ratio is five, the output ratio is five, and both counts are equal. Therefore these two correction products are equal. The source post-hit alone contributes $(4/3)^u$, $u=\lceil(t-d)/2\rceil$. Every preterminal odd target input is at least three, hence $(4/3)^u\le(10/9)^{p+u}$. Since $6/5>10/9$ this gives $u\le p$. Distinct odd target inputs are at least $3,5,7,\ldots$ in sorted order. Since $\sum_{i=1}^s 1/(2i+1)\le\tfrac12\log(2s+1)$ by integration, the same comparison yields the elementary refinement $u\le\log(4p+1)/(6\log(4/3))$.

For an absolute bound, let $A(v)$ count odd target inputs at most $v$. The finite simple-path estimate T-A3-651 gives $A(v)\le5v^{39/40}$. Also $A(v)\le v/3+2$. Indeed after the first odd step every state is a ternary unit and the odd units occupy two classes modulo six. Integrate $A(v)/v^2$ up to $L=15^{40}$ with the latter bound and above $L$ with the former. The sum of reciprocal odd inputs is at most
$$
       (40/3)\log 15+2+200/15<52.
$$
Here $\log15<11/4$, as follows by truncating the positive exponential series after degree six. Thus $u\log(4/3)<52/3$. Since $\log(4/3)>2/7$, the even integer $2u$ is less than $122$, hence at most $120$. This proves (3). The source-rank and logarithmic bounds above require only the elementary product argument. [Finite simple-path estimate T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md)

Take the last root, including time zero, and call its first endpoint $\pi(x)$. This is a uniquely determined odd positive integer, since an even root gives another root one step later. The pair from $\pi(x),5\pi(x)$ admits no positive root, by additivity of counts and determinism. Call such a source terminal. Also $x$ and $\pi(x)$ share their future, as do $5x$ and $5\pi(x)$. Thus proving $5r$ reaches one for every certified terminal $r$ coprime to three would prove full Collatz by the global forward-five criterion. When starting with a ternary unit, its iterates remain ternary units. Formula (1) shows there are at most $O(N/\sqrt{\log(2N)})$ certified terminals in any interval of $N$ positive integers, by counting all prefixes without a positive root. Each individual certified terminal $r$ coprime to three nevertheless has arbitrarily long consecutive blocks in its inverse image under $\pi$, starting in any fixed progression, by the equal-profile construction in the companion note. This gives long blocks of actual failed comparisons if even one terminal fails. [GCM-002](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md) · [Block construction](WHOLE_INTERVAL_SYNCHRONIZATION.md)

The entire family $r=(4^a-1)/3$, $a\ge2$, $3\nmid a$, already consists of certified terminals. Its source reaches one at $d=2a$ with one odd input. At clocks one and two the carries are $-2,-1$, since the first source iterate is even. The target's first iterate is $5\cdot2^{2a-1}-2$, and its second is odd, giving at least two odd inputs by clock three. Thus there is no positive root through $d$. For a later root $u\ge1$, whereas the elementary product inequality with $p=1$ gives $(6/5)^u\le10/9$, a contradiction. Thus the whole family survives the terminal reduction regardless of what its multiplied companions do. Proving closure on every certified terminal remains the pointwise task.

## Exactly which finite prefixes contain ordinary terminals?

**Every one that has avoided a positive root.** More precisely, fix $h\ge1$ and a residue $r\bmod 2^h$. There is a certified ordinary terminal in that residue if and only if its prefix contains no root at clocks $1,\ldots,h$. In the affirmative case it contains infinitely many, with any prescribed initial residue modulo a fixed power of three. Necessity follows from the definition. Here is a construction for sufficiency. Such a prefix necessarily starts odd, since an even first bit gives an immediate return.

In fact **every surviving cell can be steered to the same state $(61,2)$ without a root**. Use the earlier linear-length control from the current state, stopping just before its first root. Formula (S1) gives only two nonroot predecessors of the root. They are $(-1,-1/3)$ with a zero source bit and $(1,5)$ with a one source bit. The equal-level odd branch would require $c=4/3$, outside the level-zero lattice, and the equal-level even branch would already be at the root. From $(1,5)$ take a zero instead, reaching $(2,8)$. From $(-1,-1/3)$ take a one followed by five zeros. The successive rational states are
$$
 (-2,-4/9),\ (-2,-2/9),\ (-2,-1/9),\ (-1,1/3),\ (0,1),\ (1,2).
$$
From either $(2,8)$ or $(1,2)$ use only zero source bits. The carry follows the ordinary orbit of eight or two. Each time it passes from one to two the level increases by one. Stop at $(61,2)$. The extra length after the detour is bounded by an absolute constant, so the total refined length $H$ is $O(h+1)$.

Write the refined first index as $x=r'+2^H t$ and its current source endpoint as $z=z_0+3^p t$. Here $p\ge1$ and $3\nmid z_0$, because the initial source was odd. To force $x$ into any specified class modulo $3^a$, fix $t\equiv t_0\pmod{3^a}$. The condition $z=2^b$ reduces to $2^b\equiv z_0+3^p t_0\pmod{3^{p+a}}$. Its right side is a unit and two generates the unit group, so there are arbitrarily large $b$ giving actual positive lifts. Choose $b\ge2$. The source then reaches one for the first time at $d=H+b$, as any earlier hit would already have trapped it in $1,2$. During these $b$ halvings its level can only increase. During the next 120 steps the source has just 60 odd inputs, so the level stays positive. The deadline (3) excludes any later root. Each lift is therefore a certified terminal in the original prescribed cell. Its companion even has a common explicit description at the source first hit,
$$
 T^d(5x)=5\cdot3^{61+\lfloor b/2\rfloor}
       +\begin{cases}2,& b\text{ even},\\1,& b\text{ odd}.\end{cases}
$$
Indeed the carry alternates between two and one during the $b$ halvings. This describes the constructed representatives in each cell. It does not transfer convergence from them to other integers sharing the same prefix.

In particular the number of binary classes modulo $2^h$ occupied by actual certified odd terminals coprime to three is $\asymp 2^h/\sqrt h$ by (1). This counts occupied classes, without a height limit on the representative. Within the binary integers the closure of these ordinary terminals is exactly the closed set of infinite words avoiding every positive root. This closure has Hausdorff dimension one. For a direct lower bound, fix a root-free prefix ending at level one (for example the source parities $100$). Along future words give a depth-$j$ cylinder mass $2^{-j}k_j$ until the first level-zero visit, and zero from that visit onward, where $k_j$ is its final level. These are consistent masses of total one by the signed-level martingale, killed at zero. Each is at most $(j+1)2^{-j}$. For every $s<1$ this is at most $C_s2^{-sj}$, which implies dimension at least $s$ by summing over binary cylinder covers. The ambient space gives the opposite bound of one. The countable set of ordinary representatives itself has dimension zero.

This characterization decides the existence of certified terminals on **every** finite binary prefix. The unresolved implication concerns the companion of each individual terminal.

The [exact finite replay](check_whole_interval_returns.py) verifies the renewal convolution and the last-mark identity using all odd residues modulo $2^{14}$, checks the terminal computations against complete ordinary trajectories on supplied fixtures, and constructs terminals in every surviving eight-bit class at three prescribed ternary residues.
