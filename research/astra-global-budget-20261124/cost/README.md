# Paying for an ordinary path through multiple scales

**Universal cost bound OPEN.** All clocks below are raw shortcut clocks. Let
$T(n)=n/2$ for even positive integers and $T(n)=(3n+1)/2$ for odd ones.
Use ordinary binary length $b(n)$ and charge an edge $u,v$ the toll
$1/\max(b(u),b(v))$. We stop the bill at the first visit to 1.
The earlier [threefold-band bound](../../astra-two-centre-20261124/rewriting.md)
was per visit. Here a change in the size of a state never restarts the clock.

## An exact lifetime budget and its last eligible clock

For a word of length $t$, with ones at zero-based positions $a_1<\dots<a_p$,
write $C=\sum_{j=1}^p3^{p-j}2^{a_j}$. On its physical cylinder
$2^t z=3^p x+C$. At each prefix of the *same* ordinary source $x$,
maximize $C'$ among **all** words of that length and weight with
$C'\equiv C\pmod {3^p}$. Put $g_t=(C'-C)/3^p$.

1. The maximizing word has a positive integral source $y=x-g_t$ at that same endpoint. Inverting its branches from $z$ gives rationals with denominator a power of three; the initial source is integral by the congruence. Forward evaluation from this integer shows every intermediate denominator also divides a power of two, so every intermediate value is integral. At an integer endpoint $z'\ge1$, each integral inverse $2z'$ or $(2z'-1)/3$ stays positive and has the prescribed parity. Thus replay is physical and $0\le g_t\le x-1$.
2. Appending the actual next bit to any competing word preserves its source gain, since the new carry difference multiplies by $3^\epsilon$. Hence $g_t$ is nondecreasing and its total increase is at most $x-1$ for the entire lifetime of the source. Equivalently $x-g_t$ is the smallest ordinary source that meets the actual endpoint at this raw clock with the same accumulated odd count.
3. For a converger let $\tau(n)$ be its first visit to 1, $P_t(n)$ its odd count, and $\lambda(n)=2P_{\tau(n)}(n)-\tau(n)$. Two convergers ever meet at a common clock with the same odd count exactly when their $\lambda$'s agree. A meeting propagates to a common visit to 1, and the two-cycle contributes zero to $2P_t-t$ on each complete turn. Conversely equal $\lambda$ gives the same parity of the first-hit clocks; take a sufficiently late common visit to 1 and compare the scores there. Consequently the limiting gain for a converger is exactly $x-\min\{y:\tau(y)<\infty,\ \lambda(y)=\lambda(x)\}$.
4. Every edge satisfies $T(n)/n\le 2^{2\epsilon-1}$. Therefore $\lambda(n)\ge-\log_2 n$ for convergers. The class $\lambda=-k$ has least source $2^k$, so its gain is zero at every clock. More generally there are infinitely many strict records of first-hit time **among convergers** because $\tau(2^k)=k$. At every such record $x$, every clock $0\le t\le\tau(x)-2$ has zero gain. A smaller converging source which has already reached 1 can meet only at 1 or 2; one which has not yet reached 1 would have the same first-hit time. A nonconverger cannot meet a converger. These zero-gain prefixes have unbounded toll. Each descending orbit must cross all bit lengths from $b(x)$ down to 1, yielding at least $H_{b(x)}-1$ through its first hit, and omitting the two last edges loses at most two. This lower bound includes the ordinary cost of descending in height.

There is a finite *closing* clock for the attempted gain argument. Under strong induction, suppose all positive $m<x$ converge. Let $A\ge0$ be the maximum of their scores $2P_s(m)-s$ over all $s\ge0$, together with zero. It is computable from their paths through one complete turn after hitting 1. For any path from $x$ whose inputs and endpoint through $t$ are above two,
$$
  2^t \le x(10/3)^{P_t(x)}.
$$
This follows by multiplying the step bounds, since each odd input is at least 3. If $2P_t(x)-t\le A$, squaring gives $(6/5)^t\le x^2(10/3)^A <2^{2(b(x)+A)}$. But $(6/5)^4>2$, so
$$
           t < 8(b(x)+A).
$$
After this explicit clock no smaller source even has the same grade at an unabsorbed endpoint. Testing the finite initial window therefore decides whether this mechanism ever obtains a strict gain while the path stays above two. Absence of a gain in that window gives no bound on when the path hits two. In particular, waiting longer on a fixed minimal hypothetical nonconverger cannot produce such a same-grade gain. A comparison permitting different odd or raw clocks would require a different estimate.

## How long a single balanced history can cost

A binary word is balanced if any two of its factors of equal length differ in number of ones by at most one. This definition is hereditary under taking a contiguous segment. It does not refer to the height, direction of drift, or number of bands visited.

For $b=b(x)$, take $k=\lceil(b+1)/2\rceil$, $h=5k$, $D=h+1$.
Every prefix state of age at most $D$ is strictly below $2^h$. Indeed $2(Tn+1)\le3(n+1)$, $x+1\le2^{2k-1}$, and $3^5<2^8$, giving
$$
 (x+1)(3/2)^D \le 2^{2k-1} 2^{3k}(3/2) <2^{5k}.
$$
If two such states have the same next $h$ bits, their ordinary values coincide: identical bits force congruence modulo $2^h$ by the affine formula and odd leading coefficient.

A balanced finite word has at most $h+1$ factors of length $h$. At each length there is at most one factor with both right extensions. Indeed, two distinct such factors have a longest common suffix $v$, preceded by different bits in the factors. Their two available extensions supply both $0v0$ and $1v1$, contradicting balance. Increasing factor length thus raises the count by at most one, starting at one empty factor. If a balanced physical word has length at least $2D$, the $D+1$ windows at clocks $0,\dots,D$ fit and two initial values coincide. Write the corresponding clocks $i<j\le D$. The word includes two full turns from $i$ to $i+2(j-i)\le2D$. Every pair of cyclic factors of the period of equal length up to $j-i$ appears in these turns. Removing complete turns then proves balance at every length on the periodic tail.

A positive cycle with circularly balanced parities is the trivial one. To see this, shift to $Y=2x+1$, so $2Y'=3^{\epsilon}Y+1$. On the cycle the period product is strictly below one by this affine equation and positivity. Iterating backward around the cycle gives
$$
 Y_i=\tfrac12\sum_{k\ge0} 3^{P_{i-k:i}}/2^k ,
$$
where $P_{i-k:i}$ counts the $k$ preceding bits. The series converges by the period product. For two endpoints the ratios of all corresponding summands are at most 3; the $k=0$ terms agree. Hence $\max Y<3\min Y$, so $\max x\le3\min x$. Equality would put a multiple of three on a positive cycle, impossible since its only possible predecessor is its double, recursively. The [factor-three cycle theorem](../../astra-two-centre-20261124/rewriting.md#complete-exclusion-of-positive-cycles-within-a-factor-of-three) now leaves $1,2$. Thus an unabsorbed balanced prefix has length less than $2D$. The same conclusion covers a prefix ending at its first arrival at 1 if one extra edge is allowed in the bound.

## One inequality for all successive visits

For an arbitrary finite ordinary prefix ending at or before its first visit to 1, take its first shortest unbalanced initial block, restart just after it and repeat. Retain the last incomplete block. Each block becomes balanced after removing its final bit. For any position in a block with $r$ edges still to go, at least $r-1$ initial edges form a balanced path, with all their endpoints above 1 if $r\ge2$. The preceding deadline gives $r\le 2D(b_i)+1\le K b_i$ with $K=12$ for every positive bit length $b_i$ at such an input, since $b_i\ge2$ whenever there is a charged edge. The input bit length can rise by at most one per edge, so for the block-end bit length $E$,
$$
             E+r\le b_i+2r\le(2K+1)b_i .
$$
For a block of $L$ edges, its entire toll is therefore at most
$(2K+1)\sum_{r=1}^L 1/(E+r)\le(2K+1)\log((E+L)/E)$.
If the successive block boundary lengths are $B_0,\ldots,B_s$ and their edge counts $L_j$, telescoping yields
$$
 D(x,N)\le25\left(\log(B_0/B_s)+
       \sum_{j=0}^{s-1}\log\frac{B_{j+1}+L_j}{B_j}\right).             \tag{1}
$$
Every remaining logarithm is nonnegative since a bit length drops at most one per edge. It vanishes on a pure succession of bit-length drops, and is at most $\log(1+2L_j/B_j)$. Thus (1) allows unbounded changes of scale in either direction and arbitrary returns. On a single balanced prefix the toll is $O(\log(2b(x)))$, since $L\le12b(x)$ and $E\ge1$. The order is attained by $2^k\to1$. The unpaid sum in (1) can repeat at every new imbalance; no bound on it from $B_0$ has been proved.

## High-density prefixes can incur repeated imbalance at zero gain

Here the sources vary with the length. At length $N=3m$, the $2^m$ concatenations of the two blocks $110,101$ have different carries modulo $3^{2m}$. The two one-block carries are 5 and 7. At the latest differing block with $r$ later blocks, its difference has exact ternary valuation $2r$, whereas every earlier difference has valuation at least $2r+2$. For each residue choose a carry-maximizing length-$N$ word of weight $2m$. All its prefixes maximize in their own classes: a strictly better prefix can be followed by the unchanged suffix and would increase the final carry in the same residue. Realize the word by its unique ordinary parity representative in $[0,2^N)$; its positive weight excludes zero. This gives $2^m$ distinct positive sources with zero gain through clock $N$.

In fact there can be linearly many disjoint unbalanced factors on one of these zero-gain prefixes. Set $u=32768$, take $N$ a multiple of $3u$, and tile the word by $u$-bit blocks. The number of balanced $u$-blocks is at most $2^{u/4}$: choose at most 33 distinct 32-bit factors, encoded by a padded list of 33 words (at most $2^{1056}$ choices; repeat entries for padding), and describe the disjoint 32-bit chunks by six bits each. This costs at most $1056+6u/32<u/4$ bits. The number of length-$N$ words with at most $N/(24u)$ unbalanced tiles is consequently at most
$$
       2^{N/u}2^{N/24}2^{N/4}<2^{N/3}.
$$
Choose a maximizing word outside this set. More than $N/(24u)$ of its tiles are unbalanced, and its overall odd fraction is $2/3$. Its final endpoint is at least $(9/8)^m x>2$ for large $m$ by its affine equation. Every state after reaching 1 is at most two, so the whole prefix precedes absorption. On its canonical source $b(x)\le N$, and all bit lengths through $N$ are at most $2N$, so those tiles alone cost more than $1/48$. Arbitrarily many disjoint unbalanced windows therefore need not create even one gain. This does not contradict a budget charged to the original size: by choosing outside the at most $2^{N/4}$ canonical sources with fewer than $N/4$ bits as well, for all sufficiently large $N$ the same construction has $N/4\le b(x)\le N$.

## Evidence and open step

The proofs are proposed written results. The [Lean file](BalancedCost.lean) checks the physical parity congruence, the growth bound, the finite dictionary collision, the explicit five-step bound, the exact gain equation for two integral source histories and the scalar closing-clock inequality. Counting right-special factors, the cyclic series, cumulative logarithmic estimates, maximum selection and its physical replay are written arguments. The [finite control](check.py) checks the exact maximizing-carry arithmetic, actual ordinary collisions, the two-block residue construction, strict stopping-record plateaus, and rational block cost estimates on bounded inputs.

The unrestricted problem is to pay the full remaining sum in (1) from the original $x$, or to give a different ordinary argument which forces a first hit. The monotone gain is bounded on each individual input, but is grade-ineligible after the explicit clock on a still-unabsorbed least counterexample. Neither the count of changing finite witnesses nor the actual global gain gives the claimed universal cost budget.
