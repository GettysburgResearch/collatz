# Exponential complete denominators for every fixed odd-rotation mismatch budget

**Proposed written theorem.** For every fixed integer \(s_0\ge1\) there are \(c(s_0)>0\) and \(p_0(s_0)\) with the following property. A primitive positive rational Collatz cycle with \(p\ge p_0(s_0)\) odd departures and at most \(s_0\) unequal odd valuations at any one proper rotation has complete reduced denominator
\[
                              q\ge 2^{c(s_0)p}.                         \tag{1}
\]
There is no condition on mismatch gaps, rotation order, largest valuation, physical width or real minimum. In particular, along any sequence of positive ordinary cycles with growing least odd periods,
\[
                \min_{0<\ell<p}\#\{j:e_j\ne e_{j+\ell}\}
                       \longrightarrow\infty.                          \tag{2}
\]
The proof also gives the explicit fixed-budget exponent (11), with ineffective period onset. It does not give an explicit diverging numeric lower bound for the minimum in (2), nor does it exclude cycles with increasing mismatch counts.

The [separated-gap proof](SEPARATED_ROTATION_DENOMINATORS.md) charges each common carry once using two dyadic forms. Clustered dates can have field-linear relations among their carries. To accommodate these relations, use a basis containing the **terminal** roots at both infinity and two, and a different basis containing the **initial** roots at three. A count of common directions in chronological prefix and suffix spans controls the change of basis.

## Physical heights and the common blocks

Assume a contrary sequence \(p\to\infty,\ \log_2 q=o(p)\). Write \(\gamma=\log_2 3,\ \beta=\gamma-1\). The two laps are the same primitive rational odd orbit and its proper lag \(\ell\), reduced to \(1\le\ell\le p/2\) by reversing the lag when needed. Put \(A=\sum e_i\). All true numerators \(y_i=qx_i\) are positive odd ternary units, \(q\) is prime to six, and \(2^{e_i}y_{i+1}=3y_i+q\). These assertions follow from the complete-lap formula \(q\mid 2^A-3^p\) and the actual incoming edge at every phase. Distinct phases have distinct numerators. The exponent word has least period \(p\): the affine map of a repeated smaller block has positive slope different from one, so every point fixed by an iterate of it is fixed by that block.

At \(m=\min x_i\), \(\log_2(m+1)=O(\log p)\). Indeed for \(m\ge1\) the positive product gives \(A\le2p\) and \(0<A\log 2-p\log3\le p/(3m)\). Use the published lower bound for this nonzero two-logarithm form. For \(m<1\) the claimed logarithm is bounded. All individual odd steps satisfy \(y'+q\le(3/2)(y+q)\), so \(\log_2\max y_i\le\beta p+o(p)\). [Bondareva, Luchin and Salikhov, Theorem 1, printed p. 18](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&option_lang=eng&paperid=619&what=fullt)

Cut the synchronized laps at all post-mismatch dates. One may also add any fixed number of other dates. In each resulting block of length \(L\), regard the smaller final exponent as part of the common division sum \(B\). The other track retains its own excess at its actual endpoint. With \(F_h\) the division sum at the first \(h\) dates, \(0\le h<L\), the carry common to both tracks is
\[
                          C=\sum_{h=0}^{L-1}3^{L-1-h}2^{F_h}.
\]
It is prime to six. Taking the difference between the two genuine block equations shows \(2^B\mid y_{\rm high}-y_{\rm low}\), with the two distinct starting numerators ordered by size. In particular \(y_{\rm high}\ge2^B\). Each \(B=O(p)\), and each actual excess is \(O(p)\) by \(2^e\le3\max y_i+q\). The original bounded number of blocks gives \(A=O_{s_0}(p)\), including when \(m<1\).

We need a carry cost uniform in the full clock \(A\). On its higher starting track, for \(h<L\) the positive correction to the first \(h\) steps is bounded by
\[
 \prod_{j<h}(1+q/(3y_j))
    =1+\frac q{y_{\rm high}}\sum_{j<h}\frac{2^{F_j}}{3^{j+1}}
    \le 1+q/2 ,
\]
since \(F_j\le B\). The labels in this display follow the one track chosen at the start of this block. Set \(H_j=\log_2(y_j+q)\) on each actual lap. The physical recurrence gives
\[
 F_h-\gamma h \le H_{\rm start}-H_h+\log_2(1+q)+\log_2(1+q/2).
\]
The first two terms are bounded by the sum of the downward changes of \(H\) along this part of the block. From the displayed sum for \(C\),
\[
 \log_2 C\le\gamma L+\log_2 L+\max_{h<L}(F_h-\gamma h).
\]
At every date \(\Delta H\le\beta\). On each complete lap the sum of all downward changes equals the sum of all upward changes, hence is at most \(\beta p\). Charging each block to its selected higher track and allowing both full laps therefore gives, for any fixed bound \(k\) on the number of blocks,
\[
 \sum_{i=1}^{k}\log_2(qC_i)
 \le(\gamma+2\beta)p+
        k\big[\log_2 p+\log_2 q+\log_2(1+q)+\log_2(1+q/2)\big]
 =(\gamma+2\beta)p+o(p).                                               \tag{3}
\]
The second equality takes \(p\to\infty\) **after** fixing the partition-size bound. No global bound \(\sum\log(1+1/(3x_i))=o(p)\) is assumed for the rational orbit.

## Dyadic coefficients and a low pair independent over them

Start temporarily at the actual minimum, and let \(a(t)\) be the cumulative difference of actual division sums on the second and first laps through time \(t\). Its values change only on a mismatch and \(a(0)=a(p)=0\). There are at most \(s_0+1\) values, all \(O_{s_0}(p)\). Pass to a fixed number of indexed values. Let \(K\) be the field of evaluated rational functions in their powers \(2^{a(t)}\), with two sequences identified when they agree eventually on a stabilized subsequence. As established in the [dyadic-field lemma](SEPARATED_ROTATION_DENOMINATORS.md), one can choose fixed Laurent generators \(T_1,\ldots,T_n\), themselves powers of two of exponent \(O(p)\), such that distinct monomials are rationally independent on every further subsequence, and
\[
                      v_3(R(T))=o(p)\qquad(0\ne R\in K).               \tag{4}
\]
For clarity, stabilize all integral combinations of the boundedly many exponents to be constant or diverge absolutely. The constant lattice is saturated, giving complementary integral generators \(T\). The terms of each Laurent polynomial then have dyadic exponents diverging apart, so no nonempty fixed subsum of distinct terms vanishes eventually. One may derive (4) directly from the same classical fixed-form Subspace Theorem used below. After clearing fixed denominators and a common dyadic power, take the distinct signed monomial terms of a polynomial as integer coordinates. At infinity and two take coordinate forms. At three replace one coordinate form by the sum of all coordinates. The three-place product is a fixed positive constant times the ternary norm of the sum, since every individual monomial has fixed ternary norm and fixed prime-to-six part. The ordinary coordinate height is \(2^{O(p)}\). If the valuation of the sum were at least \(\epsilon p\) infinitely often, primitive gcd division can only improve the product and the Subspace Theorem would give a recurring fixed rational relation among distinct monomials. Ordinary largest-term dominance excludes it. For a single monomial the valuation is fixed directly. The opposite valuation bound follows from the minimum term valuation, and taking quotients proves (4). Evertse's fixed-term \(S\)-unit inequality at three gives the same conclusion. [Evertse, Theorem 2, printed p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

We use ordinary finite-dimensional linear algebra over \(K\) for sequences of actual values. For any fixed finite list of sequences, its fixed \(K\)-coefficient relations are countable. A diagonal subsequence makes each candidate linear combination either eventually zero or eventually nonzero. In the quotient of sequences by eventual equality their span is then a \(K\)-vector space with exactly these stable relations, unchanged under further subsequences. This stabilization can be performed again after adding a finite list of cut points. No independence of unrelated integer numerators is presumed.

On a part of the two laps whose intervening exponents all agree, at dates \(u<v\) the physical differences \(d_t=y_{t,1}-y_{t,0}\ne0\) satisfy
\[
                       2^{E(u,v)} d_v=3^{v-u}d_u.                      \tag{5}
\]
If both \(y_{u,1}/y_{u,0}\) and \(y_{v,1}/y_{v,0}\) were in \(K\), their nonzero differences from one have ternary valuation \(o(p)\) by (4). All actual \(y_{t,j}\) are ternary units, so \(v_3(d_u)=o(p)=v_3(d_v)\). Equation (5) forces \(v-u=o(p)\). This rules out two such field-dependent pairs at separated macroscopic dates in a genuine common run.

Choose \(\eta=1/100\) and at least \(4s_0+8\) equally spaced candidate dates, up to integer parts, in the first \(\eta p\) odd steps **forward** of the minimum. By passing to a subsequence the marks fall between these candidates in fixed positions, including any equalities. There are two candidates separated by a positive multiple of \(p\) with no mismatched departure between them. For instance, remove candidates lying on a mismatched departure and partition the remaining ones by the at most \(s_0\) mismatches. At most \(s_0+1\) resulting runs cannot each contain at most one. Stabilize their root relations. By (5) at least one candidate has its two numerators \(Y_0,Y_1\) independent over \(K\). Use it as the root of the two laps. Their true bounds give
\[
                   \log_2(Y_0Y_1)\le\beta(1/2+2\eta)p+o(p).             \tag{6}
\]
Indeed one is within \(\eta p\) forward steps of the minimum, and the other within \((1/2+\eta)p\). After this change of root, every \(2^{E_{t,1}-E_{t,0}}\) is still in \(K\): the exponent is a difference of two original values of \(a\), with total difference zero over the lap.

## Two bases from opposite ends of the lap

Choose a fixed integer \(N\) for a time mesh. In the newly rooted laps use the cut list
\[
          0=t_0<t_1<\cdots<t_k=p
\]
consisting of post-mismatch dates, endpoints and \(\lfloor j p/N\rfloor\), \(0\le j\le N\), counting ties once. Thus \(k\le s_0+N+1\), and all gaps are at most \(p/N+1\). Pass to a fixed order and incidence pattern and stabilize field-linear relations on the resulting finite list. Write \(E_{i,j}\) for the actual cumulative divisions on track \(j\) through cut \(t_i\). Set \(X=2^A/3^p\) and
\[
 Z_i=q C_i 2^{E_{i-1,0}}3^{-t_i},\qquad
 v_{i,0}=1,\quad v_{i,1}=2^{E_{i-1,1}-E_{i-1,0}}\in K .
\]
The complete-lap and partial-lap equations hold in this vector space:
\[
 R_{i,j}=Y_j+\sum_{h\le i}v_{h,j}Z_h
        =XY_j-\sum_{h>i}v_{h,j}Z_h
        =2^{E_{i,j}}3^{-t_i}y_{t_i,j}.                                 \tag{7}
\]
In particular \(v_3(Z_i)=-t_i\) and \(|Z_i|_\infty |Z_i|_2=q C_i\,3^{-t_i}\). The initial pair \(Y_0,Y_1\) and its terminal pair \(XY_0,XY_1\) are each independent over \(K\).

Let \(V\) be the \(K\)-span of both roots and all \(Z_i\), with dimension \(r\). The prefix basis consists of \(Y_0,Y_1\), followed by whichever \(Z_i\) increase the span, in increasing chronological order. Denote the selected indices by \(I\). For the suffix basis start with \(XY_0,XY_1\) and add \(Z_i\) greedily in *decreasing* chronological order, with selected indices \(J\). Both are bases by (7), with \(|I|=|J|=r-2\).

Let \(P_i=\langle Y_0,Y_1,Z_h:h\le i\rangle_K\), \(S_i=\langle XY_0,XY_1,Z_h:h>i\rangle_K\). They sum to \(V\) and both contain \(R_{i,0},R_{i,1}\). Greedy selection gives
\[
 \#(I\cap[1,i])=\dim P_i-2,\qquad
 \#(J\cap[1,i])=r-\dim S_i.
\]
Subtract and sum by parts, using the common cardinality, to obtain the exact identity
\[
 \sum_{i\in I}t_i-\sum_{i\in J}t_i
  =\sum_{i=0}^{k-1}(t_{i+1}-t_i)\,[\,2-\dim(P_i\cap S_i)\,].          \tag{8}
\]
The bracket is at most one. It is at most zero wherever the two actual tracks at this cut are \(K\)-independent, since the ratio of the factors multiplying them in (7) is in \(K\).

There are at most \(s_0\) extra mismatch cuts and at most \(s_0+1\) rank-one mesh cuts in the open common runs, up to boundary dates. More explicitly, charge each cut coinciding with a post-mismatch date to one of the at most \(s_0\) such dates, and place every other mesh date in the intervals between those post-mismatch dates, splitting also at the root. Two such mesh dates in the same interval have only matching intervening departures and are separated by at least \(p/N-1\). By (5) both pairs cannot have rank one. The root pair has rank two. Thus at most \(2s_0+2\) summands of (8) have positive bracket. In particular,
\[
              \sum_{i\in I}t_i-\sum_{i\in J}t_i
                        \le(2s_0+2)(p/N+1).                            \tag{9}
\]

## The product of fixed forms with different bases at three

Call the suffix basis \(B_-\) and the prefix basis \(B_+\). Every element of \(B_+\) is a linear combination of \(B_-\) with fixed rational-function coefficients in the Laurent generators. Clear all their denominators by a single fixed nonzero Laurent polynomial \(Q(T)\). Equation (4) gives \(v_3(Q(T))=o(p)\). This field coefficient will be used only at three.

Fix a large integer \(D\). Take \(\mathcal B=\{0,\ldots,D-1\}^n\), with a singleton if \(n=0\). Choose a fixed finite set of exponent shifts containing zero and the supports of all the Laurent expressions for \(Q B_+\) in \(B_-\). Let \(\mathcal B^+\) be the union of its translates of \(\mathcal B\). Then \(|\mathcal B^+|/|\mathcal B|=1+o_D(1)\). Our single rational vector consists of all \(bT^u\) for \(b\in B_-,u\in\mathcal B^+\). These coordinates have no fixed rational linear relation on any infinite further subsequence, by the stabilized \(K\)-basis and independence of the monomials.

At infinity and two use precisely these coordinate forms. At three use all forms representing \(Q bT^u\) for \(b\in B_+,u\in\mathcal B\). Their coefficients are fixed rationals and these forms are independent, by the prefix basis and monomial independence. Complete them to a basis of forms by any independent subset of the suffix coordinate forms, possible because these span the entire space of forms. This uses exactly \(r(|\mathcal B^+|-|\mathcal B|)\) additional forms. All these choices are fixed on the stabilized subsequence.

There is no \(\log_2|T^u|_\infty\) loss on the boundary of the exponent set. Indeed \(|T^u|_\infty|T^u|_2=1\) exactly and \(|T^u|_3=1\). Thus the logarithmic product over infinity and two, divided by \(|\mathcal B|\), is \((|\mathcal B^+|/|\mathcal B|)\sum_{b\in B_-}\log_2(|b|_\infty|b|_2)\). Each absolute logarithmic summand is \(O_{s_0,N}(p)\), independent of \(D\). The terminal roots contribute \(\log_2(Y_0Y_1)-2\gamma p\), since the numerator powers of two in each \(XY_j\) cancel at these two places. Each selected carry contributes \(\log_2(q C_i)-\gamma t_i\). At three, each initial root has norm one and each prefix carry has norm \(3^{t_i}\). The factor \(Q\) costs \(o(p)\) after division by \(|\mathcal B|\) for the already fixed field relations, and every completing coordinate form has ternary logarithmic norm at most \(\gamma p\). Consequently the base-two logarithm of the complete product, divided by \(|\mathcal B|\), is bounded above by
\[
  \log_2(Y_0Y_1)-2\gamma p+\sum_{i\in J}\log_2(q C_i)
   +\gamma\left(\sum_{i\in I}t_i-\sum_{i\in J}t_i\right)
   +o_D(1)O_{s_0,N}(p)+o(p).                                          \tag{10}
\]
The coefficient hidden in the boundary term may depend on the stabilized field and finite basis supports once \(N\) is fixed. Before applying (3) use \(qC_i\ge1\), so that the selected carry costs are bounded by the full sum.

By (3), (6) and (9), the coefficient in (10) before its boundary and vanishing terms has upper limit at most
\[
             -\gamma+\beta(5/2+2\eta)+\frac{\gamma(2s_0+2)}N .
\]
The positive margin \(\gamma-\beta(5/2+2\eta)>0\) follows, for example, from \(\gamma<8/5\) (because \(3^5<2^8\)) and \(\eta=1/100\). First choose the previously specified mesh parameter \(N\) so large that its term is below one quarter of this margin. After stabilization at that fixed mesh, choose \(D\) so the translate boundary is below a further quarter. Then let \(p\) tend to infinity. The actual product of all forms is \(2^{-c' p}\) or smaller for a fixed \(c'>0\).

All coordinates have denominators supported on two and three, and for fixed choices have ordinary and denominator heights \(2^{O(p)}\). Clear powers of two and three, which leaves the three-place product unchanged. Dividing by the integral gcd can only decrease it, since the three-place norm product of an integer is its part prime to six. The primitive coordinate height \(H\le 2^{O(p)}\), with constants allowed to depend on the stabilized generator basis, \(s_0,N,D\) and chosen fixed shifts. Apply the rational \(S\)-adic Subspace Theorem for the fixed independent forms at each of the three places. The product is smaller than \(H^{-\epsilon}\) for some fixed \(\epsilon>0\), hence the primitive vectors lie in finitely many proper rational subspaces. Bounded-height vectors would already give finitely many lines. Either conclusion contradicts the established absence of any recurring rational linear relation on these coordinates. [Schlickewei, original \(p\)-adic Subspace Theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Bilu, Theorem 2.3, rational integer form](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

We have excluded every sequence with a bounded mismatch budget and \(\log q=o(p)\). Failure of (1) for a fixed budget would give precisely such a sequence by using successively smaller positive rates. Applying (1) at \(q=1\) gives (2).

## An explicit exponent at every fixed budget

Refining the choice of cuts and the shifted-height bound gives the quantitative version
\[
  \boxed{\displaystyle
   \liminf_{p\to\infty}\frac{\log_2q}{p}
       \ \ge\ \frac{\gamma-(3/2)(\gamma-1)}{4(s_0+1)+2}
       \ =\ \frac{3-\gamma}{8s_0+12}.}                                \tag{11}
\]
The lower limit ranges over primitive cycles admitting a rotation with at most the fixed \(s_0\) mismatches. Numeric onsets remain ineffective. For \(s_0=6\) the coefficient in (11) is strictly larger than \(1/43\), since \(\gamma<8/5<69/43\). This is a strict improvement on the earlier \(1/4096\) coefficient at that budget.

Take a contrary subsequence with \((\log_2 q)/p\to\lambda\) strictly below the right side of (11). We still have \(\log q=O(p)\), \(\log_2(\max y_i+q)=O(p)\) and \(A=O_{s_0}(p)\) by the first section. The construction and neutral valuation (4) of \(K\) use only these upper bounds and the native ternary units. Fix arbitrarily small \(\eta,\delta>0\). The low independent pair can still be chosen as above, now with
\[
            \log_2(Y_0Y_1)\le 2\log_2q+\beta(1/2+2\eta)p+O(\log p).
\]

Use the original post-mismatch dates and this root, for at most \(s_0+1\) intervals. Pass to limits of their normalized lengths. In each interval of positive limiting length \(L/p\), select two candidate dates at \(\lfloor\delta L/2\rfloor,\lfloor\delta L\rfloor\) after its beginning, taking \(\delta<1/2\). They precede the last departure and are separated by a positive multiple of \(p\). Stabilize ranks at the finitely many candidates; (5) ensures at least one pair independent over \(K\). Insert one such date. No extra cut is required in an interval of length \(o(p)\). Now \(k\le2(s_0+1)\). In (8) a long original interval contributes at most \(\delta L\), as the second resulting gap starts at the independent pair. All short original intervals together contribute at most \(o(p)\). Hence the clock-weight difference in (10) is at most \(\delta p+o(p)\).

For a subblock at its higher start and \(h<L\), the common native recurrence gives the stronger shifted bound
\[
  \frac{2^{F_h}(y_h+q)}{3^h}
   =y_{\rm high}
     +q\left(\sum_{j<h}\frac{2^{F_j}}{3^{j+1}}
                       +\frac{2^{F_h}}{3^h}\right)
   \le y_{\rm high}(1+q).
\]
Every \(2^{F_j}\) appearing in parentheses is at most \(y_{\rm high}\), and \(\sum_{j<h}3^{-j-1}+3^{-h}\le1\), including \(h=0\). Thus \(F_h-\gamma h\le H_{\rm start}-H_h+\log_2(1+q)\). There is a stronger variation estimate here. Let \(H^*_t=\log_2(\max(y_{t,0},y_{t,1})+q)\) on the *synchronized* cycle. The higher track at a block start remains the higher one throughout the common strict interior, by positive affine monotonicity. Hence for every \(h<L\) its \(H_{\rm start}-H_h\) is exactly \(H^*_{\rm start}-H^*_h\). These blockwise costs can all be charged to disjoint portions of this same cyclic envelope. At every date, including a mismatch, each of the two actual shifted numerators grows by a factor at most \(3/2\), so \(H^*\) rises by at most \(\beta\). Its downward variation is at most \(\beta p\) because it returns after the lap. This single-envelope refinement was supplied by the ordinary-trajectory lane. It gives
\[
       \sum_i\log_2(q C_i)
          \le(\gamma+\beta)p+2k\log_2 q+O(k\log(p+1)).
\]
Substitute into (10), whose fixed-basis product proof is unchanged. Before the vanishing translate-boundary term, the limiting coefficient is at most
\[
             -\gamma+(3/2+2\eta)\beta+[4(s_0+1)+2]\lambda+\gamma\delta .
\]
Choose \(\eta,\delta>0\) small using the strict assumed margin, stabilize at these parameters, then take \(D\) large and \(p\to\infty\) as in the original proof. This contradicts the Subspace Theorem and proves (11).

## The native shortcut period

For the same fixed mismatch budget, every family with \(A\to\infty\) satisfies \(\liminf(\log_2 q)/A>0\), with a lower bound depending only on \(s_0\). Before assuming anything about \(q\), the minimum estimate and shifted growth give
\[
 \log_2(\max y_i+q)\le\log_2 q+\beta p+O(\log(p+1)).
\]
Use just the original at most \(s_0\) blocks. Their common sums \(B_i\) are at most the right-hand side by the nonzero difference divisor, and their final excesses are at most that side plus \(\gamma\) by \(2^e\le3\max y_i+q\). Therefore \(A\le2s_0[\log_2q+\beta p+O(\log(p+1))]\), with an absolute implied constant. If \(p\ge p_0(s_0)\), (1) gives \(p\le c(s_0)^{-1}\log_2q\). For \(p<p_0(s_0)\), the bounded period term also gives the assertion as \(A\) grows.

## Priority and scope

PR212 at 505d3fe782922904e86477990cc5d41e9110edda proves an explicit \(1/4096\) full-denominator rate for up to six arbitrary mismatches. It also excludes bounded mismatch counts on growing ordinary cycles when the chosen rotation orders tend to infinity, using Weaver's finite-descent result. Armstrong and Wren distinguished the odd-valuation mismatch question from its shortcut-parity analogue. Here the bound covers every **fixed** mismatch budget and all orders with a moving complete denominator. The explicit rate (11) depends on the budget and its uniform period onset is ineffective. It leaves growth with a specified function of increasing budgets, and the unrestricted ordinary cycle problem, open. [PR212 denominator theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ROTATION_DENOMINATORS.md) · [PR212 odd-rotation frontier](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ODD_ROTATION_COMPLEXITY.md) · [Wren, Paper 218, §7](https://rstation.ai/problems/collatz/papers/218/v3)

[Native and rank verifier](check_all_fixed_rotations.py) · [Recorded exact counts](all_fixed_rotation_controls.json). The native part uses 176 primitive rational cycles, 4,752 physical partitions and 27,456 actual prefix identities. The one-envelope carry bound includes 12,624 blocks ending at a change of higher track. A separate finite vector-space control replays 911 rank cuts in 180 modeled linear systems, including positive and negative signed losses. Twenty-four exact translated products exercise different bases with actual boundary completion and a clearing polynomial that can be divisible by three. The finite vector tests check the algebraic interfaces. The asymptotic neutral-field and Subspace Theorem arguments remain written.
