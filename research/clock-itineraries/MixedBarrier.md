# A converging source that passes both finite obstruction tests

Fix a horizon $H$ and lower bound $A$. There is an ordinary odd unit $a>A$ with $a>2$ and $a\equiv1\pmod{3^{H+1}}$ with the following properties.

- The first $H$ odd gaps of $a$ are all one, and the next odd gap lands at one.
- For every $k\le H$, the elapsed shortcut clock is exactly $k$, and the $k$-th odd state is at least $a$. In particular $2^{6k}\le(k+1)3^{6k}$, so the forward clock test never crosses during this interval.
- Every nonempty ordinary inverse path to $a$ with at most $H$ odd gaps starts strictly above $a$, with no upper bound on its shortcut clock.

To construct the source, take $M=3^{H+1}$ and choose $w>A+1$ satisfying $2^Hw\equiv1\pmod M$. Such choices exist because $(M+1)/2$ is an inverse of two modulo $M$. The odd input $a_0=2^{H+1}w-1$ then has the required ternary residue. Its first $H$ gaps are one and end at $q_0=2\cdot3^Hw-1$.

The simultaneous-shadow theorem translates this entire physical path so that one additional odd gap takes its final state to one. The change in the initial value is a multiple of $2^{H+1}M$, preserving both residues. The inverse bound follows by reducing $a\equiv1\pmod M$ to each depth and applying the no-descent theorem for the residue one. All statements concern the same known converging integer. [Lean theorem](MixedBarrier.lean)

At $H=1$, one example is $14563\equiv1\pmod9$. Its first step reaches $21845$, and $3\cdot21845+1=2^{16}$, so its next odd gap lands at one.
