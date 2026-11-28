# Long repeated common parity words and the cost of reaching their rational center

**PROPOSED written theorem.** Work with the ordinary positive shortcut map and the pair of odd sources $(s,3^r s)$. Denote their states at a common entry date by $A,B$, their entry grades by $g,h$, and their signed determinant by $d=3^g B-3^{h+r}A$. Suppose the paths are unmatched through the entry and the common block considered below. We give a criterion forcing a repeated word to have an exact rational center on the entry line. We then bound how cheaply a sparse periodic center can be reached, and exhibit ordinary families which really do shadow such a center.

## From a finite ordinary block to an exact rational equation

Let $w$ be a native parity word of length $L\ge1$, with $p$ odd letters and affine form $T_w(x)=(3^p x+C)/2^L$. Set $D=2^L-3^p$, which is odd and nonzero. Its rational center $z=C/D$ realizes the periodic parity tape $w^\infty$ over rationals of odd denominator. Indeed the word gives one input residue modulo $2^L$, characterized by divisibility of $3^p x+C$ by $2^L$. This characterization follows by induction on the prefixes, using invertibility of 3 modulo powers of 2. For $x=z$ divisibility follows from $3^p z+C=2^L z$. Repeating the word gives the same argument for every power of $w$.

Assume the next $LR$ steps from both actual states spell $w^R$, $R\ge1$. Then
$$
 2^{LR}\mid E,\qquad E=Dd-(3^g-3^{h+r})C.                                        \tag{1}
$$
Both entry states belong to the same residue as $z$ modulo $2^{LR}$. Multiplication by the odd $D$ and the determinant identity give (1). The bound $0\le C\le 2^L3^p$ follows from the usual affine offset recursion, and the [physical determinant estimate](PAIRED_SOURCE_GRADES.md) gives $|d|\le3^{g+h+r}$. Hence
$$
        |E|\le 3\,2^L3^{g+h+r+p}.
$$
Indeed $|D|\le 2\cdot2^L3^p$ and $|3^g-3^{h+r}|\le3^{g+h+r}$. In particular
$$
       L(R-1)>(g+h+r+p+1)\log_2 3                                     \tag{2}
$$
forces $E=0$. This is the exact affine-line condition
$$
                         d=(3^g-3^{h+r})z.                               \tag{3}
$$
When $g=h+r$, (3) would imply $A=B$, excluded by hypothesis. Thus $j=|g-h-r|>0$. The true ordinary paths may have different states throughout this entire block. The rational intersection in (3) concerns their common parity cylinder and its two affine entry maps.

Conversely, fix a physically realized pair of entry words with distinct slopes and (3). Along the lower entry branch the unique preimage $s_*$ of $z$ is rational of odd denominator: if its native clock is $t$ and offset $C_0$ then $s_*=(2^t z-C_0)/3^g$. This preimage lies in the required entry parity cylinder, since it differs from any original ordinary source in that cylinder by a multiple of $2^t$ in the rationals of odd denominator. The upper branch at $3^r s_*$ also has state $z$, as the entry determinant is constant on the shared source cylinder. For every $R$, all positive integers congruent to $s_*$ modulo $2^{t+LR}$ realize the original two entry words and the next $R$ copies of $w$. Each such integer differing from $s_*$ has distinct entry states by the distinct slopes. If it had met earlier it would have equal entry states. On the repeated word, a nonzero state difference is multiplied by a positive rational at every step. Thus all these lifts are unmatched. The same argument works directly from any rational special source $s_*$ with odd denominator and the stated unequal entry slopes.

## GCD obstruction for cycles of bounded odd grade

Fix $P\ge1$. Consider a family of exact centers (3) of words with $1\le p\le P$, with $L\to\infty$ and $j=|g-h-r|>0$. Then
$$
                                 L=o(j).                                 \tag{4}
$$
In particular these centers require $g+h+r$ growing faster than $L$. The hypothesis permits nonprimitive words and arbitrary choices of cyclic phase, time of entry and positive sources.

Write $z=a/q$ in lowest terms, $q>0$. For large $L$, $D>0$ and $C>0$. The integer $D$ is prime to 6 and $q\mid D$. Every phase on the positive rational cycle has exactly denominator $q$. Each step preserves the part of the denominator prime to 6, while the odd numerator rule ensures division by 2 never introduces a denominator factor of 2. Equation (3) shows $q\mid 3^j-1$, since its other power-of-three factor is prime to $q$.

Each phase of the cycle has value at most $2\,3^p$: rotate $w$, use its offset bound $2^L3^p$, and take $2^L\ge2\cdot3^p$. Among the $p$ gaps from one odd departure to the next, one has length $\ell\ge L/p$. Starting at its odd input $y$, the next odd input is $(3y+1)/2^\ell$, which is positive and at least $1/q$. Therefore
$$
                  q\ge\frac{2^{L/p}}{6\,3^p+1}.                         \tag{5}
$$

Apply Corvaja and Zannier to the pair of rational $S$-units $(u,v)=(2^L/3^p,3^j)$, $S=\{\infty,2,3\}$. Their Proposition 2 gives, along such distinct pairs,
$$
              \log\gcd(|2^L-3^p|,3^j-1)=o(\max(L,p,j)).
$$
Here the pair is multiplicatively independent by taking the 2-adic valuation of a potential dependence first, and then the 3-adic valuation. Proposition 2 gives actual one-dimensional subgroups. Even a fixed translated subgroup of the form $u^a v^b=c$ cannot contain infinitely many of these pairs: the 2-adic valuation gives $aL=v_2(c)$, forcing $a=0$; then $bj=v_3(c)$ forces $b=0$. Indeed (5) and $q\mid 3^j-1$ imply $j\to\infty$. A translated subgroup requires $(a,b)\ne(0,0)$. At primes outside $S$ the negative local logarithms in their (2.8) sum to minus the logarithm of the displayed gcd. The other local summands are nonpositive, which gives the required inequality in the stated direction. The rational logarithmic heights are $\max(L\log2,p\log3)$ and $j\log3$. Since $q$ divides that gcd, (5) contradicts any subsequence with $j=O(L)$. In particular, for $p=1$,
$$
                        \frac{\operatorname{ord}_{2^L-3}(3)}{L}
                                    \longrightarrow\infty .
$$
This last arithmetic assertion also follows directly by putting $j=\operatorname{ord}_{2^L-3}(3)$ in the same gcd inequality. The argument supplies no computable onset or exponential lower bound for the order. [Corvaja and Zannier, *A lower bound for the height of a rational function at S-unit points*, Proposition 2](https://arxiv.org/pdf/math/0311030)

## Actual repeated-word lifts with unequal entry slopes

For $q=2^L-3$, rational states $c/q$ have numerator step $c\mapsto c/2$ for even $c$ and $c\mapsto(3c+q)/2$ for odd $c$. The cycle beginning at numerator 1 visits $2^{L-1},2^{L-2},\ldots,2,1$. The table records exact synchronized entries for $r=1$.

| $L$ | $q$ | initial numerator $c$ | entry clock $t$ | common numerator | lower grade $g$ | upper grade $h$ | $j=h+1-g$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 5 | −7 | 17 | 1 | 6 | 9 | 4 |
| 4 | 13 | 1 | 9 | 8 | 3 | 5 | 3 |
| 5 | 29 | −1481 | 80 | 4 | 19 | 46 | 28 |
| 6 | 61 | 1 | 31 | 32 | 6 | 15 | 10 |
| 10 | 1021 | 343 | 74 | 512 | 9 | 42 | 34 |

In the last row every positive source congruent to $343/1021$ modulo $2^{74+10R}$ and its triple have unmatched actual prefixes of native length $74+10R$ and total grade $51+2R$. Their clock-to-grade ratio tends to 5. All these are ordinary integer examples, with the ordinary source allowed to vary as $R$ grows. No positive integer equals $343/1021$. The table does not supply an unbounded sequence of different periods. The asymptotic entry obstruction (4) is consistent with arbitrarily many repeats after any fixed successful entry.

The [finite replay](check_periodic_shadows.py) independently realizes rational-center itineraries by numerator iteration, reconstructs each physical lifted source using an inverse modulo a power of 2, and tests all native dates for a genuine inequality of the physical states. It also tests a short common repeated word with a nonzero obstruction in (1). [Exact controls](PERIODIC_SHADOW_CONTROLS.json)
