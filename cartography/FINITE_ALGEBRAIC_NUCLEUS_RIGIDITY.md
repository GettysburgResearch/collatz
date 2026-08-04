# General finite algebraic-section rigidity at the ordinary-extraction boundary

**Cartography atom:** `ACL-N092`  
**Author:** `gpt56-cartographer-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-26  
**Status:** `PROPOSED` pending independent reconstruction  
**Frozen native input:** PR #64 at `88884c3e590b08aeb2018872987e71e14de1fe7b`, especially `D-7401`, `T-7402`, and `T-7403`  
**Scope:** finite-control, eventually integer-valued algebraic-function sections carrying a complete expanding rational-base subtree  
**Counterexample candidates:** none

## 1. Full-objective role

For the six-branch chart, PR #64 proves that finite affine and finite rational-function section nuclei cannot recursively replace a large legal root by a smaller legal root. The theorem below isolates the exact general mechanism and closes all finite **algebraic** section nuclei at once.

This is an all-depth architecture exclusion. It is not a finite-prefix census and does not assume that sampled section attempts failed. Its negative conclusion is genuinely weaker than Collatz: it eliminates one broad proof mechanism inside any chart satisfying the stated hypotheses. It does not decide whether an isolated ordinary survivor exists.

## 2. Expanding rational-base chart

Let

\[
P>Q\ge2,
\qquad
\gcd(P,Q)=1,
\tag{1}
\]

and let

\[
\mathcal A=\{a_0,\ldots,a_{s-1}\}
\subset\{0,\ldots,Q-1\}
\tag{2}
\]

contain at least two distinct digits.

For each digit define its source and output representatives

\[
r_i=[-P^{-1}a_i]_Q,
\qquad
c_i={Pr_i+a_i\over Q}.
\tag{3}
\]

Thus

\[
QF(r_i+Qk)=P(r_i+Qk)+a_i,
\]

or equivalently

\[
F(r_i+Qk)=c_i+Pk.
\tag{4}
\]

If the next digit is `j`, then

\[
Qk'=Pk+c_i-r_j.
\tag{5}
\]

There are unique integers `kappa_(ij)` in `{0,...,Q-1}` and `lambda_(ij)` such that the complete child cylinder is

\[
k=\kappa_{ij}+Qt,
\qquad
k'=\lambda_{ij}+Pt,
\qquad t\in\mathbf Z_{\ge0}.
\tag{6}
\]

### Rigid-alphabet hypothesis

Assume that the digit alphabet has trivial affine stabilizer modulo `Q`:

\[
t+w\mathcal A=\mathcal A\pmod Q
\quad\Longrightarrow\quad
w\equiv1,\ t\equiv0\pmod Q.
\tag{7}
\]

Here `w` is not assumed to be a unit before the conclusion. PR #64 `T-7401` proves `(7)` for the six physical digits.

## 3. Algebraic integer-value lemma

### Lemma `ACL-N092.1`

Let `f` be a real branch, defined and analytic on some ray `[X_0,\infty)`, of a function algebraic over `\mathbf Q(X)`. Suppose

\[
f(n)\in\mathbf Z
\]

for every sufficiently large integer `n`. Then `f` is a polynomial in `\mathbf Q[X]` on that ray.

### Proof

An algebraic branch has a convergent Puiseux expansion at infinity. Consequently there is a rational exponent `\alpha` such that, for every fixed nonnegative integer `m`,

\[
f^{(m)}(x)=O(x^{\alpha-m})
\qquad(x\to+\infty).
\tag{8}
\]

Choose `m>\alpha`. Then `f^(m)(x)` tends to zero. Repeated integration gives the exact forward-difference identity

\[
\Delta^m f(n)
=
\int_{[0,1]^m}
 f^{(m)}(n+t_1+\cdots+t_m)
\,dt_1\cdots dt_m,
\tag{9}
\]

so

\[
\Delta^m f(n)\longrightarrow0.
\tag{10}
\]

Every value `f(n)` is an integer; hence every `m`th forward difference is an integer. Equation `(10)` forces

\[
\Delta^m f(n)=0
\]

for all sufficiently large `n`. Newton interpolation supplies a polynomial `p` in `\mathbf Q[X]`, of degree at most `m-1`, with

\[
f(n)=p(n)
\]

for every sufficiently large integer `n`.

Let `H(X,Y)` in `\mathbf Q[X,Y]` be an irreducible relation for the branch. Then `H(n,p(n))=0` for infinitely many `n`, so `H(X,p(X))` is identically zero. Therefore `Y-p(X)` divides `H` in `\mathbf Q(X)[Y]`. Irreducibility forces the branch itself to equal `p`. ∎

## 4. General finite algebraic-nucleus theorem

### Theorem `ACL-N092.2`

Let `Omega` be finite. For every reachable state `(omega,i)`, suppose there is a nonconstant real algebraic branch

\[
f_{\omega,i}(X)
\]

over `\mathbf Q(X)`, defined on a positive ray, such that:

1. `f_(omega,i)(n)` is a positive ordinary integer for every sufficiently large integer `n`;
2. every state has all `s` exact outgoing children;
3. for every child type `j`, some successor control `omega'` and a state-dependent permutation `pi_(omega,i)` satisfy

\[
Q f_{\omega',j}(\lambda_{ij}+Pt)
=
P f_{\omega,i}(\kappa_{ij}+Qt)
+a_{\pi_{\omega,i}(j)}
\tag{11}
\]

for every sufficiently large integer `t`.

Then every section is the original forward image:

\[
\boxed{
f_{\omega,i}(X)=PX+c_i,
\qquad
\pi_{\omega,i}(j)=j.
}
\tag{12}
\]

Consequently no finite algebraic-function nucleus gives a contracting, bounded, or seed-preserving recursive extraction of an ordinary root.

### Proof

By `ACL-N092.1`, every section is a polynomial. Write

\[
f_{\omega,i}(X)=L_{\omega,i}X^{d_{\omega,i}}+\cdots,
\qquad L_{\omega,i}\ne0.
\]

Equation `(11)` is a polynomial identity because it holds at infinitely many integers. Degree comparison along every edge gives

\[
d_{\omega',j}=d_{\omega,i}.
\tag{13}
\]

For a common edge degree `d`, leading coefficients satisfy

\[
L_{\omega',j}
=
L_{\omega,i}\left({Q\over P}\right)^{d-1}.
\tag{14}
\]

Following edges in finite control eventually reaches a directed cycle. Around a cycle of length `ell`, equation `(14)` gives

\[
L=L\left({Q\over P}\right)^{\ell(d-1)}.
\]

Since `L` is nonzero and `P` differs from `Q`, one has

\[
d=1.
\tag{15}
\]

Degree equality propagates back through every reachable state. Thus

\[
f_{\omega,i}(X)=v_{\omega,i}X+s_{\omega,i}.
\tag{16}
\]

Eventual integer values imply that both coefficients are ordinary integers: the first difference is `v_(omega,i)`, and one integer value then recovers the intercept. Eventual positivity gives a positive slope. Equation `(14)` at degree one makes the slope one common positive integer `v` on each reachable component.

Substitute `(16)` and the child transition `(5)` into `(11)`. Exact coefficient comparison leaves

\[
v(c_i-r_j)+Qs_{\omega',j}-Ps_{\omega,i}
=a_{\pi_{\omega,i}(j)}.
\tag{17}
\]

For fixed parent state, reduction modulo `Q` and the relation

\[
r_j\equiv-P^{-1}a_j\pmod Q
\]

show that the output alphabet is

\[
t_{\omega,i}+vP^{-1}\mathcal A
\pmod Q.
\]

The rigid-alphabet hypothesis `(7)` forces

\[
v\equiv P\pmod Q
\]

and fixes every label. Write

\[
v=P+mQ.
\tag{18}
\]

Define normalized section carries

\[
h_{\omega,i}=s_{\omega,i}-c_i-mr_i.
\tag{19}
\]

Using

\[
Qc_i=Pr_i+a_i,
\]

equation `(17)` simplifies exactly to

\[
\boxed{
Qh_{\omega',j}=Ph_{\omega,i}-ma_i.
}
\tag{20}
\]

The right side is independent of the chosen child `j`. Let `H` be the finite nonempty set of normalized carry values occurring after at least one transition. Because every parent has every child, each value occurs together with every current type, and therefore

\[
T_i(H)\subseteq H,
\qquad
T_i(h)={Ph-ma_i\over Q},
\quad0\le i<s.
\tag{21}
\]

Let `h_-` and `h_+` be the minimum and maximum of `H`, and let `a_min<a_max` be the extreme digits.

If `m>0`, invariance of `h_+` and `h_-` gives

\[
h_+\le {m a_{\min}\over P-Q},
\qquad
h_-\ge {m a_{\max}\over P-Q},
\]

contradicting `h_-\le h_+`.

If `m<0`, writing `m=-n` gives similarly

\[
h_+\le-{n a_{\max}\over P-Q},
\qquad
h_-\ge-{n a_{\min}\over P-Q},
\]

again a contradiction.

Thus `m=0`. Equation `(21)` becomes

\[
T_i(h)={P\over Q}h.
\]

Since `P/Q>1`, a finite invariant integer set can contain neither a positive maximum nor a negative minimum. Hence

\[
H=\{0\}.
\]

Equations `(18)` and `(19)` now give

\[
v=P,
\qquad
s_{\omega,i}=c_i,
\]

and `(12)` follows. ∎

## 5. Six-branch Collatz corollary

For the chart in PR #64,

\[
P=3^{12},
\qquad
Q=2^{19},
\]

and

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

PR #64 `T-7401` proves that this alphabet satisfies `(7)`. Therefore every finite algebraic full-tail section nucleus collapses to

\[
f_i(k)=Pk+c_i,
\]

the original expanding forward boundary value.

Combining the present theorem with PR #64 gives the strict hierarchy

```text
finite affine nucleus
  -> closed by T-7402;
finite rational nucleus
  -> closed by T-7403;
finite algebraic full-tail nucleus
  -> closed by ACL-N092.
```

## 6. Precisely scoped refinement corollary

The theorem survives any finite refinement of the control state for which each refined section still:

- is one algebraic function of the complete ordinary high quotient `k`;
- is eventually integer-valued for every sufficiently large integer `k`;
- carries every child of the refined complete subtree; and
- satisfies the exact identity `(11)`.

The refinement is simply absorbed into `Omega`. No claim is made for a formula defined only on one sparse progression with an unrelated reparametrized slope; that broader class requires its own normalization theorem.

## 7. Why this is genuine but limited progress

The theorem rules out an exhaustive method class, uniformly and without computation. A successful positive construction must now use at least one feature absent here:

- genuinely unbounded section state;
- a section not algebraic on any finite full-tail control refinement;
- a proper infinite sublanguage rather than a self-copy of the complete tree;
- or a direct ordinary-height or digit-escape theorem that decides the original least roots without recursive self-sectioning.

The theorem does **not** prove that the six-branch least roots diverge, exclude a single isolated survivor, construct a cycle, or produce a `K-####` object.

## 8. Exact remaining target

For the strict six-branch chart, full-objective status still changes only by deciding

\[
\boxed{
\sup_n m_n<\infty
\quad\text{or}\quad
m_n\to\infty.
}
\]

The first alternative writes the stabilizing root and yields the physical seed `6m-5`; the second eliminates the complete six-branch architecture. Enlarging the finite full-tail section formula again is not a meaningful offense.
