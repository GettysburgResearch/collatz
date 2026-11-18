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

## Finite forward paths contain all large nonperiodic spikes

Let `S_δ={t positive odd nonperiodic unit:h(t)≥δt}`. Here *nonperiodic* excludes points on cycles and includes transient inputs in their predecessor trees. For fixed δ>0 this set is contained in finitely many ordinary forward orbits. Moreover, it has reachability width `O(1/δ)`, and it can be covered by that many forward orbits. To see the width, apply [the bound on antichains of large finite-clock densities](SINAI_LOW_ANCESTORS.md) and pass to the pointwise limit `ρ_q(t)→h(t)` (finite subsets suffice).

No infinite decreasing chain in this set can run backwards to a fixed member r. More generally, **every** fixed positive odd unit r has only finitely many nonperiodic ancestors t with `h(t)≥δt`. For such a t, take the simple first-hit path to r of odd length d. Its prescribed reverse word has probability

    J(t,d)h(t)/h(r) ≥ c rδ/h(r),

by the uniform simple-segment reciprocal bound and the positive correction formula. The maximum mass of any length-d reverse word tends to zero as d→∞. This follows directly from [the fixed-root information weak law](https://github.com/GettysburgResearch/collatz/blob/9092b1f/research/native-pressure-20261118/PHYSICAL-CLOCK.md): an atom of size ≥a along unbounded d would itself contribute probability ≥a to information per step at most `−log(a)/d`. There are finitely many atoms at or above the fixed positive lower bound at each remaining d. Fixed-root nonatomic inverse boundary decay is also part of the prior work compared in [rStation 12](https://rstation.ai/problems/collatz/papers/12/v1). This reasoning includes cyclic r when using first-hit paths.

Take a finite Dilworth chain cover at the stated width (finite subsets, then compactness of the tree of compatible colorings). In each chain the predecessors of any one member are finite by the preceding argument. Consequently every nonempty chain has a first ordinary member and all its members lie on its forward orbit. An infinite chain must follow an escaping forward orbit, since an eventually periodic orbit has finitely many distinct states. In particular there is an exact equivalence among the following assertions:

1. Every positive orbit is eventually periodic (there may be more than one cycle).
2. `h(t)/t→0` along the positive nonperiodic odd units tending to infinity.
3. `sup_(q≥1) g_q(t)/t→0` along those units.
4. `lim_(q→∞) sup_t |(2/3)g_q(t)−h(t)|/t=0` on those units.
5. `lim_(q→∞) sup_t |g_(q+1)(t)−g_q(t)|/t=0` there.

Indeed (1) implies finiteness of each S_δ, giving (2). The earlier harmonic bound `g_q(t)≤C h(t)` for q≥1 and every-depth convergence yield (2)⇔(3) and (2)⇒(4),(5), by handling finitely many small t separately. Conversely every escaping unit spine has `h(y_j)/y_j→H∞>0` since `F(y_j)/y_j→1`. At q=j−⌊√j⌋ formula (3) shows a nonvanishing normalized error, contradicting (4). The two distinct tails of G imply some consecutive centered ages have different values, contradicting (5) by (3) along the spine. Thus these equivalences concern escape, leaving the separate issue of nontrivial cycles intact.

There is an unconditional adaptive version of (4). Define `D_B(t)` to be the largest distance to a nonperiodic unit t from any odd positive start at most B that reaches it, or zero if none does. For every ε>0 there exist finite B,K such that, simultaneously for all these t,

    q≥D_B(t)+K  implies  |(2/3)g_q(t)−h(t)| ≤ ε t.                      (4)

Choose δ small so that outside S_δ the harmonic bound handles all q≥1. For its finite forward cover take B at least all the initial members. Every eventually periodic covering path has only finitely many states, handled by fixed-root convergence. On each remaining divergent path the ordinary clock j from its selected initial state is at most D_B(t). Equation (3) and `G(k)→1` give the desired bound whenever j and q−j are sufficiently large (use boundedness of h(t)/t). The finitely many earlier roots on each path are again covered by every-depth convergence. Maximize over the finite family. Neither B nor K is claimed effective. Eliminating the target-dependent arrival clock in general is exactly the escape obstruction in assertion (4) of the equivalence list.
