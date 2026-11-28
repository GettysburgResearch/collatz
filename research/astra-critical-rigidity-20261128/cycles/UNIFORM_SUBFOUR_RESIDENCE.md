# A uniform native residence bound from all sheets of the last continued-fraction grid

**Proposed written theorem.** Put \(\gamma=\log_23,\ \theta=0.3197044778974\ldots\) as defined in the [matched physical code theorem](MATCHED_SIDON_CODES.md). Fix \(2<R<4\). Any chronological run of \(T\) distinct positive ordinary odd Collatz states in \([M,RM]\) obeys, under the cited \(\mu(\gamma)\le3\),
\[
               T\le M^{(7\theta-1)/3+o(1)}
                     =M^{0.41264\ldots+o(1)}\quad(M\to\infty).          \tag{1}
\]
This applies at all native lengths, including lengths between consecutive continued-fraction denominators. The exponent-three input enters through an upper estimate for the *following* convergent denominator. The earlier physical residence exponent is \(v=0.4333973955184\ldots\); it also bounds the number of visits in a band with specified exits. Equation (1) concerns one consecutive run. [Weaver 145/v1, Theorem 6](https://rstation.ai/problems/collatz/papers/145/v1) · [External logarithm input and scope](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

More precisely, along any subsequence on which \(\log T/\log M\to\lambda>\theta\), let \(b\le T<b'\) be the last and next convergent denominators of \(\gamma\), and suppose
\[
 \alpha=\lim\frac{\log b}{\log M},\qquad
 \xi=\lim\frac{\log b'}{\log M},\qquad \alpha+\xi<1 .
\]
Then, without the exponent-three assumption,
\[
 \lambda\le\theta+\tfrac14
         \max\{0,3\lambda-1,\lambda+\alpha+\xi-1\},
 \qquad
              3\lambda\le4\theta+\alpha+\xi-1 .                        \tag{2}
\]
The latter inequality follows because \(\theta<1/3\) and \(\lambda>\theta\). Thus every putative sequence of runs beating \(M^{\theta+\epsilon}\) must have \(bb'\ge M^{1+3\lambda-4\theta-o(1)}\) in this branch. Equation (2) uses previously established native source and convex-return bounds.

## Keeping all the sheets

The physical source estimate cited above gives \(T\le M^{v+o(1)}\), \(v<1/2\). The [earlier convergent-gap theorem, (1) and (2)](CONFINED_CONVERGENT_GAPS.md) gives \(b\le M^{\theta+o(1)}\) and \(b'\ge T M^{(1-3\theta)/2-o(1)}\) when \(\lambda>\theta\). In particular \(T/b\) grows polynomially, \(b'\gg T M^\delta\) for some \(\delta>0\), and \(b\to\infty\). The approximant \(h/b\) satisfies
\[
               \frac1{b(b+b')}<|\delta_b|=\left|\gamma-\frac hb\right|
                             <\frac1{bb'}.
\]
Use the actual native offsets \(0\le s\le U=\lfloor T/(\log M)^{10}\rfloor\). Partition the reduced ranks \(hs\bmod b\) into \(O((\log M)^3)\) consecutive cells of diameter \(O(b/(\log M)^3+1)\), and retain a largest cell. Subtract the time and rank of its spatially smallest member from all members of that cell, with ties broken arbitrarily. This gives signed times \(|s|\le U\), contained in an interval of length \(U\), and ranks \(0\le j_s\le O(b/(\log M)^3+1)\) with \(j_s\equiv hs\bmod b\). There are \(M^{\lambda-o(1)}\) retained times. Unlike a one-sheet sample, the same reduced rank may occur many times here.

Write \(k_s=(hs-j_s)/b\), \(D_s=2^{-k_s}\operatorname{shift}^s\), and \(w_s=3^s2^{-k_s}=2^{j_s/b+s\delta_b}\). Let \(V_t=2^{E_t}x_t,\ U_t=2^{E_t},\ L=M(1+R/4),\ F_t=\lfloor\log_2(V_t/L)\rfloor\), with \(E_t\) the true cumulative native valuation. Whenever the needed dates lie inside the run, including compositions of up to eleven sample shifts on the central portion,
\[
  2^{-F_t}(D_sV)(t)=2^{-F_t}V_t\,w_s(1+O_R(U/M)).
\]
The same estimate holds for the eleventh power with \(w_s^{11}\). All associated multiplier tags \(2^{-F_t}(D_sU)(t)\) are in \(\{1,2\}\). Indeed the logarithmic angular displacement is \(O((\log M)^{-3}+1/b+U/(bb')+U/M)=o(1)\) even after eleven shifts, and \(RM/2<L<2M\) has strict margins.

At each available date the normalized labels at **different** coarse ranks have the order of those ranks, since \(b(U/(bb')+U/M)=o(1)\). Within the same reduced rank, for times differing by \(kb\ne0\), the log ratio of the two true labels equals
\[
                      kb\,\delta_b+O_R(|k|b/M).
\]
The local error uses only the actual intervening dates. Since \(bb'=o(M)\) by \(\alpha+\xi<1\), its absolute value is \(o(|kb\,\delta_b|)\). Thus actual labels also have the strict order of their \(w_s\)'s *within* each fiber, with one global orientation determined by \(\delta_b\). At each reduced rank, the labels at the central anchor form a Sidon set by the [strict convex return-fiber theorem](CONVEX_RETURN_FIBERS.md), applied to these actual signed offsets. Its hypotheses follow from \(T/b\) growing polynomially, \(T<b'\), and the limit \(T=o(M)\). Our convention for \(k_s\) on one fiber changes by \(h\) per step \(b\), as required.

## Bounding every type of pair collision at the physical anchor

Take an anchor between \(T/2\) and \(2T/3\). For every nontrivial equal-sum relation between unordered pairs of its normalized integer labels, order their members by the strict order above and call the corresponding homogeneous factors \(w_0<w_1\le w_2<w_3\). The pairs are nested, with the extremes paired. The actual inhomogeneous relation gives, at a common central past date,
\[
 |w_0+w_3-w_1-w_2|
    +|w_0^{11}+w_3^{11}-w_1^{11}-w_2^{11}|\ll_R U/M.                \tag{3}
\]
We give the genuine-time justification. The signed operator \(Q=D_0+D_3-D_1-D_2\) has normalized integer forcing of absolute value at most two, so a zero propagates backward through the genuine preceding interval. The affine equation then gives \(QU_t=0\) on that interval. Ten applications of the commuting shifts stay in its interior, yielding \(Q^{11}U_t=0\) on a smaller interval. In the dyadic shift ring modulo 11, \(Q^{11}\equiv D_0^{11}+D_3^{11}-D_1^{11}-D_2^{11}\). The latter forcing, multiplied by \(2^{-F_t}\), is an integer of absolute value at most eight; it therefore vanishes exactly. Over \(\gg\log M\) consecutive genuine dates, the associated label comparison satisfies the homogeneous recurrence and its first integer is divisible by \(2^{F_{t+l}-F_t}\ge 2^{l\gamma-1}\). Since it is \(O_R(M)\), it is zero for \(l\) sufficiently large. The original comparison is zero at that date as well. Dividing through its common base and applying the shape estimate proves (3); no approximation by the *rational* slope is made at this step. The [finite-tube prime-dilation proof](FROBENIUS_BAND_EXITS.md) gives the same local characteristic-eleven mechanism.

All \(w_i=1+o(1)\). Replacing \(w_3\) by \(w_1+w_2-w_0\) in the second power-sum comparison of (3) costs \(O_R(U/M)\). The function \(y^{11}\) has strictly positive second derivative bounded away from zero near one. Its mixed second difference is the integral of this derivative over a rectangle with sides \(w_1-w_0,w_2-w_0\); hence
\[
                         (w_1-w_0)(w_2-w_0)\ll_R U/M.                  \tag{4}
\]
The first comparison then shows \(|w_0w_3-w_1w_2|\ll_R U/M\), by expanding \((w_1-w_0)(w_2-w_0)\). Taking logs and using \(|s|\le U\) gives
\[
            |j_0+j_3-j_1-j_2|\ll bU/M+U/b'=o(1).
\]
Consequently the two coarse-rank sums agree exactly. Put \(d=j_1-j_0,\ v_0=j_2-j_0\), so \(0\le d\le v_0,\ j_3-j_2=d\). The use of \(v_0\) here is for an integer side, distinct from Weaver's exponent \(v\). Count relations per fixed smallest source.

* If \(d>0\), both increments \(w_i-w_0\), \(i=1,2\), are bounded below by constants times the corresponding positive coarse-rank gaps divided by \(b\), since \(U/b'=o(1)\). Hence \(dv_0\ll b^2U/M\). There are \(O_R((b^2U/M)\log M)\) candidate positive integer side pairs, with none if the product budget is below one. Each middle source has at most \(1+U/b=O(U/b)\) possible times at its prescribed rank. Fixing both and the first label determines the fourth actual value by addition, and strict label order identifies at most one fourth source. This costs \(O_R((U^3/M)\log M)\) candidates. It includes a repeated middle point.
* If \(d=0<v_0\), the two lower sources have the same rank and are separated by \(k\ge1\) vertical steps. Then \(w_1-w_0\gg k/b'\) and \(w_2-w_0\gg v_0/b\), so \(k v_0\ll bb'U/M\). There are \(O_R((bb'U/M)\log M)\) possible \(k,v_0\), with none below unit budget. At a fixed lowest source the orientation selects at most one next source of vertical distance \(k\), fixing its exact positive label difference. The top two have common rank \(j_2=j_3=j_0+v_0\). In that fiber **at most one ordered pair** can realize the fixed difference: two different ordered representations of a positive difference would give two different unordered equal-sum pairs in the same Sidon fiber. Thus there is no extra sheet-choice factor and no assumption that their own vertical separation equals \(k\).
* If \(d=v_0=0\), all four coarse ranks coincide and the relation is excluded by the same fiber theorem.

These bounds account for every nontrivial unordered collision, including repeated centers. For \(K\) sampled sources, their total number is at most \(O_R(K(1+U^3/M+bb'U/M)\log M)\).

## All sources survive the entropy estimate

Use their genuine binary tag words over \(n=\lceil\log_3(32RM)\rceil+3\) dates after the anchor. Equal coordinatewise unordered symbol pairs force the initial label sums to agree: the integer comparison satisfies a homogeneous native recurrence over the whole horizon and the terminal dyadic divisor exceeds the initial size. Individual words are injective by the same argument. The base winding equals one or two, every winding one is followed by a two for large \(M\), and its total over the horizon is \(n\gamma+O(1+n/M)\). Thus the numbers of matched ternary pairs and remaining binary singles are \(en+o(n)\), \(sn+o(n)\), with \(e=2-\gamma,\ s=1-2e\). A winding-one pair cannot have decreasing tags by genuine positivity of the valuation. The ordered pair output of the ternary coordinate is unnecessary: its unordered pair determines the separate tag sums on the two rows.

Use the controlled-collision suffix entropy of [repeated additive packings](REPEATED_ADDITIVE_PACKINGS.md). That proof only requires a total \(O(Kd)\) of nontrivial unordered pair collisions, all such coordinate-output coincidences being charged to genuine label equalities. Here take \(d=M^{z+o(1)}\) with
\[
                       z=\max\{0,3\lambda-1,\lambda+\alpha+\xi-1\}.
\]
Since \(v<1/2,\ \alpha+\xi<1\), one has \(z<\lambda\), so its prefix is nonempty on the exponential scale. With zero five-symbol frequency, the bound gives
\[
  \lambda\le \max\{(3/5)(s+e\gamma)/\gamma+z/5,\
               (9s/16+5e\gamma/8)/\gamma+z/4\}\le\theta+z/4 .
\]
This is the first part of (2). The branch \(z=0\) contradicts \(\lambda>\theta\), and \(z=3\lambda-1\) would give \(\lambda\le4\theta-1<\theta\). The last branch proves its second part.

Under the stated irrationality-measure bound \(b'\le b^{2+o(1)}\), by applying it to \(h/b\). Hence on every subsequence with \(\lambda>\theta\) we have \(\alpha+\xi\le3\theta<1\). Applying (2) gives \(3\lambda\le7\theta-1\). Smaller exponents already satisfy (1). The extraction of convergent subsequences is legitimate since \(T\le M^{v+o(1)}\) and the denominators are polynomially bounded in this application.
