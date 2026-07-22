# Dyadic cyclotomic cutoff: exact closure of the two Newton-boundary families

Date: 2026-07-22

Status: theorem, scratch-only.  The shared repository was not edited.

## 1. Statement

Let `d=2^r` and let `q` be a primitive `2d`-th root of unity.  For

\[
 Q_u^{(5)}(q)=\frac1{(q;q)_u}
 \sum_{j=0}^u(2j+1)(-1)^j q^{5j(j+1)/2}
 {2u+1\brack u-j}_q,
\]

one has

\[
 \boxed{Q_{d-1}^{(5)}(q)\ne0,\qquad Q_{d-2}^{(5)}(q)\ne0.}
\]

The second assertion is understood directly for `d=2`, when `u=0` and
`Q_0=1`.  These are exactly the two families in which the computed
2-adic Newton polygon contains the otherwise forbidden slope `-1/d`.

Since `2d>2u+1` in both cases, `(q;q)_u` is nonzero.  It is therefore
enough throughout to prove nonvanishing of the numerator.

## 2. A root-of-unity Gaussian reduction

Put `L=2d`.  For `0<=k<L`, direct cancellation gives

\[
 {L-1\brack k}_q=(-1)^kq^{-k(k+1)/2}.                 \tag{1}
\]

More generally, write

\[
 2u+1=L-t,\qquad t=2e-1,\qquad u=d-e.
\]

For `k=u-j`, comparison with (1) gives, at `q^L=1`,

\[
 {L-t\brack k}_q
 =(-1)^kq^{-k(k+1)/2-(t-1)k}
   {k+t-1\brack t-1}_q.                              \tag{2}
\]

Indeed the quotient of the left side and `{L-1\brack k}_q` is

\[
 \prod_{s=1}^{t-1}\frac{1-q^{L-k-s}}{1-q^{L-s}}
 =q^{-(t-1)k}\prod_{s=1}^{t-1}
   \frac{1-q^{k+s}}{1-q^s}.
\]

Substitution in the numerator of `Q_u^(5)` shows that, up to a nonzero
common monomial and the common sign `(-1)^u`, it is

\[
 T_{d,e}(q)=\sum_{j=0}^{d-e}(2j+1)
 q^{2j^2+(d+e+1)j}
 {d+e-j-2\brack 2e-2}_q.                            \tag{3}
\]

Only `e=1,2` are needed below.

## 3. The family `u=d-1`

Here `e=1`, so the Gaussian factor in (3) is one.  Set

\[
 a_j=q^{2j^2+(d+2)j},\qquad 0\le j<d.
\]

Let `h=d/2` and `rho=q^2`, so `rho` is primitive of order `d`.  Then

\[
 a_j=\rho^{j^2+(h+1)j},\qquad a_{j+h}=-a_j.          \tag{4}
\]

The second identity follows because the exponent changes by `h` modulo
`d`.  Pairing `j` and `j+h` therefore gives

\[
 \sum_{j=0}^{d-1}(2j+1)a_j
 =-d\sum_{j=0}^{h-1}a_j.                            \tag{5}
\]

It remains to show that the half sum is nonzero.  For `d>=4`, put
`sigma=rho^2`, a primitive `h`-th root.  Since
`j^2+(h+1)j=j(j+1)+hj` is even,

\[
 H_d:=\sum_{j=0}^{h-1}a_j
 =\sum_{j=0}^{h-1}\sigma^{g(j)},\qquad
 g(j)=\frac{j(j+1)+hj}{2}.                          \tag{6}
\]

If `H_d=0`, the folded coefficient criterion for
`Phi_h(X)=X^(h/2)+1` would require the number of indices with
`g(j)=0 mod h` to equal the number with `g(j)=h/2 mod h`.
They are respectively two and zero:

* `g(j)=0 mod h` is equivalent to
  `2h | j(j+h+1)`.  The two factors have opposite parity.  If `j` is
  even, the only possibility in `0<=j<h` is `j=0`; if `j` is odd,
  the only possibility is `j+h+1=2h`, hence `j=h-1`.
* `g(j)=h/2 mod h` would make the even factor among `j` and `j+h+1`
  divisible by `h` but not `2h`.  In the same ranges the only possible
  multiples are `0` or `2h`, both divisible by `2h`.  Thus there is no
  such index.

So `H_d` is nonzero, and (5) proves the first assertion.  For `d=2`, the
half sum has the single term `H_2=1`, so the same conclusion holds.

## 4. The family `u=d-2`

Assume `d>=4`.  Here `e=2`.  Multiplying (3) by the nonzero factor
`(1-q)(1-q^2)` gives the Laurent polynomial

\[
 \begin{aligned}
 U_d(q)=\sum_{j=0}^{d-1}(2j+1)
 q^{2j^2+(d+3)j}(1+q^{-j})(1+q^{-j-1}).             \tag{7}
 \end{aligned}
\]

The formally added term `j=d-1` vanishes because `1+q^{-d}=0`.
Write the four exponents in the `j`-th summand as

\[
\begin{aligned}
 E_0&=2j^2+(d+3)j,\\
 E_1&=2j^2+(d+2)j,\\
 E_2&=2j^2+(d+2)j-1,\\
 E_3&=2j^2+(d+1)j-1.
\end{aligned}                                                    \tag{8}
\]

Reduce `U_d` modulo `q^d+1`.  Its coefficient at residue `1` is the
difference between the coefficient masses at exponents `1` and `1+d`
modulo `2d`.  We now compute this difference exactly.

The congruence `E_0=1 mod d` is

\[
 2j^2+3j-1=0\pmod d.                                \tag{9}
\]

Modulo two it has the unique solution `j=1`, and its derivative `4j+3`
is odd.  Hensel lifting therefore gives a unique solution `j_0 mod d`.
Neither `E_1` nor `E_2` can be `1 mod d`: the first is even, while the
second would require

\[
 j(j+1)=1\pmod{d/2},
\]

which is impossible because the left side is even and `d/2>=2`.

Finally `E_3=1 mod d` has the unique solution

\[
 j_1=d-1-j_0,                                         \tag{10}
\]

because substitution turns its congruence into (9).  Direct subtraction
also gives

\[
 E_3(j_1)-E_0(j_0)=d(3d-4-6j_0),                    \tag{11}
\]

which is divisible by `2d`.  Thus the two contributions lie in the same
one of the residue classes `1` and `1+d`, and have the same sign in the
negacyclic remainder.  Their total weight is

\[
 (2j_0+1)+(2j_1+1)=2d.                               \tag{12}
\]

Consequently

\[
 \boxed{[q^1](U_d\bmod(q^d+1))=\pm2d\ne0.}           \tag{13}
\]

This proves `U_d(q)`, hence `T_{d,2}(q)`, hence `Q_{d-2}^{(5)}(q)` is
nonzero.  The omitted case `d=2` is `Q_0=1`.

## 5. What this closes and what remains

Exact Newton-polygon scans show that for `d` the least power of two above
`u`, a slope `-1/d` occurs only at `u=d-2,d-1`.  Sections 3--4 prove that
this necessary local slope does **not** arise from the cyclotomic factor
`Phi_(2d)` in either boundary family.

The remaining all-order dyadic task is therefore the uniform Newton-gap
lemma for `u<=d-3` (and for larger dyadic `d`): prove that the 2-adic
Newton polygon of `Q_u^(5)(-1+x)` has no segment of slope `-1/d`.  The
bounded scans support this sharply, but that general Newton statement is
not proved here.



