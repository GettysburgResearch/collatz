# A complete ordinary inverse-tree bijection with signed exponent cost

23 November 2026. **Written all-depth finite-path theorem; no Collatz
closure.** This is an explicit construction on actual positive odd integers.
It pairs the complete inverse trees of any two ternary-unit roots in the
same class modulo three. The words are allowed to change. Every matched
edge remains physically legal, and its exponent cost can have either
sign. The unresolved step is amortizing that cost strongly enough to
prove the sibling comparison in `SIBLING_BASIN_COLLAPSE.md`.

## 1. A two-colour address for every actual unit parent

Let \(q>0\) be odd with \(3\nmid q\), and put
\(I_eq=(2^eq-1)/3\). An exponent \(e\ge1\) is legal precisely when
\(I_eq\) is an integer not divisible by three. Such a parent is positive
and odd, and its exact forward odd valuation is \(e\).

For each \(c\in\{1,2\}\), there is exactly one exponent
\(e_c(q)\in\{1,\ldots,6\}\) with

\[
 2^{e_c(q)}q\equiv 3c+1\pmod9.
\tag{1}
\]

This follows because 2 has multiplicative order six modulo nine. The
entire table is:

| \(q\bmod9\) | \(e_1(q)\) | \(e_2(q)\) |
|---:|---:|---:|
| 1 | 2 | 4 |
| 2 | 1 | 3 |
| 4 | 6 | 2 |
| 5 | 3 | 5 |
| 7 | 4 | 6 |
| 8 | 5 | 1 |

Every legal exponent has a **unique** representation

\[
 e=e_c(q)+6j,\qquad c\in\{1,2\},\quad j\ge0.
\tag{2}
\]

Here \(c\) is the actual parent's residue modulo three. Thus
\((c,j)\) is a complete ordinary branch address; no completion or
unrealized parity word is used.

## 2. The balanced branch bijection

Suppose \(q,q'>0\) are odd ternary units with \(q\equiv q'\pmod3\).
Pair their parent with address \((c,j)\) using

\[
 e=e_c(q)+6j,
 \qquad e'=e_c(q')+6j,
 \qquad (I_eq,I_{e'}q').
\tag{3}
\]

Both parents have the same class \(c\pmod3\), so the construction can
be repeated at the next level. The branch mapping is bijective, with
inverse obtained by exchanging the two roots.

Since the root classes agree, the two base exponents have the same
parity. Consequently

\[
 \boxed{\delta=e'-e=e_c(q')-e_c(q)
             \in\{-4,-2,0,2,4\}.}
\tag{4}
\]

A key point is the use of the *canonical representative* \(e_c\) in
\(\{1,\ldots,6\}\), rather than replacing a negative shift by an
arbitrary positive representative. For example, roots 1 and 85 have
classes 1 and 4 modulo nine. Their colour-1 edge uses exponents 2 and
6, with cost \(+4\), but their colour-2 edge uses exponents 4 and 2,
with cost \(-2\). Both signs are retained.

For a complete address
\(\alpha=((c_1,j_1),\ldots,(c_k,j_k))\), let
\(q_i,q_i'\) be the paired actual ancestors, starting at \(q_0=q\),
\(q_0'=q'\), and let \(e_i,e_i'\) be their exponents. Put

\[
 A(\alpha,q)=\sum_{i=1}^k e_i,\qquad
 \Delta(\alpha;q,q')=A(\alpha,q')-A(\alpha,q).
\]

Then

\[
 \boxed{-4k\le\Delta(\alpha;q,q')\le4k.}
\tag{5}
\]

Equations (2)--(3) give a bijection of **all** depth-\(k\) inverse words,
including arbitrarily large exponents. It is also a bijection of their
ordinary source vertices at that fixed depth: a positive ordinary source
has a unique forward word to a specified root and depth. Periodic roots
are permitted at fixed depth; vertices repeated across different depths
are not identified.

The construction is compatible with prefixes, so it gives an isomorphism
of the rooted path trees. It does not assert that the root vertices have
forward trajectories meeting one another.

## 3. Exact pressure cost of the changed word

For \(s>0\), the pressure weight of an inverse word is

\[
 W_s(\alpha,q)=\left(\frac{3^k}{2^{A(\alpha,q)}}\right)^s.
\]

The literal cost is

\[
 \boxed{W_s(\alpha,q')
        =2^{-s\Delta(\alpha;q,q')}W_s(\alpha,q).}
\tag{6}
\]

Summing over the complete address space at fixed depth is legitimate by
nonnegativity and the convergent geometric exponent sums. Therefore

\[
 \boxed{P_s^k1(q')
 =\sum_{\alpha\text{ of depth }k}
   2^{-s\Delta(\alpha;q,q')}W_s(\alpha,q).}
\tag{7}
\]

The finite-depth comparison follows:

\[
 \boxed{2^{-4sk}P_s^k1(q)\le P_s^k1(q')
                   \le2^{4sk}P_s^k1(q).}
\tag{8}
\]

Unlike the huge congruence shift \(q\mapsto S^{3^d}q\), this compiler
can compare the **fixed** pair \(q,q'=64q+21\) at every depth. Its
crude cost is exponential in depth. It does not prove a bounded or
near-logarithmic full-Green comparison.

In particular, Tonelli gives the valid lower bound

\[
 Z_s(q')\ge\sum_{k\ge0}2^{-4sk}P_s^k1(q),
\tag{9}
\]

which is a discounted Green function, not \(Z_s(q)\).
Dropping the discount would be the missing argument, not an algebraic
simplification.

## 4. The signed cost retains actual ancestor height

The two physical edge equations are
\(3q_i+1=2^{e_i}q_{i-1}\) and
\(3q_i'+1=2^{e_i'}q_{i-1}'\). Set
\(\lambda(n)=3n/(3n+1)\). Their quotient telescopes to

\[
 \boxed{2^{\Delta(\alpha;q,q')}
  =\frac{q}{q'}\frac{q_k'}{q_k}
        \prod_{i=1}^k\frac{\lambda(q_i)}{\lambda(q_i')}.}
\tag{10}
\]

This exact equality explains the remaining arithmetic cost. A small
signed exponent discrepancy would keep the transported ordinary source
small relative to the original source, up to the actual correction
products. Such control is not provided by a tree bijection alone.

If \(q,q'\) belong to an escaping component, the parent packet's
uniform positive product bound gives
\(c_*\le\prod_{i=1}^k\lambda(q_i)\le1\), where
\(c_*=\exp(-160/3)\), and likewise for the primed path. Hence

\[
 c_*\frac{q}{q'}\frac{q_k'}{q_k}
 \le2^{\Delta(\alpha;q,q')}
 \le c_*^{-1}\frac{q}{q'}\frac{q_k'}{q_k}.
\tag{11}
\]

The same-source requirement has thus not disappeared: it is exactly the
height of the transported ordinary ancestor in (10)--(11).

For the pressure probability on that component and sibling roots
\(q'=Sq\), (2) of `SIBLING_BASIN_COLLAPSE.md` also gives

\[
 \mu(q_k')=64^{-s}2^{-s\Delta(\alpha;q,Sq)}\mu(q_k).
\tag{12}
\]

When the roots are nonperiodic, their predecessor sets have unique
depths, so the complete path-tree bijection becomes a genuine bijection
between their predecessor sets. Equation (12) then transports the
whole ordinary basin mass with its exact density, including all source
height distortion. There is no collision loss hidden in this compiler.

## 5. What remains to be proved

For the original unchanged escaping ray \(q_j\), the preceding note
proves summability of \(Z_s(Sq_j)/Z_s(q_j)\). Formula (7) identifies
that ratio as the exponential moment of the signed compiler cost under
the normalized full predecessor-word pressure law. At a nonperiodic
root, that law is precisely the normalized ordinary basin mass.

The required positive estimate is an amortized upper-tail bound for
\(\Delta\) on this **actual pressure law**, strong enough to keep
that exponential moment above the nonsummable near-logarithmic scale.
No such estimate has been established. A per-edge bound \(|\delta|\le4\)
is insufficient, and the existence of both signs in (4) does not make
them independent, centered, or canceling under that law.

This checkpoint proves the complete ordinary compiler, its two-sided
finite-depth weight bound, and the exact physical distortion formula.
It does not prove sibling Harnack, escape exclusion, or a certificate
for the residue-512 implication.

The accompanying finite checker exhausts the six unit residues and both
colours in (1), checks exact inverse branches and the signed cocycle on
specified finite paths, and rejects damaged tables. Those tests are
finite supporting evidence; the all-parameter proofs are the algebra
and address decomposition above. No new Lean result is claimed here.
