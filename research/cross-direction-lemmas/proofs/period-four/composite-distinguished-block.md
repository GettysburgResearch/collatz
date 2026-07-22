# Distinguished carry block for a general peeled cyclotomic order

Date: 2026-07-22

Status: exact scratch-only lemma.  The shared repository is untouched.  This
selects, at every residual root order, one factorial block with precisely the
same carry deficit as the `q=1` odd-prime problem.  It does not prove that the
residual Rogers--Szego value is a unit after reduction modulo `p`.

## Statement

Recall the exact block decomposition

\[
 Q_u^{(5)}=\sum_{b=0}^uD_{u,b}F_{u-b,b}
\]

and, at a primitive `m`-th root in odd characteristic `p` with `p` not
dividing `m`, the factorial-block order

\[
 V_{p,m}(u,b)=
 W_p(\lfloor(2u+1)/m\rfloor)-W_p(\lfloor u/m\rfloor)
 -W_p(\lfloor(u-b)/m\rfloor)-W_p(\lfloor(2b+1)/m\rfloor)
 +2W_p(\lfloor b/m\rfloor),                                      \tag{1}
\]

where `W_p(n)=sum_(j=1)^n p^v_p(j)`.

Write

\[
 u=mB+r,\qquad0\le r<m,
 \qquad \delta=\left\lfloor{2r+1\over m}\right\rfloor\in\{0,1\}.
\]

Put `h=floor(m/2)` and choose the distinguished block

\[
 b_*=
 \begin{cases}
 0,&\delta=0,\\
 h,&\delta=1.
 \end{cases}                                                       \tag{2}
\]

(For `m=1`, this says `b_*=0`.)  Then `b_*<=u` and

\[
 \boxed{V_{p,m}(u,b_*)=
 W_p(2B+\delta)-2W_p(B)-\delta.}                                  \tag{3}
\]

If `p^a m>2u+1`, then

\[
 \boxed{2V_{p,m}(u,b_*)+1<\varphi(p^a).}                           \tag{4}
\]

Thus the arithmetic gap needed after peeling `Phi_(p^a m)` is uniform in
the residual order `m`; all additional difficulty is in cancellation and
the residual `F` value.

Finally set `R=r-b_*`.  It satisfies `0<=R<m`, and exact q-Lucas gives

\[
 \boxed{F_{u-b_*,b_*}(\zeta)=2^B F_{R,b_*}(\zeta)}.                \tag{5}
\]

The already known complementary cancellation condition

\[
 R\text{ odd},\qquad \zeta^{2b_*+R+1}=-1                         \tag{6}
\]

occurs for this distinguished state exactly when

\[
 \boxed{m\equiv0\pmod4,\qquad
 r\in\{m/2-1,m-1\}.}                                              \tag{7}
\]

This explains why two boundary residues, rather than an arbitrary family,
are singled out by the carry-optimal block.

## Proof of the floor collapse

The top two floors in (1) are

\[
 \lfloor u/m\rfloor=B,
 \qquad \lfloor(2u+1)/m\rfloor=2B+\delta.                         \tag{8}
\]

If `delta=0`, then `b_*=0`; the remaining three floors are `B,0,0`,
and (3) follows.

If `delta=1`, then `r>=floor(m/2)=h`.  Hence

\[
 \lfloor(u-h)/m\rfloor=B,
 \quad \lfloor(2h+1)/m\rfloor=1,
 \quad \lfloor h/m\rfloor=0.                                    \tag{9}
\]

Substitution again gives (3).  It also gives
`u-b_*=mB+(r-b_*)`, proving the residual form in (5); (5) itself is the
exact root-of-unity q-Lucas block identity.

## Carry gap

Perform the base-`p` addition

\[
 B+B+\delta=2B+\delta.
\]

If `c_i` is its carry out of digit `i-1`, the digit formula for `W_p`
telescopes to

\[
 V_{p,m}(u,b_*)=(p-1)\sum_{i=1}^{a-1}c_i p^{i-1}.                 \tag{10}
\]

The hypothesis `p^a m>2u+1` implies

\[
 p^a>{2u+1\over m}>2B+\delta-1,
\]

and since the right integer is
`floor((2u+1)/m)=2B+delta`, it follows that `p^a>2B+delta`.
There is consequently no outgoing carry at digit `a`.  Since every carry
is zero or one,

\[
 0\le V_{p,m}(u,b_*)\le p^{a-1}-1.                               \tag{11}
\]

For odd `p`, (4) follows exactly as in the `m=1` carry lemma:

\[
 2V+1\le2p^{a-1}-1<(p-1)p^{a-1}=\varphi(p^a).
\]

## The two complementary residues

If `m` is odd, `-1` is not a power `zeta^j` with integral `j` modulo `m`,
so (6) is impossible.  Let `m` be even.

For `delta=0`, `b_*=0` and `R=r<m/2`.  Congruence (6) forces
`r+1=m/2`, hence `r=m/2-1`.  This `R` is odd exactly when `m` is divisible
by four.

For `delta=1`, `b_*=m/2` and `R=r-m/2`.  Congruence (6) becomes
`R+1=m/2`, hence `r=m-1`; again `R` is odd exactly when `4|m`.
This proves (7).

## Exact remaining caveat

Equations (3)--(5) do **not** by themselves bound the multiplicity of the
sum over `b`.  Even if `F_(R,b_*)(zeta)` is nonzero in characteristic zero,
its algebraic value may reduce to zero at a prime above `p`.  A complete
composite-order descent must therefore retain a residual finite-field value
or resultant state, as well as the factorial carry weight.  The lemma here
closes only the arithmetic and state-selection part of that descent.


