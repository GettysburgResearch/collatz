# Randomizing the ternary coordinate above a positive-integer binary source

**Written implication from a hypothetical ordinary escape.** Fix \(1<s<2\), and use the shortcut transfer and Green measures of the [main argument](README.md). If a positive integer \(m\) escapes, there is a finite positive fixed measure on \(\mathbb Z_2\times\mathbb Z_3\) that dominates \(\delta_m\otimes m_3\), with \(m_3\) normalized ternary Haar probability. The entire ternary marginal is absolutely continuous. The conclusion assigns a full Haar law at the *specified positive binary fiber*.

Write \(y_i=T^i m\), \(d_i\) for the number of odd departures and \(g_i=3^{d_i}/2^i=P(y_i)/P(m)\). The corrected height and the uniform bound \(n\le P(n)\le K n\) on the escaping component are recalled in the main argument. Use a single uniform \(\eta\in\mathbb Z_3\), and define the coupled spine
\[
 (y_i,z_i),\qquad z_i=y_i+g_i\eta .
\]
The true forward branch at the binary integer \(y_i\) takes this point to \((y_{i+1},z_{i+1})\). In particular its inverse is always admissible.

The positive measures \(g_i^{-s}G_s(y_i,z_i)\) increase on removing the known inverse edge, exactly as in the all-odd spine construction. Each increment consists of \(g_i^{-s}\delta_{(y_i,z_i)}\) and the discounted Green measure at the remaining admissible branch, if present. The atom increments are summable, since \(g_i^{-s}\le P(m)^s y_i^{-s}\) and the \(y_i\) are distinct. After the first odd departure \(d_i\ge1\), so any other branch is admissible exactly when it is admissible at the ordinary target \(y_i\). Call its ordinary root \(b\), and let \(a\in\{1/2,3/2\}\) be its weight before taking the power \(s\). Its ternary coordinate is uniform on the ball about \(b\) of depth \(d_i\) for an even inverse, or \(d_i-1\) for an odd inverse. The Haar stopping identity in the main argument bounds the mean total Green mass there by \((1+M_s)H_s(b)\). This includes depth zero by \(H_s(b)\ge1\). Before the first odd departure there are finitely many increments, whose mean is finite by Haar change of variables on the whole ternary space or on the clopen odd domain.

It remains to sum these bounds on ordinary side roots. An inverse word from \(b\) reaching \(x\) has gain \(P(b)/P(x)\), with \(aP(b)=P(y_i)\). Its normalized contribution is exactly \((P(m)/P(x))^s\). Each actual ordinary \(x\) occurs at most once across the side trees: its forward trajectory first joins the injective spine on the indicated side edge. Each pre-join clock is unique. The side sum is therefore at most \(P(m)^s\zeta(s)\). Monotone convergence gives a finite limiting random measure almost surely and a finite averaged limit. The resolvent defect is \(g_i^{-s}\delta_{(y_i,z_i)}\to0\). The initial empty word gives the asserted Haar lower bound. Every finite-word endpoint in the construction is an invertible rational-affine image of Haar input restricted to a ternary cylinder, hence has absolutely continuous ternary law. Countable positive summation proves absolute continuity of the limiting ternary marginal.

For an ordinary \(x\) in this component, join \(y_i\) by its actual path after \(k\) steps with \(d\) odd departures. The grade \(j(x)=d_i-d\) does not depend on the joining site. On this word the inverse ternary endpoint is
\[
 x+\frac{P(x)}{P(m)}\eta,
 \qquad \frac{P(x)}{P(m)}=2^{k-i}3^{j(x)} .
\]
Integrality of this endpoint is sufficient for every earlier inverse test, because the entire forward affine path from an integral ternary point remains integral. The exact averaged measure on the positive binary fiber of \(x\) is
\[
 \left(\frac{P(m)}{P(x)}\right)^s
 3^{\min(j(x),0)}
 \;\operatorname{Unif}\big(x+3^{\max(j(x),0)}\mathbb Z_3\big).
 \tag{1}
\]
A binary descendant outside this ordinary component cannot be a positive integer, since any positive source reaching a spine point by the selected branches is a true ordinary predecessor. For ordinary points the binary coordinate gives a unique forward path, so formula (1) counts each fiber once. In the odd-map notation of the [posterior argument](POSTERIOR.md), the uniform grade reciprocal bound implies
\[
 \sum_{x\in C,\ j(x)\le0}\frac{3^{j(x)}}{P(x)}<\infty .
\]
Indeed grade is unchanged on even inverse towers, and each such tower contributes twice its odd root's reciprocal height. This is a finite critical reciprocal mass on the entire past half of the transverse construction. Inverse children with nonordinary binary coordinate still occur there, and removing them loses mass. The full diagonal critical current does not acquire this grading factor.

There is also an exact comparison of exponents. Let \(u>1\) and \(s-u>\theta\), where ordinary-orbit sparsity gives \(\#(O\cap[1,X])\ll X^\theta\) uniformly on injective positive orbits. For the ordinary fixed measure \(\lambda_s=\sum_{y\in C}P(y)^{-s}\delta_y\), Tonelli summation and the true forward source give
\[
 \int H_u\,d\lambda_s
 =\sum_{x\in C}P(x)^{-u}\sum_{i\ge0}P(T^ix)^{u-s}
 \ll_{s-u}\zeta(u).
\]
Dyadic summation of the sparsity estimate bounds the inner sum uniformly. At the matched exponent \(u=s\) every inner sum is infinite. Thus the cross-exponent estimate supplies integrability strictly off the matched line and pinpoints the loss at that line.

Averaging the nonordinary all-odd-spine examples of the main argument over their original full-measure set also gives an absolutely continuous ternary marginal when \(1<s<2\). The distinguishing hypothesis in the existence implication is the positive ordinary binary fiber.
