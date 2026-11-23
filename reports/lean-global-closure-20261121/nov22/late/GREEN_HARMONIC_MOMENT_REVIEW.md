# Independent review: canonical Green deficit harmonic moments

Date: 2026-11-22. Reviewer: `global_certificate22`.

## Exact scope and verdict

Reviewed `LATE_GREEN_HARMONIC_MOMENT.md` at SHA256
`216e2cb719c0c558a69d7167705f0e0c3866aaa38d0b24f08dbe23226020e79b`.
This final version adds the explicit repository odd-unit domain to the
five-energy definition. I inspected that clarification; the estimates and
arguments reviewed at the preceding hash
`286149ba27f0505bf2eeaf2542bae34dc9ed88c2349b6e802689c1f7ac1870be`
are unchanged.

**Verdict: VERIFIED as a written deduction under the displayed frozen
harmonic-flow, whole-predecessor-floor, and finite-orbit-count inputs.**
I independently reconstructed the distribution estimate, all constants
in the moment and occupation bounds, the extension to ordinary integers,
the Cesaro/Abel assertions, and the future-minimum counterexample. No
substantive correction is required at this source version.

This verdict does not independently establish the upstream analytic
construction of `h` and `nu`, the source-qualified population theorem,
or any full Collatz conclusion. It is not a Lean or numerical replay.
The exact input pins and their evidence level remain those recorded in
the reviewed note.

## 1. Whole-predecessor minimum and superlevels

The set `Pred(q)` includes `q` and consists of actual positive ordinary
unit predecessors. Its least element `a(q)` therefore exists and is at
most `q`. Applying the input floor comparison with `m=a(q)` uses the
whole predecessor set, as required. It does not substitute the minimum
of a later forward suffix.

The pointwise estimate is correct:

`R(q) <= 1/(3a+1) + (200/3)*a^(-1/40) <= 67*a^(-1/40)`.

For the final constant, `a>=1` gives
`1/(3a+1) <= (1/3)*a^(-1) <= (1/3)*a^(-1/40)`; adding `200/3`
gives exactly 67. The separate bound `R<=1` is preserved where the
right-hand estimate exceeds one.

If `R(q)>=t>0`, its least actual predecessor lies below `(67/t)^40`.
The target is therefore on one of finitely many genuine forward orbits.
Taking the sum of their individual `5*X^(39/40)` counts is a valid union
upper bound even when many of those orbits coalesce. There is no assumed
disjointness, invariant fresh law, or lost source-pair collision in this
argument. Together with the trivial count `<=X`, this proves equation (6).

## 2. Moment exponent and constants

Set `beta=39/40` and `t0=67*5^(1/40)*X^(-1/1600)`. Then the nontrivial
superlevel coefficient is exactly `X*t0^40`. For `0<p<40`, splitting
the finite layer-cake integral at `t0<1` gives

`X*t0^p + p*X*t0^40*(t0^(p-40)-1)/(40-p)`

which is at most `40*X*t0^p/(40-p)`. This is exactly

`C_p*X^(1-p/1600)`, with `C_p=40*67^p*5^(p/40)/(40-p)`.

If `t0>=1`, that same upper bound exceeds `X`, so the trivial estimate
handles the omitted regime. The endpoint `p=40` is deliberately not
inserted into the displayed formula with a zero denominator.

The Mellin identity used for equation (9) is valid because
`s>1-p/1600>0`. Integrating the prefix bound yields exactly
`s*C_p/(s-1+p/1600)`. At `s=1` this is `1600*C_p/p`.
For powers `p>=40`, domination by `R` gives the asserted finite harmonic
moment without an unsupported endpoint limit.

The canonical seed comparison `a0=(3+1/n)d` gives the pointwise complete
occupation bound `sum_k L^k a0/nu <=4R`. Tonelli and the `p=1` harmonic
moment consequently give `6400*C_R` in equation (13). This sums the
unchanged original seed and retains every endpoint collision. The
remaining spatial factor `1/q` is present and cannot be dropped.

## 3. Drift orientation

The Green identity `W=d+LW`, with `W=nu*R`, gives
`K_nu R=R-d/nu`; hence the stated superharmonic direction is correct.
Expanding a forward edge and using `Lnu=nu` produces the exact side-branch
term in equation (15). Its sign is not determined by the preceding
estimates. The note correctly does not infer forward monotonicity of a
quotient merely from monotonicity of its numerator and denominator.

## 4. Ordinary extension and mean statements

Every positive integer reaches an odd ternary unit by taking its odd
part and, only if that odd part is a multiple of three, one accelerated
odd step. Periodic unit states receive value zero as stated.

Summation over the initial power of two contributes a factor two. The
odd-unit part contributes the original harmonic sum. For an odd nonunit
predecessor of `q`, `x=(2^e*q-1)/3`, and the legal positive case has
`2^e*q>=2`, so `1/x<=6/(2^e*q)`. Summing over all `e>=1` bounds even
the unrestricted predecessor choices by `6/q`. Thus the ordinary
extension factor is `2*(1+6)=14`, and the final bound is `22400*C_R`.

Finite nonnegative harmonic mass implies ordinary mean zero by the fixed
finite-prefix/tail split displayed in the note. The logarithmic numerator
is bounded as well. Since the extension is bounded by one, these ordinary
mean statements imply the standard bounded Besicovitch null statements.

The exact shortcut inverse fibers in equation (18) are correct. Their
coefficient bound is `1/2+2=5/2`, using `q>=2` on the odd-parent branch.
Hence every fixed iterate and finite Cesaro average has finite harmonic
mass and ordinary mean zero.

For every fixed `alpha<1`, the Abel average is null because its tail after
`K` terms is uniformly bounded by `alpha^K`, independently of the source
integer. This argument is valid for all such alpha; it does not assert
the stronger harmonic bound obtained by summing the operator estimate
outside its convergent geometric range.

The pointwise limit of these averages can nevertheless have positive
ordinary mean. The note correctly distinguishes that pointwise limit
from convergence in the source-averaged Besicovitch seminorm.

For the harmonic absolute five defect
`E5(f)=sum_n |f(5n)-f(n)|/n`, the bound `E5(f)<=6*||f||_H` follows by
the change of variables `m=5n`; restriction to odd units can only reduce
this upper bound. Summing the finite operator bounds gives precisely the
displayed factor `((5/2)^N-1)/((3/2)*N)`. Its growth supplies no finite
limiting five energy by Fatou.

Under the stated population input, any escaping component's positive
invariant label has a positive lower ordinary mean. For a fixed
nonnegative null approximant `A`, the inequality
`||F-A|-F|<=A` then makes its lower mean absolute error exactly that
positive lower mean. This is a correctly conditional failure of the
proposed limit transfer, not a proof of existence of an escape.

## 5. The future-minimum counterexample is ordinary and explicit

The sequence

`n_j=(5*2^(6j+3)-1)/3`

consists of positive odd units. Modulo nine, its numerator is three
modulo nine, so `n_j=1 mod 3`; moreover `3*n_j+1=5*2^(6j+3)` gives
`U(n_j)=5`. These inputs grow without bound and then follow `5->1`,
so their actual future minimum is one.

For any fixed bound `M`, only finitely many of these inputs can have a
predecessor at most `M`: each such bounded predecessor must pass through
the selected input before its unique hit of the nonperiodic target five,
and has only finitely many pre-hit states. There are only finitely many
bounded predecessors. Thus `a(n_j)->infinity`, and the proved pointwise
bound forces `R(n_j)->0`.

This refutes a uniform pointwise payment `m(n)<=C*R(n)` on a fully known
convergent family, independently of the population input. It does not
refute alternative aggregate inequalities or a more elaborate charged
minimum estimate.

## Retained global boundary

The new theorem supplies global harmonic summability of every positive
power of the normalized Green deficit, explicit ordinary prefix rates,
and a complete weighted original-source occupation estimate. It supplies
neither an unweighted occupation bound nor ordinary mean approximation of
the invariant escape label. The periodic states were killed throughout.
Those are correctly retained as separate missing full-theorem steps.
