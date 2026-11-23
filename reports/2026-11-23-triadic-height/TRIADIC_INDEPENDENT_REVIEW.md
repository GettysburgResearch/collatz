# Independent reconstruction of the weighted triadic certificate

Reviewer: `/root/boundary_rigidity`. Date: 2026-11-23.

**Finding:** the written weighted-product argument and its finite horizon
`H=9E+1` are correct. This review does not establish the universal
existence of a candidate meeting its own height bound. No full Collatz
conclusion follows from the reviewed theorem alone.

The reviewed document is `TRIADIC_AMORTIZED_BUDGET.md`, SHA-256
`8249811440526b15587d345179769db54297910afb34eb3bc84084b1f41dd02f`.
The reviewed sections are 1--4, including the complete congruence consumer.
The earlier paired-state definition and congruence argument were compared
against PR178 at `4e204f54136c79cf8c9393b34e3330594f99ae0a`,
`research/global-closure-20261123/duality/TRIADIC_RANK.md`.
The author's optional polynomial-literature discussion is outside the
primary source verification scope of this review.

## Reconstruction

Write `F(r)=prod_(j<r)(1+3^j)` and `P=x*abs(w)*F(r)`. Positivity of the
ordinary coordinate and integrality of the numerator are retained at
every passed complementary-parity test; no lowest-terms assumption is
needed for `w/3^r`.

For original-odd `x>1`, parity gives `x>=3`, `w` even, and the exact ratio
is `(3x+1)/(4x)<=5/6`. Nonzero w remains nonzero in this case.

For an original-even step with `r=j+1>0`, the exact numerator is
`w'=(w+3^j)/2`. The inequalities

```text
2*abs(w') <= abs(w)+3^j <= abs(w)*(1+3^j)
F(j+1) = (1+3^j)*F(j)
```

give `P'<=P/4`. Both signs and a sign crossing are included. This is the
step that pays for a denominator drop in the same potential as all other
steps, instead of multiplying its whole later numerator budget by r.

At denominator exponent zero, a negative odd numerator has ratio
`abs(3w+1)/(4abs(w))<=3/4`; a positive odd numerator other than one is
at least three and has ratio at most `5/6`. The sole tie is `w=1`.
It produces numerator two. A further passed test forces the next ordinary
coordinate to be odd; if that coordinate is not one, the next step has
the `5/6` bound. Thus two passed nonterminal, nonzero steps always have
`P_(i+2)<=5P_i/6`. Four such blocks give strict halving because
`2*5^4=1250<1296=6^4`.

A nonzero numerator can first become zero only on the positive-exponent
even branch, at `w=-3^j`. At that step `x'=x/2` and
`x'+1<=x<=P_before`. A zero numerator then permits only original-odd
steps. L such steps force `2^L` to divide the fixed entry value `x'+1`,
by iterating `2(x_next+1)=3(x+1)` and cancelling the odd power of three.
The nonzero phase and zero phase are therefore both bounded by the same
initial weighted height.

Let `B=n*max(1,abs(a))*F(r)` and `E=bl(B)`, so B is a positive integer
and `B<2^E`. If the initial numerator is nonzero, `P_0=B`. Survival
with nonzero numerators through clock `8E`, while avoiding ordinary one,
would put the positive integer `P_(8E)` below one. Hence a first zero
occurs at some `1<=j<=8E`, unless one has already been reached. At zero
entry `0<x_j+1<=B<2^E`; at least `E+1` of the first `H=9E+1` passed
steps remain. Their divisibility is impossible. For an initially zero
numerator the separate inequality `n+1<=B+1<=2^E<2^H` gives the same
contradiction. This handles the boundary case `n=2^E-1`, in which
`n+1=2^E` rather than a strict inequality. The source `n=1` is already
terminal and needs no contraction argument.

For the final congruence, the actual complementary word sends `a/3^r` to

```text
(3^b_H*a + 3^r*D_H)/(3^r*2^H).
```

Divisibility of its numerator by `2^H` gives a terminal rational with
odd denominator. Pulling this same affine word backward uses `2y` on a
dual-even step and `(2y-1)/3` on a dual-odd step. These maps impose their
respective parities and keep denominators odd. Affine inversion recovers
the original candidate exactly. The final congruence thus certifies the
entire legal prefix, including every intermediate test; it is not merely
a matching endpoint identity.

Finally,

```text
log2 F(r) = r(r-1)*log2(3)/2 + sum_(j<r) log2(1+3^(-j)),
sum_(j<r) log2(1+3^(-j)) < 2.
```

The j=0 term is one when present; the remainder is bounded above by
`sum_(j>=1)3^(-j)/ln(2)=1/(2ln(2))<1`. Therefore the new horizon is
`O(log n + log max(1,abs(a)) + r^2)`. The removal of the previous
`r*log(abs(a))` cost is substantive. It does not supply a candidate in
the larger permitted window, and the earlier certificate can still be
shorter for particular small parameters.

## Independent finite arithmetic controls

The companion `check_triadic_review.py` independently reconstructs the
three paired transitions and checks their rational interpretation using
exact `Fraction` arithmetic. It uses explicit exceptions, not assertions
that Python optimization would remove. Its range is:

- `2<=x<=100` and `0<=r<=7`;
- numerators in `[-120,120]`, together with the positive and negative
  powers `3^r` and `3^max(0,r-1)`;
- all compatible nonzero initial states in that range, and all available
  compatible second steps with a nonterminal nonzero middle state.

The executed checks covered 95,540 compatible states, 42,500 denominator
drops, 350 zero entries, 50 ties, and 47,117 compatible two-step prefixes.
They all passed. The receipt binds both the exact checker and the reviewed
document by SHA-256. These bounded checks are a separate sanity check of
the formulas; the universal finite theorem is supported by the written
argument reconstructed above.

## Independent formal replay and exact scope

After the written reconstruction, the reviewer read the final new Lean
source and its audit and freshly compiled all three files below in a
separate output directory, with warnings treated as errors:

| Source | SHA-256 |
|---|---|
| `TriadicDualClosure.lean` | `62a3d8a9541080864deb4887ba8c014a82222892869b14597c3b6385538913c7` |
| `TriadicAmortizedBudget.lean` | `fe2411d3fe1d8063e9a788433fbf86f69f7a18c0f64b995521a7d7256746d759` |
| `TriadicAmortizedAudit.lean` | `8e0d499dfa45f625d46686c5cf3fe705b7e210714ba1f300905587cb7207e9f5` |

The paired-state dependency was compared byte-for-byte with the pinned
PR178 source and matched exactly. The compiler was Lean 4.34.1,
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Mathlib dependency objects
were reused; the three research files and their output objects were
freshly compiled. All three commands exited zero.

The audit covers all 26 authored public declarations: four definitions
and 22 theorems. The reviewer inspected all audit output. Its axiom union
is exactly `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`
or custom research axiom occurs. The source contains no admitted proof,
native decision shortcut, or replacement implementation.

The final theorem `finite_triadic_height_certificate` has precisely the
following scope: for positive integer n and one fixed signed numerator
a and denominator exponent r, compatibility of the literal deterministic
paired trajectory through clock `9*binaryBudget(n,a,r)` implies that the
literal original shortcut orbit reaches one by clock
`9*binaryBudget(n,a,r)+1`. The definition of `binaryBudget` is one plus
the natural base-two logarithm of the positive initial weighted product.
Its height coverage, all signed cases, zero-entry tail, and finite horizon
are proved inside the new module. Neither all-time compatibility nor
prior convergence is a premise.

The endpoint congruence-to-prefix argument remains written mathematics;
it is not the hypothesis of this final Lean declaration. The logarithmic
asymptotic estimate of F(r) and the universal candidate construction are
also not asserted as formal conclusions of this module.

The full execution receipt is `lean_review/LEAN_REVIEW_RECEIPT.json`,
SHA-256 `c92cccdc630bad98a530a7f14fbe5f81126cc3c3ea4cc0ed3826a9e8cc8e529f`.
It records source hashes, actual argv, separate exit codes, compiler and
Mathlib pins, and the complete axiom output. The standalone audit log is
`lean_review/TriadicAmortizedAudit.log`.
