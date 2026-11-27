# A limiting law for the first smaller meeting on a prescribed postpeak word

Let \(T(2a)=a,\ T(2a+1)=3a+2\). A source \(n\) is protected through its clock \(d\) if no \(m<n,\ m>0\), ever visits any of \(n,Tn,\ldots,T^dn\). Equivalently, no such \(m\) ever visits \(T^dn\). An earlier visitor can follow the original orbit to that endpoint.

Fix a word \(w\) of \(t\) shortcut letters, with \(f\) odd and \(q=t-f\) even. Write \(2^t T_w(x)=3^f x+A_w\) formally and \(C_w=A_w-3^f\). Suppose \(w\) is maximal among words of length \(t\) with its signed offset \(C_w\). Its **deficit set** is
\[
 D_w=\{f-\operatorname{wt}(\beta):|\beta|=t,\ C_\beta=C_w\}.
\]
It is finite and contains zero. Define \(p_{H,w}\) as the natural density, relative to the dyadic cylinder \(O^Hw\), of protection through clock \(H+t\). The [companion result](../allclock/POSTPEAK_VISITORS.md) gives existence for sufficiently large \(H\). This note identifies its limit and exhibits two limiting laws separated by more than one percentage point.

## The limit and a rate

Use normalized Haar measure \(\pi\) on \(\mathbb Z_3\). Let \(G(y)\) be the supremum of \(3^a/2^d\) over finite legal reverse shortcut words from \(y\), where \(a\) counts odds and \(d\) counts all steps. The empty word is allowed. Write \(S(M)=M/2\) for positive even \(M\) and \(S(M)=(3M-1)/2\) for positive odd \(M\). Consider only **odd** positive \(M\) that reach 1. Write \(a_M,\ell_M\) for odd and even counts **up to the first visit**. Include \(M=1\) with both counts zero. For every finite \(D\subseteq\mathbb N\), put
\[
 p(D)=\pi\left\{N:
   G\!\left(2^{\ell_M+\delta}(N+1)-M\right)
            \le 2^{\ell_M+\delta}\quad
   \text{for every such }M,\ \delta\in D\right\}.
\]
For maximal \(w\) and all sufficiently large \(H\),
\[
\begin{split}
 p(D_w)-5(3/2)^f4^q2^{-L}
 &\le p_{H,w}
 \le p(D_w)+\tfrac23\,2^{-\lfloor H/2\rfloor},\\
 L&=\left\lfloor (2H-2q-t-5)/4\right\rfloor .
\end{split}                                                    \tag{1}
\]
In particular \(p_{H,w}=p(D_w)+O_w(2^{-H/2})\). The common-scale count gives \(p(D_w)\ge284051/829440>1/3\) for every maximal word. With \(N=0\bmod3\) imposed in both probabilities, the same absolute errors apply and the limiting mass is at least \(1041139/4147200>1/4\), using the full cylinder as denominator. Nonmaximal words instead have \(p_{H,w}=0\) for \(H>t\), by the explicit smaller source in the companion note.

Weaver 178/v1, §7, Theorem 4 already identifies the pure-ascent limit \(p(\{0\})>0.510269713938\) using the first-hit reflected origins and develops the squared-gain bound. Its §8 constructs other positive-density families with late first meetings and prescribes independent future bits. Our conclusions concern the individual postpeak cylinder, its complete offset-deficit set, estimate (1), and the quantitative separation below. The transfer to ordinary integer densities uses Weaver 177/v1, §8 (3). [Weaver 178/v1 §§2,7–9](https://rstation.ai/problems/collatz/papers/178/v1) · [Weaver 177/v1 §8](https://rstation.ai/problems/collatz/papers/177/v1) · [Common-scale lower bound](../../../root/phase5/COMMON_PROTECTION.md)

### Reduction to native signed stops

Set \(h=H+f\), \(g_*=3^h/2^{H+t}\) and \(R=C_w/2^t\). For \(H\ge6q+3\), the pointwise cone excludes all smaller physical visitors with at most \(h\) odd steps. A word with more odds cannot tie \(g_*\). For a fixed deadline, where \(Y=R+g_*(n+1)\), a legal reverse word of gain \(g>g_*\) has a positive source \(<n\) for all sufficiently large \(n\); one with \(g<g_*\) has source \(>n\). This follows from the affine source \(Y/g-\text{constant}\). A legal word from an integer is an ordinary inverse walk. The finite classes in \(N=n\) have their Haar proportions on the dyadic cylinder, even after prescribing any fixed number of *additional outgoing binary bits*. The uniform-in-deadline long-arrival transfer in the companion note lets these finite events increase to their union. Consequently \(1-p_{H,w}\) equals exactly the Haar mass of some legal higher-grade word of gain strictly above \(g_*\). The same equality holds after a fixed further dyadic restriction. [Pointwise cone](../../../root/phase4/MIRROR_ENERGY.md) · [Transfer](../allclock/POSTPEAK_VISITORS.md)

Stop the reverse path at its \(h\)-th odd inverse and let \(\ell\) count evens already taken. Its legality is determined at the signed target \(R\). Read the first \(t\) reversals as a chronological forward word \(\beta\) of weight \(u\), and put \(r=t-u\). For \(h>t\), these reversals end at an ordinary signed integer \(z_0=(C_w-A_\beta)/3^u\), by ternary legality and cancellation of \(2^t\). The remaining signed prefix in forward order has endpoints \(z_*,z_0\), odd count \(p=h-u\), even count \(\ell-r\), and clock \(h+\ell-t\). Its initial letter is odd because the reverse path stopped just after the required odd inverse. The actual stopped source in ternary coordinates is
\[
 Z=z_*+2^{\ell-q}(N+1).
\]
The threshold for a profitable continuation is \(G(Z)>2^{\ell-q}\). When the threshold is at least one any such word has another odd step. If it is below one the empty continuation may pass the test; short stops below show no such case occurs in the specified range. Each \(Z\) is Haar-uniform as \(N\) varies.

When \(\ell\le L\), the signed energy trap forces \(z_0=-1\). Indeed \(|z_0|\le2\,3^r\), so its sufficient inequality is \(4(\ell-r)+7r+5\le2(h-u)\). This follows from \(4\ell+2q+t+5\le2H\), since \(r\le t\) and \(h-u=H+r-q\). The longer stops with \(z_0=-1\) obey the same algebra that follows. The Lean module proves the forced anchor, its actual physical scaling and single-origin injectivity for genuine stopped walks. The ternary word reduction and probability estimates here are written mathematics. [StoppedOrigins.lean](StoppedOrigins.lean) · [Signed energy](../../../root/phase4/MIRROR_ENERGY.md)

### Exact description of the stops at minus one

If \(z_0=-1\), then \(C_\beta=C_w\) and \(\delta=f-u\in D_w\). The signed prefix is the negative of a reflected path from an odd positive \(M=-z_*\) to 1, with \(\ell_M=\ell-r\) evens and \(H+\delta\) odds. Each step after its first arrival is the odd fixed loop at 1, so \(a_M\le H+\delta\). Conversely take \(\delta\in D_w\), a matching \(\beta\), and any \(M\) with \(a_M\le H+\delta\). Pad its first-hit reflected path with \(H+\delta-a_M\) odd fixed loops at 1. Its first letter is odd, including when \(M=1\) since \(H+\delta>0\). Its negative followed by \(\beta\) ends at \(R\) formally, and all reverse odd tests are ternarily legal: the formal forward \(\beta\) steps starting from \(-1\) have at worst dyadic denominators, hence are ternary integers. This gives exactly an admissible \(h\)-odd stop. Both the source and its cost depend only on \(M,\delta\):
\[
 Z=2^{\ell_M+\delta}(N+1)-M,\qquad g_*/g_{\rm stop}=2^{\ell_M+\delta}.
\]
Actual endpoints obtained by this construction are positive for sufficiently high physical sources at any fixed continuation deadline, as in the transfer above.

Only the origins with \(a_M>H+\delta\) can distinguish the constrained list from the list in \(p(D_w)\). For \(M>1\), remove the last even step \(2\to1\) of its first visit. The signed energy estimate ending at \(-2\) yields
\(400\,M^2 2^{a_M}\le450\,4^{\ell_M-1}\,4\), hence \(a_M\le2\ell_M\) by integrality. Also \(M\le2^{\ell_M}\), by reversing the path from 1; inverse odd steps never increase a positive reflected value. There are at most \(2^{\ell_M-1}\) odd choices when \(\ell_M\ge1\). The squared-gain bound \(\pi(G>b)\le b^{-2}\) gives total missing mass at most
\[
 \sum_{\delta\in D_w}4^{-\delta}
 \sum_{\ell>\lfloor H/2\rfloor} 2^{\ell-1}4^{-\ell}
 \le\tfrac23\,2^{-\lfloor H/2\rfloor}.                     \tag{2}
\]
This proves the upper bound of (1).

### Counting remaining origins

For a length-\(t\) word with \(u\) odds and \(r=t-u\) evens, its \(i\)-th odd letter, numbered from zero, has position at most \(i+r\). Summing \(3^{u-1-i}\) times the corresponding powers of two gives \(0\le A_\beta\le2^r(3^u-2^u)\). Put \(s=f-u=r-q\), which can have either sign for these stops. From \(3^u z_0=C_w-A_\beta\), the upper bound on \(z_0/2^r\) is \((3/2)^s\). The lower bound is \(-1-3^{f-u}/2^r\ge-1-(3/2)^f\), using \(r\ge f-u\) when \(f-u\ge0\). Thus \(|z_0|\le2^r(1+(3/2)^f)\). Integer reverse steps in the signed prefix give
\[
             |z_*|\le2^\ell(1+(3/2)^f).
\]
At fixed \(\ell\), one \(z_*\) determines the whole stop. The clock \(h+\ell-t\) is fixed, so deterministic signed iteration determines \(z_0,p\), then \(u=h-p\), then \(A_\beta=C_w-3^u z_0\). The weight and intercept at fixed length specify a unique word by parity decoding. This shows that at most \(5(3/2)^f2^\ell\) stops are available without counting the tail word a second time.

For \(\ell>L\ge q\), any continuation therefore costs at most \(4^{q-\ell}\) in Haar measure per stop. Their sum is at most \(5(3/2)^f4^q2^{-L}\). All stops outside the exact minus-one list lie here. This proves the lower bound of (1). The proof requires \(H\ge6q+3,\ h>t,\ L\ge q\). In particular the earlier maximal-word \(>1/3\) and zero-class \(>1/4\) conclusions hold throughout \(H\ge400,\ 6(t+1)\le H\). Indeed \(L\ge H/2-q/2-t/4-9/4\), and the base-two log of the error is at most \(5+11t/4-H/2\le5-H/24\). At \(H\ge400\) this is below \(-11\), whose error fits both strict margins.

## A physical first-meeting atom exceeding one percent

The words \(E\) and \(EO\) are maximal, with deficit sets \(\{0\}\) and \(\{0,1\}\) respectively. On \(N=60\bmod81\), the deficit-one origin \(M=1\) has \(Z=2N+1\), for which the reverse word \(EOOOO\) has gain \(81/32>2\). Consequently the entire ternary ball fails the deficit-one constraint.

The probability on this ball of failing some deficit-zero constraint is small. For \(\ell=0,M=1\), its target is a multiple of three and no odd inverse ever occurs. For \(\ell=2,M=3\), its target is 1 modulo three, forcing an initial reverse even, so up to four odd inverses every gain is at most \((3/2)^4/2<4\). For \(\ell\ge4\), the guard \(2^\ell\) already exceeds \((3/2)^4\). The remaining \(\ell=1,3\) have no origins. Thus every possible productive deficit-zero continuation here admits a stop at its fourth odd inverse.

Let \(S_r(z)\) be the sum of squared gains of legal routes stopped at the \(r\)-th odd inverse, with \(z\) given modulo \(3^r\), and \(S_0=1\). Conditional on that class each stopped endpoint is Haar-uniform. The squared-gain bound makes the conditional charge for a guard \(2^\ell\) at most \(4^{-\ell}S_4(z)\). The initial \(e\) even inverses followed by one odd contribute \(9/4^{e+1}\) to the factor in \(S_r\), with child \((2^{e+1}z-1)/3\) when integral. The legality and child modulo \(3^{r-1}\) repeat with period \(2\cdot3^{r-1}\) in \(e\). Summing each geometric progression gives exact rational arithmetic. The allowed \(e\)'s have at most one parity, so \(S_r\le(12/5)^r\).

Through \(\ell=7\), the complete odd origin rows are \(\{1\},\varnothing,\{3\},\varnothing,\{11\},\{15\},\{29,43\},\{39,59\}\). The finite rational charge summed over these rows is less than \(0.010922\). The tail \(\ell\ge8\) costs at most \((12/5)^4/256=81/625\), by \(2^{\ell-1}\) odd candidates per row. Dividing the resulting protection mass by 81 gives
\[
 p(\{0\})-p(\{0,1\})\ \ge\
 \frac{6886830314415271160677244916120109}
      {649037107316853453566312041152510000}
 >0.01061084>\tfrac1{100}.
\]
The code regenerates the finite origin list by deterministic iteration, computes every geometric sum as a rational, and checks the strict margin. [Exact checker](check_stopped.py) · [Output](CONTROLS.txt) · [Kernel-checked origin inventories](../../../root/phase5/SignedOrigins.lean)

On the physical dyadic cylinder \(O^HEO\), protection through \(H+1\) has the same density as on \(O^HE\), by the further-bit transfer above. Protection through \(H+2\) is its subevent. Their difference is exactly the density of a **first smaller-orbit meeting at clock \(H+2\)**, with arbitrary visitor clock. By (1) it tends to \(p(\{0\})-p(\{0,1\})\); thus it exceeds one percent of this specified cylinder for all sufficiently large \(H\). This identifies where a first ordinary meeting occurs on a subset of starts. The proof gives no universal first meeting and makes no assertion that the visitor converges.

## Replay

Run the Lean leaf with fresh compiled dependencies `ProtectedCone` and `MirrorEnergy`, and run `python3 check_stopped.py` or `python3 -O check_stopped.py`. The three listed Lean inventories in StoppedOrigins use exactly `propext`, `Classical.choice`, `Quot.sound`. The asserted limiting probabilities and gap are written results with an exact finite rational check, not kernel theorems.
