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

## A finite rational test that includes all ordinary targets

For every odd unit t define `g^*_q(t)` by summing J over ordinary x whose *first* U-hit of t occurs at exactly q, with `g^*_0(t)=1`. No all-time cycle decision is needed in this definition. For nonperiodic t it equals g_q(t). For t on a cycle C of odd period d, it equals g_q(t) for q<d and

    g^*_q(t)=g_q(t)−J_C g_(q−d)(t)     (q≥d).                           (5)

Indeed the discarded sources are exactly the whole inverse `(q−d)`-level at t followed by one lap. At every fixed ordinary unit the sequence has a limit by every-depth convergence; it is `(3/2)h(t)` off cycles and `(1−J_C)(3/2)h(t)` on C.

Uniformly over all cyclic targets and all q,

    g^*_q(t)/t ≤ C d(P(t)),                                              (6)

where d denotes ordinary predecessor density. To verify it for q≥1, first consider the nonperiodic members of a given first-hit inverse level of t. They form an antichain: a later nonperiodic member of a path cannot lie after its first arrival on the cycle, and a comparison strictly before that arrival would shorten the second member's first-hit clock. Replace its nonunit sources x by `4x+1` as before. Nonperiodic aliases remain in the same first-hit level. A cyclic alias can only be the unique cycle parent of its successor. At any fixed q the last q−1 steps after that successor determine at most one such cyclic alias: for q≤d the successor has first-hit clock q−1 on C, and for q>d there is none. At most one nonunit x thus maps to a cyclic alias. There is also at most one original cyclic source at this first-hit clock. If m_C is the cycle minimum, the reciprocal cost of these exceptions is `O(1/m_C)` (for m_C=1 use positivity of the integer sources). All other unitized sources are an antichain whose basins lie in P(t), and `J/t≤1/x`. The [linear antichain bound](SINAI_LOW_ANCESTORS.md) and the reciprocal predecessor lower bound `d(P(t))=d(P(m_C))≥c/m_C` yield (6), covering depth zero too. This lower bound is source-qualified on Wren’s theorem. In the other direction the proof of the [existing first-hit Cesàro lower bound](https://github.com/GettysburgResearch/collatz/blob/c2c25dabf3b837a223a46310d0092ef32e2119dd/research/native-pressure-20261118/ORDINARY-DENSITIES.md) counts distinct first-hit levels: a positive fraction `≥d(P(t))−o(1)` of ordinary inputs reach t in `O(log x)` steps and the distortion along their simple paths is bounded absolutely. The same argument applies to g* itself. Thus the fixed-target limit of `g^*_q(t)/t` is comparable to d(P(t)) with absolute constants on every odd unit, including cycles.

As t tends to infinity through cyclic states, `d(P(t))→0`: distinct cycles have disjoint basins so only finitely many have density above any fixed threshold, and their combined states are finite. Thus (6) handles all large cyclic targets uniformly in q. Finite cyclic targets have pointwise convergence by (5). It follows from the preceding equivalences that eventual periodicity of every positive orbit is equivalent both to `sup_q g^*_q(t)/t→0` as t→∞ through *all* ordinary odd units and to the finite-sequence condition

    M_q = max_{1≤t≤3^(q+1), t odd and 3∤t} |g^*_(q+1)(t)−g^*_q(t)|/t → 0.  (7)

Indeed a supremum on the omitted targets costs at most `(2/3)^(q+1)` because every nonnegative g* is bounded by `g_q≤2^q`. All entries in (7) are rational and effectively computable at each finite q. The transfer folds the geometric parameters over their finite ternary period, and iterating t itself for at most q+1 steps decides whether subtraction (5) applies. A proof of convergence of (7), beyond checking any finite initial segment, is still needed to exclude escape. The criterion allows nontrivial cycles.

## The maximum has a limit even under the escape hypothesis

In fact the finite rational sequence (7) always has a limit. In an escaping merger component C choose any forward unit spine, and write `H_C=lim h(y_j)/y_j`, which is H∞ since `F(y_j)/y_j→1`. This limit is independent of the chosen spine, as any two share a common tail. Changing the selected spine only shifts the integer index of its normalized scalar profile G. Put

    s_C=(3/2)H_C max_{k∈Z} |G(k+1)−G(k)|.

The maximum exists and is positive because G has the two different constant tail limits. Uniform boundedness of `g_q/h` also gives `s_C≤C₀H_C` absolutely. On this spine one has

    lim_(q→∞) sup_{j≥0} |g_(q+1)(y_j)−g_q(y_j)|/y_j = s_C.             (8)

Indeed for large j formula (3) twice approximates the signed difference uniformly in q by `(3/2)H_C [G(q−j+1)−G(q−j)]`, after dividing by y_j. Finitely many early j contribute a term tending to zero by every-depth convergence. Conversely take a maximizing k and for every large q set j=q−k. This proves both directions in (8).

With the empty supremum interpreted as zero,

    lim_(q→∞) M_q = sup_{escaping components C} s_C.                     (9)

For any δ>0, all nonperiodic targets outside S_δ contribute at most `C₁δ` by the uniform harmonic bound. Its finite cover contributes at most the largest of its finitely many limits (8) or zero for finite transient paths. Among all cyclic targets the supremum tends to zero by (5), (6) and disjointness of cycle basins, first removing all but finitely many via the uniform density bound. These observations prove the upper bound in (9); each component gives the reverse inequality by (8) and the exponentially small error from the finite cutoff in (7). If (9) is positive it is attained: only finitely many components have `H_C≥a` for any a>0, since a late representative per such component is an antichain of width bounded by that of `S_(a/2)`. In particular a subsequence with `M_q→0` suffices for eventual periodicity of every ordinary orbit. Formula (9) does not determine the sign of the limit.

The [finite rational replay](check_first_hit_maximum.py) computes M_q and all maximizing targets for q=0,…,4, using full ternary quotient transfer and a cycle test of at most q+1 odd steps per target. These finite coefficients do not determine (9).
