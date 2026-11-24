# Free tours, doublings and odd predecessors at a fixed height

The D3 positive progression has the optimal exponential order among direct predecessors from the following three free clock choices. This is a written counting result; D3's ordinary merger identity and the direct obstruction at 55 are kernel-checked separately.

Fix H≥1 and n=1+3ᴴv, where v ranges over positive 3-adic units in the ordinary integers. One may also require v≡2 modulo 4. Choose any number s of inverse positive-cycle tours around 1, then any j inverse doublings and finally any d consecutive inverse odd steps. An inverse tour replaces 1+3u by 1+4u. An inverse doubling replaces y by 2y and an inverse odd step replaces y by (2y−1)/3 when this is integral. All the powers below are ordinary integer powers.

Write a=log(4/3)/log(3/2), b=log(2)/log(3/2)=a+1. The set of v for which some three-clock word yields a positive smaller m has a relative natural density between c·3 to the power −aH and C·3 to the power −aH, with absolute positive constants independent of H.

**Proof.** Necessarily s≤H. Put t=H−s, y=1+4ˢ3ᵗv. The guard and exact result are

$$3^d\mid 2^jy+1,\qquad m+1=(2/3)^d(2^jy+1).$$

When the divisibility holds, every intermediate odd inverse is integral because after i such steps the current value plus one equals 2ⁱ(2ʲy+1)/3ⁱ. The coefficient of 3ᴴv in m+1 is μ=(4/3)ˢ2ʲ(2/3)ᵈ. If d=0, the output is at least n. If 1≤d≤t, then 3ᵈ divides 2ʲ+1. The constant term in m is at least 2ᵈ−1≥1, and μ≥(3ᵈ−1)2ᵈ/3ᵈ>1. Thus a successful word has d>t.

Size forces μ<1+2/(3ᴴv)<2. Taking logarithms gives

$$d-t>aH+b(j-t)-b.$$

At t>0 the guard forces 3ᵗ to divide 2ʲ+1. Then j is odd and v₃(2ʲ+1)=1+v₃(j); this follows by factoring an odd power with exponent prime to three and repeatedly expanding a cube. Hence j≥3 to the power t−1. At t=0 let the lower bound on j be zero.

For fixed t,j,d satisfying the necessary conditions, the guard gives one residue for v modulo 3 to the power d−t, because 2ʲ4ˢ is a unit there. Its relative density among units is at most (3/2)·3 to the power −(d−t), also after the coprime restriction modulo 4. Sum this geometric bound first over d using the strict logarithmic inequality. The total is at most a constant times

$$3^{-aH}\sum_{t\ge0}3^{bt}\sum_{j\ge j_{min}(t)}3^{-bj}.$$

The double sum converges, since j_min(t)=3^(t−1) for positive t. To justify ordinary densities of the infinite union, first restrict to v≤X. A positive successful word has 2ᵈ≤m+1<n+1 from the divisibility guard. The coefficient bound yields j=O(d+1). For each fixed H, there are O_H((log(X+2))²) potentially nonempty triples. The additive O(1) rounding error per congruence class, including the restriction modulo four, is therefore o(X). The same convergent series bounds the upper density of the complementary tails after any finite list of triples, with the tails tending to zero for fixed H. Finite unions have natural density, so the whole union does too.

For the lower bound, D3 takes s=H, j=0, d=ceil(aH). It occupies one unit class and has relative density (3/2)·3 to the power −ceil(aH). This completes both bounds.

The order statement concerns this single prescribed ordering and endpoint n. More general schedules and future mergers remain available. At the witnessed source n=55 the kernel-checked result excludes every smaller direct predecessor, regardless of its schedule. [Positive theorem and scope](README.md)
