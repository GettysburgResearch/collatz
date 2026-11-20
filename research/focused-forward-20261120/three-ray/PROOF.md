# Three-ray guards and expanding return schedules

**Status: PROPOSED, unconditional written proofs with bounded exact replay.**
All states in statements about the dynamics are positive ordinary integers.
The shortcut map and independent-clock meeting relation are defined in
[README.md](README.md). Put `C(n) := (n ~ 3n)`.

The external source pin is `(PR #146,
561d48a4d3a793a59b1cdf0406062ae1a6d47515,
research/upper-bit-mergers/THREE_RAY.md)`. Its equivalence between universal
`C(n)` and Collatz is motivation, not an assumption of these proofs.

## TR-001: when a pointwise merger extends to a binary cylinder

For a start `n` known to reach 1, let `tau(n)` be its first-arrival clock,
`q(n)` its number of odd inputs before that arrival, and

\[
                         g(n)=2q(n)-\tau(n).
\]

Assume both `n` and `3n` reach 1. Then fixed words provide an identity

\[
                         T^p(x)=T^q(3x)                         \tag{1}
\]

on a binary residue class containing `n`, for every positive lift in that
class, if and only if

\[
                         g(n)-g(3n)=2.                         \tag{2}
\]

Here the words and clocks are fixed across the class. A pointwise merger
whose words can change with `x` is a different assertion.

**Proof.** On prescribed parity words, the two sides of (1) have slopes
`3^a/2^p` and `3^(b+1)/2^q`, where `a,b` count their odd inputs. Equality on
an infinite binary class forces `p=q` and `a=b+1`. Splitting a path at any
clock `h` gives

\[
                 g(z)=2s_h(z)-h+g(T^h(z)).                     \tag{3}
\]

This remains true after first arrival because a lap `1 -> 2 -> 1` has two
steps and one odd input. Apply (3) at the common endpoint to obtain (2).

Conversely, (2) implies that the first-arrival clocks have the same parity.
At any common clock after both arrivals, the endpoints on `1 -> 2 -> 1`
therefore coincide. Equation (3) says their odd counts differ by exactly
one. Choose such a clock `h`. The inputs `x` and `3x` have the same length
`h` parity words as `n` and `3n` whenever `x == n (mod 2^h)`.
The affine slopes agree, and agreement at `n` forces the constant terms to
agree. This proves (1) throughout that class.

For example, `g(1)=0`, `g(3)=-1`, and `g(5)=g(15)=-2`. Thus `(1,3)` and
`(5,15)` meet as actual ordinary pairs but have no uniform fixed-word
certificate of this form on any binary neighborhood. The same holds after
doubling both inputs any number of times, since doubling decreases each
grade by one. This is an explicit obstruction to replacing pointwise
meeting by a fixed cylinder certificate.

The grade identity overlaps FB-001 at PR #148's prior content commit
`4312e70370a89e474bc8812734760c7de9798315`,
`research/forward-bridge-20261120/PROOF.md`. The application to slopes in
the `(n,3n)` family is reconstructed above.

## TR-002: exact ray-to-ray pullbacks preserve the odd part

Suppose positive integers `u,m` and clocks `p,q>=0` satisfy

\[
                         T^p(u)=m,\qquad T^q(3u)=3m.            \tag{4}
\]

Then `u=2^q m`. Also `p=q`, or `p>q` and `T^(p-q)(m)=m`.
In particular (4) cannot produce a new odd part for a three-ray failure.
No equality of the two clocks or odd counts is assumed.

**Proof.** After one odd step, an orbit is a unit modulo 3, and remains a
unit after every subsequent step. Since the upper endpoint `3m` is
divisible by 3, its entire length `q` path contains only even steps. Hence
`3u=2^q 3m`. For `p<q`, the lower path is still in that initial halving run,
and has value `2^(q-p)m>m`. For `p=q` it reaches `m`; for `p>q` the rest of
the lower path is a periodic return to `m`. This proves all assertions.

This does not prohibit pullbacks with offset intermediate endpoints or
other, more general physical merger diagrams.

## TR-003: ordinary guarded returns

Let

\[
 n=2^k u-1,\qquad k\ge3,\quad u\ge1\text{ odd},\qquad
 R=3^{k-1}u.
\]

The first path has `k` initial odd steps. On the second path, the first
three steps send `3n` to `9*2^(k-3)u-1`; the remaining `k-3` initial odd
steps give

\[
                       T^k(n)=3R-1,\qquad T^k(3n)=R-1.       \tag{5}
\]

The expression is valid also at `k=3`, when there are no remaining steps.

### Immediate merger

If `R == 3 (mod 4)`, both arms in (5) meet after two more steps, at
`(3R-1)/4`. Thus `C(n)` is proved by a physical common-clock certificate.

### Odd-valuation return

If `R == 1 (mod 4)`, put `v=(R-1)/4`. Two more steps give

\[
                     T^{k+2}(n)=9v+2,\qquad T^{k+2}(3n)=v.  \tag{6}
\]

Suppose the valuation of `v` is odd:

\[
                         v=2^{2r+1}m,\quad r\ge0,\quad m>0\text{ odd}.
\]

The upper arm in (6) reaches `m` after `2r+1` halvings. The lower arm first
halves to `9*4^r m+1`, takes `2r` steps to `3^(r+2)m+1`, and halves once
more to `T(3^(r+1)m)`. Therefore

\[
                         C(n)\quad\Longleftrightarrow\quad
                         m\sim3^{r+1}m.                     \tag{7}
\]

These are actual ordinary paths. The two comparison clocks are
`k+4+2r` and `k+3+2r`; (7) then removes one forward step from the first
endpoint using the meeting equivalence relation.

Consequently, whenever `3^r m<n`, the finite list

\[
                  C(m),C(3m),\ldots,C(3^r m)                 \tag{8}
\]

consists entirely of smaller-input obligations and implies `C(n)` by
transitivity. Condition `3^r m<n` is an exact arithmetic guard, not an
estimate assumed to hold universally.

For `r=0`, the guard is `R == 9 (mod 16)` and (7) becomes

\[
             C(n)\Longleftrightarrow C(m),\qquad
             m=\frac{3^{k-1}u-1}{8}.                        \tag{9}
\]

For `3<=k<=7`, `m<n`: indeed
`8(n-m)=(2^(k+3)-3^(k-1))u-7`, whose right side is positive in each of
those five cases. For `k>=8`, `3^(k-1)>2^(k+3)`, so **every** guarded
return (9) strictly increases the input. For the more general (7), the
largest required input `3^r m` is `(3/4)^r` times the value in (9).
In particular (8) also descends for all `3<=k<=7` whenever that valuation
guard holds.

### No rank using only size and the next valuation

For any specified `k>=3` and `k'>=1`, choose a positive odd `u` in the
binary class

\[
 3^{k-1}u+7\equiv2^{k'+3}\pmod {2^{k'+4}}.                  \tag{10}
\]

It exists because `3^(k-1)` is odd. Equation (10) implies the guard in
(9), and the returned value has `v_2(m+1)=k'`. Thus `k'=k` is possible
at every `k>=8`, where `m>n`. No function

\[
                         \log n+\alpha v_2(n+1)
\]

with fixed real `alpha` strictly decreases along all returns (9).
This does not refute ranks with additional state or different guards.

### Exact boundary

If `R == 1 (mod 4)` and `v_2(v)` is even, (7) does not apply. If it is
odd but the guard `3^r m<n` fails, (8) need not descend. These ordinary
classes remain unresolved by this selector. Repeated expansion within
the special return (9) is addressed next, but not universally excluded.

## TR-004: fixed blocks, aperiodicity and complexity

Consider actual consecutive returns (9), and write

\[
 x_i=n_i+1=2^{k_i}u_i,\qquad
 x_{i+1}=a_{k_i}x_i+\frac78,\qquad
 a_k=\frac{3^{k-1}}{2^{k+3}}.                               \tag{11}
\]

All `x_i` are positive ordinary integers and their displayed valuations
are exact. Restrict this section to **expanding returns**, `k_i>=8`.
Since `a_k>1`, their `x_i` strictly increase.

### Constant valuation

For a constant `k`, put `p=3^(k-1)`, `q=2^(k+3)` and `d=p-q>0`.
The odd parts obey

\[
 u_{i+1}=\frac{p u_i+7}{q},\qquad
 d u_{i+1}+7=\frac pq(d u_i+7).
\]

If `r` successive returns retain this same valuation, then

\[
 2q^r\mid d u_0+7,\qquad
 r\le\left\lfloor\frac{v_2(d u_0+7)-1}{k+3}\right\rfloor.  \tag{12}
\]

The divisibility follows because every `d u_r+7` is an even integer and
`p` is odd. Its positive right-hand integer is nonzero, so an infinite
constant-valuation run is impossible. The bound in (12) is the exact
maximum number of successive same-valuation returns, by the sufficiency
argument below.

Nevertheless every finite length `r` is realized by a positive ordinary
source: choose a positive odd `u_0` satisfying
`d u_0+7 == 0 (mod 2q^r)`. Then all intermediate `u_i` are positive odd
integers, and each is in the guard (9). To check integrality, the identity
above gives an integer value for `d u_i+7`, and reduction modulo `d`
shows that its value is `7 (mod d)` because `p == q (mod d)` and `q` is
invertible modulo the odd number `d`. Hence `u_i` is integral. Positivity
also follows directly from the affine recurrence.

The fixed completion is `u=-7/d`, a negative rational. Changing the
positive witness with `r` does not produce one positive witness for all
depths.

### Any fixed periodic block

Take a block `k_0,...,k_(s-1)` with every `k_i>=8`. Its composition has
the form

\[
 B(x)=\frac{P x+C}{Q},\qquad
 P=3^{\sum_i(k_i-1)},\quad Q=2^{\sum_i(k_i+3)},\quad C>0
 \text{ an integer}.                                      \tag{13}
\]

Indeed one step is `(3^(k-1)x+7*2^k)/2^(k+3)`, so composition preserves
integer coefficients. We have `P>Q`, and `P` is odd. With
`D(x)=(P-Q)x+C`,

\[
                         D(B(x))=\frac P Q D(x).
\]

If this same block is physically repeated `r` times from `x_0`, then

\[
 Q^r\mid D(x_0),\qquad
 r\le \left\lfloor
       \frac{v_2((P-Q)x_0+C)}{\sum_i(k_i+3)}\right\rfloor.   \tag{14}
\]

Its numerator is a fixed positive integer. Thus an expanding guarded
run cannot have an eventually periodic valuation schedule. This is not
an exclusion of an aperiodic schedule, bounded or unbounded.

There is also an exact maximum for a prescribed block. Set `k_s=k_0`
and compose the odd-part maps

\[
 u_{i+1}=\frac{3^{k_i-1}u_i+7}{2^{k_{i+1}+3}}.
\]

One block is `F(u)=(P u+C_u)/Q`, with the same `P,Q` as in (13) and an
odd positive integer `C_u`. Let `d=P-Q>0`. Starting with a specified odd
`u_0>0`, the first `r` full prescribed repetitions are legal if and only if

\[
                 v_2(d u_0+C_u)\ge r\log_2 Q+1.             \tag{14a}
\]

Thus their maximum number is exactly

\[
           \left\lfloor\frac{v_2(d u_0+C_u)-1}{\log_2 Q}\right\rfloor.
                                                                    \tag{14b}
\]

Necessity is the evenness of `d u_r+C_u` and the identity
`d F(u)+C_u=(P/Q)(d u+C_u)`. For sufficiency, (14a) makes
`P^r(d u_0+C_u)/Q^r` an even integer. Since `P == Q (mod d)` and `Q`
is invertible modulo `d`, this integer is `C_u (mod d)`. The resulting
endpoint `u_r` is therefore an odd integer. Every intermediate odd-part
expression has a denominator that is a power of 2. A nonintegral such
expression can never become integral under `(p u+7)/q` with `p` odd and
`q` a power of 2: its odd numerator stays odd and its denominator grows.
Final integrality therefore forces integrality at every earlier stage.
Each earlier input is odd because its numerator must be divisible by its
even denominator; positivity follows from the positive affine recurrences.
These facts give the exact displayed valuations and the guards (9) at
every stage. This proves sufficiency and the claimed maximum.

### Every finite valuation schedule is ordinarily realizable

Given any finite list `k_0,...,k_L>=3`, there is a positive ordinary source
whose first `L` guarded returns (9) have precisely these valuations,
including `k_L` at the endpoint. Compose the odd-part expressions above
to `(P u_0+C)/Q`. Here `P` and `C` are odd, `Q` is a power of 2, and
`C>0`. Choose the unique odd residue

\[
                     u_0\equiv P^{-1}(Q-C)\pmod {2Q}.
\]

Its least positive representative makes the last odd part a positive odd
integer. The denominator argument in the preceding paragraph makes all
intermediate odd parts positive odd integers as well. Hence each specified
valuation and physical guard holds. The case `L=0` is immediate from any
positive odd `u_0`.

In particular there is no forbidden finite word in the expanding valuation
alphabet `{8,9,...}`. This statement allows the source to change with the
chosen finite word. It supplies no fixed ordinary source for an infinite
schedule, and cannot be used as an all-time escape construction.

### Bounded alphabets require substantial factor complexity

Suppose an infinite expanding run has `8<=k_i<=K`. Put

\[
 A=a_K>1,\qquad C_0=x_0+\frac{7}{8(A-1)}.
\]

Equation (11) gives `x_j<=A^j C_0`. If two equal blocks of length `L`
start at positions `i<j`, their affine composition (13) is identical.
Subtracting its two integer outputs gives

\[
                 Q\mid x_j-x_i,\qquad Q\ge2^{11L}.          \tag{15}
\]

The difference is positive because the run strictly increases. Therefore

\[
              j\ge\frac{11L-\log_2 C_0}{\log_2 A}.          \tag{16}
\]

All length-`L` blocks starting strictly before the right side of (16)
are consequently distinct. If `p(L)` is the factor complexity of this
infinite valuation sequence, then

\[
 p(L)\ge\max\left(0,
    \left\lceil\frac{11L-\log_2 C_0}{\log_2 A}\right\rceil\right),
 \qquad
 \liminf_{L\to\infty}\frac{p(L)}L\ge\frac{11}{\log_2 A}.    \tag{17}
\]

For `K=9`, the coefficient is about `16.18`; for `K=10`, about `8.70`.
The statement is conditional on a bounded-alphabet infinite expanding
run. Aperiodic sequences can have this or greater complexity, so (17)
does not rule them out. It also makes no claim about the classes outside
the return guard or about a run using unbounded valuations.

## What remains open

These arguments do not establish `C(n)` for every fixed ordinary `n`.
The exact finite paths give a partial selector. Closing it would require
a well-founded descent or a genuine all-time ordinary exclusion covering
the remaining residue classes and every variable expanding return schedule.
Finite successful extensions, negative rational fixed completions, and
periodic-block exclusions do not provide that missing theorem.
