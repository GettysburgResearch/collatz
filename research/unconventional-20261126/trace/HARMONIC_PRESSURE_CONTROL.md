# Maximal cylinder pressure and a square-integrable density do not fix the harmonic slope

**Status.** Explicit mathematical controls for the singular head in [the Dirichlet charge theorem](DIRICHLET_CHARGE.md). These examples have ternary cylinder martingales, with no Syracuse stationarity or branch identity assumed.

There are two probability densities on \(\mathbb Z_3\), both lower semicontinuous, square-integrable, and uniformly positive on the units (and zero on the nonunits), whose depth-\(k\) conditional densities have maximal growth rate exactly \(3/2\). The maximum for both can be attained on the cylinder of \(-1\) at every depth. One has bounded centered harmonic head \(B_k\); the other has \(B_k=\alpha k+O(1)\) with \(\alpha>0\).

Write \(r=3/2\). Start at \(i=i_0\) large enough to choose a positive odd \(a_i\equiv1\pmod3\) with \(r^i\le a_i<r^i+6<2\cdot3^i\). Such a representative occurs within six integers. Define
\[
 N(z)=\sum_{i\ge i_0} r^i\mathbf1_{z\equiv-1\ (3^i)},\qquad
 P(z)=\sum_{i\ge i_0} a_i\mathbf1_{z\equiv a_i\ (3^i)} .
\]
Each sum is lower semicontinuous, and its \(L^2\) norm is finite by the triangle inequality and \(\sum r^i3^{-i/2}<\infty\). Infinite values on a Haar-null set are allowed for a density. For a fixed sufficiently large constant \(A\), normalize the two functions \(\mathbf1_{3\nmid z}+AN(z)\) and \(\mathbf1_{3\nmid z}+AN(z)+P(z)\) by their Haar means.

For either sum, the depth-\(k\) conditional expectation has supremum \(O(r^k)\): terms through \(k\) cost at most a geometric sum, and each term \(i>k\) contributes at most \(O(r^i 3^{k-i})\). The negative spikes are nested and achieve the corresponding lower bound \(\gg r^k\) on the cylinder of \(-1\). The positive spikes lie in a different unit class and are bounded above by a common constant times the maximum of the negative ones (term by term before normalization). Choose \(A\) larger than that constant. Hence the maximum remains on the cylinder of \(-1\), even in the second example. This also handles \(k<i_0\) by the projected tail estimate, or enlarging \(A\) for finitely many indices.

For a bounded finite-level function \(g\), define
\[
 \mathcal L(g)=\sum_{a>0\ {\rm odd}}[g(a)-\textstyle\int g]/a .
\]
For a single cylinder of modulus \(q=3^j\), let \(t\) be its unique positive odd representative at most \(2q\). Then
\[
 \mathcal L(\mathbf1_{t\ (q)})=\frac1t+O\!\left(\frac{1+\log q}{q}\right),  \tag{1}
\]
with an absolute constant. The first block supplies \(1/t\) minus \(q^{-1}\) times its odd harmonic sum. On the tail the centered indicator has uniformly bounded partial sums, so summation by parts costs \(O(1/q)\).

At depth \(k\) all negative spike contributions together are bounded: the representative is \(2\cdot3^{\min(i,k)}-1\), and the extra factor for \(i>k\) is \(3^{k-i}\). Formula (1) bounds their sum by \(O(\sum_i(i+1)r^i 3^{-i})\). Thus the first normalized density has bounded \(B_k\).

For \(i\le k\) each positive spike contributes \(1+O((i+1)r^i3^{-i})\), by (1). Their sum is \(k+O(1)\). For \(i>k\), the total errors from (1) are again summable. If \(a_i\le2\cdot3^k\), its representative at depth \(k\) is \(a_i\), giving main term exactly \(3^{k-i}\). For the remaining \(i\) bound the reciprocal representative by one. Such indices satisfy \(i\ge k\log_r3-O(1)\), and their main terms sum to at most a constant times
\[
 3^k(r/3)^{k\log_r3}.
\]
This decreases exponentially since \(r^2<3\). Applying the finite-dimensional linear functional \(\mathcal L\) to the projected sums is justified at each fixed \(k\) by uniform convergence of their projected tails. The positive spikes therefore contribute \(k+O(1)\), and normalization multiplies that slope by the reciprocal of the second Haar mean.

The same maximal norm exponent and even strong \(L^2\) control are consistent with different values of the harmonic slope. O15 proves more about an actual family of transfer operators, including a stationary inverse entropy dichotomy. The examples refute an inference from maximal growth and Haar integrability alone; they do not test the full Syracuse stationarity equation or rule out a new use of O15's finer arithmetic information.
