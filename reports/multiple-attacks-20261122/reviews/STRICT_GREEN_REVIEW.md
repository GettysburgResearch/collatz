# Independent review of the strict Green correction

**Verdict:** the operator argument in
`multiattack_root/STRICT_GREEN_VOLTERRA.md` is sound under its explicit
retained-path counting input. The conclusion concerns the strict
immigration correction `K=SLD` on the killed nonperiodic domain. It does
not imply decay of the original transport or exclude the removed cycles.

## Domains and compactness

For `theta<s<=1`, multiplication by `omega(n)=1/(3n+1)` maps
`X_s=ell^1(N,n^(-s))` boundedly into **unweighted** `ell^1`, because
`n^s*omega(n)<=1/3`. Transport `L` has unweighted norm at most one,
including loss at the killed boundary. The retained-path occupation
bound makes `S:ell^1->X_s` bounded with norm at most `C_s`, and its
output-height tail is at most `C_s X^(theta-s)`. Output projection has
finite rank, so this proves compactness. No boundedness or closability
of `L` on `X_s` is used.

The notation `||Da||_1` must be rendered `||Da||_(ell^1)` in this
factorization; otherwise it conflicts with the defined weighted norm
at `s=1`. This is a notation correction, not a gap in the inequality.

## Exact coefficients and the inverse

The killed domain has no periodic states. Thus each source-target pair
has at most one positive forward hitting depth, and each physical path
orders its own intermediate states. The coefficient of `K^j` selects
exactly `j-1` strictly increasing interior positions and multiplies
their immigration weights, together with the initial source weight.
No globally well-ordered enumeration of all states is necessary.

The elementary-symmetric-polynomial bound is legitimate on finite
segments and passes monotonically to infinite paths. The full path
immigration sum is at most `C=200/3`, so the displayed factorial bound
`||K^j||<=A_s C^(j-1)/(j-1)!` follows by the weighted `ell^1` column
criterion. This gives a norm-convergent Neumann series for **every**
complex parameter, with both left and right inverse identities.

The inverse sign is correct: the off-diagonal coefficient is
`-z omega(n) product_(n<u<q)(1-z omega(u))`. In particular, the
`z=1` factors are `3u/(3u+1)`. The entire inverse is not asserted
positive on arbitrary positive inputs. The exponential absolute
majorant and finite-source density justify its infinite-source kernel.

## Projections and physical clocks

For `s<1`, the omitted input tail is bounded by `A_s Y^(s-1)`;
the omitted output tail is bounded by `A_s X^(theta-s)`. Their sum
is the claimed operator-norm error. At `s=79/80`, both exponents are
`-1/80` and `A_s=395/3`.

Every finite input-output matrix entry stabilizes under increasing
physical clock truncation because a source-target hit is either absent
or occurs at a unique finite depth. This proves existence of a common
stabilizing clock for the finite matrix. It does not provide a decision
procedure for absent hits, which the note explicitly acknowledges.
Combining that fact with the two norm tails proves convergence of the
full clock truncations. The same reasoning applies to shortcut clocks.

Every truncation or projection used has a nonnegative kernel dominated
by `K`. Its powers are therefore dominated by the corresponding powers
of `K`, so the same factorial majorant and entire inverse bound apply.
The stated resolvent-difference bound has the correct order and sign.

## Endpoint witness

The six mod-nine parent formulas in Section 6 are exact. Every chosen
parent is an odd ternary unit at least twice its target and has the
displayed exact valuation. Starting at 5 gives a strictly increasing
inverse ladder with first odd hitting depth exactly equal to the
ladder index. All its sources converge through 5 to 1, hence belong to
the killed nonperiodic domain before they enter the cycle.

For a source of index `j>N`, the target-5 coefficient of the truncated
operator is zero, while the full coefficient is `omega(n_j)`.
Dividing the target-5 weighted output by the source norm at `s=1`
gives `n_j/[5(3n_j+1)]`, tending to `1/15`. Consequently the claimed
endpoint norm lower bound is valid as a supremum. It is compatible with
the convergence theorem's strict hypothesis `s<1`.

The arithmetic and first-hitting-depth statements are separately
checked in `OddDepthLadder.lean`, using pinned mathlib `Nat.ordCompl`
and the existing ordinary `CollatzShell.orbit` through `ShellCover`.
This formalization does not pretend to formalize the Banach-space
argument or its imported path-count theorem.
