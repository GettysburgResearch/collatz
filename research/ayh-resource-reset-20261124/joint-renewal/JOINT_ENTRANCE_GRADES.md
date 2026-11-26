# Uniform joint first-entrance clock residues on the actual head edges

**Written quantitative theorem using the finite binary-grid profile estimate of PR 146.** Use the positive shortcut map, with one clock at either an even or an odd input. Fix a four-trit suffix $0\le r<81$. At the parameter $n$ use the two actual starts $x_1=81n+r,x_2=n$. For each arm separately fix *any* entrance set $S_i\subseteq[1,Y]\cap\mathbb N$. The sets, floor bound and clock modulus can all change between sampling intervals. For each arm let $H_i$ be its first entrance time, $V_i=T^{H_i}x_i$ its entrance state, and $P_i$ the number of odd inputs strictly before that entrance. Give an arm that never enters its set the symbol $\infty$.

On a source with at least one entrance record the following data.

- $K$ consists of the hit/miss pattern, the exact values $V_i$ for each hitting arm, and, if both hit, the signed integer differences $H_1-H_2,P_1-P_2$. Further deterministic labels of these data may be included.
- Use the first hitting arm in **index** order (arm 1 if it hits, arm 2 otherwise), and let $G=(H_i,P_i)\bmod m$ for this arm. Thus the available other arm's modular clock pair is recovered from $K,G$. Put both-miss sources in one distinct state with no grade.

For uniform parameter $n\in[X,X+L)\cap\mathbb N$, with $X,L,Y,m$ positive integers, $L\le X$, write $\mu$ for this law. Define $\bar\mu$ to keep its actual $K$-marginal and its both-miss mass, and to replace $G$ on the remaining mass by an independent uniform element of $(\mathbb Z/m)^2$. Use total variation distance in its supremum-over-events convention. Put $\theta=\log_3 2$, $w=L/X$. For **any** integer $h\ge1$ such that $2^h\le L$ and $2^h Y<X$, and any continued-fraction denominator $Q\ge5$ of $\theta$,
$$
 d_{\rm TV}(\mu,\bar\mu)
 \ \ll\ \min\left\{1,\frac{mQ}{\sqrt h}+\frac{m}{wQ}\right\}.                 \tag{1}
$$
The implied constant is absolute once the PR 146 constant is fixed. It is uniform in the suffix, both entrance sets, the number of distinct entrance pairs, and the sizes of the signed differences. There is no natural-density or positivity input for any basin. Mixing the 81 suffix laws preserves the bound, even if the suffix is included in $K$. In particular $X=7\cdot81^{j-1}, L=81^{j-1}$ gives precisely all full head children for $j\ge1$. Subintervals of parents give shorter patches.

Every event involving the whole triple of entrance states, clock differences and grades is covered by the *same* total variation bound. For any selection determined by $K$ on the hit part, of original probability $\delta>0$, the conditional distance from its retained $K$-law times uniform is at most the right side of (1) divided by $\delta$. This does not assert a small relative error on an arbitrarily rare fiber.

## The transport at one dilation

For the following fixed maps use the full binary-grid assertion in PR 146. For two forms $z,3^s z+D$ with the bounded integer parameters used here, all but $O(2^h/\sqrt h)$ residue classes of $z\bmod2^h$ support a symbolic fusion at some common $t\le h$. Its two affine profiles agree on all positive lifts. In particular the numbers of odd inputs on the two arms of this fusion satisfy $p_{\rm base}=s+p_{\rm scaled}$: equality of the slopes on all the lifts forces this exact equation. Both signs of $D$ are allowed. The variables $z=n,81n+r$ each have odd coefficient of the free parameter. On every complete parameter period the grid counts therefore apply to each arm individually. A finite union and tiling by complete periods bound the exceptional fraction by $O(1/\sqrt h)$ on **every** interval of length at least $2^h$. No independence between arms or between successive tests is used.

Consider a single digit $d$ of the dilated parameter $n'=cn+d$ for $c=2,3$. Write $z=x_i(n)$, $z'=x_i(n')$; then
$$
 z'=cz+D,\qquad
 D=d\quad(i=2),\qquad D=81d-(c-1)r\quad(i=1).
$$
These offsets are uniformly bounded. At $c=3$ the preceding fusion with $s=1$ compares $z,z'$ directly. The two prefixes have the same length, and the new arm has one fewer odd input. All their states through the fusion are greater than $Y$, because $z,z'\ge X$, the prefix length is at most $h$, and every step satisfies $T(a)\ge a/2$. Thus each old and new arm has the same hit/miss status and eventual first entrance value. On a hit the *exact* differences new minus old in $(H_i,P_i)$ are $(0,-1)$, even if $S_i$ contains several points on a cycle.

For $c=2$, put $e=D\bmod2\in\{0,1\}$. The physical first step from $z'$ gives $3^e z+C$, where $C=D/2$ if $e=0$ and $C=(3D+1)/2$ if $e=1$. Apply the same grid to $z,3^e z+C$. The extra first step contributes exactly $e$ odds, canceled by the count difference at the later fusion. All source values on each arm exceed $Y$ before fusion: the new source is at least $2X$ (since $n'\ge2X$ and both arms dominate their parameter), so the total length up to $h+1$ is allowed. On a hit the differences are $(1,0)$. This includes $D<0$, where $C$ is interpreted as a signed integer and all actual orbit inputs are positive. If the common future never meets $S_i$, both arms still carry the same missing symbol.

Let $\tau_{(a,b)}$ translate only the graded part by $(a,b)$ and fix both-miss. The residue $d$ was arbitrary, and for a uniform $n$ and uniform digit $d<c$, the integer $cn+d$ is exactly uniform on $[cX,c(X+L))$. The test thus provides TV bounds $O(h^{-1/2})$ between the law on the double interval and $\tau_{(1,0)}\mu$, and between the law on the triple interval and $\tau_{(0,-1)}\mu$. Both use the *same* frozen $S_i$. In either comparison the differences in $K$ are preserved on all good sources. The two physical arms can synchronize with their respective dilates at different clocks. Equality of those two clocks is unnecessary. These two estimates iterate for $k$ doublings or $l$ triplings at cost $O((k+l)/\sqrt h)$: at every larger scale the period-length and safety inequalities continue to hold with the original $h,Y$. This is a triangle inequality on laws, not a product of probabilities of success on transported samples.

## Near-equal scales with independent modular shifts

Fix arbitrary residues $u,v\in\{0,\ldots,m-1\}$. There exist positive integers $k,l\ll mQ$ with $k\equiv u,l\equiv v\pmod m$ and $|k\theta-l|\le 2m/Q$. Indeed, set $k=m(Q+j)+u$, $0\le j<Q$. The $Q$ points $j\theta\bmod1$ come within $2/Q$ of any point, by comparison with the full rational grid of a convergent of denominator $Q$. Approximate $(v-u\theta)/m-Q\theta$, and choose $l=v+m t$ with the corresponding integer $t$. Positivity of $l$ follows from $Q\ge5$, $\theta>1/2$ and the stated error.

If $m/(wQ)$ exceeds a small absolute constant the claimed bound is trivial after adjusting its constant. Otherwise $2^k/3^l=1+O(m/Q)$. Uniform laws on the two integer intervals $2^k[X,X+L)$ and $3^l[X,X+L)$, interpreted as **full intervals** and not as sparse dilates, have TV distance $O(m/(wQ))$. Indeed the sum of absolute endpoint displacements divided by the shorter interval length has this bound. Both integer endpoints are exact; applying any record function only decreases total variation. Combining the two dilation estimates gives
$$
 d_{\rm TV}(\mu,\tau_{(k,l)}\mu)\ll mQ/\sqrt h +m/(wQ).
$$
The positive sign of the second coordinate comes from moving the tripling shift $(0,-l)$ to the opposite side. This holds for every translation in the entire grade group with the **same** bound. Averaging all the translates of $\mu$ gives exactly $\bar\mu$, including the atom with no grade. Convexity of total variation proves (1), without a loss of $m^2$.

## Resolution, and the signed-difference obstruction

For $Y\le X^{1-\epsilon}$, $L\ge X^{1/2}$, fixed $0<\epsilon<1$, one can take $h\asymp_\epsilon\log X$. At $\log X\asymp Q^4$ the bound is $O_\epsilon(m/(w(\log X)^{1/4}))$. For example $m\le(\log X)^{1/10}$ on patches of relative width $w\ge(\log X)^{-1/10}$ gives $O_\epsilon((\log X)^{-1/20})$ along those scales. The permitted sequence of $X$ can be restricted to actual ternary head levels by rounding their logarithms with bounded additive error.

On every sufficiently large scale take the greatest convergent denominator $Q\le h^{1/4}$. Then $Q\gg\log h$ by the elementary inequality $|q\theta-p|\gg2^{-q}$ at convergents, obtained from $|2^q-3^p|\ge1$ and the mean-value theorem. Thus (1) is at most $O(m h^{-1/4}+m/(w\log h))$. An effective all-scale power follows from the classical Baker–Wüstholz linear-forms theorem: $|q\theta-p|\ge c q^{-A}$ at convergents for absolute effective $A\ge1,c>0$, hence the next denominator is at most $C q^A$. Taking the largest $Q\le h^{A/(2(A+1))}$ gives $O(m/(w h^{1/(2(A+1))}))$. The explicit convergent bound (1) does not use this external result.

For example, among any positive-mass selection by both physical landing states and exact clock gaps, no rule predicting either common modular grade from the other and the retained data can succeed on more than a $1/m$ fraction of the selected mass plus the absolute error in (1). The grade entropy does **not** randomize $H_1-H_2$, $P_1-P_2$, or $V_1,V_2$: the new transport fixes all four. In particular the product law permits arbitrary mass on unequal entrance colors. The global obstruction remains a bound on those retained off-diagonal landing weights or a different physical comparison that moves their signed differences.

## What can be localized to actual opposite-color sources?

Suppose $f(Tz)=f(z)$ is any two-color labeling. Let $B(n)$ mean $f(81n+r)\ne f(n)$, and restrict the stopped law to the retained event where *both* entrances exist and $f(V_1)\ne f(V_2)$. This event implies $B(n)$. Let $h_j=\lfloor\tfrac12\log_2(81^{j-1})\rfloor$ for the full head levels; these are distinct, and they are safe for every polylogarithmic floor at all sufficiently large levels. The ordinary bound for the head process from $(4,r)$ gives $O(h_j^{-1/2})$ for the **entire** discordant fraction. Thus (1) alone does not yield nontrivial conditional equidistribution on that population.

Two terms in its comparison proof do permit sharper estimates. Write $h=h_j$ and retain a low-grade cutoff $K_h$ here, distinct from the retained data label $K$. At a single dilation comparison from an interval $J$ and digit $d<c$, let $E_h(J,c,d)$ be the fraction of original $n\in J$ for which

1. $B(n)$ or $B(cn+d)$ holds, and
2. on at least one of the two arm-to-dilate symbolic comparisons used above there is no symbolic fusion by clock $h$ and its terminal slope level exceeds $K_h$.

The binary comparison starts *after* the extra physical first step of the dilated arm. This definition uses the actual jointly sampled quadruple. In particular $E_h$ is not a product of two single-pair survival probabilities.

Let $g_h$ be the sum, over the finite list of comparison start states $(s,D)$ in the one-digit construction, of their full binary-grid probabilities of surviving to $h$ at level at most $K_h$. For **every** event of the stopped law restricted to the opposite-color entrances, the one-step error is bounded by
$$
 C g_h+\max_{d<c}E_h(J,c,d).                                      \tag{2}
$$
Indeed, whenever neither source is discordant both event indicators vanish. Outside the two symbolic-comparison failures the event changes exactly by its grade translation. An unfused low-level comparison costs at most a constant times its full-grid bound on any interval $|J|\ge2^h$, since each base arm has odd parameter coefficient. All other errors belong to the stated $E_h$.

The companion killed-grade occupation proof applies to any **fixed finite** initial state list: the PR 146 survival input there is $O_{s,D}((1+h)^{-1/2})$ for each start, its killed drift bound holds for signed offsets, and the occupation estimate allows arbitrary initial level and offset. The zero state contributes zero. Hence for nondecreasing $K_h$ the companion proof gives
$$
 \sum_{j:H\le h_j<2H}g_{h_j}\ll (1+K_{2H})^2/\sqrt H.
$$
Consequently the accumulated **low-level** contribution to (2) over at most $O(h_j^\gamma)$ one-digit dilations per comparison is summable over all rows when $K_h\le C h^\beta$ and $2\beta+\gamma<1/2$. This remains true when translating every modular bin and then averaging, because the number of bins does not multiply the error. No condition on how the original discordant edges are distributed was used for this summable term.

There is also a direct improvement at the near-scale comparison. Put $D_*=\min(2^k,3^l)$ and assume $m/(wQ)$ is small. For events restricted as in (2), comparison of the two dilated full intervals costs at most
$$
 {C\over\sqrt h}\left({m\over wQ}+{2^h\over D_* L}\right).          \tag{3}
$$
Every excluded endpoint strip of integer length $b$ contains $O((b+2^h)/\sqrt h)$ discordant parameters, by tiling it with full binary grids for the **original** head comparison $(4,r)$, including a final incomplete period. On the shared interior, the two different normalizing factors differ by $O((m/Q)/(D_*L))$; its total number of discordant parameters is $O((D_*L+2^h)/\sqrt h)$. Summing the interior and the endpoint strips proves (3), with both original interval locations retained.

Equations (2) and (3) identify which transport errors can affect a rare discordant selection. They do not bound the high-level joint term. Marginal first-landing caps also cannot be multiplied by a comparison's survival probability without a joint count on the same original parameter. Even for two events with identical marginal probabilities $p$, their intersection can have probability $p$. The two comparisons here use the same future binary source bits. A further multi-arm estimate or a physical transformation changing the signed differences is needed before concluding conditional mixing on the discordant population.

## Which symbolic transports can change a signed gap?

This limitation extends beyond the two single-digit constructions. Take two head families at deletion depth $s$ whose child and parent coefficients in a common parameter $t$ are $(3^s A,A)$ and $(3^s B,B)$, with arbitrary fixed offsets and $A,B>0$. Pair their arms in either order. On a matched old/new pair of source coefficients $U,V$, suppose two fixed physical parity words of lengths $a,b$ and odd counts $p,q$ give equal endpoints for **two distinct** parameter values on which those words are legal. The two endpoint functions of $t$ are affine. Equality at two points forces equality of slopes, hence
$$
 U\,2^b3^p=V\,2^a3^q,\qquad
 b-a=v_2(V)-v_2(U),\qquad q-p=v_3(U)-v_3(V).
$$
This is the elementary slope comparison from PR 146's affine classification; the following calculation applies it to both head arms simultaneously. If the words precede first entrances into the same set on each matched pair, restoring the common tail on a hit makes $b-a$ and $q-p$ the shifts of its **total** first-entrance grades. In a crossed match the target sets are crossed with their arms, or the argument can use the same target set throughout.

For the ordered pairing both ratios $V/U$ are $B/A$. Consequently the signed child-minus-parent clock gaps $(\Delta H,\Delta P)$ are preserved exactly. In the crossed pairing the ratios for the new child and new parent are $3^sB/A$ and $B/(3^sA)$, respectively. Subtract their signatures to obtain
$$
 (\Delta H',\Delta P')=(-\Delta H,-2s-\Delta P).
$$
Thus both $|\Delta H|$ and $|s+\Delta P|$ survive **every** such two-word-per-match transport with a bijection of the two arms. At the fixed head $s=4$ the second reflection is about $-4$. The assertion allows unequal word lengths, arbitrary positive recoding parameter strides and cylinder-dependent offsets. It does not cover a three-to-one merger of the four starts, nor a coincidence on just one ordinary parameter.

Even a point-specific change has a necessary clock cost. For the matched arms $Ut+b_0,Vt+d_0$, suppose their physically legal prefixes of lengths at most $H$ meet but their endpoint slopes differ. The shortcut numerator offset $B_i$ in $2^iT^i(n)=3^{p_i}n+B_i$ satisfies $0\le B_i<3^i$, by induction (on an odd final step, $B_{i+1}=3B_i+2^i$; the sharper invariant $B_i\le3^i-2^i$ makes the induction immediate). Clearing the two endpoint denominators gives an integer coefficient of $t$ with absolute value at least one and an offset of magnitude at most
$$
 (|b_0|+|d_0|+2)6^H.
$$
Hence a change in either absolute gap by a matched pairing on a single parameter $t>0$ requires $t\le(|b_0|+|d_0|+2)6^H$ on at least one match. This reproduces PR 146's pointwise delay estimate at the relevant mismatched arm, with no parity-fairness assumption. It gives no useful lower time when the recoding offsets grow comparably to $t$. The underlying single-pair bound is prior work. [PR 146 affine families](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md).

[AffineGradeRigidity.lean](AffineGradeRigidity.lean) checks equality of slopes from two parameter values, the two valuation identities, and the ordered and crossed prefix conclusions for arbitrary $s$. The stated passage to first entrances uses the common tails in the earlier formal bridge. These results specify the proof obligation for moving a signed difference; they do not supply such a transformation on the surviving states.

Leen's *Joint laws and local synchronization for Collatz minima and arrival times*, §7, is credited in the later *Conditional clocks and source couplings for Collatz synchronization* with growing-modulus total-variation independence of stable labels from **initial source residues**. Proposition 1 of the latter paper strengthens the source-residue result to individually normalized cells and nonnegative periodic weights. Here the randomized coordinates are the two **accumulated first-entrance clocks** and the retained data include the two-arm clock gaps. The one-digit proof uses source-grid fusion as an input. The later text was inspected directly; Leen's deposited full text was inaccessible during this check. [Leen's record](https://doi.org/10.5281/zenodo.23268759) · [Source-residue proposition and scope](https://rstation.ai/problems/collatz/papers/13/v1).

PR 193's fixed-modulus weighted stopping-time theorem at target one already implies a fixed joint law there by finite Fourier inversion. The result here gives a growing-modulus total-variation bound on moving short intervals, arbitrary varying entrance sets, and conditioning on the two actual landing states and both integer differences. It leaves the mass of the corresponding invariant data unrestricted.

The four declarations in [EntranceGrades.lean](EntranceGrades.lean) formalize the safe physical prefix, transfer of exact first entrance and odd counts, transfer of missing status, and the finite group averaging inequality retaining the other data. The full profile and number-theoretic bounds above are written mathematics.

[PR 146 finite profile law, frozen](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [PR 193 fixed weighted clocks, frozen](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-heavy-machinery-20261124/dynamics/WEIGHTED_CLOCKS.md) · [Classical linear-forms input](https://doi.org/10.1515/crll.1993.442.19)
