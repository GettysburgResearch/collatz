# Hitting a prescribed ordinary integer from every real interval and every dyadic cylinder

Write \(T\) for the shortcut map and \(g(w)\) for the odd count in a native word \(w\). Fix \(B>0\). Given **any** interval \(I\subset(0,B)\) of width \(u>0\), word \(w\) of length \(l\), and eligible integer \(N\ge1\), \(N\not\equiv2\pmod3\), there is a positive reduced rational \(r=m/3^n\in I\) whose first \(l\) bits are \(w\) and whose first integer is \(N\), at a date \(t>l\) satisfying
\[
                n\le t\ll_B 1+l+\log(N+1)+\log^+(1/u).                 \tag{1}
\]
All three costs have the correct worst-case order. In particular **each** admissible target's physical first preimages are dense in \(\mathbb R_{>0}\times\mathbb Z_2\), with uniform linear clock in both the real and the dyadic bit precision. The first integer landings in an inadmissible class are empty. A [renewal formula](FIXED_TARGET_RENEWAL_PROFILE.md) gives the reciprocal mass at large marks for fixed intervals. Here the interval and word can vary at every mark, including tiny intervals and arbitrarily long words at the target \(1\).

## An explicit real interval construction

The two inverse letters on odd-denominator rationals are \(E(y)=2y\), \(O(y)=(2y-1)/3\). Their backwards parity is always the designated one. First take \(q_N=O(N)=(2N-1)/3>0\), which has reduced ternary height one exactly for the eligible marks. Thereafter \(E\) preserves positive denominator height and \(O\) increases it by one: if \(3\nmid d,\ h>0\), their new numerators are \(2d\) and \(2d-3^h\). Thus every constructed positive endpoint has its first integer at the originally chosen \(N\). All earlier intermediate real values in its forward path are positive, since the forward map preserves positivity.

Let \(F_w(y)=(3^gy+C_w)/2^l\) be the forward real affine map of the requested word \(w\), \(g=g(w)\). Write \(J=F_w(I)\) with midpoint \(z\) and radius \(v=(3^g/2^l)u/2\). We first need an inverse endpoint in \(J\). Let \(b\ge0\) be an integer for which \(z'=2^{-b}z\in[1,2)\) if \(z\ge1\), using \(b=0\) when \(z<1\). Put \(\rho=8/9\). The two actual inverse blocks
\[
          O\circ O\circ E(y)=\rho y-5/9,\qquad
          E\circ O\circ O(y)=\rho y-10/9
\]
have a common multiplier. The positive carry maps \(C\mapsto\rho C+5/9\) and \(C\mapsto\rho C+10/9\) send \([5,10]\) onto two overlapping intervals whose union is \([5,10]\). Therefore for every \(c\in[5,10]\) some \(k\) such blocks have composite map \(\rho^k y-C_k\) with \(|C_k-c|\le10\rho^k\). Indeed choose successively a preimage in \([5,10]\) through a carry map covering the current point, and then replace the last residual by zero. Composition of the physical blocks in the corresponding order gives the indicated constant term.

Choose the least \(k_0\ge0\) with \(10\rho^{k_0}<2^{-b}v\) and \(\rho^{k_0}q_N\le z'+8\). Take the least \(H\ge0\) with \(2^H\rho^{k_0}q_N\ge z'+8\). Multiply this number by further factors \(\rho\) until it is at most \(z'+8\). The number of factors is at most six, since the starting number is less than \(2(z'+8)\) and \(\rho^6<1/2\). With \(k\) the resulting total exponent, the difference
\[
                          c=\rho^k2^Hq_N-z'
\]
lies in \([5,10]\): it is at most eight, and it is at least \(\rho(z'+8)-z'>6\). Apply the \(H\) inverse evens and the selected \(k\) blocks from \(q_N\). The result differs from \(z'\) by strictly less than \(2^{-b}v\). Apply \(b\) final inverse evens to reach \(J\); now undo \(w\), giving the desired \(r\in I\). Its dyadic bits read \(w\), and all states strictly before the final mark have positive reduced height. This gives an explicit construction with
\[
                      n=g+2k+1,\qquad t=l+1+H+3k+b .                    \tag{2}
\]
The estimates \(b=O_B(l+1)\), \(v\ge2^{-l}u/2\) follow directly since \(F_w(y)+1\le(3/2)^l(y+1)\). Consequently \(k_0=O_B(1+l+\log(N+1)+\log^+(1/u))\); also \(q_N\ge1/3\) gives \(H=O(k+1)\). This proves (1). Taking larger admissible \(k_0\) produces infinitely many distinct first preimages, since their grades tend to infinity.

Every word fixes its own complete class modulo \(2^l\) on \(\mathbb Z_2\), and conversely these classes give all words. This proves the two-place density. Even among all possible marks, an all-even prefix of length \(l\) forces \(2^l\mid m\), so \(n\ge(l\log2-\log B)/\log3\). For any source in \((0,B)\), \(N+1\le(3/2)^n(B+1)\), since even steps do not increase \(y+1\) and an odd step multiplies it by \(3/2\). Finally all reduced ternary denominators through grade \(n\) belong to the single grid \(3^{-n}\mathbb Z\). Some intervals in a fixed interior compact range of width comparable to \(3^{-n}\) omit this grid. These bounds prove the stated worst-case order for grades as well as clocks.

The same construction may start at any **positive nonintegral ternary rational** \(q\), using \(q\) in place of \(q_N\) and omitting the initial odd inverse. All new denominators remain nonintegral. In a fixed compact subinterval of \((0,\infty)\) the constants are uniform over \(q\), regardless of its reduced height. In particular one backwards path from a specified \(N\) can visit every member of a countable base in the real and dyadic product: at each attained rational simply continue the construction to the next requested product neighborhood. This stronger density concerns one connected inverse path.

## Optimal costs after prefixes of one fixed aperiodic ordinary source

Fix one positive integer \(x\) whose ordinary orbit is aperiodic, and one finite interval \(I\) of positive length in \((0,\infty)\), allowing lower endpoint zero. Write \(w_l\) for its first \(l\) steps, \(z_l=T^l x\) and \(g_l=g(w_l)\). For any eligible \(N\), consider all first preimages in \(I\) which read \(w_l\) and land at \(N\) **strictly after** it. Write \(h=n-g_l\) and \(\tau=t-l\) for the extra odd grade and native clock. Uniformly in all eligible \(N\), for \(l\) sufficiently large,
\[
 \begin{split}
 \min h&=[\log_{3/2}(N/z_l)]_++O_{x,I}(1),\\
 \min\tau&=[\log_{3/2}(N/z_l)]_++[\log_2(z_l/N)]_++O_{x,I}(1).
 \end{split}                                                          \tag{3}
\]
One witness attains both upper bounds. In particular an arbitrarily long prefix can still lead to the specified target \(1\) with only a bounded number of additional odd departures. In the opposite size direction each additional odd can give almost its full native growth factor \(3/2\).

To prove this, the true prefix correction gives \(z_l=L_l(x+A_l)\), \(L_l=3^{g_l}/2^l\). The correction \(A_l\) is constant on even steps and tends to a finite positive limit on an aperiodic integer orbit by Garcia and Tal's orbit sparsity and the correction product. Also \(z_l\to\infty\) and \(J_l=F_{w_l}(I)=L_l(A_l+I)\). Thus the midpoint \(z\) and radius \(v\) of \(J_l\) each obey positive upper and lower constant bounds after division by \(z_l\); every element of \(J_l\) is comparable to \(z_l\), since \(A_l\) is eventually bounded below away from zero. These bounds apply at all native dates. [Fixed-orbit correction and source intervals](FIXED_ORDINARY_LANDING_FIBRES.md) · [Garcia and Tal, Lemma 3 and Corollary 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf)

Start from \(q_N=(2N-1)/3\), take \(H\) inverse evens and then \(k\) inverse odds. The resulting value is
\[
                        y+1=(2/3)^k(2^Hq_N+1).                           \tag{4}
\]
Choose the least \(k_0\ge0\) with \((2/3)^{k_0}q_N\le z+1\). Then \(k_0=[\log_{3/2}(N/z_l)]_++O_{x,I}(1)\). Put \(\theta>0\) sufficiently small, depending only on \(x,I\), that the interval \([z+1,(1+\theta)(z+1)]\) lies strictly inside \((1+z-v/2,1+z+v/2)\) for all large \(l\). The successive phases \(k\log_2(2/3)\pmod1\) are an irrational rotation. A finite initial segment is dense to any fixed positive tolerance, uniformly after translation. Thus for some \(k_0\le k\le k_0+K_{x,I}\) one can choose an integer \(H\) with
\[
               z+1\le(2/3)^k2^Hq_N\le(1+\theta)(z+1).
\]
Necessarily \(H\ge0\) by the choice of \(k_0\) (or choose \(H=0\) at equality). The remaining term \((2/3)^k\le1\) in (4) is less than \(v/2\) for all large \(l\), uniformly in \(N\), so \(y\in J_l\). Undo \(w_l\) to finish. The number of extra odds is \(k+1\) and \(H=[\log_2(z_l/N)]_++O_{x,I}(1)\), by taking logs in the last inequality and substituting \(k=k_0+O_{x,I}(1)\). These prove the upper estimates. Conversely every such source is at some \(y\asymp_{x,I} z_l\) after its prefix. The exact maps give \(N+1\le(3/2)^h(y+1)\), \(N\ge y/2^\tau\) and \(\tau\ge h\). One of the two positive parts in the clock formula vanishes. This proves the matching lower estimates.

If the fixed ordinary \(x\) is eventually periodic, its eventual period has \(3^{g_{\rm lap}}<2^{t_{\rm lap}}\) from its strictly positive carry. Hence \(L_l\) decays exponentially in \(l\). For a reduced \(m/3^{g_l+h}\in I\) reading \(w_l\), the nonzero integer \(m-3^{g_l+h}x\) is divisible by \(2^l\). As \(I\) is bounded, this gives \(3^h L_l\ge1/\sup_{r\in I}|r-x|\). Thus every candidate requires \(h\gg_x l-O_{x,I}(1)\). For each fixed eligible \(N\), (1) gives a matching upper order \(O_{x,I,N}(l)\). In particular divergence of this fixed \(x\) is equivalent to bounded extra grade along an unbounded sequence of prefixes reaching **one and the same** first mark \(1\) from a fixed positive interval. The first preimages are genuine rationals of growing denominators.

Earlier real/ternary support estimates and a bounded real inverse selector for the random joint affine law appear in Weaver 19, equations (B8)–(B13). The [coherent numerator transplantation](COHERENT_LANDING_SPECTRUM.md) uses that selector to prescribe a ternary numerator class and keep an old finite tail. The [bounded witness construction](BOUNDED_REAL_WITNESSES.md) gives a pair of rational arms reaching a chosen merger. Here the target is a specified *first integer*, the second place is dyadic, and (1) and (3) bound the actual native clock to that target. [Weaver 19/v2, §9.1](https://rstation.ai/problems/collatz/papers/19/v2) · [Weaver 23, description of the real/ternary support theorem](https://rstation.ai/problems/collatz/papers/23)
