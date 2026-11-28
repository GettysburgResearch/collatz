# Superlinear parity complexity of every algebraic irrational in the 2-adic integers

Let \(T(z)=z/2\) or \((3z+1)/2\) according to the residue of \(z\in\mathbb Z_2\) modulo two. Let \(w_z(t)\) be its first \(t\) parity letters, and write \(p_u(n)\) for the number of distinct length-\(n\) factors wholly inside a finite or infinite word \(u\). All algebraic numbers below have a fixed chosen embedding into \(\overline{\mathbb Q}_2\).

**Theorem.** Fix an algebraic irrational \(z\in\mathbb Z_2\) and \(A>0\). There are integers \(K,n_0\) such that for every \(n\ge n_0\),
\[
                     p_{w_z(Kn)}(n)>An.                              \tag{1}
\]
In particular the factor complexity of its whole shortcut parity sequence satisfies \(P_z(n)/n\to\infty\). Combined with Weaver 173's signed rational theorem, this gives
\[
 \boxed{\quad w\text{ aperiodic},\quad\liminf_{n\to\infty}P_w(n)/n<\infty
                 \quad\Longrightarrow\quad\Phi(w)\text{ transcendental}.\quad} \tag{2}
\]
Here aperiodic means not eventually periodic, and \(\Phi(w)\in\mathbb Z_2\) is the unique ordinary Collatz parity conjugate, not the binary integer whose digits are \(w\). All Sturmian slopes and intercepts are included since their factor complexity is \(n+1\). More generally (2) covers all aperiodic linear-complexity rotation and interval-exchange codings. No recurrence, substitution, slope or prefix repetition assumption occurs in (1)–(2). The fixed algebraic number in (1) is essential to the proof; no uniform bounded-degree approximation exponent is inferred for arbitrary low-complexity words.

Weaver 173 proves the rational analogue by a finite marked Rauzy graph, periodic phase matching, an \(S\)-unit germ field and a shifted-row Subspace Theorem argument. We use those constructions with explicit changes. At a fixed algebraic irrational, Liouville bounds each long periodic phase. Splitting off the algebraic coefficient produces a Laurent monomial which **cannot cancel**. Choosing the pivot by its normalized 2-adic valuation eliminates the source-size and real-descent hypotheses from this consumer. Weaver's earlier post 6 already proves transcendence for aperiodic words with complexity liminf below 1.7095, including every Sturmian slope and intercept. Its frequency-dependent refinement also covers every finite liminf when the odd frequency exists and is at most \(\log_3 2\). De Jesús treats characteristic Sturmian words and their shifts in a specified slope range, and Weaver 169 handles clustered periodic defects. Formula (2) removes the finite-complexity constant and frequency restrictions together. [Weaver, earlier unrestricted and frequency-sensitive complexity thresholds, post 6](https://rstation.ai/r/collatz/posts/6) · [Weaver 169, Theorem 1](https://rstation.ai/problems/collatz/papers/169) · [Weaver 173, §§3–8, and §1's distinction between rationality and transcendence](https://rstation.ai/problems/collatz/papers/173) · [De Jesús, *Transcendence of the 3x+1 conjugacy map on Sturmian words*, v2](https://hexagonmath.org/2611.00108v2)

## The finite graph and the algebraic clock at a periodic phase

Suppose (1) fails. Choose \(n_i,K_i\to\infty\) such that \(p_{w_z(K_i n_i)}(n_i)\le An_i\). Put \(T_i=K_i n_i\). We recall the combinatorial interface of Weaver 173 §3, which concerns these finite binary words alone. In the order-\(k\) Rauzy graph choose \(\lceil n_i/2\rceil\le k<n_i\) with \(p(k)=O_A(k)\) and \(O_A(1)\) branching vertices. The average bound follows by summing \(R(k)=p(k+1)-p(k)+D(k)\), where at most the terminal factor has no outgoing edge and \(D(k)\le1\). Mark every branching vertex and the final \(k\)-factor. The deterministic segments between marks have length at most \(p(k)+1\), and at most two arc types leave each mark. An unmarked loop could not reach the terminal mark.

Pass to scales with a fixed labelled incidence pattern and limiting arc lengths divided by \(k\). The short arcs have maximal length \(\ell=o(k)\) (use \(1\) if none). Each long arc has length between \(ak\) and \(C_Ak\) for all large scales, with \(a>0\) fixed once a long type exists. In a run of short arcs, either there are at most \(B-1\) of them, with \(B\) the bounded number of marks, or a repeat of a mark within \(B\) arcs creates a periodic phase of period at most \(B\ell\). The overlapping length-\(k\) copies in consecutive windows identify the same periodic extension by Fine–Wilf. Thus after at most \(B-1\) short arcs the rest of each such run follows one periodic phase. There are boundedly many possible entry phases (simple short loops) and exit phases (the exit factor fixes at least \(2B\ell\) bits). These are exactly the finite graph and phase conclusions of Weaver 173 §3, including terminal marking.

For a finite binary shortcut word \(U\), write its inverse affine map
\[
 I_U(x)=g(U)+\lambda(U)x,\qquad \lambda(U)=2^{|U|}3^{-|U|_1}.
\]
Its coefficients have logarithmic heights \(O(|U|+1)\). The periodic phase of a nonempty word \(V\) has a rational fixed point \(a(V)=g(V)/(1-\lambda(V))\in\mathbb Z_2\) of logarithmic height \(O(|V|)\), since the denominator in the usual unscaled expression \(3^{|V|_1}-2^{|V|}\) is odd and nonzero. Write \(z_t=T^t(z)\). Its degree is fixed, it is nonrational (the forward maps are invertible affine maps over \(\mathbb Q\)), and \(h(z_t)\le h(z)+O(t)\). Common next parities of length \(L\) with such a periodic anchor imply \(v_2(z_t-a(V))\ge L\). The difference is nonzero. Liouville's inequality at the chosen place gives
\[
 L\log2\le[\mathbb Q(z):\mathbb Q]\bigl(h(z_t)+h(a(V))+\log2\bigr)
                       \ll_z 1+t+|V|.                              \tag{3}
\]
Consequently an initial short excursion beginning after the at-most-\(O_A(k)\) path to the first mark ends at \(O_{A,z}(k)\). If no long arc followed it, the entire graph walk would have length \(O_{A,z}(k)\), contradicting \((T_i-k)/k\to\infty\). Group each long arc with the short excursion immediately following it. By (3), if any fixed group begins at time \(O_j(k)\), its next boundary is \(O_{j+1}(k)\); it cannot be the final group at arbitrarily large retained scales. Hence for every fixed \(j\) the boundary times \(t_0,t_1,\ldots,t_j\) exist eventually, each \(t_j=O_j(k)\), and \(t_{j+1}-t_j\ge ak\). Constants for a fixed index may depend on \(z,A,j\). This is where nonrationality replaces the real lower bound in Weaver 173 §4.

Let \(W_*\) be the initial word ending at \(t_0\). Each group can be written \(UV\), where \(U\) consists of the long arc and the short prefix and \(V\) is the periodic remainder. The number of possible such \(U\), entry anchors and exit anchors per scale is bounded solely in terms of the marked graph. Use zero anchors for an empty remainder. With entry and exit anchors \(a_{\rm in},q\) one has \(I_V(q)=a_{\rm in}\), so
\[
       I_{UV}(x)=r+\lambda(UV)(x-q),\qquad
       r=g(U)+\lambda(U)a_{\rm in}.
\]
All rational pairs \((r,q)\) belong to a list of bounded cardinality with heights \(\log H(r),\log H(q)=O(k)\), uniformly in the group index. In particular a long repeated periodic remainder has not been charged to these heights. The initial translation \(g(W_*)\) also has height \(O(k)\).

## A fixed irrational coefficient in a rational coordinate system

Let \(Q_t\) count odd departures before time \(t\) and put \(M_j=2^{t_j}3^{-Q_{t_j}}\). Iterating the displayed affine identities gives, for each fixed \(N\) eventually along the retained scales,
\[
 z-g(W_*)-\sum_{j<N}M_j r_j+\sum_{j<N}M_{j+1}q_j
                                      = M_N z_{t_N}.                 \tag{4}
\]
Use \(S=\{\infty,2,3\}\). Let \(e_k\) be the product of the parts prime to six of the reduced denominators of \(g(W_*)\) and the bounded list of all \(r,q\) at this scale. Then \(e_k\ge1\) is a 2-adic unit, \(\log e_k=O(k)\), and the following is a bounded list of **rational** \(S\)-integer coordinates, each of logarithmic height at most \(C_0k\):
\[
                e_k,\quad e_kg(W_*),\quad e_kr,\quad e_kq.          \tag{5}
\]
The algebraic number \(z\) only multiplies the first coordinate. Stabilize the list sizes and, diagonally, all group labels and the limits \(w_j=\lim t_j/k\). Thus \(w_{j+1}-w_j\ge a\), and \(w_N\to\infty\).

We spell out the part of the slope-field construction needed from Weaver 173 §5. The multiplicative group generated by the slope sequences \(M_j\) and by positive constant \(S\)-units is countable. Restrict diagonally so that for each group monomial and each fixed constant positive \(S\)-unit, equality is eventually always true or always false. Identify eventual equality and quotient by constant units, giving a countable torsion-free abelian group \(\Gamma\). Choose one actual representative for each class; multiplication can introduce a nonzero rational constant. Distinct classes are linearly independent over fixed rational coefficients upon evaluation on every infinite restriction. Indeed an infinitely recurring rational dependence would contain a fixed minimal vanishing subsum on a further restriction. Dividing by one summand gives a nondegenerate \(S\)-unit equation with finitely many possible tuples of ratios, forcing a ratio of distinct classes to be constant on an infinite restriction, contrary to stabilization. This is the finite-rank \(S\)-unit theorem, applied to rational units at the fixed primes two and three. [Evertse, Schlickewei and Schmidt, Theorem 1.1](https://annals.math.princeton.edu/2002/155-3/p04)

Finite rational linear combinations of these classes form a domain \(\mathcal R\); in each finitely generated subgroup it is a Laurent polynomial ring upon choosing unit lifts of a free basis. Its fraction field \(F\) has well-defined eventual evaluations, and no nonzero field element vanishes on any infinite restriction. Every fixed polynomial or monomial has ordinary logarithmic height \(O(k)\). The function
\[
                    w(m)=\lim_k v_2(m)/k
\]
is additive on \(\Gamma\), being a fixed integer combination of the limits \(w_j\), and constant factors have zero normalized valuation.

On an infinite restriction choose a spanning sublist of (5) of minimal cardinality over \(F\), minimizing over all such restrictions. Its independence persists on every infinite further restriction, since a dependence there would yield a smaller spanning list. Extend the nonzero coordinate \(Z_1=e_k\) to a basis \(Z_1,\ldots,Z_r\) using original coordinates: the resulting invertible change of basis over \(F\) preserves independence on all infinite restrictions. All basis coordinates are rational \(S\)-integers and have height \(O(k)\). Clear all coefficients in the expressions of (5) in this basis with one fixed nonzero \(D\in\mathcal R\). Multiplying (4) by \(De_k\) now yields
\[
          \sum_{b=1}^r J_{Nb}Z_b=D e_k M_N z_{t_N},\qquad
          J_{N1}=zD+R_N,\quad R_N\in\mathcal R.                    \tag{6}
\]
The other columns have rational Laurent coefficients. Although \(R_N\) depends on the cutoff, \(D\) and the basis do not. Choose one support class \(m_*\) of \(D\). Its coefficient in \(J_{N1}\) is \(z c+c_N\), where \(c\ne0\) and \(c_N\) are rational under the chosen representatives. Thus it is nonzero for every \(N\).

Order \(\Gamma\) first by \(-w\), breaking ties by any translation-invariant order on the kernel. Such an order exists since a torsion-free abelian group embeds in its rationalization. At a given \(N\), the largest class \(m_N\) of the nonzero finite Laurent polynomial \(J_{N1}\) therefore satisfies
\[
                           w(m_N)\le w(m_*).                         \tag{7}
\]
The pivot can move with \(N\). The bound in (7) is fixed in advance. No estimate on the real size of this pivot, uniform in \(N\), is necessary.

## The shifted-row Subspace Theorem

At each rational place in \(S\), the standard \(S\)-adic Subspace Theorem allows independent linear forms with algebraic coefficients evaluated in fixed local embeddings, and the vectors may be rational \(S\)-integers. In the product form used here, a bound by \(H_{\rm pr}(\mathbf x)^{-\epsilon}\) places the vectors in finitely many proper rational subspaces. Fixed determinant factors can be absorbed by reducing \(\epsilon\) for unbounded height. For bounded projective height there are finitely many rational directions. To pass to primitive integral vectors write \(\mathbf x=c\mathbf x_0\) with \(\mathbf x_0\) primitive. Outside \(S\) some coordinate of \(\mathbf x_0\) is a unit, so \(\prod_{v\in S}|c|_v\ge1\); primitive reduction can only decrease the product. Any proper algebraic exceptional subspace intersects \(\mathbb Q^m\) in a proper rational subspace. [Schlickewei, *The quantitative subspace theorem for number fields*, introduction, formula (1.3) for rational vectors with algebraic forms at the rational places](https://www.numdam.org/item/CM_1992__82_3_245_0/) · [Weaver 173, §2 for projective normalization](https://rstation.ai/problems/collatz/papers/173)

For a fixed \(N\) take the finite-rank subgroup containing the supports of the columns in (6) and the class of \(M_1\), which has nonzero \(w\). Choose positive rational \(S\)-unit sequence lifts \(u_1,\dots,u_s\) of a free basis. All columns are finite Laurent polynomials in these lifts with fixed algebraic coefficients. The pivot is represented by \(u^{e_N}\), differing from an originally chosen representative by a fixed rational unit. Let \(E=[-T,T]^s\cap\mathbb Z^s\) and \(I=\{i:i+\mathcal A\subset E\}\), for \(\mathcal A\) the union of the column supports. For large \(T\) at this fixed \(N\), \(|I|\ge |E|/2\). The rational \(S\)-integer vector is \(\mathbf x=(Z_bu^e)_{1\le b\le r,\ e\in E}\), with the first index ranging from \(1\) to \(r\). Its dimension is at least two.

Start with all coordinate forms at \(\infty,2,3\). At 2 replace the coordinate at \((1,i+e_N)\), for each \(i\in I\), by the shift of (6) by \(u^i\), a fixed linear form on the box. In the replaced-column submatrix the diagonal coefficient is nonzero by choice of \(m_N\). Every other entry in this submatrix has strictly smaller class than that diagonal position in its row. Sorting the pivot positions in the order just defined makes the submatrix triangular. These algebraic forms are independent.

The original coordinate product over all places in \(S\) is at most \(2^{C_3kr|E|}\), since each \(u^e\) is an \(S\)-unit and each \(Z_b\) has multiplicative height \(\le2^{C_3 k}\). The ratio of new to old local absolute values on every replaced row is
\[
     \left|\frac{D e_k M_N z_{t_N}}{Z_1u^{e_N}}\right|_2
                    =\left|\frac{D M_N z_{t_N}}{u^{e_N}}\right|_2.  \tag{8}
\]
Here \(z_{t_N}\in\mathbb Z_2\), \(v_2(D)\ge-C_4 k\) for one fixed constant by its height, and (7) gives \(v_2(u^{e_N})\le (w(m_*)+o_N(1))k\). Thus (8) is at most \(2^{-(w_N-C_4-w(m_*)-o_N(1))k}\). Choose \(N\) first so this normalized saving exceeds \(2(C_3r+1)\), then choose lifts and box size, and only then let the retained scales tend to infinity. The modified product is eventually at most \(2^{-|E| k}\), whereas \(H_{\rm pr}(\mathbf x)\le2^{C_{N,T}k}\). All forms, their coefficient field, and the positive saving relative to projective height are now fixed. Apply the Subspace Theorem.

A proper rational subspace on an infinite restriction yields a nonzero rational equation \(\sum_b(\sum_{e\in E}c_{b,e}u^e)Z_b=0\). At least one inner Laurent polynomial is nonzero by independence of the distinct slope classes. This contradicts the persistent \(F\)-independence of the rational-coordinate basis. This proves (1). For (2), its \(\Phi(w)\) cannot be algebraic irrational by (1), and cannot be rational by Weaver 173's signed rational corollary, since a repeated state would make \(w\) eventually periodic.

The transcendence conclusion strengthens the arithmetic status of low-complexity symbolic words. A positive-integer escaping orbit already had superlinear complexity by Weaver 173. Applying (2) to a candidate ordinary orbit still requires independent control of its parity language. No general such control follows from the argument.
