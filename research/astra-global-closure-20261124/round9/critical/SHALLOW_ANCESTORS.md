# First depth admitting a smaller bad-multiple certificate

**Exact finite search and written extension to ordinary integers.** Suppose $s\ge10^{11}$ satisfies the local conditions for the restricted cycle. It suffices that $s=1\pmod9$ and its previous 17 odd sites along the minimal-exponent path exist in $[s,(16s+7)/3]$. A useful odd ancestor $z$ in this test must satisfy either $4z<3s+1$, the known good interval, or $3\mid z<2s+1$, the known good multiples. Then these conclusions hold.

* No inverse word of one through fifteen odd steps ending at $s$ supplies such a $z$.
* At sixteen odd steps none supplies the good interval. An inverse word supplies a smaller multiple of three precisely on $s=116582680\pmod{3^{17}}$, subject to the stated local hypotheses.

The test permits arbitrary even-step counts between its odd steps. It concerns paths ending at the prescribed $s$. Other endpoints in its component are separate tests. The sufficiency of the stated class follows from the actual ordinary progression in [the main proof](README.md).

For a reversed odd word with exponents $a_i\ge1$, put $A_j=a_1+\cdots+a_j$ and $C_0=0$, $C_j=2^{a_j}C_{j-1}+3^{j-1}$. Its prospective ancestor satisfies

$$
  3^j z=2^{A_j}s-C_j,\qquad
  z=\frac{2^{A_j}}{3^j}(s-\eta_j),\qquad
  0<\eta_j=\sum_{k=1}^j\frac{3^{k-1}}{2^{A_k}}\le(3/2)^j-1<656\quad(j\le16).
$$

Legality requires $s=C_j2^{-A_j}\pmod{3^j}$. A terminal multiple of three requires the same congruence modulo $3^{j+1}$. These necessary tests suffice for exclusion. The positive paths on the retained explicit progression were verified separately. If $2^{A_j}/3^j>2$, its excess over 2 is at least $3^{-16}$. If it exceeds $3/4$, its excess is at least $1/(4\cdot3^{16})$. The displayed bound on $\eta_j$ and $s\ge10^{11}>656+(3\cdot656+1)3^{16}$ show that an ancestor meeting either height test must satisfy respectively $2^{A_j}\le2\cdot3^j$ or $4\cdot2^{A_j}\le3\cdot3^j$. This accounts also for arbitrarily large individual $a_i$.

For the restricted reference path, let $G_j$ be its reverse cumulative exponent and write its $j$th site as $2^{G_j}3^{-j}s-d_j$. Then $d_0=0$ and $d_{j+1}=(2^{e}d_j+1)/3$, $e\in\{1,2\}$, giving $d_j\le(4/3)^j-1$. Since the actual sites are in the given height interval, for $1\le j\le17$ their coefficients satisfy

$$
         1<2^{G_j}/3^j\le161/30.
$$

The strict lower bound follows from positivity of $d_j$ and the minimum $s$. The upper bound follows from the stated height, the bound on $d_j$, and $s\ge10^{11}$. Each next $e$ determines exactly one further ternary digit of $s$ that makes the next inverse integral. This enumerates an explicit superset of all allowed initial ternary classes. There are 1,557 at precision 16 and 3,114 at precision 17 after imposing $s=1\pmod9$.

At odd depth $j$ the search enumerates all compositions with length $j$ and total at most $M_j=\lfloor\log_2(2\cdot3^j)\rfloor$, checking its total count against $\binom{M_j}{j}$. It checks each good-interval class against the precision-$j$ reference set, and each multiple class against the precision-$(j+1)$ reference set. Across all sixteen depths it checks 7,813,124 compositions. Only the stated depth-sixteen multiple class survives. Both standard and optimized Python print identical results with explicit guards. [Full enumerator](depth_sieve.py) · [Integer counts at every depth](../../../../reports/astra-global-closure-20261124/round9/critical/depth_sieve.json)
