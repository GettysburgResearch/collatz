# Factoring-in-P machinery and the missing Collatz bridge

**SOURCE-QUALIFIED intake and PROPOSED deductions.** The requested repository is [gfreund123/factoring-in-p](https://github.com/gfreund123/factoring-in-p). The selected exact heads and file blobs are retained in [SOURCE_INTAKE.json](SOURCE_INTAKE.json). Complete selected Markdown proofs were read; no complete rebuild or blanket mathematical approval of that repository is claimed.

The direct conclusion is precise: the selected factoring results do **not** supply the \(1/8\) median synchronous-collision lower bound. Their most useful positive mechanism is an explicit reversible sampler. Its application would require an ordinary-orbit-preserving operation which those arithmetic algorithms do not construct. The companion [finite-certificate theorem](MULTIPLIER_CERTIFICATE_RIGIDITY.md) makes one central obstruction exact and connects it to the actual shortcut dynamics in Lean.

## Which results were actually inspected

| Pinned source | Useful mechanism | Remaining promise relevant to Collatz |
|---|---|---|
| [PR 21, a9d7771](https://github.com/gfreund123/factoring-in-p/blob/a9d77718c6648899e45d53db1206212425af6da0/research/sparse-overflow/carry-and-certificates.md) | Recover a raw multiplication polynomial from a bounded number of exceptional carry columns, then factor it over the rationals. | The unknown factors must possess the stated sparse raw columns. Almost all balanced prime pairs violate every fixed support bound. |
| [PR 30, 34fd3aa](https://github.com/gfreund123/factoring-in-p/blob/34fd3aa1bc805f7df524385de6cf9c9eb3b69cc2/docs/cubic-constant-precision.md) | Clipping a cubic character sum preserves a component-specific Fourier coefficient; a heavy-Fourier algorithm decodes factors from a supplied accurate evaluator. | The constant-accuracy evaluator is still an oracle. Its CRT coordinates are prime factors, not Collatz components. |
| [PR 31, 7541f06](https://github.com/gfreund123/factoring-in-p/blob/7541f06ef7b80d949e443c713aee7256d114f0d0/research/semiprime-collision-2026-11-26/notes/collision-extraction.md) | Derivative masking removes exact public matches; product-tree descent extracts a proper gcd from supplied colliding lists. | A guaranteed list of proper hidden-prime collisions remains necessary. Numerical residue collisions are different from same-date Collatz equality. |
| [PR 35, 41c80c3](https://github.com/gfreund123/factoring-in-p/blob/41c80c3716454659cb0f984947c8ac4682cb4bb9/notes/joint-cf-2026-11-26.md) | A small rational reconstruction error recovers a shifted product and then the hidden factor sum. | The joint divisibility and error inequality are promised; a uniform public choice is not obtained. |
| [PR 282, 1a0a7c6](https://github.com/gfreund123/factoring-in-p/blob/1a0a7c640b734c72f79f870dcb97d52dc1b0c8a3/research/all-semiprime-scales/PROOF.md) | One input-only decoder covers every scale ratio on an unconditional counted semiprime family. | The lower count may have vanishing relative density. It gives no all-input or orbit property. |
| [PR 296, 2d451e1](https://github.com/gfreund123/factoring-in-p/blob/2d451e192641f62531aca378f0dc34bcccb81adb/notes/coverage-frontier-2026-11-27.md) | Reversible permutations recover an internal mark from the product's own digits; small-bias walks hit arbitrary dense targets. | Translation parameters and labels are independent in the counting experiment. There is no Collatz merger attached to an inverse position. |
| [PR 355, 17bbd7a](https://github.com/gfreund123/factoring-in-p/blob/17bbd7a645ce721fe3a4284975952b904865e47f/research/abundance-frontier/turnpike/RESIDUE_LATTICE.md) | Read guarded low rows, then use a complete univariate small-root lattice at the quarter-bit boundary. | Readable low rows and the size inequality are structural assumptions on unknown factors. |
| [PR 359, ed5f35d](https://github.com/gfreund123/factoring-in-p/blob/ed5f35db43d346f26a28218c7f8088c5755aa4f3/research/fast-factor-phase-2026-11-27/notes/balanced-cubic-spectrum.md) | A fractional Fourier law with balanced local mass yields factors from approximate samples. | Acquiring the critical law is open. Its \(1/8\) is a total-variation tolerance, not the Collatz collision probability. |

The descriptions in this table have narrower status than an independent full proof audit of each analytic input. The actual written arguments were used to identify the exact operation, its parameter costs and its unpaid promise.

## The genuinely reusable sampler

Here is the algebraic core of PR #296 without its elliptic application. Let \(G\) be a finite group, let \(F_i:G\to G\) be public bijections, and take \(p,j\in G\). If

\[
          q=p^{-1}F_i(j),\qquad N=pq,
\]

then

\[
                    j=F_i^{-1}(N).                         \tag{F1}
\]

Thus the product alone recovers the hidden mark at each enumerated position. No factorization is needed to perform the inverse map.

For \(G=(\mathbb Z/2^w)^\times\), the inspected source gives polynomially many explicitly invertible positions. For every target \(A\subseteq G\) of density \(\gg1/w\), independent uniform \(p,j\) miss \(A\) at every position with probability at most \(2^{-(1/16-o(1))w}\). Its two reversible registers avoid the false assertion that an adaptively selected successful position leaves a fresh independent seed: the proof fixes a position first and only then unions over positions.

This distinction matters for a Collatz experiment. One can generate many candidate integer labels from a starting integer using these maps. What is missing is a statement that one candidate both has the desired orbit property and is connected to the **same actual starting orbit**. Formula (F1) supplies the first kind of bookkeeping. It supplies no second kind of connection.

### Exact conditional transfer target

Let \(V_X\) be a finite source population with a doubly stochastic transition matrix \(P_X\), and let \(b(n)\in\{0,1\}\) mark an actual Collatz basin. Write \(\bar b_X\) for its population mean. Suppose a Poincaré bound with parameter \(\gamma_X>0\) holds:

\[
 \gamma_X\bar b_X(1-\bar b_X)
 \le \frac1{2|V_X|}\sum_{n,m\in V_X}P_X(n,m)(b(n)-b(m))^2.
                                                               \tag{F2}
\]

Every transition accompanied by a genuine asynchronous merger has zero summand. If the total normalized transition weight lacking such a certificate is \(\epsilon_X\), then

\[
          \bar b_X(1-\bar b_X)
                      \le \frac{\epsilon_X}{2\gamma_X}.        \tag{F3}
\]

Consequently an orbit-preserving expander with \(\epsilon_X=o(\gamma_X)\), together with positive lower density of the basin of one and positive predecessor density for any counterexample, would prove universal convergence. This is a **conditional sufficient theorem**, not a completed construction. The factor \(1/2\) matches the energy convention in (F2); a convention without that factor changes both formulas together.

The useful engineering target is therefore an explicit kernel with a provable gap **and actual merger certificates for its transitions**. A freely chosen random permutation has a gap but no certificates. Local coalescence provides many certificates but the obvious kernel has no macroscopic gap.

### A scale obstruction for local kernels

The last sentence has an elementary quantitative form. On \(V_X=\{1,\ldots,X\}\), let every transition satisfy \(|n-m|\le R\). With \(f(n)=n-(X+1)/2\),

\[
 \operatorname{Var}(f)=(X^2-1)/12,\qquad
 \frac1{2X}\sum_{n,m}P_X(n,m)(f(n)-f(m))^2\le R^2/2.
\]

Thus every Poincaré constant valid for all real functions is at most

\[
                   \gamma_X\le\frac{6R^2}{X^2-1}.             \tag{F4}
\]

The known growing-block coalescence theorem supports \(R=\exp(o((\log X)^{1/8}))\) for every member of a block at logarithmic native dates. At that scale the bound (F4) is \(X^{-2+o(1)}\). A merely vanishing or polylogarithmic certificate failure bound cannot be divided by that gap. This does not rule out a long-range kernel, multiscale argument or a basin-specific inequality; it prevents this direct short-range-expander import from closing the proof.

For a **fixed** low-bit width, reversible permutations preserve each high-quotient block. The kernel is then disconnected on the full source interval, and its global gap is exactly zero. The factorization sampler's global mixing cannot be claimed for this ordinary lift.

## Why the two occurrences of \(1/8\) are different

The Collatz criterion is

\[
 \Pr(T^{\lfloor\mu\log X\rfloor}n_1
       =T^{\lfloor\mu\log X\rfloor}n_2)\longrightarrow\frac18.
\]

It is a maximal concentration statement about independent ordinary sources under the exact integer map.

In PR #359, the law proportional to \(|\widehat S|^{4/3}\) has independently balanced local prime-component types. An approximate sampler within total variation \(1/8\) retains a constant probability of separating a chosen pair of prime factors. Its decoder uses a gcd of a discriminant norm. The sampling source is already assumed to approximate the desired law.

The two constants have no shared normalization or established implication. In particular, computing many easy off-critical Fourier samples does not produce the critical law: the source proves a restricted obstruction for adaptive Boolean combinations of those masks, and explicitly leaves arbitrary arithmetic transformations outside that obstruction. This is a useful warning about an unproved acquisition step, not evidence for or against the Collatz lower bound.

## A positive exact collision identity to retain

For a finite initial population of ordinary Collatz sources, let \(p_t(y)\) be the mass at state \(y>0\) after \(t\) shortcut steps. Its collision mass \(K_t=\sum_y p_t(y)^2\) obeys

\[
 K_{t+1}-K_t
   =2\sum_{\substack{y>0\\ y\equiv2\pmod3}}
        p_t(2y)\,p_t((2y-1)/3).                              \tag{F5}
\]

The only two possible positive preimages of \(y\) are the even source \(2y\) and, when \(y\equiv2\pmod3\), the odd source \((2y-1)/3\). Expand the square of their sum and sum over \(y\). All old squares occur exactly once. This proves (F5), including the cycle states, with no probabilistic independence assumption.

Thus a direct lower-bound route could control the **integrated genuine branch-overlap mass** through the median clock. A factorization collision extractor could help enumerate exact finite witnesses, but it supplies no lower bound on this sum. CRT collisions at hidden primes do not contribute to (F5) until an ordinary equality certificate has been produced.

The next constructive question is specific: can the reversible residue sampler produce branches for (F5), or transitions for (F2), while preserving actual source identity and keeping total failed weight \(o(\gamma_X)\)? The current imported algorithms do not. The finite multiplier theorem shows why the most immediate affine realization cannot be supplied by a fixed parity-cell template. This is the load-bearing boundary to attack, rather than the cost of factoring a supplied semiprime.
