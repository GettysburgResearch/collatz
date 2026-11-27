# Ordered odd cycles and their denominators

**OPEN.** The bounded-cycle alternative in PR 205 allows an ordinary cycle whose minimum is $s=(3q-1)/2$, whose odd valuations are 1 or 2, and whose odd values lie in $[s,8s)$. This section gives a written order reduction and a Lean-checked rational example. Ordinary cycle exclusion remains open. [Source hypothesis at the frozen head](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md)

## Order and the weighted congruence

Write each of the $p$ odd values as $x_i=2^{j_i}t_i$ with $s\le t_i<2s$ and $j_i\in\{0,1,2\}$. The $t_i$ are distinct since two positive odd integers cannot differ by a nontrivial factor of two. Each is on the quarter-integer grid. Before renormalization, the odd step sends $t_i$ to $3t_i+2^{-j_i}$. Distinct increasing mantissas differ by at least $1/4$, while their corrections differ by at most $3/4$. Thus their raw images are nondecreasing. Equality would produce the same next mantissa and contradict injectivity on the cycle. At the seam the last raw image is strictly below twice the first one, since the last mantissa is at most $2s-1/4$ and the first is $s$ with correction 1. The lift therefore preserves cyclic order.

Consequently the sorted ranks advance by a fixed shift. Extend the sorted list by doubling after every $p$ ranks. The raw image ranks form $p$ consecutive lifted ranks, since the reduced ranks form an order-preserving permutation. Their common lifted displacement is $h=\sum_i a_i$, where $a_i$ are the odd valuations. Indeed, writing the normalized carries as $k_i=a_i+j_{i+1}-j_i$, their sum around the cycle is $h$. For each sorted rank $r$, the exact carry is therefore $\lfloor(r+h)/p\rfloor$. Primitivity gives $\gcd(h,p)=1$.

Set $z_r=4t_r$ and $c_r=2^{2-j_r}\in\{1,2,4\}$, indexed by sorted rank. Then, with $r'=(r+h)\bmod p$,
$$
 2^{\lfloor(r+h)/p\rfloor}z_{r'}=3z_r+c_r.
$$
Let $D=2^h-3^p>0$. For $D>1$ choose integers $m,n$ with $mp+nh=1$ and put $u=2^m3^n\pmod D$. Both bases are units, $u^p=2$, and $u^h=3$. Multiplication by $u^{-(r+h)}$ turns the recurrence into a telescoping difference of $z_{r'}u^{-r'}$ and $z_ru^{-r}$, giving
$$
       \sum_{r=0}^{p-1}c_r u^{p-1-r}=0\pmod D .
$$
For a constant coefficient $c$, multiplying this congruence by $u-1$ gives $c(u^p-1)=c=0\pmod D$, impossible because $c$ is a unit. This recovers the balanced case. Kevin Knight proves the high-cycle exclusion in the original physical parity word. [Published paper](https://www.sciencedirect.com/science/article/pii/S0012365X25004200)

## A rational control with a proper common divisor

Take the 41 odd valuations
$$
     12112212212212121212212121221221212121222 .
$$
Their sum is $h=65$. In chronological order let $A_i=\sum_{j<i}a_j$ and $C=\sum_{i=0}^{40}3^{40-i}2^{A_i}$. The exact values are
$$
 D=420491770248316829,\quad C=326313631156465704911,\quad \gcd(C,D)=19 .
$$
The rational cycle has minimum
$$
 s=\frac{17174401639813984469}{22131145802542991}.
$$
Every odd value lies in $[s,8s/3)$. Its normalized ranks advance by 65 modulo 41. Its reduced denominator is coprime to 18 and the numerator and denominator are equal modulo 18. Thus $s\equiv1\pmod{18}$ and $q=(2s+1)/3\equiv1\pmod{12}$ in the rational localization. The minimum has reduced denominator greater than 1, so the word supplies no ordinary cycle.

[DecorationControl.lean](DecorationControl.lean) checks the numerator, denominator, common divisor, failure of complete divisibility, and every exact positive rational transition in common-denominator coordinates. It checks return, the minimum, the height range, and the normalized rank advance at each point. All four declarations passed Lean 4.34.1 using kernel reduction. The axiom audit lists only `propext` where used. From the repository root run `lean research/astra-universal-closure-20261124/cycle/DecorationControl.lean`.

The example refutes extending the balanced numerator coprimality claim to all bounded dyadic coefficients. Its congruences and ordered rational orbit supply no ordinary least-basin hypothesis. The remaining obligation is to show that the *whole* $D$ cannot divide the numerator of any nontrivial ordinary candidate compatible with that hypothesis.

## The lower basin cutoff at every inverse depth on a rational lattice

The fixed lattice $\{m/13:m\in\mathbb N_{>0}\}$ supports the same rational shortcut formulas. In numerator coordinates its map is $S(m)=m/2$ at even $m$ and $S(m)=(3m+13)/2$ at odd $m$. Color a numerator bad exactly when its orbit enters the following cycle, read in shortcut clocks:

$$
  283,\ 431,\ 653,\ 986,\ 493,\ 746,\ 373,\ 566,\ 283.
$$

The least bad numerator is 283. The least bad numerator divisible by three is 579. The least positive numerator whose color changes under tripling is 193. Indeed, $S^9(579)=283$ and every positive $m<283$, as well as every positive multiple of three $m<579$, lies in a disjoint forward basin. There is consequently no path of any length consisting of legal undirected lattice edges from the distinguished cycle to a lower numerator of either kind.

For the finite certificate take the union $E$ of the eight cycles with minimum numerators $1,13,131,211,227,251,259,287$. The check uses the explicit list of 70 members, verifies forward closure, verifies $S^{70}(283)\notin E$, and verifies $S^{70}(m)\in E$ for each required $m$. If such an $m$ reached 283 at any clock $k$, then $S^{70+k}(m)$ would both belong to $E$ by closure and equal $S^{70}(283)$. This proves the exclusion for all clocks, including arbitrarily long inverse searches. Basin color is constant on each undirected edge since 283 is periodic.

In original units the minimum is $s=283/13$ and $q=193/13=(2s+1)/3\equiv1\bmod12$. The largest odd value is $653/13<8s/3$ and every odd valuation is 1 or 2. Here ordinary 1 has numerator 13 and is good. The good set includes several basins, while ordinary Collatz uses the specific basin of 1. The model also uses the lattice denominator 13. Both distinctions matter when applying a proposed proof to ordinary inputs. In particular, the exact least-source color conditions and the closed cycle can coexist without forcing a smaller bad multiple by any composition of the legal lattice edges. [Lean proof](RationalBasin.lean)

The file imports only Lean's standard library. Running Lean 4.34.1 on it checks the quantified all-clock exclusion and both least elements. The axiom audit lists only the three standard axioms.

## Why repeating the original inverse cycle cannot lower a source

For an odd inverse step write $I_a(x)=(2^a x-1)/3$. At the first divergence from a cycle using only $a\in\{1,2\}$, the alternative exponent is $a+2k$ for some $k\ge1$. Its output, relative to the observed output $X$, is $4^kX+(4^k-1)/3$. At subsequent steps write the alternative value as $Y=2^\delta X+c$, where $\delta$ is its excess total exponent. For observed exponent $a$ and alternative exponent $b$ one obtains

$$
 \delta'=\delta+b-a,\qquad
 c'=(2^{\delta'}+2^b c-1)/3 .
$$

While $\delta'\ge0$ this preserves $c\ge0$. Consequently every lift that keeps $\delta\ge1$ after first divergence stays at least $2s+1$ at its odd lattice sites in the ordinary integer case. At a first return to excess zero one must have $\delta=1$, $a=2$, $b=1$. Integrality requires $3\mid c$, and $c$ is a positive odd integer because $Y=2X+c$ is odd. Traversing the unaltered inverse word for a full lap has slope $2^h/3^p>1$. The original word does not create the required return to zero. The rational example above additionally shows that changing the inverse exponents arbitrarily need never produce a qualifying smaller lattice source. An argument using the full integer cycle equation or the ordinary basin of 1 is still needed.

The positive real weight of the ordered recurrence also has an exact sign. Put $t=2^{1/p}$ and $w_r=t^{-r}$. Since $2^{k_r}w_r=t^h w_{r'}$, summing the weighted recurrence over all ranks gives
$$
 \sum_r w_r c_r=(2^{h/p}-3)\sum_r w_r z_r .
$$
Both sides are positive for every positive fixed point with $D>0$, including the rational controls. Thus the canonical positive weighting recovers $2^h>3^p$ and leaves the full ordinary congruence unresolved.

## Ternary order at physical clocks

The exceptional cycle also has a ternary normalization. Every physical value is below $9s$ for $s>4$, since an even value is twice a run entry bounded by $4s+2$. Write $x=3^jt$ with $s\le t<3s$ and $j\in\{0,1\}$. No positive cycle vertex is divisible by 3, so all $h$ mantissas are distinct. Before normalization the shortcut step acts by $(t+\varepsilon/3^{j+1})/2$, with $\varepsilon$ its odd indicator. The grid spacing is at least $1/3$, as large as the greatest correction. Raw images preserve order, including at the seam since the minimum is odd. The sum of ternary carries equals $p$, giving the rank shift $r'=(r-p)\bmod h$ and carry $k_r=\mathbf1_{r<p}$.

Put $Z_r=3^{1-j}(2x+1)$ and $c_r=3^{1-j}\in\{1,3\}$. The identity $2(2Tx+1)=3^\varepsilon(2x+1)+1$ gives $2Z_{r'}=3^{k_r}Z_r+c_{r'}$. For the same modular unit $u$ as above, telescoping gives $\sum_{r=0}^{h-1}c_r u^{h-1-r}=0\bmod D$. This is the original cycle congruence in physical-rank coordinates. On the eight-clock rational example the ternary ranks are $0,3,6,1,4,7,2,5$. Both orders and the lower basin cutoffs hold there. Full divisibility for ordinary cycles remains open.

[Independent exact replay](check_cycle.py) reconstructs the two rational cycles, both rank checks on the eight-clock cycle, the 41-odd-step common divisor and the complete 70-clock basin certificate. From the repository root run the script with Python normally and with `-O`.
