# Local certificate receipt

Date: 20 November 2026. This is a local execution receipt for this packet,
not the complete-repository validation or an independent verification of
the Subspace-Theorem argument. The parent investigation records the
complete checkout and publication checks separately.

Command actually run from the repository root:

```sh
python -X utf8 -B research/independent-attack-20261120/check_cubic_descent.py
```

Exit status: `0`.

```text
scalar bounds: {'extra_drop_upper': '944067/2887091', 'comparison_margin_lower': '56369617346/250642805165'}
(2, 2, 2) covered; exact recursion nodes: 173
(2, 2, 3) covered; exact recursion nodes: 77
(2, 3, 2) covered; exact recursion nodes: 27
(2, 3, 3) covered; exact recursion nodes: 8
(3, 2, 2) covered; exact recursion nodes: 13
(3, 2, 3) covered; exact recursion nodes: 5
(3, 3, 2) covered; exact recursion nodes: 5
(3, 3, 3) empty height domain
negative controls: square-descent witness retained; missing comparisons rejected
ordinary powered-block arithmetic replays: 378
PASS: seven cubic-descent cones; total recursion nodes: 308
```

## What was checked

The cone computation clears denominators and uses exact integer
determinants and comparisons. The domains are bounded because successive
nonnegative multiplier-cost bounds give successive upper bounds on the
three gains. The recursive cover is valid for closed failed-margin
regions, including lower-dimensional intersections. No approximate LP
result is accepted by this checker.

The physical arithmetic replay covers every binary root of widths 1
through 6, with repeat counts 2, 3 and 4. For each repeated word it
constructs an ordinary positive input in the exact parity cylinder,
replays all steps, and checks both endpoint brackets, the two
divisibilities, the shared positive integer multiplier, the geometric
displacement, and the direction of motion. These 378 cases support the
algebra; their finite coverage is not the proof of the identities.

The two negative controls test distinct risks:

1. For three rising squares and a descending square,
   `g=(1/2,1/2,1)` satisfies all necessary cone inequalities and escapes
   every available comparison. The method must leave that point open.
2. With all comparisons removed, the cubic-descent cone is nonempty and
   the recursive checker must return a witness instead of declaring
   coverage.

## What was not checked by computation

The checker does not search all cycles, compute an ineffective period
bound, reconstruct Rhin's logarithmic-form proof, or implement the
p-adic Subspace Theorem. The passage from a hypothetical unbounded
ordinary-cycle family to its limiting cone, and the fixed-form
Diophantine comparison, are written arguments in [PROOF.md](PROOF.md).
