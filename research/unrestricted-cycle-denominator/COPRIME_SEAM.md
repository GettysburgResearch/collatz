# One seam for the origin energy test at coprime length and weight

Assume a primitive positive shortcut word has L≥2 letters, K ones,
gcd(L,K)=1 and D=2^L−3^K>0. Repeating it k times does not by itself
extend the [exact periodic gauge](ORIGIN_ENERGY.md). Any n dividing
both kL and kK divides k, and each block width (k/n)L returns to the
same physical phase.

Instead choose 1≤b<L with bK≡1 mod L, and a=(bK−1)/L. From any
cyclic cut, traverse b laps in L consecutive length-b blocks. Their
starts visit every physical phase because gcd(b,L)=1. For their
weights k_i and affine numerators C_i define

    s_0=0,  s_(i+1)=s_i+k_i−a,   S=max_(0≤i≤L) s_i,
    λ=3^a/2^b,   f_i=3^(S−s_(i+1)) C_i/2^b,
    z=(Σ_(j=0)^(L−1) λ^(L−1−j) f_j)/(1/3−λ^L),
    g_i=f_i+(2/3)z 1_(i=L−1).

All these quantities are explicit in the word. The denominator in z
is positive because λ^L=(3^K/2^L)^b/3. An integer realization requires

    Σ_(1≤t<L) |ĝ(t)|²/|exp(2πit/L)−λ|² ≥ (L²−1)/12,

and max over cyclic intervals I of |Σ_(i∈I)(g_i−mean(g))|≥(L−1)/2,
with the Fourier normalization in the linked note.

Indeed write x_i for the actual block entry and put Z_i=3^(S−s_i)x_i.
These are distinct integers for i=0,...,L−1 since their ternary
valuations distinguish different gauges and the physical phases are
distinct. The unclosed recurrence is Z_(i+1)=λ Z_i+f_i. Here s_L=1
and x_L=x_0, so Z_L=Z_0/3; iterating gives Z_0=z. Replacing the
last output with Z_0 adds exactly (2/3)z at the last step. Parseval
and the centered discrepancy proof now apply to the periodicized
forcing g. Only the multiplicative gauge mismatch is bounded by a
constant: the additive impulse (2/3)z can be arbitrarily large.

For a nonvacuous finite example, W=1101010 has (L,K)=(7,4), b=2
and unnormalized physical input 101/47. The normalized variance
equals 204860/108241<4, so the energy test rejects it. There is also
an infinite family of rejections: W=10^(L−1), L≥4, has K=b=1 and
a=0. Its first state is 1/(2^L−3), the first normalized state is
3/(2^L−3), and each later normalized state is at most
(1+3/(2^L−3))/2<1. Their variance is less than one, below the
threshold. Neither example proves rejection for all near-critical
coprime words.
