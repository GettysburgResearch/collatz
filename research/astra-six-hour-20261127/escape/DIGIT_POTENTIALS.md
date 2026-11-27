# Long ordinary ascent against sparse corrections at every digit depth

Let \(\mathcal P\) be any finite set of primes. For every \(p\in\mathcal P\) and \(j\ge1\) choose any real table \(u_{p,j}\) on \(\mathbb Z/p^j\mathbb Z\), with the **unnormalized** size
\[
       \sum_{j\le D}\ \sum_{a\bmod p^j}|u_{p,j}(a)|\le C_p(D+1)
                         \qquad(D\ge1).                              \tag{1}
\]
For each \(p\) allow an arbitrary nonnegative integer cutoff \(L_p(n)\le B_p\log_2(2+n)\), with \(B_p\) uniform in the positive ordinary input \(n\). Consider the actual scalar
\[
 V(n)=\log_2 n+\sum_{p\in\mathcal P}\sum_{1\le j\le L_p(n)}
                 u_{p,j}(n\bmod p^j)+e(n),\qquad
                 \frac{e(n)}{\log_2(2+n)}\longrightarrow0.
\]
For every \(\epsilon>0\), every floor \(F\), and arbitrarily large clock counts \(K\), some positive ordinary source \(x\) satisfies
\[
     \min_{0\le t\le K}T^t x>F,\qquad
     V(T^K x)-V(x)\ge K\bigl(\log_2(3/2)-\epsilon\bigr).            \tag{2}
\]
The baseline constant is sharp over this class. For \(V=\log_2 n\), each ratio \(T(n)/n\) at height \(n>F\) is at most \((3+1/F)/2\). In particular no such \(V\) can decrease along every sufficiently high positive shortcut edge.

The class includes truncated logarithmic kernels of finite signed \(p\)-adic measures. Taking \(u_{p,j}(a)=\nu_p(a+p^j\mathbb Z_p)\) gives depth \(j\) mass at most \(\|\nu_p\|_{\rm TV}\). With \(L_p(n)=\lceil\log_p(1+n)\rceil\), the corresponding correction is \(\int\min(v_p(n-t),L_p(n))\,d\nu_p(t)\). These corrections can have order \(\log n\) near atoms. General tables in (1) need no compatibility between consecutive depths. Haar-normalized average table size would be a different hypothesis.

## Ordinary clocks, separate cylinders, and a sum over candidates

Write \(d_*=\log_2(3/2)\). Choose \(N\) distinct positive integers \(m_i\), all large enough that the word \(W_i=1^{m_i}0\) has real logarithmic forward drift
\[
   d_i=\frac{m_i}{m_i+1}\log_2 3-1>d_*-\epsilon/3>0.
\]
It suffices to prove the result for small \(\epsilon\). Write \(h_i=m_i+1\), and let \(r_i\) be the rational fixed point of this word's forward affine map. Its denominator in lowest terms divides \(3^{m_i}-2^{h_i}\), a unit at both 2 and 3. The distinct infinite words \(W_i^\infty\) give distinct \(r_i\) by the native binary cylinder bijection. Choose a fixed \(J\) large enough that their residues are pairwise distinct both modulo \(2^J\) and modulo \(3^J\), and \(p^J>2N\) at all remaining primes. All choices up to this point can depend on \(N,\epsilon\), independently of \(K\).

For every common multiple \(K\) of the \(h_i\), put \(M_i=K/h_i\). Impose \(x_i\equiv r_i\bmod 2^{K+J}\). Its actual first \(K\) clocks then follow \(W_i^{M_i}\). The endpoint \(y_i=T^Kx_i\) satisfies the ordinary identity
\[
                 y_i-r_i=(3^{m_iM_i}/2^K)(x_i-r_i).                \tag{3}
\]
Thus \(y_i\equiv r_i\bmod2^J\). Impose \(x_i\equiv r_i\bmod3^J\) as well, giving \(y_i\equiv r_i\bmod3^J\). At any remaining \(p\in\mathcal P\setminus\{2,3\}\), the forward affine map of this finite word is a bijection modulo \(p^J\): its denominator is \(2^K\) and its numerator slope is \(3^{m_iM_i}\), both units there. This uses the finite word's integer carry and works even if \(r_i\) has denominator divisible by \(p\). Greedily choose a residue for \(x_i\bmod p^J\) so that all starts are distinct and all images are distinct. At most \(2(i-1)\) residues are forbidden.

CRT gives all these prescriptions with a modulus \(2^K D_N\), where \(D_N\) is independent of \(K\). Take the representative in \([(F+2)2^K D_N,(F+3)2^K D_N)\), increasing the integer multiplier if \(F\) is not integral. Every intermediate value is at least \(x_i/2^K>F\). Uniformly over this fixed finite family, \(\log_2 x_i=K+O_{N,F}(1)\), and (3) gives \(\log_2 y_i=(1+d_i)K+O_{N,F}(1)\). In particular \(\log_2(2+x_i),\log_2(2+y_i)\le2K\) once \(K\) is large, with the leading constant **independent of \(N\)**. Also \(\log_2(y_i/x_i)=d_iK+o(1)\).

At each \(p,j\ge J\), the \(N\) initial classes are all distinct, and the \(N\) terminal classes are all distinct. This remains true if some indices are removed because of their individual cutoff. Sum the absolute values of all corrections at all \(2N\) endpoints. On the depths \(j\ge J\), disjointness and (1) bound this sum by
\[
          2\sum_{p\in\mathcal P} C_p\bigl(2 B_pK+1\bigr).
\]
Earlier depths cost \(O_{N,F,\epsilon,V}(1)\), since there are finitely many of them. Thus some arc has combined absolute corrections at both ends at most \(4(\sum_p C_pB_p)K/N+O_{N,F,\epsilon,V}(1)\). Choose \(N\) first, large enough that its linear coefficient is less than \(\epsilon/3\). Since all endpoints tend to infinity with \(\log_2(2+n)\le2K\), the two errors \(e(n)\) cost \(o(K)\), uniformly over this fixed family. Combining these estimates proves (2).

The sources here vary with the test horizon. Result (2) concerns proposed descent functions asserted to work on **all** sufficiently large integers. It leaves the fate of each fixed ordinary source open.

Sylve Recursions uses positive shadows of the negative cycle \((-5,-7)\) to rule out a different arithmetic potential class containing prime counts, a fixed modulus and a carry-depth function. The theorem here controls unbounded digit depths through the combined mass (1) and achieves the sharp maximal shortcut ascent as a lower bound. [Sylve Recursions, paper 3, Theorem 1](https://rstation.ai/problems/collatz/papers/3)
