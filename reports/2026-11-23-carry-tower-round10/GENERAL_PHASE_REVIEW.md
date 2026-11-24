# Independent review of the general paid-return construction

23 November 2026. Reviewer: `density_free_germ8`.

**Verdict: VERIFIED for R10-P1--R10-P5 in their stated domains.**
The finite procedure constructs a paid return or sound rejection for
a supplied rational phase, with a separately checked canonical-cycle
branch. It does not decide the infinite equality after arbitrarily
many returned sources.

## Exact review binding

Parent: `c369ae3c426ec6aaf9a280ec9578b9910c2147d5`.
Paths are under `research/carry-tower-round10-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `GENERAL_PHASE_RETURN.md` | `df7c79ffabdd628b36db2b0e7478c35fe57c80d2` | `73721b10e68ac7b045a57e42bc4ac631a84f688f8dc9db0b17bf2618d045bbb8` |
| `general_phase_controls.py` | `945bacbd3da14a894872eca517d6e37e491160df` | `bff571c0f590b54dd57986b41222f4c3a6f1fe23858d61f0ae8773a996cae285` |
| `GeneralPhaseReturn.lean` | `e728e06ecc19228fc9dd4d37aac3cb3e3bedb2d3` | `a920fa79010a93d1865826470ddbddaecda0e0347a3e1782ebacb638003bf0e7` |

The actual scalar, carry normal form, and complete finite cylinders
are the four exact parent dependencies pinned in Section 1 of the
note. This review retains their positive ordinary scope and their
strict scalar lower bound. No pressure maximum is used.

## Guarded rank and arbitrary carries

From `p>1/2` and `3(p+k)<=B+3`, an integer carry satisfies
`3k<=B+1`. For `k>=1`, this gives `k<=B-1`, including the smallest
possible bit lengths. The ordinary lower bound `q>=2^(B-1)` then
gives `Y=q/2^k>=1`; k=0 is immediate. This proves R10-P1 from
finite necessary guards, without assuming the candidate is the
actual scalar.

The complete equation cancels the destination carry and gives
`Y'=3Y/2^(b+2k)+1/2^(b+3k)`. When k is positive, this is bounded
by `H(Y)=3Y/8+1/16`, and `Y>=1` gives the factor `7/16`.
Starting from `Y<2^(bl(s)-k)`, that many consecutive guarded high
transitions would give an endpoint below one. Thus the stated high
budget is sound for false candidates as well as for a true supplied
equality. A true equality cannot fail a necessary guard.

At entry from a zero carry, the exact normalized value is
`E_b(x)=(3x+1)/2^b`; the first positive carry requires b=2 or b=3.
The fixed point of H is 1/10, and these entries are at least 1/2.
Monotonicity and iteration of H therefore give the arbitrary-length
bound in R10-P2, with exactly `(9x+5)/32` or `(9x+7)/64` after
the first high transition. The latter is at most the former for
positive x. The comparison is to the last low entry state, and
the note correctly retains the cost of reaching that state.

## Exact ordinary departure and totality

The canonical word has positive charges, an odd affine carry C,
and an odd nonzero signed denominator D. Its rational fixed point
and every cyclic shift are odd rational states with the prescribed
valuations. For an ordinary positive source with `Dq+C!=0`, the
difference valuation T is finite and at least one.

There is a unique n with `A_n<T<=A_(n+1)`. The finite difference
equation preserves every canonical gap before n. If equality holds
at the upper endpoint, cancellation of two terms with the same
binary valuation forces a strictly larger actual gap. Its candidate
scalar is at most one half, including the endpoint phase 3/2, so
rejection is justified. If T lies strictly inside the clock interval,
the actual gap is `T-A_n`, and the first positive carry is exactly
`b_n-(T-A_n)`. No arbitrary gap is chosen by the procedure.

The first high state is reached after at most T steps. Its bit length
is at most `B_0+n+1`, and its carry is at least one. The guarded
high-stage budget consequently yields the stated total bound
`B_0+2T`. For the height-only estimate, the positive absolute value
`|Dq+C|` is less than twice the larger of the two power-of-two
height bounds. This gives
`T<=max(bl|D|+B_0,bl C)`, exactly the bound needed in (15).

When `Dq+C=0`, the finite canonical cycle is checked explicitly.
Its exact scalar follows from its periodic gaps and canonical phase
recurrence. This is separate from the paid-return branch; when D is
positive, the canonical fixed point is negative and cannot be the
supplied positive source.

Backward substitution proves (17) for every returned actual prefix,
even when its initial candidate was false. Thus the transform preserves
equality in both directions but does not accept an unchecked infinite
equality. These arguments verify R10-P3 and R10-P4.

## The complete denominator-1456 example

The canonical word has length 12, clock 19, carry 700273, and signed
denominator 7153. Its strict internal clock positions produce exactly
the residues `{7,9,11,13,15,17,18}` in the valuation gate. A true
candidate must follow the first six canonical one-gaps, hence
`2^7 | q+1` and `bl(q)>=7`. With the displayed constant heights,
the budget `3bl(q)+26` follows.

For the complete W/V family, the shifted W map is multiplication
by R around the rational center `-c`. Composing its m-fold iterate
with V gives exactly `alpha_m(q+c)+kappa`, retaining the affine
constant. The first reduced canonical charge is at position
`12m+6`, so the full ordinary source has valuation `19m+7`.
This funds the source bound used for all m>=2.

The three exact slope/affine comparisons in the note then prove
descent for every source in the complete family through m=101 and
expansion for every source from m=102 onward. The small cases m=0,1
are checked separately with the weaker source bound q>=3. The proof
does not extrapolate a sample of canonical residues to the whole
class. The first paid low return occurs after `12m+8` transitions;
the remaining transitions of V are an explicit same-phase completion,
not a claimed generic normalization of arbitrary excursions.

## Code and formal scope

I inspected the full implementation. The replay takes every gap
from the actual ordinary map, carries exact rational candidates,
processes the signed-denominator zero case before valuation, and
uses explicit exceptions rather than removable assertions. Its
finite true-scalar transport checks compute the selected trajectories
to one with a stated cap; the mathematical transformer does not
assume that arbitrary inputs terminate.

The fourteen Lean declarations provide the integral guard, normalized
lower rank, arbitrary-carry high envelope and path iteration, both
paid affine comparisons, and the finite high-budget contradiction.
They do not formalize the real scalar, canonical rational cycle,
ordinary valuation departure, or entire transformer attachment.

The owner reports strict compilation and identical normal/optimized
control results with 16,541 checks. This review inspected their full
sources and reconstructed the universal arguments; fresh execution
and publication receipts are assigned to root. No broad duplicate
run is claimed by this reviewer.

The remaining step is the sequence of returns on one fixed actual
orbit. The source-dependent expanding low prefixes and changed
fractional phases have not been shown to be paid for globally.
