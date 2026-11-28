# Every intermediate landing-clock rate occurs along a generic coherent ternary source

For \(n\ge1\) and a unit \(1\le m<3^n\), let \(\tau(n,m)\) denote the first integral landing clock of the positive shortcut source \(m/3^n\), and let \(J(n)=\max_m\tau(n,m)\). For a ternary unit \(z\in\mathbb Z_3^\times\), write \(m_n(z)\) for its least positive residue modulo \(3^n\). Use the compactified positive real line when allowing an infinite upper limit.

**Proposed theorem.** Put \(\Lambda=\limsup_{n\to\infty}J(n)/n\), so \(3\le\Lambda\le+\infty\). The complete set of subsequential limits of \(\tau(n,m)/n\) on the changing grids is the interval \([1,\Lambda]\). For a residual set of **single coherent ternary units** \(z\), the subsequential limits of \(\tau(n,m_n(z))/n\) form this same interval. For Haar-almost every such unit the only limit is two by the [complete-grid concentration theorem](TYPICAL_INTEGER_LANDING.md).

More generally take any prescribed countable list of positive functions \(f\) on the positive integers with \(f(n)\to\infty\) and \(f(n+j)/f(n)\to1\) for each fixed nonnegative integer \(j\). On one residual set, simultaneously for each such \(f\),
\[
    \limsup_{n\to\infty}\frac{\tau(n,m_n(z))}{f(n)}
                 =\limsup_{n\to\infty}\frac{J(n)}{f(n)}.                \tag{1}
\]
Consequently a pointwise \(O_z(f(n))\) bound on a nonmeager set of ternary units already implies \(J(n)=O(f(n))\). This holds for \(f(n)=n\log(2+n)\). The topology in these statements is ternary. The ordinary unmatched realizations of these grid records use different ordinary source cylinders.

## Exact prefix transplantation

For \(0<y\le1\) of reduced denominator \(3^h\), \(h\ge1\), choose
\[
             F(y)=\begin{cases}2y,&y\le1/2,\\(2y-1)/3,&y>1/2.\end{cases}
\]
Both branches are positive, at most one, and return to \(y\) by one actual native step. Writing \(y=d/3^h\), the new reduced numerator is \(2d\) on the first branch and \(2d-3^h\) on the second. Its denominator exponent is \(h\) or \(h+1\), respectively. In particular every added state stays nonintegral. Weaver used this same real inverse branch in the proof of (B10), with a harmless different convention at \(1/2\); an input of reduced denominator \(3^h>1\) cannot equal this boundary. His gap count gives the growth estimate used below. [Weaver, Paper 19/v2, §9.1, equations (B9)–(B10)](https://rstation.ai/problems/collatz/papers/19/v2)

Start at \(m/3^n\), and prescribe a unit \(a\bmod 3^k\) with \(1\le k\le n\). After \(e\) inverse dates its numerator is \(2^em\bmod3^k\), independently of the chosen branch history. The elementary order formula \(\operatorname{ord}_{3^k}2=2\cdot3^{k-1}\) follows from \(v_3(4^j-1)=1+v_3(j)\), by cubing and then taking powers coprime to three. Choose \(0\le e<2\cdot3^{k-1}\) to attain \(a\). The resulting admissible grid entry \(m'/3^{n'}\) satisfies
\[
   m'\equiv a\pmod{3^k},\qquad n\le n'\le n+e,\qquad
                         \tau(n',m')=\tau(n,m)+e.                       \tag{2}
\]
The entire old native trajectory occurs after the added prefix. In particular this transplantation can preserve an arbitrarily long old record, however narrow its binary cylinder.

For any fixed cylinder, the additive changes in (2) are bounded independently of the record height. Sets defined by a finite-height strict bound on \(\tau(n,m_n(z))/f(n)\) are open and closed. For every threshold strictly below the right side of (1), the union of the open exceedance sets over \(n\ge N\) is dense for every \(N\), by (2) and shift stability. Taking a countable intersection of these open dense sets proves (1); the reverse inequality holds pointwise by the maximum definition. The case of right side zero needs only that pointwise inequality. The same argument transfers any subsequential finite rate on the complete grids into the cluster set of a residual collection of coherent sources. For finite rates, both additive changes in (2) alter \(\tau/n\) by \(o(1)\) as the starting heights tend to infinity.

## Filling the interval of rates

At every sufficiently large height there is a witness with \(\tau=n\). The all-odd shortcut word of length \(n\) holds for inputs congruent to \(-1\bmod 2^n\). Pick \(1\le m<3^n\) prime to three with \(m\equiv-3^n\bmod2^n\); for large \(n\) the interval contains at least three consecutive representatives of this binary class. Each of the \(n\) letters removes a denominator factor three.

After an odd inverse departure of \(F\), the value is at most \(1/3\). From such a value \(y\), the next inverse odd departure is completed after the least \(e\ge1\) with \(2^e y>1\), and its value becomes \((2^e y-1)/3\). Thus \(e\ge2\), and \(e=2\) makes the new value at most \(1/9\), forcing the following gap to be at least four. Pair each two with its following gap. Over \(E\) native inverse dates from any permitted start, the number \(r_E\) of added odd grades is at most \(E/3+2\), and it tends to infinity with \(E\) because consecutive doublings of a positive real eventually exceed one half. The native inverse from \(1/3\), which originally lands at \(1\) in one step, passes through every height \(n\) and yields \(J(n)\ge3n-O(1)\). This lower bound uses the existing (B10) gap estimate on actual reduced rational lifts.

Now start from a fast witness at height \(n\). At inverse date \(E\) the rate is \((n+E)/(n+r_E)\). Its liminf is at least three as \(E\to\infty\). On one native step the upward change is at most \(1/n\): an unchanged height gains one date, and at a simultaneous increment of numerator clock and height a rate already at least one cannot increase. Thus every fixed rate in \((1,3)\) is crossed upwards with overshoot at most \(1/n\), along arbitrarily large starting heights.

For downward crossings, start from any grid witness \(y=m/3^n\). Choose the unique integer \(e\ge1\) with \(2<2^e y\le4\). The inverse odd source \(y'=(2^e y-1)/3\) has real value in \((1/3,1]\), reduced denominator \(3^{n+1}\), and a true native word consisting of one odd then \(e-1\) evens to \(y\). Intermediate states may exceed one. The endpoint before this word is the admissible grid entry \(y'\). Continue in the same way. After the first choice each \(e\) is two or three. A three occurs only from \(y\le1/2\) and gives \(y'>(8/3-1)/3=5/9>1/2\), hence is followed by a two. From any starting record the limsup mean cost of this extension is at most \(5/2\) per added grade.

Take \(5/2<\alpha<\Lambda\) and arbitrarily high records with rates greater than \(\alpha\). The endpoint rates of these extensions eventually cross down to \(\alpha\) or below. At the first such crossing from height \(h\), the new clock is at least \(\alpha h+1\), so the undershoot is at most \((\alpha-1)/(h+1)\). This gives \(\alpha\) as a subsequential limit; upward crossings already cover every smaller interior rate. The endpoints one and \(\Lambda\) follow from the minimum examples and the definition of limsup. No larger finite rate or rate below one is possible. Apply (2) to a countable dense set of rates and use closedness of the cluster set in the compactified line to prove the coherent version. In fact the exact \(\tau=n\) witnesses can be chosen in any fixed ternary source cylinder by the Chinese remainder theorem for \(2^n\) and \(3^k\) once \(3^n\ge 2^n3^k\). Thus a residual set attains exact equality infinitely often.

## Precision required of an ordinary numerator

If the new numerator is required to equal one fixed ordinary unit \(m_0>0\), any true inverse prefix of length \(e\) from a height-\(n\) record \(m/3^n\) must satisfy
\[
                              2^e m\equiv m_0\pmod{3^n}.                \tag{3}
\]
This follows for every positive inverse word, including those leaving the unit interval: the even predecessor doubles the current numerator, and the odd predecessor doubles it then subtracts the current denominator. Heights never decrease backwards. At full height the least nonnegative exponent in (3) ranges over all \(2\cdot3^{n-1}\) possibilities as the original unit \(m\) ranges over its grid. Thus the **necessary** discrete-logarithm cost can be exponential for specified entries. No such lower bound has been established here for the maximizing entries. Satisfying the congruence alone need not make the resulting numerator exactly \(m_0\). This identifies the distinction between extending into any fixed cylinder and extending to one fixed ordinary numerator at every record height.
