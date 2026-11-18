# Real scaling and support at rational poles of the ternary offset

**PROPOSED, source-qualified.** Let $(X,Y)$ be the common iid geometric affine-offset series in the real and ternary completions (stationary joint law of [paper 19](https://rstation.ai/problems/collatz/papers/19/v2)). Write $[r]_q=r+3^q\mathbb Z_3$, $g_q(r)=3^q\Pr(Y\in[r]_q)$ and $F_w(x)=\beta_w+J_wx$ for the real action of an inverse-prefix word. Conditional on $Y\in[r]_q$, the length-$q$ prefix weights are exactly $J_w/g_q(r)$ on its compatible words, and the real series from the remaining independent iid letters has the unconditional law of $X$.

## A negative cyclic root

Take a negative odd-rational phase $r$ on a cycle of period $d$ and multiplier $J>1$. The [rational trace theorem](RATIONAL_PHASE_TRACE.md) defines first-hit word sums $h^*_k$, bounded uniformly in $k$ at this root, and $C_l=\sum_{u\ge0}J^{-u}h^*_{l+ud}>0$. At depths $q=md+l$, $0\le l<d$, the law of
$$
 (X-r)/J^m\ \big|\ Y\in[r]_{md+l}
$$
converges **in total variation** to the following positive finite random variable. Choose $u\ge0$ and a first-hit inverse word $v$ of length $l+ud$ at $r$ with weight $J^{-u}J_v/C_l$, independently sample $X'$ with the unconditional real-offset law, and return
$$
 J^{-u}(F_v(X')-r).
$$
The convergence error in total variation is $O_r(J^{-m})$. Indeed every word decomposes uniquely into $m-u$ full reverse laps from $r$, followed by that first-hit word. The real lap map is $x\mapsto r+J(x-r)$. The finite conditional law is therefore precisely the stated mixture conditioned on $u\le m$, with the omitted probability bounded by a geometric sum. This identifies absolute real heights supporting the ternary pole.

Also, uniformly in $q$ and $T\ge0$,
$$
 3^q\Pr(Y\in[r]_q,\ X\le T)\ll_r 1+T.
$$
If $i$ full outer laps occur, then $X\ge |r|(J^i-1)$. Summing the unnormalized weights $J^i h^*_{q-id}$ only over $J^i\le1+T/|r|$ proves the bound. Conversely the supremum over $q$ is $\gg_r T$ for every sufficiently large $T$: choose $q=md$ with $J^m$ within a fixed factor of $T$ and small enough that the limiting scaled law has positive mass below the cutoff. The scaled law is supported in $(0,\infty)$ and is finite almost surely.

## All rational phases and the support of finite real codes

For any rational ternary unit $r$, the supremum over depths of the preceding bounded-real joint density stays comparable to one as $T\to\infty$ at a finite-trace root, and is comparable to $T$ at any pole. For the upper bound at an even numerator $r=2^k u$, $u$ odd and $k>0$, the words correspond to the subset at $u$ with outer exponent greater than $k$ and with both real offsets and weights multiplied by $2^k$. For an even denominator $r=2^{-k}u$ split the outer exponent at $k$ as in the rational trace theorem: the large-exponent group is the full law at $u$ rescaled by $2^{-k}$ in both coordinates of real value and mass, and each remaining single branch is an affine image of a smaller-denominator root. This finite recursion propagates $O_r(1+T)$. At a finite-trace root the stronger uniform bound $\sup_q g_q(r)<\infty$ holds, while any fixed positive-probability prefix gives a nonzero lower bound for large $T$. At any pole, fix one word from a negative cycle to $r$; restricting to this word embeds the cyclic-root lower bound at a fixed affine rescaling.

Let $S_r$ be the closure of the finite real offsets of **infinite** legal codes at $r$; an infinite code whose real series diverges contributes no point. Every rational unit has $\operatorname{Leb}(S_r)=0$ and $\dim_H(S_r)=1$, including the poles. At finite roots this is the [compact null support theorem](FINITE_TRACE_FIBRES.md). At a negative cyclic root, let $E_r$ be the offsets of codes that first depart from its reverse cycle within the first full lap, taking closure. This is a finite union of compact null sets. Indeed at each of at most $d$ possible departure positions the smaller-than-required exponents are a finite family of affine images of off-cycle finite-trace roots. The larger-than-required exponents as a group are an affine image of the finite-trace even numerator $2^{a_0}s$, where $s$ is the phase of departure and $a_0$ its required cycle exponent. The grouping is exact for real offsets as well as ternary legality. Finite-trace supports are the closures of all legal offsets. Consequently
$$
 S_r=\bigcup_{i\ge0}\bigl(r+J^i(E_r-r)\bigr).
$$
The omitted pure cyclic code has divergent real offset. This union is locally finite since every point of $E_r$ is nonnegative and $r<0$. In particular it is closed and null. For a general rational unit the same finite dyadic-denominator splitting bounds its closure by a finite union of affine images of such closed null sets and of finite-trace supports. Full Hausdorff dimension follows from the bounded legal Cantor family at every unit phase. Thus rational poles have unbounded ternary density and unbounded real heights in their contributing codes while their attainable finite real offsets still have null closure.
