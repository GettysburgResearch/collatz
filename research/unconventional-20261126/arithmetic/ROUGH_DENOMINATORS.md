# Mechanical cycle minima that avoid every prescribed finite collection of primes

**Status.** Proposed written theorem. The congruence construction and the two-place comparison below are elementary. One consequence about competing inverse paths is explicitly conditional on PR200's depth-192 certificate. The examples are positive rational cycles of the odd Collatz map on fractions of denominator coprime to six. Their numerators obey the generalized integer map with addend equal to the denominator.

Let \(\alpha=\log_2 3\). Use the two-sided coordinates \(u_2,u_3\) from [the integer bound](MIXED_MECHANICAL.md) at intercept \(t=0\). Write \(P^-(D)\) for the least prime divisor of \(D>1\).

**R1.** For every \(0<\epsilon<1\) and every integer \(M\ge1\) coprime to six, there exist infinitely many primitive positive rational cycles of least odd period \(p\to\infty\), with minimum \(s\), such that
\[
 \begin{gathered}
 s\gg_\epsilon p^{2-\epsilon},\qquad s\ll p^2,\qquad
           s\le x<2s\quad\text{at every odd phase},\\
 D=2^A-3^p\text{ is the full reduced denominator of every phase},\quad
 D\equiv-2\pmod M,\quad
 P^-(D)\ge c_\epsilon\log p,\\
 2^{v_2(s-u_2)}3^{v_3(s-u_3)}
        \ge \exp(c_\epsilon p^{1-\epsilon}).
 \end{gathered}
\]
Here \(A\) is the physical period in the shortcut clock. All sufficiently late members of each sequence enjoy the estimates, with the threshold allowed to depend on \(M\). In fact \(\log D\asymp p\), so the least-prime bound is also \(\gg_\epsilon\log\log D\). In particular no uniform polynomial in the real value of an approximant can replace the left side's restriction to ordinary integers, even if integrality at arbitrarily many prescribed places is retained. A polynomial in the full rational height is a different question.

### Primitive approximation in a congruence class

Take any upper regular continued-fraction convergent \(P/Q\) to \(\alpha\) with preceding lower convergent \(P'/Q'\). Write \(v=(P,Q)\), \(w=(P',Q')\). At large indices \(0<Q'<Q\), the determinant \(P Q'-P'Q=1\), and \(v\) and \(v-w\) are an integral basis. Both lie above the target line, since \(0<P-Q\alpha<1/Q\) and \(0<Q'\alpha-P'<1/Q\). The slope of \(v-w\) is strictly above that of \(v\).

For a positive integer \(L\), express the residue \((0,1)\) as \(a_0v+b_0(v-w)\pmod L\). No prime divisor of \(L\) divides both \(a_0,b_0\) by unimodularity. Choose \(1\le a\le L\) representing \(a_0\). Let \(K\) be the product of the distinct primes dividing \(a\) but not \(L\). The congruences \(b=b_0\pmod L\) and \(b=1\pmod K\) have a representative \(1\le b\le LK\le L^2\). Every prime divisor of \(a\) then fails to divide \(b\). This also works for \(L=1\). Consequently
\[
  (A,p)=av+b(v-w)
\]
is primitive, \(A=0\pmod L,\ p=1\pmod L\), and its slope is strictly between those of \(v\) and \(v-w\). The same basis gives the quantitative controls
\[
 Q\le p\le 2L^2Q,\qquad
  b/Q < A-p\alpha <3L^2/Q.                               \tag{1}
\]
For the lower bound use \(AQ-pP=b\) and \(P/Q>\alpha\).

Let \(y=c\log Q\) with small \(c=c(\epsilon)>0\), and take \(L\) to be the least common multiple of \(\varphi(M)\) and all \(\ell-1\) for primes \(3<\ell\le y\). Then \(D\equiv1-3=-2\pmod M\), and similarly modulo each of these primes, by Euler's theorem. The primes two and three already do not divide \(D\). For completeness \(\log\operatorname{lcm}(1,\ldots,n)=O(n)\) follows elementarily: each prime power in \((m,2m]\) contributes its prime to \(\binom{2m}{m}\), by the factorial valuation formula. At most one power of each prime occurs in this interval. Thus the lcm at \(2m\) is at most the lcm at \(m\) times \(4^m\). Induction at powers of two and monotonicity give \(\operatorname{lcm}(1,\ldots,n)\le4^{2n}\) for \(n\ge1\).

Choose \(0<\tau<\epsilon/8\). Taking \(c\) sufficiently small and then \(Q\) sufficiently large gives \(L\le Q^\tau\). Put \(\delta=A-p\alpha\). Equations (1) give \(\delta\le3Q^{-1+2\tau}\), \(p\le2Q^{1+2\tau}\), hence
\[
 \delta\ll_\epsilon p^{-1+\epsilon},\quad
 Q\gg_\epsilon p^{1-\epsilon},\quad
 y\gg_\epsilon\log p.
\]
We retain \(\delta>1/Q\), which gives the complementary upper height bound below.

### Complete denominator and minimum

For slope \(A/p\), use the backwards gap word with prefix sums \(S_j=\lceil jA/p\rceil\), \(1\le j\le p\), and define
\[
 C=\sum_{j=1}^p3^{j-1}2^{A-S_j},\qquad D=2^A-3^p.
\]
The inverse recurrence gives \(s=C/D\) as its positive fixed phase. Every cyclic shift has a positive odd numerator by the identical rotation formula. The inverse identities \(3x_{j+1}+1=2^{e_j}x_j\) give physical forward valuations and the same common full denominator before reduction. The primitive period is \(p\) since the clock pair is primitive. The suffix clocks for this upper word are \(\lfloor hA/p\rfloor\), \(0\le h<p\); for all other rotations the suffix clocks are these floors or one higher. Thus the selected phase is a minimum and every other phase is strictly less than twice its value (the \(h=0\) term is common). Also
\[
 {p\over6}\le {C\over3^p}
 ={1\over3}\sum_{h=0}^{p-1}{2^{\lfloor hA/p\rfloor}\over3^h}
 \le {p\over3}2^\delta.
\]
This gives \(s\asymp p/\delta\) when \(0<\delta<1\). With (1), we obtain the asserted bounds on \(s\), and
\( D=3^p(2^\delta-1)\asymp 3^p\delta\) has \(\log D\asymp p\).

We reproduce PR200's full-denominator arithmetic to keep the coprimality assertion attached to its hypothesis. Let the prefix sums of the cyclic rotations be
\(S_j(t)=\lfloor(jA+t)/p\rfloor\), \(0\le t<p\). These are rotations because \(A\) is a unit modulo \(p\). Between neighboring \(t\) and \(t+1\) with \(t<p-1\), exactly one internal prefix sum rises by one. Consequently their carries differ by a nonzero product of powers of two and three. The cyclic inverse equation \(3C'=2^e C-D\) preserves the gcd of the carry with \(D\), since \(D\) is prime to six. The common gcd divides a nonzero integer supported at the primes two and three and hence is one. Here \(p\to\infty\) so \(p\ge2\). [PR200, minimum-closure, Theorem R](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md)

### Both local agreements

The neighboring fractions \(P'/Q'\) and \(P/Q\) have determinant one. So do \(P/Q\) and \((P-P')/(Q-Q')\). Any fraction strictly between determinant-one neighbors has denominator at least the sum of their denominators, since its numerator/denominator vector is a positive integral combination of the two endpoint vectors. Thus there is no rational of denominator less than \(Q\) between \(\alpha\) and \(A/p\), including endpoints. Consequently the floors and ceilings of \(j\alpha\) and \(jA/p\) agree for every \(1\le j<Q\).

The backwards word from the cycle minimum has prefix sums \(\lceil jA/p\rceil\), and its forward word has prefix sums \(\lfloor jA/p\rfloor\) by reversing the lap. The backward affine congruence now gives \(s=u_3\pmod{3^{Q-1}}\). Equal forward gaps with odd terminals give \(s=u_2\pmod{2^{\lfloor(Q-1)\alpha\rfloor+1}}\). This proves the simultaneous lower bound in R1. Meanwhile the upper bound \(s\ll p^2\) guarantees this precision eventually exceeds any fixed power of its real size.

For an additional fixed finite set of primes, absorb its primes above three into \(M\). Successively taking \(M\) divisible by all previously produced denominators also gives a sequence with pairwise coprime full denominators, with the requested size and precision estimates on selected members. The new condition is imposed at each stage before choosing an arbitrarily large upper convergent.

### What the inverse screen adds

All sufficiently late slopes lie in PR200's interval \((84/53,485/306)\). Its universal 192-depth inverse-word theorem therefore applies at every phase. In PR200's notation \(q=(2s+1)/3\) and \(n=2s+1\) give its ternary multiple merging with this cycle, and every competing positive rational inverse ending at a ternary multiple within 192 odd steps is at least \(n\). This uses the upstream theorem at its stated bound. It does **not** establish an all-depth basin minimum for the new unbounded family. PR200's six small all-depth models have a separate finite fate certificate and separate quantifiers. [PR200, I192 and inverse-path hypotheses](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md) · [PR200, all-depth model scope](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/RATIONAL_MINIMA.md)

Lagarias's rational-cycle correspondence and terminal-zero construction provide historical context. The fixed-numerator deformation in his Theorem 3.4 need not avoid a prescribed prime set, produce near-critical large minima, or control other components in the basin. Halbeisen and Hungerbühler give classical balanced-cycle minimum bounds. No priority is claimed for the mechanical cycle itself or its minimum extremality. [Lagarias, Acta Arithmetica 56 (1990)](https://doi.org/10.4064/aa-56-1-33-53) · [Halbeisen and Hungerbühler, Acta Arithmetica 78 (1997)](https://user.math.uzh.ch/halbeisen/publications/pdf/collatz.pdf)
