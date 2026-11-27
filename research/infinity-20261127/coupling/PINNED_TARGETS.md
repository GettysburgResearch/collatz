# Joint visitation of prescribed targets and dyadic copies of a fixed pair

**Collatz remains open.** Use the positive shortcut map $T(2n)=n$, $T(2n+1)=3n+2$. Write $P(a)=\{x>0:T^i x=a\text{ for some }i\ge0\}$. Two targets are forward-comparable when one visits the other. Their trajectories can instead meet at a third point.

## Joint counts recover forward order

Let $I_X=[X,2X)\cap\mathbb N$ and $J_{a,b}(X)=\#\{x\in I_X:x\in P(a),\ 3x\in P(b)\}$. **SOURCE-QUALIFIED quantitative theorem.** For each fixed $0<\theta<1$, uniformly in all $a>0$ and $1\le b\le X^\theta$,

$$J_{a,b}(X)=\#(I_X\cap P(a)\cap P(b))+O_\theta(X/\sqrt{\log(2X)}).$$

The intersection equals $P(a)$ if $a$ visits $b$, equals $P(b)$ if $b$ visits $a$, and is empty if they are incomparable. If both directions hold, their predecessor sets coincide. For fixed ternary-unit targets, the joint count therefore has a positive lower fraction on all sufficiently large octaves exactly when the targets are forward-comparable, using the separate positive predecessor-density input. Cumulative counts follow by summing octaves. [Finite comparison](JointVisits.lean) · [PR146 finite coalescence clock](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md) · [Mazur, fixed unit predecessor theorem](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [Even-unit conversion and octave argument](https://rstation.ai/problems/collatz/papers/221/v1)

**Proof.** Take $h=\lfloor(1-\theta)(\log_2 X)/2\rfloor$. For large $X$, $2^h b<X$. Every orbit satisfies $2^iT^i x\ge x$. Thus neither $x$ nor $3x$ visits any gate at most $b$ before $h$. If the arms match at $h$, then at *every* absolute clock their visit indicators agree for *all* these gates simultaneously. Replacing $3x\in P(b)$ by $x\in P(b)$ costs at most the number of missed equalities at $h$. PR146's fair-bit estimate gives $O(2^h/\sqrt h)$ failures on each complete block of $2^h$ starts. Covering $I_X$ by such blocks gives the asserted order. Comparison of clocks, the finite counting inequality and forward comparability are kernel-checked. The asymptotic estimate uses PR146's separate proof. For an upstream unit, discard small starts from its positive lower cumulative count, then send each remaining start into the octave by doubling with bounded multiplicity.

**REFUTED universal lower bound at the repaired targets.** For canonical $q=113$, $T(3q)=509$. Both targets are units. They reach 1 after 10 and 33 shortcuts respectively, and neither visits the other. Lean checks both trajectories and the terminal cycle. Consequently $J_{113,509}(X)=O(X/\sqrt{\log(2X)})$. A universal positive-density bound, or a universal lower bound of order $X/(\log X)^\gamma$ with $\gamma<1/2$, fails for this corrected pair of targets. There are nondyadic witnesses: the odd $455907$ visits 113 in 31 steps and its triple visits 509 in 116. The upper bound supplies no matching lower estimate. A later shared target is a different prescribed pair. [Kernel control](JointVisits.lean) · [Independent ordinary computation](PINNED_TARGET_CONTROLS.json) · [Earlier multiple-of-three obstruction](../../../reports/six-hour-20261127/FINAL_CROSS_ATTACK.md)

## The same two centers at every scale

For any integer-valued ordinary invariant $b$, set $d(n)=b(n+1)-b(n)$. For every $q>0$ and $k\ge0$,

$$b(3q)-b(q)=d(2^{k+2}q)-d(2^k3q).$$

The centers halve to $q,3q$. Their right neighbors meet by $T^2(4v+1)=3v+1$. For the reach-one predicate, a disagreement at $q,3q$ forces exactly one center at each depth to differ from its right neighbor. [Kernel proof](DyadicPins.lean)

For every odd $q>0$ and $J\ge0$, some $J\le k<J+128$ and $h\le9$ give one common ordinary value for all four paths below.

| Starts, for $m=q,3q$ | Clock |
|---|---:|
| $2^k m-1$ | $k+h$ |
| $4^k m+1$ | $2k+h$ |

The initial prefixes end at $3^k m-1$ and $3^k m+1$. At $x=99+256v$ the four values $x-1,x+1,3x-1,3x+1$ meet in eight steps at $11+27v$, with grades $3,3,2,2$. At $x=237+512v$ they meet in nine steps at $38+81v$, with grades $4,4,3,3$. Among 128 successive powers of three times any odd residue modulo 512, one reaches one of these classes. Lean checks every residue, the affine lifts and all four original paths. The largest first successful wheel index for these two specified classes is 127. [Kernel proof](DyadicPins.lean) · [Replay](check_pinned_targets.py) · [Controls](PINNED_TARGET_CONTROLS.json)

## Finite neighborhoods about a fixed pair

**SOURCE-QUALIFIED written extension.** Fix a finite set $D$ of positive offsets known to reach 1, and $L\ge1$. For each fixed odd $q$, on a set of exponents $k$ of lower Banach density one, all the following starts share a single ordinary endpoint after their initial prefixes and a common further clock:

$$2^{k+j}m-1,\qquad 4^{k+j}m+d\qquad(m=q,3q;\ 0\le j<L;\ d\in D).$$

The first expression uses $k+j$ odd departures. For the second, lift the first $2(k+j)$ steps of the fixed offset $d$ on its dyadic cylinder. Once the clock exceeds $d$'s first hit at 1, the endpoint is $3^{k+j+c_d}m+s_d$, where $c_d$ is fixed and $s_d$ is 1 or 2. Each two further clocks on the cycle add one odd step. All endpoints consequently have the form $3^s u+e$ with fixed $s\ge0$, $e$, after taking $u=3^{k-k_0}q$ for one fixed $k_0$. For a block of $N$ exponent choices this geometric progression visits a subgroup coset modulo $2^h$, $h=\lfloor\log_2 N\rfloor\ge3$, with period $2^{h-2}$. Each period visits distinct residues. The full binary failed-residue count therefore bounds failures on one complete exponent period. Apply PR146's finite affine-pair estimate against a common reference arm and take a finite union bound. Padding the successes to the common further clock $h$ gives $O_{D,L}(N/\sqrt{\log(2N)})$ exceptions uniformly in interval location, apart from the fixed initial range. [Finite affine and exponent estimates](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Physical prefix lifting](../../six-hour-20261127/coupling/FloorCounting.lean)

If the centers have opposite reach-one labels, the common label disagrees with one center throughout this entire block. Taking nested finite offset sets and longer blocks, one *fixed* member of $\{q,3q\}$ has arbitrarily long such blocks. The negative neighbor uses dyadic exponent $k+j$ and positive offsets use $2(k+j)$. The construction does not supply an ordinary path from either center to its displaced neighbors. As a local control, the predicate of ever visiting 5 differs on 113 and 339, with its only failed forward-invariance edge at $5\to8$. At late exponents every prefix in the four-neighbor theorem avoids 5 through its merger. This is an almost-invariant control; the universal canonical implication for the exact reach-one predicate remains open.
