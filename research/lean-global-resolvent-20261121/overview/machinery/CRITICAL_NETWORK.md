# Applying graph criticality to the actual ordinary transport

**Status: written theorem under the pinned ordinary harmonic-reference
input. No escape-exclusion estimate is proved.** This note applies the
criticality theory of Keller, Pinchover and Pogorzelski to the actual
symmetrized ordinary transport. The application succeeds: every hypothetical
escaping component is a recurrent, critical weighted network. Its
consequence is a precise limitation on a proposed Hardy/energy argument,
not the disappearance of that component.

The attempted positive argument was to obtain the extra coercivity needed
to bound PR177's run-weighted terminal energy. Criticality shows that no
nonzero global Hardy weight can be obtained for this symmetric form on an
escaping component. Moreover, compact approximation in the ordinary
Dirichlet energy already holds there. Such approximation cannot itself
remove the escaping source.

## 1. The actual domain and imported data

Use the positive odd ternary-unit domain killed on first entering any
periodic state, with

\[
U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

The pinned construction provides a function on ordinary integer states,

\[
0<\nu(n)\le A,\qquad
\sum_{Ux=q}\nu(x)=\nu(q).
\tag{1}
\]

Its predecessor-population and canonical-envelope qualifications remain
attached. Fix one escaping connected component \(\mathcal C\), if such a
component exists. There is no killing within this component. No state is
periodic, and all forward rays in the component eventually meet.

PR183 constructs an integer clock \(h\) and a capacity \(c\in(0,A]\) with

\[
h(Un)=h(n)+1,\qquad
\sum_{h(n)=r}\nu(n)=c\quad(r\in\mathbb Z).
\tag{2}
\]

Choose the clock so that a prescribed root \(o\) has \(h(o)=0\).
On \(\ell^2(\mathcal C,\nu)\), write

\[
(\mathsf C f)(n)=f(Un),\qquad
(Kf)(q)=\nu(q)^{-1}\sum_{Ux=q}\nu(x)f(x).
\]

Then \(\mathsf C\) is an isometry, \(K=\mathsf C^*\), and
\(K\mathsf C=I\). These are actual integer operators, with all
source collisions included.

## 2. The symmetric network and its exact energy

Put one undirected edge between each \(n\) and \(Un\), with conductance

\[
b(n,Un)=b(Un,n)=\nu(n).
\tag{3}
\]

There are no loops or pairs counted twice: either would give a periodic
state. Infinite vertex degree is allowed. Equation (1) gives local
summability and the exact weighted degree

\[
\sum_y b(n,y)=2\nu(n)<\infty.
\tag{4}
\]

The associated reversible transition is
\(P_{\rm sym}=(\mathsf C+K)/2\). Its forward step has probability one
half; its other half is the actual inverse kernel. The energy, with each
edge counted once, is

\[
\mathcal E(f)=\frac12\sum_{x,y}b(x,y)|f(x)-f(y)|^2
=\sum_n\nu(n)|f(n)-f(Un)|^2
=\|(I-\mathsf C)f\|_\nu^2.
\tag{5}
\]

In particular \(\mathcal E(f)\le4\|f\|_\nu^2\) for \(f\in\ell^2(\nu)\).
The normalized nonnegative Laplacian is
\(2I-\mathsf C-K\); dividing it by two gives \(I-P_{\rm sym}\).

## 3. Explicit null functions, including finite-support approximation

For \(m\ge1\), define

\[
v_m(n)=\max\{0,1-|h(n)|/m\}.
\tag{6}
\]

This function has finitely many nonzero clock layers, but not necessarily
finitely many vertices. Equation (2) makes it square summable. Its
successive clock differences have magnitude \(1/m\) on exactly \(2m\)
edges of the integer clock. Hence

\[
v_m(o)=1,\quad 0\le v_m\le1,\quad v_m(n)\longrightarrow1,
\qquad \mathcal E(v_m)=\frac{2c}{m}.
\tag{7}
\]

The infinite support within a layer must not be suppressed. Enumerate the
component and choose a finite set \(F_m\), containing \(o\) and its first
\(m\) vertices, such that

\[
\|v_m-v_m\mathbf1_{F_m}\|_\nu\le1/m.
\]

Such a set exists because \(v_m\in\ell^2(\nu)\). Set
\(e_m=v_m\mathbf1_{F_m}\). Then \(e_m\) has genuinely finite support,
\(e_m(o)=1\), \(0\le e_m\le1\), and \(e_m\to1\) pointwise. Using (5),

\[
\mathcal E(e_m)^{1/2}
\le\mathcal E(v_m)^{1/2}
   +2\|e_m-v_m\|_\nu
\le\sqrt{2c/m}+2/m\longrightarrow0.
\tag{8}
\]

This is a finite-support null sequence for the actual network, with no
replacement of its infinite branching by a locally finite approximation.

## 4. A successful application of the literature theorem

Keller--Pinchover--Pogorzelski, *Criticality theory for Schrödinger
operators on graphs*, Theorem 5.3, identifies a finite-support null
sequence with criticality on a connected locally summable weighted graph.
With zero potential, their Remark 5.8 identifies this with recurrence.
All the hypotheses were verified in (3)--(8). The same theorem gives
uniqueness, up to scale, of positive superharmonic functions. Here the
ground state is the constant one. Their Theorem 5.10 also identifies the
extended energy space with all finite-energy functions.

Thus, on each hypothetical escaping component:

1. The symmetric network is recurrent and critical.
2. Every positive symmetric superharmonic function is constant.
3. There is no nonzero nonnegative vertex weight \(w\) satisfying
   \(\mathcal E(\varphi)\ge\sum_nw(n)|\varphi(n)|^2\) for every
   finitely supported \(\varphi\).
4. Every finite-energy function admits finite-support approximation in
   the energy-plus-one-root-value norm.

The third consequence also follows immediately from (8): if \(w(x)>0\)
at any vertex, then \(e_m(x)\to1\), whereas \(\mathcal E(e_m)\to0\).
The fourth can be proved directly for a bounded finite-energy function
\(f\), which is the case needed below. Multiply it by \(e_m\). The identity

\[
((1-e_m)f)(x)-((1-e_m)f)(y)
=(1-e_m(x))(f(x)-f(y))+f(y)(e_m(y)-e_m(x))
\]

and \(|a+b|^2\le2|a|^2+2|b|^2\) show
\(\mathcal E((1-e_m)f)\to0\): the first edge sum tends to zero by
dominated convergence against the finite energy of \(f\), and the second
is at most \(2\|f\|_\infty^2\mathcal E(e_m)\).

This application is not a new proof of the general criticality theorem.
The concrete Collatz deduction is the explicit null sequence (6)--(8)
from the actual synchronous-class masses.

## 5. Why the canonical Green charge is not eliminated

The canonical bounded potential satisfies

\[
0<R<1,\qquad R-KR=g=d/\nu>0,
\qquad K^jR(q)\downarrow0
\tag{9}
\]

at each fixed ordinary vertex. On the forward ray of an escaping
component,

\[
R(U^j x)\longrightarrow F_{\mathcal C}
=D_{\mathcal C}/c\in(0,1).
\tag{10}
\]

The strict upper bound follows from the imported canonical comparison
\(h\ge\delta\nu\) and \(R=1-\lambda h/\nu\), with \(\lambda\to1\).

Equation (9) makes \(R\) superharmonic for the **directed inverse**
kernel. It does not make \(R\) superharmonic for the symmetric walk. In
fact the exact symmetric Laplacian is

\[
(2I-\mathsf C-K)R=g+R-\mathsf C R.
\tag{11}
\]

The last difference is a signed term. Criticality proves it cannot be
discarded: if the right side were nonnegative everywhere, the bounded
positive function \(R\) would be constant. Then \(KR=R\), contrary to
\(g>0\). Consequently each hypothetical escaping component contains a
vertex with

\[
R(Un)-R(n)>g(n).
\tag{12}
\]

The prospective extra sign is not merely unverified; it is incompatible
with the other inputs on an escaping component. This does not prove that
the component exists or that it cannot be ruled out arithmetically.

The canonical \(R\) has finite ordinary energy under PR175's input. By
Section 4 it has finite-support approximants in that energy even if
\(F_{\mathcal C}>0\). This does not conflict with PR180's positive defect
for the particular finite inverse-Green truncations \(R_M\): a specified
sequence can fail to converge in energy although other approximants do
converge. In particular, the existence of *some* energy approximation is
too weak to prove that the original escaping charge vanishes.

The optimal-Hardy construction of Keller--Pinchover--Pogorzelski also
requires the stated positive supersolutions and properness of their
ratio. Using \(R\), or \(R/(1-R)\), as that proper coordinate fails on
(10): an infinite forward ray remains in a compact subinterval of
\((0,\infty)\). The relevant symmetric supersolution condition already
fails by (11)--(12).

## 6. What remains of the positive energy attack

PR177 proves that a positive escaping coefficient forces the terminal
energy \(\mathfrak e_N\) to satisfy

\[
\sum_q4^{\operatorname{runs}(q)}\mathfrak e_N(q)\longrightarrow\infty.
\]

The present criticality theorem does not bound that weighted energy.
Its quadratic form is the unweighted ordinary energy (5), and it permits
the positive forward boundary (10). A new inequality exploiting the
actual numerical labels or binary runs is still required. No such upper
bound was obtained in this attempt. A global Hardy weight for (5), an
unproved symmetric-superharmonic sign for \(R\), or compact energy
approximability cannot be substituted for it.

## Exact sources and evidence

- Primary literature: M. Keller, Y. Pinchover and F. Pogorzelski,
  *Criticality theory for Schrödinger operators on graphs*,
  [arXiv:1708.09664v1](https://arxiv.org/html/1708.09664v1),
  Theorems 5.3 and 5.10, Remark 5.8. The cited statements and their graph
  hypotheses were read directly.
- Primary literature: the same authors, *Optimal Hardy inequalities for
  Schrödinger operators on graphs*,
  [arXiv:1612.04051v2](https://arxiv.org/html/1612.04051v2),
  Theorem 1.1 and Corollary 1.3. Their properness and supersolution
  hypotheses are not supplied by the canonical directed potential.
- PR183, `68345f60a4f757acb42a69a4ac95910f8ce26163`,
  `research/profound-step-20261122/operator/WOLD_CHANNELS.md`,
  equations W1--W7: exact ordinary flow, component clock and layer mass.
- PR185, `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`,
  `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`:
  the upstream canonical harmonic construction and its qualifications.
- PR175, `728389c2ad4796853948250a90188b0697483d92`,
  `research/lean-global-closure-20261121/LITERATURE_DIRICHLET_BOUNDARY.md`:
  finite canonical Dirichlet energy.
- PR180, `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
  `research/central-step-20261122/CRITICAL_BOUNDARY.md`:
  canonical forward boundary and the defect of the specified \(R_M\).
- PR177, `431d858d1ac92e88f4a58f6610c0d67733dc7242`,
  `research/lean-exact-witness-global-20261121/TERMINAL_DIRICHLET_RUN_MASS.md`:
  the terminal energy measure and its run-weighted divergence.

This is written mathematics, not an imported Lean axiom or a new formal
proof of the infinite network statements. No numerical experiment is
used to infer criticality or recurrence.
