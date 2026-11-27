# Strong connectivity using only canonical tripling sources

Retain both directions of each ordinary shortcut edge $x\leftrightarrow T(x)$ and add only the directed arrows $q\to3q$ with $q\equiv17\pmod{48}$. Write $L(x)=\lceil\log_2 x\rceil$ for $x\ge1$.

**Written finite-graph theorem.** Every positive $n$ has a path **from 1 to $n$** with at most $690144L(n)$ edges. Every directed tripling source is at most $(40505344/43)n<941985n$. All positive vertices are at most $(102325187227157840/9440091)n<10839428056n$. Joining this construction to the previous return gives a directed path from *any* positive $a$ to *any* positive $b$ with at most $425138L(a)+690144L(b)$ edges. The return and outward height bounds apply separately to the two segments. [Constructive return to 1](CANONICAL_PATHS.md) · [Outward tree and path constructor](check_canonical_connections.py)

Consequently, if $n$ fails to reach one under ordinary iteration, some canonical $q\le(40505344/43)n$ has $G(q)$ and $\neg G(3q)$. Indeed a path from 1 to $n$ starts inside the ordinary basin and ends outside. Its first edge leaving the basin must be a forward canonical arrow. The previous return to 1 supplies the opposite orientation $\neg G(y)$ and $G(3y)$ at a canonical $y\le98304n$. In particular, either one of the two possible **universal** one-way basin implications on the single class $17\bmod48$ would suffice for ordinary convergence. Strong connectivity is proved in the augmented graph. Both ordinary implications remain open.

## Thirty-one contracting rows in the opposite orientation

Start at an odd $n=2t+3$. Each internal node splits $t$ by its residue modulo two or three, with all children present. A leaf lists positive ordinary forward blocks, negative ordinary inverse blocks, and zeros. A zero takes the temporary step $3w\to w$ at $w\equiv1\bmod16$. The 31 leaves cover the full progression and have total relative mass one. Before replacing the zeros their exact bounds are as follows.

| Quantity on one descent from $n$ | Bound |
|---|---:|
| Terminal divided by $n$ | $1405/1479$ |
| Any physical vertex divided by $n$ | $66752/43$ |
| Any binary cofactor $w$ divided by $n$ | $9889/43$ |
| Number of ordinary and temporary edges | $169$ |
| Number of temporary edges | $13$ |

For each row the checker expands all ordinary shortcuts at both affine coefficients. A zero requires slope divisible by 48 and intercept 3 modulo 48 at its input. Dividing both by three therefore gives a whole positive cofactor row $1\bmod16$. Its two coefficients and those of each physical vertex are compared with the coefficients of the original $n$. Every leaf ends at a strictly smaller positive integer. For example, $n=2304t+1479$ ends at $2187t+1405$, attaining the stated contraction at $t=0$. Even $n$ can be halved.

For the actual outward path **reverse each descent**. Each zero now requires $w\to3w$, precisely the direction established by the canonical localization graph. Replace it by the finite ordinary-and-canonical path at that same $w$. Such a replacement uses at most 3780 edges, has canonical sources at most $4096w$, and visits only vertices at most $(10347374580560/219537)w$. Maximizing the sum over each of the 31 rows gives 49296 edges per expanded stage. Multiplying the source and height ratios by $9889/43$ gives the two outward caps. All earlier descents in the chain start at most at the original terminal $n$. Since $2\cdot1405^{14}\le1479^{14}$, at most $14L(n)$ stages are needed. Reversing their order constructs the claimed outward route. [Local path and finite-graph proof](CANONICAL_PATHS.md) · [Exact outward controls](CANONICAL_CONNECTION_CONTROLS.json)

The callable `outward_path(n)` returns each positive edge, in its actual direction, from 1 to the requested integer. The checker replays seven paths, including the route to $5^{54}+2$, which uses 3054 edges and 105 canonical arrows. The all-input result uses the 31 complete affine rows and the finite local graph proof. Its exact logarithmic constants and path construction are written and independently computed. They are separate from the kernel's ordered-defect statements.

Paper 228 gives paths from 1 using odd tripling cofactors. Paper 232 gives strong connectivity using odd unit cofactors and smaller height constants, including a $7n$ return bound. PR197 supplies the directed and nonunit exchanges in the local canonical plan. The present result requires every directed cofactor, in both directions of travel between endpoints, to lie in $17\bmod48$. [Paper 228](https://rstation.ai/problems/collatz/papers/228/v1) · [Paper 232](https://rstation.ai/problems/collatz/papers/232) · [Pinned PR197 modules](GLOBAL_RETURN_CONTROLS.json)
