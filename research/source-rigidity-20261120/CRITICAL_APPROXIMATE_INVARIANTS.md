# Critical approximate invariants for the actual ordinary operators

**Status: PROPOSED, elementary proof. No Collatz conclusion.** This note
continues the endpoint investigation in `ENDPOINT_CAPACITY.md`. It retains
the actual odd Collatz branch in the defect calculation, rather than using
only doubling and an abstract variation inequality. The functions below are
not exactly Collatz invariant. Their normalized defects tend to zero, so a
uniform stability inequality for arbitrary functions cannot replace exact
invariance at the critical harmonic weight.

All states are positive ordinary integers. Let

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\qquad U(m)=\frac{3m+1}{2^{v_2(3m+1)}}\quad(m\text{ odd}).
\]

Write \(o(n)=n/2^{v_2(n)}\). For an integer \(M\ge1\), set

\[
b_M(n)=\mathbf1_{o(n)\le M},\qquad
L_M=\sum_{n\ge1}\frac{b_M(n)}n
   =2\sum_{\substack{m\le M\\m\text{ odd}}}\frac1m.
\tag{1}
\]

Thus \(L_M=\log M+O(1)\) as \(M\to\infty\). Although each support contains
infinitely many dyadic lifts, (1) is finite. No assertion about convergence
of the first \(M\) odd integers is used.

## CA1. Exact doubling invariance and bounded tripling defect

For every \(n\), \(b_M(2n)=b_M(n)\), and

\[
\Delta_3(M):=\sum_{n\ge1}\frac{|b_M(3n)-b_M(n)|}{n}
=2\sum_{\substack{M/3<m\le M\\m\text{ odd}}}\frac1m
\longrightarrow\log3.
\tag{2}
\]

This is the exact calculation also used in EC1 of the companion note. It
follows by partitioning into dyadic fibers of the odd part; tripling sends
the odd part \(m\) to \(3m\).

## CA2. The actual Collatz defect has a finite nonzero limit

The same cutoffs satisfy

\[
\boxed{\quad
\Delta_T(M):=\sum_{n\ge1}\frac{|b_M(Tn)-b_M(n)|}{n}
\longrightarrow\frac{\log2}{2}.
\quad}
\tag{3}
\]

In particular \(\Delta_T(M)<4\) for every \(M\ge1\).

### A uniform bound including every source

Even inputs have zero defect. At an odd input \(n\), doubling invariance
identifies \(b_M(Tn)\) with \(\mathbf1_{U(n)\le M}\). The defect is
therefore exactly the harmonic weight of odd inputs crossing the cutoff
\(M\) under \(U\), in either direction.

For outward crossings \(n\le M<U(n)\), the inequality
\(U(n)\le(3n+1)/2\) implies \(n>(2M-1)/3\ge M/3\).
For any interval \((M/3,M]\), its odd harmonic sum is at most
\(1+\tfrac12\log3<2\): retain its first term, and bound each later
term by one half of the integral over the preceding interval of length two.

For inward crossings, fix the odd endpoint \(t\le M\). If \(3\mid t\)
there are no odd predecessors. Otherwise its odd predecessors have the
form \((2^a t-1)/3\), with \(a\) in one positive parity class. After the
first predecessor \(x_0>M\), all subsequent ones are

\[
x_j=4^j x_0+\frac{4^j-1}{3}\ge4^j x_0.
\]

Their total harmonic weight is at most \(4/(3x_0)<4/(3M)\). There are
at most \((M+1)/2\) possible odd endpoints, so the entire inward weight
is at most \(2(M+1)/(3M)\le4/3\). This proves the stated uniform bound.
Every omitted original source is accounted for by an infinite geometric
fiber; this is not a finite-source estimate.

### The limit at each fixed valuation

The exact valuation class \(v_2(3n+1)=a\) is one odd residue modulo
\(h_a=2^{a+1}\). Within that class,
\(U(n)=(3n+1)/2^a\). For \(a=1\), the crossing interval is

\[
(2M-1)/3<n\le M.
\]

For \(a\ge2\), it is

\[
M<n\le(2^aM-1)/3.
\]

The harmonic sum over a fixed residue class in \((\alpha M+O(1),
\beta M+O(1)]\), with \(0<\alpha<\beta\), tends to
\(h_a^{-1}\log(\beta/\alpha)\). This follows directly from upper and
lower integral sums, or from a Riemann sum after dividing the integers by
\(M\). Hence the contribution of valuation \(a\) tends to

\[
2^{-a-1}\left|\log\frac3{2^a}\right|.
\tag{4}
\]

### A uniform tail justifying the infinite valuation sum

Fix \(A\ge3\). All crossings with valuation \(a\ge A\) are inward.
For each odd endpoint \(t\le M\), let \(x_0\) now be its first
predecessor with both \(a\ge A\) and \(x_0>M\). Since

\[
x_0\ge\frac{2^A t-1}{3}\ge\frac{2^{A-1}t}{3},
\]

the same geometric fiber bound gives a total tail at most

\[
\frac43\sum_{t=1}^{M}
\min\left(\frac1M,\frac{6}{2^At}\right).
\tag{5}
\]

For fixed \(A\), take \(M\) sufficiently large that
\(K=\lceil6M/2^A\rceil\le M\). Splitting at \(K\) and comparing the
remaining harmonic sum with an integral shows that (5) is at most

\[
\frac8{2^A}\left(1+\log\frac{2^A}{6}\right)
+\frac4{3M}
\le\frac{8(1+A\log2)}{2^A}+\frac4{3M}.
\tag{6}
\]

Its upper limit as \(M\to\infty\) tends to zero with \(A\). Thus the
fixed-valuation limits (4) can be summed. The sum is elementary:

\[
\begin{aligned}
\sum_{a\ge1}2^{-a-1}\left|\log\frac3{2^a}\right|
&=\frac14\log\frac32
 +\sum_{a\ge2}2^{-a-1}(a\log2-\log3)\\
&=\frac14\log\frac32+\frac34\log2-\frac14\log3
=\frac12\log2.
\end{aligned}
\]

This proves (3) without exchanging an uncontrolled limit and sum.

## CA3. Joint approximate invariants on a specified critical space

Let

\[
X_p=\ell^p(\mathbb N_{>0},1/n),\quad p=1,2,
\qquad
K_Tf(n)=f(Tn),\quad K_jf(n)=f(jn),\quad j=2,3.
\]

These are bounded composition operators. For \(K_j\), its weighted
\(p\)-norm to the power \(p\) is at most \(j\). For \(K_T\), the
preimages of \(t\) are \(2t\) and, when legal, \((2t-1)/3\). Thus
the coefficient of \(|f(t)|^p/t\) is

\[
\frac12+\mathbf1_{t\equiv2\ (3)}\frac{3t}{2t-1}
\le\frac52.
\tag{7}
\]

The upper value is attained at \(t=2\). In particular all the following
residual statements concern bounded operators on the stated space.

Set \(v_{M,p}=b_M/L_M^{1/p}\). Then \(\|v_{M,p}\|_{X_p}=1\),
\(K_2v_{M,p}=v_{M,p}\), and, since a Boolean difference has the same
absolute value and its \(p\)-th power,

\[
\|(K_T-I)v_{M,p}\|_{X_p}^p=\frac{\Delta_T(M)}{L_M},\qquad
\|(K_3-I)v_{M,p}\|_{X_p}^p=\frac{\Delta_3(M)}{L_M}.
\tag{8}
\]

Both tend to zero, at order \(1/\log M\) before taking the \(p\)-th
root. Thus adding the actual odd-branch defect to the tripling defect
does not yield a uniform critical inequality of the form

\[
\|f\|_{X_p}\le C\bigl(\|(K_T-I)f\|_{X_p}
                         +\|(K_3-I)f\|_{X_p}\bigr)
\tag{9}
\]

even on the exactly doubling-invariant subspace.

For \(p=2\), the vectors tend weakly to zero: each fixed coordinate
tends to zero, they are uniformly bounded, and finitely supported vectors
are dense. Therefore \(1\) is an essential approximate spectral point
of \(K_T\). It is also one for every bounded operator

\[
L=\alpha_TK_T+\alpha_2K_2+\alpha_3K_3,
\qquad\alpha_T+\alpha_2+\alpha_3=1,
\]

with fixed complex coefficients. Indeed (8) gives \((L-I)v_{M,2}\to0\).
If \(L-I\) were Fredholm, a bounded left inverse modulo compact operators
would contradict the unit norms of this weakly null sequence. This uses
no false assertion that the unit basis of ordinary \(\ell^1\) is weakly
null; the essential-spectrum statement here is on \(X_2\).

## What this does and does not settle

The ordinary Collatz branch, multiplication by two, and multiplication by
three simultaneously admit the explicit approximate invariants (8) at
the harmonic endpoint. These functions provide a precise obstruction to
uniform defect-based stability on the full critical space. This is a
different space and different operators from the derivative-weighted
\(\ell^2\) operators of PR143–144 and PR156; no spectrum is transferred
between them.

The counterexample does **not** produce a nonconstant exactly invariant
Collatz label. For example, if \(M\equiv3\pmod4\), then
\(b_M(M)=1\) but \(b_M(U(M))=0\), since \(U(M)=(3M+1)/2>M\).
There is no interchange of approximate and exact invariance. A theorem
that uses exact odd-branch invariance, source-dependent information, or
additional arithmetic restrictions is still possible. No escape or
nontrivial-cycle exclusion has been obtained.

## Source and evidence boundaries

- The cutoff family and its relaxed shell-variation use were developed in
  this pass's `ENDPOINT_CAPACITY.md`, EC1–EC2.
- PR155 at `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
  `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
  OD1–OD4, and `ENDPOINT_BOUNDARY.md` are the endpoint source being tested.
- PR157 at `64361ecca770092d6c8242dc6211e38818af2e50` supplies a different
  positive-return occupation target; (8) neither proves nor refutes that
  specific-vector estimate.
- `check_critical_cutoffs.py` provides exact all-source enclosures at selected
  cutoffs through geometric inverse-fiber tails, separate literal-prefix
  comparisons, and damaged-identity controls. Those finite checks do not
  prove the limiting or Fredholm arguments above.
