# Unverified and pending source work — wave 9

An entry here is an honest gap, not a negative verdict.

## U9-01 — Matveev normalization used by PR #53 and PR #70

The official 2000 paper and English PDF were located, but the exact theorem statement, normalized heights, coefficient parameter `B`, and numerical constant used natively were not inspected in full.

**Needed:** upload or acquire the complete English PDF and map every native parameter line by line.

## U9-02 — PR #70 three-pulse all-repetition source audit

The native theorem depends on a specific Matveev cutoff and subsequent continued-fraction reduction. The exact source-to-native inequality remains unverified by this literature agent.

## U9-03 — Dubickas 2006 nearest-integer constants

The abstract confirms explicit constants in terms of `p,q` and Thue–Morse, but the exact formula, endpoint convention, and equality cases at `(p,q)=(81,64)` were not obtained.

**Needed:** full PDF of DOI `10.1016/j.jnt.2005.07.004`.

## U9-04 — Dubickas 2008 two-interval theorem

The abstract gives the `3/2` model result, but the general theorem hypotheses and interval geometry needed for the centered `81/64` chart were not inspected.

**Needed:** full PDF of DOI `10.1002/mana.200510651`.

## U9-05 — Dubickas 2009 small-interval theorem

The paper was located through EuDML, but the exact theorem statement and constants were not parsed in this pass.

**Needed:** full PDF of *Acta Arithmetica* 137 (2009), 233–239.

## U9-06 — Chim 2025 exact constants

Only the official abstract and metadata were inspected. Applicability to a native pulse equation requires the exact algebraic-number, prime, independence, and exponent-height hypotheses.

## U9-07 — Bugeaud 2002 simultaneous m-adic constants

Only the official abstract and metadata were inspected. No native mixed-prime inequality is claimed.

## U9-08 — de Weger implementation details

The source supplies a general lattice-reduction architecture, but the precise lattice, initial bound, and finite search required by a PR #53/PR #70 equation remain to be derived.

## U9-09 — rational-base normality

The Andrieu–Eliahou–Vivion statement is a conjecture, not a theorem. It must never be used to promote six-branch termination.

## U9-10 — zero-digit occurrence

No located theorem proves that every positive minimal word in base `3^12/2^19` contains zero. `LIT-KTHM-0057` only shows that this one-letter statement would eliminate the chart.

## U9-11 — subalphabet size two through five

Dubickas–Mossinghoff prove universal termination for singleton allowed residue sets. No general theorem was located for allowed-set sizes `2,...,5`, including subsets of the six physical residues.

## U9-12 — positive implication through the physical chart

The implication from a nonterminating six-branch rational-base root to an ordinary Collatz counterexample remains branch-qualified to PR #45/PR #50 and is not independently reconstructed in this wave.

## U9-13 — bounded-observable theorem versus PR #66

`LIT-KTHM-0055` supports finite linear rigidity, but it does not subsume PR #66's exact classification of filters that preserve the six-element alphabet. That native classification remains independently reviewable.

## U9-14 — Väänänen–Wallisser beyond finite dimension

The supplied 1991 paper is finite-dimensional and has a dimension-dependent numerical condition. No period-uniform or infinite-dimensional consequence is inferred.

## PDF acquisition priority

```text
1. Dubickas 2006 nearest-integer paper;
2. Dubickas 2008 two-interval paper;
3. Dubickas 2009 small-interval paper;
4. Matveev 2000 English paper;
5. Chim 2025 p-adic logarithms;
6. Bugeaud 2002 simultaneous m-adic logarithms.
```