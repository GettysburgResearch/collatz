# Moving the carry origin and paying for ordinary return

**PROPOSED.** A true first equal-grade crossing now gives a strictly smaller canonical reverse disagreement, with its original upper certificate, on a nonempty arithmetic progression. This replacement can occur consecutively to any prescribed finite depth on one positive source. Every fixed positive component with a 3-unit can be entered through such a chain. The selected source's triple has an explicit endpoint. Its convergence and a universal selection of a smaller reverse disagreement remain open.

Use the ordinary shortcut map $T$, its iterate $T^h$, its odd-departure count $Q_h$, and $C(n)$ for a finite hit at one. A canonical reverse disagreement means $z\equiv17\pmod{48}$, $C(3z)$, and $\neg C(z)$. All clocks below use this normalization.

## A first crossing which returns to the required orientation

For every nonnegative integer $a$, take
$$
 z=89585+48\,2^{19}a,\qquad w=1121+48\,3^8a .
$$
Both are 17 modulo 48 and $0<w<z$. At clock 14 the lower and upper physical states are $10+32w$ and $3+32w$. This is their first equal-grade crossing: their odd counts are 8 and 7, respectively, and the lower count was strictly less than one plus the upper count at every earlier clock. The carry is 7. The upper state is odd, so the earlier rule that used available initial halvings of the upper cannot spend any positive time on that carry.

Use 10 and 3 as the two low representatives. After five clocks they have both reached 1 with respectively one and two odd steps. Consequently the original states at clock 19 are $1+3w$ and $1+9w$. Each next shortcut meets the next shortcut from $w$ and $3w$, respectively. Thus $C(z)\iff C(w)$. **Every** supplied $T^H(3z)=1$ gives an actual $T^{H-19}(3w)=1$ and
$$
 Q_H(3z)=8+Q_{H-19}(3w).
$$
The upper arm at clock 19 is greater than 2, so the original hit must cover the matching clock even when it is the first hit. A canonical disagreement on this row therefore yields a smaller one. All its sources lie in class 3569 modulo 12288, missed by the sixteen-row bank at PR197's pinned head. This is one exact progression within that class. [MovingOrigin.lean](MovingOrigin.lean) · [PR197 guarded rows](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/paired-reductions/GuardedResidueCover.lean)

The general return allows any actual pair $y+c,y$, with $y=v+2^e u$ and $u$ odd. If $T^e(v+c)=T^e v=1$ at grades $p+1,r+1$, then the bad arm meets $3^p u$ and the good arm meets $3^r u$ at the next shortcut. A given upper suffix transfers with exactly $r$ fewer odd departures. The exact hypotheses price the extra odd step on the replacement. They allow arbitrary $v,c,e$ and arbitrary reference words. The smaller canonical row realizes $p=0,r=1$, retaining the orientation. [MovingOrigin.lean](MovingOrigin.lean)

Another family has $27z=251+2^{18+2k}u$ with odd $u$. At its first crossing, clock 5, the carry is 1 and the upper state $8+2^{13+2k}u$ has exactly three trailing zero bits. The carry 1 returns to one only at even clocks. Taking representatives 8 and 9 instead gives a good $3^{4+k}u$ and bad $3^{5+k}u$ for any reverse disagreement here. The original supplied upper certificate loses exactly $6+k$ odd steps including the five-clock prefix. For $k\ge84$, $2^{40}3^{5+k}u<z$, which contradicts minimality via the published quantitative return. There are canonical examples at each $k$: choose an odd $u\equiv13(2^{14+2k})^{-1}\pmod{81}$. This row has the opposite tower orientation from the preceding one. [MovingOrigin.lean](MovingOrigin.lean) · [Quantitative return](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean)

## Arbitrary depth and the fixed-component entry problem

Write $B=2^{19}$, $D=3^8$. Every prescribed $N$ occurs on unbounded positive sources with $N$ consecutive applications of the first row. On any supplied upper hit this saves $19N$ clocks and $8N$ odds. One constructive proof uses the commuting affine maps
$$
 L(a)=204954140672a+729593939,\qquad R(a)=2564819559a+9130222.
$$
The row's target at $L(a)$ equals its source at $R(a)$. Consequently $L^{N-j}R^j(a)$, for $0\le j\le N$, specifies successive source indices. A chain from $Z$ to $W$ also lifts to one from $Z+48B^Nt$ to $W+48D^Nt$ for every $t\ge0$. Each intermediate lift shifts by $48B^{N-j}D^jt$, exactly preserving both physical arms. In particular the *terminal* progression requires only ternary precision after the common factor 48. This removes the extraneous coprime factor from the particular commuting construction. [IteratedReturn.lean](IteratedReturn.lean)

Monks, Monks, Monks and Monks prove in Theorem 4.1 that every positive 3-unit back-traces into any prescribed residue class modulo $d=2^n3^mb$, $b$ coprime to 6. Their bound $2(b-1)\operatorname{ord}_b(3/2)+n+1$ counts inverse odd steps. Section 4 distinguishes that length from the norm which also counts inverse halvings. The CRT step uses powers of two to meet a ternary admissibility condition. For a translated progression $Z+D_0t$, use residue $Z$ modulo $qD_0>Z$ to exclude representatives below $Z$. Applying the theorem to this source progression gives a chain in every fixed bad 3-unit's component, with no condition on the label of the selected triple. A bad multiple of three has a 3-unit on its forward orbit after removing initial factors of two and taking an odd step. [Primary paper, definitions and Theorem 4.1](https://www.mathematicalgemstones.com/maria/papers/mmmm.pdf)

There is a more economical, explicit entry into the terminal progression. Fix a positive $x$ with $3\nmid x$, and take any witnessed chain terminal $W=1+16v_0\equiv17\pmod{48}$. Solve
$$
 2^k x\equiv 1+9v_0 \pmod{3^{8N+3}}.
$$
Powers of 2 generate the units modulo every positive power of 3. Add a multiple of their order to $k$ until $2^kx\ge1+9v_0$. Then $v=(2^kx-1)/9=v_0+3D^Nt$ with $t\ge0$, and $w=1+16v=W+48D^Nt$ belongs to the terminal progression. At the two physical endpoints,
$$
 T^{4+k}w=x,\quad Q_{4+k}(w)=2,\qquad
 T^{4+k}(3w)=3^{k+1}x-1,\quad Q_{4+k}(3w)=2+k.
$$
Indeed four clocks give $1+9v=2^kx$ and $2+27v=3\cdot2^kx-1$. The former takes $k$ halvings, and the latter takes $k$ odd shortcuts. A nonempty chain meets its terminal after one step and then preserves every subsequent iterate, so its initial arms at $19N+4+k$ give $x,3^{k+1}x-1$ with costs $8N+2,8N+2+k$. Thus **one fixed bad component realizes arbitrary finite depth with just two further odd steps on the terminal lower arm**. The starting inputs may change with $N$. The four-clock and tail identities as well as the strict height comparison for $x>1$ are in Lean. Primitive-root surjectivity and the written assembly with the translated progression use the published elementary number theory above. [PowerBacktrace.lean](PowerBacktrace.lean) · [IteratedReturn.lean](IteratedReturn.lean)

### The price in clocks for a fixed input

On every row write $z=17+48s, w=17+48t$. Then $Bt=Ds-184202$, with fixed rational coordinate $-184202/517727$, since $B-D=517727$. In unnormalized heights the fixed point is $-40337/517727$, and any $N$-step chain satisfies
$$
 B^N(517727w+40337)=D^N(517727z+40337).
$$
Because $z\equiv17\pmod{48}$, the rightmost parenthesis is divisible by 3. Thus $3^{8N+1}\mid517727w+40337$. The four-clock entry equation gives $9w=16\cdot2^kx-7$. Substitution gives the exact necessary divisibility
$$
 3^{8N+3}\mid 517727\,2^kx-203816.
$$
Equivalently $2^kx$ has prescribed ternary digits from the fixed rational $203816/517727$. [Lean centered identity](IteratedReturn.lean)

**Source-qualified written theorem.** For each fixed positive 3-unit $x$, every exponent in this entry satisfies $8N+3<C_x\log\max(3,k)$ for a finite positive constant $C_x$. Apply Kunrui Yu's Theorem 1 over $K=\mathbb Q$, $p=3$, $e=f=1$, with units $\alpha_1=2$, $\alpha_2=517727x/203816$ and exponents $(k,1)$. Condition $1.2$ holds because $3^f\equiv3\pmod4$. Both rational numbers have valuation zero at 3. The product differs from one since $203816/517727<1\le2^kx$. Yu bounds the valuation of the product minus one by $C(2,1,(3))h'(2)h'(517727x/203816)\log\max(3,k)$; the denominator 203816 is a 3-unit. Therefore the minimum legal $k$ eventually exceeds every linear function of $N$, and in fact grows at least exponentially in $N$ for fixed $x$. No uniform constant in $x$ is asserted. [Yu, *p-adic logarithmic forms and group varieties II*, Acta Arith. 89 (1999), Theorem 1 and (1.2), (1.5), (1.8), (1.9)](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

This construction cannot pay its return height by saving $8N$ odds on the original certificate. For $x>1$ the terminal $w=(16\cdot2^kx-7)/9$ already exceeds $x$, and every preceding row source exceeds $w$. For a least reverse disagreement $x$, the known hit is from $3x$. The selected triple instead reaches $3^{k+1}x-1$. Leastness compares smaller ordinary sources and supplies no hit there. The exact missing inference is a paired entrance whose triple has a known hit and whose terminal falls below the original source, or a different return that bypasses this accumulated cost.

## Two independent limits on extending the return

* In the canonical rank-three hard family $81z+271=2^{m+7}$, $m=11+162j$, the clock-five crossing has $x=y+1$, $y$ even and $3y+8=4\cdot2^m$. For **every** nonnegative low representative $v$, native clock $e$ and positive odd quotient $u$ with $y=v+2^eu$, one has $T^e(v+1)\ne1$. Depth zero conflicts with the parity of $y$; at depth one a positive odd input cannot hit one. Later legal depths have $e-2<m$. The lower trajectory reaches $2^m-1$ in two steps and is still odd after $e-2$ further steps, whereas a lower reference hit would give the even value $1+3^{Q_e(v+1)}u$. This excludes every nonnegative origin in the new mechanism at that crossing. The family can consist of convergent sources. [InverseEnvelope.lean](InverseEnvelope.lean) · [Pinned family](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean)
* For an arbitrary physical path of $h$ clocks and $q$ odds from $3^R w$ to $3^iu-1$, assume $u>0$ and $R+q\le i$. Then $w+1\ge 2^q3^{i-q}u$. For $R=0$ and prescribed $q\le i$, the all-odd inverse word attains equality. To see the bound, the corrected affine offset $S$ satisfies $2^h(T^h n+1)=3^qn+S$ with $0<S\le2^{h-q}3^q$. Divisibility gives $S=3^{R+q}d$ with $1\le d\le2^{h-q}/3^R$. Write $i=R+q+g$; then $w+d=2^{h-q}2^q3^gu\ge d\,2^q3^{i-q}u$, proving the result. Applied to phase $i$ in the ascent from $2^m-1$, it rules out every core $w<2^m-1$ whose rank plus odd cost is at most $i$, under any parity word and any number of halvings. The earlier PR195 bounded-block obstruction and PR197 rational-phase tests have different quantifiers. [InverseEnvelope.lean](InverseEnvelope.lean) · [PR195 round 12](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/README.md) · [PR197 paired reductions](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/paired-reductions/README.md)

The finite checker evaluates actual trajectories, both transformed arms, native-depth misses, affine minima, and discrete logarithms with fixed inputs. The large fixed-input exponents are verified modulo the stated precision; the separate moderate-clock examples run both complete ordinary paths. [Checker](check.py) · [Replay](../../../reports/astra-literature-closure-20261125/carry/finite.json) · [Strict compilation](../../../reports/astra-literature-closure-20261125/carry/replay.json)
