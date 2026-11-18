# Occupation of states with few binary runs

**PROPOSED.** Fix an integer R≥1. In any segment of N distinct positive odd Collatz states, the number with at most R runs of ones in ordinary binary notation is

$$
 O_R\left(N^{1-1/(2R)}(1+\log N)^{2R}\right).
$$

The estimate is uniform in the initial value and location of the segment. In particular, on any nonperiodic ordinary positive orbit, the set of odd event times with at most R binary runs has upper Banach density zero. The same holds for any fixed popcount cap, since each run contains at least one set bit. A run can have arbitrary length, as in the one-run sources $2^a-1$.

The map counts odd events, $U(n)=(3n+1)/2^{v_2(3n+1)}$. Use the extension $U(1)=1$ for describing a window after an input. A segment with distinct states can contain at most one occurrence of 1. The extension only supplies convenient bookkeeping outside such a segment.

The homogeneous multiplication and fixed-source carry separation idea comes from PR #141, head `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`, `research/ay-persistent-20261031/PROOF.md`, HC-1–HC-3. That packet treats capped popcount and one threshold crossing. Below we use signed run boundaries, an entire period of residues, and a disjoint-window count. All needed arithmetic is given here.

## 1. A signed cut survives a long gap

An odd n with r binary runs has the unique expression
$$
 n=2^{e_{2r-1}}-2^{e_{2r-2}}+\cdots+2^{e_1}-2^{e_0},
 \qquad 0=e_0<e_1<\cdots<e_{2r-1}.
$$
Each run from bit a through bit b contributes $2^{b+1}-2^a$. Zeros between different runs make the boundary exponents strictly increasing.

If some adjacent exponents satisfy $D=e_{i+1}$, $d=D-e_i$, split at D to write $n=2^D u+v$. Here u is a positive odd integer: the highest term is positive and dominates all smaller terms, and the term at D is odd after scaling. The alternating sum v is odd, can be negative, and has $|v|\le 2^{e_i}=2^{D-d}$. Extend the formula for U to negative odd integers. Its numerator cannot be zero, so all the shadow values $v_j=U^j(v)$ are nonzero odd integers.

Let $A_0=0$, and let $A_j$ sum the first j valuations of $3v_i+1$. Put $P_j=2^{A_j}v_j$. Then $P_{j+1}=3P_j+2^{A_j}$, $2^{A_j}\le|P_j|$, and $|P_j|\le 4^j|v|$. Fix $L\ge1$. If $d\ge2L+1$, then $|P_j|<2^D$ for $0\le j\le L$. Thus $A_j<D$. Induction on j gives
$$
 U^j(n)=2^{D-A_j}3^j u+v_j,\qquad |v_j|<2^{D-A_j}.
$$
Indeed at step j the upper contribution in the numerator is divisible by $2^{D-A_j}$, whereas $v_2(3v_j+1)=A_{j+1}-A_j<D-A_j$. Division gives precisely the next formula. Taking the integer quotient by $2^{D-A_j}$ leaves $3^j u$ if $v_j>0$ and $3^j u-1$ otherwise. Since $3^j u$ is odd, subtracting one changes only bit zero. Consequently **bits 1 through m−1 of $3^j u$ occur together as a substring of $U^j(n)$**, with higher zero padding allowed. Such padding adds no runs of ones.

## 2. Few times in a full residue period can have few runs

Take $m\ge3$ and $L=2^{m-2}$. The order of 3 modulo $2^m$ is L. Indeed $v_2(3^{2^s}-1)=s+2$ for $s\ge1$, by the difference-of-squares factorization, and odd exponents give valuation one. Thus $3^j u\bmod 2^m$, $0\le j<L$, are distinct odd residues. Dropping bit zero preserves injectivity among odd m-bit residues.

A length-(m−1) word with exactly t nonempty runs of ones has $\binom{m}{2t}$ possibilities: choose the 2t boundaries among the m positions between or just outside the digits. Let
$$
 B_R(m)=\sum_{t=0}^R\binom{m}{2t},
$$
with impossible binomials zero. A substring of a word with at most R runs has at most R runs. Therefore whenever the initial source has any run-boundary gap $d\ge 2L+1$, at most $\min(L,B_R(m))$ of the L states indexed $0,\ldots,L-1$ have at most R runs. This argument also bounds the count in every prefix of that window. It requires no independence assumptions about the signed lower shadow or subsequent windows.

## 3. A finite-time count and its consequences

For clarity this explicit bound works for every integer $m\ge3$:
$$
 \#\{0\le j<N:\ r(U^j(n))\le R\}
 \ \le\ \sum_{t=1}^R (2L)^{2t-1}
       +\lceil N/L\rceil\min(L,B_R(m)),
 \qquad L=2^{m-2}.
$$
Its sole trajectory hypothesis is that the N displayed states are pairwise distinct. Indeed a source with t≤R runs and every gap at most 2L is encoded by its $2t-1$ successive positive gaps, each at most 2L. The least exponent is zero because the source is odd. Such sources can appear at most the displayed first sum of times, even when separated by many different types of state.

Scan the time interval from left to right. At a low-run source with any gap exceeding 2L, reserve its next L time indices, truncated at the end, and resume after them. Otherwise advance one index. The starts of the reserved windows are at least L apart, and Section 2 bounds the occupancy in each one. All remaining low-run sources have only short gaps and the distinctness count applies. This proves the bound including the final partial window.

Choose $m=2+\max(1,\lfloor\log_2(N)/(2R)\rfloor)$, so $L\asymp_R N^{1/(2R)}$. The short-gap count is $O_R(L^{2R-1})$, and $B_R(m)=O_R((1+\log N)^{2R})$. Substitution gives the stated power saving. The bound is uniform over all intervals of length N on a nonperiodic orbit, because any repeated state would make the forward orbit eventually periodic. Dividing by N and taking the supremum over starting indices proves upper Banach density zero.

## 4. A growing run threshold

More quantitatively, fix any $0<c<1/\sqrt{8}$. There exists $\delta_c>0$ such that in every segment of N pairwise distinct odd states, all but
$$
 O_c\!\left(N\,2^{-\delta_c\sqrt{\log_2 N}}\right)
$$
states have **more than $c\sqrt{\log_2 N}$ runs of ones**. This controls a threshold growing with the observation window, independent of its position and starting height.

To see this, put $s=\sqrt{\log_2 N}$, $R=\lfloor cs\rfloor$, and choose $4c<\alpha<1/(2c)$. Take $m=\lfloor\alpha s\rfloor$ for sufficiently large N. After division by N the short-gap count is at most $R(2L)^{2R}/N=2^{-(1-2c\alpha)s^2+O_c(s+\log s)}$. Choose a fixed $2c/\alpha<p<1/2$; then $2R\le pm$ eventually. The binomial tail estimate $\sum_{i\le pm}\binom{m}{i}\le2^{m H_2(p)}$, where $H_2(p)=-p\log_2 p-(1-p)\log_2(1-p)<1$, follows by weighting each term by $p^i(1-p)^{m-i}\ge 2^{-mH_2(p)}$. The window fraction is at most $2 B_R(m)/L$ when $N\ge L$, hence at most $8\cdot 2^{-m(1-H_2(p))}$. The two bounds give the assertion, and changing the implied constant covers small N.

**Effective bounded-run consequence.** Choose m with $B_R(m)<2^{m-2}$, possible for every fixed R. In an orbit that stays below or at this run cap, no state can have a gap exceeding 2L by Section 2. All odd states therefore belong to the explicitly enumerable short-gap set in Section 3. Such an orbit repeats or hits 1. For each R one can decide whether there is a nontrivial positive cycle under that cap by searching this finite set and retaining only actual U edges in it. This is an effective finite decision procedure for each fixed R.

## 5. Adaptive enumeration through five runs

A smaller exhaustive core uses $h_R(u)=\min\{j\ge0:r(\lfloor 3^j u/2\rfloor)>R\}$ for positive odd u. This clock exists: choose m with $B_R(m)<2^{m-2}$ and apply the injectivity count of Section 2 to the shifted odd residues. At depth k the current prefix u has k signed boundary terms. Start with u=1 at depth one. For each $1\le d\le 2h_R(u)$ append the next boundary by replacing u with $2^d u+(-1)^k$. Include positive sources at even depths, and stop at depth 2R. The alternating signs give exactly the canonical boundary list. When the next gap instead exceeds $2h_R(u)$, Section 1 applied through that clock forces the full orbit above R runs: after removal of low bits and bit zero, the observed upper quotient is exactly $\lfloor3^{h_R(u)}u/2\rfloor$. At clock zero the quotient already occurs in the original source. Thus the first unadmitted gap at any parsed prefix certifies exit, and every permanently capped source lies in this finite enumeration.

A direct odd-orbit replay, stopping at 1, cap exit or repetition, gives the following results. The outside bound is the maximum $h_R(u)$ over all visited nonterminal prefixes. Clocks count odd events.

| Allowed runs | Core sources | Reach 1 inside cap | Maximum core clock | Outside clock bound | Source attaining core maximum |
|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 1 | 1 | 3 | 3 |
| 2 | 220 | 12 | 8 | 6 | 33 |
| 3 | 4,932 | 79 | 19 | 7 | 129 |
| 4 | 165,442 | 556 | 42 | 10 | 879 |
| 5 | 5,867,804 | 12,564 | 68 | 13 | 128,395 |

There were zero nontrivial repeats. In particular every positive odd source either starts above five runs, reaches 1, or exceeds five runs within 68 odd events. The 12,564 successes were also reconstructed as an exact set by backward search from 1. For odd unit targets q modulo 3 the first odd predecessor is $(2^a q-1)/3$ with $a\in\{1,2\}$ chosen for integrality. The complete remaining fan iterates $p\mapsto 4p+1$, which adds exactly one isolated low run. Multiples of three have no odd predecessor. Thus the finite cap cutoff applies on every fan, and complete backward search terminates because all successful states belong to the proven finite core.

Run `python -B experiments/binary-run-occupancy/check.py --cap 5` from the repository root. The checker additionally replays 360 signed-shadow windows, including negative shadows; the finite replays exercise the identities and do not replace their proofs.

**Open.** These conclusions impose an orbitwise restriction on a hypothetical divergent orbit. They give no global upper bound on binary runs, no lower bound on the frequency of low-run visits on every orbit, and no exclusion at unbounded R. Frequency throughout is at odd event times. No inference for sampling after each individual halving is made.
