# Independent scoped review of AR-4 and AR-5

**Verdict: the stated finite ordinary constructions pass the written arithmetic
review below. Full Collatz remains OPEN. This is not a verification of the
entire arithmetic note or of a global closing inference.**

Reviewed file:
`research/literature-closing-20261121/arithmetic/ARITHMETIC_CLOSURE.md`.

Reviewed SHA-256:
`7e1725f2d572f77acd5993258964c6fd3b20b760f5a903382d6ce3ede5194a76`.

The merger lane independently reconstructed §8, AR-4 and AR-5, at this
file version on 2026-11-21. The scope is modular legality, the exact chosen
valuation words, positivity, same-shell and marked-band inequalities,
parity agreement, and the coupled-remainder gcd. The unbounded parameter
input is used at the exact approximation strength stated in the note; this
review does not reverify the entire pinned PR 182 Lean development.

## 1. A direct legality lemma for either construction

Let a finite word have positive valuations \(a_0,\ldots,a_{s-1}\), and
write \(A_i=\sum_{h<i}a_h\), \(A=A_s\). Define

\[
C_0=0,\qquad C_{i+1}=3C_i+2^{A_i},\qquad
N_i=3^i x+C_i.
\]

Suppose \(x>0\) and the terminal congruence is

\[
N_s\equiv2^A\pmod{2^{A+2}}.
\]

For every \(i<s\), expand the exact recurrence:

\[
N_s=3^{s-i}N_i+
\sum_{h=i}^{s-1}3^{s-1-h}2^{A_h}.
\]

Reduce modulo \(2^{A_i+1}\). The first summand in the tail is

\[
3^{s-1-i}2^{A_i}\equiv2^{A_i}\pmod{2^{A_i+1}},
\]

and every later tail summand is zero modulo this modulus, because all
valuations are positive. The terminal numerator is also zero modulo this
modulus. Since \(3^{s-i}\) is odd, multiplication by its inverse fixes the
nonzero residue \(2^{A_i}\) modulo \(2^{A_i+1}\). Hence

\[
N_i\equiv2^{A_i}\pmod{2^{A_i+1}}.
\]

Consequently \(x_i=N_i/2^{A_i}\) is a positive odd integer for every
intermediate clock, and \(x_s=N_s/2^A\equiv1\pmod4\). The adjacent
identities

\[
2^{a_i}x_{i+1}=3x_i+1
\]

now imply \(v_2(3x_i+1)=a_i\), since the next quotient is odd. This proves
the intended word is the **actual** ordinary odd-step itinerary. It is
not merely a final divisibility condition. The modular inverse exists
because \(3^s\) is odd, and replacing the residue representative by

\[
x=2^d+r,\qquad d\ge A+2,
\]

preserves the terminal congruence. The ordinary shortcut clock is exactly

\[
T^A(x)=U^s(x).
\]

This proof applies to any positive valuation order. The restrictions

\[
a_i\in\{1,2\},\qquad a_0=1
\]

used in AR-4 serve its combinatorial count and immediate parity mismatch;
they are not extra hidden requirements for this legality lemma.

## 2. AR-4 reconstruction

The assumptions are

\[
q\ge8,\qquad q\le A<2q,\qquad
1<\gamma=3^q/2^A\le1+4/q.
\]

A word with \(q\) entries in \(\{1,2\}\), first entry one and total

\[
A=q+\#\{i:a_i=2\},
\]

exists for every such pair. There are exactly

\[
\binom{q-1}{A-q}
\]

choices. Applying the legality lemma with \(s=q\) gives the actual
trajectory and the terminal residue \(y\equiv1\pmod4\). Since

\[
a_0=1,
\]

the initial odd source satisfies \(x\equiv3\pmod4\). Thus its first
two shortcut parity digits are \(11\), while the endpoint's first two
digits are \(10\). Distinct words give disjoint full parity cylinders,
so the chosen residues modulo \(2^{A+2}\) are distinct.

Set \(d=A+q+8\). The residue satisfies

\[
0<r/2^d<2^{-q-6}\le1/(64q).
\]

For the carry,

\[
0<C<2^{A-1}3^q,
\]

because \(A_i\le A\) and the geometric sum of the powers of three is

\[
\sum_{i=0}^{q-1}3^{q-1-i}=(3^q-1)/2.
\]

The assumption \(q\ge8\) gives \(\gamma\le3/2\). Therefore

\[
\frac{C}{2^{A+d}}
 <\gamma2^{-q-9}
 \le\frac3{1024q}.
\]

It follows that

\[
0<y/2^d-1
 <\frac4q+\frac3{128q}+\frac3{1024q}
 <\frac5q<1.
\]

Both \(x\) and \(y\) lie in \([2^d,2^{d+1})\), so their binary depth is
exactly \(d\). Since

\[
d+1=A+q+9\le3q+8\le4q,
\]

the normalized band products are strictly below \(1/16\) for \(x\) and

\[
20<70
\]

for \(y\). Both are marked. Also \(y=\gamma x+C/2^A>x\), and the same
upper estimate gives \(y/x<1+5/q\).

The approximation input

\[
0<q\log_2 3-A<2/q
\]

is enough to provide unbounded admissible pairs: for \(q\ge2\), convexity
on \([0,1]\) gives \(2^t\le1+t\), so in fact

\[
1<\gamma<1+2/q.
\]

For sufficiently large \(q\), the integer \(A\) lies strictly between

\[
q<A<2q.
\]

No assumption about unbounded continued-fraction partial quotients is
needed for this one-sided approximation strength.

## 3. AR-5 reconstruction

Assume

\[
q\ge8,\qquad q<A<2q,\qquad
1<\gamma=3^q/2^A\le1+2/q.
\]

A prefix \(P\) of \(q-2\) entries from \(\{1,2\}\) and sum \(A-3\)
exists, because the integer hypotheses imply

\[
q-2\le A-3\le2q-4.
\]

For \(w_1=P(1,2)\) and \(w_2=P(2,1)\), the carry recurrence gives

\[
c_1=9c_P+5\,2^{A-3},\qquad
c_2=9c_P+7\,2^{A-3}.
\]

Thus

\[
c_2-c_1=2^{A-2}.
\]

Apply the legality lemma to the concatenation, with \(s=2q\), total
valuation \(2A\), residue modulus \(2^{2A+2}\), and

\[
d=2A+2q+8.
\]

This supplies positive ordinary \(x_0,x_1,x_2\), with

\[
2^A x_1=3^q x_0+c_1,\qquad
2^A x_2=3^q x_1+c_2.
\]

Both carries are positive and \(\gamma>1\), so

\[
x_0<x_1<x_2.
\]

The residue obeys

\[
0<r/2^d<2^{-2q-6}\le1/(64q).
\]

Furthermore \(\gamma\le5/4\) and

\[
\gamma^2-1\le4/q+4/q^2\le4.5/q.
\]

Writing \(C_{12}\) for the concatenated carry, the same geometric-sum
bound gives

\[
C_{12}<2^{2A-1}3^{2q},\qquad
\frac{C_{12}}{2^{2A+d}}
 <\gamma^2 2^{-2q-9}
 \le\frac{25}{8192q}.
\]

Hence

\[
0<x_2/2^d-1
 <\frac{4.5}{q}+\frac{25}{1024q}+\frac{25}{8192q}
 <\frac5q<1.
\]

By strict increase, the other two points satisfy the same upper bound.
All three therefore have depth \(d\). The integer bound

\[
d+1\le6q+7\le7q
\]

puts every normalized band product below \(35<70\).

Let \(u_i=x_i-2^d\). Eliminating the common powers of two gives exactly

\[
\begin{aligned}
\mathcal R_{01}&=2^A u_1-3^q u_0
 =c_1+(3^q-2^A)2^d,\\
\mathcal R_{12}&=2^A u_2-3^q u_1
 =c_2+(3^q-2^A)2^d.
\end{aligned}
\]

Each carry is odd: its first summand is odd and all later summands have
positive powers of two. The added common monomial is even. Both remainders
are therefore odd, and their difference is \(2^{A-2}\). Every common
divisor divides this power of two and is odd, proving

\[
\gcd(\mathcal R_{01},\mathcal R_{12})=1.
\]

Finally, the common valuation prefix \(P\) determines \(A-3\) common
shortcut parity digits. The final valuation pairs determine tails \(110\)
and \(101\): the next digit agrees and the following digit differs. The
initial parity words at \(x_0\) and \(x_1\) consequently agree for exactly

\[
A-2
\]

digits. The finite parity-cylinder bijection makes this equivalent to

\[
v_2(x_1-x_0)=A-2.
\]

## 4. What this review does and does not establish

Each admissible parameter pair and word yields an actual finite ordinary
trajectory, with the indicated marked visits. The constructions allow
unbounded heights and arbitrarily close leading ratios. AR-4 supplies
immediate parity disagreement; AR-5 supplies coprime coupled remainders
despite three increasing close marked visits.

The witnesses vary with the finite parameters. The proof does not provide
one fixed ordinary source realizing those choices forever. It does not say
these marked endpoints are consecutive first returns, does not exclude
some stronger source-preserving arithmetic selection principle, and does
not establish a divergent orbit. No claim in this review substitutes the
finite constructions for the missing universal Collatz argument.
