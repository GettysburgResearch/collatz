# Independent review of the supplied peak minima

The [literal Python replay](../../../research/astra-infinite-descent-20261127/merger/check_minima_independent.py) reproduced both first meeting clocks and both selected gaps and savings for the 16 supplied rows with the smallest absolute paid horizons. In this order their indices are $2,8,12,18,13,17,16,10,19,20,14,25,30,31,33,34$. It examined all 7,801 candidate gaps $1\le d<H$ for these rows and advanced 4,398,676 scalar clock pairs. All 16 rows had multiple eligible paid gaps arriving at their first paid clock, so each exercised the saving-and-gap tie rule. The complete 192-row numerical replay belongs to the [ordinary GMP verifier](../../../research/astra-infinite-descent-20261127/merger/verify_peak_minima.cpp). [Supplied results](SUPPLIED_MINIMA.csv)

For each gap the independent code computes $3^{m-d}\bmod 2^H$ directly, constructs its own pair of nonnegative representatives, and follows both trajectories one parity step at a time to the horizon. It records the earliest coincidence of both the physical states and the augmented grades. It collects all hits before selecting the earliest clock, greatest saving and least gap, and performs the paid selection separately. This replay shares the mathematical representative identity and pinned price table with the primary verifier. Its loop uses no blocks of gaps or steps, terminal-grade pruning or state deduplication.

The written completeness argument also checks. The pinned independent-clock gap theorem gives $d<H$. The lower exponent then exceeds $2H$ under the height guard. In the $x+1$ coordinate the affine remainders satisfy $0\le C_i<3^i$, so a multiple of $3^{m-d}$ with absolute value below $3^{m-d}$ must vanish. The dyadic valuations force equal physical clocks, and the ternary factors force the augmented-grade equality. That equality persists at every later clock on a merged pair.

In the GMP checker, $2^H\bmod 3$ is its own inverse; adding the selected multiple of $2^H$ before each exact division by three maintains the required positive residue. All representatives for one group lift by a common parameter, and matching augmented grades give the same high-part increment. A lower arm can only increase its grade by zero or one per remaining step, so terminal-grade pruning preserves every possible merge by $H$. Any unrestricted first date is no later than the first paid date. The strict gap bound also excludes ties at a current deadline from unexamined gaps at least that large. Once lower arms coincide in state and augmented grade, the rest of their histories are identical. Keeping the largest saving and then least gap preserves the unrestricted and paid selectors. [Release census and proof](../../../research/astra-infinite-descent-20261127/merger/RELEASE_CENSUS.md)

## Reviewed SHA-256 hashes

| File | SHA-256 |
|---|---|
| RELEASE_CENSUS.md | 95feb45560d1e63ca9b63988f1591adfe44ee92ba38b9d1dee34bbcb7c00efde |
| check_peak_minima.py | 85ae3c31763de38d2370227229bbf4365193155c7f425faf83d32c2cfb81ae5c |
| verify_peak_minima.cpp | e79a5f784b8e1c1814b2187aca7cdb12fa8762a04dd539d76ef2aaeca3af793b |
| SUPPLIED_MINIMA.csv | 78fd3f8240a385e237549c9a7422174de2dc56e9e456cb09144af04c0e92c538 |
| ReturnDescentRows.lean | c9a230e606436c88d3529322ad369fd4f5830238c14e20d1df240a2f2d0d93c2 |
| check_minima_independent.py | e6fdc484cf7159e2faa3731627ba877d19c8223dfe467e72c150f79ccbb13ada |
