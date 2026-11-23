# Independent narrow review: unconditional cycle and escape boundary

23 November 2026.

Reviewed file:
`/workspace/scratch/957bb0caa6f2/risk26/root/UNCONDITIONAL_CYCLE_BOUNDARY.md`

Reviewed SHA-256:
`0e747ae8121a434d4ec99b0457cd3bf3202d9e8b0bec35e48b7070143e488d65`

**Verdict: VERIFIED at written-proof scope for UB2--UB6 and
UB8--UB11.** The conclusion is restricted to these exact bytes and
claims. The primary arithmetic gcd problem remains open. No Lean
verification or new audit of the full PR180 operator construction is
claimed.

## 1. Actual scope of the counting input

I independently opened PR182
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, Sections
1--6. Its theorem quantifies over every forward-invariant set of
positive odd integers on which the odd map is injective. Section 1
explicitly includes the union of all positive odd periodic points.

The proof itself has that scope. It advances every charged source by
one shared number of odd transitions. Injectivity of that same iterate
charges the high binary-clock sources to a smaller part of the same
set, and the low binary-clock sources are counted by their exact parity
cylinders. No single-component, single-orbit, or finite-period premise
appears in that argument. The dyadic scale iteration has an absolute
constant independent of the set.

On the union of all positive periodic states, the odd map is a
permutation. Distinct cycles cannot share a state, and each periodic
state has exactly one periodic predecessor. The same facts hold for
the subunion of complete cycles whose minima are at least a fixed real
`M>=1`. Removing low-minimum cycles removes them in their entirety,
so forward invariance is preserved.

## 2. UB2--UB3: simultaneous defect budget and floor tail

The logarithmic product identity UB2 follows from multiplying the actual
odd transition equations on each finite cycle. All summands are positive.
Counting each primitive cycle once counts every periodic odd state once.

For the indicated subunion `S`, every element is at least `M`; hence

`sum_(x in S) 1/x = integral_M^infinity F_S(t)/t^2 dt`

holds by Tonelli, including a possible state exactly equal to `M`.
The integral bound uses
`sqrt(1+log t)>=sqrt(1+log M)` and integrates `t^(theta-2)`.
It gives exactly the displayed constant `C/[3(1-theta)]` and the
displayed floor tail. At `M=1` it gives a finite absolute total budget.
No predecessor-density assumption is required.

## 3. UB4--UB6: product, zeros, and tail estimate

For each cycle, `beta_c` is the real-parameter disk automorphism
`(a-z)/(1-az)` evaluated at `z=w^(A_c)`, so it maps the disk into
itself. Direct subtraction yields

`1-beta_c(w)=(1-a_c)(1+w^(A_c))/(1-a_c w^(A_c))`.

The inequalities in UB4 follow from `1-exp(-delta)<=delta`,
`A_c>=1`, and `|w|<=r<1`. The total defect budget consequently
gives a summable sequence of uniform factor errors on every compact
subdisk. The infinite product converges normally. Its value at zero is
the nonzero quantity `exp(-sum delta_c)`, so it is not identically zero.

At a fixed nonzero point `w` in the disk, any vanishing group satisfies
`delta_c=-A_c log|w|>=-log|w|>0`. Only finitely many groups can do so.
The remaining nonzero factors have a convergent nonzero product.
Every zero of one group is simple; at overlaps the multiplicities add.
At `w=0` there are no group zeros.

There are finitely many cycles with minimum less than `M`, since their
distinct integer minima lie in a finite set. The finite-product
telescoping bound uses only that every factor has modulus at most one.
Passing to the normally convergent product gives UB6 with the exact
tail sum from UB3. The note correctly distinguishes this mathematical
finite product from an algorithm deciding periodicity below `M`.

## 4. UB8--UB11: one unchanged escaping ordinary source

On a nonperiodic forward odd orbit, all states are distinct; its range
and every future ray satisfy the same injective-set hypothesis. Their
minimum exists by well-ordering. The future minima tend to infinity:
an injective positive-integer sequence visits each finite height set
only finitely many times.

Both recurrences in UB8 follow directly from the same actual transition
equation. The positive product is bounded using the reciprocal moment,
so its limit is finite and larger than the initial source. Telescoping
gives exactly the positive scalar series in UB9.

For an odd initial source, the odd shortcut times are precisely `A_i`,
and the corresponding odd counts after that step are `i+1`. Thus the
nonzero terms of the stated shortcut forcing series at two coincide
with the odd-clock summands in UB9; no clock change loses a term.

The rational partial sum equals `E_i-n`. Since `x_i` and `3^i` are
two-adic units and `A_i>=i`, its correction `E_i` tends to zero
two-adically. The two-adic limit is therefore `-n`, as stated. Its
positive real limit is not the same equality in the real field. The
note explicitly preserves the distinction and does not assert a
contradiction between completions.

Finally the tail product beginning at `i` is bounded by
`exp(L(M_i))` using the future ray. Multiplication by the same `E_i`
gives UB11. No effective rate in the time index is inferred from the
floor tail.

## 5. Import and non-claims

UB7 is a valid local analytic implication **given** the separately
pinned PR180 classification of the operator-norm resolvent's poles as
simple cycle poles: multiplication by an analytic zero removes each
such pole. I did not rereview that full operator theorem here.

Section 5's external adelic theorem statements were outside this narrow
review request. Their citation does not acquire a new review from this
report.

The verified result removes the predecessor-density assumption from the
all-cycle defect budget and the grouped product construction. It does
not show that any unknown cycle is absent, bound the number of cycles,
solve the complete numerical gcd problem, or glue the two scalar
completions. These limits are correctly stated in the reviewed note.


## Metadata-only binding addendum

23 November 2026. The source is now SHA-256
`8e9c1d89a7cb797b9a880c35e1f9dddcc7ad0e670ff51bd3ee49fbddbafa35cd`.
The sole change is the source-table citation for
`CYCLE_RESOLVENT_BRIDGE.md`, from Sections 1--5 to Sections 1--4.
An exact byte comparison was performed: reversing only that range
correction reproduces the previously reviewed SHA-256
`0e747ae8121a434d4ec99b0457cd3bf3202d9e8b0bec35e48b7070143e488d65`.
The mathematics is unchanged, so the existing narrow review verdict
and its stated scope also bind the new source hash. No proof was
re-reviewed and no mathematical or computational checks were rerun.
