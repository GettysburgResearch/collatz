# Exactly which critical types split into contracting pieces?

Put $p=\log_3 2$. For $n\ge2$, take $u=\lfloor np\rfloor$ and $\delta_n=np-u=\{np\}$. A binary word with $n$ bits and $u$ odd departures has multiplier $3^u/2^n<1$. A factor of length $L$ and weight $v$ contracts if $pL-v>0$ and expands if $pL-v<0$. Since $p$ is irrational, every nonempty factor satisfies exactly one of these alternatives.

Call $n$ a lower record if $\delta_n<\{Lp\}$ for every $1\le L<n$. There are infinitely many lower records since the positive fractional parts $\{np\}$ approach zero along a subsequence and are pairwise distinct. This note gives elementary type and height comparisons. It makes no historical priority claim.

## A criterion independent of the word

For every cyclic binary word of length $n$ and weight $u$, the following conditions are equivalent.

1. Some rotation is a concatenation of two nonempty contracting words.
2. Some rotation is a concatenation of at least two nonempty contracting words.
3. The length $n$ is not a lower record.

Indeed (1) implies (2), and combining all parts after the first preserves contraction, so (2) implies (1). If a piece of length $1\le L<n$ and weight $v$ and its complement both contract, then
$$
                 0<\{Lp\}\le Lp-v<\delta_n.
$$
The last inequality follows by subtracting the positive complementary deficit. This precludes a lower record.

Conversely choose $L<n$ with $\{Lp\}<\delta_n$ and put $v=\lfloor Lp\rfloor$. The average of the counts in the $n$ cyclic windows of length $L$ is
$$
              Lu/n=v+\{Lp\}-L\delta_n/n\in(v-1,v+1).
$$
Adjacent windows change their integer count by at most one. Therefore some window has count exactly $v$; otherwise the minimum and maximum cannot straddle $v$, and the average lies outside the displayed open interval. This window and its complement have positive deficits $\{Lp\}$ and $\delta_n-\{Lp\}$ respectively. The equivalence holds for every ordering of the bits, including words presented with a repeated period.

At a record, $\gcd(n,u)=1$. A common divisor $d>1$ would give $L=n/d$ with $\{Lp\}=\delta_n/d<\delta_n$. Thus every word of a record type is primitive: repeating a shorter word would multiply both counts by its repetition number. Each such word has a positive rational periodic realization via the affine anchor formula, since $u>0$ and $2^n>3^u$. This supplies realizations of every record type with no assertion that their reduced denominators equal one. [Affine anchor formula and splice assumptions](../phase9/ROTATION_SPLICES.md)

## Complete height order at a lower record

Write $y_j>0$ for the actual periodic values in chronological order, with indices taken modulo $n$. Let $U_j$ count the odd bits before index $j$ on the periodic lift, and put $H_j=nU_j-uj$, so $H_{j+n}=H_j$.

At a lower record and for every cut $i$, proper length $1\le L<n$ and intervening weight $v$, one has
$$
 \operatorname{sign}(y_{i+L}-y_i)
   =\operatorname{sign}(3^v-2^L)
   =\operatorname{sign}(nv-uL)
   =\operatorname{sign}(H_{i+L}-H_i).                                \tag{1}
$$

If the chosen factor expands, its multiplier exceeds one and its affine intercept is nonnegative, so it increases every positive input. If it contracts, its complement must expand by the type criterion; the complement carries $y_{i+L}$ back to $y_i$, making $y_i>y_{i+L}$. Finally $\{Lp\}>\delta_n>L\delta_n/n$, so $uL/n=Lp-L\delta_n/n$ and $Lp$ have the same integer part and both lie strictly between consecutive integers. Comparison of $v$ against either threshold gives the same strict sign. The final equality follows from the definition of $H$.

In particular the real phases have precisely the order of the centered integer heights $H_j$. Their unique minimum is at the minimizing index for $H_j$; the integers $H_j$ are distinct modulo $n$ because $\gcd(n,u)=1$. Starting at that minimum, **every proper prefix has multiplier strictly greater than one**. The first coefficient contraction occurs at the full lap, when the physical input returns exactly to its initial value.

## Two short examples and the remaining issue

At $n=4$, $u=2$ and $\{2p\}<\{4p\}$. Every circular word of this type has a length-two window with one odd bit and a complement with one odd bit. Both contract.

At $n=5$, $u=3$ and $\{5p\}$ is a lower record. The word $11100$ realizes the successive positive rational states
$$
                           (19,31,49,76,38)/5.
$$
Its centered integer heights are $0,2,4,6,3$, in exactly the real phase order in (1). From $19/5$, the first four prefix multipliers exceed one and the full multiplier is $27/32$. The positive ordinary period-two word $10$ is another lower-record example.

The density-one denominator theorem allows exceptional approximating period types, and the same-side splice inequalities require at least two contracting pieces in the positive case. Lower records are an explicit infinite family on which that partition is impossible for every bit arrangement. For a hypothetical nontrivial ordinary cycle at one of these records, physical strict descent at the first coefficient contraction from its minimum would rule it out. The rational example shows why the order comparison alone supplies no such descent. Finite or band-specific first-exit statements have their own horizon and domain hypotheses. [Density-one census](../phase8/ASCENT_CENSUS.md), [same-side splices](../phase9/ROTATION_SPLICES.md), [first-exit analysis](../FIRST_EXIT.md), [Weaver Paper 223, v1](https://rstation.ai/problems/collatz/papers/223/v1)
