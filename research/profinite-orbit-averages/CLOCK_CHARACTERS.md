# Joint residues of the two branch counts at first arrival

**PROPOSED; source-qualified on equal-clock coalescence.** Fix any positive target b. Among all n in any fixed proportional window [uX,vX] that eventually reach b, let e(n) and o(n) be the numbers of even and odd shortcut inputs before their first visit. For any fixed positive moduli d,e and any prescribed pair of residues, the count with those branch counts modulo d,e equals the count of all hits in the window divided by de, plus o(X). One may simultaneously prescribe the starting residue modulo any fixed q: the main term is then divided by q as well. This is an absolute asymptotic even if the hit count is o(X). It becomes a relative law whenever that count has positive lower density.

The argument below also identifies the only two-branch complex weights which could have a nonzero profile on proportional windows. It uses the natural source average and retains the directions of the ordinary affine maps.

## Equal-count synchronization input

For each fixed gap, a density-one set of ordinary pairs synchronizes on some finite equal-clock binary cylinder with equal odd counts. Equivalently for gap one, as h increases the proportion of good residues modulo 2^h tends to one. This is the qualitative consequence needed here. See Duran's pair process and David Leen, *Quantitative synchronization for Collatz trajectories*, October 2026. Leen also proves a stronger spatial transfer for first-hit labels and the **starting** residue; that transfer is distinct from uniformity in the **arrival-clock** residues asserted above. We claim no priority for coalescence or the spatial transfer. [Quantitative synchronization](https://doi.org/10.5281/zenodo.23268755) · [Joint laws and local synchronization](https://doi.org/10.5281/zenodo.23268759)

Let U,V be complex numbers of modulus one. Put f(n)=U^e(n) V^o(n) when n reaches b, and f(n)=0 otherwise (the powers here use e(n),o(n) as exponents). Apart from b this gives f(2n)=U f(n) and f(2n+1)=V f(3n+2) with the possible exception interpreted at the left source. On a good fixed-horizon cylinder both n and n+1 stay above b before their meeting once n>2^h b, since a shortcut can reduce a positive integer by at most a factor two per step. Equal prefix counts and the common future give f(n+1)=f(n). Taking first X and then h to infinity proves

    X^(−1) Σ_(n≤X) |f(n+1)−f(n)| → 0.                          (1)

In particular the same holds on proportional windows and for every fixed additive shift. It holds for the basin indicator too. Any fixed residue class samples the same weak profile as all integers, with its relative frequency: partition into fixed-length blocks and use (1) to replace each block by its first value at a total cost o(X).

## Classifying scale profiles

Along any X tending to infinity, pass to a subsequence on which the bounded step functions f(floor(Xt)) converge weakly against compactly supported integrable tests on t>0 to a bounded function H(t). Diagonal extraction on compact intervals suffices. Relation (1), applied to the fixed residue samples in the two branch identities, gives almost everywhere

    H(2t)=U H(t),       H(3t)=(U/V) H(t).                       (2)

For example testing f(2n+1)=V f(3n+2) at n on the scale X gives the relation H(2t)=V H(3t); the offsets and fixed sampling strides disappear by (1). Only finitely many inputs involve the exceptional target edge.

Put s=log t. Choose a real κ₀ with exp(iκ₀ log 2)=U. Then h(s)=exp(−iκ₀ s)H(exp s) is log-2-periodic almost everywhere. Translation by log 3 on that circle is an irrational rotation. Its only eigenfunctions in L² are individual Fourier characters, by uniqueness of Fourier coefficients. Thus either H=0, or

    H(t)=c t^(iκ),     U=2^(iκ),     V=(2/3)^(iκ)

for a real κ and a complex constant c depending on the subsequence. At most one κ works because log 2 / log 3 is irrational. In particular if U,V are both roots of unity and at least one is nontrivial, H=0: otherwise both κ log 2 and κ log 3 are rational multiples of 2π, forcing κ=0. This proves vanishing on every proportional interval for every nontrivial finite character. Finite Fourier inversion in the two branch counts proves the stated residue law. With U=V=1 all subsequential profiles are constants, so the count of all hits in [uX,vX] is (v−u) times the count in [1,X], up to o(X), whether or not the latter density converges.

For example, if a positive target basin has positive lower density, every prescribed pair of even-count and odd-count residues occurs with a positive lower density in each fixed proportional shell. The ordinary clock counts e+2o and the shortcut clock e+o, so their joint classes modulo the same modulus are also equidistributed (the defining integer matrix has determinant one). The conclusion applies separately to each target. It does not identify which targets can be reached from an individually prescribed source.
