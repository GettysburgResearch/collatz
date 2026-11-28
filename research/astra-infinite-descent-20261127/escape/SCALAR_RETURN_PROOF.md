# A return-time proof of the scalar square-root upper bound

The counted adjacent-pair absorption theorem and the inverse-square-root upper rate are prior results of Said Duran and Leen, respectively. This note gives a self-contained written derivation of the upper bound for the [first-arrival atom argument](CLOCK_ANTICONCENTRATION.md), using the packet's finite counted merger at the last step. It gives neither the prior exact leading constant nor a lower asymptotic. [Said Duran, Prop. 2.2 and Thm. 3.1](https://doi.org/10.5281/zenodo.23003524) · [Leen, exact rates](https://doi.org/10.5281/zenodo.23268751) · [Weaver 124/v1, scalar kernel and uniform time estimates](https://rstation.ai/problems/collatz/papers/124/v1).

## The physical chain

Start with a Haar binary integer \(v\) and the two formal counted states \((v,3^k v+c)\), where \(k\ge0\) and \(c\) is an arbitrary integer. The formal pre-count of the higher-slope state exceeds the other by \(k\). Apply the positive-map shortcut formulas as maps of binary integers. At each step reorder by the formal count and use the lower-slope current value as anchor. At a tie retain the current orientation, with the choice determined by the known prefix. A counted merger is the first state \((k,c)=(0,0)\). From an ordinary pair \((v,v+1)\), the probability of surviving through clock \(t\) equals the fraction of failed counted comparisons among the \(2^t\) binary residues, by the parity lift.

For a fresh anchor bit \(b\in\{0,1\}\) put \(p=(b+c)\bmod2\). The tentative new exponent is \(j=k+p-b\). When \(j\ge0\), the new offset is \((3^p c+p-3^j b)/2\). When \(j=-1\) (only \(k=0,b=1,p=0\)), swap the roles; the new exponent is 1 and its offset is \((1-3c)/2\). Conditional on every finite past, the new anchor is an odd integral affine function of the unused Haar suffix. Its parity is therefore fresh and fair, including after a swap. The same fact holds after any almost surely finite stopping prefix by conditioning on its length and word. Declare the fused state absorbing.

Put \(U=|c|/3^k\), fix \(\alpha=1/2\), and use the ordinary physical step clock. The two formulas give
\[
 U'\le (3^b/2)U+1/2,
 \qquad \mathbb E[(U')^\alpha\mid k,c]\le\chi U^\alpha+2^{-\alpha},
 \quad \chi=(2^{-\alpha}+(3/2)^\alpha)/2<1.                           \tag{1}
\]
Indeed in the unswapped case the additive part divided by \(3^j\) has magnitude at most \(1/2\); in the swapped case use \(|1-3c|/6\le U/2+1/6\). The count gap stays fixed when \(c\) is even. At a mixed step (\(c\) odd) it moves by equally likely signs when \(k>0\) and moves to one at zero. Thus \(\mathbb E[(k')^2\mid k,c]\le k^2+1\). These inequalities also hold at absorption.

## A zero-level return from any positive gap

While the count gap stays at a fixed positive level \(j\), let \(W\) include the first physical step where the two parities differ. For \(\ell\ge0\), no mixed step among the first \(\ell\) means the two full parity words agree. The shortcut word labels are a bijection on residues modulo \(2^\ell\). Therefore
\[
 \Pr(W>\ell\mid j,c)
 =\Pr((3^j-1)v\equiv-c\pmod{2^\ell})
 \le\min(1,2^{v_2(3^j-1)-\ell}).
\]
Its sum gives \(\mathbb E W\le2+v_2(3^j-1)\le4+v_2(j)\). For odd \(j\) the first valuation is one. For even \(j\), factor \(3^j-1\) by successive differences of squares to obtain \(v_2(3^j-1)=2+v_2(j)\). In particular each wait is almost surely finite. The event that the next step is mixed is decided by the already known offset; the still fresh anchor bit then chooses its sign. The positive count gap observed at successive mixed steps is the ordinary unbiased nearest-neighbor walk until its first visit to zero.

Stop that walk at \(0\) or \(K\), starting at \(0<k<K\). The probability of the upper exit is \(k/K\). The expected number of visits to each internal \(j\), including the starting visit when appropriate, is
\[
       G_K(k,j)=2\min(k,j)(K-\max(k,j))/K\le 2k.
\]
Both results follow by solving the linear second-difference equation with zero-endpoint boundary values (for the probability the upper boundary is one; for \(G\) the equation adds \(1_{k=j}\)). The finite walk exits almost surely, for example a string of \(K\) identical signs forces exit. At each entry to a level the conditional waiting expectation just proved is uniform in the current offset. Consequently the expected number of **physical** steps to either boundary is at most
\[
     2k\sum_{j<K}(4+v_2(j))\le10kK,
\]
where the sum is over \(j=1,\ldots,K-1\) and \(\sum_{j<K}v_2(j)=\sum_{r\ge1}\lfloor(K-1)/2^r\rfloor<K\). The average over levels keeps the logarithm of the individual worst waiting time out of this estimate. Thus if \(T_0\) denotes first arrival at zero count gap, counting an initial zero as time zero,
\[
                \Pr_{k,c}(T_0>t)\le C k/\sqrt{t+1}\quad(k\ge1,t\ge0).  \tag{2}
\]
For \(k<\lceil\sqrt t\rceil\) use upper-exit probability plus Markov's inequality for exit time with \(K=\lceil\sqrt t\rceil\); otherwise the trivial probability bound suffices after a fixed change of constant. In particular \(T_0\) is almost surely finite, uniformly in the sense of (2).

## Excursions with an offset-dependent initial waiting budget

At a live zero-level state \((0,c)\) define \(B(c)=\max(2,\lceil C_1\log(2+|c|)\rceil)\), with \(C_1\) such that \(\chi^{B(c)} |c|^\alpha\le1\). First run the chain for exactly \(B=B(c)\) physical steps, extending an absorbed trajectory by the absorbing state. Then wait until the first zero level from the resulting state; let \(D=B+T\) be this complete duration. From (1) and the squared-gap inequality,
\[
       \sup_{j\ge B}\mathbb E U_j^\alpha\le C_2,
       \qquad \mathbb E k_B^2\le B.
\]
By (2), \(\Pr(T>t)\le C\sqrt B/\sqrt{t+1}\). Absorbing the deterministic initial time into this bound gives
\[
                 \Pr(D>t)\le C_3\sqrt B/\sqrt{t+1}.                     \tag{3}
\]
Both constants are independent of \(c\).

At the terminal zero level write \(c'\) for its integer offset, including zero at absorption. For \(u\ge2\) let \(H=\lceil e^{\alpha u/2}\rceil\). The chance that \(\log(2+|c'|)>u\) is at most \(\Pr(T>H)\) plus the sum, over \(0\le i\le H\), of \(\Pr(U_{B+i}> e^u-2)\). Indeed \(U=|c'|\) at level zero. No independence between the return time and the offset is needed. The preceding bounds give
\[
 \Pr(\log(2+|c'|)>u)\le\min(1,C_4(1+\sqrt B)e^{-\alpha u/4}).          \tag{4}
\]
Integrating this bound at the point where the two alternatives cross yields \(\mathbb E B(c')\le C_5(1+\log B)\); Jensen gives \(\mathbb E\sqrt{B(c')}\le\sqrt{C_5(1+\log B)}\). Fix \(B_*\) so this last quantity is at most \(\tfrac12\sqrt B\) whenever \(B>B_*\).

The offsets with \(B(c)\le B_*\) form a fixed **finite** set. For each live member there exists a binary cylinder of positive measure on which the pair \((v,v+c)\) merges with identical physical clock and odd grade. For \(c>0\) use the [kernel-checked fixed-gap equal-grade theorem](../merger/FixedGapClock.lean) at one fixed target and clock; its positive integer witness gives an entire cylinder by the affine lift identity. For \(c<0\) translate the Haar anchor and exchange the pair. This is the known finite counted-coalescence mechanism. It requires no density theorem and no claim that every ordinary pair coalesces. There are a common finite integer \(B_{\rm fin}\ge B_*\) and \(\eta>0\) such that the chance of fusion by \(B_{\rm fin}\) is at least \(\eta\) from every live state of this finite set. From now on, use burn time \(B_{\rm fin}\) on this set, and use \(B(c)\) as the burn elsewhere. The weight \(\sqrt{B(c)}\) retains its original logarithmic definition on **every** state, including the finite set. Equations (3)–(4) remain valid with enlarged absolute constants on this finite set; in particular its terminal expected square-root weight is bounded by an absolute \(C_{\rm fin}\). The large-state inequalities are unchanged.

Set \(V(0)=0\) on the absorbed zero-offset state and \(V(c)=\sqrt{B(c)}+J\) for a live zero-level state. At all such states, with \(J\) a sufficiently large fixed constant,
\[
              \mathbb E[V(c')\mid c]+\tfrac12\sqrt{B(c)}\le V(c).       \tag{5}
\]
At a large state the terminal square-root expectation costs at most half the initial weight, and the additive \(J\) costs at most itself. At the remaining states the risk of absorption pays at least \(\eta J\) toward the bounded terminal expected weight. This proves (5).

Restart at each episode end while the state is live. The finite-prefix fresh-bit property permits the same conditional estimates at every restart. Telescoping (5) through a bounded number of episodes and applying monotone convergence gives
\[
        \mathbb E\sum_{i\ {\rm live}} \sqrt{B(c_i)}\le2V(c_0).
\]
There are only finitely many live episodes almost surely, and every individual complete duration is finite by (2). For any \(t\ge1\), integrate (3) to get
\(\mathbb E[\min(D_i,t)\mid c_i]\le C\sqrt{B(c_i)}\sqrt t\).
The first counted absorption time \(\sigma\) is at most the sum of the live episode durations. By subadditivity of truncation and the preceding budget,
\[
     \Pr_{0,c_0}(\sigma>t)
       \le \frac{\mathbb E\sum_{i\ {\rm live}}\min(D_i,t)}{t}
       \le \frac{C V(c_0)}{\sqrt t}.                                    \tag{6}
\]
In particular (6) for the single fixed state \((0,1)\) supplies the bound needed by the finite rotation argument. This is a written proof using elementary walk and moment bounds. The logarithmic source rate in that argument now has an independent derivation; the separate Gaussian lower comparison supplying sharpness at target 1 still uses a prior fixed-target timed law.
