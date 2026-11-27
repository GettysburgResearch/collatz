# Which fixed targets admit large odd joint predecessors at bounded grade?

**PROPOSED.** Use the shortcut map on ordinary positive integers, with one native step per halving or odd operation $T(x)=(3x+1)/2$. The grade counts odd departures. Say that $a,b$ are forward-comparable when one visits the other, allowing zero steps. Two incomparable targets can still have a common future.

## Fixed-target classification

For fixed positive integers $a,b$, the following are equivalent.

1. Both are units modulo three and they are forward-comparable.
2. There is a constant $G$ for which arbitrarily large **odd** positive integers $s$ admit native clocks $i,j$ with $T^i s=a$, $T^j(3s)=b$, and total grade at most $G$. The clocks may differ.

For necessity, the only one-step predecessor of a multiple of three is its even double. Every odd source reaching such a target must therefore be the target itself. This applies separately to $s$ and $3s$. For incomparable targets let $G$ denote the total grade of one supplied pair of paths. The following explicit bound holds.

$$
                     s\le \max(a,b)\,2^{(2G+3)G}.                 \tag{1}
$$

For sufficiency, choose the upstream target $u$ and fix its actual finite path to the downstream target, with grade $h$. Both $s=23+32t$ and $3s=69+96t$ reach $20+27t$ after five native steps. Their grades are three and two, respectively. The first paths at $t=0$ are $23,35,53,80,40,20$ and $69,104,52,26,13,20$. Adding $32t$ to the first input and $96t$ to the second adds $27t$ to both endpoints. Choose arbitrarily large $e$ with $2^eu\equiv61\pmod{81}$, possible since two has order 54 modulo 81. Set $t=(2^eu-61)/81$. It is eventually positive and odd, and

$$
                      3(20+27t)+1=2^e u.
$$

Thus both paths reach $u$ in precisely $e$ further native steps with one further odd departure apiece. Append the fixed link on the appropriate arm. The total grade is $7+h$ at arbitrarily large odd sources. The two constructed paths need not make their first visit at the displayed times. Replacing them by first visits only reduces the grades.

## Deterministic clock bound before a meeting

More generally take $A_t=T^t s$ and $B_t=T^t(3^r s)$ for any odd positive $s$ and $r\ge0$. Write $g_t,h_t$ for the true grades on the two paths and $G=g_k+h_k$. If $A_t\ne B_t$ for every $0\le t\le k$, then

$$
                             k\le [2(G+r)+1]G.                  \tag{2}
$$

There is no floor condition, probabilistic input or comparable-height assumption. The case $r=0$ has no such prefix. The proof of (2), including the physical Collatz steps, is checked in [PairedClock.lean](PairedClock.lean) as **unmatched_ternary_power**.

Define

$$
                    D_t=\left|3^{g_t}B_t-3^{h_t+r}A_t\right|.
$$

For either source the physical affine numerator gives $2^t A_t=3^{g_t}s+C_t$, with $0\le C_t\le 2^t3^{g_t}$. Use the same formula with intercept $C'_t$ for the second arm. At an odd step the intercept changes to $3C_t+2^t$. At an even step it stays fixed. After cancelling the term in $s$, the two remaining nonnegative numerators in $2^t D_t$ are each at most $2^t 3^{g_t+h_t+r}$. Consequently $D_t\le3^{g_t+h_t+r}$.

Both arms start odd. After their first odd departure every subsequent state on each is a ternary unit. If $D_t=0$ for $t\ge1$, the exact powers of three in the two terms must agree, so $A_t=B_t$. Thus $D_t$ is a positive integer throughout the unmatched prefix after time zero. Every simultaneous-even date halves it exactly. Set $V_t=\max(1,D_t)$ and $M=2(G+r)$. On a simultaneous-even step $2V_{t+1}=V_t$. The initial date is odd. At an active step, if $e\in\{1,2\}$ odd departures occur, then $V_{t+1}\le2^M$ and $V_t\ge1$, hence $2V_{t+1}\le2^{(M+1)e}V_t$. Multiplying from 0 to $k-1$, $2^kV_k\le 2^{(M+1)G}V_0$. Here $D_0=0$, so $V_0=1$, yielding (2).

For (1) take $k=\min(i,j)$ and $r=1$. A common state at any date through $k$ puts both marked targets on its forward orbit. Incomparability therefore supplies the full hypothesis of (2). Every native step retains at least half of its positive input. At the earlier marked visit either $s\le2^k a$ or $3s\le2^k b$. This proves (1).

## What the classification separates

The bound applies to genuine fixed incomparable targets even in the component of 1. For example $113$ and $509=T(339)$ are incomparable, although both reach 1. The odd integer $455907$ and its triple visit them at clocks 31 and 116. Formula (1) makes the set of such odd inputs finite at each prescribed grade budget. Dyadic copies of any witness give arbitrarily large even inputs at the same grade, which is why the restriction to odd inputs is essential. A hypothetical odd $q$ avoiding 1 with $3q$ reaching 1 has incomparable $q,T(3q)$. Thus a method that supplies a fixed-grade pair of genuinely new odd preimages all the way up that **same** target pair cannot apply.

Grade can grow with height. Neither (1) nor (2) gives an upper bound on the number of unrestricted visits to a fixed pair, or a proof that its components agree. The sharp growth rate of the minimum grade over long unmatched odd-source pairs is open here.

**Prior work.** PR201 at dac732467c6ed5307d1b78eaa8534653aeeb7a4c established an unrestricted joint-count upper bound and the $113,509$ ordinary control. [PINNED_TARGETS.md](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/coupling/PINNED_TARGETS.md)

PR146 at f431078244e868dc699fad011044f0d5e7f76437 studied the two-arm process and finite deadline probabilities. PR212 at 505d3fe782922904e86477990cc5d41e9110edda gives stronger placement for a supplied common target. None of these estimates is required for (1), (2), or the fixed-pair equivalence above. [THREE_RAY_CLOCKS.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_CLOCKS.md) · [AFFINE_WINDOWS.md](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/merger/AFFINE_WINDOWS.md)
