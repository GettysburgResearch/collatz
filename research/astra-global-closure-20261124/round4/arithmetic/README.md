# Large full denominators for damaged quadratic-residue schedules

**PROPOSED written theorem.** A quadratic-residue schedule chooses between two distinct physical Collatz blocks of the same length and weight. At any fixed number of arbitrarily placed intervals, replace every bit by any word of the same total length and weight as that interval. If the altered intervals have sublinear total length, the complete reduced cycle denominator has $(1-o(1))$ bits per shortcut step. An explicit positive fraction of altered bits still forces exponential denominator growth. The theorem includes near-critical rational cycles of arbitrarily high minimum whose every nonidentity binary rotation differs on a positive fraction of the period. It leaves unrestricted ordinary cycles and escaping trajectories open.

## Statement on the actual word

Use the shortcut map $x\mapsto x/2$ on even inputs and $x\mapsto(3x+1)/2$ on odd inputs. For an odd-denominator rational, parity is the parity of its reduced numerator. Take two distinct binary words $U_0,U_1$ of length $L$ and weight $p\ge1$, with $Q=2^L>P=3^p$. Let $C_i$ be their complete integer carries, so the maps are $(Px+C_i)/Q$. Put $\Delta=C_1-C_0\ne0$. Indeed the parity of a carry is the initial bit. Removing the initial bit $b$ replaces the carry by $(C-b3^{p-b})/2$ and the weight by $p-b$, so equal carries at equal clocks would recover identical words.

Let $N\ge7$ be prime, $N\equiv3\pmod4$. At slot $i\in\mathbb Z/N$ use $U_1$ if $i$ is a nonzero quadratic residue, and $U_0$ otherwise. Choose $r\ge1$ circular intervals of positive lengths $h_j\le H$ in slots with disjoint interiors. At interval $j$, replace its $h_jL$ bits by **any** word of that length and weight $h_jp$. Its individual length-$L$ cells can have different weights and carries. Intervals may wrap around zero or touch one another. Using at most $r$ intervals gives the same bounds by increasing the parameter $r$. The unaltered case has a sharper bound below.

The resulting physical word has length $A=NL$ and weight $Np$. Put $D=Q^N-P^N=(Q-P)S$, where $S=\sum_{i=0}^{N-1}Q^iP^{N-1-i}$. At any cut the full carry $C$ gives the positive rational cycle point $C/D$ with reduced denominator $d=D/\gcd(D,C)$. Indeed the first parity agrees, and applying its exact branch gives the cyclically rotated fixed point by affine composition. Since $\gcd(D,6)=1$, each branch preserves the common reduced denominator. No least-period condition is needed.

For every integer $K\ge1$ with $K^r<N$, writing $c=(N+1)/4$, one has the finite inequality

$$
\boxed{\quad
 d\ \ge\ \frac{Q^{N-1-4N/K}}
 {\big((r^2+r+c)3^{2HL}\big)^{K^r}}.\quad}                         \tag{1}
$$

In particular the following hold uniformly in the two templates and in all replacement words.

* For fixed $r$, $N\to\infty$ and $H=o(N)$ imply $\log_2 d/(NL)\to1$. More generally this holds for $r=o(\log(N/J))$ and $J=H+\log_2(N+r+1)/L$ when $N/J\to\infty$. Take $K=\lfloor (N/J)^{1/(2r)}\rfloor$. Then $K\to\infty$, $K^rJ/N\to0$, and $d\le D<Q^N$. In particular $o(\log N)$ widely separated individual erroneous slots are allowed.
* At each fixed $r$, if $\limsup H/N\le16^{-(r+1)}$, taking $K=16$ gives $\liminf\log_2d/(NL)\ge 3/4-(\log_2 3)/8>1/2$. One interval may therefore cover a fixed positive fraction of the whole word. For $r=1$ optimizing $K$ gives a loss from $(N-1)L$ of $O(\sqrt{NL(HL+\log(N+1))}+HL+\log(N+1))$ bits.
* With no alteration one has the exact identity $\gcd(S,C)=\gcd(S,\Delta)$, hence $S/\gcd(S,\Delta)\mid d$. This takes the full common gcd, with prime-power multiplicities. The factor $Q-P$ can contribute further denominator.

## The physical carry at a common cut

The complete carry of an arbitrary $b$-bit word is nonnegative and strictly below $3^b$. In fact appending an even bit leaves the carry alone, and appending an odd bit replaces it by $3C+2^b$. Induction yields the maximum $3^b-2^b$. Choose the cut $b$ at a slot boundary outside the interiors of the designated intervals. Let $g=\gcd(S,C)$ at this cut. The case $g=1$ already gives $S\mid d$. In $\mathbb Z/g$ both $P,Q$ are units. Set $t=Q/P$ there. We have $t^N=1$ and $\sum_{i<N}t^i=0$.

Write $R$ for the nonzero quadratic residues modulo $N$, and $F(X)=\sum_{i\in R}X^i$. Without alterations the carry divided by $P^{N-1}$ at the chosen cut is $C_0\sum t^i+\Delta t^{-b}F(t)$. If interval $j$ starts at slot $a_j$ in the original coordinates, let $J_j$ be its replacement carry minus its reference carry. At the chosen cut its first slot has representative $a'_j=(a_j-b)\bmod N$, with $a'_j+h_j\le N$. Its contribution to the change in the full carry is exactly $Q^{a'_j}P^{N-a'_j-h_j}J_j$. Changes add because the two versions of each complete interval have identical slope. Multiplication by $t^b P^{H-1}$ after the common division gives

$$
 B F(t)+\sum_{j=1}^r E_j t^{a_j}=0 \pmod g,\qquad
 B=P^{H-1}\Delta\ne0,\qquad E_j=P^{H-h_j}J_j.                         \tag{2}
$$

All $|E_j|$ and $|B|$ are at most $M=3^{HL}$. Changing weights within the interval is fully absorbed in its single $J_j$. For every prime valuation $v$, $v(d)=\max(0,v(D)-v(C))\ge\max(0,v(S)-v(C))$, so $S/g\mid d$. This is the step from the auxiliary geometric sum to the **complete reduced** denominator.

## The quadratic period and its numerical modulus

Modulo $X^N-1$, let $F^-(X)=F(X^{-1})$. Since $-1$ is a quadratic nonresidue,

$$ F+F^-=\sum_{i<N}X^i-1,\qquad FF^-=c+\frac{N-3}{4}\sum_{i<N}X^i. $$

For the second identity the coefficient at zero is $(N-1)/2$ and at every other difference it is $(N-3)/4$. To check the latter directly, let $\chi$ be the quadratic character with $\chi(0)=0$. For $h\ne0$, the identity $\sum_x\chi(x)\chi(x+h)=-1$ counts $y^2=x(x+h)$: the two factors $2x+h-2y$ and $2x+h+2y$ have product $h^2$, giving $N-1$ solutions. Expanding the two quadratic-residue indicators $(1+\chi(x)-1_{x=0})/2$ gives $(N-3)/4$ since $\chi(h)+\chi(-h)=0$.

At $t$ the two identities yield $F(t)^2+F(t)+c=0$, even when the ring has zero divisors. In fact $F(t)$ is already a unit modulo $S$. If a prime $\ell\mid S$, the order of $Q/P\bmod\ell$ divides $N$. Order one gives $\ell\mid N$ by the geometric sum. Otherwise the order is $N$ and $N\mid\ell-1$. All prime divisors of $S$ are at least $N$, and $0<c<N$. Thus $F(t)(F(t)+1)=-c$ is a unit in $\mathbb Z/S$. The unaltered carry identity now gives the claimed exact gcd with $\Delta$, including primes shared with $Q-P$. This period identity is classical. The use of autocorrelation to bound a numerical denominator for *unaltered ordinary base-two sequences* appears in Hu, §1, and Xiong–Qu–Li. Here the numerical base is $Q/P$, the numerator is a literal Collatz carry, and arbitrary interval substitutions enter (2). [Hu](https://arxiv.org/abs/1406.3889) · [Xiong–Qu–Li](https://arxiv.org/abs/1309.1625)

## Eliminating widely dispersed errors

Put $K^r+1$ points $(ma_1/N,\ldots,ma_r/N)\bmod1$, $0\le m\le K^r$, into $K^r$ equal half-open boxes in the unit cube. Two points lie in one box. Their difference gives $1\le u\le K^r<N$ and integers $s_j\equiv ua_j\pmod N$ with $|s_j|<N/K$. Since $N$ is prime, take $v$ with $uv\equiv1\pmod N$. In $\mathbb Z/g$ the unit $z=t^v$ satisfies $z^u=t$ and $z^{s_j}=t^{a_j}$ for every $j$, including negative $s_j$.

Let $E(X)=\sum_j E_j X^{s_j}$ and $T=\max_j|s_j|$. The two ordinary integer polynomials

$$
 A_u(X)=P X^u-Q,\qquad G(X)=X^{2T}\big(E(X)^2-BE(X)+cB^2\big)                \tag{3}
$$

share the root $z$ in $\mathbb Z/g$ by (2) and the quadratic equation. No inverse of $B$ is used modulo $g$. The polynomial resultant has an integer-polynomial Bézout identity, so $g\mid\operatorname{Res}(A_u,G)$. This conclusion holds for the entire numerical $g$.

**Why the resultant is nonzero.** A common complex root $x$ would be nonzero and $\mathbb Q(x)$ would contain $2E(x)/B-1$, whose square is $1-4c=-N$. In fact *every* root of $P X^u-Q$ has a field omitting $\sqrt{-N}$. Here is a local proof which also handles a reducible binomial. Let $R=\mathbb Z_{(N)}$ and $f$ be the monic minimal polynomial of $x$. The monic polynomial $X^u-Q/P$ belongs to $R[X]$ and its monic factors belong to $R[X]$ by Gauss's lemma. Its reduction modulo $N$ is squarefree by its derivative, since $N\nmid uPQ$. Thus $\bar f$ is squarefree. The domain $O=R[X]/(f)$ is a finite free $R$-module with the power basis, and $O/NO=\mathbb F_N[X]/(\bar f)$ is reduced. Consequently $N\mid y^2$ implies $N\mid y$ in $O$.

If a square root of $-N$ lay in $\mathbb Q(x)$, clear its rational power-basis coefficients to write it $a/b$ with $a\in O$ and $0\ne b\in R$, scaling until $a,b$ are not both in $NO$. This is possible by the minimal $N$-adic valuation of their finitely many coefficients. Then $a^2=-Nb^2$ forces $a=Na'$ by reducedness. Cancellation gives $b^2=-N(a')^2$ and reducedness also gives $b\in NO$, a contradiction. In this characteristic-zero step $B\ne0$ suffices, including $N\mid B$. It follows that (3) has a nonzero integer resultant.

Finally $\deg G\le4T$, and the sum of its absolute coefficients is at most $(r^2+r+c)M^2$. Every complex root of $A_u$ has modulus $(Q/P)^{1/u}>1$. The resultant product formula therefore gives

$$
 0<|\operatorname{Res}(A_u,G)|
 \le Q^{\deg G}\,\|G\|_1^u
 \le Q^{4N/K}\big((r^2+r+c)3^{2HL}\big)^{K^r}.                         \tag{4}
$$

Indeed the leading factor $P^{\deg G}$ cancels the denominator in the product of the root-modulus bounds. As $S\ge Q^{N-1}$ and $S/g\mid d$, (4) proves (1).

## Near-critical words separated at every physical shift

The following example applies (1) on a positive-entropy family at any sufficiently large upper convergent $L/p$ of $\log_2 3$. Let $\mathcal U$ be the eight-bit-cell family in PR188 §4. It has $2^{\lfloor L/8\rfloor}$ marked words of weight $p$, each with absolute cyclic interval count discrepancy at most 18 from slope $p/L$. The counting proof in that source gives a member $U_0$ with $d_H(U_0,\sigma^v U_0)\ge\lfloor L/8\rfloor/20$ for every $0<v<L$. Here $d_H$ counts differing bits and $\sigma$ rotates a word. Take $U_1=\sigma U_0$, which preserves the same discrepancy. In particular the two templates are distinct. [PR188, `f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d`, §4](https://github.com/GettysburgResearch/collatz/blob/f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d/research/astra-global-step-20261124/SHIFT_DISTANCE.md)

In the unaltered reference a physical shift $kL$, $k\not\equiv0\pmod N$, disagrees at $(N+1)d_H(U_0,U_1)/2$ sites, by the difference counts above. For a shift $kL+v$, $0<v<L$, fix a physical coordinate $j$ where $(U_0)_j\ne(U_0)_{j+v\bmod L}$. The two slot indices differ by $k$ or $k+1$, determined by $j$. If the difference is zero, both slots have label zero at $(N+1)/2$ possible first indices. If it is nonzero, inclusion-exclusion with the residue intersection count gives $(N+1)/4$ first indices with both labels zero. Each gives a distinct mismatch. Thus every nonzero physical shift differs at least $(N+1)\lfloor L/8\rfloor/80$ times, at least $NL/720$ once $L$ is large. Modifying $HL$ bits can remove at most $2HL$ mismatches at each offset, because a changed bit enters at most twice in the comparison.

Choose any one interval of $H=\lfloor N/4096\rfloor$ slots, and independently replace each of its slots by any member of $\mathcal U$. There are $2^{H\lfloor L/8\rfloor}$ distinct resulting marked words. Each still has at least $(1/720-1/2048)NL$ mismatches at every nonidentity physical shift. These words have least period $NL$. Formula (1) gives $\liminf \log_2 d/(NL)>1/2$ uniformly on this entire family as $N\to\infty$. Its logarithmic cardinality per physical bit tends to $(\log2)/32768$ as $N,L\to\infty$, with natural logarithms. In contrast the sublinear-error conclusion supplies essentially the full $NL$ denominator bits.

All these rational cycles have a minimum $\gg p^2$ uniformly in $N$ for sufficiently large convergents. Each used block has bounded discrepancy as above. Its own one-block fixed point, including any internal rotation of the block, is $\gg p^2$ by the suffix calculation in PR188 §4: the $i$-th odd position at an odd cut satisfies $2^{e_i}\gg3^i$ from discrepancy, so the carry is $\gg p3^{p-1}$, whereas $Q-P=P(e^{\Lambda_0}-1)$ and $0<\Lambda_0=L\log2-p\log3=O(1/p)$. Even phases are at least as large as their next odd state. Every full block acts as $x\mapsto(P/Q)x+(1-P/Q)y$, where its individual fixed point $y\gg p^2$. The minimum over boundaries of a closed concatenation is therefore at least the smallest such $y$. Any prefix of a used block has coefficient $3^q/2^s\ge3^{-18}(P/Q)^{s/L}\gg1$, so the same lower bound propagates to every physical phase. Along independently growing $N$ and upper convergents, $p/L\to\log_3 2$. One can additionally choose $p\gg N^2$ so that the full-period logarithmic imbalance $N\Lambda_0$ tends to zero. These examples are rational cycles of the literal map.

[The cyclotomic degree theorem](CYCLOTOMIC_DEGREE.md) permits many distinct reference blocks and every prime slot count at least five. Its undamaged reflection bound allows unboundedly many templates.

## Scope, comparison and evidence

The earlier equal-shape dictionary theorem BC5 uses a lattice of carry differences to rule out mixed integer cycles under an explicit carry-spread condition. In (1) the two templates are arbitrary, the raw denominator bound is exponential in the complete physical word length, and the replacements need only preserve an interval's total weight. PR188 gives high floors and widespread disagreements for random cells, together with a large denominator for at least half of its switching pairs. Its word construction, discrepancy and probability bound are inputs to the example above. Hu's ideal autocorrelation and the standard Gaussian-period calculation are existing methods. The interval replacement, short simultaneous exponents and nonvanishing numerical resultant provide the pointwise damaged-word estimate. [BC5 at `2fbc5706d2caff5d1485247e5291374ff4885041`](https://github.com/GettysburgResearch/collatz/blob/2fbc5706d2caff5d1485247e5291374ff4885041/research/lean-exact-witness-global-20261121/universal-step-20261123/cycles/BLOCK_CARRY_CAPACITY.md) · [Hu's Theorem 1](https://arxiv.org/pdf/1406.3889)

The prime macroperiod forces a common divisor $N$ of the total flip and division clocks. Neither an arbitrary primitive parity word nor a hypothetical integer cycle with coprime clocks is known to have this decomposition. Even at fixed clocks, the number of marked words covered by two templates and at most $r$ intervals of length at most $H$ is at most $NL\,2^{2L+rHL}N^{2r}$, allowing rotations of the physical cut. The bound counts choices of the two words, the endpoints of each interval and every replacement bit. With $r$ fixed, $H=o(N)$ and $p/L$ bounded away from 0 and 1, this is an exponentially small part of all $\binom{NL}{Np}$ words. Changing total interval weight would also change the modulus $D$. High rotational separation alone supplies no quadratic period relation at the complete numerical gcd. No closure statement for the remaining ordinary cases follows.

[PaleyResultant.lean](PaleyResultant.lean) checks the conjugate-product quadratic, clearing a possibly nonunit carry, signed modular exponent substitution, common-root divisibility of the actual polynomial resultant over $\mathbb Z/g$, and the reduced-algebra square contradiction. The construction of a quadratic-residue schedule, local squarefree reduction, real size bounds and final asymptotic theorem are written mathematics. [Kernel report](../../../../reports/astra-global-closure-20261124/round4/arithmetic/lean.json) · [Finite replay](controls.py)
