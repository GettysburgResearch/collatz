# The surviving principal factor can be fully absorbed at the correct fibre

## Purpose and result

The elementary principal-survival theorem leaves the irreducible factor
`M=X^b-2^a` in the residual polynomial denominator. One proposed next
step was to transport positivity at its real root to nondivisibility at
`X=3` modulo `|M(3)|`, using all cyclic inequalities.

The following unbounded family shows why those inputs do not suffice.
For every `g>=4` with `g=4 mod5`, there is a primitive positive rational
Collatz cycle whose entire orbit is above `19/10`, with:

\[
\gcd_{\mathbb Q[X]}(F,Q)=1,\qquad
M=X^3-32,\quad |M(3)|=5,
\qquad 5\mid Q(3).
\]

The full 5-primary part of `2^A-3^p` is absorbed by `Q(3)` at the
actual distinguished evaluation `X=3`. The full denominator is not
absorbed. These are exact rational controls, not integer Collatz cycles.

Thus principal survival must be combined with a new restriction on the
other factors or on simultaneous arithmetic integrality. Positivity
alone does not furnish the missing principal-ideal witness.

## 1. Word and exact factorization

Take `A=5g`, `p=3g`, and the binary word

\[
w=01110\,(11100)^{g-1}.
\tag{1}
\]

It has odd positions

\[
d_{3j+r}=5j+r+k_j,\qquad 0\le j<g,\quad0\le r<3,
\quad k_0=1,\quad k_j=0\ (j>0).
\]

Put

\[
B(X)=X^2+2X+4,
\quad S_g(X)=\sum_{j=0}^{g-1}32^jX^{3(g-1-j)}.
\]

Then its exact numerator and binomial are

\[
Q_g(X)=B(X)\bigl(S_g(X)+X^{3(g-1)}\bigr),
\qquad F_g(X)=X^{3g}-32^g.
\tag{2}
\]

There is no polynomial cancellation. The roots of `B` have modulus
2, whereas the roots of `F_g` have modulus `32^(1/3)>3`. At a root
`alpha` of `F_g` with `alpha^3!=32`, the identity
`(X^3-32)S_g=F_g` gives `S_g(alpha)=0`, leaving the nonzero term
`alpha^(3(g-1))`. At a root with `alpha^3=32`, the second factor of
`Q_g` equals `(g+1)32^(g-1)`, also nonzero. Thus `gcd(F_g,Q_g)=1`.

The word is primitive. In its cyclic sequence of zero runs between
the length-three odd runs, one zero run has length one, one has
length three, and all others have length two. A nontrivial repetition
would repeat the unique run of length one, which is impossible.

## 2. Correct-fibre divisibility of the principal factor

Writing `D_g=32^g-27^g`, evaluation at 3 gives

\[
C_g=Q_g(3)
=19\left(\frac{D_g}{5}+27^{g-1}\right).
\tag{3}
\]

Since `32=27+5`, the binomial theorem modulo 25 gives

\[
D_g\equiv5g\,27^{g-1}\pmod{25}.
\]

For `g=4 mod5`, this proves `v_5(D_g)=1` and

\[
C_g\equiv19(g+1)27^{g-1}\equiv0\pmod5.
\]

Thus the whole principal divisor and the full 5-primary component of
`D_g` divide the actual numerator. Because the polynomial gcd is one,
this is also `5 | Q_0(3)` for the residual numerator. No norm or wrong
conjugate is being substituted for the distinguished fibre.

## 3. All cyclic states stay above a fixed positive floor

The rational fixed point of the word is

\[
x_g=\frac{C_g}{D_g}
=\frac{19}{5}+\delta_g,
\qquad
\delta_g=\frac{19\,27^{g-1}}{32^g-27^g}>0.
\tag{4}
\]

The branch maps here are `x -> x/2` for a zero and
`x -> (3x+1)/2` for a one. The fixed word is legal on rational
numbers with odd denominator. For completeness, if `C_j` is the
correction numerator of the cyclic rotation starting at position `j`,
the affine identity gives

\[
2C_{j+1}=3^{w_j}C_j+w_jD_g.
\]

Modulo 2 this forces the rational state's numerator parity to be
`w_j`, since `D_g` is odd. The states `C_j/D_g` therefore realize
the stated branch word, and are all positive.

For the stronger uniform floor, the initial block `01110` sends `x` to
`(27x+38)/32`. Its first intermediate state is `x/2>19/10`; its
next three odd steps strictly increase it. The last intermediate
state is `(27x+38)/32>19/5` whenever `x>19/5`.

Every subsequent block `11100` sends `z` to
`(27z+19)/32`. This map preserves the interval `(19/5,infinity)`.
Within such a block, the first three states increase; the two later
halvings end at a state still above `19/5`. All of those intermediate
states are also above `19/5`. Hence every phase of the cycle is
strictly greater than `19/10`.

This rules out an explanation based only on the presence of a rational
state between zero and one.

## 4. The other denominator factors really remain

These words do not accidentally supply integer Collatz cycles.
For `g=4`, direct integer comparison in (3) gives `4<x_g<5`.
For `g>=9`,

\[
0<\delta_g\le\delta_9<\frac15,
\qquad \frac{19}{5}<x_g<4.
\]

The last strict bound follows from the exact comparison
`32^9>122*27^8`. Monotonicity follows because

\[
\frac{\delta_{g+1}}{\delta_g}
=\frac{27D_g}{D_{g+1}}<1,
\qquad D_{g+1}=32D_g+5\,27^g.
\]

The allowed values are `g=4,9,14,...`, so all fixed points are
nonintegral. In particular, the complete `D_g` does not divide `C_g`.

The finite script `check_principal_fiber_control.py` checks sample
members, exact branch legality, all cyclic floors, primitivity,
the displayed integer formulas, and the endpoint comparisons. The
unbounded family and its polynomial gcd statement are proved above;
they are not inferred from those samples.

## Scope for the central proof attempt

This control directly tests a proposed use of the new principal
survival theorem. A proof of full cycle exclusion must still address
simultaneous divisibility through all surviving factors. The family
does not refute a method that uses additional integrality conditions,
other evaluation components, or a new interaction between them.
It refutes the universal claim that polynomial coprimality, real
positivity, primitivity, and a uniform cyclic floor above one already
force a witness in the principal factor alone.
