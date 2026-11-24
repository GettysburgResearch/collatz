# Equal counting exponents in every fixed gap and ternary cylinder of an ordinary basin

**PROPOSED written corollary.** Fix a positive odd ternary-unit target \(t\). In its ordinary predecessor basin, imposing any finite list of initial accelerated Collatz gaps and any source congruence modulo a power of three preserves both the lower and the upper logarithmic counting exponent. The proof gives an explicit comparison of counts at a constant factor change of cutoff.

The input is the finite gluing theorem in `BRIDGE_AUDIT.md`, Git blob `9cadbfab1677a0ec6e021ad1279361c73e527332`, SHA-256 `5f73fac2bac5056dd9d40b1576122c46c7e322c817f1714d28955425a84c6e96`. The proof below includes the strengthening from sufficiently large exponents to every positive representative.

## Exact predecessors of one target

Write \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on the positive odd integers. Fix a word \(w=(a_0,\ldots,a_{n-1})\) of positive integers, \(m\ge0\) and \(u\bmod3^m\). Either the word or the congruence restriction may be empty. Let \(\mathcal C\) contain the positive odd \(x\) with these first \(n\) gaps and \(x\equiv u\pmod{3^m}\). Set

\[
A_i=\sum_{j<i}a_j,\quad A=A_n,\quad C=\sum_{i<n}3^{n-1-i}2^{A_i},
\qquad P=2\cdot3^{n+m}.
\]

For each positive odd \(z\) coprime to three, there is a unique \(r_0(z)\in\{1,\ldots,P\}\) satisfying

\[
2^{r_0(z)}\equiv
(2^A+3C+3^{n+1}u)(2^A z)^{-1}\pmod{3^{n+m+1}}.
\]

The right hand side is a unit. The order of 2 modulo \(3^h\) equals \(2\cdot3^{h-1}\), by \(v_3(4^{3^j}-1)=j+1\) and reduction modulo 3. Put

\[
c=\frac{2^A}{3^{n+1}},\qquad e=\frac{2^A+3C}{3^{n+1}}.
\]

The complete set \(\{x\in\mathcal C: U^{n+1}(x)=z\}\) consists of the distinct integers

\[
x_k=c z\,2^{r_0(z)+kP}-e,\qquad k=0,1,2,\ldots .
\]

Indeed, the full affine equation for \(w\) followed by the terminal gap \(r\) forces this expression and congruence. Conversely, a positive representative \(r\) gives integral \(Q=(2^r z-1)/3\), integral \(x\), and each intermediate quotient is integral by splitting the word carry and canceling the power of two modulo the remaining power of three. Equivalently, modulo \(3^{n-i}\) the complete carry is \(2^{A_i}C_{i,n}\), so \(2^{A-A_i}Q-C_{i,n}\) is divisible by \(3^{n-i}\). Backward induction starts at the positive odd \(z\). Each new integral predecessor \((2^g y-1)/3\) of a positive odd \(y\) with \(g\ge1\) is positive and odd, proving exact legality even for the smallest positive \(r\). The expression is strictly increasing with \(r\).

In particular, at this exact depth the count through a real cutoff \(X\ge1\) is

\[
\max\!\left(0,\,1+\left\lfloor\frac{\log_2((X+e)/(cz))-r_0(z)}P\right\rfloor\right)
=\frac{\log_2 X}P+O_{w,m,u,z}(1).
\]

The choice of the least representative defines \(L(z)=x_0\) for *every* ternary-unit target \(z\). With the same constant for all such \(z\),

\[
U^{n+1}(L(z))=z,\qquad L(z)\in\mathcal C,\qquad
L(z)\le K z,\qquad K=\frac{2^{A+P}}{3^{n+1}} .
\]

The map \(L\) is injective because applying \(U^{n+1}\) recovers \(z\).

## Counts in the fixed ordinary basin

Define \(B_t=\{y>0: y\text{ odd and }U^j(y)=t\text{ for some }j\ge0\}\) and \(N_E(X)=\#\{y\in E:y\le X\}\). Then for every \(X\ge1\),

\[
N_{B_t\cap\mathcal C}(X)\le N_{B_t}(X)
\le 2N_{B_t\cap\mathcal C}\big(K(4X+1)\big)
\le 2N_{B_t\cap\mathcal C}(5KX).
\]

To see the second inequality, send a ternary-unit \(y\in B_t\) to \(z=y\), and a nonunit \(y\in B_t\) to \(z=4y+1\). In the latter case \(z\equiv1\pmod3\) and

\[
3z+1=4(3y+1),\qquad U(z)=U(y).
\]

Since \(t\) is a unit, a nonunit \(y\) in its basin is at least one step before a visit to \(t\). The common successor therefore still belongs to \(B_t\), so \(z\in B_t\). Each \(z\) has at most two preimages under this operation, one from each branch. The map \(z\mapsto L(z)\) is injective and returns a source in \(B_t\cap\mathcal C\). The composite has multiplicity at most two and sends \(y\le X\) to a source at most \(K(4X+1)\).

Consequently, for \(\star=\liminf\) and for \(\star=\limsup\),

\[
\underset{X\to\infty}{\star}
\frac{\log(1+N_{B_t\cap\mathcal C}(X))}{\log X}
=
\underset{X\to\infty}{\star}
\frac{\log(1+N_{B_t}(X))}{\log X}.
\]

The additive constant in the logarithm, the factor two in the count and a fixed factor in \(X\) leave both exponents unchanged. For example, any eventual lower bound \(N_{B_t}(X)\ge c_0X^\delta\) for fixed \(t\) and \(\delta>0\) yields \(N_{B_t\cap\mathcal C}(X)\ge c_0X^\delta/(2(5K)^\delta)\) for all sufficiently large \(X\).

The same proof applies to an entire ordinary component defined by eventual intersection with the forward orbit of a fixed target. Sharing a successor preserves that component even when the target itself is divisible by three.

## Specifying ordinary residue classes

One may instead prescribe any odd residue modulo \(2^k\), together with the ternary residue \(u\bmod3^m\). Choose one positive odd representative of the dyadic class, follow its actual gaps until \(A+1\ge k\), and retain that finite word. The terminal state is odd, so every positive source executing this word satisfies \(3^n x+C\equiv2^A\pmod{2^{A+1}}\). This is one source class because \(3^n\) is odd. The resulting gap cylinder thus lies inside the desired dyadic cylinder. The preceding lower comparison and the trivial inclusion upper bound give the same two exponent equalities there.

The comparison keeps the target or component fixed while its predecessor sources vary. The displayed \(P=2\cdot3^{n+m}\) occurs in the exponent of 2 in \(K\), so a varying cylinder can require a doubly exponential change in cutoff. A lower collision dimension for the time averages of one fixed forward orbit, a descent of every positive source and exclusion of nontrivial cycles remain open.
