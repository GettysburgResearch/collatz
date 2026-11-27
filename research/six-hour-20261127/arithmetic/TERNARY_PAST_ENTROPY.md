# Binary pasts give sharp hereditary energy and force long descents

Let $\mathcal B$ be the union of the odd phases of all positive ordinary cycles whose accelerated exponents belong to $\{1,2\}$. No height bound, period bound, common component or least-disagreement assumption is needed for the first two conclusions.

1. Every finite $A\subset\mathcal B$ contains no nonconstant three-term arithmetic progression. Its ordered additive energy and sumset satisfy
   $$
       E(A)\le |A|^{\kappa},\qquad |A+A|\ge |A|^{4-\kappa},
       \qquad \kappa=\log_2 6 .
   $$
   A progression of length $L\ge1$, at any nonzero integer spacing, contains at most $2^{\lceil\log_3 L\rceil}$ points of $\mathcal B$. There is an exact smaller occupancy function below.
2. The same energy bound holds modulo $3^n$ for any set of distinct residues admitting $n$ binary odd predecessors. The exponent is sharp for the wider class of all ternary residue trees with at most two children per vertex. The sharpness claim is for these trees.
3. Consider primitive ordinary binary cycles of unbounded odd periods $p$, minimum $s$, and maximum at most $Cs$, for any fixed $C$. Put $\gamma=\log_2 3$. For every subsequential weak limit $\nu$ of their uniform cyclic valuation-word laws,
   $$
          h_2(\nu)\ \ge\ \frac{3\gamma}{\kappa}
                   \limsup\frac{\log p}{\log s}
   $$
   with the limsup on that subsequence and entropy in bits per odd edge. This uses fixed-place Subspace-Theorem separation through Weaver's Paper 145. With the additional quoted bound $\mu(\gamma)\le3$, it gives $h_2(\nu)\ge\gamma/\kappa>3/5$. In particular some $c_C>0$ and $p_C$ ensure at least $c_C p$ occurrences of **three consecutive exponent-two descents** at every $p\ge p_C$. A positive proportion of actual run starts satisfy $x\equiv257\pmod{384}$ and $x\ge1+64(s-1)/27$. The constants are ineffective.

Weaver's Paper 145, Theorem 7, gives a hereditary bound from a Boolean encoding of canonical-height-one cycles, with a logarithmic transfer loss and a conclusion for their full shortcut state set. Paper 31 treats unrestricted finite shortcut segments through return equations. Here the two-branch ternary past is the restriction, and the unweighted bounds above apply directly to the odd physical integers. Paper 74 already uses reverse determinism for binary valuations. The scalar inequality in the energy argument is Kane–Tao's Lemma 8. PR195's population result gives the basic ordinary-word entropy bound and a positive density of $17\bmod48$ canonical phases from two successive twos. The entropy-bin transfer below forces three successive twos in every fixed physical ratio. [Kane–Tao, §2](https://arxiv.org/pdf/1702.00912) · [Weaver, Paper 145](https://rstation.ai/problems/collatz/papers/145/v1) · [Weaver, Paper 31](https://rstation.ai/problems/collatz/papers/31) · [Wren, Paper 74](https://rstation.ai/problems/collatz/papers/74) · [PR195, population and canonical sources](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/cycles/PHASE_POPULATION.md) · [Chudnovsky, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

## The two choices in a ternary cylinder

For a binary odd step ending at $y$, its exponent $a\in\{1,2\}$ is fixed by $2^ay\equiv1\pmod3$. The earlier source is $(2^a y-1)/3$. Consider a residue class modulo $3^j$ with a binary past through these $j$ steps. Every representative has the same exponents in these steps. Indeed the inverse of a common step divides endpoint differences by three and multiplies by the unit $2^a$. The three lifts to $3^{j+1}$ have three distinct residues modulo three at the end of the $j$-step reverse calculation. Exactly two of those residues admit one further binary predecessor. This gives a ternary tree read from the least significant digit, with at most two children at every occupied prefix of any selected endpoint family. Its missing digit can depend on the entire prefix. For an actual forward word $w$ of length $n$ and total valuation $T$, the endpoint residue $2^{-T}B(w)\bmod3^n$, $B(w)=\sum_{i<n}3^{n-1-i}2^{E_i}$, consequently recovers the word uniquely backwards. A positive odd lift realizing each word exists by the usual forward dyadic cylinder, and the checker verifies such lifts directly at depths through eight.

Three residues in arithmetic progression have all three trits in the first digit where their common difference is a unit. In particular if three integer endpoints have $n$ binary predecessors, their progression spacing is divisible by $3^n$. Equivalently one can reverse all three at once while the spacing is divisible by three. They use the same native exponent, their earlier sites remain a progression, and their spacing loses exactly one factor of three. An additional backward step at a unit spacing would require three nonzero trits. Repeating for all $n$ proves the progression-free assertion.

More generally, let $v+dt$, $0\le t<L$, $d\ne0$, be an integer progression. Strip the common prefix of length $v_3(d)$. On the remaining digits, translation and multiplication by the unit $d/3^{v_3(d)}$ permute the three children of every prefix. Hence the occupied indices have at most two ternary children per vertex. Writing $D(0)=0,D(1)=1$, define $D(3q+r)$ for $3q+r\ge2$, $0\le r<3$, as the sum of the two largest values among $D(q+\mathbf1_{j<r})$ for $j=0,1,2$. A consecutive interval has fiber sizes $q$ or $q+1$ modulo three. Recursion proves an occupancy bound $D(L)$, with $D(3^j)=2^j$ and $D(L)\le2^{\lceil\log_3 L\rceil}$. It is attained among unrestricted two-child trees, since the two chosen subtrees may be filled separately at each vertex. For finite pasts the argument needs only $v_3(d)+\lceil\log_3 L\rceil$ steps.

## A sharp bound on ordinary four-sums

For a subset $A\subset\mathbb Z/3^n\mathbb Z$ supported on a two-child tree, split at the initial trit. Write $A_i$ for the quotient residues of the at most two fibers, with an empty fiber available. The three unordered pair sums of two distinct trits have different residues modulo three. In a self-energy collision the two pairs of trits therefore have the same multiset and the first ordinary digits cancel. Writing $r_i(t)$ for the difference multiplicities in each child group modulo $3^{n-1}$ gives exactly
$$
 E(A)=E(A_0)+E(A_1)+4\sum_t r_0(t)r_1(t).
$$
Cauchy–Schwarz bounds the mixed sum by $\sqrt{E(A_0)E(A_1)}$. The two subtrees can have different missing digits at all later levels. Using the inductive bounds for these individual subtrees, Kane–Tao's scalar inequality
$$
 u^\kappa+4(uv)^{\kappa/2}+v^\kappa\le(u+v)^\kappa\qquad(u,v\ge0)
$$
closes the induction. The depth-zero group gives the base case. Choosing constant allowed digits zero and one at each level gives $2^n$ leaves and exactly $6^n$ modulo-$3^n$ collisions, so the exponent is sharp on the abstract trees. Four different equally embedded sets, with any prescribed signed residue, have at most the geometric mean of their four self-energies by Fourier Hölder. For a finite set of ordinary cycle phases take $3^n$ larger than its diameter, to distinguish every phase. Integer equalities are among the residue equalities, giving the asserted integer energy bound. Cauchy–Schwarz yields the sumset estimate.

## Keeping the entropy of each actual bridge

Take the four cut-conditioned $n$-edge interiors, two guards $g=\lceil\eta n\rceil$, seven cuts and true source circle of the earlier physical source proof, with $n\sim(\log_3 s)/3$. Its uniform bounds hold at every origin of a cycle lying in $[s,Cs]$ with fixed $C$. Every origin is low. The real parameter $\varphi=\log_2(x_0/s)+O((n+g)/s)$ puts all dates in a common strip of fixed width about $i\gamma+\varphi$. Its integer floor breakpoints and both sides of the lower strip at each cut give $O(n+g)$ phase types. The seven endpoint dates have boundedly many possibilities in each type. Including both guards costs $O(g+\log(n+2))$ bits. The deep input is precisely the separation of ordinary integer four-sums from quantized four-sum grid collisions within each segment. [Ordinary placement, exact reciprocity, separation and convolution](FOUR_COPY_TAILS.md)

Choose an origin uniformly among the $p$ odd phases. Write $W_n$ for the random chronological length-$n$ native word and $H_n$ for its Shannon entropy in bits. In every interior additionally record
$$
       J_j=\lfloor-\log_2\Pr(W_n=w_j)\rfloor
$$
for the word actually present there. All four marginals are the same by cyclic invariance. The four recorded integers range from zero to $\lfloor\log_2p\rfloor$. Thus their total entropy cost is $O(\log\log(2p))$, which is $O(\log(n+2))$ since $p\le Cs$. In bin $J$ there are at most $2^{J+1}$ words.

Fix all recorded data. Interior $j$ uses a fixed total valuation $T_j$ and a family $\mathcal W_j$ of $N_j\le2^{J_j+1}$ actual words. Raw ordinary numerator equalities imply signed equalities of their terminal residues $2^{-T_j}B(w)\bmod3^n$. Distinct words have distinct residues and these residues lie on the binary-past tree. Thus this family's ordinary four-sum collision count is at most $N_j^\kappa$. The located four-segment bound gives at most $6\prod_jN_j^{\kappa/4}$ actual sources in the environment. It bounds the larger Cartesian product of segment families; the original cyclic words need no independence. Taking conditional entropy of the origin and averaging gives
$$
  \log_2 p\le O(g+\log(n+2))+\frac\kappa4\sum_j\mathbb E(J_j+1)
             \le O(g+\log(n+2))+\kappa H_n .
$$
For each fixed $d$, block subadditivity and stationarity give $H_n/n\le H_d/d+d/n$. Pass to the chosen weak limit at fixed $d$, then let $\eta\downarrow0$ and take the infimum over $d$. This proves the stated entropy bound. If $\mu(\gamma)\le3$, the native product $0<(\sum e_i)/p-\gamma\le1/(3s\ln2)$ gives $\liminf\log p/\log s\ge1/3$ on an unbounded family, after reducing the fraction's denominator if necessary.

## A positive density of three-step descents

If the fraction of $222$ occurrences tended to zero on an unbounded family, take a weak limit of its uniform phase laws. It gives $222$ zero probability at every position. Its letter frequencies are $a=2-\gamma$ for one and $b=\gamma-1$ for two, by the same cycle product. In a finite word without $222$, the initial run of twos has length at most two. Each subsequent one carries a run of zero, one or two twos. Weight these options by $1,2,4$. For fixed counts $(u,v)$ the number of words is at most $7^{u+1}2^{-v}$. Conditioning on the number of ones in a block of length $d$ costs at most $\log_2(d+1)$ bits. Consequently
$$
        h_2(\nu)\le a\log_2 7-b<43/72<3/5<\gamma/\kappa .
$$
The strict comparisons follow from $3^{12}>2^{19}$, $7^6<2^{17}$ and $3^5>6^3$. This contradicts the entropy lower bound, giving the positive-density conclusion.

Across $r$ consecutive twos the exact affine map is $x\mapsto1+(3/4)^r(x-1)$. In the fixed band $[s,Cs]$, $s\to\infty$, every such run has length bounded in terms of $C$. Hence a positive density of the phases are starts of runs of at least three twos, preceded by a one. The preceding edge gives $x=2\bmod3$. The next three give $x=1\bmod128$ by the odd endpoint and the exact formula. Their common residue is $257\bmod384$, and comparison of the third successor with $s$ gives the height lower bound. On the least-disagreement branch this also gives a positive density of the previously established good tripling marks at this finer class. These results leave cycles containing the required long descents open.

The Lean proof checks finite-depth progression spacing and the all-depth exclusion over actual signed affine predecessor steps, together with first-trit pair-sum separation. The energy induction, scalar inequality import, source separation and Shannon argument are written mathematics. The exact control independently lifts all binary words through depth eight, checks modular progressions and energy recursions, enumerates all 2,187 complete two-child trees of depth three, and verifies the finite entropy comparisons. [Lean proof](TernaryPast.lean) · [Exact checker](check_ternary_past.py) · [Integer output](TERNARY_PAST_CONTROLS.json)
