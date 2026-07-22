# Latest checkpoint — cross-repo sweep and phase-allocation closure

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Draft PR:** #20  
**Status:** every theorem-level claim below is `PROPOSED` pending independent reconstruction

## Existing periodic theorem chain

```text
L-9408  exact finite-word / repeated-block transfer
   |
L-9409  scalar Gaussian-binomial Padé
   |
T-9412  constant-increment irrationality
T-9413  eventually constant irrationality
   |
L-9410  simultaneous block Gaussian-binomial Padé
   |
T-9414  every positive periodic word of length <=3 is irrational
T-9415  every finite prefix followed by such a tail is irrational
```

The equal-allocation exponent is

```text
mu_r
 =[1/log_64(81)]*(1+1/[r(r+1)]).
```

Hence

```text
r=1: 1.419591945535... >1,
r=2: 1.104127068750... >1,
r=3: 1.025260849553... >1,
r=4: 0.993714361875... <1.
```

No positive periodic stack word of minimal period at most three selects an
ordinary initial context. An arbitrary finite steering prefix cannot repair such
a tail.

## Cross-repository sweep

The latest live work supplied four relevant interfaces.

1. **PR #33:** a general exact cylinder-block recurrence and a finite-trap
   nonstabilization theorem for uniformly contracting integral transitions.
   The raw active stack is supercritical, so the trap theorem does not transfer
   without a new renormalized height.
2. **PR #16:** independent carry rigidity with the identical criticality constant,
   all-depth EQ, a centered rational-power ordinary-section equivalence, and an
   exact depth-46 nontrivial survivor minimum above `2^227`. These reinforce the
   completion-height strategy but do not repair the period-four Padé deficit.
3. **PR #3:** a forward positive ordinary quadratic bulk generator that creates
   finite connector bits. Exact residual-cylinder routing remains open.
4. **Issue #21:** finite-state feedback collapses to an open-loop tail for an
   ordinary integer; one-counter/S-adic tails remain the genuine frontier.

See `CROSS_REPO_SWEEP_2026-07-22.md` for the full status and dependency audit.

## New exact result — unequal phase allocation is closed

`L-9411` constructs the complete phasewise root-product denominator with
arbitrary cancellation lengths

```text
n_0,...,n_(r-1).
```

`T-9416` proves that if `p_j=n_j/sum n_i`, then the universal pre-reduction
valuation-to-height shape satisfies

```text
min_j e_j(p)/h(p)
 <=(r^2+r+1)/(r(r+1)),
```

with equality only at

```text
p_0=...=p_(r-1)=1/r.
```

Thus equal allocation is uniquely optimal throughout the entire phasewise
root-product class. At period four every unequal allocation remains below

```text
0.993714361875...<1.
```

`R-9404` records the resulting refutation: moving the existing roots between
phases cannot repair the deficit.

## External theorem audit

`R-9405` audits Rochev's broad 2011 p-adic q-series theorem. The periodic stack
phase vector is exactly Tschakaloff-type, but its natural parameter

```text
q=(81/64)^(9S|W|)
```

expands at both the `2`-adic and archimedean places. The inspected p-adic theorem
uses one expanding place and nonexpansion at the others. It therefore cannot be
quoted directly for the stack values.

This confirms that the period-four obstacle is a real global-height problem.

## Verification

`X-9410` exhausts every weak phase allocation for

```text
2<=r<=7,
1<=D<=18.
```

It checks `657,774` exact vectors. Every shape lies below the theorem bound and
every finite maximizer is balanced.

```text
SHA-256
aab92d29cf446b13c39c9e7eb9cc681c09f4199bf52d6ae0ee6a9ffa923d2259
```

Finite checks validate the asymptotic functional interface only. `T-9416` is the
proof.

## Current boundary

Closed within the current Padé architecture:

```text
- constant and eventually constant tails;
- periodic tails of minimal period 2 and 3;
- arbitrary unequal phasewise root allocation;
- direct use of the inspected single-expanding-place q-series theorem.
```

Still alive:

```text
- quadratic-scale gcd reduction;
- cross-phase cancellation;
- adjacent-order Casoratians with linearly growing cancellation depth;
- phase-sensitive Hermite–Padé using P_W;
- completion-height determinants using PR #16 / PR #33 coordinates;
- the balanced nonperiodic 17/18 directive.
```

## Review first

1. `claims/L-9411-phase-allocation-root-product.md`
2. `claims/T-9416-equal-phase-allocation-optimality.md`
3. `claims/R-9404-unequal-phase-allocation-shortcut.md`
4. `claims/R-9405-rochev-single-place-near-miss.md`
5. `CROSS_REPO_SWEEP_2026-07-22.md`
6. `Q-9412-coupled-period-four-determinants.md`
7. `experiments/X-9410-phase-allocation/run.py`
8. `claims/L-9410-block-gaussian-pade.md`
9. `claims/T-9414-short-period-irrationality.md`

## Next theorem target

Construct a **genuinely coupled** period-four approximant. A successful object
must cancel a number of combined phase coefficients proportional to Padé order,
prove nonvanishing, and report exact reduced height. A bounded extra cancellation
or a phasewise root redistribution cannot alter the quadratic exponent.