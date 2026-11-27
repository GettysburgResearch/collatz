# The closed first-hit real support has zero length

For each positive odd root \(a\), let \(K_a\) be the closure of the real offsets \(R_w\) of its finite ordinary first-hit inverse words, including the empty word. Under the retained joint floor, the ordinary trace floor, the fixed-root inverse-path law and the qualitative counted-synchronization inputs below,
\[
                              |K_a|=0.                                  \tag{1}
\]
The closure includes values of exceptional paths, even paths of zero probability for every natural terminal law. In particular the closed natural terminal support at 1 has zero Lebesgue measure under Leen’s support identification. Weaver’s Paper 175, Theorem 2, gives conditional consequences of positive length for exactly this \(K_a\), and its §12 records the length of the closed natural terminal support at 1 as open. Theorem 3 there provides the null *carrier* used in the argument. The cited passage, synchronization and inverse-density results are written inputs with their respective stated review status. [Weaver, Paper 175, §§1, 6 and 12](https://rstation.ai/problems/collatz/papers/175/v1) · [fixed-root inverse paths and source pins](CANONICAL_INVERSE_PATHS.md)

There is also a component version. If a positive ordinary odd component escapes, the closure of the values of its all-future correction \(F(x)=\prod_{j\ge0}3U^jx/(3U^jx+1)\) has zero length. This compact set carries its common corrected real fibre, which has Hausdorff dimension one. The component version uses the existing grade-flux identities and the bilateral coupling. [Real fibre and front](REAL_FIBRE_AND_FRONT.md)

## A one-sided mass estimate at the true ordinary source

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\). For a ternary unit odd root \(y\), write \(P_{h,y}\) for the inverse chain whose mass on the cylinder of a unit-ended word \(w\), ending at \(u\), is \(A_wh(u)/h(y)\). Here \(A_w=3^{|w|}2^{-\sum e_i}\), \(R_w=\frac13\sum_{i=1}^{|w|} A_{w|i}\), and \(A_w u=y-R_w\). The mark \(R_\infty\) increases from zero along a sampled inverse path. Let \(\mu_y\) be its law. There are absolute \(c,C>0\) such that at all real \(M\ge y\)
\[
              h(y)\,\mu_y([0,C y/M])\ \ge\ c y/M.                      \tag{2}
\]

To prove this use Weaver’s Paper 12, Lemma 13. It supplies a fixed unit cylinder \(\mathcal C\) and constants \(c_0,R_0,B_0>0\). For every sufficiently large \(k\) and each \(r\in\mathcal C\), the sum of \(A_w\) over compatible length-\(k+1\) words with \(\max_i A_{w|i}\le R_0\) and \(R_w\le B_0\) is bounded below by a positive constant. Indeed sum equation (39) over \(|d-2(k+1)|\le2\sqrt{k+1}\). Its right side is bounded below uniformly by the negative-binomial central mass (or Chebyshev since its variance is \(2(k+1)\)). A congruence modulo \(3^{k+1}\) recovers actual integral prefixes, and for the \(r\)'s used here the bounds \(r>B_0\) ensure all are positive. Intermediate states are units because they have an odd predecessor. At the last state, divisibility by three is allowed. Remove that last letter. The sum of multipliers of *all* single-letter extensions, relative to the preceding multiplier, is at most \(\sum_{e\ge1}3\,2^{-e}=3\). The resulting distinct length-\(k\) prefixes end at units, have \(R_{w|k}\le B_0\) and still have a total multiplier bounded below. The all-unit trace floor \(h(u)\ge\alpha_0>0\) and the cylinder law therefore give
\[
           h(r)P_{h,r}(R_k\le B_0)\ge c_1
       \quad(r\in\mathcal C,\ r>B_0 \text{ positive odd}).
\]
The events decrease, so \(h(r)\mu_r([0,B_0])\ge c_1\). This estimate is only needed on the selected cylinder. [Weaver, Paper 12, Lemma 13 and Appendix A](https://rstation.ai/problems/collatz/papers/12/v1)

For arbitrary \(y\le M\), use the bridge in the proof of Weaver’s Theorem 14. It chooses a single exponent \(e\) with
\[
  r=(2^ey-1)/3\in\mathcal C,\qquad c_2M\le r\le C_2M,\qquad r>2B_0 .
\]
Given this first letter, \(R_\infty^y=3\,2^{-e}(1/3+R_\infty^r)\). Its cylinder has canonical weight \(3\,2^{-e}h(r)/h(y)\) and \(3\,2^{-e}=3y/(3r+1)\asymp y/M\). Applying the selected-cylinder estimate proves (2). [Weaver, Paper 12, proof of Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1)

## Singular measure and finite crossings at a fixed root

For each odd \(x\) hitting \(a\), let \(s(x)\) be the product of \(3u/(3u+1)\) over the odd states before its *first* hit, with \(s(a)=1\). If \(x\ne a\), then
\[
 s(Ux)-s(x)=s(x)/(3x),\qquad R_{w(x)}=a(1-s(x)).                       \tag{3}
\]
There are no repeated states before that first hit. The uniform reciprocal bound from orbit-set sparsity gives a fixed positive lower bound for \(s(x)\) on these paths. It is enough below to have a bound depending on the root. If \(3\mid a\), its only first-hit word is empty, so suppose \(3\nmid a\).

Let \(\nu_a\) be the law of \(1-R_\infty^a/a\) under \(P_{h,a}\), including the ordinary repeated-loop words when the root is periodic. This is a singular probability by the fixed-root gap frequencies and mean two, together with Weaver’s Paper 175, Theorem 3. Its singularity alone would allow its closed support to have positive length. The following estimate controls the finite first-hit edges through this *one* probability. [Fixed-root path law](CANONICAL_INVERSE_PATHS.md) · [Weaver, Paper 175, Theorem 3](https://rstation.ai/problems/collatz/papers/175/v1)

For a unit \(y\) on a first-hit path into \(a\), fix the specific inverse prefix from \(a\) ending at \(y\). Its coefficient is \(A=a s(y)/y\). Conditional on this prefix, the mark is exactly \(s(y)(1-R_\infty^y/y)\). Equation (2) gives, for all \(M\ge y\),
\[
 \nu_a([s(y)-C/M,s(y)])
 \ \ge\ \frac{a s(y)h(y)}{y h(a)}\cdot\frac{cy}{M h(y)}
 \ \ge\ \frac{c_a}{M}.                                                 \tag{4}
\]
Every edge source \(x\ne a\) has unit target \(y=Ux\le2x\), even a nonunit leaf. Take \(M=2x\). For each \(\theta\in(s(x),s(Ux)]\), equations (3)–(4) give
\[
        \nu_a([\theta-C'/x,\theta+C'/x])\ge c'_a/x.                     \tag{5}
\]
The symmetric one-dimensional density of the singular finite measure \(\nu_a\) is zero at Lebesgue-almost every \(\theta\). At each such \(\theta\), at most finitely many distinct integers \(x\) can have \(s(x)<\theta\le s(Ux)\), by (5).

Let \(0<\theta<1\) have this finite-crossing property. A vertex with \(s(z)<\theta\) reaches \(s(a)=1\) through a strictly increasing finite path. It passes through one of the finitely many crossing sources, with \(s(z)\le s(x)<\theta\). The maximum of the finitely many lower ends is strictly below \(\theta\). If the crossing family is empty there are no values below \(\theta\). In both cases a left neighborhood of \(\theta\) contains no values \(s(z)\). A positive-measure closure of these values would have a Lebesgue density point with the finite-crossing property; its left neighborhood then gives a contradiction. By the affine identity in (3) this proves (1). At root 1, the positive uniform reciprocal bound keeps all first-hit correction factors in a compact subinterval of \((0,1]\). Thus the logarithmic terminal coordinate and its translations and reductions modulo the specified period preserve length zero. Leen’s identification of the minimum-one support gives the asserted closed-support conclusion. [Weaver, Paper 175, §6](https://rstation.ai/problems/collatz/papers/175/v1)

## A single null closed set for an escaping component

Use the bilateral law of \((Z_v)_{v\in\mathbb Z}\) on an escaping component with grade \(g(y)\), flux \(M_y=h(y)F(y)/y\) and grade total \(H>0\). Let \(\nu=\mathcal L(J)\) be its singular corrected mark law. At grade \(g(y)\) the event \(Z_{g(y)}=y\) has probability \(M_y/H\). On that event the mark has law \(F(y)(1-R_\infty^y/y)\), giving
\[
 \nu([F(y)-C/M,F(y)])\ \ge\ \frac{c F(y)}{HM}
       \qquad (y\text{ a unit of the component},\ M\ge y).             \tag{6}
\]
This only conditions on one grade and one actual vertex at a time. Uniform reciprocal packing bounds \(F\) away from zero on the component. The edge rule (3) holds everywhere with \(s=F\), also at nonunit leaves. Its deterministic future has \(F(U^n x)\to1\), since its strictly positive product tails tend to one. Thus each path starting below any \(\theta<1\) crosses that phase after finitely many steps. Taking \(M=2x\) at the unit target and repeating (5) and the finite-crossing argument gives
\[
               \bigl|\overline{\{F(x):x\text{ in the component}\}}\bigr|=0.
\]
Every bilateral sample has \(F(Z_{-n})\to J\), so this compact set carries \(\nu\). Its Hausdorff dimension is one by the previously obtained full dimension of \(\nu\). A positive-density basin can itself have zero-length closed correction support, as root 1 illustrates. A proof of no positive escape would need an additional incompatibility from the escaping component or the original ordinary trace. [Bilateral coupling and full real dimension](REAL_FIBRE_AND_FRONT.md)
