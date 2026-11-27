# Logarithmic-length returns with canonical tripling arrows

Let $T(2v)=v$ and $T(2v+1)=3v+2$. On the positive integers, join $x$ to $T(x)$ in both directions and add the directed arrows $q\longrightarrow3q$ for $q\equiv17\pmod{48}$. Count each ordinary traversal and each directed arrow as one edge.

**Written finite-graph theorem.** Every $n\ge1$ admits a directed path in this graph from $n$ to 1 such that
\[
 \text{length}\le425138\lceil\log_2 n\rceil,\qquad
 \text{every vertex}\le\frac{82778996644480}{73179}\,n,\qquad
 \text{every tripling source}\le98304n .
\]
The integer $1131185131$ also suffices as the height factor. The path is constructive. Its logarithmic length counts edges in the augmented graph, including the extra canonical arrows. Replacing each such arrow by an ordinary equivalence of basin membership is precisely an additional Collatz implication. The kernel results establish the ordered-defect conclusions. The directed path, height and length statements here follow by the finite-graph argument below and the independent affine checks. [Canonical return certificate](OptimizedBank.lean) · [Constructive path checker](check_canonical_paths.py)

## An actual path from each binary source to its triple

Fix a positive $w\equiv1\bmod16$. At the root of the localization plan take $t=(w-1)/16$. At each radix node retain the unique child selected by the current parameter and pass its quotient to that child. At a nonunit exchange retain **both** children. All rows in this finite specialization give actual positive integers. Form a graph on their physical vertices as follows.

* At the unit exchange retain both ordinary mergers $x\leftrightarrow x'$ and $3x\leftrightarrow3x'$.
* At the nonunit exchange $x=3u$ retain the three ordinary mergers
  \[
  x\leftrightarrow16u+1,\qquad 3(16u+1)\leftrightarrow32u+1,\qquad
  3(32u+1)\leftrightarrow3x .
  \]
* At a direct leaf keep its one canonical arrow. At a word leaf keep the ordinary moves from the historical source $s$ to $3s$. Expand every $M$ letter at $q=32v+11$ into the ordinary edge to $y=(3q+1)/2$, the canonical arrow $y\to3y$, and an ordinary path from $3y$ to $3q$ through $T^4(3y)=T^5(3q)$. Add both orientations of each ordinary edge. [PR197 ordinary exchanges](pr197-floor/UnitResidueExchange.lean) · [Nonunit chain](pr197-floor/NonunitExit.lean) · [Plan and source-budget proof](DefectBank.lean)

In this finite graph let $G(v)$ mean that $v$ can reach $3w$, and let $D(v)$ mean $\neg G(v)\land G(3v)$. Suppose there were no path from $w$ to $3w$. Then $D(w)$ holds. Each retained ordinary merger preserves $G$ in both directions. At a unit node the displayed equalities propagate $D$. At a nonunit node the three equalities give a chain from the bad lower label to the good upper label. Either $D(16u+1)$ or $D(32u+1)$ holds, according to the intermediate label. All earlier labels in the selected history remain available. This reaches a terminal with $D(s)$. The terminal's included edges give a path from $s$ to $3s$, which contradicts that label. This argument uses ordinary invariance only on the edges actually included in this finite graph.

Every canonical source in the graph is at most $4096w$. Every vertex is at most $(10347374580560/219537)w$. For the edge count, take the maximum over children of a radix split. Add the two merger lengths at a unit node, or all three merger lengths and both child bounds at a nonunit node. Count a canonical direct leaf as one edge. At a word leaf sum the ordinary edges and the expanded $M$ paths. The resulting uniform bound is **3780 edge occurrences**. A shortest $w$-to-$3w$ path is simple, so it uses at most 3780 edges even when an ordinary occurrence was installed in both directions. Breadth-first search in the finite specialization constructs one. [Affine height controls](OPTIMIZED_BANK_CONTROLS.json) · [Edge-count recurrence and implementation](check_canonical_paths.py)

## Strict descent and concatenation

For odd $n\ge3$ the 140 first-stage rows give a path to a positive $v<n$. Each initial tripling source $w$ is at most $24n$ and is 1 modulo 16. For an affine source $at+b$ and terminal $At+B$, checking both $A/a$ and $B/b$ gives the uniform contraction $v\le(725/763)n$. On the row $n=6912t+763$ the terminal is $6561t+725$, attaining the bound at $t=0$. The one-step even descent has ratio $1/2$.

Before replacing the binary-source arrows, every physical intermediate vertex is at most $162n$. A word has at most 135 individual edges and at most eight binary-source arrows. Replacing each such arrow by a simple canonical path gives at most **30367 edges** on any one descent. The count is evaluated per first-stage word. All new vertices satisfy the local height bound multiplied by 24, and $24\cdot4096=98304$ bounds every canonical source relative to the original input. Each subsequent descent starts below that input. [First-stage plan](ReturnTwentyFour.lean) · [Exact bounds](CANONICAL_PATH_CONTROLS.json)

The integer inequality $2\cdot725^{14}\le763^{14}$ means that every fourteen descents halve the remaining input unless it has already reached one. At most $14\lceil\log_2 n\rceil$ descents suffice. Their concatenation gives the stated length bound. At $n=1$ the empty path realizes the formula.

## Reproduction and scope

The checker expands complete affine ordinary mergers. Its callable `path_to_one(n)` specializes both plans and returns a list of triples $(x,y,c)$ for the actual input, where $c$ records whether the edge is a directed canonical tripling. It verifies seven literal routes, including $2^{127}-1$, for which it obtains 358 edges and seven canonical arrows. The claimed uniform bounds use the exhaustive finite recurrences, independently of these examples. [Checker](check_canonical_paths.py) · [Archived literal routes and uniform controls](CANONICAL_PATH_CONTROLS.json)

Paper 228, §2, gives paths from 1 to $n$ with odd tripling cofactors and linear height. Paper 232, §7, gives returns from $n$ to 1 with odd cofactors prime to three and height at most $7n$. The present return theorem restricts every extra arrow to the single canonical class $17\bmod48$, gives an explicit logarithmic length bound, and pays a substantially larger height constant. PR197 supplies the physical exchanges used to enforce that residue restriction. [Paper 228](https://rstation.ai/problems/collatz/papers/228/v1) · [Paper 232](https://rstation.ai/problems/collatz/papers/232) · [Pinned PR197 source metadata](GLOBAL_RETURN_CONTROLS.json)
