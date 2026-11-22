# Actual moving ordinary fibres in Cesàro mean absolute error

**Status: source-qualified written theorem, not Lean formalized.** This note
combines an explicitly pinned ordinary-integer trace theorem with the
repository's actual contact laws. It proves a uniform, moving-clock
comparison for the joint real/ternary stationary law. It does not eliminate
the surviving positive escape amplitude. Section 8 identifies an explicit
persistent original-source submeasure, so that this distinction is visible
inside the theorem rather than left to interpretation.

## 1. Sources and normalization

The new external input is Lucas Valbuena, *A positive semicontinuous density
for the Syracuse stationary law*, at commit
`a7275d5a73814d3d9a400c6fe6577de9542b03a3` (2026-10-08):

- [Pinned TeX](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex).
- [Pinned raw TeX](https://raw.githubusercontent.com/x1xhlol/collatz-two-coordinate-obstruction/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex).

Its Corollary `cor:integer`, equation `eq:cesaro-absolute`, states, at
**every positive ordinary integer** (a),

\[
 \frac1R\sum_{j=0}^{R-1}|D_j(a)-h(a)|\longrightarrow0.
 \tag{1}
\]

Here this note calls the source's `rho_j` by `D_j` and its arithmetic `g`
by `h`. The source uses additive Haar probability on all of
\(\mathbb Z_3\), exactly the normalization here. Its proof first constructs
a lower semicontinuous density representative (E) satisfying (E(a)=h(a))
at every positive integer; lower semicontinuity gives
\(\liminf_j D_j(a)\ge h(a)\). Together with the source's signed Cesàro trace,
the identity
\(|D_j-h|=D_j+h-2\min(D_j,h)\) proves (1). This is a genuinely stronger
input than signed Cesàro convergence alone. Neither convergence at each
individual depth nor uniformity over ordinary integers is asserted.
The source's analytic/formal dependencies are retained as dependencies;
this note does not claim to have independently replayed them.

Repository inputs, all still source-qualified, are:

- PR176, `31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6`,
  `research/lean-global-resolvent-20261121/overview/literature/ABEL_CANONICAL_COMPARISON.md`,
  especially equations (1), (3), and (6): the least finite excessive
  envelope (V), its harmonicization (G), the positive atom floor
  \(\alpha\), and their comparisons with every finite density.
- PR180, `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
  `research/central-step-20261122/STOPPED_MIXING.md`, equations (1)--(10):
  the actual critical Doob law, finite common contact reference,
  original-label weights, and centered ordinary-clock identity.
  That note pins its underlying common-reference input to PR180
  `ab3973099f0d285bbe88972382ad599bb02cd460`,
  `research/lean-joint-20261122/ORDINARY_BOUNDARY.md`, B28--B37.
- The reciprocal-orbit product bound used only in Section 8 is the
  repository's existing constant \(\delta>0\), not an additional conclusion
  of the present trace theorem.

The fixed-integer fibre idea is also developed in
[LyapunovWeaver, *Geometry, integer fibres, and dyadic equidistribution of
the joint Collatz affine law*, v2](https://rstation.ai/problems/collatz/papers/19),
Section 9.2. The proof below derives its required fixed-root selection
statement directly from (1), so it does not import an almost-everywhere
disintegration at ordinary integer points.

## 2. Ordinary operator and a uniform comparison of full path laws

Let (U) be the accelerated odd Collatz map. Work on nonperiodic positive
odd ternary units, with forward transport killed when it first enters a
periodic orbit. A nonperiodic point may enter a cycle later. Every inverse
ancestor of a nonperiodic point is nonperiodic.

On all positive integers define

\[
 (Pf)(a)=\sum_{\substack{e\ge1\\2^e a\equiv1\pmod3}}
       \frac3{2^e}f\!\left(\frac{2^e a-1}{3}\right),
 \qquad D_j=P^j\mathbf1.
 \tag{2}
\]

The source trace is exactly this (D_j). One may verify this by successively
conditioning the first (j) affine digits of the stationary ternary
series. Its first-depth values are

\[
 D_1(a)=1\ (a\equiv1\bmod3),\quad
 D_1(a)=2\ (a\equiv2\bmod3),\quad
 D_1(a)=0\ (3\mid a).
 \tag{3}
\]

Reduce the atom-floor constant if necessary so that (0<\alpha\le1).
The pinned envelope comparison and (1) give

\[
 \alpha G\le\alpha V\le h\le2G\le2V,
 \qquad h\ge\alpha\text{ on units},\qquad h=0\text{ on nonunits}.
 \tag{4}
\]

Also (Ph=h). To see this without a hidden tail interchange, use
\(D_j\le2V\) for (j\ge1), (PV\le V<\infty), and apply dominated
convergence to the *Cesàro means* in the countable parent series.
The difference between the shifted and unshifted means is
\((D_{R+1}-D_1)/R\), which tends to zero at each fixed ordinary target.

Let (K_G,K_h) be the actual unit-parent kernels, and let
\(\mathbb P_a^G,\mathbb P_a^h\) denote their path laws:

\[
 K_G(a,x)=\frac3{2^e}\frac{G(x)}{G(a)},\qquad
 K_h(a,x)=\frac3{2^e}\frac{h(x)}{h(a)},\qquad Ux=a.
 \tag{5}
\]

Put (r=h/G\in[\alpha,2]). For every actual inverse prefix of length (j),
ending at (X_j), its probability ratio is exactly

\[
 \frac{\mathbb P_a^h[\text{prefix}]}{\mathbb P_a^G[\text{prefix}]}
   =\frac{r(X_j)}{r(a)}\in[\alpha/2,2/\alpha].
 \tag{6}
\]

These ratios form a bounded (\mathbb P_a^G)-martingale. Its (L^1) limit
defines the full-path Radon--Nikodym derivative and has the same bounds.
Agreement on finite cylinders identifies the measure with
\(\mathbb P_a^h\). In particular,

\[
 \boxed{\frac\alpha2\mathbb P_a^G\le\mathbb P_a^h
       \le\frac2\alpha\mathbb P_a^G},\qquad
 \boxed{\alpha G(a)\mathbb P_a^G
       \le h(a)\mathbb P_a^h\le2G(a)\mathbb P_a^G}.
 \tag{7}
\]

These are uniform in the ordinary root and hold for every path event,
including an almost surely finite stopping event. They do not identify
(h) with (G).

## 3. The one finite reference and all centered-clock shifts

Use (C_2=\{V\le2\}\) and first inverse contact, including time zero.
Write \(\tau\) for its depth and \(\mu_a^G,\mu_a^h\) for its endpoint laws.
The pinned input supplies a finite measure \(\sigma_*\) on ordinary contact
points and, for a fixed original source (p),

\[
 c_j=(j+1)^{-1/2}-(j+2)^{-1/2},\quad
 \kappa=3\delta/4,\quad
 C(p)=\frac1{\kappa c_{\ell(p)}\nu(p)}\le C_0p^{5/2},
 \tag{8}
\]

where \(\nu\) is the repository's ordinary harmonic weight and
\(\ell(p)\) counts strict future contacts. Every retained forward state
\(q_k=U^kp\) satisfies

\[
 \mu_{q_k}^G\le\delta^{-1}C(p)\sigma_*.
\]

Full-path comparison (7) proves, with one constant independent of (k),

\[
 \boxed{\mu_{q_k}^h\le M_p\sigma_*,\qquad
 M_p=\frac{2C(p)}{\alpha\delta}.}
 \tag{9}
\]

The contact time is finite (\mathbb P^h)-almost surely because it is finite
under (\mathbb P^G). There is no new stopping-time integrability assumption.

On each acyclic ordinary component choose an integer coordinate (c)
satisfying (c(Ux)=c(x)+1) on retained edges. If (X_\tau=x), then

\[
 \tau-k=d_p(x),\qquad d_p(x):=c(p)-c(x).
 \tag{10}
\]

The centered depth (d_p(x)) is allowed to be **negative**. At a particular
root it necessarily satisfies (d_p(x)\ge-k) on the support of the contact
law; it need not be nonnegative on the whole reference space.

Here is the averaging fact used throughout. Suppose nonnegative sequences
\(b_j(x)\le B\), (j\ge0), satisfy
\(R^{-1}\sum_{j<R}b_j(x)\to0\) at each ordinary endpoint. Define

\[
 Q_R^p[b](x)=\frac1R
   \sum_{r=\max(0,d_p(x))}^{R-1} b_{r-d_p(x)}(x)
   +B\frac{\min(R,(d_p(x))_+)}R,
 \tag{11}
\]

where an empty sum is zero. Then (Q_R^p[b](x)\to0) at every fixed (x)
and (0\le Q_R^p[b]\le B). For (d<0), the sum begins at index (-d);
for (d\ge0), at index zero with at most (d) omitted time slots. Both are
fixed shifts for that endpoint. Consequently

\[
 M_p\int Q_R^p[b],d\sigma_*\longrightarrow0.
 \tag{12}
\]

This is a dominated-convergence statement against one finite **ordinary**
reference measure, not a uniform Cesàro theorem over all integers.

## 4. Moving scalar densities: absolute error inside the average

Put

\[
 g=D_1/h,\quad 0\le g\le C_g:=2/\alpha,\quad
 K_h^jg=D_{j+1}/h,\quad B_g:=1+2/\alpha.
 \tag{13}
\]

In particular (e_j(x):=|K_h^jg(x)-1|\le B_g), and (1) gives
\(R^{-1}\sum_{j<R}e_j(x)\to0\) at every fixed ordinary endpoint.

**Theorem 1.** For each fixed original nonperiodic source (p),

\[
 \boxed{\lim_{R\to\infty}\sup_{k:\,q_k\text{ retained}}
 \frac1R\sum_{r=0}^{R-1}
 \left|\frac{D_{k+r+1}(q_k)}{h(q_k)}-1\right|=0.}
 \tag{14}
\]

**Proof.** At deterministic time (t=k+r), split the expectation of
\(g(X_t)-1\) into \(\tau>t\) and \(\tau\le t\). On the first event its
absolute value is at most (B_g). On the second, the strong Markov property
and (10) identify the remaining depth as (r-d_p(x)\ge0). Therefore

\[
 |K_h^{k+r}g(q_k)-1|
 \le B_g\Pr_{q_k}^h(\tau>k+r)
 +\int_{d_p(x)\le r}e_{r-d_p(x)}(x),d\mu_{q_k}^h(x).
 \tag{15}
\]

The event \(\tau>k+r\) is exactly \(d_p(X_\tau)>r\).
Average (15), use (9), and obtain the upper bound
\(M_p\int Q_R^p[e],d\sigma_*\). Equation (12) proves (14).
All conditional restarts are at \(\tau\) on the event \(\tau\le k+r\);
equivalently they use the bounded stop \(\tau\wedge(k+r)\).
No optional-stopping theorem at an uncontrolled unbounded horizon is used.
\(\square\)

With only signed Cesàro input the same proof yields the weaker absolute
value of the depth average. Equation (14) specifically uses the stronger
pinned source (1).

## 5. A bounded path-functional selection lemma

For any fixed root (x) and bounded measurable function (F) of its full
inverse path,

\[
 \frac1R\sum_{j=0}^{R-1}
  |\mathbb E_x^h[(g(X_j)-1)F]|\longrightarrow0.
 \tag{16}
\]

For a function (F_m) measurable through a fixed finite depth (m), use
the Markov property when (j\ge m):

\[
 |\mathbb E[(g(X_j)-1)F_m]|
 \le\mathbb E[|F_m|e_{j-m}(X_m)].
\]

Average and use the fixed-integer mean absolute trace and bounded
convergence over (X_m). General bounded (F) is approximated in (L^1)
by \(F_m=\mathbb E[F\mid X_0,\ldots,X_m]\); the error is bounded uniformly
in (j) by \(B_g\mathbb E|F-F_m|\).

If a family of such path functionals is compact in the sup norm, the mean
of the supremum of the absolute correlations also tends to zero. Indeed,
choose a finite \(\varepsilon\)-net, bound the supremum by the sum of the
finitely many net-point errors plus (B_g\varepsilon), apply (16), and
then let \(\varepsilon\downarrow0\). This is the uniformity needed below;
no unproved mixing rate is inserted.

## 6. Joint real fibres and exact terminal-digit bookkeeping

Let \(e_i\) be independent with \(\Pr(e_i=e)=2^{-e}\), and set

\[
 S_j=\sum_{i\le j}e_i,\quad A_j=3^j2^{-S_j},\quad
 B_j=\sum_{i=1}^j3^{i-1}2^{-S_i}.
 \tag{17}
\]

The same series has limits (R_0\in\mathbb R_+) and (Z\in\mathbb Z_3)
under this independent-digit law. Write \(\mathbf m\) for their joint law;
it is different from the repository's harmonic weight \(\nu\).
For each (0<\beta<1),

\[
 m_\beta:=\mathbb E R_0^\beta
 \le\frac1{2^{1+\beta}-1-3^\beta}<\infty.
 \tag{18}
\]

This follows by subadditivity of (t^\beta) and summing the geometric
series with ratio \(3^\beta/(2^{1+\beta}-1)<1\).

Under an actual inverse path from the ordinary root (a), (17) instead
describes its realized affine prefix and satisfies

\[
 a=B_j+A_jX_j,\qquad 0\le B_j\uparrow B_\infty\le a.
 \tag{19}
\]

Define \(\widehat\mu_a^h\) to be the law of \(B_\infty/a\) under
\(\mathbb P_a^h\). This is an actual, specified probability measure on
([0,1]) at every ordinary root. It is not a version of a conditional
probability defined only almost everywhere.

For depth (j\ge1), define a finite real measure

\[
 \Phi_j^a(f)=\frac{3^j}{h(a)}
   \mathbb E[f(R_0/a)\mathbf1_{\{Z\equiv a\ (3^j)\}}].
 \tag{20}
\]

It has mass \(D_j(a)/h(a)\); it is **not** separately normalized by
\(D_j(a)\). Let (d_{\rm BL}) be the bounded-Lipschitz metric on finite
measures on \(\mathbb R_+\), using tests \(\|f\|_\infty\le1\),
\(\operatorname{Lip}(f)\le1\).

Condition on exactly (t) affine digits, leaving **one terminal ternary
digit**. For each valid ordinary unit prefix (w), let (x_w) be its
endpoint, and (A_w,B_w) its affine coefficients. Independence of the
remaining joint pair \((R'_0,Z')\) gives the exact formula

\[
 \Phi_{t+1}^a(f)=\frac3{h(a)}\sum_{w}A_w
 \mathbb E\!\left[
 f((B_w+A_wR'_0)/a)\mathbf1_{\{Z'\equiv x_w\ (3)\}}
 \right].
 \tag{21}
\]

Nonunit endpoints contribute zero because (Z') is a ternary unit.
Replacing the real argument by (B_w/a) turns the right side into
\(\mathbb E_a^h[g(X_t)f(B_t/a)]\). Since
\(|f(u+z)-f(u)|\le2z^\beta\), the replacement error is at most

\[
 C_\beta\mathbb E_a^h X_t^{-\beta},\qquad
 C_\beta=6m_\beta/\alpha.
 \tag{22}
\]

Indeed the prefix probability under \(\mathbb P_a^h\) is
\(A_wh(x_w)/h(a)\); use (h(x_w)\ge\alpha) and
\(A_w/a\le1/x_w\), which follows from (19).
The final ternary digit is essential to this calculation. Dropping it
would replace the correct seed (D_1) by (D_0) and admit nonunit parents
in a unit-path argument.

## 7. Uniform moving joint-fibre convergence in mean BL distance

**Theorem 2.** For each fixed original source (p),

\[
 \boxed{\lim_{R\to\infty}\sup_{k:\,q_k\text{ retained}}
 \frac1R\sum_{r=0}^{R-1}
 d_{\rm BL}(\Phi_{k+r+1}^{q_k},\widehat\mu_{q_k}^h)=0.}
 \tag{23}
\]

This is a mean of per-depth distances, stronger than convergence of the
averaged measure alone. The ternary precision is (k+r+1), aligned to
the actual forward clock (k).

**Proof.** At a fixed ordinary root (x), put

\[
 a_j(x)=\mathbb E_x^h X_j^{-\beta},\qquad
 b_j(x)=\mathbb E_x^h[(B_\infty-B_j)/x],
\]

and

\[
 c_j(x)=\sup_{\substack{\|\varphi\|_\infty\le1\\
                     \operatorname{Lip}(\varphi)\le1}}
 |\mathbb E_x^h[(g(X_j)-1)\varphi(B_\infty/x)]|,
 \tag{24}
\]

where the functions in (24) are on ([0,1]). Actual inverse paths have
distinct positive integer states; a repeated state would make their
root periodic. Thus (X_j\to\infty) on every path, and bounded convergence
gives (a_j(x)\to0). Monotone convergence of (B_j\) gives (b_j(x)\to0).
The family of functions in (24) is compact in the sup norm, so Section 5
gives \(R^{-1}\sum_{j<R}c_j(x)\to0\).

Set

\[
 E_j(x)=C_\beta a_j(x)+C_g b_j(x)+c_j(x),\qquad
 B_*=C_\beta+C_g+B_g.
 \tag{25}
\]

Then (0\le E_j\le B_*) and its Cesàro mean tends to zero at every fixed
ordinary endpoint.

We claim the precise stopped inequality

\[
 d_{\rm BL}(\Phi_{k+r+1}^{q_k},\widehat\mu_{q_k}^h)
 \le B_*\Pr_{q_k}^h(\tau>k+r)
  +\int_{d_p(x)\le r}E_{r-d_p(x)}(x),d\mu_{q_k}^h(x).
 \tag{26}
\]

To prove it, decompose each test-function error into (22), the error from
replacing (B_t) by (B_\infty), and the bounded selection correlation
\(\mathbb E[(g(X_t)-1)f(B_\infty/q_k)]\), with (t=k+r).
On \(\tau>t\), these three errors are bounded respectively by
(C_\beta,C_g,B_g), times the event probability.

On \(\tau\le t\), condition on the entire prefix through contact and write
(x=X_\tau), (s=t-\tau=r-d_p(x)\). For the first error the remaining state
is exactly the inverse state at depth (s) from (x). For the second,
affine composition and (19) give

\[
 \frac{B_\infty-B_t}{q_k}
 =\frac{A_\tau}{q_k}(B_\infty^x-B_s^x)
 \le\frac{B_\infty^x-B_s^x}{x}.
 \tag{27}
\]

The coefficient estimate \(A_\tau/q_k\le1/x\) holds for every actual
prefix individually. It is not an average estimate at a moving integer.
For the selection term put (u=B_\tau/q_k\in[0,1]). Then

\[
 B_\infty/q_k=u+(1-u)B_\infty^x/x.
\]

The function \(\varphi(v)=f(u+(1-u)v)\) belongs to the very same bounded
Lipschitz unit ball on ([0,1]), whatever the prefix and the moving root.
Consequently its correlation is bounded by (c_s(x)). These statements
give (26), uniformly over all allowed test functions.

Average (26) and apply (9)--(12) with (b=E\), (B=B_*). The bound is

\[
 \frac1R\sum_{r<R}
 d_{\rm BL}(\Phi_{k+r+1}^{q_k},\widehat\mu_{q_k}^h)
 \le M_p\int Q_R^p[E],d\sigma_*\longrightarrow0,
 \tag{28}
\]

independently of (k). This proves (23). \(\square\)

### Original labels and unchanged weights

Take the existing label (n), original weight (w_n=n^{-4}), and projected
root (p_n\le2n). Let (I_k) retain precisely the labels not yet killed
at clock (k). The one measure on label/endpoint pairs

\[
 \Xi_h(n,x)=w_nM_{p_n}\sigma_*(x)
 \mathbf1_{\{x\in\operatorname{Comp}(p_n)\}}
 \tag{29}
\]

is finite because (M_{p_n}\le\mathrm{const}\,n^{5/2}\).
Apply bounded convergence to (11) on these pairs, with the shift
\(d_{p_n}(x)\) for each pair. Both the scalar and joint conclusions extend
to

\[
 \lim_{R\to\infty}\sup_k\sum_{n\in I_k}w_n\,
 \frac1R\sum_{r<R}
 d_{\rm BL}(\Phi_{k+r+1}^{q_{n,k}},\widehat\mu_{q_{n,k}}^h)=0
 \tag{30}
\]

and the analogous sum of scalar absolute errors. Colliding labels are
added with their original weights. No new source distribution appears.

## 8. The original source contributes a persistent positive submeasure

This theorem controls the trace error; it does not make its limiting
ordinary fibre small. Here is the exact mass that survives on an escaping
original path.

For an actual retained forward prefix (p=q_0,\ldots,q_k), let

\[
 a_k=\prod_{i<k}\frac3{2^{v_2(3q_i+1)}},\quad
 b_k=q_k-a_kp,\quad
 \lambda_k=\frac{a_kp}{q_k}
   =\prod_{i<k}\frac{3q_i}{3q_i+1}.
 \tag{31}
\]

The inverse prefix from (q_k) back to the **same original point (p)**
has exact (\mathbb P^h)-probability (a_kh(p)/h(q_k)). Once it is
traversed, the continuation is \(\mathbb P_p^h\). Therefore, as nonnegative
measures on ([0,1]),

\[
 \boxed{\frac{h(q_k)}{q_k}\widehat\mu_{q_k}^h
 \ \ge\ \lambda_k\frac{h(p)}p
       (\psi_{\lambda_k})_*\widehat\mu_p^h,\qquad
 \psi_\lambda(t)=1-\lambda+\lambda t.}
 \tag{32}
\]

In particular \(h(q_k)/q_k\ge\lambda_kh(p)/p\).
Under the pinned reciprocal-orbit product bound, an escaping retained
orbit has \(\lambda_k\downarrow\lambda_\infty\ge\delta>0\). For every
nonnegative bounded continuous (f), (32) yields

\[
 \liminf_{k\to\infty}\frac{h(q_k)}{q_k}
        \widehat\mu_{q_k}^h(f)
 \ge\lambda_\infty\frac{h(p)}p
   \int f(1-\lambda_\infty+\lambda_\infty t)
          \,d\widehat\mu_p^h(t).
 \tag{33}
\]

For (f=1) the right side is at least \(\delta h(p)/p>0\).
This is a lower bound conditional on escape, not a construction of an
escaping orbit. It explicitly retains the original atom that a closing
estimate must rule out.

Finally (7), pushed through the real-limit map, gives

\[
 \alpha G(a)\widehat\mu_a^G
       \le h(a)\widehat\mu_a^h
       \le2G(a)\widehat\mu_a^G.
 \tag{34}
\]

Thus the new trace limit is uniformly comparable with the canonical
ordinary fibre used in the repository. Equation (34) is a comparison,
not a proof that those two fibres or amplitudes are identical.

## 9. What has been discharged, and the exact remaining estimate

The imported ordinary fixed-integer trace can now be applied at the actual
moving forward roots, with absolute error inside the depth average and
with one finite reference retaining every original label. The real
coordinate is controlled at the same moving roots by (23), including the
real normalization factor in (27). This pays an actual centered-clock
comparison that an almost-everywhere fibre theorem alone does not pay.

There is no quantitative rate in (14), (23), or (30). Their precision is
\(k+r+1\); a finite-floor certificate whose admissible depth remains fixed
as (k\to\infty) cannot be inserted. Most importantly, (32) survives the
new limiting operation. To exclude escape one still needs a genuinely
vanishing amplitude estimate, such as (h(q_k)/q_k\to0\) on every possible
retained escaping source, or a sibling-loss comparison forcing that
conclusion. Uniform Cesàro trace convergence itself provides neither.

The theorem also does not assert absolute continuity, a Frostman bound,
or a dimension estimate for \(\widehat\mu_a^h\) at an ordinary integer.
Any such additional property must be proved for these actual path-law
fibres; an almost-everywhere disintegration of the joint stationary law
does not cover this countable exceptional set automatically.
