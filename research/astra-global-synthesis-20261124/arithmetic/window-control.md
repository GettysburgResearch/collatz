# Exact inverse-clock optimization can persist for arbitrarily long wide deficit windows

**PROPOSED control theorem for ordinary finite segments.** This addresses a specific proposed step from full finite-window minimization to the absolute-width bound $B_i\le3$ in [the optimality argument](optimality.md). It retains all odd predecessors and their integer heights. It does not construct an infinite positive escape or identify the actual corrected height of a positive source after the common finite horizon.

## The control

Fix a horizon $H\ge1$, a floor $L$ and a positive real tolerance $\epsilon$. One positive odd source has an actual path $q_0,\dots,q_H$ above $L$, all odd ternary units, with the following joint properties.

1. Its valuations alternate $1,2,1,2,\dots$. The displayed valuation is the least unit predecessor valuation of its successor, and is also the least unrestricted odd predecessor valuation there.
2. For every $0\le i<j\le H$, among **all positive ordinary odd** $(j-i)$-step predecessors of $q_j$, the actual $q_i$ is the unique minimizer of the **total clock**, and also the unique smallest **ordinary starting value**. Both assertions remain true upon restricting to units. No bound on a competitor's valuations is part of the statement.
3. The path admits homogeneous heights $M_i=q_i+5$ at even $i$ and $M_i=q_i+7$ at odd $i$, with $2^{a_i}M_{i+1}=3M_i$. The ratios $M_i/q_i$ can all be made smaller than $1+\epsilon$, and the sum of actual logarithmic corrections along the whole path can be made smaller than $\epsilon$. The infinite alternating *clock* has full deficit series $B_i=5,7$ alternately. The displayed $M_i$ are finite comparison data and attain these two deficits, not assertions about the true infinite positive trajectories.

### A strict signed minimizer for every depth

The signed $3x+1$ odd map has the two-cycle $c_0=-5,c_1=-7$ with valuations 1 and 2. On magnitudes this is the positive map $V(w)=(3w-1)/2^{v_2(3w-1)}$, with cycle $5,7$. Fix any endpoint on the signed cycle and any odd-step depth. The signed cycle path is the **unique** odd predecessor path having the smallest total clock.

Every signed odd predecessor of a negative endpoint is negative. On magnitudes, 1 is fixed and 3 maps to 1, so any odd ancestor off the $5,7$ cycle is at least 9. Compare an alternative path with the cycle path to the same endpoint at the same depth. Before first entering the cycle every alternative magnitude $w$ exceeds each baseline magnitude. After entry the two paths agree at the same times, since the cyclic predecessor permutation is invertible and the endpoint and remaining number of steps are the same. Multiply the step ratios to get

$$2^{E-A}=\frac{w_{\rm start}}{w_{\rm baseline}}\prod_{t<h}\frac{3-1/w_t}{3-1/w_t^{\rm baseline}}>1$$

for any genuinely different path. This uses monotonicity of $3-1/w$ and includes a possible multiple of 3 at the first source. Therefore $E\ge A+1$.

### Transfer to one positive source for all windows at once

Let $A_j$ be the partial clocks of the alternating word and choose any positive integer $t$. Set

$$q_0=-5+2^{A_H+1}3^{H+1}t,\qquad q_j=c_j+2^{A_H+1-A_j}3^{H+1+j}t.$$

All these integers are positive odd units. The signed cycle equations directly show $3q_j+1=2^{a_j}q_{j+1}$, so the valuations are exact, and the displayed $M_j=q_j-c_j$ have the asserted homogeneous law. Take $t$ large enough to meet the stated floor and tolerance and make $q_j>2(3/2)^H$ throughout. Since the targets at a clock 1 are congruent to $-7\equiv2\pmod9$ and those at a clock 2 to $-5\equiv4\pmod9$, these are their least legal exponents with or without the unit condition.

For any window ending at $q_j$, a competing actual inverse word of length $h=j-i$ transfers to the negative target $c_j$ with the **same complete word**. Indeed $q_j-c_j$ is divisible by $3^{H+1}$. At one inverse step of exponent $e$, the difference of the predecessors is $2^e(q_j-c_j)/3$, an even integer retaining one fewer factor of 3. Induct backwards for all $h$ steps. Integrality, oddness, and each mod-3 unit test are preserved. Negativity of every comparison source follows from the negative endpoint. Hence a different word on the positive path must have $E\ge A+1$ by the signed minimization, where $A=A_j-A_i$. A fixed endpoint and word have exactly one starting value, proving the strict clock claim.

For the height claim, a competing positive source $z$ obeys $3^hz=2^E q_j-C$. The uniform complete carry estimate is $0<C/2^E\le(3/2)^h-1$, obtained by summing the $h$ suffix factors and using every valuation at least one. Thus

$$3^hz\ge 2^E\big(q_j-((3/2)^h-1)\big)>2^{E-1}q_j\ge2^A q_j>3^h q_i.$$

Every different word therefore costs a strictly larger starting integer as well. The alternating clock has $B_{\rm even}=1/3+(2/3)B_{\rm odd}$ and $B_{\rm odd}=1/3+(4/3)B_{\rm even}$, with convergent two-step series of ratio $8/9$. This gives $B_{\rm even}=5$, $B_{\rm odd}=7$.

## Scope of the obstruction

The two kinds of minima in PR182 at `f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67`, `research/central-closure-20261124/FIXED_FLOOR.md`, §2, and the unit-minimum finite-window inequalities in [the section packet](../section/proof.md), §4, motivate retaining both predecessor sets. Over the entire constructed finite horizon they give the *same* minimizing representatives. The correction and height tolerances do not repair a fixed-window proof of a $B_i\le3$ event. The initial positive source is allowed to change with $H$. In fact an infinite literal alternating word from one ordinary positive source would have to equal the signed cyclic source by the parity-cylinder congruences at every depth. The trick cannot pass from these finite minima to the full synchronous classes of one escaping orbit. Controlling unbounded merger horizons on that source, or finding an independent infinite obstruction, remains open.
