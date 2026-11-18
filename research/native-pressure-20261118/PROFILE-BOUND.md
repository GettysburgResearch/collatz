# A polynomial pathwise bound for the harmonic profile

For every fixed positive odd unit t and every D>5, the canonical inverse
path satisfies h(X_i)≤i^D eventually almost surely. In particular

    −log p_i = log X_i + O_path(log(2+i)).

Thus the prefix-information process in the [inverse functional central
limit theorem](INVERSE-BROWNIAN.md), centered by d⌊Qu⌋ and divided by
log 2 √(2Q), converges jointly and stably to the same Brownian motion
as the physical log height, in the uniform topology. This improves
the separate fixed-time information conclusion there.

[Short-source stabilization and shell notation](ITERATED-LOG-BOUND.md)
· [Uniform finite ternary L^r bounds for 1<r<2](ANTICHAINS.md)
· [Simple-path affine distortion](ORDINARY-DENSITIES.md).

## Count the heavy labels of the fixed-root inverse tree

First suppose t is nonperiodic. On an octave Y≤y<2Y consider its
ancestors at depth i≤C L, with h(y)>L^b. Their number is at most

    C_t Y L^(1−b).                                                     (1)

Indeed at each fixed depth the prefix probabilities sum to one.
For such y its unique prefix has probability J_w h(y)/h(t), where
the simple-path distortion bound gives J_w≥c t/y. Sum over the
O(L) possible depths. Denote the resulting deterministic heavy-label
set on this octave by A_Y. Constants below may depend on the selected
fixed root, r and the shell conventions.

## Count encounters on the true short-source word

Use the incoming shell with outer threshold R and inner threshold
R^(1/a), a=1.001, L=log R. For the proxy source z drawn with reciprocal
weights on odd [R^a,R^(a²)], outside summable error its actual first
entry at the inner threshold occurs by N=⌊L/20⌋, with log endpoint
at least L/2. These facts follow from the maximal short-source
calculation. All vertices before this first entry exceed R^(1/a).
For each such sampled z in an octave [T,2T) and every prefix ending
at y∈[Y,2Y) on this portion, of length n≤N and exponent sum S,

    2^S/3^n=(z/y) Π_(j<n)(1+1/(3U^j z)) ≤ 4T/Y.

Also y≤2T (3/2)^N up to a harmless fixed factor: shortcut odd heights
grow by at most a factor two per step, and on this large-height
segment the product of the affine corrections is ≤2. Thus all visited
octaves satisfy √R/2≤Y≤exp(C L), with only O(L) possibilities.

For fixed n,T,Y count the eligible sources whose endpoint lands in A_Y.
Each source gives a word and y; these determine the source. Its
contribution 1 equals (2^S/3^n) J_w with J_w=3^n/2^S. Consequently
the number divided by T is at most

    (4/Y) Σ_(y∈A_Y) g_n(y) ≤ C_r (|A_Y|/Y)^(1−1/r),                  (2)

where g_n(y) sums J_w over all n-letter words compatible modulo 3^n.
For the inequality, g_n is periodic modulo 3^n and has uniformly
bounded normalized L^r norm for any 1<r<2. Since 3^N≤√R/2 for large
R, a full octave of length Y has sum of g_n^r at most C_r Y. Apply
Hölder. This step uses the actual physical constraint on 2^S/3^n;
it avoids a loss exponential in the square root of the log height.

Sum (2) over n≤N and all eligible Y. For logarithmic sampling of z,
a source octave contributes at most a constant times the normalized
count divided by the total reciprocal mass, which is comparable to L.
There are O(L) source octaves, so their sum costs only a fixed factor.
The probability of encountering any heavy label is therefore at most

    C_t,r L^[2−(b−1)(1−1/r)]

plus the summable proxy failures. This upper bound for the entire
short-source route also bounds the event on its segment between the
two actual landings, without requiring a distributional assumption
at either hitting time. Transfer that segment to the canonical inverse
law by first-passage stabilization and the density-boundary comparison.
The added O_t(L^(−c)) is summable on L_j=a^j. Given D>5 choose
5<b<D and r<2 close enough to two that the displayed exponent is
negative. The successive shell depths are comparable to L; all depths
on a shell are eventually ≤C L for a fixed sufficiently large C by
the strong law, so (1) included every possible realized heavy label.
Borel–Cantelli proves h(X_i)≤O(i^b) eventually, and the extra exponent
absorbs the constant. A countable intersection gives all D>5.

At a periodic root condition on its almost surely finite exit prefix.
The normalized path identity and the bounded simple-path log correction
give −log p_i=log X_i−log h(X_i)+O_path(1); h is bounded below.
Taking maxima up to Q leaves an O_path(log(2+Q)) discrepancy, proving
the uniform functional information assertion.

## Restricting both clocks improves the exponent to 7/2

In fact the conclusion holds for every D>7/2. Fix b between 7/2 and
D and an arbitrarily small η>0. In (1) it suffices to count fixed-root
depths |i−(log Y)/d|≤L^(1/2+η). Indeed the realized depths in this
shell are comparable to L, and the all-depth pathwise clock bound gives
|log X_i−di|=O_path(√(L log log L)); the fixed octave width and
random constant are absorbed eventually. The number in (1) improves
to O_t(Y L^(1/2+η−b)). This restriction on the deterministic candidate
set is made before any proxy comparison.

Independently, on the summably good actual short-source event of the
maximal argument, uniformly for n≤N,
log U^n z=log z−d n+O(√(L log log L)). Thus for the specified source
and endpoint octaves T,Y, only |n−log(T/Y)/d|≤L^(1/2+η) need be
summed in (2). The complement of this simultaneous good event was
already included as one proxy failure, independent of the octave
union. The resulting exponent in the probability estimate is

    3/2+η − (b−1/2−η)(1−1/r).

Choose r sufficiently close to two and η sufficiently small that this
is negative. The remaining transfer and Borel–Cantelli steps are
unchanged. The improved bound also sharpens the polylogarithmic
Hausdorff gauge of the real fibre: substituting profile power 7/2+δ
in its cylinder count gives r(log(1/r))^(4+ε) for every ε>0.
