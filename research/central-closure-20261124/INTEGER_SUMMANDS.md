# Testing the missing positive-integer summand bound

**Status.** Written theorem using the published unit-equation finiteness
theorem below. Not formalized in Lean. This refutes a proposed uniform
queue estimate; it does not refute tightness along one fixed infinite orbit.

Fix a finite prime set \(P\supseteq\{2,3\}\). Let \(h_P(x)\) be the
minimum number of positive **integer** \(P\)-units that sum to \(x\).
The finite-source argument in PR192's `SOURCE_EXTENSION.md` would exclude
an escaping orbit if its empirical distributions of these lengths had a
tight subsequence for some fixed \(P\). That is the missing upper bound
we tried to supply from binary carry operations.

## An ascending ordinary family defeats a uniform queue bound

**Theorem.** For every \(L,K\ge1\), infinitely many positive odd starts
\(q_0\) have \(h_P(q_0)\le2\), while their next \(L\) odd iterates
strictly increase, all gaps are one, and

\[
h_P(q_j)>K\qquad(1\le j\le L).
\]

Choose arbitrarily large positive exponents \(k\) satisfying

\[
3^k\equiv-5\pmod{2^{L+1}},\qquad q_0=3^k+4.
\]

There are infinitely many such exponents. To see this, impose the
congruence modulo \(2^B\), \(B=\max(3,L+1)\), and write \(k=1+2r\).
The residue \(-5/3\) is one modulo eight. The powers of nine generate
the complete subgroup of residues one modulo eight, because
\(v_2(9^{2^a}-1)=a+3\). Thus the permitted exponents include a
nonempty arithmetic progression.

For \(0\le j\le L\), set

\[
q_j=\frac{3^j(q_0+1)}{2^j}-1.
\tag{1}
\]

The congruence ensures these are odd positive integers, including at
\(j=L\). They satisfy \(2q_{j+1}=3q_j+1\), so their exact accelerated
gaps are one. Moreover \(q_{j+1}-q_j=(q_j+1)/2>0\). The original source
is the strict minimum of this entire block, and it is the sum of the two
integer \(P\)-units \(3^k\) and four.

Fix \(j\ge1\). A presentation of \(q_j\) by \(t\le K\) positive
integer \(P\)-units would give

\[
2^j(u_1+\cdots+u_t)-3^{k+j}=5\cdot3^j-2^j=:B_j>0.
\tag{2}
\]

No nonempty subsum on the left is zero: a zero subsum must contain the
sole negative summand, which is odd, whereas every sum of positive
summands is even. Divide by the fixed nonzero \(B_j\). This is a
nondegenerate equation with fixed rational coefficients in a finite-rank
subgroup of \((\mathbb Q^*)^{t+1}\). The last variable is \(3^{k+j}\),
so it determines \(k\).

Evertse--Schlickewei--Schmidt, Theorem 1.1, gives finitely many such
nondegenerate solutions for every fixed \(j,t\). Removing the finite
union of exceptional exponents for \(1\le j\le L\), \(1\le t\le K\)
leaves infinitely many admissible \(k\). This proves the theorem.

If \(5\in P\), the starting queue can have size one: use
\(q_0=5\cdot3^k\), choose \(3^k\equiv-1/5\pmod{2^{L+1}}\), and
replace (2) by

\[
2^j(u_1+\cdots+u_t)-5\cdot3^{k+j}=3^j-2^j.
\]

The same congruence subgroup and parity argument apply.

## Why this does not close the fixed-source question

Multiplying each token by three and adding one preserves a rational
\(P\)-unit presentation with one additional token. Dividing the total
by two need not leave the individual tokens integral. Formula (2) shows
that no uniformly bounded conversion back to positive integer tokens
exists, even on a long ordinary block that never drops below its source.

The construction changes \(q_0\) as \(L,K\) change. It says nothing
about the asymptotic empirical lengths on a single hypothetical escaping
orbit. Such an orbit could still have a tight subsequence by a global
mechanism not expressible as this local bounded queue. The new theorem
therefore does not supply PR192's missing hypothesis or a counterexample
to it. An argument excluding escape would still need a separate treatment
of nontrivial positive cycles.

Primary reference: J.-H. Evertse, H. P. Schlickewei and W. M. Schmidt,
*Linear equations in variables which lie in a multiplicative group*,
Annals of Mathematics 155 (2002), 807--836, Theorem 1.1, p. 808.
[Journal page](https://annals.math.princeton.edu/2002/155-3/p04) ·
[Authors' preprint](https://arxiv.org/abs/math/0409604).
