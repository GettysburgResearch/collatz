# Essential spectra with continuous functions of ordinary log height

**Proposed mathematical theorem.** Consider any positive ordinary Collatz component `Γ`, or the entire positive integer graph. On `ℓ²(Γ)` take the squared-slope composition operator `C`, its adjoint, every bounded periodic arithmetic multiplier, and all diagonal multipliers

\[
      (D_F f)(n)=F(\log n) f(n),\qquad
      F:\mathbb R\longrightarrow\mathbb C\ \text{bounded and uniformly continuous}.
\]

The essential norm of every unital *-polynomial in finitely many indicated generators is independent of `Γ`, including the full graph. The generated unital C*-algebras in the corresponding Calkin quotients are canonically isometrically *-isomorphic and corresponding elements have identical essential spectra. In particular the essential disk in [LOCAL_OPERATOR_ALGEBRA.md](LOCAL_OPERATOR_ALGEBRA.md) persists in this larger algebra. The sequence (n^{it}) is one of the allowed multipliers for each real `t`. The same proof permits bounded sequences uniformly insensitive, at sufficiently large indices, to a small relative change of the index.

This statement is about norms modulo compact operators. A height multiplier supported in a bounded interval can act nontrivially at a specified vertex, so there is no assertion that ordinary norms agree for all the enlarged operators.

## Every component occurs in each fixed residue class at comparable heights

Fix an arithmetic progression `x≡r mod m` and a positive component `Γ`. For every `ε>0` and **every** sufficiently large real `X`, there is `x∈[X,(1+ε)X]` in that progression and component.

Write `m=2^a b`, `b` odd. First choose `x_*` in the progression reaching 1. This follows by applying the ordinary predecessor-block theorem with target 1 and width `m`; the same theorem puts arbitrarily large members of any AP in `Γ` by choosing a ternary unit in it. The theorem is formalized in [BasinBlocks.lean](BasinBlocks.lean). If necessary pad the path from `x_*` through the `1,2` cycle so its arrival time `h` at 1 is at least `a`. Let `p` be the number of odd inputs on that path. Reading its inverse word from a variable endpoint `V` gives the affine start

\[
                 x(V)=x_*+2^h(V-1)/3^p.
\]

For every positive `V≡1 mod K`, with the odd modulus `K=3^p b`, the whole word is legal and `x(V)≡r mod m`. Each odd inverse consumes one factor of three in the congruence to the original word. Every integral odd inverse from a positive endpoint is positive, and the factor `2^h b` in the final difference supplies the full original modulus.

Let `o` be the multiplicative order of 2 modulo `K`, taking `o=1` for `K=1`. Put `P=o log 2`. The ratio `log(4/3)/P` is irrational by unique prime factorization. Thus for any small `η>0` there is a finite `L` for which the phases `s log(4/3) mod P`, `0≤s≤L`, form an `η`-net. Fix a sufficiently large `Y∈Γ` with `Y≡1 mod K3^L`, again using the block theorem. All the positive integers

\[
             Y_s=1+(4/3)^s(Y-1),\qquad 0\le s\le L ,
\]

belong to `Γ` and are 1 modulo `K`. Indeed these are successive applications of the inverse word `y↦(4y−1)/3`, whose odd image reaches `y` in two shortcut steps. The congruence through `3^L` makes every stage integral. For all `j≥0` the numbers `V=2^(oj)Y_s` remain in the component and stay 1 modulo `K`. Therefore their affine starts `x(V)` lie in the required component and progression. Uniformly in `s≤L,j≥0`,

\[
 \log x(V)=\log(2^hY/3^p)+s\log(4/3)+jP+ O_{x_*,h,p}(1/Y).
\]

Choose `η<log(1+ε)/4` and choose the fixed `Y` so large that the error is less than `η`. For every sufficiently large `X`, the finite phases select `s` and the integer padding selects `j≥0` within `η` of the midpoint `log X+log(1+ε)/2`. The result lies in the required multiplicative interval. For fixed modulus and precision the height threshold can be made uniform over residues by taking a maximum over its finitely many classes. This argument only needs qualitative occupancy. PR202 `3b10b24d12d4b349cb20f4cbc83086c8a09f807e` treats stronger quantitative counts of long blocks using additional routing and predecessor-density inputs.

## Norm localization on any functional graph

Give the graph its undirected path metric. For any integer `L≥1` and vertex `x` let

\[
      \eta_x=L^{-1}\sum_{j=0}^{L-1}\delta_{T^j x},\qquad
      \xi_x(z)=\sqrt{\eta_x(z)} .
\]

These are defined even on repeated cycles. The vectors `ξ_x` have Hilbert norm one and support within distance `L` of `x`. At one edge the probability measures differ in `ℓ¹` norm by at most `2/L`, by cancellation of the common window. Hence if `dist(x,y)≤d` then `||ξ_x−ξ_y||₂²≤2d/L`, using the coordinatewise square-root inequality.

For a fixed finite-propagation polynomial `P`, use `d` as its propagation bound and `K` as a uniform upper bound on the row and column absolute sums of its matrix. The graph degree is bounded and the generating weights and multipliers are bounded, so one `K` works on all the spaces in the theorem. Define the diagonal window `M_z f(x)=ξ_x(z)f(x)`. Then `Σ_z||M_z f||²=||f||²`. Weighted Cauchy–Schwarz over each matrix row gives

\[
  \sum_z\|PM_z f-M_z P f\|^2
    \le \sum_x\left(\sum_y|P_{xy}|\right)
       \sum_y |P_{xy}|\,|f(y)|^2\,\|\xi_y-\xi_x\|^2
    \le 2d K^2\|f\|^2/L .
\]

Taking the Hilbert direct-sum norm in `z`, any finite nonzero input therefore has some nonzero `M_z f`, supported in a radius-`L` ball, whose norm ratio is at least `||Pf||/||f||−K sqrt(2d/L)` (or arbitrarily close to this bound). The localized support is a subset of the original support. This direct estimate is why arbitrarily large, complicated supports need no additional global graph-comparison hypothesis.

## Transplanting a localized computation without losing its height labels

For a bounded operator on a countable Hilbert basis, its essential norm is the limit of its operator norms on the orthogonal complements of increasing finite sets exhausting that basis. Multiplication by the deleted finite projection is finite rank. Conversely a compact error restricted to these complements tends to zero in norm. Thus, on the source graph, take a sequence of finite unit inputs supported farther and farther from the finite sets with norm ratios approaching the essential norm. At fixed `L` apply the preceding localization. The resulting supports and their centers escape all finite sets: any fixed finite set has finite radius-`L` neighborhood by bounded degree.

Set `R=L+d`. For a center tending to ordinary height infinity, the rooted radius-`R` graph is eventually acyclic. A ball containing a cycle must lie within radius `R` of a cycle of length at most `2R+1`. Only finitely many such ordinary cycles exist by the affine formula for each bounded-length parity word; their fixed-radius neighborhoods are finite. This also covers the full graph regardless of the number of longer cycles.

All labeled possible paths through `R` steps are compositions of the four rational affine branch maps in [the finite tree proof](LOCAL_OPERATOR_ALGEBRA.md), a **fixed finite list** at this radius. To compare two large centers take one modulus `M=m6^(R+1)`, where `m` is a common period of the finitely many arithmetic multipliers used. Congruent centers have matching integrality, parity, available inverse branches and arithmetic labels on all partial paths. Among this fixed finite list, distinct affine functions can coincide at only finitely many exceptional center heights. Discard all those heights, also including comparisons of one further branch if needed to test an interior edge. The equality pattern and the entire required collar then agree at two sufficiently large centers in the same residue class. Paths that identically retrace remain identical on both lifts. All seen vertex heights tend to infinity with the center since all slopes are positive.

For the source centers `x_i→∞` and any receiving component, select centers `x'_i≡x_i mod M` there with `x'_i/x_i→1`. For each fixed precision, the preceding AP result works above one threshold common to all finitely many classes. Use increasingly fine precision past the corresponding thresholds. For each of the finitely many affine forms `g` involved, `g(x'_i)/g(x_i)→1`, uniformly over the list. Consequently all logarithmic labels in the paired collars differ by `o(1)` by uniform continuity. Transport the coefficient vector exactly between the graph copies. A telescoping expansion in the finitely many factors of each word of `P` bounds the difference between the two output norms by `o(1)` times the input norm: each local diagonal error has norm at most the uniform label error on the collar, and the remaining factors have common bounded norms. The normalized receiving vectors escape finite sets and hence are weakly null because they are supported in fixed-radius balls whose vertex heights tend to infinity.

This bounds the source essential norm by the receiving essential norm plus `K sqrt(2d/L)`. Let `L→∞` and interchange the two spaces. To take the receiving space as the full graph, choose centers in any one of its components. The C*-algebra and essential-spectrum claims now follow as in [the arithmetic operator note](LOCAL_OPERATOR_ALGEBRA.md). The exact kernel at a point of the essential spectrum, including the physical value 1, remains outside this comparison.
