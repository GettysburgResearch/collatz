# Prescribed ternary digits and two thin dyadic progressions

**PROPOSED.** Work with the positive shortcut map and the ordered component comparison in [the main proof](README.md). All uses of its grid estimate (3) retain the PR 146 source qualification. The first two statements here are independent of any predecessor-density hypothesis.

### All prescribed words on one parent

Let $d$ be the initial dyadic row exponent, $m=\lfloor\log(d)/12\rfloor$, and let $\ell$ be the largest integer with $3^\ell\le d^{.30}$. Outside a relative fraction at most $\exp(-d^{.01}/2)$ on the same initial row and prescribed binary residue as in (1), **every** word $c_1,\ldots,c_m$ of units modulo $3^\ell$ is realized on a chain of the theorem. Its $i$th new unit $u_i$ obeys
$$
 u_i\equiv c_i\pmod {3^\ell},\qquad
 \max\{v_2(3u_i+1),v_2(9u_i+1)\}\ge \lceil d^{.25}\rceil .
$$
The initial ordered component pair is the same throughout each chain and across these choices of chains.

For either denominator $q_0=3,9$, enlarge the lower endpoint of the exponent menu to $\max(k_0,\lceil d^{.25}\rceil)$. At stage $i$ choose the first exponent with $2^k V\equiv 1+q_0 c_{i+1}\pmod{q_0 3^\ell}$, where $V$ is the original arm specified by grade order. The residue on the right and $V$ are units. The order of 2 modulo $3^j$ is $2\cdot3^{j-1}$: $4=1+3$ and cubing $1+3^a w$, $3\nmid w$, increases the valuation of its difference from one by exactly one. Reduction modulo 3 supplies the factor two. Thus the search radius is $O(d^{.30})$. The low prefix determines $V\bmod q_0 3^\ell$, since its grade is $\gg D\gg\ell$. This choice lifts to an ordinary odd unit having precisely the requested congruence (no exact valuation at $\ell$ is required).

The residual grade discrepancy $g$ in (3) is now $O(d^{.30})$, including the imposed dyadic exponent. Still $g=o(\sqrt h)$, $h=\lceil d^{.74}\rceil$. The additive offset bound becomes $\log(2+|J|)\ll 1+k+g+\log(2+E_i)$, allowing for either grade order after tuning. The existing $8\lceil M\rceil$ allowance in $K_{i+1}$ absorbs the new additions for large $d$. Every other grid and fiber bound of the main proof is unchanged. In particular each word separately has exceptional fraction at most $\exp(-d^{.01})$. There are at most $(d^{.30})^m=\exp(O((\log d)^2))$ words. The union bound gives the simultaneous assertion, with a possibly different physical chain for each word.

### A single stage with deeper dyadic and ternary requirements

There exists an absolute $c>0$ for the fixed tripling input $n,3n$ with the following property. Write
$$
 H(x)=\sqrt{\log(2+x)/\log\log(16+x)} .
$$
For any prescribed ternary unit $\beta\in\mathbb Z_3^\times$, outside $O(d^{-3})$ of all parents on dyadic row $d$, the two ordered components of $n,3n$ have an odd unit representative $u$ with
$$
 2^{.80d}\le u<2^{.85d+1},\qquad
 \max\{v_2(3u+1),v_2(9u+1)\}\ge c H(u),\qquad
 3^{v_3(u-\beta)}\ge c H(u).                                      \tag{5}
$$
Use $v_3(0)=+\infty$. All statements are uniform in $\beta$; only a finite residue of $\beta$ enters at each row.

Indeed take $h=\lfloor d/(C_1\log d)\rfloor$ and checkpoints spaced $h$ apart in $[3d/4,7d/8]$, with a sufficiently large fixed $C_1$ so that $2^{-\#\mathrm{checkpoints}}=O(d^{-4})$. Use an unconditioned initial row. Requiring each physical count within $C_2\sqrt{d\log d}$ of $t/2$ and both scalar errors at most $d^{12}$ at every checkpoint costs $O(d^{-4})$, taking $C_2$ large and using the scalar square-root moment. Choose $3^\ell$ largest below $\delta\sqrt h$ and impose $k\ge\lceil\delta\sqrt h\rceil$ in the two menus, where $\delta>0$ is fixed sufficiently small. Taking $c_{i+1}=\beta\bmod3^\ell$ now gives $g\le C_3\delta\sqrt h+O(1)$ and $k=O(\sqrt{d\log d})$. The square-root-log-offset term of (3), divided by $\sqrt h$, tends to zero, since $\log(2+|J|)=O(k+g+\log d)$. The grade term is at most $C_4\delta+o(1)$. Choosing $\delta$ using the absolute grid constant makes the conditional failure probability at most $1/2$. The same checkpoint argument supplies a good success on the original parent outside $O(d^{-3})$. The height bounds and the comparison $\sqrt h\asymp H(u)$ prove (5), decreasing the absolute $c$ as needed.

For an **unordered** pair one may fix either $q_0=3$ or $q_0=9$ in advance, and replace the maximum in (5) by $v_2(q_0u+1)$. Select the smaller-grade state $V$ regardless of its original arm. For $q_0=3$ lift $V$ to the first state and compare the other lift state against the larger-grade arm using the lower formula. For $q_0=9$ lift $V$ to the second state and compare the first state using the upper formula. In a grade tie, either arm may serve as $V$ and the exponent search in the upper formula starts at 2. The same estimates hold in both cases. The returned pair still witnesses every initial disagreement. Its orientation can depend on which arm had the smaller grade.

### Consequence for a universal convergence proof

Assume the fixed-target positive-lower-density premise **M** used in [PR 197, macroscopic pair closure](https://github.com/GettysburgResearch/collatz/blob/b0538639df0ab7edd239281bd897e705160f732c/research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md). Under failure of Collatz, the harmonic sum of odd tripling defects for the basin-of-one color diverges. To specify this implication, PR 195's [two-sided series bound](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/head/README.md#the-full-two-sided-series-and-its-power-threshold) charges the full normalized head series to the harmonic sum of odd tripling defects. Summability of that full series rules out a counterexample under M in the cited macroscopic closure result. The bounded comparable-height [directed-cut inequality (3) of PR 146](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/DIRECTED_TRIPLING.md#consequences-for-directed-cuts) then implies divergence separately in both directions, by summing comparable octaves with reciprocal weights.

The discarded parents of (5) have finite harmonic weight. Thus every proposed counterexample would force arbitrarily high actual unit failures of **each** orientation on the common two-center set (5), for every prescribed $\beta$. An eventual directed unit implication there, for either one chosen orientation, would imply universal convergence under M. If both directions are tested, the unordered construction shows that either named center $q_0=3$ or $9$ alone suffices. These are pointwise tests. On the dyadic row of exponent $j$ the two-center set itself has relative size $O(2^{-c'\sqrt{j/\log j}}+2^{-j})$ from the dyadic condition alone. Its entire harmonic weight is therefore finite, including when no orbit condition is imposed.

The first missing step on this route is equality of the two actual basin labels on the stated sparse arithmetic inputs (or a directed implication on their union) for one prescribed $\beta$. The written descent counts establish no such equality. Without M the classical $X^{.84}$ predecessor exponent does not imply divergence of either harmonic sum, and the exceptional estimate in (5) alone permits a set that large.
