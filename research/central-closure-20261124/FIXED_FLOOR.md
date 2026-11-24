# Keep the original ordinary floor fixed

**Status: written diagnostic; no universal merger or descent is proved.**
The quarter-predecessor calculation is already present in the source-pinned
critical-section work in PR197. Here it is applied to the proposed minimum
argument. The exact source is listed in `SOURCES.json`.

## 1. Strong induction gives a finite target, not a forced visit

Suppose \(q>2\) is a least positive ordinary nonconverger. Every positive
\(x<q\) then has a finite trajectory to one. Let \(K_q\) be the union
of these trajectories, together with the trivial shortcut cycle \(1,2\).
Let \(D_q\) be the maximum number of odd inputs before the first hit of
one over all these smaller starts. Both objects can be computed under the
induction hypothesis by running finitely many terminating trajectories.

For any \(Y\ge q\),

\[
\exists x<q\ \exists t\ge0:\ T^t(x)=Y
\quad\Longleftrightarrow\quad Y\in K_q.
\]

Such a hit must occur before the first visit to one, hence uses at most
\(D_q\) odd inputs. Allowing still larger inverse budgets at this same
floor cannot add any new target. A two-sided merger proof must therefore
force an actual forward iterate of this same \(q\) into this specific
finite set. Cofinal inverse ancestors of \(q\) do not supply that incidence.

Even pure inversion at an arbitrary starting endpoint is insufficient when
convergence is true. The complete shortcut forward union from 1 through 6
is \(\{1,2,3,4,5,6,8\}\), which misses 7, although 7 converges. The
required meeting point must be allowed to lie later on the original orbit.

## 2. Minima of ordinary odd-clock levels cannot have a large next valuation

In an acyclic component, choose the integer level function \(\ell\) with
\(\ell(q)=0\) and \(\ell(U(x))=\ell(x)+1\). More explicitly, if
\(U^a(x)=U^b(q)\), put \(\ell(x)=b-a\). Acyclicity makes this
well-defined. Every positive level occurs along the forward orbit. Every
negative level occurs as well: from the ternary unit \(U(q)\), keep taking
positive odd predecessors coprime to three. Among the first two allowed
inverse exponents, at least one predecessor is coprime to three, since
at most one of the three consecutive permitted exponents gives a multiple
of three.

Let \(m_k\) be the smallest positive odd integer at level \(k\). Then
\(m_k\to\infty\) as \(k\to+\infty\) and as \(k\to-\infty\):
each bounded interval contains finitely many integers, each with one level.

**Level-minimum fact.** Every \(m_k\) satisfies

\[
v_2(3m_k+1)\le2.
\tag{1}
\]

If the valuation is at least three, write \(m_k=8r+5\). The smaller
positive odd integer \(x=(m_k-1)/4=2r+1\) satisfies
\(3m_k+1=4(3x+1)\), so \(U(x)=U(m_k)\). Therefore \(x\) is at
the same level, contradicting minimality. The value one has valuation two
and causes no exception.

There is an exact recurrence. Let \(b_i\) be the smallest member of level
\(k+1\) congruent to \(i\pmod3\), for \(i=1,2\), omitting an empty
class. Then

\[
m_k=\min\left\{\frac{4b_1-1}{3},\frac{2b_2-1}{3}\right\}.
\tag{2}
\]

These are the smallest positive odd predecessors of their targets; each
inverse formula is increasing in its target. Every level-\(k\) member
maps to a ternary unit at level \(k+1\), proving both inequalities in (2).

## 3. Why critical cofinality does not close this minimum argument

PR197's critical marks satisfy, with \(d=\lfloor\log_2 n\rfloor\) and
\(e=v_2(3n+1)\),

\[
(d+1)(n-2^d)\le70\,2^d,\qquad d+1\le5e\le d+8.
\]

Their next odd values obey \(U(n)\le4n^{4/5}\). If the level minima
were such marks eventually, the inequality
\(m_{k+1}\le4m_k^{4/5}\) would contradict their escape to infinity.
But (1) proves that this hypothesis is false at every octave \(d\ge10\).

Minimizing only over marks at a level does not repair the argument. If a
mark has \(e\ge3\), the same quarter deletion preserves its mark.
Indeed, with \(n=4x+1\) and \(D=\lfloor\log_2 x\rfloor\), the old
mark reads

\[
(D+3)\bigl(4(x-2^D)+1\bigr)\le280\,2^D,
\]

which implies \((D+1)(x-2^D)\le70\,2^D\). Thus the smallest mark
at any level containing marks also has valuation at most two. A large
critical mark is necessarily nonminimal, even in this smaller set.

Taking the minimum only among critical marks forfeits the comparison to
the unrestricted level minimum. For a critical \(n\) at level \(k\),
one only obtains

\[
m_k\le\frac{2^a U(n)-1}{3},
\qquad a\in\{1,2\}
\]

with the parity of \(a\) fixed by the target modulo three. This bounds
\(m_k\) from above; it cannot supply an upper bound on \(U(n)\) in
terms of \(m_k\). The original floor \(q\) has not been beaten.

In a component with a positive cycle of odd-map period \(L\), the levels
are defined modulo \(L\), not in the integers. The quarter deletion and
minimum recurrence still hold. The two-ended divergence argument was
specific to the acyclic case and cannot exclude that cycle case.
