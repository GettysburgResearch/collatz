# The arithmetic capacity of equal-grade paired returns

**PROPOSED.** Let \(T(2n)=n,\ T(2n+1)=3n+2\). Consider a pair of positive ordinary trajectories starting at \((Y,3Y-1)\). A clock applies \(T\) to each coordinate. A return of length \(H\) ends at \((X,3X-1)\), for a specified positive ordinary \(X\). Its grade is \(p\) if each arm takes exactly \(p\) odd departures. The result below limits the number of ternary residue classes the initial \(Y\) can occupy when the target \(X\) is fixed. It uses no regularity assumption about Collatz components.

## O4. Clock bound before a merger

Write \(x_t=T^tY,\ y_t=T^t(3Y-1)\). Let \(a_t,b_t\) count odd departures on the respective arms before clock \(t\). Introduce
\[
 r_t=1+b_t-a_t,\qquad
 C_t=3^{(-r_t)_+}y_t-3^{(r_t)_+}x_t,\qquad C_0=-1 .
\]
If \(x_H\ne y_H\), then \(C_t\ne0\) for \(0\le t\le H\). Indeed \(y_t\) stays prime to three. Once \(a_t>0\), \(x_t\) also stays prime to three, since an odd step gives residue two while division by two preserves ternary units. If \(a_t=0\), then \(r_t>0\), so the first term in \(C_t\) is a unit and the second is divisible by three. When \(a_t>0\), equality of the two terms would force \(r_t=0\) by their ternary valuations, and then \(x_t=y_t\). An actual merger would persist through clock \(H\). Every ordinary return has distinct endpoints because \(X\ne3X-1\).

Let \(e,f\in\{0,1\}\) give the parity of \(x_t,y_t\); put \(r'=r_t+f-e\). Substitution in the ordinary shortcut formulas gives
\[
 2C_{t+1}=A C_t+B,\quad
 A=3^{(-r')_++f-(-r_t)_+}
  =3^{(r')_++e-(r_t)_+}\in\{1,3\},\quad
 B=3^{(-r')_+}f-3^{(r')_+}e.
\]
For \(e=f=0\), this reads \(2C_{t+1}=C_t\). At any other clock \(\lvert B\rvert\le3^{|r'|}\), and \(\lvert C_t\rvert\ge1\). Multiplication of the one-step bounds and cancellation of the intermediate absolute values therefore give the integer inequality
\[
 2^H\ \le\prod_{t:\,e+f>0}\big(3+3^{|r_{t+1}|}\big).
 \tag{1}
\]
The same clock bound works for any nonmerged final pair, even when its endpoint lies off the return line.

Suppose each arm has \(p\) odd departures. Let \(s\) count simultaneous odd departures and \(u=p-s\); exactly \(u\) solo departures occur on each arm. Ignore simultaneous steps momentarily. After the \(j\)-th solo departure, \(1\le j\le2u\), the distance of \(r\) from one is at most \(\min(j,2u-j)\), since the path starts and ends at rank one. The sum of these bounds is \(u^2\). Each of the \(s\) simultaneous odd clocks contributes at most \(u+1\) to \(\max(1,|r|)\). Over all \(p+u\) active clocks this yields
\[
 \sum_{\rm active}\max(1,|r_{t+1}|)\le 2u+u^2+s(u+1)
 =p(u+1)+u\le p^2+2p.
\]
Using \(3+3^{|r|}\le2\cdot3^{\max(1,|r|)}\) in (1) yields
\[
 \boxed{\,2^H\le2^{2p}3^{p^2+2p}\,}.
 \tag{2}
\]
If \(R=\max_{0\le t\le H}|r_t|\), then \(R\ge1\) and (1) also gives \(2^H\le(2\cdot3^R)^{2p}\). In particular \(H\le2p(1+R\log_2 3)\). For zero grade (1) gives \(H=0\).

## O5. Cost of covering ternary classes from one terminal pair

Fix \(X\) and an integer budget \(P\ge1\). Put \(D=\lfloor2P+(P^2+2P)\log_2 3\rfloor\). For a given length \(H\) and lower parity word of weight \(p\), the lower-arm equation is \(2^H X=3^pY+c\), where \(c\) is determined by the word. Consequently there is at most one possible ordinary \(Y\), including before the upper-arm conditions are imposed. Summing over lengths by the hockey-stick identity, the number of distinct ordinary sources of grade at most \(P\) is bounded above by
\[
 \sum_{p=0}^P\sum_{H=0}^D {H\choose p}
 =\sum_{p=0}^P{D+1\choose p+1}
 \le(P+1)\left(\frac{e(D+1)}{P+1}\right)^{P+1}.
 \tag{3}
\]
Here \(D\ge2P+1\), so the binomial coefficients in the last sum are increasing. The resulting \(\exp(O(P\log(P+1)))\) bound is uniform in \(X\), with no separately imposed limit on \(H\) or on source height. Projecting these actual \(Y\)'s into any residue ring can only reduce their number. To cover even the \(2\cdot3^{L-1}\) ternary units modulo \(3^L\) requires \(P\log(P+1)\gg L\), hence \(P\gg L/\log(2+L)\). This excludes \(P=O(L^\alpha)\) for every fixed \(\alpha<1\) in a paired analogue of the single-arm all-class construction.

If every allowed path also has \(R\le R_0\), replace \(D\) by \(\lfloor2P(1+R_0\log_2 3)\rfloor\) in (3). The resulting covering requirement is \(L\ll(P+1)\log(2+R_0)\). In particular any such uniform covering with \(P=o(L)\) requires maximum relative rank at least \(\exp(\Omega(L/(P+1)))\). A single rank-one terminal does not control the interior rank.

Each counting assertion fixes the ordinary target \(X\) first. The set of possible \(Y\) may change with \(X,P\), and the same fixed target may admit a cheaply reachable particular class. Equations (1)–(3) impose no lower bound on the cost of the one specially chosen class used in the canonical portal.

**Lean scope.** [PairedCapacity.lean](PairedCapacity.lean) verifies the physical nonvanishing, the exact update, individual cost, product (1), the common-budget bound \(2^H\le(3+3^{P+1})^{2P}\) allowing unequal grades, and the uniqueness of an ordinary source at fixed lower parity word and endpoint. It imports mathlib and defines the positive shortcut arithmetic directly on naturals. The sharpened equal-grade excursion area in (2), binomial summation in (3), and asymptotic covering estimates are written arguments. [Compiler and axiom output](../../../reports/astra-unconventional-20261126/operator/paired_capacity_lean.txt).
