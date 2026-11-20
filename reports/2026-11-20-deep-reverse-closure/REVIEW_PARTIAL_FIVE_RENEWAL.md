# Independent reconstruction of the partial physical five renewal

**VERIFIED for sections D/E of `CLOSING_ATTEMPTS.md`, SHA-256
`fe6c06c541337246295e7747c606d314e45c844dba8176622b6e391b6db4d64e`.**
This primary-agent reconstruction is distinct from
the author of that note. It does not establish finiteness of the uncovered
energy, a positive occupation upper bound, or Collatz.

The imported physical statement is PR162,
`2279da37ac612dbe049777354cdedb3c0aa03282`,
`research/creative-closure-20261120/five_closure.md`, C5-001. The primary
agent read that proof and `occupation.md` at the same full head.

For `x=64u+49`, the actual six-step paths end at `9u+7` and `5(9u+7)`.
The odd inputs occur at clocks 0 and 2 on the lower arm, and 0 and 5
on the multiplied arm. Common trailing halvings therefore give the exact
pair `(q,5q)`, where `q=oddpart(9u+7)` is a positive odd ternary unit.
Furthermore `x>=7(9u+7)>=7q`, since the first difference is `u>=0`.
This proves the defect identity and the claimed decrease on the entire
stated source progression, without an assumption of convergence.

For fixed odd unit `q`, the inverse equation is
`9x+7=2^ell*q`, with `ell>=6`. Because the order of 2 modulo 9 is six,
the integral clocks form one residue class modulo six. Positivity is
automatic at the first allowed clock: `2^ell*q>=64q>7`. Removing nonunit
sources only reduces the nonnegative sum. The successive members before
that removal satisfy `x_(ell+6)=64*x_ell+49>=64*x_ell`.
Every member lies in `x=49 mod64` and hence is at least `7q`. Summing
these disjoint exact inverse fibers proves

`sum x^(-s) <= 7^(-s)/(1-64^(-s)) * q^(-s)`.

If `x<=M`, its target is at most `M/7`. Regrouping the **finite** source
sum gives the stated truncated inequality with its uncovered remainder.
Each metric distance is finite, even if the metric label is unbounded.
Thus when `kappa_s<1`, one may use `E(s;M/7)<=E(s;M)` and subtract
`kappa_s E(s;M)` within this finite inequality. This yields the uniform
bound `E(s;M)<=R(s;M)/(1-kappa_s)`, followed by monotone passage to the
full sum. It never subtracts two infinite quantities. The converse
finiteness implication follows simply from `R<=E`.

The constants are correct: `kappa_1=64/441`, and for `s=.84>1/2`,
`7^s>2`, `64^(-s)<1/8`, so `kappa_s<4/7<1`. No floating-point
estimate or empirical extrapolation is needed.

The source unit guard is retained throughout. A paired inverse selector
only constructs larger examples and does not prove that every remaining
source can descend into this one class. The remainder therefore stays
an infinite unbounded source domain.

Finally, a killed deterministic pushforward satisfies
`||sum_j H^j r||_1=sum_u r(u)*tau(u)` for nonnegative input, with
infinite values allowed, by Tonelli and direct original-source counting.
For a terminating source, `tau` counts its nonabsorbed returns; for a
surviving source with positive input weight, the sum is infinite. This
confirms the exact mass obligation for countably many Poisson repairs.
The source's first-hit capacity changes this counting rule, and is not
an ordinary invariant label. No conversion of those constructions into
the missing five-boundary remainder estimate is justified.
