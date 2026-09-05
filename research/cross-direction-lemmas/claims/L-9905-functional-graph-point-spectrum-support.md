# L-9905 -- Functional-graph point spectrum and exact support extraction

Claim ID: `L-9905`
Title: Atomic point eigenvectors on the full trivial-basin quotient detect exactly nontrivial functional-graph components, while cycle-only quotients and approximate spectrum do not
Status: `PROPOSED / EXACT ABSTRACT SUPPORT THEOREM AND METHOD BOUNDARY`
Authoring agent: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Reviewing agents: `gpt56-synthesis-01-wave22-h-sunit-transfer` (adversarial self-review); `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: issue #27 as frozen at its 2026-07-21 update; PR #38 `ACL-N054` at `5ad965771869a647102e22115ed56749dbe2e254`
Scope: deterministic maps of countable sets; exact atomic pushforward on weighted sequence spaces; shortcut Collatz specialization
Related counterexample candidates: none; the theorem supplies an exact spectral equivalence, not a certified eigenvalue
Related atom: PR #38 `ACL-N054`

## 1. Result in one paragraph

For a deterministic countable map, the atomic pushforward on a weighted
`ell^1` space decomposes exactly over completely invariant functional-graph
components.  Quotienting by the **whole basin** of an accounted cycle, rather
than by the finite cycle alone, makes every nonzero quotient point eigenvector
live on an unaccounted component.  Such a component contains either another
directed cycle or no directed cycle at all.  For the shortcut Collatz map and
the explicit weight

\[
 w_s(n)=(1+n)^{-s},\qquad s>1,
\tag{1}
\]

the converse also holds: every nontrivial cycle gives finite-support point
eigenvectors, while every cycle-free component gives bilateral-chain point
eigenvectors for every

\[
 1<|\lambda|<2^s.
\tag{2}
\]

Thus a rigorously certified nonzero point eigenvector on the full-basin
quotient would prove a Collatz counterexample component exists.  The exact
operator is bounded but not compact, so this theorem does not supply the
nuclear/Fredholm certificate requested in the second half of issue #27.

## 2. Weighted atomic sequence spaces

Let `X` be countable, let

\[
 T:X\longrightarrow X
\tag{3}
\]

be deterministic, and fix a faithful weight

\[
 w:X\longrightarrow(0,\infty).
\tag{4}
\]

Put

\[
 E_w=\ell^1(X,w)
 =\left\{f:X\to\mathbf C:
          \|f\|_w:=\sum_{x\in X}|f(x)|w(x)<\infty\right\}.
\tag{5}
\]

Every coordinate evaluation is continuous.  In particular, support is a
literal atomic notion; no almost-everywhere quotient is being taken.

Define the atomic pushforward first on basis vectors by

\[
 P\delta_x=\delta_{T(x)}.
\tag{6}
\]

In coordinates this is

\[
 (Pf)(y)=\sum_{T(x)=y}f(x).
\tag{7}
\]

Also define the composition operator

\[
 (Uf)(x)=f(Tx).
\tag{8}
\]

These are different operators on `E_w`; neither should be called the adjoint
of the other without specifying a separate dual pairing.

## 3. Exact boundedness criteria

Define

\[
 A_P=\sup_{x\in X}{w(Tx)\over w(x)},
\tag{9}
\]

and

\[
 A_U=\sup_{y\in X}
 {\sum_{T(x)=y}w(x)\over w(y)},
\tag{10}
\]

where an infinite preimage sum is allowed to be `+infinity`.

### Proposition 1 -- boundedness is equivalent to the weight inequalities

The pushforward extends boundedly to `E_w` if and only if `A_P<infinity`, and

\[
 \boxed{\|P\|=A_P.}
\tag{11}
\]

The composition operator is bounded if and only if `A_U<infinity`, and

\[
 \boxed{\|U\|=A_U.}
\tag{12}
\]

### Proof

If `A_P<infinity`, then every preimage sum in (7) converges absolutely and

\[
 \begin{aligned}
 \|Pf\|_w
 &\le\sum_yw(y)\sum_{T(x)=y}|f(x)|\\
 &=\sum_x|f(x)|w(Tx)
 \le A_P\|f\|_w.
 \end{aligned}
\tag{13}
\]

Testing on `delta_x/w(x)` proves the reverse norm inequality and necessity.
Similarly,

\[
 \begin{aligned}
 \|Uf\|_w
 &=\sum_x|f(Tx)|w(x)\\
 &=\sum_y|f(y)|\sum_{T(x)=y}w(x)
 \le A_U\|f\|_w,
 \end{aligned}
\tag{14}
\]

and testing on `delta_y/w(y)` proves necessity and equality. **QED**

These criteria are part of the theorem hypotheses.  A formal matrix on a
weighted space is not a spectral operator until the relevant bound is proved.

## 4. Complete invariance and the correct quotient

A subset `B subseteq X` is **completely invariant** when

\[
 T^{-1}(B)=B.
\tag{15}
\]

Put `C=X\B`.  Both `B` and `C` are then forward and backward invariant.  The
coordinate subspaces

\[
 E_B=\{f\in E_w:\operatorname{supp}f\subseteq B\},
 \qquad
 E_C=\{f\in E_w:\operatorname{supp}f\subseteq C\}
\tag{16}
\]

are closed, and

\[
 E_w=E_B\oplus_1 E_C.
\tag{17}
\]

Both `P` and `U` reduce this decomposition.  Hence the Banach quotient is not
an abstract lifting problem:

\[
 \boxed{E_w/E_B\ \cong\ E_C}
\tag{18}
\]

isometrically, through coordinate restriction.  We write `bar(P)` for the
induced pushforward, identified with `P|_(E_C)`.

For a directed cycle `O`, its full basin

\[
 \mathcal B(O)=\{x\in X:T^k x\in O\text{ for some }k\ge0\}
\tag{19}
\]

is completely invariant.  The finite span of the cycle alone generally is
not the correct accounted subspace: it leaves arbitrarily deep transient
trees in the quotient.

## 5. Point-spectrum support extraction

Declare two vertices weakly equivalent when they lie in the same connected
component of the undirected graph generated by the edges `x--T(x)`.  These
functional-graph components are completely invariant.  A component of a
deterministic functional graph contains at most one directed cycle.

### Theorem 2 -- exact component extraction

Assume `A_P<infinity`, let `B` be completely invariant, and let

\[
 0\ne f\in E_C,
 \qquad
 Pf=\lambda f
\tag{20}
\]

for any `lambda in C`.  Then some functional-graph component
`K subseteq C` has

\[
 0\ne f|_K\in E_w,
 \qquad
 P(f|_K)=\lambda f|_K.
\tag{21}
\]

The component `K` satisfies exactly one of:

1. `K` contains a directed cycle outside `B`; or
2. `K` contains no directed cycle, and every forward orbit in `K` is
   injective.

### Proof

Restriction to a functional-graph component commutes with `P`, since every
preimage and image of a vertex stays in its component.  At least one component
restriction of the nonzero vector `f` is nonzero, proving (21).

Two distinct directed cycles cannot lie in one functional-graph component:
following the unique forward edge from any connecting path would force the
two forward tails to merge and hence enter the same cycle.  Finally, if
`T^m x=T^n x` with `m<n`, the vertices from `T^m x` through `T^(n-1)x` form a
directed cycle.  Thus every forward orbit in a cycle-free component is
injective. **QED**

The theorem is about **point eigenvectors**.  A small residual
`\|Pf-lambda f\|` is not a substitute for (20).

## 6. Why quotienting only the cycle is false

Let

\[
 X=\mathbf Z_{\ge0},
 \qquad
 T(0)=0,
 \qquad
 T(n)=n-1\quad(n\ge1),
\tag{22}
\]

and use unweighted `ell^1`.  Every vertex reaches the accounted fixed point
`0`.  Nevertheless, modulo only `span{delta_0}`, for every `|lambda|<1`,

\[
 f_\lambda=\sum_{n\ge1}\lambda^{n-1}\delta_n
\tag{23}
\]

is nonzero and

\[
 Pf_\lambda=\delta_0+\lambda f_\lambda.
\tag{24}
\]

Thus its quotient class is a genuine eigenvector of eigenvalue `lambda`, even
though no nontrivial cycle or divergent component exists.  Quotienting the
whole basin makes the quotient zero and removes this artifact.

## 7. Shortcut Collatz specialization

Let

\[
 \mathcal C(n)=
 \begin{cases}
  n/2,&n\text{ even},\\
  (3n+1)/2,&n\text{ odd},
 \end{cases}
 \qquad n\in\mathbf Z_{>0}.
\tag{25}
\]

Its accounted trivial cycle is

\[
 \mathcal O_0=\{1,2\}.
\tag{26}
\]

Fix `s>1` and use the conjecture-independent weight (1).  This weight is
faithful and summable on all positive integers; it is defined without knowing
whether a counterexample component exists.

### Proposition 3 -- both exact atomic operators are bounded

For the pushforward `P_s delta_n=delta_(mathcal C(n))`,

\[
 \boxed{\|P_s\|=2^s.}
\tag{27}
\]

Indeed, on an even input `n=2m`,

\[
 {w_s(\mathcal C(n))\over w_s(n)}
 =\left({1+2m\over1+m}\right)^s<2^s,
\tag{28}
\]

with supremum `2^s`, while on an odd input `mathcal C(n)>n`, so the ratio is
at most one.

The composition operator is also bounded.  Every `y` has the even preimage
`2y` and at most one positive odd preimage `(2y-1)/3`.  When the latter is
admissible,

\[
 {w_s((2y-1)/3)\over w_s(y)}=\left({3\over2}\right)^s.
\tag{29}
\]

Consequently

\[
 \boxed{\|U_s\|\le1+(3/2)^s.}
\tag{30}
\]

### The full trivial-basin quotient

Put

\[
 \mathcal B_0
 =\{n:\mathcal C^k(n)\in\{1,2\}
       \text{ for some }k\ge0\},
 \qquad
 \mathcal D=\mathbf Z_{>0}\setminus\mathcal B_0.
\tag{31}
\]

The basin `B_0` is completely invariant.  Define

\[
 \mathcal Q_s
 =\ell^1(\mathbf Z_{>0},w_s)/E_{\mathcal B_0}
 \cong\ell^1(\mathcal D,w_s),
\tag{32}
\]

and let `bar(P_s)` be the induced pushforward.

### Theorem 4 -- exact quotient point-spectrum equivalence

The following are equivalent:

1. `mathcal D` is nonempty;
2. `mathcal Q_s` is nonzero;
3. `bar(P_s)` has a nonzero point eigenvector with nonzero eigenvalue.

More precisely:

- if a component of `mathcal D` contains a directed cycle of length `p`, then
  every `lambda` with `lambda^p=1` is a point eigenvalue supported on that
  cycle;
- if a component of `mathcal D` is cycle-free, then every

  \[
   1<|\lambda|<2^s
  \tag{33}
  \]

  is a point eigenvalue supported on a bilateral path in that component.

### Proof

The implications `3=>2=>1` are immediate from the exact quotient (32).

Suppose first that a component contains the cycle

\[
 x_0\longmapsto x_1\longmapsto\cdots
 \longmapsto x_{p-1}\longmapsto x_0.
\tag{34}
\]

For `lambda^p=1`, the finite vector

\[
 f_\lambda=\sum_{j=0}^{p-1}\lambda^{-j}\delta_{x_j}
\tag{35}
\]

satisfies `P_s f_lambda=lambda f_lambda`.

Now suppose the component of `n_0` is cycle-free.  The shortcut map has the
canonical predecessor `2n` of every `n`.  Define a bilateral path by

\[
 x_k=\mathcal C^k(n_0)\quad(k\ge0),
 \qquad
 x_{-j}=2^j n_0\quad(j\ge1).
\tag{36}
\]

It obeys `mathcal C(x_k)=x_(k+1)` for every integer `k`.  Its vertices are all
distinct, because a repetition would create a directed cycle.  For (33), put

\[
 f_\lambda=\sum_{k\in\mathbf Z}\lambda^{-k}\delta_{x_k}.
\tag{37}
\]

The nonnegative half converges in `ell^1(w_s)` because

\[
 \sum_{k\ge0}|\lambda|^{-k}w_s(x_k)
 \le\sum_{k\ge0}|\lambda|^{-k}<\infty.
\tag{38}
\]

For the negative half,

\[
 \sum_{j\ge1}|\lambda|^jw_s(2^jn_0)
 \le n_0^{-s}
     \sum_{j\ge1}\left({|\lambda|\over2^s}\right)^j
 <\infty.
\tag{39}
\]

Absolute convergence and boundedness of `P_s` permit reindexing:

\[
 P_sf_\lambda
 =\sum_{k\in\mathbf Z}\lambda^{-k}\delta_{x_{k+1}}
 =\lambda f_\lambda.
\tag{40}
\]

The whole path remains in `mathcal D` by complete invariance.  This proves
`1=>3`. **QED**

### Collatz implication

A certified nonzero point eigenvector of `bar(P_s)` proves `mathcal D` is
nonempty.  The component extracted by Theorem 2 then contains either:

1. a positive directed cycle other than `{1,2}`; or
2. a cycle-free positive orbit.

In the second case the orbit consists of infinitely many distinct positive
integers and is therefore unbounded.  Either case is a counterexample to the
shortcut Collatz conjecture, and hence to the standard Collatz conjecture.

The space definition does not assume such a component: the weight and full
space are explicit on every positive integer.  However, certifying that a
quotient vector is nonzero cannot be replaced by merely finding a small
residual on the unquotiented operator.

## 8. The one-sided orbit sum in issue #27 has a boundary term

For an injective forward ray `x_(k+1)=T(x_k)`, the formal one-sided sum

\[
 g_\lambda=\sum_{k\ge0}\lambda^{-k}\delta_{x_k}
\tag{41}
\]

obeys, whenever it belongs to the space,

\[
 \boxed{Pg_\lambda
       =\lambda g_\lambda-\lambda\delta_{x_0}.}
\tag{42}
\]

It is not an eigenvector.  The bilateral construction (36)--(40), made
possible by the exact doubling predecessors, removes this source boundary.
For a general countable map, a cycle-free component need not contain a
bi-infinite path, so the converse half of Theorem 4 is Collatz-specific.

## 9. Approximate spectrum is not point spectrum

Let

\[
 X=\{o\}\cup
   \{(m,j):m\ge1,\ 1\le j\le m\},
\tag{43}
\]

with

\[
 T(o)=o,
 \quad
 T(m,1)=o,
 \quad
 T(m,j)=(m,j-1)\quad(j\ge2).
\tag{44}
\]

Use unweighted `ell^1` and quotient only by `span{delta_o}`.  Every basis
vector is killed after finitely many quotient iterates, and every original
vertex reaches `o`.  The quotient pushforward has no nonzero point
eigenvalue: for such an eigenvalue, projection to each finite chain would
give an eigenvector of a nilpotent finite-chain block, hence would vanish;
then every coordinate of the original eigenvector would vanish.

Nevertheless, for every `|lambda|=1`,

\[
 v_m={1\over m}\sum_{j=1}^m\lambda^{j-1}\delta_{(m,j)}
\tag{45}
\]

has norm one and

\[
 \|Pv_m-\lambda v_m\|_1={1\over m}\longrightarrow0.
\tag{46}
\]

Thus a bounded direct sum of finite nilpotent blocks, in which every basis
orbit terminates, can have large approximate spectrum without a nonzero point
eigenvalue and without any counterexample component.  (The completed direct
sum is not algebraically locally nilpotent on every infinite-support vector.)
Galerkin eigenvalues or pseudospectral residuals do not satisfy `ACL-N054`.

## 10. Composition and smooth-density artifacts

Because `s>1`, the constant function belongs to the Collatz space:

\[
 \mathbf1\in\ell^1(\mathbf Z_{>0},w_s),
 \qquad
 U_s\mathbf1=\mathbf1.
\tag{47}
\]

This eigenfunction exists whether or not a counterexample component exists.
After passage to the full-basin quotient, its restriction is nonzero exactly
when `mathcal D` is nonempty, which restates the question rather than
detecting it.  The pushforward theorem uses atomic coefficients and component
restrictions; it does not apply automatically to a Koopman eigenfunction,
an invariant density modulo a reference measure, or an analytic inverse-branch
transfer operator.

To transport a spectral certificate from another function space `H`, one
must prove an exact intertwining map preserving the relevant quotient and
show that the certified eigenvector lies in the image of the atomic space.
Nuclearity or smoothness alone supplies neither fact.

## 11. The faithful operator here is not nuclear

Let

\[
 e_m={\delta_{2m}\over w_s(2m)}.
\tag{48}
\]

Then `\|e_m\|_(w_s)=1`, while

\[
 \|P_se_m\|_{w_s}
 ={w_s(m)\over w_s(2m)}
 \longrightarrow2^s.
\tag{49}
\]

The images have pairwise disjoint supports and hence no norm-convergent
subsequence.  Therefore `P_s` is not compact.  Since every nuclear operator
between Banach spaces is compact, `P_s` is not nuclear; no Hilbert-space
trace-class assertion is being made on this weighted `ell^1` space.

This is the exact division of labor between the two atoms in PR #38:

- `ACL-N054` is resolved here for the atomic point spectrum and full-basin
  quotient;
- `ACL-P055`, a certified spectral excess for a nuclear operator together
  with a support-preserving bridge back to this quotient, remains open.

A Fredholm determinant of a different smoothed operator cannot be inserted
into Theorem 4 without that bridge.

## 12. Weight failures and sharp scope

The boundedness hypotheses cannot be omitted.  For shortcut Collatz:

- with `w(n)=exp(-n)`, the even-edge ratio

  \[
   {w(n/2)\over w(n)}=e^{n/2}
  \tag{50}
  \]

  is unbounded;
- with `w(n)=exp(n)`, the odd-edge ratio is

  \[
   {w((3n+1)/2)\over w(n)}=e^{(n+1)/2},
  \tag{51}
  \]

  also unbounded.

Thus neither naive exponential decay nor naive exponential growth defines a
bounded atomic pushforward.

The annulus (33) is a uniform sufficient range for every cycle-free Collatz
component under `w_s`.  At `|lambda|=2^s`, the negative doubling tail in
(39) does not converge.  At the lower boundary `|lambda|=1`, convergence of
the forward half depends on the particular orbit, so no universal endpoint
claim is made.

## 13. Source and dependency audit

- Issue #27 explicitly identifies the missing point-spectrum/support theorem
  and warns that approximate spectrum of a locally nilpotent operator is not
  enough.  Equation (42) corrects its one-sided eigenvector sketch.
- PR #38 `ACL-N054` asks for point-spectrum support extraction after removing
  the trivial component.  The full basin in (31), not merely the two cycle
  vertices, is the necessary meaning of that removal.
- No nuclearity, trace formula, spectral determinant, interval computation,
  or external functional-analysis theorem is imported.
- Proposition 1, the component theorem, and every Collatz eigenvector are
  proved directly from the weighted `ell^1` norm and the functional graph.
- No support outside the trivial basin is assumed in the space definition.
  Such support appears only in the hypothesis that a quotient vector is
  nonzero or in the conditional construction beginning with a nonempty
  component.

## 14. Gap audit

- The equivalence does not itself certify `mathcal Q_s ne 0`; doing so is the
  Collatz problem in spectral form.
- The quotient norm is

  \[
   \|[f]\|=\sum_{n\in\mathcal D}|f(n)|w_s(n).
  \tag{52}
  \]

  A coordinate proof that this is positive already exhibits mass on a
  counterexample component.  A genuinely nonconstructive route would need an
  independent operator-theoretic certificate for a nonzero quotient spectral
  projection.
- The exact atomic operator is not compact.  A nuclear realization must come
  with a proved support-preserving intertwiner; smooth invariant densities and
  approximate eigenvectors are insufficient.
- A nonzero eigenvector on a quotient by only the finite trivial cycle has no
  counterexample implication, by (22)--(24).
- The theorem does not claim that the support of an arbitrary complex
  eigenvector equals an entire component.  It proves that a nonzero component
  restriction is itself an eigenvector and that the component is
  unaccounted.

## 15. Suggested next attack

Construct a compact or nuclear operator `L` together with an injective,
quotient-compatible intertwiner from a dense `P_s`-invariant atomic subspace,
and prove that a certified spectral projection of `L` lies in the completed
image.  The `3n-1` positive control from issue #27 should then recover its
known nontrivial cycles as finite-support atomic eigenvectors before any
Collatz spectral excess is trusted.

## Source links

- [Issue #27 -- spectral witness accounting](https://github.com/gfreund123/collatz/issues/27)
- [PR #38 -- global counterexample map and `ACL-N054`](https://github.com/gfreund123/collatz/pull/38)
