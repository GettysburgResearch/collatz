# How many even steps can a Collatz merger require?

**PROPOSED.** Use the shortcut map $T(x)=x/2$ on even positive integers and $T(x)=(3x+1)/2$ on odd ones. A merger means $T^i(x)=T^j(y)$ for some independent nonnegative clocks. An even step means that the input of a shortcut step is even. Two sources in the same merger component have a common future iterate.

Take an odd $r<2^h$ and compare $r$ with $r+2^h$. After $h$ steps their values differ by $3^s$, where $s$ counts the odd steps of $r$ before that time. For every fixed $0<c<\tfrac12\log_2 3$, the fraction of such $r$ for which these **two endpoints** can subsequently merge with at most $ch$ even steps on each path is exponentially small in $h$. Both clocks and both odd-step counts may be arbitrarily large. There are exponentially many exceptions that meet in a single further step, and the accompanying proof characterizes every such simultaneous one-step meeting. Two finite-certificate criteria for the full conjecture follow. Criterion (4) is elementary and unconditional. The shorter scale range and larger tolerance in (3) use a specified external first-landing estimate for freely chosen residue classes. Constructing certificates at all scales remains open.

## Affine identities

For a legal word of length $i$ with $a$ odd steps, let its odd positions be $0\le d_1<\cdots<d_a<i$. Direct composition gives

$$
T^i(x)=3^a2^{-i}(x+E),\qquad
E=\sum_{j=1}^{a}2^{d_j}3^{-j}.
$$

Since $d_j\le i-a+j-1$, summing a geometric progression gives $0\le E\le 2^{i-a}(1-(2/3)^a)\le 2^{i-a}$. The right-hand side depends only on the number of even steps. The parity word of length $h$ depends only on $x\bmod 2^h$, and

$$
T^h(r+2^h m)=T^h(r)+3^{s_h(r)}m,\qquad m\ge0.
$$

At each binary extension the two lifts of the same residue have identical earlier parities and opposite next parities, by the displayed formula at that depth. Induction gives a bijection between residues and parity words. In a fixed class $r\equiv b\bmod 2^k$, the last $h-k$ parities thus run over all binary words of that length exactly once.

## A finite bound for arbitrary clocks

Fix integers $1\le k<h$, an odd $0<b<2^k$, an even-step budget $B\ge0$, and an odd-count cutoff $s_0\ge3$ with $2^B/3^{s_0}\le1/8$. In this section choose $r$ uniformly from the $2^{h-k}$ representatives of $b$ in $[1,2^h)$. Write $s_*=s_k(b)$ and set

$$
W=2^{-s_0}+3\,2^B3^{-s_0},\quad
D=\left\lceil (h+B+2)/\log_2(3/2)\right\rceil,\quad
N=(2B+1)(2D+1).
$$

The fraction of pairs whose two endpoints after time $h$ subsequently merge using at most $B$ even steps on each path is at most

$$
\Pr\{s_*+\mathrm{Bin}(h-k,1/2)<s_0\}+N(2W+2^{-(h-k)}). \tag{1}
$$

**Proof.** Discard the binomial tail and put $s=s_h(r)$, $g=3^s$, $v=T^h(r)/g$. The two endpoints are $gv$ and $g(v+1)$. The first word's offset gives

$$
0\le v-r/2^h\le 2^{-s},\qquad 0<v\le9/8.
$$

Let the subsequent words have $a_i$ odd and $e_i$ even steps, $i=1,2$. Divide their additive offsets by $g$ and denote the results by $u,w$. Both lie in $[0,d]$, with $d=2^B/g\le1/8$. A merger implies

$$
R(v+u)=v+1+w,\qquad R=(3/2)^{a_1-a_2}2^{e_2-e_1}.
$$

Hence $R-1=(1+w-u)/(v+u)\ge1/2$. Also $|(R-1)v-1|=|w-Ru|\le Rd$, which gives $|v-1/(R-1)|\le3d$. The grid point $r/2^h$ is within $W$ of $1/(R-1)$.

Even with unbounded odd counts the list of centers is finite. From $v\ge2^{-h}$ one gets $R\le1+(1+d)/v\le2^{h+2}$. Taking logarithms in the ratio formula gives $|a_1-a_2|\le D$ since $|e_2-e_1|\le B$. Thus there are at most $N$ candidate centers. Each interval of radius $W$ contains at most $1+2W 2^{h-k}$ points of the prescribed residue grid. Summing proves (1).

**Asymptotic consequence.** Fix $0<\epsilon<\tfrac12\log_2 3$ and $0<\delta<1$. Whenever $h-k\ge\delta h$, uniformly in the odd residue $b$, the fraction in (1) is $O(\exp(-c_{\epsilon,\delta}h))$ for some $c_{\epsilon,\delta}>0$ if

$$
B\le (\log_2 3)s_*+
       \bigl(\tfrac12\log_2 3-\epsilon\bigr)(h-k).
$$

Take $s_0=s_*+\lfloor(\tfrac12-\epsilon/(2\log_2 3))(h-k)\rfloor$. The binomial lower tail is exponentially small by the elementary Chernoff bound. Both terms in $W$ decay exponentially in $h-k$, and $N=O(h^2)$. Taking $k=1$ proves the opening assertion. The constant $\tfrac12\log_2 3$ is a lower bound for this test's cost. Its optimality is open.

## The cost tracks the actual gap

Write $M_h(r)$ for the least possible maximum of the two subsequent even-step counts over all mergers, with value $+\infty$ if there is no merger. Set $\lambda=\log_2 3$. For uniformly random odd $r<2^h$,

$$
\Pr\!\left\{M_h(r)\le \lambda s_h(r)-4\log_2 h\right\}=O(h^{-2}).
$$

Indeed discard $s<h/4$, an exponentially unlikely binomial tail. For any remaining pair satisfying the displayed event, take the actual budget $B=M_h(r)$. Then $2^B/3^s\le h^{-4}$ and $B\le \lambda h$. The proof of (1) places $r/2^h$ within $2^{-h/4}+3h^{-4}$ of a center. All pairs use the same list of $O(h^2)$ possible centers since the differences of odd and even counts are bounded by using $B\le\lambda h$ in $D$ and $N$. Counting grid points proves the estimate for all sufficiently large $h$.

This also gives an almost-sure statement about finite integers. Choose an infinite sequence of independent fair bits above a fixed low bit 1 and let $r_h$ be its integer truncation to $h$ bits. The failure probabilities above are summable. By the first Borel–Cantelli lemma, for almost every sequence, **at every sufficiently large depth** any merger requires more than $\log_2(3^{s_h(r_h)})-4\log_2 h$ even steps along at least one path. No independence between depths is needed.

**Explicit exceptions.** At each $h\ge13$, at least $2^{\lfloor(h-1)/6\rfloor-1}$ distinct odd starts actually have $M_h(r)=1$. There are also explicit examples for every even $h$ and every odd count $1\le s<h$, including $s$ within one of $h/2$. In particular, for every fixed $0<c<\lambda/2$, the fraction with $M_h(r)\le ch$ is bounded above and below by exponentials in $h$ with strictly negative rates. The upper bound is (1), and the lower bound is $2^{\lfloor(h-1)/6\rfloor-h}$ once $ch\ge1$. [Proof and examples](FAST_MERGERS.md)

There is a corresponding fixed-budget bound at the scale of the binomial fluctuations. Put $n=h-k$, assume $n\ge\delta h$ for fixed $\delta>0$, and choose any real $z$. In every odd residue cell, uniformly in $b$,

$$
\limsup_{h\to\infty}
\Pr\!\left\{M_h(r)\le \lambda(s_*+n/2)+z\lambda\sqrt n/2\right\}
\le \Phi(z),
$$

where $\Phi$ is the standard normal distribution function and the limsup allows $k,b$ to vary. Use the integer part of the displayed budget for $B$ in (1) and take $s_0=\lceil(B+4\log_2 h)/\lambda\rceil$. Then $2^B3^{-s_0}\le h^{-4}$, $s_0$ grows at least linearly in $n$, and the entire grid error tends to zero. The binomial cutoff has standardized value $z+O((\log h)/\sqrt n)$, so the binomial central limit theorem gives the conclusion. In particular a budget at the mean log gap can certify at most $1/2+o(1)$ of any such cell.

## What would settle Collatz using these pairs

**SOURCE-QUALIFIED input.** Fix an odd target $t$ prime to three. The first-landing estimate used here supplies constants $\eta_t>0$ and a common integer $A\ge2$ such that, for every sufficiently large $k$ and every odd $b\bmod 2^k$, at least $\eta_t 2^{Ak-k}$ of its positive representatives below $2^{Ak}$ reach $t$. The local result counts first landings in $[X/4,X]$ with a prescribed initial valuation word, at $X\ge C t\exp(C(k+1))$. Take $X=2^{Ak}$, choose $A$ with $A\log2>C$, and use the odd-residue consequence in the pinned proof. The hitting-count statement alone suffices here. [Arithmetic input and its external dependencies](https://github.com/GettysburgResearch/collatz/blob/4e94f656236485ebf854711528b06c18b91d4ad3/research/critical-orbit-mellin/LOCAL_FIRST_LANDING.md#consequence-for-separating-ordinary-basins)

For $h\ge k$ let $p_h(b,k)$ be the fraction of $r\equiv b\bmod 2^k$ in $[1,2^h)$ for which $r$ and $r+2^h$ have no merger at any clocks. Equivalently, use the two endpoints after $h$ steps. Removing finite initial pieces preserves the existence of a merger since a shared future can always be followed further.

Subject to the input above, the whole conjecture is equivalent to

$$
\liminf_{k\to\infty}\ \min_{\substack{1\le b<2^k\\b\ {\rm odd}}}
       \sum_{h=k}^{Ak-1} p_h(b,k)=0. \tag{2}
$$

If all positive integers reach 1, every summand vanishes. Conversely, suppose another component exists. It contains an odd ternary unit $t$: strip powers of two, then if the resulting odd number is divisible by three, take one odd step and strip the remaining powers of two. Choose a uniformly random truncation to $Ak$ bits in the prescribed class $b$. At level $k$ it equals $b$. If $b$ reaches 1, the arithmetic input gives probability at least $\eta_t$ that the final truncation belongs to the component of $t$. Otherwise use target 1. With probability at least $\eta=\min(\eta_1,\eta_t)>0$ the two endpoints differ in membership in the basin of 1.

Reveal the intervening bits from least to most significant. At level $h$ the current truncation $r$ is uniform on the specified residue grid. A fair next bit either leaves it fixed or takes it to $r+2^h$. A change of component requires the latter option and a nonmerging pair. The union bound gives $\eta\le\frac12\sum_{h=k}^{Ak-1}p_h(b,k)$ in **every** cell for all sufficiently large $k$. This proves (2). Random bits here sample finite ordinary starting integers. No convergence assumption for a 2-adic orbit enters the argument.

**A condition with finite witnesses.** Write $p_h^{(B)}(b,k)$ for the fraction of the same grid with $M_h(r)>B$. This rational number is computable. Starting at either endpoint, enumerate the states through the input of the $(B+1)$st even step. Every run of consecutive odd inputs ends, since $T(x)+1=3(x+1)/2$ on an odd input. A repeated state can also terminate that enumeration. Intersecting the two enumerated sets decides whether a merger fits the budget. For a fixed finite block, increasing $B$ eventually certifies every pair in that block that ever merges. Consequently (2) is equivalent to

$$
\forall m\ge1\quad \exists\, k\ge m,\ b\ {\rm odd},\ 1\le b<2^k,\ B\ge0:
\qquad \sum_{h=k}^{Ak-1}p_h^{(B)}(b,k)<1/m. \tag{3}
$$

This pinpoints the missing upper bound. It would suffice to construct witnesses to (3) for unbounded $m$. The same $B$ covers every level of a witness. At its last level $h=Ak-1$ put $n=h-k$. Along any sequence of witnesses with $m\to\infty$, the fraction certified at that level tends to one. The normal bound above forces

$$
\frac{B-\lambda(s_k(b)+n/2)}{\lambda\sqrt n/2}\longrightarrow+\infty.
$$

Otherwise some subsequence of these standardized budgets stays below a fixed $z$, where the certified fraction has limsup at most $\Phi(z)<1$. Thus one can quantify how a small-budget proof of (3) fails while the existence of arbitrary-budget witnesses remains open. Both a nontrivial positive cycle and a divergent positive trajectory would supply a second component in the argument for (2).

## An unconditional finite criterion

There is a direct way to place an ancestor of any positive target $t$ coprime to three inside any odd binary residue class $b\bmod2^k$, $k\ge1$. Let $s=s_k(b)\ge1$, $g=3^s$, $y=T^k(b)$, and $d=\varphi(g)=2\cdot3^{s-1}$. Then $0<y<2g$ by the affine identity. Also $3\nmid y$, because an odd step produces a unit modulo three and every subsequent step preserves being a unit. The powers of two run through all units modulo $g$. Indeed $v_3(4^{3^j}-1)=j+1$ by induction from the difference of cubes, so the multiplicative order of $2$ modulo $3^s$ is $2\cdot3^{s-1}$.

Put $L=\lceil\log_2(2g)\rceil$. Choose $v\in[L,L+d-1]$ so that $2^v t\equiv y\pmod g$. This gives the integer

$$
0\le w=\frac{2^v t-y}{g}<2^{d+1}t,\qquad T^k(b+2^k w)=y+gw=2^v t .
$$

The bound uses $2^L<4g$. This representative reaches $t$ by $v$ further halvings and requires at most $j_t=d+\lceil\log_2(2t)\rceil$ extra source bits. For example, when $k$ is even and $b=(2^k-1)/3$, the formula becomes $T^k(b+2^k w)=1+3w$. In that cell every unit $t$ already has either $t$ or $2t$ among the values $1+3w$.

The full conjecture is equivalent, **without any density input**, to the following statement about finite computations. In it $d=d(b,k)$ is determined by the chosen residue as above.

$$
\forall m\ge1\quad \exists\,k\ge m,\ b\ {\rm odd},\ 1\le b<2^k,\ B\ge0:
\qquad 2^{d}\sum_{h=k}^{2k+d-1}p_h^{(B)}(b,k)<1/m. \tag{4}
$$

If all starts reach 1, any such finite block has a common budget certifying every pair. Conversely, take an odd unit $t$ in any second component. For every $b$, choose target $t$ if $b$ reaches 1, and target 1 otherwise. Membership in the basin of 1 differs between $b$ and the constructed representative, which uses at most $j_t$ extra bits. On the binary path from $b$ to this representative, some edge changes that membership. At its level $h\le k+j_t-1$, one failed pair accounts for at least $2^{-(h-k)}\ge 2^{1-j_t}$ of its grid, for every budget $B$. As soon as $k\ge\lceil\log_2(2t)\rceil$, the block in (4) includes this level, and its weighted sum is at least $2^{1-\lceil\log_2(2t)\rceil}>0$ uniformly in $b,k,B$. This contradicts (4) for large $m$. The explicit weight and depth quantify the price of using one constructed representative of an arbitrary component.

One can also fix the particular class $b_k=(2^k-1)/3$ at every even $k$. Here $d=2$ and $j_t$ is bounded independently of $k$ for fixed $t$. Thus (3) with $A=2$, $k$ even and $b=b_k$ prescribed is unconditional as well. Its force comes from the identity $T^k(b_k+2^k w)=1+3w$, so a failed merger at a fixed relative depth recurs at the same relative depth in every one of these cells.

In particular there is an elementary pointwise version. Collatz holds if and only if the two positive integers

$$
1+3w,\qquad 1+3(w+2^j)
$$

have a common future iterate for every $j\ge0$ and $0\le w<2^j$. Indeed, removing the highest binary digit of any positive $n$ writes $n=w+2^j$. Induction on $n$ would then put every $1+3n$ in the component of 1. For each unit $t$ modulo three either $t$ or $2t$ belongs to $1\bmod3$, and $2t$ steps to $t$. Every positive integer divisible by three reaches a unit after stripping its powers of two and taking one odd step. The converse follows immediately from convergence. This is exactly the family in the cell $k=2,b=1$ after its first two steps. Applying (1) there shows that a fraction exponentially small in $j$ can meet after their next $j$ steps with fewer than $cj$ subsequent even steps on each side, for every fixed $0<c<\lambda/2$.

## Reducing the remaining cases

At depth $h$ one needs only the least index for each pair consisting of the odd-step count and endpoint. At most $O(2^{0.965385 h})$ such indices suffice. Outside an exponentially small exception, each index also has at least $\lfloor2^{0.20h}\rfloor$ strictly smaller alternatives reaching its exact state after $h$ steps, uniformly in its higher digits. For ordinary starts in any length-$N$ interval, further iteration gives a smaller same-time partner inside the interval for all but $O_\epsilon(N^{0.949956+\epsilon})$ starts in $O_\epsilon(\log(2N))$ steps. Lean checks the equivalence of testing just the least representatives to full Collatz. [Proof, count and exact recursion](PREFIX_REPRESENTATIVES.md)

The depth parameter $d=2\cdot3^{s-1}$ in (4) can be replaced by an effective $D(s)=\exp(O(s/\log(s+2)))$. Finite Fourier inversion gives genuine positive ancestors for every odd binary class and every odd target prime to three, even at every sufficiently late prescribed clock. The resulting block criterion is unconditional. Constructing sufficiently accurate blocks, or proving merger for every retained pair above, remains open. [Ordinary construction and proof](SHORTER_ANCESTORS.md)

## A lower bound for every smaller source

If $3^A\mid n$ and $8^k\mid n+5$, a smaller positive start meeting the first $3k$ shortcut steps of $n$ must spend at least $A+1$ more odd steps than $n$ has spent by the meeting. For $A\ge6$ it must spend at least $A+2$ more. Its own clock can be arbitrarily large. On powers $n=3^a$ one may take $A=a$. The proof compares an ordinary positive path with the signed cycle through $-5$ and then lifts the initial part of a proposed competing path to a small positive integer. Lean checks both bounds and the quantitative extraction of the small integer. If a fixed excess above $A$ were realized for unbounded $A$, the extracted starts would include one with a divergent positive orbit. Constructing such mergers remains open. [Theorem and proof](NEGATIVE_FIVE_CHECKPOINT.md)

For every $k$, a complete exponent residue class, apart from finitely many small terms, attains the earliest possible direct descent after those $3k$ steps. There are also ordinary examples with arbitrary $k,A$ whose orbits provably reach 1, and examples reaching any prescribed target prime to three. The note derives an exact counting law for first descent after the initial segment. The explicit constructions and counting law are written proofs. [Exit times and constructions](NEGATIVE_FIVE_CHECKPOINT.md#the-first-possible-time-for-direct-descent-is-attained)

## Evidence and prior work

Powers of four remain least representatives at every eligible depth. Their comparisons reduce exactly to convergence of $3^a+1$ and $3^a+2$ in specified exponent ranges. The same two families control the high-bit tail of every row whose lower start is known to reach 1. An elementary count proves simultaneous descent for the three consecutive numbers starting at $3^a$, with $O(N^{0.949956})$ exceptional exponents in any interval of $N$ exponents. A separate density-one comparison to the preceding power uses the cited fixed-gap synchronization theorem. [Ordinary survivors and shifted powers](PREFIX_REPRESENTATIVES.md#a-family-the-filter-always-retains)

The follow-up formal declarations establish the least-representative equivalence and that an integral word certificate gives a legal ordinary endpoint. The entropy bounds, iterated short-interval estimate and Fourier estimate are written proofs. A separate exact checker compares the prefix recursion with 32,767 directly computed prefixes through depth 14, and modular tuple counts with 1,848 ordinary paths in six small fixed-clock boxes. Five boxes hit all target residues and the sixth hits 220 out of 243. The finite boxes illustrate the count identity at those parameters. The same checker replays 320 shifted-power tail identities. Lean also verifies that powers of two retain their representative whenever eligible and that a lower arm reaching 1 gives the claimed tail formula. [Checker for the reductions](check_reductions.py)

Lean checks the parity counts, the exact affine numerator, its even-step bound, the shift by any multiple of $2^h$, the error in the starting grid position, and the real localization inequality applied to actual orbits with independent clocks. It also checks the complementary-orbit identity, the one-step meeting used in the constructions, and the complete pointwise equivalence in `collatz_iff_binary_mergers`. The counting and probability arguments and the finite-block reductions (2)–(4) are written proofs. Only the unrestricted-cell versions of (2)–(3) use the external landing estimate. Replay the formal file using Lean 4.34.1 with Mathlib at `d13f23b723b8a846827a245b89c10fc7d3f11612` via `lake env lean -DwarningAsError=true /absolute/path/to/HighBit.lean`. [Lean source](HighBit.lean)

Run `python -B research/upper-bit-mergers/check.py` from the repository root for a separate exact-arithmetic check. It covers all odd starts at each depth 1 through 14, with up to four subsequent even steps per path. It counted 16,383 start–depth pairs, 3,038 common states summed over pairs, and 1,898 meetings satisfying the hypotheses of the interval estimate. The one-step characterization identified all 51 synchronous one-step mergers on this grid. The check also verified the exact paths for 465 prescribed-count examples, 884 pairs from the branching construction and 1,016 target ancestors in binary residue classes. [Executable check](check.py)

The November 18 investigation studies the sibling pair $2n,2n+1$ and reads prefixes from their most significant end. The pairs here share the least significant $h$ bits and split by $3^s$ after a common parity word. The offset and ratio calculation is derived above. The underlying parity-vector parametrization is classical. [Earlier sibling-pair argument, pinned from PR 145](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/profinite-orbit-averages/ONE_STEP_LAG.md) · [Bernstein and Lagarias, *The 3x+1 conjugacy map*](https://doi.org/10.4153/CJM-1996-060-x)
