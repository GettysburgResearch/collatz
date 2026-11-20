# Independent reconstruction of the sparse-return packet

**Verdict:** SR-1 is VERIFIED conditional only on the explicitly imported
Evertse--Schlickewei--Schmidt theorem; SR-2, the fixed-source carry
identity in SR-3, and the combinatorial implication SR-4 are VERIFIED at
the scopes stated below. This is mathematical reconstruction by a
separate agent, not formal proof-assistant verification or a claim that
Collatz is solved.

## Reviewed bytes

The reviewed note is `agent-alternative/SPARSE_RETURN_SPECTRUM.md`,
13,154 bytes, SHA-256
`8e2c20a79b969d3312c8f8349375092d67db2aa6383ad6105cce188bb2e39e02`.
The inspected author checker is `check_sparse_returns.py`, 5,742 bytes,
SHA-256
`0c7806208082ffbac729136ef3dfb77356183e943417f91ae4949a1aaeda25c7`.
These hashes delimit this review; later edits require a delta review.

The source pins are PR #141 at
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` and PR #145 at
`dd245a712f985909f541590e3f6c179b7ba011e4`.

## 1. Uniformity of the S-unit application

I separately inspected the primary paper's Theorem 1.1 and definition
of nondegeneracy at
<https://arxiv.org/pdf/math/0409604>, pp. 1--2, printed pp. 807--808.
The theorem applies to a fixed coefficient equation in a finite-rank
subgroup of a coordinatewise multiplicative group; it bounds the number
of solutions with no vanishing subsum by
`exp((6m)^(3m)(r+1))`.

The note's reduction meets these hypotheses. A minimal zero subsum of
the binary-expansion identity has both signs. Dividing by one positive
left term yields an equation with coefficients fixed at `+1` and `-1`.
Any zero subsum after division would contradict the minimality of the
chosen relation. The coordinate group is fixed once `p,q` are fixed:
its `m` independent coordinate powers of two and its common power-of-three
vector generate a group of rank `m+1`. The coefficients and the group
do not change with the original integer `u` or exponent `h`.

The exponent is recovered as the 3-adic valuation of any coordinate
containing the common factor `3^h`. Therefore finitely many normalized
solutions imply finitely many possible `h`, even though `u` ranges
over arbitrarily large ordinary integers. The `p=q=1` case forces
`h=0` and is correctly removed. The cardinality formula uses
`r+1=m+2=p+q+1`, with the correct exponent. It does not bound the
largest permitted `h`, and the note explicitly retains that distinction.

The strongest possible degeneracy objection is harmless here: other
parts of the original binary expansions may form further zero subsums,
but one minimal relation already carries the same `h` and suffices for
the finite-union argument. No bound on the number or location of those
other parts is used.

## 2. The elementary spectra

The one-bit case is immediate. I reconstructed the two-bit classification
independently. For `u=1`, the factorization of `3^(h/2)-1` and
`3^(h/2)+1` handles every exponent after the two small cases. For
`u=2^d+1`, divisibility of `2^e+1` gives `d|e` and odd `k=e/d` from
the standard binary-plus gcd identity. If `d` is even, the quotient
is one modulo three. If `d` is odd, its 3-adic valuation is `v_3(k)`.
It can be a pure power of three only if the entire quotient is at most
`k`; this fails for `k>=5`. At `k=3` only `d=1` survives. Thus the
three listed positive-exponent pairs, and `E_2={0,1,2}`, are complete.

## 3. Carry separation retains one original source

The largest-gap inequality is correct: a source with `r<=S` bits has
`r-1` positive gaps summing to its highest set-bit position, so the
largest gap is at least the stated ceiling with denominator `S-1`.

The actual induction uses the *next* cumulative valuation. For
`j+1<=J`, the bound `P_(j+1)<2^D` gives `A_(j+1)<D`. Thus the low
numerator has valuation strictly less than the upper term's current
power of two, and the actual valuation equals the shadow valuation.
This proves the affine identity through the entire guarded window.
The strict inequality on the lower block also proves disjointness of
binary supports. Its nonzero contribution leaves at most `S-1` bits
in the homogeneous upper block. The time difference consequently lies
in the same fixed `E_(S-1)`.

There is no switch to a different representative or a different
2-adic completion. The shadow value 1 is legitimate because the odd
map fixes 1 with exponent two. The full separated source remains
strictly larger than 1. The controls at 5 and 257 correctly disprove
the proposed extension after the guard closes.

## 4. The occupancy bound

An odd `r`-bit source is fixed by its `r-1` adjacent positive gaps,
because the lowest bit is at position zero. Hence the short-gap census
is exactly `(2L)^(r-1)`; no translation factor is missing.

The greedy reserved windows are disjoint and have length `L`, except
possibly the last. Their starts are separated by at least `L`, so
there are at most `ceil(N/L)`. Every sparse event outside them has
only short gaps. Inside each window the spectrum bounds the number of
events by `|E_(S-1)|`. Possible double counting with the short-gap term
only enlarges the upper bound. Choosing `L` of order `N^(1/S)` yields
the stated exponent `1-1/S` with no logarithmic loss.

Distinctness is indispensable for the short-gap census. Applying the
bound to infinitely repeated cycles would be invalid; the note limits
it to a primitive tour. The uniformity over the starting position
does support the claimed upper Banach density conclusion for a
nonperiodic ordinary orbit.

## 5. Independent finite reconstruction

I wrote and executed `review_sparse_arithmetic.py`, independently of
the author's checker. It uses repeated division for valuations and an
explicit greedy window partition. Its output `sparse-review-report.json`
records:

* 16,200 two-bit homogeneous pairs in a specified finite box;
* 2,240 selected original-source cuts at popcounts two through eight;
* 64,387 exact cut-state identities;
* 20,120 greedy occupancy decompositions;
* 3,229 separately checked reserved windows.

All passed. This replay does not execute the imported S-unit theorem
or compute a general maximum exponent. The universal verdicts above
come from the proof reconstruction, not from the finite sample.

## 6. Consequence and limits for a least counterexample

The new spectrum does not close an additional least-counterexample
class by itself. It bounds sparse returns from above, while an escaping
orbit is allowed to spend all sufficiently late time at growing
popcount. Neither being the least nonconverger nor staying above its
initial value supplies a conflicting lower bound on sparse visits.
In particular, restarting the carry cut at later dense states does
not preserve the original sparse upper block or charge the new clock.

One useful direct corollary concerns an assumed cap on an entire
primitive cycle. Put `K=|E_(S-1)|` and `L=2K` in SR-4. If every vertex
of an odd cycle has at most `S` bits, its primitive period `N` obeys

\[
N\le2\sum_{r=1}^{S}(4K)^{r-1}+2K.
\]

This is an effective period bound from the cardinality estimate alone,
without a numerical value of `H_S`. It is restricted, overlaps the
earlier finite-core conclusion in spirit, and does not exclude a
cycle with unboundedly large bit count across candidate cycles.

No correction to the reviewed mathematical statements is required.
No claim outside the stated bytes or source-qualified input is covered
by this verdict.

## Quantitative delta: the fixed S-unit theorem

A subsequent narrow review covers the additional SR-1Q paragraph and
the corresponding status/attribution edits in the note with SHA-256
`1b1bba8fefb70da52f2194c656db015d81bf37d7de6804603051ffe9a63f3283`.
The earlier mathematical statements are preserved. The new claim is
**VERIFIED subject to the explicitly imported Evertse theorem**.

I separately opened Evertse's primary preprint
<https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf> and checked
Theorem 3 on printed p. 7. All normalized variables in the existing
minimal relation are rational units outside `{infinity,2,3}`, so the
number of places is three. Applying the theorem with
`m=p+q-1<=2S-1`, and then enlarging all at most `S^2` summands to their
maximum, gives exactly

\[
|E_S|\le1+S^2\bigl(2^{35}(2S-1)^2\bigr)^{3(2S-1)^3}.
\]

No new coefficient depends on `u` or `h`; the prior nondegeneracy and
valuation-recovery checks apply unchanged. This sharpens the bound on
the *number* of exponents. It still does not give a largest-exponent
bound. In particular it gives
`log K_(S-1)<=(48+o(1))S^3 log S`, with natural logarithms, as the cap
increases. This delta review does not promote a growing-cap corollary
as stronger than the separate binary-run results already in PR #145.
