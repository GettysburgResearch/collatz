# A positive all-odd ascent can suppress every fresh inverse branch

**Elementary written theorem.** Suppose $q>0$ is odd and $q\equiv-1\bmod 3^j$, $j\ge1$. It is the actual terminal of $j$ consecutive unit odd steps from the positive odd integer
$$
       a=\frac{2^j(q+1)}{3^j}-1 .
$$
Their physical multiplier is $M_j=(3/2)^j$. Read an inverse word of positive odd gaps $e_1,\dots,e_k$ backwards from $q$, with gain $g=3^k/2^{\sum e_i}$. Call it fresh if $e_1\ne1$, so it enters $q$ through a different immediate odd predecessor. Only legal ordinary positive paths are counted.

1. There is an absolute $C$ such that every fresh word with $k\le j$ has $g\le C$. There is a sequence $\delta_j\to0$, independent of $q$, such that every fresh word with $k\ge j$ has
   $$
           g/M_j\le \delta_j(3/2)^{k-2j}. \tag{1}
   $$
   In particular, over all $k\le2j+O(1)$ the supremum of the fresh **relative** gains tends to zero with $j$. Up to $(2-\epsilon)j$ they decay exponentially for every fixed $\epsilon>0$.
2. There is an absolute $K$ such that, among the positive odd $q\in[X,2X)$ in the above ternary class, a proportion tending to one has **every** fresh word of **every** grade bounded by $g\le K$, whenever $j=j(X)\to\infty$ and $j\le(\log_2 X)/1024$. Thus their full fresh supremum divided by their actual ascent multiplier is at most $K(2/3)^j$. The same assertion holds with $X\to\infty$ first and then $j\to\infty$.

**With the exact finite signed census below, the uniform cap at grades $k\le j$ is $3/8$. In the population conclusion, the full fresh maximum equals $3/8$ and only the one-edge word $e=3$ attains it. This conclusion holds simultaneously at the late phases of one ascent.** The existence of an absolute cap above uses the elementary analytic proof alone.

Here the initial ordinary sources vary. On a single supplied orbit the deterministic bound (1) applies to each segment that actually consists of $j$ unit steps. The population estimate does not force these segments or these selected terminals to recur on any one orbit. Fresh branches of a unit terminal include unit parents with positive predecessor density under the known all-unit positivity input. Branch population and relative gain can therefore have very different sizes.

Paper 178, §7, already evaluates an inverse prefix on this same signed anchor $-1$, identifies its first-visit magnitudes, and proves a nonzero limiting protected density for **all** comparison words at the rising threshold $(3/2)^j$. The two estimates here concern words leaving the main branch at the very first inverse edge. This removes every initial signed lap. It gives an absolute cap independent of $j$ for most complete ordinary trees, and the factor-two grade delay for every terminal in the ball. The finite-interval transfer below gives its own elementary proof for this bound. [The first meeting with a smaller Collatz orbit, Theorem 4](https://rstation.ai/problems/collatz/papers/178)

## The signed first-visit bound

Inverting one odd transition sends $z$ to $(2^e z-1)/3$. At the signed root $-1$, a legal word traces $-s_0=-1,-s_1,\ldots,-s_k$ with positive odd magnitudes
$$
                    s_i=(2^{e_i}s_{i-1}+1)/3.
$$
These are actual inverse odd steps for the sign-minus map, whose shortcut branches are $v/2$ and $(3v-1)/2$. A fresh word has $s_1>1$. No later $s_i$ can be one, since its forward odd image would then also be one. A repetition among $s_1,\dots,s_k$ would put one of them on a cycle whose orbit reaches the fixed point one, which is impossible. Thus $s_k$ first reaches one in exactly $k$ odd steps. In particular the legal fresh words of a fixed length $k$ have distinct positive signed magnitudes $s_k$.

There is an absolute bound on $\sum_i 1/s_i$ on these paths. For clarity, at physical clock $h=\lceil\log_2 N\rceil$ the number of distinct sign-minus images of $[1,N]$ is $O((1+h)N^\rho)$, $\rho=\max(H_2(3/5),(3/5)\log_2 3)<1$. The binary parity bijection also holds for the sign-minus map because increasing the start by $2^h$ leaves its prefix fixed and increases its image by the odd number $3^p$. A word of weight $p\le3h/5$ has image at most $3^p N/2^h$ since its additive term has negative sign. The other words number at most $2^{h H_2(3/5)}$. On the physical **first-hit** path to one, $T_-^h$ is injective outside its final $h$ states. Consequently at most $O((1+h)N^\rho+h)$ distinct magnitudes lie below $N$. Dyadic summation gives the asserted uniform reciprocal bound.

Telescoping the signed odd equations and using $s_i\ge3$ now gives
$$
       g=\frac1{s_k}\prod_{i=1}^k(1-1/(3s_i))^{-1}
           \le C/s_k . \tag{2}
$$
For $b\le j$ inverse gaps, the legal roots form one residue class modulo $3^b$. This follows either by successive inverse steps, or by pulling back each next trit test under a coefficient prime to three. Thus legality through the first $b$ gaps at $q$ is exactly the same as at $-1$. For fixed $j$, let $\mathcal S_j$ be the possible signed magnitudes at the end of $j$ fresh gaps. Each positive magnitude has at most one first-hit odd time at one, so the finite set of magnitudes up to any prescribed bound is eventually absent from $\mathcal S_j$. Set $\delta_j=\sup_{s\in\mathcal S_j} C/s$, with zero for an empty set. Then $\delta_j\to0$. Apply (2) to the first $\min(k,j)$ gaps and bound each remaining odd multiplier by $3/2$. This proves (1).

## Identifying the signed maximum by exact finite computation

The following refinement is a mathematical finite reduction followed by an integer computation. It is independent of the Lean kernel. On a simple signed first-hit path define $A_k$ to be the number of its odd magnitudes in $[2^k,2^{k+1})$. For every $k\ge1$,
$$
 A_k\le B_k=\min\left(2^{k-1},\min_{0\le p\le k}
    \left[2\cdot3^p+k+\sum_{i=p+1}^k {k-1\choose i-1}\right]\right).
$$
The shell contains exactly $2^{k-1}$ odd integers. For a $k$-clock word with $i>p$ odd inputs, its first bit is one and its remaining bits have $i-1$ ones. There is at most one starting representative per word. All other images lie below $2\cdot3^p$ by the negative carry bound, and are distinct after discarding the final at most $k$ states. The finite exact sum $\sum_{k=1}^{399}2^{-k} B_k$ is less than $22$; its complete numerator and denominator are in the control output. For $k\ge400$, the cutoff $p=\lfloor3k/5\rfloor$ gives $2^{-k}B_k\le3\cdot2^{-k/40}+k2^{-k}$ by the two entropy exponents above. The first tail is bounded by $120\sum_{a=10}^{\infty}2^{-a}=120/512$ by grouping forty consecutive $k$; the second is less than $1/2$. Thus the signed reciprocal sum is less than $23$.

For each $s_i\ge3$, $-\log(1-1/(3s_i))\le(3/8)s_i^{-1}$. Equation (2) gives $g<e^9/s_k<3^9/s_k$. If $g\ge3/8$, its source is an odd integer in $3\le s_k<8\cdot3^8=52488$. Two independent integer iterations, one odd-accelerated with memoization and one at ordinary shortcut clocks with local cycle detection, classify every such origin. Of the 26,243 odds, 8,735 reach one and 17,508 reach a different repeated state. Comparing $8\cdot3^b$ to $3\cdot2^h$ at the first visit to one for every successful source gives exactly one qualifying triple $(s,b,h)=(3,1,3)$. Its fresh signed gain is exactly $3/8$ and its word is the single gap $e=3$. [Exact verifier](check_fresh_ascent.py) · [Integer replay output](FRESH_CONTROLS.json)

This proves the sharp cap for the first $j$ gaps at every positive terminal. To obtain the exact maximum over all grades in the population statement, use $K'=1/3$ in the continuation test below for words of length greater than $j$. At most a vanishing fraction acquire any such additional word of gain greater than $1/3$. All their shorter words are already classified by the signed census, including the legal one-edge word of gain $3/8$. For this cutoff, a longer winning word has positive source at most $q/K'=3q<6X$ in a root shell $[X,2X)$; the late-visit entropy bound applies to $[1,6X]$ with the same exponent. The same replacement in the simultaneous estimate works because the factor $(K')^{-t}$ is fixed. At $j\ge2$ this winning positive predecessor is itself a multiple of three, by reduction of $(8q-1)/3$ modulo three using $q\equiv-1\bmod9$.

## Why completing the positive root does not restore a large fresh gain

Use normalized ternary Haar probability only as an intermediate count of legal residue classes. For $1<t<2$ let $G(z)$ be the supremum of gains of all finite legal inverse words at $z\in\mathbb Z_3$, including the empty word. A word with $b$ gaps has one legality class of Haar mass $3^{-b}$. Summing the $t$-th powers word by word gives
$$
 \int G(z)^t\,dz
 \le \sum_{b\ge0}\left(\frac{3^{t-1}}{2^t-1}\right)^b=C_t<\infty. \tag{3}
$$
The ratio is strictly below one because $\log(2^t-1)$ is strictly concave and agrees with $(t-1)\log 3$ at one and two. In particular $\Pr(G(z)>F)\le C_t F^{-t}$.

On the target ball write $q=-1+3^j z$ with $z$ Haar. For a fixed legal fresh prefix $w$ of $j$ odd gaps the next root is $-s+2^{\sum_{i\le j}e_i} z$, which is again Haar. If any fresh word exceeds $K=\max(2,C)$, (2) forces its length to exceed $j$. Some $j$-gap prefix must admit a continuation of gain greater than $K/g_w$. By the union bound, (2) and (3), the conditional probability of this occurrence is at most
$$
    e_j=C_t K^{-t}\sum_{s\in\mathcal S_j}(C/s)^t=o(1). \tag{4}
$$
The signed endpoints are distinct and escape every finite set, and the full series over positive $s$ converges. This estimate uses no independence between the different continuation roots.

## Transferring the infinite search back to ordinary positive integers

Put $L=\log_2 X$ and $H=\lfloor L/8\rfloor$. Words of at most $H$ gaps beating $K$ select a union of residue classes modulo $3^H$. For $j\le H$, imposing the terminal ball, odd parity and the interval $[X,2X)$ gives their count at most
$$
        \frac{X}{2\cdot3^j}\,e_j+O(3^H). \tag{5}
$$
All roots in any one class give the same legality result for these lengths. The additive error is the sum of the endpoint rounding over at most $3^H$ classes, so no bound on the number of words is needed.

For a longer winning word at a positive $q<2X$, its positive ordinary source $v$ has $v\le q/g<2X$ by the nonnegative forward affine offset. Its physical clock is at least its odd grade, hence at least $H$. Thus $q$ lies on the union of entire forward trajectories from $T^H[1,\lceil2X\rceil]$.

The latter seed set has size $O((1+L)X^{1-1/320})$. For high odd counts $p>3H/5$, any parity word has at most $1+\lceil 2X\rceil/2^H$ representatives, giving $O(X2^{-(1-H_2(3/5))H})$ such starts. At fixed $p\le3H/5$ the possible images are at most $2X3^p/2^H+(3/2)^p+O(1)$ in number, by the sharp positive carry envelope. Sum over $p$. The two inequalities $H_2(3/5)<39/40$ and $(3/5)\log_2 3<39/40$ give the claimed exponent.

For any deterministic map on a countable set, let $\mathcal O$ be the union of forward orbits of $J$ seeds. Then
$$
 \sum_{z\in\mathcal O}(\#\{w\in\mathcal O:T(w)=z\}-1)_+\le J.
$$
Add the complete forward orbits one at a time. Before hitting the previous union or repeating a vertex, each new path is injective. At a first entry into the previous union it adds at most one excess incoming edge. If the new path repeats before entering, it joins its own cycle, producing at most one excess edge there. A new simple infinite path adds none. Thus at one clock any finite subset of $\mathcal O$ loses at most $J$ distinct images, and at $h$ clocks at most $hJ$. Apply this to $\mathcal O\cap[X,2X)$ at $h=\lceil L\rceil$. Its image is bounded by the elementary translated-interval image estimate $O((1+L)X^\rho)$ from the companion note. The original shell therefore contains at most $O((1+L)^2X^{1-1/320})$ points of $\mathcal O$. [Elementary translated-interval compression](ENTRY_EDGE_GAINS.md)

The relative errors from this last count and (5) tend to zero even after multiplication by $3^j$ for $j\le L/1024$, because $\log_2(3)/1024<1/320$ and $\log_2(3)/8+\log_2(3)/1024<1$. For each fixed $j$ they of course also vanish. The odd terminals in the given class number $X/(2\cdot3^j)+O(1)$, so (4)–(5) prove the ordinary all-depth assertion.

The all-odd target-cylinder method, the signed first-visit parameterization and the use of interval compression for late ordinary visits have antecedents. The stronger high-state theorem of Weaver is also available, but the proof above needs only an $o(X/3^j)$ estimate. The statement here gives a finite, varying-source barrier to forcing large fresh relative gains at every long ascent by branch conservation. A deterministic lower bound on fresh gains along the same fixed escaping ray remains open. [Physical late visits to high targets, Paper 219, §3](https://rstation.ai/problems/collatz/papers/219)

## One ordinary ascent through every late phase

There is a simultaneous version on the trajectory of the **same** source at all the phases under consideration. For even $u\in[X,2X)$ set $a=2^n u-1$ and $q_j=3^j2^{n-j}u-1$ for $0\le j\le n$. These are positive odd integers connected by unit odd steps. Uniformly in $J\le n\le(\log_2 X)/1024$, the proportion of those even $u$ for which some $J\le j\le n$ has a fresh inverse word of any grade with gain greater than $K$ is at most
$$
                   \sum_{j\ge J}e_j+o_{X\to\infty}(1). \tag{6}
$$
In particular the iterated upper limit is zero as $J\to\infty$. The first-hit signed layer sets $\mathcal S_j$ are disjoint as $j$ varies, because each signed magnitude has just one first-hit time. Thus (4) gives the absolutely convergent series
$$
   \sum_{j\ge1}e_j
       \le C_t K^{-t} C^t\sum_{s\ge3} s^{-t}<\infty.
$$
At phase $j$, the free ternary coordinate of $q_j$ is $2^{n-j}u$, a ternary unit multiple of the actual common parameter $u$. Its finite residue law has one visit to every class in a period, also after imposing even parity on $u$. For $Y=3^j2^{n-j}X$ use $H_j=\lfloor(\log_2(Y+1))/8\rfloor$ in the finite-word test, which costs $O(3^{H_j})$ rounding in the $u$ count. The root interval $[Y-1,2Y)$ lies in a union of at most two comparable factor-two intervals, so the late-word argument costs $O((1+\log Y)^2Y^{1-1/320})$ absolute exceptions, even after restricting to our progression of ordinary roots. Equivalently one may center the interval at $[Y-1,2(Y-1))$ and include its two possible extra integers.

Now $Y\le 3^nX\le X^{1+\log_2(3)/1024}$. Both error bounds summed over $n=O(\log X)$ phases are $o(X)$. In the second one use $(1+\log_2(3)/1024)(1-1/320)<1$. The first one uses $\log_2(3)(1+\log_2(3)/1024)/8<1$. The union bound directly in the original $u$ interval proves (6), without independence between phases. This establishes the barrier while retaining the same positive initial anchor during all $n$ steps. A fixed positive integer can supply only a finite initial all-odd ascent, since the $n$-step condition forces a growing power of two to divide $a+1$.

The kernel file [FreshAscentShadow.lean](FreshAscentShadow.lean) proves the integer endpoint uniqueness, full-list shift, transfer to the signed fixed point, and the two strict magnitude inequalities after leaving the fixed point. It does not formalize either the counting estimates or their limiting assertions.

## Where a smaller ordinary visitor can first attach

Let $a=2^n-1$ and $Y_i=3^i2^{n-i}-1$ for $0\le i\le n$. These form the actual increasing shortcut ascent through the even peak $Y_n$. Fix a factor $F>1$ and take any ordinary positive visitor $w<a/F$ reaching $Y_u$. Use its first visit to $Y_u$. Let $Y_i$ be its first contact with the displayed prefix $Y_0,\ldots,Y_u$. Determinism carries it from $Y_i$ along the prefix to $Y_u$. Let $k$ count odd departures from $w$ up to that first prefix contact.

For $i\ge1$ the first inverse edge differs from the known predecessor, since otherwise $Y_{i-1}$ would have been visited already. Indeed the only odd immediate shortcut predecessor of $Y_i$ is $Y_{i-1}$; the competing predecessor must be $2Y_i$. Remove any initial halvings from $w$, leaving an odd value $w'\le w$. There is an odd departure before the contact since an all-halving path from $w<Y_i$ cannot reach $Y_i$. Read backward to this $w'$ in blocks of one odd inverse and its preceding inverse doublings. The first exponent differs from one. When the endpoint is the even peak, this first block is a partial final coast of the physical path. Its exact row is still $3v+1=2^eY_i$. Every later inverse output is odd. The signed-root proof uses these rows and $Y_i\equiv-1\bmod3^i$, so it applies unchanged.

The first-visit physical segment is simple. Its nonnegative correction product $\prod(1+1/(3v))$ is at most an absolute $C_+$ by the same elementary short-clock sparsity proof, allowing its last $h$ physical states as in the signed argument above. Since $Y_i+1=(3/2)^i(a+1)$, the path from $w'$ to $Y_i$ has gain
$$
    g\ge \frac{Y_i}{C_+ w'}>\frac F{C_+}(3/2)^i .
$$
The absolute cap for $k\le i$ excludes that case at sufficiently large $i$. Equation (1) then gives the following uniform lower bound for the total **surplus odd count** $d$ of the witness up to $Y_u$:
$$
     d=(k+u-i)-u=k-i
       \ \ge\ i+\log_{3/2}\!\left(\frac F{C_+\delta_i}\right)
       =i+\omega(1)   \quad(i\to\infty). \tag{7}
$$
An empty signed layer means that such a word of grade at least $i$ cannot occur. Thus witnesses of a given bounded surplus must first attach near the beginning of the actual ascent, even if the reported meeting is at a much later phase. Equation (7) restricts a visitor that exists and leaves its existence unresolved.
