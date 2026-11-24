# Multiscale sparse ranks with only one reset level per physical step

**Scope.** Proposed written construction. All clocks below are *physical shortcut* clocks, not numbers of valleys. This repair constructs a finite proper multiscale score at every positive ordinary integer, keeps a decidable sparse exceptional set, and reduces simultaneous resets to one explicitly measurable return time. Its displayed proper score fails strict descent at ordinary inputs. No cycle or escape is asserted or excluded.

## Forward wrapping of nested sparse markers

Retain the computable sparse image S from ../SPARSE_RESET_MEASURE.md, including its selector from n to x in at most H(n) shortcuts with x≥√n. Choose increasing integer cutoffs B_j, j≥1, with B_j≥2^{2j}, B_j≥4 and

    #(A_j∩[1,X]) ≤ 2^{−4j} X for all X≥1,     A_j = S∩[B_j,∞).

The cutoffs can be found effectively. In the fixed-depth proof for S take t=5j. Search for a finite open projected rotation cover on the positive circle using rational endpoints and multiplicative powers of three. For its largest clock K, find a source lower bound N guaranteeing D≥t, H≥K and (1+2^K/(3N))^K smaller than the ratio of the upper window endpoint to the upper interior endpoint. The finitely many outputs below this source threshold can be enumerated and excluded by B_j. The upper bound for W_t is at most (3/14)3^{−t}X+O(log(2+X)), from the explicit geometric sum and at most one rounding error per window; increasing B_j further makes the rounding term at most 2^{−4j−1}X whenever X≥B_j.

Define

    M_l = ⋃_{j≥l} ⋃_{0≤d≤j−l} T^d(A_j)       (l≥1),     M_0 = all positives.

The M_l are nested. The forward wrapping ensures T(M_l)⊂M_{l−1} whenever l≥1. For any contributing seed s, its image n≥s/2^d≥B_j/2^j≥2^j and s≤2^d n. Thus membership is decidable by a finite search over j,d,s, and J(n)=max({l:n∈M_l}∪{0}) is finite at every ordinary n. Every M_l has natural density zero. The finitely many images from bounded j each have density zero, since a seed mapping to ≤X is at most 2^d X. The remaining images contribute at most X Σ_{j≥J_0} 2^{−4j}Σ_{d≤j}2^d, which is o_{J_0}(X). These statements use ordinary dynamics and no distribution on a purported escape.

For each l, kill at M_l, at 1, or at any periodic vertex on a cycle entirely below B_l². The last finite set is decidable by enumeration of the finite graph below that height. Define t_l(n) to be the first physical killing clock, allowing zero. If n≥B_l², the selector hits A_l by time H(n). Otherwise, before crossing B_l² the orbit reaches a terminal, repeats in the finite graph, or exits in at most B_l² clocks; at its first exit its height is below 2B_l². Consequently

    t_l(n) ≤ L_l+H(n),     L_l=B_l²+H(2B_l²)+1.

This is an independent all-source horizon bound, including at a hypothetical divergent source.

## The exact single-refill identity

Let w_l>0 have W_1=Σw_l<∞ and W_j=Σ_{l≥j} w_l. For example, w_l=2^{−l}/L_l guarantees G(n)=Σw_l t_l(n) is finite on every positive integer by the bound above. For a nonperiodic source n, including an escaping source or a transient convergent source, let z=Tn. Then

    G(n)−G(z) = W_1                               if J(n)=0,
    G(n)−G(z) = W_{J+1} − w_J t_J(z)             if J=J(n)>0.

For l>J, n is not terminal (it is nonperiodic), so its exact debit is one. For l<J, both n and z are in M_l by wrapping, giving zero. At l=J the source is terminal and contributes precisely −t_J(z). Thus a deep source cannot simultaneously refill every coarser level. For a periodic n the same expressions are upper bounds, since an additional terminal can only reduce its own debit. Special finite cycles are accounted for explicitly rather than assumed absent.

A proper all-ordinary score is R(n)=4G(n)+W_1 b(n), where b(n)=⌊log₂(n+1)⌋. This equals the weighted sum of the proper integer levels 4t_l+b. It is computable with the explicit weights above and is finite everywhere; R≥W_1 b is proper. The interpolation result applies on all positive integers by using the same spikes on Z₂ instead of the odd coset, or on the odd restrictions directly. Strict ordering of a proper real-valued score, if achieved, is enough: its integer order label N(n)=#{m:R(m)≤R(n)} is finite, proper, and has a uniform integer debit on every strict comparison. Thus tiny strict debits would not require a separate divergent-series argument for a proper score. One can apply the diffuse interpolation to the integer order label once instead of summing fixed approximation errors that could swamp arbitrarily small margins. This is an existence statement: computability of the order label is not inferred from comparisons of arbitrary computable real values.

Off M_1, R has debit at least 3W_1 at a nonperiodic source since b(Tn)−b(n)≤1. Across marks the exact remaining term is 4(W_{J+1}−w_J t_J(Tn))+W_1(b(n)−b(Tn)). This particular properization actually fails, even with forward wrapping. Every n=7·3^m is in S, since at clock zero it is eligible at maximal allowed depth. It belongs to A_j for any fixed j once m is large enough. There are arbitrarily large m such that b(Tn)=b(n)+1: choose the fractional parts of log₂(7·3^m) in a fixed open subinterval of (1−log₂(3/2),1), using irrationality of log₂3, and allow the vanishing +1 errors. For m≥1 such n is nonperiodic, because no positive cycle can contain a multiple of three (after any odd input the target is a ternary unit, and the following even divisions preserve it). On these ordinary inputs

    R(n)−R(Tn) ≤ 4W_{J(n)+1}−W_1 < 0

eventually. This is an actual increasing edge for every choice of summable positive weights for which G is finite, not a failure inferred solely from a tail bound. A smoother or dynamically compensated proper toll is still possible.

## A critical weight and its horizon cost

There is a simple reference model with one boundary per step even without wrapping: kill at height ≥2^j, at 1, and at vertices of cycles entirely below 2^j. Let e_j(n) be this physical first-hit time. A nonperiodic source n with D=⌊log₂n⌋, D≥1, has exact weighted debit W_{D+1} on an odd (growing) shortcut. On an even shortcut the debit is W_{D+1}−w_D e_D(n/2). Other coarser levels are terminal at both ends. Already e_10(834)=52: the actual orbit first reaches ≥1024 at 1079, not 1. Thus 1668→834 refills 52 physical clocks at its single boundary. This refutes a universal bound e_D(n/2)≤3D even if returns to 1 are set aside.

For an escaping fixed source n, let X_i=max_{0≤k≤i}T^k(n). Tonelli gives the exact extended-real identity

    Σ_{j≥1} w_j e_j(n) = Σ_{i≥0} Σ_{j:2^j>X_i} w_j.

Indeed the contribution of clock i means exactly that its running maximum remains below the ceiling. For the critical weights w_j=1/[j(j+1)], the right side is Σ_i 1/(1+⌊log₂ X_i⌋). Since X_i+1≤(3/2)^i(n+1), this diverges harmonically along *every* escaping trajectory. At a fixed ordinary source reaching 1 all e_j are eventually bounded by its actual stopping time. Thus at these critical weights the needed finite-source bound is a genuine arithmetic obligation; it cannot be inferred from a finite mass allocation for the diffuse measures.

The same height tradeoff applies to the sparse wrapped levels. On any escaping path reaching M_l, the first marked value is at least B_l/2^l if B_j/2^j is nondecreasing (choose the cutoffs successively to ensure this). Therefore t_l(n) ≥ log_{3/2}((B_l/2^l+1)/(n+1)) whenever the right side is positive. The unconditional rapidly decaying weights provide finiteness but little nominal debit on deep marks. Conversely a choice forcing Σ_l w_l(log B_l−l log 2)=∞ would require a separate proof of sourcewise finiteness that already excludes escape. This calculation is on one original source, not changing finite witnesses.

A physical debit ≳1/log(n+2) at every nonterminal physical shortcut would have divergent total along every infinite trajectory by the same growth bound. On valley clocks the corresponding target is the sum of the physical costs within the valley, not one such cost at its source. The missing step is a well-founded proper toll or another sourcewise estimate which controls both the actual single-refill time and the change of the toll on *every required return*. No such estimate has been established.

## A proper toll that does not refill at any sparse marked edge

There is a stronger repair of the elementary log-height toll just refuted. Enlarge the computable B_j at construction time; all preceding nesting, spatial sparseness and horizon bounds survive with the new L_j. We first ensure separation of wrapped-marker blocks in **physical time**, even when a marked state is the image of a seed on a different predecessor branch.

Write φ(x)=log₃(x) mod 1, α=log₃2. Fix j and let Δ_j=min_{1≤p≤4j}‖pα‖>0. Choose a positive rational ε_j<Δ_j/20. Effective choice is possible by strict separation of the finitely many unequal powers of 2 and 3. Find Y_j such that every s∈S with s≥Y_j has phase within ε_j of φ(7); the effective fixed-window proof above does this. Increase B_j recursively to satisfy, for example,

    B_j ≥ 2^{j²},      B_j ≥ 10⁴·200^j·(Y_j+j/ε_j+1),

as well as all the preceding conditions. The generous factors permit the following estimates using only T(x)≥x/2 and T(x)+1≤(3/2)(x+1).

Fix one arbitrary positive physical orbit x_i. A virtual start at t≥0 of level j means that x_{t+d}=T^d(s) for a seed s∈A_j and 0≤d<j. A marked observation is accounted for by such a start except when its index i<d; then 2^i≤2^j≤x_i≤(3/2)^i(x_0+1), so (4/3)^i≤x_0+1. This omits only a finite initial portion of this one orbit.

**Separation.** Two distinct virtual starts t,u of levels j,k cannot satisfy 0<|t−u|≤4 max(j,k). To verify, relabel so j≥k. At the shared endpoint for the j-record its height is at least B_j/2^j. Every earlier value on its two length-d paths, including x_t and s, has value plus one at least B_j/3^j by the upper growth bound. If |t−u|≤4j, then x_u+1 and every intermediate true state plus one are at least B_j/(3^j 2^{4j}). This uses x_{i+1}+1≥(x_i+1)/2 going forward and x_i+1≥(2/3)(x_{i+1}+1) going backward. The shared endpoint for the k-record has value plus one at least 2^{−j}(x_u+1); pulling back through at most j more shortcuts shows that its alternative seed and all states on both short k-record paths have value plus one at least B_j/(9^j 2^{4j})=B_j/144^j. Thus both actual seeds exceed Y_j and every orbit segment in this comparison stays high.

Over ≤4j physical clocks at these heights the phase advance differs from −pα by at most 4j/[3 log(3)(B_j/144^j−1)]<ε_j. The error is the actual sum of log₃(1+1/(3x)) at odd clocks. Equality at the shared endpoint says that each virtual starting phase differs from the corresponding seed phase by at most 2ε_j. Thus φ(x_t) and φ(x_u) are each within 3ε_j of φ(7). Comparing their true intervening segment gives ‖(t−u)α‖≤7ε_j<Δ_j, a contradiction. This argument retains the coalescence time of the seed actually witnessing membership; no common earlier source is assumed.

For a fixed virtual start t there is a maximal level j_t since x_t+1≥B_j/3^j→∞. Its associated marked observations lie in [t,t+j_t). Distinct such start times are separated by more than four times either associated length. Moreover j_t=O_{x_0}(√(t+1)) by B_j≥2^{j²} and x_t+1≤(3/2)^t(x_0+1). Consequently on **every positive ordinary orbit** the upper physical time density of M_1 is at most 1/4: sum the covered lengths before the last start using the successive start gaps, and bound the final partial block by o(t). In particular every infinite trajectory encounters infinitely many unmarked clocks, whether it eventually cycles or escapes.

Define a new integer toll

    b_*(n)= min_{m≥1, k≥0, T^k(m)=n} [ m + #{0≤i<k : T^i(m)∉M_1} ].

The empty path from n gives b_*(n)≤n. Every candidate of cost ≤R starts at m≤R. Along each of these finitely many actual paths there are only finitely many clocks before its (R+1)-st unmarked edge, by the preceding separation theorem. Hence b_* is proper. It is computable: simulate each m≤n until its unmarked count exceeds n, recording any occurrences of n and the empty path. Extending a minimizing path by one literal shortcut gives

    b_*(Tn) ≤ b_*(n) + 1_{n∉M_1}.

In particular this proper toll never increases across **any** marked edge, including the expanding 7·3^m family. The new R_*(n)=4G(n)+W_1 b_*(n) is finite, computable, and proper at every positive ordinary input. It pays at least 3W_1 when J(n)=0 at a nonperiodic source. For a nonperiodic source with J>0 its exact debit is

    4(W_{J+1}−w_J t_J(Tn)) + W_1(b_*(n)−b_*(Tn)),

with the last term nonnegative. At a periodic source the expression is only an upper bound, because high levels can stop at additional cycle vertices. This is a repair of a specific obstruction on genuine ordinary sources. There is no proof that the last nonnegative term pays the single remaining refill on every marked exit, or that all the required returns are strictly decreasing. The physical upper density bound controls time spent inside blocks, not the size of a first-return clock after a block ends. A least nonconverger could still retain that single deficit.

For an exactly rational boundary test on nonperiodic sources one may prescribe W_j=2^{−j}/L_j and use w_j=W_j−W_{j+1}>0 (take the L_j increasing). This preserves w_j≤2^{−j}/L_j and the same finiteness proof, while both the tail and the single-weight term in the final debit are explicit rationals. All quantities in the test can then be evaluated by finite integer computations, without comparing two infinite real series. It is a decision of the displayed boundary inequality, not a decision that the source is nonperiodic.
