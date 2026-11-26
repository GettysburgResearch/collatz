# A summable arithmetic part of the actual discordant landing weight

Take $R=81^j$, $d=\log_2 R$, $7R\le x=81n+r<8R$ with $0\le r<81$, and fix $0<c<1$. Set $h=\lfloor cd\rfloor$. The color can be any orbit-invariant two-coloring. Write $\mathcal D_j$ for the actual original children with different colors at $x,n$.

Fix $3/4<\beta\le1$. Put $y=\exp(\eta d^\beta)$, with a sufficiently small fixed $\eta>0$ depending on $c$. Call an integer $y$-rough when it has no prime divisor $\le y$. Then
$$
 \frac1R\#\{x\in\mathcal D_j:\ \exists\,0\le t\le h,             T^t n,\ T^t x\ \hbox{both }y\hbox{-rough}\}
 \ll_{c,\eta} (\log(2d))^2 d^{1/2-2\beta}.                         \tag{1}
$$
In particular actual discordant original children whose two physical arms are simultaneously prime at **some** one of these $O(d)$ clocks have summable normalized mass. At $\beta=1$ the upper bound is $O(d^{-3/2}(\log(2d))^2)$. A union over $O(d)$ times of the unconditioned two-dimensional sieve alone has only the borderline scale $d^{-1}$ up to logarithms. Here the gain comes from the independently available high part of each original integer after exposing its actual shared low bits.

For $1/2<\beta\le1$ there is also the one-arm bound
$$
 \frac1R\#\{x\in\mathcal D_j:T^{t(u)}z(u)\ \hbox{is }y\hbox{-rough}\}
 \ll_{c,\eta} (\log(2d))d^{-1/2-\beta},                           \tag{2}
$$
where the chosen time $0\le t(u)\le h$ and arm $z(u)\in\{n,x\}$ are arbitrary functions of the suffix $r$ and the entire joint $h$-bit source cylinder $u$. The same estimate bounds the normalized sum, over discordant sources, of the *fraction* of all $2(h+1)$ labeled observations that are rough, by averaging (2). Thus restricting to sources with at least any fixed positive rough fraction costs a summable total mass. The predicate need not be fixed in advance on every future basin mark: intersecting either counted set with any marked subset can only decrease its original mass. There is no asserted relative bound inside an arbitrary unrestricted record fiber.

### Complete source cylinders and a uniform upper-bound sieve

For fixed $r$, first expose $u=n\bmod2^h$. Every true disagreement belongs to a cylinder on which the two counted affine trajectories have not fused by time $h$. The square-root survival bound from [the published pair inputs](../joint-renewal/KILLED_GRADE_OCCUPATION.md) gives at most $C2^h/\sqrt d$ such residues. This is the only color-specific inference in the proof. On every single surviving cylinder, $n=2^h q+u$ with $q$ in an interval of $Q\asymp R/2^h$ consecutive positive integers. For every $t\le h$, both labeled actual values are integral affine forms in $q$,
$$
   L_i(q)=3^{a_i+p_i(t)}2^{h-t}q+b_i,\qquad (a_1,a_2)=(0,4).
$$
Their slopes have no prime factor greater than three. The intercepts at $q=0$ are ordinary endpoints from $u$ or $81u+r$ and are $O(3^{O(h)}2^h)$, by the ordinary affine formula even if $u=0$. Thus every nonzero determinant of a pair of forms has absolute value at most $\exp(Cd)$.

Here is the sieve bound used on that actual interval. For one form, or two forms with nonzero determinant $\Delta$, omit all primes $p\le d^2$, and in the two-form case also omit those dividing $\Delta$. At each remaining prime $p\le y$ roughness excludes $k$ distinct residues of $q$, where $k=1$ or $2$. The product of the local factors $1+k/(p-k)$ over the retained primes is
$$
             \gg_{c,\eta} (\log y/\log(2d))^k.                    \tag{3}
$$
Indeed $\log(1+k/(p-k))=k/p+O(p^{-2})$. Mertens' prime sum formula gives (3) before excluding divisors of $\Delta$. Since $\log |\Delta|=O(d)$, the sum of reciprocals of its prime divisors larger than $d^2$ is $O(1/d)$, so this exclusion changes the lower bound by at most an absolute factor.

To see the ordinary sieve upper bound directly, put $P=\lfloor Q^{1/3}\rfloor$ and let $S$ be the set of remaining integers $q$ after sieving. Give a squarefree product $l$ of retained primes weight $g(l)=\prod_{p\mid l} k/(p-k)$, including $g(1)=1$. The normalized product distribution with these weights includes $p$ with probability $k/p$. Hence $\mathbb E\log l\le k\sum_{p\le y}(\log p)/p\le C k\log y$. Choose $\eta$ sufficiently small that this is at most $(\log P)/2$ for $\beta\le1$ and all large $d$. This choice is possible since $\log Q\asymp_c d$. Markov shows that $\sum_{l\le P}g(l)$ retains at least half of (3).

For a retained prime use the mean-zero local function equaling $k/(p-k)$ on its allowed residues and $-1$ on its forbidden residues. Its squared norm for uniform measure is $k/(p-k)$. Multiply these functions over the primes in $l$; its Fourier transform on $\mathbb Z/l$ is supported on primitive frequencies, with squared norm $g(l)$ by finite Parseval. Its value on every $q\in S$ is $g(l)$. Cauchy--Schwarz therefore gives
$$
       |S|^2 g(l)\le
       \sum_{(a,l)=1}\left|\sum_{q\in S}e^{2\pi i a q/l}\right|^2.
$$
For $l=1$ use the zero frequency. All these reduced frequencies for $l\le P$ are $P^{-2}$-separated. The additive large-sieve inequality of [Montgomery and Vaughan, *The large sieve*](https://doi.org/10.1112/S0025579300004708) bounds their summed squares by $O((Q+P^2)|S|)$. Consequently
$$
       |S|/Q\ll_{c,\eta}(\log(2d)/\log y)^k,
$$
uniformly on the full survivor cylinder and in the chosen affine forms.

If the two clock-$t$ forms have zero determinant, they are proportional by an integral power of three after ordering their slopes. Equal slopes and endpoints would be counted fusion and is excluded on this cylinder. With unequal slopes the high value is divisible by three; simultaneous standard roughness is impossible. Thus $k=2$ suffices for every clock contributing to (1). Apply the uniform bound to the chosen clock for (2), or take the union of all $h+1$ clocks for (1). Multiply by the total full-cylinder survivor mass $O(d^{-1/2})$, allowing the fixed factor accounting for the 81 suffixes and integer endpoints. This proves both estimates. For large $R$ every physical coordinate through $h$ exceeds $R^{1-c}/81>y$, so a prime coordinate is $y$-rough. The series over rows converges in the exponent ranges stated. Timely entrance exceptions in the passage construction already have summable mass; intersecting the bounds with its genuine ordered first-landing weights is therefore valid.

This removes the indicated actual arithmetic subpopulation from the unrestricted weighted target. Discordant trajectories having a small prime factor on at least one arm at each inspected clock are not bounded by (1).
