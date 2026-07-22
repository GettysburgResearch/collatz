# Source ledger — literature audit wave 5

Only sources actually located during wave 5 appear here. Full theorem inspection is distinguished from abstract-level positioning. No abstract-only source is used as a proof dependency.

## S51 — Väänänen and Wallisser, full p-adic Tschakaloff theorem

**Record:** K. Väänänen and R. Wallisser, *A Linear Independence Measure for Certain p-Adic Numbers*, Journal of Number Theory 39 (1991), 225–236.

**Inspected:** complete twelve-page paper supplied by the repository owner; Theorem 1, its numerical condition, the Padé construction, determinant nonvanishing, and the proof were all inspected.

**Located content:** for

```text
f_q(z)=sum_(n>=0) q^(n(n-1)/2) z^n,
```

with rational `q=s/t`, a prime `p|s`, evaluation points in distinct multiplicative `q^Z`-orbits, and

```text
1+log|s|_p/log max(|s|,t)
 <(2D+1-sqrt(1+4D^2))/(2D),
```

the numbers `1,f_q(y_1),...,f_q(y_D)` have a quantitative `Q`-linear-independence measure.

**Native use:** `LIT-KTHM-0042`. For the PR #20 periodic stack parameter, the source condition holds exactly through `D=9` and fails at `D=10`. This proves irrationality of every eventually periodic positive increment directive of minimal eventual period at most nine.

## S52 — Evertse, Schlickewei, and Schmidt, finite-rank S-unit equations

**Record:** Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics 155 (2002), no. 3, 807–836. DOI `10.2307/3062133`.

**Inspected:** official abstract and theorem scope.

**Located content:** for a fixed linear equation in variables from a finite-rank multiplicative group, the number of nondegenerate solutions—those with no vanishing proper subsum—is explicitly bounded in terms of the number of variables and the group rank.

**Native use:** candidate black box for fixed-word cap-stitch equations in PR #3/PR #33 and successive H-core equations in PR #19/PR #34, after the native expressions are reduced to a fixed finite-term S-unit equation and all proper-subsums are classified. No such reduction is yet complete.

## S53 — Chim, explicit two-term p-adic logarithmic forms

**Record:** Kwok Chi Chim, *Lower bounds for linear forms in two p-adic logarithms*, Journal of Number Theory 266 (2025), 295–349. DOI `10.1016/j.jnt.2024.07.012`.

**Inspected:** publisher abstract and scope statement.

**Located content:** explicit lower bounds for the p-adic distance between two integral powers of algebraic numbers, equivalently explicit upper bounds for valuations of their difference.

**Native use:** candidate quantitative input for PR #19's critical near-Pillai regime and for any fixed cap-stitch reduction of the form `alpha^m-beta^n`. Exact algebraic-number, multiplicative-independence, and exponent hypotheses must be checked before use.

## S54 — Bugeaud, two m-adic logarithms

**Record:** Yann Bugeaud, *Linear Forms in Two m-adic Logarithms and Applications to Diophantine Problems*, Compositio Mathematica 143 (2007), no. 2, 461–480.

**Inspected:** publisher theorem scope and metadata.

**Located content:** explicit estimates for linear forms in two `m`-adic logarithms with applications to exponential Diophantine equations.

**Native use:** an older complementary source for the H near-Pillai and cap-stitch valuations. It does not replace the native reduction to an exact two-term logarithmic form.

## S55 — Dubickas, nearest-integer rational powers

**Record:** Artūras Dubickas, *On the distance from a rational power to the nearest integer*, Journal of Number Theory 117 (2006), no. 1, 222–239. DOI `10.1016/j.jnt.2005.07.004`.

**Inspected:** publisher abstract and bibliographic record; full explicit constants were not obtained.

**Located content:** explicit large and small limit-point bounds for `||xi(p/q)^n||`, with constants depending on `p,q` and a Thue–Morse construction.

**Native use:** specialize to `(p,q)=(81,64)` for PR #16 `T-9315`. The real error language is already a full shift, so the useful comparison is with the nearest-integer block recurrence and its arithmetic stabilization, not with real-cylinder emptiness alone.

## S56 — Dubickas, rational powers in two intervals

**Record:** Artūras Dubickas, *On the powers of 3/2 and other rational numbers*, Mathematische Nachrichten 281 (2008), no. 7, 951–958. DOI `10.1002/mana.200510651`.

**Inspected:** publisher abstract and bibliographic record.

**Located content:** noncontainment results for rational-power fractional parts in certain unions of two intervals.

**Native use:** geometric neighbor for the centered two-arc condition in PR #16. Exact specialization to the four-phase `3/2` schedule and radius `1/81` remains unverified.

## Inspection cautions

- Väänänen–Wallisser gives a direct theorem only through dimension nine for the current parameter. Failure of its numerical hypothesis at dimension ten is not evidence of rationality.
- The S-unit theorem applies only after a fixed finite-term multiplicative-group equation and a complete proper-subsum audit are supplied.
- Explicit p-adic logarithmic-form theorems require exact algebraic inputs and multiplicative-independence hypotheses; the phrase “near-Pillai” is not enough.
- Dubickas's `(81,64)` constant and two-interval inequalities have not yet been specialized from the full source.
- No source in this ledger constructs a positive ordinary Collatz counterexample or proves the conjecture.
