# Independent review of the actual-source real-growth gap

23 November 2026. Reviewer: `/root`.

**Verdict: VERIFIED as written mathematics at the exact bytes below.**
The finite jump and late-defect estimates imply the stated exponential
lower bound for the running real maximum of the inherited canonical
stream. The upper estimate needed to construct a universal witness
remains open. No new Lean proof or universal regularity property is
included in this verdict.

## Frozen sources

| File | SHA-256 |
| --- | --- |
| `research/reassessment-20261123/construction/REAL_GROWTH_GAP.md` | `7116b007679deb512b26ee1a8d641184c8733a1850e30b8b6070ad769a7bc5b3` |
| `research/reassessment-20261123/construction/README.md` | `973df4262030f4a700c3407b5aff5da97ad06da5e7f3167b048063c29c00f711` |
| `reports/2026-11-23-reassessment/construction-sources.json` | `b0bd4e1d5eeca6b80d70e23bad73398fb25c863b9ff98f4032782921a7c7c34b` |

These are new local files over
`c91b80a3156e640ad471cf30c47721145ae21eb1`. I read the complete note,
its README and ledger, and reconstructed every new inequality. I
checked the inherited defect identities in the pinned local source
and directly inspected the two primary Monks papers at the statements
used below. The older Lean modules and peer proof trees were not rebuilt.

## 1. The actual prefix supplies the count inequality

At an odd positive state, `T(x)<=2x`; at an even one, the update is
exact halving. Multiplying along the same actual prefix gives
`x_t 2^b_t <= n 2^p_t`. Positive integrality makes `x_t>=1`.
Since `n<2^N`, this even gives `b_t<p_t+N`; the note uses the valid
weaker inequality `2b_t<=t+N`. At a genuine defect, the inherited
complete-carry recurrence has absolute jump `2^t/3^b_t`. Squaring
proves equation (4), including signed jumps of either kind.

This reasoning keeps the fixed positive source. An arbitrary binary
word with a new positive realizer for every length would not supply
the same fixed constant `N`.

## 2. The final alternating block and its endpoints

Let `h-1` be the last defect before `K`, or set `h=0` if there is
none. The clock indices `h,...,K` supply exactly `K-h+1` parity bits.
They agree with the core point `d_h` of the same parity. Finite parity
coding therefore gives divisibility by `2^(K-h+1)` of `x_h-d_h`.
The no-core hypothesis makes this a strictly positive integer, so
`x_h>=d_h+2^(K-h+1)`.

The bound `T(x)+1<=(3/2)(x+1)` holds at both branches. Thus
`x_h+1<=(n+1)(3/2)^h`. Multiplication by `2^h` gives the strict
inequality `2^(K+1)<(n+1)3^h`; strictness comes from the positive
additional `d_h+1`. If `h=0`, it contradicts `n+1<=2^N` and
`K>=N`. Hence the last defect exists in the tested prefix. No future
parity beyond `x_K` is assumed in this argument.

## 3. The finite growth bound and the limiting quantifiers

Both endpoints of the last jump lie among `eta_0,...,eta_K`, so
its absolute value is at most `2M_K`. Substitution of equation (4)
and the strict late-defect inequality gives exactly

\[
M_K>\frac{1}{2\,3^{N/2}}
\left(\frac{2^{K+1}}{n+1}\right)^{\log(4/3)/(2\log3)}.
\]

For a source that never reaches the core, the hypotheses hold for
every `K>=N`. Dividing logarithms by `K` yields the claimed positive
liminf. A convergent source has an eventually constant stream by the
credited boundary identity, so its running maximum is bounded. Since
`M_K>=1`, boundedness implies `log M_K/K -> 0`, and the lower bound
excludes that limit for any nonconvergent source. Equation (8) follows.

The running maximum, the fixed source-dependent constants, and the
distinction from the earlier optimized candidate height are essential
and correctly retained. The proof gives no lower bound for every
individual signed or absolute stream value.

For the stronger escape-only estimate I directly read Monks--Yazinski,
[*The autoconjugacy of the 3x+1 function*](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Theorem 2.7(b) and its proof. Its divergent rational-orbit lower bound
on the odd-frequency liminf is the one used in the note. Substitution
gives `log|jump_t| >= t log(4/3)-o(t)`. The late defect satisfies
`h>=K log2/log3-O_n(1)` and `h<=K`, so the error remains `o(K)`.
This verifies equation (9). It is not applied to a possible nontrivial
positive cycle.

## 4. Polynomial interpretation and construction boundary

I directly inspected Monks,
[*On q-Analogs of the 3x+1 Dynamical System*](https://cs.uwaterloo.ca/journals/JIS/VOL28/Monks/monks6.pdf),
Theorem 5, Conjecture 6, and the affine definition. For `A=1` and
`B=1+z^2`, iterating `H(n)=z H(Tn)+e_0 B` in the formal power-series
topology gives exactly `H(n)=(1+z^2)sum e_k z^k`. Its coefficients
after degree one are `e_k+e_(k-2)`, equal modulo two to the sum of
the adjacent two defect symbols.

If the first hit at one is `tau>=2`, the final original states are
`4,2,1`. The coefficient at `tau` is one, the coefficient at `tau+1`
is zero, and all subsequent coefficients vanish by alternation.
Thus the degree is exactly `tau`; the direct values at sources one
and two give degrees zero and one. This checks the note's precise
interpretation without importing a finite-support conclusion for
arbitrary positive inputs.

The original-source inequality controls the other stream from above,
and the jump-product identity has the indicated negative sign. Neither
is an upper bound on the canonical complementary stream. The paper
correctly identifies that missing estimate as an equivalent unresolved
construction task, rather than using the new growth gap to assert
universal convergence. No mathematical correction was required at the
listed hashes, and no finite numerical census was used as evidence.
