# Whole denominators, odd runs and periodic pieces

| File | Result and verification scope |
| --- | --- |
| [ADJACENT_SWAPS.md](ADJACENT_SWAPS.md) | Full classification of a proper rotation reachable by at most two cyclic unequal-neighbor swaps. Two disjoint opposite swaps leave an explicit geometric factor in the reduced denominator, giving \(d>2^{n/2}\) with sharp exponent. Two disjoint same-direction swaps give \(\log G=o(n)\) using BCZ. One-swap and overlapping local predecessors receive credit. |
| [SwapArithmetic.lean](SwapArithmetic.lean) | Strict Lean proofs of the finite modular-power gcd step, geometric divisor, strict leading-term bound and reduced-denominator growth from the two displayed divisibilities. The preceding binary-word classification, BCZ and asymptotic sharpness are written proofs. |
| [BOUNDED_RUNS.md](BOUNDED_RUNS.md) | For fixed \(K\) odd runs, \(\log_2d/n\ge\max(1/K,1/\gcd(n,u))-o_K(1)\). Coprime counts give \(\log G=o(n)\). Uses the outside-\(S\) gcd theorem of Levin and Rhin's two-logarithm bound. Includes a primitive three-run family with denominator exponent \(3/4\). |
| [DILATIONS.md](DILATIONS.md) | For each fixed binary mask, exact limiting denominator exponent under uniform dilation of every symbol. An integer cyclotomic algorithm computes the surviving Fourier frequencies. A primitive mask with prime count gcd has full exponent. Uses the published outside-\(S\) gcd theorem, with no logarithmic-form input. |
| [RATIONAL_PIECES.md](RATIONAL_PIECES.md) | Extension of the team's integer-source result to reduced rational denominators. For a path with \(K\) pieces whose fixed points have logarithmic height \(o(L)\), a violation of \(\log_2\max(1,x)+K\log_2d\ge(1-o(1))L\) forces an actual piece return. Primitive positive cycles with \(K\) proper pieces have denominator exponent at least \(1/K\), sharp at \(K=2\). Uses the \(S\)-adic Subspace Theorem and, in the cycle corollary, Rhin. |
| [check_transport.py](check_transport.py) | Exhausts all 3,899 primitive positive necklaces through length 15 and all one- and two-swap presentations of every proper rotation in each necklace. Replays sharp critical controls through length 31,040. |
| [check_dilations.py](check_dilations.py) | Checks 2,084 positive necklaces through length 14, including all exact stabilizers and symbolic divisors for dilation factors 1, 2, 3. Eight primitive templates in this range have nontrivial symbolic cancellation. |

## Reproduction

Run from this directory with standard Python:

~~~sh
python -OB check_transport.py
python -OB check_dilations.py
~~~

The same controls pass with `python -B`. Each uses explicit checks under optimized Python. For Lean, use the research directory's [replay_lean.py](../../replay_lean.py) and the pinned repository toolchain. The author replay used Lean 4.34.1 and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612` with `-j1 -DautoImplicit=false -DElab.async=false -DwarningAsError=true`. All four printed declarations in `SwapArithmetic.lean` have exactly `propext`, `Classical.choice`, and `Quot.sound`. No external Diophantine theorem is entered as a Lean axiom.

The sequence-level statements have ineffective onset. They impose restrictions on structured words and trajectories. A complete result excluding arbitrary ordinary cycles or escaping positive trajectories remains open.
