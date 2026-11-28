# Exact position-by-position digit certificates at every floor

Let $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. Write the canonical ternary digits with one left and one right padding symbol, repeated outside the numeral. A radius-$r$ window is the $2r+1$ symbols centered on an actual digit. The following certificates allow an arbitrary real coefficient for each pair consisting of a position and a window. They also allow the coefficients to depend on the exact length.

**Theorem.** For $r=1,2$, at every integer length $L\ge L_r$ there is a finite multiset of positive integers prime to three such that all sources and their true shortcut images have exactly $L$ trits. At each individual position the entire window histogram of the inputs equals that of the images. The odd fraction is the same at every $L$, and exceeds $53/84>\log_3 2$. Here $L_1=10$ and $L_2=16$. In particular the testing integers can all exceed any prescribed floor. The multisets test source-dependent parity prices in the usual way: summing $F(Tn)-F(n)\le q-\mathbf1_{2\nmid n}$ against their weights forces $q$ to be at least the indicated odd fraction for every additive position/window score $F$.

The width-three fraction is $1132203/1790170$. The width-five fraction is

$$
\frac{160681138885642518752824520956448583294976942825721687}
{254478872673344227832204140442397827003658231711827181}.
$$

Paper 189/v2 constructed actual balanced certificates for smaller feature families, including width five at a stated floor. The companion [finite-witness theorem](DIGIT_RANKING_FINITE_WITNESSES.md) gives arbitrary radii and fixed polynomial position degree without a numerical size bound. Here the two displayed fractions come from explicit ordinary integers and the certificates balance the positions separately even as the length increases. This result concerns one-step additive rankings.

## Integer seeds

The complete data consist of [the two integer-weight lists](position_pump_seeds.json). The independent standard-library [checker](check_position_pump.py) computes each $T(n)$ directly, converts both numbers to trits, and compares each individual window. For the extra two-layer test it computes the quotient and remainder of the entire leading prefix by two. No linear-programming library or inferred decimal weight enters the verification. The [receipt](../../../reports/astra-global-20261128/escape/POSITION_PUMP_CHECKS.json) gives the exact totals and number of different nonzero interior arcs. The checker also inserts one and two copies of each layer, splits and joins integer path weights, reconstructs the new ordinary integers, and checks all their true window histograms and parity totals afresh. These four tests contain 202, 233, 2,088 and 2,356 distinct sources.

| Radius | Length | Sources | Smallest | Largest | Interior layers, starting at 0 | Different interior arcs |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 170 | 19,801 | 59,048 | 5, 6 | 68 |
| 2 | 16 | 1,822 | 14,351,215 | 42,876,134 | 9, 10 | 558 |

The searchable finite flow problem used long division from the most significant digit. Its variables were nonnegative arc weights in a finite layered graph. Flow conservation, signed position/window balance, normalization and equality of the two designated arc layers are linear. A floating-point solver supplied candidate paths. Exact integer elimination on their actual signed feature columns produced the two lists. Verification of the theorem uses only these lists and the argument below.

## Repeating a middle layer

Write $d_j$ for the input digit at zero-based index $j$ from the left, $P_j$ for the integer represented by the first $j$ digits, and $(Q_j,c_j)=\operatorname{divmod}(P_j,2)$. On reading $d_j$, ordinary long division emits $q_j=\lfloor(3c_j+d_j)/2\rfloor$ and updates $c_{j+1}=(3c_j+d_j)\bmod2$. Write $e=n\bmod2$. The seeds have leading digit $2-e$. For $e=0$ the output numeral is $q_0\ldots q_{L-1}$. For $e=1$ the leading quotient digit is zero and the true output numeral is $q_1\ldots q_{L-1}2$, since $T(n)=3\lfloor n/2\rfloor+2$.

At an interior layer retain the state $(e,c_j,P_j\bmod 3^{2r},Q_j\bmod 3^{2r})$. An arc consists of its starting state and new digit $d_j$. It determines its ending state by the displayed division, and the input and output windows completed by its trits. The repeated layers start after at least $2r+1$ input trits and precede the last digit, so all retained tails there consist entirely of genuine digits, with fixed length $2r$. An arbitrary-width numeral description using the separate padding symbols is kept through the initial and final layers.

Let $A_k$ be the arc counts of the true seed paths at layer $k$. The checker proves $A_j=A_{j+1}$ entry by entry. The ending state counts of $A_j$ equal the starting state counts of $A_{j+1}$ by conservation along the original paths. Thus this common arc layer can be inserted any $h\ge0$ times between them while preserving conservation at both joins. The resulting finite layered integer flow decomposes into paths by repeatedly following a positive arc from the source to the sink and subtracting the least count on the path. Initial, terminal and parity tags agree along every resulting path. The initial digit still determines $e$, the final carry is still $e$, the source remains a unit at three, and the quotient rules above give its true shortcut image. The total flow of each tag and hence the odd fraction are preserved.

For clarity, an interior window whose final digit has index $k$ receives its input histogram from layer $k$, its even-image histogram from layer $k$, and its odd-image histogram from layer $k+1$. These histograms are functions of the corresponding arc alone, including its two stored digit tails. A neighboring ordered pair of transducer layers before the insertion is reproduced afterward, up to translating the position, except that the pair $(A_j,A_{j+1})=(A_j,A_j)$ now occurs $h$ additional times. Its input-minus-output histogram at the window completed there is zero by the original position balance. The initial and final padding windows retain their original counts, with the final part translated $h$ positions. This proves positionwise balance at length $L+h$. Counting positions from the right gives the same conclusion, since every source and image in one multiset has that same length. Finally every $L$-trit source is at least $3^{L-1}$.
