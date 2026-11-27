# A positive-definite kernel and a fixed ordinary pair

Let $K(i,j)$ be one if the forward orbits of two positive ordinary integers meet at possibly different clocks, and zero otherwise. Meeting is an equivalence relation. For transitivity, advance the two meeting points on the shared middle orbit to the later clock. With one orthogonal unit vector per component, $K$ is their Gram matrix. A common random map $\phi$ from indices to positive integers consequently gives a positive-semidefinite matrix $\mathbb E K(\phi(i),\phi(j))$.

Suppose a positive bad source $m$ exists. The original matrix has $K(1,2)=1$ and $K(1,m)=0$. Both entries survive every common dilation $\phi(i)=2^ki$, including any mixture of such dilations. The resulting matrix is the original one. By contrast, averaging over common translations $\phi(i)=s+i$ through increasingly long initial intervals gives limit one for every fixed pair of positive indices by fixed-gap absorption. These two explicit choices show where the fixed source enters the analytic argument. [Counted-absorption estimate and residue transfer](https://rstation.ai/problems/collatz/papers/13)

There is also a natural common affine average whose limiting Toeplitz kernel can have two different values. On a prime row $P$, sample $S,D$ independently and uniformly modulo $P$, allowing $D=0$, and set $\phi(i)=1+[(S+iD)\bmod P]$. If $p_C$ is the fraction of the actual ordinary row $\{1,\ldots,P\}$ in component $C$, then exactly

$$
 \mathbb E K(\phi(i),\phi(j)) =
 \begin{cases}
 1,&i=j\bmod P,\\
 c_P=\sum_C p_C^2,&i\ne j\bmod P.
 \end{cases}
$$

For unequal residues the two outputs are independent uniform row indices, by invertibility of the $2\times2$ coefficient matrix. The representing measure on the circle is $c_P\delta_0+(1-c_P)P^{-1}\sum_{r<P}\delta_{r/P}$. If a bad source exists, the good and bad parts of the row each have positive lower density by the fixed-target result, so $1-c_P$ stays bounded below. Yet for $P>m$ this average assigns the *same* value to $(1,2)$ and $(1,m)$. The finite-field sampling with wraparound is an averaging device for ordinary labels. It asserts no Collatz intertwining modulo $P$. [Mazur, fixed-target theorem](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

For any common random indexing let $D(i,j)=1-\mathbb E K(\phi(i),\phi(j))$. This is a pseudometric by the triangle inequality for pointwise label disagreement. If $D(1,2)=0$ and $D(1,m)\ge\epsilon$, then some $2\le j<m$ has $D(j,j+1)\ge\epsilon/(m-2)$. Here $m>2$ since 1 and 2 are good. More generally $D(1,m)\le D(1,2)+(m-2)\max_{2\le j<m}D(j,j+1)$. Hence a Toeplitz limit with exact agreement at distance one necessarily assigns agreement one to every fixed pair. The finite counting lemma is checked for arbitrary component labels and any common finite family in [ComponentGram.lean](ComponentGram.lean).

A global proof along this route would need an averaging procedure that retains both the known edge and an hypothesized fixed separation while proving translation invariance for those averages. The formulas identify the exact loss in three candidate averages. Positivity of the full component Gram holds before any averaging and supplies no additional estimate on that loss.
