# A positive real-offset test for ordinary escape

**PROPOSED, source-qualified.** Let $U$ be the ordinary accelerated odd map, and keep $g_Q(t)=\sum_{U^Qx=t}J_w$ and the normalization of [the finite harmonic criterion](../unsafe-return-weights/SIGNED_MASS.md), commit `1602f45`. Write $t=J_w x+F_w$ for the **real** affine offset of a length-$Q$ odd word. For $0<\theta<1$ define
$$
 B_Q(\theta)=\sum_{\substack{t\le2\cdot3^Q\\t\ \mathrm{odd}}}\frac1t
 \sum_{\substack{U^Qx=t,\ \mathrm{path\ pairwise\ distinct}\\ F_w\ge\theta t}}J_w.
$$
Every positive orbit is eventually periodic if and only if $\liminf_{Q\to\infty}B_Q(\theta)/Q=0$ for every fixed $\theta>0$. In the eventual-periodic direction $B_Q(\theta)$ is bounded in $Q$ for each $\theta$. One may equivalently test $\theta=1/k$ for integers $k\ge2$. The test has positive terms and no baseline subtraction. It discards words near the zero-relative-offset part of the joint law. Every retained target satisfies $t\le((3/2)^Q-1)/\theta$, by the maximal real offset for positive valuations. At fixed $Q,t$ the legal-word sum is interpreted as a nonnegative convergent series, as for $g_Q(t)$ itself.

The exact product identity gives
$$
 F_w/t=1-\prod_{i<Q}(1+1/(3U^i x))^{-1}.
$$
On a simple path avoiding all states $\le R$, the right side is at most $\sum_{i<Q}1/(3U^i x)$, which tends to zero uniformly as $R\to\infty$ by [the simple-segment reciprocal bound](CRITICAL_MOMENT.md). Fixing $\theta$ therefore forces each marked path to visit a bounded state $s\le R(\theta)$. If all orbits are eventually periodic, the targets then belong to the finite union of forward orbits of those states. The pointwise uniform bounds on $g_Q(t)$ at each of these finitely many ordinary targets give $B_Q(\theta)=O_\theta(1)$. Removing repeated visits in the definition prevents long runs around potentially large periodic cycles from mimicking a large simple-path distortion. [Ordinary finite-height bounds and external inputs](../native-pressure-20261118/ORDINARY-DENSITIES.md)

Conversely take a divergent odd ordinary unit $n$, available upon advancing at most one odd step on any nonperiodic orbit. Put $y_j=U^j(n)$ and $D_j=J(n,j)$. Along the path from $n$ to $y_j$, the real offset is at least $y_j/(3n+1)$ for $j\ge1$ by the first product factor. All longer words through $n$ have at least this offset by positivity of composition. Their paths are necessarily simple since they belong to a nonperiodic component. The distinct $y_j$, $1\le j\le Q$, lie below $2\cdot3^Q$ for all sufficiently large $Q$ because $y_j\le(n+1)(3/2)^j$. Consequently
$$
 B_Q(1/(3n+1))\ \ge\ \sum_{j=1}^Q\frac{D_j}{y_j}g_{Q-j}(n).
$$
Here $D_j/y_j\to r(n)/n>0$ by the reciprocal-product bound. The bounded sequence $g_k(n)$ has a strictly positive Cesàro mean $b(n)$ by the ordinary canonical trace. The normalized right side tends to $r(n)b(n)/n$, proving the equivalence. Thus any nonperiodic component puts linear harmonic mass on words whose real offset is a fixed positive fraction of the physical target. Bounded-real regularity alone misses exactly these inherited low-ancestor contributions. [Valbuena, canonical Cesàro trace](https://doi.org/10.5281/zenodo.23025885)

## Why Haar bounds alone do not settle the finite test

There are positive mean-one densities $f$ on $\mathbb Z_3$ with every finite moment, exponentially accurate $L^1$ martingale truncations $f_Q$, and
$$
 \liminf_Q\frac1Q\sum_{\substack{t\le2\cdot3^Q\\ t\ \rm odd}}f_Q(t)/t>\tfrac12\log3 .
$$
Fix an integer $K\ge3$. For each sufficiently large $j$ choose an odd $t_j$ in $[j^2,j^2+j]$ outside all previously chosen cylinders modulo $3^{Ki}$. Excluding earlier cylinders with small moduli removes $O(j\sum_{i\ge j_0}3^{-Ki})+O(\log j)$ integers: any earlier modulus $3^{Ki}>2j^2$ excludes none, as all earlier $t_i<t_j$ and are already below $j^2$. There are $O(\log j)$ remaining moduli. Their total density can be made arbitrarily small by taking $j_0$ large. Hence the new odd point exists. The cylinders $C_j=t_j+3^{Kj}\mathbb Z_3$ are disjoint. Put $d=\sum_{j\ge j_0}t_j3^{-Kj}$ and
$$
 f=1-d+\sum_{j\ge j_0}t_j{\bf1}_{C_j}.
$$
Its finite moments follow from $t_j=O(j^2)$ and exponential cylinder decay, and $\|f-f_Q\|_1\le2\sum_{Kj>Q}t_j3^{-Kj}\ll Q^2 3^{-Q}$. Every $j\le Q/K$ contributes its height $t_j$ at the sampled point $t_j$, giving a slope at least $(1-d)\log3/2+1/K>\log3/2$ for large $j_0$. This countermodel does not satisfy the Syracuse transfer; it isolates the need for arithmetic control of the sampled representatives. In particular arbitrarily good bounded-real $L^p$ estimates in isolation do not provide such control. The actual offset-cone bound $B_Q(\theta)=o(Q)$ on all ordinary targets remains open.

## Recovering the whole escape mass without a signed subtraction

Let $m_C=\lim_j r(y_j)b(y_j)/y_j$ be the mean-one normalized canonical mass of a nonperiodic component, so it equals $(3/2)H_C$ in the signed criterion. The full moving-clock transport gives
$$
 \lim_{\theta\downarrow0}\liminf_Q B_Q(\theta)/Q
 =\lim_{\theta\downarrow0}\limsup_Q B_Q(\theta)/Q
 =\sum_{C\ \mathrm{nonperiodic}}m_C .
$$
For fixed $\theta$, every marked word hits one of the finitely many low states $s\le R(\theta)$. The finitely many bounded orbits of these states contribute $O_\theta(1)$ as before. Within each of their nonperiodic components, their forward union is contained in one spine and a finite set; after the low-state hit at most $Q$ steps remain, so only the first $Q+O_\theta(1)$ vertices of that spine occur. On a spine anchored at $n$, using the notation of the [uniform profile theorem](SPINE_CLOCK_PROFILE.md),
$$
 \frac1Q\sum_{j=0}^{Q}g_Q(y_j)/y_j
 =\frac1Q\sum_{j=0}^{Q}(D_j/y_j)P_j(Q-j)\longrightarrow m_C .
$$
Indeed the $P_j$ are uniformly bounded and converge uniformly to $P$, whose positive-age Cesàro mean is $n m_C/r(n)$; also $D_j/y_j\to r(n)/n$. Boundedly many additional terms are harmless by the ordinary uniform height bound $g_Q(y)/y\ll1$ for nonperiodic $y$. This proves the upper bound by the sum of the masses of these finitely many components.

For the reverse direction choose any finite set of nonperiodic components and advance each anchor $n_C$ far enough that $r(n_C)b(n_C)/n_C$ approximates its $m_C$ from below. For $\theta\le\min_C(3n_C+1)^{-1}$ the previous lower-bound words through those anchors qualify, and targets in distinct components are disjoint. Take the lower limit in $Q$, let the anchor errors shrink, and then take the supremum over finite component families. Finiteness of the total mass follows from the signed identity or the antichain-width estimate. This double-limit formula does not assert an exchange of limits or convergence at each individual $\theta$.

## The limiting distribution away from zero

The normalized simple-word measure on relative offset $z=F_w/t$ has a vague limit $\mu$ on $(0,1]$. In particular $B_Q(\theta)/Q\to\mu([\theta,1])$ at every continuity threshold, and $\mu((0,1])=\sum_Cm_C$. Its distribution can be reconstructed from finite ordinary traces.

To see this, mark for every odd $s\le R$ whether the length-$Q$ path visits $s$ at a time strictly before its endpoint. Approximate its distortion by $z_R=1-\prod_{s\text{ marked}}(1+1/(3s))^{-1}$. On simple paths $|z-z_R|$ tends uniformly to zero with $R$ by the simple-segment reciprocal tail. The total normalized simple-word mass is bounded uniformly for large $Q$ by the signed identity applied to the unrestricted positive mass. Thus replacing a continuous observable $\psi(z)$ by $\psi(z_R)$ incurs uniformly vanishing integral error.

Take $\psi(0)=0$. On the finite Boolean cube, $\psi(z_R)$ is a multilinear polynomial in the visit indicators with zero constant term. Every nonempty monomial, marking a fixed nonempty set $E$, has a limiting normalized integral. If the marked points are in periodic components, the possible endpoints form a finite set and their normalized contribution tends to zero. If no forward orbit visits them all, the monomial vanishes. Otherwise in a nonperiodic component write $s$ for the earliest marked point in their unique forward ordering and $d$ for its distance to the last marked point. With $y_j=U^js$, the normalized integral for all sufficiently large $Q$ is exactly
$$
 Q^{-1}\sum_{j=d+1}^Q J(s,j)g_{Q-j}(s)/y_j
 \ \longrightarrow\ r(s)b(s)/s .
$$
All sources in this formula have simple paths, and the lower cutoff accounts for excluding the endpoint. This proof includes multiples of three, for which the positive-depth inverse weights vanish. For fixed $R$ it gives a finite inclusion-exclusion procedure in terms of ordinary traces. Passing to $R\to\infty$ defines a bounded positive functional on continuous functions vanishing at zero, hence a finite measure on $(0,1]$. Approximation from above and below gives convergence of cone counts at its continuity thresholds. Taking such thresholds decreasing to zero in the double-limit identity yields its total mass. The argument leaves possible atoms at individual positive thresholds.

## Identification with whole-orbit distortion

Let $E$ denote normalized odd logarithmic mean, $V_\infty$ the reciprocal of the whole-orbit correction product, and $\delta=\log(4/3)/2$. For continuous $\psi$ with $\psi(0)=0$,
$$
 \int\psi\,d\mu=\delta E[V_\infty {\bf1}_{\rm escape}\,\psi(1-V_\infty)] .
$$
Indeed mark every odd state visited on the **entire** escaping orbit. For a nonempty visit monomial supported on a compatible escaping chain with earliest state $s$, its integral against the weighted source mean is $\delta r(s) E[W_s]=r(s)b(s)/s$, by the [canonical visit formula](../unsafe-return-weights/SIGNED_MASS.md). Here $W_s$ is the previsit product, defined to be zero off the visit event. Other monomials have zero weighted mean. This matches every truncated polynomial above. The simple-orbit reciprocal tail controls the whole-orbit truncation uniformly, proving existence of the mean and the identity.

Consequently every positive cone threshold is a continuity point. More precisely, $\mu$ is either zero or singular continuous, has lower Hausdorff dimension one when nonzero, and is supported on a compact Lebesgue-null subset of $[0,1]$. To verify this, condition the ordinary limiting source law on its global minimum $t$. Escape is then determined by the orbit of $t$. On escaping cells one has
$$
 -\log_2 V_\infty=R_* -\log_2 r(t)
$$
with $R_*$ the terminal residue up to the first hit of $t$. The all-source terminal law applies also to odd natural sampling: subtract the even subsample, whose terminal pair equals that of its halved input, from the entire interval count. Partial summation then gives the same odd logarithmic law. Minimum tightness permits summing the individual cell identities. On each escaping cell the displayed translation followed by $u\mapsto1-2^{-u}$ is bi-Lipschitz on the bounded relevant range. The pushforward therefore charges no set of dimension less than one and has compact null support, by the [terminal dimension theorem](../terminal-residue/REAL_DIMENSION.md) and [terminal support theorem](../terminal-residue/SUPPORT.md). Multiplication by the bounded positive weight $\delta V_\infty$ preserves these properties. Over escaping cells with $t\to\infty$, the whole simple trajectory stays at least $t$, so the reciprocal packing tail forces the supports uniformly toward zero. Their union with zero is thus compact and null. In particular absolute continuity of this limiting cone measure is equivalent to eventual periodicity of every positive ordinary orbit.

## Localization obstruction for arithmetic-progression estimates

In the countermodel above the entire excess can be placed arbitrarily close to the single ordinary ternary point $1$, already at heights $O(Q\log Q)$. More precisely let $L_j=\lfloor\log_3\log j\rfloor$, $t_j=1+2\cdot3^{L_j}(3j+1)$, and use the same spikes $C_j$ and weights for sufficiently large $j\ge j_0$. These odd centers have $v_3(t_j-1)=L_j$ and $t_j\asymp j\log j$. Distinct levels give disjoint cylinders because $L_j<Kj$. Within one level, for $i<j$ we have $j\le i^3$, hence $0<t_j-t_i<3^{Ki}$ for all sufficiently large $i$. The limiting density has all finite moments and exponential martingale approximation as before. Its martingale values converge pointwise at every ordinary integer: at a point other than $1$, all sufficiently late centers differ from the point modulo a fixed power of three; at $1$, the unresolved centers coinciding modulo $3^Q$ require $j\ge\exp(3^Q)$, and their projected contributions tend to zero.

For every fixed cylinder $A$ modulo $3^a$, write $\lambda(A)=\int_A f\,d\mathrm{Haar}$. Then the exact progression discrepancy is
$$
 \lim_{Q\to\infty}\frac1Q\sum_{\substack{t\le2\cdot3^Q,\ t\ {\rm odd}\\t\in A}}\frac{f_Q(t)}t
 =\tfrac12\log(3)\lambda(A)+\frac1K{\bf1}_{1\in A}.
$$
Indeed for resolved $j\le Q/K$ the harmonic sum on $C_j$ equals the first term $1/t_j$ plus $(Q-Kj)\log(3)/(2\cdot3^{Kj})+O(3^{-Kj})$, by integral comparison over the odd progression. Here $t_j$ is its first representative. Summing the latter terms after multiplication by $t_j$ gives the Haar baseline with bounded error since $\sum jt_j3^{-Kj}<\infty$. A fixed $A$ contains every sufficiently late cylinder if $1\in A$, and otherwise none; the finitely many larger early cylinders intersecting $A$ contribute their usual restricted baseline and bounded errors. For $Q/K<j\le Q^2$, each unresolved projection has height $t_j3^{Q-Kj}$ on the cylinder of $t_j$ modulo $3^Q$. Its only sampled representative is $t_j$, so these unresolved contributions sum to $O(1)$. The remaining $j>Q^2$ cost at most $\sum t_j3^{Q-Kj}=o(1)$. Finally restriction to $t\le C Q\log Q$ for a sufficiently large fixed $C$ retains all the resolved first terms, while the baseline logarithm there is only $O(\log Q)$. Thus sampling only this moderate range, divided by $Q$, gives $K^{-1}{\bf1}_{1\in A}$. The anomalous progression measure is an atom even though all fixed ordinary martingale values converge. These examples do not obey the Syracuse transfer.
