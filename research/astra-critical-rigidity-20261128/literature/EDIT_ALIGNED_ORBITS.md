# Exact heights of separated Collatz paths under insertions, deletions and substitutions

**Proposed written theorem.** Use either of two native descriptions of the shortcut Collatz map. A shortcut letter $b\in\{0,1\}$ sends the numerator $y$ over a common odd denominator $q$ to $(3^b y+bq)/2$. An odd-map letter $e\ge1$ sends an odd numerator to $(3y+q)/2^e$ at its genuine next odd date. Assume $q>0$ is prime to six. The two supplied finite words use the same description. Allow either two positive paths or two negative paths, with the indicated sign holding throughout. A letter's **grade** is $b$ in the first description and one in the second.

Align the two words by a sequence of columns. A column consumes one letter from each track, or one from one track while the other waits. The cost is one for an insertion, deletion or unequal matched-position substitution, and zero for a pair of equal letters. At all column boundaries, including the first and last, require that the two actual numerators be distinct. Let $G$ be the sum over columns of the **larger** of the two grades, a waiting track contributing zero. For a fixed cost budget $s$ the two actual total grades each differ from $G$ by at most $s$. At every boundary put
$$
H=\log_2(\max_j |y_j|+q),\qquad h=\log_2(\min_j |y_j|+q).
$$
For every family of such paths of edit cost at most $s$ and $G\to\infty$,
$$
 \liminf\frac{H_{\rm start}+h_{\rm end}+(5s+4)\log_2 q}{G}\ge1.       \tag{1}
$$
This is uniform over alignments obeying separation. In particular for fixed $s$ and $\epsilon>0$ there is an ineffective finite constant $C(s,\epsilon)$ such that $(1-\epsilon)G$ is bounded by the numerator on the left plus $C(s,\epsilon)$ at every length. A single edit can carry an arbitrarily large odd valuation.

The [ordinary exact-endpoint theorem](../ordinary/EXACT_ARC_ENDPOINTS.md) gave (1) at synchronized odd clocks with substitutions alone and the better $4(s+1)$ denominator coefficient there. The [two-basis denominator proof](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md) supplies the fixed-form Subspace Theorem argument. Here a waiting side has no carry, the two accumulated odd clocks can differ, and both signs and the raw shortcut clock are included. The open bound applies to arbitrary words without a complexity or rotation model.

## Physical coordinates with unequal clocks

Consider a subsequence violating (1) by a fixed positive fraction of $G$. Then $H_{\rm start}=O(G)$ and $\log q=O(G)$. At every active odd grade the shifted magnitude $|y|+q$ grows by a factor at most $3/2$. A waiting side stays fixed and an even shortcut cannot increase this magnitude. Both complete paths thus have logarithmic height $O(G)$. Write $\gamma=\log_23$ and $\beta=\gamma-1$.

Isolate each of the at most $s$ exceptional columns as a singleton and partition the remaining path into at most $s+1$ equal-word runs. In an equal run of total dyadic exponent $B$ the difference of the two physical states satisfies
$$
                 2^B d_{\rm end}=3^g d_{\rm start},\qquad
                    d_{\rm start}d_{\rm end}\ne0.
$$
Hence $2^B\le|d_{\rm start}|\le\max |y_{\rm start,j}|$ for states of the same sign. A singleton dyadic exponent costs at most $O(G)$ by its actual branch equation, including for negative odd numerators. There are only finitely many pieces. All cumulative dyadic exponents are $O_s(G)$, including in the shortcut description when a run has many even letters.

Let $K$ be the field over $\mathbb Q$ of the dyadic powers of the cumulative inter-track division differences, evaluated on a stabilized subsequence. These differences change only at the exceptional columns. The [dyadic-field lemma](../cycles/SEPARATED_ROTATION_DENOMINATORS.md) applies with scale $G$: there are finitely many Laurent generators with heights $2^{O(G)}$, every nonzero fixed field element has $v_3=o(G)$, and distinct Laurent monomials are rationally independent on every further infinite restriction. Stabilize $K$-relations for any subsequent fixed finite list of actual states and carries as in the cited proof. On the shortcut clock the dyadic differences are bounded by $s$, so after stabilization $K=\mathbb Q$.

Within each equal run whose grade divided by $G$ has a positive limit, insert an independent boundary pair within the first $\delta$ fraction of its grade for any previously fixed $0<\delta<1/2$. To see this, choose the two boundaries immediately after the $\lfloor\delta g/2\rfloor$-th and $\lfloor\delta g\rfloor$-th odd departures. All numerators at these boundaries are ternary units, since an incoming odd step has numerator congruent to $q$ times a dyadic unit modulo three. Subsequent even shortcuts preserve this property. If both pairs had rank one over $K$, their nonzero differences would each have $v_3=o(G)$, by writing $d=y_0(y_1/y_0-1)$. The matching recurrence between the dates increases that valuation by a positive multiple of $G$, a contradiction. Thus one of the two is independent. Runs of grade $o(G)$ need no new cut. There are now at most $2(s+1)$ equal subblocks and $s$ exceptional singletons, including possible subblocks of zero grade.

At the resulting boundaries let $D_{i,j},g_{i,j}$ denote each track's true cumulative dyadic exponent and grade, beginning at zero. Let $t_i$ denote the cumulative common clock (sum of columnwise maximum grades), so $t_0=0$, $t_k=G$. It may have repeated weights. The nonnegative losses $t_i-g_{i,j}$ are at most $s$ and become fixed integers on the chosen subsequence. In an equal subblock $i$ of grade $g>0$ its common carry is
$$
 C_i=\sum_{h\text{ an odd departure}}3^{g-1-g_h}2^{F_h},
$$
where $F_h,g_h$ are the prior local divisions and grade. This integer is prime to three because its last odd summand is a dyadic power. It can be even on the shortcut clock. A grade-zero equal subblock contributes no carry. At a singleton with at least one odd departure use $C_i=1$; its carry is present on each side that actually departs on an odd branch, and absent on the other. A singleton with no odd departure also contributes no coordinate.

For each present carry set
$$
 Z_i=q C_i 2^{D_{i-1,0}}3^{-t_i}.
$$
The normalized physical partial states $R_{i,j}=2^{D_{i,j}}3^{-g_{i,j}}y_{i,j}$ satisfy
$$
 R_{i,j}=Y_j+\sum_{h\le i}c_{h,j}Z_h
        =W_j-\sum_{h>i}c_{h,j}Z_h ,
 \quad Y_j=y_{{\rm start},j},\quad
 W_j=2^{D_{k,j}}3^{-g_{k,j}}y_{{\rm end},j}.                         \tag{2}
$$
In a present position the coefficient is $2^{D_{h-1,j}-D_{h-1,0}}3^{t_h-g_{h,j}}\in K$ when that side contributes, and is zero otherwise. This handles a simultaneous unequal substitution, both kinds of one-sided step, and each strict equal-word run. Ratios of the two normalization factors at every boundary lie in $K$. The local absolute values are
$$
 v_3(Z_i)=-t_i,\qquad |Z_i|_\infty|Z_i|_2
       = (qC_i)2^{-v_2(C_i)}3^{-t_i}\le qC_i3^{-t_i}.
$$
Initial roots have ternary norm at most one. Each terminal root costs at most $\log_2|y_{{\rm end},j}|-\gamma G+O(s)$ at infinity and two, even if its native numerator is even.

## Cost of the common carries

On a matching subblock use the starting state $M$ of greatest magnitude. It continues to be the state of greatest magnitude throughout the subblock, since all applied affine maps are strictly increasing and the two states retain the same sign. Every original dyadic exponent used in the sum for $C_i$ has $2^{F_h}\le|M|$. On positive paths,
$$
 2^{F_h}(|y_h|+q)3^{-g_h}
  = |M|+q\left(\sum_{u<h\text{ odd}} 2^{F_u}3^{-g_u-1}
                       +2^{F_h}3^{-g_h}\right)\le |M|(1+q).
$$
The geometric coefficients in parentheses have sum $(1+3^{-g_h})/2\le1$ before multiplication by their respective dyadic powers. For a negative pair the affine carry in the formula for $|y_h|$ has a minus sign and may be dropped, so the same upper bound follows. Consequently
$$
 F_h-\gamma g_h\le H_{\rm start}-H_h+\log_2(1+q).
$$
For every equal subblock of positive grade,
$$
 \log_2 C_i\le\gamma g+\log_2(g+1)
          +\max_{h\text{ odd}}(F_h-\gamma g_h).
$$
Its largest selected envelope drop is bounded by the downward variation on that block. All these portions are disjoint in the same envelope, which can rise by at most $\beta$ on each of the $G$ positive-grade columns and cannot rise on other columns. Its total downward variation is at most $\beta G+H_{\rm start}-H_{\rm end}$. Each equal subblock charges $\log_2 q+\log_2(1+q)\le2\log_2q+1$ and each exceptional singleton with a carry charges only $\log_2 q$. Thus
$$
 \sum_{i:Z_i\text{ present}}\log_2(qC_i)
 \le(\gamma+\beta)G+H_{\rm start}-H_{\rm end}
       +(5s+4)\log_2q+O_s(\log(G+1)).                                  \tag{3}
$$

## Exact endpoint ranks and the fixed forms

In (2), form the prefix span of both $Y_j$ and all present $Z_h$ through cut $i$, and the suffix span of both $W_j$ and all present $Z_h$ strictly after the cut. These sum to the full $K$-space and both contain the two partial states $R_{i,j}$. Let $a,b\in\{1,2\}$ be the initial and terminal root ranks. Greedily complete the initial basis by chronological carries at indices $I$ and the terminal basis by reverse chronological carries at indices $J$. The exact [endpoint-rank identity](../ordinary/EXACT_ARC_ENDPOINTS.md) applies to these nondecreasing weights, even across a carry-free column or repeated grade:
$$
 \sum_{i\in I} t_i-\sum_{i\in J}t_i=(b-2)G+
  \sum_{i<k}(t_{i+1}-t_i)[2-\dim(P_i\cap S_i)] .
$$
Every intersection has dimension at least one. In each macroscopic equal run the second subblock starts at an independent pair, and only the initial $\delta$-fraction can charge a positive loss. The remaining equal runs contribute $o(G)$ in total; the defect columns have total grade at most $s$. Therefore the last sum is at most $\delta G+o(G)$.

Use the terminal basis at infinity and two and the initial basis at three. Clear the fixed Laurent denominators in the latter change of basis at three with a single nonzero polynomial whose valuation is $o(G)$. The [finite translate construction](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md) gives fixed rational forms: use terminal basis times every monomial in the enlarged box for coordinates, the cleared initial basis times the core box for forms at three, and complete those at three with terminal coordinate forms. All coordinates have denominator supported at two and three, heights $2^{O(G)}$ for these fixed choices, and no rational relation recurs on a further subsequence. Boundary monomials have $|T|_\infty|T|_2=|T|_3=1$. For every fixed cut system the translate boundary fraction can therefore be made arbitrarily small, with absolute cost $O(G)$ per excess row. On the binary shortcut clock both bases are over $\mathbb Q$ and a singleton monomial box suffices.

The terminal roots cost $-b\gamma G$ plus at most $\log_2|y_{{\rm end},0}y_{{\rm end},1}|+O_s(1)$. The signed carry weights restore $\gamma(b-2)G$, irrespective of the initial rank. By (3) the log product per core monomial is consequently at most
$$
 -G+H_{\rm start}+h_{\rm end}+(5s+4)\log_2q+
       \gamma\delta G+o_{\rm box}(1)O(G)+o(G).
$$
Choose $\delta$ for the strict deficit, stabilize at these cuts, and then fix the box size. A macroscopic equal run supplied an independent internal pair, so the resulting dimension is at least two. The rational $S$-adic Subspace Theorem at $S=\{\infty,2,3\}$ contradicts the strict exponentially small product: clearing only dyadic and ternary denominators preserves it, and dividing by an integral gcd can only decrease it. This proves (1). [Schlickewei, original Subspace Theorem](https://doi.org/10.1016/0022-314X(77)90073-7)

## Near returns on one actual rational trajectory

A nonperiodic signed rational trajectory has distinct states, hence their magnitudes tend to infinity since the reduced denominators divide the fixed initial odd denominator. After finitely many odd steps its denominator is prime to six. Those steps occur infinitely often, since arbitrarily long all-even tails of a nonzero rational cannot occur forever. A positive state stays positive; if no positive state ever occurs the remaining states are negative. Thus after a fixed initial shift either sign hypothesis holds. One can apply the conclusions below to that tail, or discard a fixed number of letters from the two compared windows. Such trimming changes the edit budget and endpoint indices by at most a fixed amount. For alignment separation on a fixed orbit it is simplest to start directly on this tail, as the conclusions do.

Consider an equal-length prefix and its own lag-$\ell$ word of length $P$. A path through an edit alignment can pair the same physical state only by gaining an index offset of $\ell$; since the offsets at the two ends agree, this costs at least $2\ell$ insertions and deletions. Therefore every cost-$s$ alignment is separated if $2\ell>s$. The corresponding cyclic sufficient condition is $2\min(\ell,p-\ell)>s$ for a length-$p$ cycle. Omitting separation admits the tautological alignment of cost $2\ell$ obtained by trimming the two ends.

On odd dates put $\Lambda_{\rm odd}=\limsup\log_2(|x_j|+1)/j\le\beta$. For $P\to\infty$, bounded edit cost, separated states and $\ell/P\to A<\infty$, equation (1) gives
$$
                1\le(1+A)\Lambda_{\rm odd}.                            \tag{4}
$$
In particular a zero-growth odd orbit has $\ell/P\to\infty$ along any sequence of nontrivial bounded-edit returns. This extends the [substitution-only bound](../ordinary/EXACT_ARC_ENDPOINTS.md) across insertions and deletions.

For the binary shortcut clock put $g(t)=\sum_{j<t}(y_j\bmod2)$ and $L(t)=\log_2(|x_t|+1)$. The actual logarithmic recurrence gives
$$
 L(t)=\gamma g(t)-t+o(t).
$$
The one-step odd correction $\log_2|1+1/(3x_t)|$ tends to zero on either sign, while the even step has no correction in $\log_2|x_t|$. Let $\Lambda_{\rm raw}=\limsup L(t)/t\le\beta$. A bounded-edit return contributes $G=g(P)+O_s(1)$; moreover $g(P)\ge(P-o(P))/\gamma$ so $G\to\infty$. Since $H_{\rm start}\le L(\ell)+O(1)$ and $h_{\rm end}\le L(P)+O(1)$ on the fixed orbit, (1) gives
$$
   P\le \gamma L(\ell)+\beta L(P)+o(P+\ell),\qquad
   \boxed{\displaystyle 1\le(\gamma A+\beta)\Lambda_{\rm raw}.}       \tag{5}
$$
Both (4) and (5) force $A\ge(2-\gamma)/(\gamma-1)>0.709$ in their respective clocks. These conclusions constrain arbitrary high-complexity words on actual rational trajectories. In particular, an arbitrarily long prefix cube with only bounded edits between its length-$2P$ overlaps is excluded on either clock. The result assumes no fixed dictionary.

## Full denominator for edit-aligned odd rotations

For a positive primitive rational cycle with $p$ odd steps suppose the native valuation word and its rotation by $\ell$ admit a circularly closed alignment with at most fixed $s$ edits and distinct physical phases at every column boundary. A usual equal-length alignment is circularly closed by identifying its endpoints. The preceding condition $2\min(\ell,p-\ell)>s$ suffices. Interchange the tracks if needed so the forward separation at the original cut is $\ell\le p/2$. Rotate the **alignment columns** to the phase where track zero is at the minimum $M$. Its partner then lies at forward separation at most $p/2+s$, unless the original lag is at most $s$ and the signed offset crosses the index seam. The latter cannot occur in a separated alignment: the index difference moves by units and starts and ends at $\ell>0$, so it cannot reach zero or $p$. Thus $H_{\rm start}\le\log_2q+\beta(p/2+s)+O(\log(p+1))$ and $h_{\rm end}=\log_2(qM+q)\le\log_2q+O(\log(p+1))$, by the [cycle minimum bound](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md). Here $G=p+O_s(1)$ and the final physical pair equals the initial one. Equation (1) yields the explicit lower rate with ineffective onset
$$
   \liminf\frac{\log_2q}{p}\ge\frac{1-\beta/2}{5s+6}.
$$
For substitutions alone the denominator coefficient in [the clustered theorem, (11)](../cycles/ALL_FIXED_ROTATION_DENOMINATORS.md) is better.

## Prior factor-complexity result and scope

Weaver's [Paper 173/v1, §§1 and 9, 19 November 2026](https://rstation.ai/problems/collatz/papers/173/v1) proves $P(k)/k\to\infty$ for every nonperiodic signed rational shortcut orbit. In particular it already excludes exact codings by any fixed finite union of intervals of an irrational circle rotation, whose length-$k$ factor count is $O(k)$. It also excludes uniformly bounded edit approximation along arbitrarily long prefixes by **any family** with a common linear bound on factor counts: a single edit can introduce only $O(k)$ newly crossing length-$k$ factors. These qualitative exclusions should be credited to that prior result. Present inequalities (1), (4) and (5) use the two actual window heights and permit completely unrestricted factor languages. The [ordinary lane's weighted Hamming return theorem](../ordinary/FIXED_SOURCE_MISMATCH_WEIGHT.md) treats the odd clock; its finite rotation grid gives explicit scales for the named models. No mandatory bounded-edit return has been shown for every hypothetical exceptional orbit.
