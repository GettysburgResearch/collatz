# The proposed Hermite–Padé family is an exact binomial power

**Status:** PROPOSED exact algebraic result, with standalone rational-arithmetic
checks. This does not prove Collatz, coefficient stopping, first-crossing
exclusion, or a new periodicity bound. It diagnoses the mathematical content of
the supplied approximation construction, not the prospects of all Hermite–Padé
methods.

## Sources and scope

The reviewed input is `route_4_diophantine_sc_fc_and_powered_cycles_pr148/` in
the user-supplied `collatz_multi_route_proposals_2026-11-20.zip`. In particular,
the claims are in `PROOF_AND_IDEAS.md`, Section 3; the actual implementation is
`verify_type1_hermite_pade_prototype` in `verify_diophantine_cycles.py`.

The repository baseline is main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Its
[`research/open-obligations/README.md`](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/open-obligations/README.md)
asks for a reduced-height approximation with **explicit nonzero error and
denominator bounds**. Merely displaying a high vanishing order does not meet
that obligation. No status of the resident Padé results is changed here.

## HP-001 — exact identification of the supplied prototype

The program returns

\[
\begin{aligned}
P_0(z)&=-27+28z^2,\\
P_1(z)&=54+54z-8z^2,\\
P_2(z)&=-27-54z+z^2.
\end{aligned}
\]

Its series recurrence computes `(1+z)^(i/3)`, despite the documentation saying
`(1-z)^(i/3)`. Let `y=(1+z)^(1/3)` and substitute `z=y^3-1`. Direct expansion
gives the polynomial identity

\[
P_0(z)+P_1(z)y+P_2(z)y^2=(y-1)^8.                 \tag{1}
\]

Thus its verified leading coefficient `1/6561=1/3^8` is exactly the leading
coefficient of `((1+z)^(1/3)-1)^8`. The computation is correct for the **plus**
series, but it is an elementary binomial power in a cubic algebraic basis.

For the documented **minus** series with the polynomials unchanged, the
coefficient of `z^2` is **36**; the claimed order eight is false. The simple
sign repair is to replace every `P_i(z)` by `P_i(-z)`, obtaining

\[
P_0(-z)+P_1(-z)(1-z)^{1/3}+P_2(-z)(1-z)^{2/3}
=((1-z)^{1/3}-1)^8.                              \tag{2}
\]

The implementation never evaluates the form on any period-dependent Collatz
input. The document's assertion that it confirms nonvanishing at such inputs
for periods through twelve therefore exceeds the executable evidence.

## HP-002 — complete classification for equal degree budgets

Let `m>=2`, `d>=0`, and `N=m(d+1)-1`. Work with the formal power series branch
`y=(1-z)^(1/m)` satisfying `y(0)=1`. For polynomials `P_i` of degree at most `d`,
put

\[
L(z)=\sum_{i=0}^{m-1}P_i(z)y^i.
\]

If `L(z)=O(z^N)` and `L` is not the zero function, then there is a nonzero
rational constant `c` such that

\[
L(z)=c(y-1)^N.                                   \tag{3}
\]

In particular, its order is exactly `N`; imposing order `N+1` forces all
polynomials to be zero.

**Proof.** Substitute `z=1-y^m`. The space of the resulting polynomials

\[
R(y)=\sum_{i=0}^{m-1}P_i(1-y^m)y^i
\]

is exactly the space of polynomials of degree at most `N`: the exponents
`i+mk`, with `0<=i<m` and `0<=k<=d`, enumerate `0,...,N`, and the change of
basis within each residue class modulo `m` is triangular with nonzero diagonal.
Since `dz/dy=-m` at `y=1`, order at `z=0` equals order at `y=1`. A polynomial
of degree at most `N` vanishing to order at least `N` at `1` is a multiple of
`(y-1)^N`. The change of basis is injective, so the zero polynomial corresponds
only to the zero vector of `P_i`. This proves the statement. □

One explicit normalization is

\[
P_i(z)=\sum_{\substack{k\ge0\\i+mk\le N}}
 (-1)^{N-i-mk}\binom{N}{i+mk}(1-z)^k.             \tag{4}
\]

For `m=3,d=2`, (4) is exactly the sign-corrected prototype in (2).

## HP-003 — unequal budgets reduce to sparse-polynomial contact

Let `d_i>=0` be arbitrary degree budgets, and define

\[
S=\{i+mk:0\le i<m,\ 0\le k\le d_i\},\qquad M=|S|.
\]

The same substitution identifies the approximation space with
`span_Q{y^s:s in S}`. A nonzero form has order at most `M-1` at `z=0`.
The unique one-dimensional space attaining this maximum is represented by

\[
R_S(y)=\sum_{s\in S}\frac{y^s}{\prod_{t\in S,t\ne s}(s-t)}.             \tag{5}
\]

It has exact order `M-1` at `y=1`, with leading coefficient `1/(M-1)!`.

**Proof.** The matrix of the first `M` derivatives of `y^s` at `1` has rows
`(s)_k`, `0<=k<M`, where `(s)_k` is the falling factorial. Since these are
monic polynomials in `s` of degrees `k`, its determinant is a nonzero
Vandermonde product. This proves the upper bound and uniqueness up to scale
at order `M-1`. Lagrange interpolation gives

\[
\sum_{s\in S}\frac{f(s)}{\prod_{t\ne s}(s-t)}=0\quad(\deg f<M-1),
\]

and the same sum is `1` for a monic polynomial of degree `M-1`. Apply this to
the falling factorials to obtain all the stated derivative identities. □

After clearing denominators, `R_S(y)` is divisible by `(y-1)^(M-1)` in
`Q[y]`. Unequal budgets can leave a nonconstant quotient, so (3) is not claimed
for unequal budgets. Equation (5) describes what must actually be studied:
the quotient's height, norm, and word-dependent arithmetic, rather than the
number of formal cancellation equations alone.

## HP-004 — the algebraic norm contains the entire displayed vanishing

Fix rational `r>0` and put `z=1-r`. In the algebra
`A=Q[Y]/(Y^m-r)`, use the determinant norm; this formulation also handles
reducible `Y^m-r`. Its elementary identity is

\[
\operatorname{Norm}_A(Y-1)=(-1)^m(1-r)=(-1)^m z.   \tag{6}
\]

For example, (6) follows by evaluating the monic polynomial `Y^m-r` at `1`
and taking the product of `(root-1)` over all roots. By multiplicativity,

\[
\operatorname{Norm}_A((Y-1)^N)=((-1)^m z)^N.       \tag{7}
\]

At the proposed Collatz evaluation `r=3^q/2^j`, write `D=2^j-3^q`. For the
normalized equal-budget form,

\[
2^{jN}\,\big|\operatorname{Norm}_A(L)\big|=|D|^N. \tag{8}
\]

This is an exact difference-of-powers identity, not a new lower bound for
`D`. Nonvanishing for `j,q>0` already follows from unique factorization,
`2^j!=3^q`. For unequal budgets, writing
`R_S(Y)=(Y-1)^(M-1)H(Y)` gives

\[
\operatorname{Norm}_A(R_S)=((-1)^m z)^{M-1}
                           \operatorname{Norm}_A(H).                 \tag{9}
\]

Therefore the high contact alone does not provide a better arithmetic
height/error ratio: the same small factor appears to that full power in its
norm. A useful new construction must bound the remaining factors and the
cleared denominator in the actual native problem. This result does not rule
out differently chosen functions, combined moments, or a genuinely favorable
quotient `H`; it shows that the supplied equal-budget example cannot by itself
justify the proposed improvement.

## HP-005 — asymmetric maximal contact has no residual real cancellation

This strengthens HP-003 without assuming equal degree budgets. In fact, let
`S={s_0<...<s_K}` be any set of nonnegative integer exponents with `s_0=0`.
Multiply (5) by the unique positive rational constant that makes its
coefficients relatively prime integers, and call the result `R`. Then

\[
R(Y)=(Y-1)^K H(Y),\qquad
H\in\mathbb Z_{\ge0}[Y],\qquad H(0)\ge1.           \tag{10}
\]

Consequently, for every real `y>=0`,

\[
H(y)\ge1,\qquad |R(y)|\ge|y-1|^K.                \tag{11}
\]

The quotient degree is `s_K-K`. For `0<=y<=1`, its positive coefficients also
give `y^(s_K-K)H(1)<=H(y)<=H(1)`. Thus merely switching to unequal degree
budgets in this **maximal-contact radical-basis family** cannot introduce a
second small real factor after the known contact factor has been removed.
This does not rule out lower-contact forms with different arithmetic height,
or unrelated transcendental approximation constructions.

### Self-contained positivity proof

For a strictly increasing exponent list `s=(s_0,...,s_K)`, define initially
at distinct nonzero variables

\[
V_s(x_0,...,x_K)=
\frac{\det(x_i^{s_j})_{0\le i,j\le K}}
     {\prod_{0\le i<j\le K}(x_j-x_i)}.             \tag{12}
\]

We first prove directly that this is a polynomial with nonnegative integer
coefficients. With `x=(x_0,...,x_{K-1})`, it satisfies

\[
V_s(x,y)=\sum_{\substack{s_i\le r_i<s_{i+1}\\0\le i<K}}
 y^{\sum_{i=0}^K s_i-\sum_{i=0}^{K-1}r_i-K}\,V_r(x).                 \tag{13}
\]

The exponents of `y` are nonnegative: their minimum is `s_0`. Every allowed
list `r` is strictly increasing. Starting with `V_(s_0)(x_0)=x_0^(s_0)`,
(13) proves polynomiality and coefficient positivity by induction on the
number of variables. These are commonly called Schur alternants, but no
Schur positivity theorem is needed as an input here.

To verify (13), multiply its right side by the Vandermonde in `x`. Sum the
determinants by multilinearity in their columns. The result is

\[
y^{\sum s_i-K}\det\!\left(
  \sum_{r=s_j}^{s_{j+1}-1}x_i^r y^{-r}\right)_{0\le i,j<K}.
\]

Each entry is the geometric sum

\[
\frac{y\big(x_i^{s_j}y^{-s_j}-x_i^{s_{j+1}}y^{-s_{j+1}}\big)}{y-x_i}.
\]

After multiplying by `prod_i(y-x_i)`, the determinant becomes
`y^(sum s_i) det(U_j-U_(j+1))`, where the column `U_j` has entries
`x_i^(s_j)y^(-s_j)`. This is exactly the full numerator determinant in (12):
scale its columns by `y^(-s_j)`, subtract each next column from the previous
one, and expand along the last row, which is then `(0,...,0,1)`. This proves
(13) on distinct nonzero inputs, hence as a polynomial identity.

Now let the first `K` variables tend to `1`. Write
`Delta(S)=prod_(i<j)(s_j-s_i)>0`. Taylor expansion of the first `K` rows in
(12) replaces them, after division by their Vandermonde, with
`binom(s_j,a)`, `0<=a<K`. Expanding the resulting determinant along the last
row gives

\[
V_s(\underbrace{1,...,1}_{K},y)
 =\frac{\Delta(S)}{\prod_{a=0}^{K-1}a!}\,
    \frac{R_S(y)}{(y-1)^K}.                        \tag{14}
\]

Indeed, the cofactor omitting exponent `s_j` is its smaller Vandermonde
divided by `prod_(a=0)^(K-1) a!`; its signed ratio to `Delta(S)` is exactly
`1/prod_(t in S,t!=s_j)(s_j-t)`. This also establishes (14) at `y=1` by
continuity. For `K=0` the assertion is immediate and empty products are one.

By (13), the left side of (14) has nonnegative integer coefficients in `y`.
Its constant coefficient is strictly positive when `s_0=0`: in (13), choose
the unique maximal tuple `r_i=s_(i+1)-1`; this gives exponent zero and the
positive value `V_r(1,...,1)`. Thus the rational quotient of `R_S` has
nonnegative coefficients and positive constant coefficient.

Finally the normalized `R` has integer coefficients, and division by the
monic polynomial `(Y-1)^K` leaves an integer polynomial because its remainder
vanishes. Multiplication by the positive normalizing constant preserves the
coefficient signs just proved. Its constant is therefore a positive integer,
which proves (10) and (11). □

For this family the known `D` factor in (9) is not hiding an additional
positive-real cancellation. An arithmetic improvement must come from a
separately proved denominator or conjugate-factor estimate, or a different
approximation space. None follows from the cancellation count itself.

## Why `(j,q)` alone omits the cycle arithmetic

For shortcut Collatz, a length-`j`, weight-`q` parity word `w` has affine form
`T_w(n)=(3^q n+C_w)/2^j`. A positive periodic realizer is
`n=C_w/(2^j-3^q)`, and ordinary integrality requires the **whole** denominator
to divide `C_w`.

The words `1010` and `1100` have the same `(j,q)=(4,2)` and `D=7`, but their
constants are respectively `7` and `5`. Their realizers are `1` and `5/7`.
The first is the trivial positive integer cycle repeated; the second is a
noninteger rational cycle. The proposed approximation evaluated only at
`1-3^q/2^j` has identical value on these two words. It contains no test of
`7|C_w`. A later argument may incorporate `C_w`, primitivity and ordinary
replay, but none is present in the prototype.

## Other Route 4 audit findings

1. **The conditional SC/FC implication is valid.** In the shortcut map, let
   `tau(n)` be the first `j>0` with `3^q<2^j`, and `sigma(n)` the first strict
   descent below `n`; either may be infinite. Since the affine constant is
   nonnegative, `tau(n)<=sigma(n)`. The supplied FC statement is exactly
   `tau(n)=sigma(n)` for `n>=2`, including the automatic equality when both
   are infinite. This is Terras's coefficient-stopping-time conjecture, not a
   proved new local lemma. SC asserts finiteness of `tau(n)`; SC and FC together
   imply finite descent for every `n>1`, hence Collatz by strong induction.
   The implication does not establish either premise.

2. **Arbitrary subcritical endpoints do not necessarily descend.** The actual
   orbit `7,11,17,26,13,20,10,5,8` has `T^8(7)=8` with coefficient `243/256<1`.
   This is not a counterexample to FC: its first coefficient crossing is at
   time seven and gives `5<7`. This distinction is explicit in
   [Rozier–Terracol, arXiv:2502.00948v2, Definition 1.2](https://arxiv.org/html/2502.00948v2).
   That is a primary source for the prior status of the CST formulation.

3. **The printed convergent sides are wrong.** Of the listed values,
   `8/5`, `65/41` and `485/306` are **upper** approximants to `log_2(3)`, as
   certified exactly by `2^8>3^5`, `2^65>3^41`, `2^485>3^306`.
   Initial lower convergents are `1/1`, `3/2`, `19/12`, `84/53`, `1054/665`.
   The supplied program discovers candidate continued fractions using binary
   floating point, so it does not prove that an arbitrary-length generated
   table is the exact continued fraction, though each displayed side can be
   checked by integer powers.

4. **The proposed Farey-corridor forcing is unsupported.** The inequalities
   `j/q(j)<log_2(3)` do not imply recurrent closeness to that boundary. For
   every `L>=1`, the positive ordinary source `n=2^L-1` has its first `L`
   parities all odd and
   `T^j(n)=3^j 2^(L-j)-1`, `0<=j<=L`. Hence `j/q(j)=1` throughout that
   prefix. These sources vary with `L`; they do not refute any actual
   all-time positive-integer statement. They do show why an additional
   theorem forcing near-critical returns is needed before applying a
   near-equality logarithmic-form or Farey estimate. The signed fixed point
   `-1` provides the same all-odd pattern forever, outside the positive domain.

The substantive repair is HP-002/003/004: a complete algebraic description of
the proposed approximation space, including arbitrary degree budgets;
HP-005 additionally excludes residual real cancellation in its maximal-contact
members after primitive integer normalization. The
full Collatz obstruction remains ordinary-source control, or complete
word-dependent denominator exclusion, rather than a larger formal nullspace.

### The actual native Padé target is a different function

At the pinned source commit
[`82ca2f932438a9fe0897704ba62959ca23ec830f`](https://github.com/GettysburgResearch/collatz/tree/82ca2f932438a9fe0897704ba62959ca23ec830f/research/padic-repetition/claims),
`L-9407` identifies the native stack value with a sparse **2-adic** series
`sum_j (64/81)^(H_j)`. For fixed periodic increment words, `L-9418` constructs
delayed Gaussian-binomial approximants to a finite sum of Tschakaloff phases;
`T-9422` obtains the verified period-nine range from its explicit error and
height exponents. `L-9415` already gives an order-two homogeneous q-difference
equation for the combined native function, without claiming a theorem about
its values at the physical 2-adic argument.

The supplied cubic radical calculation is not an approximant to that native
function. It supplies neither its 2-adic error nor a denominator-height bound
for it. The theorems above are therefore an exact audit of the new proposed
family, not a ceiling theorem for the existing partial-theta route. A native
improvement must prove a nonzero error and reduced height for the actual
combined q-moments, or verify a value theorem at the relevant finite place.
