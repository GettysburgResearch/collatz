# When a clock language would force finitely many integer cycles

**PROPOSED written theorem.** Let $L$ be the set of **nonempty** binary shortcut words obtained by starting at any phase of any positive integer cycle and making any positive number of full laps. Let $P(L)=\{(|w|,\#1(w)):w\in L\}$. Then the following are equivalent.

1. There are finitely many primitive positive integer cycles.
2. $L$ is regular.
3. $L$ is context-free.
4. $P(L)$ is semilinear, meaning a finite union of a base point plus all nonnegative integer combinations of finitely many period vectors.
5. $P(L)$ admits a semilinear cover contained in $\{(h,p)\in\mathbb N^2:p>0,\ 2^h>3^p\}$.

The argument yields a finite arithmetic cutoff from explicit cover generators. Its existence is open. The equivalence includes the possibility of finitely many nontrivial cycles. Divergent trajectories are a separate question.

## The clock margin

A positive cycle necessarily has an odd departure since a nonempty entirely even lap strictly decreases. Write its odd vertices in chronological order as $x_i$, put $m=\min_i x_i$ and let $e_i\ge1$ be the number of divisions by two before the next odd vertex. Then $2^{e_i}x_{i+1}=3x_i+1$, $\sum_i e_i=h$, and the number of odd edges is $p$. Multiplication around the closed orbit gives
$$
               3<2^{h/p}=\left(\prod_i (3+1/x_i)\right)^{1/p}
                         \le3+1/m.                                 \tag{1}
$$
Different cycles have different integer minima by determinism. If there are infinitely many, a sequence of them has $m\to\infty$ and therefore $h/p\to\log_2 3$. Each individual slope remains strictly above this irrational number. A fixed rational slope gives a bounded minimum and can occur on only finitely many distinct cycles.

More generally any semilinear subset of the strict half-plane $p>0,\ h>p\log_2 3$ stays a fixed angular distance above its boundary in the coordinate $h/p$. Each base in a linear component lies in this half-plane. For a generator $(u,v)$ with $v>0$, the whole ray through the base remains there, so $u/v\ge\log_2 3$. Equality is impossible since $2^u=3^v$ is impossible for positive $v$. A generator with $v=0$ cannot decrease the ratio, including the zero generator. The least among the finitely many base slopes and positive-$v$ generator slopes gives an explicit rational $A/B>\log_2 3$. Every sum of the base and generators satisfies $Bh\ge Ap$. This proves $5\Rightarrow1$ by (1). An empty cover would have no positive cycles; in the stated setting the trivial cycle already belongs to $L$.

For the other implications, finitely many primitive cycles yield a finite union of languages consisting of the positive powers of their finitely many rooted rotations. These are regular. Every regular language is context-free. Parikh's theorem makes the count vectors $(\#0,\#1)$ of a context-free language semilinear, and the linear map $(a,b)\mapsto(a+b,b)$ preserves semilinearity. Finally (1) shows that $P(L)$ is its own eligible cover when semilinear. The proof requires neither a logarithm irrationality-measure bound nor the Subspace Theorem. [Parikh, *On Context-Free Languages*](https://doi.org/10.1145/321356.321364)

## Exact finite use of a supplied cover

For $B\ge1$ and integer $A$ with $2^A>3^B$, the two inequalities $Bh\ge Ap$ and (1) give
$$
             2^A m^B\le(3m+1)^B
               \le 3^B m^B+(4^B-3^B)m^{B-1}.
$$
The upper bound follows by expanding the binomial and bounding every proper power of $m$ by $m^{B-1}$. Thus every candidate satisfying the supplied clock margin has
$$
                 m\le\left\lfloor\frac{4^B-3^B}{2^A-3^B}\right\rfloor.
$$
A verification that all ordinary sources up to this explicit bound reach 1 excludes nontrivial cycles in the covered population. The bounded formal derivation works directly on a list of native equations $2^{e_i}x_{i+1}=3x_i+1$ with an arbitrary positive floor throughout its closed path. [Lean physical cutoff](ClockFloor.lean)

For example the clock margin $h/p\ge 8/5$ gives the bound $(4^5-3^5)/(2^8-3^5)=781/13$, hence minimum at most 60. This example illustrates the finite calculation. It supplies no such margin for every cycle. Deep hypothetical cycles approach the irrational boundary from above, and a cover which crosses that boundary no longer implies a finite cap.
