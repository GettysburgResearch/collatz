# L-9864 — Exact four-step Padé block isolates the missing endpoint invariant

Claim ID: `L-9864`  
Title: Four q-Pascal steps give a filtered twisted-pair operator with exact branch gains  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`  
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-h`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9848`, `L-9856`, `L-9859`, `L-9861`, `L-9862`  
Scope: exact characteristic-two block algebra for the normalized Padé residual family; no new layer order is asserted

## Definitions

Put `Q=1+X` and let

\[
C=Q^c,
\qquad c\in\mathbf Z_2.
\tag{1}
\]

Work either in `F_2[[X]]` or in any truncation of it.  Retain the normalized
size summands

\[
\mathscr S_{n,v}
=C^vQ^{-3\binom v2}{n\brack v}_Q
\tag{2}
\]

and package them in the size-marked polynomial

\[
P_n(Y)=\sum_{v=0}^{n}\mathscr S_{n,v}Y^v.
\tag{3}
\]

Thus

\[
F_{n,c}(Q)=P_n(1).
\tag{4}
\]

For a twist index `j`, define the parity pair

\[
\mathbf E_{n,j}
=\sum_{v\text{ even}}Q^{-4jv}\mathscr S_{n,v},
\qquad
\mathbf O_{n,j}
=\sum_{v\text{ odd}}Q^{-4jv}\mathscr S_{n,v},
\tag{5}
\]

and write

\[
\mathbf V_{n,j}
=\begin{pmatrix}\mathbf E_{n,j}\\ \mathbf O_{n,j}\end{pmatrix},
\qquad
\Sigma=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{6}
\]

If a finite twist modulus `M` is used, assume `Q^(-4M)=1` at the chosen
truncation height, as in `L-9862`.  Then all twist subscripts below may be
read modulo `M`.

## Statement

### 1. Exact four-step size-marked block

The one-step q-Pascal operator is

\[
\boxed{
P_{n+1}(Y)
=P_n(Y)+CQ^nY P_n(Q^{-4}Y).
}
\tag{7}
\]

Four consecutive steps collapse to the exact five-branch identity

\[
\boxed{
P_{n+4}(Y)
=\sum_{k=0}^{4}
C^kQ^{nk-3\binom k2}{4\brack k}_Q
Y^kP_n(Q^{-4k}Y).
}
\tag{8}
\]

This identity holds in the polynomial ring over `F_2[[X]]`; it is not an
asymptotic expansion.

### 2. Exact Boolean Gaussian factors

At `Q=1+X`, the five Gaussian coefficients in (8) are

\[
\boxed{
{4\brack0}_Q={4\brack4}_Q=1,
\qquad
{4\brack1}_Q={4\brack3}_Q=X^3,
\qquad
{4\brack2}_Q=X^2(1+X+X^2).
}
\tag{9}
\]

Consequently (8) is equivalently

\[
\boxed{
\begin{aligned}
P_{n+4}(Y)
={}&P_n(Y)\\
&+X^3CQ^nY P_n(Q^{-4}Y)\\
&+X^2(1+X+X^2)C^2Q^{2n-3}Y^2P_n(Q^{-8}Y)\\
&+X^3C^3Q^{3n-9}Y^3P_n(Q^{-12}Y)\\
&+C^4Q^{4n-18}Y^4P_n(Q^{-16}Y).
\end{aligned}
}
\tag{10}
\]

The exact branch filtration gains, before any cancellation among outputs,
are therefore

\[
\boxed{(0,3,2,3,0)\quad\text{for }k=0,1,2,3,4.}
\tag{11}
\]

### 3. Exact four-step twisted-pair transition

For `0<=k<=4`, put

\[
b_{n,j,k}
=C^kQ^{nk-3\binom k2-4jk}{4\brack k}_Q.
\tag{12}
\]

Then the twisted parity pairs satisfy

\[
\boxed{
\mathbf V_{n+4,j}
=\sum_{\substack{0\le k\le4\\k\text{ even}}}
b_{n,j,k}\mathbf V_{n,j+k}
+\sum_{\substack{0\le k\le4\\k\text{ odd}}}
b_{n,j,k}\Sigma\mathbf V_{n,j+k}.
}
\tag{13}
\]

Thus even `k` preserves size parity and odd `k` swaps it.  More explicitly,

\[
\boxed{
\begin{aligned}
\mathbf V_{n+4,j}
={}&\mathbf V_{n,j}
+X^3CQ^{n-4j}\Sigma\mathbf V_{n,j+1}\\
&+X^2(1+X+X^2)C^2Q^{2n-3-8j}\mathbf V_{n,j+2}\\
&+X^3C^3Q^{3n-9-12j}\Sigma\mathbf V_{n,j+3}\\
&+C^4Q^{4n-18-16j}\mathbf V_{n,j+4}.
\end{aligned}
}
\tag{14}
\]

### 4. Forced filtration and the exact endpoint problem

Let

\[
d_{n,j}=C^4Q^{4n-18-16j}
=Q^{4c+4n-18-16j}.
\tag{15}
\]

Its deviation from `1` has exact augmentation order two:

\[
\boxed{\operatorname{ord}_X(d_{n,j}+1)=2.}
\tag{16}
\]

Equation (14) therefore implies the exact filtered decomposition

\[
\boxed{
\mathbf V_{n+4,j}
-\mathbf V_{n,j}-d_{n,j}\mathbf V_{n,j+4}
\in X^2\bigl(\mathbf F_2[[X]]\bigr)^2,
}
\tag{17}
\]

and the parity-swapping part of the remainder lies in `X^3`.  In particular,

\[
\boxed{
\mathbf V_{n+4,j}
\equiv\mathbf V_{n,j}+\mathbf V_{n,j+4}
\pmod {X^2}.
}
\tag{18}
\]

The gain `2` in (17) is sharp at the operator level because the normalized
`k=2` coefficient has constant term `1`.

At the untwisted residual readout, the same block gives the independent
absolute congruence

\[
\boxed{
F_{n+4,c}(Q)-F_{4,c+n}(Q)F_{n,c}(Q)
\in X^8\mathbf F_2[[X]].
}
\tag{19}
\]

The exponent eight is sharp uniformly in the phase: at `n=1`,

\[
\boxed{
F_{5,c}(Q)-F_{4,c+1}(Q)F_{1,c}(Q)
\equiv X^8\pmod {X^9}
\qquad(c\in\mathbf Z_2).
}
\tag{19a}
\]

Since `L-9848/(23)` gives

\[
F_{4,d}(Q)\equiv QX^6\pmod {X^8}
\qquad(d\in\mathbf Z_2),
\tag{20}
\]

one also has

\[
\boxed{
F_{n+4,c}(Q)\equiv QX^6F_{n,c}(Q)\pmod {X^8}.
}
\tag{21}
\]

For `n>=1`, one has `F_(n,c) in X F_2[[X]]`, so this simplifies further to

\[
\boxed{
n\ge1
\quad\Longrightarrow\quad
F_{n+4,c}(Q)\equiv X^6F_{n,c}(Q)\pmod {X^8}.
}
\tag{21a}
\]

These statements identify the exact bridge needed for an induction: after
normalization, one must control cancellation between the endpoint states
`V_(n,j)` and `V_(n,j+4)`.  Equations (17)--(21) do **not** supply that
endpoint invariant.

## Proof

### From q-Pascal to the four-step operator

The summand transition `L-9856/(7a)` is

\[
\mathscr S_{n+1,v}
=\mathscr S_{n,v}+CQ^{n+4-4v}\mathscr S_{n,v-1}.
\tag{22}
\]

Multiply by `Y^v`, sum over `v`, and put `u=v-1` in the second sum.  Its
coefficient becomes

\[
CQ^{n+4-4(u+1)}Y^{u+1}
=CQ^nY(Q^{-4}Y)^u,
\tag{23}
\]

which proves (7).

To collect four steps without hidden cancellations, use the subset form of
`L-9848/(6)`.  Split a subset of `{0,...,n+3}` into an old subset of
`{0,...,n-1}` of size `u` and a new subset of `{n,n+1,n+2,n+3}` of size
`k`.  Relative to the old exponent, a fixed new subset `J` contributes

\[
ck+\sum_{i\in J}i-4\binom k2-4uk.
\tag{24}
\]

Writing `J=n+J_0`, the Gaussian subset identity gives

\[
\sum_{\substack{J_0\subseteq\{0,1,2,3\}\\|J_0|=k}}
Q^{\sum_{i\in J_0}i}
=Q^{\binom k2}{4\brack k}_Q.
\tag{25}
\]

After summing the new subsets, (24)--(25) contribute

\[
C^kQ^{nk-3\binom k2}{4\brack k}_Q
\tag{26}
\]

and replace `Y^u` by `Y^k(Q^(-4k)Y)^u`.  Summing over the old subsets proves
(8).  This is the grouped algebra of four iterations of (7), so the
q-Pascal and group-ring derivations agree term by term.

### Gaussian factorization and parity action

The outer Gaussian coefficients are

\[
{4\brack1}_Q={4\brack3}_Q=1+Q+Q^2+Q^3
=(1+Q)(1+Q^2),
\tag{27}
\]

and

\[
{4\brack2}_Q=1+Q+2Q^2+Q^3+Q^4.
\tag{28}
\]

In characteristic two,

\[
1+Q=X,
\qquad
1+Q^2=X^2,
\tag{29}
\]

so (27) is `X^3`.  Reducing (28) modulo two and substituting `Q=1+X`
gives

\[
1+Q+Q^3+Q^4=X^2+X^3+X^4
=X^2(1+X+X^2).
\tag{30}
\]

This proves (9)--(11).

In the `k` branch of (8), evaluate the size marker at `Y=Q^(-4j)`.  The
factor `Y^k` contributes `Q^(-4jk)`, while the old polynomial is evaluated
at `Q^(-4(j+k))`.  Adding `k` new elements preserves old parity for even
`k` and reverses it for odd `k`.  These observations give (12)--(13), and
substitution of (9) gives (14).

### Filtration and scalar residual congruence

The exponent in (15) is

\[
4c+4n-18-16j
=2\bigl(2c+2n-9-8j\bigr),
\tag{31}
\]

and the factor in parentheses is an odd 2-adic integer.  Hence

\[
d_{n,j}=(1+X^2)^{2c+2n-9-8j}
=1+X^2+O(X^4),
\tag{32}
\]

which proves (16).  Equations (9) and (14) now prove (17); reducing the two
endpoint coefficients modulo `X^2` proves (18).  The unit
`1+X+X^2` shows that the `k=2` branch has exact operator order two.

It remains to prove (19).  Put `Y=1` in (8) and write

\[
a_{n,k}=C^kQ^{nk-3\binom k2}{4\brack k}_Q.
\tag{33}
\]

Since

\[
\sum_{k=0}^{4}a_{n,k}=F_{4,c+n}(Q),
\tag{34}
\]

subtracting `F_(4,c+n)F_(n,c)` from (8) gives

\[
\sum_{k=1}^{4}a_{n,k}
\bigl(P_n(Q^{-4k})-P_n(1)\bigr).
\tag{35}
\]

For every polynomial `P`, the difference `P(Z)-P(1)` is divisible by
`Z-1`.  Here

\[
\operatorname{ord}_X(Q^{-4k}-1)
=(4,8,4,16)
\quad\text{for }k=1,2,3,4,
\tag{36}
\]

while (11) gives

\[
\operatorname{ord}_X(a_{n,k})=(3,2,3,0).
\tag{37}
\]

Taken separately, the four summands in (35) have orders at least

\[
(7,10,7,16).
\tag{38}
\]

The two possible degree-`7` terms cancel.  Indeed, put

\[
D_n(Z)=\frac{P_n(Z)-P_n(1)}{Z-1}.
\tag{39}
\]

For `k=1,3`, one has

\[
\frac{a_{n,k}}{X^3}\equiv1\pmod X,
\qquad
\frac{Q^{-4k}-1}{X^4}\equiv1\pmod X,
\qquad
D_n(Q^{-4k})\equiv D_n(1)\pmod X.
\tag{40}
\]

After division by `X^7`, the `k=1` and `k=3` summands in (35) therefore
both reduce to `D_n(1)` modulo `X`; their sum is zero in characteristic two.
The other two summands already lie in `X^10` and `X^16`.  This proves the
stronger error bound (19).

For sharpness, set `n=1`.  Then `P_1(Y)=1+CY`, so `D_1(Z)=C`.  After the
common factor `X^3` is removed, the sum of the `k=1,3` terms in (35) is

\[
\begin{aligned}
&Q^{2c+1}(Q^{-4}+1)+Q^{4c-6}(Q^{-12}+1)\\
&\qquad
=X^4\left(
Q^{2c-3}+Q^{4c-18}(1+X^4+X^8)
\right).
\end{aligned}
\tag{40a}
\]

The bracket has zero constant term, while its coefficient of `X` is
`(2c-3)+(4c-18)=1` in `F_2`.  The other branches start above degree eight,
so (40a) proves (19a).

Equation (20) now proves (21).  If `n>=1`, evaluation at `X=0` gives

\[
F_{n,c}(1)=\sum_{v=0}^{n}\binom nv=2^n=0
\quad\text{in }\mathbf F_2,
\tag{41}
\]

so `F_(n,c)` is divisible by `X`; replacing `QX^6` by `X^6` changes the
product only in `X^8`.  This proves (21a).  The sharp example (19a) shows
that no congruence modulo `X^9` is licensed without additional control of
the shifted old states.  This completes the proof. ∎

## Motivation

Claims through `L-9862` prove eight consecutive period-four layers, but by
finite state certificates.  The exact four-step operator is the natural
map from one actual layer to the next.  Its filtration pattern is far more
rigid than a generic five-branch sum: only the two endpoints occur at order
zero, the middle branch starts at order two, and parity swapping starts at
order three.

This localizes the missing induction mechanism.  A normalized relation
between twists `j` and `j+4` could make the endpoint terms cancel to the
forced baseline increment, after which the already-filtered interior terms
could be controlled.  The present claim proves the operator structure but
does not assume such a relation.

## Dependency audit

- `L-9848` supplies the characteristic-two subset form and the exact base
  identity for `F_(4,d)`.
- `L-9856` supplies the one-step q-Pascal summand transition.
- `L-9859` supplies the criterion under which finite twist indices may be
  read cyclically.
- `L-9861` and `L-9862` supply the twisted parity state and its general
  finite realization.
- The four-step block, Gaussian factorizations, twisted-pair matrix,
  filtration gains, and order-eight scalar congruence are proved here.
- No finite-layer table, numerical root approximation, or phase
  specialization is used.

## Gap audit

- The endpoint congruence (18) is not an endpoint cancellation theorem.
  The relation between `V_(n,j)` and `V_(n,j+4)` after forced-factor
  normalization remains unknown.
- Congruences (21)--(21a) are absolute only through degree `7`; their error
  begins at degree `8` independently of `ord_X(F_n)`.  They cannot propagate
  the large known orders by themselves.
- No uniform slack formula, future layer order, or target nonvanishing is
  inferred from this block operator.
- The all-layer identity
  `lambda_(4t)=4t+2*sum_(m<=t)2^(nu_2(m))` remains conjectural.
- Odd-macro numerator and phase jets remain outside the claim.

## Adversarial tests

- The endpoint `k=4` coefficient is not `1`; it differs from `1` first in
  degree `2`.  Dropping this deviation loses a term at the same filtration
  as the middle branch.
- The `k=2` branch preserves parity.  Treating every non-endpoint branch as
  a swap gives the wrong block matrix.
- The shifts `P_n(Q^(-4k)Y)` are essential.  Replacing them all by `P_n(Y)`
  turns the absolute congruence (19) into a false exact product identity.
- Estimating the `k=1,3` errors separately gives only order `7`; their equal
  leading divided differences must be paired to obtain the correct
  order-`8` bound.
- Finite twist subscripts can be reduced modulo `M` only after checking
  `Q^(-4M)=1` at the working height.

## Remaining uncertainty

Does forced-factor normalization put the endpoint pair
`V_(4t,j)+d_(4t,j)V_(4t,j+4)` on a one-dimensional unit line, or is an
additional endpoint jet required?  This is now the precise obstruction to
turning the exact block into an order induction.

## Suggested next attack

Divide each actual-layer state by its proved baseline `X^(B_(4t))` and apply
(14) modulo the next predicted slack window.  Track the endpoint sum and its
first `X^2` correction as separate coordinates.  If those two coordinates
close under the four-step block, the binary order recurrence of
`L-9848/(16)` may follow without further layer-by-layer Boolean tables.
