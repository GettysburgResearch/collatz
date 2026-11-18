# Exact ordinary endpoint laws at centered inverse ages

**PROPOSED, source-qualified.** Assume a divergent positive odd Syracuse spine `y_j=U^j(n)`, taking n to be a ternary unit by discarding at most one initial state. Put `F(x)=x∏_{i≥0}(1+1/(3U^i x))` throughout its merger component, with `F(Ux)=J_x F(x)`, `J_x=3/2^v₂(3x+1)`. Let h be the ordinary harmonic representative of `(2/3)dμ/dλ`, positive on units and zero on ternary nonunits. The canonical reverse transition from t to its parent x has probability `J_x h(x)/h(t)`. Set `H_j=h(y_j)/F(y_j)`. We use the [ordinary harmonic trace and transition](https://github.com/GettysburgResearch/collatz/blob/dbdfc911e3f77b8ab9633e4ac70d9b3cf644a217/research/native-pressure-20261118/CANONICAL-RETURN.md) and [earlier uniform scalar profile and reversed-spine concentration](https://github.com/GettysburgResearch/collatz/blob/8b397ea58775f1cccd23393a5190b482386b6102/research/critical-orbit-mellin/SPINE_CLOCK_PROFILE.md). Positivity of the actual spine-parent transition gives `H_(j+1)≥H_j>0`; `h(y)≪y` on this nonperiodic component gives a finite positive limit H∞.

For an ordinary component member define its phase `φ(x)=i−d` whenever `U^d x=y_i`. The injective spine makes this single-valued. For each integer k define an ordinary discrete probability

    π_k({x}) = 1_{φ(x)=−k} h(x)/(H∞ F(x)).                             (1)

Indeed for `j+k≥0` let `A_(j,k)={x:U^(j+k)x=y_j}` restricted to odd units. These sets increase with j and exhaust the phase −k unit slice. The actual probability of each x in the set is `h(x)/(H_j F(x))` by telescoping the canonical transitions. Their sums are one, so increasing exhaustion proves (1) is a probability. In particular for every j and every k with `j+k≥0`,

    Law_(y_j)(X_(j+k)) = π_k( · | A_(j,k)),
    TV(Law_(y_j)(X_(j+k)),π_k) = 1−H_j/H∞.                            (2)

Here total variation is the supremum over events. The displayed error is *exact*, independent of the centered age and of the observable. Applying the same Markov kernel to both sides gives the identical total variation distance for the whole subsequent reverse path when the endpoint itself remains observable. The π_k form an entrance law: one reverse transition sends π_k to π_(k+1), since each prospective child has a unique forward parent and F obeys its multiplier identity.

## The normalized scalar profile has both tails

For q≥1, `g_q=L^(q−1)g_1`, where `g_1` equals 0, 1, 2 modulo 3 on residues 0, 1, 2. The bounded terminal observable on units is therefore `g_1/h` at inverse time q−1. Direct use of `1/h` would omit the nonunit sources present in `L^q1`. Define

    G(k) = (2/3) ∫ (g_1/h) dπ_(k−1).

For every admissible q=j+k≥1, (2) gives

    |(2/3)g_q(y_j)/h(y_j)−G(k)| ≤ C(1−H_j/H∞).                        (3)

As k→−∞, `π_(k−1)` concentrates on the single state `y_(1−k)` with mass `H_(1−k)/H∞`, by (1). There `h(y_(1−k))→∞`, so `G(k)→0`. As k→+∞ fix N in (3); [every-depth convergence of the finite densities](https://github.com/GettysburgResearch/collatz/blob/27cd7ced4381a0d49470683c9cb492d23d207576/research/native-pressure-20261118/EVERY-DEPTH.md) gives `(2/3)g_(N+k)(y_N)/h(y_N)→1`. Letting N→∞ proves `G(k)→1`. Thus for arbitrary moving depths q with j→∞ the normalized density tends to 0 if `q−j→−∞`, and to 1 if `q−j→+∞`. Depth zero also tends to zero since `g_0=1`. At fixed k the limit is G(k); it is positive at every finite k because the earlier scalar profile includes an ordinary ancestor of positive weight. In particular negative fixed ages sufficiently far back have a value strictly between 0 and 1. An unbounded additive lag is sufficient for the post-age limit, in contrast with the longer horizon needed to wash out the initial spine contribution in an empirical *time average*.

In positive centered time the disjoint phase sets mean that π_k and π_l have total variation distance one for every k≠l. Thus equilibration of terminal observations on compact completions is a weak limit; it cannot be convergence of those countable ordinary laws in total variation. For the joint endpoint, [instantaneous fixed-root mixing at e28cd7c](https://github.com/GettysburgResearch/collatz/blob/e28cd7c73a2042c64a872841d684a872156569eb/research/native-pressure-20261118/INSTANTANEOUS-RETURN.md) shows every fixed positive unit t has `Law_t((X_q,X_q)) ⇒ ν` on the dyadic–ternary compact state space. Hence (2) implies `π_k ⇒ ν` there as k→+∞: first compare to the law from fixed y_N at depth N+k and then take N→∞. Consequently the same weak limit holds whenever `q−j→+∞`. In the negative-age direction (1) and (2) give concentration at `y_(j−q)` whenever `j−q→∞`. These statements leave each fixed ordinary spine compatible with the fixed-root quantifiers and exhibit exactly where nonuniformity is necessary.
