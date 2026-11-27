# Exact binary-cost smaller-parent rows at one original source

The stochastic smaller-parent map from [the grade calculation](GRADE_PARENT.md) has ordinary inverse children
\[
 v_e(q)=2^e q+\bigl(2(-1)^{e+1}2^e-1\bigr)/3,\qquad e=1,2,\ldots ,
 \qquad S(v_e(q))=3q+2(-1)^{e+1}.
\]
Here \(q\) is any positive odd integer. Its exact-cost row \(A_n(q)\) contains the endpoints obtained from \(q\) by composing children in chronological order \(e_1,\ldots,e_t\), with \(\sum_i e_i=n\), allowing every positive composition of \(n\). The following finite and limiting geometry is unconditional.

## Every odd residue once and an entire ordinary interval

For \(n\ge1\), \(A_n(q)\) contains one representative of every odd residue modulo \(2^n\). Given two equal endpoint residues, the final exponent \(e=v_2(3v+1)\) is determined if \(e<n\). If the valuation is at least \(n\), the cost forces a single final exponent \(e=n\) and no other letters. In the first case the two parents differ by the endpoint difference divided by \(2^e\), since the final signs agree. They have equal residues modulo \(2^{n-e}\); induction recovers all remaining letters. The \(2^{n-1}\) compositions therefore map injectively to the \(2^{n-1}\) odd residues. This argument permits \(q=1\).

Write \(c_e=1\) for odd \(e\) and \(c_e=-3\) for even \(e\), \(E_i=e_1+\cdots+e_i\), \(E_0=0\). The exact real representation is
\[
 \frac{v}{2^n}=q+\frac{1+W_t}{3}-\frac{2^{-n}}3,\qquad
 W_t=\sum_{i=1}^t 2^{-E_{i-1}}c_{e_i}.                              \tag{1}
\]
Indeed \(3v_e(q)+1=2^e(3q+1+c_e)\). The two families of similarities \(x\mapsto c_e+2^{-e}x\) send \([-4,2]\) into \([-1,2]\) for odd \(e\) and \([-4,-5/2]\) for even \(e\). Apply them to the zero tail in (1). In particular all normalized endpoints lie in the two intervals
\[
 \left(q+[-1,-1/2]\right)-2^{-n}/3,\qquad
 \left(q+[0,1]\right)-2^{-n}/3 .
\]
Every odd integer in
\[
                         (2^n(q+1/2),\ 2^n(q+1))                    \tag{2}
\]
belongs to the row. Its companion representative one period lower is in the forbidden gap, and no other representative is within the bounds. All comparisons here are strict; at the upper end a grid point is at distance at least \(2^{-n}\) from the excluded endpoint.

## The physical window and natural means

Take iid geometric exponents with \(\mathbb P(e=k)=2^{-k}\). They are the successive gaps between ones of independent fair binary bits numbered from 1, with an initial renewal at zero. Let \(W\) be the infinite series in (1), and \(Z=(1+W)/3\). Its tail after total \(n\), at a renewal there, obeys the exact normalized identity
\[
                           q+Z=v/2^n+2^{-n}Z'
\]
with \(|Z'|\le1\). Conditional on the bit at \(n\) being one, the preceding completed compositions of \(n\) are equally likely. By the residue result the conditional fractional part of \(v/2^n\) is uniform on the odd grid modulo one. The bit at \(n\) is asymptotically independent of each *fixed* bounded measurable function of the entire sequence: approximate that function in \(L^1\) by one depending only on its first \(k\) bits, then take \(n>k\). Testing continuous functions on the circle proves that \(Z\bmod1\) is exactly Haar-uniform. In particular its real law is absolutely continuous.

Let \(T=\operatorname{supp}Z\). It is compact, contained in \([-1,-1/2]\cup[0,1]\), and has positive Lebesgue measure. Its similarities are
\[
           \psi_e(z)=\bigl(2(-1)^{e+1}-2^{-e}\bigr)/3+2^{-e}z.
\]
The support is the union of their images up to the two possible limits of images as \(e\to\infty\). The images are Lebesgue-disjoint modulo null sets because their lengths add to \(|T|\). Therefore normalized Lebesgue measure on \(T\) satisfies the same distributional recurrence with branch weights \(2^{-e}\). It is the unique stationary probability on the bounded interval, by coupling with the same exponents and the contraction \(2^{-e}\le1/2\). Thus \(Z\) is uniform on \(T\). Haar-uniform fractional part implies that \(\sum_{k\in\mathbb Z}\mathbf1_T(x+k)=|T|\) for Lebesgue-almost every \(x\) modulo one. This makes \(|T|\) a positive integer. The displayed gap makes \(|T|<2\), so \(|T|=1\) and the multiplicity is one. In particular \([1/2,1]\subset T\) by compactness and the missing negative interval. Statement (2) already holds in the finite row.

Thicken each row point \(v/2^n\) to its half-open real grid cell of length \(2^{1-n}\). These cells are disjoint with total length one and lie within \(3\cdot2^{-n}\) of \(q+T\) by the infinite-tail identity. Their union therefore converges to \(q+T\) in measure, by compactness and \(|T|=1\). Consequently for every bounded odd arithmetic sequence \(f\) possessing an odd natural mean \(\bar f\),
\[
               2^{1-n}\sum_{v\in A_n(q)} f(v)\longrightarrow\bar f
                         \qquad \text{at every fixed }q.              \tag{3}
\]
Approximate \(q+T\) in measure by a finite union of intervals; on each interval the assertion for all odd lattice points follows by subtraction of the two natural partial sums. The symmetric-difference error is bounded by the sup norm of \(f\) times the difference area, apart from vanishing endpoint cells. This statement does not assume a natural mean for arbitrary arithmetic labels. In particular when a nonperiodic unit predecessor basin \(B_a\) has the positive odd natural density \(d_a\) of the retained Valbuena input, it has proportion \(d_a\) in every fixed row. Taking \(a=q\) yields a positive proportion of ordinary return sources to \(q\)'s component without requiring existence of a natural density for that entire component. [Fixed-root natural predecessor input](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md)

The window boundary satisfies an additional check. The branch \(\psi_5(T)\) lies strictly inside \((1/2,1)\). Every infinite code of a boundary point must therefore avoid the letter 5, since a finite composition maps the interior into the interior. Finite codes completed by a limit branch at infinity are also allowed. Fix \(\rho<2\) sufficiently close to 2 that \(\sum_{e\ge1,e\ne5}\rho^{-e}<1\). The number of admissible exact-cost \(m\) prefixes is at most \(\rho^m\) by induction. Stop at the last completed prefix with cost \(m<n\) before the next positive exponent reaches or passes \(n\). After such a prefix all next choices \(e\ge n-m\), including the two limiting endpoints, lie in two intervals of diameter \(O(2^{-n})\). This covers the boundary by \(O(\rho^n)\) intervals of that size, including individual terminal limit endpoints whose finite prefixes have cost \(<n\). An infinite sequence of limit-branch endpoints is already included by compactness or the same stopping description. It follows that its upper box dimension is at most \(\log_2\rho<1\). In particular the row's geometric symmetric-difference error is \(O((\rho/2)^n)\). No rate for a particular arithmetic natural mean is assumed in (3).

## At most polynomially many returns to the original escaping grade

Now fix an odd unit \(q\) in a hypothetical escaping ordinary component \(C\). Use its corrected height \(P(x)=x/F(x)\) and integer odd grade \(g(x)\). There are finite constants \(T=T(q,C)\) and \(B=B(q,C)\) such that
\[
        \#\{v\in A_n(q):\,v\in C,\ g(v)=g(q)\}
                      \ \le\ B(1+n)^T \qquad(n\ge1).                 \tag{4}
\]
The criterion is imposed only on the actual endpoint; the intermediate smaller-parent vertices may leave and re-enter the component.

First, write \(d(x)=P(x)-x\), \(b_x=3\,2^{-e(x)}\). The actual edge identity gives \(d(x)=1/3+d(Sx)/b_x\) with \(d>0\). Since every \(b_x\le3/2\), summing finite nonnegative contributions gives \(d(x)\ge1\) at every escaping \(x\). In fact, if \(j=v_2(q+1)\), the first \(j-1\) exponents are one, and the next is at least two: during this initial run \(S^i(q)+1=(3/2)^i(q+1)\), and the first \(1\bmod4\) state has even \(3x+1\) divisible by four. From that edge onward the inverse multiplier product is at least twice its all-ones lower bound. Summing the geometric tail gives
\[
                         P(q)\ \ge\ q+1+(2/3)^j .                    \tag{5}
\]

Every vertex of an escaping component exceeds the verified floor. The [independent distortion bound above the verified cutoff](../descent/DISTORTION.md) gives \(F(x)>5/6\), and Paper 175's lower-cutoff bound already gives \(4/5<F(x)\le1\) uniformly; see [the outer-band proof](UNIT_STRIPS.md). Every row endpoint satisfies \(q-1-2^{-n}/3\le v/2^n\le q+1\). For an endpoint in the same grade the lattice cocycle gives \(P(v)/(2^n P(q))\in2^{\mathbb Z}\). Since \(q>2^{68}\), the row bounds and \(4/5<F\le1\) put this dyadic ratio strictly between \(1/2\) and \(2\). Thus \(P(v)=2^nP(q)\), and
\[
                 F(v)\le(q+1)/P(q)<1.                               \tag{6}
\]
This is a fixed strict gap at the original \(q\) conferred by (5), even if arbitrarily many intermediate smaller-parent edges fail.

The uniform simple-path reciprocal tail now forces each such \(v\) to visit a fixed finite odd floor. Its visit to \(u\) there is at odd depth exactly \(g(u)-g(q)\). These finitely many nonnegative depths have a fixed maximum \(T\), taking zero if empty. For an odd path of length at most \(T\) from \(v=O_q(2^n)\), all states are \(O_{q,T}(2^n)\) by the forward one-step bound. Every exponent is consequently at most \(n+O_{q,T}(1)\). An endpoint \(u\) and its at most \(T\) reversed exponents determine \(v\) uniquely. Counting over the finite floor proves (4). Compared with the \(2^{n-1}\) exact-row size this bound is exponentially small up to the stated polynomial, on the same fixed ordinary source.

For a bounded range of grades \(g(v)-g(q)\), a qualitative \(o(2^n)\) return count also follows without (5). Each possible \(P(v)/(2^nP(q))=3^d2^\ell\) is one of finitely many numbers by the height and grade restrictions. Hence \(v/2^n\) belongs to a finite union of scalar multiples of the global compact null correction set in [Global correction gaps](GLOBAL_CORRECTION_GAPS.md). The grid-cell comparison bounds their row fraction by the measure of a shrinking neighborhood, which tends to zero. The strictly positive excess in (6), needed for the polynomial count, was proved for the original grade.

Together (3) and (4) show the exact distinction at one original source. Positive-density genuine predecessors return to its component, but the occupants of its original grade have exponentially small proportion. A way to convert those other grades into a cheaper witness below \(q\) remains open.

[ParentRows.lean](ParentRows.lean) checks the scaled affine composition, undoing a common final branch, the two parity bands, and propagation of the first strict gain in (5). [Strict axiom receipt](../../../reports/astra-sixhour-20261127/transport/parent-rows-lean.txt). The residue induction, limiting tile and conditional escaping-grade argument are written. [Independent integer enumeration](check_parent_rows.py) checks all endpoint residues, the exact real gap, and the mandatory interval for six ordinary seeds at costs 1 through 15. [Finite receipt](../../../reports/astra-sixhour-20261127/transport/parent-rows.json).
