# Independent review of the signed stationary flux interface

Reviewer: factoring bridge lane, 2026-11-28.

Reviewed source: `research/astra-collision-factor-bridge-20261128/RECENT_CONCURRENT_INTERFACES.md`, Section 1.

SHA-256: `37794ca4869a8c2f936b286bd669ce03f5cbe8eb840690245a386a2a8664f4fd`.

**Verdict: the exact stationary transfer and its error budget pass.** This review checks the new interface to the stated PR 218 criterion. It does not independently rebuild PR 218's imported analytic inputs or certify its whole external proof chain.

The four native residues give `d(y)=b(y)+b(Ty)-1`: the respective values at residues 0, 1, 2, 3 are −1, 0, 0, 1. Summing this identity at the even-spaced observation clocks produces exactly the stated postcritical odd-count excess divided by `g`.

Since `q=3^A` is odd, the displayed `s_j` is the unique residue in `[0,4q)` with `s_j≡r (mod q)` and `s_j≡j (mod4)`. The two floor differences count the half-open interval `(R,R+L]` exactly, including endpoints and grade zero. `R≥0` supplies positivity. Summing the signed endpoint selector against fair words produces precisely `(2^h/N) E D`, with the actual same-path grade retained.

The observable has range `[-1,1]`, so the full-law total-variation error is at most `2δ_N` at each clock. There are `g/2` terms and the statistic divides by `g`; the total error is therefore `δ_N`, without a growing-clock loss. The fair stationary fractional-moment estimate supplies the stated `O(log N/N)` error uniformly in `h`.

Finally, when `N≤2^h`, the unsplit one-copy window has length at most one ternary lattice spacing. It selects at most one endpoint, hence `D∈{−1,0,1}` and `P(|D|=1)≤P(K=1)=N/2^h`. The note correctly preserves this rare-event precision and does not replace the signed, grade-correlated, full-conductor trace by a marginal or fixed-conductor quantity. No signed inequality forcing its expectation is proved by the transfer itself.
