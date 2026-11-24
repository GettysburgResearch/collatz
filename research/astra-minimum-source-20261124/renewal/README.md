# Tripling comparisons on actual ordinary lifts

Use the positive shortcut map and let an invariant binary label be constant on each orbit. Write a defect for an odd positive q whose label differs from the label of 3q. If q is the least defect, every odd x strictly below q has equal labels at x and 3x. The arithmetic lane also proves that for the basin-of-one label every number up to q is good.

## Descent at the first even input of the bad triple

Write $3q=2^a b-1$ with $b$ positive odd and $a\ge2$. Put $r=3^a b$. After $a$ consecutive odd inputs the original triple is exactly $r-1$. Two tests discharge candidates at this actual clock, allowing arbitrarily large $a$.

**First test.** Suppose $r=1\bmod4$. The triple and $y=(3q-1)/2$ have a common ordinary future. In fact $y=2^{a-1}b-1$ reaches $r/3-1$ in $a-1$ steps. The value $r-1$ halves twice to $(r-1)/4$. Since $r/3=3\bmod4$, the value $r/3-1$ halves once and takes one odd step to that same integer. The initial runs follow from $T^i(2^i z-1)=3^i z-1$.

This discharges all of the following original sources.

| Residue condition on $q$ | Smaller-source proof that $y$ is good |
| --- | --- |
| $q=12k+5$ | $y=18k+7=T^2(3(8k+3))$. The odd integer $8k+3<q$ and its triple are both good by minimality. |
| $q=1\bmod4$, $q=0\bmod9$ | Put $u=q/3$, so $3\mid u$. The number $z=4u-1$ reaches $y$ in three steps, by the $4\bmod9$ row of the arithmetic table. The odd predecessor $(2z-1)/3=(8u-3)/3$ is positive and smaller than $q$. |
| $q=1\bmod4$, $q=3\bmod9$ | Again $4u-1$ reaches $y$. Now $u=3v+1$, so $4u-1=3(4v+1)$ and the odd input $4v+1$ is smaller than $q$. |

For example the first row includes arbitrarily large actual $a$. For any $a\ge3$ choose $b$ in the unique class modulo 36 with $b=(-1)^a\bmod4$ and $2^ab=16\bmod9$. These independent congruences give $2^a b=16\bmod36$, hence $q=(2^a b-1)/3=5\bmod12$. Every sufficiently large positive lift works.

**A test on the other parity class.** Suppose $s=3^{a-2}b=147\bmod256$. Here $r=9s=3\bmod4$. The ordinary inputs $9s-1$ and $s-1$ merge after eight steps on this entire progression. At its base, 1322 and 146 both reach 47, with two and four odd steps respectively. Increasing $s$ by $256t$ increases both endpoints by $81t$. Meanwhile $(3q-3)/4=2^{a-2}b-1$ reaches $s-1$ in $a-2$ steps. This gives an ordinary representative strictly smaller than $q$ for every $q>1$ in this family. Every exponent $a\ge2$ has such positive sources: one specifies $b$ modulo 256 by the displayed condition and independently modulo three by $2^a b=1\bmod3$.

Both first-exit deductions are checked for all lifts by the Lean declarations `first_exit_reduces` and `complementary_exit` in [UpperRepresentative.lean](UpperRepresentative.lean). The latter declaration proves label equality with the displayed smaller representative.

## Two discarded dyadic families

For q=8v−1, v≥1, the upper source 3q has actual trajectory
$$
  24v-3\to36v-4\to18v-2\to9v-1.
$$
The odd integer 6v−1 also reaches 9v−1 in one step, and 6v−1<q. Thus 3q is good under the preceding minimum hypothesis.

For q=8192t−21, t≥1, the following is an independent check of the root's shorter comparison. Define A=6912t−17. The first five steps from q end at A. Eight steps from 3A and thirteen from 3q both end at 2187t−5. To see the identities, the corresponding signed constant terms evolve as follows.

- From −21 the five-step trajectory ends at −17 with three odd inputs.
- From −51 the eight-step trajectory ends at −5 with three odd inputs.
- From −63 the thirteen-step trajectory ends at −5 with six odd inputs.

The leading coefficients are respectively 8192·27/32, 20736·27/256 and 24576·729/8192. All indicated parities persist on the ordinary lifts. The first coefficient is 6912 and the latter two are both 2187. Since A is an odd unit strictly between 0 and q, a defect at q would yield a smaller one at A. This family needs no condition at three and applies to any orbit-invariant binary label. In particular it disposes of the mixed direction with dyadic coordinate −21 and ternary coordinate 1 by an allowed smaller comparison.

## Remaining pointwise step

For an arbitrary remaining $q$ there is still no proof that $r-1$ reaches the good interval, reaches a smaller multiple of three, or meets the known good component of some $2^{a-j}b-1$ with $2\le j\le a$ and $2^{a-j}b>1$. Dividing $r-1$ by its actual power of two gives the ordinary odd endpoint $U=(3^a b-1)/2^{v_2(3^a b-1)}$. The sufficient inequality $8U+1<9q$ need not hold, and virtual agreement before this first even input does not control the subsequent physical orbit.

At PR201 `73a145ca99448a78219bd149e273f33b6e3fda4b`, the pointwise two-ended count retains a central clock on the unprescribed middle word. PR197 `b0538639df0ab7edd239281bd897e705160f732c` permits individual height increases in its unit-exit comparisons. Neither gives a relative height saving on every remaining source.

At PR201 `2978d84f8a1fda9083593b26c6bf724d5976d859`, `escape-analysis/README.md` proves that a counterexample would force exponentially many sources at one actual terminal per large central row. The least-odd-defect hypothesis gives an explicit **lower** size bound for every such source in its bad component. If $x$ reaches a bad odd terminal $w$ in $k$ odd steps with $2k$ total halvings, telescope the ordinary multipliers to get

$$
x=w(4/3)^k\,\bigg/\prod_{y}(1+1/(3y)) \;\ge\; w(5/4)^k.
$$

The product runs over the $k$ odd inputs, counted with multiplicity. Every one is at least 5 since 1 and 3 converge. Since $w>q$ by the minimum theorem and $(5/4)^5>3$, every such source with $k\ge5$ exceeds $3q$. This holds also for repeated states and arbitrarily high relative carry. The central multiplicity therefore yields no smaller multiple of three on the original bad component. The upper estimate for the maximum at the end of the referenced PR201 packet remains open.

[Finite replay](check.py) checks actual integer paths in both first-exit families and both fixed dyadic families. [Verification record](../../../reports/astra-minimum-source-20261124/renewal/REVIEW.md).
