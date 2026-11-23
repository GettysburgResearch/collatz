# Complementary denominator capacity

Read [COMPLEMENTARY_DENOMINATOR_CAPACITY.md](COMPLEMENTARY_DENOMINATOR_CAPACITY.md).

The direct cycle-symmetry attack yields a quantitative statement after
the full numerical gcd: a nontrivial positive integer shortcut cycle of
least period `K` has complementary reduced denominator `q>K/2`.
The core has `K=2,q=1`, so every positive integer cycle satisfies
`K<=2q`. A proved arbitrary-rational dual certificate with initial odd
denominator `Q` can therefore use the eventual period bound `K<=2Q`.

The proof uses the exact cycle product, distinct positive odd numerators,
and a convex midpoint integral. It also gives an explicit stronger
envelope and the asymptotic coefficient `0.7864098721...` along a
hypothetical sequence of integer cycles with periods tending to infinity.

The attempted closing upper bound on `q` remains open. This is written
mathematics with no new Lean theorem, cycle census, or novelty claim for
the general product method. It does not exclude unrestricted positive
cycles or construct the rational dual.
