# L-6803 — Canonical start–end rectangle for every parity word

**Claim ID:** `L-6803`  
**Title:** Every finite shortcut-parity word has one canonical source–endpoint pair, and all ordinary realizations lie on one affine ray  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine composition  
**Scope:** finite parity words; no Collatz conclusion

## 1. Setup

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

For a binary word

\[
w=(v_0,\ldots,v_{j-1})\in\{0,1\}^j,
\qquad
q=\sum_{i=0}^{j-1}v_i,
\]

write its exact affine map as

\[
\boxed{
T_w(x)=\frac{3^q x+A_w}{2^j}}
\tag{1}
\]

with `A_w` the usual nonnegative integer affine numerator. Put

\[
P=2^j,
\qquad
Q=3^q.
\tag{2}
\]

## 2. Canonical rectangle theorem

There is a unique pair of integers

\[
\boxed{
1\le r_w\le P,
\qquad
1\le s_w\le Q}
\tag{3}
\]

such that

\[
\boxed{P s_w=Q r_w+A_w.}
\tag{4}
\]

Equivalently,

\[
r_w\equiv-Q^{-1}A_w\pmod P,
\tag{5}
\]

where residue zero is represented by `P`, and

\[
s_w=T_w(r_w).
\tag{6}
\]

The pair `(r_w,s_w)` will be called the **canonical start–end pair** of `w`.

### Proof by exact one-bit lifting

Use the empty word as the base case:

\[
P=Q=1,
\qquad
A=0,
\qquad
(r,s)=(1,1).
\]

Assume `(r,s)` is the canonical pair for a word with scales `(P,Q)`, and append a bit `b\in\{0,1\}`. Since `Q` is odd, there is a unique

\[
\varepsilon\in\{0,1\}
\]

such that

\[
z:=s+\varepsilon Q\equiv b\pmod2.
\tag{7}
\]

Define

\[
r'=r+\varepsilon P,
\tag{8}
\]

and

\[
s'=\frac{3^b z+b}{2}.
\tag{9}
\]

The new scales and affine numerator are

\[
P'=2P,
\qquad
Q'=3^bQ,
\qquad
A'=3^bA+bP.
\tag{10}
\]

Using `Ps=Qr+A`,

\[
\begin{aligned}
Q'r'+A'
&=3^bQ(r+\varepsilon P)+3^bA+bP\\
&=P\bigl(3^b(s+\varepsilon Q)+b\bigr)\\
&=2P s'\\
&=P's'.
\end{aligned}
\tag{11}
\]

Also `1\le r'\le2P`. If `b=0`, then `z` is even and lies in `[2,2Q]`, so

\[
1\le s'=z/2\le Q=Q'.
\]

If `b=1`, then `z` is odd and lies in `[1,2Q-1]`, so

\[
1\le s'=(3z+1)/2\le3Q-1<Q'.
\]

Thus `(r',s')` lies in the new rectangle. Uniqueness follows from the unique residue modulo `P'`, or inductively from the unique choice in `(7)`. This proves `(3)`–`(4)`. ∎

## 3. Complete ordinary ray

Every positive integer whose first `j` parity bits equal `w` is uniquely of the form

\[
\boxed{x=r_w+tP,\qquad t\in\mathbf Z_{\ge0}.}
\tag{12}
\]

Its endpoint is

\[
\boxed{T_w(x)=s_w+tQ.}
\tag{13}
\]

Indeed, substituting `(12)` into `(1)` and using `(4)` gives `(13)`. Conversely, the standard parity-cylinder bijection says that the source condition is exactly one residue modulo `P`.

Consequently the endpoint displacement on the whole cylinder is

\[
\boxed{
T_w(x)-x
=(s_w-r_w)+t(Q-P).}
\tag{14}
\]

This formula retains simultaneously:

- the exact parity cylinder;
- its least positive ordinary source;
- the exact endpoint;
- the coefficient drift `Q-P`;
- the complete dependence on the ordinary lift `t`.

## 4. The residue–remainder identity

Put

\[
\Delta_w=s_w-r_w.
\tag{15}
\]

Equation `(4)` gives

\[
\boxed{
A_w=(P-Q)r_w+P\Delta_w.}
\tag{16}
\]

When `P>Q`, let `D_w=P-Q`. Then

\[
\boxed{
\frac{A_w}{D_w}
=r_w+\frac{P}{D_w}\Delta_w.}
\tag{17}
\]

Therefore

\[
\boxed{
r_w>\frac{A_w}{P-Q}
\iff
\Delta_w<0
\iff
s_w<r_w.}
\tag{18}
\]

Similarly, equality in the proposed residue–remainder inequality is exactly

\[
\Delta_w=0,
\qquad
T_w(r_w)=r_w.
\tag{19}
\]

Thus the joint quantity proposed in `Q-6801`,

\[
\log r_w-
\log\!\left(\frac{A_w}{P-Q}\right),
\]

has positive sign exactly when the canonical endpoint lies below the canonical source. The two quantities are not independent; their difference is the one integer displacement `\Delta_w`.

## 5. Exact first-crossing interpretation

Suppose `w` is coefficient-first-crossing:

\[
3^{q_m}\ge2^m\quad(1\le m<j),
\qquad
Q=3^q<P=2^j.
\tag{20}
\]

Then `(14)` becomes

\[
T_w(r_w+tP)-(r_w+tP)
=\Delta_w-t(P-Q).
\tag{21}
\]

Hence:

```text
Delta_w < 0:
    every positive member of the parity cylinder descends at time j;

Delta_w = 0:
    the canonical source is a positive periodic point of w;

Delta_w > 0:
    the canonical source is paradoxical at its coefficient stopping time,
    and only finitely many higher lifts can remain paradoxical.
```

More precisely, the non-descending lifts are exactly those integers `t>=0` satisfying

\[
t\le\frac{\Delta_w}{P-Q}.
\tag{22}
\]

## 6. Trivial boundary

For the first-crossing word

```text
w = 10
```

one has

\[
P=4,
\qquad
Q=3,
\qquad
A_w=1,
\qquad
(r_w,s_w)=(1,1).
\]

Thus

\[
r_w=rac{A_w}{P-Q}=1.
\]

The strict inequality in the literal all-word formulation of Box 2 therefore has this unavoidable trivial exception. The corrected CST target is:

\[
\boxed{
\Delta_w<0
\text{ for every coefficient-first-crossing word with }r_w\ge2.}
\tag{23}
\]

## 7. Gap audit

- `(23)` is not proved here.
- `(23)` is precisely the smallest-member form of Terras's coefficient-stopping-time conjecture, not a routine consequence of the affine formula.
- Equality for a word other than the trivial `10` would give a nontrivial positive periodic orbit.
- Positive `\Delta_w` is the genuinely paradoxical first-crossing obstruction.
- The theorem does not use finite computation and makes no density or genericity inference.

## 8. Handoff

The correct finite-crossing target is the sign problem

\[
\boxed{s_w-r_w<0.}
\]

Future work should attack this integer displacement directly under the full least-counterexample constraints, rather than separately estimating two algebraically dependent quantities `r_w` and `A_w/(P-Q)`.