# Finite augmented merger classes on every odd tower

Fix an odd positive integer $w$, let $x_r=3^rw$, and use the ordinary shortcut map $T(n)=n/2$ on even $n$ and $T(n)=(3n+1)/2$ on odd $n$. Let $P_h(n)$ be the number of odd states departed in the first $h$ steps. Call $r,s$ **linked** if for some common clock $h\ge0$,

$$
 T^h x_r=T^h x_s,\qquad r+P_h(x_r)=s+P_h(x_s).                 \tag{1}
$$

The second equality compares the two accumulated exponents, including the exponents of the starting points. Ordinary mergers allow independent clocks and require just the endpoint equality.

**Theorem 1.** Every equivalence class of (1) on every fixed odd tower is finite. Consequently there are infinitely many class minima, each an exponent with no link to any earlier exponent, at any common clock. This holds for all positive orbit types, including potential divergent orbits and nontrivial cycles.

**Theorem 2.** Fix additionally $3\nmid w$, a finite bank of nonempty parity words, and an integer $K\ge0$. On each arm allow at most $K$ blocks, with each block consisting of any positive number of repetitions of a bank word. For infinitely many $r$ there is no such ordinary two-arm meeting from $x_r$ to any start $2^i3^sb$ with $b>0$, $i,s\ge0$, and either $b<w$ or $b=w,s<r$. Both clocks and all repetition counts are unbounded. The theorem concerns actual integer trajectories. It includes the unsmoothed target $i=0$ of FrontierMerger.

The first proof finds a finite set of small states that every augmented neighbor of a fixed nonperiodic reference must visit, then shows that each such state can occur at only one elapsed clock across its neighbors. For a periodic tail, an odd-count invariant replaces that time rigidity. In the two-arm argument, the ordinary equality itself forces both conditions in (1) at sufficiently high source exponents after initial halvings of the competitor have been removed.

## 1. A uniform reciprocal estimate on finite simple paths

Take a finite chronological orbit segment $n_0,\ldots,n_{l-1}$ of distinct positive integers. For real $X\ge1$ let $N(X)$ count its entries at most $X$. Then

$$
 N(X)\le6X^{79/80},\qquad
 \sum_{i:n_i\ge M} n_i^{-1}\le480M^{-1/80}\quad(M\ge1).          \tag{2}
$$

Put $u=\lfloor(\log_2 X)/20\rfloor$, $k=10u$. Discard at most $k$ terminal indices whose $k$-step endpoints lie outside the segment. Length-$k$ parity words are in bijection with the residue classes modulo $2^k$. Indeed an integer with a prescribed parity prefix of length $j$ gives $T^j(n+2^jt)=T^j(n)+3^{P_j(n)}t$, so the two lifts choose opposite next parities. The number of words with at least $6u$ ones is at most $(3/2)^{-6u}(1+3/2)^k$. Each residue occurs at most $2X/2^k$ times among positive starts up to $X$, since $2^k\le X$. Distinctness of the starts bounds the heavy contribution by $2Xq^u$, for $q=(5/4)^{10}/(3/2)^6$.

For every word of length $k$, $2^kT^kn=3^{P_k}n+B$ with $0\le B\le3^k-2^k$. The bound follows by induction, using $B'=B$ at an even step and $B'=3B+2^j$ at an odd step at clock $j$. For the light starts this gives $T^kn\le a^u X+(3/2)^k$, where $a=729/1024$. Their endpoints are distinct because their chronological indices are distinct and the segment is simple. Thus

$$
 N(X)\le 2Xq^u+Xa^u+(3/2)^{10u}+10u .
$$

Both $q^4$ and $a^4$ are less than $1/2$ by integer arithmetic. Now $2^{20u}\le X<2^{20u+20}$, the carry is at most $X^{1/2}$, and $10u\le X^{79/80}$ (for $u\ge1$, $10u\le2^{4u}$). The inequality $3\cdot2^{1/4}+2<6$ proves the first bound of (2). Integrate the count of segment entries in $[M,t]$ against $dt/t^2$ from $M$ to infinity to get the second. Both bounds also apply after restricting to odd states.

For the precise multiplicative correction write

$$
 D_h(n)=\frac{2^hT^hn}{3^{P_h(n)}n}
       =\prod_{\substack{0\le j<h\\T^jn\ \mathrm{odd}}}\left(1+\frac1{3T^jn}\right).  \tag{3}
$$

The equality follows step by step. If the $h$ departed states are distinct and their odd states are at least $M$, (2) gives $0\le\log D_h(n)\le160M^{-1/80}$, using the natural logarithm. In particular $\log D_h(n)\le160$ for every simple prefix. A related elementary estimate is present in the repository in an odd-accelerated form. García and Tal's published density result concerns orbit sets. The argument above supplies the finite-segment reciprocal estimate used here. [Repository sparsity argument, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/4fd8af31c1ea525252b4d8f7411b5921dd447048/research/astra-three-routes/pass3/FINITE_RECORDS.md) · [García and Tal, *A note on the generalized 3n+1 problem*, Acta Arithmetica 90 (1999)](https://doi.org/10.4064/aa-90-3-245-250)

## 2. The finite classes

Once (1) holds, both equalities persist at all later common clocks. This proves transitivity by extending two witnesses to the later clock, and reflexivity and symmetry are immediate. Equation (3) gives $D_h(x_r)=D_h(x_s)$ at every witness.

First fix $s$ whose reference $y=x_s$ is not eventually periodic. Every linked source has an injective forward orbit, as a repeat would make its common tail eventually periodic. If $r\ne s$, $h>0$ since $x_r\ne x_s$. The reference is odd, so $D_h(y)\ge1+1/(3y)$. Choose an integer $M$ so large that $160M^{-1/80}<\log(1+1/(3y))$. Every such $x_r$ visits an odd $z<M$ before its witness clock, by (3) and the uniform tail estimate. For each particular $z$, any two linked sources $x,x'$ visiting it at times $i,j$ must have $i=j$. They are physically equal at some common clock $t$, so at time $t+i+j$ one has $T^{t+j}z=T^{t+i}z$. The orbit from $z$ is injective. There are at most $2^iz$ positive starts reaching $z$ at the resulting fixed time $i$, since $2Tn\ge n$. The finite set of possible $z$ therefore supports only finitely many linked sources. The gates may differ from the states on the reference orbit.

Next suppose $y$ is eventually periodic. Its cycle consists of positive integers. Fix one phase $z$, its least period $L>0$, and $q=P_L(z)$. We have $q>0$, since an all-even period would force $2^Lz=z$. By (3), $2^L/3^q=D_L(z)>1$. All linked sources reach this cycle. For each, let $h$ be its first time at $z$ and $p=P_h(x_r)$. The departed prefix is simple, since a repeat before this first hit would either exclude $z$ or already traverse it. The integer

$$
 I=L(r+p)-qh                                                       \tag{4}
$$

is constant on the class. Indeed advance a common augmented meeting beyond the two hits and then to a common visit at $z$. The added time and odd count from each designated hit are $jL,jq$ for a nonnegative integer $j$, since the return times at $z$ are multiples of its least period. Both sources then have identical augmented count and elapsed time. Evaluating (4) there proves the claim. By (3),

$$
 I=(L-q\log_2 3)(r+p)+q\log_2(z/w)-q\log_2 D_h(x_r).
$$

The coefficient of $r+p$ is strictly positive, while $\log_2 D_h(x_r)\le160/\log 2$. Thus $r+p$, and hence $r$, is bounded on the class. The two cases exhaust every fixed reference. The same finiteness holds for an even base: write $w=2^a u$ with $u$ odd. Distinct starts remain distinct during their shared first $a$ halving steps, and removing or prepending these steps preserves linkage. An infinite set of exponents cannot be a finite union of finite classes, giving the assertion about minima.

For a reference with an actual hit $T^k x_s=1$, the positive cycle has $L=2,q=1$. If $T^h x_r=1$ as well, then

$$
 r\sim_w s\quad\Longleftrightarrow\quad 2(r+P_h(x_r))+k=2(s+P_k(x_s))+h .  \tag{5}
$$

For sufficiency use the common clock $h+2(s+P_k(x_s))=k+2(r+P_h(x_r))$. Each extra cycle lap returns to 1 and adds one odd step. For any linked source, eventual coalescence first provides such a hit, and the pointwise inequality $2^hT^hn\le4^{P_h(n)}n$ gives

$$
 4^r2^k\le 4^{s+P_k(x_s)}3^r w .                                 \tag{6}
$$

In particular $r>0$ never links to exponent zero on the tower $w=1$, even if $3^r$ has an ordinary hit at 1. [Lean proofs of (5) and (6)](AugmentedMerger.lean)

The [bounded-lag theorem](HIGH_GATE.md) extends finiteness to ordinary two-arm mergers with a fixed nonperiodic reference and any fixed bound on the difference between the two clocks. Neither clock itself is bounded. It also gives a direct binomial certificate for automatic linkage of common-clock mergers on high simple paths.

## 3. A two-arm rigidity theorem for bounded numbers of powered words

First set $i=0$. We prove more than Theorem 2 needs. For all sufficiently large $r$, every indicated two-arm ordinary meeting with $0<b\le w$ and arbitrary $s\ge0$ has $b=w$, equal clocks, and equal augmented counts. The threshold depends on the fixed bank, $K$ and $w$.

A nonempty word of length $E$ with $P$ odd departures induces the rational affine map $n\mapsto\alpha n+\beta$, where $\alpha=3^P/2^E$ and $\beta=B/2^E$. Since $E>0$, $\alpha\ne1$. Its fixed point $C=B/(2^E-3^P)$ is rational with odd denominator, and may be zero. Fix an ordered list of $k\le K$ words. Let $e_j>0$ be their repetition counts, let $F_j=\prod_{l=1}^j\alpha_l^{e_l}$ with $F_0=1$, and denote the respective fixed points by $C_j$. The endpoint from start $n$ is $F_kn$ plus a sum of at most $k+1$ corrections,

$$
 -C_1F_k+\sum_{j=1}^{k-1}(C_j-C_{j+1})F_k/F_j+C_k .             \tag{7}
$$

Iteration of the affine map about its fixed point proves (7). The empty word list has slope 1 and no correction. Every correction is a fixed rational coefficient times a suffix slope, including the complete slope or the empty suffix. Drop zero coefficients, including all corrections when the list consists solely of all-even words.

**The finite-rank input.** For a homogeneous vanishing sum of monomials in fixed nonzero rational numbers, select an inclusion-minimal vanishing subset containing a distinguished term. Such a subset has no nonempty proper vanishing subsum: if a zero subsum omits the distinguished term, removing it gives a smaller one that still contains that term. Divide by another term and move that term to the opposite side, obtaining a nondegenerate unit equation with fixed rational coefficients. Evertse, Schlickewei and Schmidt prove that it has finitely many solutions in a multiplicative subgroup of finite rank in characteristic zero. In this application, after fixing both ordered word lists and $b$, every vector of variable term ratios is generated by varying one of the integer parameters $r,s$ and the at most $2K$ repetition counts by one. The subgroup is contained in a product of copies of $\mathbb Q^\times$ and has rank at most $2K+2$. The rational coefficient ratios remain fixed outside this group. Finite possibilities for a projective ratio give finite possibilities for its ternary valuation. A two-term vanishing sum gives a constant ratio directly. [Evertse, Schlickewei and Schmidt, Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04)

Subtract the two expressions (7), including the leading source terms, and divide by the total slope of the arm with **larger total odd count**, choosing either in a tie. Call this the primary arm. The normalized primary leading term is its start up to sign. For every correction, its ternary valuation is at most the valuation of its fixed coefficient: the suffix odd count is at most the number of odds on that arm, which is at most the primary total. If the minimal vanishing subset containing the primary leading term includes a correction, their ratio has finitely many possible valuations. The primary start therefore has bounded ternary valuation. These bounds are uniform over the finitely many choices of lists, subsets, orientations and $b$.

If the subset has no correction then the two leading terms cancel. Writing $H_A,H_B$ and $P_A,P_B$ for the two total lengths and odd counts, this gives

$$
 2^{H_B}3^{r+P_A}w=2^{H_A}3^{s+P_B}b .
$$

Since $w$ is prime to 6, $w\mid b$, hence $b=w$. Taking the 2-adic valuation gives $H_A=H_B$, after which $r+P_A=s+P_B$. The actual endpoint equality supplies the other part of (1).

It remains to treat bounded primary valuation. If the primary arm starts at $x_r$ then $r$ is bounded immediately. Otherwise $s$ is bounded, so the contender $3^sb$ belongs to a finite set. From **each fixed positive integer seed** there are only finitely many possible endpoints under the given bank and block budget, even with unrestricted powers. To see this for one block, write its fixed point as $A/D$ with $D$ positive odd. After $e$ actual repetitions from $n$ to $m$, integrality gives

$$
 2^{Ee}(Dm-A)=3^{Pe}(Dn-A).
$$

If $Dn=A$, then $m=n$ for every allowed repetition count. Otherwise $2^{Ee}$ divides the fixed nonzero integer $Dn-A$, bounding $e$. Iterating this finite branching through at most $K$ blocks proves the assertion, also for $P=0$ or an empty list. For each resulting fixed endpoint $m$, divide the source-arm endpoint equation by its total slope. The distinguished term is $3^rw$. Every other nonzero term has valuation bounded by its fixed coefficient valuation: the corrections have nonpositive variable valuation and the terminal term is $-m/F_k$. The same minimal-subsum argument then bounds $r$. There must be another term in a vanishing subset since the distinguished term is nonzero. This proves the unsmoothed rigidity claim, including either zero clock.

For a target $2^i3^sb$ with target clock $H_B\ge i$, remove exactly the first $i$ even steps. The remaining target word is a suffix of its original block string. A cut inside one repetition leaves a suffix of that single bank word, the remaining repetitions of that word, and the subsequent original blocks. A finite expanded bank containing every nonempty suffix of the original words, and budget $K+1$, therefore represents every resulting trace, including the empty trace. The preceding rigidity claim applies with common clock $H_A=H_B-i$. For a proper lower-cone target it forces a link to $s<r$ on the same base.

If $H_B<i$, the meeting state is $2^j3^sb$, $j=i-H_B>0$. The source is odd, so a source clock zero is impossible. At its first departure $2T(x_r)=3x_r+1$ is prime to 3, and every later state stays prime to 3 (halving preserves ternary units and every odd step produces one). Thus $s=0$ and $3\nmid b$. The remaining equation is a source trace ending at $2^jb$, where $j$ is unbounded. Apply the fixed-endpoint argument above with terminal term $-2^jb/F_k$. Its valuation is again bounded above by $v_3(b)$, and the extra parameter $j$ adds at most one generator to the finite-rank group. This bounds $r$ uniformly here as well. The case $H_B=i$ was already covered by removing all $i$ steps. These arguments allow all-even blocks on either arm, an all-even target path, and a power-of-two terminal state.

Apply this rigidity to every sufficiently high class minimum from Theorem 1. A two-arm merger to the full lower cone would have to give exactly the earlier link that the minimum excludes. This proves Theorem 2. The finite-rank argument is qualitative, and does not provide a numerical threshold for $r$. [Prior one-arm argument and exact affine normalization](../../round11/formal/BOUNDED_TEMPLATE.md)

## 4. Implications for the ordinary frontier

On the tower $w=1$, every $r\ge2$ meets the numerical hypotheses in the existing FrontierMerger statement. The residue of $3^r$ modulo 8 is 1 or 3, so $2^{v_2(3^r+1)}\le4\le3^r$, and $3^r\bmod512$ cannot equal 85 since $85\bmod8=5$. Thus infinitely many exponents in its actual numerical domain escape **every given** fixed bank and budget. The bank and budget are chosen before the infinite exceptional set. A finite bank containing the two one-letter words with a growing budget can describe every parity word, so Theorem 2 does not cover that case.

In the positive direction, the PR206 finite tower-block theorem produces recurring runs of 513 exponents in one linked class on each odd tower. Its written extension through the PR146 finite-list construction produces such runs of every prescribed finite length. Combined with Theorem 1, this yields finite classes of unbounded size on each tower and arbitrarily long intervals without a class minimum (use the run after its first exponent). Its fixed-tower density transfer, conditional on the PR146 quantitative pair-absorption estimate, gives upper Banach density zero for the failures of linkage between adjacent exponents. For clarity, a complete length-$h$ binary grid has $O(2^h/\sqrt h)$ nonabsorbed residues at initial pair state $(1,0)$ under that input. Absorption gives equality of endpoints and equality of compensated odd counts. The values $3^rw$ visit a cycle of $2^{h-2}$ distinct residues modulo $2^h$ for $h\ge3$, as follows from $v_2(3^{2^a}-1)=a+2$ for $a\ge1$. Thus for any $N\ge8$ consecutive exponents, take $h=\lfloor\log_2 N\rfloor$. They traverse at most eight full or partial periods and contain $O(N/\sqrt{\log N})$ adjacent pairs without absorption by $h$. The constants are uniform in the location of the interval and the fixed odd base. The conditional density estimate and the unconditional finite-class theorem can hold together: each class minimum other than 0 lacks an adjacent link, even when these minima have density zero. [PR206, including its input qualification](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontier.md) · [PR146 proposed pair estimate](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md) · [Leen, quantitative synchronization preprint](https://doi.org/10.5281/zenodo.23268755)

For a first failure at base $w$ and exponent $r$, every actual ordinary meeting to the lower cone would convey Good from the competitor, irrespective of odd counts or clocks. In particular such an $r$ must itself be an augmented class minimum: linkage to an earlier exponent would pass Good from that exponent. The missing pointwise assertion is existence of such a merger at the individual first failure. In particular, on an augmented class minimum, same-base affine cancellation alone cannot supply it. Neither the quantitative pair estimate nor the finite-block analysis constructs the requisite different merger there. The ordinary theorem and Collatz remain open.

The Lean module checks linkage equivalence, visit-time rigidity, the exact stopping-certificate criterion and ceiling, and the pure-power obstruction against exponent zero. The module also proves the charge identity (4) at any pair of hits of the designated phase, for any supplied period. The reciprocal and logarithmic estimates (2)–(3), the full finite-class theorem, the unit-equation application and its two-arm consequence have written proofs. [Lean kernel](AugmentedMerger.lean) · [Finite ordinary-orbit checks](check.py)
