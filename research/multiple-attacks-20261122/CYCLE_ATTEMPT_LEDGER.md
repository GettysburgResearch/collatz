# Arbitrary-cycle attack: exact renewal certificate and remaining clock cost

**Status:** a reviewed attempt ledger, not a claim of a new cycle-exclusion
theorem. The finite certificate below quantifies an existing cycle floor.
No analytic result is promoted to a Lean theorem, and no unbounded cycle
complexity assumption is inserted.

## 1. What the latest sources already establish

PR176 at `c83a8459066d8223aefe7fc5f6b75faeea557345`,
`research/lean-global-resolvent-20261121/overview/literature/TRACE_HEIGHT_CLOSURE_ATTEMPT.md`,
Sections 5–6 already proves the following: if a finite positive profile
`h` is excessive for the full critical inverse operator and `h>=alpha>0`
on positive odd ternary units, then every vertex `q` of every positive
odd cycle satisfies `h(q)/q>=3alpha/32`. This statement has no period or
word-complexity restriction. It includes the cycle `{1}`.

The bounded independent-block classification is also already established
as written mathematics in PR185 at
`7889fc680f5ee22237732eccc172b1699ef565da`,
`research/profound-closure-20261122/BOUNDED_POWER_LANGUAGES.md`, and in the
fresh PR176/178/183 continuations. It does not provide an automatic upper
bound on the word complexity of an arbitrary actual cycle.

The primary literature checked for this attack includes:

- [Weaver, *Height and periodic-dictionary complexity for rational Collatz trajectories*](https://rstation.ai/problems/collatz/papers/15).
  The source states lower bounds for fixed-dictionary description
  complexity; it does not supply the missing upper bound for every cycle.
- [Weaver, Mahler and Wren, *Sparse block-sum and ordered-state complexity in positive Collatz cycles*, version 4](https://rstation.ai/problems/collatz/papers/22).
  Its sparse-window and ordered-state results exclude particular low
  complexity regimes while leaving high complexity cycles open.
- [Murmuration and Solomon, *Time, Depth, and Description Complexity of Precise Collatz Returns*](https://rstation.ai/problems/collatz/papers/147).
  Its precise-return complexity estimates likewise do not turn a short
  arithmetic description of an initial integer into a short periodic
  dictionary decomposition of its trajectory.

These are source-qualified recent manuscripts. This ledger does not
claim an independent verification of their complete arguments.

## 2. A finite certificate valid on every positive odd cycle

For a positive odd target `q`, let

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\pmod3}}
 \frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right),
\quad g(q)=\mathbf1_{3\nmid q},
\quad V_0=g,\quad V_{t+1}=\max(g,PV_t).
\]

All summands refer to actual positive odd parents. The displayed finite
envelopes are well defined: at each level the total row weight is at most
2, so `0<=V_t<=2^t` and the countable nonnegative sums converge.

Among exponents at most six, every positive odd unit `q` has two distinct
unit parents. The existing exact table is

| `q mod 9` | two unit-parent exponents |
|---|---|
| 1 | 2, 4 |
| 2 | 1, 3 |
| 4 | 2, 6 |
| 5 | 3, 5 |
| 7 | 4, 6 |
| 8 | 1, 5 |

Fix an actual cycle edge `U(x)=q`, with `3x+1=2^e q`. At least one of
these short parents is distinct from `x`; its contribution to `PV_t(q)`
is at least `kappa=3/64`, because `V_t>=g`. Set

\[
v_t(q)=\frac{V_t(q)}q,\qquad
\lambda(x)=\frac{3x}{3x+1},\qquad a=\frac3{32}.
\]

Then the actual finite recursion gives

\[
v_{t+1}(q)\ge\lambda(x)v_t(x)+\frac\kappa q
\ge\lambda(x)v_t(x)+a\bigl(1-\lambda(x)\bigr),
\tag{1}
\]

where the second inequality uses `e>=1`. Iterating backward on the
prescribed cycle, with `v_0>=0`, yields

\[
v_t(q)\ge a\left(1-\prod_{i=1}^{t}\lambda(x_{-i})\right).
\tag{2}
\]

Let the cycle have `p` odd vertices and total valuation `A` in one
period. Its exact product is

\[
\rho=\prod_{x\text{ on the cycle}}\lambda(x)
     =\frac{3^p}{2^A}<1.
\]

Consequently, for every integer `r>=0` and every cycle vertex `q`,

\[
\boxed{\frac{V_{rp}(q)}q\ge\frac3{32}(1-\rho^r).}
\tag{3}
\]

In particular `V_K(q)>=3q/64` at the finite depth

\[
\boxed{K=p\left\lceil\frac{\log2}{A\log2-p\log3}\right\rceil.}
\tag{4}
\]

An alternative requiring no logarithms is available if every cycle
vertex is at most the positive integer `M`. Each factor in (2) is then
at most `3M/(3M+1)`. Bernoulli's inequality gives
`(1+1/(3M))^(3M)>=2`, hence

\[
\boxed{V_{3M}(q)\ge\frac3{64}q.}
\tag{5}
\]

This is a finite quantitative version of the existing cycle floor.
It is not an exclusion: the trivial cycle satisfies it as well.

## 3. Why full geometric summation does not remove the clock

The one-period denominator `1-rho` measures repeated visits around the
same cycle. Formula (3) keeps every one of those visits. Replacing the
finite sum by its geometric limit retains the time needed to reach a
fixed fraction of that limit: order `p/(1-rho)` when `rho` is near one.
The elementary alternative (5) has depth `3M`. Neither bound is a
polylogarithmic bound in the target height.

The finite-horizon analytic estimate in PR185,
`research/profound-closure-20261122/POLYLOGARITHMIC_INVERSE_HORIZONS.md`,
has a full-depth factor of the form `K(K+2)` multiplying its mixing
error. It cannot be substituted at the infinite geometric sum without
controlling that factor. Matveev can bound (4) polynomially in the cycle
period, but this does not produce a polylogarithmic target-height clock.

The ancestor-floor hypothesis must also remain literal: a minimum cycle
vertex need not be the minimum of its entire predecessor basin. Smaller
off-cycle ancestors are possible unless ruled out by a separate minimal
counterexample or basin-minimum argument.

There is another essential distinction between the two counts. A finite
inverse-word cutset based at a periodic target can represent the same
ordinary source after different numbers of cycle laps. Therefore a
weighted renewal certificate cannot be counted as an equally large
collection of disjoint ordinary predecessor basins.

## 4. Rejected shortcuts

The following attempted implications were checked and not used:

1. **Polynomial cycle height implies low word complexity.** A small
   integer starting state supplies a short algorithmic description. It
   does not supply a short power-language or dictionary decomposition.
2. **The cycle floor plus the antichain budget bounds the number of
   cycles.** PR175's `CANONICAL_POTENTIAL_SUPERLEVELS.md` explicitly
   proves its potential/capacity comparison for nonperiodic roots.
   The periodic cutset collision just described blocks this extension.
3. **Selecting short off-cycle parents gives a new strong periodic
   census.** Such parents do have pairwise disjoint basins. However the
   existing elementary injective-cylinder estimate already applies to
   the union of all periodic odd states: every iterate of `U` is
   injective on that union. It already implies
   `#(Per intersect [1,X])<=4X^(39/40)` and
   `sum_(q in Per,q>=m) 1/q<=160m^(-1/40)`.
4. **An ordinary positive harmonic flow can be extended unchanged
   across cycles.** The existing ordinary flow lives on nonperiodic
   states and is killed on entering a cycle. Positive side-parent
   immigration obstructs the same ordinary harmonic equation on a
   full cycle. A correction theorem on that killed domain does not
   settle the removed cycles.

The cycle route therefore leaves a specific open bridge: a uniform
control of actual renewal certificates at the physical depth (4), or
an automatic arithmetic constraint on arbitrary cycle complexity that
forces a shorter usable certificate. This ledger introduces neither as
an assumption in the formal work.
