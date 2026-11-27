# How far a primitive integer cycle must move from a balanced word

**Written proof.** Every primitive positive integer cycle of the shortcut map with large least binary period $A$ needs $\gg A^{2/3}$ adjacent circular swaps to reach any mechanical word of the same weight. If the swaps have pairwise disjoint supports, it needs $\gg A/\log A$ swaps. Their locations, directions and the span between them are unrestricted. An exact finite inequality below retains the full reduced denominator for positive rational cycles. This is a consequence of PR188's intrinsic shift bound and a word transport estimate. A separate signed product identity gives arithmetic restrictions at the actual disagreeing states.

## Exact finite estimate

Write $T(x)=x/2$ on even inputs and $T(x)=(3x+1)/2$ on odd inputs, with parity defined on rationals of odd denominator. Let $w$ be the word of a positive rational cycle of least bit period $A>1$, with $0<p<A$ odd steps. Composing the maps yields $D x_0=C_w$, where $D=2^A-3^p>0$ and $C_w$ is the integer carry. Put
$$
d=D/\gcd(D,C_w),\qquad \eta=D/2^A.
$$
All phases have the same reduced denominator $d$, since $2,3$ are units modulo $d$ and the branches give integer numerators after clearing $d$.

Let $u_i=\lfloor(i+1)p/A+\theta\rfloor-\lfloor ip/A+\theta\rfloor$ for any real $\theta$. Choose any sequence of $K$ adjacent circular exchanges of $01$ and $10$ taking $u$ to $w$. Let $R$ be the range of the cumulative differences of the bits of $w$ and $u$ around the circle, including the zero initial difference. Put $\delta=2$ if $\gcd(A,p)=1$ and $\delta=0$ otherwise. Then
$$
 \boxed{\quad\log_2 d >
 {A\over 4K+\delta}-1-\log_2{p\over 2\eta}
                 -(1+R)\log_2 3,\qquad R^2\le 2K.\quad}                 \tag{1}
$$
The denominator $4K+\delta$ is positive on these hypotheses. When $\delta=0$, $u$ has a proper period so cannot equal $w$.

For the proof, let $f_i$ be the signed net number of ones transferred across the oriented edge $(i,i+1)$ by the swaps. Conservation gives $w_i-u_i=f_{i-1}-f_i$, so $R=\max f-\min f$, $|f_i-f_{i-1}|\le1$ and $\sum|f_i|\le K$. The cyclic walk through the values of $f$ crosses each level from $j$ to $j+1$ and back, for $\min f\le j<\max f$. Charge each crossing $(|j|+|j+1|)/2$. The sum of these charges is at most $\sum|f_i|$, since including every cyclic edge with half of each endpoint's absolute value gives precisely this sum. Thus
$$
 K\ge \sum_{j=\min f}^{\max f-1} (|j|+|j+1|)
   =\sum_{j=\min f}^{\max f-1}|2j+1|\ge \lceil R^2/2\rceil .
$$
The last minimum is attained by the $R$ consecutive odd integers centered as close as possible to zero. The odd count in any cyclic interval changes from $u$ to $w$ by at most $R$. The mechanical count differs from the interval length times $p/A$ by less than one. Consequently the maximum positive cyclic discrepancy $B$ of $w$ is at most $1+R$.

If $p$ is invertible modulo $A$, rotate by $h=p^{-1}\bmod A$. The ones of $u$ are a block of $p$ consecutive residues in the coordinates $ip\bmod A$. Translating the block by one changes exactly two bits. If $g=\gcd(A,p)>1$, choose the proper period $h=A/g$ of $u$. Either way $0<h<A$. Each swap changes two positions, so $t=\#\{i:w_i\ne w_{i+h}\}\le4K+\delta$ by the triangle inequality, and $t>0$ by primitivity.

For clarity, the PR188 intrinsic estimate follows directly. For every cyclic interval of length $s$ with $q$ ones, the suffix multiplier satisfies $3^q/2^s\le3^B$, since $3^p<2^A$. Summing the $p$ insertions of $1/2$ times their suffix multipliers gives $\eta x_i\le(p/2)3^B$ at every phase. A matching run between two consecutive disagreements has length $L\ge A/t-1$ for some run. Subtracting the common affine steps gives $2^L\mid d(x_i-x_{i+h})$ at its start, since their common multiplier numerator is odd. The difference is nonzero by deterministic primitivity. Positivity makes its absolute value strictly smaller than $d\max_j x_j$. Hence $\log_2 d>A/t-1-\log_2(p/(2\eta))-B\log_2 3$. Substitution proves (1).

## Consequences for actual cycles

The two-logarithm estimate $|A\log2-p\log3|\ge(\log3/1200) A^{-13.3}$ and $1-e^{-z}\ge\min(1,z)/2$ for $z>0$ give $\log_2(p/(2\eta))=O(\log(A+1))$ uniformly. This is the only transcendence input. [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

* For $d=1$, (1) forces $K\gg A^{2/3}$ uniformly for all sufficiently large $A$. Indeed $A\ll(K+1)(\sqrt K+\log A)$. When $K\le A^{2/3}$ the second factor is $O(A^{1/3})$, giving the bound, and larger $K$ already suffices.
* When the adjacent swaps are pairwise disjoint, $f_i\in\{-1,0,1\}$, so $R\le2$. In fact this conclusion holds whenever each edge transports net magnitude at most one. Then $d=1$ requires $K\gg A/\log A$. For $K>0$, $K=o(A/\log A)$ yields $\log d\gg A/K$ along such a sequence. These conclusions cover multi-site perturbations spread over the entire word.
* If only the Hamming distance $H$ between $u$ and $w$ is given, then $t\le2H+\delta$ and $B\le1+H/2$, since each sign of the discrepancy occurs at $H/2$ sites. The same proof gives $H\gg\sqrt A$ for $d=1$. The comparator here is a same-weight circular word. Related prefix separation from critical Sturmian factors, with explicit dependence on the initial integer, appears in [Weaver, §7](https://rstation.ai/problems/collatz/papers/84).

## A signed product on each nonidentity rotation

For *any* $0<h<A$ put $n_i=d x_i\in\mathbb Z_{>0}$. At every mixed pair $(i,i+h)$ let $o,e$ denote its odd and even numerators in that order. Use one factor per mixed index, including repetitions. The same primitive cycle obeys
$$
 2^A\prod_{\rm mixed}(o-e)
   =3^{p-t/2}\prod_{\rm mixed}(3o+d-e).                                  \tag{2}
$$
Indeed $2(n_{i+1+h}-n_{i+1})/(n_{i+h}-n_i)$ is $1$ at an even-even pair, $3$ at an odd-odd pair, and $(3o+d-e)/(o-e)$ at a mixed pair. Pair differences are nonzero at every phase. Multiplication around one lap cancels their signed ratios. There are $p-t/2$ odd-odd pairs because the two directions of mismatch have equal cardinality.

As $o-e$ is odd, the $t$ integers $3o+d-e$ have total $2$-adic valuation exactly $A$. The $3$-adic valuation of $\prod|o-e|$ exceeds that of $\prod|3o+d-e|$ by $p-t/2$. In particular one mixed pair has $v_2(3o+d-e)\ge\lceil A/t\rceil$, and a possibly different pair has $v_3(o-e)\ge\lceil(p-t/2)/t\rceil$. Every prime above three has identical aggregate valuation on the two sides' mixed products. The dyadic budget can also be read from the word. If exactly $L$ agreements follow a mixed pair before the next mismatch, its factor $3o+d-e$ has valuation $1+L$. Indeed it is twice the next difference up to sign, and every matching step removes one power of two until the next mixed difference is odd. Thus the dyadic condition recovers the run lengths. The signed identity additionally compares all the odd prime valuations on actual endpoint differences and retains the full denominator at every offset. The Lean module proves the signed identity for two closed, disjoint pointwise walks with the same carry, including all four local parity formulas. Its application to rotations, the valuations and the transport estimates are written proofs.

## Boundaries and antecedents

PR188, head f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d, research/astra-global-step-20261124/SHIFT_DISTANCE.md §2 supplies the intrinsic discrepancy/shift inequality used in (1). PR196, head 27d03cfe902660e06604eb55bb28ca3d2754ff48, research/astra-orbit-cycle-20261124/cycles/ROTATIONAL_EXCLUSION.md supplies earlier rotational restrictions. Coprime Christoffel full-denominator coprimality and Farey single-transposition exclusions already appear in [the rStation manuscript, Theorems 3–5](https://rstation.ai/problems/collatz/papers/4). The transport bound here measures physical binary adjacent exchanges, allows both directions and needs no short containing interval. It does not sharpen the exact balanced denominator or the one-transposition constants.

Primitive contracting words can have large transport cost and many mismatches at every offset. PR188 §4 constructs near-critical rational examples with every $t(h)\gg A$. Equations (1)–(2) leave ordinary realization open when the mismatch products accommodate both prime budgets. Near-minimum independent center denominators from the preceding round do not supply the missing upper bound. For an integral cycle a reduced center $a/b$ has $\gcd(a-mb,b)=1$ for every integer $m$. Large denominator primes therefore persist in the pole of the difference at every integer endpoint, and there is no upper bound on them from the endpoint size alone.
