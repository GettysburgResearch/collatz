# A sharp sparse-sum bound at the full cycle determinant

Let \(D=2^n-3^u>0\), with integers \(n,u\ge1\), and set \(g=\gcd(n,u)\). With \(k\ge1\) fixed, take fixed nonzero rational coefficients \(c_i\) and a nonzero sum
\[
                   G=\sum_{i=1}^k c_i2^{t_i}3^{s_i}.
\]
Assume \(|t_i|,|s_i|\le Cn\) and \(\max t_i-\min t_i\le(1-\delta)n\) for fixed \(C,\delta>0\). Clear the fixed coefficient denominators and all powers of two and three when taking \(\gcd(D,G)\). The fixed clearing convention changes its logarithm by at most a constant.

Weaver's sparse-multiple gap already proves qualitative nondivisibility when one exponent coordinate stays in a proper interval. Its proof passes to a minimal translated torus, removes common binomial components, and uses the full-character remainder basis to exclude cancellation on every component. We use that argument below. A Fourier support bound and a field-norm degree bound quantify the surviving fraction of components. The rational construction attains this fraction with actual words. [Weaver 22/v3, Lemma 3, equations (17)–(21)](https://rstation.ai/problems/collatz/papers/22/v3)

**Theorem 1.** Uniformly as \(n\to\infty\),
\[
       \log_2\gcd(D,G)\le
       \left(1-\frac1{\min(k,g)}+o(1)\right)n.                         \tag{1}
\]
In particular every fixed sparse sum in a proper time interval has subexponential gcd at coprime clocks. The exponents need not be ordered in the ternary coordinate, the signs are unrestricted, and the clock need only have \(D>0\). A repeated binary exponent is permitted if the entire sum is nonzero. The same conclusion holds with a ternary gap \(\max s_i-\min s_i\le(1-\delta)u\) in place of the binary gap, when \(u\to\infty\).

**Theorem 2.** Let two distinct rooted shortcut words of the same clocks differ by \(k\) disjoint adjacent swaps \(10\leftrightarrow01\), in either direction. All their other symbols are arbitrary. Write \(q,q'\) for the complete denominators of their positive rational realizations. Then
\[
               \log_2\operatorname{lcm}(q,q')
               \ge\left(\frac1{\min(k,g)}-o(1)\right)n.                \tag{2}
\]
In particular a bounded number of such edits at coprime clocks takes any \(q=2^{o(n)}\) to \(q'=2^{n-o(n)}\). At all clocks an ordinary word has \(q'\ge 2^{n/k-o(n)}\) after the edits. If the two words are proper distinct rotations, they have the same \(q\) and (2) bounds it directly. No condition is imposed on the unedited word's width, run count or complexity. The estimates are ineffective and leave arbitrary ordinary words open.

The exponent \(1/k\) in (2) is attained for each fixed \(k\ge2\) by two actual least-period words with \(g\to\infty\), \(q=2^{o(n)}\), \(q'=2^{n/k+o(n)}\), and \(n\log2-u\log3\to0\). Both examples can use only valuations one and two. The construction builds on the independently editable cells and narrow-width realization in PR 212. [Independent clocks at exact source](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md)

## The torus selected by a subsequence

Consider any proposed infinite violating subsequence. Pass further to one with constant \(g<k\), or with \(g\ge k\) throughout. In the split torus use the point with coordinates \(2^n,3^u,2^{t_i},3^{s_i}\). Choose a translate \(V=P_*H\) of a connected subtorus of smallest dimension containing infinitely many of these points, retaining them and choosing \(P_*\) among them. A subtorus of a split torus is given by character equations, and the rational point \(P_*\) makes the translate rational. By minimality no proper translated subtorus of \(V\) contains an infinite further subsequence. Use split Laurent character coordinates on \(H\), evaluated on \(P/P_*\). Their logarithmic heights are \(O_V(n)\), and their values are positive rational units outside \(2,3\).

The character given by the normalized ratio \((2^n/3^u)/(2^{n_*}/3^{u_*})\) is nonconstant, since a fixed ratio determines both exponents by prime factorization. It is \(T^d\), where \(T\) is a primitive character completed to coordinates \(T,\mathbf W\) and \(d\ge1\) is fixed on \(V\). Put \(c=3^{u_*}/2^{n_*}\). The full determinant divided by a unit outside two and three is \(F=T^d-c\). At every input,
\[
           T=P/Q,\qquad
           P=2^{(n-n_*)/d},\qquad Q=3^{(u-u_*)/d}.
\]
The exponent differences are multiples of \(d\), since \(T\) is a positive rational unit outside two and three. Choose a subsequence on which \(u\) is nondecreasing before selecting the torus, so that \(P,Q\) are integers past its base point. Both are at most \(O_V(2^{n/d})\).

Up to a Laurent monomial, the sparse sum on \(V\) is
\[
 G=\sum_b \mathbf W^b G_b(T),\qquad
 G_b(T)=\sum_{i:b_i=b}\eta_i T^{a_i},
 \qquad \eta_i=c_i2^{t_{i,*}}3^{s_{i,*}}.
\]
The monomial used to clear exponents evaluates to a unit outside two and three. Take the monic rational polynomial \(A=\gcd(F,\{G_b\}_b)\) after that clearing, and put \(h=\deg A\). Its \(h\) distinct complex roots are precisely the components of \(F=0\) on which \(G\) vanishes identically.

## Integer multiples of the clock and Fourier support

If \(b_i=b_j\) and \(a_i-a_j=md\) for some integer \(m\), the ratio of the two normalized monomials along the retained sequence equals \(T^{md}\). Uniqueness of rational prime factorization yields
\[
 t_i-t_j=(t_{i,*}-t_{j,*})+m(n-n_*),\qquad
 s_i-s_j=(s_{i,*}-s_{j,*})-m(u-u_*).
\]
The proper binary time interval, or the stated proper ternary interval with \(u\to\infty\), forces \(m=0\). Hence inside each class \((b,a\bmod d)\) the terms have equal actual character exponents. If every \(G_b\) vanished modulo \(T^d-c\), summing coefficients inside these classes would give \(G=0\) already on \(V\). This contradicts the nonzero inputs. Thus at least one \(G_b\) has nonzero remainder.

Choose \(\xi=c^{1/d}>0\) and a primitive complex \(d\)-th root of unity \(\zeta\). For the preceding \(b\), the list \(G_b(\xi\zeta^j)\), \(0\le j<d\), is the discrete Fourier transform of a nonzero vector supported on at most \(k\) residues modulo \(d\). If a nonzero vector has support \(s\) and its unnormalized transform has support \(r\), Cauchy–Schwarz gives \(\|\widehat v\|_\infty\le\sqrt{s}\|v\|_2\), while Parseval gives \(d\|v\|_2^2=\|\widehat v\|_2^2\le r s\|v\|_2^2\). Thus at least \(d/k\) roots survive and \(d-h\ge d/k\).

Every algebraic root \(\alpha\) of \(T^d=c\) of degree \(e\) also satisfies \(\operatorname{Norm}(\alpha)^d=c^e\). Taking the two rational prime valuations shows that \(d\mid en_*\) and \(d\mid eu_*\), hence \(e\ge d/\gcd(n_*,u_*)\). The nonempty complement of the roots of \(A\) is rationally invariant, so
\[
                         1-h/d\ge 1/\min(k,g_*).
\]
This yields \(h=0\) for coprime clocks, even for arbitrary signed coefficients.

## The whole numerical gcd

Write \(F=AB,\ G=AJ\) on \(V\). The two Laurent polynomials \(B,J\) are coprime since \(F\) is squarefree and every common component was removed. Levin–Wang's outside-\(S\) gcd theorem for coprime polynomials, with \(S=\{\infty,2,3\}\), gives logarithmic gcd \(o(n)\) for their actual values. Indeed for any fixed positive error relative to the coordinate heights, the exceptional set lies in finitely many translates of proper algebraic subgroups. The minimal choice of \(V\) discards each of these after finitely many indices. Monomials may be cleared, then removed from common coordinate content. A nonzero constant gives bounded gcd directly. This is the same exceptional-torus input used in the earlier primitive-clock expression theorem. [Levin and Wang, Theorem 1.13(a)](https://doi.org/10.1515/crelle-2019-0033) · [Earlier primitive-clock argument](PRIMITIVE_CLOCK_EXPRESSIONS.md)

In fact the retained subsequence has
\[
                         \log_2\gcd(D,G)=(h/d)n+o(n).                  \tag{3}
\]
To see the numerical accounting, homogenize \(A(T)\) at \((P,Q)\) as \(A^\sharp=Q^h A(P/Q)\), and do the same for \(B\). Fixed constants clear every rational coefficient. The product \(A^\sharp B^\sharp=D/2^{n_*}\) is exact. The factors have upper bounds \(O_V(2^{hn/d})\) and \(O_V(2^{(d-h)n/d})\) respectively. The usual two-logarithm bound gives \(\log_2D=n-O(\log n)\), so each upper exponential rate is attained. Both homogeneous factors have bounded two- and three-parts after clearing fixed denominators, by their product and \(\gcd(D,6)=1\).

At primes outside two and three, all character arguments are units. Polynomial values have valuations bounded below by the fixed coefficient denominators. The common \(A\) contributes \(\log|A^\sharp|+O_V(1)\) to the logarithmic gcd, with the residual \(B,J\) gcd \(o(n)\) as above. This proves (3), then (1) on the alleged violating subsequence. All constants used after choosing \(V\) can depend on it. This subsequence proof supplies the stated uniform qualitative estimate without an effective threshold. [Two-logarithm bound, Bondareva–Luchin–Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

## A cycle-specific consequence of the ternary gap

For \(u<n<2u\), write \(a_i\ge1\) for the odd-to-odd valuations, and \(T_{i+u}=T_i+n,\ T_{i+1}-T_i=a_i\). Choose any \(1\le h<u\), put \(v=\lfloor hn/u\rfloor+1\), and let \(m\) count indices modulo \(u\) with \(T_{i+h}-T_i\ne v\). For fixed bounded \(m\), the complete reduced denominator of this single word satisfies
\[
                \log_2 q\ge (1/\min(2m,g)-o(1))n.
\]
Indeed Weaver's exact normalized residual \(R\) in equation (6) has \(2m\) signed monomials, binary exponents \(O(n)\), ternary span at most \((1-1/m)u\), and odd nonzero value. Equations (3) and (6) and the extension to every upper window in the proof of Theorem 5 give \(\gcd(D,C)\mid\gcd(D,R)\). Theorem 1 in its ternary-gap form proves the bound. The source's effective defect counts for ordinary cycles remain separate. [Weaver 22/v3, equations (3), (6), (23) and Theorem 5](https://rstation.ai/problems/collatz/papers/22/v3)

## Edit distance and optimal examples

Choose a seam between marker pairs. A swap whose left site is \(t_i\) changes the carry by \(+2^{t_i}3^{s_i}\) or its negative, where \(s_i\) is the number of ones after the pair. Disjoint swaps preserve one another's suffix odd counts. The \(k\) left sites are distinct, so their signed sum is nonzero by its unique least dyadic valuation. Multiply the difference by a power of two modulo \(D\) to put its binary exponents in a proper interval of length at most \((1-1/k)n\), using \(2^n=3^u\) there to wrap individual exponents across a largest gap. Distinct dyadic valuations persist, and the new ternary exponents remain \(O(n)\). For \(k=1\) the difference is already a unit. If the two carries are \(C,C'\), then
\[
             D/\operatorname{lcm}(q,q')=\gcd(D,C,C')\mid\gcd(D,C'-C).
\]
This proves (2).

For sharpness choose large \(M\) as the product of a growing list of distinct primes greater than \(k\). Use \(g=kM\) equal-clock cells. Each original cell has length \(L\), weight \(V\) with \(\gcd(L,V)=1\), and survives all marked swaps with those counts. Use the PR 212 balanced template with independently editable disjoint \(10\) slots. At one slot swap precisely on cell indices divisible by \(k\). At the other original slots use the separate prime clocks from \(M\). Reserve one more disjoint slot. If the full word were an \(r\)-fold repetition, then \(r\mid\gcd(gL,gV)=g\), so its period \((g/r)L\) is necessarily a whole-cell shift. The common multiple of the original marker periods is \(g\), so no proper cell shift preserves all slots. This proof works for composite \(k\) as well. Write \(A=2^L,\ B=3^V\). The baseline cut fraction is the sum of a constant forcing over denominator \(A-B\) and separate periodic forcings with denominators dividing \(A^k-B^k\) and \(A^\ell-B^\ell\) for the selected primes. Thus \(\log_2 q\le L(1+k+\sum_{\ell\mid M}\ell)=o(n)\), where \(n=kML\). The least period stays \(n\) after any independent use of the reserved slot by the old marker test.

In the second word, swap the reserved slot exactly in cells \(0,M,\ldots,(k-1)M\). Its cell-carry change there is a fixed \(d_0\), a positive product of powers of two and three. At the common cut the change of actual rational coordinate is exactly
\[
 \frac{d_0\sum_{j=0}^{k-1}A^{jM}B^{kM-1-jM}}{A^{kM}-B^{kM}}
                  =\frac{d_0B^{M-1}}{A^M-B^M}.
\]
This fraction is reduced. Adjoining \(x'\) to \(x\) generates the same additive subgroup of \(\mathbb Q\) as adjoining their difference to \(x\), so the exact common denominator is \(\operatorname{lcm}(q,A^M-B^M)\). Choose the upper convergent \(L/V\) after \(M\), with \(L\) arbitrarily large compared with \(kM\). Then \(\log_2(A^M-B^M)=ML-o(ML)\) by the two-logarithm bound, the full clock gap tends to zero, and the original prime-slot construction places all sites in the short mechanical phase window that prevents consecutive zero bits. The same proof covers the one extra reserved slot. Both words have only valuations one and two and bounded odd width. It follows that \(q'=2^{n/k+o(n)}\).

Earlier equal-clock cyclotomic selectors and PR 212 already establish cancellation and exact denominators for their specified periodically forced examples. The upper estimate (1) here goes in the other direction for all fixed signed sparse sums in a proper time interval. Its application (2) compares complete denominators even when the unedited portions have no prescribed structure. [Earlier cyclotomic-selector analysis, §4](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-ordinary-boundary-20261124/arithmetic/README.md)

[Exact finite checks](check_sparse_full_modulus.py) replay the signed swaps, rotated support and primitive optimal examples.
