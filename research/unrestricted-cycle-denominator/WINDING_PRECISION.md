# Beyond every fixed polynomial precision in the winding test

In the [coprime modular tour](COPRIME_JET_WINDING.md) one can require
that the winding residual tend to zero faster than **every fixed
negative power of L**, still with all vertices comparable to L² and
with all the same exact tests. The measure remains one unit per
distinct ordinary source. This is an approximation statement.

First, the two errors in u C_i−C_(i−1) have the same sign after
subtraction. The previous convergent error satisfies

    1/(q_i+q_(i−1)) < |q_(i−1) α−p_(i−1)| < 1/q_i.

Together with the upper bound from the linked note, this gives
δ comparable to 1/L. Put R_0=L/δ, of order L².

## Equal-count choices at many scales

Use one of the fixed affine prototypes with a positive odd count.
At parameter t its contribution to the winding sum is the function

    f(t)=Σ_(v+ut odd) log(1+1/(3(v+ut))),

where the sum selects the lines of odd intercept, and each positive
slope is an even integer. Setting A=Σ_(odd lines) 1/(3u)>0, for
each fixed j≥0,

    f^(j)(t) = (−1)^j j! A t^(−j−1) (1+O_j(1/t)).

For example, write each summand as the integral of
1/(v+ut+x) over 0≤x≤1/3 and differentiate. For any fixed r≥2,
reserve 2^(r−1) copies. Choose their offsets, relative to one base
translation, from the even- or odd-digit-sum half of the integers
0,...,2^r−1, multiplied by a spacing h. The difference between
the resulting sums is

    G_r(t,h) = ∏_(j=0)^(r−1) (1−shift_(2^j h)) f(t).

Iterating the fundamental theorem of calculus and the derivative
bound shows it is positive and comparable to h^r/R_0^(r+1),
uniformly when t is comparable to R_0 and h=O_r(sqrt(R_0)).
The implicit constants are positive and can depend on r and the
fixed prototypes. Both configurations use the same number of copies
and keep all exact jet, label, and shape balances.

Fix an arbitrary final order s≥2. For each r=2,...,s use spacings
J,2J,...,2^m J, where J is a fixed integer larger than every absolute
intercept difference within the chosen prototype and 2^m J is
between R_0^(1/r) and 2R_0^(1/r). Use a sufficiently large fixed
number of identical gadgets at each spacing (their base translations
may differ). This reserves O_s(log L) prototype copies, leaving a
proportion tending to one available for ordinary rounding.

Take all the gadgets initially in their higher-winding configuration.
Assign base translations nonnegative of size O_s(L) so no two
same-slope sources from different gadgets or ordinary copies coincide
under any allowed choices. Each old gadget or ordinary copy rules
out at most O_s(1) translation values for the new one: the possible
sets of line offsets are of bounded cardinality, even when h grows.
Within a gadget J makes equal-slope collisions impossible between
different offset indices. Permit increments 0,1,2 for each ordinary
copy in the same selection. As before, all different slopes are
separated for R/L sufficiently large.

Solve the continuous winding equation in the common real translation
R with these initial choices. Its solution R_* is comparable to
R_0: at fixed positive multiples of R_0 all the offsets are o(R_0),
and the number of odd terms is comparable to L. Start at floor(R_*).
Raising every *ordinary* copy by two would take the sum below or to
the desired value: the reserved O_s(log L) copies account for o(1)
of the absolute total derivative, and on this bounded translation
range each individual derivative varies by a factor 1+O_s(1/R_0).
Thus by raising the ordinary copies singly by unit steps, stopping
before the first crossing (or at exact equality), one gets a
nonnegative excess of at most O(R_0^(−2)).

## Refining the remaining excess

At order r suppose the nonnegative excess is at most D_r R_0^(−r)
with a fixed D_r. Consider the spacings from largest to smallest.
At the first spacing a single decrement is between two positive
constant multiples of R_0^(−r); at subsequent spacings the scale
decreases by exactly 2^r. At each spacing greedily apply available
decrements that do not exceed the remaining excess. If the number
of gadgets is large enough, their total minimum decrement exceeds
the entering upper bound. Thus the leaving excess is below the
maximum single decrement there. For the first spacing take the
number of gadgets using D_r; at later spacings a fixed multiple of
2^r times the ratio of the uniform upper and lower constants suffices.
At h=J the excess is O_r(R_0^(−r−1)). This supplies D_(r+1).
All constants and multiplicities can therefore be chosen in order
before routing or rounding. The uniform constants for R_*/R_0 can
be chosen from the fixed slopes and the odd fraction alone for
large L, since every offset is o(R_0).

For fixed s this yields residual O_s(R_0^(−s−1)). Select larger
lengths successively for s=2,3,..., large enough to absorb the
constants. The resulting sequence has superpolynomial winding
precision. Uniform proportional-shell constants persist in the
diagonal selection, taking the stage large enough that all offsets
are at most o(R_0). The leading-slope argument still excludes exact
invariance of the sets.

## Exact winding without a high-shell or simplicity requirement

For comparison Applegate and Lagarias proved that the semigroup of
ratios n/T(n) is the set of positive rationals whose reduced denominator
is coprime to 3. Therefore *any* finite prescribed multiset of
ordinary edges with initial vertices prime to 3 can be enlarged to
a multiset satisfying exact product-one winding. Its prescribed
product is a ternary unit, so its reciprocal lies in the semigroup.
No factor with positive ternary valuation can enter a representation
of that unit, since all generators have nonnegative ternary valuation.
Even factors equal to 2 can always be represented by an even ternary
unit. The published semigroup theorem does not ensure the added
odd inputs are distinct or high, or that any jet balances survive.
[Applegate and Lagarias, Theorem 1.1](https://arxiv.org/pdf/math/0411140)
