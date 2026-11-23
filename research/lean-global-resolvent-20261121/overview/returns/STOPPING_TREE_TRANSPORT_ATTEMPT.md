# The actual optimal stopping law in the sibling comparison

**Status: unsuccessful direct attack on OPEN-F/S.** The finite stopping-tree
identities below are proved, but the required logarithmic distortion bound
is not. They are included to specify the law and the quantity that were
actually tested. They are not a new global estimate, a Lean theorem, or a
claim that the closing problem has become easier.

## 1. Exact inputs and stopping tree

Use positive odd ternary units that are not themselves periodic, with
forward transport killed at periodic states. Retain the critical inverse
operator and unit obstacle

\[
(Pf)(n)=\sum_{Ux=n}\frac3{2^{v_2(3x+1)}}f(x),\qquad
u(n)=1,\qquad V^{[0]}=u,\quad V^{[r+1]}=\max(u,PV^{[r]}).
\]

All parents in this display are retained unit parents. The imported
construction gives finite values, \(V^{[r]}\uparrow V\),
\(G\le V\le2\chi G\), and a fixed positive lower bound \(\delta\) for
the product of \(3x/(3x+1)\) along each actual finite retained path.
The provenance is PR180
`a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
`research/central-step-20261122/CRITICAL_BOUNDARY.md`, §§1 and 6.

Fix a retained root \(n\) and a depth \(r\). The Bellman recursion has
an exact stopping policy: stop at a node if the obstacle is chosen by its
maximum, otherwise continue to all its unit parents, and stop at the
depth limit. Choose a definite rule in a tie. Let \(\mathcal T\) be the
resulting prefix-free set of leaf words. It can be countably infinite,
because each inverse node has infinitely many parents; every leaf has
length at most \(r\).

For a leaf \(w\), put

\[
\ell_w=|w|,\quad A_w=\sum_{i=1}^{\ell_w}a_i,\quad
\omega_w=3^{\ell_w}2^{-A_w},\quad X_w=\text{its ordinary endpoint}.
\]

Induction on the depth, with nonnegative countable sums, gives

\[
V^{[r]}(n)=\sum_{w\in\mathcal T}\omega_w.
\tag{1}
\]

Consequently

\[
\mu(w)=\omega_w/V^{[r]}(n)
\tag{2}
\]

is the relevant probability law. It is the normalized **actual leaf
contribution law**, not independent geometric gaps and not the unstopped
law of a different root.

## 2. Transport the complete stopping tree

Let \(y\equiv n\pmod3\) be a second retained root. At paired states
\(x,z\), the PR175 signed repair selects the unique
\(d\in\{0,2,4\}\) with \(2^dz\equiv x\pmod9\). Write an allowed
gap as \(a+6k\), where \(1\le a\le6\). Replace \(a\) by the
representative of \(a+d\) modulo six, leaving \(k\) unchanged.

This is a bijection of the two allowed unit-parent classes and their
nonnegative six-step quotients. The paired children have the same
residue modulo three. It therefore defines a depth-preserving rooted
tree bijection. Each changed gap differs from the old one by an element
of \(\{-4,-2,0,2,4\}\).

Apply this bijection to every leaf and retain the same stop/continue
decisions. Denote its endpoint by \(Y_w\), total gap by \(B_w\), and
coefficient by \(\omega'_w=3^{\ell_w}2^{-B_w}\). The transferred tree
is a legal stopping policy at \(y\), so

\[
Z_y:=\sum_w\omega'_w\le V^{[r]}(y).
\tag{3}
\]

No terminal point is replaced by a rational or nonunit shadow. Since
\(|B_w-A_w|\le4r\), both the ratio \(\omega'_w/\omega_w\) and its
reciprocal are bounded by \(16^r\), uniformly over the countable leaf
set.

### Exact cost identity and entropy form

Put \(\Delta_w=B_w-A_w\). Equations (1)--(3) give

\[
\boxed{\frac{Z_y}{V^{[r]}(n)}
      =\mathbb E_\mu 2^{-\Delta_w}.}
\tag{4}
\]

In particular, Jensen's inequality yields the actual-law estimate

\[
V^{[r]}(y)\ge V^{[r]}(n)
               2^{-\mathbb E_\mu\Delta_w}.
\tag{5}
\]

All expectations are finite because \(|\Delta_w|\le4r\). If
\(\widetilde\mu(w)=\omega'_w/Z_y\), the exact relative-entropy
identity is

\[
D(\mu\Vert\widetilde\mu)
 =\log\frac{Z_y}{V^{[r]}(n)}
   +(\log2)\mathbb E_\mu\Delta_w.
\tag{6}
\]

Thus (5) is simply the nonnegativity of this relative entropy. It is
not a claim that the entropy term or the signed carry cost is small.

### Equivalent terminal-height form

Let \(\Lambda_w^x,\Lambda_w^y\) denote the actual path products at
the paired leaves. The ordinary affine identities give

\[
\omega_w=\frac n{X_w}\Lambda_w^x,\qquad
\omega'_w=\frac y{Y_w}\Lambda_w^y,
\]

and hence

\[
\boxed{\frac{Z_y}{V^{[r]}(n)}
=\frac yn\mathbb E_\mu
 \left[\frac{X_w}{Y_w}\frac{\Lambda_w^y}{\Lambda_w^x}\right]
\ge\delta\frac yn\mathbb E_\mu\frac{X_w}{Y_w}.}
\tag{7}
\]

The empty leaf is included: its endpoints are the two roots and its
products are one. Equation (7) retains the same source contribution law
as (4); it does not average under a second convenient ensemble.

## 3. Precisely what would pay OPEN-F

Take \(B(n)=64n+21\), and suppose \(n,U(n)\) are retained, as they
are along an escaping path. Then all \(B^j(n)\) are retained. Construct
the preceding transport separately to \(y_j=B^j(n)\), always from the
**same** stopping tree and probability law (2).

For every finite \(J\), (7) gives

\[
\sum_{j=1}^J64^{-j}V^{[r]}(B^j(n))
\ge\delta V^{[r]}(n)
 \sum_{j=1}^J\mathbb E_\mu\frac{X_w}{Y_w^{(j)}},
\tag{8}
\]

because \(64^{-j}B^j(n)/n\ge1\). Equivalently, (5) gives

\[
\sum_{j=1}^J64^{-j}V^{[r]}(B^j(n))
\ge V^{[r]}(n)
 \sum_{j=1}^J2^{-6j-\mathbb E_\mu\Delta_w^{(j)}}.
\tag{9}
\]

One sufficient estimate at an actual linear spike
\(V^{[r]}(n)\ge\eta n\) would therefore be, for some sibling index
\(j\),

\[
6j+\mathbb E_\mu\Delta_w^{(j)}
\le\log_2\log(2+n)+C_\eta.
\tag{10 -- UNPROVED}
\]

This would pay the required inverse-logarithmic lower bound with the
same target depth \(r\). A lower bound for the sum in (8) or (9) is
weaker and would also suffice. OPEN-F itself permits larger target
depths, so failure to prove (10) would not refute OPEN-F.

## 4. The attempted drift argument and its first missing step

The attempt was to exploit the signed repairs, stopping when the source
policy reaches the obstacle, and show that their mean accumulated cost
is only logarithmic in \(\log n\). Three observations do not supply
that conclusion:

1. Matching the child's residue modulo three determines the repaired
   exponent class uniquely. The per-edge negative costs are genuine,
   but no cancellation identity for their actual probabilities follows.
2. The conditional continuation weights of the original Bellman policy
   involve the values \(V^{[r-t]}(x)\) at its actual children. Replacing
   those weights by independent geometric gaps changes (2). The
   currently proved high-spike inequality bounds the total in (1), not
   the signs of the conditional repair costs.
3. Allowing ascending-gap or class-swapping pairings gives more tree
   transports, but it does not establish a drift inequality under (2).
   A terminal-height bound under an auxiliary law would still have to
   be transferred to this stopping law.

The fresh moving-fibre theorem in PR175 controls one specified root's
ordinary path law and its centered-depth trace error. Its comparison
does not identify the paired endpoint heights of these two different
inverse subtrees. Its explicit retained original-source submeasure
also prevents treating trace convergence as vanishing mass.

No bound of the strength (10), no adequate aggregate lower bound in
(8), and no alternative OPEN-F estimate was obtained. The proved
worst-case bound remains exponential in depth. The high-spike premise
does not currently supply an upper bound on an adequate obstacle depth,
either. No Lean formalization of (4)--(9) was undertaken: formalizing
these identities would not discharge the missing arithmetic expectation
bound, and they are not presented as an additional closing achievement.

## Exact fresh sources

- PR175, `08fe1388ad63c758680b3695249aca319515c47d`,
  `research/lean-global-closure-20261121/machinery/ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md`,
  §§2--3: actual signed tree bijection and the terminal-height identity.
- The same head, `MOVING_CESARO_FIBRES.md`, §§2--3 and 8--9: actual
  full-path comparison, moving trace, retained source, and its scope.
- PR180, `a66a44c9bf058cd7efe1018827ddda9a13297a21`,
  `research/deep-machinery-20261122/RENEWAL_TRANSPORT.md`, §5:
  singular ambient sibling translates do not determine the required
  ordinary-spike comparison.
- PR180's unchanged `research/central-step-20261122/CRITICAL_BOUNDARY.md`,
  §6: OPEN-S, OPEN-F, their canonical input qualifications, and the
  actual summability contradiction they would supply.

This is a record of a direct attempted proof and its exact unsupported
step. It does not improve a quantitative global closing bound.
