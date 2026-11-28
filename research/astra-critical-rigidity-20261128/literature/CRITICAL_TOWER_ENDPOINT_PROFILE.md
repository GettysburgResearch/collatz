# The critical endpoint profile for two powers of three

Let \(T\) be the shortcut map on rationals of odd denominator. Use either of the fixed towers \(X_n^\pm=c+M3^{\pm n}\), with \(c\in\mathbb Z\), \(M\) a positive integer, and discard any finitely many nonpositive ascending terms when desired. Set \(t=\lfloor\log_2 N\rfloor\) and let positive integers \(k=k(N)\) satisfy \(k/\sqrt t\to\lambda\), with \(0<\lambda<\infty\). Then for each tower,
\[
 \sup_{a\ge0}\left|
 \frac1N\#\{a\le n<a+N:T^t(X_n^\pm)\ne T^t(X_{n+k}^\pm)\}
                 -[2\Phi(\sqrt2\lambda)-1]\right|\ \longrightarrow0.      \tag{1}
\]
Here \(\Phi\) is the standard normal distribution function. These are actual numerical comparisons at the common deadline. The same profile at the two extremes is supplied by the [short-block and long-endpoint bounds](TERNARY_TOWER_SYNCHRONIZATION.md). At a positive finite critical parameter (1) concerns the two endpoints. It only upper bounds the probability of synchronous equality of the entire intervening block.

We first prove a moving-initial-state statement for Leen's fresh-bit process. A canonical state \((s,D)\) represents bases \(x,3^s x+D\). Let \(R\) be its first return to level zero and \(A\) its full canonical absorption time. Uniformly along all sequences with \(s/\sqrt t\to\lambda\) and \(|D|/3^s=O(1)\),
\[
                 \mathbb P_{s,D}(A>t)\longrightarrow
                                      2\Phi(\sqrt2\lambda)-1.            \tag{2}
\]
The proof uses Leen's original *uniform expected occupation* of the killed epoch chain and his exact holding formulas. The published fixed-state meander and fixed-state tail alone do not imply (2). [Leen, *Exact rates in Collatz synchronization*, Sections 4–5 and “Raw and coasted return moments”](https://doi.org/10.5281/zenodo.23268751) · [Leen, exact labelled cylinders](https://doi.org/10.5281/zenodo.23268755)

## From the uniform expected occupation to an ordinary clock law

First pass to an odd raw level with odd offset. At a positive level \(s\), the hold until an odd offset is at most \(e_s+G\) in stochastic order, where \(e_s=v_2(3^s-1)\le2+\log_2(s+1)\) and \(\Pr(G=i)=2^{-i-1}\), by the original holding law. Starting at even level, one further mixed direction step and one further hold suffice. These at most two initial holds cost \(o_{\mathbb P}(t)\) uniformly in the offset and change the level by at most one. For large \(t\) the moving initial height exceeds two, so this preparation cannot reach zero. The subsequent clock estimates are uniform in the possibly changed offset.

From an odd level with odd offset, let \(S_j\) be the ordinary simple symmetric walk of mixed directions, starting at that level and killed on its first hit of zero at direction \(K\). Let \(\sigma_j\) be the native clock to its \(j\)-th direction landing, using \(\sigma_K=R\) from this entrance. For every deterministic \(m=O(t)\),
\[
              [\sigma_{K\wedge m}-2(K\wedge m)]/t
                                  \ \longrightarrow0\quad\text{in probability}.       \tag{3}
\]
At the odd-level, odd-offset epochs before every other direction bit the chain is \(Z_v=(J_v,D_v)\) with raw level \(2J_v+1\); write \(\tau\) for its killing step. Its level increments are \(-1,0,1\) with probabilities \(1/4,1/2,1/4\) at \(J\ge1\); at zero it is killed with probability \(1/2\), stays or goes up with probability \(1/4\) each. Thus visits to zero before killing have a uniform geometric tail. The deterministic number of epochs which can contribute to (3) is \(m/2+O(1)\).

Here are the required estimates for the holding bias. At an ordinary odd-level epoch, \(\bar\eta(2J+1,D)\) is the conditional mean of the next even-level holding, setting the killed down-branch holding to zero. At \(J\ge1\), Leen's exact cap construction provides a bounded joint cylinder \(\psi_b(J,D)\), periodic in the level and odd offset, such that
\[
 \int\psi_b\,d\pi=0,\qquad
 |\bar\eta-1-\psi_b|\le f_b(J)=E(J)\boldsymbol1_{E(J)>b},\quad
 E(J)=3+v_2(J(J+1)).
\]
Here \(b\ge3\) is fixed, \(\pi\) is the product of Haar level and Haar odd offset, and the same cylinder formula extends to all modular residues of \(J\). At the actual integer boundary \(J=0\), the separate holding bias has absolute value at most one; the total difference with the bounded cylinder there is tight for fixed \(b\) by the geometric visit count. The original cap estimate, its Haar-odd mean and cylinder dependence are the formulas headed “Odd landings and even predictable means” and “cap error” in the exact-rates paper.

If \(f\) is any fixed bounded joint cylinder of \(\pi\)-mean zero, Leen's theorem “Uniform fixed-test expected occupation” states, with \(a_L(z)=\mathbb E_z(\tau\wedge L)\), that
\[
 \sup_z\frac1{a_L(z)}
      \left|\mathbb E_z\sum_{v<\tau\wedge L} f(Z_v)\right|=o_L(1).
\]
The supremum includes moving ordinary initial levels and every odd offset. Divide a deterministic horizon \(u=O(t)\) into blocks of \(L\) epochs and extend rewards by zero after killing. By the Markov property, each block has conditional expected sum of absolute magnitude at most \(L\,o_L(1)\). The centered block sums are martingale differences bounded by \(2L\|f\|_\infty\), with total variance \(O_f((t/L+1)L^2)\); one incomplete block costs \(O_f(L)\). Divide by \(t\), let \(t\to\infty\) then \(L\to\infty\). The stopped sum of \(\psi_b\) divided by \(t\) converges to zero in probability, uniformly in the starting law. This argument needs an ordinary weak law, without rare-event conditioning.

To remove the cap put \(f_b(0)=0\). Leen's elementary valuation count gives its mean \(a_b=(b+2)2^{3-b}\) over the positive integers and \(\sum_{j=1}^x(f_b(j)-a_b)=O_b(\log^2(x+2))\). Define \(g(0)=g(1)=g(\partial)=0\), \(g(j+1)-g(j)=4\sum_{i=1}^j(f_b(i)-a_b)\). The killed level kernel has drift \((P-I)g=f_b-a_b\) in its interior. At the zero boundary the discrepancy is bounded for fixed \(b\). In \(u=O(t)\) epochs, \(J_v\le J_0+u=O(t)\), so the corresponding stopped martingale has increments \(O_b(\log^2(t+2))\). Its variance divided by \(t^2\) tends to zero. Also \(|g(j)|=O_b((j+1)\log^2(j+2))\). The initial \(J_0=O(\sqrt t)\); coupling to the un-killed direction walk and the square-integrable maximal inequality show that before killing or \(u\), the maximum of \(J\) exceeds \(t^{3/4}\) with probability \(O(t^{-1/2})\). Both corrector endpoints are therefore \(o_{\mathbb P}(t)\). It follows that
\[
           \sum_{v<u\wedge\tau} f_b(J_v)\ \le\ a_b u+o_{\mathbb P,b}(t).
\]
Use the bounded-cylinder law at fixed \(b\), then let \(b\to\infty\). The complete sum of even-level predictable biases is \(o_{\mathbb P}(t)\).

Finally the centered odd-level holding increments have conditional variance two at each genuine odd landing, by averaging its preceding fair direction. The centered even-level holding increments have conditional variance \(O(\log^2(t+2))\) up to \(m\) directions, using the exact holding law at levels at most \(s+m\); a killed down-branch contributes zero with its specified conditional mean. Summing each martingale through the deterministic direction cutoff or killing gives \(o_{\mathbb P}(t)\). The initial odd-epoch holding is zero. The numbers of contributing even and odd holdings differ from the corresponding half-direction counts by at most one; a possible end holding is \(O_{\mathbb P}(\log(t+2))\), uniformly even when selected among these \(O(t)\) entries, by the geometric tail and a union bound. These estimates give (3), with the factor two coming from one direction step and one mean holding per mixed direction. The cap and holding conventions also cover a terminal hit on the first step of an epoch. Leen's exact-rates proof spells out this odd-offset entrance in “Fixed positive-level returns.”

## The return, the remaining absorption, and the arithmetic towers

For the direction walk started at \(s+O(1)\sim\lambda\sqrt t\), simple reflection and the binomial central limit theorem give \(\Pr(K>\lfloor vt\rfloor)\to 2\Phi(\lambda/\sqrt v)-1\) for each fixed \(v>0\). Apply (3) at \(m=\lfloor(1/2\pm\varepsilon)t\rfloor\), \(0<\varepsilon<1/2\). If \(K\) is below the lower cutoff, its return clock is at most \(t\) except on probability \(o(1)\). If it exceeds the upper cutoff, its return clock exceeds \(t\) except on probability \(o(1)\). The initial preparation costs \(o_{\mathbb P}(t)\) and can be absorbed in the fixed slack. Sending \(\varepsilon\downarrow0\) gives the profile in (2) for \(R\).

Apply Leen's raw first-return moment bound to the *original* state before the preparation. For some \(0<p<1\) and \(0<r<1\), the return offset \(U\) has \(\mathbb E|U|^p\le r^s|D/3^s|^p+C\). His “Remaining absorption from a scalar state” lemma then gives \(\Pr(A-R>\varepsilon t)\le C(1+\mathbb E|U|^p)/\sqrt{\varepsilon t}=o(1)\). Comparing with \(R\) at \((1-\varepsilon)t\) and using the continuous profile proves (2).

For a tower endpoint comparison orient the inputs as \(x=c+y,3^k x+(1-3^k)c\), with \(y=M3^n\) ascending and \(y=M3^{-(n+k)}\) descending. The two depth-\(d=v_2(M)+3\) cylinders and the period \(P_u=2^{u-v_2(M)-2}\) are those in the tower theorem. On each fixed initial cylinder the residual oriented base is Haar. If the two initial words have odd grades \(a,b\) and carries \(C_1,C_2\), the new level is \(s'=k+b-a\), positive before any orientation change for large \(t\). The new normalized offset is exactly
\[
 \frac{D'}{3^{s'}}=
   \frac{-3^a c(1-3^{-k})+C_2/3^{s'}-C_1}{2^d}.
\]
Both \(s'/\sqrt t\to\lambda\) and \(|D'|/3^{s'}=O_{c,M}(1)\) hold uniformly for those finitely many initial words, even as \(k\) varies. Equation (2) after these \(d\) dates gives the same survival profile on their union.

To transfer it at the full deadline take \(j=t-\lceil2\log_2(t+2)\rceil\). In any length-\(N\) exponent interval the canonical-survival fraction at \(j\) differs from its conditional Haar probability by at most \(P_j/N=o(1)\). For the *same* exponent gap \(k=k(N)\), the survival probabilities at \(j\) and \(t\) have the same limit by (2). Additional absorptions in the interval thus have fraction at most \((1+P_t/N)o(1)=o(1)\), using the exact finer residue period. The descending arm begins at index \(n+k\), which just shifts the exponent interval. The physical unequal-slope coincidences cost at most \(O_{c,M}(t+1)\) indices by equation (4) in the tower theorem, uniformly in the gap. This proves (1).
