# A precise limitation of folds within the Mersenne family

This concerns one particular symbolic folding grammar, not arbitrary
certificate transformations and not the possibility of proving the theorem.

Let `x_e=3^e-1`, `e>=1`. A prefix of the ordinary shortcut trajectory has
`q` odd steps and `A` total shortcut steps. Its affine formula is

\[
 T^A(x_e)=\frac{3^{e+q}-D}{2^A},
 \qquad D=3^q-C,
\]

where `C` is the usual positive affine correction of the parity word.
Here `A` is the total division clock, not the odd count. For an accelerated
word, it is the sum of its odd division exponents, plus any initial even
steps.

Consider symbolic paired folds that compare `x_e` with a smaller
`x_f`, `f<e`, by matching the coefficients and constants of these affine
formulas, allowing the two endpoints to differ by a power of two. Such a
fold necessarily matches

\[
 e+q_e=f+q_f,\qquad D_e=D_f.
\tag{1}
\]

If `x_e` has a supplied finite certificate to 1 with total odd count `q`
and shortcut clock `A`, define

\[
 \kappa(e)=2(e+q)-A.
\]

Appending the ordinary `1 -> 2 -> 1` cycle changes `(q,A)` by `(1,2)`, so
this value does not depend on terminal padding. Determinism makes it
independent of the choice of finite certificate to 1.

Every fold satisfying (1) preserves `kappa`: after the two displayed
endpoints are aligned by even steps, their total `e+q` and their clocks
agree; they then use a common terminal suffix.

However, `3n+1<=4n` at every positive odd input gives

\[
 2^A\le4^q(3^e-1),
 \qquad
 \kappa(e)\ge2e-\log_2(3^e-1)
   >(2-\log_2 3)e.
\tag{2}
\]

Consequently a finite collection of certified starting exponents, together
with only folds of type (1), can cover only finitely many exponents: their
`kappa` values belong to the finite collection of initial values, while
(2) bounds `e` in terms of that collection. Even if every Mersenne were
known to converge, infinitely many first occurrences of `kappa` would
remain outside a smaller-exponent recursion of this restricted kind.

The escape is to change the shape of the certified source rather than
fold only to another power-of-two source. The companion valuation-reset
grammar does exactly that on its explicit guards: it replaces a power-of-two
source prefix by a longer certificate whose every inserted state is smaller
than the removed state. It therefore does not preserve the invariant above.
