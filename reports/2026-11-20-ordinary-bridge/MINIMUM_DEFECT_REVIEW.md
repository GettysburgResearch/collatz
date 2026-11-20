# Independent reconstruction of the square obstruction and MD-001

Reviewer: the parent research agent, separate from the author of the cycle
packet. Date: 20 November 2026.

**Verdict: VERIFIED within the stated source-qualified limiting-profile
scope.** This review does not prove the cited logarithmic-form or rational
p-adic Subspace Theorem inputs, and it does not exclude the remaining
small-defect profiles or construct an ordinary cycle.

## Frozen content

All four files are under `research/independent-attack-20261120/`.

| File | SHA-256 |
| --- | --- |
| `SQUARE_OBSTRUCTION.md` | `27345e62f4bc4715a1c650a958edc8db1a0614a1eef33eb0c1cec296a6013c39` |
| `check_square_obstruction.py` | `2d7b6c81ff022ec24404a6d01e47edfc602d56c5104b2aaa85079850b5ba0c7a` |
| `MINIMUM_DEFECT.md` | `e5849bfa76ca20eb513cbdb945e60c900e9b83d9575e57dfcdc9a9d281be0361` |
| `check_minimum_defect.py` | `4d81686c507ddde339041db8a8ffcc2db246dabdc3d732190c7e9cfd1eeeeafe` |

The shared comparison lemma and powered-block estimates are in `PROOF.md`,
SHA-256 `7d3a63cfd53fd0298c5beebe9fe80ee414a7d43780169a6aab3e2c3920c55bed`.
Its independent reconstruction is recorded in
[CYCLE_REVIEW.md](../../research/forward-bridge-20261120/CYCLE_REVIEW.md).

## Reconstruction

The box obstruction concerns the old upper multiplier costs. Affine extrema
at rational box vertices certify feasibility and failure of each stated
charge test. Using a lower bound for `log_2(3)` is conservative here: increasing
the logarithm weakens the domain constraints and increases the multiplier
costs, while decreasing the transport saving. I checked these signs and the
18-test enumeration. The note does not assert ordinary realizability of its
formal upper-cost profile.

For MD-001, a four-factor length bound gives `L=O(H)` along the assumed
unbounded family. The least-phase input gives `log(m+1)=O(log L)`, and the
distinct-phase product bounds the total nonhomogeneous correction by
`O(log L)`. Both are `o(H)`. Thus the suffix from the minimum to the exit has
limiting homogeneous gain exactly one, even when the words and the location
of the split vary. Passing to a subsequence is legitimate because all
normalized widths are bounded.

With positive limiting gains, the leading terms in the exact square
displacements dominate exponentially. I recomputed
`mu_i=u_i-(c/gamma)*r_i` and
`p_0=u_P-(c/gamma)*kappa` directly from those displacements and the suffix
count identity. I also reconstructed the finite identity
`n-m=P*2^beta*3^q_A` by applying the common root prefix to the difference
between consecutive root entries. This supplies ordinary arithmetic
information absent from the original upper-cost box.

The two-term comparison from the first rising square to the descending
square has saving `2*g_1` throughout this box; both the descending gap and
the transport gap are strictly larger. The retained-term gap is `g_1`,
so the fixed three-coordinate comparison lemma applies whenever
`2*mu_1+p_0<2*g_1`. Its exact-relation conclusion is contradicted by the
2-adic valuation: the transported numerator contains the odd factor
`3^q_1+2^w_1`, and the intervening power of two is in the denominator.
It strengthens, rather than weakens, the required divisibility of `M_1`.

Rearranging the failed strict comparison gives exactly the threshold
printed in MD-001. That threshold increases with `c`; its maximum over
the box at the outward upper bound is `11191/48500`. The limiting even
fraction `(c-1)*r_1/(g_1+c*r_1)` increases with `c` and `r_1` and decreases
with `g_1`, giving the stated rational ceiling. The actual logarithm is
strictly smaller than the outward bound, which justifies the strict ceiling.

No gap was found in these arguments at the frozen contents above.

## Executed finite checks

The parent ran both commands successfully from the complete repository:

```sh
python -X utf8 -B research/independent-attack-20261120/check_square_obstruction.py
python -X utf8 -B research/independent-attack-20261120/check_minimum_defect.py
```

The box checker returned domain margin `49/100`, 18 failed charged
comparisons, weakest failure gap `3974/9725`, full-displacement margin
`-45096/9725`, and rejected the two stated mutations.

The minimum-defect checker returned threshold `11191/48500`, uniform
quarter-defect charge margin `467/8950`, divisibility margin `36043/8950`,
even-fraction ceiling `2003189/19971815`, and 186 ordinary minimum-split
replays. Its zero-defect control remains unexcluded, as it should.

These executions verify the finite arithmetic and local identities.
They do not replace the written limiting argument or the analytic input.

## Remaining boundary

A zero normalized defect can still conceal an unbounded number of parity
exceptions. Neither this review nor MD-001 replaces such a word by an exact
run of odd steps. Control of the remaining small-defect class is open.
