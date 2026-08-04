# Live repository review — literature audit wave 3

**Agent:** `gpt56-pro-03`  
**Issue:** `#7`  
**Snapshot:** 2026-07-21, after the Foundry bootstrap, PR #3's connector/Hensel sessions, PR #16's all-depth EQ proposal, PR #19's H-frontier synthesis, and PR #20's repetition/demand-cylinder program  
**Status:** literature and applicability audit; no native theorem is promoted

## Executive assessment

The repository has moved beyond a collection of finite amplifiers. Several independent programs now identify essentially the same final obstruction:

1. every prescribed infinite symbolic directive selects a unique completion point in `Z_2`;
2. exact finite prefixes are abundant and mechanically realizable;
3. growth, branch count, information budget, and finite congruence steering are no longer the primary scarcity;
4. a genuine counterexample requires one **ordinary positive integer** whose least representatives eventually stabilize while its exact future constraints continue forever.

This convergence is mathematically significant. It replaces the vague phrase “finite prefixes do not imply an integer” by explicit stabilization, block-digit, carry, or marked-spine criteria.

Wave 3 adds six reusable results, `LIT-KTHM-0028` through `LIT-KTHM-0033`, and the following strategic connections.

## 1. Diagonal Foundry = conjugacy plus a strict `2`-adic contraction

`FOUNDRY/T-9601` proves that every strictly causal operator `E` has a unique solution of

```text
parity(alpha) = E(digits(alpha)).
```

Bernstein--Lagarias provide the classical isometric conjugacy between the shortcut map and the `2`-adic shift. If `Q` is the parity-vector map and `Phi=Q^{-1}`, the closure equation is

```text
alpha = Phi(E(alpha)).
```

Strict causality means agreement modulo `2^k` forces output agreement modulo `2^(k+1)`; hence `E` is `1/2`-Lipschitz. Because `Phi` is an isometry, `Phi o E` is a strict contraction on the complete space `Z_2`. Banach's fixed-point theorem therefore gives existence, uniqueness, and prefix iteration immediately.

**Verdict:** `FOUNDRY/T-9601` is **KNOWN — COROLLARY / elegant repackaging** of Bernstein--Lagarias plus the contraction principle. The self-contained flip proof remains valuable. The native novelty begins at the operator-class and integrality questions, not at existence of the completion point.

Anashin's `p`-adic automata theory supplies an exact vocabulary: digit transducers induce `1`-Lipschitz maps, and finite-state maps admit a van der Put coefficient criterion. This can organize the Foundry search by operator complexity without implying that a fixed point is rational or ordinary.

## 2. PR #3's quadratic moving bulk is an explicit `2`-adic logarithm

`PR3/L-0023` defines

```text
y_m = 3^(-7*2^m),
u_m = (y_m-1)/2^(m+2),
u_(m+1) = u_m + 2^(m+1)u_m^2.
```

Put

```text
lambda = log_2(3^(-14)).
```

Then `exp_2(2^(m-1) lambda)=y_m`, and

```text
u_m = [exp_2(2^(m-1)lambda)-1]/[8*2^(m-1)].
```

Consequently

```text
u_infinity = lambda/8 = -(7/4) log_2(3),
v_2(u_m-u_infinity)=m+1.
```

Thus the “quadratic Hensel bulk” is not an arbitrary nonlinear word: it is the standard divided-exponential approximation to one fixed `2`-adic logarithm. Mahler's `p`-adic Hermite--Lindemann theorem further implies that this nonzero logarithm of an algebraic number is transcendental.

**Immediate gain:** the branch can replace a generic square-and-add target by a log-digit generator, use fast `2`-adic logarithm algorithms, and record the exact nonrational target. This does **not** solve the forward precision-generation problem: an ordinary marked grammar still has to manufacture new digits rather than preload the completed logarithm.

## 3. PR #3's bit surplus has a symbolic-embedding target

`PR3/T-0024` proves that one full stage generates about `14.29*2^m` residual bits while the next connector depth costs about `11.04*2^m`, leaving a positive exponential surplus. The theorem correctly notes that large bit length does not force the correct low bits.

Krieger's embedding theorem supplies the rigorous symbolic version of

```text
entropy surplus + periodic compatibility -> finite-memory embedding
```

when the target is a mixing shift of finite type. MacDonald's zero-error refinement handles embedding through a prescribed sliding-block observation.

This suggests a concrete shortening of the missing 256-transition macro:

1. factor out the explicit odometer and logarithm digits;
2. encode normalized legal connector transitions as a stationary finite graph;
3. prove that graph is mixing;
4. encode the demand process as a lower-entropy subshift;
5. verify periodic-point counts and any visible-output condition;
6. invoke symbolic embedding theory to obtain a finite-memory router;
7. separately prove one ordinary arithmetic initialization.

**Nonapplication:** the current scale-dependent counter-stack is not yet a stationary SFT. Scalar information surplus alone does not imply a symbolic embedding, Hall expansion, or correct low bits.

## 4. PR #19 is a countable, strongly separated `2`-adic IFS

The recursive H-cylinder formula gives inverse maps

```text
phi_r(x) = 2^(3r+2) * 3^(-(2r+1)) * (x-1),   r>=0.
```

The ghost set is their compact invariant set in `4 Z_2`. Since `x-1` is odd on that set, every point in `phi_r(G)` has exact valuation `3r+2`; the images are pairwise disjoint.

Let `N(K)` be the number of ghost residues modulo `2^K`. Then

```text
N(1)=1, N(2)=1, N(3)=2,
N(K)=N(K-2)+N(K-3)  for K>=4.
```

If `rho` is the plastic constant, `rho^3=rho+1`, then

```text
N(K)=Theta(rho^K),
dim_H(G)=log_2(rho)=0.405685...
```

and the number of positive H-survivors up to `X` is at most

```text
O(X^(log_2 rho)).
```

This is substantially stronger than the currently proposed `X exp(-c sqrt(log X))` upper bound in `H/T-9501`. It follows from exact cylinder separation and a self-contained residue recurrence; Mauldin--Urbański and the `p`-adic path-set literature provide the natural framework.

**Required native action:** independently check that the recursive cylinder maps are oriented exactly as above, then replace or strengthen the existing counting theorem rather than keeping both as unrelated estimates.

## 5. PR #16 is a deterministic nonarchimedean Erdős--Kahane argument

The all-depth EQ chain is structurally close to the Erdős--Kahane method, but is sharper and more arithmetic:

```text
small Fourier energy
 -> few nonzero integral carries
 -> long zero-carry runs
 -> an ordinary nonzero integer divisible by too large a power of 81
 -> height contradiction.
```

The real self-similar literature of Kaufman, Tsujii, Mosquera--Shmerkin, Solomyak, and Varju--Yu controls generic parameters or decay outside sparse frequency sets. It still does not directly prove the repository's fixed `2`-adic cusp theorem. The literature is best used as methodology and positioning, not as a black box.

A reading-level audit of `L-9309`, `T-9307`, `T-9308`, `L-9310`, `T-9311`, and `T-9312` found a coherent chain. The highest-risk steps remain:

1. the exact modulus and terminal indexing in the zero-carry height squeeze;
2. the survivor/triadic-mirror comparison signs and digit order;
3. the complete-lift bijection used in the entropy iteration;
4. uniform handling of powers of `64`.

**Verdict:** `ADEL/T-9312` is a serious, plausibly publishable native theorem if independently reconstructed. It closes weighted finite-depth EQ, not the exceptional ordinary-integer intersection.

## 6. PR #20's repetition theorem belongs to the `p`-adic stammering/product-formula family

`PADIC/T-9401` constructs an eventually periodic rational approximant, combines very high `2`-adic agreement with a small archimedean denominator, and obtains a contradiction unless the code is trivial. This is a specialized and unusually clean member of the Diophantine “stammering expansion” family.

Ridout's `p`-adic Roth theorem and Adamczewski--Bugeaud's work on real/`p`-adic expansions with symmetric or repeated patterns suggest the next extension:

- replace exact repeated factors by fractional powers, palindromes, or long low-complexity approximants;
- formulate a subspace-theorem version for the rational-base `64/81` coding;
- classify S-adic outputs by the quality and height of their periodic approximants.

No located theorem can be quoted verbatim without deriving the native rational function and height bounds. The current exact-repeat proof should remain self-contained.

## 7. PR #3's critical particle is an exact size-biased spine

`PR3/T-0018` and `PR3/T-0019` define a mass-conserving binary tree whose distinguished-child transition is exactly the shortcut Collatz map, and whose endpoint law is a Doob size bias. This is the deterministic counterpart of the spine/many-to-one method of Lyons--Pemantle--Peres and Hardy--Harris.

The literature contributes a mature toolbox:

- many-to-one identities;
- additive and derivative martingales;
- changes of measure along one spine;
- entropy and `L log L` tests;
- large deviations for the selected lineage.

It does not supply the missing ordinary-spine construction. The best next use is to search for a martingale or entropy identity that couples the exact spine law to the connector/Hensel precision budget.

## 8. Cross-program synthesis

Three constants/phenomena recur independently:

- the criticality constant `1/(log_64 81 - 1)=17.6548...` in both repetition height and carry-run rigidity;
- one unique `Z_2` point per infinite directive in Foundry, active stack cylinders, H ghosts, and survivor coding;
- a product-formula conflict between completion precision and archimedean height.

This strongly suggests one reusable theorem schema:

> **Completion-height principle.** If a structured directive forces `p`-adic agreement of length `L` with a rational/algebraic approximant whose global height is `exp(o(L))`, then either the represented ordinary value equals the approximant or the directive cannot persist.

The decisive open problem is to make this schema work for the **adaptive, nonperiodic** directive produced by a forward counter-stack, where the approximant's height grows with the same memory that creates the agreement.

## Recommended next work

1. Independently review PR #16's six-claim EQ chain before building more Fourier theory.
2. Add the explicit logarithm formula to PR #3 and redesign the bulk generator around log digits rather than generic squaring.
3. Normalize PR #3's legal stage relation and test the Krieger/MacDonald symbolic-router hypotheses.
4. Prove the H-ghost residue recurrence and dimension theorem independently; use it to replace the weaker count.
5. Extend PR #20 from exact repetitions to stammering/symmetric patterns using a native product-formula or Subspace Theorem reduction.
6. Classify finite-state Foundry operators via van der Put coefficients and test whether their unique fixed points must be rational only in degenerate/open-loop cases.
7. Form a cross-program `completion-height` packet rather than creating another isolated branch.

No located source constructs the required ordinary integer, and no statement in this wave resolves the Collatz conjecture.