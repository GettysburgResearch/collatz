# A retained divisor detects the exact ratios of successive reset depths

**Status.** Proposed written arithmetic refinement of [the fixed-reset theorem](PERSISTENT_RESET_DIVISOR.md). Its upper bound uses Evertse's theorem on sums at specified places. Uniformity over arbitrarily many unequal pieces uses the earlier fixed-fragment duration estimate from Paper 147. The lower constructions use ordinary integers and complete physical words. No cycle- or escape-exclusion is asserted.

Take \(r\ge1\) complete ascent-and-reset blocks, with shifted boundary values \(Y_j=x_j+1=2^{t_j}w_j\) and
\[
 2^{b_j}x_{j+1}=3^{t_j}w_j-1,\quad
 Y=Y_0,\quad T=\sum_{j<r}t_j,\quad B=\sum_{j<r}b_j,\quad
 g=\gcd(w_0,\ldots,w_r),\quad b_*=\gcd(b_0,\ldots,b_{r-1}).
\]
In particular \(t_r=v_2(x_r+1)\). Let \(\alpha=\log_23\), \(\beta=\alpha-1\).

**Theorem E1.** The persistent odd divisor is exactly
\[
                        g=\gcd(Y,2^{b_*}-1).                      \tag{1}
\]
If \(g>1\), take \(e=\operatorname{ord}_g(2)\). Then \(e\mid b_*\). For \(g=1\) use \(e=1\). For each fixed \(r\) and \(\epsilon>0\) there is a possibly ineffective constant independent of all actual depths and of \(g\) such that
\[
              g^{1+B/e}\,2^{T+t_r}\le C_{r,\epsilon}Y^{1+\epsilon}.    \tag{2}
\]
The weaker choice \(e=b_*\) works without knowing the factorization of \(g\). In that case \(B/e=\sum_j m_j\) for the primitive integer depth ratios \(m_j=b_j/b_*\). Two resets with exact depth ratio \(1:100\) charge 102 powers of the same retained divisor. Merely counting resets would give three powers.

To prove (1), the block identity
\[
    2^{t_j+b_j}Y_{j+1}=3^{t_j}Y_j+2^{t_j}(2^{b_j}-1)
\]
shows that \(g\) divides every \(2^{b_j}-1\), hence their gcd \(2^{b_*}-1\) by the Euclidean algorithm. Conversely any odd divisor of both \(Y\) and \(2^{b_*}-1\) propagates across this same identity since 2 is a unit modulo that divisor. This proves equality, with every prime power included. Multiplicative order gives the assertion about \(e\).

For (2) one may use **any** divisor \(e\mid b_*\) for which \(g\mid2^e-1\). Put \(K=B/e\). In the positive integer sum of Theorem D, replace the coordinate for reset \(j\) by \(b_j/e\) positive coordinates, using
\[
           \frac{2^{b_j}-1}{g}
            =\frac{2^e-1}{g}\sum_{h=0}^{b_j/e-1}2^{he}.
\]
All other factors in each such coordinate are powers of two and three. The unchanged root coordinate is \(3^T w_0/g\), hence odd. This yields \(1+K\) positive integer coordinates, total dyadic valuation \(T+B-t_0+t_r\), and no nonempty vanishing subsum. Their combined product of absolute values at \(\infty,2,3\) is at most
\[
       \frac{w_0}{g}\left(\frac{2^e-1}{g}\right)^K
        <\frac{w_0 2^B}{g^{K+1}}.
\]
For fixed \(K\), Evertse's Theorem 2 with dyadic subset gives (2) by precisely the positive-sum argument in D. The archimedean maximum of the split coordinates is bounded by the original positive sum, which is at most \(Y^{O_r(1)}\). For bounded \(K\) we can therefore use the maximum of finitely many constants. [Evertse (1984), printed p. 228, Theorem 2, (13)–(14)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

Here is the separate large-\(K\) argument that makes the exponent uniform. The source physically executes the shortcut word
\(O^{t_0}E^{b_0}\cdots O^{t_{r-1}}E^{b_{r-1}}O^{t_r}\), of length \(N=T+B+t_r\). It uses at most \(2r+1\) fragments of the fixed single-bit dictionary \(O,E\); their respective affine centers are \(-1,0\) and every entrance is positive. Thus for any fixed \(\delta>0\),
\[
                    N\le(1+\delta)\log_2Y+C_{r,\delta}' .
\]
This is the earlier fixed-fragment duration estimate at its actual entrance. Since \(g<2^e\), \((K+1)\log_2g+T+t_r\le(1+1/K)N\). Choose \(\delta\) small and a fixed cutoff \(K_0(\epsilon)\) large enough that \((1+1/K_0)(1+\delta)\le1+\epsilon\). The duration bound handles every \(K\ge K_0\) with one constant. Evertse at fixed dimension handles the finitely many smaller \(K\). Neither argument uses an estimate with an unbounded and uncontrolled dimension. [Paper 147 v1, Proposition 1, (21) and Appendix A](https://rstation.ai/problems/collatz/papers/147/v1)

In particular if \(g\ge Y^c\) with a fixed \(c>0\) on a sequence with \(Y\to\infty\), (2) forces \(K+1\le(1+o(1))/c\). All possible tuples of *exact* positive integers \((b_j/e)_j\) then lie in a fixed finite set. In particular a sequence with unbounded primitive depth-ratio sum tending to infinity can retain only \(g=Y^{o(1)}\). This latter qualitative fact also follows from \(g<2^{b_*}\) and the elementary fixed-block bound \(B=O_r(\log Y)\).

### The sharp profile with prescribed depth ratios

Fix a primitive positive tuple \((m_0,\ldots,m_{r-1})\), put \(M=\sum m_j\), and restrict to paths with \(b_j=m_j b_*\). Also fix \(\lambda,\kappa>0\), \(0\le\nu<1\) and \(0\le\sigma<\alpha-\beta\nu\). Require that
\[
                 x_r\ge\lambda Y^\sigma,\qquad
                 2^{t_r}\ge\kappa Y^\nu.
\]
**Theorem E2.** Among these ordinary blocks,
\[
 \limsup_{Y\to\infty}\frac{\log g}{\log Y}
  =\min\left\{\frac{1-\nu}{M+1},
           \frac{\alpha-\sigma-\beta\nu}{M+(M+1)\beta}\right\}.       \tag{3}
\]
The same limsup holds on positive odd multiples of three. Taking \(\nu=0,\kappa=1\) removes the terminal-duration constraint. The protected-start exponent at \(\sigma=1,\nu=0\) is \(\beta/[M+(M+1)\beta]\). For example a two-reset ratio \(1:2\) gives about \(0.10955\), whereas two equal depths give about \(0.15579\).

For the upper bound set \(h=\log_2 Y\), \(d=\log_2g\). Applied with \(e=b_*\), (2) gives \((M+1)d+T\le(1-\nu+o(1))h\). The complete block formulas give \(Y_r\le2^rY (3/2)^T2^{-B}\), since each positive multiplicative correction is below two. Since \(B=Mb_*>Md\), the floor gives \(Md\le(1-\sigma)h+\beta T+O_{r,\lambda}(1)\). Eliminate \(T\) and also use \(T\ge0\) to obtain (3). Only the bounded-dimension part of the proof of E1 is needed for this fixed tuple.

For sharpness take odd \(b\to\infty\), \(H=2^b-1\), set \(b_j=m_jb\), and prescribe positive integer initial odd-run lengths \(t_j\) of total \(T\), as well as a terminal odd-run length \(u\ge1\). The complete binary word
\[
           O^{t_0}E^{m_0b}\cdots O^{t_{r-1}}E^{m_{r-1}b}O^u E
\]
fixes one source class modulo \(2^{T+Mb+u+1}\). Its final even input guarantees \(t_r=v_2(Y_r)=u\) exactly. Impose \(Y\equiv0\bmod H\) and \(x_0\equiv0\bmod3\), and choose a representative between the combined modulus and twice that modulus. The moduli are coprime because \(b\) is odd. By (1), \(g=H\) exactly since the tuple of ratios is primitive. For large \(b\), \(\operatorname{ord}_{H}(2)=b\), as every smaller positive power minus one lies strictly between zero and \(H\). The finite positive correction factors in D give, uniformly in these prescribed clocks,
\[
   \log_2Y=T+(M+1)b+u+O(1),\quad
   \log_2x_r=\alpha T+b+u+O_r(1),\quad
   \log_2g=b+o(1).                                                    \tag{4}
\]

For an explicit limit argument, first increase \(\nu,\sigma\) slightly to \(\nu',\sigma'\), keeping \(\nu'<1\) and \(\sigma'<\alpha-\beta\nu'\). Let \(v>0\) denote the right-hand side of (3) at those larger parameters and set \(a=1-\nu'-(M+1)v\ge0\). Take \(T=(a/v)b+O_r(1)\), \(u=(\nu'/v)b+O(1)\), with \(T\ge r\) and \(u\ge1\) integral. The first equation in (4) then has main term \(b/v\). The terminal duration fraction tends to \(\nu'\), and the terminal height exponent tends to \(\alpha a+v+\nu'=1+\beta a-Mv\ge\sigma'\). Thus the two floors hold for all sufficiently large \(b\), including the prescribed multiplicative constants, and the retained fraction tends to \(v\). Decrease the primed parameters to their original values and use continuity. This proves sharpness at the branch boundary too.

**Scope.** The reset counts \(r\) are fixed for the uniform inequality, while the ratios and the underlying divisor can vary without bound. A nonconvergent path need not retain a common divisor at polynomial scale. Neither (2) nor (3) forces that missing event for any positive integer cycle. The [finite controls](check_depth_ratios.py) reconstruct the complete odd itinerary, the terminal valuation, the exact shared divisor and the split-coordinate identity on unequal-depth examples. The Evertse estimate and asymptotic optimization are written proofs.
