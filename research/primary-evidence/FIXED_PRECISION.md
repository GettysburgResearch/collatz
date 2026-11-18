# Fixed excess precision from the geometric clock

**PROPOSED.** For the ordinary odd Syracuse transfer $L$ on $\mathbb Z_3$ with Haar probability $\lambda$, put $g_n=L^n1$. For each fixed locally constant real function $f$ and every $A>0$,
$$
 \|L^nf-\lambda(f)g_n\|_{L^1(\lambda)}=O_{A,f}(n^{-A}). \tag{1}
$$
Consequently there is an absolute $c>0$ such that every nonnegative local $f$ satisfies
$$
 L^nf(t)\ge c\lambda(f)\,1_{3\nmid t}
 \quad(t\in\mathbb Z_3,\ n\ge N(f)). \tag{2}
$$
These imply the [every-depth pointwise convergence theorem](../native-pressure-20261118/EVERY-DEPTH.md) with its original stationary-density and ordinary Cesàro identifications. In deriving (1)–(2) below, the only non-elementary analytic input is the renewal estimate in the published proof of Tao's Proposition 1.17. The natural-depth joint clock has prior work by Jaan Allikvere. The positive selected families and arithmetic smoothing used for (2) are due to N. El Jaouhari. The argument here explains why a deficit proportional to the length and a lower bound at each individual clock total are unnecessary for this consequence. [Tao, Sections 6–7](https://doi.org/10.1017/fmp.2022.8) · [Allikvere](https://doi.org/10.5281/zenodo.21499244) · [El Jaouhari](https://doi.org/10.5281/zenodo.23377671)

## A natural-depth mixing estimate retaining the clock

Let $a_i$ be independent with $\Pr(a_i=h)=2^{-h}$ for $h\ge1$, $S_i=\sum_{v=1}^ia_v$, and $\beta_i=\sum_{v=1}^i3^{v-1}2^{-S_v}$. A dyadic rational defines an ordinary residue at each ternary modulus. Denote the joint mass vector at spatial depth $m$ by $P^{(i)}_m(z,s)=\Pr(\beta_i=z\bmod3^m,S_i=s)$. Write $A_k$ for averaging the spatial argument on each fiber modulo $3^k$, at each fixed clock. All norms of mass vectors in this section are unnormalized counting $\ell^1$ norms, summed over space and integer clock.

For every $B>0$,
$$
 \|(1-A_k)P^{(m)}_m\|_1=O_B(m^{-B}),\qquad 0.9m\le k\le m. \tag{3}
$$
We give the details to identify exactly how much of the published proof is used. For conductor $l$, every primitive character $\chi$ modulo $3^l$, and every bounded $H$ with $|H|\le1$,
$$
 |\mathbb E[\chi(\beta_l)H(S_l)]|\ll_B l^{-B}.
$$
This strengthening follows from Tao's displayed equations (7.4)–(7.6) and Proposition 7.3, rather than from the statement of Proposition 1.17 alone. Condition on the pair totals $a_{2i-1}+a_{2i}$ and on the last singleton if $l$ is odd. Conditional independence gives a product of the pair factors $f$ in (7.4), times a unit complex phase. The clock is measurable under this conditioning. In (7.5) the resulting expectation of the product of absolute factors is bounded by the white-point estimate of Proposition 7.3 and Lemma 7.2. The possible last singleton is independent of all the pairs. The same estimate holds for a length greater than $l$, since later terms vanish modulo $3^l$ and averaging their independent clock replaces $H$ by another bounded function.

Here is a direct collision argument for the conversion to (3). Split a natural length $m$ after $r=\lfloor17m/20\rfloor$ letters. Discard prefix totals below $d_0=\lceil m\log_2 3\rceil$ and full totals above $4m$, costing $O(e^{-c m})$ in mass by geometric Chernoff bounds. Set $u=1+1/(4m)$ and $f_d(z)=\Pr(S_r=d,\beta_r=z\bmod3^m)$. For fixed $d$ the nonnegative integer numerators $B_w=2^d\beta_w$ of the words are distinct: recover the final valuation from $v_2(B_w-3^{r-1})$ for $r\ge2$, divide by the corresponding power of two and iterate; the last single exponent follows from the specified total. Each earlier distinct numerator in the same residue class is separated from $B_w$ by a positive multiple of $3^m$. Counting each unordered pair once therefore gives
$$
 3^m\sum_z f_d(z)^2\le3^m2^{-d}\Pr(S_r=d)+2\mathbb E[\beta_r;S_r=d].
$$
The first term's prefactor is at most one for the retained $d$. With $A=u/(2-u)$ and $D=u/(4-u)$ one has
$$
 \mathbb E u^{S_r}=A^r=O(1),\qquad
 \mathbb E[u^{S_r}\beta_r]=\sum_{i=1}^r3^{i-1}D^iA^{r-i}=O(m)
$$
because $A,3D\le1+1/m$. Thus
$$
 (\sum_{d\ge d_0}u^{-d})3^m\sum_{z,d\ge d_0}u^d f_d(z)^2=O(m^2).
$$
For a spatial frequency $\xi$ with $j=v_3(\xi)<m-k$, the suffix character in $\beta_m=\beta_r+3^r2^{-S_r}\beta'_{m-r}$ has conductor $l=m-r-j\gg m$. The suffix length $m-r$ is at least $l$. Let $h_t(\eta)$ be the unnormalized spatial Fourier transform of the suffix mass at exact clock $t$ and modulus $3^{m-r}$. Parseval in its integer clock, followed by the preceding bounded-clock estimate with $H(s)=e^{2\pi i\theta s}$, gives $\sum_t|h_t(2^{-d}\xi)|^2\ll_{B'}m^{-2B'}$, uniformly in $d$ and the retained frequencies.

The full spatial transform at overall clock $s$, with only the prefix-total restriction imposed, is $\sum_{d\ge d_0}\widehat f_d(\xi)h_{s-d}(2^{-d}\xi)$. Cauchy–Schwarz with weights $u^{-d}$, then summation over clocks and high frequencies and spatial Plancherel for $f_d$, bounds its total squared magnitude there by $O_{B'}(m^{2-2B'})$. For each clock the spatial $\ell^1$ norm of the high-frequency projection is at most the square root of its unnormalized Fourier squared sum. There are at most $4m$ relevant clocks. Cauchy–Schwarz over these clocks completes (3), taking $B'>B+2$. Discarded nonnegative mass costs at most twice its total in the oscillation norm.

## Removing one letter without losing a power of the spatial modulus

Fix a spatial depth $m$. On joint mass vectors $(z,s)\in(\mathbb Z/3^m)\times\mathbb Z$ let $R$ increment $s$ by one, acting by pushforward, and let $D_i$ be pushforward by $(z,s)\mapsto(z+3^i2^{-s},s)$. Both are permutations and commute with every $A_k$ since spatial averaging commutes with translations at each fixed clock. Appending an inner letter at position $i+1$ gives the exact equality
$$
 P_m^{(i+1)}=D_i G P_m^{(i)},\qquad G=\sum_{a\ge1}2^{-a}R^a.
$$
In bounded operators on $\ell^1$, $G^{-1}=2R^{-1}-I$. Consequently undoing $k$ letters costs at most $3^k$ in $\ell^1$, also for the projected vectors $(1-A_j)P$. With $m=n+k$ and $k$ fixed, (3) gives
$$
 \|(1-A_n)P_{n+k}^{(n)}\|_1\ll_{B}3^k(n+k)^{-B}. \tag{4}
$$
The same estimate holds for $k\le n/9$, with the stated exponential factor. For fixed local $f$ of precision $k$, the terminal input $X$ with Haar density $f\ge0$ gives output $\beta_n+3^n2^{-S_n}X$ of density $L^nf$. At depth $n+k$ it is the corresponding weighted average of translations of the clock slices, each a shift by a multiple of $3^n$. Its spatial average on depth $n$ is exactly $\lambda(f)g_n$. Spatial $\ell^1$–Haar $L^1$ conversion for normalized densities now gives (1) from (4) multiplied by $\lambda(f)$. Decompose a signed local $f$ into positive and negative parts.

## Positive approximation on one cylinder

We include El Jaouhari's unconditioned selected-block construction in the normalization needed here. Set $b_0=10^6$, $b_{i+1}=b_i+\lfloor b_i/100\rfloor$, $k_i=\lfloor b_i/4\rfloor$ and $d_i=\sum_{v<i}b_v$. Accept a block of length $b_i$ when $|S-2b_i|\le\lceil b_i^{3/5}\rceil$. Rejection has probability $O(\exp(-c b_i^{1/5}))$ by exponential Markov for the geometric sum. Each acceptance probability is positive, and their infinite product is positive. Denote by $K_i$ the sum of transfer operators of all accepted prefixes of length $d_i$. Appending an inner tail composes these operators on the right.

On profiles of ternary precision $h\le2b_i$ there is a bound
$$
 \|K_i v\|_\infty\le C(b_i+1)^2\|v\|_1, \tag{5}
$$
where $C$ is absolute and the right norm uses Haar probability. In fact there are $O(1+b_i)$ possible prefix totals, by geometric growth of the $b_j$. The slope of an accepted block satisfies $3^{b_j}2^{-S}\le16^{-(b_{j+1}-b_j)}$, since $\lceil b_j^{3/5}\rceil\le b_j/10$ and $b_{j+1}-b_j\le b_j/100$. Thus prefix slopes satisfy $\omega\le16^{b_0-b_i}$, so $3^h\omega$ is bounded absolutely. Prefix offsets are also bounded by one absolute constant $B_0$: block $j$ has offset at most $2^{b_j}$, multiplied on composition by at most $16^{b_0-b_j}$. At fixed total, the physical input lifts $(z-\beta_w)/\omega$ landing at a fixed integer representative $z$ are distinct integers in an interval of length at most $B_0/\omega$, by numerator injectivity above. In any one class modulo $3^h$ their total slope is at most $B_0/3^h+\omega$. Summing over classes and totals proves (5). The estimate applies to signed $v$ by positivity.

Consider the nonnegative local functions $u_i=K_i g_{k_i}$ of integrals equal to the prefix acceptance probabilities. They are uniformly Cauchy. Indeed inside $K_i$ replace the next selected block followed by $g_{k_{i+1}}$ by the unrestricted profile $g_{b_i+k_{i+1}}$. The $L^1$ error is the next block rejection probability, since each word transfer preserves integral times its geometric probability. Replace this unrestricted profile by $g_{k_i}$ at further cost $O_A(k_i^{-A})$ by Tao's Proposition 1.14. The precision $b_i+k_{i+1}$ is at most $2b_i$; multiplying the two errors by (5) gives a summable series. The uniform limit is continuous and has positive integral. Thus there is a fixed unit cylinder and $c_0>0$ on which $u_i\ge2c_0$ for all sufficiently large $i$.

For any large length $n$ choose $i$ with $d_i+k_i\le n<d_{i+1}+k_{i+1}$. Then $t=n-d_i$ satisfies $k_i\le t<b_i+k_{i+1}\le1.26 b_i$. Normalize a nonzero local $f\ge0$ to integral one. Its precision is fixed, so $t+\operatorname{prec}(f)\le2b_i$ eventually. By (1), Proposition 1.14 and (5),
$$
 \|K_i L^t f-u_i\|_\infty
 \le C(b_i+1)^2(\|L^tf-g_t\|_1+\|g_t-g_{k_i}\|_1)=o_f(1).
$$
By positivity $L^nf\ge K_i L^t f$. This proves the fixed floor $c_0$ on that cylinder, independent of $f$ after its onset. For any unit target choose one bounded outer exponent $1\le v\le2\cdot3^h$ so $(2^v t-1)/3$ belongs to this cylinder modulo $3^h$. This is possible since $2$ generates the units modulo $3^{h+1}$. The extra step contributes at least $3\,2^{-2\cdot3^h}c_0$. This proves (2). The rest of the every-depth argument uses only (2), martingale projection, and its residual integral decomposition.

The use of Proposition 1.14 above may alternatively be deduced from (3): sum out the clock, use projectivity of the spatial laws, and chain successive depth ratios between $0.9$ and $0.95$ to reach any coarse depth. The resulting geometric series is $O_A(k^{-A})$. Thus the paired renewal bound from Tao's Section 7 suffices as the single non-elementary estimate in this proof.

The loss $3^k$ in the general inverse argument has a real obstruction. Use an alternating clock $(-1)^s$ multiplied by a primitive spatial character of conductor $n+1$ at ambient depth $n+k$. One may use the finite even clock $s\bmod 2\cdot3^{n+k-1}$, or truncate to an interval in the integer clock and pass to arbitrarily long intervals. This vector has zero projection under $A_n$. During removal of the last $k-1$ letters ($i\ge n+1$), each spatial translation is invisible to its character and $G^{-1}$ multiplies the alternating clock by $-3$. The last inverse has lower norm bound one, since its forward operator has norm at most one. Thus the projected inverse operator norm is at least $3^{k-1}$. A fixed or logarithmic deficit can be combined with arbitrary polynomial natural-depth rates. A fractional deficit is a genuinely stronger regime than this general inverse estimate supplies.
