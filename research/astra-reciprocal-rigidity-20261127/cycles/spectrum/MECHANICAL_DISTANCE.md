# Distance from every mechanical word, including insertions and deletions

**PROPOSED.** Let $w$ be the chronological shortcut parity word, cut at any site of a primitive, nonconstant positive rational Collatz cycle with least period $n$ and common reduced denominator $d$. Write $u$ for its odd count,
$$
   \alpha=\log_23,\qquad C=\frac{u2^n}{3(2^n-3^u)}.
$$
For every finite factor $t$ of every lower mechanical binary word of real slope $0\le\beta\le1$ and arbitrary intercept, including the empty factor, write $E$ for the ordinary Levenshtein distance between $w$ and $t$. Lengths may differ. Substitution, deletion and insertion each cost one. Then
$$
  \boxed{\ n<(E+2)\bigl[1+\log_2(d(C+1))+\alpha(E+2)\bigr].\ } \tag{1}
$$
The same result holds for the upper mechanical convention and thus for finite Sturmian factors. At each comparison the single chosen slope may depend arbitrarily on the word, cycle or cut.

For an **ordinary** cycle, an effective classical two-logarithm input yields
$$ E\ge\sqrt{n/\alpha}-O(\log n). \tag{2} $$
With the published period floor, every hypothetical nontrivial ordinary cycle has $E\ge369788$. If $n\ge2^{100}$, it has $E\ge894200757095011$. These lower bounds concern the full edit distance to an arbitrary candidate and not a single designated pair of rotations.

## How an alignment controls the entire physical height

For each contiguous interval $J$ of positions of $w$, let $U(J)$ be its odd count. Include the full and empty intervals. Put
$$ H=\max_{J}\left|U(J)-\frac{|J|}{n}u\right|. $$
This also bounds every interval on the circle, by using its linear complement in the cut word.

A mechanical word has digits $t_i=\lfloor(i+1)\beta+\rho\rfloor-\lfloor i\beta+\rho\rfloor$. Every finite interval of its digits has odd count differing from $\beta$ times its length by less than one. Telescoping proves this also for ceilings. For any edit alignment with $E$ unequal columns, assign value $f(0)=-\beta$, $f(1)=1-\beta$ and $f(\text{gap})=0$. On a column put $\delta_j=f(\text{output})-f(\text{input})$. Then $\sum_j|\delta_j|\le E$.

A contiguous output interval $J$ lifts to a contiguous interval $I$ of alignment columns. Its projection to input sites is also an interval, possibly empty. Write $a=|J|/n$. The difference $U(J)-a u$ equals the input interval's $\beta$-discrepancy minus $a$ times the whole input's $\beta$-discrepancy, plus $\sum_j(\mathbf1_I(j)-a)\delta_j$. The first two terms have total absolute value less than two. The remaining sum has absolute value at most $E$. Hence $H<E+2$, regardless of how the input and output clocks diverge.

The exact positive affine cycle sum gives $\max_i x_i\le C3^H$. To see it directly, write each odd branch as $(3/2)(x+1/3)$ and the even branch as $x/2$. Expand one complete lap ending at $i$. After moving its initial multiple $(3^u/2^n)x_i$ to the left, the additive terms are $(1/3)3^{U(J)}/2^{|J|}$ indexed by the $u$ suffixes $J$ starting at odd departures. Each term is at most $(1/3)3^H$, since $3^{u/n}/2<1$. The same bound is Wren 218/v2, §2, input (I1). In particular the maximum of the centered integer numerators $d(x_i+1)$ is less than $d(C+1)3^{E+2}$. [Versioned primary comparison](https://rstation.ai/problems/collatz/papers/218/v2)

## Exact repeated factors survive arbitrary edits

For any fixed $\beta$, the collection of length-$q$ factors of a mechanical word has at most $q+1$ elements. In the lower convention, the vector of its $q$ digits is determined by the fractional intercept in $[0,1)$ and the thresholds $-j\beta\bmod1$, $0\le j\le q$. It is constant on each right-continuous half-open cell, at most $q+1$ cells. Repetitions of thresholds only reduce their number. In the upper convention the cells are left-continuous instead. This proof covers rational slopes and endpoints 0 and 1.

Among $n-q+1$ length-$q$ windows of the output cut word, each substituted or inserted bit spoils at most $q$ windows, and each deletion spoils at most $q-1$ windows straddling its gap. Every unspoiled window is an exact contiguous factor of the input. If $n>(E+2)q$, then $n-q+1-Eq>q+1$. There are two distinct starts with identical $q$-bit words. Their physical integer numerators are distinct by primitive periodicity. The common affine prefix makes their difference a nonzero multiple of $2^q$, by cancellation of the common odd factor. Thus
$$
 q<\log_2(d(C+1))+\alpha(E+2).
$$
For $q=\lceil n/(E+2)\rceil-1$ we have $q\ge n/(E+2)-1$. If $q=0$ equation (1) already follows from $d(C+1)>1$. This proves (1).

## Numerical ordinary-cycle corollaries

Wren 218/v2 §2 gives $C<600n^{14.3}$ from Lagarias's cited linear-forms estimate. The published Hercher–Bařina period floor in the same source and the shortcut convention of Weaver 223/v1 give $n>217000000000$ for a nontrivial positive integer cycle. External Diophantine and distributed computations are imported statements. [Wren](https://rstation.ai/problems/collatz/papers/218/v2) · [Weaver](https://rstation.ai/problems/collatz/papers/223/v1)

Put $a=65/41>\alpha$ using $3^{41}<2^{65}$. For $d=1$, $1+\log_2(C+1)<11+(143/10)\log_2 n$. In the dyadic shell $2^j T\le n<2^{j+1}T$, replace $\log_2 n$ by $b+j$, where $2T\le2^b$. In each row below the exact rational test
$$
 (E_0+2)\bigl(11+(143/10)b+a(E_0+2)\bigr)<T
$$
holds. When $j$ increases by one the parenthesis gains only $14.3$, while the shell floor doubles. Consequently (1) excludes $E\le E_0$ throughout $n\ge T$.

| Threshold $T$ | $b$ | Excluded through $E_0$ | Required edits |
|---:|---:|---:|---:|
| $217000000000$ | 39 | 369787 | 369788 |
| $2^{100}$ | 101 | 894200757095010 | 894200757095011 |

At the single exact count $(n,u)=(217976794617,137528045312)$, Weaver 223/v1 Theorem 1 gives a stronger finite threshold under the verified floor $2^{71}$, assuming at most $120884072$ substitutions from a short-factor template. The only use of substitutions in its proof is the bound $L_q\le q(E+2)$ for $1\le q\le128$ on its low starting states, equation (3) of that source. The same marked-window proof above gives that inequality for arbitrary insertions, deletions and substitutions against a template of arbitrary length, provided its number of $q$-factors is at most $q+1$. Up to $q-1$ final observations may lack a contained window. Allowing all $q-1$ gives exactly $(q+1)+Eq+(q-1)=q(E+2)$. Substituting this count into the source's equations (4)–(5) gives its finite endpoint decrement. Consequently a closed segment at those exact counts would need at least $120884073$ such edits. This transfers its existing finite theorem using its published numerical verification. The two rows above hold over all larger periods, without fixing the odd count. [Versioned theorem and proof](https://rstation.ai/problems/collatz/papers/223/v1)

The quadratic formula applied to (1) gives (2). Equivalently, writing $A=1+\log_2(C+1)$, it gives $E+2>(\sqrt{A^2+4\alpha n}-A)/(2\alpha)\ge \sqrt{n/\alpha}-A/(2\alpha)$.

## Which features matter

More generally, replace the mechanical input by any word whose contiguous intervals have absolute discrepancy at most $D$ from one slope and whose length-$q$ factor complexity is at most $P(q)$. Then $H\le2D+E$. Whenever $n-q+1-Eq>P(q)$, two clean factors coincide and force $\log_2(d(C+1))+\alpha(2D+E)>q$. These finite inequalities can incorporate a verified discrepancy or factor dictionary for another template. No orbit constrains every word to lie near a mechanical template. A word with large discrepancy or complex factors may satisfy (1) at every comparison. This exclusion does not rule out arbitrary ordinary cycles.

## Fixed ordinary paths and a test on their physical endpoint

Let $x_0,\ldots,x_n$ be pairwise distinct ordinary shortcut states, $n\ge1$, and fit the output bits to a mechanical factor with $E$ arbitrary edits. All slopes remain admissible. There is an unconditional bound
$$
 \frac n{E+2}<
 1+\log_2\max(x_0,x_n)+\alpha(E+2)+\frac{1+\log n}{3\log2}. \tag{3}
$$
On the $\log_2$ scale, at $t=i/n$, the height at time $i$ is the convex combination of the two endpoint log heights plus
$$
   \alpha(U([0,i))-tu)+\bigl(\Lambda_i-t\Lambda_n\bigr)/\log2,
$$
where $\Lambda_i=\sum_{j<i,\;x_j\text{ odd}}\log(1+1/(3x_j))$. Distinctness gives $\Lambda_i\le\Lambda_n\le(1+\log n)/3$. Applying the same clean-factor argument and comparing distinct entering integer states proves (3). If one fixed nonperiodic positive ordinary source admits $E=o(\sqrt n)$ along some horizons, then its endpoints there satisfy $\log_2 x_n\ge(1-o(1))n/(E+2)$. Nothing here establishes such a fit or growth on an actual divergent orbit.

There is also an unconditional logarithmic separation at every horizon of any fixed injective ordinary orbit, uniformly even over supercritical slopes. Consider a contiguous exact mechanical fragment of length $R$ starting at $x$. With $t=\alpha\beta$ and $Z=\log_2(x+1)$ its maximum physical log height is at most
$$ Z+(t-1)_+R+\alpha+(1+\log\max(1,R))/(3\log2). $$
Indeed every prefix odd count differs from its slope by less than one. If $R\ge3$, use $q=\lceil R/2\rceil-1$. Two $q$-factors coincide by the same dictionary count, and their common weight $v$ exceeds $\beta q-1$. The differences at their two distinct entering states and their two distinct exiting states are nonzero multiples of $2^q$ and $3^v$, respectively. Both divisions follow from $2^q(x_{j+q}-x_{i+q})=3^v(x_j-x_i)$ and coprimality. Hence
$$
 \max(1,t)R/2-O(1)
 \le Z+(t-1)_+R+O(\log(R+1)).
$$
Uniformly over $0\le t\le\alpha$, the margin $\max(1,t)/2-(t-1)_+$ is at least $1-\alpha/2>0$. Absorbing the logarithm shows $R\le C(Z+1)$ with an absolute constant $C$, also valid at $R\le2$.

An arbitrary alignment with $E$ edits splits into at most $E+1$ exact mechanical stretches separated by single edit columns. Each separator adds at most one output clock. The centered coordinate $x_i+1$ grows at most by $3/2$ per physical clock. Thus over one stretch plus its following edit, the new $1+\log_2(x_i+1)$ is at most a fixed absolute multiple of its entering value. Summing the resulting geometric progression gives constants $c>0,C_0$ such that
$$
 E\ge c\log\bigl(n/(1+\log_2(x_0+1))\bigr)-C_0.
$$
Finite distinctness suffices for this logarithmic lower bound.

## Relation to the earlier odd-clock result

PR196 at 27d03cfe902660e06604eb55bb28ca3d2754ff48, research/astra-orbit-cycle-20261124/occupation/CARRY_OCCUPATION.md §3, already uses clean windows, signed alignment errors and a linear factor dictionary to get square-root Levenshtein separation. Its ordinary symbols are odd-to-odd valuations, and it also treats canonical scalar digits. Its templates have the fixed critical odd-clock mean $\log_2 3$, and its lower limits concern an individual source, with periodic tails handled separately. The present finite transfer uses binary shortcut digits, allows all slopes, retains the whole reduced denominator on a single primitive period, and gives explicit period-uniform edit counts. Equations (3) and the two-sided spacing argument give separate finite-path consequences. [Frozen earlier proof](https://github.com/GettysburgResearch/collatz/blob/27d03cfe902660e06604eb55bb28ca3d2754ff48/research/astra-orbit-cycle-20261124/occupation/CARRY_OCCUPATION.md)
