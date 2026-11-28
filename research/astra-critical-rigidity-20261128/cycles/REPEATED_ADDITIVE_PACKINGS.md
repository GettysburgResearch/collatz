# Polynomially many different near-complete packings of true phase quadruples

**Proposed written theorem.** Use the positive primitive rational cycle, true physical heights, complete \(q\), colors, bin width \(p^{-\kappa}/\log p\), and height and denominator exponents \(\sigma,\beta\) of the [physical additive-packing theorem](PHYSICAL_ADDITIVE_PACKINGS.md). Write
\[
 B=(\sigma+\beta-\kappa)/\gamma,\quad U=\omega\log_25,\quad
 K=(e-\omega)\gamma+U,\quad
 D_2=3(s+K)/5,\qquad D_3=9s/16+5K/8 .
\]
Fix \(\nu\ge0\). Among the same prescribed-color, four-distinct, physical equal-sum quadruples, declare any hypergraph of maximum vertex degree \(\le p^{\nu+o(1)}\) unavailable. Any maximal packing from the remaining quadruples has uncovered population \(J\) satisfying
\[
 \limsup\frac{\log(1+J)}{\log p}\le
 \kappa+\lambda+
 \max\{\nu+BU,\ BD_2+\nu/5,\ BD_3+\nu/4\}.                         \tag{1}
\]
The estimate is uniform over such forbidden families when their degree budgets are uniform. In particular, one can choose \(\lfloor p^\nu\rfloor\) successive packings whose **quadruple sets are disjoint across all rounds**, using (1) for the number of uncovered phases in each round. The four phases in a quadruple are distinct, and quadruples in one round are vertex-disjoint. A phase may occur in different rounds, with different sets of three partners.

Assume the imported \(\mu(\log_23)\le3\) and \(q=p^{o(1)}\). At limiting physical width at most four, and without prescribed colors or a polynomial shrinking factor, every
\[
                         \nu<4(1-3\theta_4)=0.16354626\ldots             \tag{2}
\]
allows \(p^{\nu+o(1)}\) different packings, **each** covering \(p-o(p)\) phases. In particular there are at least \(p^{1.16354626\ldots-o(1)}\) four-distinct physical equal-sum quadruples of relative width at most \(1/\log p\). The same estimate for every subset obtained by deleting \(o(p)\) phases follows by restricting the eligible vertices to that subset. For the two-sided itinerary coloring in the preceding theorem, the term \(\lambda=2c\gamma\) pays for exact simultaneous transport of every quartet through all \(|j|\le c\log_2p\) native dates. For instance \(\nu=0.06,\ c=0.006,\ \kappa=0\) have strict room in (1) at limiting width four. At any fixed translated date the transported quadruple sets remain different across rounds, because native translation is a bijection of the cycle phases. All numerical corollaries here use the same source-qualified measure hypothesis as the preceding theorem.

## How many unordered equal-sum relations can a local set have?

Consider a single bin and color in the uncovered population. Its \(M\) physical sources have induced degree at most \(d\), where \(d\ge1\) is the given forbidden-degree budget rounded up. Otherwise an allowed quadruple with all four phases still uncovered could be added. Hence their number \(C_4\) of four-distinct additive quadruples is at most \(Md/4\). At each center \(b\), let \(t_b\) count unordered pairs of distinct sources \(a,c\) with \(a+c=2b\). Different pairs representing this sum share no member. Moreover four distinct members have only one equal-sum pairing, its common sum determines \(b\), and sorting determines the pair partition. Thus \(\sum_b\binom{t_b}{2}\le C_4\). By Cauchy–Schwarz,
\[
     \sum_b t_b\le M+\sqrt{2MC_4}.
\]
Pairs with a member in common agree only if identical. Therefore the number \(C\) of nontrivial collisions between unordered physical pairs, allowing repeated members, is \(O(Md)\). The implied constant is absolute. This counts both genuine four-distinct edges and all possible repeated-center defects.

## Prefix entropy with a collision budget

Use all \(M\) words, without taking a Sidon subset. The exact calendar and the horizon \(n\) in the preceding theorem still imply singleton word injectivity and that equal coordinatewise unordered pair outputs force *actual* pair-sum equality. Different unordered word pairs with equal coordinatewise outputs therefore contribute at most \(C\) unordered collisions. Write \(g=\omega+u,\ f=e-g\) for the temporary angular margin in that proof. The code has \(sn+o(n),fn+o(n),gn+o(n)\) binary, ternary and five-symbol coordinates. Order them by decreasing alphabet size; a bounded number of endpoint symbols has no asymptotic cost.

Take a limiting subsequence with \(x=\lim(\log_2M)/n,\ z=\lim(\log_2d)/n\). If \(x\le z\), keep \(x\le z\). Otherwise take the longest prefix with possible capacity \(N\le M/(dn^2)\). Then \(\log_2 N=(x-z)n+o(n)\). The number \(T'\) of **distinct ordered pairs** \((u,v)\), meaning \(u\ne v\), which agree in the prefix is
\[
                   T'=\sum_h M_h^2-M\ge M^2/N-M\ge M(dn^2-1).
\]
Choose one uniformly. Record its suffix difference, with equal symbols producing zero and different symbols producing their ordered pair. If two different ordered pairs produce the same difference, their cross pairs have identical coordinatewise unordered pairs in the suffix. They also have this property in the prefix because the two members of each original ordered pair have identical prefixes. Those cross pairs are genuinely different: unordered equality \(\{u,v'\}=\{v,u'\}\) would give either \(u=v\), or \(u=u',v=v'\). Thus every off-diagonal coincidence of the difference produces one of the \(C\) original collisions, with at most eight possible orderings/inversions per unordered collision. If \(m_a\) is the multiplicity of a difference output,
\[
                \sum_a m_a^2\le T'+8C .
\]
The entropy of that output is at least its order-two Rényi entropy, hence at least \(\log_2T'-\log_2(1+8C/T')\ge (x+z)n-o(n)\).

For each coordinate, restoring the \(M\) diagonal pairs changes its outcome distribution in total variation by \(M/(T'+M)\le1/(dn^2)\). In this restored distribution the zero probability is at least \(1/h\) for an alphabet of size \(h\), by Cauchy–Schwarz within each prefix fiber. As in the [matched-code proof](MATCHED_SIDON_CODES.md), the entropy upper bound per coordinate is \((2-1/h)\log_2 h\), with \(o(1)\) error after conditioning away the diagonal by continuity on a fixed finite alphabet. This argument treats even high multiplicities of the same difference output.

Let \(K_u=f\gamma+g\log_25\). When \(x-z\le g\log_25\), use \(x\le z+g\log_25\). When \(g\log_25\le x-z\le K_u\), subadditivity on the remaining suffix gives
\[
           x+z\le 3s/2+(5/3)(K_u-x+z),
 \qquad x\le9s/16+5K_u/8+z/4.
\]
When \(x-z\ge K_u\), it gives \(x+z\le(3/2)(s+K_u-x+z)\), hence \(x\le3(s+K_u)/5+z/5\). Coordinates arbitrarily close to a regime boundary cost \(o(n)\). Multiplying by \(n/\log_2p\to B\), taking \(u\downarrow0\) and summing over the bins and colors proves (1). The argument applies to a largest cell even if the forbidden families, the colors, and the round chosen for producing the largest residual all vary with \(p\). This proves the stated uniformity.

At limiting width four \(U=0,\ B\le3/\gamma\) when \(\kappa=0\). A direct substitution gives \(3D_2/\gamma<3D_3/\gamma=3\theta_4\), and \(0<4(1-3\theta_4)<1\). Each of the three terms in (1) is strictly less than one whenever (2) holds. To generate successive rounds, mark every previously used quadruple unavailable. The vertex degree of this forbidden family after \(j\) rounds is at most \(j\), since one vertex belongs to at most one quadruple per round. Each nearly complete round has \((p-o(p))/4\) distinct new edges. This proves the claimed growth exponent by taking \(\nu\) arbitrarily close to the endpoint from below.

The method uses the Della Fiore–Dalai prefix difference proof on a code with controlled collisions, including a separate estimate for repeated-center physical relations. Attributing the homogeneous zero-collision argument and the physical three-grade chart as in the preceding theorem, no bound for arbitrary unrestricted mixed codes or additive-energy conjecture is assumed. [Original difference-code paper, Theorem 2.1](https://doi.org/10.1016/j.disc.2021.112751)
