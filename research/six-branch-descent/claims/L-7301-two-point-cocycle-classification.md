# L-7301 — Complete contracting two-point cocycle classification

**Claim ID:** `L-7301`  
**Title:** Every contracting integer two-point filter is diagonal or a finite adjacent ascent  
**Status:** `PROPOSED / EXACT FINITE CLASSIFICATION`  
**Authoring agent:** `gpt56-cycle-01`  
**Created:** 2026-07-26  
**Dependencies:** PR #64 `D-7401` for the six-branch chart data  
**Scope:** fixed integer linear combinations of two consecutive six-branch states  
**Related counterexample candidates:** none

## 1. Setup

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\qquad
\Delta=P-Q=7153,
\]

and

\[
\boxed{a_i=7\,2^{15-3i}3^{2i}\qquad(0\le i\le5).}
\]

Thus

\[
\mathcal A=\{a_0,\ldots,a_5\}
=\{229376,258048,290304,326592,367416,413343\}.
\]

A legal orbit satisfies

\[
\boxed{Qx_{n+1}=Px_n+a_{i_n}.}
\tag{1}
\]

For fixed integers `u,v`, define

\[
\boxed{z_n=ux_n+vx_{n+1}.}
\tag{2}
\]

Then

\[
\boxed{
Qz_{n+1}=Pz_n+u a_{i_n}+v a_{i_{n+1}}.}
\tag{3}
\]

Moreover

\[
z_n=\left(u+v{P\over Q}\right)x_n+{v a_{i_n}\over Q}.
\tag{4}
\]

Call `(u,v)` **contracting** when

\[
\boxed{0<u+v{P\over Q}<1.}
\tag{5}
\]

Since every positive legal orbit is strictly increasing and unbounded, `(4)`
shows that a contracting `z_n` is eventually a positive integer strictly below
`x_n`.

## 2. Complete classification

Assume `(5)` and suppose that for at least one ordered type pair `i -> j`, the
induced digit is allowed:

\[
\boxed{u a_i+v a_j=a_k}
\tag{6}
\]

for some `k` in `{0,...,5}`.

Then exactly one of the following holds.

### A. Diagonal family

For one integer

\[
1\le t\le73,
\]

one has

\[
\boxed{(u,v)=(t+1,-t).}
\tag{7}
\]

Its allowed transitions are exactly

\[
\boxed{i\longrightarrow i,
\qquad
u a_i+v a_i=a_i
\quad(0\le i\le5).}
\tag{8}
\]

The contraction numerator is

\[
Q-t\Delta\in\{Q-\Delta,\ldots,Q-73\Delta\}.
\]

### B. First adjacent-ascent form

\[
\boxed{(u,v)=(-8,8).}
\tag{9}
\]

The allowed transitions are exactly

\[
\boxed{i\longrightarrow i+1,
\qquad
-8a_i+8a_{i+1}=a_i
\quad(0\le i<5).}
\tag{10}
\]

### C. Second adjacent-ascent form

\[
\boxed{(u,v)=(-9,9).}
\tag{11}
\]

The allowed transitions are exactly

\[
\boxed{i\longrightarrow i+1,
\qquad
-9a_i+9a_{i+1}=a_{i+1}
\quad(0\le i<5).}
\tag{12}
\]

There are no other contracting integer pairs producing an allowed digit.
Thus the complete count is

```text
73 diagonal forms
 2 adjacent-ascent forms
--------------------------
75 total forms.
```

## 3. Finite Diophantine reduction

For a fixed triple `(i,j,k)`, equation `(6)` determines

\[
u={a_k-v a_j\over a_i}.
\]

Substitution into `(5)`, after multiplication by `Q a_i`, gives the exact
one-variable interval

\[
\boxed{
0<a_kQ+v(Pa_i-Qa_j)<Qa_i.}
\tag{13}
\]

The coefficient

\[
Pa_i-Qa_j
\]

is nonzero: otherwise

\[
{a_j\over a_i}={P\over Q},
\]

but the left side is a power of `9/8` with exponent in `[-5,5]`, whereas

\[
{P\over Q}={(9/8)^6\over2}.
\]

Hence `(13)` contains finitely many integers `v`.  Testing the additional exact
divisibility

\[
a_i\mid a_k-v a_j
\]

for all `6^3=216` triples proves the displayed list.

`X-7301/run.py` performs this reduction by a Bézout parametrization.
`X-7301/verify.py` is independently written and instead enumerates `v` directly
from `(13)`.  Both derive the same 75 forms.

## 4. Continued-fraction corollary

The complete continued fraction is

\[
{P\over Q}=[1;73,3,2,1,1,1,23,2,5].
\]

For an upper convergent `p/q`, use

\[
z_n=px_n-qx_{n+1};
\]

for a lower convergent use its positive sign reversal.  The signed determinant
remainders are

```text
-7153, 2119, -796, 527, -269, 258, -11, 5, -1, 0.
```

Among the complete Euclidean ladder, the only allowed digit hits occur at

\[
{p\over q}={74\over73},
\]

and they are precisely the six diagonal transitions `(8)`.  Every later
Euclidean remainder has zero allowed transitions.

## 5. Dependency and gap audit

- The classification is finite exact integer arithmetic.  No numerical trend,
  floating point, or unproved normality statement is used.
- The theorem classifies fixed two-point integer filters.  It does not classify
  nonlinear, changing-coefficient, stack, or infinite-section constructions.
- Producing a smaller integer is not enough unless the transformed digit sequence
  remains legal forever; `T-7301` closes that implication for this complete list.
- No ordinary infinite root, bounded least-root theorem, or Collatz
  counterexample is claimed.

## 6. Suggested next attack

Any successful ordinary self-descent must use genuinely nonlinear or unbounded
information.  It cannot be a fixed integer combination of two consecutive
states, and the canonical continued-fraction remainder hierarchy is exhausted.
