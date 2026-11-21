# Near-minimal early mergers occur at a sparse set of ternary depths

**PROPOSED, unconditional.** Use the shortcut Collatz map $T(x)=x/2$ on even positive integers and $T(x)=(3x+1)/2$ on odd ones. Write $s_j(x)$ for the number of odd inputs before time $j$. Fix an integer $E\ge1$. Let $\mathcal A_E$ be the set of integers $A\ge1$ for which there exist $k\ge1$, $0<m<n$, and clocks $i,j\ge0$ satisfying

$$
 3^A\mid n,\qquad 8^k\mid n+5,\qquad i\le3k,\qquad
 T^j(m)=T^i(n),\qquad s_j(m)-s_i(n)\le A+E.
$$

**Theorem.** The phases $\{A\log_2 3\pmod1:A\in\mathcal A_E\}$ have only finitely many accumulation points on the circle. In particular $\mathcal A_E$ has zero upper Banach density, meaning
$$
 \lim_{N\to\infty}\sup_{b\ge0}
 \frac{|\mathcal A_E\cap[b+1,b+N]|}{N}=0 .
$$
Outside this set of depths, every such meeting costs more than $A+E$ extra odd inputs. Both the length $3k$ of the protected segment and the clock $j$ on the smaller start may vary without bound. For powers $n=3^a$ one can set $A=a$. The theorem permits infinitely many exceptional depths for a fixed $E$.

## Data supplied by an actual meeting

Extend a meeting to the checkpoint $Y=T^{3k}(n)$ along the common path. This preserves the excess in odd counts. The basic checkpoint bound gives an excess $A+e$ with $1\le e\le E$. The proof of its small-witness theorem splits off $e$ odd inputs from $m$ to a state $v$, then $A$ odd inputs through a segment of length $J$, leaving a suffix with $2k$ odd inputs. The suffix, pulled back from the signed point $-5$, supplies $M\ge5$ and $b\ge0$ with
$$
 S^{3k+b}(M)=5,\qquad s^{S}_{3k+b}(M)=2k,\qquad c=5\cdot2^b-M ,
$$
where $S(x)=x/2$ on evens and $(3x-1)/2$ on odds. The middle segment supplies a positive ordinary $\beta$ with
$$
 c=T^J(\beta),\quad s_J(\beta)=A,\quad
 g=3^A/2^J,\quad v=\alpha n+\beta,\quad
 \alpha=2^b/g<(3/2)^e,\quad \beta+1<5(3/2)^e .
$$
In particular the possible $\beta$ form a finite set depending only on $E$. Every odd affine offset of $T$ is positive, so $c/g\ge\beta$. Consequently
$$
 (2/3)^E < c/2^b=(c/g)/\alpha\le5 .
$$
[Derivation of the signed suffix and ordinary middle segment](NEGATIVE_FIVE_CHECKPOINT.md#what-a-near-minimal-merger-would-imply)

## Which signed and ordinary paths actually produce mergers?

The extraction has an exact converse. Suppose $k,e,A\ge1$, $\beta>0$, $s_J(\beta)=A$, and $c=T^J(\beta)$. Suppose also that $S^{3k+b}(M)=5$ with exactly $2k$ odd inputs, $b\ge0$, $c=5\cdot2^b-M$, and
$$
 \alpha=2^{J+b}/3^A<(3/2)^e .
$$
Then infinitely many pairs of ordinary starts $0<m<n$ realize a merger at the checkpoint with exactly $A+e$ extra odd steps. The first $e$ steps of $m$ can all be odd.

Indeed choose a positive integer $d$ by the two simultaneous congruences
$$
 3^A d\equiv-5\pmod{8^k},\qquad
 2^{J+b}d\equiv-(\beta+1)\pmod{3^e}.
$$
The coefficients are invertible in their respective moduli, and the Chinese remainder theorem supplies arbitrarily large $d$. Set $n=3^A d$, $t=(n+5)/8^k$, $v=2^{J+b}d+\beta$ and $m=2^e(v+1)/3^e-1$. Then $m$ is integral and its first $e$ steps are odd and end at $v$, since $T(x)+1=3(x+1)/2$ at an odd input. The coefficient of $n$ in $m$ is $(2/3)^e\alpha<1$, so $0<m<n$ for all sufficiently large choices of $d$. The next $J$ steps have the same parities as the orbit of $\beta$, and end at $z=2^b n+c$. Finally $z+M=2^{3k+b}t$. The paths from $z$ and $-M$ agree in parity for $3k+b$ steps, so the positive endpoint equals $3^{2k}t-5=T^{3k}(n)$. The three parts of the competing path have $e,A,2k$ odd inputs. The construction requires divisibility by $3^A$ and allows higher ternary valuation. Together with the extraction above this characterizes the existence of such mergers at any depth $A$ and excess $e$. Strictness at the slope threshold is necessary by the extraction, and equality of the dyadic and ternary powers in that threshold is impossible for $A,e\ge1$.

For every $A,k\ge1$ there is an explicit choice. Under $S$ the path $19\to28\to14\to7\to10\to5$ has length five and two odd steps. Append $k-1$ laps at 5. This gives $b=2$ and $c=5\cdot4-19=1$. From $\beta=1$ take $J=2A$ steps around the positive cycle, so $g=(3/4)^A$ and $\alpha=4(4/3)^A$. Choose
$$
 e=\left\lfloor\log_{3/2}\!\big(4(4/3)^A\big)\right\rfloor+1 .
$$
The construction produces infinitely many admissible $n$ having a smaller partner at $i=3k$ with exactly $A+e$ extra odd inputs. In fact $3\nmid d$ in this example since $2^{J+2}d\equiv-2\pmod3$, so $A$ is the exact ternary valuation of each constructed $n$. The surplus above $A$ is $(\log(4/3)/\log(3/2))A+O(1)=0.70951\ldots A+O(1)$. This upper bound is existential in the start at each prescribed depth.

## A countable closed set of normalized suffix values

Stop the $S$-path from $M$ at its first visit to 5. Let $h$ and $l$ denote the number of odd inputs and the number of steps up to that visit. Each removed lap $5\to7\to10\to5$ had two odd inputs and length three. Hence $h$ is even and $l=b+3h/2$, including when the first visit is at time zero.

Every vertex before the first hit is at least 5 because $\{1,2,3,4\}$ is forward invariant. The value 7 occurs at most once before that hit, and every other odd input is at least 9. Along the first-hit path the multiplicative identity is
$$
 2^l\,5/M=\prod_{x\ {\rm odd\ input}}(3-1/x).
$$
At 7 the factor exceeds $\sqrt8$. At odd $x\ge9$ it is at least $26/9=\sqrt8\,\theta$ with $\theta>1$. Thus for $h\ge1$,
$$
 0<M/2^b\le5\,\theta^{1-h}.
$$
For $h=0$ the entire path consists of halvings, $M/2^b=5$ and $c=0$. Otherwise $h\ge2$ is even. Thus every positive intercept satisfies the uniform gap
$$
 c/2^b\ge \delta_0=5(1-1/\theta)>0 .
$$
Sequences with $h\to\infty$ have $M/2^b\to0$.

For a fixed $h$ write $0\le t_1<\cdots<t_h<l$ for the odd positions. The affine formula for $S$, with its negative odd offset, gives
$$
 \frac{M}{2^b}
   =\left(\frac{\sqrt8}{3}\right)^h
     \left(5+\sum_{j=1}^h 3^{h-j}2^{t_j-l}\right).
$$
Every $2^{t_j-l}$ belongs to the compact countable set $\{0\}\cup\{2^{-d}:d\ge1\}$. The finite product of these sets is compact and countable, and so is its continuous affine image. This contains the closure of the normalized values at fixed $h$. For any convergent sequence of normalized values, a subsequence either has a common $h$ or has $h\to\infty$. The only additional possible limit in the second case is zero. It follows that the closure of all $M/2^b$ from the signed suffixes is compact and countable. The same holds for $c/2^b=5-M/2^b$. Intersect the latter closed set with $[\delta_0,5]$ and take $\log_2$ modulo one. This gives a single compact countable subset $K$ of the circle containing the phase of every $c$ above.

## The ordinary trajectory determines the other phase

For a positive $\beta$, the normalized value at time $j$ is
$$
 D_{\beta,j}=\frac{T^j(\beta)}{3^{s_j(\beta)}2^{-j}}
   =\beta\prod_{\substack{0\le v<j\\T^v(\beta)\ {\rm odd}}}
      \left(1+\frac1{3T^v(\beta)}\right).
$$
It is nondecreasing, and is constant on all clocks with the same odd count. At any clock supplied by a merger there is also the uniform bound
$$
 1\le D_{\beta,J}=c/g=(c/2^b)\alpha<5(3/2)^E .
$$
Fix a $\beta$ occurring at unbounded $A$. Since $J\ge A$, the nondecreasing sequence $D_{\beta,j}$ is bounded at unbounded clocks. Thus it converges to a finite positive $D_\beta$. This direct bound only uses the observed meetings. A separate orbitwise reciprocal theorem gives a finite normalized limit along any nonrepeating positive orbit. [Reviewed orbitwise reciprocal bound](../astra-three-routes/pass2/ORBIT_MELLIN.md)

The trajectory of this $\beta$ cannot be eventually periodic. In each complete positive cycle the affine constant is positive, so the period multiplier is less than one. Repeated periods would force $g\to0$, contradicting $g>(2/3)^E$ at the observed clocks. Thus the values along the trajectory are distinct, and they tend to infinity.

There is additional information from the first $b$ steps of the positive orbit from $c$. Because $c+M=5\cdot2^b$, the starts $c$ and $-M$ have the same $b$-step parity word. With $r$ its odd count this gives
$$
 T^{J+b}(\beta)=T^b(c)=5\cdot3^r-S^b(M)<5\cdot3^h.
$$
Here $b\le l$ and the signed first-hit path had $h$ odd inputs. Along any sequence with $A\to\infty$, the left side tends to infinity. Hence $h\to\infty$, and the signed bound gives $M/2^b\to0$ and $c/2^b\to5$.

It follows, along all productive clocks for this seed, that
$$
 A\log_2 3=\log_2(c/2^b)-\log_2(c/g)\pmod1
   \ \longrightarrow\ \log_2(5/D_\beta)\pmod1 .
$$
Every convergent subsequence of phases from distinct exceptional depths has a further subsequence with a common seed $\beta$ by the finite seed bound. There is at most one accumulation point per seed, proving the theorem. The compact countable signed spectrum above also describes the available finite suffixes before passage to these limits.

## Uniformity in intervals and separation of depths

A compact countable subset of the circle has measure zero and can be covered by finitely many open arcs of arbitrarily small total length. The rotation by $\log_2 3$ is irrational. Its visiting frequency in any fixed finite union of arcs tends to the arc measure uniformly in the initial phase. For example, averages of each nonconstant Fourier character are bounded by a geometric-sum constant divided by $N$, independent of the initial phase. Continuous majorants of the arcs then give the asserted uniform upper density. This proves the theorem.

For each seed occurring at unbounded depths, the successive depths it supplies have gaps tending to infinity. Indeed if a fixed gap $d\ge1$ recurred infinitely often, both phase sequences would tend to $\log_2(5/D_\beta)$ although their difference is $d\log_2 3\not\equiv0\pmod1$. Thus $\mathcal A_E$ is a finite union of such sequences and a finite set. For two different seeds, any fixed integer gap recurring infinitely often must match the difference of their phase limits modulo one. There are only finitely many such integer gaps, since irrationality allows at most one for each ordered pair of limits.

The same argument applies to any fixed finite signed sum of the exceptional set with itself. Its phases lie in the corresponding image of a finite product of the compact countable phase closure. In particular the positive separations between pairs of exceptional depths have zero upper Banach density. A proof that the exceptional set is empty beyond a finite point for every $E$ would require further input.

## An exact criterion using one set of ordinary target values

Define $\mathcal C$ as follows. For each $M$ that reaches 5 under $S$, stop at its first hit, at time $l$ with $h$ odd inputs. If $h$ is even, $b=l-3h/2\ge0$, and $c=5\cdot2^b-M>0$, include $c$ in $\mathcal C$. Removing complete laps does not change $c$ or $b$.

There is a fixed $E$ with infinitely many depths in $\mathcal A_E$ **if and only if** one positive ordinary trajectory visits infinitely many distinct values in $\mathcal C$. In the forward direction select a common $\beta$ along unbounded depths. Its infinitely many clocks have multipliers $g>(2/3)^E$. Every positive cycle has a strictly contracting multiplier over a full period, because that period has positive affine offset. Thus $\beta$ is nonperiodic, and its clock values $c\in\mathcal C$ are distinct on a subsequence. In the reverse direction such an orbit is nonrepeating, so the orbitwise reciprocal bound cited above gives a finite normalized limit $D_\beta$. At every visit, $\alpha=(c/g)/(c/2^b)\le D_\beta/\delta_0$. Choose a fixed $e\ge1$ with $(3/2)^e>D_\beta/\delta_0$. The odd count $A$ at the visits is unbounded, since no positive orbit can halve forever. Each first-hit representation has $h\ge2$ and permits $k=h/2$. The CRT construction above realizes the prescribed excess for every visit with $A\ge1$.

Membership in $\mathcal C$ can be determined by short exact signed trajectories. For given $c>0$, it suffices to try the bounded number of integers $b$ for which $c/5\le2^b\le c/\delta_0$. For each positive $M=5\cdot2^b-c$ the signed cost gives $\theta^{h-1}\le 5\cdot2^b/M\le2^{b+3}$. Since $\theta^{64}=(169/162)^{32}>2$, an eligible first hit occurs within $b+\tfrac32(1+64(b+3))$ steps. One can use rational slack in the range for $b$, for example $\delta_0>1/16$. Check the odd count and the defining equality at the first hit.

There is also an absolute $\eta>0$ with $|\mathcal C\cap[1,X]|=O(X^{1-\eta})$. At each fixed $b$, the cases $h\ge b/8$ give $M=O(2^b\theta^{-b/8})$ and hence at most that many intercepts. When $h<b/8$, $l=b+3h/2\le2b$, and the odd positions determine $M$ uniquely for each $h$. These position sets account for at most $\sum_{h\le b/8}\binom{2b}h\le2^{2bH_2(1/16)}$ choices, where $H_2$ is binary entropy and $2H_2(1/16)<1$. Sum the two geometric estimates through $b\le\log_2(X/\delta_0)$. The resulting sparse set does contain values on convergent orbits. Whether a single positive trajectory visits infinitely many distinct members remains open.
