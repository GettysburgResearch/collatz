# Independent review of root recurrence and infinite subcritical pressure

**Verdict: VERIFIED WITH FIXES, at the exact final hash recorded
below.** The mathematical conclusions are a Haar almost-sure root-return
theorem, a finite-delay paired-descent theorem with zero upper Banach
failure density, null recurrence of the root class, and infinite
subcritical average inverse-fiber pressure for the specified full return
selection. They are not ordinary forward-five closure or Collatz.

Final subject: `AFFINE_SECTION_ROOT_RETURN.md`, SHA-256
`4079ef1361418368bb81e604b27cb59b02076f2c22c76b71ae9863ddb7619f94`.
The initially reviewed version had SHA-256
`2aecc794ae10765cc885baaf0c14951d0a3c7bd110e532dc6d9cf07be4ed9a66`.
The requested precision fix in R5.3 is incorporated in the final pin:
the prefix-free dictionary must use a selection decided by the bits
through its endpoint clock, rather than arbitrary longer lookahead.
The first odd-endpoint return and the strict-slope version satisfy this
condition. The general expectation statement R5.2 needs no such fix.

## Source checks and independent reconstruction

The reviewer read the source controller directly at PR146 full head
`66970775e4bdc945a68308e37a8eb028ebde42d2`,
`research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`, Section 1.
The reviewer also read PR167 full head
`e83cc8b35ad614c616df7c00318cc9645a174c34`,
`research/least-failure-closure-20261121/DENSITY_CONGESTION.md`, DC1--DC3.
Only their stated controller and finite-family inverse-fiber identity
are used. No review of the other theorems at those heads is implied.

The Foster premise was separately reconstructed in
`REVIEW_AFFINE_SECTION_RECURRENCE.md`. This companion review checks the
controller, the repeated-trial deduction, the density passage, the
stopped-martingale argument, the exponential tail estimate, and all
normalizations in the finite-family pressure limit. It does not claim
execution of the author's separate full checker.

## 1. The controller and almost-sure return deduction

Putting `D=3^max(0,-k)*c` in S1 gives exactly R2. Its exponents are
nonnegative in all four parity cases. For nonzero k, at most two chosen
bits make D odd, using the exact valuation of
`3^k_minus-5*3^k_plus`; one more bit then lowers `|k|`. Thus level zero
is reached in at most `3|k|` bits.

At level zero and odd D, the proposed excursion returns with
`D'=(f+1)/2`, where f is the signed odd part of `(3D-5)/2`. The stated
inequalities imply strict decrease of `|D|` whenever `|D|>3`.
The small values `1,-1,3` reach zero or one, and direct substitution in
R2 confirms the seven-bit path from `D=-3`. Even offsets halve. This
is a well-founded deterministic proof of accessibility, for a freely
selected continuation. It does not prescribe the already fixed higher
bits of an ordinary source.

The finite core from Theorem S admits a finite collection of such words.
Padding with zero bits after reaching the root makes all lengths equal
to some finite L. At each core visit the success probability is at least
`2^-L`. Failed trials can be followed by another almost-surely finite
wait to the core. The conditional failure probability through m trials
is at most `(1-2^-L)^m`. This proves root hitting from every state and,
by conditioning at each deterministic time, infinitely many root visits.
No irreducibility or independence between trials is assumed here.

An odd endpoint can be selected almost surely: while the next source
bit is zero, a root state persists. The next one bit arrives almost
surely, and its starting clock is an odd-source root visit. Repeating
after deterministic delays gives arbitrarily late odd-endpoint returns.

## 2. Strict descent and zero upper Banach density

The source parity strong law gives `3^p_h/2^h -> 0`. Along the arbitrarily
late odd-endpoint root visits, the slope is therefore eventually less
than any specified `theta/2`. Each accepted finite cylinder gives an
ordinary formula `q=(3^p*x+B)/2^h`, with B nonnegative. Its positive
ordinary lifts satisfy `q<theta*x` beyond a finite height threshold.

Approximating the probability-one union by finitely many such cylinders
is sufficient for the uniform interval-density claim. Refine the finite
union to one binary period and impose the independent ternary-unit
restriction. Periodic counting has a bounded error uniform in interval
position. The finitely many ordinary points deleted by the height
thresholds also have a bounded error. Letting the finite union's mass
approach one proves zero upper Banach density of failures for each fixed
theta and delay. No quantitative rate or countable-intersection claim
is supplied.

## 3. Infinite expected return time

Under odd initial input the first transition is from the root to
`(0,-2)`. The next carry is either `-1` or `-5`, so at least one active
martingale increment must occur before hitting the root. If its hitting
time tau had finite expectation, the bounded-increment stopped k-process
would be Cauchy in L2: its tail second moment is at most
`E(tau-n)_+ -> 0`. Its terminal value is zero, but the martingale
second-moment identity would give

\[
0=\mathbb E k_\tau^2
=\mathbb E\sum_{t<\tau}{\bf1}_{c_t\text{ odd}}\ge1.
\]

This contradiction proves infinite expected return. The half-probability
odd branch makes the unconditioned positive root return have infinite
expectation as well. This establishes null recurrence of the root's
reachable communicating class; it does not assert finite mean renewal.

## 4. Infinite inverse-slope moment

For any almost-surely finite positive root-return choice sigma, including
one which looks at endpoint parity, `E sigma=infinity` by pointwise
domination of the first positive return. For t>=1 under odd initial input,

\[
\mathbb E2^{p_t}=\frac43(3/2)^t,
\qquad
\Pr(p_t\ge3t/5)\le\frac43\alpha^t,
\quad\alpha^5=243/256<1.
\]

Summing over the event `sigma=t` bounds the expectation of sigma on the
high-odd-count event by `(4/3) sum t alpha^t`, a finite number. This uses
only event containment, so endpoint lookahead creates no stopping-time
gap. On its complement,

\[
\log(2^\sigma/3^{p_\sigma})
>\frac\sigma5\log(32/27)>0.
\]

The positive log has infinite expectation, and exponentiating gives
infinite expectation of `(2^sigma/3^p_sigma)^(1-s)` for every `0<s<1`.
No independence of the selection rule and its parity counts is used.

## 5. The prefix and endpoint normalization

For the dictionary application use a choice determined by the parity
bits at clocks `0,...,L`, with its endpoint bit equal to one. These are
L+1 specified bits; conditional on odd initial input their cylinder mass
is exactly `2^-L`. The first successful odd-endpoint root return, with
or without the strict-slope condition, has this property and is
prefix-free. A rule reading additional future bits would generally
have smaller cylinders and must not be assigned the same mass.

For each dictionary word the inverse source is
`x_w(q)=(2^L*q-B)/3^p`, with p>=1, B>0 and B prime to three.
Integrality selects one unit residue modulo `3^p`. Exactly two of its
three lifts modulo `3^(p+1)` give a ternary-unit source. Relative to all
unit endpoint classes this fraction is `3^-p`. Consequently its mean
limiting kernel contribution is

\[
3^{-p}(3^p/2^L)^s
=2^{-L}(2^L/3^p)^{1-s}.
\]

Finite sums give R9 with no infinite averaging interchange. At s=1,
the increasing sums approach total dictionary mass one. At `0<s<1`,
the inverse-slope moment just proved makes their supremum infinite.
Thus a uniform column bound outside a fixed finite endpoint set must
be at least one at s=1 and cannot be finite at subcritical exponents.
Removing finite ordinary source exceptions from each fixed finite
subdictionary does not change these limits.

This does not prove divergence of the energy of any actual invariant
label, whose defect support is constrained and may vanish at all the
large-pressure endpoints. The distinction is preserved in the note.

## Final scope

The verified synthesis supplies exact probabilistic recurrence, an
ordinary finite-delay density theorem, and a limitation of the full
positive return kernel. A prescribed ordinary certificate has a fixed
eventually periodic source tail; the controller may not replace it with
fresh random bits. In fact every certified source has finitely many root
returns, as proved in the companion review. No deterministic mechanism
that excludes every remaining ordinary failed five-comparison is supplied.
