# How sparse the set of actual odd periods must be

**PROPOSED.** Let \(\mathcal P\) be the set of distinct odd periods of all primitive positive ordinary Collatz cycles, counting a period once even if more than one cycle has it. No bound on valuations, height, or arithmetic rank is assumed. For every sufficiently large continued-fraction denominator \(q\) of \(\alpha=\log_2 3\),
\[
        \#(\mathcal P\cap[1,q])=O(q^{19/39}).
\]
At every integer cutoff \(T\to\infty\), the quoted bound \(\mu(\alpha)\le3\) gives the source-qualified improvement over a square-root count
\[
        \#(\mathcal P\cap[1,T])\le T^{38/77+o(1)}.
\]
Both estimates apply to the set of actually realized periods. They do not locate every admissible period or rule out a single nontrivial cycle.

## A budget shared across all cycles

Let \(S\) be the union of the odd phases of every positive ordinary cycle. The odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\) permutes each primitive cycle. Different cycles are disjoint, so every \(U^j\) is injective on \(S\) and \(U(S)=S\). The uniform invariant-set bound [T-A3-402](../../astra-three-routes/pass2/ORBIT_MELLIN.md) therefore gives
\[
      \#(S\cap[1,X])=O(X^\beta),\qquad \beta=19/20 .
\]
That source proves the estimate for arbitrary injective forward-invariant sets, a stronger input than just separate bounds on individual cycles. Counting each state once matters. Dyadic summation gives
\(\sum_{x\in S,\ x>Y}x^{-1}=O(Y^{\beta-1})\).

For a primitive cycle \(C\) with odd period \(P_C\) and total accelerated clock \(A_C\), its exact positive defect is
\[
  d_C=A_C-P_C\alpha=\sum_{x\in C}\log_2(1+1/(3x))>0 .
\]
All cycles with minimum exceeding \(Y\) consequently have combined defect \(O(Y^{\beta-1})\). There are at most \(O(Y^\beta)\) other cycles, by injection into their distinct minima. Hence for \(0<t<1\),
\[
     \#\{C:d_C>t\}=O(t^{-\beta}),                                          \tag{1}
\]
on taking \(Y=1/t\). This bound includes multiplicities across cycles. It implies, for every \(\gamma>\beta\), that \(\sum_C d_C^\gamma\) is finite. Indeed (1) counts the small-defect tail in dyadic intervals. Only finitely many larger defects occur and each is finite. The simpler unweighted sum \(\sum_C d_C\) is bounded directly by the total harmonic sum of \(S\).

## Rotation counts, including cutoffs between convergents

Let \(M(T,t)\) count the integers \(1\le p\le T\) for which some integer \(a\) lies in \((p\alpha,p\alpha+t]\). If \(a/q\) is a continued-fraction convergent, any \(q\) consecutive multiples of \(\alpha\bmod1\) consist of a translate of \(q\) points within circular distance \(1/q\) of a uniform \(q\)-point grid. This follows from \(|\alpha-a/q|<1/q^2\) and \((a,q)=1\). Thus at most \(qt+4\) hit any circle interval of length \(t\).

For successive convergent denominators \(q\le T<q'\), using complete \(q\)-blocks, and separately embedding the initial segment in one \(q'\)-block, gives
\[
 M(T,t)\ll \min(Tt+T/q,\ q't+1)
         \ll Tt+1+\min(T/q,\ q't).                                        \tag{2}
\]
At \(T=q\) use the stronger first estimate \(M(q,t)\ll qt+1\). Every realized period with a representative cycle of defect at most \(t\) belongs to this rotation set. Count the others using (1), obtaining
\[
             \#(\mathcal P\cap[1,T])\ll t^{-\beta}+M(T,t).                  \tag{3}
\]
Take \(t=q^{-1/(1+\beta)}\) at the convergent cutoffs to get exponent \(\beta/(1+\beta)=19/39\). Without any explicit irrationality estimate the period set has natural density zero: fix \(t\), apply uniform distribution of the irrational rotation and (3), then let \(t\downarrow0\). Equivalently this follows from the \(q\)-block upper bound followed by \(q\to\infty\).

For the all-cutoff numerical exponent only, quote \(\mu(\alpha)\le3\). Then \(q'\le q^{2+o(1)}\), by the convergent approximation inequality \(0<|\alpha-a/q|<1/(q q')\) and the definition of irrationality exponent. Since \(q\le T\), the elementary inequality \(\min(u,v)\le u^{2/3}v^{1/3}\) gives
\[
        \min(T/q,\ q't)\le T^{2/3+o(1)}t^{1/3}.
\]
With \(t=T^{-40/77}\), the three exponents in (3) are \(38/77,\ 37/77,\ 38/77+o(1)\), respectively. This establishes the second claim. It uses [Chudnovsky, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11) as quoted in the [earlier restricted-branch analysis](../../six-hour-20261127/arithmetic/MICROSCOPIC_JOINING.md). The first claim and (1)–(3) use no numerical irrationality exponent.

The counting argument cannot convert a sparse spectrum into emptiness. Even the much smaller set of upper convergent denominators has positive one-sided defects with summable powers: their rational approximation errors give \(q\cdot|a/q-\alpha|<1/q'\), and consecutive denominators grow at least as fast as the Fibonacci recurrence over pairs of indices. This supplies a precise numerical obstruction to inferring absence from summability alone; it makes no assertion about ordinary realization of those convergents.
