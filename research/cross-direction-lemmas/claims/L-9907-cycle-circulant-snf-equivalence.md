# L-9907 -- The cyclic Smith obstruction is exactly the positive-cycle condition

Claim ID: `L-9907`
Title: The accelerated cycle matrix has one nontrivial Smith factor, and its augmented lattice class vanishes exactly for a cycle
Status: `PROPOSED / EXACT EQUIVALENCE AND METHOD BOUNDARY`
Authoring agent: `gpt56-synthesis-01-wave22-fixed-width-sunit`
Reviewing agents: `gpt56-synthesis-01` (independent reconstruction)
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904` at repository head `b77a84c7e4ff15f36b59b29627671f1cb6544072`; local `L-9906` only for the cut-defect comparison
Scope: primitive accelerated valuation words and integer-lattice attacks on positive cycles
Related counterexample candidates: none; this result identifies an exact reformulation and rules out a proposed shortcut

## 1. Result in one paragraph

For an accelerated valuation word `w=(a_0,...,a_(k-1))`, put one row

\[
 -3x_j+2^{a_j}x_{j+1}=1
\]

at each cyclic index.  The resulting integer matrix `M_w` has Smith normal
form

\[
 \operatorname{diag}(1,\ldots,1,|2^A-3^k|).
\]

Thus its cokernel is cyclic and sees only the length `k` and total valuation
`A`, not the order of the letters.  The class of the all-ones vector has exact
order

\[
 { |D|\over\gcd(D,C_0,\ldots,C_{k-1})}.
\]

For positive drift, that class vanishes exactly when the rotation constants
`C_j` divided by `D` are the integer states of a positive exact cycle.
Consequently a universal strict-gcd theorem for primitive words other than
`(2)` is not a new route around the cycle problem: it is logically equivalent
to excluding every nontrivial positive accelerated cycle.  Smith form,
resultants, and cut defects provide exact diagnostics, but no independent
obstruction without new arithmetic input showing that some prime factor of
`D` misses `C_0`.

## 2. Cyclic cycle matrix

Let

\[
 w=(a_0,\ldots,a_{k-1}),
 \qquad a_j\in\mathbf Z_{\ge1},
 \qquad A=\sum_{j=0}^{k-1}a_j,
\tag{1}
\]

and read indices modulo `k`.  Define

\[
 \boxed{D=2^A-3^k.}
\tag{2}
\]

Let `M=M_w` be the cyclic `k` by `k` integer matrix whose row `j` has
`-3` in column `j`, `2^(a_j)` in column `j+1`, and zero elsewhere.  For
`k=1` the two entries occupy the same position and are added, so

\[
 M=[2^{a_0}-3]=[D].
\tag{3}
\]

For `k>=2`, the associated system is

\[
 \boxed{-3x_j+2^{a_j}x_{j+1}=1
        \qquad(0\le j<k).}
\tag{4}
\]

An integral solution is exactly a cyclic list satisfying the accelerated
Collatz edge equations.

For each rotation `w^(j)` beginning at `a_j`, let `C_j` be its affine
constant in the notation of `L-9904`.  The rotation identity is

\[
 \boxed{2^{a_j}C_{j+1}=3C_j+D.}
\tag{5}
\]

Therefore, with `C=(C_0,...,C_(k-1))^T` and `1` the all-ones column,

\[
 \boxed{MC=D\mathbf1.}
\tag{6}
\]

## 3. Exact Smith normal form

### Theorem 1 -- all lower determinantal divisors are one

For every nonempty word (1),

\[
 \boxed{
 \operatorname{SNF}(M)
 =\operatorname{diag}(1,\ldots,1,|D|).}
\tag{7}
\]

In particular,

\[
 \boxed{\det M=(-1)^{k-1}D,}
\tag{8}
\]

and, when `D!=0`,

\[
 \boxed{\mathbf Z^k/M\mathbf Z^k\cong\mathbf Z/|D|\mathbf Z.}
\tag{9}
\]

### Proof

Only two permutations contribute to the determinant: the product of the
`-3` diagonal and the cyclic product of the `2^(a_j)` entries.  Hence

\[
 \det M=(-3)^k+(-1)^{k-1}2^A
       =(-1)^{k-1}(2^A-3^k),
\tag{10}
\]

which is (8).

Fix `1<=r<k`.  The first `r` consecutive rows and the same `r` columns give
a triangular minor `(-3)^r`.  The same rows and the next `r` consecutive
columns give the minor

\[
 2^{a_0+\cdots+a_{r-1}}.
\tag{11}
\]

The `r`th determinantal divisor, the gcd of all `r` by `r` minors, therefore
divides two coprime integers and equals one.  The top determinantal divisor is
`|det M|=|D|`.  The invariant-factor characterization of Smith normal form
now gives (7)--(9).  The case `k=1` is immediate from (3). **QED**

### Resultant form

Let `P` be the weighted cyclic shift with

\[
 (Px)_j=2^{a_j}x_{j+1}.
\tag{12}
\]

Then `P^k=2^A I`, `M=P-3I`, and

\[
 \det(P-3I)=(-1)^{k-1}(2^A-3^k).
\tag{13}
\]

Equivalently, evaluating the characteristic relation
`X^k-2^A` at `X=3` produces `3^k-2^A=-D`.  This resultant contains no
letter-order information beyond `(k,A)`, exactly as (7) predicts.

## 4. The augmented class

Assume `D!=0` and set

\[
 \boxed{G=\gcd(D,C_0,\ldots,C_{k-1}).}
\tag{14}
\]

### Theorem 2 -- exact order of the all-ones class

The maximal determinantal divisor of the augmented matrix `[M|1]` is `G`,
and the class of `1` in the cokernel (9) has exact order

\[
 \boxed{\operatorname{ord}_{\operatorname{coker}M}[\mathbf1]
       ={ |D|\over G}.}
\tag{15}
\]

Moreover,

\[
 \boxed{G=\gcd(D,C_0)=\gcd(C_0,\ldots,C_{k-1}).}
\tag{16}
\]

### Proof

Cramer's rule applied to (6) says that replacing column `j` of `M` by
`1` gives determinant `+C_j` or `-C_j`, according to the global orientation
in (8).  The `k` by `k` minors of `[M|1]` are therefore `det M` and these
signed rotation constants, proving the first assertion.

The equation

\[
 Mx=m\mathbf1
\tag{17}
\]

has the unique rational solution `x=mC/D`.  It is integral exactly when
`D` divides every `mC_j`, whose least positive `m` is `|D|/G`.  This proves
(15).

Finally, every divisor of `D` and `C_j` also divides `C_(j+1)` by (5), since
it is odd and hence coprime to `2^(a_j)`.  Thus `gcd(D,C_0)` divides every
rotation constant.  Conversely, a common divisor of `C_j` and `C_(j+1)`
divides `D` by (5).  Chaining around the cycle proves (16). **QED**

## 5. Exact equivalence with a positive cycle

### Theorem 3 -- lattice solvability is cycle solvability

Assume `D>0`.  The following are equivalent:

1. `[1]=0` in `coker M`;
2. `G=D`;
3. `D` divides `C_0`;
4. every quotient `n_j=C_j/D` is a positive odd integer and

   \[
    2^{a_j}n_{j+1}=3n_j+1;
   \tag{18}
   \]

5. `w` is a positive exact accelerated-cycle certificate.

### Proof

Theorem 2 gives the equivalence of 1--3.  If `D|C_0`, equation (16) gives
`D|C_j` for every rotation, and (5) becomes (18).  Positivity is immediate
from `C_j,D>0`.  The divisibility-to-exact-replay theorem `L-9904` proves that
the states are odd and that each displayed `a_j` is the exact valuation of
`3n_j+1`, giving 4--5.  Conversely, any exact cycle supplies the integral
solution of (4), so `[1]=0`. **QED**

### Corollary 4 -- the proposed universal gcd theorem is equivalent

Restrict to primitive positive-drift words.  Then

\[
 \boxed{
 \gcd(C_0,\ldots,C_{k-1})<D
 \quad\hbox{for every primitive }w\ne(2)}
\tag{19}
\]

holds if and only if there is no nontrivial positive accelerated Collatz
cycle.

The word `(2)` is the trivial positive cycle: `D=C_0=1` and `n_0=1`.
For every other primitive word, equality in (19) is, by Theorem 3, exactly a
nontrivial positive cycle.  Thus proving (19) still requires the unresolved
arithmetic content of positive-cycle exclusion.

## 6. Why cut defects do not complete the lattice attack

For a proper cyclic cut at rotation `j`, local `L-9906` gives

\[
 \Omega_j=C_0-C_j.
\tag{20}
\]

Under a cycle certificate,

\[
 \boxed{\Omega_j=D(n_0-n_j).}
\tag{21}
\]

Primitivity makes a proper-return defect nonzero, but then it merely gives
`|Omega_j|>=D`, fully compatible with distinct positive integer cycle states.
Its exact 2-adic valuation cannot by itself obstruct divisibility by the odd
integer `D`.

The primitive positive-drift test word

\[
 w=(1,1,3)
\tag{22}
\]

has

\[
 D=5,
 \qquad(C_0,C_1,C_2)=(19,31,49),
 \qquad |C_0-C_1|=12,
 \qquad |C_0-C_2|=30.
\tag{23}
\]

Thus every rotation constant and both displayed cut defects exceed `D`, but
`D` still fails to divide `C_0`.  Neither a universal small rotation nor a
universal small cut defect is available.

Order and sign are also essential.  The primitive word `(1,2)` has

\[
 D=-1,
 \qquad(C_0,C_1)=(5,7),
\tag{24}
\]

and gives the exact negative cycle `-5 -> -7 -> -5`.  Smith form and word
primitivity permit it; the unresolved arithmetic is specifically the
positive-drift, positive-state case.

## 7. Adversarial boundary

1. **Smith form is order-blind.**  It depends only on `k` and `A`, so it
   cannot distinguish a promising arrangement of the same valuation multiset.
2. **The augmented class restores all difficulty.**  The class of `1`
   depends on `C_0`; deciding whether it vanishes is exactly the cycle test.
3. **A strict gcd bound is not progress unless independently derived.**  The
   statement `G<D` for all nontrivial primitive words is the desired
   no-positive-cycle theorem in new notation.
4. **Cut divisibility is necessary, not contradictory.**  Nonzero multiples
   of `D` are expected at distinct states of an integral cycle.
5. **Finite searches are not proof inputs.**  Exact enumeration can test the
   formulas and reject bounded words, but it cannot establish (19).
6. **Divergent orbits are outside scope.**  This matrix treats finite cyclic
   valuation words only.  Excluding all positive cycles would not by itself
   exclude a divergent Collatz trajectory.

## Strongest conclusion

> The cyclic linear system has the simplest possible nontrivial Smith form,
> but its sole augmented cokernel class vanishes exactly when the original
> accelerated word is a positive cycle certificate.  Therefore Smith normal
> form, the associated resultant, and rotation gcds do not bypass the cycle
> problem.  A successful continuation must add genuinely new arithmetic—for
> example, a theorem producing a prime divisor of `D` that does not divide
> `C_0`—rather than restating augmented-lattice nonsolvability.

## Suggested next attack

Factor only conceptually: choose a prime power `p^e || D` and study the
normalized rotation sum

\[
 C_0=3^{k-1}\sum_{j=0}^{k-1}2^{A_j}3^{-j}
      \pmod {p^e}.
\tag{25}
\]

The next theorem must prove nonvanishing for at least one divisor of `D` from
word structure not already equivalent to `D` not dividing `C_0`.  Primitive-
divisor, cyclotomic, and character-sum proposals should first be tested
against words that become constant after reducing the exponents modulo the
relevant multiplicative order.
