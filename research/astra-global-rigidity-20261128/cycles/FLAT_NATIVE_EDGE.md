# The full sparse asymptotic series for actual low parity types

Retain \(L,t,\kappa,p_0,D,\theta,A_N(p)\) from [the first-arrival count](NATIVE_LOWER_TYPE.md). Write \(p=p_0+Dr/\kappa\). There are absolute \(c,C>0\) such that for each fixed \(\kappa>1\) and every sufficiently small fixed \(r>0\), both the upper and lower ordinary counting exponents lie within
\[
 Cr\exp[-c(\log(1/r))^2]
 \quad\hbox{of}\quad
 J(r)=(1+\theta r)H_2\!\left(\frac{r}{1+\theta r}\right)-r\log_2 3 .
                                                                    \tag{1}
\]
The lower count can be restricted to \(N/2<n\le N\) converging to one. The limits are still large-\(N\) liminf and limsup. The error is smaller than every fixed power of \(r\). In particular the two terms of the earlier theorem extend to the full asymptotic series of the displayed function. Formula (1) is a statement about the original, unstopped parity types. It neither identifies a common rate at a supplied \(r>0\) nor proves the full upper-tail assertion of R6.

## An almost constant positive eigenfunction at long mean inverse gap

Let \(U=\mathbb Z_3^\times\) carry normalized additive Haar measure. For \(s\in(0,1)\), set \(z=1-s\), and on functions define
\[
 (P_sf)(y)=3s\!\sum_{e\ge1:\,I_e(y)\in U} z^{e-1}f(I_e(y)),
 \qquad I_e(y)=(2^ey-1)/3 .
\]
All powers of this positive operator also have their exact ordinary interpretation at every supplied positive odd unit. Only its estimates use the finite ternary classes. The integral of \(P_sf\) equals the integral of \(f\). Indeed for fixed \(e\), the affine map \(x\mapsto2^{-e}(3x+1)\) sends \(U\) injectively into \(U\), with additive Jacobian \(1/3\). This cancels the factor three before summing the normalized geometric law.

If \(f\) is constant on classes modulo \(3^j\), \(j\ge1\), then \(P_sf\) is constant modulo \(3^{j+1}\). For a mean-zero such \(f\), one has the uniform estimate
\[
                        \|P_sf\|_\infty\le (2\cdot3^j)s\|f\|_\infty .  \tag{2}
\]
Put \(B=2\cdot3^j\). The powers of two run through every unit class modulo \(3^{j+1}\) in one period of length \(B\). This follows by induction from \(v_3(4^{3^k}-1)=k+1\) (factor each new difference of cubes). Thus for every supplied \(y\in U\), the legal exponents in a complete period hit each of the \(B/3\) units \(I_e(y)\bmod3^j\) exactly once. In the periodized sum multiply by \(3s/(1-z^B)\). Subtract one from the weights \(z^{e-1}\), because the unweighted sum vanishes. Bounding \(|z^{e-1}-1|\le1-z^{B-1}\le1-z^B\) proves (2) simultaneously for all input classes.

The constant function has \(\|P_s1-1\|_\infty\le Cs\) for small \(s\). The six-term period has two terms with \(z^{e-1}=1+O(s)\), and \(1-z^6=6s+O(s^2)\). Write \(h_m=P_s^m1\), \(d_m=h_{m+1}-h_m\). The mean-zero \(d_m\) has depth at most \(m+2\) and
\[
 \|d_0\|_\infty\le Cs,\qquad
 \|d_{m+1}\|_\infty\le 2\cdot3^{m+2}s\,\|d_m\|_\infty .
\]
Take \(m=\lfloor \frac12\log_3(1/s)\rfloor\). For \(s\) sufficiently small every multiplier up to that index is at most \(18\sqrt{s}<1/2\). Hence
\[
 1-Cs\le h_m\le1+Cs,
 \qquad \|P_sh_m-h_m\|_\infty\le \exp[-c_0(\log(1/s))^2] .
\]
Shrinking \(c_0>0\) gives \(e^{-b_s}h_m\le P_s h_m\le e^{b_s}h_m\), where \(b_s=\exp[-c_0(\log(1/s))^2]\). Positivity and iteration now give
\[
 C^{-1}e^{-q b_s}\le 3^q\Pr_s(\mathcal E_q(y))\le C e^{q b_s}
 \qquad(q\ge1,\ y\in U),                                            \tag{3}
\]
where \(\mathcal E_q(y)\) means that all \(q\) independent geometric-\(s\) gaps give legal successive unit parents from \(y\). The constant is absolute for small \(s\). No infinite-dimensional perturbation or unquantified interchange of cylinder and orbit limits is used. Each legal parent of a positive odd unit is again positive and odd.

## Exact physical count above and below

For an upper bound take \(s=r/(1+\theta r)\), \(z=1-s\), so \(1/s=(1+\theta r)/r\). The last inverse letter from the first-arrival proof may produce a nonunit, costing a bounded factor against the total geometric law after applying (3) to the other \(q-1\) letters. At \(q\le rL+O_\kappa(\log L)\) and total native clock \(h\le L+\theta q+O_\kappa(\log L)\), multiply the weighted count by \(z^{-h}\). Initial binary halvings cost \((1-z)^{-1}\). At this fixed \(r\), polynomial-in-\(L\) factors and fixed constants vanish in the large-\(N\) rate. The resulting bound is
\[
 -\log_2z + r\log_2\!\left(z^{-\theta}\frac{z}{3s}\right)
             +O(rb_s)
 =J(r)+O(rb_s),
\]
since the factor raised to \(q\) exceeds one for small \(s\). This controls the original population, without assuming convergence of its small visited states.

For the lower bound fix the ordinary target \(5\), whose first hit of \(1\) takes four shortcut steps with one odd departure. Every unit inverse word from \(5\) yields a positive odd seed. Its odd path is simple up to its first visit to \(5\), because \(5\) is nonperiodic and the forward path is deterministic. Distinct exponent words of length \(q\) give distinct seeds. Let \(S_q\) be their total valuation. We use the following finite estimate. If \(s'\) is sufficiently small, put \(\delta=\exp[-c_1(\log(1/s'))^2]\), with an absolute \(c_1>0\) sufficiently smaller than \(c_0\). For sufficiently large \(q\) at that fixed \(s'\), uniformly at every ordinary positive unit \(y\),
\[
 \Pr_{s'}\left(\mathcal E_q(y),\ |s'S_q/q-1|\le\delta\right)
                        \ge (2C)^{-1}3^{-q}e^{-q b_{s'}}.            \tag{4}
\]
Indeed change parameter to \(s_\pm=s'/(1\pm\delta)\) on the appropriate tail. The ratio of product probabilities at \(S_q=S\) is
\[
 (s'/s_\pm)^q((1-s')/(1-s_\pm))^{S-q}.
\]
It is largest on that tail at the boundary \(S=q/s_\pm\), with log ratio at most \(-c_2q\delta^2\). For verification define \(u=1\pm\delta\); the boundary log ratio divided by \(q\) is
\[
 l(u)=\log u+(u/s'-1)\log[(1-s')/(1-s'/u)].
\]
It has \(l(1)=l'(1)=0\) and \(l''(u)=-1/[u(u-s')]\) near one. For integer totals use the monotonic ratio and the real boundary. Apply (3) at \(s_\pm\); taking \(c_1\) small makes \(b_{s_\pm}+b_{s'}<c_2\delta^2/2\). The two upper errors are smaller than half the lower bound in (3) when \(q\) is large. This proves (4).

Choose \(s'=s(1+4\eta)\) with \(\eta=\exp[-c_3(\log(1/s))^2]\), \(0<c_3<c_1\). The \(\delta\) of (4) is at most \(\eta\) for all sufficiently small \(s\). Set \(q=\lfloor rL\rfloor-C_4\), where the fixed \(C_4\) handles the one odd departure from \(5\) and endpoint rounding below. The windows in (4) satisfy
\[
 S_q\le (1+\delta)q/s'\le L+\theta q-\log_2 5
\]
for all sufficiently large \(L\) at fixed \(r\), due to the strict relative slack. Each resulting ordinary odd ancestor \(u\) has \(u\le 5\cdot 2^{S_q}3^{-q}\le N\). Lift to \(n=2^{\lfloor\log_2(N/u)\rfloor}u\in(N/2,N]\); distinct odd parts remain distinct. Its first hit time \(h\) at \(1\) satisfies \(h=\log_2 n+\theta(q+1)+O(\log L)\), with the error nonnegative by the first-arrival product. Thus \(h<t\) for all sufficiently small fixed \(r\) and large \(N\). On its exact alternating suffix \(Q_t(n)\le(t-L)/2+D(q+1)+1\le pt\), using a sufficiently large \(C_4\) independent of \(N\).

Dividing (4) by the maximum probability of one word in the window gives, in natural logs per inverse step, a count exponent at least
\[
 -\log3-\log s'-(1/s'-1)\log(1-s')-O(\delta+b_{s'}).
\]
Indeed \(|\log(1-s')|/s'\) is bounded from above. Replacing \(s'\) by \(s\) changes the entropy term by \(O(\eta)\), since its derivative is \(s^{-2}\log(1-s)=O(1/s)\). Multiplying by \(q/L\to r\) and converting to base two gives (1). The argument uses direct bounds on finite, legal, positive inverse paths and their actual forward histories.
