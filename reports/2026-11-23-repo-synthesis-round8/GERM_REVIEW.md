# Independent review of the actual center-one scalar and candidate budget

23 November 2026. Reviewer lane: `pressure_construction8`.

**Verdict: VERIFIED at the written elementary claim level for
R8-G1--R8-G4, with the formalization and global construction boundaries
retained. No mathematical correction was required.**

The reviewed source is the round-eight child of PR182 parent
`3954c775ba74e1f40776ff38cb4282698d4a334a`. These local source blobs
identify the exact versions reviewed; the parent publication receipt
supplies the final containing commit.

| Path under `research/repo-synthesis-round8-20261123/` | Git blob | Scope |
| --- | --- | --- |
| `GERM_BRIDGE.md` | `540110f09cf68e3309fd83fea9c7ae497536ded4` | R8-G1--R8-G4 and their stated boundaries |
| `germ_bridge_controls.py` | `5d4d09073d4ad088807d77543de5f5e437111403` | Actual candidate implementation and finite controls |
| `GermBridge.lean` | `d6a9d41f6fc348ab6ed636645e2711ae7f95615d` | Statement inspection of six finite arithmetic lemmas |

This review reconstructs the mathematics and independently checks the
candidate boundaries. It does not claim that a repository check or the
finite Lean module proves the infinite scalar's arithmetic type.

## 1. R8-G1: actual real construction, bounds, and strict endpoint

The full accelerated equation is `2^g_i q_(i+1)=3q_i+1`, with the
literal positive ordinary q_i and `g_i>=1`. Multiplying its elementary
upper bounds gives `2^A_m q_m<=4^m q_0`, hence
`A_m<=2m+log_2 q_0`. This proves convergence of the positive discounted
gap series independently of eventual convergence of the Collatz orbit.

Direct summation by parts gives

`h(q)=(2/3) sum_(m>=1) A_m/3^m`.

The two geometric sums then give `h(q)<=1+log_2(q)/3`, with the stated
constants. The recurrence `h(Uq)=3h(q)-g_0` follows by shifting the
same absolutely convergent series, not by defining a different scalar.

The endpoint is strictly greater than one half. If equality held,
positivity of every term in `sum (g_i-1)/3^(i+1)` would make every
gap one. Iterating `q_(i+1)+1=(3/2)(q_i+1)` would imply that every
power of two divides the fixed positive integer `q+1`. This rules out
the only equality case for a positive ordinary source. The strict
endpoint is needed for the denominator-two phase analysis elsewhere.

The finite enclosure uses exactly the actual tail state q_N. Its
upper bit-length bound follows from `log_2 q_N<bl(q_N)` and is
deliberately slightly loose. Since `q_N<=2^N q_0`, its width tends to
zero effectively. This does not supply a precision at which a rational
representation can be inferred from an approximation.

## 2. Actual derivative and even-source normalization

The odd positions of the shortcut parity series are exactly A_i.
Thus `B_q(z)=sum z^A_i/3^(i+1)`. For `1<=|z|<sqrt(3)`, the bound on
A_i gives a convergent geometric majorant; for `|z|<1`, the original
geometric coefficient bound suffices. Termwise differentiation at one
is therefore justified. The summation-by-parts identity above gives
`2B'_q(1)=h(q)` and `B_q(1)=1/2`.

For an arbitrary positive ordinary `n=2^b q`, q odd, the initial b
even shortcut steps shift the same series by `z^b`. Differentiation
therefore gives `H(n)=b+h(q)`. The displayed shortcut recurrence
`H(Tn)=3^e H(n)-1` follows in both parity cases; its odd case uses
the complete gap g, including the first binary division of the
shortcut step. No clock is silently changed.

The source q=1 has all odd gaps equal to two, so `h(1)=1` and
`B_1(z)=1/(3-z^2)`. For powers of two, `H(2^b)=b+1` and the first
hit of one occurs after exactly b shortcut transitions.

## 3. R8-G2: triadic equivalence

If q reaches one, its complete finite discounted prefix plus the
standard tail `h(1)=1` is triadic. In the converse direction, after r
actual odd steps a value `a/3^r` becomes an integer. The strict lower
bound then makes the actual tail scalar at least one, and the
recurrence preserves integrality.

The potential `R=q/2^h` satisfies the exact step ratio
`R'/R=(3+1/q)/4^h`. An odd ordinary source avoiding one is at least
three, so the integer-stage ratio is at most `5/6`. Meanwhile the
unconditional upper scalar bound gives `R>=q^(2/3)/2>=1/2`. An infinite
integer-stage tail is impossible. The even-source formula above
preserves membership in `Z[1/3]` by subtracting the integer b.

This establishes the stated equivalence, without constructing a
successful numerator or denominator exponent for an arbitrary source.
No claim of arbitrary rationality or uniform contraction for all
positive real scalar values is used.

## 4. R8-G3: complete polynomial contraction

Independently substitute `a=2^h`, `b=2^g`, `c=2^(h')`. The exact
scalar and ordinary equations give `bc=a^3` and `bq'=3q+1`.
Cross-multiplication of the desired potential inequality yields

`E=3(q-1)(a^3-b)-4(3q+1-b)(a-1)>=0`.

The coefficient of q is `3a^3-3b-12a+12`. Since `2b<=a^3`, it is
at least `(3/2)(a-2)(a^2+2a-4)>=0`; q can be reduced to three.
The resulting expression is
`6a^3-40a+40+b(4a-10)`. At a=2 it is `8-2b>=0`, using b<=4.
Otherwise the integral a is at least three, so replacing b by two
is valid and leaves
`6a^3-32a+20=(a-2)(6a^2+12a-8)+4>0`.

The complete powers and quotient are retained in this proof. It is
precisely the `3/4` contraction of `(q-1)/(2^h-1)` when both scalar
charges are positive integers. The inspected Lean statements match
these finite hypotheses. Compilation and declaration-dependency audit
are recorded by the executing parent, not asserted as an independent
compiler run in this review.

## 5. R8-G4: total candidate decision and every boundary case

The source candidate is exactly `a/3^r`, not a rounded real scalar.
The implementation checks q=1 before applying nonterminal bounds.
It accepts there precisely when the transported candidate is one.
Reversing the finite recurrence proves acceptance equivalent to the
initial candidate equality. Either failed guard is incompatible with
the actual scalar bounds, so rejection concerns that candidate only.

After r transitions a surviving candidate is integral. The lower guard
`2t>=1` makes it at least one. At a nonterminal odd source its bit
length B is at least two. The upper guard `3t<=B+3` implies
`t<=B-1`: for B=2 integrality gives t<=1; for B>=3 the real bound is
already at most B-1. Therefore `2^t-1<=q-1` and the surviving
potential is at least one.

At step r, `q_r<=2^r q_0<2^(r+B_0)` and the positive integral
potential is strictly below q_r. Another `3(r+B_0)` transitions would
contract it below one, because `(3/4)^3=27/64<1/2`. Thus a hit or
guard rejection occurs by

`r+3(r+B_0)=4r+3B_0`.

This argument includes r=0 and unreduced representations. Increasing r
only delays the certified integral stage and increases the safe budget.
The loop visits clocks zero through K inclusively, so a hit or guard
failure exactly at K is handled before its impossible-budget exception.

At q=1 the endpoint test gives the correct zero-transition decision,
including for incorrect, negative, and zero candidates. No claim
`t<=B-1` is applied there. For even n, subtracting b from the candidate
for H(n) retains the same denominator `3^r`, possibly unreduced, and
uses the same odd-source recognizer.

For a correct candidate, the total odd binary clock obeys
`A_N<=2N+floor(log_2 q)`. Since `N<=4r+3bl(q)`, adding the initial b
even transitions gives exactly the claimed upper bound
`b+8r+7bl(q)-1`. This includes q=1 and b=0; it is a safe upper bound,
not an assertion that every candidate uses its full budget.

## 6. Execution evidence and scope

The reviewed `germ_bridge_controls.py` was executed under `python -O`
through its `run_checks()` entry point. It returned PASS with 31,334
exact checks, 140 explicitly convergent odd sources, 2,715 literal odd
transitions, 1,812 candidate decisions, and 1,967 additional polynomial
cases. Its maximum candidate run used 195 odd transitions. The checks
are ordinary conditional failures, so optimization does not erase them.

A separate review replay used division by two to recompute every
literal gap for all 64 odd sources from 1 through 127. It computed the
oracle scalar from the forward discounted prefix plus the exact tail
at one, independently of the source script's reverse recursion. This
gave 576 checks of true and adjacent candidates at the reduced
denominator exponent and at two unreduced exponents; 256 checks of
negative, zero, and very large integral candidates; and 832 even-source
checks with initial binary exponents zero through twelve. The latter
replayed the literal shortcut map and checked both the exact clock
`b+sum(gaps)` and the advertised shortcut bound.

All 1,664 independent boundary checks passed. The maximum candidate
run in that replay was 43 odd transitions, and the maximum shortcut
run was 87 transitions. These finite executions verify the recorded
domains only; the uniform budget rests on the reconstructed proof.

**Remaining global obligation:** construct membership of the actual
scalar in `Z[1/3]` for every fixed positive ordinary source, or another
actual arithmetic condition strong enough to close the remaining
phase classes. Effective approximation and total recognition of a
supplied candidate do not supply that construction.
