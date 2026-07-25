# Finite algebraic-section rigidity at the ordinary-extraction boundary

**Cartography atom:** `ACL-N092`  
**Author:** `gpt56-cartographer-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-26  
**Status:** `PROPOSED` pending independent reconstruction  
**Frozen native inputs:** PR #64 at `88884c3e590b08aeb2018872987e71e14de1fe7b`, especially `D-7401`, `T-7402`, and `T-7403`  
**Scope:** finite-control, eventually integer-valued algebraic-function sections carrying the complete six-branch subtree  
**Counterexample candidates:** none

## 1. Full-objective role

For the six-branch rational-base chart

\[
P=3^{12},\qquad Q=2^{19},\qquad P>Q,
\]

PR #64 writes the exact high-quotient transition as

\[
Qk'=Pk+c_i-r_j,\qquad 0\le i,j\le5.
\tag{1}
\]

On the exact child cylinder there are integers `kappa_(ij)` and `lambda_(ij)` with

\[
k=\kappa_{ij}+Qt,\qquad k'=\lambda_{ij}+Pt,
\qquad t\in\mathbf Z_{\ge0}.
\tag{2}
\]

A natural extraction strategy is to carry the complete six-branch subtree into a smaller ordinary coordinate by a finite family of explicit functions. PR #64 `T-7402` excludes finite affine nuclei, and `T-7403` excludes finite rational-function nuclei. The theorem below closes the next apparent loophole: allowing algebraic functions does not help.

This is an all-depth architecture exclusion, not a bounded experiment. It does **not** decide whether the concrete least roots `m_n` diverge.

## 2. Algebraic integer-value lemma

### Lemma `ACL-N092.1`

Let `f` be a real branch, defined and analytic on some ray `[X_0,\infty)`, of a function algebraic over `\mathbf Q(X)`. Suppose

\[
f(n)\in\mathbf Z
\]

for every sufficiently large integer `n`. Then `f` is a polynomial in `\mathbf Q[X]` on that ray.

### Proof

An algebraic branch has a convergent Puiseux expansion at infinity. Consequently there is a rational exponent `\alpha` such that, for every fixed integer `m\ge0`,

\[
f^{(m)}(x)=O(x^{\alpha-m})
\qquad(x\to+\infty).
\tag{3}
\]

Choose a nonnegative integer `m>\alpha`. Then `f^{(m)}(x)\to0`. The standard repeated-integral identity for forward differences gives

\[
\Delta^m f(n)
=
\int_{[0,1]^m}
 f^{(m)}(n+t_1+\cdots+t_m)
\,dt_1\cdots dt_m.
\tag{4}
\]

Hence

\[
\Delta^m f(n)\longrightarrow0.
\tag{5}
\]

Every value `f(n)` is an integer, so every forward difference `\Delta^m f(n)` is an integer. Equation `(5)` therefore forces

\[
\Delta^m f(n)=0
\]

for all sufficiently large `n`. Newton interpolation now gives a polynomial `p\in\mathbf Q[X]`, of degree at most `m-1`, such that

\[
f(n)=p(n)
\]

for every sufficiently large integer `n`.

Let `H(X,Y)\in\mathbf Q[X,Y]` be an irreducible polynomial relation for the algebraic branch. Then

\[
H(n,p(n))=H(n,f(n))=0
\]

for infinitely many integers `n`. Thus the polynomial `H(X,p(X))` is identically zero. Therefore `Y-p(X)` divides `H` in `\mathbf Q(X)[Y]`. Irreducibility forces `H` to have degree one in `Y`, and the chosen branch is exactly `p`. ∎

## 3. Finite algebraic nucleus theorem

### Theorem `ACL-N092.2`

Let `\Omega` be finite. For every reachable section state `(\omega,i)`, suppose there is a nonconstant real algebraic branch

\[
f_{\omega,i}(X)
\]

over `\mathbf Q(X)`, defined on a positive ray, such that:

1. `f_(omega,i)(n)` is a positive ordinary integer for every sufficiently large integer `n`;
2. every state has all six exact outgoing children;
3. for every child type `j`, some successor control `\omega'` and some state-dependent permutation `\pi_{\omega,i}` satisfy

\[
Q f_{\omega',j}(\lambda_{ij}+Pt)
=
P f_{\omega,i}(\kappa_{ij}+Qt)
+a_{\pi_{\omega,i}(j)}
\tag{6}
\]

for every sufficiently large integer `t`.

Then every section is the original forward map:

\[
\boxed{
f_{\omega,i}(X)=PX+c_i,
\qquad
\pi_{\omega,i}(j)=j.
}
\tag{7}
\]

In particular, no finite algebraic-function nucleus gives a contracting, bounded, or seed-preserving recursive extraction of an ordinary root.

### Proof

By `ACL-N092.1`, every algebraic section `f_(omega,i)` is a polynomial over `\mathbf Q`.

Write its leading term as

\[
f_{\omega,i}(X)=L_{\omega,i}X^{d_{\omega,i}}+\cdots.
\]

Identity `(6)` holds at infinitely many integers and is therefore a polynomial identity. Degree comparison along every edge gives

\[
d_{\omega',j}=d_{\omega,i}.
\tag{8}
\]

For a common edge degree `d`, comparison of leading coefficients gives

\[
L_{\omega',j}
=
L_{\omega,i}\left(\frac QP\right)^{d-1}.
\tag{9}
\]

Following edges in finite control eventually reaches a directed cycle. Around a cycle of length `s`, equation `(9)` yields

\[
L=L\left(\frac QP\right)^{s(d-1)}.
\]

Since `L\ne0` and `P\ne Q`, one has `d=1`. Degree equality propagates this conclusion back through every reachable state.

Thus every section is affine. Eventual integer values make its slope and intercept ordinary integers, and eventual positivity makes the common slope positive. The exact constant equations in `(6)` are now precisely the finite affine-nucleus hypotheses of PR #64 `T-7402`. That theorem forces the unique affine solution

\[
v=P,\qquad s_{\omega,i}=c_i,
\qquad \pi_{\omega,i}(j)=j,
\]

which is `(7)`. ∎

## 4. Precisely scoped refinement corollary

The same proof applies after any **finite refinement of the control state** for which each refined section still uses one algebraic function of the complete ordinary high quotient `k`, is eventually integer-valued for every sufficiently large integer `k`, and satisfies the exact child identity `(6)` on all six outgoing cylinders. The refinement is then simply absorbed into `\Omega`.

This covers finite piecewise-algebraic descriptions only when their pieces are promoted to genuine full-tail section states with the displayed eventual-integrality and complete-subtree properties. No claim is made here for formulas defined only on one sparse progression with an unrelated reparametrized slope; that broader class would require a separate normalization theorem.

## 5. Why this is genuine but limited progress

This theorem eliminates an exhaustive class of proposed extraction mechanisms:

```text
finite affine nucleus
  -> closed by PR #64 T-7402;
finite rational nucleus
  -> closed by PR #64 T-7403;
finite algebraic full-tail nucleus
  -> closed by ACL-N092.
```

The negative conclusion is genuinely weaker than Collatz: it rules out one method class inside one strict six-branch subsystem. It neither excludes a single isolated survivor nor proves `m_n -> infinity`.

A successful positive construction must now use at least one feature absent from the theorem:

- genuinely unbounded section state;
- a section not algebraic on any finite full-tail control refinement;
- a construction confined to a proper infinite sublanguage rather than a self-copy of the complete subtree;
- or a direct ordinary-height/digit-escape theorem that decides the original least roots without recursive self-sectioning.

## 6. Gap and adversarial audit

- The complete-subtree hypothesis is essential. A single survivor may occupy a proper infinite sublanguage.
- Eventual integer-valuedness on the complete ordinary tail is essential to `ACL-N092.1`.
- Transcendental functions, pushdown sections, sparse-progression sections lacking a full-tail normalization, oracle-like future data, and genuinely unbounded arithmetic state remain outside scope.
- The theorem does not produce a root, a positive cycle, or a `K-####` object.
- The only branch-qualified dependency is the affine rigidity theorem `T-7402`; no status is silently promoted.

## 7. Exact remaining target

After this closure, enlarging the finite full-tail section formula again is not a meaningful offense. The chart changes full-objective status only by deciding

\[
\boxed{
\sup_n m_n<\infty
\quad\text{or}\quad
m_n\to\infty.
}
\]

The first alternative writes the stabilizing root and yields the physical seed `6m-5`; the second eliminates the complete six-branch architecture.
