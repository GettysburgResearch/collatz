# All color patterns on a fixed list of ordinary trit queries

**PROPOSED written consequence of SELECTED_TRIT_CELLS.md** (SHA-256 4288ae981f46f9e079e60393060da373205303f19330904e88046f9d6fc13e4f). The tree there chooses its next query after the branch is known. Here a common list of queries, physical real windows and ternary residue classes is chosen once for the entire opening cell. Its guaranteed size tends to infinity whenever the chosen ternary depth satisfies $\log d+u=o(m_*)$, including the two choices below. Each pattern is attained by many sources of the **same originally selected population**. The source-qualified finite merger and ordinary regeneration assumptions are exactly those of the tree.

Use that note's late slab of $W=\lceil\sqrt{d\log d}\rceil$ clocks, its polynomial-density set $S$, and one opening cell supporting the tree. Its depth is $m_*=\lfloor W/b\rfloor$ with $b=\lceil K_1\sqrt{W\log\log d}\rceil$, and all its sources have the same coarse exterior and the same $m\bmod 3^B$, $B=\lfloor\kappa b\rfloor$. Fix an integer $0\le u\le B$. There is a list of at least
$$
                    k\ \ge\ c\,\frac{m_*}{\log d+u}
$$
questions at clocks in **different designated time blocks**. A question fixes the clock, the choice of original physical arm, the trit truncation depth, a coarse-coordinate exponent and correction, and one residue class modulo $3^u$. There is a fixed ordinary real interval of length $2^{O_A(W)}$ for each question; these intervals may be chosen pairwise disjoint. For every one of the $2^k$ binary answer patterns, at least $\exp(c'W)$ distinct coarse integers of actual sources in $S$ simultaneously satisfy the following requirements.

* At each specified clock the original physical search really reaches the specified trit query on the designated arm. Its ordinary argument is in the specified interval and ternary residue class, has the fixed coarse formula, and gives the prescribed invariant-color answer.
* One entire leaf of the original chronological tree witnesses the pattern. At each of its $k$ questions the sources in that leaf give at least $\exp(c'W)$ **distinct ordinary trit arguments**, all of the prescribed color. All these realizations belong to the same opening cell across patterns, and any ordered original disagreement prescribed in $S$ is preserved.

In particular $u=\lceil\log d\rceil$ gives $k\gg(d\log d)^{1/4}/(\log d\sqrt{\log\log d})$ with polynomial ternary moduli. Alternatively $u=\lfloor\sqrt{m_*}\rfloor$ makes both the prescribed ternary depth and the number of common questions $\gg\sqrt{m_*}$. The list, the windows and the classes may depend on $S$ and its opening cell. The statement concerns source-dependent ordinary **arguments of fixed questions**. One fixed integer cannot have two invariant colors.

## A finite domain of partially defined questions

Write $m=\ell+2^{\Delta_t}q$ at time $t$. For a trit truncation at a split of the tree, its actual argument is
$$
 z=3^e q+c_\ell=\lfloor 3^e m/2^{\Delta_t}\rfloor+b',\qquad
 b'=c_\ell-\lfloor 3^e\ell/2^{\Delta_t}\rfloor .
$$
The current physical arm, its exponent, its truncation depth and $c_\ell$ are determined by the opening seeds, the public prefix and the earlier replies at this clock. Both branches of this particular split therefore have *one identical* $b'$. The physical scalar intercept relative to the original coarse affine leading term is polynomial on every good source, since the true original iterate has intercept $O_A(d^{C_A})$, dropping the fractional part of $c_0n$ costs at most one at these re-based scales, and ternary truncation divides the error with a bounded rounding adjustment. Thus $|b'|\le d^{C_A}$ at every tree node. No branch is subdivided by a source-dependent rounding correction in the original $n$ coordinate.

Since $m\bmod3^B$ is fixed and the low binary prefix agrees at a split, the two branches also share $q\bmod 3^B$, so their common feature can include $z\bmod3^u$. Two different splits can use the same feature without the node histories being identical. Define a feature by the tuple $(t,i,v,e,b',z\bmod3^u)$, with $i$ one of the two initial arms and $v$ the trit depth. The number of such features on the whole tree is at most $N_f=d^{C_A}3^u$, since $v,e=O_A(W)$ and there are $W$ clocks. For a particular source the response can be left **undefined** if its search does not visit this physical arm and depth at $t$ with the specified exponent, correction and residue. The feature is definite on every source in both children of its own split.

Across the whole opening cell, $m$ ranges in one interval of length $2^H$. A fixed $(t,e,b')$ thus has arguments in a single interval of diameter at most $1+3^e2^{H-\Delta_t}=2^{O_A(W)}$. If the list is realized by a leaf then a common source in that leaf realizes all of its feature centers. The different-clock logarithmic separation of SELECTED_TRIT_CELLS.md and the exponential physical heights make all the prescribed intervals disjoint for large $d$.

## Counting block-transversal subsets

At a leaf put only the empty feature set in its inventory. Induct upwards. If the two children's inventories are $\mathcal A,\mathcal B$ and the current split feature is $x$, take
$$
    (\mathcal A\cup\mathcal B)\ \cup\
        \{Y\cup\{x\}:Y\in\mathcal A\cap\mathcal B\}.
$$
Every inventoried set uses at most one feature per time block, as $x$ belongs to the current block and all descendant features belong to later blocks. Every binary pattern on such a set is witnessed by an **entire descendant leaf which actually splits at the corresponding features along its path**. This is immediate for the empty set. A member of the union uses the indicated child. For $Y\cup\{x\}$, the requested answer at $x$ selects the child, and $Y$ already has every pattern witnessed in that child. The induction therefore never extends any partial response by an invented answer.

The two parts of the displayed inventory are disjoint, adjoining $x$ is injective on the intersection, and the inventory cardinality equals $|\mathcal A|+|\mathcal B|$. There are at least $2^{m_*}$ inventoried feature sets at the root. If the largest size is $k$, the number of subsets of a domain of cardinality $N_f$ having size at most $k$ is at most $(N_f+1)^k$ (sort their members in a fixed order and pad to $k$). This proves the stated lower bound. This finite inclusion argument follows the classical shattering count of N. Sauer, *On the density of families of sets*, Journal of Combinatorial Theory A 13 (1972), 145–147, DOI 10.1016/0097-3165(72)90019-2. The block order, partially defined responses and preservation of the whole leaf are checked directly above.

Finally each witnessing leaf retains at least $\exp(c'W)$ distinct coarse integers by the original source occupancy bound and $W$-bit reserve, including after its last split. All have identical low prefixes through each distinguished split on that path. At one such split the fixed $q\mapsto3^eq+c_\ell$ is injective on these distinct coarse integers. This proves the ordinary site counts simultaneously without claiming that different trit arguments on different features are independently sampled.

An upper estimate on the number of these simultaneous realized patterns in genuinely discordant selected populations remains open. Neither univariate ordinary color density in a window nor a count for a single trit query supplies this upper estimate.
