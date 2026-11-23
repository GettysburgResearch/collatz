# Independent review of the finite rational-dual certificate

23 November 2026. Reviewer: `/root/triadic_selector`.

**Verdict: PASS for the stated finite sufficient certificate and its
seven numerical Lean lemmas.** The certificate does not establish
universal witness existence or unrestricted positive-cycle exclusion.
The full certificate remains a written theorem, with a Lean-checked
numerical core. No claim that its visit counting or parity argument is
formalized is made here.

## Frozen material and fresh build

The reviewed note is
`research/central-step-20261123/rational/FINITE_RATIONAL_CERTIFICATE.md`,
SHA-256
`990dbdff54e440791c1144e824beedb6681a78d614300b6faa9596ccdc93ad55`.
Its README, both Lean files, and author receipt were checked against the
author's supplied hashes before and after the independent build.

Both modules were freshly compiled into the previously unused external
directory `/workspace/scratch/56e7a5765d0c/central-rational-independent-review`,
using Lean 4.34.1, mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`,
`-DautoImplicit=false`, and `-DwarningAsError=true`. Both exited zero.
The audit contains all seven authored theorem declarations. Its axiom
lists contain only `propext`, `Classical.choice`, and `Quot.sound`;
`abs_numerator_bounds` does not need `Classical.choice`.

Exact commands, environment search paths, timestamps, source hashes,
exit codes and output hashes are in
[rational-review-receipt.json](rational-review-receipt.json).
The raw outputs are
[rational-review-compile.log](rational-review-compile.log) and
[rational-review-axioms.log](rational-review-axioms.log).
Only these two new modules were built. Existing mathlib dependency
objects were reused; the earlier Collatz corpus was not rebuilt.

After the build, I also inspected the added
[rational-sources.json](rational-sources.json), SHA-256
`95a55b0e902b2beec6b418c53959b45f1fe5650ad4870c1663a6aa255946d988`.
Its local capacity hash matches the current file. Its PR176 comparison
entry matches the exact source recorded by this reviewer in the triadic
source ledger. It correctly separates prior qualitative attribution,
the local period-bound dependency, the comparative triadic horizon,
and the unproved witness-construction obligation. This additional
metadata check did not change or rebuild any frozen mathematical source.

## 1. Both signs and zero are covered by the potential

For a positive odd integer `q`, the map `S_q` sends every signed integer
to a signed integer. Opposite parity is imposed at the actual clock; it
is not inferred from an unrelated word. The potential
`V=x max(1,|w|)` is a positive integer whenever the original state `x`
is positive. In particular, `w=0` is retained and causes no failure of
positivity.

At a large state `A=|w|>=q+1`, the original-even branch gives
`2x'=x` and `3A-q<=2A'<=3A+q`. The lower bound makes `A'>=1`,
so both potentials really are `xA` and `x'A'`. The difference in the
stated contraction comparison is exactly `xq(A-q-1)>=0`.
At the original-odd branch, `2A'=A` and `A'>=1`, while the corresponding
difference is `A(q(x-1)-1)>=0`. The no-hit assumption gives `x>=2`,
which is sufficient. The proof does not require an assumption that the
complementary numerator is positive or is already in lowest terms.

For a small state, `|w|<=q` gives `|w'|<=2q`, including the negative and
zero cases. The literal ordinary map satisfies `x'<=2x` for every
positive `x`. Hence `V'<=4qx<=4qV`. These are exactly the estimates
used in the written excursion proof and the finite numerical modules.

## 2. The visit count and all endpoints fit inside the horizon

Set `c=4q+3`, `J=2q+2`, `M=B(4q)^J`, `L=bl(M)`, `R=cL`,
`t_*=J(R+1)`, and `H=t_*+L`, as in the note. Here `B>=1`, `q>=1`
and `L>=1`. The stated Bernoulli inequality gives `rho^c<=1/2` for
`rho=c/(c+1)`. Consequently, any `R` consecutive large updates from
`V<=M<2^L` would end below one, contradicting positive integrality.

The bound preceding the `J`th small visit is correct: if fewer than
`J` small clocks have occurred, at most `J-1` small updates precede
the current clock. The other updates are nonincreasing, so
`V<=B(4q)^(J-1)<=M`.

To audit the block count precisely, the `h`th block of clock indices is

`[h(R+1), (h+1)(R+1)-1]`, for `0<=h<J`.

If the block contains no small clock, use the first `R` updates in it.
Their endpoint is `h(R+1)+R`, the last clock of that same block.
Thus both the beginning and endpoint stay in `0,...,t_*-1`, and all
needed paired tests and no-hit assumptions are available. Under the
hypothesis of fewer than `J` small visits, the initial potential of
each such run is at most `M`. Every block must therefore contain a
small clock, giving at least `J` in total and the desired contradiction.
The extra clock in a block of length `R+1` is a valid conservative
choice; no endpoint at an untested clock is needed.

The first `J=2q+2` small visits take their numerator values in the
`2q+1`-element integer set `[-q,q]`. Pigeonhole gives `i<j<t_*` with
`w_i=w_j`. At each of these first `J` visits, at most `J-1` prior
small updates have occurred. Therefore `0<x_i,x_j<=M<2^L`, exactly
the size hypothesis needed in the next step.

## 3. A repeated numerator forces a repeated ordinary state

Equality of the two numerator states implies equality of their entire
future `S_q` trajectories by determinism. For the length-`L` windows
starting at `i,j`, the largest required parity-test clock is
`j+L-1<=t_*+L-2=H-2`, which is inside the assumed range `k<H`.
The two original windows consequently have the same parity word.

The complete affine carry depends only on this shared word. Subtracting
the two length-`L` identities yields divisibility of `3^p(x_i-x_j)`
by `2^L`. Since `3^p` is odd, `2^L` divides `x_i-x_j`. Both original
states are strictly between zero and `2^L`; their difference has
absolute value less than `2^L`, so it is zero.

The two full paired states therefore repeat. Every parity check on the
block from `i` to `j-1` is already among the assumed tests. Determinism
repeats this tested block indefinitely, proving eventual periodicity
and all-time complementary agreement from that point. This is a proved
promotion from a finite prefix, not an extra periodicity assumption.

## 4. The endpoint congruence is genuinely equivalent

Prescribe the complementary branches of the actual original prefix.
Their finite affine iterate, starting from `a/q`, is
`(3^b_H a+qD_H)/(q2^H)`. Because `q` is odd, 2-adic integrality of
this endpoint is equivalent to the displayed integer divisibility by
`2^H`.

If all prescribed branches are legal, this endpoint is clearly
2-adically integral. Conversely, take the first parity failure, if one
exists. Its input is 2-adically integral and the wrong prescribed
branch makes its numerator odd, so the output has valuation `-1`.
For an input of negative valuation, either subsequent prescribed branch
reduces that valuation by exactly one: multiplication by three is a
unit operation, and addition of one cannot cancel a term of strictly
negative valuation. The final endpoint could not then be integral.
This proves both directions of the endpoint criterion for signed `a`,
including zero, without a reduced-fraction hypothesis.

## 5. Use of the cycle capacity result and formal boundary

Once a paired state repeats, the positive ordinary cycle is established
independently of the separate capacity theorem. The rational values on
the paired periodic orbit have reduced denominators dividing the
original supplied `q`. The full complementary denominator is one of
these denominators. Equivalently, over an original primitive period the
complementary affine map has slope `3^b/2^K != 1`; a point periodic under
an iterate of this affine map must be its fixed point. This verifies
that the paired rational orbit is the actual complementary cycle, even
if the initially found repeated block was longer than its primitive
period.

Thus the separate conclusion `K<=2d` for the full complementary
denominator `d`, with `d|q`, is correctly consumed as `K<=2q`.
The note explicitly leaves that capacity proof to its own written
packet and independent review. Its specialized triadic consequence
also retains the denominator qualification: a periodic complementary
denominator is prime to three and divides `3^r`, hence is one.

All seven Lean declarations match the limited numerical scope stated
in the README. The complete visit count, parity coding, endpoint
equivalence, and cycle consumer are written mathematics. No universal
candidate-existence axiom, unproved mixing premise, or assumed absence
of other positive cycles enters the certificate. The remaining
source-specific approximation and cycle-exclusion obligations are
stated accurately.
