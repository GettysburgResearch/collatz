# The asymptotic slope of the original Syracuse collision energy

Let \(m\) be Haar probability on \(\mathbb Z_3\). Use the original independent fair gaps \(\Pr(e=j)=2^{-j}\), and put
\[
 A_k=3^k2^{-(e_1+\cdots+e_k)},\quad A_0=1,\qquad
 H_n=\max_{0\le k\le n}A_k,\quad H=\sup_{k\ge0}A_k.
\]
Use outer-prefix order for the stationary ternary coding \(Z\), so \(Z\bmod3^n\) depends only on the first \(n\) gaps. Denote the stationary density by \(\rho\), the conditional expectation on the depth-\(n\) ternary partition by \(Q_n\), the finite density by \(\rho_n=Q_n\rho\), and \(E_n=\int\rho_n^2dm\).

**Source-qualified theorem.** In the notation of Weaver's Paper 146,
\[
                 \lim_{n\to\infty}\frac{E_n}{n}
                    =2\kappa\mu=\mathcal D,\qquad
                 \mu=\log3-\tfrac43\log2>0.                         \tag{1}
\]
Here \(m(\rho>t)\sim\kappa t^{-2}\) and \(\mathcal D=\int\sum_{e\ne f}b_e b_f\,dm\) is the finite positive distinct-branch interaction. Weaver proves these facts and \(E_n\asymp n\), and explicitly leaves the existence of a slope in this normalization open. The upper bound below separates the tilted first-crossing clock from the unrestricted real cap. All results here concern the original ternary probability; no assertion about a supplied positive orbit follows from (1) alone. [Weaver, Paper 146/v1, (2a), (3), (19)–(25) and §9](https://rstation.ai/problems/collatz/papers/146/v1)

## Inputs and the lower bound

Write \(\sigma_B\,dm=\Pr(H\le B,\ Z\in dz)\). Weaver proves
\[
 \int\sigma_B^3\,dm\ll B,\qquad
 \int(\sigma_{2B}-\sigma_B)^3\,dm\ll B\qquad (B\ge1).
\]
The first of these bounds alone suffices below. With \(a_e=3/2^e\), define \(b_e(z)=a_e1_{z\in F_e\mathbb Z_3}\rho(F_e^{-1}z)\). The paper gives
\[
 D_n=E_{n+1}-E_n\ge0,\qquad
 \mathcal D=\int\sum_{e\ne f}b_e b_f\,dm\le\liminf_nD_n,\qquad
 \mathcal D=2\kappa\mu.
\]
These imply \(\liminf E_n/n\ge\mathcal D\) by summing increments. Our proof does not presume that the individual \(D_n\) converge.

## A finite prefix shell above the tilted time scale

For \(B\ge1\), define \(h_{n,B}\) by
\[
 h_{n,B}(z)=3^n\Pr(B<H_n\le2B,\ Z\equiv z\bmod3^n).
\]
Under the original law \(A_k\) is a nonnegative mean-one martingale. The change of measure on \(k\) letters with derivative \(A_k\) gives independent gaps with probabilities \(3/4^e\); decorate their probabilities by a star. At the first strict crossing \(\tau_B\), the likelihood \(A_{\tau_B}>B\), giving
\[
                \int h_{n,B}\,dm\le
                \Pr(\tau_B\le n)\le B^{-1}\Pr_*(\tau_B\le n).       \tag{2}
\]
This follows by summing over first-crossing words of length at most \(n\).

Given the prefix, its independent fresh fair suffix has a maximum \(H'\) of the same law as \(H\) and \(H=\max(H_n,A_n H')\). The martingale inequality gives \(\Pr(H'>2)\le1/2\). On each prefix counted by \(h_{n,B}\), imposing \(H'\le2\) therefore retains at least half its probability and forces \(B<H\le4B\). The depth-\(n\) residue is already determined by the prefix. Consequently
\[
             h_{n,B}\le2 Q_n(\sigma_{4B}-\sigma_B).
\]
Conditional expectation contracts \(L^3\), so the cubic cap bound gives \(\int h_{n,B}^3\,dm\ll B\). Cauchy–Schwarz on \(h^{1/2}h^{3/2}\) and (2) yield
\[
                  \|h_{n,B}\|_2^2\ll \Pr_*(\tau_B\le n)^{1/2}.      \tag{3}
\]

Fix \(\epsilon>0\) and \(B_0=\exp((\mu+\epsilon)n)\). Under the tilted law the increments \(\log a_e\) have mean \(\mu\), finite exponential moments near zero and a bounded positive part. Choose \(\lambda>0\) small enough that \(1<\mathbb E_*a_e^\lambda<e^{\lambda(\mu+\epsilon/2)}\). Union and Chernoff bounds at \(1\le k\le n\) give
\[
         \Pr_*(\tau_B\le n)\le
               n B^{-\lambda}(\mathbb E_*a_e^\lambda)^n
                  \le n e^{-\lambda\epsilon n/2}\qquad(B\ge B_0).
\]
Because \(H_n\le(3/2)^n\), at most \(O(n+1)\) dyadic shells starting at \(B_0\) are nonempty. Applying (3) and the \(L^2\) triangle inequality, the total finite density contributed by \(H_n>B_0\) has \(L^2\) norm \(O_\epsilon(e^{-c_\epsilon n})\), for a smaller \(c_\epsilon>0\).

## Capping all later excursions while retaining the low prefix

Take \(B_1=\exp((\mu+2\epsilon)n)\). On \(H_n\le B_0\), a later strict crossing of \(B_1\) requires \(H'>B_1/A_n\). Conditionally on the \(n\) letters this has probability at most \(A_n/B_1\le B_0/B_1\). The finite density \(l_n\) contributed by those low prefixes therefore satisfies
\[
                       l_n\le (1-B_0/B_1)^{-1}Q_n\sigma_{B_1}.       \tag{4}
\]
Importantly, this bounds the low-prefix **density** on each depth-\(n\) residue, not only its overall mass. Since \(\rho_n=l_n+\sum_{r\ge0}h_{n,2^rB_0}\), we have reduced its squared norm to the cap norm at a deterministic height.

For every \(B\ge1\), \(0\le\sigma_B\le\rho\) and
\[
      \int\sigma_B^2\,dm
       \le \int \min(\rho,B)^2\,dm+B^{-1}\int\sigma_B^3\,dm
       \le \int_0^B 2s\,m(\rho>s)\,ds+O(1).
\]
The exact tail of \(\rho\) makes the last integral \(2\kappa\log B+o(\log B)\). Equations (3)–(4), \(L^2\) contraction and \(B_0/B_1=e^{-\epsilon n}\) now give \(\limsup E_n/n\le 2\kappa(\mu+2\epsilon)\). Letting \(\epsilon\downarrow0\) and using the lower bound proves (1).

This also gives the explicit Cesàro disappearance of any excess finite-cylinder branch interaction: \(n^{-1}\sum_{k<n}|D_k-\mathcal D|\to0\), since the negative part tends to zero by the lower limit and the signed Cesàro means tend to zero by (1). This conclusion allows a sparse set of exceptional individual depths. The constant is specified by Weaver's convergent interaction integral and is not numerically evaluated here.

## The whole shared prefix at a true finite collision

Take two independent length-\(n\) words of fair geometric gaps, conditional on their ternary codes agreeing modulo \(3^n\). This event has probability \(3^{-n}E_n\). Write \(L_n\) for the number of initial letters the two outer words share. If a prescribed length-\(r\) word \(w\) is common, the remaining condition is precisely a depth-\(n-r\) collision of the independent suffixes. Indeed each shared affine branch reduces ternary precision by one upon inversion. Writing \(p_*(w)=\prod_{e\in w}3/4^e\), we obtain
\[
  \Pr(L_n\ge r,\ \text{common first \(r\) letters }w)
       =p_*(w)\,E_{n-r}/E_n .
\]
In particular \(\Pr(L_n=l)=D_{n-l-1}/E_n\) for \(0\le l<n\), with \(\Pr(L_n=n)=1/E_n\). Given \(L_n=l\) of positive probability, the common word has exactly \(l\) iid tilted letters and is independent of the remaining pair conditioned on immediate splitting and suffix collision. The completely identical case \(l=n\) also gives the tilted word law.

By the absolute Cesàro bound after (1), the total variation distance from the law of \(L_n\) to the discrete uniform law on \(0,\ldots,n-1\) tends to zero. Indeed the sum of differences from \(1/n\) is at most \(\sum_{k<n}|D_k-\mathcal D|/E_n+|n\mathcal D/E_n-1|\), with the remaining atom \(1/E_n\). Therefore the **whole common word**, of random finite length, is asymptotically in total variation an iid tilted word stopped at an independent uniform index in this range.

The common ternary residue has law \(\rho_n^2\,dm/E_n\) on the depth-\(n\) partition. At every depth \(r\le n\), the event \(L_n\ge r\) gives exactly the depth-\(r\) tilted stationary law, since the common first \(r\) letters determine the common residue modulo \(3^r\). Hence its distance in total variation from that tilted marginal is at most \(1-E_{n-r}/E_n\), uniformly for every \(r\). In particular it tends to zero along every \(r=o(n)\). This is a statement on colliding genuine fair words; it makes no assumption about the coding of a prescribed positive integer.
