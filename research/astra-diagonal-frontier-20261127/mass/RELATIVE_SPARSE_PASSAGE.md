# Relative passage for sparse changes of label

This written transfer uses the relative first-landing estimate and the finite-quotient moment estimate. Both are external analytic inputs. The separate [two-scale argument](FIRST_PERMANENT_ENTRY_LAW.md) uses Valbuena's weaker landing comparison and elementary word counting.

Let \(U(n)=(3n+1)/2^{v_2(3n+1)}\) on positive odd integers. Write \(W_Y\) for the **uniform odd source** in \([Y,2Y)\), \(J_r\) for its first odd-map time at or below \(r\), and \(\operatorname{Pass}_r\) for that value on successful passage. Allow any countable label \(L\) satisfying \(L(x)=L(Ux)\) off a fixed set \(E\). Suppose that, for every \(B>0\),
\[
 \#(E\cap[Z,2Z))\le C_B Z(\log Z)^{-B}\qquad(Z\ge3).                 \tag{1}
\]
In particular any positive power saving in the exponent suffices. Constants below can be chosen uniformly over labels with the same \(E\).

For every \(0<c<5/143\) the label has a limiting probability \(\mu\) in total variation for \(W_Y\), for the uniform odd integers through \(X\), and for their reciprocal normalization. For every \(A>0\) and all tests \(0\le g\le1\) on the label set, the stronger **octave** bound is
\[
 \left|\mathbb E g(L(W_Y))-\mu(g)\right|
 \le C_{c,E}\mu(g)(\log Y)^{-c}+C_{A,c,E}(\log Y)^{-A}.            \tag{2}
\]
As in the stated external relative estimate, allowing dependence on \(A\) also in the first constant suffices for every conclusion below. The uniform law through \(X\) satisfies the same type of bound. The reciprocal law through \(X\) converges in norm at rate \(O((\log X)^{-c})\); its low inputs prevent simply transferring the all-order additive term from one octave.

For \(P,F,\mu\) in the first-permanent-entry note, (1) holds with \(E=P\) by PR201. The finite part satisfies
\[
 \mu\{z\in P:z\ge M\}\ll_{A}(\log M)^{-A}\qquad\text{for every }A>0.    \tag{3}
\]
In particular it has every finite positive moment of \(\log(2+z)\). On any actual escaping ray of nonperiodic units, if \(a\) is an initial unit and \(z\) is any permanently safe subsequent phase, then
\[
 \sum_{\substack{z\ {\rm permanent\ on\ the\ ray}\\z\ge M}} q_z
 \le d_a^{-1}\mu\{z\in P:z\ge M\}\ll_{A,a}(\log M)^{-A}.               \tag{4}
\]
The \(q_z\) here are the natural-density inverse probabilities of *never* producing a nonnegative reverse debt at positive time. Even infinitely many permanent phases satisfying \(q_z\ge c_0(\log z)^{-B}\) for just one finite \(B\) would exclude that escaping ray. The existence of these phases with this probability is open.

## Inputs and a local physical estimate

Fix \(\alpha=1001/1000\). The external relative passage input, as stated explicitly in Weaver's equation (15), is the following. For each \(r\) there is a positive functional \(H_r\), independent of \(Y\), such that whenever \(Y\ge r^\alpha\) and \(0\le f\le1\) on odd landing states at or below \(r\),
\[
 \Lambda_{Y,r}(f):=\mathbb E[1_{J_r(W_Y)<\infty}f(\operatorname{Pass}_r(W_Y))]
   = H_r(f)(1+O((\log r)^{-c}))+O_{A,c}((\log r)^{-A}).             \tag{5}
\]
The constants and onset are uniform in the test. In particular, if a particular nonnegative fresh expectation at \(Y'\ge r^\alpha\) is \(O_A((\log r)^{-A})\) at every order, then so is the expectation at every \(Y\ge r^\alpha\): solve the lower estimate at \(Y'\) for \(H_r(f)\), then use the upper estimate at \(Y\). The statement is for ordinary dyadic uniform sources with failed passage omitted. [Weaver, Paper 12, §6, equation (15)](https://rstation.ai/problems/collatz/papers/12) gives the exact input and attributes it to [Leen, Theorem 5.3](https://doi.org/10.5281/zenodo.23046896) and [Leen, relative landing law](https://doi.org/10.5281/zenodo.23252395).

The finite ternary density \(\rho_j(y)\) is \(3^j\) times the independent geometric-word probability of the affine terminal congruence of \(y\bmod3^j\). Each word of positive gaps has weight \(2^{-\sum e_i}\). The integer inverse congruence for this word is necessary for its occurrence at that \(y\). The external finite-quotient \(L^p\) bound, \(1<p<2\), implies
\[
 \sum_{\substack{y\in S\subset[Z,2Z)\\y\ \mathrm{odd}}}\rho_j(y)/y
       \ll_p (|S|/Z)^{1-1/p}\qquad (3^j\le Z).                        \tag{6}
\]
This follows by covering the octave by periods and applying Hölder. The bound at \(j=0\) uses \(\rho_0=1\). [PR193, fixed-root paper, equation (3)](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) · [Weaver, finite densities, §§1–2](https://rstation.ai/problems/collatz/papers/9/v2).

For \(r\le Y\le r^{\alpha^2}\), set \(R=\lfloor0.1\log r\rfloor\), \(b=\lfloor\tfrac12\log_2 r\rfloor\). The distribution of \(W_Y\bmod 2^{b+1}\) is within \(O(2^b/Y)\) of uniform odd residues. Up to the first time their cumulative sum exceeds \(b\), the forward gaps therefore have the independent positive geometric law, up to that total-variation error. If \(J_r>R\), multiplying the actual odd edges on which every departure and terminal state exceeds \(r\) gives
\[
 A_R\log 2 < \log(2Y/r)+R\log(3+1/r) < 1.8 R\log2
\]
for all large \(r\), since \(\log(3)+10(\alpha^2-1)<1.8\log2\). The independent lower tail at \(1.8R\), the upper tail at \(b\) (whose ratio to \(R\) tends to \(5/\log2\)), and the binary discrepancy are all \(O(r^{-\epsilon})\) for an absolute \(\epsilon>0\). Consequently \(\Pr(J_r>R)=O(r^{-\epsilon})\), including passage failure.

For \(0\le j<R\), take an actual \(v\) in the source octave such that \(j<J_r(v)\) and \(y=U^jv\in E\). Its intermediate departures all exceed \(r\). Write \(A_j\) for *its* sum of forward gaps. The ordinary edge product gives
\[
 {1\over v}={3^j2^{-A_j}\over y}\prod_{i<j}\left(1+{1\over3U^iv}\right)
       \le {2\,3^j2^{-A_j}\over y}.
\]
The empty prefix uses the identity. Every uniform source atom is \(O(1/v)\). For fixed \(y,j\), a complete word has at most one ordinary source; only after the preceding bound may we enlarge its word sum to all words obeying the necessary congruence, giving \(O(\rho_j(y)/y)\). Every marked \(y\) lies between \(r\) and \(2Y\,2^R\le r^{1.1}\) for sufficiently large \(r\), by the elementary one-step growth bound \(Uu\le2u\). Partition into \(O(\log r)\) dyadic octaves, the first of height at least \(r/2\). Here \(3^j\le r^{0.1\log3}\le r/2\). Fix \(p=3/2\) in (6). The contribution per octave per clock is \(O_{B,E}((\log r)^{-B/3})\) by (1); take \(B>3(A+2)\) and sum over octaves and clocks. Together with the late-passage error, this proves
\[
  \Pr\bigl(J_r(W_Y)=\infty\text{ or some departed site before }J_r(W_Y)
                 \text{ belongs to }E\bigr)\ll_{A,E}(\log r)^{-A},
  \qquad r\le Y\le r^{\alpha^2}.                                      \tag{7}
\]
The terminal landing itself is never charged. An earlier visit to a marker and a failed passage are both charged.

## Transfer across all heights

Let \(r_i=r^{\alpha^i}\). For any \(Y\ge r^\alpha\), take \(N\ge1\) with \(r_N\le Y<r_{N+1}\). Apply (7) directly to the top segment down to \(r_{N-1}\), since \(Y<r_{N-1}^{\alpha^2}\). If \(N=1\), this finishes the path. For each \(i=N-2,\ldots,0\), define \(f_i(t)\) on \(t\le r_{i+1}\) to be one if the path from \(t\) to its first landing at or below \(r_i\) fails or departs from a marker before that landing. It is zero when \(t\le r_i\). At the fresh source \(W_{r_{i+2}}\), any path having landed at or below \(r_{i+1}\) and then satisfying this test belongs to the failure-or-mark event of (7) for \(r_i\). The first passages at nested thresholds are sequential even when one physical step crosses several. Hence
\[
 \Lambda_{r_{i+2},r_{i+1}}(f_i)\ll_{A,E}(\log r_i)^{-A}.
\]
Both \(Y\) and \(r_{i+2}\) are at least \(r_{i+1}^\alpha\). Apply (5) to this single test at both sources. Positivity and \(\log r_{i+1}=\alpha\log r_i\) give the same upper bound at \(Y\). No claim of independence of different stages is used. Any failure in an upper stage is charged there, so omission of failed upper landings from \(\Lambda\) does not miss that failure. Union-bounding the stages costs at most \(C_{A,E}\sum_{i\ge0}(\alpha^i\log r)^{-A}=O_{A,E}((\log r)^{-A})\). On every remaining trajectory, passage succeeds and the label agrees exactly at its source and landing. Thus for \(Y\ge r^\alpha\),
\[
 |\mathbb E g(L(W_Y))-\Lambda_{Y,r}(g\circ L)|\ll_{A,E}(\log r)^{-A}.
                                                                         \tag{8}
\]

For \(Y,Y'\ge r^\alpha\) combine (8) and (5). The two label expectations both equal \(H_r(g\circ L)(1+O((\log r)^{-c}))+O_{A,c,E}((\log r)^{-A})\). Taking \(g=1\) in (5) shows \(H_r(1)\le 2\) for large \(r\). Consequently choosing \(r=\min(Y,Y')^{1/\alpha}\) gives a Cauchy family in total variation, uniformly over \(g\). Completeness of the probability measures on a countable discrete space in this metric supplies a countably additive probability \(\mu\). Fix \(Y\), set \(r=Y^{1/\alpha}\), and let \(Y'\) tend to infinity. Solving the limiting lower bound for \(H_r(g\circ L)\), then subtracting the two estimates, gives (2) with the multiplicative factor \(\mu(g)\). Constants and onset can be enlarged for bounded \(Y\).

To pass to the uniform law up to \(X\), partition \([1,X)\) into ordinary factor-two octaves above \(\sqrt X\), whose logarithms are comparable to \(\log X\); the residual has uniform mass \(O(X^{-1/2})\). Endpoint rounding contributes \(O(X^{-1/2})\). To treat reciprocal weights use partial summation of this uniform counting estimate: \(0<c<1\) gives a normalized norm error \(O((\log X)^{-c})\). For the cutoff in (3), choose \(Y=M/3\) and \(g\) the indicator of finite labels at least \(M\). The octave has zero such labels since \(F(v)\le v<2M/3\) whenever finite. Absorb \(C(\log Y)^{-c}\mu(g)\) for large \(M\), giving (3). Equation (4) now follows by natural first-entry disintegration \(\mu_z=d_zq_z\), distinctness of the escaping phases, and \(d_z\ge d_a>0\) along their common forward ray.

The slow-climb examples in the tree of 1 show that the unrestricted \(q_z\) do not obey a uniform strictly positive floor. They leave their dependence on the moving height open. The relative transport input and (4) bound these probabilities from above on a hypothetical escaping ray. They do not supply the conflicting lower bound. Periodic components require their own argument.
