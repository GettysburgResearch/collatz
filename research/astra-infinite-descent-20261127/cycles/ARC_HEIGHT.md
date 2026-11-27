# Effective height constraints on arbitrary arc partitions

Let a primitive positive rational shortcut orbit have length \(h\), \(p>0\) odd letters and reduced denominator \(q\). Its determinant is \(D=2^h-3^p>0\). Put \(\rho=3^p/2^h\), \(\Delta=1-\rho\), \(\gamma=\log_2 3\), and \(c=\gamma-1\). Every point of the orbit has denominator \(q\). Indeed \(q\mid D\), so \(q\) is coprime to six, and neither shortcut branch changes a reduced odd denominator coprime to three.

Partition the entire circular word into \(r\ge2\) nonempty consecutive arcs of lengths \(L_j\), odd counts \(P_j\), and actual initial values \(x_j\). Each arc is proper. Let \(s_j=u_j/v_j\) be the affine fixed point of the **arc by itself**, with \(v_j>0\) and the fraction reduced. The fixed point exists since \(2^{L_j}\ne3^{P_j}\). Signed centers, including the pure even center \(0\) and pure odd center \(-1\), are allowed. Every \(x_j\ne s_j\). Equality would return a deterministic physical state after \(L_j<h\) ordinary shortcut steps, contradicting the least period. For \(H=\max_j\max(|u_j|,v_j)\), the following inequalities are effective and uniform in the number of arcs, their lengths and their internal words.

\[
 \boxed{\quad \Delta\ \le\
     q\sum_{j=1}^r \frac{v_j|s_j-s_{j-1}|}{2^{L_j}}\quad}                 \tag{1}
\]

\[
 \boxed{\quad q\ \ge\
   \frac{\Delta}{(2r+1)H^2}\,2^{\,c h/(\gamma^r-1)}.\quad}              \tag{2}
\]

The first bound also gives \(q\ge \Delta 2^{\min L_j}/(2rH^2)\). This can exceed (2) when the lengths are comparable. Bound (2) applies to very unequal partitions and involves no unspecified exceptional set. All powers and rational quantities in (1) are exactly computable from the printed word.

## The transport, lattice and variation

In fact use any rational **reference trajectory** for each arc, with prescribed starting and ending values \(\xi_j = u_j/v_j,\ \eta_j=w_j/v_j\) and a common denominator \(v_j>0\) for those two endpoints. Reduction is optional. The trajectory must obey that arc's affine law, and \(\xi_j\ne x_j\) is required for each arc. This is an exact hypothesis on separately chosen references and follows automatically for the arc's own center. Set \(H=\max_j\max(|u_j|,|w_j|,v_j)\). In (1) replace \(|s_j-s_{j-1}|\) by \(|\xi_j-\eta_{j-1}|\). Bound (2) still holds.

At each arc
\[
 2^{L_j}qv_j(x_{j+1}-\eta_j)
   =3^{P_j}qv_j(x_j-\xi_j).
\]
Both scaled differences are nonzero integers. The powers of two and three are coprime, including \(P_j=0\). Thus \(qv_j(x_j-\xi_j)=2^{L_j}k_j\) and \(qv_j(x_{j+1}-\eta_j)=3^{P_j} k_j\) for a nonzero integer \(k_j\). Multiplying the transport ratios and changing cyclic indices gives
\[
  \rho
  =\prod_j\frac{x_j-\eta_{j-1}}{x_j-\xi_j}
  =\prod_j(1+e_j),\qquad
  e_j=\frac{\xi_j-\eta_{j-1}}{x_j-\xi_j}.
\]
If \(\sum_j|e_j|\ge1\), then \(1-\rho\le\sum_j|e_j|\) immediately. Otherwise each factor is positive, and
\(\prod(1+e_j)\ge\prod(1-|e_j|)\ge 1-\sum |e_j|\), by induction. The divisibility bound on \(x_j-\xi_j\) proves (1). This calculation tolerates negative errors and endpoint sign changes.

At an interface the same identities give a system of coupled integer equations
\[
 v_{j-1}2^{L_j}k_j-v_j3^{P_{j-1}}k_{j-1}
   =q(v_j w_{j-1}-v_{j-1}u_j).
\]
The actual assignments of the reference numerators \(u_j,w_j\) matter. Choosing a reference identical to the physical trace would give \(k_j=0\) and invalidate (1).

## Traversing from a small boundary value

Let \(M=\min_j x_j\). If \(M>H\), the factors above are positive and
\[
 \rho \ge ((M-H)/(M+H))^r
       \ge 1-2rH/(M+H).
\]
The second step is Bernoulli's inequality. This proves \(M\le 2rH/\Delta\), which also holds if \(M\le H\).

Start at a boundary attaining \(M\) and write \(S_j\) for elapsed shortcut time just before arc \(j\). On positive inputs either shortcut branch satisfies \(T(x)+1\le(3/2)(x+1)\). From the nonzero integer \(k_j\) it follows that
\[
 2^{L_j}\le qv_j|x_j-\xi_j|
       \le qH(x_j+1)\le qH(M+1)(3/2)^{S_j}.
\]
Consequently \(S_{j+1}\le\gamma S_j+B\), with \(B=\log_2(qH(M+1))\). Since \(S_1=0\),
\(h\le B(\gamma^r-1)/c\). Use \(M+1\le(2r+1)H/\Delta\) to obtain (2).

The standard effective lower bound for the nonzero linear form \(h\log 2-p\log 3\) yields \(-\log_2\Delta=O(\log(2h))\) for \(0\le p\le h\). Concretely one can apply Matveev's theorem for two fixed algebraic numbers to \(|2^{-h}3^p-1|\). The exact bounds (1) and (2) need no transcendence estimate. For \(q=1\), (2) gives
\[
 r\ \ge\ \log_\gamma\!\left(1+
  \frac{c h}{2\log_2 H+\log_2(2r+1)-\log_2\Delta}\right).
\]
It imposes a logarithmically growing count on covers with bounded or polynomial endpoint height. For arbitrary words \(W=U_1^{n_1}\cdots U_r^{n_r}\), possibly changing with \(h\), choose the individual motif fixed points. If \(|U_j|\le d\), then \(H\le3^d\). To see this, the carry of a word of length \(d\) is maximized by the all-one word, whose carry is \(3^d-2^d\), and \(|2^d-3^p|\le3^d\). Each arc is a power of its motif and therefore shares its center. For \(r\ge2\) properness ensures separation. For \(r=1\) a primitive word equal to a pure motif power has \(n_1=1\), hence \(h\le d\).

This covers motifs with arbitrarily many internal odd runs. Classical fixed-run integer \(m\)-cycle finiteness and estimates exponential in the number of local minima are due to Simons and de Weger. Their stronger specialized estimates remain relevant for the dictionary consisting of pure odd and even runs. The translation to arbitrary rational reference fragments, weighted variation at each interface, and the denominator \(q\) are the claims here. A primitive positive integer trajectory can still have many pieces or large required reference heights. These constraints leave that case open. [Simons and de Weger, *Acta Arithmetica* 117 (2005)](https://doi.org/10.4064/aa117-1-3)

[ArcHeight.lean](ArcHeight.lean) kernel-checks the coprimality gap, exact telescoping, individual error estimate and weighted inequality (1) for a general physical trace with arbitrary rational reference endpoints. The common denominator is absorbed into the integer physical coordinates. The Lean trace takes each arc's scaled transport and nonzero starting separation as hypotheses. The derivation of these hypotheses from an arbitrary native rational cycle and its least period is the written argument above. The final order estimate (2) is proved above. The finite controls use rational arithmetic on actual shortcut cycles.
