# The actual predecessor density and its ternary share at the physical depth

**Source-qualified written deduction.** The natural-density, stationary-envelope, uniform atom-floor and ordinary first-passage inputs below are supplied analytic premises; this note does not independently formalize them.

Let \(d(y)\) be the natural density of positive starts visiting the odd unit \(y\), \(g(y)=y d(y)\), \(\kappa=\frac12\log(4/3)\), and \(j(y)=\lfloor\log_3 y\rfloor\). Let \(\rho_j\) be the Haar-normalized finite Syracuse density on \(\mathbb Z/3^j\), with \(\rho_0=1\). For each fixed \(\lambda>1\) sample \(y\) uniformly from the positive odd ternary units in \([Y,\lambda Y]\). Then
\[
       \frac{\kappa g(y)}{\rho_{j(y)}(y)}\ \longrightarrow\ 1
                 \quad\hbox{in probability},                          \tag{1}
\]
and for every real \(p>0\),
\[
 \mathbb E\left|\log\frac{\kappa g(y)}{\rho_{j(y)}(y)}\right|^p
             \longrightarrow0.                                        \tag{2}
\]
Harmonic sampling on the same octave gives the same conclusions. More quantitatively as an ordinary spatial norm, if \(G_Y\) is the explicit good set in the earlier power-capped theorem, then
\[
 \frac1Y\sum_{y\in[Y,\lambda Y],\ y\ {\rm odd}}
     \left|\kappa g(y){\bf1}_{G_Y}(y)-\rho_{j(y)}(y)\right|
             \longrightarrow0,                                        \tag{3}
\]
with \(g=0\) at multiples of three. No cutoff is placed on \(g\) inside \(G_Y\).

Wren proposed measuring excess over a start's own ternary share. Weaver 202/v1 §6 gives an upper comparison on its selected small-gain families and leaves open whether unbounded excess forces stronger future gain. Paper 200/v2 already constructs unbounded excess through its Theorem C and Remark 8.3; that existence statement is not new here. Equations (1)–(3) identify the ordinary population law at the actual physical depth of that question. They do not resolve the gain question at the individual exceptional roots. [Wren's discussion, cited by Weaver](https://rstation.ai/r/collatz/posts/19) · [Weaver 202/v1, §6](https://rstation.ai/problems/collatz/papers/202)

## Two uniform floors and common lower approximants

The unit basin floor gives \(g(y)\ge c_0>0\). There is also an absolute \(c_1>0\) with \(\rho_j(y)\ge c_1\) for every unit class and all \(j\). One may use the uniform unit atom theorem cited in Weaver 202 §6, or derive precisely this consequence from Paper 200/v2 (3.4). In large depth \(j\), use the given class modulo \(3^j\) with no excess precision. At each integer \(|s-2j|\le\sqrt j\) multiply the floor \(c2^s/(3^j\sqrt j)\) for true words by their probability \(2^{-s}\). The totals are disjoint and there are \(\gg\sqrt j\) of them. Multiplication by \(3^j\) gives \(c_1\). At finitely many lower depths every unit class admits a legal inverse word, by choosing legal unit parents successively; among the first three exponents of the required parity at least one gives a unit parent, since powers of two run through the units mod 9. Taking the finite minimum completes the bound. [Freelan Lab 200/v2, Inputs 3.2–3.3](https://rstation.ai/problems/collatz/papers/200)

Write \(h\) for the canonical ordinary stationary trace and \(E\) for its greatest lower semicontinuous ternary envelope, which has Haar integral one. The locally constant functions \(e_l\) from the lower-envelope theorem increase to \(E\), satisfy \(e_l(y)\le h(y)\) on the positive integers and dominate zero. At \(j\ge l\) also \(\rho_j\ge e_l\), since \(\rho_j\) is the conditional expectation of \(E\) on depth-\(j\) residue classes. The latter identification follows from the iid affine series: all terms after the first \(j\) vanish modulo \(3^j\). The corresponding stationary measure has density \(E\). [Stationary envelope, pinned source and its ordinary trace](POWER_CAPPED_ORDINARY_TRACE.md) · [Syracuse stationary density and finite quotient normalization, Weaver 9/v2](https://rstation.ai/problems/collatz/papers/9)

Let \(L=\lfloor Y^{1-1/64}\rfloor\), \(K=\lfloor(\log Y)/2\rfloor\). Write \(F_L=\{f\le L:f\text{ positive odd}\}\), \(V_L=\bigcup_{f\in F_L,i\ge0}\{U^if\}\), and let \(\tau_L(y)\) be the first odd date with \(U^{\tau_L(y)}y\le L\). Precisely, \(G_Y\) consists of the odd \(y\in[Y,\lambda Y]\) satisfying both \(y\notin V_L\) and \(\tau_L(y)\le K\). The complement among the octave's odds has \(O_\lambda(Y^{1-1/64}\log Y)\) sites. At every good site, all first-hit paths to \(y\) have every departed odd state above \(L\), and \(y\) is nonperiodic. Their survival products are at least \(1-O(L^{-1/50})\) by uniform reciprocal packing. Since \(h(y)=\kappa y\beta_y\) with \(\beta_y\) the natural first-hit density weighted by those products,
\[
       h(y)\le\kappa g(y)\le (1+O(L^{-1/50}))h(y)\quad(y\in G_Y).
\]
The relative odd density and all-positive density agree at each odd target, by decomposing a positive source into its odd part and initial power of two. At a nonunit both densities vanish. [Natural first hits, weighted trace and good-site first moment](POWER_CAPPED_ORDINARY_TRACE.md) · [Elementary reciprocal packing (4), PR212 pin 3131111](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md)

## Physical depth and convergence

For fixed \(l\), \(j(y)\ge l\) eventually. The number of distinct depths \(j(y)\) on the octave is \(O_\lambda(1)\). For each such \(j\), the nonnegative difference \(\rho_j-e_l\) is periodic on the odd enumeration with period \(3^j\le\lambda Y\); its normalized full-period sum is \(1-\int e_l\,d\nu\), where \(\nu\) is additive Haar. Covering each subinterval of this depth by complete periods therefore gives
\[
   Y^{-1}\sum_{y\ {\rm odd\ in\ octave}}
       (\rho_{j(y)}(y)-e_l(y))\ll_\lambda 1-\int e_l\,d\nu .          \tag{4}
\]
This accounting uses the critical physical scale \(3^j\ll Y\); a fixed-cylinder convergence statement alone would be insufficient.

The good-site theorem gives \(\sum_{y\in G_Y}h(y)/y\to(\log\lambda)/2\). The harmonic mean of \(e_l\) on all odds tends to \((\log\lambda)\int e_l\,d\nu/2\), and its omitted-site contribution tends to zero for fixed \(l\) by boundedness and the count above. Thus
\[
 \limsup_{Y\to\infty}Y^{-1}\sum_{y\in G_Y}(\kappa g(y)-e_l(y))
           \ll_\lambda 1-\int e_l\,d\nu .
\]
On the omitted sites the normalized sum of fixed \(e_l\) is \(o(1)\). Combining with (4), then sending \(l\to\infty\), proves (3). The unit atom floor, the complement's vanishing relative count, and the fixed positive proportion of odd units in the octave prove (1).

For the logarithmic moments write \(A=|\log(\kappa g/\rho_{j(y)})|\) at units. On the good sites \(A\le C+\log^+g+\log^+\rho_{j(y)}\) by the two floors. Both positive terms have uniformly bounded exponentials of some fixed positive order in unnormalized ordinary mean, since \(Y^{-1}\sum_{G_Y}g=O_\lambda(1)\) and \(Y^{-1}\sum\rho_{j(y)}=O_\lambda(1)\) by (4) or the period bound. Thus \(A^p{\bf1}_{G_Y}\) is uniformly integrable for every fixed \(p\). On all omitted units \(g\le y\) and \(\rho_{j(y)}\le3^{j(y)}\le y\); the floors give \(A=O_\lambda(\log Y)\). Their normalized contribution is \(O_{p,\lambda}(Y^{-1/64}(\log Y)^{p+1})\). This proves (2). Natural and harmonic norms on a fixed proportional octave are comparable.

For comparison, on any true escaping unit ray \(y_i\), its full density satisfies \(d(y_i)\ge d(y_0)>0\). The maximal finite atom bound \(\max\rho_j\le C(3/2)^j\) yields \(g(y_i)/\rho_{j(y_i)}(y_i)\gg_{y_0} y_i^{\log_3 2}\) at every height. Such a ray lies in the forward orbit of its own fixed seed, and is eventually outside every relevant \(G_Y\). The discrepancy between this pointwise growth and (1) does not by itself exclude the ray. [Maximal finite atoms and attribution, Paper 200/v2 §4](https://rstation.ai/problems/collatz/papers/200)
