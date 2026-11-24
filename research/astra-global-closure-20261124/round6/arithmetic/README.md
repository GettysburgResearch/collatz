# Complete denominators along one fixed ordinary orbit

**PROPOSED written theorem.** Fix an ordinary positive integer \(n\) whose shortcut Collatz orbit is injective. At clock \(L\), repeat its first \(L\) physical bits to close a rational physical cycle and a rational companion cycle. Write \(G_L,G_L^*\) for the two **entire factors cancelled** in reducing their respective numerical fixed points. For each \(\epsilon>0\), put
\[
 K_\epsilon=\left\lceil(\log(16)/\epsilon)^2\right\rceil .
\]
For every fixed window length \(H\ge1\), all sufficiently late intervals \([L,L+H)\) contain at most \(2K_\epsilon\) indices \(j\) with
\[
                  \max(\log G_j,\log G_j^*)\ge\epsilon j.             \tag{1}
\]
Each coordinate separately has bound \(K_\epsilon\). The starting threshold can depend on \(H,\epsilon,n\) and is ineffective. In particular both full denominators attain their raw logarithmic exponents in upper Banach density on this **same** orbit. This means that for every fixed tolerance the exceptional set has upper Banach density zero. No averaging over starting points or parity words occurs.

Every sufficiently late prefix of an escape also has physical reduced denominator \(\gg_n 2^L\), including the individual exceptional clocks in (1). For **every** positive ordinary \(n\), fixing \(0<\epsilon<\log2\), the clocks in (1) have positive upper Banach density if and only if \(n\) itself is periodic. In that case the bad clocks eventually coincide with the multiples of its least period. A transient input to a cycle has uniformly bounded cancellation in both rows. The [all-input corollary and consequences for the genuine scalar](COMPANION.md) include the proofs, an exact dyadic agreement formula, a pointwise almost-unit theorem, and the remaining cycle obstruction.

## 1. Two rational points at the physical clock

Write \(x_0=n,\ x_{i+1}=T(x_i)\), where \(T(x)=x/2\) on evens and \(T(x)=(3x+1)/2\) on odds. Put \(e_i=x_i\bmod2,\ p_i=\sum_{j<i}e_j\). Define the two rows at \(L\ge1\) by

| Quantity | Physical | Companion |
|---|---|---|
| Clock numerator \(a_L\) | \(2^L\) | \(2^{L+p_L}\) |
| Clock denominator \(b_L\) | \(3^{p_L}\) | \(3^L\) |
| Starting trial \(s\) | \(n\) | \(0\) |
| Carry \(c_L\) | \(\sum_{i<L}e_i2^i3^{p_L-p_{i+1}}\) | \(\sum_{i<L}e_i2^{i+p_i}3^{L-1-i}\) |
| Endpoint \(y_L=(b_Ls+c_L)/a_L\) | \(x_L\) | \(W_L=c_L/2^{L+p_L}\) |

For either row let \(u_L=a_L/b_L\), \(D_L=a_L-b_L\), \(G_L=\gcd(|D_L|,c_L)\), and \(d_L=|D_L|/G_L\), using stars for the companion when the rows appear together. The signs of \(D_L\) are unrestricted. Both rows have literal rational closed phases. Indeed the affine block fixed point is \(c_L/D_L\), with that reduced denominator. Rotation gives the next rational phase since the affine branch slopes are nonzero. The physical branches preserve the indicated parities, because all phases are dyadically integral and the alternative parity would give a nonintegral successor. In the companion row the branches are \(w\mapsto 3w/2,\ (3w+1)/4\). Dyadic integrality requires respectively \(w\equiv0\bmod2,\ w\equiv1\bmod4\). The other residue \(3\bmod4\) has no legal branch. Thus the prescribed bits occur at the closed phases. The trial \(W_L\) computed from zero is a different rational from the closed phase. [Halbeisen–Hungerbühler, §2, Lemmas 1–2](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf) · [PR193, full companion divisor and finite phase conditions, frozen head](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/arithmetic/README.md)

Let \(S=\{\infty,2,3\}\). Both \(u_L,u_L^{-1},y_L\) lie in \(\mathbb Z[1/6]\). At all sufficiently large clocks \(p_L>0\), so \(|D_L|\) is coprime to six in both rows. Congruences modulo its divisors can be taken in \(\mathbb Z[1/6]\). Every complete cancelled factor in either row is characterized by
\[
 g\mid G_L\quad\Longleftrightarrow\quad
           u_L\equiv1,\quad y_L\equiv s\pmod g
 \qquad(\gcd(g,6)=1).                                            \tag{2}
\]
Indeed \(a_Ly_L=b_L s+c_L\) and both clocks are units modulo \(g\). In particular \(G_L=\gcd(|2^L-3^{p_L}|,x_L-n)\) in the physical row.

The reviewed orbitwise reciprocal estimate gives \(\sum_{i:e_i=1}1/x_i<\infty\). Thus
\[
         (2^L/3^{p_L})x_L=n\prod_{i<L,\ e_i=1}(1+1/(3x_i))
              \longrightarrow H_n\in(0,\infty).
\]
Since distinct positive integers escape every finite set, \(x_L\to\infty\). Hence \(2^L/3^{p_L}\to0\) in the reals, and the physical raw divisor is asymptotic in magnitude to \(3^{p_L}\). At all large clocks its cancellation divides the nonzero integer \(x_L-n\). In fact
\[
     \liminf_{L\to\infty}\frac{d_L}{2^L}\ \ge\
     \lim_{L\to\infty}\frac{3^{p_L}-2^L}{2^L(x_L-n)}
     = H_n^{-1}.                                                   \tag{3}
\]
Also \(p_L/L>\log_3 2>3/5\) eventually. Since \(2^8>3^5\), \(u_L^*=2^{L+p_L}/3^L\) grows exponentially and \(D_L^*\sim 2^{L+p_L}\). [Reviewed fixed ordinary orbit estimate](../../../integrated/orbitwise-boundaries/README.md) · [PR195, pinned two-place product and separated-visit source](https://github.com/GettysburgResearch/collatz/blob/1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97/research/astra-global-closure-20261124/closing/adelic/README.md)

## 2. Avoidance of every fixed curve in both rows

We show that each nonzero polynomial in \(\mathbb Q[U,Y]\) vanishes only finitely often on either sequence \((u_L,y_L)\) of this fixed escape. The argument for the companion uses the true scalar
\[
 \mathcal D(n)=\sum_{i\ge0} e_i\,2^{i+p_i}/3^i\in\mathbb Z_2 .
\]
The PR182 written theorem proves that a rational value at a positive ordinary source forces eventual periodicity of its physical orbit. Briefly, a rational companion evolves on a bounded-denominator grid under the two companion branches. The signed trial \(-\mathcal D(x_i)/3\) is eventually positive on an escape using the growing weights \(u_i^*\). Its phases are distinct because equal phases determine all later physical parities and hence the same ordinary source. Both the ordinary and companion states then tend to positive infinity in the reals. The product \(x_i^2(-\mathcal D(x_i)/3)^3\) contracts by a fixed factor below one on both branches once \(x_i\ge20\) and \(-\mathcal D(x_i)/3\ge64\), a contradiction. We use the resulting irrationality only under our fixed escape hypothesis. [PR182, rationality theorem and branch constants, frozen head](https://github.com/GettysburgResearch/collatz/blob/234fd2ece3a17c8950dce452291198705b4e6e60/research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md)

Suppose infinitely many distinct points of one row lie on a fixed curve. Take the Zariski closure of those rational points in \(\mathbb G_m\times\mathbb A^1\) and retain a geometrically irreducible curve containing infinitely many. Such a component is defined over \(\mathbb Q\), since distinct Galois conjugates intersect only finitely and every point under consideration is rational. Isolated points and singular points form a finite discarded set. The first coordinate \(U\) on the component is nonconstant since \(v_2(u_L)\to+\infty\). Lift its rational nonsingular points to the normalization. These points are \(S'\)-integral on the normalized affine curve for a single finite enlargement \(S'\) of \(S\). Indeed its coordinate ring is finite over the original affine coordinate ring generated by \(U,U^{-1},Y\). Choose finitely many integral generators, clear the finitely many rational coefficient denominators in their monic equations by enlarging \(S\), and evaluate. Their rational values are integral over the integrally closed ring of \(S'\)-integers.

By the \(S'\)-integral form of Siegel's theorem, the smooth projective completion has genus zero and at most two geometric points removed. Both zeros and poles of \(U\) are removed since \(U,U^{-1}\) are regular on the affine curve. A nonconstant function has at least one of each, so there are exactly two punctures. Its unique zero and unique pole are individually rational since each is Galois stable. A genus-zero curve with a rational point is \(\mathbb P^1_{\mathbb Q}\). Take a rational parameter \(t\) vanishing at the first puncture with a simple pole at the second. The divisor of \(U\) now gives \(U=c t^r\) with \(c\in\mathbb Q^\times,r\ge1\), and \(Y\in\mathbb Q[t,t^{-1}]\), by regularity away from these two points. This is an expression on the normalized curve itself, so all the retained rational points give rational values of \(t\). No roots of arbitrary rational numbers are adjoined. [Corvaja–Zannier, *A subspace theorem approach to integral points on curves*, §1, pp. 268–269, Theorem 1 and the stated \(S\)-integral extension](https://www.numdam.org/item/10.1016/S1631-073X%2802%2902240-9.pdf) · [Their Annals paper, p. 705 and §0](https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p09.pdf)

In the physical row \(v_2(t)\to+\infty\) and \(v_3(t)\to-\infty\), since \(v_2(U)=L\), \(v_3(U)=-p_L\). A negative lowest exponent of \(Y\) forces \(v_2(Y)\to-\infty\), since it uniquely minimizes the valuation for sufficiently large \(v_2(t)\). A positive highest exponent similarly forces \(v_3(Y)\to-\infty\). Integrality of \(x_L\) at two and three rules out both cases. The remaining constant \(Y\) is impossible since \(x_L\to\infty\). This also handles horizontal components.

In the companion row \(v_2(t)\to+\infty\) since \(v_2(U)=L+p_L\), whereas
\[
          u_L^* W_L={1\over3}\sum_{i<L} e_i2^{i+p_i}/3^i
              \longrightarrow \mathcal D(n)/3
                      \qquad\text{in }\mathbb Q_2.                \tag{4}
\]
The Laurent polynomial \(U Y\) with rational coefficients must be regular at \(t=0\) to have a finite limit there. Its limit would be a rational constant. This contradicts the pinned fixed-source irrationality, proving avoidance also on this row. The endpoint \(W_L\) need not be an ordinary integer for this argument.

## 3. An integer interpolant for the full cancellations

Fix \(H\) and select any \(m\ge1\) offsets \(0\le h<H\). For an indicated row let \(a,b,c\) denote its clocks and carry for the actual \(h\) local bits starting at time \(L\), with \(a=b=1,c=0\) at offset zero. The long clocks satisfy \(u_{L+h}=(a/b)u_L\), and \(a y_{L+h}=b y_L+c\). In the ring modulo \(G_{L+h}\), (2) gives
\[
          (u_L,y_L)\equiv (\alpha_h,\beta_h)
           := (b/a,(a s-c)/b) \pmod {G_{L+h}}.                   \tag{5}
\]
The right side depends only on \(h\), the local bits, the row and the fixed initial trial \(s\). It uses neither \(x_L\) nor \(W_L\) as a target coefficient. All its denominators are products of twos and threes. In either row the first coordinates at distinct offsets are different rational numbers, because the intervening numerator is a positive power of two and the intervening denominator is a power of three.

If \(h<h'\), any common divisor of the two raw clock differences divides the difference of the intervening clocks. This follows by dividing the two unit clock relations in the composite residue ring. In particular
\[
                   \gcd(G_{L+h},G_{L+h'})\le4^H.                 \tag{6}
\]

Let \(k=\lfloor\sqrt m\rfloor\). Since \((k+1)^2>m\), rational linear algebra supplies a nonzero polynomial \(P(U,Y)\) of degree at most \(k\) in each variable vanishing at all \(m\) target pairs. Clear its coefficient denominators to choose integral coefficients. For fixed \(n,H\) there are finitely many window words, selections of offsets and choices of row. Choose a single polynomial for each configuration once. Section 2 now makes each \(P(u_L,y_L)\) nonzero at all sufficiently large \(L\), simultaneously over this finite list. We do not use an integral-points theorem uniform in growing polynomials.

For a rational \(z\) write \(\operatorname{den}z>0\) for its reduced denominator and \(h(z)=\log\max(|\operatorname{num}z|,\operatorname{den}z)\). Then
\[
         N=(\operatorname{den}u_L)^k(\operatorname{den}y_L)^k
                                     P(u_L,y_L)
\]
is a nonzero integer divisible by each full \(G_{L+h}\). For prime valuations of these \(m\) divisors, the sum minus the maximum is bounded above by the sum of the pairwise minima. Using (6) therefore yields
\[
 \begin{aligned}
    \sum_h\log G_{L+h}
       &\le\log |N|+\tbinom m2 H\log 4\\
       &\le k\big(h(u_L)+h(y_L)\big)+O_{n,H}(1)\\
       &\le (\log16)\sqrt m\, L+O_{n,H}(1).                      \tag{7}
 \end{aligned}
\]
The middle constant can include \(\log\sum|P_{ij}|\), finite for the entire fixed list. For the physical row use \(h(u_L)\le L\log3\) and \(x_L+1\le(3/2)^L(n+1)\). In the companion row both heights are at most \(L\log4\), since \(2^{L+p_L}\le4^L\) and
\(\sum_{i<L}4^i3^{L-1-i}=4^L-3^L\) bounds the full carry.

Choose only the offsets with \(\log G_{L+h}\ge \epsilon(L+h)\). If \(m>K_\epsilon\) then the left side of (7) is at least \(m\epsilon L\), with \(m\epsilon>(\log16)\sqrt m\). The choices of \(m\le H\) are finite, giving the eventual per-row bound. Combine the two rows by a union bound. For the upper Banach density, partition an arbitrarily long interval into blocks of fixed length \(H\). Discard at most the finite initial threshold and one incomplete block. The upper density is at most \(2K_\epsilon/H\); then let \(H\to\infty\). Equivalently the \((2K_\epsilon+1)\)-st bad clock counted starting at a sufficiently late bad clock must recede arbitrarily far from the first one. The same bounded-cluster conclusion holds with any fixed finite set of offsets in place of an interval by enclosing it in one.

Section 1 shows both raw log divisors have size comparable to \(L\), so (1) gives simultaneous relative log loss tending to zero in the indicated density sense. The raw gcd of the two clock differences is \(\exp(o(L))\) pointwise by the independent two-unit argument of PR193. Thus the logarithm of the least common multiple of the two reduced denominators also agrees with the sum of their raw logarithms up to \(o(L)\) in upper Banach density along this one orbit. PR193 obtained the complete exponents by sampling words at a given weight. Here the congruences at consecutive clocks and the curve argument do the work on a prescribed ordinary path. [PR193, fixed-weight census and raw gcd, frozen head](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/arithmetic/CLOCK_FIBERS.md)

[PrefixInterpolation.lean](PrefixInterpolation.lean) checks finite composite-ring target extraction, clock overlap, existence of the nonzero rational bivariate interpolant, and the full product divisibility including every pairwise gcd. [check.py](check.py) computes both numerical carries, local targets, rational cycles, exact nonzero interpolant values where available and valuation agreements. Siegel's theorem, the fixed-source avoidance proof and the limiting estimates above are written mathematics.
