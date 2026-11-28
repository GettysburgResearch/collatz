# Fast ordinary predecessors in every short relative interval

Use the shortcut map \(T\), put \(\gamma=\log_23\), \(a_0=1/\log2\) and \(\mu=2/\log(4/3)\), and write \(\log\) for natural logarithm. Fix **one** integer target \(a\ge1\) prime to three and any fixed native word \(w\) of length \(l\) and grade \(g\). For every
\[
  0<\beta<1/2,\qquad c>a_0,\qquad
  0<\theta<\min\{1,(c-a_0)/(\mu-a_0)\},
\]
all sufficiently large real \(X\) admit at least \(X^\theta\) distinct **positive integers** \(y\) satisfying
\[
 X<y<X(1+(\log X)^{-\beta}),\quad y\equiv1\bmod3,\quad
 y\text{ reads }w,\qquad T^j y=a\text{ for some }j\le c\log X.        \tag{1}
\]
If \(c\ge\mu\) the count is \(X^{1-o(1)}\). At \(c=\mu\), one may replace the deadline by \(\mu\log X+v\sqrt{\log X}\) for any fixed real \(v\). The halving bound \(j\ge\log_2(y/a)\) makes \(a_0\) the least possible leading clock coefficient. The power exponent in (1) is a lower bound. No optimality is asserted for it.

The width exponent uses \(\mu_{\rm irr}(\log_23)\le3\) from Chudnovsky's original source, separately rebuilt in this pass. More generally the same conclusion holds for every \(\beta<1/(m-1)\) given the bound \(\mu_{\rm irr}(\log_23)\le m\). A formulation below in terms of actual continued-fraction denominators requires no irrationality-measure estimate. At a fixed relative width the usual fixed-target natural density and arithmetic-progression law already control the main macroscopic counts. The extra issue is simultaneous localization at a shrinking width, with the specified ordinary target and possibly subtypical clock. [Chudnovsky source and rebuild](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

## Positive-density input and a physical inverse route

Fix any real \(v_0\). Leen's every-target corollary gives natural density \(h_T(a)\Phi(v_0/\sigma)>0\) to sources reaching \(a\) within \(\mu\log n+v_0\sqrt{\log n}\) shortcut steps, where \(\sigma^2=2(\log3)^2/\log^3(4/3)\). Positivity follows from Mazur's fixed-target lower density, applied to the full-map target \(2a\), whose ordinary predecessors are shortcut predecessors of \(a\) by his (1.3). These are imported results for each fixed target. An alternative for a fixed logarithmic time bound is Shaik's original Theorem I.2 at every full-map clock coefficient \(>3/\log(4/3)\), applied to \(2a\) before shortcutting. [Leen, every-target corollary](https://doi.org/10.5281/zenodo.23269488) · [Mazur, Theorem 1.1 and (1.3)](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) · [Shaik, Theorem I.2](https://hexagonmath.org/pdf/2610.00523v1)

For every sufficiently large real \(Y\) there are \(\gg_{a,v_0}Y\) **ternary-unit** seeds \(b\asymp_{a,v_0}Y\) reaching \(a\) in \(\mu\log Y+v_0\sqrt{\log Y}+O_{a,v_0}(1)\) steps or fewer. Indeed discard from the preceding positive-density set below \(Y\) its members below \(\delta Y\) and those divisible by \(2^J\), choosing \(\delta\) small and \(J\) large. For each remaining \(n=2^e u\), \(u\) odd and \(e<J\), take \(b=(3u+1)/2\equiv2\bmod3\). All discarded initial path values before \(b\) exceed \(a\) when \(Y\) is large. Each \(b\) has at most \(J\) original representatives and \(b\asymp Y\), proving the assertion.

Let \(F_w(y)=(3^g y+C_w)/2^l\) be the actual word map, put \(M=3^{g+1}\), \(P=2\cdot3^g\), and \(E=3P\). Since 2 is primitive modulo every power of 3, successively choose \(1\le e_i\le E\) with \(2^{e_i}b_{i-1}\equiv4\bmod 3M\), starting from \(b_0=b\), and put
\[
       b_i=(2^{e_i}b_{i-1}-1)/3,\qquad D_j=\sum_{i=1}^j e_i .
\]
Each \(b_i\) is an odd positive integer congruent to \(1\bmod M\) for the sizes used below, and takes exactly the specified \(e_i\)-step path to \(b_{i-1}\) (earlier equality is immaterial). For \(i\ge2\) one has \(e_i\equiv2\bmod P\). The endpoint \(y\) obtained by undoing \(w\) from \(2^H b_j\) is
\[
                y=(2^{l+H}b_j-C_w)/3^g.
\]
It is an integer congruent to \(1\bmod3\) exactly when \(2^{l+H}b_j\equiv C_w+3^g\bmod M\). The right side is a unit: for \(g>0\) the last odd contributes a nonzero power of two modulo three, and for \(g=0\) the right side is 1. Thus for every \(j\ge1\) the same residue \(H\equiv H_0\bmod P\) works. The backward affine word is dyadically integral throughout, since division by three preserves dyadic integrality and undoing each actual parity letter restores that letter. Its resulting integer \(y\) therefore reads the specified word. It is positive once it lies in the desired real interval.

After unrolling the inverse path,
\[
 b_j=\frac{2^{D_j}}{3^j}\left(b-\sum_{i=1}^j3^{i-1}2^{-D_i}\right).
\]
Uniformly for \(1\le j\le K\), the correction inside parentheses is \(O(3^K)\). For \(3^K\ll Y\), the logarithms base two of the possible targets \(2^H b_j\), taken modulo \(P\), are
\[
       \log_2 b+e_1-2+H_0+j(2-\gamma)+O(3^K/Y).                      \tag{2}
\]
This residue computation is independent of the later choices of the individual exponents.

Let \(\epsilon\le1\) be the desired relative width. Choose a convergent denominator \(K\) of the irrational \((2-\gamma)/P\) with \(K>A_w/\epsilon\), for a sufficiently large fixed \(A_w\). Its first \(K\) multiples have covering radius at most \(2/K\) on the unit circle, by comparison with the permuted grid of the convergent numerator. The interval \(\log_2 F_w((X,(1+\epsilon)X))\) has length \(\gg_w\epsilon\) for large \(X\). Hence (2) can be placed strictly inside this interval by some \(j\le K\), provided \(3^K/Y=o(\epsilon)\). The chosen lift \(H\equiv H_0\bmod P\) is nonnegative if \(X/Y\ge\exp(B_w(K+1))\) for a sufficiently large \(B_w\), since \(D_j\le EK\). This constructs an actual \(y\) for each seed.

The total extra shortcut clock from \(y\) to \(b\) is
\[
          l+H+D_j=\log_2(X/Y)+j\gamma+O_{w,a,v_0}(1),                 \tag{3}
\]
by the exact unrolled formula, \(b\asymp Y\) and \(F_w(y)\asymp_w X\). The large padding exponents cancel on its left. For each \(j\), all possible exponent lists number at most \(E^j\). Given such a list, (3) puts \(H\) in an interval of bounded length independent of \(X/Y\). A fixed list and \(H\) define an injective affine map in \(b\). The number of distinct realized \(y\)'s is thus
\[
                   \gg_{a,w,v_0} Y\exp(-O_w(K+1)).                    \tag{4}
\]
No density at a stopped or adaptively chosen intermediate residue is used.

## Selecting the scales

For \(\epsilon=(\log X)^{-\beta}\), the least convergent denominator above \(A_w/\epsilon\) obeys \(K\le(\log X)^{\beta(m-1)+o(1)}=o(\log X)\), since irrationality exponent is unchanged by a nonconstant rational affine transform and \(q_{r+1}\le q_r^{m-1+o(1)}\). In particular \(K\to\infty\). For \(a_0<c<\mu\), choose \(\theta<\alpha<(c-a_0)/(\mu-a_0)\) and put \(Y=X^\alpha\). Both conditions for (2) hold. Equations (3) and (4) give a clock at most \([a_0+(\mu-a_0)\alpha]\log X+o(\log X)\) and at least \(X^{\alpha-o(1)}\) distinct starts. This proves (1) in this range.

For \(c\ge\mu\), take \(Y=X\exp(-B(K+1))\) with \(B\) fixed sufficiently large. Then (4) is \(X\exp(-O(K+1))\), and the clock from the seed estimate and (3) is at most
\[
 \mu\log X+v_0\sqrt{\log Y}
       -(\mu-a_0)B(K+1)+\gamma K+O_{a,w,v_0}(1).
\]
For the stated deadline with any prescribed \(v\), take \(v_0<v\) and use \(\sqrt{\log Y}/\sqrt{\log X}\to1\), increasing \(B\) if necessary. For fixed \(\epsilon>0\), \(K\) is fixed and (4) supplies a positive fraction of \(X\) at this central deadline. More generally, before substituting an irrationality exponent the same proof works for every schedule of widths and actual convergent denominators satisfying \(K>A_w/\epsilon,\ K=o(\log X)\).

## Members of an exact first-landing cohort which join the distinguished orbit

Fix an aperiodic positive integer orbit from \(x\) and let \(z_n\), \(t_n\), \(L_n\), \(A_n\) denote its state just after its \(n\)-th odd departure, the date, multiplier and input correction. Then \(L_n=z_n/(x+A_n)\to\infty\), \(A_n\to A_x>0\). Its reduced first landings from a real interval \(I\) which agree with all \(t_n\) initial parities are precisely the distinct integers \(N\in L_n(I+A_n)\) with \(N\not\equiv2\bmod3\). [Exact cohort theorem](FIXED_ORDINARY_LANDING_FIBRES.md)

Choose a fixed ternary-unit state \(a\) on this orbit, for instance any post-odd state. In every fixed positive real source interval \(I\), a positive fraction of the cohort subsequently reaches this actual \(a\) in \(\mu\log z_n+O(\sqrt{\log z_n})\) further steps. A disjoint positive fraction reaches 1 in that clock. Indeed apply the positive-count conclusion twice inside a fixed relative subinterval of \(L_n(I+A_n)\), prescribing \(y\equiv1\bmod3\). The constants depend on the fixed orbit, interval and targets. Fix instead a center \(r>0\) and a real source interval \((r,r+(\log z_n)^{-\beta})\): its terminal interval has lower endpoint comparable to \(z_n\) and relative width comparable to \((\log z_n)^{-\beta}\). The proof, with the constant in \(A_w\) enlarged, yields \(z_n^{\theta}\) members of each kind for every \(\theta\) in (1) and every leading deadline \(c>a_0\) (use slack in both exponents and \(c\) below the given cutoffs). The two source families share the entire specified ordinary prefix and have disjoint ultimate basins.

For all sufficiently large \(n\), after reaching \(a\) one can follow its fixed orbit forward to \(z_n\). Thus members of the first family **actually visit the distinguished state \(z_n\)**. A visit at positive lag cannot also be a same-date synchronization with \(z_n\), since that would repeat a state on its aperiodic orbit. Here the visit has positive lag: apart from possibly \(N=z_n\), any first hit of \(z_n\) is positive, and that exceptional integer is excluded by \(z_n\equiv2\bmod3\). Conversely, if some earlier visit of such an \(N\) to \(z_n\) preceded its promised visit to \(a\), the later visit to \(z_n\) would itself force a repetition. This proves a genuine asynchronous collision statement for the distinguished source at every large grade.
