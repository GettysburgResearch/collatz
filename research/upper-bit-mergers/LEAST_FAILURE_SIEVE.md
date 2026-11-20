# A sparse sufficient set for the directed adjacent-pair test

**Proposed theorem.** Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Let $C$ be the positive integers reaching 1. Write $X=128k+1$, $Y=64k+1$, where $k>0$ and $4\nmid k$. Put $n=27k+1=T^6(Y)$, and let $b_i$ count the odd inputs in the first $i$ steps from $n$. Retain $k$ exactly when
$$
       2^{16}3^{b_i}\ge 2^i
       \quad(1\le i\le\lfloor\log_2 k\rfloor).                 \tag{1}
$$

Full Collatz convergence is equivalent to $X\in C\Rightarrow Y\in C$ just for the retained indices. For every discarded index there is a computable list of $O(\log(2k))$ smaller implications that together suffice to prove $Y\in C$. Their upper starts are all less than $5X/8$. In every interval of $N\ge2$ indices the number retained is
$$
 O\!\left(\frac{N^\rho}{(\log(2N))^{3/2}}\right),\qquad
 p=\log_3 2,\qquad \rho=-p\log_2p-(1-p)\log_2(1-p)=0.949955527\ldots .
$$
On $[2^h,2^{h+1})$ this order is attained, even by retained indices on the already solved class $k\equiv6\pmod{16}$. The [exact enumerator](check_least_failure_sieve.py) generates the retained indices from the surviving words. The count concerns the explicit test (1). Convergence transfer on its remaining inputs is open.

## Why the restriction suffices

If Collatz fails, the [directed adjacent-pair theorem](DEEP_REVERSE_BASIN.md) supplies a least failing $X$. The height bound of the deep-reverse follow-up gives $m\in C$ for every positive $m<X/176106$. In its 71 directed descent certificates, every auxiliary convergence implication needed for a ternary unit $v$ has antecedent below $88053v$. For $v<X/88053$ all such implications therefore hold by minimality. Strong induction along the descent proves convergence of those units. Removing powers of two and taking one odd step from an odd multiple of three extends the bound to $m<X/176106$. [Height proof and exact certificate](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md)

Every iterate of $n$ is outside $C$ for this least failure. Composing the first $i$ branches gives $T^i(n)=3^{b_i}2^{-i}(n+E)$ with $0\le E\le2^i$ by summing $2^d/3^j$ over the odd positions $d<i$ and their ordinals $j\ge1$. Throughout the test $n+E\le29k$. A violation of (1) gives $176106 T^i(n)<176106\cdot29k/65536<128k+1$, a contradiction. Thus a least failure passes the test. Full convergence gives the converse immediately.

For an explicit reduction at *any* discarded index, set $m=T^i(n)$ at the first violation. Remove factors of two from $m$ and, if necessary, take one odd step to reach a positive ternary unit below $2m$. Apply the 71 descent certificates (halving even units) until 1. Each stage takes at most $198$ edges and has an endpoint at most $24/25$ of its starting value. Replace each auxiliary tripling by its two directed binary comparisons as in the height proof and record their upper antecedents. The list has length at most $396\lceil\log(2m)/\log(25/24)\rceil$. All its antecedents are less than $176106m<78k<5X/8$. If the listed implications hold, reading the path backwards from 1 proves $m\in C$ and hence $Y\in C$. Iterating gives a finite reduction with $O(\log(2k))$ levels. Consequently, verifying the retained comparisons up to any cutoff certifies every eligible comparison through that cutoff.

## Counting all surviving parity prefixes

A length-$h$ parity word from $27k+1$ identifies exactly one class of $k$ modulo $2^h$. At each binary extension the two lifts have endpoints differing by an odd power of three, so their next parities are opposite. For a uniform binary word let $S_i=b_i-pi$; (1) demands $S_i\ge-B$, $B=16p$.

For completeness, give the bits success probability $p$ temporarily. For a centered walk with these bounded increments, the probability of staying above $-u$ for $m$ steps is $O((1+u)/\sqrt m)$ for $u\ge0$. The same estimate holds with the sign reversed. To see it, take $u\le\sqrt m$ and stop on leaving $[-u,\sqrt m]$. The upper exit probability is at most $(u+1)/(\sqrt m+u+1)$ by the zero-mean martingale and overshoot at most one. The square martingale then bounds the mean exit time by $O((u+1)\sqrt m)$. Optional stopping here is justified by geometric tails for exit from a bounded interval, obtained by consecutive equal bits. Markov's inequality gives the claim.

For a specified terminal count $j$ write $s=j-ph\ge-B$. Split the word into three successive blocks of lengths within one of $h/3$. The first must stay above $-B$. The centered sums of the last block read backwards must stay below $s+B$. Conditional on these two independent blocks, the middle block must attain one prescribed count, of probability $O(h^{-1/2})$ by the binomial maximum. Hence the probability of surviving with this count is $O_B((1+s+B)h^{-3/2})$. Each word at that count has probability $2^{-h\rho}(p/(1-p))^s$. Dividing by its probability and summing the convergent geometric tail over $s\ge-B$ proves the stated prefix count. For an interval of $N$ indices, take $h=\lfloor\log_2 N\rfloor$ on the portion $k\ge2^h$ and cover it by at most three binary blocks. Sum dyadically for smaller $k$.

For the matching lower bound prescribe $k\equiv6\pmod{16}$, where the first four parities from $27k+1$ are odd, odd, even, even. All four prefixes meet (1). For the remaining $m=h-4$ bits prescribe $\lceil pm\rceil$ ones. In each cyclic orbit of such words a rotation beginning at a minimum centered partial sum has all partial sums nonnegative, since the total sum is nonnegative. This gives at least $\binom{m}{\lceil pm\rceil}/m\gg 2^{h\rho}h^{-3/2}$ accepted suffixes by Stirling's formula. Each gives an index in the dyadic block. The two arms on this class merge at the fifth odd step. [Five-step construction](DEEP_REVERSE_BASIN.md#five-odd-steps-can-reach-any-prescribed-odd-target-coprime-to-three)

## A rank-five family that always survives the sieve

Write $e=119+162j$, $j\ge0$, $P=2^e$, $M=P-1$ and $k=(8P-22)/243$. The follow-up proves that $X=(1024P-2573)/243$ first reaches 1 using five odd inputs and $Y$ reaches $M$. Here $n=(8P-13)/9$ reaches $M$ in three steps with parities odd, odd, even. The next $e$ inputs are odd. Since $k<P$, every such index passes (1), including at the unbounded exponents. [Rank-five certificate K3](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md)

**Every arithmetic progression inside this exponent family has a subprogression excluded from being a least failure.** Write the given progression as $e=e_0+Dt$, $162\mid D$, $D>0$. Put $d=v_3(2^D-1)$. At precision $3^{d+L}$, $M$ runs through all lifts of its fixed residue modulo $3^d$ as $t$ runs modulo $3^L$. Indeed each cubing of $2^D$ increases the valuation of its difference from one by exactly one, so its order modulo $3^{d+L}$ is $3^L$.

Perform $d$ ordinary odd inverse moves $I_b(v)=(2^b v-1)/3$ starting at $M$. The first $d-1$ moves can use fixed $b\le4$ and keep the output a ternary unit. From a unit choose $b=1$ or $2$ making $2^bv\equiv1\pmod3$; if the product is one modulo nine, increase $b$ by two. There are enough fixed digits for these choices, and $M\equiv1\pmod3$. On the last move only integrality is required. The resulting $v$ has the form $(2^A M-F)/3^d$ with $A\le4d$ and $F>0$. Thus $v$ runs through every residue modulo $3^L$. Choose the single subprogression giving $v\equiv-1\pmod{3^L}$ and take $L$ more inverse moves with $b=1$. All are positive odd integers. The resulting ordinary ancestor $w$ satisfies
$$
 w=(2/3)^L(v+1)-1<(2/3)^L(16/3)^d M.
$$
With $L=5d+30$, this gives $176106w<M<X$, since $(2/3)^5(16/3)<1$ and $176106(2/3)^{30}<1$. If $X$ were the least failure, $w$ would reach 1, so $M$ and $Y$ would reach 1 as well. This excludes the subprogression under exactly the least-failure hypothesis.

## How deep an ordinary path to a smaller representative can have to go

For every $H\ge5$ there are infinitely many of the same exponents such that, **simultaneously at every clock $0\le i\le e$ of the entire Mersenne ascent**, any positive $z$ reaching $T^i(M)$ with at most $i+H$ odd inputs satisfies $z\ge M/100$. Any number of even inputs is allowed. In particular no such $z$ is below $X/176106$. This extends the scope from predecessors of $M$ itself to all those ascent vertices, for the purpose of finding a representative below the least-failure height cutoff. [Earlier predecessor obstruction with an eligibility constraint](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/MERSENNE_WITNESS_DEPTH.md)

Choose $M\equiv184\pmod{3^H}$. This is possible on an entire exponent progression since $2^{119}\equiv185\pmod{243}$ and $v_3(2^{162}-1)=5$. Fix $i$ and reverse the proposed path starting from $T^i(M)=3^i2^{e-i}-1$. The reverse maps are $u\mapsto2u$ and $u\mapsto(2u-1)/3$. Reverse up to $i$ odd inputs, or the whole path if it has fewer. If this segment uses $r\le i$ odd and $b$ even inverses, its exact output is
$$
             2^b(3/2)^{i-r}P-m,\qquad 1\le m\le2^b .
$$
Indeed the signed output on input $-1$ is $-m$. The odd inverse preserves $(-\infty,-1]$ and does not increase magnitude there, whereas doubling multiplies it by two. The actual and signed inputs initially differ by a multiple of $3^i$, so every signed division is integral through these $r$ odd inverses. Transporting the difference gives the formula. If the entire path has at most $i$ odd inputs the formula already gives $z\ge M$.

Otherwise take $r=i$ (the empty segment if $i=0$). Apply the remaining inverse maps, containing at most $H$ odd inverses, to $2^b(u+1)-m$ and call the resulting affine function $G(u)$. Its value at $u=M$ is $z$. At $u=184$ the intermediate divisions remain integral because the starting values differ by a multiple of $3^H$. The initial value at this center is positive and every integral inverse step preserves positivity. Thus $G(184)\ge1$. On the other hand $G(-1)\le-1$ because that path begins at $-m$. The slope of $G$ is consequently at least $2/185$. Hence $z\ge1+2(M-184)/185>M/100$ for $e\ge119$. Finally $X/176106<M/100$ follows directly from the displayed $X$. Longer excursions beyond the ascent or unbounded excess odd counts remain available.
