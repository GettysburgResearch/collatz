# Independent review of the two directed progression certificates

**VERIFIED at the file pins below.** For each separately selected residue 1 or 5 modulo 6, the finite trees cover all positive odd integers and give a path from n to 3n. Each non-Collatz edge is a forward tripling in that same residue. The ordered-cut interval inequality (1) in the accompanying global-bridge note follows for every binary label invariant on ordinary Collatz edges. The positive Collatz conjecture and the imported assumptions for subsequent analytic corollaries are outside this verdict.

## Scope and pins

The contribution is based on PR 201 head `73a145ca99448a78219bd149e273f33b6e3fda4b`. These added files under `research/killed-green-head-closure-20261124/global-bridge/` were reviewed before their first publication commit. The pins are SHA-256 of their bytes.

| File | SHA-256 |
|---|---|
| check.py | `8b7e4e0f8b11d1499ba1954c077007aade3228e4239eddd888167645fb7bc27c` |
| cover1.txt | `03fe44cd5c3d01e2a89b7ce6f5c95d6456e9c5526cc43d7e4de26e0e6deb96e0` |
| cover5.txt | `062bc68e7dc2e34b24a0aa2e155a6ffc7b832b2bf6d6b0d228cba3d1ab283815` |
| CONTROLS.json | `62ffc3064da23d7f504507270ba3916c9a7922fd30bf511fbd12cdf6e3615516` |

## Coverage, direction and charging

The root 2t+1 uses every t≥0. At a p-way split, t=ps+j with 0≤j<p and s≥0 is unique, so its children are disjoint and cover their parent, including t=0. All promised child subtrees must be consumed exactly once. In the author's stack implementation, an orphan node fails at pop time and unconsumed children fail at EOF. Its divisibility and congruence checks on a leaf progression guarantee the entire row is in each move's domain. The base and slope stay positive. For an input in a rule's class is+j with 0≤j<i, nonnegative input and that congruence force s≥0. The reverse odd move at 3s+2 has predecessor 2s+1 with T(2s+1)=3s+2. The ordinary reverse moves require only invariance of the label on actual T edges. The extra move takes u to 3u and applies only on u≡r modulo 6.

I independently replayed the codebooks with a temporary recursive parser and a direct integer implementation of the five transitions, without importing the author's checker. At each word I propagated the images at the two consecutive leaf parameters 0 and 1. At each transition both sources had to satisfy the direct congruence and both images had to form a strictly increasing positive pair. Each rule is affine on its residue class, so these two checks establish the congruence and positive integral affine image for *every* t≥0 by induction. Final images at the two parameters were 3b and 3(b+m) on the leaf mt+b. All declared tree nodes were consumed, and the reciprocals 1/m of the disjoint leaf moduli summed to exactly 1/2 in each tree.

| Residue | Nodes | Leaves | Letters replayed | Forward query positions | Leaves with no query | Maximum queries on a leaf | Query/input bounds |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 1,606 | 948 | 35,627 | 2,325 | 14 | 6 | 27145/732923 through 26406895/30563 |
| 5 | 2,130 | 1,263 | 49,015 | 2,701 | 18 | 6 | 65/4167 through 4614215/6759 |

Write the binary label at n as i and the label at 3n as 1−i. Along its complete path the first departure from label i is a directed query i→1−i. A leaf with no such query cannot contain an ordered defect. For one chosen leaf and query position the input mt+d determines u=at+b, and a>0 makes this map injective on that leaf. The ratio u/n lies between a/m and b/d, since it is a weighted mean of these two fractions. Charging each n to its first departure gives multiplicity at most the total number of query positions over all leaves, regardless of overlap between different positions. This proves (1) with the independently recovered bounds above. This argument compares a specified ordering of binary labels. A path may cross additional components and provides no merger of specified ordinary trajectories.

No independent reconstruction of PR 146's reverse-direction transfer, PR 195's descent tables, the classical predecessor exponent, or the head-density and pair estimates was performed in this narrow review.
