# All-orders first-hit asymptotics near the fastest shortcut clock

Let \(T\) be the positive shortcut map, \(\theta=\log_2 3\), \(y\) a positive odd ternary unit, \(L=\log_2(X/y)\), and \(a_y(X,k)\) the number of \(X\le n<2X\) whose first visit to \(y\) occurs at shortcut time \(k\). The elementary integer alphabet already gives the first two terms of this count. [Two-term argument](../phase5/FAST_CLOCK_EDGE.md)

**Theorem.** Take \(B=20\) and put
\[
 R_y(L,\delta)=\frac1L\log_2\max_{|k-(1+\delta)L|\le B} a_y(X,k),
 \qquad
 J(\delta)=(1+\delta)H_2\!\left(\frac{\delta}{(1+\delta)\theta}\right)
                   -\frac{\delta}{\theta}\log_2 3.
\]
Here \(H_2\) is binary entropy. For every \(c<1/(4\ln3)\) with \(c>0\) there exist \(C_c,\delta_c>0\) such that for each fixed \(0<\delta<\delta_c\),
\[
 \limsup_{L\to\infty}\ \sup_y
       |R_y(L,\delta)-J(\delta)|
       \ \le\ C_c\exp\{-c(\ln(1/\delta))^2\}.                       \tag{1}
\]
The supremum couples each target with its own shell \(X=2^L y\). Thus the integer count agrees with the ternary-filtered binomial exponent to every algebraic order in the excess clock after the scale limit. The statement concerns a bounded window of exact first-hit clocks. It neither identifies a limit for a fixed nonzero \(\delta\) nor makes an independence assumption on inverse exponent congruences.

## The finite ternary correction

Let \(U=\mathbb Z_3^\times\) with normalized Haar probability. Use natural logarithms in this section. For \(t>0\) define the positive operator
\[
 A_t f(z)=3(e^t-1)\sum_{\substack{e\ge1\\ x=(2^ez-1)/3\in U}}e^{-te}f(x),
 \qquad \lambda(t)=\frac{1}{3(e^t-1)}.                              \tag{2}
\]
For positive odd integer roots all admitted \(x\) are positive odd integers at their exact inverse time \(e\). On \(3\)-adic units, \(A_t\) preserves the Haar integral. Indeed the inverse substitution \(z=2^{-e}(3x+1)\) has Jacobian \(1/3\), with image in \(U\), and \((e^t-1)\sum_{e\ge1} e^{-te}=1\).

If \(f\) is constant on residues modulo \(3^m\), \(m\ge1\), then \(A_tf\) is constant on residues modulo \(3^{m+1}\). Write \(P_m=2\cdot3^m\), the order of two modulo \(3^{m+1}\). For fixed \(z\), as \(e\) traverses one period, every unit child class modulo \(3^m\) occurs exactly once. This follows by solving \(2^ez\equiv3x+1\pmod {3^{m+1}}\). Hence the coefficient for each child in the finite action is
\[
 3(e^t-1)e^{-t r}/(1-e^{-tP_m}),\qquad 1\le r\le P_m .
\]
There are \(P_m/3\) child classes. If \(tP_m\le1\), all coefficients equal \((3/P_m)(1+O(tP_m))\) with an absolute implied constant. Thus a zero-mean cylinder function satisfies
\[
        \|A_t f\|_\infty\le C t P_m\|f\|_\infty.                    \tag{3}
\]
In particular \(A_t1-1\) has mean zero, modulus nine and norm \(O(t)\).

Set \(h_m=A_t^m1\), \(b_0=A_t1-1\), \(b_j=A_t^j b_0\). Each \(b_j\) has mean zero and modulus \(3^{j+2}\). Iterating (3) gives
\[
 \|b_j\|_\infty\le Ct(C't)^j\,3^{j(j+3)/2}                         \tag{4}
\]
as long as the moduli used satisfy \(2t3^{j+1}\le1\). Choose \(m=\lfloor \ln(1/t)/\ln3\rfloor-K\), with one sufficiently large absolute \(K\) and \(t\) small enough that \(m\ge1\). Each successive multiplier from (3) through this depth is at most \(1/2\). Thus \(h_m=1+\sum_{j<m}b_j=1+O(t)\) uniformly. With \(h=h_m\), (4) gives
\[
 \left|\ln(A_th(z)/h(z))\right|\le\eta(t),\qquad
 \eta(t)\le \exp\!\left\{-\frac{\ln^2(1/t)}{2\ln3}
                               +O(\ln(1/t))\right\}.                 \tag{5}
\]
This is a finite cylinder correction, allowed to depend on \(t\). Alternatively, retaining any fixed \(m\) yields relative error \(O_m(t^{m+1})\). No limit of the functions \(h_m\) as \(m\to\infty\) is needed.

Write \(Z_j(t,z)=\sum_w e^{-t S(w)}\), summed over all \(j\)-letter legal unit words from \(z\), where \(S(w)\) is their total exponent. By (2), \(Z_j=\lambda(t)^j A_t^j1\). Positivity and (5) give for all \(j,z\),
\[
 \tfrac12\lambda(t)^j e^{-j\eta(t)}
       \le Z_j(t,z)\le 2\lambda(t)^j e^{j\eta(t)}.                  \tag{6}
\]
Here and below \(t\) is sufficiently small that \(\sup h/\inf h\le2\). The estimate controls every integer starting residue, with an exponential-in-depth error whose rate is flat at \(t=0\).

## A family of paths with bounded prefix offsets

Use the actual probability of each transition
\[
 P_t(z,e)=\frac{e^{-te}h(x)}{\lambda(t)A_th(z)},\qquad
              x=(2^ez-1)/3\in U .
\]
The denominator is the sum of its numerator over all eligible \(e\). For any word of length \(j\) from the supplied vertex, the product law obeys
\[
 \tfrac12 e^{-tS}\lambda(t)^{-j}e^{-j\eta(t)}
 \le P_t(w)\le
 2e^{-tS}\lambda(t)^{-j}e^{j\eta(t)}.                              \tag{7}
\]
This follows by telescoping the factors \(h(x)/h(z)\); no independence of letters is used. In particular for all \(|s|<t/2\), by (6) at \(t-s\),
\[
 \mathbb E_t e^{sS_j}
 \le 4\exp\{j[\ln\lambda(t-s)-\ln\lambda(t)
                      +\eta(t-s)+\eta(t)]\}.                        \tag{8}
\]

There is a positive absolute probability, uniformly in the path length, that every prefix satisfies \(S_i\ge(\theta+1)i\). Indeed, conditionally on any past, \(\mathbb E_t(e^{-e_i}\mid\text{past})\le Ct\) since the numerator is bounded by \(2\sum_{e\ge1}e^{-e}\) and the denominator is \(\gg1/t\). Thus the probability of a violation at \(i\) is at most \((e^{\theta+1}Ct)^i\). For all sufficiently small \(t\) the sum over \(i\ge1\) is less than \(1/4\).

For such a prefix, \(Q_i=2^{S_i}/3^i\ge2^i\) and the positive ordinary state reached in inverse order from a prepared integer \(Y>100y\) is
\[
             z_i=Q_i\left(Y-\tfrac13\sum_{\ell=1}^i Q_\ell^{-1}\right)>Y.
\]
The total correction inside parentheses is at most \(1/3\). This condition permits small individual valuations, including \(e_i=1\), while controlling the full real orbit.

## Concentration at the count budget

Put \(\rho=\delta/\theta\), \(E_0=(1+\delta)/\rho\), and let \(t_0=-\ln(1-1/E_0)\). Then \(E(t)=-(\ln\lambda)'(t)=1/(1-e^{-t})\) satisfies \(E(t_0)=E_0\) and \(t_0\asymp\delta\). Fix \(c<c'<1/(4\ln3)\) with \(c>0\) and set \(b=\exp[-c'\ln^2(1/t_0)]\). By (5), uniformly for \(t'\in[t_0/2,2t_0]\),
\[
                         \eta(t')=o(b^2).                            \tag{9}
\]
Use the slightly stronger tilt \(t=t_0(1+b)\). For small \(t_0\), \(b/(2t_0)\le E_0-E(t)\le2b/t_0\), by differentiating \(E\). Also \((\ln\lambda)''(t')\le C/t_0^2\) throughout that interval. Apply (8) with \(s=\pm\kappa b t_0\) where \(\kappa>0\) is a sufficiently small fixed constant. Markov's inequality, Taylor's formula and (9) give
\[
 \Pr_t\!\left(\left|S_j/j-E(t)\right|>b/(4t_0)\right)
                         \le 8e^{-c_1 b^2j}
\]
for an absolute \(c_1>0\) and all sufficiently small \(t_0\) (depending on \(c'\)). Consequently at least half the probability, for \(j\) sufficiently large depending only on \(\delta,c'\), belongs to paths satisfying the complete prefix condition above and
\[
              j(E_0-3b/t_0)\le S_j\le j(E_0-b/(4t_0)).             \tag{10}
\]

Prepare \(Y\asymp y\) as in the elementary proof, and take \(j=\lfloor\rho L\rfloor\). For fixed \(\delta\) and all large \(L\), the upper end of (10) is at most \(\log_2(X/Y)+j\theta\): \(j(E_0-\theta)\le L\) and the strict spare term \(jb/(4t_0)\) eventually exceeds the bounded prep cost. Hence every such odd word gives a distinct endpoint \(z_j\le X\). Its least dyadic lift into \([X,2X)\) has first clock as in the two-term proof,
\[
 e_0+\left\lceil\log_2(X/Y)+j\theta
                  -\log_2\!\left(1-\frac1{3Y}\sum_{\ell=1}^jQ_\ell^{-1}\right)\right\rceil .
\]
There are at most two such clocks. The preparation identity \(e_0+\log_2(X/Y)=L+\theta-\log_2(1-1/(2^{e_0}y))\) contributes less than \(\theta+1\) beyond \(L\); rounding \(j=\lfloor\rho L\rfloor\) costs at most \(\theta\), and prefix correction plus ceiling cost less than two. Both clocks are in the stated \(B=20\) window. All previous physical states exceed \(y\). At least half of the distinct sources realize one common clock.

By (7) and the lower end of (10), the log count of the words before this last pigeonhole step is at least
\[
         j\,[t E_0+\ln\lambda(t)-O(b)]-O(1).
\]
The minimum of \(uE_0+\ln\lambda(u)\) for \(u>0\) occurs at \(t_0\). Replacing \(t\) by \(t_0\) in this lower bound is therefore legitimate. Direct evaluation gives \(\rho[t_0E_0+\ln\lambda(t_0)]/\ln2=J(\delta)\).

## Upper bound at every clock

If \(a_y(X,k)\) counts a first visit with \(q\) odd inputs, the exact affine numerator gives \(q\le(k-L)/\theta\). With \(q\ge1\), reverse the odd transitions from \(y\). Every child before the last is a ternary unit. The terminal nonunit exception costs at most \(k\) choices of exponent; for a fixed word, the initial dyadic exponent is forced by \(k\). Thus each \(q\) contributes at most \(k e^{t_0 k}Z_{q-1}(t_0,y)\). For \(q=0\) there is at most one source. By (6), \(\lambda(t_0)>1\) for small \(\delta\), and \(q\le\rho L+O_B(1)\). Summation and division by \(L\ln2\) give the upper exponent at most \(J(\delta)+O(\rho\eta(t_0))+o_\delta(1)\), uniformly in the target. The lower exponent is at least \(J(\delta)-O(\rho b)-o_\delta(1)\). Since \(t_0\asymp\delta\) and \(c<c'\), these errors imply (1).

## Literature and scope

The weighted affine branches and their ternary Haar Jacobian appear in work on the geometric Syracuse laws and on finite inverse routing. Wren's joint atoms and Weaver's retained prefix bounds give per-depth source counts around the central physical speed on their stated mixing hypotheses. The present argument uses the different limit of geometric parameter \(1-e^{-t}\to0\), where each fixed ternary cylinder is averaged with a small uniform error. The all-orders ordinary first-hit conclusion uses the finite correction (5), the prefix barrier and the exact dyadic clock cancellation. It makes no estimate for the original untilted law \(1-e^{-t}=1/2\). [Tao, Forum Math. Pi](https://doi.org/10.1017/fmp.2022.8) · [Weaver 37, finite inverse transfer](https://rstation.ai/problems/collatz/papers/37) · [Weaver and Wren 50, near-critical Fourier estimates](https://rstation.ai/problems/collatz/papers/50) · [Wren 10, joint central atoms](https://rstation.ai/problems/collatz/papers/10/v3) · [Weaver 12, first landings](https://rstation.ai/problems/collatz/papers/12)

The theorem counts preimages of each endpoint, including endpoints on the known cycle and any hypothetical escaping orbit. It does not connect the future of an arbitrary endpoint to the known cycle.
