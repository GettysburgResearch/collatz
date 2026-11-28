# Exact cost of a distinct signed rational inverse path

The [Lean module](SignedDistinctCost.lean) proves the finite arithmetic estimate used in the [strict finite-window improvement](../broad/STRICT_FINITE_WINDOW_IMPROVEMENT.md). It concerns an actual signed rational trajectory and explicitly assumes distinct departure states. It does not assert distinctness for every controller, or prove a global Collatz conclusion.

Write a negative state as `-q_j/D`, with a fixed positive integer denominator `D` and positive integer numerators `q_j`. A legal inverse gap `e_j>=1` gives the literal equation

$$3q_{j+1}=2^{e_j}q_j+D.$$

The source definition `Follows D q e n` uses `e j+1` to encode the positive gap and requires this identity at every date below `n`. Let `S_n` be the sum of those gaps. If the `n` departure numerators are pairwise distinct and the terminal numerator is positive, the module proves

$$
3^n\le 2^{S_n}q_0\binom{D+n}{n}.
$$

This estimate has no unspecified constants. For fixed `D,q_0`, the binomial factor is polynomial in `n`; taking logarithms and dividing by `n` gives the written consequence `liminf S_n/n >= log_2 3` on any infinite path satisfying the hypotheses. The limit argument and the proof that a particular policy produces distinct states remain in the companion manuscript.

## The finite extremal product

For a finite set `s` of distinct positive integers, with cardinality `n`, `extremal_product` proves

$$
n!\prod_{q\in s}(q+D)
\le (D+1)(D+2)\cdots(D+n)\prod_{q\in s}q.
$$

Its proof inserts the largest element `q`. Distinctness and positivity imply `q>=n`; the new factor is controlled by `n(q+D)<=(n+D)q`. This is an integer proof of the fact that the product of `1+D/q` is largest on the first `n` positive integers. It uses no real logarithms or analytic approximation.

The private native calibration multiplies `3q_{j+1}<=2^{e_j}(q_j+D)` through the path while retaining all integer factors. Applying the extremal product to the actual image of the departure indices and cancelling its positive product gives the stronger public estimate

$$
3^nq_n n!\le 2^{S_n}q_0(D+1)(D+2)\cdots(D+n).
$$

`positive_terminal_cost` drops the positive `q_n`; `binomial_cost` uses the exact rising-factorial/binomial identity and cancels `n!`. All cancellations carry their positivity hypotheses. The finite theorem also permits `D=0`; the signed rational application uses `D>0`.

## How the strict-memory argument uses it

The companion construction provides, for each observed row, a negative rational periodic path with two indistinguishable observed states requiring different next gaps. A deterministic finite-window rule must leave that path. The uniqueness of the actual forward odd predecessor prevents it from returning or repeating a state, so the displayed finite hypothesis holds for the baseline rule. The periodic alternative has a lower total cost. Both finite words remain valid on a sufficiently precise ordinary positive source cell. Substitution on those cells and a finite Bellman bias calculation then produce a genuinely better stationary finite-window policy.

The Lean module checks the arithmetic after the recurrence and distinctness have been supplied. The construction of the signed cycle, its dynamical nonrepetition, the policy improvement, and the infinite optimum are separately reviewed written arguments. The broad-track reviewer independently reconstructed the extremal product, the native multiplication, the image reindexing and the exact positive cancellations. The new binomial presentation is just the standard factorial identity applied to that reviewed endpoint. The aggregate checkpoint receipt audits every generated and private declaration as well as the public theorems.
