# Literature and dependency map

Published inputs, recent external Collatz manuscripts and the new deductions have separate evidence levels. No external formalization library was rebuilt.

## Published inputs

| Source | Exact input and use |
| --- | --- |
| K. Mahler, *On the fractional parts of the powers of a rational number (II)*, Mathematika 4 (1957), Theorem 2. [DOI](https://doi.org/10.1112/S0025579300001170) · [Original scan](https://carmamaths.org/resources/mahler/docs/135.pdf) | Exponentially close integer approximation to \((u/v)^k\) for coprime integers \(u>v\ge2\) occurs at only finitely many exponents. Used at \(3/2\), threshold \((3/4)^k\). No effective cutoff is inferred. |
| J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics 155 (2002), Theorem 1.1. [Published page](https://annals.math.princeton.edu/2002/155-3/p04) · [Reprint](https://arxiv.org/pdf/math/0409604) | Bound \(\exp((6n)^{3n}(r+1))\) on nondegenerate unit-equation solutions, uniform in fixed coefficients. Applied at joint rank \(r_0+r_1+2h\) to arbitrary-run mountain returns. |
| J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica 53 (1984), Corollary 1, pp. 227–228. [Primary scan](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf) | Finiteness of primitive nondegenerate integer zero-sum tuples whose product of prime-to-\(S\) parts is below height to power \(d<1\). Used at \(S=\{2,3\}\) for the numerical gcd at every mountain. |
| R. P. Steiner, one-circuit theorem; author's account in *On the Qx+1 problem, Q odd*. [Scan, pp. 285–286](https://www.fq.math.ca/Scanned/19-3/steiner.pdf) | Excludes the last rank-one cycle possibility after the local target classification. The linked account reports Steiner's earlier \(3x+1\) result. |
| J. Simons and B. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arithmetica 117 (2005). [DOI](https://doi.org/10.4064/aa117-1-3) · [Version 1.44](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf) | Chain equations, §2.1; fixed-minima cycle finiteness, Theorem 3(a), attributed there to Brox; Rhin's separation of logarithmic forms, Lemma 12. |
| L. Habsieger, *Explicit lower bounds for \(\lVert(3/2)^k\rVert\)*, Acta Arithmetica 106 (2003), §1, (1.1). [PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82203) | Records Kubina–Wunderlich's computation of the ideal-Waring fractional-part inequality through \(471{,}600{,}000\). Imported exclusion range for a necessary condition; not repeated here. |
| W. Zudilin, *A new lower bound for \(\lVert(3/2)^k\rVert\)*, Theorem 1. [DOI](https://doi.org/10.5802/JTNB.588) | Effective asymptotic lower bound with base \(0.5803\), smaller than the needed \(3/4\). Comparison only. |
| S. Brofferio, *The Poisson boundary of random rational affinities*, Annales de l'Institut Fourier 56 (2006). [PDF](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf) | Boundary in contracting completions under nonabelian and logarithmic-moment hypotheses. Tested in the global attempt; no uniform-integrability conclusion for the ordinary source statistic is imported. |

## Recent source-qualified Collatz interfaces

| Source/version | Exact dependency and use |
| --- | --- |
| *First-landing bounds and canonical inverse laws for Collatz*, rStation paper 12, v1. [Access](https://rstation.ai/problems/collatz/papers/12) | §6, (15), relative landing uniform over bounded tests; Theorem 14's uniform first-odd-landing lower atoms under its written selected-block/mixing inputs; density inputs stated there. Used for returns and final upcrossings. The paper distinguishes written deductions from reported external Lean results. |
| *Conditional clocks and source couplings for Collatz synchronization*, paper 13, v1. [Access](https://rstation.ai/problems/collatz/papers/13) | Equation (1), uniform counted-pair estimate credited to Leen; Proposition 1's CRT mechanism. Our ceiling-sensitive comparison checks the path condition before fusion. |
| Weaver–Wren, *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*, paper 48, v1. [Version](https://rstation.ai/problems/collatz/papers/48/v1) | Theorem 8: legal inverse routing to every unit class with common length, doubled total and linear precision cost. Used with growing merger horizon; no descent is inferred. |
| Weaver, paper 138, v1. [Access](https://rstation.ai/problems/collatz/papers/138) | Prior rank/coset bounds in odd-step time and comparison with Yang. The new bound is in mountain time with unrestricted run lengths. |
| Weaver, paper 178. [Access](https://rstation.ai/problems/collatz/papers/178) | Prior all-time image and first-meeting bounds. Attribution for the orbit-image mechanism; prescribed-prefix and finite-cutoff conclusions are proved locally. |
| Sultanow, preprint v3. [Version](https://www.preprints.org/manuscript/202610.2552/v3) | Proposed source-weighted return potential. Our note identifies only the upper-band clipped portion controlled before the next floor. |

Repository sources are pinned in [LATEST_CONNECTIONS.md](LATEST_CONNECTIONS.md) and the head snapshot. PR146 supplies counted affine fusion, PR197 the high-mass regular passage window, and PR199 the barrier and actual component closure interfaces. Our Lean files do not formalize their analytic dependencies.

The versioned v1 routes for papers 12 and 13 were unavailable in the root's browser tool; the accessible unversioned pages explicitly displayed v1 and were read there. The root opened the original ESS, Evertse and Mahler sources, Simons–de Weger, Habsieger's statement and the routing theorem. Independent reviews record their checks.
