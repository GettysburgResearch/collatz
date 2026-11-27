# Finite inverse comparisons permit full multiplicative rank

PR192 proves that at clock $i$ on an escaping component's height-minimizing orbit, every inverse depth $h$ gives a lower bound on its least admissible cost $V_h(y_i)$. It also identifies the largest carry amongst minimum-cost words at the actual depth. For $h>i$ the test begins reading ternary digits of the source. The following proposition tests whether arbitrarily many *finite* such comparisons constrain the multiplicative ranks or shared prime factors of the same segment. [PR192, commit `5720732`](https://github.com/GettysburgResearch/collatz/blob/5720732b9c83361f5cded4f8bfac24e36f469937/research/astra-universal-step-20261124/arithmetic.md)

**Proposition.** Take any actual positive odd trajectory segment $y_0,\ldots,y_N$ for the accelerated odd map, including a segment with repeats. At each position choose any finite list of inverse depths, allowing depths larger than $N$. There are arbitrarily large ordinary odd sources whose trajectory segments have all the following properties.

1. Every forward division exponent agrees with the given segment.
2. At every selected position and depth, exactly the same inverse words are admissible, with the same costs and carries. In particular the truth of $V_h(y_i)\ge\lceil E_i+(h-i)\log_2 3\rceil$, the minimum cost itself, and the maximizing carry amongst the minimizing words agree. The actual forward prefix is the same word whenever the comparison tests it. These arithmetic predicates can be evaluated on any orbit. Attainment of a global minimum of corrected height on a component is a separate hypothesis.
3. Every pair of corresponding positions has exactly the original numerical gcd.
4. All $N+1$ new odd states are multiplicatively independent. Each has a prime divisor dividing none of the other $N$ states. In particular any selected local minima have the maximal possible rank.

**Proof.** Let $E_i$ be the cumulative division exponent, $E=E_N$, and $C_i$ the chronological carry, so $2^{E_i}y_i=3^iy_0+C_i$. Take $B$ at least as large as every tested depth. Vary the source by $2^{E+1}3^B q$ for nonnegative integers $q$. The states become

$$
L_i(q)=y_i+a_i q,\qquad a_i=2^{E+1-E_i}3^{B+i}.
$$

All these lifts remain odd, including the last state. The added factor two at the origin ensures precisely this last parity. Substitution into $2^{E_{i+1}-E_i}L_{i+1}=3L_i+1$ now verifies each *exact* exponent. Each $L_i$ agrees with $y_i$ modulo $3^B$, so every selected inverse word of depth $h\le B$ has the same ternary integrality test. A positive odd endpoint always gives a positive odd inverse at each integral reverse step, as $2^e y-1>0$. The set of admissible words, and thus each cost and carry comparison, is identical.

For clarity, a competing word of depth $h$ and cost $F$ has ordinary origin $(2^FL_i(q)-C)/3^h$. The slope of its difference from $L_0(q)$ is $a_0(2^{F-E_i}3^{i-h}-1)$. Same-depth, same-cost comparisons have zero slope, so their ordinary origin ordering is preserved as well. Different clocks can have a nonzero slope. The proposition makes no assertion about preserving their numerical order or the corrected-height minimum of a new source.

For distinct $i,j$ the determinant $\Delta_{ij}=a_i y_j-a_j y_i$ is nonzero. In fact

$$
\frac{y_i}{a_i}=\frac{y_0+C_i/3^i}{2^{E+1}3^B},\qquad
\frac{C_{i+1}}{3^{i+1}}-\frac{C_i}{3^i}=\frac{2^{E_i}}{3^{i+1}}>0.
$$

Every common divisor of $L_i(q),L_j(q)$ divides $\Delta_{ij}$. Let $G$ be the least common multiple of the absolute nonzero determinants, using $G=1$ for an empty list. Impose $q\equiv0\pmod G$. Then for each pair its gcd equals $\gcd(L_i(q),L_j(q),|\Delta_{ij}|)=\gcd(y_i,y_j)$, since both lifts retain their residues modulo that determinant.

For each position choose a different prime $p_i$ dividing neither $G$ nor any $a_j$. Impose $q\equiv-y_i/a_i\pmod {p_i}$. At this residue $p_i\mid L_i(q)$, while $p_i\mid L_j(q)$ for $j\ne i$ would force $p_i\mid\Delta_{ij}$. All the imposed moduli are pairwise coprime, and the Chinese remainder theorem gives arbitrarily large $q$. The $p_i$-valuation of any relation $\prod_i L_i(q)^{n_i}=1$ forces $n_i=0$. This proves the proposition, including repeated original states.

The full cyclic word divisor is preserved as a *word predicate*: $D=2^E-3^N$ and $C_N$ only involve the prescribed exponents. When $D>0$ and $D\mid C_N$, the unique actual returning source for this word is $C_N/D$. A lifted source can have the same word, identical pairwise gcds, and maximal rank on the finite segment while its endpoint differs from its initial value. For instance the word of $N$ consecutive division exponents equal to two has $C_N=D=4^N-3^N$ and returning source one. This explains exactly where comparison with the specific quotient is required to use the divisor for an exclusion.

**First unsupported step.** The proposition preserves every prescribed finite subset of the inverse comparisons, including ones whose depths grow arbitrarily far beyond the prefix. Its sources depend on that finite subset. The rank and gcd estimates give no opposing upper bound at a *single* ordinary source satisfying all depths along its infinite forward orbit. Nor can multiplication of successive gcd-loss ratios around a cycle impose such a bound: for $g_i=\gcd(y_i,y_{i+1})$ on a cyclic list, $\prod_i(y_i/g_i)=\prod_i(y_{i+1}/g_i)$ identically. The proposition is a written Chinese remainder argument and supplies neither universal descent nor a new cycle exclusion.
