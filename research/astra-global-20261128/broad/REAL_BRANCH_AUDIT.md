# A real conjugacy sum whose prescribed branches violate ordinary parity

**PROPOSED, exact counterexample to a stated intermediate lemma.** López and Stoll use the ordinary shortcut map and separately apply the affine formulas indicated by the bits of a prescribed infinite word. Their Lemma 24 says that for an aperiodic word $v$ with finite real conjugacy sum $\Phi_{\mathbb R}(v)$, its successive real values are all distinct. Their proof of Theorem 1 also uses the assertion that an accumulating real pseudo-orbit cannot start at a rational with odd denominator. Both assertions about the prescribed real branches have the following counterexample. It does not refute Theorem 1's conclusion about genuine rational 2-adic orbits. [López and Stoll, arXiv:2101.12747v1, introductory Scheme 2, Lemma 24 and the proof of Theorem 1](https://arxiv.org/pdf/2101.12747).

Start at $x_0=-5$. First use the word $(110)^2$, where a one applies $x\mapsto(3x+1)/2$ and a zero applies $x\mapsto x/2$. Both the length-three and the length-six prefixes end at $-5$, by the explicit cycle $-5,-7,-10,-5$. Next prescribe a zero. Its real image is $-5/2$.

Put $r=-x-1$. At this point $r=3/2$. At all subsequent times choose one if $r<1$ and zero otherwise. The updates are
$$
 r\longmapsto\frac{3r}{2}\quad(1),\qquad
 r\longmapsto\frac{r-1}{2}\quad(0).
$$
The initial denominator is two. Each update doubles the reduced denominator, since an odd numerator remains odd over the new denominator. In particular $r=1$ never occurs. The interval $0<r\le3/2$ is invariant from that time on. Immediately after each zero, $0<r\le1/4$. At least four ones are then required to reach $r\ge1$ again. A run of ones is finite because the positive $r$ multiplies by $3/2$ until the threshold. Therefore the lower asymptotic proportion of ones is at least $4/5$, and $3^{s_t}/2^t$ grows exponentially.

The infinite word is aperiodic, including after any finite deletion. If a period of length $L$ with $h$ ones were repeated eventually, $h/L\ge4/5$ and the affine period has slope $3^h/2^L>1$. Boundedness under all its forward repeats forces the real state to equal the unique real affine fixed point at that phase. The strictly increasing reduced denominators exclude such periodic states.

Write the affine action of the first $t$ prescribed symbols as $x_t=(3^{s_t}x_0+B_t)/2^t$. The real conjugacy partial sum is $-B_t/3^{s_t}=x_0-x_t2^t/3^{s_t}$. The states $x_t$ are bounded, hence this sum tends to $x_0=-5$. The same argument applies to every suffix, so the successive prescribed real states are exactly the conjugacy sums of those suffixes. Two of them equal $-5$. The later values form an infinite bounded set of distinct dyadic rationals, and so have an accumulation point. The real sum belongs to the odd-denominator rationals.

The failure occurs at the seventh prescribed symbol: it is zero at the odd integer $-5$. The genuine 2-adic realization of $v$ differs from $-5$ at precisely dyadic depth six. Its rationality is undetermined here. Thus ordinary rationality of a real conjugacy sum does not force the prescribed word to be its parity word. Equating those two words is the step used on the page containing Lemma 24 (PDF index 27, counting its first page as index zero). The subsequent implication from an accumulating real pseudo-orbit to failure of odd-denominator rationality, used in the proof of Theorem 1 (PDF index 28), also fails for this example.

More generally, every negative integer $-m$ with $m\ge2$ has an aperiodic prescribed real word with lower density at least $4/5$ and real conjugacy sum $-m$. Initially choose the branch opposite its ordinary parity. If $m$ is even, the chosen odd branch sends $r=m-1$ to $3r/2>0$. If $m$ is odd ($m\ge3$), the chosen even branch sends $r$ to $(r-1)/2>0$. In both cases the new reduced denominator is two. The same threshold rule first enters $0<r\le3/2$ and then gives the preceding construction. This extension concerns the real conjugacy sum only.

## The threshold four in the real inverse branches

At the state after an even symbol, group the ensuing $g$ ones and the next zero. The inverse map on the real post-even variable is
$$
 I_g(r)=(2/3)^g(1+2r).
$$
For $G\ge2$ put $R_G=(2/3)^G/(1-2(2/3)^G)$. Each $I_g$ with $g\ge G$ maps $[0,R_G]$ into itself. Its image interval is $[(2/3)^g,(2/3)^g(1+2R_G)]$. Adjacent intervals overlap or touch exactly when $(2/3)(1+2R_G)\ge1$, equivalently $R_G\ge1/4$. This holds for $G=2,3,4$ and fails for all $G\ge5$. For $G=4$ the right endpoint is $16/49$; for $G=5$ it is $32/179$.

In the overlapping cases every interior point can be continued with such a branch. A left endpoint of one interval also lies in the interior of its neighbor because the overlap is strict for the three integer values of $G$. The top endpoint has the fixed branch $G$. Thus every $r\in(0,R_G]$ has an infinite expansion in these inverse branches. In the disjoint cases the images already leave open real gaps at the first level. The ordinary 2-adic word is fixed by its initial value in both regimes.
