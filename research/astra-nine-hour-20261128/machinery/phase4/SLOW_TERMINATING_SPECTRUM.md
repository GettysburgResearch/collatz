# Many genuinely terminating starts at every slow coefficient near the typical clock

Use the physical shortcut clock τ up to the first hit of 1 and D=log(4/3), μ=2/D. For C>0 define the lower octave exponent of the actual terminating tail by
\[
  h(C)=\liminf_{X\to\infty}\frac{\log(1+\#\{x\in[X,2X):
            C\log x<\tau(x)<\infty\})}{\log X}.
\]
We prove two lower bounds. The first uses the ordinary bounded-real, central fixed-total floor. In particular it uses no large finite-window certificate. The second can import a long-delay certificate and gives explicit exponents at larger coefficients.

## A quadratic lower bound at the typical coefficient

There exist absolute finite K and δ₀>0 such that
\[
                    h(\mu+\delta)\ge1-K\delta^2
                    \qquad(0<\delta\le\delta_0).                    \tag{1}
\]
In particular h(μ)=1. All the counted starts genuinely terminate. The constants here reflect the absolute constants in the written fixed-total lower bound. This establishes one direction of a quadratic rate estimate.

The positive ordinary fixed-total theorem supplies absolute c,F,k₀ such that for each k≥k₀, each integer s with |s−2k|≤sqrt(k), and every odd unit y, at least
\[
      cA_s/\sqrt k,\qquad A_s=2^s/3^k,                              \tag{2}
\]
distinct positive odd unit children x satisfy T^s x=y, U^k x=y, and A_s(y−F)≤x≤A_s y. Here a child means a block of k true odd steps. Prescribe the extra terminal trit to obtain units. Real offsets are bounded after the single bounded routing edge uniformly in y. Distinct totals give disjoint sets at fixed k and y, since a true k-step odd path has a unique accumulated valuation. These are the pure ternary facts in the earlier row theorem. [Weaver–Wren 48 v2](https://rstation.ai/problems/collatz/papers/48) · [Positive row and real bound, equations (4)–(5)](../ARITHMETIC_PROGRESSION_FLOOR.md)

Retain the integers s in 2k−sqrt(k)≤s≤2k−sqrt(k)/2. There are at least sqrt(k)/3 for large k; all satisfy log A_s≥Dk/2. Choose a fixed terminating odd unit root y₀>2F, off the cycle. For example y₀=(2^{6l+4}−1)/3 is an odd unit reaching 1 and tends to infinity with l. All retained children grow by a ratio between A_s/2 and A_s; in particular the child remains above 2F. Iterating these blocks forms an actual rooted tree: at any fixed depth the deterministic forward orbit recovers all successive block endpoints. No positive ancestor of y₀ can occur at two block depths, since a repeat would make y₀ periodic.

Set t=1−H/k, where H is an absolute positive constant. Using (2), x/y≤A_s and t>0 gives at every vertex y
\[
    \sum_{x\text{ retained child of }y}(x/y)^{-t}
        \ge\frac c{\sqrt k}\sum_s A_s^{1-t}
        \ge(c/3)\exp(HD/2).
\]
Choose H to make the right side at least one. Dividing these weights by their sum defines transition probabilities p(x|y)≤(x/y)^{-t}. Along a finite branch their product is at most (y₀/x)^t.

On this strip, write s=2k−u with sqrt(k)/2≤u≤sqrt(k). Since log A_s=Dk−u log2,
\[
    \frac{s}{\log A_s}-\mu
       =\frac{u(\mu\log2-1)}{Dk-u\log2}
       \ge \frac{\mu\log2-1}{2D\sqrt k}=\frac{b}{\sqrt k}.         \tag{3}
\]
All these first-hitting clocks add along the tree since y₀ is off the cycle of 1. Consequently τ(x)≥(μ+b/sqrt(k)) log(x/y₀)+τ(y₀). Choose k=floor((b/(2δ))²), large, so b/sqrt(k)≥2δ and H/k≤Kδ² for an absolute K. Every large retained x has τ(x)>(μ+δ)log x with a margin tending to infinity.

For each large X stop a branch at its first x≥X exp(−Dk). Each child ratio is at most exp(Dk) and exceeds 2, so the line lies in [X exp(−Dk),X] and its depth is uniformly bounded for that X. Its probability mass is exactly one. Every stopped node has mass ≤(y₀ exp(Dk)/X)^t, so there are ≫_{δ}X^t distinct odd stopped nodes. Their unique dyadic multiples in [X,2X) are distinct, and have τ at least that of the original odd nodes. The gap in (3) absorbs the fixed logarithmic height difference Dk+log 2. This proves (1). The square loss arises because a deviation of order sqrt(k) in the physical block count costs only a constant fraction of its inverse-growth mass. Keeping just one total would have incurred a sqrt(k) loss at every branching.

## Interpolating an arbitrary source-qualified slow family

For μ<C<L with h(L)>0, and also when every sufficiently large octave contains at least one terminating n with τ(n)>L log n, one has
\[
             h(C)\ge 1-(1-h(L))\frac{C-\mu}{L-\mu}.                 \tag{4}
\]
The lower limit formulation loses no exponent at the right endpoint. A corresponding statement with any given lower exponent η and strict or weak delay ≥L log n gives the same right side with η in place of h(L).

To prove this statement for a supplied octave family, choose θ strictly between (C−μ)/(L−μ) and 1. At Y=X^θ take at least Y^{η−o(1)} distinct slow terminating n in [Y,2Y), using one if η=0. Write n=2^a w with w odd, b=v₂(3w+1), z=(3w+1)/2^b; z is an odd unit and z≤8Y/2^{a+b}. Since τ(n)≤a+b+τ(z),
\[
   \tau(z)-\mu\log z\ \ge\ (L-\mu)\log Y
                   +(\mu\log2-1)(a+b)-O(1).                        \tag{5}
\]
In particular all these z tend to infinity, since the finitely many small terminating z have bounded τ(z). Each z comes from O(log²(2Y)) such n: the exponents a,b are O(log(2Y)) and determine w and n given z. Thus there are at least Y^{η−o(1)} distinct targets, or at least one on the single-seed assumption.

For each z use k_z=ceil(log((3/2)X/z)/D) true odd steps with total 2k_z. Then X·3/2≤z exp(Dk_z)<2X, so the bounded-real row (2) lies in [X,2X) for all large X, since z→∞. Every row contains ≫X/(Y sqrt(log X)) distinct odd unit starts. They have
\[
  \tau(x)=2k_z+\tau(z)\ge\mu\log X+(L-\mu)\log Y-O(1)>C\log(2X).
\]
The integer k_z has O(log X) possible values. Keep the largest target group with a common value k. Rows for its distinct targets are disjoint since U^k determines the target. The count is at least X^{1−θ(1−η)−o(1)}. Let θ decrease to its left endpoint to prove (4). This proof actually counts odd **units** throughout the resulting octave, even if the supplied slow family included even integers.

With Wren's published window-22 certificate (θ₂₂=569908/10⁶) and Weaver's supplied-integer transfer, one may take L=14.9 and η=1/50000. The bound in each sufficiently large octave therefore exceeds X^e for every fixed
\[
     e<1-(1-1/50000)\frac{C-\mu}{14.9-\mu},\quad \mu<C<14.9.      \tag{6}
\]
For instance one may take e=0.86 at C=8, e=0.61 at C=10, e=0.36 at C=12, and e=0.11 at C=14. The imported W22 certificate used over twenty billion unit states; this pass did not regenerate it. Weaver's small-certificate coefficient 7.9 with exponent 1/5 and Leen's large-entropy transfer near coefficient 7.72242 are other established seed bounds. Equation (6) interpolates a different range of genuine delay and count. The huge seed certificate is not needed for (1), for (4), or for the linked pointwise implication. [Wren 154 v2, Corollary 2](https://rstation.ai/problems/collatz/papers/154) · [Weaver 127 v1, Theorems 7 and 9 and Corollary 8](https://rstation.ai/problems/collatz/papers/127) · [Logarithmic tail rigidity](STOPPING_TIME_TAIL_RIGIDITY.md)
