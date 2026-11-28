# A local cubic rank difference can take both signs at every finite depth

For four lifted integer labels $K_{i,j}$, $0\le j<4$, define the third difference $J_i=-K_{i,0}+3K_{i,1}-3K_{i,2}+K_{i,3}$. The full-band rank theorem of PR201 obtains strictly positive first and second differences on actual large cycles under its hypotheses. A third difference of fixed positive sign at all ranks would imply a cubic height lower bound by summation. The finite native constraints permit both signs even if an arbitrarily long window is imposed on both sides. [PR201, full-width strict second differences and inputs](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md)

**Finite ordinary realization.** Fix any finite past and future padding lengths. The four columns below can be realized as four trajectories of actual positive odd integers with native exponents one or two throughout this entire padded interval. They share the given mechanical clock after scaling by their actual lowbits in $\{1,2\}$. At every time their labels have strictly increasing positive first differences. All physical odd states in all columns and times lie in a common band of ratio strictly less than four. The third difference is zero outside the ten-edge pulse and takes both signs inside. The four columns are individually realized. This construction supplies no identification of the columns with four ranks of a common cycle.

Use $\gamma=\log_2 3$, dates $B_i=\lfloor17/100+i\gamma\rfloor$ and $m_i=B_{i+1}-B_i$ on all times in the chosen interval. For $i=0,\ldots,9$ the mechanical letters are $(1,2,1,2,2)^2$. This finite comparison also follows from $19/12<\gamma<46/29$ using integer powers. The table gives the four lowbits $\ell_{i,j}$ and the target third difference.

| Time $i$ | $m_i$ | Four lowbits | $J_i$ |
|---:|---:|:---|---:|
| 0 | 1 | 1, 1, 1, 1 | 0 |
| 1 | 2 | 1, 2, 1, 2 | 0 |
| 2 | 1 | 1, 1, 1, 2 | 1 |
| 3 | 2 | 1, 1, 2, 2 | 2 |
| 4 | 2 | 1, 1, 2, 1 | 1 |
| 5 | 1 | 1, 1, 1, 1 | 0 |
| 6 | 2 | 2, 1, 2, 1 | 0 |
| 7 | 1 | 2, 1, 1, 1 | −1 |
| 8 | 2 | 2, 2, 1, 1 | −2 |
| 9 | 2 | 1, 2, 1, 1 | −1 |
| 10 | — | 1, 1, 1, 1 | 0 |

Put all four lowbits equal to one throughout the padding. With $\Delta^3=(-1,3,-3,1)$, every edge obeys
$$
    2^{m_i}J_{i+1}=3J_i+\Delta^3\ell_i,\qquad
    2^{m_i}\ell_{i+1,j}/\ell_{i,j}\ \in\{2,4\}.                    \tag{1}
$$
[Lean checks of all ten edges and the affine third-difference identities](CubicPulse.lean)

## Lifting to positive ordinary trajectories

Number the padded edges $0,\ldots,N-1$ temporarily and denote the relative cumulative clock by $E_i=\sum_{t<i}m_t$. Put $A=2^{E_N}$ and
$$
           C_j=\sum_{i<N}3^{N-1-i}2^{E_i}\ell_{i,j}.
$$
The recurrence for $J$ with both boundary values zero gives $\Delta^3 C=0$. Choose the terminal $Y_0,Y_1,Y_2$ to be any odd integers in the respective residue classes $A^{-1}C_j\bmod3^N$, and impose $Y_3=Y_0-3Y_1+3Y_2$. The fourth value is odd and satisfies its required residue. This uses an invertible $A$ modulo $3^N$, and each of the first three choices ranges over one entire class modulo $2\cdot3^N$.

The starting label is $(A Y_j-C_j)/3^N$. Backwards iteration of $K_{i,j}=(2^{m_i} K_{i+1,j}-\ell_{i,j})/3$ is integral at every step. For example the congruence for the full interval implies each suffix congruence by reducing it modulo the corresponding power of three and canceling the dyadic prefix factor. Since each $Y_j$ is odd with terminal mark one, backwards induction in (1) gives $K_{i,j}/\ell_{i,j}$ an odd integer. In fact
$$
   3(K_{i,j}/\ell_{i,j})+1
      = (2^{m_i}\ell_{i+1,j}/\ell_{i,j})(K_{i+1,j}/\ell_{i+1,j}).
$$
Thus $\ell_{i,j}$ is the exact lowbit, and the odd quotients follow the literal accelerated Collatz map. The actual $J$ equals the displayed one by backward uniqueness at the chosen terminal third difference zero.

There is also a quantitative placement in consecutive geometric ranks. Fix the entire padded interval, choose $2<\xi\le3$, and let an integer parameter $P$ tend to infinity. For $j=0,1,2$ take $Y_j$ in its odd residue class nearest to $P^\xi 2^{j/P}$. Each error is bounded by $3^N$. For $j=3$ the quadratic completion changes this bound to at most $7\cdot3^N+P^\xi(2^{1/P}-1)^3=O_N(1)$. At every earlier time all four labels have the form
$$
            K_{i,j}=C_i^*2^{j/P}+O_N(1),\qquad
            C_i^*=P^\xi\,2^{E_N-E_i}/3^{N-i}.                       \tag{2}
$$
The slope and curvature of the main term at each fixed time grow respectively as $P^{\xi-1}$ and $P^{\xi-2}$. This gives positivity and strictly increasing positive gaps at every time for sufficiently large $P$ depending on the chosen padding. The ratio of the greatest and least $C_i^*$ on this finite interval is strictly less than two because the $E_i-i\gamma$ differ only by translated fractional parts lying in an interval of width strictly less than one. Formula (2) and marks at most two then give the strict physical ratio four. The geometry and error in (2) concern a fixed finite interval before passing to $P\to\infty$; $P$ is a placement parameter rather than an established cycle period.

The [exact control](check_sparse_cycles.py) constructs the four real integer trajectories for padding lengths $0,1,7,25,64$ on both sides using a positive integer quadratic terminal shape. It rechecks the actual binary odd transitions, lowbits, strict first and second differences, common physical height band and signed pulse for every state. The smooth placement (2) is a separate written argument. This example leaves room for an inherently cyclic third-difference estimate using the shared phase orbit or an average over all ranks.
