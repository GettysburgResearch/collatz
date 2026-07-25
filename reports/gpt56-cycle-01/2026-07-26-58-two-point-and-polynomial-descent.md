# Six-branch global offense — exact contraction classification and polynomial-nucleus closure

**Agent:** `gpt56-cycle-01`  
**Issue:** `#58`  
**Date:** 2026-07-26  
**Branch:** `agent/gpt56-cycle-01/58-increment-descent-offense`  
**Base:** draft PR #64 at branch creation  
**Status:** no boundedness proof, ordinary infinite root, or Collatz counterexample

## 1. Objective

The only positive target was the boundedness of the nested least roots for

\[
Qx_{n+1}=Px_n+a_{i_n},
\]

with

```text
P=531441,
Q=524288,
a_i=7*2^(15-3i)*3^(2i).
```

A bounded sequence would stabilize at an explicit integer `m`; the exact
physical seed would be `6*m-5`.  No finite prefix, inverse-limit completion, or
conditional growth theorem was accepted as a substitute.

## 2. Initial descent coordinates

The first ordinary contraction is the increment

\[
y_n=x_{n+1}-x_n,
\]

which satisfies

\[
Qy_{n+1}=Py_n+a_{i_{n+1}}-a_{i_n}.
\]

Its 36 possible digits avoid the six-letter alphabet.  The first Euclidean
upper-convergent remainder is

\[
z_n=74x_n-73x_{n+1},
\]

with

\[
Qz_{n+1}=Pz_n+74a_{i_n}-73a_{i_{n+1}}.
\]

Its allowed outputs occur exactly on the diagonal `i_n=i_(n+1)`.

The complete continued fraction

\[
{P\over Q}=[1;73,3,2,1,1,1,23,2,5]
\]

has determinant remainders

```text
-7153, 2119, -796, 527, -269, 258, -11, 5, -1, 0.
```

Every later Euclidean remainder has zero allowed output digits.

## 3. Breakthrough — all two-point contractions, not only Euclidean ones

For arbitrary fixed integers `u,v`, put

\[
z_n=ux_n+vx_{n+1}.
\]

The exact cocycle is

\[
Qz_{n+1}=Pz_n+u a_{i_n}+v a_{i_{n+1}}.
\]

The contraction condition is

\[
0<u+vP/Q<1.
\]

For a fixed type triple `(i,j,k)`, the allowed-digit equation and contraction
condition reduce to

\[
0<a_kQ+v(Pa_i-Qa_j)<Qa_i,
\qquad
a_i\mid a_k-v a_j.
\]

This is a finite exact interval because `Pa_i-Qa_j` is nonzero.  Exhausting all
216 triples gives exactly 75 integer pairs.

### Complete answer

```text
73 forms:
    (u,v)=(t+1,-t), 1<=t<=73;
    legal edges only i->i, output i.

1 form:
    (u,v)=(-8,8);
    legal edges only i->i+1, output i.

1 form:
    (u,v)=(-9,9);
    legal edges only i->i+1, output i+1.

all other forms:
    none.
```

Thus every recurrent edge graph in the complete contraction classification is
constant-type.  Constant type is impossible for a positive ordinary tail:
with

\[
Y_n=(P-Q)x_n+a_i,
\]

one has `QY_(n+1)=P Y_n`, so every power of `Q` divides one fixed positive
integer.  The two non-diagonal forms require an infinite strict ascent inside
`{0,...,5}`, also impossible.

This closes **every fixed integer two-point linear descent on one hypothetical
orbit**, not merely the natural increment and continued-fraction choices.

## 4. Full-language generalization

For a fixed affine sliding filter

\[
Y_n=s+\sum_{r=0}^{d}b_r x_{n+r},
\]

the induced digit set is

\[
(Q-P)s+b_0\mathcal A+\cdots+b_d\mathcal A.
\]

The integer sumset inequality

\[
|X+Y|\ge|X|+|Y|-1
\]

shows that two nonzero coefficients would already produce at least eleven
digits.  A one-coefficient affine image of the six-element alphabet is forced
to be the identity.  Hence every fixed finite-order affine filter carrying the
complete language is only a time shift.

## 5. Polynomial-nucleus generalization

Allow a finite control graph and an arbitrary integer polynomial in the exact
high quotient at every section.  On an edge

\[
Qk'=Pk+c_i-r_j,
\]

the self-replication identity forces leading coefficients to satisfy

\[
L'=L(Q/P)^{d-1}.
\]

A finite control cycle therefore forces polynomial degree `d=1`.  Positive
constant sections are impossible because every edge strictly increases them.
The remaining degree-one system is exactly PR #64 `T-7402`, which collapses to

\[
f(k)=Pk+c_i.
\]

Thus no finite-control polynomial full-subtree nucleus can supply a nonlinear
ordinary self-descent.

## 6. Geometric vertical conjugacy

The alphabet itself is one geometric orbit:

\[
a_{i+1}=(9/8)a_i.
\]

Scaling an ordinary root by `(9/8)^c`, when the required divisibility and type
bounds hold, shifts every type by `c`.  The phase-free valuation identity makes
this scaling ordinary on actual type-confined tails.

A direct minimality consequence is:

\[
\boxed{\text{the least positive all-time root, if it exists, uses type 0.}}
\]

If every type were at least one, `9|x_1` and `8x_1/9` would be a smaller
positive all-time root with all types shifted down one.

## 7. Verification

`X-7301` contains independent exact implementations:

- author path: Bézout parametrization of each digit equation;
- verifier path: eliminate `u`, enumerate `v` from the direct contraction
  interval, then reconstruct `u` by divisibility.

Local standard-library replay passed:

```text
independent X-7301 classification checks passed
```

Frozen semantic digest:

```text
2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f
```

No finite least-root census is used in any theorem.

## 8. Honest global status

The boundedness of `m_n` remains open.  The new result is a method-class
breakthrough rather than an extracted root:

```text
direct quotient:                    closed;
finite affine quotient nucleus:     closed by PR #64;
all fixed two-point contractions:   closed here;
all finite-order affine filters:    closed here;
finite polynomial full subtree:     closed here;
nonlinear unbounded ordinary state: still open.
```

A positive solution must now cross the type-zero boundary and use genuinely
nonlinear or unbounded arithmetic information generated from one finite root.
A negative solution may leverage these closures to prove that every remaining
section has escaping canonical representatives.
