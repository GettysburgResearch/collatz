# Independent review of the minimum-only critical-tail gap

Reviewer: factoring bridge lane, 2026-11-28.

Reviewed source: `research/astra-collision-factor-bridge-20261128/collision/CRITICAL_TAIL_WITHOUT_PACKING.md`.

SHA-256: `1b8496ec2968f06fccd381725d2bb30973821f6b19564bb3c1deab557f1d8512`.

**Verdict: the complete written upper-gap proof passes at its stated source-qualified scope.** It does remove the orbit-packing and height-process inputs from the sufficient critical-quantile criterion. It neither proves the required lower bound nor gives the stronger exact cycle-mixture formula without its additional input.

Starting at the true positive minimum `m`, every future state is at least `m`. Multiplying the exact step ratios gives `2^t y/m≤(3+1/m)^b`; since `y/m≥1`, the claimed lower odd-count rate follows. A bad minimum is an odd integer at least three, so the uniform rate `β_3` applies even to a hypothetical escaping future.

Before the first minimum, the departed states are distinct. Their correction is bounded by one third of the harmonic sum through the number of departures, hence by `(1+log h)/3` at every relevant clock. The finite grade identity, endpoint positivity, and `δ_1 h−log X∈(−δ_1,0]` then give the uniform preminimum lower bound `W_X≥−ε_X`. In particular a fixed strictly negative grade event is already postminimum for sufficiently large `X`.

Splitting the odd count at the minimum gives the displayed postminimum lower bound. Dropping `log(X/n)` and `log m` is legitimate because both are nonnegative. The specified `ε_X` pays both the floor error and the harmonic correction. The remaining coefficient is exactly `c_X r_*`, with `c_X→1` and `0<r_*<1`. Dividing by that positive coefficient gives the literal event inclusion (6), uniformly in every source through `X`.

On the known basin, the future from its minimum 1 has odd count within one half of half its elapsed length. Thus, on already-entered sources, `W_X−c_X Z_X` consists only of the preminimum correction, the bounded cycle/floor errors, and a multiple of `log(X/n)/sqrt(h)`. The latter is negligible in probability by its elementary exponentially decreasing tail. Sources not yet entered are excluded from a fixed negative threshold by the uniform preminimum bound. This proves the known-basin Gaussian contribution from the stated joint minimum/clock law.

The bad-basin contribution is bounded by the same joint clock law and the moving threshold in (6); continuity of the Gaussian distribution justifies its limit. Subtracting the known-basin clock law from the unconditional one gives the complementary basin law directly, so no countable cycle classification or orbit-packing truncation is hidden in this step. The resulting inequality (7) has the stated strict Gaussian gap whenever the known-basin density is below one.

The full ordinary-to-stationary transfer and final positive-predecessor upgrade remain the separately named inputs. The original minimum/clock source was directly inspected earlier in this lane; this receipt does not claim a fresh formal rebuild of that external analytic development. No new Lean certification is asserted for these logarithmic or probabilistic inequalities.

The final appended Section 5 was checked against the complete `MinimumProduct.lean` source and its `minimum-product-lean.json` receipt. Its four roots concern exactly the native step cap, finite-prefix product, cancellation at a supplied positive finite minimum, and the `10/3` specialization. The general denominator-cleared inequality yields the written logarithmic count bound by taking logarithms; the probability limits remain outside that kernel. The receipt matches the stated source hash, Lean version, four-root audit, and `Quot.sound`/`propext` axiom list. This review inspected that evidence and did not launch a separate compiler or cold dependency rebuild. The appended formal-scope description is accurate and does not alter Sections 1–4.
