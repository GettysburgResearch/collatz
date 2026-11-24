# Exact proportions for weighted stopping clocks

Use the shortcut map T(n)=n/2 on even n and T(n)=(3n+1)/2 on odd n. Write B for the set of positive n that hit 1 and δ for its ordinary natural density. Fix integers w_e,w_o≥0 and m≥2 with gcd(m,w_e,w_o)=1. For n∈B let W(n) be the sum of w_e over even inputs and w_o over odd inputs **strictly before the first hit of 1**. Thus W(1)=0. Assign a separate symbol ∞ on the complement of B, and write B_c={n∈B:W(n)≡c mod m}.

**Written theorem.** For each c modulo m and every fixed automatic set S in any integer base,

    |B_c ∩ S ∩ [1,X]| = (δ/m) |S ∩ [1,X]| + o(X).

The symbol ∞ has coefficient 1−δ. This includes shortcut stopping time (w_e,w_o)=(1,1), ordinary unaccelerated stopping time (1,2), and number of odd inputs (0,1). If the gcd is greater than one, division by that common gcd with m yields the corresponding uniform law on the reachable subgroup.

PR #200 already gives the arbitrary-base sparse-error obstruction and constructs disjoint ordinary blocks of every weighted residue with prescribed starting dyadic digits in every fixed relative interval, using only its stated predecessor inputs. Its Theorem C gives an error count of order at least X^0.84/log(2X) with Krasikov–Lagarias. Here finite-clock synchronization and a natural mean yield exact limiting coefficients, including on nonperiodic automatic tests. No local formalization of the density or synchronization inputs is claimed. [PR #200, LOCAL_BLOCKS.md](https://github.com/GettysburgResearch/collatz/blob/c43fcbe6643c3d816975a4fb4328dc19dbdac6fb/research/regularity-rigidity-20261124/LOCAL_BLOCKS.md) · [PR #200, AUTOMATA.md](https://github.com/GettysburgResearch/collatz/blob/c43fcbe6643c3d816975a4fb4328dc19dbdac6fb/research/regularity-rigidity-20261124/AUTOMATA.md)

## Adjacent changes

For fixed clock H, the inputs n and n+1 coalesce at that clock with **equal counts of odd inputs** on a union of binary residue classes. Said Duran's Corollary C states that the proportion of the good classes tends to one as H→∞. Equality of odd counts makes the affine lifts agree throughout each good class. For n>2^H, both trajectories stay above 1 up to the merger. Their first H steps therefore have equal weight, and their futures after the merger agree. They have identical weighted labels, including if both fail to reach 1. Removing finitely many small n at fixed H and then letting H tend to infinity proves that the set of adjacent label changes has ordinary density zero.

The equal-count condition matters here because equality of endpoints at unspecified clocks need not preserve the accumulated weight. The ordinary natural density δ and unweighted adjacent variation can be inspected in Valbuena's pinned formalization. For weighted labels we use the underlying equal-count cylinder statement and the preceding finite-floor argument. [Said Duran, Corollary C](https://doi.org/10.5281/zenodo.23003524) · [Exact finite-cylinder input and transfer, §3](https://rstation.ai/problems/collatz/papers/12) · [Valbuena, rows 16 and 18](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/basin-lean-claims.md)

## The nontrivial Fourier characters

Let 1≤l<m and ζ=exp(2πil/m). Set f(n)=ζ^W(n) on B and f(n)=0 elsewhere. We have |f|≤1 and Σ_{n≤X}|f(n+1)−f(n)|=o(X). Define F(X)=X^(-1)Σ_{1≤n≤X}f(n) for real X≥1. For fixed k≥1 and r∈{0,…,k−1}, the mean of f(kn+r) for 1≤n≤X equals F(kX)+o(1): compare all k positions in each disjoint length-k block, charging the differences to at most k times the total adjacent variation. Endpoints contribute O_k(1/X). No prior existence of a limit for F is used.

Put α=ζ^(w_e), ω=ζ^(w_o). The step recurrences f(2n)=αf(n) and f(2n+1)=ωf(3n+2) hold for n≥1, on both convergent and nonconvergent inputs. Only the source 1 is exceptional in the general weighted-step rule. The progression estimate gives

    F(2X)=α F(X)+o(1),       F(3X)=(α/ω) F(X)+o(1).

Consequently for every fixed a,b∈ℤ,

    F(2^a 3^b X)=α^a(α/ω)^b F(X)+o_{a,b}(1).

Positive powers follow by finitely many substitutions at fixed scales. A negative power follows by applying its positive-power identity at the reciprocal scale and multiplying by its inverse unit phase.

The character (a,b)↦α^a(α/ω)^b is nontrivial. Otherwise the order of ζ, which exceeds one and divides m, would divide both weights. Choose a residue pair (a₀,b₀) mod m where its value η differs from one. The subgroup ℤ log 2+ℤ log 3 is dense in ℝ because log 2/log 3 is irrational. Its multiple by m remains dense, as does its translate by a₀ log 2+b₀ log 3. Given ε∈(0,1), choose a fixed pair in that residue class with |a log 2+b log 3|<ε. Then λ=2^a 3^b lies within a factor exp(ε) of one and has the fixed phase η.

For |f|≤1, changing the cutoff from X to λX changes F by at most 2(1−exp(−ε))+O_λ(1/X). Combining with the fixed-pair identity gives

    |1−η| limsup_{X→∞}|F(X)| ≤ 2(1−exp(−ε)).

Letting ε↓0 proves F(X)→0. The zero character is the basin indicator with mean δ. Finite Fourier inversion now supplies mean δ/m for every B_c, and its indicator has the sparse adjacent changes already proved. The automatic testing lemma in AUTOMATIC_TESTS.md yields the displayed joint formula. The ∞ formula follows by taking the complement of B.

## Full fixed-length blocks

Fix 0<A<B', M≥1, d≥0 and r modulo 2^d. The number of starts n∈[AX,B'X] satisfying n≡r mod 2^d for which every one of n,…,n+M−1 lies in B_c is

    ((B'−A)δ/(m 2^d)) X + o(X).

First test the single value n by the periodic residue condition. A start with the correct initial color but an incorrect later color is within M−1 places of an adjacent change, costing o(X). Requiring the whole block to lie in the interval costs at most M additional starts. A disjoint family of linear size is obtained by retaining one compatible residue class modulo 2^d ceil(M/2^d), whose spacing is at least M; this fixes the period before taking the large-X limit. The same proof for the symbol ∞ has coefficient (B'−A)(1−δ)/2^d, possibly zero. For the single unweighted target set Anc(t), the coefficient is (B'−A)h(t)/2^d, where h(t) is its natural density.

An independent improvement of PR #200's constructive *lower bound* uses its existing bounded-multiplicity gluing with the external positive linear pool of odd ancestors of a fixed odd unit t. Any odd ancestor n divisible by three maps injectively under its first shortcut to a ternary unit before visiting t; the other n are already units. Each resulting unit, even or odd, has a bounded-clock odd-unit inverse as in PR #200. These bounded multiplicities preserve a positive linear count, yielding linearly many disjoint certified blocks of each fixed type. [Lau, v2, fixed-target lower bound](https://hexagonmath.org/2610.00249v2)

The positive and negative block proportions depend on δ. Their sum determines neither δ nor the missing convergence certificates on a positive-density automatic test. The dilation argument kills exactly the nontrivial clock characters; its zero character remains the original basin mass.
