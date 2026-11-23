# Independent review of the actual ordinary return construction

23 November 2026. Reviewer: `density_free_germ8`.
Published parent: `3954c775ba74e1f40776ff38cb4282698d4a334a`.

**Verdict: PASS for R8-O1--R8-O5 within their stated written scopes.
No mathematical correction is required.**

This review independently reconstructs the finite ordinary construction,
its actual scalar bounds, and the high-state estimate. It inspects the
complete control source and the Lean statement boundaries. The parent
owns the separate normal/optimized execution and fresh Lean receipts;
those broad runs were not repeated for this review. No science file
was modified.

## Exact source pins

Paths are relative to `research/repo-synthesis-round8-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `ORDINARY_SELECTOR.md` | `27ac47ee345d3197bcd85d5128419c601da6ebe3` | `78ff6c1742cd4d1799fb2fddea016e299444837a56bb17ee95e4ae4d25237208` |
| `selector_controls.py` | `7093c020392ed3193fcc14f54018d060ab726136` | `de51e5d8c738d7eb8ac7bf812ae050cb0dc1636a02cea65aa547524e285e295e` |
| `OrdinarySelector.lean` | `0296d5bc7faab46351bad7351a4be854050285f6` | `240732a9b7cd101ca035b2ea9b66cb83d9cbadb11dce54a983b34f72f8364dce` |

The actual scalar input is R8-G1 in `GERM_BRIDGE.md`, frozen blob
`540110f09cf68e3309fd83fea9c7ae497536ded4`. This reviewer authored
that dependency; its separate independent review is not claimed here.

## 1. R8-O1: complete ordinary realization and source size

For `D=9^(m+1)` and `a=m+5`, the coefficient `2^(a+4)` is a unit
modulo D. The solution class for t is nonzero because `D>=81>13`.
Its representatives c and c+D in `(0,2D)` have opposite parity, proving
the asserted unique odd t. The quotient u is an integer by construction,
positive, and odd because both its numerator and denominator are odd.

The displayed L and P block equations have positive odd quotients.
They certify exact valuations, not merely powers dividing a numerator.
For every `j<m`, the explicit boundary q_j is 9 modulo 16, and its
L endpoint equals q_(j+1). At the last boundary x, the complete identity
`9x+5=32r` with r odd gives `9x+5=32 mod 64`, hence `x=3 mod 64`.
Thus the final P block is literal. Every intermediate remains a positive
ordinary integer, and the complete affine constant `-29/16` is retained.

From `t<2D` one gets `u<2^(a+5)+1`, hence the integral inequality
`u<=2^(a+5)`. This gives `q<2^(4m+11)`. Separately,
`r<2^(a+1)D<2^(5m+10)`. These bounds are correctly described as
source and endpoint sizes, not stopping times.

## 2. R8-O2: unconditional low endpoint scalar

For the first `a-1` steps from r, the explicit state plus one is
divisible by four. Its next numerator is therefore 2 modulo 4, giving
exact gap one and the next displayed state. The terminal value of this
finite prefix is `v=2*3^(a-1)t-1`.

The scalar identity is exactly
`h(r)=1/2+(h(v)-1/2)/3^(a-1)`.
The size bound `v<2^(2a+4m+4)` and the unconditional actual scalar
upper bound imply

`h(r)<1/2+(12m+31)/(6*3^(m+4))`.

The last expression is below 5/8 precisely when
`48m+124<3^(m+5)`. The stated base case and induction prove this
for all required m. Strict lower bound `h(r)>1/2` is also available
unconditionally. No termination of r or v enters this proof.

## 3. R8-O3--R8-O4: one high visit, expanding returns, and approximation

Both blocks have scalar prefix contribution 7/9. With
`b=h(r)` in `(1/2,5/8)`, backward substitution therefore gives

`h(q_j)=7/8+(b-7/8)/9^(m+1-j)`.

Every block boundary lies strictly between 5/6 and 7/8. An L
intermediate is `3h(q_j)-2`, strictly between 1/2 and 5/8. The P
intermediate is `(4+b)/3`, strictly between 3/2 and 37/24. Together
with the low endpoint, these account for all `2m+3` state occurrences:
exactly one is high and every other one is low.

The complete endpoint equation is
`r=A_m q+7A_m-29/16`, with `A_m=(9/32)(9/8)^m` tending to infinity.
For any prescribed C, choosing `A_m>max(C,1)` makes both the slope
margin and additive remainder positive, so `r>Cq`. Dependence of q
on m does not defeat this inequality. Since `h(q)>5/6` and `b<5/8`,
the potential return ratio is strictly larger than `(4/3)(r/q)`.

The same exact substitution gives

`1/(4*9^(m+1)) < 7/8-h(q) < 3/(8*9^(m+1))`.

The initial actual scalars approach 7/8 from below. Their first L
intermediate scalars approach 5/8 from below. This correctly refutes a
source-independent open neighborhood excluding all actual scalar values
near those phases. It supplies neither equality at the limiting phase
nor one fixed positive integer realizing the infinite limiting word.

## 4. R8-O5: the 35/36 high-state bound

The ratio is exactly
`(3+1/q)h/(2^g(3h-g))`, and `q>=3` bounds the first factor by 10/3.
For g equal to one or two, `h/(3h-g)` decreases on the positive
denominator interval; its value at h=1 yields 5/6 in both cases.

For integer `g>=3`, positivity `h'>1/2` gives
`h/h'<(2g+1)/3`. The resulting bound
`(20g+10)/(9*2^g)` decreases with integral g and equals 35/36 at g=3.
Thus the claimed weak bound follows, with a strict bound in this latter
case. The argument applies to the actual scalar by its unconditional
recurrence and lower bound. It controls one high step, not the complete
low-to-low return constructed above.

## 5. Computational and formal scope

The control program constructs the modular representative directly,
replays every proposed gap, checks the complete affine equations and
source sizes, and propagates exact rational scalar enclosures from the
finite tail prefix. The subsequent finite replays to one are separate
checks permitting exact scalar evaluations; they are not used to fund
the unconditional interval proof. The direct weighted-sum evaluation
agrees with reverse scalar transport, including the standard tail.
All mathematical checks use explicit exceptions and survive `-O`.

The Lean module has eleven public finite arithmetic theorems. The
complete-gap statements concern natural-number source formulas and
odd quotients. The affine iteration and scalar identities and intervals
are over the rationals. The exponential bound and the affine expansion
consequence have their explicit finite hypotheses. The module does not
formalize the actual real scalar, modular existence, the complete
all-parameter attachment to U, the unbounded-family theorem, or the
real-variable 35/36 estimate. Those remain the written arguments
reconstructed above; no stronger kernel-checked scope is inferred.

The resulting obstruction is precise: arbitrarily large actual returns
with only one high visit defeat an amortization based solely on a fixed
reward per high visit. Richer source-sensitive return estimates remain
possible. Controlling unbounded integer scalar carries together with one
unchanged positive ordinary source is still the open obligation.
