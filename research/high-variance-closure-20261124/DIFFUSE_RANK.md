# Diffuse valuation potentials can represent every proper ordinary rank

**Status.** Proposed written theorem. This establishes representability and a necessary singularity of the potential on the completion. Constructing its global ordinary debit without assuming termination remains open.

On the odd 2-adic integers let H_μ(x)=∫v₂(x−r)dμ(r) for a finite positive measure. Allow ∞ on the completion and require finiteness on positive odd ordinary integers. The summable rational atomic obstruction in GLOBAL_RANK.md at PR182 checkpoint f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67 used a finite logarithmic height moment; it did not address diffuse measures without a regularity bound.

## Interpolation theorem

Let D be the positive odd integers and F:D→nonnegative integers be proper (each sublevel is finite). For any ε,η>0 there is an atomless measure singular to odd 2-adic Haar measure, of total mass at most η, satisfying

    F(n) ≤ H_μ(n) ≤ F(n)+ε     for every n∈D.

A second construction gives an absolutely continuous finite measure with an L¹ density and the same estimates. The measure may depend on F. The theorem does not assert an independently known formula for a Collatz rank.

For the singular construction let U=Σ_{i≥0} X_i 2^{2i}, with independent equiprobable {0,1} digits X_i. Its law is atomless and supported on a Haar-null set (all odd-indexed digits vanish). The function L(t)=E[v₂(t−U)] is continuous and bounded by two, with L(0)=2. Indeed L=Σ_{m≥1}Pr(U≡t mod 2^m); each summand is locally constant and bounded by 2^{−ceil(m/2)}, whose sum is two. Given odd n and k≥1, the translate n+2^k U stays odd. Its probability measure has potential exactly v₂(x−n) if v₂(x−n)<k, and k+L((x−n)/2^k) otherwise. It attains its global maximum k+2 at n. It is continuous. For the absolutely continuous variant use Haar-uniform U on Z₂, so L(t)=1 everywhere and the maximum becomes k+1.

Enumerate n_1,n_2,... in nondecreasing order of F. Write δ_j>0 with Σδ_j<ε and β_j>0 with Σβ_j≤η. Begin with the zero measure. At stage j the previous finite potential H is continuous. Choose an outer ball B=n_j+2^R Z₂, R≥1, containing no earlier n_i and with |H(x)−H(n_j)|≤δ_j throughout B. If H(n_j)≥F(n_j) add no measure. Otherwise set A=F(n_j)−H(n_j)>0. Use the indicated spike of depth k≥R and mass w=A/(k+2) (or A/(k+1) for the Haar version). Choose k large enough that w≤β_j and wR≤δ_j.

The spike fills the deficit exactly at n_j. On B the new potential is at most F(n_j)+δ_j, because the spike peaks at n_j. Off B its leakage is at most δ_j. Starting with zero and using nondecreasing F, the global supremum at stage j is at most F(n_j)+Σ_{i≤j}δ_i; in the skip case use the preceding bound. Each earlier n_i only gains leakage ≤δ_j. At the end, n_j has H≥F(n_j) and H≤F(n_j)+Σ_iδ_i. Monotone convergence identifies the pointwise increasing sums with the potential of the sum measure. The mass bound and absence of atoms pass to this sum; in the singular construction the countable union of its supporting sets is Haar-null. For the Haar construction its density is the sum of integrable nonnegative densities.

## Exact equivalence and a computable basin construction

The following are equivalent for positive ordinary Collatz:

1. Every positive integer reaches 1.
2. There exists a finite atomless singular continuous μ, finite in potential at every positive odd ordinary input, and some δ>0 such that H_μ(y)≥H_μ(z)+δ for every positive odd y>1 and its next true valley z.
3. The same statement as (2) holds with an absolutely continuous μ of arbitrarily small positive total mass instead.

If (1) holds, take F(n) to be the number of ordinary shortcuts from n to its first 1. This is a proper integer rank since every shortcut is at least half its input, so F(n)≥log₂ n. A whole valley starting at y>1 can first encounter 1 only at its odd endpoint: intermediate odd steps strictly increase at positive inputs above 1, and the halving run reaches 1, if at all, at its endpoint. Hence F(y)=a+b+F(z) with a+b≥2. Approximate F as above with ε<1, giving a uniform debit of at least 2−ε. Either flavor of measure works with arbitrarily small mass. Conversely nonnegative finite H with that debit makes an infinite path avoiding 1 impossible, since H(y) bounds its number of valleys by H(y)/δ. Even inputs first reach an odd input by halving.

There is also an unconditional construction with the same debit on every convergent source and finite potential even at hypothetical outsiders. Enumerate only the odd members of the positive inverse basin of 1 in nondecreasing first shortcut time (finite layers obtained by the two elementary inverses). Perform the construction on these members. At stage j also require the outer ball to exclude the first j positive odd ordinary integers in their natural order except n_j itself. This adds a finite separation condition. For each outsider m the cumulative contribution after its natural index is at most Σδ_j, so its potential is finite; for basin members the previous proof applies. With explicit rational error and mass budgets and the Haar version, every finite stage uses decidable rational arithmetic. This supplies no debit at a hypothetical outsider: such a source is outside every enumerated layer. Treating enumeration of the basin as an enumeration of all positive odd integers would reintroduce the conjecture.

## Exact finite optimization and the first missing estimate

Take any finite directed graph of prescribed true valley edges on positive ordinary vertices. Require H(y)≥H(z)+1 on every displayed edge and H≥0. A directed cycle is infeasible. If the graph is acyclic and L(v) denotes the length of its longest path starting at v, then for each specified v the **infimum of H(v) equals L(v)**, even when restricted to singular continuous μ of total mass at most any prescribed η>0 (or the absolutely continuous L¹ alternatives). The infimum need not be attained.

Indeed summing along a longest path gives the lower bound. For the reverse estimate, extend the integer labels L from the finite vertex set to a proper nonnegative integer function on all positive odd integers (e.g. give other m the label m). The interpolation theorem with error e in (0,1) gives all displayed debits at least 1−e. Rescale the measure by 1/(1−e), initially choosing mass at most η(1−e). This gives the required debit and H(v)≤(L(v)+e)/(1−e). Let e decrease to zero. The finite LP therefore has no extra constraint arising from dyadic geometry or the requested small mass.

In particular, for the first K successive edges of a fixed injective ordinary trajectory the optimum at its source is K. Arbitrarily small mass can realize all finite systems separately, but their source potentials cannot stay bounded. Compactness of the mass measures by itself gives no global rank, since the valuation kernel is unbounded. An independent bound uniform in the horizon, for the same source, is essential. This also shows exactly where even optimal finite-stage synthesis encounters the escape obstruction.

## Necessary regularity failure on the completion

For either proposed global rank, lower semicontinuity follows by writing H_μ(x)=Σ_{k≥1} μ(x+2^k Z₂). Each summand is constant on level-k cylinders. Any uniformly debiting H finite on ordinary inputs must be unbounded on each odd open cylinder. For any chosen ordinary n_0 in that cylinder, take sufficiently many complete valley bits from n_0 to fix the specified binary residue, append N full (1,1) valleys, and realize the extended prefix by sufficiently large ordinary inputs (inverse parity prefixes are a full residue modulo the total clock on Z₂; adding arbitrarily large multiples of that modulus gives positive inputs). Every step of the finite path then stays above 1. Its initial H is at least Nδ. Thus {H>M} is dense and open for every M and {H=∞} is residual in the odd completion. On the other hand it is Haar-null, since integrating H against normalized odd Haar gives 2μ(total) by Tonelli. This need for large potential values on completion points is compatible with finiteness at each ordinary positive integer.

In particular bounded densities cannot implement the rank. More strongly no absolutely continuous density f of finite entropy ∫ f log(1+f) can do so. With odd Haar, v=v₂(x−r) has a uniform finite exponential moment ∫exp(αv) for any 0<α<log 2. The elementary Young bound f αv≤f log(1+f)+exp(αv) gives a uniform finite bound on H across x. The L¹ interpolation construction is therefore necessarily irregular for a proper unbounded F.

The positive interpolation theorem removes diffuse representability as an independent obstruction. Finding an ordinary debit for a measure specified independently of termination, or exhibiting a positive ordinary orbit contradicting termination, remains the substantive missing step.
