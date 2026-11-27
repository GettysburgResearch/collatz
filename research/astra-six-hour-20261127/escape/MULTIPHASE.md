# Several growing blocks in each stage

Fix finitely many literal shortcut words \(V_i,U_i\), \(1\le i\le k\), with each \(V_i\) nonempty. At stage \(n\ge0\) read
\[
                   V_1^n U_1\,V_2^n U_2\cdots V_k^n U_k.
\]
Writing \(H=\sum |V_i|\) and \(P=\sum p(V_i)\), put \(s=2^H,\ r=3^P,\ q=r/s\), and \(Q=\max(r,s)\). The dense growing portion thus supplies \(P\) odd letters in \(H\) clocks. Read all finite words in their original chronological direction.

Let \(b_i\) be the rational fixed point of \(f_{V_i}\), using [the native inverse maps](STAIRCASE.md). Set \(b_{k+1}=b_1\) and count the **active** boundaries
\[
         \ell=\#\{i:\ d_i=f_{U_i}(b_{i+1})-b_i\ne0\}.
\]
If \(\ell=0\), the prescribed infinite word is periodic, with binary seed \(b_1\). When \(\ell\ge1\), the prescribed binary seed is irrational, and a positive ordinary integer \(x\) can agree through only \(O_{\rm template}(\log(2+x))\) clocks, provided
\[
        q\le1\qquad\text{or}\qquad
        a=\frac{\log_2 q}{H}<\frac{2}{2\ell-1+\sqrt{1+4\ell^2}}.    \tag{1}
\]
The equality case in the positive-drift inequality has no conclusion here. This statement includes any independently affine multiplicities \(a_i n+r_i\), \(a_i\ge1,\ r_i\ge0\), by substituting \(V_i^{a_i},V_i^{r_i}U_i\) for \(V_i,U_i\). The one-active-boundary case covers the full native drift since \(\log_2(3/2)<(\sqrt5-1)/2\). For two active boundaries the permitted drift is \(a<2/(3+\sqrt{17})\), including the two growing blocks \(1,10\) with empty separators. Their distinct fixed points activate both boundaries, and \(q=9/8>1\).

## Reduction to a finite sum of series

Write \(v_i=a_{V_i}\), \(u_i=a_{U_i}\), \(A=\prod_i u_i\) and \(q^{-1}=\prod_i v_i\). In stage \(n\), subtract \(b_i\) at the entrance to phase \(i\) and \(b_{i+1}\) at its exit, with the last exit in the next stage. The centered input and exit satisfy
\[
       x_{n,i}-b_i = v_i^n\bigl(d_i+u_i(x_{\rm exit}-b_{i+1})\bigr).
\]
At the beginning of stage \(n\) the accumulated linear multiplier from stage zero is \(A^n q^{-\binom n2}\). Consequently the selected binary source is
\[
 b_1+X,\qquad X=\sum_{i:d_i\ne0} c_i T_q(z_i),\qquad
 c_i=d_i\prod_{j<i}u_j,\qquad z_i=A\prod_{j\le i}v_j .
\]
The fixed points \(b_i\) are binary integral and the tail multiplier tends to zero. If all boundaries vanish, the word of stage 1 fixes \(b_1\) and has positive length. Its iterations give the periodic itinerary of \(b_1\), which also realizes the whole directive by the centered recursion. In the active case, the binary valuations \(\lambda_i=v_2(z_i)>0\) are strictly increasing. Their total span is **less than \(H\)**, including after inactive boundaries are discarded.

## A shift polynomial with a unique leading binary term

Reindex the active phases in increasing order of \(\lambda_i\). For \(y\in\mathbb Q_2\) define
\[
 Y_m(y)=q^{\binom m2}\left(y-\sum_i c_i\sum_{j<m}z_i^j q^{-\binom j2}\right).
\]
At the selected \(X\), the exact binary expansion is
\[
                 Y_m(X)=\sum_{t\ge0}\sum_i c_i z_i^{m+t}q^{-tm-\binom t2}.        \tag{2}
\]
Write \(z_i=e_i/f_i\) in lowest terms with \(f_i>0\), and let \(E\) shift \(m\) to \(m+1\). Use the integer polynomial
\[
  P_n(Z)=\prod_i\prod_{j=0}^{n-1}(f_i r^j Z-e_i s^j),\qquad I_n(y)=P_n(E)Y_m(y).
\]
The term in (2) at \(t,i\), viewed as a function of \(m\), is multiplied by \(P_n(z_i q^{-t})\); it vanishes for \(0\le t<n\). At \(t\ge n\) all factors have exactly the valuation \(v_2(e_i)+Hj\), with \(i,j\) here indexing the factor. Indeed the first term of that factor, evaluated at \(z_h q^{-t}\), has valuation \(v_2(f_i)+\lambda_h+Ht>v_2(f_i)+\lambda_i+Hj\) since the \(\lambda\) span is less than \(H\). Therefore
\[
        v_2\big(P_n(z_h q^{-t})\big)=n\sum_i v_2(e_i)+\ell H\binom n2.
\]
At fixed \(t\ge n\) and sufficiently large \(n\), the first active phase uniquely minimizes \(v_2(c_i)+(m+t)\lambda_i\), uniformly in \(m\ge0\). Its valuation strictly increases with \(t\), so the term \(t=n,i=1\) is uniquely smallest even if signs differ. Thus \(I_n(X)\ne0\), and its **exact** valuation for such \(n\) is
\[
 L_n=H\left((\ell+1)\binom n2+mn\right)
              +n\sum_i v_2(e_i)+(m+n)\lambda_1+v_2(c_1).            \tag{3}
\]

## Comparison with one ordinary starting value

Suppose that \(y\in\mathbb Q\) and
\[
                   v_2(y-X)>L_n+H\binom{m+\ell n}{2}.              \tag{4}
\]
The general convention is \(v_2(0)=+\infty\). Because \(P_n\) has integer coefficients, (4) makes \(I_n(y)-I_n(X)\) have valuation greater than \(L_n\). Hence the nonzero rational \(I_n(y)\) has valuation exactly \(L_n\).

The denominator of \(B Y_j(y)\), \(B=\operatorname{den}(y)>0\), divides \(D^{m+\ell n+1}\) for every \(m\le j\le m+\ell n\) with \(D\) fixed by the template. At odd primes this follows by expanding the definition: the powers \(q^{\binom j2-\binom t2}\), \(t<j\), have only dyadic denominators. The other denominators come from fixed \(c_i,z_i^t\). At 2, the expansion (2) gives \(v_2(Y_j(X))\ge\min_i v_2(c_i)\) since \(\lambda_i>0\). The replacement error \(q^{\binom j2}(y-X)\) has valuation greater than \(L_n\), which tends to infinity. A single fixed power of 2 suffices. At the real place,
\[
 |B Y_j(y)|\le H(y) C^{m+\ell n+1}\max(1,q)^{\binom{m+\ell n}{2}}
\]
for a template constant \(C\), by its finite definition. The sum of absolute coefficients of \(P_n\) is at most \(C^nQ^{\ell\binom n2}\) after increasing \(C\). The nonzero integer \(D^{m+\ell n+1}B I_n(y)\) now implies
\[
  L_n\le \log_2 H(y)+\ell\binom n2\log_2Q+
          \binom{m+\ell n}{2}\log_2^+q+O_{\rm template}(m+n+1).     \tag{5}
\]
The error constants are independent of \(y\). Here \(H(y)\) denotes rational height while the unadorned \(H\) counts growing shortcut clocks.

Set \(m=\lfloor\beta n\rfloor\) for \(\beta\ge0\). The available quadratic gain in twice (5), over \(n^2\), is
\[
         g=H(\ell+1+2\beta)-\ell\log_2 Q-(\beta+\ell)^2\log_2^+q.
\]
For \(q\le1\), this is \(H(1+2\beta)>0\). For \(q>1\) its positivity is exactly \(1+2\beta>a(\ell+(\beta+\ell)^2)\). The maximum permitted \(a\) occurs at \(\beta=(-1+\sqrt{1+4\ell^2})/2\), giving (1). With \(g>0\) choose \(n\) immediately above the larger root of \((g/2)n^2=\log_2 H(y)+O_{\rm template,\beta}(n+1)\), using an explicit upper bound for the linear error. Equations (3) and (5) contradict (4), proving
\[
 v_2(y-X)\le
 \frac{H\left(\ell+1+2\beta+(\beta+\ell)^2\right)}{g}\log_2 H(y)
     +O_{\rm template,\beta}\!\left(\sqrt{\log_2 H(y)}+1\right).
\]
In particular \(X\notin\mathbb Q\). For a fixed positive ordinary source use \(y=x-b_1\). This bounds its initial native agreement with the prescribed stages. The coefficients' separation was proved at the binary place, so phase cancellation and signed rational sources are both covered.

Weaver already proves a stronger numerical multi-value independence criterion that applies to these positive separated arguments, and treats finite rational agreement by two-place Hankel determinants. In particular every pure-growing two-block schedule with distinct centers is excluded there, including high positive drifts outside (1). The shift-polynomial proof above is an alternative elementary calculation with explicit arbitrary separators and a local noncancellation certificate. We claim no improved multiphase drift range. [Weaver, paper 70, §§4–7](https://rstation.ai/problems/collatz/papers/70) · [Weaver, paper 136, strengthened height constants](https://rstation.ai/problems/collatz/papers/136)

The underlying p-adic Tschakaloff linear-independence problem is classical. This note supplies the boundary coefficients, the native phase separation, and the finite ordinary agreement estimate directly. [Väänänen and Wallisser, J. Number Theory 39 (1991)](https://www.sciencedirect.com/science/article/pii/0022314X9190045D)
