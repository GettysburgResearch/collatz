# A twelve-cell ordinary inverse cover

For a positive integer $q$ coprime to three, use $L_a(q)=(2^a q-1)/3$ when it is integral. Each row lists the allowed classes of the current integer and an inverse word read **left to right**. Every intermediate result is an odd positive integer coprime to three. The first target $q$ may be even.

| Modulus | Residues | Successive inverse exponents |
|---:|---|---|
| 9 | 1, 4 | 2 |
| 9 | 2, 8 | 1 |
| 9 | 5 | 3 |
| 27 | 7, 16 | 4, 2 |
| 81 | 25, 52 | 6, 1, 2 |
| 243 | 79 | 4, 6, 1, 1 |
| 243 | 160, 241 | 4, 4, 2, 1 |

To check coverage, start with the six unit classes modulo nine. The remaining class seven splits into 7, 16, 25 modulo 27; the remaining class 25 splits into 25, 52, 79 modulo 81; the remaining class 79 splits into 79, 160, 241 modulo 243. For word length $r$ the row modulus is $3^{r+1}$. Applying any first $j$ inverses to a translate of a displayed residue by $3^{r+1}t$ changes the result by $2^{A_j}3^{r+1-j}t$, where $A_j$ is the sum of these exponents. Testing the displayed representatives therefore checks integrality and nondivisibility by three through the **last** output, uniformly on every lift. Oddness follows since the numerator is odd. An integral inverse is positive and the shortcut map takes it to its own preceding target in exactly $a$ steps. This remains true if that target is even.

Each block has positive length $r\le4$ and total clock at most $3r$. Iterate the choice starting from any positive unit and enumerate *every* intermediate inverse, obtaining a path $y_0=q,y_1,y_2,\ldots$ with $T^{A_s}(y_s)=q$. Every prefix of length $i$ in the small table has cost at most $3i+4$. Thus $s\le A_s\le3s+4$, including within the last block. In particular
$$
 y_s\le 2^{A_s}3^{-s}q,\qquad y_s+1\ge(2/3)^s(q+1).
$$
All $s\ge1$ give ordinary odd endpoints. When $q\ge2^Q$, $1\le s\le Q$, the smallest intermediate value is at least $(4/3)^Q-1$. The exact logarithm contains the signed accumulated correction
$$
 \log_2 y_s = \log_2 q + A_s-s\log_2 3
 +\sum_{j=1}^s\log_2\!\left(1-\frac1{2^{a_j}y_{j-1}}\right).
$$
Its magnitude is $O(Q(3/4)^Q)$ after removing the first three terms, uniformly over all the target values and legal rows in this range. Thus the phase mesh uses each $s$, including the partial blocks. A later marked predecessor whose first odd endpoint is $y_s$ can serve at most $3Q+5$ selected targets, since each target lies on its ordinary forward orbit within $3Q+4$ clocks.

For the one-sided grid estimate one may take a subsequence with $|\alpha-a/Q|<1/(2Q^2)$, for $\alpha=\log_2 3$. Consecutive convergents $a/q,b/r$ lie on opposite sides of $\alpha$ and have distance $1/(qr)$. Both errors cannot be at least $1/(2q^2),1/(2r^2)$ respectively, since their sum would exceed $1/(qr)$ for distinct positive $q,r$. Hence infinitely many denominators admit the factor $1/2$. For these denominators the perturbations of the complete rational grid over $1\le s\le Q$ lie in one interval of length at most $1/(2Q)$, so its one-sided mesh is at most $3/(2Q)$.

[InverseWordCover.lean](InverseWordCover.lean) checks the complete table for arbitrary positive ternary units and the precise physical single-link clock. The infinite concatenation, cumulative exponent and phase bounds use the elementary arguments above. [check_inverse_word_cover.py](check_inverse_word_cover.py) independently checks both the residue table and concatenated physical paths, including even roots.
