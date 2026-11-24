# Primary literature used in this closure attempt

## Effective logarithmic forms: used in a positive theorem

Qiang Wu and Lihong Wang, *On the irrationality measure of log 3*, Journal of Number Theory 142 (2014), 264–273, [DOI 10.1016/j.jnt.2014.03.007](https://doi.org/10.1016/j.jnt.2014.03.007), Theorem 1.

The publisher's complete statement was read. It bounds the nonzero form $a+b\log2+c\log3$ below by $H^{-4.1163051-\varepsilon}$ for sufficiently large $H=\max(|b|,|c|)$; the integer constant coefficient is free. We use $(a,b,c)=(0,A,-p)$ on one complete ordinary cycle. The coefficient norm satisfies $p\le H\le2p$. This gives a polynomial upper bound on the cycle minimum, which converts the exact profile-counting estimate into the positive-fraction occupation theorem.

This use is distinct from applying Corollary 1's irrationality measure for $\log3$ to the ratio $\log_2 3$. The actual Theorem 1 is the required statement. Its analytic proof and effective constants are not formalized in this packet.

## Subspace theorem: a retained fixed-arity condition

Jan-Hendrik Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica 53 (1984), 225–244, [primary scan](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf), Corollary 1, printed page 227.

The primary statement concerns primitive nondegenerate integer zero sums for a fixed number of summands and a fixed prime set. PR206's [SparseDefects.md at its frozen head](https://github.com/GettysburgResearch/collatz/blob/37d2b5d644664a746891042c199e58cfb06f1176/research/clock-itineraries/SparseDefects.md) applies it after an explicit shifted identity, common-divisor removal and no-proper-zero-subsum argument. Its constants may vary with the number of exceptions.

The present search asked whether many synchronized ordinary cycle phases could yield a fixed-dimensional contradiction. They do not supply that conclusion: the rotated physical divisibility equations are equivalent, while the distinct-past information constrains a separate companion denominator. No uniform-in-arity version or independent congruence family is assumed.

## Nonsingular dynamics: the supplied atom must retain mass

Idris Assani, *Collatz map as a non-singular transformation*, final accepted version, [arXiv:2208.11675v3](https://arxiv.org/html/2208.11675v3), Theorem 1.2 and Definition 2.5.

The existence of an invariant finite measure is different from the theorem's finite measure equivalent to counting measure, power bounded in $L^1$, with conservative part $\{1,2\}$. The latter is an equivalent formulation of universal Collatz convergence. It is not an available input.

The packet's elementary coboundary makes the relevant entrance-set issue exact: every stationary ordinary probability law assigns zero mass to odd multiples of three. A finite measure charging a source and uniformly dominating all of its pushforwards would already rule out an injective orbit from that source. We prove no such dominating measure.

## Source-qualified recent inverse-law input

Weaver and Wren, [paper 48 v2](https://rstation.ai/problems/collatz/papers/48/v2), Lemma 7, is the named floor F used by PR205's [joint real annulus argument](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/analytic/JOINT_REAL_FLOOR.md).

We retain F as an explicit source hypothesis in the separate clock-mass deduction. We do not independently validate that analytic theorem here, and neither the cycle-occupation result nor any Lean module depends on F. The deduction shows why the large-relative-carry filter cannot be dropped when trying to oppose PR201's exact-row lower bound.

## Scope of literature claims

This is a targeted use of primary sources at the remaining ordinary-source and complete-cycle interfaces, not an exhaustive literature survey or a priority claim. Reports of unrelated recent breakthroughs were not mathematical inputs. No unproved theorem is treated as established because of a claimed announcement.
