# Three ordinary parents meet after their Mersenne peaks

**PROPOSED.** At the same supplied positive source in the three-odd upper-certificate family of PR197, two strictly smaller candidates have the same lower basin label and independently certified upper hits. The construction works on explicitly decidable infinite progressions, including progressions in every prescribed odd congruence class for the parameter and arbitrarily close to the exceptional anchor in the binary integers. Complete pointwise coverage is open.

Use the ordinary shortcut map $T$. For integers $m\ge0$ write

$$
 J_m=11+162m,\qquad Z_m=(128\,2^{J_m}-271)/81,\qquad M_j=2^j-1.
$$

These are positive integer parents with $Z_m\equiv17\pmod {48}$. To see the residue directly, use $2^{162}\equiv1\pmod {243}$ and the initial parent 3233. The factor 16 in the residue of the quotient follows from its numerator at any exponent. The ordinary lower and upper certificates are

$$
 T^7 Z_m=M_{J_m},\qquad T^{J_m+7}(3Z_m)=1.
$$

The upper clock is a first hit with three odd departures. Those statements, including the first-hit check, come from PR197 and PR192. The lower identity and the upper hit are also independently proved here. The first-hit time and odd-count identification use the pinned results. No assertion that the *lower* arm hits one enters the construction. [PR197 family and upper trace](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean) · [PR192 upper first hit and original lower obstruction](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/transport/CanonicalDeadline.lean)

## The source-specific theorem

Let $S$ be the positive integer named `seed` in [PostPeakMerger.lean](PostPeakMerger.lean). It is the least nonnegative residue modulo $2^{1379}$ of PR206's constant `one`. Fix $L\ge0$. Use precisely the parameters satisfying

$$
 3^{162m}-1=2^{949+2L}u,\qquad
 3^L u\equiv S\pmod{2^{1379}}. \tag{1}
$$

The congruence makes $u$ positive and odd. Such $m$ form one nonempty residue class modulo $2^{2325+2L}$. They satisfy $v_2(m)=946+2L$, in particular $m\ge3$. Every one of the three distinct positive parents
$Z_m,Z_{m-1},Z_{m-3}$ reaches the **same actual ordinary integer**. Their respective clocks, for $i=0,1,3$, are

$$
  7+J_{m-i}+947+2(L+1)+1379. \tag{2}
$$

Consequently $Z_{m-3}<Z_{m-1}<Z_m$. If $Z_m$ were a least reverse defect in the residue $17\bmod48$, the two smaller parents would both be reverse defects: each triple independently reaches one and each lower orbit shares the parent's endpoint. This contradicts leastness. Their clock differences from the original parent are 162 and 486. The theorem does not assume an odd-count match between the complete parent paths. [Kernel statements `three_peaks`, `three_parents`, `upper_hit` and `excludes_least`](PostPeakMerger.lean)

## Why the post-peak times can be aligned

The first $j$ steps from $M_j$ reach $3^j-1$. This follows by successively replacing $2^a v-1$ by $2^{a-1}3v-1$ while $a>0$. The three relevant post-peak starts are $3^{11-162i}R-1$, $R=3^{162m}$. To find compatible finite parity words, first study the rational centers $3^{11-162i}-1$ with $R=1$. Use ordinary numerator parity on rationals of odd denominator. If $p$ odd inputs are used through $h$ steps, a perturbation divisible by $2^h$ in the odd-denominator rationals adds $3^p/2^h$ times its original value to the endpoint. This follows by induction on the ordinary branches.

| $i$ | Center | First hit at 1 | Odd count there | Odd count at clock 947 | $11-162i+P_{947}$ |
|---:|---|---:|---:|---:|---:|
| 0 | $3^{11}-1$ | 89 | 45 | 474 | 485 |
| 1 | $3^{-151}-1$ | 327 | 151 | 461 | 310 |
| 3 | $3^{-475}-1$ | 947 | 475 | 475 | 0 |

All three hits occur at odd clocks, so full turns of the $1,2$ cycle bring every center to one at clock 947. The signed traces are finite discovery data. The Lean proof instead computes positive ordinary representatives using the least residue $A\equiv3^{-475}\pmod{2^{947}}$, then proves the identities for every original source by the ordinary high-bit lift.

Write $t=(R-1)/2^{947}$. The actual endpoints at clock 947 are $1+3^g t$ at grades $g=485,310,0$. Equation (1) makes $t=4^{L+1}u$. Each pair of steps sends $1+4v$ to $1+3v$. After $L+1$ such pairs the endpoints are $1+3V_g$, $V_g=3^{g+L}u$. Each $V_g$ is odd. The even point $1+3V_g$ and the odd point $V_g$ have the same immediate successor.

For $g=0,310,485$, at the concrete positive starts $3^gS$, clock 1379 gives the same endpoint $C$ and $g+P_{1379}=658$. The Lean kernel recomputes these three complete ordinary prefixes. It also computes their lifts: for $3^Lu=S+2^{1379}b$, all $T^{1379}(V_g)$ equal $C+3^{658}b$. Positivity and the least-residue convention ensure $b\ge0$. The first of these 1379 steps accounts for the shared successor just identified. Adding the actual clocks gives (2). This uses three entries of one explicit certificate from PR206, independently rebuilt. It does not assume that a change of basin label recurs or that a later coalescence block covers a prescribed exponent. [PR206 source constant and larger certificate](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontierMergers.lean)

## Existence, exact residual and the obstruction at 3233

If $a\equiv1\pmod 4$, then $v_2(a^{v}-1)=v_2(a-1)+v_2(v)$ for positive $v$. Factor the difference for the odd part, then successively square; the sum factor at each square has valuation one. Here $v_2(3^{162}-1)=3$. For $e=949+2L$, put $k=e-3$ and $B=(3^{162})^{2^k}$, so $v_2(B-1)=e$. The normalized map $f(v)=(B^v-1)/2^e$ preserves the 2-adic valuation of differences: for $v>w$, factor out the odd $B^w$ and apply the same formula to $v-w$. It thus induces a bijection on every finite ring of binary residues, by injectivity on a finite set. In particular exactly one residue $v\bmod 2^{1379}$ solves $3^Lf(v)\equiv S$. It is odd. Taking $m=2^k v$ proves the progression assertion and the valuation requirement. This arithmetic proof of progression existence is written mathematics. The complete positive-source merger under the gate is the Lean statement.

The progressions for different $L$ are disjoint, since their valuations differ. Their union has natural density $4/(3\cdot2^{2325})$ in the parameter $m$. Indeed the sum of their densities is geometric, with ratio $1/4$, and the uncounted tail lies in a single class of integers divisible by $2^{946+2L}$. The Chinese remainder theorem allows any prescribed residue modulo **any odd modulus**, including $3^r\mid m$, within every one of the progressions. Increasing $L$ also makes $m$ divisible by every prescribed power of two.

The exact complement of this particular comparison can be identified at each $m>0$: the valuation $v_2(m)$ must have the form $946+2L$, and then its uniquely determined $L,u$ must pass the single residue test in (1). Outside this set the three-arm certificate makes no claim. The first unproved pointwise step would supply a successful construction for each remaining least defect, or establish an independent reason it cannot be one.

At $m=0$, PR197 rules out all 67 smaller residue-17 candidates reaching any of the twelve phases through $M_{11}$'s initial ascent. The present comparisons occur *after* both Mersenne peaks and keep the original upper hits for the smaller parents. Thus the new progressions include arbitrarily high binary and ternary contact with that anchor while respecting its all-clock exclusion of the old phase targets. The special smaller comparisons here do not produce a smaller parent at $m=0$. [PR197 missing-source and denominator argument](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/paired-reductions/CENTER_PHASE_OBSTRUCTION.md)

Using just the first two rows of the table gives a companion written result. Stop at 327, where the grades are 175 and 0, and replace $949$ by $329$ in (1). The same $S$ also merges grades 0 and 175 at clock 1379 with augmented grade 658. This proves a two-parent merger on one class modulo $2^{1705+2L}$ for every $L$, with $v_2(m)=326+2L$. The rational traces, integral representatives, tower words, finite binary-index inversions and residue exclusions are independently replayed by [check.py](check.py). The checks of huge exponent classes use exact modular arithmetic. They do not expand $Z_m$ or enumerate its doubly exponential-sized orbit.

The two constructions select disjoint parameters. If both valuations held with lap counts $L_2,L_3$, they would force $L_2=L_3+310$. Both normalized odd parts would then be the same $u$. Their residue tests would imply $(3^{310}-1)S\equiv0\pmod{2^{1379}}$, whereas $S$ is odd and $v_2(3^{310}-1)=3$. Thus the union on which at least one of these two prescribed comparisons succeeds has exact density $(4/3)(2^{-1705}+2^{-2325})$. This disjointness argument was supplied in the [independent review](../../../../reports/astra-global-closure-20261124/round13/trace/MERGER_REVIEW.md).

The [arbitrary finite-offset theorem](../trace/FINITE_FAMILY.md) proves an effective subprogression in every prescribed arithmetic progression and establishes that every actual augmented post-peak class is finite. A [separate density estimate](DENSITY.md) applies the pinned PR146 pair-absorption bound to growing blocks of earlier parents.
