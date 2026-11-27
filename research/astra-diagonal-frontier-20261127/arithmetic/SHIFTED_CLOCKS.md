# Integer halves of a binary ordinary cycle preserve the homogeneous clock

Let \(2^{a_i}x_{i+1}=3x_i+1\) be a primitive ordinary positive cycle of odd period \(p\), clock \(A=\sum a_i\), minimum \(s>1\) and maximum \(X\). Here every \(a_i\) belongs to \(\{1,2\}\). Let \(H_N\) send each positive real \(v\) to the least dyadic lift of an odd integer at most \(N\) that is at least \(3v\), for \(N\) odd. Its rotation \(\rho_N\) is decreasing in \(N\), in the weak sense, and depends only on the grid. [Homogeneous ceiling and Farey switches](HOMOGENEOUS_MEETINGS.md)

The two positive integral lists \(u_i^-=(x_i-1)/2\) and \(u_i^+=(x_i+1)/2\) satisfy
\[
 2^{a_i}u^-_{i+1}-3u^-_i=\mathbf1_{a_i=1},\qquad
 2^{a_i}u^+_{i+1}-3u^+_i=\mathbf1_{a_i=2}.                      \tag{1}
\]
In particular \(H_N\) has the **exact original clock** \(\rho_N=A/p\) on each of the following sets of odd cutoffs, whenever that set is nonempty:
\[
 \begin{array}{c|c}
 \text{integer representatives along the orbit}&\text{cutoffs}\\ \hline
 u_i^- & (X-2)/3\le N<3(s-1)/2\\
 u_i^+ & (X+1)/2\le N<2s+1\\
 x_i   & X\le N<3s .
 \end{array}                                                       \tag{2}
\]
Every odd cutoff between the smallest and largest cutoffs in these nonempty sets has the same clock by monotonicity. Thus along any sequence with \(s\to\infty\), fixed \(X/s\le R<4\) gives a common homogeneous plateau from \((X-2)/3\) up to \(2s\), with endpoints restricted to odd integers. Fixed \(R<3\) raises the upper end to \(3s-1\). Under fixed \(R<9/2\), at least the first shifted interval is nonempty eventually. The exact intervals (2) retain parity and strict endpoint conventions.

## Divisibility and exact endpoints

Equation (1) follows by substitution and \(2^a-3\in\{-1,1\}\). Both valuations occur on any nontrivial positive cycle, since an exponent-one edge increases its source while an exponent-two edge strictly decreases any source above one. At a unit-defect edge \(2^a u'=3u+1\) the source \(u\) is odd. If \(3u>N\), every dyadic noninteger above \(3u\) has odd part greater than \(N\). Thus when the target \(3u+1\) is eligible, it is the homogeneous ceiling. On zero-defect edges the true target is already the exact triple and only its eligibility is needed. A sufficient condition is consequently
\[
 \max_i\operatorname{oddpart}(u_i)\le N<3\min_{i:\,2^{a_i}u_{i+1}-3u_i=1}u_i .
\]
This lifts the entire cyclic list. Its logarithmic rotation is \(A/p\), even if an odd part repeats in the list. The argument uses the ordinary full denominator one through positive integer odd parts of \(u_i^\pm\).

At the minimum the outgoing exponent is one and the incoming exponent is two. At the maximum the outgoing exponent is two and the incoming exponent is one. The largest exponent-one source is therefore \((2X-1)/3\), and the least exponent-two source is \((4s-1)/3\). At an exponent-one source \(u^-\) is odd. Its largest such value is \((X-2)/3\). At an exponent-two source \(x\equiv1\bmod8\), so \(4\mid u^-\) and \(\operatorname{oddpart}(u^-)\le(X-1)/8<(X-2)/3\) for \(X>3\). The least exponent-one \(u^-\) is \((s-1)/2\). At the maximum \(u^+=(X+1)/2\) is odd and attains its largest odd-part value. The least exponent-two \(u^+\) is \((2s+1)/3\). These give the first two rows. The last row follows directly from \(3x\ge3s>N\).

There is another integral representation \(v_i=\lfloor x_i/3\rfloor\). Write \(r_i=x_i\bmod3\in\{1,2\}\). The previous exponent determines \(r_i\), and \(2^{a_{i-1}}r_i=4\). Therefore
\[
 v_i=2^{1-a_{i-1}}u_{i-1}^-,\qquad
 2^{a_i}v_{i+1}-3v_i=r_i-1.
\]
This construction has precisely the same dyadic orbit as the minus representation with a one-step shift.

## A universal bounded adjustment cannot keep dividing by arbitrary integers

Suppose a proposed local rule treats every finite ordinary binary valuation path. Fix a divisor \(M\ge1\). Ask the rule to output positive integers \(u_i=(x_i+t_i)/M\), with a uniform bound \(|t_i|\le K_M\), and auxiliary defects \(b_i=2^{a_i}u_{i+1}-3u_i\in\{0,1\}\) at every edge. This imposes
\[
            1+2^{a_i}t_{i+1}-3t_i=M b_i,\qquad t_i\equiv-x_i\bmod M.       \tag{3}
\]
Even a choice depending on the entire finite input path cannot satisfy these requirements on all paths for any \(M\ge4\).

To see this use longer and longer finite binary words cut from the two-sided calendar
\[
    \cdots 222\mid 1,2\mid 111\cdots .
\]
The two central exponents are \(a_0=1,a_1=2\). Each finite word is realized as an actual positive odd integer trajectory by the dyadic cylinder construction. For \(M=7,11\), also impose \(x_0\equiv0\bmod M\) at its first central edge. This is an independent unit-prime congruence on the initial integer because both 2 and 3 are units there. The realizing integers may be chosen as large as needed. Bounded integral offsets on successively longer words would admit, by diagonal extraction in a finite alphabet, a two-sided solution of (3) on this calendar.

Along the exponent-two past, \(t_{i+1}+1\ge(3/4)(t_i+1)\). Boundedness sent from the remote past gives \(t_0\ge-1\). Along the exponent-one future, \(t_i-1\le(2/3)(t_{i+1}-1)\), so \(t_2\le1\). Propagating these one-sided bounds across the two central edges gives
\[
 -1\le t_0\le1,\qquad -2\le t_1\le1,\qquad -1\le t_2\le1 .
\]
For \(M\ge12\) both central defects must be zero because their unscaled nonnegative numerators cannot exceed 11. But \(2t_1=3t_0-1,\ 4t_2=3t_1-1\) have no such integer triple. For \(4\le M\le11\), direct enumeration of these 36 triples leaves only \(M=7\) with \((-1,-2,0)\), or \(M=11\) with \((-1,-2,1)\). Both violate the imposed central congruence \(t_0\equiv0\bmod M\). This proves the obstruction on literal finite ordinary paths. Divisors 2 and 3 do admit the explicit positive constructions above on paths of large enough minimum.

This obstruction concerns the requirement of one bounded adjustment for **all** binary paths. Its two long constant tails leave every fixed physical ratio. Restricting the rule to candidates in a bounded physical strip, or allowing other auxiliary digits, remains open. The plateaus (2) themselves give no upper bound on homogeneous plateau width for arbitrary cutoffs and do not exclude a positive cycle.

[Exact ordinary-edge and cutoff controls](check_shifted_clocks.py) · [Recorded controls](shifted_clock_controls.json)
