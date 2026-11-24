# Actual return towers: a growth bound, a repetition rank, and a finite obstruction

23 November 2026. Parent PR182:
`c369ae3c426ec6aaf9a280ec9578b9910c2147d5`.

**Status: PROPOSED written theorems with finite Lean arithmetic and
exact ordinary controls. The iterated denominator-eight exclusion and
full Collatz remain OPEN.**

The parent controls every individual paid carry excursion. This note
controls its iteration in three ways. First, arbitrary paid excursions
obey a source-dependent upper bound on the growth of successive unpaid
run lengths. Second, a fixed expanding return has an exact integer
valuation rank and therefore cannot repeat forever at one positive
ordinary source. Third, explicit actual finite towers show that physical
height and the true scalar potential can increase repeatedly while the
current shifted valuation remains unchanged. None of these statements
turns changing finite sources into a fixed all-time realization.

## 1. Actual finite returns and pinned inputs

Use the positive odd map

\[
U(q)=(3q+1)/2^{g(q)},\qquad g(q)=v_2(3q+1),\qquad
h(q)=\sum_{i\ge0}g(U^iq)/3^{i+1}.
\]

The actual scalar satisfies

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).
\tag{1}
\]

The exact source is the parent head above,
`research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`, R8-G1.
The local return input is
`research/scalar-rigidity-round9-20261123/CARRY_RETURN.md`, R9-C1--R9-C4
at that same head. Its complete ordinary assertions are retained:

* `L=(2,1)` has map `L(q)=(9q+7)/8`, with `L(q)+7=(9/8)(q+7)`.
* At an actual `h(q)=7/8` state, exactly
  `m=(v_2(q+7)-1)/3` unpaid L pairs precede the next paid excursion.
* Every paid first excursion, normalized to end at scalar `7/8`, has
  physical endpoint at most `P(x)=(9x+5)/32` from its entrance x.
  No bound on the integer carries is assumed.
* Such a return exists in a finite source-dependent odd-clock budget.
* If the set of positive odd sources with scalar `7/8` is nonempty,
  its least member is at least `2^34-7`. Therefore every member has
  that same lower bound.

The finite physical majorant also applies to a closed candidate carry
prefix: the candidate need not equal the actual infinite scalar.
Accordingly Sections 2--3 apply to any finite ordinary tower satisfying
those literal return conditions. An actual equality supplies an
unbounded sequence to which every finite bound would apply.

## 2. The complete shifted recurrence for arbitrary paid words

Let q_j be successive normalized return boundaries, let m_j be the
number of unpaid pairs in the j-th return, and put

\[
X_j=q_j+7,\qquad M_j=\sum_{i<j}m_i,\qquad\lambda=\frac98.
\]

If x_j is the entrance to the paid excursion, then
`x_j+7=lambda^(m_j)X_j`. The complete P majorant gives

\[
\boxed{X_{j+1}\le
\frac9{32}\lambda^{m_j}X_j+\frac{83}{16}.}
\tag{2}
\]

Since `x_j>=3`, its shifted value is at least ten, and

\[
\frac{P(x_j)+7}{x_j+7}
=\frac9{32}+\frac{83}{16(x_j+7)}\le\frac45.
\]

Thus every finite tower has

\[
\boxed{X_j\le X_0\lambda^{M_j}(4/5)^j,\qquad
2^{3m_j+1}\le X_j.}
\tag{3}
\]

The second inequality is the complete shifted-valuation requirement
for the next unpaid run. It is additional ordinary source information;
an arbitrary sequence of symbolic low-run lengths need not satisfy it.

At actual `7/8` states the parent's least-source theorem gives
`X_j>=2^34`, including every unpaid entrance. Consequently (3) sharpens
to

\[
\boxed{X_j\le X_0\lambda^{M_j}\rho^j,
\qquad\rho=\frac9{32}+\frac{83}{2^{38}}
=\frac{77309411411}{274877906944}<1.}
\tag{4}
\]

This use of the least-source theorem supplies a universal lower bound
on the specified scalar level set. It does not identify any return
boundary with a pressure maximum.

## 3. A positive fixed-source growth theorem for successive valuations

**R10-T1 (arbitrary-return growth bound).** Let `B=bl(X_0)`. For every
finite ordinary tower in Section 2 and every displayed next run m_j,

\[
\boxed{3\cdot15^j m_j<(B-1)16^j.}
\tag{5}
\]

This permits arbitrary paid words and arbitrarily large carries.

**Proof.** Drop the factor `(4/5)^j<=1` in (3), use `X_0<2^B`,
and raise the resulting inequality to the fifth power. The exact
comparison `9^5=59049<65536=2^16` says `lambda^5<2`. Hence

\[
2^{15m_j+5}\le X_j^5<2^{5B+M_j},
\qquad15m_j<5(B-1)+M_j.
\tag{6}
\]

Set `T_j=M_j+5(B-1)`. Then

\[
15T_{j+1}=15T_j+15m_j<16T_j.
\]

Induction gives `15^j T_j<=5(B-1)16^j`. Multiply the strict inequality
`15m_j<T_j` by `15^j`, combine, and cancel five to obtain (5).

For one fixed ordinary source, a proposed infinite return schedule
violating (5) is impossible. For example, a lower bound
`m_j>=c beta^j` with `c>0` and `beta>16/15` cannot persist for
arbitrarily large j. This is a growth restriction, not a decreasing
rank: constant or sufficiently slowly growing run lengths satisfy it.

### The sharper real budget on the exact scalar level set

Define

\[
\theta=-\frac{\log\rho}{\log\lambda},\qquad
\alpha=1+\frac{\log_2\lambda}{3}=\log_8 9,
\qquad C_0=\frac{\log_2X_0-1}{3}.
\]

Here `theta=10.7698983756...` and `alpha=1.0566416671...`; these
decimals are explanatory, and the exact formulas are used.

For an actual `7/8` return tail, (4) and `X_j>=2^34` imply

\[
M_j\ge\theta j+\frac{\log(2^{34}/X_0)}{\log\lambda}.
\tag{7}
\]

If q_0 is a global least source at this scalar, `X_j>=X_0`, so the
stronger prefix condition is simply `M_j>=theta j` for every j.
For any actual starting source, (7) implies
`liminf M_j/j>=theta`.

The next-run inequality in (3) further gives

\[
m_j\le C_0+(\alpha-1)(M_j-\theta j).
\]

Writing `E_j=M_j-theta j` yields
`E_(j+1)<=alpha E_j+C_0-theta`. Since `E_0=0`, induction proves

\[
\boxed{m_j\le\theta+(C_0-\theta)\alpha^j.}
\tag{8}
\]

The coefficient is positive: `X_0>=2^34` gives `C_0>=11`, and the
exact comparison `rho lambda^11>1` gives `theta<11`. Thus (8)
improves the exponential base in (5). Both estimates leave the
constant schedule `m_j=11` numerically compatible. The next section
rules out that one literal return type by different integer information.

## 4. An exact repetition rank for the expanding return R

Fix

\[
R=L^{11}P,\qquad
a=9^{12}=282429536481,\qquad b=2^{38}=274877906944,
\]

\[
d=a-b=7551629537,\qquad
c=7a-29\cdot2^{34}=1478790549031.
\]

The complete word has 24 odd transitions and binary clock 38, with

\[
bR(q)=aq+c.
\tag{9}
\]

Its slope exceeds one. Define the positive integer

\[
Z(q)=dq+c=d(q+7)+83\cdot2^{34}.
\tag{10}
\]

**R10-T2 (exact constant-return run length).** For every positive odd
q, the maximum number of consecutive literal R words is exactly

\[
\boxed{N(q)=\left\lfloor\frac{v_2(Z(q))-1}{38}\right\rfloor.}
\tag{11}
\]

In particular

\[
N(q)\le\left\lfloor\frac{\operatorname{bl}(Z(q))-2}{38}\right\rfloor.
\tag{12}
\]

**Proof.** The literal source class for R is equivalent to
`aq+c=b mod 2b`. Because q is odd, this is equivalent to
`Z(q)=0 mod 2b`, or `v_2(Z(q))>=39`. The complete finite valuation
word has a single ordinary cylinder, so this endpoint congruence
certifies all 24 prescribed gaps, not merely its composite quotient.
This is also obtained directly from R9-C1's complete source class.

The full affine equality gives

\[
bZ(R(q))=aZ(q).
\tag{13}
\]

Since a is odd, every literal R reduces this valuation by exactly 38.
Conversely, while the valuation is at least 39 the next R is literal.
The integer Z(q) is positive, so its valuation is finite. Iteration
therefore gives exactly (11), and `v_2(Z)<=bl(Z)-1` gives (12).

This supplies a genuine integer rank for a constant return type,
including its complete additive term. It neither bounds the change
of that rank when a different paid excursion occurs nor proves that
the same rank works across changing unpaid lengths. Fixed-word affine
center arguments already occur in the repository; the present role
is to expose the exact return-type budget and its reset boundary.

## 5. Actual finite towers with constant shifted valuation

**R10-T3 (ordinary expanding towers).** For every N>=1 there is an
explicit positive odd source q whose actual orbit contains N
consecutive expanding R returns, such that at all N+1 boundaries

\[
v_2(q_j+7)=34,\qquad
0<h(q_{j+1})<h(q_j)<\frac78,
\qquad q_{j+1}>q_j.
\tag{14}
\]

The first inequality is meant for successive boundaries; all actual
scalar values are still strictly greater than one half. In particular
both `q_j/h(q_j)` and `q_j/2^(h(q_j))` strictly increase at each of
these N returns.

### Construction with a controlled actual tail

Set `T=N+1`, and prescribe T complete R words. Put

\[
K=24T,\quad G=38T,\quad D=3^K=a^T,\quad s=K+6,
\quad C_T=c\frac{a^T-b^T}{a-b}.
\]

Here C_T is the full positive integral affine numerator of the entire
word. Choose the unique odd integer `0<t<2D` satisfying

\[
2^{G+s}t\equiv2^G+C_T\pmod D.
\tag{15}
\]

The power of two is invertible modulo D. The right side is nonzero
modulo three, since the last prescribed gap is four; hence its
residue is nonzero. Exactly one of the two representatives in `(0,2D)`
is odd. Define

\[
r=2^s t-1,\qquad
q=\frac{2^G r-C_T}{D}.
\tag{16}
\]

This is an odd integer by (15). It is positive: for any word of K
positive gaps, its complete affine constant satisfies
`C_T/2^G<2^K`, whereas `r>=2^(K+6)-1`. Moreover

\[
\boxed{q<2^{G+s+1}=2^{62T+7}.}
\tag{17}
\]

The complete composite equality in (16), together with odd r,
places q in the literal finite cylinder. One direct check is to
reduce that equality modulo `2^(A_i+1)` at each prefix clock A_i:
the prefix numerator has valuation exactly A_i. Thus every displayed
intermediate is an actual positive odd ordinary state with precisely
the prescribed next gap.

The endpoint r has `s-1` initial gaps equal to one, ending at
`v=2*3^(s-1)t-1`. Since `t<2*3^K`,

\[
v<2^{2(s+K)},\qquad
\frac12<h(r)
<\frac12+\frac{8K+27}{6\cdot3^{K+5}}<\frac58.
\tag{18}
\]

The first scalar bound follows from (1) and its exact finite-tail
identity. The final comparison is `32K+108<3^(K+6)`, which follows
by elementary induction from K=0. No convergence of r or q to one
has been assumed.

### True scalars and the exact end of the constant run

Every two-step L or P has scalar prefix contribution `7/9`. Therefore,
at the j-th complete R boundary, `0<=j<=T`,

\[
h(q_j)=\frac78+\frac{h(r)-7/8}{3^{24(T-j)}}.
\tag{19}
\]

For `j<T`, each boundary starts another literal R, so its shifted
valuation is exactly 34. The parent threshold and (9) give
`q_(j+1)>q_j`, while (18)--(19) give strictly decreasing true scalars.
Taking only the first N=T-1 returns leaves valuation 34 at both ends
of every comparison in (14).

Their actual scalar distance from the exceptional phase obeys

\[
\frac1{4\cdot3^{24(T-j)}}
<\frac78-h(q_j)
<\frac3{8\cdot3^{24(T-j)}}.
\tag{20}
\]

One may prescribe extra unused R words before the controlled tail
to make every considered boundary lie in any requested neighborhood
below `7/8`. This still changes the initial ordinary source.

Finally `v_2(r+7)=1`, so (10) gives `v_2(Z(r))=1`. Equation (13)
then gives `v_2(Z(q))=38T+1`. These sources realize exactly T
consecutive R words and no further one, agreeing with R10-T2.

## 6. What the tower does and does not refute

For any fixed real function f of the current shifted valuation, the
actual quantities

\[
\frac{q_j}{h(q_j)}+f(v_2(q_j+7)),\qquad
\frac{q_j}{2^{h(q_j)}}+f(v_2(q_j+7))
\]

increase at every one of the first N returns, because the added
correction is the same number f(34). The same conclusion holds for
a positive multiplicative correction depending only on that valuation.
Thus such corrections cannot provide a uniform decreasing rank for
all actual low-to-low returns near the exceptional phase.

The construction does **not** refute a theorem restricted to exact
`h=7/8`; its actual scalars are strictly below that value. It does
not address arbitrary nonmonotone functions of q or additional
global information. In particular the integer rank Z in Section 4
does detect and bound these finite repetitions.

The growth restrictions (5), (7), and (8) are compatible with these
finite constant-length towers. They forbid sufficiently fast sparse
return schedules, but do not by themselves eliminate every slowly
changing schedule. The precise remaining task is to control the
reset of a useful integer rank across arbitrary successive return
types at one fixed positive ordinary source.

## 7. Formal and computational boundary

`ReturnTower.lean` proves finite affine and product identities, the
discrete growth-budget induction, and the fixed-return center
transport. The actual infinite scalar, complete cylinder attachment,
and construction of the infinite family of finite towers remain
written mathematics. Their roles are kept separate from the exact
scope of the Lean declarations.

`tower_controls.py` retains every affine constant, replays the literal
ordinary gaps, checks the exact repetition rank and maximal run length,
and propagates unconditional rational enclosures for the actual scalar.
It also checks the growth-budget inequalities on finite towers. No
ordinary orbit is assumed to terminate in order to obtain (18)--(20),
and all checks stay active under `python -O`.

**First unsupported step:** a rank or return-selection argument that
cannot be reset indefinitely by changing low lengths and paid words.
No full Collatz theorem, universal denominator-eight recognizer, or
fixed positive infinite tower is claimed.
