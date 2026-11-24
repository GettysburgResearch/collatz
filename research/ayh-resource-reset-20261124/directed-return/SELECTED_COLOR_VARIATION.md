# Exponential ordinary color variation in the selected windows

**PROPOSED written corollary.** Use the hypotheses, opening cell and fixed list in FIXED_TRIT_PATTERNS.md (SHA-256 44e942fda19002fd074a84ff200b05bd2665b7059e58707b534716e2b7652902). Write $J_i$ for the full fixed real interval of feature $i$, and $a_i\bmod 3^u$ for its fixed ternary class. The $k$ windows are disjoint, each has length at most $2^{C_A W}$, and every one of the $2^k$ binary patterns is realized simultaneously by ordinary sources in the chosen population. Here the common gap $3^u$ is fixed before extracting the feature list.

Let $V_i$ count consecutive points of the finite progression $J_i\cap(a_i+3^u\mathbb Z)$ having different invariant colors: each is a literal pair $z,z+3^u$ of positive ordinary integers. For **every** subset $E$ of $r\ge1$ listed windows,
$$
                      \sum_{i\in E} V_i\ \ge\ 2^r-1.
$$
In particular, in nondecreasing order $V_{(r)}\ge(2^r-1)/r$. At least $k-\lceil k/2\rceil+1$ disjoint physical intervals thus each contain at least $(2^{\lceil k/2\rceil}-1)/\lceil k/2\rceil$ different fixed-gap color changes. Along each progression the nonzero changes alternate, so each direction occurs at least $\lfloor V_i/2\rfloor$ times there. Each $J_i$ also contains at least $V_i$ genuine unit-spacing adjacent changes of the ordinary invariant label. These are defect counts within the indicated physical intervals; the intermediate transition sites need not themselves be queried by the original search.

For each binary pattern on $E$ choose one realizing coarse integer $m$ by extending it arbitrarily on the other listed features. Different patterns give different integers. Sort these $2^r$ integers as $m_1<\cdots<m_{2^r}$. For fixed $i$, the actual query arguments at these representatives equal one monotone function
$$
       z_i(m)=\left\lfloor3^{e_i}m/2^{\Delta_{t_i}}\right\rfloor+b_i .
$$
All are in the designated finite progression. Whenever the $i$-th answer changes between two consecutive representatives, their $z_i$ values differ. Some consecutive lattice pair in the half-open interval from the earlier $z_i$ up to the later one changes color. Those half-open intervals do not overlap for different such changes in the same coordinate; equal argument plateaus cost no change. Each of the $2^r-1$ consecutive pairs of patterns differs on at least one coordinate. This proves the bound. Apply it to the $r$ smallest $V_i$. Finally the half-open ordinary unit-gap intervals between adjacent progression sites are disjoint within $J_i$; whenever their endpoints disagree at least one intervening ordinary adjacent label changes.

For $u=\lfloor\sqrt{m_*}\rfloor$, both $u$ and $k$ are at least constant multiples of $(d\log d)^{1/8}/(\log\log d)^{1/4}$. This demands a superpolynomial number of true color changes on one fixed translation gap in each of many selected real windows. Polynomial relative density of two colors by itself can coexist with a single boundary. The source-conditioned oscillation proved here uses all joint patterns along a common ordered parameter. The available ordinary merger bounds do not give a contrary upper bound in these selected intervals.
