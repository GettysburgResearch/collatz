# Last-pass deductions and the exact remaining targets

**Status: written arguments, independently reconstructed by the
coordinator after the 93-module freeze. No new Lean theorem is claimed.**
The [fifth checkpoint](CHECKPOINT_05.md) and its full replay remain
unchanged. These deductions sharpen the next questions; none closes
Collatz. In particular they do not turn a restricted cycle theorem, a
finite table, or a family of chosen sources into a universal result.
The [written review record](FINAL_FRONTIER_REVIEW.json) identifies what
was reconstructed and which prior source was read.

## 1. A sufficient range for the cycle mismatch theorem

Let a cyclic word of positive odd-division exponents have length `p >= 2`
and mean `mu = h/p` in `[4/3,5/3]`. Write `n_j` for the number of letters
equal to `j`, and `s(l)` for the number of mismatches at proper lag `l`.
An exact averaging identity is

```
sum_{l=1}^{p-1} s(l) = p^2 - sum_j n_j^2.
```

Consequently some proper lag satisfies

```
s(l) <= p^2/(p-1) * [2/3 - (2-mu)^2/2].
```

Here is the elementary optimization giving the stated constant. Put
`B=(2-mu)/2` and let `f*` have masses `1/3+B, 1/3, 1/3-B` at letters
one, two and three. Its mean is `mu`; on this range of means it is the
positive part of the affine sequence `b_j=1/3+B*(2-j)`. Every other
probability distribution `f` of mean `mu` has
`sum f_j b_j = sum (f*_j)^2`. Since `f*_j >= b_j` and `f_j >= 0`,
`sum f_j f*_j >= sum (f*_j)^2`. Expanding the nonnegative squared
distance gives `sum f_j^2 >= sum (f*_j)^2 = 1/3+2B^2`. Apply this to
`f_j=n_j/p` and average the mismatches.

For any hypothetical unbounded family of distinct positive integer
cycles, their minima tend to infinity: a specified minimum determines
its entire forward orbit, so only finitely many cycles can have bounded
minimum. The cycle product formula then gives `h/p -> log_2(3)`, and
`h <= 2p` ensures the odd periods also tend to infinity. Thus such a
family has some proper lag with

```
s(l) <= [c + o(1)] p,
c = 2/3 - (2-log_2(3))^2/2 = approximately 0.58054.
```

This is a linear ceiling, not the bound of six needed by our denominator
theorem. A sufficient new route would exclude denominator one uniformly
through this linear mismatch range and also eliminate the remaining
finite cases. No such arithmetic theorem is proved here. PR211's
density-one period restriction does not supply it: a lone exceptional
period, or a sparse collection of exceptional periods whose every
proper odd lag has at least seven mismatches, survives both restrictions.
Repeating a word does not increase its least period.

## 2. An exact transport-and-cancellation identity for the unmarked rate

Retain the original odd inverse operator and the original target weight

```
(Kf)(z) = sum_{e>=1, y=(2^e z-1)/3 positive odd unit} 3*2^(-e)*f(y),
pi(y) = 1/[y*(3y+1)].
```

An odd unit is a positive odd integer prime to three. Let `rho_{d+1}`
be the original all-visit density, so `rho_{d+2}=K rho_{d+1}`. Put
`delta_d=rho_{d+2}-rho_{d+1}` and
`R_d=sum_{y>1} pi(y)*max(delta_d(y),0)` on the odd targets. This is the
unmarked positive variation, not the full marked statistic.

Write `U(y)=(3y+1)/2^e`, where `e=v_2(3y+1)`, and `omega(y)=3*2^(-e)`.
At each odd target `z>1` define

```
Splus_d(z)  = sum_{U(y)=z} omega(y)*max(delta_d(y),0),
Sminus_d(z) = sum_{U(y)=z} omega(y)*max(-delta_d(y),0),
C_d = sum_{z>1} pi(z)*min(Splus_d(z),Sminus_d(z)).
```

Set `D(y)=3y/[3U(y)+1]` when `U(y)>1`, and `D(y)=0` whenever
`U(y)=1`, including every positive preimage of one.
Then, exactly,

```
R_{d+1} = (2/3) R_d + I_d - C_d,
I_d = sum_{y>1} pi(y)*max(delta_d(y),0)*(D(y)-2/3).
```

Indeed `(a-b)_+=a-min(a,b)` for nonnegative `a,b`, while
`pi(U(y))*omega(y)/pi(y)=D(y)` by the actual equation `3y+1=2^e U(y)`.
The finite-grade inverse row bound makes the weighted series absolutely
convergent, so these rearrangements are legitimate. The target one has
no outward contribution to targets greater than one.

At exponent-one states `D-2/3` is negative, with numerator `-5` when
written over `3*(3U(y)+1)`. At every nonsink state with exponent at
least two it is positive. Thus the positive transport excess comes
from genuine longer divisions; `C_d` records actual opposing signs
arriving at the same target. Iteration gives

```
(3/2)^n R_n = R_0 + sum_{d=0}^{n-1} (3/2)^(d+1)*(I_d-C_d).
```

A polynomial upper bound on the right along an unbounded sequence is
exactly the desired exponential subsequence bound for this unmarked
component. For example an eventual bound
`I_d-C_d <= A*(d+1)^a*(2/3)^d` would suffice. **It is not proved.**
The separate marked component must still be handled; under exclusion
of nontrivial cycles, the existing narrow-band argument removes it.
The identity retains the original ordinary source correlations and
all visit multiplicities.

### Why a generic fixed-block norm contraction cannot fill the gap

For every fixed `L>=1`, the operator `K^L` is unbounded in the weighted
norm `||f||_pi=sum_{odd y>1} pi(y)*|f(y)|`, even on periodic signed tests
whose average over one additional ternary digit is zero. This is a
statement about the space of test functions, not a counterexample for
the particular sequence `delta_d`.

Choose any actual unit inverse word of grade `L-1` ending at five; let
its source be `b` and its clock `m0`. Such words exist at every grade by
the already checked capped-word construction. Append an arbitrarily
large admissible gap `e`, making `x=(2^e b-1)/3` a positive odd unit.
Admissible gaps recur modulo six, so `x` is unbounded. The complete word
has grade `L` and multiplier `w=3^L*2^(-m0-e)`.

For sufficiently large `k`, take the periodic test

```
f_k(n) = 1_{n=x mod 3^(k+1)} - 1_{n=x+3^k mod 3^(k+1)}.
```

Its two signed residue cylinders share a parent modulo `3^k`, and their
new-digit average is zero. On ordinary positive odd integers it tends
pointwise to the singleton indicator at `x`; domination by the summable
kernel gives `||f_k||_pi -> pi(x)`. Absolute convergence of the finite
grade row and determinism of the ordinary odd map give
`K^L f_k(5) -> w`. There is only one actual length-`L` odd word from
this `x` to five. The limiting ratio of just this output contribution
to the input norm is

```
pi(5)*w/pi(x) = pi(5)*3^L*2^(-m0)*b*x,
```

which is unbounded as `e` grows. Therefore a universal block estimate
based only on the current weighted norm and such digit cancellation
cannot bootstrap the polynomial mean estimate. A special estimate for
the actual transport excess minus actual opposite-sign cancellation
could still succeed.

## 3. The exact finite matching problem behind V_j

The finite statistic from [the original-rate theorem](../../research/astra-infinite-descent-20261127/escape/FINITE_ORIGINAL_RATE.md)
can be viewed as an ordered fractional matching problem, without
discarding the opposite-sign mass. At each retained target put grade
`j+1` mass in a positive list and grade `j` mass in a supply list.
Order their actual rational marks through `1/(j+1)`; collapse every
larger mark to one final bin, representing the unmarked total.

A positive mass in bin `i` may use supply in a bin no later than `i`.
The minimum unmatched positive mass is exactly the maximum of zero
and all cumulative positive-minus-supply deficits. Necessity follows
from each initial segment. For sufficiency, process bins in order,
retain all unused earlier supply, and match as much of the current
positive demand as possible. Whenever the running deficit reaches a
new maximum, precisely the increase is left unmatched; otherwise
earlier surplus covers the demand. Thus total unmatched mass is the
maximum cumulative deficit. The final bin includes the total-mass
condition.

After weighting by `pi(y)` and summing over targets, this minimum is
exactly `V_j`. This permits cancellation between different clocks and
different sources at the same target; requiring every displayed
gap-three pair to synchronize is stronger. The remaining target is
to certify a polynomial-times-`(2/3)^j` unmatched mass on an unbounded
sequence. Merely computing a finite number of these matching problems
does not establish that assertion.

## 4. Why the ordinary-source constructions do not supply induction

The finite-pattern/window theorem selects a source after the pattern,
modulus and relative width have been fixed. Its onset depends on those
choices. Here is a direct obstruction to identifying a selected source
with an arbitrary supplied `z`: to force a multiple `qz`, choose
`q=2^n>2`, residue zero, and window `[qz,q(z+1/2)]`. Its sole multiple
of `q` is `qz`, and halving `n` times would recover `z`. But the theorem
simultaneously places a source in every residue modulo `q`, while this
window has only `q/2+1<q` integer sites. It cannot meet the theorem's
onset at this width. A stronger single-residue assertion forcing that
very window would already entail the desired pointwise conclusion.

The three-odd-departure certificate has another visible short-gap
boundary. If `Y` is canonical and `(27Y+5)/4=2^g w`, then the last odd
step in the upper certificate writes `w=(2^a-1)/3`. Hence

```
Y = [2^(g+2+a)-2^(g+2)-15]/81.
```

The entire hard-parent form `z=(2^(m+7)-271)/81` is the slice
`g=6, a=m-1`. Obtaining descent for all sufficiently large intermediate
gaps therefore does not settle this family. The given source already
has the actual lower iterate `T^7(z)=2^m-1<z`, but that Mersenne iterate
does not belong to the canonical induction domain. A least defect in
the canonical reverse relation need not be a least ordinary
nonconvergent integer.

Prior work gives a stronger limitation on the special counted merger
architecture. [PR195's finite-family theorem](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md)
shows that the actual synchronized, augmented-grade classes in the
hard-parent progression are finite. Thus infinitely many class minima
have no earlier merger of that exact form within that progression,
even at unlimited clocks.
This is an attributed prior written result, not a fresh formalization
here. It does not rule out unequal-clock, unmatched-grade or pre-ascent
routes, and it does not locate such a minimum in the 192-input
cofactor-one sequence.

The certified return tables also do not close under their own outputs.
For the original 192 inputs, `J>=22` and `v_2(m+1)=J-2`, while every
tabulated gap `d` is below `2^18`. Hence for the earlier exponent
`t=m-d`, one has `v_2(t+1)=v_2(d)<=17`. Its new initial valuation is
at most 19, outside both the original `J>=22` batch and the thirteen
sharp classes with `J>=856`. Repeated application of these particular
tables is therefore unavailable.

The full formal reciprocal-mass equivalence remains an exact
universal target. Neither these deductions nor the final attempt
proves its small-mass side, the necessary signed estimate, or the
unrestricted absence of cycles.
