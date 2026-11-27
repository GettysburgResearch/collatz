# Positive integer traces of the tilted ternary Riesz potential

**PROPOSED.** Write \(\alpha_e=3/2^e\), \(\phi_e(z)=(3z+1)/2^e\), and \(\psi_e(y)=(2^ey-1)/3\). A gap \(e\ge1\) is legal at \(y\in\mathbb Z_3\) if \(2^ey\equiv1\bmod3\). Given \(1<t<2\), set \(W=\sum_e\alpha_e^t=3^t/(2^t-1)\) and \(p_e=\alpha_e^t/W\). These probabilities are geometric with ratio \(2^{-t}\). The unique stationary ternary probability \(\nu_t=\sum_ep_e(\phi_e)_*\nu_t\) is the law of the almost surely convergent affine series. In fact the coding converges at every infinite word, since every map contracts the ternary distance by exactly \(1/3\). This is the geometric Syracuse family studied by Leen and Weaver. The global entropy dimension and Haar singularity results for their family concern the entire measure; a specified positive integer can have a different local dimension. [Weaver, definitions and Theorem 1](https://rstation.ai/problems/collatz/papers/135/v1).

## The exact corrective singularity

For \(\beta>0\), put
\[
 I_\beta(y)=\int|y-z|_3^{-\beta}\,d\nu_t(z),\qquad
 (L_tf)(y)=\sum_{e\ {\rm legal}}\alpha_e^t f(\psi_e y).
\]
Stationarity gives the identity, including at infinite values,
\[
        3^\beta L_t I_\beta(y)+\sum_{e\ {\rm illegal}}\alpha_e^t
          = W I_\beta(y).                                             \tag{1}
\]
On a legal branch use \(|y-\phi_e z|_3=|\psi_e y-z|_3/3\), whereas on every illegal branch this distance is one. The illegal mass has a positive uniform lower bound depending on \(t\), since at least one of \(e=1,2\) is illegal. Thus \(I_\beta\) solves a strict additive drift inequality at \(\beta_*=\log_3 W\), and a strict multiplicative one for \(\beta>\beta_*\) wherever the values are finite. One has \(0<\beta_*<1\) since \((2^t-1)/3^{t-1}>1\) for \(1<t<2\): this follows from the strict concavity of \(\log(2^t-1)\) and equality at the two endpoints.

For \(k\ge1\) set \(A_{t,k}(y)=\sum_{|w|=k,\;y\in\phi_w(\mathbb Z_3)}\alpha_w^t\), multiplying the \(\alpha_e\)'s along the word (the outer letter is closest to the target). Every length-\(k\) cylinder is exactly a depth-\(k\) ball. Monotone shell summation gives
\[
 \nu_t(y+3^k\mathbb Z_3)= W^{-k}A_{t,k}(y),\qquad
 I_\beta(y)=1+(1-3^{-\beta})
                \sum_{k\ge1}(3^\beta/W)^k A_{t,k}(y).                 \tag{2}
\]
For a positive odd target \(y\), legal words are exactly the positive odd paths ending at \(y\). Indeed an integral inverse parent of a positive odd integer is again positive and odd, and its forward division exponent is specified exactly. For a source \(x\) at time \(k\),
\[
      \alpha_w=(y/x)\prod_{j<k}3U^jx/(3U^jx+1).
\]
The product is in \([c,1]\) on every finite simple path, with an absolute \(c>0\) from the simple-path reciprocal packing bound. A first arrival is simple up to its destination. For a nonperiodic target, each source has at most one contributing depth. For a periodic target of odd period \(L\), all additional visits repeat the cycle with its gain \(\rho=\prod_{\rm cycle}3z/(3z+1)<1\). Consequently \(I_{\beta_*}(y)<\infty\) at **every** positive odd target, with
\[
 \sum_{k\ge0} A_{t,k}(y)
   \le y^t\!\sum_{x\ {\rm odd}}x^{-t}
        \begin{cases}
           1,&y\ {\rm nonperiodic},\\
           (1-\rho^t)^{-1},&y\ {\rm periodic}.
        \end{cases}                                                    \tag{3}
\]
Here \(A_{t,0}=1\). Formula (3) needs no first-hit time estimate. See [packing and the ordinary transport](ORDINARY_HARDY.md). The squared-gain endpoint \(t=2\) at integer roots is related to [Weaver, Paper 178](https://rstation.ai/problems/collatz/papers/178/v1).

A strict gain in local dimension above \(\beta_*\) has a precise arithmetical cost. For each fixed positive odd \(y\), the following are equivalent:

1. Some \(I_\beta(y)\) is finite with \(\beta>\beta_*\).
2. \(\liminf_{k\to\infty}[-\log \nu_t(y+3^k\mathbb Z_3)]/(k\log3)>\beta_*\), with zero cylinder mass assigned infinite information.
3. Every positive odd \(x\) reaching this \(y\) has first odd hitting time \(\tau_y(x)\le C_y\log(2x)\) for a finite \(C_y\).

For the first two implications use (2), choosing a smaller strict exponent when necessary. If \(I_\beta(y)<\infty\), a single first-hit term with \(\tau=\tau_y(x)\) gives
\[
       (3^\beta/W)^\tau(cy/x)^t\le C_{\beta,y},
\]
and hence the clock bound. Conversely choose \(a>1\) so close to one that \(C_y\log a<t-1\), and in the periodic case also \(a^L\rho^t<1\). The sum of the first-hit contributions at multiplier \(a\) is at most \(y^t\sum_x(2x)^{C_y\log a}x^{-t}<\infty\). Later laps contribute only the finite geometric factor \((1-a^L\rho^t)^{-1}\). Taking \(3^\beta/W=a\) proves the converse. In particular whether there is a strictly improved ordinary local dimension is independent of the choice of \(t\) in this interval. At a nonunit target there are no positive-depth words, and the clock property is immediate. The argument concerns ordinary points of a fixed stochastic law, without identifying them with Haar-typical points.

## Growth required by an escaping spine

Set \(s=2-t\), \(Bf(y)=\sum_{e\ {\rm legal}}\alpha_e^2 f(\psi_e y)\) on positive odd integers. For \(H(y)=y^s I_{\beta_*}(y)\), (1) gives an unconditionally finite function with
\[
       (BH)(y)\le H(y)-c_t y^s.                                       \tag{4}
\]
Here \(\psi_e(y)\le y/\alpha_e\), and (1) supplies the uniform subtracted mass. On an escaping path from a fixed \(x\), however, (2) and the lower packing bound force \(H(U^k x)\ge c_{t,x}(U^kx)^2\). The stationary conformal mass \(m_y=P(y)^{-2}\) therefore has \(\sum_y m_yH(y)=\infty\) on that component. Summing (4) by subtracting two infinite quantities would incorrectly exclude the spine.

More generally a positive comparison \(c x^s\le H(x)\le Cx^a\) with \(a<1\), \(s\ge0\), satisfying \(BH\le\lambda H\) for \(\lambda\le1\), would force along every simple odd segment \(U^k x=y\)
\[
          y^{2-a}\ \le C'\lambda^k x^{2-s}.                           \tag{5}
\]
A single inverse term yields \(H(y)\ge\lambda^{-k}\alpha_w^2H(x)\). Packing proves (5). Removing repeated laps shows that the maximal accelerated height of every orbit would be \(O(x^{(2-s)/(2-a)})\), with exponent strictly less than two. The shortcut maximal height has the same power bound up to an absolute factor, since between consecutive odd states it is at most \((3x+1)/2\) at the first step from the preceding odd state \(x\). The true family starting at \(2^k-1\) visits \(2\cdot3^{k-1}-1\) after \(k-1\) odd rises, forcing this exponent at least \(\log_2 3\). When \(\lambda<1\), taking \(k\)-th roots in (5) on this family in fact gives the necessary \(\lambda\ge 3^{2-a}/2^{2-s}\). The standard stochastic model predicts a maximum-excursion exponent of two. This prediction places the global comparison in (5) beyond the expected power bound, but it does not refute it for the integer map. [Kontorovich–Lagarias, §§2.6 and 4](https://arxiv.org/abs/0910.1944).

The correction in (1) sums the propagated singularities of all branches with the correct weights. The remaining obstacle is its growth on the diagonal, including precisely the ordinary paths from fixed sources in (2).
