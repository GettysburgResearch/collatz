# A full rank attempt: exact debit, ordinary refill, and global charge

**Status.** The current-type rank and the specified summable atomic repair
are refuted. The full rational envelope is evaluated exactly. Its restricted
inverse-tree version is OPEN. Only the finite algebra and ordinary arithmetic
identified in `lean/ClosureDiagnostics.lean` have been checked in Lean.

## 1. What would have closed the problem

A nonnegative integer-valued rank that strictly decreases along some finite
actual return from every positive odd source above one would prove
termination. A bounded-below real expression with a uniform positive debit
would also suffice. The candidates below try to pay for all ordinary height
growth, including switches between run types. Finiteness of a charge and a
debit within one type are insufficient by themselves.

Write \(y=2^a u-1\), with \(u\) positive odd and \(a\ge1\), and put
\(b=v_2(3^a u-1)\ge1\). After \(a\) consecutive odd shortcut inputs
and \(b\) consecutive even inputs, the next odd valley is

\[
z=(Py+C)/Q,\quad P=3^a,\quad Q=2^{a+b},\quad C=P-2^a.
\]

For \(D(y)=(P-Q)y+C\), exact algebra gives

\[
QD(z)=PD(y),\qquad v_2(D(z))=v_2(D(y))-(a+b)
\]

when the same defect is used at both ends and it is nonzero. Since
\(P\) is odd, this pays a definite valuation debit even on an expansive
branch. The candidate proof tried to use it to dominate growth of
\(\log_2 y\).

## 2. A switch on positive ordinary integers breaks the current charge

For every integer \(t\ge0\), the literal shortcut paths are

\[
\begin{aligned}
512t+91&\to768t+137\to1152t+206\to576t+103,\\
576t+103&\to864t+155\to1296t+233\to1944t+350\to972t+175.
\end{aligned}
\]

Their types are exactly \((2,1)\) followed by \((3,1)\). For the first
type the defect is \(y+5\); for the next type it is \(11z+19\). Thus

\[
v_2(y+5)=v_2(32(16t+3))=5,
\quad
v_2(11z+19)=v_2(64\cdot9(11t+2))=6+v_2(11t+2).
\]

The second quantity is unbounded on ordinary nonnegative \(t\), since
11 is invertible modulo every power of two. Meanwhile
\(z-y=64t+12>0\). In particular, \(1115\to1255\) (\(t=2\)) increases
the current charge from five to nine. Every expression
\(c\log_2 y+w\,v_2(D_{\mathrm{current}}(y))\), with \(c\ge0\) and
\(w>0\), increases on that step. This refutes that proposed rank on actual
ordinary inputs, independently of Collatz.

## 3. Precharging every inverse center: a theorem under explicit hypotheses

For positive \(a,b\), define on odd 2-adic values

\[
F_{a,b}(z)=\frac{2^a(2^b z+1)}{3^a}-1=\frac{Qz-C}{P}.
\]

The inverse has the exact source run type \((a,b)\). Indeed
\(v_2(F(z)+1)=a\), and after those odd inputs its value is \(2^b z\).
Different pairs therefore give disjoint images. For odd rational centers,

\[
v_2(F_{a,b}(z)-F_{a,b}(r))=a+b+v_2(z-r).
\]

Let \(\mathcal R\) be any countable set of distinct odd rational centers
\(r=p_r/q_r\) in lowest terms, with \(q_r>0\) odd. Exclude positive
ordinary integer centers. Extend the nonnegative weights \(w(r)\) by zero
outside the set, and assume the finite logarithmic moment

\[
\sum_r w(r)\bigl(1+\log_2(1+|p_r|+q_r)\bigr)<\infty.
\tag{1}
\]

Then

\[
H(n)=c\log_2 n+\sum_r w(r)v_2(n-r)
\tag{2}
\]

is finite at every positive odd integer. The elementary bound is
\(v_2(n-r)\le\log_2 n+\log_2(1+|p_r|+q_r)\); valuations are
nonnegative because both arguments are odd 2-adic integers.

**Claim.** If (2) is weakly decreasing at every sufficiently large ordinary
valley source, then every weight is zero.

Fix a supported center \(r\) and a pair \((a,b)\). For arbitrarily large
\(m\), choose a positive ordinary odd \(z_m\) satisfying

\[
v_2(z_m-r)=m,\qquad 2^b z_m+1\equiv0\pmod{3^a}.
\]

The first condition is a residue modulo \(2^{m+1}\). CRT with the fixed
ternary modulus, followed by adding one or two full moduli if necessary,
gives \(z_m=\Theta_{a,b}(2^m)\). Its predecessor
\(y_m=F_{a,b}(z_m)\) is positive integral and has exactly the required
run. Also \(y_m=\Theta_{a,b}(2^m)\).

For any fixed center different from \(r\), its target valuation divided
by \(m\) tends to zero; at \(r\) the limit is one. At the source the
corresponding indicator is that of \(F_{a,b}(r)\). The bounds above and
(1) give a summable majorant for these normalized valuations. Dominated
convergence is therefore legitimate. Divide \(H(y_m)\ge H(z_m)\) by
\(m\). The logarithmic height difference divided by \(m\) tends to zero,
leaving

\[
w(F_{a,b}(r))\ge w(r).
\tag{3}
\]

The infinitely many pairs \((a,b)\) have distinct images of this same
center. If \(w(r)>0\), (3) already forces infinite weight in the first
generation, contradicting (1). This proves the claim.

A clock discount \(\rho^{a+b}\) has one-generation total
\((\rho/(1-\rho))^2\); summing that geometric tree would require
\(\rho<1/2\). Every such discount violates (3). The uniform diffuse
measure on odd 2-adic integers gives a different charge, but its mean
valuation is the constant \(\sum_{k\ge1}2^{-(k-1)}=2\), hence supplies
no drift. These arguments do **not** exclude singular continuous measures,
signed corrections, nonlinear charges or a charge required to decrease only
on selected multi-valley returns.

## 4. A finite nonlinear envelope, and its exact value

For a reduced odd rational center \(r=p/q<0\), \(q>0\), put

\[
H_r=\max(|p|,q),\qquad s_n(r)=v_2(qn-p)-\log_2 H_r.
\]

For every **positive odd** integer \(n\),

\[
\sup_{r<0,\ p,q\text{ odd}}s_n(r)=\log_2(n+1).
\tag{4}
\]

The same value results if \(r<-1\) is required. For the upper bound use
\(2^{v_2(qn-p)}\le qn-p\le(n+1)H_r\). For the lower bound, let
\(q_k\) be the largest positive odd integer strictly below
\(2^k/(n+1)\), and set \(p_k=nq_k-2^k\). The fraction is reduced
because \(q_k\) is odd and \(\gcd(q_k,p_k)=\gcd(q_k,2^k)=1\).
It is below \(-1\), its numerator is odd, and the valuation is exactly
\(k\). Since \(q_k=2^k/(n+1)+O(1)\),
\(H_{p_k/q_k}=2^k/(n+1)+O_n(1)\), proving (4).

Exponentiating the supremum gives exactly the original integer height
\(n+1\). A strict finite-return decrease of that rank is ordinary first
descent. This evaluation therefore does not prove the needed decrease.
It is essential to take the supremum before rounding. For odd \(n\),
an individual center attains equality only at \(r=-1\) when \(n+1\)
is a power of two; in other cases taking floors first changes the result.
The odd-input domain is essential too: for positive even \(n\), every
\(qn-p\) is odd, and the envelope over all negative odd rationals is zero.

## 5. The restricted inverse tree remains open

Restrict the centers to the full inverse valley tree of \(-5\). All
centers stay below \(-1\), so the same upper bound ensures finiteness.
For a reduced center \(r=p/q\), its image is
\((Qp-Cq)/(Pq)\), with reduction factor

\[
g=\gcd(Qp-Cq,P),\qquad
M=\frac{\max(|Qp-Cq|,Pq)}{g\max(|p|,q)}.
\]

Here \(\gcd(Qp-Cq,q)=1\). The factor \(g\) is odd. Direct substitution
on an ordinary edge \(y\to z\) gives the exact transfer

\[
s_y(F(r))-s_z(r)=\log_2 Q-\log_2 M.
\tag{5}
\]

The hoped-for inequality at **every** center is false. For
\((a,b)=(16,1)\) and \(r=-5\),

\[
P=43046721,\ Q=131072,\ C=42981185,\ g=9,
\quad M=43636545/45>Q.
\]

Thus (5) is negative. Actual positive sources with this run type exist
by the same CRT construction. This counterexample refutes the uniform
centerwise estimate; it does not show that the supremum itself increases,
or that the root is near-maximizing on any such edge. Another maximizing
center or a longer return could succeed. Formula (5), with composed
\(P,Q,C\), remains exact for a finite itinerary, but no universally
successful itinerary or strict discrete debit has been proved.
