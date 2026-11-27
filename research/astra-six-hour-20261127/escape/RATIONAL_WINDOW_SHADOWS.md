# Ternary rational obstructions in positive translated intervals

Negative integer shadows give wholly positive translated intervals with many misses of the threshold \(Fx/N\) up to a finite deadline \(H\). The usual construction translates by \(2^H\). A rational shadow with denominator a power of three reduces the required height, because its actual negative trajectory becomes integral after the prescribed number of odd departures. This gives obstructions at polynomial translates arbitrarily close in exponent to one. At the exact centers of an escaping component's synchronized packets a separate arithmetic argument gives arbitrarily long runs that avoid these rational obstructions.

## A finite-deadline obstruction at smaller translates

Use the shortcut map \(T\), the odd map \(U\), and \(D=\log(4/3)\), with natural logarithms. Fix \(p>1\) and
\[
          p < h\log2 < p+\frac{\log3}{D}.                              \tag{1}
\]
Let \(N\to\infty\), \(1\le F=N^{o(1)}\), and take any integer deadlines \(H=(h+o(1))\log N\). There are intervals of \(N\) consecutive positive integers with initial point \(X\asymp N^p\) on which at least \((1-o(1))N/F\) starts satisfy
\[
               T^t(x)\ge Fx/N\qquad(0\le t\le H).                     \tag{2}
\]
The same holds through the corresponding ordinary step at each source. In particular for every \(1<p<2\log2/D\), the interval can be chosen with the typical endpoint clock \(H=(2/D)\log N+o(\log N)\). When \(1<p\le 2.410\), the construction already lies in the polynomial translation range suggested by the positive escaping-ray packets. It concerns any specified finite horizon in (1). [Weaver, translated intervals and the negative-integer construction, §§2–4, 6](https://rstation.ai/problems/collatz/papers/191)

Here is the finite-source input from that paper's proof. For every fixed \(0<\theta<1\), in **any** interval of \(L\) consecutive positive integers, all but \(o(L)\) starts satisfy
\[
    \max_{0\le t\le (2\theta/D)\log L}|b_t-t/2|
                     =O_\theta(\sqrt{\log L\log\log L}),               \tag{3}
\]
where \(b_t\) counts odd departures before shortcut time \(t\). To extract (3), take the record cutoff parameter \(B=K\log_2\log_2 L\) with a sufficiently large fixed \(K\). Equation (7) bounds the rejected starts by \(o(L)\). The prefix-count estimate immediately after (7) holds at all steps up to the stopping entrance \(v\). At this entrance, \(B/2<U_v\le B\) and
\[
 U_v=\log_2 L-\frac{D}{2\log2}v+(\log_2 3)(b_v-v/2).
\]
It follows that \(v=(2/D)\log L+O(\sqrt{\log L\log\log L})\), as needed. This uses the actual source's prefix estimates and the uniformity in translation.

Choose the integer
\[
 r=\left\lfloor\frac{H\log2-p\log N}{\log3}\right\rfloor,
 \qquad Z=\frac{2^H}{3^r}.
\]
Then \(N^p\le Z<3N^p\) and \(r/\log N\to(h\log2-p)/\log3\in(0,1/D)\). Put \(L=\lfloor N/F\rfloor\), choose the full interval \([\lfloor Z\rfloor-N+1,\lfloor Z\rfloor]\), and apply (3) in its last \(L\) positions. Those positions satisfy \(0<Z-x\le L\le N/F\), since \(r\ge1\) for large \(N\) makes \(Z\) nonintegral. Write \(v_x=Z-x\). For the retained starts the time \(t_r\) of the \(r\)-th completed odd departure satisfies
\[
        t_r=2r+O(\sqrt{\log N\log\log N})<H .
\]
Indeed choose \(\theta\) strictly between \(D\lim r/\log L\) and one. The bound (3) reaches that departure. The inequality \(2\lim r/\log N<h\) follows from (1) and \(p>1\): its equivalent form \(hD<2p\) holds already at the upper endpoint of (1).

Write the real affine word through time \(t\) as \(T^t(x)=a_t(x+G_t)\), with \(a_t=3^{b_t}2^{-t}\) and \(G_t\ge0\). Through \(t_r\), (3) implies
\[
 \max_{t\le t_r}a_t^{-1}\le \exp(Dr+O(\sqrt{\log N\log\log N})).
\]
Each addition to the real intercept contributes at most \(1/(2a_{j+1})\) to \(G_t\). Consequently both \(\max a_t^{-1}\) and \(\max G_t\) through \(t_r\) are at most \(L^{1-\eta}\) for some fixed \(\eta>0\) and all sufficiently large \(N\). Exclude also the \(O(L^{1-\eta/2}+1)=o(L)\) starts with \(v_x\le L^{1-\eta/2}\).

Extend the shortcut parity rule to rationals of odd reduced denominator using their two-adic parity. The rational \(x'=x-Z=-v_x\) shares the first \(H\) shortcut parities with \(x\) since \(v_2(Z)=H\). For \(t\le t_r\),
\[
              T^t(x')=a_t(-v_x+G_t)\le-1
\]
by the two preceding bounds. At \(t_r\), subtraction of the common affine histories gives
\[
             T^{t_r}(x)-T^{t_r}(x')=a_{t_r}Z=2^{H-t_r}.
\]
The negative state is therefore an integer. Every later state of that integer is at most \(-1\). It follows throughout \(t\le H\) that \(a_tv_x\ge1+a_tG_t\ge1\), proving (2). Before every actual odd shortcut step the extra ordinary intermediate value exceeds its positive departing state. Taking \(h=2/D\) in (1) uses \(2\log2/D=1+\log3/D\). For deadlines below \(p\log_2 N\), the earlier negative integer shift \(2^m\) with \(m\ge H\) can already give polynomial height \(N^p\).

## A fixed positive ray avoids these shifts for long blocks

Let \(a_k=U^k(a)\) be an actual escaping positive odd trajectory. At the central inverse clock its packet endpoint and width scale are
\[
             X_k=(4/3)^k a_k,\qquad N_k=(4/3)^k .
\]
For \(H=2k\) the distance from \(X_k\) to a rational shadow shift is exactly
\[
  |X_k-m2^{2k}/3^r|=N_k|a_k-m3^{k-r}|.                                 \tag{4}
\]
Here any integer \(m\) may be used in this arithmetic identity. For every fixed \(B<\infty\), \(\delta>0\), and positive integer \(J\), there are arbitrarily late intervals of \(J\) consecutive odd times \(k\) on which
\[
     \min_{m\in\mathbb Z}|a_k-m3^{\lfloor\delta k\rfloor}|>B.           \tag{5}
\]
In particular all these packet endpoints have distance greater than \(BN_k\) from *every* shift in (4) with \(0\le r\le(1-\delta)k\). The actual selected sources lie within \(O(N_k)\) of the endpoint, as in [the equal-clock construction](GRADED_CORRECTION_SETS.md). This excludes the exhibited family at those packet locations. A converse classifying all delayed positive intervals has not been established.

We give the Diophantine input explicitly. For fixed rational coefficients \(u_1,\ldots,u_s\), a fixed \(K\), and \(0\le m_i\le Kn\), every nonzero
\[
              A=\sum_i u_i2^{m_i}\qquad\hbox{satisfies}\qquad
              v_3(A)=o(n)                                                \tag{6}
\]
uniformly in the exponents, in the upper-bound sense. This is a direct fixed-dimensional consequence of the \(p\)-adic Subspace Theorem. Remove zero coefficients and factor out the smallest power of two, which preserves the valuation. The resulting integral vector of powers of two is primitive, of maximum norm \(H_0\le 2^{Kn}\). At \(\infty,2\) take the coordinate forms. At 3 replace the first coordinate form by \(\sum_i u_iX_i\), keeping all the others. The forms are independent at each place, and their unnormalized product over all places is \(|A|_3\). If \(v_3(A)\ge\epsilon n\), this product is at most \(H_0^{-c}\) for a fixed \(c>0\). The Subspace Theorem therefore puts the primitive vectors of unbounded height in finitely many proper rational subspaces. The bounded-height ones have only finitely many possible valuations for nonzero values. On each subspace solve one fixed linear relation for a coordinate and substitute into the form. The remaining coordinates are still powers of two. If the resulting form vanishes identically the original sum is zero; otherwise the number of coordinates decreases. Induction excludes the proposed sequence, since a single nonzero term has a fixed valuation. This also treats cancellation of proper subsums. [Schlickewei's real and \(p\)-adic linear-forms theorem](https://gdz.sub.uni-goettingen.de/download/pdf/PPN365956996_0018/PPN365956996_0018.pdf) · [Statement for primitive integer vectors, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

Suppose the times failing (5) have eventually bounded gaps. At each such time choose \(|c_i|\le B\) with \(a_i\equiv c_i\pmod{3^{\lfloor\delta i\rfloor}}\). For successive chosen times \(i<j\) with \(d=j-i\) bounded, let \(S_l\) be the total actual exponents in the first \(l\) edges after \(i\). Then
\[
    2^{S_d} a_j=3^d a_i+\sum_{l=0}^{d-1}3^{d-1-l}2^{S_l}.
\]
The expression
\[
   2^{S_d}c_j-3^d c_i-\sum_{l=0}^{d-1}3^{d-1-l}2^{S_l}                 \tag{7}
\]
is divisible by \(3^{\lfloor\delta i\rfloor}\). Its coefficient tuple ranges through a finite set. Its exponents are \(O_a(i)\): for instance, each of the bounded number of valuations is at most \(\log_2(3a_{i+l}+1)\), and \(a_t+1\le(3/2)^t(a+1)\). By (6), (7) vanishes exactly for all sufficiently late successive chosen pairs. The exact equalities give
\[
       2^{S_d}(a_j-c_j)=3^d(a_i-c_i).
\]
Telescope from one sufficiently late chosen \(i\). Unbounded powers of two divide the fixed nonzero integer \(a_i-c_i\); it is nonzero since \(a_i\to\infty\). This contradiction proves (5). The observation concerns ordinary values along one trajectory and requires neither a density for its ternary residues nor independence of its division exponents.
