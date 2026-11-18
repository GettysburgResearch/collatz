# Individually excluded quadratic-image survivor codes

**PROPOSED.** Let $e(j)=Aj^2+Bj+u(j)$ with rational $A>0,B$ and rational periodic $u$, and suppose $e(j)$ is an integer for every $j\in\mathbb Z$. Let $D$ be any nonempty periodic subset of $\mathbb Z$. The binary survivor code whose support is
$$
\{e(j): j\in D,\ e(j)\ge0\}
$$
has transcendental value in $\mathbb Q_2$. Arbitrary finite edits preserve transcendence. This gives individual exclusions for square, triangular and generalized pentagonal support, periodic sieves of any of these, and the two-sided exponent images canonically attached to every native periodic increment word.

Indeed, for any fixed pair of residue classes of $j,k$ modulo a common period, the collision equation with $j\ne k$ reads
$$
(j-k)(j+k+B/A)=(u(k)-u(j))/A.
$$
If its right side is nonzero it has only finitely many integral solutions, by clearing its fixed denominator and factoring a fixed nonzero integer. Otherwise a collision can only be the reflection $k=-B/A-j$. In particular whenever this reflection exists it is unique. Give each $j\in D$ weight $1/2$ if its reflection is integral, belongs to $D$ and has the same $u$, and weight 1 otherwise. Put weight 0 off $D$. These weights are periodic. Except for the finitely many non-reflected collisions, the possible fixed point of the reflection, and finitely many negative exponents, summing the weights at a given image exponent gives exactly its binary indicator.

Consequently the survivor value differs by a rational number from $(17/81)\sum_{j\in\mathbb Z}w_jT^{e(j)}$, $T=64/81$. Complete the square and combine reflected root-variable weights as in [the bilateral sum proof](COMPANIONS.md). The resulting even periodic weight is nonzero, since all nonzero original weights are positive in the real embedding. The resulting value is transcendental by the [2-adic modular theorem](PROOF.md). The normalization is the repository's [binary survivor chart, D-9401](https://github.com/gfreund123/collatz/blob/82ca2f932438a9fe0897704ba62959ca23ec830f/research/padic-repetition/claims/D-9401-survivor-code.md).
