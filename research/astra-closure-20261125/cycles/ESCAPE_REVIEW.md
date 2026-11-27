# Independent check of the same-cycle construction

**Verdict: VERIFIED at the stated finite guard depths, with the cited logarithmic-forms estimates as external inputs to the asymptotic existence theorem.** I reconstructed the finite ancestor tests in reverse order, checked the compatibility of the bit changes with the rotation argument, and constructed a separate rational cycle on which all the finite conditions can be inspected simultaneously. No ordinary cycle or all-depth basin assertion follows.

I reviewed [JOINT.md](JOINT.md) at SHA-256 1c2dd1674f38312a01a5a69399dfd105630032f5a7e23184226b411225aac47a and the [prime-power proof](README.md) at SHA-256 3efbc43ac2ce3168ec4ad2a831fc309b4f703b6ad6d48cc1b511d3d9ed5d2cd6. The ancestor definitions in [BASIN.md](BASIN.md) had SHA-256 6a9bd73f4d981b66be0c8c53c786c436fe5ea717ef423edf941d435d4ee86991. This review concerns the joint rational-cycle theorem and does not review the separate 90-step block entropy calculation.

## Exact inverse enumeration

I used the actual terminal history to obtain an integer representative $u$ modulo $3^{17}$ and grew inverse paths out of $u$. At reverse depth $j$, total valuation $A$ and carry $C$, the prospective source is $(2^A x-C)/3^j$. For an additional gap $e\ge1$, require $2^e u-1$ divisible by three and recurse with

$$
 (u,j,A,C)\ \longmapsto\
 \big((2^e u-1)/3,\ j+1,\ A+e,\ 2^e C+3^j\big).
$$

Using $u$ as an integer, without re-reducing at each step, is harmless: at depth $j$ this obtains the exact endpoint modulo $3^{17-j}$. Thus multiple-three status is determined through depth 16 and ordinary inverse legality through depth 17. I pruned a branch only when even the minimal remaining positive gaps exceeded the total budget. For floor slope $f\in\{3/4,2\}$ the small-total budget at depth $k$ is $\lfloor\log_2(f3^k)\rfloor$. For larger totals the first omitted power strictly exceeds $f3^k$. The universal inverse offset bound $\eta\le(3/2)^k-1$ handles all those totals at each of the finitely many depths as the minimum grows.

For the generic windows my exact rational implementation split $[1,2)$ at the normalized numbers $c3^i$, $0\le i\le17$, $c\in\{1,4/3,8/5,19/10\}$, and at 2. The 55 resulting intervals suffice for the wraps and free-bit membership of all 18 vertices of a 17-gap history. On each interval I used the left endpoint to bound height and tested every subset of available lowerings. The 1,728 interval/pattern combinations gave minimum ratio $8/5$ to the competing slope threshold, including the auxiliary minimum floor 1. The original checker uses additional cuts and returned the same margin in 3,168 comparisons. The apparent coincidences caused by $4/3$ are the same next-step wrap as the normalized endpoint $1$: under rational rotation its moving threshold is $4/2^{h/p}$. Distinct base constants $1,8/5,19/10$ cannot acquire a coincidence in the limiting finite list by multiplying by powers of 2 and 3. Order and one-sided cell ownership persist at sufficiently late clocks.

In the anchor neighborhood I recovered each actual site as $a_i s+b_i$ using the finite physical edges from time zero. The strict leading comparisons had smallest ratio $4/3$. The twelve tied branch tests were all at $i=k$ and all required a multiple of three. The table gives their full list; the smallest surviving affine intercept was exactly 1 in every row. An ordinary-floor tie would instead require at least $1/4$.

| $i=k$ | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Total $A$ | 7 | 9 | 11 | 12 | 14 | 15 | 17 | 19 | 20 | 22 | 23 | 25 |
| Minimum $(2^A b_i-C)/3^k$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

This is precisely where an $o(1)$ relative height error would be insufficient. The anchor computation uses the actual affine equation with unrounded slope and intercept. The deleted temporal neighborhood contains every 17-gap history touching one of the four anchor vertices. All other choices in such a history are fixed, even after solving the local divisibility equations.

## One joint rational witness

Take $p=306$, $h=485$, $D=2^{485}-3^{306}$. Use octave 1 except at these 40 rank indices, which have octave 0:

~~~text
0 127 179 212 215 217 218 227 228 229 230 232 233 234 236 238 239 240 241 244
245 246 251 253 254 255 258 261 262 263 267 268 269 273 274 276 279 280 281 282
~~~

Starting at $r=0$, use $r'=(r+485)\bmod306$, $e=\lfloor(r+485)/306\rfloor+j_r-j_{r'}$. From $(A,C)=(0,0)$ update $(A,C)\mapsto(A+e,3C+2^A)$ once per gap. Starting at $s=C/D$, I walked the literal rational trajectory for a full lap and applied the independent reverse enumeration above at **each of the 306 odd phases**. For the omitted large totals I checked, for each site and depth, the inequality with the first omitted $2^A$ and the worst allowed $\eta$. Rational comparison gives both finite guards over all valuations, including all anchor equalities.

The period has 485 distinct physical phases. The full 929-primary part of $D$ is 929 and cancels in $C$. The remaining reduced denominator has **466 binary digits**, $\lfloor s\rfloor=39859$, and the odd width is approximately $3.99097116235$. Sorting the actual dyadic and ternary mantissas gave the claimed two permutations. The smallest sorted-octave mismatch count over the 305 nonzero shifts was 38; the temporal shift gave 74. There were 266 odd phases above $2s$. On the 485-step physical cycle I checked all backward score sums of lengths from 1 to 485 with integer increments $5e_i-3$ for the physical parity $e_i\in\{0,1\}$. Since the lap has positive score, these suffice for strict all-pasts records. There were 61, all above $2s$. These numbers describe this single witness.

## Correction interval, two orders and denominator count

Writing $r_i=ih\bmod p$ gives cumulative valuation $\lfloor ih/p\rfloor-j_{r_i}$ since $j_0=0$. For $Q=\prod_{\ell\in S}\ell^{v_\ell(D)}$, Bezout gives a unit $u$ with $u^p=2$ and $u^h=3\bmod Q$. After multiplying the carry by $2\cdot3^{1-p}$ its summand at $r_i$ is $(2-j_{r_i})u^{-r_i}$. Solving the bit sum therefore cancels the whole prescribed primary part of this physical word, including all multiplicities.

For each active prime the difference of the two supported bit patterns is a translate of $\prod_i(v^{t_i}-1)$ with $v=u^{-1}$. The doubling gaps between the $t_i$ make the two coefficient supports disjoint. The elementary odd-prime lifting formula gives precisely the specified digit valuation at the active prime and at least the required multiplicity at every other prime. The first block sets the common low residues and each corrected digit preserves all earlier ones. Yu's consequence of Theorem 1 applies to the nonzero $2^h3^{-p}-1$ with two fixed local units and fixed field at each prime. This bounds $v_\ell(D)$ by $O_\ell(\log p)$ and the number of changed ranks by $p^{o(1)}$ for fixed $S$. The bounded deletion near the anchor splits the positive-length free interval into finitely many pieces; one piece has length $\gg p$ and contains the whole correction support at late clocks. [Yu, pp. 337–338](https://doi.org/10.4064/aa-89-4-337-378)

Changing $T$ bits changes each centered partial sum of the affine offset along a lap by $O(T)$, including recomputation of the mean. The uniform $o(p)$ discrepancy thus survives. Abel summation of the contracting normalized recurrence gives normalized heights $V+o(p)$ with $V\gg p^2$ for fixed approximant accuracy. Consecutive nominal mantissas differ by $\gg p$, so sorting is stable. When reducing a ternary label modulo $h$ one divides the corresponding physical height by 3; its additional nominal error is $O(1)$ since $(2^{h/p}/3-1)V=O(1)$. All labels lie below $3p<2h$. This checks both rotation orders on the corrected trajectory. Each changed rank affects at most two mismatch indicators per shift. In contrast, the initial bounded-differences estimate has linear slack, and the number of free ranks exceeds $p/5$ by a positive linear margin. The entropy surplus survives both the bounded anchor deletion and the $2^{o(p)}$ upper bound on input multiplicities after correction.

The inherited real two-logarithm bound supplies a polynomial upper bound on $s$; any fixed polynomial suffices here. Distinct retained octave patterns give distinct minima, since the exact orbit of a minimum and its sorted dyadic mantissas recover the pattern. There are only $O(\operatorname{poly}(p)Y^2)$ rational minima with reduced denominator at most $Y$. Taking $Y=2^{p/10}$ leaves joint examples above this denominator. The argument with increasing prescribed cancellation at a single prime uses a diagonal over fixed prime-power requirements on upper approximants, not an assertion of those congruences along the ordinary sequence of continued-fraction convergents.

The finite inverse depths, the prime set fixed before taking large clocks, the source-qualified logarithmic-forms inputs, and the rational domain are essential to this verdict. The independent enumeration and literal witness are exact finite arithmetic. The full asymptotic existence argument remains written mathematics.
