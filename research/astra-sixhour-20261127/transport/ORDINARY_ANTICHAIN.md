# An ordinary antichain for unbounded paired steering

**PROPOSED.** Suppose every sufficiently large positive \(X\equiv r\bmod
3^b\) admits an ordinary \(Y\equiv a\bmod3^L\) with \(Y\le B X\) and
\[
     (T^H Y,T^H(3Y-1))=(X,3X-1)
\]
for some common clock \(H\) depending arbitrarily on \(X\). Here \(T\) is
the positive shortcut Collatz map. Then
\[
                              B\ge 3^{L-b}/16 .                      \tag{1}
\]
Both odd counts may be arbitrary or unequal. There is no restriction on
clocks, ranks, number of words used or the initial target floor.

Write \(X=3+16u\), \(u\ge0\). The trajectories through clock four are

| Clock | Lower | Upper |
|---:|---:|---:|
| 0 | \(3+16u\) | \(8+48u\) |
| 1 | \(5+24u\) | \(4+24u\) |
| 2 | \(8+36u\) | \(2+12u\) |
| 3 | \(4+18u\) | \(1+6u\) |
| 4 | \(2+9u\) | \(2+9u\) |

The merger identity is in the earlier [common-hold
calculation](../../astra-unconventional-20261126/operator/COMMON_HOLDS.md).
The difference at clock three is positive, so determinism makes four the
*first* synchronous merger. A paired source can hit at most one target in
this class: the source's first synchronous merger time must be \(H+4\).
Consequently two hits from the same source would have the same \(H\),
hence the same target.

Among the prescribed ordinary targets up through \(N\), the class
\(3\bmod16\) has cardinality \(N/(16\cdot3^b)+O(1)\), by the Chinese
remainder theorem. The available ordinary sources number at most
\(BN/3^L+1\). The preceding injection, division by \(N\) and passage to
the limit give (1). More generally one may replace \(1/16\) by the
dyadic proportion of any fixed first-merger time slice.

This proves an ordinary restriction even on a countable choice of words,
in the setting where the coverage hypothesis ranges over all sufficiently
large integers in the indicated ternary class. On a target restricted by
opposite component labels, every first-merger slice is empty. Additional
dyadic restrictions on the targets also require their own nonempty
intersection with a suitable slice. The proof gives no smaller source for
a particular least disagreement.
