# What selects the reciprocal moment at 1

The positive trace budget involves the individual-depth limit of the original geometric law. Even full pointwise harmonicity on ordinary odd integers, bounded comparability to this trace, any finite set of its point values, and any finite initial list of moments of its exit law at 1 do not select the reciprocal moment. There are positive bounded perturbations within the actual transient branches of 1 satisfying all these tests and taking different reciprocal moments. This shows where the depth selection of the genuine trace must enter a stationary uniqueness argument. The perturbed traces are auxiliary comparison functions.

Write \(M_y=h(y)\mu_y\) for the unnormalized canonical real fibre. Take the exit law \(E\) at 1 in [the first-return formula](FIRST_RETURN_POISSON.md). Its contribution \(E_e\) from the immediate transient unit parent \(z_e=(2^e-1)/3\), with \(A_e=3/2^e\), is the law of \(u=A_e(z_e-R_\infty)\) under the path mass \(A_e h(z_e)P_{h,z_e}\). This is a positive non-atomic measure in a fixed compact interval \([c,1]\) with \(c>0\). Non-atomicity follows from full lower real dimension of \(\mu_{z_e}\). There are infinitely many distinct such direct units, for instance \(e=6j+4\). Their predecessor trees are disjoint, so given any finite list of ordinary odd points choose one such tree disjoint from the list. [Canonical real fibres](REAL_FIBRE_AND_FRONT.md)

Fix \(N\ge0\). Let \(g\) on \([c,1]\) be the function \(u^{-1}\) minus its orthogonal projection in \(L^2(E_e)\) onto the real polynomials of degree at most \(N\). This continuous function satisfies
\[
 \int u^j g(u)\,dE_e=0\quad(0\le j\le N),\qquad
 \int u^{-1}g(u)\,dE_e=\int g(u)^2\,dE_e>0 .
\]
Indeed \(u^{-1}\) cannot equal such a polynomial on an infinite support in this positive interval. Choose nonzero \(\epsilon\) with \(|\epsilon|\|g\|_\infty<1/2\). For each unit vertex \(x\) in the selected tree let \(V(x)\) be the conditional expectation of \(1+\epsilon g(u)\) on the prefix from \(z_e\) to \(x\). At a unit of the tree that prefix is unique and has positive probability. Outside the tree set \(V=1\). One has \(V(z_e)=1\). The Markov property gives \(V(x)=\sum_{Uz=x}P_{h,x}(z)V(z)\) on its interior. The same identity holds off the tree because the only edge entering it from the root side leads to \(z_e\). Consequently \(\widetilde h=hV\) satisfies exactly the original stationary trace recursion at every positive odd integer, preserves the selected finite point data and has \(\tfrac12h\le\widetilde h\le\tfrac32h\). At nonunits both functions vanish. Changing values on the countable ordinary set also preserves all Haar integrals, including averages on all ternary cylinders, of any measurable ambient representative. This last observation concerns averages only.

On the selected exit branch the canonical transition probabilities for this new harmonic function telescope over a prefix to the original probabilities times its conditional tilt \(V(x)/V(z_e)\). The cylinder generating property, or the bounded martingale convergence theorem, identifies its full path law with the original law weighted by \(1+\epsilon g(u)\). All other exit branches and the waiting multiplier \(3/4\) at 1 retain their original laws. The resulting exit measure is
\[
 \widetilde E=E+\epsilon gE_e,\qquad
 \int u^j\,d\widetilde E=\int u^j\,dE\ (0\le j\le N),\qquad
 \int u^{-1}\,d\widetilde E-\int u^{-1}\,dE
        =\epsilon\|g\|^2_{L^2(E_e)} .
\]
The individual-depth finite geometric laws select exactly \(h\). They are an additional condition beyond the harmonic equations and finite data above. In particular this comparison does not vary the ordinary, intrinsic basin density of 1.
