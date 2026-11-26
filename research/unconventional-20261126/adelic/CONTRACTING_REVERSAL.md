# A contracting same-grade reversal can finish above both ordinary starts

For the native shortcut map there are adjacent positive integers $859,860$ whose respective 46-step paths have 29 odd departures, yet the first ends at $890$ and the second at $866$. Both endpoints exceed both starts. Their chronological parity words and exact integer carries are as follows.

| Start | 46 parity digits | Integer carry | First descent | Least height in segment |
|---:|---|---:|---|---|
| 859 | `1101110101011100000101011100111101011011101111` | 3674688161686463 | 776 at clock 16 | 47 at clock 28 |
| 860 | `0011100011011101111010011101101111110011110001` | 1917207924057644 | 430 at clock 1 | 91 at clock 8 |

Here $3^{29}=68630377364883<70368744177664=2^{46}$. For each row the exact endpoint is $(3^{29}x+C)/2^{46}$, with $C$ computed by appending a zero-stretch bit unchanged or appending an odd bit by $C\mapsto3C+2^j$ at zero-based clock $j$. This refutes the proposed claim that the lower endpoint of any contracting same-grade reversal must lie below its smaller initial value. Rozier and Terracol already reported the individual post-descent segment $859\mapsto890$ at this clock. The comparison here uses the adjacent path at the same grade. [Rozier and Terracol, *Paradoxical behavior in Collatz sequences*, 2026, §5](https://arxiv.org/abs/2502.00948)

A version imposing the smaller initial value $a>1$ as a floor at **every** intermediate step of both paths has a different status. If the sources are adjacent, one is even and falls to at most $(a+1)/2<a$ at its first step. For unrestricted $b>a$, any counterexample with $3^{p_h(a)}<2^h$ would already be a counterexample to Terras's coefficient-stopping-time conjecture at $a$, irrespective of the comparison with $b$. At the first coefficient contraction $j\le h$, the height would still be at least $a$ while the conjecture requires it to be below $a$. Rozier and Terracol's Corollary 5.2 verifies equality of these two stopping times for $2\le a\le2.8\cdot10^{19}$. A large unchecked starting value remains a genuine open case, and the two-path condition could impose additional constraints. [Rozier and Terracol, Corollary 5.2](https://arxiv.org/abs/2502.00948)

[OrderReversals.lean](OrderReversals.lean) uses the same native step and run as the existing `CoreBranching` module. Kernel `decide` checks these two outputs, both grades and the contraction inequality. It also checks the two seed reversals and all 65 residues in the three finite wrap-order cases of [Theorem O](ORDER_REVERSALS.md). A fourth theorem proves the full two-word carry cancellation from the adjacent-reversal identity. These finite declarations do not formalize the all-length classification or the external stopping-time result.
