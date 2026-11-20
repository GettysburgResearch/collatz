# Narrow mathematical check of actual unsafe transport

## Frozen scope and independence

Reviewed file: `ACTUAL_TRANSPORT.md`, SHA-256

```
d4e493edf472ead85c4ca0a9db0b4167579d287c901b6e88236f206e03a4ec3b
```

Source checkout: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The relevant source files are:

- `research/astra-three-routes/pass4/MOVING_GHOST_RANK.md`, T-A3-901/902;
- `research/astra-three-routes/pass5/RANK_MOMENTS.md`, T-A3-1001 and
  R-A3-1003(a);
- `research/astra-three-routes/pass5/UNSAFE_REPAYMENT.md`, sections 1–2;
- `research/integrated/renewal-transport/README.md`, for the existing
  source and review boundaries.

A separate agent reconstructed AT1–AT4 from these definitions rather than
using the new author's numerical output. The same reviewer contributed
to AT5 and its approximate-eigenvector argument and then checked the final
written proof. AT5 is consequently a collaboratively developed, checked
deduction; it is not advertised as an independent-origin or external peer
review. No formal proof-assistant verification is claimed. The verdicts
below concern deductions from the stated A/R source interfaces and do not
promote every neighboring claim or later file revision.

## Claim verdicts

| Claim | Verdict | Exact boundary |
|---|---|---|
| Total unsafe return B | VERIFIED from the stated interface | After the first A step, each further quarter-safe step reduces a positive integer rank by at least four; the excursion therefore terminates in U or 1. |
| AT1, every positive power moment can be destroyed | VERIFIED | A separate full-support summable input is supplied for each p>0. This is a domain obstruction, not an assertion that any particular ordinary orbit diverges. |
| AT2, logarithmic domain preserved | VERIFIED | Norm amplification is at most 6 per unsafe return, and at most `6^q` for the qth power of the logarithm. It is not a contraction. |
| Safe occupation estimates (9)–(11) | VERIFIED | They require the actual safe-entry distribution to have the specified logarithmic moment; the source-tail and quantitative bounds have the stated hypotheses. |
| AT3, log-log budget | VERIFIED | The budget grows with the number of unsafe returns. Finite psi-moment is required for a finite numerical bound. |
| AT4, Cesaro tightness criterion | VERIFIED AS A CONDITIONAL IMPLICATION | Uniform tightness and exclusion of nonabsorbing finite B cycles remain unproved. Full support of the initial finite mass is essential to cover every ordinary source. |
| AT5, essential norms and spectral radii | CHECKED; REVIEWER CONTRIBUTED | Every positive power has essential norm one on the specified weighted space. The proof uses finite ordinary cylinders and compact output-tail control. |
| Approximate spectral point 1 | CHECKED; REVIEWER CONTRIBUTED | Different finite ordinary shadows give the vectors. No infinite positive periodic shadow is inferred. |
| Collatz convergence | OPEN | None of the proved estimates supplies the source-persistent tightness or a complete cycle exclusion required by AT4. |

## Reconstruction of the operator calculations

The operator convention is source-to-endpoint:

```
(Hf)(y) = sum_{u in U: B(u)=y} f(u),   y in U,
```

with mass killed at 1. In particular, its weighted column norm at u is
`w(Bu)/w(u)` if that return survives, and zero otherwise. This is the
pushforward of the actual transported input. It is not a new distribution
drawn at each return.

For AT1, set `x_j=3^(4+16j)` and
`y_j=(9x_j+7)/16`. The source identity gives `B(x_j)=y_j`,
`R(x_j)=x_j`, and `R(y_j)>= (25/729)x_j^2`. Giving x_j the mass
`R(y_j)^(-p)` makes its output p-moment equal to one while its input
p-moment is at most `(729/25)^p x_j^(-p)`. The input series converges
geometrically for every p>0, and the output series diverges. Adding
`1_U R^(-p-1)` supplies full support; its input p-moment is bounded by
the source theorem `sum 1/R <=55/6`. Nonnegativity prevents cancellation.

For AT2, each step in the chain

```
R(A(n))+6 <= (A(n)+5)^2 <= (n+5)^6 <= (R(n)+6)^6
```

has the correct direction. The first follows from `R(m)<=m^2` and is
also valid at the killed endpoint m=1. The second is the square of the
source height bound. The third uses `n-1<=R(n)`. Later safe steps decrease
R, so the inequality also bounds the surviving B endpoint. Taking logs
and then summing source masses gives the stated bound without any input
envelope or equidistribution assumption.

For safe occupation, an initial rank r can support at most
`1+floor(log_4 r)` visits to G. A visit surviving to occupation index J
requires `r>=4^J`. These two facts prove the source-tail bound directly.
For q>1, writing s for the number of visits, use
`(s-J)_+ <= s^q J^(1-q)` and
`s <= (1/log 7 + 1/log 4) log(R+6)`.

For AT4, tight Cesaro distributions have an ordinary ell-one convergent
subsequence and preserve their limiting mass. The telescoping identity
`H mu_N-mu_N=(H^N f-f)/N` makes its limit invariant. Invariance forces
zero mass at killed inputs and their finite predecessors; positive mass
on an infinite injective orbit would contradict finite total mass, and
positive preperiodic influx into a cycle is also impossible. Thus a
nonzero invariant measure must charge a finite cycle. Equivalently, one
can see the nonperiodic obstruction directly: a deterministic orbit
without repeated states visits a finite set F at most `|F|` times. Its
positive initial atom would leave at least that fixed amount of Cesaro
mass outside every F asymptotically, contradicting uniform tightness.

## Reconstruction of the spectral boundary

Fix j and take `K=floor(j/2)+1`. The conditions

```
n=10 mod243,   v2(17n+73)=6K,   n>=11
```

define an infinite ordinary arithmetic progression. The source's exact
`111010` calculation supplies more than j successive unsafe sources.
Thus `B^j(n)=A^j(n)` on this prefix, and this endpoint is a fixed affine
function of n with positive slope. Both endpoint and initial ranks are
quadratic in n. Their psi-weight ratio tends to one as n grows in this
fixed progression.

For the essential-norm upper bound, truncate finitely many input columns.
The remaining ratios are bounded by
`1+j log(6)/psi(n)` and their excess tends to zero, since psi is proper.
For the lower bound, apply a compact perturbation to normalized atoms
`delta_n/psi(n)` along the progression. The true outputs escape all
finite endpoint sets with norm tending to one, whereas compact images
of a unit ball have uniformly small weighted output tails. This proves
distance one from every compact operator. It does not use the false
claim that the ell-one unit basis is weakly null.

The power bound grows at most linearly, so Gelfand's formula gives
spectral radius at most one. Essential norms of every positive power
equal one, giving both spectral radii equal to one.

For the approximate eigenvectors, every fixed finite shadow has distinct
affine slopes: the slopes are `(81/64)^k` and
`(27/16)(81/64)^k`. Cross-parity equality would require an exponent of
three divisible by four to equal one congruent to three modulo four.
Consequently any coincident values can occur at only finitely many
parameters for a fixed horizon; sufficiently large progression members
avoid all of them. The normalized finite occupation vector telescopes
under `I-H` to its two endpoint atoms, giving the printed residual
`(2+1/J)/(J-1)`. Taking successive starts beyond all previous supports
gives vectors at pairwise distance two. A left inverse modulo compact
operators would force a convergent subsequence and is therefore
impossible. This verifies the essential spectral point 1.

Additional killing at a fixed ordinary floor preserves every upper bound.
For a fixed finite shadow each physical intermediate state has a positive
affine slope in n, so sufficiently large ordinary members avoid the floor
altogether. The lower spectral bounds and AT1's direct unsafe family
therefore survive such killing.

## Computational evidence actually obtained

In addition to the written reconstruction, a separately implemented exact
integer calculation checked 24 shadow horizons, totaling 324 unsafe A
edges. It reconstructed the CRT class, active modes 3/1, maximal count
one, quadratic rank identities, strict unsafe guards, affine endpoints,
and distinct physical A states. These finite checks support the arithmetic
interfaces; the unbounded spectral and moment conclusions follow from
the proofs above, not from increasing the sample horizon.

For the attachment audit, `check_routes_1_5.py` passed both normal Python
and Python `-O`, with the same printed local results. No repository-wide
validation, Lean build, remote CI, or GitHub publication is claimed by
this reviewer; those are separate publisher actions.

## Practical interpretation

The new space preserves finite moments under actual unsafe transport. Its
critical spectral point also survives: this rules out a uniform strict
spectral-gap argument on this particular space. Strong stability in
ordinary unweighted ell-one is equivalent to eventual absorption of each
point mass and hence to Collatz. Weighted strong stability for every
finite-psi-moment input does not follow merely from pointwise absorption,
because the proved weighted power bound is not uniform in time.
