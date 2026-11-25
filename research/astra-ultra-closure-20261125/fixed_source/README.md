# Descent below the base at a growing range of ternary exponents

**Scope.** These are partial results on the ordinary shortcut Collatz map. They bound the exceptional set for a simultaneous finite descent and prove recurring physical mergers at a fixed base. The least exceptional base and its first bad exponent remain open.

Write $T(2u)=u$, $T(2u+1)=3u+2$. Fix $h$ clocks and a starting base $a\ge2^h$. In every consecutive block of $2^h$ bases $w=a+i$, the following estimate concerns the *same* bases for every exponent $0\le r\le R$. A base succeeds if all those trajectories satisfy $0<T^h(3^r w)<w$. Each such endpoint supplies the exponent-zero destination of the smaller-base merger in PR192. In particular, if a first bad tower has $r\le R$ and its base belongs to this block, its base must lie in the exceptional set. [PR192, frozen formulation and minimum hypotheses](https://github.com/GettysburgResearch/collatz/blob/a0d7c6e36c378bbb6c826002039aef486bbe0383/research/astra-universal-closure-20261124/global/SmoothCore.lean)

## Finite coverage

The last two columns restrict the count to bases eligible for that minimum. For each $a\ge2^{1024}$ with $a\equiv1$ or $5\pmod6$, the eligible progression consists of $w=a+6i$, $0\le i<2^{1023}$. Each row applies to every such block.

| Clocks | Exponents required at each successful base | Success among all $2^{1024}$ consecutive bases | Success among $2^{1023}$ bases in each eligible progression |
|---|---|---|---|
| 1024 | $0,\ldots,64$ | $>99.9980462\%$ | $>99.9977544\%$ |
| 1024 | $0,\ldots,115$ | $>8.0234\%$ | $>2.1538\%$ |

These percentages come from exact integer inequalities. The generic binomial bounds and their implications for actual descent are kernel-checked. The calculation for these rows is replayed by [check_towers.py](check_towers.py) using a multiplicative binomial recurrence with remainder checks. A separate implementation uses Python's binomial function. For the full 116-exponent row, Lean verifies the numerical inequalities with kernel reduction and derives the physical existence statements `full_block_116` and `odd_ray_116`. The sharper 65-exponent percentages above use exact integer replay. Lean also verifies a more conservative 65-exponent existence bound in `block_1024`. [116-exponent kernel certificate](../machinery/TowerCertificate.lean) · [Independent computation and review](../machinery/REVIEW_FIXED_SOURCE.md)

Let $p$ be the number of odd inputs in the first $h$ steps from $n=3^rw$. Induction gives
$$2^h T^h(n)\le3^p(n+2^h).$$
Thus $3^p(3^r+1)<2^h$ guarantees the desired endpoint. Multiplication by $3^r$ preserves distinct residues modulo $2^h$. Each of the $2^h$ binary parity words occurs exactly once as $w$ runs through its block. A failure must therefore occupy one of at most
$$D_{h,r}=\sum_{\substack{0\le p\le h\\2^h\le3^p(3^r+1)}}\binom hp$$
candidate positions. The exceptional set has size at most $\sum_{r=0}^R D_{h,r}$, by a union bound. Exponents may have arbitrarily correlated words. At $R=116$ both numerical union bounds exceed their respective populations, so these bounds alone give no positive coverage there.

For $w=a+6i$ all first inputs are odd. After that step the possible seeds have odd stride $3^{r+2}$ as $i$ varies. The remaining $h-1$ bits cover every word once on $2^{h-1}$ consecutive indices. In the formula use $\binom{h-1}{p-1}$ and $p\ge1$. The strict population inequality then gives a base on the specified eligible ray with positive, smaller endpoints at every requested exponent. [Kernel proof for both populations](BinomialTower.lean)

At the particular clock 1024 the ordinary decision itself has a sharper pointwise description. For **every** $w\ge2^{1024}$ and $r\ge0$, with $p$ the actual 1024-step odd count, $T^{1024}(3^rw)<w$ if and only if $p+r\le646$. The proof bounds the additive correction in the complete parity word uniformly and checks the strict integer gap at the two neighboring powers of three. This criterion includes individual exceptional bases. It decides the one specified clock and requires the actual parity count there. [Exact kernel theorem](../machinery/TowerCertificate.lean)

## Growing ranks

A simple closed form avoids evaluating binomial coefficients. Assign each odd bit weight $A$ and each even bit weight $B$, with $A\ge B\ge0$. Total weight is $(A+B)^h$ at each exponent. If $K\le h$ and $3^K(3^R+1)<2^h$, a failing word has more than $K$ odd bits. Consequently
$$
 \#\mathrm{exceptions}\, A^K B^{h-K}\le (R+1)(A+B)^h.
$$
For $h=32t$, $R=2t$, $K=18t$, $(A,B)=(9,7)$ and $t\ge1$, the exceptional fraction in each full block is at most
$$
 (2t+1)\left(\frac{8^{32}}{9^{18}7^{14}}\right)^t,
 \qquad \frac{8^{32}}{9^{18}7^{14}}<0.779 .
$$
Thus the admissible window grows while the guaranteed exceptional fraction tends to zero. The exponent and word count need only satisfy the displayed general inequality. Finite parity coding and density-one stopping arguments are classical. The contribution here is their explicit simultaneous application to the lower-base rank, its restriction to eligible units, and the Lean proof. [Kernel estimates and first-bad consumer](TowerDescent.lean) · [Terras, 1976](https://doi.org/10.4064/aa-30-3-241-252)

## A merger on each individual ray

For every fixed odd $w$, including $w=1$, and every $s\ge0$, some $0\le d<32$ satisfies
$$T^7(3^{s+d+1}w)=T^7(3^{s+d}w).$$
At $x=23+32k$, $x$ and $3x$ reach $20+27k$ at clock five. At $x=59+128k$, both reach $38+81k$ at clock seven. Starting at any odd residue modulo 128, one of the next 32 successive powers of three times that residue reaches one of these classes. Lean checks all residues and lifts these finite words to every ordinary input. The chosen adjacent pair depends on the starting phase. [Kernel proof](TowerWindows.lean)

## An infinite family missed by both short tests

Fix $t\ge1$, $h=32t$, $r=2t$. Choose any large odd $w$, prime to three, satisfying $3^{r+1}w\equiv-5\pmod{2^h}$. There are infinitely many because $3$ is invertible modulo $2^h$ and multiples of $2^h$ vary the residue modulo three. Set $n=3^rw$. The first two steps reach $(3n+1)/4$, and its successor parameter $(3n+5)/4$ is divisible by $2^{h-2}$. Therefore the next $h-2$ inputs are all odd. The first step increases $n$, the second value exceeds $w$, and the remaining odd steps increase it. Every clock through $h$ stays at least $w$.

These inputs have $n\equiv169\pmod{512}$, a one-input initial odd run and $2\le3^r$, so they lie on the short-run branch beyond the 85-modulo-512 guard of the frozen PR192. Their predecessor $x=n/3$ is $99\pmod{128}$. For $x=99+128k$, the seven-clock endpoints from $x$ and $3x$ are $7+9k$ and $1700+2187k$, respectively. Thus even the actual neighboring orbits fail to meet by clock seven. For the separate ordinary control $w=2^{32}+3$, $r=2$, the first lower-base hit occurs at clock 62 and equals 3774236102. This illustrates the scope of a missed deadline. The family argument is written and the checker tests sixteen lifts.

The first unsupported step is supplying a source-dependent merger for every surviving least base and exponent. Small exceptional fractions allow prescribed exceptions, and an adjacent merger elsewhere on that same tower does not determine the supplied exponent. The ordinary excursion bounds of PR205 and reverse-defect return in PR197 do not assert that the present exceptional sets omit the least failure. [PR205 at its reviewed head](https://github.com/GettysburgResearch/collatz/tree/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124) · [PR197 at its reviewed head](https://github.com/GettysburgResearch/collatz/tree/b27a6fe31a487adf5615e173329ad009b975a3cd/research/ayh-resource-reset-20261124/closing-proposal)
