# Joint high-value law of the original density and the maximum legal gain

Use full ternary Haar probability \(m\), the fair Syracuse density \(\rho\), the largest legal gain \(G\), and the tilted stationary ternary probability \(\sigma\) with gap weights \(p_e=3/4^e\). The two scalar exact tails have respective positive constants \(\kappa\) and \(\kappa_G\). In particular the density itself, with its ternary location retained, satisfies
\[
                 t^2 1_{\{\rho>t\}}dm\Rightarrow\kappa\sigma.            \tag{1}
\]
On every cylinder \(y+3^r\mathbb Z_3\), the conditional tail coefficient is exactly \(\kappa 3^r\sigma(y+3^r\mathbb Z_3)\). The scalar density tail is Weaver's result. [Weaver 146, §8](https://rstation.ai/problems/collatz/papers/146/v1) · [The scalar and angular maximum-gain result with its sources](../phase9/MAXIMUM_GAIN_ANGULAR_TAIL.md)

More generally take \(a,b\ge0\) and \(Y=\max(a\rho,bG)\). There is a constant \(K(a,b)\) such that
\[
           t^2 1_{\{Y>t\}}dm\Rightarrow K(a,b)\sigma .
\]
It is positive away from \((0,0)\), is homogeneous of degree two, and is given by an integrable signed formula below. Consequently \((\rho,G)\) is jointly regularly varying with index two, its blowup on \([0,\infty)^2\setminus\{0\}\) retaining the limiting ternary location independently with law \(\sigma\). No claim of independence between the two real coordinates is made.

Put \(F_e(x)=(3x+1)/2^e\), \(a_e=3/2^e\), and \(v_e=a_e1_{F_e\mathbb Z_3}Y\circ F_e^{-1}\). Let \(V=\max_e v_e\), with zero on a nonunit. Almost everywhere,
\[
                    V\le Y\le\max\{b,\sum_e v_e\}.
\]
Indeed the density is the sum of its branch densities, and the gain is the maximum of one and its branch gains. The earlier comparison \(G\le C(1+\rho)\) and Weaver's integrability of distinct branch products imply
\[
                     \int\sum_{e\ne f}v_ev_f\,dm<\infty.
\]
For each point integrate the signed difference of the indicator of \(Y>t\) and the sum of the indicators of \(v_e>t\), against \(t\,dt\). Its absolute integral before averaging is bounded by half \(Y^2-V^2+\sum_e v_e^2-V^2\). The first difference is at most \(b^2+(\sum_e v_e)^2-V^2\); the sum of squares of the nonmaximal entries is at most the sum of their products with a maximal entry. The preceding integrability gives the signed renewal forcing required by the same two-sided key renewal argument as for \(G\). The weak square-tail bound follows from the two scalar upper bounds. Thus for \(\mu=\log 3-(4/3)\log2\),
\[
     \lim_{t\to\infty}t^2 m(Y>t)=K(a,b)
       ={1\over 2\mu}\int\big[Y^2-\sum_e v_e^2\big]dm .
\]
The bracket is a single integrable signed function. Positivity follows from either nonzero scalar term.

The rescaled intersections of two branch exceedances have total mass \(o(1)\), by dominated convergence on the distinct branch products. The sum of the rescaled one-branch masses tends to \(K(a,b)\): the branch Jacobian is \(1/3\), the rescaled weights are \(p_e\), and the scalar tail is bounded with a limit. Their union is contained in the \(Y\) exceedance, whose rescaled mass has the same limit. Therefore the difference of the rescaled location measures from their single-branch recursion tends to zero in total variation. Iteration to any fixed ternary precision identifies their weak limit with \(K(a,b)\sigma\), as in the maximum-gain proof. Choosing \((a,b)=(1,0)\) gives (1).

For the bivariate assertion the rescaled laws are locally bounded on sets a positive distance from the origin by the scalar weak-tail bounds. The probability of escaping to either coordinate greater than \(R\) is \(O(R^{-2})\) after rescaling. In the two extreme single-coordinate cases the limiting tails are continuous, so every positive-coordinate vertical or horizontal level line has zero mass for each subsequential limit. For positive cutoffs \(u,v\), use inclusion–exclusion on the union \(\{\rho>ut\}\cup\{G>vt\}\), tested on any fixed ternary cylinder. The joint upper-rectangle limit is
\[
     [\kappa/u^2+\kappa_G/v^2-K(1/u,1/v)]\,\sigma(\text{cylinder}).
\]
These rectangles and the two marginal tails determine each subsequential vague limit, including mass on the axes by monotone exhaustion. Hence the full limit exists and factors into a bivariate index-two tail measure and the ternary probability \(\sigma\).
