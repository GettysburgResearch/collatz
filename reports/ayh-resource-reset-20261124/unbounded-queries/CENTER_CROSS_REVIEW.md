# Independent review of the two ordinary center theorems

**Verdict.** Verified at the four source hashes below. The progressions exclude possible least defects at actual ordinary parents. They select a subset of parameters on the e=6 family. No conclusion applies to every such parameter or every least defect.

## Fixed depth, cofinal parameters, ordinary comparisons

For fixed $n$ and arbitrary $L$, put $g=7n$, $h=11n$, $D=3^{8+g}$, and $K=2561\cdot2^{161h}$. The proof sets $B=DK-13047808$. The product is large enough for the subtraction in the natural numbers and $B$ is a ternary unit. The earlier ordinary lifting theorem returns $e\ge29+162L$ and $k\ge0$ with $2^e=B+3^{13+g}k$. Reduction modulo 243 forces $e=29+162m$, so $m\ge L$. Writing $q=K+243k$ gives $2^e+13047808=Dq$. As $128\mid Dq$ and $D$ is odd, $q=128t$ with integral $t$. Reduction of $2^h q$ modulo 243 supplies an ordinary $w$ with $81w+2399=128\cdot2^h t$, $w\equiv17\bmod48$. Thus $w>0$. Dividing the equation for $Dq$ by 128 gives the required terminal relation. The existing Mersenne family constructs an actual parent $z$ for every such $m$.

The seven-step entries for the lower and upper arms are $2^h t-17$ and $3\cdot2^h t-55$. Every lap at either signed phase consumes 11 supplied binary factors and gains seven powers of 3. Two final ordinary affine rows at residues 31 and 89 give precisely $2^{11+162m}-1$ and $2^{9+162m}$. These numbers are respectively the parent’s lower endpoint and a power of two. The strict shrink follows from $2048\le2187$ in the exact integer equations, including their intercepts. If the parent were a least reverse defect, the strictly smaller $w$ would therefore be a reverse defect. For arbitrarily large savings the construction chooses the depth after the desired factor, and then chooses $m$ above its prescribed cutoff. Nothing chooses $n$ for an already supplied arbitrary $m$.

At a valid positive-depth parameter, the earlier intermediate charts genuinely need fractional arithmetic. The final chart is an integer, while the center has ternary valuation −4. Thus their difference has valuation −4. Moving back from depth n to any earlier i adds 7(n−i) to that valuation. The resulting difference has strictly positive valuation, so adding back the center leaves the earlier chart at valuation −4. Its denominator is a power of three by the chart formula. Hence its reduced denominator is exactly 81, as the final note states. The physical query uses the integral final chart directly.

## Exact classes and the previous seventeen residues

With $G=8+7n$ the parameter congruence is
$$
2^{11n}(2^{29+162m}+13047808)\equiv 3^G\cdot2561 \pmod{3^{G+5}}.
$$
The valuation of $2^{162}-1$ is exactly five. Its successive cubes gain exactly one more ternary factor. Consequently each successive digit of $m$ has exactly one choice, and the period is $3^G$. The valuation of $2^{29+162m}+13047808$ is $G$ on this class, so classes of different depths are disjoint. For all $n\ge1$, $G\ge15$ gives the same congruence modulo $3^{14}$ and hence $m\equiv3122\bmod 19683$. I independently checked this exponent and expanded the 13 published rows, including the two shorter periods, to all 17 residues modulo 19683. They omit 3122. Depth zero reproduces the old 5903 row.

A further written consequence is that the union over $n\ge1$ has natural density $1/14342346$. The finite partial sums of the disjoint progression densities tend to $\sum_{n\ge1}3^{-8-7n}$. The tail $n\ge N$ is contained in one class modulo $3^{3+7N}$ by the same valuation and order calculation. Its upper density tends to zero, justifying the sum.

## Denominator obstruction

The all-clock proof uses the exact inequality for the positive orbit, splits at $a=11+d+E$, and retains parity agreement with the signed translate only through the supplied precision. When extra odds exceed 11, their remaining word yields an interval bounded by $3^r-2^{r-11}$ and $3^r-1$. The lower bound is positive and forces the original signed translate to be positive. The complete finite trap, with its post-arrival two-cycle argument, yields only $(3233,18,15,11)$; this makes the required slope inequality an equality. Thus the claimed $d\ge k+5$ holds for this normalized lower-phase mechanism at every $m=3^k t$, including $t=0$. Its hypotheses explicitly include the shrinking slope and prescribed lower phase. The written fixed-chart obstruction at the zero address uses fixed rational centers; it does not exclude changing-chart schemes.

## Replays

I compiled copies of both Lean sources into a fresh local object directory with Lean 4.34.1, the pinned Mathlib objects, and the existing project dependencies. Both passed with auto-implicit declarations disabled and warnings treated as errors. All eleven printed declarations used only the usual Lean axioms. I also ran the supplied checker under optimized Python and recovered both large physical traces and the full small-source trap. A separate modular solver computed each next exponent digit by one linear congruence; it verified depths 0, 1, 2, 3, 6, 16, 32 and 64. These finite checks complement the general proof.

| File | Reviewed SHA-256 |
|---|---|
| AllDepthCenter.lean | 3c3cfa27db12ef34434a5dd2df2073545a27f492fa9a1bfb10125c2dd1f01472 |
| RationalCenterPump.lean | 98c1a8320e892137eef3cf71730f52e5cfc329081d9432523ff3d006320f102c |
| check_rational_pump.py | 0fedea6af2f5c1da2aae4c6ed3e5ec46e44771634c43ee770ae36cdf5ffc11d7 |
| RATIONAL_CENTER_PUMP.md | b0c292a809cdd5382730b16496e88b640215b1d74cae3daa1b7e6654f900650a |
| Independent two-module build log | d53d3061a7174acf18e62d75afe40580dd882a6a5cbe40762e1d057566988d92 |
