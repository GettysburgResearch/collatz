# The sharp retained odd divisor across one ordinary Collatz reset

**Status.** Proposed theorem for positive ordinary integers. The upper bound uses Schlickewei's two-dimensional Subspace Theorem. Its asymptotic threshold is ineffective. The lower examples are unconditional ordinary multiples of three with a physically exact first block. Their subsequent fates do not enter the construction.

Let \(x\) be any positive odd integer. Write \(Y=x+1=2^t w\) with \(w\) odd and \(t\ge1\). Follow its \(t-1\) exponent-one Syracuse steps and the next true reset to \(z\). Equivalently,
\[
 b=v_2(3^t w-1)\ge1,\qquad 2^b z=3^t w-1.
\]
The actual division exponent at the last odd input is \(b+1\). The odd common divisor of the two shifted endpoints is
\[
 g=\gcd(w,z+1)=\gcd(w,2^b-1).
\]
Put \(\alpha=\log_2 3\), \(\beta=\alpha-1\).

**Theorem C.** For every \(\epsilon>0\) there is a constant \(C_\epsilon\) such that every complete block satisfies
\[
                         g^2\le C_\epsilon wY^\epsilon.                 \tag{1}
\]
Fix \(\lambda>0\) and \(0\le\sigma<\alpha\). Among blocks with \(z\ge\lambda Y^\sigma\), the sharp exponent is
\[
 \limsup_{Y\to\infty}\frac{\log g}{\log Y}
 = \min\left(\frac12,\frac{\alpha-\sigma}{2\alpha-1}\right).           \tag{2}
\]
Restricting the inputs throughout the limsup to positive odd multiples of three gives the same answer. In particular when the first reset stays above a fixed positive fraction of the initial scale the maximal exponent is
\[
                  \frac{\log_2(3/2)}{1+2\log_2(3/2)}
                    =0.2695772896908149\ldots.
\]
Thus for any \(\epsilon>0\), a larger common divisor than \(Y^{0.2695772896908149\ldots+\epsilon}\) forces a genuine first-block descent below \(\lambda Y\) at all sufficiently large sources. The constant term in the exponent denotes the exact displayed logarithmic ratio.

## Square-root bound in the odd part of the source

Set \(u=w/g\), \(v=(2^b-1)/g\). Both are odd, positive and coprime. With \(X=3^t u\), \(V=v\), the exact block equation gives
\[
                    2^b\mid X+V.
\]
Indeed \(g(X+V)=3^t w+2^b-1=2^b(z+1)\), and \(g\) is odd.

Apply the rational two-dimensional Subspace Theorem at the three places \(\infty,2,3\). Use the coordinate forms \((X,V)\) at infinity and three and the forms \((X+V,V)\) at two. Each pair is linearly independent. The product of the six absolute values at the actual vector satisfies
\[
      \Phi\le (3^t uv)\,2^{-b}\,3^{-t}
           =\frac{uv}{2^b}
           =\frac{w(2^b-1)}{2^bg^2}<\frac{w}{g^2}.                    \tag{3}
\]
The coordinates may have a common factor even though \(u,v\) are coprime. Their gcd \(d=\gcd(3^t u,v)\) is a power of three, and \(\prod_{p=\infty,2,3}|d|_p=1\). Dividing both coordinates by \(d\) leaves \(\Phi\) unchanged. Let \(H=\max(X/d,V/d)\), the height of this primitive positive vector. Then \(H\le3^t w\le Y^\alpha\), since \(2^b\le3^t w-1\).

For every fixed \(\delta>0\), a block with \(g^2\ge w H^\delta\) satisfies \(\Phi<H^{-\delta}\). Schlickewei's theorem places every resulting primitive vector on finitely many proper rational lines. A line contains at most a single positive projective slope \(r=X/V\). Each such slope allows only finitely many complete ordinary blocks, by the physical identity
\[
          r=\frac{3^t w}{2^b-1}
           =z+\frac{z+1}{2^b-1}.
\]
There are finitely many positive integers \(z<r\). For each, \(2^b-1=(z+1)/(r-z)\) determines \(b\), and the positive integer \(2^b z+1\) has finitely many factorizations \(3^t w\). Taking \(\delta=\epsilon/\alpha\) and absorbing the finitely many exceptional blocks gives (1), even when \(z\) is small. The argument supplies no effective list of these exceptional lines. [Schlickewei, original 1977 theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Evertse, primitive-vector formulation, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

## Upper bound for the protected output

The exact inequalities
\[
            g<2^b,\qquad gz<3^t w = Y(2^t)^\beta
\]
give, if \(z\ge\lambda Y^\sigma\),
\[
    \log g\le (1-\sigma)\log Y+\beta t\log2+O_\lambda(1).
\]
On the other hand (1) implies
\[
           2\log g+t\log2\le (1+o(1))\log Y
\]
uniformly over all complete blocks as \(Y\to\infty\). This already gives the first ceiling in (2). Substitute the second display in the first to get
\[
       (1+2\beta)\log g\le(\alpha-\sigma+o(1))\log Y.
\]
This proves the other ceiling with no rank or prime-height limit anywhere.

## Matching actual integer triples

Let \(b\) tend to infinity through odd integers. For a positive integer \(t\) to be chosen, put \(G=2^b-1\). Choose \(u\in[2^b,7\cdot2^b)\) from the single class modulo \(3\cdot2^{b+1}\) determined by
\[
    3^t G u\equiv 1+2^b\pmod{2^{b+1}},\qquad
    2^t G u\equiv1\pmod3 .
\]
The first coefficient is odd. In the second congruence \(G\equiv1\pmod3\) since \(b\) is odd. The Chinese remainder theorem gives existence in the stated half-open interval. These conditions make \(u\) odd, \(x=2^tG u-1\) a positive odd multiple of three, and the first reset parameter exactly \(b\). Moreover \(w=G u\) and \(g=G\) exactly. Uniformly in \(t\ge1\), with base-two logarithms,
\[
   \log_2 Y=t+2b+O(1),\qquad
   \log_2 z=\alpha t+b+O(1),\qquad
   \log_2 g=b+o(1).                                                 \tag{4}
\]
When \(0\le\sigma<1/2\), take \(t=1\). Then \(z/Y^\sigma\to\infty\), while \(\log g/\log Y\to1/2\). For \(1/2\le\sigma<\alpha\), take
\[
 t=\left\lceil\frac{2\sigma-1}{\alpha-\sigma}\,b\right\rceil+K
\]
with a fixed sufficiently large positive \(K\). By (4), \(\log_2 z-\sigma\log_2Y\) is bounded below by \((\alpha-\sigma)K-O_\sigma(1)\), and \(K\) can ensure \(z\ge\lambda Y^\sigma\) for every sufficiently large \(b\). Dividing the last line of (4) by the first gives \((\alpha-\sigma)/(2\alpha-1)\). At \(\sigma=1,\lambda=1\), the entire observed odd and shortcut first block stays at or above its initial source. The noninitial odd inputs of the ascent strictly increase and the final halving run stays above its odd landing.

## Relation to the minimum problem and the coarse duration profile

For the upper leg \(x=3s\) of an actual least disagreement, the first landing \(z\) must exceed \(s\), since all positive starts through \(s\) are good. Thus the numerical exponent \(0.269577\ldots\) applies to its possible inherited odd content, with \(\lambda=1/3\) for the shifted source (integer \(z>s\) gives \(z\ge(3s+1)/3\)). The examples show sharpness among ordinary first-block survivors at precisely this kind of numerical floor. They do not establish a least disagreement or prescribe the ultimate fate of those triples. Ordinary integrality forbids the oversized-gcd region; the remaining region contains many actual integer first blocks.

Paper 147 already describes the simplex of normalized durations for each fixed list of shortcut templates, in particular a run of odd steps followed by a run of halvings. The complete-block identity and the coarse duration profile are prior material. Here the extra coordinate is the gcd of the odd parts of the two shifted ordinary endpoints, with its uniform square-root bound and its matching sharp profile under a lower bound on the landing. The analytic step uses only the three fixed places \(\infty,2,3\) and permits every prime in the gcd to vary. The accompanying Lean module checks the elementary finite bounds in the companion note. The Subspace Theorem, its physical exceptional-line analysis and the matching asymptotic construction are written proofs. [Paper 147, Proposition 1 and Theorem 3](https://rstation.ai/problems/collatz/papers/147) · [Relative endpoint and elementary divisor bounds](RELATIVE_RESET_RIGIDITY.md)
