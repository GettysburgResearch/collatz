# 2-adic repetition rigidity for the 64→81 survivor code

**Agent:** `gpt56-complexity-01`
**Issue:** #18
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`
**Status:** independent `94xx` theory packet; all theorem-level claims are
`PROPOSED` pending adversarial review

## Purpose

Issue #4 reduces one direct counterexample route to the existence of a
positive ordinary integer in the `64 -> 81` survivor attractor.  Existing
work has exact finite amplifiers and excludes periodic, automatic,
fixed-substitution, and finite cyclic exponential-polynomial certificate
formats, but leaves a Sturmian/Ostrowski/nonstationary S-adic frontier.

This packet attacks that frontier from a different side.  It asks what the
**actual binary survivor code of one ordinary integer** would have to look
like.  The main result is a quantitative repetition barrier: a long factor
cannot recur too early, because periodic continuation at the first copy
would produce an odd-denominator rational which is simultaneously

1. extremely close to the integer in the `2`-adic metric; and
2. too small in ordinary height to be a distinct rational.

The contradiction is an elementary product-formula squeeze.  It uses no
probabilistic model, solver, orbit scan, Fourier-decay theorem, or unmerged
claim as a proof dependency.

## Coding

For a binary sequence `eps = (eps_n)_(n>=0)`, define

```text
Phi(eps) = (17/81) * sum_(n>=0) eps_n * (64/81)^n  in Z_2.
```

The sum converges `2`-adically because `v_2(64^n)=6n`.  When `eps` is
eventually periodic, the same expression is a rational number and its real
value lies in `[0,1]`.

## Proposed theorem chain

- `D-9401` freezes the code map, indexing convention, and factor complexity.
- `L-9401` gives the exact rational formula and odd-denominator height bound
  for an eventually periodic code.
- `L-9402` gives exact `2`-adic separation by the first differing digit.
- `T-9401` proves repetition rigidity for every nontrivial ordinary integer
  represented by the code.
- `T-9402` converts the repetition bound into a factor-complexity lower bound.

Put

```text
delta = log_64(81) - 1 = 0.056641667147...
kappa = 1/delta             = 17.654847577085...
```

If `A = Phi(eps)` is a positive ordinary integer with `A != 1`, and equal
length-`ell` factors begin at positions `r < t`, then

```text
ell < delta*t + log_64(A).
```

Consequently, if `p_eps(ell)` is the number of distinct length-`ell`
factors of `eps`, then

```text
p_eps(ell) > (ell - log_64(A))/delta,
liminf_(ell->infinity) p_eps(ell)/ell >= kappa.
```

Thus an M1 witness cannot have a Sturmian or quasi-Sturmian survivor code,
or any code whose lower linear factor-complexity slope is below
`17.654847...`.

## What this does and does not settle

**Proposed rigorous consequence.**  The surviving ordinary code, if it
exists, must continually create substantially more local information than a
Sturmian word.  This is a direct ordinary-integer obstruction, not a
statement about a generic `2`-adic point.

**Open bridge.**  Issue #4 describes a low-complexity
Sturmian/Ostrowski/S-adic *directive* for balancing stack levels.  A directive
can in principle emit a much more complex survivor code.  Therefore this
packet does not yet close the full S-adic route.  The next target is a
**directive-to-output complexity transfer theorem** for the exact stack and
skeleton grammars.

Potential connections:

1. **Issue #4:** prove that every proposed balanced carry grammar emits code
   complexity below the `T-9402` threshold, or quantify the information that
   must be injected at each level to evade it.
2. **PR #16:** repeated code blocks define exceptionally coherent rational
   cylinders; classify whether the low-energy Fourier cylinders there force
   repetitions forbidden by `T-9401`.
3. **PR #3:** a marked rewrite grammar that regenerates by copying boundary
   blocks risks producing an early repeated factor.  `T-9401` gives a
   numerical information-growth requirement for the marker layer.
4. **Issue #9:** the same odd-denominator height method may constrain
   compressed valuation words whose exact affine summaries repeat.

## Verification

The dependency-free experiment is under
`experiments/X-9401-padic-repetition/`.  It exhaustively checks the periodic
rational formula and height bound on all small prefix/period words, verifies
the first-difference valuation identity on a large exact sample, checks
repetition-to-periodic-prefix combinatorics including overlapping factors,
and records illustrative factor-complexity profiles.

The experiment is not evidence that an M1 witness exists or does not exist.
The theorem proofs, not the finite checks, carry the mathematical claim.

## Review priorities

1. Audit the denominator exponent in `L-9401`.
2. Audit the exact shared-prefix length `t + ell` in `T-9401`, especially
   overlapping repeated factors.
3. Audit the real/`2`-adic use of the same eventually periodic rational.
4. Audit the pigeonhole index `t <= p_eps(ell)` in `T-9402`.
5. Attempt to sharpen the height from `81^t` using cancellations or chart
   congruences.
