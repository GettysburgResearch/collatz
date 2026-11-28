# A uniform algebraic-approximation bound for a full binary substitution subshift

Let \(\sigma\) be a primitive binary substitution of constant length \(k\ge2\) whose subshift \(\mathcal X\) is aperiodic. Here \(\mathcal X\) contains all one-sided words whose factors occur in substitution iterates. Let \(\Phi(w)\in\mathbb Z_2\) be the unique starting value with native shortcut parity sequence \(w\). For each fixed positive integer \(d\), there is a finite \(C_{\sigma,d}\) such that, in a fixed embedding into \(\overline{\mathbb Q}_2\),
\[
 v_2\bigl(\Phi(w)-\gamma\bigr)\le C_{\sigma,d}\bigl(1+h(\gamma)\bigr)
 \quad(w\in\mathcal X,\ [\mathbb Q(\gamma):\mathbb Q]\le d).        \tag{1}
\]
Here \(v_2(2)=1\), \(v_2(0)=+\infty\), and \(h\) is absolute logarithmic Weil height. Every \(\Phi(w)\) is consequently transcendental. A positive integer \(n\) can follow any word in the whole subshift for at most \(C_{\sigma,1}(1+\log n)\) native letters. Both estimates are uniform in the location of the origin in the substitution system. Existence of these constants gives no small numerical cutoff.

Weaver 173 proves superlinear factor complexity for every aperiodic signed rational orbit. That already excludes rational realizations throughout these linearly complex subshifts. Weaver 16 also treats automatic and primitive fixed words via local Mahler coherence. The assertions here are transcendence and a uniform bounded-degree approximation measure extending over the entire subshift. The proof uses the classical auxiliary-function method for chains of Mahler equations. [Weaver 173, theorem and corollary](https://rstation.ai/problems/collatz/papers/173) · [Weaver 16, especially §§1, 12, 15–18](https://rstation.ai/problems/collatz/papers/16) · [Y. Flicker, *Algebraic independence by a method of Mahler*, §§1–4, Theorem 2](https://doi.org/10.1017/S144678870001209X)

## A scalar identity with a moving ternary weight

For a word \(u\), put \(s_t=\sum_{i<t}u_i\) and
\[
 H_u(X,Y)=\sum_{t\ge0}u_tX^tY^{s_t},\qquad
 S_u(X,Y)=\sum_{t\ge0}X^tY^{s_t}.
\]
The identity \((1-X)S_u+X(1-Y)H_u=1\) follows by telescoping consecutive monomials. The native inverse congruences give
\[
                    \Phi(u)=-\tfrac13 H_u(2,1/3).                  \tag{2}
\]
Indeed each odd letter at position \(t\) contributes \(-2^t/3^{s_t+1}\) and the finite remainder has valuation at least the prefix length. This identity is in \(\mathbb Q_2\).

For \(a\in\{0,1\}\) let \(U_a\) be the finite polynomial defined by the same sum for \(\sigma(a)\) and let \(h_a\) be its number of ones. Put \(\delta=h_1-h_0\). Grouping the positions by their substitution block gives
\[
 H_{\sigma(u)}=B+A H_u(X',Y'),\quad
 X'=X^kY^{h_0},\quad Y'=Y^\delta,\quad
 B=\frac{U_0}{1-X'},\quad A=U_1-U_0\frac{1-X'Y'}{1-X'}.            \tag{3}
\]
This uses the telescoping formula for \(S_u(X',Y')\). Evaluate at \(X_0=2,Y_0=1/3\), and define successive points by the primed transformation. Then
\[
 v_2(X_j)=N_j=k^j,\quad h(X_j)\ll N_j,\quad
 Y_j=3^{-\delta^j},\quad v_2(Y_j)=0.                               \tag{4}
\]
The height bound follows since \(X_j=2^{N_j}/3^{|\sigma^j(0)|_1}\). Primitivity gives \(|\delta|<k\) unless the two images are constant opposite blocks, which cannot generate a primitive aperiodic substitution. Consequently \(h(Y_j)=o(N_j)\).

Every \(w=w_0\in\mathcal X\) has a tower \(w_j={\rm shift}^{a_j}\sigma(w_{j+1})\), with \(w_j\in\mathcal X\) and \(0\le a_j<k\). Indeed approximate \(w_j\) by shifts of a fixed point of a power of \(\sigma\), or by factors of arbitrarily deep iterates. Extract a subsequence of enclosing level-one blocks with fixed origin offset, then a coefficientwise limit of the right-infinite sequence of their preimage letters. All its factors lie in the language. Iterating gives the tower and never requires uniqueness of the decomposition. A primitive aperiodic substitution has a compact minimal subshift, hence contains no eventually periodic word. One can see minimality directly: a given factor occurs in some \(\sigma^m(a)\), and primitivity places that letter in all sufficiently high supertiles. Every sufficiently long legal factor then contains the given factor.

Deleting \(a_j\) initial letters subtracts their finite prefix sum from (3) and divides by \(X^{a_j}Y^{s_{a_j}}\). Thus with \(F_j=H_{w_j}(X_j,Y_j)\) there are rational numbers \(A_j,B_j\) such that
\[
                  F_j=A_jF_{j+1}+B_j,\quad
       A_j\ne0,\quad |v_2(A_j)|+h(A_j)+h(B_j)\le c N_j .           \tag{5}
\]
The number \(c\) is uniform in the tower. The two images of \(\sigma\) differ, since identical images make the subshift periodic. At their first differing position \(r<k\), the first nonzero term of \(U_1-U_0\) is \(\pm X^rY^s\). The extra summand in \(A-(U_1-U_0)\) has valuation at least \(kN_j\), and all later polynomial terms have strictly larger valuation than \(rN_j\). Therefore \(v_2(A_j)=(r-a_j)N_j\). The height bounds follow from (4) by evaluating a finite list of fixed rational functions. The denominators \(1-X_{j+1}\) never vanish.

## Uniform auxiliary polynomials

For any non-eventually-periodic binary word \(u\) and any nonzero rational \(y\), \(H_u(X,y)\) is transcendental over \(\mathbb Q(X)\). An algebraic equation would reduce to a nonzero algebraic equation modulo every prime outside a finite set, after clearing denominators. At primes not dividing the numerator or denominator of \(y\), the support of the reduced coefficient sequence is exactly the set of ones of \(u\). Christol's theorem makes each reduced sequence automatic in that prime base. Coding nonzero coefficients by one makes \(u\) automatic in each such base. Cobham's theorem at two distinct primes forces eventual periodicity. Also \(H_u(X,Y)\) is transcendental over \(\mathbb Q(X,Y)\): divide any polynomial relation by its common power of \(Y-1\) before specializing at \(Y=1\). This recovers the finite-alphabet consequence of Fatou at weight one. [Christol, Kamae, Mendès France and Rauzy, Theorem 1](https://www.numdam.org/articles/10.24033/bsmf.1926/) · [Cobham, *On the base-dependence of sets of numbers recognizable by finite automata*](https://doi.org/10.1007/BF01746527) · [Borwein and Coons, Theorem 1](https://arxiv.org/abs/0806.1563)

Fix \(m\ge2\) and put \(M=m^2\). First take \(|\delta|\ge2\). For each possible \(M\)-letter prefix of a word \(u\in\mathcal X\), choose a nonzero \(P(X,Y,W)\in\mathbb Z[X,Y,W]\), with \(\deg_X,\deg_W\le m\), such that
\[
                  P(X,Y,H_u(X,Y))=O(X^M).                           \tag{6}
\]
Solve \(M\) homogeneous linear equations in \((m+1)^2\) unknowns over \(\mathbb Q(Y)\), then clear denominators. The first \(M\) coefficients depend on the given prefix only. There are finitely many chosen polynomials. For each such \(P\), the first nonzero coefficient of \(P(X,Y,H_u)\), viewed as a polynomial in \(Y\), has order bounded above uniformly in \(u\in\mathcal X\). Otherwise compactness produces a limit word with the whole formal series identically zero, contrary to the preceding paragraph. Thus for the selected polynomial its leading order \(\nu\) lies in \([M,J_m]\). Its nonzero leading coefficient \(c_\nu(Y)\) belongs to a finite list since only a bounded prefix of \(u\) is used.

The numbers \(Y_j=3^{-\delta^j}\) are pairwise distinct in this case. For all sufficiently large \(j\) none is a root of any of these finitely many leading polynomials. The product formula gives \(0\le v_2(c_\nu(Y_j))=O_m(1+h(Y_j))=o_m(N_j)\), since \(Y_j\) is a 2-adic unit and the coefficients are integers. All later coefficients evaluate to 2-adic integers. Consequently the leading term strictly dominates for all sufficiently large \(j\), uniformly in \(w_j\), and
\[
        M N_j\le v_2\!\left(P(X_j,Y_j,F_j)\right)
                     \le (J_m+1) N_j.                               \tag{7}
\]
In particular the evaluated number is nonzero.

If \(\delta=0\), all \(j\ge1\) have \(Y_j=1\). If \(\delta=1\) or \(-1\), the weights form a subset of \(\{1/3,3\}\). For each of these actual weights \(y\), use the same prefix-linear-system construction directly over \(\mathbb Q\) for \(H_u(X,y)\). Clear denominators to obtain finitely many \(P(X,W)\in\mathbb Z[X,W]\). The compactness bound uses the fixed-weight transcendence just proved. The finitely many nonzero leading rational coefficients have bounded valuation; every coefficient is 2-adically integral because these weights are units. This proves (7) also in these cases. The polynomials used in (7) may depend on \(w_j\), but their entire lists, order bounds and height constants are uniform in \(\mathcal X\). The quadratic lower exponent \(M=m^2\) is essential below.

## Comparison with arbitrary algebraic approximants

Begin with an algebraic \(r_0\) of degree at most \(d\) and form \(r_{j+1}=(r_j-B_j)/A_j\). All these values belong to \(\mathbb Q(r_0)\). Standard height inequalities, (5), and \(\sum_{i<j}N_i\le N_j\) give
\[
 h(r_j)\le h(r_0)+c_1 N_j,\qquad
 v_2(F_j-r_j)\ge v_2(F_0-r_0)-c_1 N_j.                             \tag{8}
\]
The constant \(c_1\) is independent of \(m,d\), and the estimates hold for every admissible tower. If \(v_2(F_0-r_0)>(c_1+J_m+2)N_j\) and \(j\) is sufficiently large, then \(r_j\) is integral at 2 and the valuation of the difference between \(P(X_j,Y_j,r_j)\) and \(P(X_j,Y_j,F_j)\) exceeds \((J_m+1)N_j\). This follows by factoring the difference in the last argument, since all the remaining inputs and integer polynomial coefficients are integral at 2. By (7), \(b_j=P(X_j,Y_j,r_j)\ne0\) and \(v_2(b_j)\ge m^2N_j\).

The height of this algebraic number satisfies
\[
       h(b_j)\le m h(r_0)+c_2 m N_j+o_m(N_j)+O_m(1),                \tag{9}
\]
where \(c_2\) depends only on \(\sigma\). In fact the polynomial evaluation bound is \(\deg_XP\,h(X_j)+\deg_WP\,h(r_j)+\deg_YP\,h(Y_j)+\log\|P\|_1\). The \(Y\)-degree and coefficient norm are bounded only after fixing \(m\), which is sufficient because \(h(Y_j)=o(N_j)\). Fixed-weight polynomials omit the \(Y\)-term. At the chosen place the product formula yields \(v_2(b_j)\log 2\le d\,h(b_j)\).

Choose \(m\) so large that \(m^2\log 2>2d(c_2+1)m\), then take \(j\) sufficiently large for (7) and (9). If \(r_0=F_0\), arbitrarily large \(j\) contradict these inequalities. Otherwise let \(V=v_2(F_0-r_0)\). When \(V\) is large, choose the largest \(j\) with \((c_1+J_m+3)N_j<V\). Since \(N_{j+1}=kN_j\), this gives \(V\le k(c_1+J_m+3)N_j\), while (7)–(9) give \(N_j\ll_{\sigma,d}1+h(r_0)\). Smaller \(V\) are covered by an enlarged constant. Taking \(r_0=-3\gamma\) and using (2) proves (1).

If a rational 2-adic integer shares the first \(t\) parities of \(w\), its difference from \(\Phi(w)\) is divisible by \(2^t\) (apply the common affine numerator with odd leading coefficient). Thus (1) for \(d=1\) gives the stated ordinary clock. This quantitative bound controls approximations to all words in one supplied subshift. It does not bound the complexity of an arbitrary escaping orbit. Sharpe's independently formalized example treats the substitution \(0\mapsto011,1\mapsto110\) with a concrete Padé certificate at \(8/9\). The general auxiliary-function technique for nonautonomous \(p\)-adic Mahler equations predates these Collatz applications. [Sharpe, word-complexity ladder and running example](https://github.com/msharpe248/collatz) · [Flicker, §4 after Theorem 2, crediting Mahler, Kubota, Loxton and van der Poorten](https://doi.org/10.1017/S144678870001209X)
