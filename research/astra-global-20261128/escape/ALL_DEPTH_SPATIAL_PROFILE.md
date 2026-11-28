# The original finite rows at arbitrary simultaneous depth and height

**Status.** Written deductions from the actual ordinary canonical inverse path, the preceding uniform spatial theorem, and the stationary limits at fixed ordinary roots. Every finite measure below uses the real intercept of its own inverse word. Constants and onset heights inherited from the limiting trace can be ineffective.

Use the notation and the three source interfaces of [the stationary spatial theorem](SPATIAL_TRACE_TAIL.md). At a positive odd target define the finite positive measure on complementary relative marks by
\[
 P_{d,y} = y^{-1}(R\mapsto 1-R/y)_*M_{d,y},\qquad
 P_{d,y}([0,1])=\rho_{d+1}(y)/y .
\]
At a positive-trace unit set \(g(x)=\rho_1(x)/h(x)\). Set \(g=0\) on nonunits, whose initial rows vanish. The positive-trace theorem gives \(0\le g\le G=2/\alpha_0<\infty\) on ordinary sites. Let \(X_j\) be the canonical reverse path from \(X_0=y\) and \(b_d(x)\) the survival from \(x\) through its first \(d\) odd steps. The probability of the elementary reverse cylinder to \(x\), with \(U^dx=y\), is \(a_x b_d(x)/a_y\). The actual real intercept satisfies \(1-R/y=b_d(x)\) on this cylinder. Consequently
\[
    P_{d,y}= a_y\,\mathbb E_y[g(X_d)\,\delta_{b_d(X_d)}],
       \qquad P_{d,y}([0,1])\le G a_y.                           \tag{1}
\]
This follows by telescoping the harmonic branch probabilities, or by multiplying the original word coefficient by \(1/y\). Its mass is \(\rho_1(x)b_d(x)/x\). Sources with zero initial weight can be omitted. The stationary row is \(a_y\nu_y\). [Canonical inverse paths, PR193](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) · [Marked real law, PR193](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md).

## Finite entrance times

Fix a height floor \(M\). At sufficiently high nonperiodic \(y\), use the finite set of last low paths \(m\in E_M(y)\) from [the spatial theorem, (1)–(2)](SPATIAL_TRACE_TAIL.md). Write \(k=k_m\), \(b=b_k(m)\) in the summand below. At every depth \(d\), the actual row is the sum of
\[
 \sum_{m:\, k\le d} b (D_b)_*P_{d-k,m}
 +\sum_{m:\, k>d} a_m b\,g(U^{k-d}m)\,\delta_{b_d(U^{k-d}m)}
                                                                    \tag{2}
\]
and a positive residual of mass at most \(GC M^{-\sigma}\), uniformly in \(d\). Indeed the first reverse visit to the low set at \(m\) has probability \(a_m b/a_y\). Conditional on this event, the path back through time \(k\) is predetermined and the remaining inverse path has the canonical law from \(m\). This gives each of the two contributions in (2) by (1). The omitted path event has probability at most \(C M^{-\sigma}/a_y\) from stationary spatial (2). On targets with no low ancestor the same argument gives the full upper bound, with an empty sum.

For measures on \([0,1]\) write \(\|\mu\|_K=\sup_t|\mu([0,t])|\). Let
\[
   \Delta_M(L)=\max_{m\le M,\,a_m>0}
     \sup_{j\ge L}\| P_{j,m}/a_m-\nu_m\|_K .
\]
This tends to zero for fixed \(M\) by [the original full-threshold convergence](SUMMABLE_ORIGINAL_TRACE.md). At all sufficiently high nonperiodic \(y\) for which \(d\ge L+\max_{m\in E_M(y)} k_m\),
\[
   \|P_{d,y}-a_y\nu_y\|_K
        \le (1+G)CM^{-\sigma}+\kappa\Delta_M(L).                    \tag{3}
\]
For an empty set use maximum zero. Subtract the stationary last-low expansion and use \(\sum_m a_m b_{k_m}(m)\le a_y\le\kappa\); dilations preserve the cumulative seminorm. This is a late-depth estimate in the actual odd entrance times. Along the escaping rays meeting the low set, those entrance times differ by fixed integer offsets after the finite set of merge vertices.

## The real moving profile

For each escaping component choose the bilateral grade-zero origin at its selected ray \(r_C=(r_n)_{n\ge0}\). The finite positive measures
\[
    \Gamma_{C,v}=H_C\mathbb E_C[g(Z_v)\,\delta_{F(Z_v)}]
       =\sum_{\substack{x\in C\ {\rm unit}\\{\rm grade}_C(x)=v}}
                      \frac{\rho_1(x)F(x)}{x}\,\delta_{F(x)}
          \quad(v\in\mathbb Z)                                      \tag{4}
\]
have mass at most \(G H_C\). The marginal identity giving the second equality is restricted to this single grade. Set \(s_y=F(y)\) if \(y\) escapes, and \(s_y=1\) otherwise. The whole finite trace satisfies
\[
 \boxed{\;
   \lim_{Y\to\infty}\sup_{y\ge Y\ {\rm odd},\ d\ge0}
   \left\|\tau_y s_y(D_{s_y})_*P_{d,y}
       -\sum_{C,n:\ r_n=y}\Gamma_{C,n-d}\right\|_{\rm TV}=0 .\;}     \tag{5}
\]
Here the variation norm of a positive measure is its mass. To prove (5), fix \(y=r_n\) and set \(A_n=\{Z_n=r_n\}\). Conditioning (1) on \(A_n\) gives the exact submeasure identity
\[
 F(y)(D_{F(y)})_*P_{d,y}
  = H_C \mathbb E_C[g(Z_{n-d})\,\delta_{F(Z_{n-d})}\,1_{A_n}].       \tag{6}
\]
Indeed \(F(Z_{n-d})=b_d(Z_{n-d})F(y)\) on this event. Its probability times \(H_C\) is \(a_y F(y)\). The difference between (4) and (6) is positive of mass at most \(G H_C\Pr_C(A_n^c)\) at every depth. This tends to zero uniformly in \(d\) on each single ray. For the supremum over targets, there are finitely many charges above any positive threshold. The tails of their selected rays have just been covered, and (6) bounds the error on any remaining selected ray by \(G H_C\). At large sites off all selected rays the stationary spatial theorem (6) gives \(\tau_y a_y=o(1)\) uniformly. Equation (1) proves (5).

At the forward end,
\[
       \|\Gamma_{C,v}\|_{\rm TV}\longrightarrow0\quad(v\to+\infty).
                                                                    \tag{7}
\]
Almost every bilateral path eventually joins the selected ray. On it, \(a_{r_v}\to H_C>0\), and \(r_v\to\infty\), whence \(g(r_v)\to0\). Dominated convergence applies. At the backward end,
\[
       \|\Gamma_{C,v}-H_C\eta_C\|_K\longrightarrow0\quad(v\to-\infty).
                                                                    \tag{8}
\]
On the bilateral path \(F(Z_v)\to J\) as \(v\to-\infty\). Test first against a continuous function \(f\) on \([0,1]\), replacing \(f(F(Z_v))\) by \(f(F(Z_{-k}))\) for fixed \(k\). The limiting error is bounded by \(G\mathbb E|f(J)-f(F(Z_{-k}))|\), which tends to zero as \(k\to\infty\). Conditional on \(Z_{-k}=z\), \(\mathbb E[g(Z_v)\mid z]=\rho_{1-k-v}(z)/h(z)\to1\) by the fixed-root trace limit, and is bounded by \(G\). Hence the weak limit is \(H_C\eta_C\). The law \(\eta_C\) is atomless since its conditional laws given \(Z_0\) are dilations of atomless ordinary fibres. Compactness and a finite grid for its cumulative distribution give (8).

For different grades of the same component, the purely atomic measures in (4) have disjoint supporting countable sets. If two positive odd units \(x,x'\) merge at \(z\) after \(i,j\) steps of respective division clocks \(s,s'\), equality of \(F(x),F(x')\) implies \(3^i2^{-s}x=3^j2^{-s'}x'\). Cancelling the two-adic valuation yields \(s=s'\); cancelling the three-adic valuation yields \(i=j\) and then \(x=x'\). Thus every atom is an individual ordinary source. In particular (8) cannot be upgraded to convergence in variation norm in an escaping component. The positive limit is atomless while each approximant is countably supported.

## Uniformity and its obstruction

Let the positive-part stationary shortfall be
\[
   V_d=\sup_{y\ {\rm odd},\ t\in[0,1]}
            \tau_y\bigl(a_y\nu_y([0,t])-P_{d,y}([0,t])\bigr)_+ .
\]
Then
\[
          \lim_{d\to\infty}V_d=\sup_C H_C,                           \tag{9}
\]
with zero for an empty family; a positive supremum is attained. For fixed \(d\), \(\rho_{d+1}\) is bounded by its finite ternary period, so along each escaping ray the finite normalized row tends to zero. Taking \(t=1\) gives \(V_d\ge H_C\). At large heights the stationary spatial theorem bounds every shortfall by \(\sup_C H_C+o(1)\), uniformly in depth. On each finite remaining set of heights the full-threshold convergence makes every shortfall tend to zero. This proves (9). Two-sided uniform convergence in \(K\) is equivalent to absence of escaping components: the reverse implication follows from (1) and the uniform spatial classification at large heights, plus fixed-target convergence at bounded heights.

## A depth bound using only physical height

Put \(q=3/2\), \(B=1+\log_2 q=\log_2 3\) and \(\gamma=\log 2/\log B\). The original rows vanish in the following height region, uniformly over all positive odd targets and all depths:
\[
 \boxed{\quad
  \lim_{A\to\infty}\ 
   \sup_{\substack{d\ge0,\,y\ {\rm positive\ odd}\\
                    y\ge A q^d/(1+d)^\gamma}}
       \tau_y\,\rho_{d+1}(y)/y=0 .\quad}                               \tag{10}
\]
The scale includes a polynomial saving over the pointwise growth factor per odd step. No stopping time or future-component membership appears in the tested region.

We first give a deterministic estimate on any fixed escaping positive odd orbit \(r_i=U^i r_0\). Write \(e_i=v_2(3r_i+1)\) and let \(J_n\) count the indices \(0\le i<n\) with \(e_i\ge2\). A consecutive run of \(e_i=1\) of length \(\ell\) beginning at index \(s\) requires \(2^\ell\mid r_s+1\), since \(r_{s+\ell}+1=(3/2)^\ell(r_s+1)\). Every step satisfies \(r_{j+1}+1\le q(r_j+1)\). Hence this run has length at most \(L+s\log_2 q\) with \(L=\log_2(r_0+1)\). Starting a new run immediately after each of the \(J_n\) exceptional steps gives indices obeying \(s'\le Bs+L+1\), starting at zero; the final run may be incomplete. Iteration gives
\[
       n+1\le C_{r_0} B^{J_n},\qquad
       2^{-J_n}\le C'_{r_0}(1+n)^{-\gamma}.
\]
The exact product formula and the uniform survival lower bound for simple ordinary paths give
\[
        r_n= r_0 q^n\,2^{-\sum_{i<n}(e_i-1)}/b_n(r_0)
           \le C''_{r_0}q^n(1+n)^{-\gamma}.                            \tag{11}
\]
The run-length argument and the exponent $\gamma$ in (11) were already proved in [PR193, stopped-rate test, derivation of (2)](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/STOPPED_RATE_TEST.md). Here they enter the all-target finite-row estimate (10).

Consider a sequence in (10) with \(A\to\infty\). Its heights tend to infinity since \(q^d/(1+d)^\gamma\) has a positive minimum. By (5) and (4), only the finitely many selected rays of charge greater than any given small positive threshold can have appreciable normalized mass; \(s_y\) has the uniform lower bound \(c_0\) on escaping targets. On any such fixed ray, \(y=r_n\to\infty\). If \(n-d\) is bounded above, (11) makes \(y(1+d)^\gamma/q^d\) bounded: for \(d\ge n\) use \(q^{-(d-n)}(1+d-n)^\gamma=O(1)\), and the finitely bounded positive differences are harmless. Hence \(n-d\to+\infty\). The front mass tends to zero by (7), proving (10).

One also obtains a late-depth region at simultaneous record heights. Fix \(M\) and a physical upper bound \(P\) on the heights of all the last-low segments in (2), including their endpoints. Each segment is simple. Elementary ordinary path packing gives \(k_m\le 12P^{49/50}\), uniformly in its length and root, by applying the bound to its shortcut expansion and counting its odd departures. If intermediate even highs exceed \(P\), this causes no difficulty: the packing theorem counts the number of states *below* \(P\) on any simple shortcut path, whose total height is unrestricted. Formula (3) applies as soon as \(d\ge L+12P^{49/50}\). On a fixed escaping component meeting the low set, the finitely many low forward orbits share one tail; at every sufficiently late record height \(y\) of that tail one can take \(P=y\) for all the segments. This bounds the late depth at those record heights using physical height alone. The early and late estimates still allow the positive profile (4) at intermediate depths. [Elementary simple-path packing, PR212](../../astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md).

The fixed-source sparse-break theorem also allows **any** fixed power in place of \(\gamma\) in (10). In its shortcut coding every even step between the first \(n\) positive odd departures contributes to \(S_n-n\). The all-positive-source Subspace Theorem bound gives \((S_n-n)/\log n\to\infty\): if the factor \(S_n/n\) is large the assertion is immediate, while otherwise the count of even shortcut steps through \(S_n\) grows faster than \(\log S_n\). The product formula used in (11) gives \(r_n\ll_{C,B}(3/2)^n(1+n)^{-B}\) for each fixed \(B\). The proof of (10) then goes through unchanged. This is the stronger original-row height region; the arithmetic input on one fixed ordinary trajectory is prior. [Fixed-source sparse approximation proof](../broad/SPARSE_APPROXIMATION.md) · [PR193, stopped-rate test, including the stronger source-qualified rise-group bound](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/STOPPED_RATE_TEST.md).
