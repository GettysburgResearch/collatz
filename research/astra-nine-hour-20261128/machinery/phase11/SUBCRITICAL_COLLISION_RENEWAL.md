# Bounded subcritical collision renewal at all depths

Let \(0<r<1/2\), \(u=r^2\), and give a positive gap \(e\) mass \((1-r)r^{e-1}\). Let \(\mu_{r,n}\) denote the law of the \(n\)-letter affine offset modulo \(3^n\), with this *tail* parameter convention. Then
\[
 1\le U_n=\left(\frac{1+r}{1-r}\right)^n
                    \sum_z\mu_{r,n}(z)^2\ \uparrow\ U_\infty(r)<\infty.       \tag{1}
\]
Thus the collision sum is asymptotic to the strictly positive finite constant \(U_\infty(r)\) times \(((1-r)/(1+r))^n\). In the source's notation \(U_n=U_n^{(u)}(\sqrt u)\), so (1) answers the boundedness question in §6, first item, of Cassian Mahler 164/v1 for every \(0<u<1/4\). The prior paper proves \(O_u(\sqrt n)\), has the correct exponential base, and supplies an exact first-divergence identity for its nonnegative renewal increments. Here the clock separation is free to vary. The proof also gives an exponentially decreasing upper bound in that separation, uniform in depth. [Mahler 164, (2.1), Theorem 1 and §6](https://rstation.ai/problems/collatz/papers/164) · [Mahler 162, diagonal energy correspondence](https://rstation.ai/problems/collatz/papers/162)

**Arithmetic and the collision tilt.** Use chronological odd gap words \(w=(e_1,\ldots,e_n)\). Put \(S_j=\sum_{i\le j}e_i\), \(s=S_n\), and
\[
 D_w=\sum_{j=1}^n3^{n-j}2^{S_{j-1}},\quad
 Z_w=2^{-s}D_w\bmod3^n,\quad R_w=3^{-n}D_w.
\]
Reversal of iid gaps gives the usual offset law. At fixed \(n,s\), \(D_w\) determines \(w\): subtract \(3^{n-1}\), extract the exact two-adic valuation \(e_1\) of the remaining term if \(n>1\), and recurse; the last gap is then given by \(s\). Equivalently this is the fixed-total parity-numerator decoder. [Leen, tilted Syracuse laws, §3](https://doi.org/10.5281/zenodo.23268832)

Give words the auxiliary probability \(Q(w)=(1-u)^n u^{s-n}\). Expanding the square in (1), each ordered pair with \(s_v=s_w+d\), \(Z_v=Z_w\) contributes exactly \(r^d Q(w)\); this equality follows by cancelling the powers of \(1\pm r\). Let \(T_{n,d}\) be the sum of those weights. Swapping the pair gives \(T_{n,-d}=T_{n,d}\). For \(d\ge0\), equality of ternary residues is precisely the integrality of
\[
                  h=(2^dD_w-D_v)/3^n,\qquad -R_v<h<2^dR_w.          \tag{2}
\]
At fixed \(w,d\) this \(h\) determines \(v\); at fixed \(v,d\) it determines \(w\). In the second ordering it also belongs to a **single residue class modulo \(2^d\)**, since \(3^nh\equiv-D_v\bmod2^d\). The two one-sided bounds in (2) apply in the ordinary real ordering of integers.

**Summable clock separation.** Under \(Q\) the gaps have law \((1-u)u^{e-1}\). Write \(R_n=\frac13\sum_{j=0}^{n-1}2^{S_j}/3^j\). There is \(p>1\) with
\[
 \sup_n\mathbb E_Q R_n^p<\infty,\qquad
                 p>2-\frac{\log2}{-\log r}.                            \tag{3}
\]
Indeed set \(x=-\log_2r>1\), \(p_0=2-1/x\), and choose \(p_0<p<2x-1\); the interval is nonempty by \((2x-1)(x-1)>0\). Then \(u=2^{-2x}<2^{-(p+1)}\). Convexity at \(1,3\) gives \(3^p+1\ge2^{p+1}\), hence
\[
 2^{-(p+1)}\le\frac{3^p-2^p}{2^p(3^p-1)} .
\]
This proves \(M_p=\mathbb E_Q(2^{e}/3)^p=(1-u)2^p/(3^p(1-2^pu))<1\). By Minkowski, \(\|R_n\|_p\le 1/[3(1-M_p^{1/p})]\). This proof does not require independence between the two words of a selected collision.

For \(h\ge0\), count at \(w\). There are at most \(1+2^dR_w\) choices, so their weight in \(T_{n,d}\) is at most \(r^d+(2r)^d\mathbb E_QR_n\). For \(-L\le h<0\) there are at most \(L\) choices at \(w\), at weight at most \(r^dL\). For \(h<-L\), count instead at \(v\). Now \(R_v>L\), and the single residue modulo \(2^d\) in the interval \((-R_v,-L)\) gives at most \(1+2^{-d}R_v\) choices. Crucially \(r^d Q(w)=r^{-d}Q(v)\) in this ordering. Thus the last part is at most
\[
        \mathbb E_Q R_n^p\,[r^{-d}L^{-p}+(2r)^{-d}L^{1-p}].           \tag{4}
\]
Take \(L=\exp(ad)\), with \(a<-\log r\) sufficiently close to \(-\log r\). The three bases \(r e^a,r^{-1}e^{-pa},(2r)^{-1}e^{(1-p)a}\) are all strictly below one, by \(p>1\) and (3). Also \(2r<1\). We obtain \(T_{n,d}\le C_r b_r^d\) for all \(n,d\ge0\) with \(b_r<1\). Summing over the two signs proves the bound in (1). The \(d=0\) diagonal pairs already give one. Appending the same outermost letter to both inverse words preserves their collision at depth \(n+1\); its total normalized weight is exactly the old weight since \(((1+r)/(1-r))\sum_e[(1-r)r^{e-1}]^2=1\). Equivalently this is the source's nonnegative-increment identity. It proves monotonicity and hence the finite positive limit.

In particular \(\sum_{n\ge1}(U_n-U_{n-1})<\infty\) for every subcritical \(u\). This yields neither an exponential rate for those **depth** increments nor the specific numerical tail bound for the binary splice in Mahler 164 (4.2); the exponential bound proved here concerns the difference of the **two physical clocks** \(s_v-s_w\) at the same depth. The critical \(r=1/2\) unrestricted collision energy instead grows linearly. [Weaver 146](https://rstation.ai/problems/collatz/papers/146) · [Discussion of the depth-rate conditions](https://rstation.ai/r/collatz/posts/87)

**Collision genealogy.** Draw two independent words with the original tail parameter r, conditional on equality of their n-trit offsets. Let L be the length of the common outer prefix of the two inverse words. For \(0\le k\le n\),
\[
                     \mathbb P(n-L\le k\mid\text{collision})=U_k/U_n.
\]
Indeed the shared \(n-k\) letters contribute \((\sum_e p_e^2)^{n-k}\) times the probability of a suffix collision at depth k. Conditional on this event those common letters are independent with the squared tilt \(Q\). Thus the length remaining after the last shared outer letter has a limiting finite law: mass \(1/U_\infty\) at zero and \((U_k-U_{k-1})/U_\infty\) at \(k\ge1\). In the critical fair law the linear collision slope leads to a different, macroscopic split. [Critical collision genealogy](../../escape/phase9/EXACT_COLLISION_ENERGY_SLOPE.md)
