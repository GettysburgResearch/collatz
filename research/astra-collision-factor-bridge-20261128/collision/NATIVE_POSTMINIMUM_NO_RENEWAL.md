# The genuine post-minimum process has no fresh parity source

**Exact native observation and source-qualified entropy consequence.** This note examines a proposed way to improve the nonsummable component-boundary estimate: after a typical descent, restart a fair-parity excursion from the minimum and obtain another independent contraction. The proposed renewal step is false for the genuine map, already on the known component of one.

Throughout,

\[
 T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
 \quad m(n)=\min_{t\ge0}T^t(n),
 \quad\tau(n)=\min\{t:T^t(n)=m(n)\}.
\]

The minimum and its first occurrence exist for every positive ordinary source, including a hypothetical escaping source.

## 1. An exact deterministic identity

For every positive \(n\) and every \(j\ge0\),

\[
                         T^{\tau(n)+j}(n)=T^j(m(n)).             \tag{1}
\]

This is simply composition of genuine iterates. In particular the complete parity sequence after the first minimum is a deterministic function of that minimum. Once \(m\) is specified, there is no remaining source randomness in the future states.

Every attained global minimum is odd: an even positive minimum would be followed by its smaller half. Thus the first post-minimum bit is one for **every** positive source. There is also an exact two-bit distinction. If \(m>1\) and \(m\equiv1\pmod4\), two shortcut steps give \((3m+1)/4<m\), contradicting minimality. Consequently
\[
 \bigl(T^{\tau(n)}n\bmod2,\ T^{\tau(n)+1}n\bmod2\bigr)
 =\begin{cases}(1,0),&m(n)=1,\\(1,1),&m(n)>1.\end{cases}        \tag{1a}
\]
The **second** post-minimum bit is exactly the indicator that the source never reaches one. This is an identity using the actual all-time minimum. It is not a finite stopping test: the argument supplies no algorithm certifying that a currently observed record minimum is the global minimum.

For a concrete positive example, \(5\to8\to4\to2\to1\), after which the parity tape is exactly \(1,0,1,0,\ldots\). The same tape follows the first minimum of **every** source in the known component. A claimed conditional probability of one-half for the first post-minimum parity is therefore already wrong on this component: that parity is one with probability one.

This is compatible with Brownian descent before the minimum. Independence of a limiting descent process from the minimum label does not turn the deterministic future of that label into a new independent walk.

## 2. Proper minimum law gives an exact continuation mixture

Let \((p_m)_{m\ge1}\) be the proper natural-density minimum law supplied by [Leen's original manuscript](https://doi.org/10.5281/zenodo.23269488): the density of sources with minimum \(m\) is \(p_m\), and \(\sum_m p_m=1\). The inspected original TeX is pinned at SHA-256 `211bc4fe107b3821e510486be28cf53f69751f71394582822faf385d09561e37`. The source's analytic status remains external; no fresh full rebuild is claimed here.

For each fixed length \(L\), put

\[
 w_L(m)=\bigl(T^j(m)\bmod2\bigr)_{0\le j<L}.
\]

Then for every binary word \(w\) of that length, the limiting source proportion with post-minimum word \(w\) is exactly

\[
                 \sum_{m:w_L(m)=w}p_m.                          \tag{2}
\]

To justify the potentially infinite union, first retain minima at most a fixed \(R\). This is a finite union of minimum fibers. The discarded source proportion is at most \(1-\sum_{m\le R}p_m\), which tends to zero. Thus (2) follows without exchanging a growing word length with the source cutoff.

Consequently the limiting post-minimum process can be constructed by drawing **one** ordinary minimum \(M\) with law \(p\), then following its genuine deterministic orbit. This description applies jointly to every finite collection of post-minimum times.

Even without a quantitative tail bound, that limiting law is supported on the countable collection of tapes arising from ordinary minima. It is therefore singular to the fair Bernoulli tape law, which gives every fixed infinite tape mass zero. Properness of the minimum law is what justifies this countably supported limiting description; countability of each finite-source population alone would not justify it.

## 3. The whole limiting continuation has finite entropy

Leen's stated minimum-tail estimate is stronger than what is needed here: for every fixed \(A>0\),

\[
          \Pr(M>R)\ll_A(\log R)^{-A}\qquad(R\to\infty).
\]

Taking \(A=2\) and integrating the tail of \(\log M\) gives

\[
                             \mathbb E\log M<\infty.
\]

The comparison distribution \(q_m=1/(\zeta(2)m^2)\), together with the elementary entropy bound by cross-entropy, gives

\[
 H(M)=-\sum_m p_m\log p_m
       \le\log\zeta(2)+2\mathbb E\log M<\infty.                 \tag{3}
\]

Since \(w_L(M)\) is a deterministic function of \(M\),

\[
                       H(w_L(M))\le H(M)\quad\text{for all }L. \tag{4}
\]

The same conclusion holds conditionally on any fixed component having positive mass: its conditional minimum law still has finite logarithmic moment. This gives a uniform finite entropy bound for that component's entire family of finite post-minimum parity words. On the known component, the bound sharpens to zero because \(M=1\).

A fresh fair sequence would have entropy \(L\log2\). Equations (3)–(4) therefore exclude that proposed renewal description even without conditioning on the exact minimum. This statement concerns the limiting finite-word laws constructed in (2). It makes no unproved claim that finite-source entropies converge uniformly when \(L\) grows with the cutoff.

## 4. The native one-bit defect in the collision endpoint

Let \(b=p_1\) be the known component's natural density and let \(\eta\) be the limiting mean of the second post-minimum bit. Equation (1a) gives exactly
\[
                              \eta=1-b.                       \tag{5}
\]
The [prior median phase formula](../../astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md), together with the fact that genuine positive cycles have period at least two, implies
\[
 L_T(0)\le\frac{b^2+(1-b)^2}{8}
          =\frac18-\frac{\eta(1-\eta)}4.                       \tag{6}
\]
The known component has positive density under the named predecessor input. Thus any positive value of \(\eta\) makes the endpoint strictly smaller than one-eighth. Conversely \(\eta=0\), together with positive predecessor density for any hypothetical bad component, gives full convergence. This localizes the missing mass in one exact native bit; it does not evaluate that bit's mean. The Gaussian first-minimum clock is unchanged by adding one step and therefore cannot determine this unit-scale defect.

## 5. What a valid post-minimum estimate must control

For two minima \(m,r\), define the genuine continuation relation

\[
 K(m,r)=\mathbf1_{\{\exists a,b\ge0:\ T^a(m)=T^b(r)\}}.
\]

This is determined by their actual ordinary futures. The asynchronous component of a source is the component of its minimum. Consequently the two-independent-source probability of sharing a component is the absolutely convergent mixture

\[
                         Q=\sum_{m,r}p_mp_rK(m,r).              \tag{7}
\]

The same finite-minimum truncation proves (7). This is an exact description of the remaining data, not an evaluation of them. Finite merger certificates prove individual entries equal to one; absence of a currently found certificate does not prove an entry zero.

The synchronous median statistic additionally needs the genuine cycle periods and arrival phases, as the prior phase-dispersion formula shows. Those quantities also belong to the future of the selected ordinary minima. The independently reviewed edited-map example is one illustration of how much stopped data can leave unspecified, but the no-renewal statement (1) is entirely native and needs no edited map.

Thus the attempted additional fair excursion after a minimum cannot supply a summable boundary upper bound. A valid improvement would have to control the seed-specific continuation relation, or introduce an auxiliary random process with proved ordinary label transport and a quantitative return mechanism. The Gaussian descent and proper minimum law do not by themselves provide either input. No such closing theorem is proved in this note.

## 6. Finite native kernel

[NativeMinimum.lean](NativeMinimum.lean) has five public roots. It proves oddness from one-step non-descent; the exact local classification
\[
 m\le Tm\ \text{and}\ m\le T^2m
       \quad\Longleftrightarrow\quad m=1\ \text{or}\ m\equiv3\pmod4
 \qquad(m>0);
\]
the next parity of a true minimum; the deterministic continuation identity; and equivalence between a zero second post-minimum bit and convergence of the original source. The last statement explicitly assumes a positive attained value \(m=T^a n\) and the all-time lower bound \(m\le T^t n\) for every \(t\). It does not supply or decide that premise.

All five roots were freshly compiled and imported into a separate complete root/axiom audit using Lean 4.34.1 and pinned Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The only reported axioms are `Quot.sound` and `propext`. The [receipt](../../../reports/astra-collision-factor-bridge-20261128/collision/native-minimum-lean.json) and [runner](check_native_minimum.py) record exact hashes and scope. Cached pinned dependencies were reused; no cold rebuild or independent LeanChecker replay is claimed. The limiting mixture, entropy calculation and phase-defect inequality remain written and source-qualified. The mean \(\eta=0\) needed for the full proof remains unproved.
