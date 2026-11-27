# Smaller canonical visitors at specified Mersenne parents

Use the shortcut map $T(2v)=v$, $T(2v+1)=3v+2$. Write $M_m=2^m-1$, $G(x)$ for an ordinary visit to 1, and call $x$ canonical if $x\equiv17\pmod {48}$. For $m=11+162j$ define $81z+271=128\cdot2^m$. The native lower first reaches $M_m$ at clock seven, while $3z$ reaches $2^{m-2}$ at clock nine and first reaches 1 at $m+7$. A canonical disagreement has a bad lower and a good triple. A smaller canonical $Y$ that meets $z$ and has a genuinely good triple excludes $z$ as the least canonical disagreement. Proving $G(Y)$ itself would give $G(z)$. [Native physical paths](ReturnDescent.lean)

## Two first contacts on 33 entire delayed classes

Set $m=12\cdot2^{18k}-1$ for the originally specified positive parameter $k$. On every class in the table, Lean constructs a strictly smaller canonical $Y$ and an integer $h\le32$ such that

$$
T^hY=M_m=T^7z,\qquad T^{h+2}(3Y)=2^{m-2}=T^9(3z).
$$

Each displayed clock is the first visit to its indicated target on that trajectory. The first hit of 1 from $3Y$ is at $m+h$. Both lower arms meet before the native Mersenne ascent begins. Thus a bad $z$ in any listed class produces an actual smaller canonical disagreement, without assumptions on bounded orbits or on smaller ordinary integers. [Physical paths and exact sizes](PassageDescentDelayed.lean) · [First visits](PassageDescentFirst.lean)

| Modulus of $k$ | Positive residues |
|---:|---|
| 6,561 | 3130, 4831 |
| 19,683 | 457, 862, 1375, 2401, 3447, 5020, 7092, 10420, 14065, 14794, 16900 |
| 59,049 | 531, 3373, 7504, 8233, 9610, 16444, 28645, 31804, 37825, 38365, 40501, 42685, 44602, 52702, 53343, 53350, 57076, 57879, 58210 |
| 43,046,721 | 270 |

The classes are disjoint. Counting them at the common modulus $3^{16}$ gives $51{,}031/43{,}046{,}721$, approximately $0.11855\%$ of all positive $k$. This fraction measures the displayed sufficient family.

For example, at each $k=3130+6561s$ take
$$
Y=\frac{2^{m+18}-2{,}692{,}031}{3^{12}}.
$$
Here $3Y<z$. The lower reaches $M_m$ in 18 steps with 12 odd departures. The upper reaches $2^{m-2}$ in 20 steps with 11 odd departures. At each $k=270+43{,}046{,}721s$, the formula is $(2^{m+32}-51{,}901{,}264{,}991)/3^{20}$, with 32 lower steps and 19 odd departures on the upper prefix. The 33 classes include members beyond the earlier table of 512 individual parameters. Earlier paid comparisons joined Mersenne peaks after their ascents. [Earlier 512-parameter calculation](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/coupling/DELAYED_BATCH.md)

Each certificate checks one small ordinary source $y_0$ and terminal upper value $b$. At lower clock $h$ it reaches $4b-1$ with $r+1$ odd departures. At upper clock $h+2$, $3y_0$ reaches $b$ with $r$ odd departures. Modular squaring proves $2^{m-2}=b+3^{r+2}t$ throughout the specified delayed class. The positive lift $Y=y_0+3\cdot2^{h+2}t$ then has both claimed trajectories. For $k=3130\bmod6561$ the small pair is $y_0=25{,}937$, $b=13{,}148$. [Lifting and congruences](PassageDescentDirect.lean)

## Eleven upper odd departures are necessary and attained

For **every** $m=11+162j$, suppose $Y<z$ is canonical, $T^hY=M_m$, and $T^{h+2}(3Y)=2^{m-2}$. At least eleven upper odd departures occur by that second clock. The first example above attains eleven. The statement allows every nonnegative $h$. [All parameters and attainment](PassageDescentFirst.lean)

For $j>0$, an upper grade at most ten first forces $h\le18$ by bounding the ordinary affine word and using $Y<z$. Express $Y$ as a canonical low residue $b=48i+17$ plus a multiple of $3\cdot2^{h+2}$. The enormous terminal $2^{m-2}$ forces equality of both the constant terms and the translating coefficients in the two lifted words. The original ternary phase gives $2^{m-2}\equiv512\pmod{243}$. Under these constraints the complete finite check leaves only $h=7$, upper grade three, and $81Y+271=128\cdot2^m$, which is the original $z$. At $j=0$ every smaller canonical start reaches 1 while avoiding $M_{11}=2047$. [Rank proof](PassageDescentRank.lean) · [Kernel exhaustion in 512-input blocks](PassageDescentRankTable.lean)

With **independent clocks**, let $T^lY=M_m$ with $p$ odd departures and $T^u(3Y)=2^{m-2}$ with $r$ odd departures. For any $m,u\ge2$, either $u=l+2$ and $p=r+1$, or
$$
2^m\le\max\{2^{u-r}3^{p+r},\;2^{l-p}3^{p+r+1}\}.
$$
This statement does not require canonicality or a size comparison. The affine intercept $A$ of an $l$-step word with $p$ odds satisfies $A+2^l\le2^{l-p}3^p$. Eliminating $Y$ from the two affine equations yields two remainders bounded by the displayed terms. If both are below $2^m$, reduction modulo $2^m$ equates the remainders and then their leading coefficients. Uniqueness of the binary valuation gives the clock equality. In particular, for a smaller canonical candidate on the hard row with $j>0$ and $r\le10$, one necessarily has $u\le20$ and $2^m<3^{l+20}$. [General synchronization and independent-clock floor](PassageDescentIndependent.lean)

## No finite rank suffices for all delayed parameters

For every odd-step budget $K$ and every lower limit $L$, Lean exhibits an ordinary delayed parameter $k\ge L$ such that **every** smaller canonical $Y$ reaching its $M_m$ spends more than $K$ lower odd departures. The clock is unrestricted and the conclusion places no condition on $3Y$. For equal-lag comparisons with the fixed upper cut, a single $k$ can force both grades beyond any two prescribed budgets. These are lower bounds on every candidate at the selected parent. Existence of a candidate there remains open. [Cofinal ordinary delayed parents and both grade bounds](PassageDescentAnchor.lean)

The pointwise condition is $2^m\equiv590\pmod{3^{K+1}}$ and $2^m\ge590+75{,}521\cdot3^K$. If a lower word had $p\le K$ odds, write $2^m=590+3^p w$ with $3\mid w$. The endpoint $2^m-1$ forces $Y\ge2^h w$ because a lower start below $2^h w$ stays below $3^p w$ at the end of this word. Thus $b=Y-2^h w$ is an ordinary nonnegative start with $T^h b=589$. Four initial clocks are necessary for a canonical start to reach $M_m$, so $b$ is canonical too. The original price and $w\ge75{,}521$ give $81\cdot2^h\le128\cdot3^p$. The ordinary leading coefficient then gives $b\le930$. Among the twenty canonical starts in this range, the only hit at clock at least four is $T^7(929)=589$, with four odd departures. Its lift is $Y=z$.

Two successive ternary power lifts place actual delayed exponents arbitrarily deep in the required class. For the upper-grade assertion, $T^{h+2}(3Y)=2^{m-2}$ with $r$ odd departures and $Y<z$ imply $h\le2r+2$, since each odd shortcut increases a positive input by at most a factor of two. The ternary control $590$ and a broader written classification of fixed forward and inverse words appeared in PR 195. The present computed control, transfer to ordinary positive parents and unrestricted-clock grade conclusions are kernel checked. [Prior fixed-word classification at 590](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-unconventional-20261126/renormalization/FINITE_COVER_BARRIER.md)

## A paid return on the full binary class of the 499-clock comparison

On every $j\equiv1\pmod{2^{496}}$, for the original $m=11+162j$ there is a canonical $Y$ meeting $z$ with $Y<2^m$, $2Y<z$, and $T^H(3Y)=1$ at $H\le m+17$ with at most ten odd departures. All ternary residues are covered. When $j\equiv1\pmod3$ or $27\mid j$, the same construction gives $27Y<2z$, $H\le m+8$ and at most six odd departures. This applies to every $j=b^n$ for odd $b$ and positive $n$ divisible by $2^{494}$. The upper bound permits one clock more than the original first upper hit. [53 templates and complete covering](PassageDescentCover.lean) · [All odd-base powers and canonical minimality](PassageDescentPowers.lean)

At ordinary postpeak clock 499, the native peak $3^m-1$ and each earlier peak at gap $9,10,17,18,19,20$ reach the same endpoint. On the earlier arm the odd count exceeds the native count by exactly the gap. These two facts let the checked finite comparison at $m=173$ lift over the whole binary class. PR 195 established 499 as the least uniform postpeak budget for earlier-peak contacts on the indicated odd-base perfect powers. Higher-grade upper templates now turn those contacts into actual smaller canonical visitors. At the stronger input precision $j\equiv1\pmod {2^{760}}$, a 763-clock contact at gap 27 yields a smaller visitor whose triple hits 1 in at most $m$ steps with exactly three odd departures. [Peak charts and three-odd return](PassageDescent.lean) · [Template transport](PassageDescentRows.lean) · [Prior sharp postpeak budget](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/ordinary/SHARP_ODD_POWER.md)

The remaining global obligation is to produce a smaller disagreement at every possible least canonical source or prove that its lower reaches 1. The 33 delayed classes and the binary class each eliminate their supplied parents from leastness. For an uncovered delayed $k$, the original lower still has no uniform paid return proved here. The first-hit pair theorem of PR 212 constructs two starts at a prescribed additive distance that hit a common target. Its source varies with the requested interval. Elsenhans’s November 2026 algorithm uses ordinary affine words to compute total stopping times for sampled billion-digit inputs. Neither result supplies the missing fixed-parent implication. [PR 212 first-hit pairs](https://github.com/GettysburgResearch/collatz/blob/8cac31f51d9a5a2bd03c211495dec8f90c2aa48e/research/astra-infinite-descent-20261127/merger/FAST_FIRST_HIT_PAIRS.md) · [Elsenhans, Research in Number Theory](https://doi.org/10.1007/s40993-026-00811-5)
