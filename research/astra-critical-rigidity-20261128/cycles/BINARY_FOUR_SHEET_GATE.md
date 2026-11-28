# The exact four-sheet pair obstruction also has binary native valuations

In the [four-sheet construction](FOUR_SHEET_PAIR_COLLISIONS.md), every true accelerated valuation can additionally be required to belong to \(\{1,2\}\). The odd period remains exactly \(4P\), the real widths tend to four, and the signed pair register is zero at exactly sixteen dates, supported on four reduced ranks. At all other reduced ranks two sheets have positive and two have negative register. This is a construction in one primitive positive rational cycle with clock gcd four; it does not produce four distinct short offsets within an ordinary coprime clock.

Use the same permutation \(\pi\), taking the regular tuple \(D_t=(2,2,4,2)\) when \(b_t=1\), and \((4,4,4,2)\) when \(b_t=2\). The scalar register is two on this template. At every winding one each tag is nondecreasing to the next row; at every winding two it is nonincreasing. These are exactly the two binary-native constraints for regular tags two and four. Insert the following neighborhood at each \(jP\), with the same sheet permutations and signs as in the original construction.

| \(t-jP\) | \(b_t\) | Raw tags | Raw signed height |
|---:|---:|---|---:|
| \(-5\) | 1 | \(2,2,4,2\) | 2 |
| \(-4\) | 2 | \(4,4,4,2\) | 2 |
| \(-3\) | 1 | \(2,2,4,2\) | 2 |
| \(-2\) | 2 | \(4,4,4,2\) | 2 |
| \(-1\) | 2 | \(2,2,4,2\) | 2 |
| \(0\) | 1 | \(1,2,4,2\) | 1 |
| \(1\) | 2 | \(2,4,4,2\) | 0 |
| \(2\) | 1 | \(2,2,2,2\) | 0 |
| \(3\) | 2 | \(4,4,4,4\) | 0 |
| \(4\) | 1 | \(2,2,4,4\) | 0 |
| \(5\) | 2 | \(4,2,4,4\) | \(-2\) |

Each transition satisfies \(2c_t\le2^{b_t}c_{t+1}\le4c_t\), including both edges incident to the sole tag one; the endpoints agree with \(D_{-5}\) and \(\pi D_5\). The register row check is \(2^{b_t}H_{t+1}=3H_t+c_1+c_2-c_3-c_4\). The first tag at gates now takes the value one exactly once in four sheets. It therefore cannot have period \(2P\). The word fixed-point, primitive-period, four actual shifted phases, exact register, and width proof in the original construction all apply without any other change. The four zero ranks are \(B,2B,3B,4B\bmod P\), distinct for all \(P>4\).

[Exact binary-native checks](check_binary_four_sheet_gate.py) · [Finite receipt](binary_four_sheet_gate_controls.json)
