# Independent review of the tower estimates

**Verdict.** The tower developments establish a counting theorem for physical descents below the base and a bounded-gap theorem for mergers of adjacent exponents on one odd tower. I reconstructed their algebra and quantifiers and rebuilt their source files in a fresh output directory. I authored their imported arithmetic dependency `PhysicalEcho.lean`. My independent review applies to the tower arguments; it does not provide independent authorship of that dependency.

| Reviewed file | SHA-256 of rebuilt source |
|---|---|
| `fixed_source/TowerDescent.lean` | `17d9758604a1cdfc775ddf1755c6cca6f304ffca9d99a6feb66932565be6a0ce` |
| `fixed_source/TowerWindows.lean` | `81adb06400f2e3bdb0180e8b87808902440bbe07f75794b3adcef55149588eb7` |
| `fixed_source/BinomialTower.lean` | `7a8a22aece95ce42fa2a057b6a54e172eb413c50abc87d7128dc10eec6f1a3a7` |
| `machinery/PhysicalEcho.lean` | `b4c007afc3b5f620fb626b7085b6a72dadae9ed7243127fe96a07a077e9832dd` |

I used Lean 4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612` with `-DautoImplicit=false -DwarningAsError=true`. Lean compiled a fresh copy of each source in dependency order and printed only subsets of `propext`, `Classical.choice` and `Quot.sound` for the audited declarations. The checks used the installed Mathlib build.

## Counting physical endpoints

Fix $r,h,a$ and vary the base as $w=a+i$ with $0\le i<2^h$. If two parity codes agree, their seeds $3^r(a+i)$ agree modulo $2^h$. Cancellation of $3^r$, subtraction of $a$, and the interval for $i$ give identical indices. There are $2^h$ indices and $2^h$ length-$h$ binary words, so each word occurs exactly once for each *fixed* exponent. The empty word at $h=0$ also gives a one-point bijection.

For a code of weight $q$, the endpoint bound is $2^h T^h(n)\le 3^q(n+2^h)$. For example, after dividing the exact affine numerator by $3^q$ the additive correction is a sum of terms $2^j/3^{q_{j+1}}$ over odd positions $j<h$. Its sum is at most $\sum_{j<h}2^j<2^h$. With $w\ge2^h$, $r\le R$, $q\le K$, the upper bound becomes $3^K(3^R+1)w$. The strict coefficient budget $3^K(3^R+1)<2^h$ therefore gives $0<T^h(3^rw)<w$ for positive $w$.

Consequently every failing base for that exponent has $q>K$. For $0\le B\le A$, its monomial weight $A^q B^{h-q}$ is at least $A^K B^{h-K}$, by replacing $q-K$ factors $B$ by $A$ without dividing. Summing over the bijection gives $(A+B)^h$. Summing the resulting bound over $r=0,\ldots,R$ is a union bound and allows arbitrary correlations between the codes. Division by the threshold is valid only when it is positive. The Lean theorem retains the multiplication inequality even in the degenerate zero-weight cases.

For $(h,K,R,A,B)=(1024,576,64,9,7)$, the exceptional fraction is at most $65\,16^{1024}/(2^{1024}9^{576}7^{448})<0.021353$. On every base outside the union, each of the 65 source trajectories reaches its own positive smaller base at clock 1024. The endpoint can depend on $r$. A least bad base with a known offending exponent in the window must be inside this union. Neither the count nor the existential good-base conclusion puts a particular prescribed base outside it.

## Seven-step same-ray mergers

At seeds 23 and 69 the five-step flights end at 20, with respectively three and two odd inputs. On the full progression $x=23+32k$, the pair $x,3x$ therefore has the same endpoint $20+27k$ at clock 5, and still agrees at clock 7. At seeds 59 and 177 the seven-step flights end at 38, with respectively four and three odd inputs. On $x=59+128k$ the common endpoint at clock 7 is $38+81k$.

The multiplier 3 acts on the 64 odd residues modulo 128 in two cycles of length 32, represented by 1 and 5. In the first cycle the only target is 59 at position 27. In the second the targets at positions 7, 15, 23, 31 are 55, 23, 119, 87 respectively. Thus every starting phase hits one target within an offset from 0 through 31, and residue 49 first hits at 31. I regenerated this cycle enumeration separately. The statement gives some adjacent pair in each block. It supplies neither a prescribed pair nor descent below the tower base.

## A rank-specific counting improvement with a kernel-checked certificate

Instead of assigning every rank the same cutoff, put $h=1024$ and define $K_r$ to be the largest $k\le h$ with $3^k(3^r+1)<2^h$ for $0\le r\le116$. For each fixed $r$, the physical code bijection gives exactly $\binom{h}{j}$ candidate bases of weight $j$. The number of ordinary failures for that rank is bounded above by $\sum_{j>K_r}\binom hj$. Writing $D_R$ for the sum of these upper bounds over $0\le r\le R$, integer comparisons give

$$
 \frac{D_{64}}{2^{1024}}<0.000019538,\qquad
 \frac{D_{115}}{2^{1024}}<0.919766,\qquad
 D_{116}>2^{1024}.
$$

In particular more than 8.0234% of the bases in every full block beginning at or above $2^{1024}$ have an actual lower-base descent at clock 1024 for *all 116* exponents $0,\ldots,115$. If bases are restricted to either class $1,5\pmod6$, take $2^{1023}$ consecutive terms of that progression. The map into odd-starting words is injective because $v_2(6)=1$, and it is bijective by cardinality. The weight-$j$ count in each class is $\binom{1023}{j-1}$. Thus the exceptional fraction in each class at $R=115$ is below $0.978462$, giving more than 2.1538% good bases in this eligible population. At $R=64$ the exceptional fraction in each class is below $0.000022456$. For the lower-base implication the first progression term must be at least $2^{1024}$. The last comparison exhausts this particular union estimate. It gives no lower bound on the number of actual failures. The reviewed `BinomialTower.lean` proves the generic exact binomial union bounds for both populations. My separate `TowerCertificate.lean` proves the strict 116-exponent probability budgets by an exact consecutive-binomial recurrence, checked with `decide +kernel`. Its theorems `full_block_116` and `odd_ray_116` consume the bounds to obtain the ordinary lower-base endpoints. All four principal declarations audited with only `propext`, `Classical.choice` and `Quot.sound`. The following independently executed Python 3 certificate checks both fractions and the next-rank limitations.

```python
from math import comb

h = 1024
population = 2**h
row = [comb(h, j) for j in range(h + 1)]
assert sum(row) == population
odd_row = [0] + [comb(h-1, j-1) for j in range(1, h+1)]
assert sum(odd_row) == population // 2
total = 0
odd_total = 0
for r in range(117):
    p = 3**r + 1
    k = max(j for j in range(h + 1) if 3**j * p < population)
    total += sum(row[k + 1:])
    odd_total += sum(odd_row[k + 1:])
    if r == 64:
        assert 10**9 * total < 19538 * population
        assert 10**9 * odd_total < 22456 * (population // 2)
    if r == 115:
        assert 10**6 * total < 919766 * population
        assert 10**6 * odd_total < 978462 * (population // 2)
    if r == 116:
        assert total > population
        assert odd_total > population // 2
```

## The exact single-rank test at clock 1024

The additional Lean theorem `TowerCertificate.exact_clock_1024` proves, for every $w\ge2^{1024}$ and every $r\ge0$,

$$
 T^{1024}(3^rw)<w
 \quad\Longleftrightarrow\quad
 r+q_{1024}(3^rw)\le646 .
$$

The supporting lemma `affine_sandwich` retains the exact linear term $3^qn$ and bounds the entire nonnegative additive remainder by $3^h$ in the numerator $2^hT^h(n)$. Indeed the remainder bound satisfies $A_{h+1}\le2A_h+3^h$ on peeling off the first physical step. At the chosen clock the certified integer margins are $3^{1024}<(2^{1024}-3^{646})2^{1024}$ and $2^{1024}\le3^{647}$. Thus the remainder cannot change which side of the threshold the ordinary endpoint lies on.

For one exponent, the failing fraction in a full dyadic block is therefore *exactly* the binomial upper tail $2^{-1024}\sum_{j+r\ge647}\binom{1024}{j}$. The fixed odd progressions have the analogous tail for the remaining 1023 free bits after the leading odd bit. Using these marginal tails only improves the simultaneous union estimate for $R=115$ by less than $10^{-16}$ in each population. It yields the same rounded certified fractions and does not change the 116-exponent boundary. The remaining information needed to improve the union estimate materially is joint behavior across different ranks.
