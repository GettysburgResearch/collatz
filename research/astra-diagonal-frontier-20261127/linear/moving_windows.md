# An ordinary predecessor in every prescribed moving binary cylinder and height window

**Status.** PROPOSED. The construction carries each supplied positive endpoint prime to three to an actual positive ancestor. Its word and exact integer affine replay are kernel-checked. The modular selection, rotation estimate, asymptotics, and counting corollary have written proofs. Universal convergence remains open.

Use $T(2n)=n$, $T(2n+1)=3n+2$, with $T(0)=0$ used only in computing a canonical prefix. All clocks count shortcut steps. Here a unit means a positive integer prime to three, including even units.

## Every sufficiently long prescribed clock

Fix $k\ge0$, $0\le r<2^k$. Follow $r$ for $k$ steps, writing $q$ for its number of odd inputs and $t=T^k(r)$. For any $v\ge0$ the ordinary source $r+2^kv$ has the same prefix and ends it at $t+3^qv$. Also $t<3^q$. For the latter, if the current value is below $2^{k-i}3^{q_i}$, then the even branch halves that bound, while the odd branch gives at most $(3(2^{k-i}3^{q_i}-1)+1)/2<2^{k-i-1}3^{q_i+1}$. The initial inequality is $r<2^k$.

**Theorem 1.** Fix the supplied unit $y$, the prefix above, and the desired number $m=d+1\ge1$ of *additional* odd inputs. Put
\[
 s=q+d+1,\qquad A=3(3^d-2^d),\qquad P=2\cdot3^{s-1}.
\]
For every $H\ge d+P$ there is a unique $j\in[d,d+P)$ such that
\[
       2^j\equiv 2^H y-A-3^{d+1}t\pmod{3^s}.
\]
Define
\[
 z=\frac{2^Hy-A-2^j}{3^{d+1}},\qquad
 x=r+2^k\frac{z-t}{3^q}.
\]
If $z\ge t$ and $x>0$, then $x\equiv r\bmod 2^k$, $T^{k+H}(x)=y$, and the added word after the native prefix has odd positions exactly $0,\ldots,d-1,j$ (positions start at zero). The positivity conditions hold for all sufficiently large $H$ uniformly over $y\ge1$ at fixed $k,d$.

**Proof.** The right hand side of the congruence is a ternary unit. The order of 2 modulo $3^s$ is $P$. Indeed $v_3(4^{3^h}-1)=h+1$ by induction using $(1+3^e u)^3-1$ with $e\ge1$, $3\nmid u$. Modulo three the order of 2 is two. The order divides $2\cdot3^{s-1}$ by Euler's theorem, and the displayed valuation rules out every smaller even divisor for $s>1$. Thus $P$ consecutive exponents yield all units, including at $s=1$. The congruence implies $z=t+3^qv$ with integral $v$, nonnegative by hypothesis.

The word of length $H$ has $d$ initial odd inputs, $j-d$ even inputs, one odd input, and $H-j-1$ final even inputs. Its forward affine numerator has multiplier $3^{d+1}$ and constant $A+2^j$. This follows from the identity $2^dT^d(z)=3^dz+3^d-2^d$ on the initial odd branch. Conversely, an exact affine row with an integer input and output enforces each bit of the prescribed word: reduce modulo two, divide the legal first branch, and iterate. This also verifies every intermediate parity when $j=d$ and when the final halving run is empty. The constructed $z$ satisfies the row, and $x=r+2^kv$ realizes the native prefix. [Physical word and integer replay in Lean](UnitWindowLift.lean)

Write $W=2^{H+k}y/3^s$. The native affine identity implies $r\le2^kt/3^q$. Before testing positivity the rational identity gives
\[
       0\le W-x
          =\frac{2^kt}{3^q}-r+\frac{2^k(A+2^j)}{3^s}
          \le 2^k(4+2^j).
\]
It is valid also for $q=0$ or $d=0$. When its right edge is negligible compared with $W$, $x>r$ and hence $z>t$ automatically.

The placement of one movable odd step to adjust a discrete logarithm has an antecedent in the closing construction in Theorem 20 of fourier_wren, Section 10.4. The present statement prescribes the original ordinary endpoint, low source bits, total clock, and extra odd count simultaneously. All sufficiently long clocks work, and the loss in height is uniform in the supplied endpoint and clock. [Automaticity of saturated sets, v3, October 31, 2026](https://rstation.ai/problems/collatz/papers/64/v3)

## Quantified rotation without an irrationality-measure input

Put $\alpha=\log_2 3$. The maximum gap on the unit circle between points $\{m\alpha:1\le m\le M\}$ is $O(1/\log M)$ for sufficiently large $M$.

For an integer $Q\ge2$, pigeonholing $0,\alpha,\ldots,Q\alpha$ into $Q$ equal arcs gives $1\le h\le Q$, $u\in\mathbb Z$ with $0<\delta=|h\alpha-u|\le1/Q$. Since $3^h$ and $2^u$ are distinct positive integers here, $1\le|3^h-2^u|\le 2\cdot3^h\delta$, by the mean-value theorem on $[-1/2,1/2]$ for $2^v$. Therefore $\delta\ge(2\cdot3^Q)^{-1}$. The first $\lceil1/\delta\rceil$ positive multiples of $h\alpha$ have maximum circular gap at most $\delta$: after rotation and possible reflection these are the consecutive multiples $0,\delta,\ldots,(\lceil1/\delta\rceil-1)\delta$. Their positive indices are at most $Q(2\cdot3^Q+1)$. With $Q=\lfloor\frac12\log_3 M\rfloor$ this is at most $M$ for large $M$. This proves the stated rate. Irrationality alone, without the elementary integer separation, would not justify it.

## A shrinking window with growing modulus

**Theorem 2.** Fix $0<c<\beta<1$. There is a constant $C=C(c,\beta)>0$ such that the following holds for every sufficiently large real $X$. Write $L=\log_2 X$. Simultaneously for every
\[
  0\le k\le c\log_3 L,\qquad 0\le r<2^k,\qquad
  1\le y\le X\,2^{-8L^\beta},\quad 3\nmid y,
\]
there exists a positive $x$ with
\[
 x\equiv r\bmod2^k,\qquad
 X\le x\le X\left(1+\frac{C}{\log\log\log X}\right),\qquad
 T^\ell(x)=y\ \hbox{for some }\ell=O(L).
\]
The implied constants and the lower threshold on $X$ do not depend on $k,r,y$. In particular all units $y\le X^{1-\eta}$ are covered for any fixed $\eta>0$ and sufficiently large $X$. Each $y$ is the original supplied integer.

**Proof.** Take $M=\lfloor(\beta-c)\log_3 L\rfloor$. For $1\le m\le M$, $q+m\le k+M\le\beta\log_3 L$. Hence the chosen odd position in Theorem 1 satisfies $j<M+2L^\beta$. Let $\rho=C_0/\log M$ dominate the maximum circular gap from the preceding estimate. For large $X$ assume $0<3\rho<1$. The reflected and translated rotation points have the same maximum gap. Thus for some $m\in[1,M]$ and integer $H$,
\[
  \rho\le H-\bigl(\log_2(X/y)-k+(q+m)\alpha\bigr)\le3\rho.
\]
This means $X2^\rho\le W\le X2^{3\rho}$. We also have
\[
 H\ge8L^\beta-k \ge M+2L^\beta,\qquad k+H\le L+O(\log L).
\]
Theorem 1 applies, and its height loss is at most $2^k(4+2^{M+2L^\beta})=2^{o(L)}$. Since $X(2^\rho-1)\gg X/\log M$, that loss is smaller than the margin above $X$. Thus $x\ge X>r$ and both positivity guards hold. Finally $2^{3\rho}=1+O(1/\log M)$, with $\log M$ of order $\log\log\log X$. This proves all claims.

## A fixed exceptional endpoint would force many starts in every such window

Use only the following external input for this section. Lech Mazur's September 6, 2026 manuscript gives positive lower natural density of ordinary, unaccelerated predecessors of each fixed positive target prime to three. The public formalization records this target-dependent lower density. It has not been rebuilt for this packet. For the shortcut, apply it to $2a$: an ordinary visit to $2a$ is followed by $a$, and the shortcut visits $a$ whether or not it skips that occurrence of $2a$. [Positive Lower Density of Collatz Predecessors and exact formal scope](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html)

For every eligible fixed $a$, the *unit* shortcut predecessors $y\le Y$ of $a$ still number $\gg_a Y$ for large $Y$. Start with at least $h_a Z$ shortcut predecessors $n\le Z$, $Z=\lfloor Y/3\rfloor$. Discard multiples of $2^{J+1}$ where $2^{-J-1}<h_a/2$. Keep a unit $n$ as $y=n$. For $3\mid n$, write $n=2^i u$ with $u$ odd and $i\le J$, and use $y=T(u)\le Y$. Every earlier vertex up to $u$ is divisible by three, so $y$ still reaches $a$. Each output is produced at most $J+2$ times, by direct retention or by a fixed $i$ and the uniquely determined $u$.

Take $Y=\lfloor X2^{-8L^\beta}\rfloor$ in Theorem 2 and fix *any* allowed cylinder. Every one of these unit predecessors $y$ supplies an $x$ in the stated narrow window and cylinder. A given $x$ can supply at most $O(L)$ distinct $y$, since there are at most $O(L)$ possible physical clocks. Consequently for each fixed $a$ and all sufficiently large $X$ the number of starts in that cylinder and window which reach $a$ is at least
\[
          \gg_{a,c,\beta} \frac{X\,2^{-8(\log_2 X)^\beta}}{\log X}.
\]
In particular it exceeds $X^{1-\epsilon}$ for each fixed $\epsilon>0$ once $X$ is large enough. The clock bound applies up to $y$. The later time from $y$ to $a$ is unrestricted. The pointwise Theorem 2 does give an $O(\log X)$ clock for the single target $y=a$, with no claim of this multiplicity at the shorter clock.

**A sufficient convergence test.** Fix $c,\beta$ as above and the window constant from Theorem 2. Suppose that for some $\epsilon>0$ and an unbounded sequence of $X$, there are choices of the allowed $k,r$ for which at most $X^{1-\epsilon}$ starts in the entire stated window and cylinder lack a proof of reaching 1. Then every positive integer reaches 1. Otherwise strip powers of two from a bad source and take one odd step if necessary to obtain a fixed bad unit $a$. Its predecessors in every such window have the displayed lower bound, which exceeds the allowed omissions. No such coverage estimate is established here. The result uses neither stationarity in a transported head nor an independently changing target.

## Comparison and the principal-gate obstruction

Monks, Monks, Monks and Monks studied sufficient sets and backward itineraries in arithmetic progressions. fourier_wren's Theorem 20 uses movable-bit steering. The later protected-window program obtains different asymptotic counts using external natural-density and distribution inputs. The contribution here is the every-clock affine family and the simultaneous deterministic control of a moving growing cylinder, relative real height, and an individually supplied endpoint. The density corollary requires only the fixed-target lower-density result above. [Monks et al., Discrete Mathematics 313 (2013)](https://arxiv.org/abs/1204.3904) · [Protected first meetings, Appendix A.5 and preceding density comparison](https://rstation.ai/problems/collatz/papers/179/v1)

For an odd starting and ending site, the $7/4$ prefix gate of PR 201 requires $4A_i\le7i$ at each odd date, where $A_i$ is elapsed shortcut time. In the construction above there are $q+m=O(\log\log X)$ odd inputs. At $y\le X^{1-\eta}$ the total elapsed time is at least $\eta\log_2X-O(\log\log X)$. The terminal prefix therefore violates the gate for large $X$. The final word has a long physical run of halvings. Reanchoring after it can send many different starts to the same fixed old source. This precludes transferring the near-linear count to a population of distinct principal sites by this argument.

The basic fact that 7 has no positive predecessor below 7 also limits universal inverse-only descent. The two eligible inputs 1 and 2 demonstrate why the unit condition and exact positive cofactors matter. A multiple of three cannot be the final vertex of a shortcut word with any odd input. The adjoining exact checker replays both the native and the appended parities and visits for 2,268 concrete ordinary lifts. It also compares the separate linear representation test against 520 finite models.
