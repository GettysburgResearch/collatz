# Coherent affine charts, the actual real boundary, and a routing test

Date: 2026-11-23.

**Status: SOURCE-QUALIFIED written deductions and a direct closing attempt
that remains incomplete.** The preceding parameter experiment varied an edge
multiplier while holding the integer orbit fixed. This pass instead deforms
the entire actual affine orbit coherently, constructs its common real
boundary, and identifies that boundary with the normalized inverse fibres
used by the latest entropy attack. The resulting representation is exact.

Under the separately identified routing input, the support of this boundary
law has Hausdorff dimension one. This does **not** establish dimension one
for the canonical probability law or for the actual ternary time law. The
attempted change of measure retains an explicit original-root cost, given
below. Neither escape nor nontrivial positive cycles are excluded.

## 1. Exact inputs and normalization

Let

\[
 U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1),
 \qquad \lambda(n)=\frac{3n}{3n+1}.
 \tag{1}
\]

Fix a hypothetical escaping component \(E\) of positive odd ternary units.
All its vertices and inverse parents are nonperiodic. Every two vertices
have eventually coalescing forward orbits. The graph and every finite
path below consist of the supplied ordinary integers; no freely chosen
valuation sequence is substituted for them.

The inherited analytic inputs are

\[
 L\nu=\nu,\quad h=L(\lambda h),\quad
 0<\delta\nu\le h\le\nu\le M,\quad \nu(n)\ge\gamma/n,
 \tag{2}
\]

where \(\delta,\gamma>0\), \(h=G/n\), and \(L\) is ordinary inverse
counting. The canonical ordinary inverse kernel is

\[
 K(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)}.
 \tag{3}
\]

The distinct-state path count and its reciprocal consequence are

\[
 \#\{n\text{ on a finite actual path}:n\le X\}\le5X^{39/40},
 \qquad
 \sum_{n\text{ on a path},\ n\ge m}\frac1n\le200m^{-1/40}.
 \tag{4}
\]

The second bound also applies to a subset of a path; the version needed
below is a whole path whose states exceed \(m\). Increasing finite path
segments supplies the same bounds on two-sided paths. In particular
\(\delta=e^{-200/3}\) is a valid common lower bound for all retained
products of \(\lambda\).

Use the integer component clock \(\ell(Un)=\ell(n)+1\). Its stationary
level mass is \(c_E>0\), and the probability law \(\Pi_E\) on two-sided
actual paths \((Q_r)_{r\in\mathbb Z}\), with \(\ell(Q_r)=r\), satisfies

\[
 \Pi_E(Q_r=n)=\nu(n)/c_E,\qquad
 \nu(U^kq)\uparrow c_E.
 \tag{5}
\]

Its forward motion is deterministic and its inverse motion uses (3).
Write

\[
 D_E=\sum_{n\in E}(1-\lambda(n))h(n),\qquad F_E=D_E/c_E.
 \tag{6}
\]

The frozen sources are:

| Source | Location and use |
|---|---|
| PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2` | `research/retained-source-attacks-20261122/CANONICAL_CHARGE.md`, (1)--(5), (12)--(20): canonical functions, actual whole-path law, physical path products, and the boundary value \(c_E-D_E\). |
| PR180, same SHA | `research/retained-source-attacks-20261122/ANALYTIC_PARAMETER.md`, Sections 2--4: the previous distinct parameter families. No identification of those families is reused. |
| PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6` | `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, Sections 1--2: (2)--(4), including \(G\ge\gamma\) and hence \(\nu(n)\ge\gamma/n\). |
| PR178, `7e4569476e152f6b8537bdc1711df595ec1ffd89` | `research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md`, Sections 2--6: exact spine retracing and the specified normalized real fibre for the comparable critical trace \(h_{\rm tr}\). |
| PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2` | `research/retained-source-attacks-20261122/SIBLING_MASS.md`, (S2)--(S5): the source-qualified Paper 37 v4 count and its complete ordinary-legality consumer. Used only in Section 6. |

The population, finite-envelope, trace and recent-manuscript qualifications
of these sources remain in force. The new infinite conclusions below are
written arguments, not Lean axioms or kernel-checked analytic theorems.

## 2. A rational affine coordinate on the entire actual component

Choose a reference \(q_0\in E\). There is a unique positive function
\(\chi:E\to\mathbb Q_{>0}\), normalized by \(\chi(q_0)=1\), with

\[
 \chi(Un)=\frac3{2^{a(n)}}\chi(n).
 \tag{7}
\]

To construct it at \(n\), choose an actual meeting
\(U^r n=U^kq_0\) and transport the multiplier along those two finite
paths. Continuing past a meeting changes both sides by the same
multiplier, so the result is independent of the meeting. Equivalently,
the undirected component is a tree: an undirected finite cycle in an
out-degree-one graph would force a directed cycle. Thus the transport
has no holonomy. In particular

\[
 \chi(n)=2^{d(n)}3^{\ell(n)},\qquad d(n)\in\mathbb Z,
 \tag{8}
\]

after shifting the clock so \(\ell(q_0)=0\).

Define the rational coordinate

\[
 y(n)=\frac n{\chi(n)}.
\]

The literal edge relation gives two exact formulas:

\[
 \boxed{y(Un)-y(n)=\frac1{3\chi(n)},\qquad
         \lambda(n)=\frac{y(n)}{y(Un)}.}
 \tag{9}
\]

Therefore \(y\) increases strictly on every forward orbit. The product
bound from (4) gives a finite positive limit

\[
 b_E:=\lim_{k\to\infty}y(U^k n),\qquad
 \frac{y(n)}{b_E}=\prod_{k\ge0}\lambda(U^kn)\in[\delta,1).
 \tag{10}
\]

Coalescence makes \(b_E\) independent of \(n\). Put

\[
 a_E=\inf_{n\in E}y(n).
 \tag{11}
\]

Then \(0<\delta b_E\le a_E<b_E\). The infimum is not attained:
each positive odd unit has infinitely many legal unit parents, and
every parent has a strictly smaller \(y\)-coordinate by (9).

This coordinate is injective on \(E\). If \(y(n)=y(m)\), (8) says
that \(n/m\) is a product of integer powers of 2 and 3. Both integers
are positive and coprime to 6, so unique factorization gives \(n=m\).
This observation does not bound the separation of the rational
coordinates: the exponents in (8) retain the complete orbit clock.

On a two-sided path define

\[
 Z=\lim_{r\to-\infty}y(Q_r).
 \tag{12}
\]

Monotonicity gives \(a_E\le Z<b_E\), and the full path product is

\[
 \prod_{r\in\mathbb Z}\lambda(Q_r)=\frac Z{b_E}.
 \tag{13}
\]

Let \(\mu_E\) be the distribution of \(Z\) under \(\Pi_E\), and
\(s_E=\mathbb E_{\Pi_E}Z\). The previous physical boundary identity
therefore becomes

\[
 \boxed{F_E=1-\frac{s_E}{b_E}.}
 \tag{14}
\]

## 3. Exact support of the actual real boundary

The support is not an unspecified abstract inverse boundary:

\[
 \boxed{\operatorname{supp}\mu_E
        =\overline{\{y(n):n\in E\}}.}
 \tag{15}
\]

One inclusion follows at once from (12). For the other, fix an actual
vertex \(q\) and \(\varepsilon>0\). A legal unit parent
\(p=I_e(q)\) satisfies

\[
 \chi(p)=\frac{2^e}3\chi(q),\qquad
 y(p)=y(q)-\frac1{2^e\chi(q)}.
 \tag{16}
\]

There are arbitrarily large such exponents. Fix a large integer \(M_1\).
Only finitely many of these parent cones can contain an integer at most
\(M_1\). Indeed, each such integer has one deterministic route to \(q\)
and, if that route is nonempty, one last parent of \(q\). The root
\(q\) itself lies in no parent cone because its orbit is nonperiodic.
Avoid these finitely many parents, and choose a remaining exponent so
large that \(y(q)-y(p)<\varepsilon/2\). Every state in the complete
inverse cone of \(p\) is then greater than \(M_1\).

On every whole path through \(p\), (4) and (9) imply

\[
 y(p)\exp\!\left(-\frac{200}{3}M_1^{-1/40}\right)
 \le Z<y(p)<y(q).
 \tag{17}
\]

Choose \(M_1\) first so the exponential loss is less than
\(\varepsilon/2\). The event that the path passes through \(p\) has
the strictly positive probability \(\nu(p)/c_E\), by (5). Thus every
neighborhood of \(y(q)\) has positive \(\mu_E\)-mass. This proves
(15) without replacing the canonical law by an independent word law.

The set in (15) is compact and perfect. Formula (16) approximates
every \(y(q)\) from below by distinct actual-parent coordinates; limits
of those coordinates cannot introduce isolated points. Its endpoints
are \(a_E\) and \(b_E\). In particular \(Z\) is nonconstant and

\[
 \boxed{a_E<s_E<b_E,\qquad \operatorname{Var}_{\Pi_E}(Z)>0.}
 \tag{18}
\]

This is a support statement. It does not yet imply absolute continuity,
nonatomicity, or positive entropy for \(\mu_E\).

## 4. Identifying the newest normalized real fibres

Condition \(\Pi_E\) on passing through a fixed vertex \(q\). Its
inverse path is exactly (3); denote this conditional law by \(\Pi_q\).
From the canonical inverse-product representation of \(h\),

\[
 \boxed{\mathbb E_{\Pi_q}Z
          =y(q)\frac{h(q)}{\nu(q)}=:s(q).}
 \tag{19}
\]

For an actual inverse prefix ending at \(x\), write its forward affine
map as \(q=\omega x+\beta\). Its multiplier is
\(\omega=\chi(q)/\chi(x)\), so

\[
 \boxed{\frac\beta q=1-\frac{y(x)}{y(q)}.}
 \tag{20}
\]

As the inverse prefix increases, the normalized real intercept therefore
tends to \(1-Z/y(q)\). This is the actual affine intercept of the
same ordinary inverse path, including every division.

The critical inverse kernel for \(G\) is

\[
 K_h(q,n)=\mathbf1_{Un=q}\lambda(n)\frac{h(n)}{h(q)}.
 \tag{21}
\]

On the finite prefix ending at \(x\), its likelihood ratio relative to
\(K\) telescopes, using (9) and (19), to

\[
 \frac{y(x)}{y(q)}
 \frac{h(x)/\nu(x)}{h(q)/\nu(q)}=\frac{s(x)}{s(q)}.
 \tag{22}
\]

The numerator is the conditional expectation of \(Z\) given this
inverse prefix. The bounded martingale converges to \(Z\), which is
measurable from the full inverse path. Since \(Z\ge a_E>0\), the
infinite change of measure is uniformly bounded above and below:

\[
 \boxed{\frac{d\Pi_q^h}{d\Pi_q}=\frac Z{s(q)}.}
 \tag{23}
\]

Along \(q_k=U^kq_0\), the conditioning event in (5) has probability
tending to one. Thus \(\Pi_{q_k}\) converges in total variation, when
viewed on whole paths by adjoining the deterministic future, to
\(\Pi_E\). Also \(y(q_k)\to b_E\) and \(s(q_k)\to s_E\). Equations
(20)--(23) identify the common normalized real fibre:

\[
 \boxed{\widehat\mu_\infty^G
   =\operatorname{Law}\left(1-Z/b_E\right)
        \text{ under }\frac Z{s_E}\,d\Pi_E.}
 \tag{24}
\]

The convergence after the varying affine rescaling is weak (for example
in bounded-Lipschitz distance). No total-variation convergence of those
rescaled real pushforwards is asserted.

Two exact consumers of this identification are

\[
 \boxed{
 F_E=1-\left(\int\frac{d\widehat\mu_\infty^G(t)}{1-t}\right)^{-1},
 \qquad
 F_E-\int t\,d\widehat\mu_\infty^G(t)
       =\frac{\operatorname{Var}(Z)}{b_Es_E}>0.}
 \tag{25}
\]

The integrals are finite because \(Z\ge a_E\ge\delta b_E\). To check
the algebra, the first integral is \(b_E/s_E\). The second mean is
\(1-\mathbb EZ^2/(b_Es_E)\), and subtracting it from (14) yields the
displayed variance. The canonical escape charge is therefore recoverable
from this specific actual fibre, not merely comparable to an unspecified
real moment.

### Keeping the PR178 trace law distinct

PR178's Section 6 uses the different critically harmonic function
\(h_{\rm tr}\), with \(\eta G\le h_{\rm tr}\le2G\) for a fixed
\(\eta>0\). Put \(u_{\rm tr}=h_{\rm tr}/n\) and
\(w=u_{\rm tr}/h\). Then \(\eta\le w\le2\), and \(w\) is harmonic
for (21). Its inverse-path martingale has a bounded positive terminal
value \(W\in[\eta,2]\). The full trace path law is consequently the
additional tilt by \(W\). On the component, the limit in PR178 is

\[
 \widehat\mu_\infty^{\rm tr}
  =\operatorname{Law}(1-Z/b_E)
       \text{ under }\frac{ZW}{\mathbb E(ZW)}\,d\Pi_E.
 \tag{26}
\]

One can construct \(W\) on the whole path by the bounded martingale
\(w(Q_{-r})\) under the \(Z/s_E\)-tilted law. Its conditional future
identities give exactly the finite trace kernels; the mass of paths not
through \(q_k\) tends to zero under the bounded tilt. This verifies the
component limit in (26).

In particular, the two real limiting laws are mutually absolutely
continuous with Radon--Nikodym ratio between \(\eta/2\) and
\(2/\eta\). They have the same support,

\[
 \overline{\{1-y(n)/b_E:n\in E\}}\subset[0,1-a_E/b_E].
 \tag{27}
\]

They are not asserted equal. Formula (25) is for the \(G\)-law;
dropping \(W\) from the trace law would be an unjustified substitution.

## 5. The coherent deformation and its exact arithmetic domain

For a real parameter \(t\), deform every vertex by

\[
 x_t(n)=n+t\chi(n)=\chi(n)(y(n)+t).
 \tag{28}
\]

Equations (1) and (7) give, at every actual edge,

\[
 3x_t(n)+1=2^{a(n)}x_t(Un).
 \tag{29}
\]

Thus this deformation preserves the entire affine path, rather than
assigning unrelated parameters to its edges. All real vertices remain
positive exactly when \(t\ge-a_E\), since the infimum in (11) is
unattained. For \(t>-a_E\), define

\[
 \lambda_t(n)=\frac{3x_t(n)}{3x_t(n)+1}
             =\frac{y(n)+t}{y(Un)+t}.
 \tag{30}
\]

Its actual whole-path product telescopes to \((Z+t)/(b_E+t)\).
The harmonic family on this same labelled graph and its component
boundary are therefore explicitly

\[
 \boxed{
 h_t(q)=\frac{y(q)h(q)+t\nu(q)}{y(q)+t},\qquad
 C_E(t)=c_E\frac{s_E+t}{b_E+t}.}
 \tag{31}
\]

The first formula is the conditional inverse-product expectation;
it obeys \(h_t=L(\lambda_t h_t)\). The second follows from (5) and
(19). At \(t=0\), this is exactly the original \(h\) and its boundary
\(c_E-D_E\). Its loss is

\[
 c_E-C_E(t)=\frac{b_ED_E}{b_E+t}>0.
 \tag{32}
\]

The unique zero of the meromorphic boundary in (31) is \(-s_E\).
By (18), \(-s_E<-a_E\), outside the whole-component positivity range.
Even at the positive-real endpoint \(t=-a_E\), its boundary is
\(c_E(s_E-a_E)/(b_E-a_E)>0\). Thus this linked family cannot erase
the escaping boundary while keeping all its real vertices positive.

The information profile also has an explicit form. Let
\(d\Pi_{E,t}=(Z+t)/(s_E+t)\,d\Pi_E\). In the orientation from the
original law to this tilted law,

\[
 \mathcal I_E(t)=c_ED_{\rm KL}(\Pi_E\Vert\Pi_{E,t})
 =c_E\left(\log(s_E+t)-\mathbb E\log(Z+t)\right)>0
 \quad(t>-a_E),
 \tag{33}
\]

with

\[
 \frac{\mathcal I'_E(t)}{c_E}
 =\frac1{s_E+t}-\int\frac{d\mu_E(z)}{z+t}<0,
 \qquad
 \mathcal I_E(t)=\frac{c_E\operatorname{Var}(Z)}{2t^2}+O(t^{-3}).
 \tag{34}
\]

Compact support justifies differentiation and the expansion; strictness
uses (18). The Stieltjes integral here is displayed explicitly, so no
representation theorem is being imported to manufacture positivity.

### Ordinary integrality leaves only the original parameter

Suppose even one entire forward shadow from \(q_0\) consists of
integers. At its initial vertex, \(x_t(q_0)=q_0+t\) implies
\(t\in\mathbb Z\). If
\(A_k=\sum_{j<k}a(U^jq_0)\), then

\[
 \chi(U^kq_0)=3^k/2^{A_k}.
\]

Integrality at clock \(k\) forces \(2^{A_k}\mid t\), since
\(3^k\) is odd. Each gap is positive, so \(A_k\ge k\). Hence

\[
 \boxed{x_t(U^kq_0)\in\mathbb Z\ \text{for every }k\ge0
        \quad\Longrightarrow\quad t=0.}
 \tag{35}
\]

This is stronger than needing two-sided integrality. On a finite
forward prefix through clock \(k\), integrality is exactly
\(t\in2^{A_k}\mathbb Z\). Requiring all displayed states to remain
odd strengthens it to \(t\in2^{A_k+1}\mathbb Z\); positivity is an
additional real inequality. The lattice spacing grows with the original
clock instead of producing nearby analytic samples.

Changing the reference vertex only rescales \(\chi\) by a positive
rational constant and rescales \(t\) inversely. Two ordinary source
charts in \(E\) coalesce at an actual common future. A deformation
which agrees with that unchanged future has zero parameter there, and
therefore zero parameter in both charts. Coalescence supplies a
consistent chart, but no second ordinary interpolation value.

## 6. A stronger support theorem from actual routing

This section uses one extra recent-manuscript input, with its status
kept separate from Sections 2--5. Paper 37, version 4, Lemma 11,
equation (143), together with its legal inverse consumer (145)--(146),
supplies constants \(c_0,F,b_*>0\) such that, for every sufficiently
large block length \(b\), every positive odd unit root has at least

\[
 R_b:=\left\lfloor\frac{c_0}{3\sqrt b}(4/3)^b\right\rfloor
 \tag{36}
\]

distinct legal unit inverse endpoints, reached in exactly \(b\) odd
steps with total valuation \(2b\) and real forward offset
\(0\le\beta\le F\). Use extra precision \(k=1\) and one prescribed
unit endpoint class; this is why the factor 3 appears and why final
unit legality is retained. The constants are fixed while \(b\)
increases. The source-independent count, not mere route existence,
is essential.

Fix a large \(b\) with \(2\le R_b<X:=(4/3)^b\), and choose an
actual root \(q\in E\) so large that

\[
 q>\frac F{1-X^{-1}}.
 \tag{37}
\]

Such roots occur on the hypothesized escaping orbit. At every selected
endpoint choose exactly \(R_b\) of the available routes and repeat.
This defines a tree of genuine ordinary inverse paths. At block depth
\(j\), all endpoints \(n\) have

\[
 \chi(n)=X^j\chi(q),\qquad n\le X^jq,
\]

and different routes have different endpoints: deterministic forward
motion recovers their full valuation words at this common depth.
Their \(y\)-coordinates are separated by at least
\(1/(X^j\chi(q))\). Every infinite continuation from such an endpoint
has its boundary in

\[
 \left[y(n)-\frac{C_F}{X^j\chi(q)},\ y(n)\right],
 \qquad C_F=\frac F{1-X^{-1}}.
 \tag{38}
\]

Indeed, each block changes \(y\) by \(-\beta/\chi(\text{root})\),
and its future changes sum to the geometric bound (38). Condition
(37) also shows directly that these boundary values stay positive.

Assign the uniform choice among the \(R_b\) branches at each block.
Every inverse **path cylinder** at depth \(j\) has probability
\(R_b^{-j}\). Its image under the boundary map can overlap the images
of other cylinders; no injectivity of that map is needed. Write
\(\sigma_b\) for the boundary pushforward. An interval of length
\(\varepsilon\) meets at
most \(\varepsilon X^j\chi(q)+C_F+2\) of the intervals (38), by
the common endpoint spacing. Choose \(j\) so
\(1\le\varepsilon X^j\chi(q)<X\), for sufficiently small positive
\(\varepsilon\), so \(j\ge0\). The preimage of the interval is
contained in the union of the corresponding path cylinders. Summing
their probabilities gives

\[
 \sigma_b(I)\le C_b|I|^{d_b},\qquad
 d_b=\frac{\log R_b}{\log X}.
 \tag{39}
\]

All constants may depend on this fixed block and root; enlarging the
constant covers larger intervals. For any interval
cover of the support, (39) implies
\(1\le C_b\sum_I|I|^{d_b}\), so its Hausdorff dimension is at least
\(d_b\). Every path used is an actual inverse path in \(E\), hence
its boundary belongs to (15). Finally \(d_b\to1\) as \(b\to\infty\).
Thus

\[
 \boxed{\dim_H\operatorname{supp}\mu_E=1.}
 \tag{40}
\]

The same holds for the supports of both actual normalized fibre limits
in (24) and (26), by affine rescaling and their positive bounded tilts.
No claim of positive Lebesgue measure is made.

### The attempted canonical-measure upgrade retains its source cost

The natural closing attempt is to transfer the auxiliary full-dimension
construction to the canonical probability law. Its exact finite cost is
computable. Let \(\mathsf S_j\) be the uniform law on the \(R_b^j\)
selected complete inverse words, and \(\mathsf K_{q,jb}\) the actual
canonical \(K\)-law at root \(q\). Each selected endpoint obeys

\[
 \mathsf K_{q,jb}(\text{its complete word})
  =\frac{\nu(n)}{\nu(q)}
  \ge\frac\gamma{X^jq\nu(q)}.
\]

Consequently

\[
 \boxed{
 D_{\rm KL}(\mathsf S_j\Vert\mathsf K_{q,jb})
 \le \log\frac{q\nu(q)}\gamma+j\log\frac X{R_b}.}
 \tag{41}
\]

The block contribution per odd step tends to zero as \(b\to\infty\),
but the first term retains the supplied original root. The directly
available mass lower bound on the whole selected depth-\(j\) family is

\[
 \mathsf K_{q,jb}(\text{selected})
 \ge \frac\gamma{q\nu(q)}\left(\frac{R_b}X\right)^j.
 \tag{42}
\]

Since \(R_b<X\), this lower bound tends to zero. It is not an upper
bound and does not prove that the selected infinite tree is null. It
does show why the present calculation supplies neither absolute
continuity of \(\sigma_b\) with respect to the canonical boundary
law nor a positive canonical mass of its high-dimension set.

At the moving escaping root \(q_N\), \(\nu(q_N)\to c_E>0\), so
the initial term in (41) is \(\log q_N+O(1)\). The latest exact
retracing theorems force the canonical law to follow the original
spine with probability tending to one at horizons before the
original-source clock. Equations (41)--(42) do not contradict that
fact: they have no bound strong enough to remove the original-root
cost at those horizons. The support theorem cannot be relabeled as an
entropy lower bound for that same time ensemble.

There is also a sharp limit to the proposed near-diagonal route.
For every actual finite inverse word ending at \(n\) from root \(q\),
the retained product bound gives

\[
 \frac\beta q=1-\frac{y(n)}{y(q)}\le1-\delta.
 \tag{43}
\]

Thus attempting to force \(a_E=0\) merely from the complete ordinary
inverse tree would contradict an already available bound for each
of its finite paths, including known convergent predecessor trees.
The routing count with \(\beta\le F\) instead places substantial
support near the *upper* \(y\)-boundary. A new use of escape-specific
arithmetic would be needed to obtain the missing incompatible property.

## 7. Outcome and remaining step

The coherent coordinate gives one exact representation of the actual
component, the canonical whole-path boundary, and the latest real-fibre
limit. The charge is reconstructed by (25); the trace law is connected
by the explicit bounded tilt (26). Under the specified routing input,
their common support has Hausdorff dimension one by a construction
using only actual legal integer inverse paths.

The attempted completion fails at a concrete measure comparison.
Full-dimensional support and high-dimension auxiliary inverse laws do
not supply an entropy lower bound for the canonical time ensemble;
(41) retains \(\log(q\nu(q)/\gamma)\). The coherent analytic family
also supplies no independent ordinary sample: (35) leaves only the
original parameter. No bound erasing that root cost, canonical
absolute-continuity theorem, or global source descent was obtained.

## Primary literature inspected

1. Lyapunov Weaver, *Almost linear valuation budgets for pointwise
   modular routing in Collatz inverse trees*, Paper 37, **version 4**,
   27 October 2026, Lemma 11 and Theorem D. The current primary page
   identifies version 4, and the exact version download is
   <https://rstation.ai/api/v1/papers/collatz_37/versions/4/download>.
   Page: <https://rstation.ai/problems/collatz/papers/37>.
   Only the stated count and ordinary consumer are used; its deep
   analytic proof is not independently reconstructed here.
2. NIST DLMF, Section 1.14(vi), Stieltjes transform and differentiation,
   <https://dlmf.nist.gov/1.14>. This supplies terminology and a primary
   reference for the displayed integral in (34). The note proves its
   required compact-support differentiation directly and uses no
   unverified analytic-continuation or inversion premise.
