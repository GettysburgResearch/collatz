# Independent reconstruction and fresh replay: exact finite candidate rigidity

23 November 2026. Reviewer: the infinite-optimizer agent, separate from
the triadic construction author. **PASS in the stated formal and written
scope.** No universal candidate construction or full Collatz proof is
claimed by this review.

## 1. Frozen files

| Source | SHA-256 |
|---|---|
| `EXACT_CANDIDATE_RIGIDITY.md` | `3362a3efbefe945b0e4167f9db714d15bdf650df57c031d877105308f53ccee7` |
| `lean/TriadicCertificateRigidity.lean` | `d1696a47a85525a242dbe100d594dfec9487d1cc40d25090bdf119f49712d958` |
| unchanged `lean/TriadicAmortizedBudget.lean` | `fe2411d3fe1d8063e9a788433fbf86f69f7a18c0f64b995521a7d7256746d759` |
| unchanged `lean/TriadicDualClosure.lean` | `62a3d8a9541080864deb4887ba8c014a82222892869b14597c3b6385538913c7` |

I read the complete written proof and all new Lean declarations. I
independently reconstructed the clock, signed/zero cases, terminal defect,
and written denominator consequences. During development I suggested the
two-initial-tests proof of the n=1 weight bound; the author formalized it.
This contribution is disclosed rather than described as an external,
fully isolated review of that implementation choice.

## 2. The 8E first-hit bound

Use the unchanged candidate-dependent budget `B`, `E=bl(B)`, `H=9E+1`.
If the actual original coordinate has no hit of one through `8E`, it is
strictly greater than one throughout that interval. If the numerator also
never vanishes there, the checkpoint-16 eight-step contraction iterated E
times contradicts the initial potential bound `P_0<=B<2^E`.

Otherwise take the first zero clock `j<=8E`. The preceding nonzero step
and monotonicity give `0<x_j+1<=P_(j-1)<=B<2^E` when j>0. At j=0 use
the separate `n+1<=2^E` bound, which follows from the literal initial
budget. Continued compatibility at zero forces original odd steps and
preserves the zero numerator. The first `E+1` such steps are available
because `j+(E+1)<=H`; they imply `2^(E+1)|(x_j+1)`, impossible under
the positive height bound. This proves the early original hit.

There is no unsupported assertion that zero cannot occur at the first
hit itself. The later terminal-defect argument covers that case too.

## 3. Size and divisibility of the cycle defect

The denominator exponent is nonincreasing. Before the first original hit,
the integer potential is nonincreasing, including compatible zero states.
At the first hit tau the resulting bound is therefore
`|w_tau|F(r_tau)<=B`.

The weight inequality `1+3^j<=2F(j)` holds at j=0 and is preserved by
`F(j+1)=F(j)(1+3^j)`. For n>=2, the literal initial budget gives
`B>=2F(r)`. For n=1, compatibility at zero forces a even. An initially
zero numerator gives the next state `(2,0,r)`, where the second test fails.
Thus every accepted candidate at n=1 has nonzero even a and `|a|>=2`,
which supplies the same weight bound. Since E>=1, the finite premise
contains both initial tests.

At tau set `d=w_tau-2*3^r_tau`. Multiplying the elementary triangle
bound by the positive `F(r_tau)` gives

`(|w_tau|+2*3^r_tau)F(r_tau) <= B+B*3^r_tau <= 2B F(r_tau)`.

Hence `|d|<=2B<2^(E+1)`. On the original cycle, for
`d=x,w,r ↦ w-(3-x)3^r`, I checked each branch explicitly:

- At original state 1, `2d'=d`.
- At original state 2 with positive denominator exponent, `2d'=d`.
- At original state 2 with exponent zero, `2d'=3d`.

Every compatible step therefore removes exactly one required factor of
two from the initial defect; the optional factor of three is coprime to
two. The available `E+1` transitions starting at tau force
`2^(E+1)|d`. The strict absolute bound makes d zero. This uses the
same unreduced numerator and exponent; no normalization assumption is
silently introduced.

## 4. Formal semantic boundary

`finite_triadic_exact_pair` takes exactly positivity of the original n
and the first `9*binaryBudget n a r+1` compatibility tests. It discharges
the numeric potential, zero, and denominator-weight bounds from that
literal budget and the first two tests. Its conclusion is an actual
state by `8*binaryBudget` with original coordinate one and numerator
`2*3^r_current`.

`exactCycle` records both integer representations of the standard
complementary pair. `exactCycle_next` and `exactCycle_compatible` prove
its invariance under the literal deterministic state rule, including
unreduced denominators. `finite_certificate_alltime` uses the supplied
finite tests before the attained clock and this invariant afterward.
It does not invoke a conjectured all-time candidate or choose a new
candidate at a later clock. `finite_certificate_iff_alltime` adds the
immediate reverse implication.

The infinite autoconjugacy interpretation, uniqueness between two accepted
representations, exact reduced denominator count, first-hit logarithmic
bound and sign classification are written corollaries. The note does
not claim those as additional declarations in the new Lean module.

## 5. Written corollaries

Every first hit from n>2 ends at `4,2,1`. Pulling back dual value two gives
`1/3,1,2` on those three states. At 1/3 the numerator is a ternary unit.
An earlier original-odd pullback doubles it; an earlier original-even
pullback sends `u/3^j` to `(2u-3^j)/3^(j+1)` with j>0, whose numerator
remains a unit modulo three. Thus every earlier original even step adds
one reduced denominator factor. The formula `r_*=b_tau-1` follows.

The original affine relation at its actual first hit is
`2^tau=3^(tau-b_tau)n+C`, with C>=0. Substitution gives the written
clock inequality. C=0 holds exactly when there was no original odd input,
which is precisely the power-of-two case. The equality qualification is
therefore correct.

For n outside {1,2,4}, the first-hit path also contains 8 immediately
before 4. Its pulled-back dual is -1/9. Both earlier complementary inverse
branches preserve negativity. Thus the first sign crossing is exactly
`(8,-1/9)->(4,1/3)` for a successful candidate. This does not turn an
arbitrary shorter compatible sign crossing into a successful certificate.

## 6. Independent fresh strict replay

I copied the two unchanged dependencies and the sealed new source into a
separate review directory and freshly compiled all three with warnings
treated as errors. I generated a separate audit covering every new
declaration: **15 theorem declarations and two definitions**. The audited
axiom union is only `propext`, `Classical.choice`, and `Quot.sound`.

The executable is Lean 4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`; existing Mathlib and package
objects at commit `d13f23b723b8a846827a245b89c10fc7d3f11612` were reused.
The Mathlib tracked checkout was clean. No historical project suite was
rebuilt.

The exact commands, stdout and hashes are recorded in
`lean_rigidity_review/REPLAY_RECEIPT.json`, SHA-256
`ba101e9b87e1da7ec134b7ed06fc6c908483fb7340324dbc841b05da82ea3ea2`.

The result certifies exactness of a supplied successful finite candidate.
It does not establish that every positive n has such a candidate.
