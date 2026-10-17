# LIT-KTHM-0056 — Restricted rational-base charts are approximate-multiplication maps

**Status:** `KNOWN — EXACT SOURCE + EXACT NATIVE IDENTIFICATION`  
**Source:** Artūras Dubickas and Michael J. Mossinghoff, *Lower Bounds for Z-Numbers*, Mathematics of Computation 78 (2009), 1837–1851, DOI `10.1090/S0025-5718-09-02211-X`  
**Source inspection:** complete author-uploaded text, especially map (1.1), Proposition 3.1, and Proposition 3.2  
**Native interfaces:** PR #64 `D-7401/Q-7401`; PR #45/PR #50 physical six-branch chart  
**Counterexample status:** no Collatz counterexample is claimed

## Source map

Let `p>q>1` be coprime and let

\[
S\subsetneq\{0,1,\ldots,q-1\}
\]

be nonempty. Dubickas and Mossinghoff study the partial integer map

\[
G_S(x)=
\begin{cases}
\lceil px/q\rceil,&x\bmod q\in S,\\
\mathrm{STOP},&x\bmod q\notin S.
\end{cases}
\tag{1}
\]

They call this a problem of approximate multiplication.

Their Proposition 3.2 proves:

\[
\boxed{|S|=1\Longrightarrow G_S\text{ terminates on every positive start}.}
\tag{2}
\]

Their Proposition 3.1 proves that if `G_S` terminates on every positive start, then every sequence

\[
\{\lambda(p/q)^n\},\qquad\lambda>0,
\]

has an accumulation point at least

\[
\min\{|S|/p,1/q\}.
\]

In particular, if

\[
p<|S|q,
\]

then universal termination of `G_S` implies nonexistence of a `Z_(p/q)`-number.

## Exact native identification

For the six-branch chart put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\]

and

\[
F(x)=\left\lceil {Px\over Q}\right\rceil,
\qquad
\delta(x)=QF(x)-Px.
\]

The allowed digit set is

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

Since `P` is invertible modulo `Q`, digit restriction is equivalent to source-residue restriction. Define

\[
\mathcal S=\{-P^{-1}a\bmod Q:a\in\mathcal A\}.
\]

Using the exact native table,

\[
\boxed{
\mathcal S=
\{294912,331776,438784,297024,6472,466033\}.}
\]

Then

\[
\boxed{
\delta(x)\in\mathcal A
\iff
x\bmod Q\in\mathcal S.}
\]

Therefore the six-branch extraction problem is exactly the map `(1)` with

\[
(p,q,S)=(P,Q,\mathcal S).
\]

It is not merely analogous to the Dubickas–Mossinghoff problem.

## Consequences

### 1. The chart is one explicit instance of a long-standing general question

A positive all-time six-branch root is a nonterminating positive orbit of the approximate-multiplication map `(1)` for a six-element residue set.

A proof that every six-branch root terminates solves this one explicit instance of the general Dubickas–Mossinghoff termination question.

### 2. Singleton subcharts are already closed externally

Every one-symbol restriction of the six-branch chart terminates on every positive start by `(2)`. This agrees with, but does not replace, the stronger native exclusions of periodic and finite-state controllers.

The first genuinely open alphabet size in this general framework is at least two.

### 3. A `Z_(P/Q)`-number would force a six-branch survivor

Here

\[
P<6Q.
\]

By the contrapositive of Proposition 3.1,

\[
\boxed{
Z_{P/Q}\ne\varnothing
\Longrightarrow
\exists x>0\text{ whose }G_\mathcal S\text{-orbit never stops}.}
\]

Subject to the branch-qualified physical conjugacy, such a root would give a Collatz counterexample.

This is only a sufficient positive route. A six-branch survivor need not itself produce a `Z_(P/Q)`-number.

## Applicability audit

- `P,Q` are coprime and satisfy `2<=Q<P`.
- `S` is nonempty and proper, with cardinality six.
- The native digit map and source-residue map are related by multiplication by the unit `-P^{-1} mod Q`.
- Proposition 3.1 is used only in its exact logical direction and contrapositive.

## Gap audit

- The 2009 paper does not prove termination for `|S|=6`.
- The general termination question is still presented as difficult in the 2026 rational-base normality literature.
- A `Z_(P/Q)`-number is not known and is conjecturally absent.
- This connection does not decide the native least-root sequence.

## Suggested use

The six-branch project should be compared against the approximate-multiplication hierarchy by allowed-set size:

```text
|S|=1: externally proved terminating;
2<=|S|<=5: possible intermediate theorem targets;
|S|=6: exact physical Collatz chart;
all proper S: the broad Dubickas–Mossinghoff question.
```

Any subalphabet theorem should preserve the exact ordinary root and distinguish a true all-time survivor from a compatible rational-base completion.