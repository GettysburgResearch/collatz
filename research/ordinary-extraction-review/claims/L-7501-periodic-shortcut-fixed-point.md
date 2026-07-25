# L-7501 — Periodic shortcut blocks have explicit completions and least-root escape

**Claim ID:** `L-7501`  
**Title:** Every periodic shortcut parity block is either an integral positive cycle or has exponentially escaping positive roots  
**Status:** `PROPOSED / EXACT ALGEBRAIC THEOREM`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-25  
**Dependencies:** the finite parity-cylinder bijection proved in `T-7602`  
**Scope:** periodic parity schedules for the shortcut Collatz map  
**Related counterexample candidates:** none

## 1. Statement

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2
\end{cases}
\]

on \(\mathbf Z_2\). Fix a nonempty binary word

\[
w=(\varepsilon_0,\ldots,\varepsilon_{L-1})
\]

of length \(L\), and put

\[
s=\sum_{j=0}^{L-1}\varepsilon_j,
\qquad
Q=2^L,
\qquad
A=3^s.
\]

Define \(C_w\) by the exact block identity

\[
\boxed{
T^L(x)=\frac{Ax+C_w}{Q}}
\tag{1}
\]

whenever the first \(L\) parity bits are \(w\). Then:

1. The constant is
   \[
   \boxed{
   C_w=
   \sum_{\substack{0\le j<L\\ \varepsilon_j=1}}
   2^j3^{\,s-s_{j+1}},
   }
   \tag{2}
   \]
   where \(s_{j+1}=\varepsilon_0+\cdots+\varepsilon_j\). In particular,
   \(C_w>0\) whenever \(s>0\).

2. The infinite periodic word \(w^\infty\) has the unique \(2\)-adic initial value
   \[
   \boxed{
   x_w=\frac{C_w}{Q-A}.}
   \tag{3}
   \]
   The denominator is odd, so \(x_w\in\mathbf Z_2\).

3. If \(A>Q\), then \(x_w<0\). Thus no positive ordinary integer realizes
   \(w^\infty\), even though every finite prefix has infinitely many positive
   ordinary representatives.

4. If \(A<Q\), then \(x_w>0\). It is an ordinary integer exactly when
   \[
   \boxed{Q-A\mid C_w.}
   \tag{4}
   \]
   In that case the exact parity replay closes to a positive shortcut-Collatz
   cycle, of period dividing \(L\).

5. Let \(r_m\in\{0,\ldots,Q^m-1\}\) be the canonical residue realizing the
   first \(m\) copies of \(w\), and let
   \[
   \mu_m=
   \begin{cases}
   r_m,&r_m>0,\\
   Q^m,&r_m=0
   \end{cases}
   \]
   be the least **positive** representative of that cylinder. Exactly one of
   the following occurs:

   - \(x_w\) is a positive ordinary integer; then \(\mu_m=x_w\) for all
     sufficiently large \(m\);
   - otherwise \(\mu_m\to\infty\), and in every nonzero block case the escape
     is exponential.

   More precisely, for all sufficiently large \(m\):

   - if \(A<Q\), put \(D=Q-A\). There is a periodic sequence
     \(t_m\in\{0,\ldots,D-1\}\) satisfying
     \[
     t_mQ^m\equiv-C_w\pmod D,
     \qquad
     \boxed{r_m=\frac{C_w+t_mQ^m}{D}.}
     \tag{5}
     \]
     The value \(t_m=0\) occurs exactly in the integral-cycle case. Otherwise
     \(t_m\ge1\) and
     \[
     \mu_m=r_m\ge\frac{Q^m+C_w}{D}.
     \tag{6}
     \]

   - if \(A>Q\), put \(D=A-Q\). There is a periodic sequence
     \(t_m\in\{1,\ldots,D\}\) satisfying
     \[
     t_mQ^m\equiv C_w\pmod D,
     \qquad
     \boxed{r_m=\frac{t_mQ^m-C_w}{D}.}
     \tag{7}
     \]
     Consequently
     \[
     \mu_m=r_m\ge\frac{Q^m-C_w}{D}.
     \tag{8}
     \]

Thus every periodic shortcut schedule is decided at the ordinary-extraction
boundary: its positive minima either stabilize at an exact positive cycle or
escape to infinity. A supercritical periodic block always lies on the wrong
signed boundary face.

## 2. Exact affine block

Starting with

\[
T^j(x)=\frac{3^{s_j}x+C_j}{2^j},
\qquad C_0=0,
\]

a zero branch leaves the numerator constant unchanged, while a one branch gives

\[
C_{j+1}=3C_j+2^j.
\]

Iterating this recurrence proves `(1)` and `(2)`.

## 3. Unique periodic completion

The shifted point \(T^L(x_w)\) has the same infinite parity word \(w^\infty\)
as \(x_w\). By the finite parity-cylinder bijection of `T-7602`, two
\(2\)-adic integers with the same infinite parity word are congruent modulo
\(2^n\) for every \(n\), and hence are equal. Therefore

\[
T^L(x_w)=x_w.
\]

Substituting `(1)` gives

\[
(Q-A)x_w=C_w,
\]

which is `(3)`. Since \(Q\) is even and \(A\) is odd, \(Q-A\) is odd.

If \(s=0\), then \(A=1\), \(C_w=0\), and the unique completion is \(0\).
The canonical residues are all zero, but the least positive representatives are
\(\mu_m=Q^m\), so no positive ordinary extraction occurs.

Assume henceforth that \(s>0\), so \(C_w>0\). The sign assertions in parts 3
and 4 follow immediately from `(3)`. In the subcritical case, positivity and
ordinary integrality are equivalent to `(4)`. Because \(x_w\) is the unique
\(2\)-adic realization of \(w^\infty\), an integral value automatically replays
every advertised parity bit and returns after \(L\) steps.

The equality \(A=Q\) cannot occur for \(s,L>0\), because an odd power of three
cannot equal a positive power of two.

## 4. Canonical positive-root formulas

The first \(mL\) bits of \(w^\infty\) select exactly one residue modulo
\(Q^m\), by `T-7602`. Since \(x_w\) realizes that prefix in \(\mathbf Z_2\),
that residue is the canonical representative of \(x_w\pmod {Q^m}\).

### Subcritical case

Let \(D=Q-A>0\). For every sufficiently large \(m\), the congruence

\[
Dr_m\equiv C_w\pmod {Q^m}
\]

has the canonical form

\[
Dr_m-C_w=t_mQ^m,
\qquad 0\le t_m<D.
\]

Reducing modulo \(D\) gives the congruence in `(5)`. Because \(Q\) is a unit
modulo the odd number \(D\), \(Q^{-m}\pmod D\) is periodic, so \(t_m\) is
periodic. The value \(t_m=0\) is possible exactly when \(D\mid C_w\), in which
case \(r_m=C_w/D=x_w\) once \(Q^m>x_w\). If that divisibility fails,
\(t_m\ge1\), proving `(6)`.

### Supercritical case

Let \(D=A-Q>0\). For every sufficiently large \(m\),

\[
Dr_m\equiv-C_w\pmod {Q^m},
\]

or equivalently

\[
Dr_m+C_w=t_mQ^m.
\]

Choose the representative \(t_m\in\{1,\ldots,D\}\), using \(D\) rather than
zero for the zero class. Reducing modulo \(D\) gives `(7)`. Again \(t_m\) is
periodic because \(Q\) is invertible modulo \(D\), and `(8)` follows.

This proves the theorem. ∎

## 5. Relationship to the full Collatz objective

This is an exhaustive negative result for one entire certificate format:
periodic shortcut schedules.

- A supercritical periodic amplifier cannot have a positive ordinary root.
- A subcritical periodic schedule either closes to an exact positive cycle or
  has escaping positive minima.
- The result does not address genuinely aperiodic seed-first arithmetic
  machines.

It is therefore strictly narrower than the Collatz conjecture, while directly
closing every periodic schedule-first counterexample proposal.

## 6. Dependency and gap audit

- No numerical experiment or external theorem is used.
- The only imported interface is the elementary finite parity-cylinder
  bijection already proved inside `T-7602`.
- Canonical residues and least positive representatives are kept distinct;
  residue zero has positive minimum equal to the modulus.
- The theorem concerns canonical initial roots, not the magnitude of later
  hypothetical runtime states.
- A negative integral periodic completion is correctly classified as escape
  from the positive ordinary face, even though it is an ordinary signed value.
- The formulas do not imply that every aperiodic completion is nonordinary.

## 7. Suggested next attack

For a current changing-modulus machine, seek an analogue of `(5)` or `(7)` for
its canonical least initial roots. A recurrence that forces a nonzero
coefficient of the growing modulus would prove escape; a zero coefficient from
some depth onward would extract one ordinary seed.