# The canonical obstacle removes the whole avoiding boundary

**Status:** written analytic theorem with a separately checked abstract
Lean core. The Collatz-specific existence and regularity inputs remain
source-qualified. This is an inverse first-entrance theorem, not a theorem
that an ordinary forward orbit returns to the contact set.

The starting source is PR180 at
`bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`, in particular
`research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`
and `research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md`.
The former constructs the least envelope and removes individual ray
atoms; the latter supplies its stationary normalization and already
credits the finite-depth comparison. Neither result is claimed here as
new. The present argument removes an entire killed inverse boundary and
produces an exact contact-entrance expansion.

## 1. Actual operator and canonical data

On all positive integers let

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
\frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right),
\qquad g(q)=\mathbf1_{3\nmid q}.
\tag{1}
\]

Every parent is a positive odd integer. On odd targets these are the
actual inverse edges of the odd map \(U\). An even target is handled
by a shortcut word stopping before the remaining halvings. We preserve
this all-positive domain when using minimality.

The imported canonical envelope is finite at every positive integer and
satisfies

\[
V=\max(g,PV),\qquad V\ge g,\qquad PV\le V.
\tag{2}
\]

It is the least nonnegative excessive majorant of \(g\). In particular,
the parent sum \(PV(q)\) is finite for each ordinary \(q\). Its
harmonicization satisfies

\[
PG=G,\qquad \frac{V}{2\kappa}\le G\le V,
\qquad 0<\kappa<\infty.
\tag{3}
\]

Both functions vanish at multiples of three; at units, \(V\ge1\)
and \(G>0\). The exact value \(\kappa=\mu^{-1}\) and the
stationary-density proof of (3) belong to the frozen source. The earlier
critical-Abel comparison supplies an alternative absolute comparison.

## 2. General minimality lemma

Suppose \(V\) is a least nonnegative excessive majorant of a
nonnegative obstacle \(b\). Let \(\phi\ge0\) be subharmonic:
\(P\phi\ge\phi\). Assume a constant \(\delta>0\) satisfies

\[
\delta\phi\le V-b,
\tag{4}
\]

and subtraction in the parent sum is legitimate. Then \(\phi=0\).

Indeed, \(W=V-\delta\phi\ge b\), and

\[
PW=PV-\delta P\phi\le V-\delta\phi=W.
\]

Leastness gives \(V\le W\), whence \(\delta\phi\le0\).
For a countable nonnegative kernel, the conditions \(0\le\phi\le V\)
and \(PV(q)<\infty\) justify the subtraction by ordinary absolute
summability. The Lean module proves both the abstract lemma and this
countable-kernel implication.

The formal minimality interface quantifies only over competitors
\(b\le W\le V\), which is sufficient because the subtraction above
has precisely these bounds. This restriction is deliberate: a Lean
`Real.tsum` is defined to be zero on a nonsummable family, so unrestricted
real-valued competitors could otherwise create a false zero parent sum.
For the restricted competitors, \(0\le W\le V\) and summability
of the parent series of \(V\) guarantee genuine summability. A
separate kernel lemma derives the restricted interface from minimality
over explicitly summable competitors.

## 3. Killing outside a near-contact set leaves no surviving inverse mass

Fix \(\varepsilon>0\). Define

\[
C_\varepsilon=\{q>0:3\nmid q,\ V(q)\le1+\varepsilon\},
\qquad
A_\varepsilon=\{q>0:3\nmid q,\ V(q)>1+\varepsilon\},
\tag{5}
\]

and the kernel killed on leaving the continuation set by

\[
(Q_\varepsilon f)(q)=
\mathbf1_{A_\varepsilon}(q)(Pf)(q).
\tag{6}
\]

Put \(f_n=Q_\varepsilon^nV\). Since \(Q_\varepsilon V\le V\),
positivity gives \(0\le f_{n+1}\le f_n\le V\). Its pointwise
limit \(\phi\) is finite. For each fixed target, the summands are
dominated by the finite parent series \(PV(q)\). Dominated convergence
therefore gives

\[
Q_\varepsilon\phi=\phi.
\tag{7}
\]

In particular \(\phi=0\) outside \(A_\varepsilon\); inside it,
\(P\phi=\phi\). Outside it, positivity gives \(P\phi\ge0=\phi\).
Thus \(\phi\) is subharmonic on the whole positive domain.

Choose \(\delta=\varepsilon/(1+\varepsilon)\). On
\(A_\varepsilon\),

\[
\delta\phi\le\delta V\le V-1=V-g,
\]

because \(V>1+\varepsilon\). Outside that set, \(\phi=0\)
and \(V\ge g\). The preceding lemma applies and proves

\[
\boxed{Q_\varepsilon^nV(q)\longrightarrow0
\quad\text{for every positive ordinary }q.}
\tag{8}
\]

This is more than the removal of a single inverse-ray atom: every
possible branching distribution of surviving mass that remains entirely
above the obstacle gap has vanished. The conclusion has no supplied
uniform rate in \(q\), \(\varepsilon\), or the depth \(n\).

## 4. Exact ordinary first-contact expansion

Let \(B_\varepsilon=\mathbf1_{C_\varepsilon}V\). On
\(A_\varepsilon\), (2) and \(V>1\) give \(PV=V\); at a
nonunit both sides of the desired identity are zero. Consequently

\[
V=B_\varepsilon+Q_\varepsilon V.
\]

Iterating, then using (8) and monotone convergence, gives

\[
\boxed{
V(q)=\sum_{j\ge0}(Q_\varepsilon^jB_\varepsilon)(q).
}\tag{9}
\]

Each term is a sum over actual inverse words whose first \(j\)
states are in \(A_\varepsilon\) and whose terminal state is in
\(C_\varepsilon\). If \(\mathcal H_\varepsilon(q)\) denotes
this first-contact word family, \(x_w\) its ordinary endpoint and
\(\omega_w=3^{|w|}2^{-A(w)}\), the expansion is

\[
\boxed{V(q)=\sum_{w\in\mathcal H_\varepsilon(q)}
\omega_wV(x_w).}\tag{10}
\]

The empty word is included when \(q\in C_\varepsilon\). A branch
ending at a nonunit contributes zero to (9), and is not included in
\(\mathcal H_\varepsilon(q)\).

For the unweighted terminal contact payoff put
\(J_\varepsilon(q)=\sum_{w\in\mathcal H_\varepsilon(q)}\omega_w\).
Every terminal value is between \(1\) and \(1+\varepsilon\), so

\[
\boxed{J_\varepsilon(q)\le V(q)
\le(1+\varepsilon)J_\varepsilon(q).}\tag{11}
\]

Thus \(J_\varepsilon(q)\to V(q)\) as \(\varepsilon\downarrow0\).
This is an actual positive-source first-entrance representation. It does
not replace words by independent random surrogate sources.

More generally, every \(P\)-harmonic function \(F\) satisfying
\(|F|\le cV\) is determined by its contact values:

\[
F(q)=\sum_{w\in\mathcal H_\varepsilon(q)}\omega_wF(x_w).
\tag{12}
\]

For a nonnegative \(F\), telescope as above and use
\(Q_\varepsilon^nF\le cQ_\varepsilon^nV\to0\). The signed
case follows from absolute domination. Formula (12) applies to \(G\)
and to every common critical Abel limit constructed in checkpoint 7.
It also gives uniqueness within this growth class once the contact
boundary values are specified.

### 4.1 An exact stopped V-Doob probability

On a positive unit \(q\in A_\varepsilon\), define transition
probabilities by

\[
\mathcal K_V(q,x)=\frac{\omega(q,x)V(x)}{V(q)}.
\tag{12a}
\]

These sum to one because \(PV(q)=V(q)\) on the continuation set.
At \(q\in C_\varepsilon\), make the state absorbing. This defines
a genuine stopped Markov chain on positive units; nonunit parents have
zero weight. Let \(\tau\) be its first contact time, including zero.
For every integer \(L\ge0\), pathwise cancellation gives

\[
\boxed{\Pr_q^V(\tau\ge L)=
\frac{Q_\varepsilon^LV(q)}{V(q)}.}\tag{12b}
\]

The index is intentional: \(\tau\ge L\) means that the first
\(L\) states \(X_0,\ldots,X_{L-1}\) remain in the continuation
set; the terminal state \(X_L\) may be a contact.

Put
\(F_L(q)=\sum_{0\le j<L}Q_\varepsilon^jB_\varepsilon(q)\) and
\(p_L(q)=\Pr_q^V(\tau<L)\). The finite entrance identity is exactly

\[
F_L(q)=V(q)p_L(q),\qquad
V(q)=F_L(q)+Q_\varepsilon^LV(q).
\tag{12c}
\]

Since \(B_\varepsilon\le(1+\varepsilon)1\) and
\(Q_\varepsilon\le P\), the supplied finite densities give the
explicit interface

\[
\boxed{\frac{V(q)}q\le
\frac{(1+\varepsilon)\sum_{j<L}D_j(q)}{q\,p_L(q)}
\quad\text{whenever }p_L(q)>0.}\tag{12d}
\]

The companion synthesis inserts its sharper finite-depth bound and
chooses a native logarithmic clock. Equation (12d) needs a lower bound
on the corresponding contact probability. Fixed-root convergence
\(p_L(q)\to1\) as \(L\to\infty\) gives no uniform bound when
both \(q\) and \(L=L(q)\) change. No such rate is asserted here.

## 5. The inverse Doob chain returns near the obstacle

On positive units define

\[
\mathcal K_G(q,x)=
\frac{\omega(q,x)G(x)}{G(q)}.
\tag{13}
\]

The actual parent weights are aggregated if needed; nonunits carry zero
mass. Harmonicity of \(G\) makes (13) stochastic. Let \(\tau\)
be the first entrance into \(C_\varepsilon\), including time zero.
Since \(R=V/G\ge1\), the exact change of measure gives

\[
\Pr_q^G(\tau\ge n)
\le\mathbb E_q^G[R(X_n)\mathbf1_{\tau\ge n}]
=\frac{Q_\varepsilon^nV(q)}{G(q)}\longrightarrow0.
\tag{14}
\]

The first contact is therefore almost surely finite. Restarting after
one step and using the Markov property proves infinitely many contacts
almost surely. This statement holds for every fixed ordinary unit
starting point, including points on a positive cycle.

There is a useful pathwise normalization. The process \(R(X_n)\) is
a bounded supermartingale, with

\[
1\le R\le2\kappa,\qquad
\mathbb E_q^GR(X_n)=P^nV(q)/G(q)\longrightarrow1.
\]

Hence \(R(X_n)\to1\) almost surely. Applying the contact recurrence
to the countable sequence \(\varepsilon=1/j\) yields

\[
\liminf_nV(X_n)=\liminf_nG(X_n)=1
\quad\text{almost surely}.\tag{15}
\]

For a nonperiodic odd root the inverse path has distinct states, hence
its ordinary height tends to infinity. For a periodic odd root, the
probability of staying on the reverse cycle for \(\ell\) full turns
is its multiplier \(\lambda^\ell\), where \(0<\lambda<1\).
It exits that cycle almost surely and then has distinct states. Thus a
consequence at every fixed positive odd unit root is

\[
\inf_{\substack{x\in\operatorname{Pred}(q)\ \text{odd unit}\\x\ge M}}
V(x)=1\qquad(M>0).\tag{16}
\]

This strengthens the component infimum normalization to arbitrarily
high ordinary ancestors in every fixed basin. It is still an inverse
statement and does not place a low-\(V\) value on a prescribed forward
orbit.

## 6. Exact remaining height and orientation issue

For a nonperiodic odd root, a source cannot occur at two different
inverse depths. Consequently the prefix-free first-contact word family
in (10) can be identified with distinct actual ordinary sources. Its
affine identity gives

\[
\frac{V(q)}q
=\sum_{w\in\mathcal H_\varepsilon(q)}
Z_w\frac{V(x_w)}{x_w},\qquad
Z_w=\frac{\omega_wx_w}{q}\in(0,1].
\tag{17}
\]

Thus a sufficient global upper estimate would be

\[
\sum_{w\in\mathcal H_\varepsilon(q)}\frac1{x_w}
\longrightarrow0
\quad\text{uniformly over large marked nonperiodic }q.
\tag{18}
\]

The known predecessor population bound gives a uniform finite bound on
such antichain reciprocal sums, not the vanishing required in (18).
At periodic roots, repeated words and their geometric weights must be
retained in (10); (17) cannot be rewritten as a distinct-source sum
without the corresponding cycle factor.

The entrance identity removes the residual inverse boundary term for
this particular contact set. It does not establish (18), a finite
height bound for the contact set, a uniform entrance time, or a uniform
bound on the contact tails as the marked target moves.

In particular an escaping ordinary source may follow an arbitrarily
long forward path outside \(C_\varepsilon\). The inverse Doob chain
started later on that path can hit a contact ancestor on a side branch.
Even when it hits a fixed contact ancestor on the same path, that
ancestor can remain a positive contribution at every later target.
Almost-sure inverse entrance therefore cannot be read as ordinary
forward absorption.

### 6.1 Why a finite-cylinder contact certificate is unavailable

There is a direct finite-word obstruction to approximating the contact
indicator from below pointwise by a nonzero ternary cylinder function.
Every unit cylinder contains a smaller cylinder on which all positive
ordinary values of \(V\) exceed any prescribed constant.

To see this, fix a unit cylinder modulo \(3^t\). The finite unit atom
floor supplies an inverse word \(w\) of some length \(r\ge t\)
whose forward affine map
\(F_w(z)=\omega_wz+\beta_w\) sends \(-1\) into that cylinder.
Indeed \(\omega_w\equiv0\pmod{3^r}\), so
\(F_w(-1)\equiv\beta_w\pmod{3^r}\), and a sufficiently deep
finite density is positive on every unit residue.

For \(k\ge0\), consider the smaller ternary cylinder

\[
\mathcal B_k=F_w(-1+3^{k+1}\mathbb Z_3).
\]

Every positive ordinary \(q\in\mathcal B_k\) has the legal
inverse prefix \(w\), ending at a positive odd integer
\(x\equiv-1\pmod{3^{k+1}}\). All intermediate parents are positive:
each legal inverse letter has the form \((2^e y-1)/3\) with
\(y>0\) and \(e\ge1\). Follow that prefix by \(k\) letters
\(e=1\). Their terminal residue is still \(-1\pmod3\), where
\(D_1=2\). Positivity of the finite word sum gives

\[
D_{r+k+1}(q)\ge2\omega_w(3/2)^k.
\]

The previously established \(D_j\le2V\) therefore yields

\[
\boxed{V(q)\ge\omega_w(3/2)^k
\quad\text{for every positive integer }q\in\mathcal B_k.}\tag{19}
\]

Choosing \(k\) large proves the claim. Thus no nonzero
finite-cylinder indicator supported on units is pointwise below
\(1_{C_\varepsilon}\) on the positive ordinary integers. A
finite-cylinder \(L^1\) approximation can still be useful, but passing
its errors through the discrete ordinary inverse kernel needs an
additional trace estimate. The mere existence of a Haar approximation
does not give the missing lower bound for \(p_{L(q)}(q)\).

This is a diagnosis of the direct finite-cylinder minorization route,
not a proof that all weighted counting approaches fail. The spikes in
(19) are also consistent with a sublinear upper bound at their actual
ordinary heights.

## 7. Formal and literature scope

`MinimalObstacle.lean` proves the abstract no-slack-subharmonic theorem,
its killed fixed-point specialization, and the countable-kernel
subtraction and summable-competitor justifications. The monotone killed limit, the entrance
series, and the probabilistic consequences above are written proofs;
they are not represented as Lean theorems in this module.

The general optimal-stopping interpretation is classical, not a novelty
claim. A primary author exposition is Yury Polyanskiy's
[Notes on optimal stopping of Markov processes](https://people.lids.mit.edu/yp/homepage/data/opt_stop.pdf),
Sections 1.2--1.6 and Theorem 6: bounded nonnegative payoffs have a least
excessive majorant and finite approximately optimal entrance times.
Here the normalized reward is \(g/G\), the Markov kernel is (13), and
the value is \(V/G\). The direct subtraction proof above establishes
the precise countable ordinary-kernel version used here, without
importing an unverified stochastic independence premise for a forward
Collatz orbit.
