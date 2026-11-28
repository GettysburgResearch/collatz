# Successive positive targets and the entire alternative-parent budget

Consider a supplied positive odd source \(x\) on an escaping orbit. Write \(y_j=U^j x,\ e_{j+1}=v_2(3y_j+1)\). In the stationary tilted gap law \(p_e=3/4^e\), let \(w_j=(e_j,\ldots,e_1)\), in inverse chronological order, and \(p(w_j)=\prod_{i\le j}p_{e_i}\). Write \(\sigma_j(y)=\sigma(y+3^j\mathbb Z_3)\); \(\sigma_0=1\). Define the finite posterior ratio
\[
                      R_j=\frac{\sigma_j(y_j)}{p(w_j)} .
\]
Then \(1=R_0\le R_1\le\cdots\le R_\infty<\infty\), with \(R_\infty\ll x^2\) using the uniform simple-path correction bound. Indeed Weaver's ordinary trace gives exactly
\[
      R_j=\frac{x^2}{f_j(x)^2}
                   \sum_{U^j v=y_j}\frac{f_j(v)^2}{v^2}.
\]
The sum of the inverse squares is uniformly bounded, and \(f_j(x)\) stays above an absolute positive constant on this simple path. Monotonicity follows from stationarity: in the one-step recursion for \(\sigma_{j+1}(y_{j+1})\) the actual parent \(y_j\) contributes \(p_{e_{j+1}}\sigma_j(y_j)\). For every \(k\ge1\), conditioning an iid tilted word on the depth \(j+k\) residue of \(y_{j+k}\), the probability its **first \(k\) inverse letters** are precisely the true segment \((e_{j+k},\ldots,e_{j+1})\) is
\[
                   \frac{R_j}{R_{j+k}}\longrightarrow1
                    \quad\text{uniformly over every } k\ge1.           \tag{1}
\]
Its numerator before cancellation is \(p(e_{j+k},\ldots,e_{j+1})\sigma_j(y_j)\). This is a successive-target statement about the full exact posterior at the usual tilted law, without averaging the ray in its source integer. [Weaver, original tilted row and exact word probabilities](https://rstation.ai/problems/collatz/papers/9)

Let \(S(y)=4y+1\) on \(\mathbb Z_3\). Every true parent of exponent \(e\) has higher-exponent alternatives \(S^h(y)\) of exponent \(e+2h\). Put
\[
       A_j(y)=\sum_{h\ge1}16^{-h}\frac{\sigma_j(S^hy)}{\sigma_j(y)}
\]
at positive-mass residues, and zero elsewhere. Thus \(R_{j+1}/R_j\ge1+A_j(y_j)\), including the alternatives even when their positive-integer row is zero. Expanding the finite product of \(1+A_j\) gives the summable necessary condition
\[
                \sum_{j\ge0} A_j(y_j)\le R_\infty-1 .                 \tag{2}
\]
In particular the ratios for the single fixed affine comparison \(y\mapsto4y+1\) are summable on the actual sequence. When \(e\ge3\), the smaller legal exponents contribute their corresponding nonnegative terms to the same full ratio as well.

## What the independent tilted coding theorem implies

For iid gaps \(E_i\) under this same law, with coded residue \(Z\bmod3^m\), put \(h_m=H(E_1\mid Z\bmod3^m)\) in nats. The bounded full conditional word entropy in Weaver's Theorem 5 gives
\[
                         \sum_{m\ge1}h_m<\infty.                      \tag{3}
\]
Indeed after conditioning on the first letters, invert their affine branches; every supplied letter lowers the remaining ternary precision by exactly one, and the iid suffix has its original law. The chain rule thus gives \(H((E_1,\ldots,E_k)\mid Z\bmod3^k)=\sum_{m=1}^k h_m\). More generally \(H((E_1,\ldots,E_k)\mid Z\bmod3^{j+k})=\sum_{m=j+1}^{j+k}h_m\), tending to zero uniformly in the additional \(k\). This sharpens the comparison to finite-depth affine-translate singularity. [Weaver, Theorem 5 and the full-value decoding argument after Corollary 6](https://rstation.ai/problems/collatz/papers/9) · [Exact affine overlap classification](../../machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md)

In the entropy of the first digit at depth \(j+1\), retain just paths whose digit is \(1\). Their output has the form \(F_1(y)=(3y+1)/2\) modulo \(3^{j+1}\) for an independent depth-\(j\) residue with law \(\sigma_j\). The other possible first digits are \(1+2h\) with suffix residue \(S^h(y)\), since \(F_{1+2h}(S^hy)=F_1(y)\). The conditional probability of digit one is exactly \(1/(1+A_j(y))\). Consequently
\[
               p_1\sum_{j\ge0}\mathbb E_{\sigma_j}
                         \log(1+A_j)\le\sum_{m\ge1}h_m<\infty .       \tag{4}
\]
For **any** moving random residues \(Z_j\) whose individual marginals are \(\sigma_j\), without any independence across \(j\), Tonelli gives \(\sum_j\log(1+A_j(Z_j))<\infty\) almost surely. Then \(\sum_j A_j(Z_j)<\infty\) almost surely, since the terms tend to zero and each is finite. The actual escaping states in (2) have no asserted tilted marginal. Equations (2) and (4) explain the direction of the comparison: the full coding entropy also enforces summable alternative-parent likelihood on its own typical population. Turning that separation into a positive lower budget on the actual moving integers would need an additional ordinary arithmetic estimate.

## Distinguishing the three ordinary forward behaviors

The same \(R_j(x)\) is defined at every supplied positive odd \(x\). The following thresholds concern that one physical orbit. Its behavior on escape is bounded by (2). If \(x\) reaches any cycle other than the cycle through one, then
\[
                   \limsup_j R_j(x)^{1/j}\le(10/9)^2<4/3.
\]
Indeed the ordinary trace is \(x^2 f_j(x)^{-2}\) times a sum bounded by \(\sum_v v^{-2}\); on that cycle the minimum odd vertex exceeds one and every inverse correction factor \(1+1/(3u)\) is at most \(10/9\).

If \(x\) reaches one at odd depth \(j_0\), its subsequent true letters are all \(2\), so \(p(w_j)=c_x(3/16)^j\) there. In the central row \(U^j v=1,\ S_j(v)=2j\), at least \(c(4/3)^j/\sqrt j\) distinct positive odd sources have the indicated exact \(j\)-letter words. Distinct sources give distinct words because a fixed word and endpoint determine the source. Each word has tilted probability \((3/16)^j\). Summing proves
\[
                  R_j(x)\gg_x (4/3)^j/\sqrt j
                   \qquad (j\text{ sufficiently large}).
\]
Thus reaching one is equivalent to \(\limsup R_j(x)^{1/j}\ge4/3\), and equally to the same bound on the liminf. These are asymptotic tests on observed true letters. The central inverse row is an imported quantitative lower bound at the fixed target one. [Window and consecutive-block theorem, first assertion](../../machinery/phase2/COUNTED_BLOCKS_AND_PROGRESSIONS.md)

The same row theorem gives a physical distinction without stationary weights. Call two shortcut sources counted-fused if at some common time their states and cumulative odd counts agree. If \(x\) reaches one at shortcut time \(s_0\) and odd count \(j_0\), it reaches one again at every pair \((s,j)=(s_0+2k,j_0+k)\). Their difference \(s-2j\) is fixed, so these exact rows contain consecutive blocks of unbounded length. Every member of each block is counted-fused with \(x\). Conversely an escaping \(x\) has a **finite** counted-fusion class: on a simple forward trajectory define \(P(x)=x/f_\infty(x)\), extending across even halvings. The identity \(P(x)=2^s3^{-j}P(T^sx)\) shows equal time, count and endpoint imply equal \(P\). Every class member is then a positive integer at most \(P(x)\). This distinction leaves the counted-fusion classes of possible other cycles open. [Correction identity and simple-path lower bound](../phase4/HARMONIC_SOURCE_PHASE.md)
