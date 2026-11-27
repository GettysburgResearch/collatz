# Sharp post-ascent meeting tails and a full-dimensional two-adic exception

Let \(T\) be the shortcut Collatz map. Under the natural-density law conditioned on \(H\ge2\) initial odd steps, let \(\tau_H=0\) if the orbit has already met some smaller positive source by time \(H\). Otherwise \(\tau_H\) is the number of further original steps until this first smaller-orbit meeting. The visitor may take any number of steps. Let \(\tau\) be the post-ascent limiting variable in [the joint profile](PROFILE.md).

There are positive absolute constants \(c,C\) such that
\[
 \Pr(\tau_H>t)\le C(t+1)^{-1/2}\quad(H\ge2,\ t\ge0),
 \qquad
 \Pr(\tau_H>t)\ge c(t+1)^{-1/2}
       \quad(H\ge400,\ 6(t+1)\le H).                         \tag{1}
\]
The upper bound already holds for the one prescribed smaller visitor \(m=(n-1)/2\), and that visitor inherits the lower bound in the indicated window. In particular
\[
              c(t+1)^{-1/2}\le\Pr(\tau>t)\le C(t+1)^{-1/2}
              \qquad(t\ge0).                                \tag{2}
\]
The limiting variable is finite almost surely; its positive moment of order \(a\) is finite exactly when \(a<1/2\).

## The physical upper uses one smaller visitor

Write \(n=2^Hv-1\), \(m=2^{H-1}v-1\). Both are positive and \(m<n\). Their initial odd ramps reach
\[
       x=3^Hv-1=3y+2,\qquad y=3^{H-1}v-1,
\]
after \(H,H-1\) respective shortcuts. The adjacent pair \(2y,2y+1\) reaches \(y,x\) in one shortcut. If this adjacent pair has counted-fused by time \(t+1\), then \(n,m\) meet by original clock \(H+t\). Counted fusion means the two values and accumulated odd counts agree at the same shortcut clock. The implication only needs agreement of values.

For Haar \(z\in\mathbb Z_2\), the chance that \(z,z+1\) have not counted-fused through \(t+1\) is \(O((t+1)^{-1/2})\). Conditioning \(z\) to be even costs at most a factor of two, and \(2y\) has exactly this conditional law since \(v\mapsto y\) has odd slope. Equivalently one may apply the canonical-pair bound directly to the state \((y,3y+2)\) with accumulated gap one. For a fixed horizon the tested parities are determined by a finite dyadic source class. For the adjacent pair, the equal-count condition ensures equal slopes in that class, so equality of values holds on the entire class or nowhere. Consequently the Haar estimate transfers to ordinary source natural density exactly, for every \(H,t\) separately with the same constant. The known pair tail is the only external synchronization input. Said Duran gives the pair chain and density-one fusion; Leen proves the quantitative pair estimate. Weaver 124/v1 explicitly restates the bound and attributes these scalar inputs. [Said Duran](https://doi.org/10.5281/zenodo.23003524) · [Leen, *Exact rates in Collatz synchronization*](https://doi.org/10.5281/zenodo.23268751) · [Weaver 124/v1, Theorem 1 and §2](https://rstation.ai/problems/collatz/papers/124/v1)

In fact for each fixed \(H,t\) the complete-orbit miss probability of this **specific** \(m\) equals exactly the Haar counted-fusion survival from the single scalar state \((y,3y+2)\) with initial gap one, independent of \(H\). This also proves existence of the sibling's natural density when its own clock is unrestricted. Fix \(K\ge t\). Outside relative upper density \(O((K+1)^{-1/2})\), the pair is aligned by the postpeak clock \(K\), so \(T^d(m)=T^{d+1}(n)\) for every \(d\ge H+K-1\). If the visitor reaches \(Y=T^{H+t}(n)\) at \(d>H+K-1\), then \(Y\) is periodic because \(d+1>H+t\). Periodic positive integers have zero density even when infinitely many cycles are allowed: \(T^k\) is injective on the union of all periodic points, hence the number of periodic integers at most \(X\) is bounded by \(|T^k([1,X])|\ll X^{49/50}\) for \(k=\lfloor\log_2X\rfloor\), from the companion image estimate. On each of the finitely many fixed upper length-\(H+t\) cylinders, \(n\mapsto Y\ll_{H,t}n\) is injective. Thus periodic targets cost zero relative density.

It remains to check finitely many \(d\le H+K-1\). On fixed parity words the physical slopes in \(v\) at \(Y\) and \(T^d(m)\) are respectively \(3^{H+f}/2^t\) and \(2^{H-1}3^k/2^d\), where \(f\) counts postpeak original odds and \(k\) counts all visitor odds. Equality outside finitely many isolated sources therefore forces \(d=H+t-1,\ k=H+f\). The residual visitor has precisely \(f+1\) postpeak odds and the high member \(x\) has \(f\), so equality is exactly counted fusion from the stated gap-one state. A hit on an earlier original point is equivalent to an endpoint hit by following its forward path. Let \(K\to\infty\) to prove the claimed equality with the finite canonical law. This identity identifies the fixed sibling with an existing scalar chain; no numerical leading coefficient is needed here. [Image bound](../allclock/SCALED_TARGETS.md)

For the all-smaller lower bound in (1), the earlier stopped result protects more than one third of every maximal \(t\)-word cylinder in the indicated window. There are at least \(\binom t{\lfloor t/2\rfloor}\) maximal words by grade-intercept uniqueness. Their ordinary relative mass in \(O^H\) is exactly their number divided by \(2^t\). Combining the two established estimates proves (1). Taking \(H\to\infty\) proves (2), including the upper estimate on all deadlines. The moment conclusion follows by summing \(t^{a-1}\Pr(\tau>t)\). For \(T=\lfloor H/6\rfloor-1\) the same sums give \(\mathbb E\min(\tau_H,T+1)\asymp\sqrt H\), and more generally order \(\log H\) at exponent \(a=1/2\) and \(H^{a-1/2}\) for \(a>1/2\) on this truncated window. The law of \(\tau_H\) exists on all integer bins for \(H\ge2\) by the finite-deadline transfer (at each original clock one can use the unrestricted finite-word comparison, including finite ties, and the least-ancestor tail from Weaver 177). Its mass at infinity vanishes by (1). For each fixed \(H\), a density-one assertion leaves open individual positive starts. [Stopped lower and all-clock transfer](STOPPED_LAW.md)

The earlier total variation estimate through \(T=\lfloor H/6\rfloor-1\) now controls the untruncated law of the first smaller meeting as well. The two tail masses beyond \(T\) are \(O(H^{-1/2})\) by (1)–(2), giving total variation distance \(O(H^{-1/2})\) for the complete clock law. Jointly with the first \(T\) postbits the same bound follows by expanding the \(>T\) bin, since the sum of its masses over all bit words is still \(O(H^{-1/2})\). Uniform integrability from (1) also gives convergence of the positive moments of order \(a<1/2\).

## Simultaneously growing integer shells

For all sufficiently large \(X\), simultaneously for \(400\le H\le(\log_2 X)/120\) and \(6(t+1)\le H\), the proportion in the ordinary shell \(X\le n<2X,\ n\equiv-1\bmod2^H\) protected through \(H+t\) is \(\asymp(t+1)^{-1/2}\), with absolute positive comparison constants. The same two comparisons apply when the visitor is restricted to \(m=(n-1)/2\). This version counts an actual finite shell while both clocks grow.

For the lower bound, \(B=H+t\le(\log_2 X)/90\). The fixed-word shell proof in the companion note uses this bound on \(B\) for its denominator, affine intercept comparison, finite ternary test and least-ancestor error. Its only separate use of the narrower ratio \(t/H\) is the bound on discarded high-even stops. The present sharper stopped estimate replaces that loss by at most \(2^{5-H/24}\), retaining more than one third on every maximal postword cylinder uniformly for sufficiently large \(X\). Each such cylinder has \(X/2^{H+t}+O(1)\) representatives. Summing the central-binomial number of maximal words gives the lower estimate with relative rounding \(O(2^{H+t}/X)\). For the upper bound the counted-fusion test of \((y,3y+2)\) through \(t\) is a union of \(v\bmod2^t\) classes. Its finite-shell discrepancy relative to all \(v\) in this shell is \(O(2^{H+t}/X)\). This is smaller than \((t+1)^{-1/2}\) uniformly in the indicated range. [Uniform finite-shell transfer](../allclock/POSTPEAK_VISITORS.md)

## All-prefix maximality has full Hausdorff dimension

A Haar-null exception remains large in Hausdorff dimension. Bias the independent postword letters to give an odd step probability \(p\in(1/2,1)\). Each signed-offset fibre among length-\(t\) words has a unique top grade \(u\), and at most one word of every lower grade. With \(r=(1-p)/p<1\), a word of deficit \(\delta\) has tilted mass \(r^\delta\) times the top word's mass. The entire fibre therefore has mass at most \(1/(1-r)\) times the top mass. Summing these inequalities proves
\[
      \Pr_p(w_t\text{ maximal})\ge1-r=(2p-1)/p .
\]
Maximality at all preceding lengths follows from maximality at the final length, because equal offsets and grade differences survive a common suffix. Continuity of probability on decreasing events gives the same positive lower bound for the set \(\mathcal A\) of binary paths maximal at **every** finite length. For each \(N\) in the common ternary protection set, every \(W\in\mathcal A\) survives forever in the limiting model. This last set has at least \(s(2p-1)/p\) probability under independent common ternary and biased binary coordinates, with \(s=284051/829440\).

Give binary paths the dyadic metric. Almost every tilted path has limiting odd frequency \(p\) by the strong law. Its length-\(t\) cylinder has measure \(2^{-t(h_2(p)+o(1))}\), where \(h_2(p)=-p\log_2p-(1-p)\log_2(1-p)\). For every \(d<h_2(p)\), some positive-mass subset of \(\mathcal A\) has all its sufficiently long cylinder masses bounded by \(2^{-dt}\) at a common starting length, by the increasing union over these lengths. Cylinder covers then have positive \(d\)-dimensional content. Hence \(\dim_H\mathcal A\ge h_2(p)\). Letting \(p\downarrow1/2\) proves \(\dim_H\mathcal A=1\). Its fair Haar measure is zero, since \(p(D_w)\ge s\) gives \(s\Pr_{\rm fair}(w_t\ {\rm maximal})\le\Pr(\tau>t)\) and (2) tends to zero.

## Complete disjoint orbits on the two-adic domain

This dimension statement has an ordinary two-adic dynamics interpretation independent of the ternary limiting law. Let \(x\in\mathbb Z_2\) have parity sequence \(W\), and for every \(\delta\ge1\) put \(x_\delta=3^{-\delta}(x+1)-1\). The parity conjugacy identifies source and symbolic cylinders isometrically: the first \(j\) letters specify a unique residue modulo \(2^j\), and conversely. [Bernstein and Lagarias, *The \(3x+1\) conjugacy map*](https://websites.umich.edu/~lagarias/doc/bernstein.pdf)

For **every nonrational** \(x\), a meeting \(T^a(x)=T^b(x_\delta)\), allowing unrelated clocks, first forces \(a=b\). If \(w,\beta\) are the respective words with odd grades \(f,u\), equality reads
\[
 \frac{3^f(x+1)+C_w}{2^a}
   =\frac{3^{u-\delta}(x+1)+C_\beta}{2^b}.
\]
Nonrationality forces equality of slopes; unique factorization gives \(a=b,\ u=f+\delta\), and then \(C_\beta=C_w\). Conversely, any same-length, same-offset, heavier \(\beta\) of grade \(f+\delta\) is the actual initial word of \(x_\delta\): the displayed affine equality gives an integral two-adic endpoint. Modulo \(2^a\), this is precisely the native parity class of \(\beta\), by oddness of its slope numerator. Thus every finite postprefix of \(x\) is maximal if and only if the entire orbit of \(x\) is disjoint from every entire orbit of \(x_\delta,\delta\ge1\).

Removing the countably many rationals preserves the full dimension proved above. Therefore the set of \(x\in\mathbb Z_2\) whose orbit is disjoint from **all** of these scaled companion orbits has Hausdorff dimension one and Haar measure zero. In particular a full-dimensional Haar-null set of two-adic \(m\)'s has the adjacent pair \(2m,2m+1\) with disjoint complete orbits. Take \(x=3m+2,\ x_1=m\). The images after one step are \(m,3m+2\); if the original adjacent pair met at unequal clocks involving a time zero, taking one further step would still give an intersection of these images. The affine change \(m\leftrightarrow x\) is an isometry. The proof deliberately removes every rational, including every ordinary positive integer. It measures the rigidity available from dyadic parity information alone and leaves ordinary pointwise merger open.
