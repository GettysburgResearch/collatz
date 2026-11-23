# Full upper local dimension of the actual canonical real boundary

Date: 2026-11-23.

**Status: SOURCE-QUALIFIED written theorem.** Under the retained canonical
trace, its positive floor and selection identity, and the distinct-path
reciprocal estimate, the real boundary of the **actual inverse law from each
fixed nonperiodic ordinary unit root** is nonatomic and has upper local
dimension one almost everywhere. The same conclusion holds for the common
real boundary of the retained whole-component ordinary law, and for its
bounded positive tilts. This improves the earlier dimension-one **support**
statement to a statement about the supplied probability law itself.

No lower local dimension, exact dimensionality, uniform concentration rate,
forward-time entropy bound, escape exclusion, or cycle exclusion is proved.
The infinite theorem below is a written deduction, not a Lean declaration.

## 1. Inputs, source pins, and exact law

Write

\[
 U(n)=\frac{3n+1}{2^{e(n)}},\qquad e(n)=v_2(3n+1),
 \qquad \lambda(n)=\frac{3n}{3n+1}.
 \tag{1}
\]

Fix a positive odd ternary unit \(q\) which is not periodic. Every vertex
in its inverse unit tree is nonperiodic. The trace \(F\) obeys

\[
 F(v)=\sum_{Ux=v}3\,2^{-e(x)}F(x),\qquad
 F(x)\ge\alpha>0\quad(3\nmid x),
 \tag{2}
\]

and vanishes on multiples of three. All states below are ordinary positive
odd units, and their inverse kernel is exactly

\[
 K_F(v,x)=\mathbf1_{Ux=v}
 \frac{3}{2^{e(x)}}\frac{F(x)}{F(v)}.
 \tag{3}
\]

Let \(\mathsf P_q\) be this path law, \(X_0=q\), and put

\[
 A_r=\sum_{j=1}^r e(X_j),\qquad
 a_r=\frac{3^r}{2^{A_r}},\qquad
 R_r=\sum_{j=1}^r\frac{3^{j-1}}{2^{A_j}}.
 \tag{4}
\]

Thus \(A_r\) is the actual accumulated valuation clock, not a sampled or
averaged replacement. The finite cylinder ending at \(n=X_r\) has mass

\[
 \mathsf P_q(W_r=w)=a_r\frac{F(n)}{F(q)},
 \qquad q=R_r+a_r n.
 \tag{5}
\]

The two additional analytic inputs, with their source qualifications, are:

\[
 \sum_{x\text{ on a distinct actual path},\ x\ge m}\frac1x
 \le200m^{-1/40};
 \tag{6}
\]

and, with \(g=D_1/F\), \(D_1=P\mathbf1\),

\[
 0\le g\le2/\alpha,\qquad D_1\le2,\qquad
 \mathbb E_q\!\left[\mathbf1_H\frac1N
             \sum_{j<N}g(X_j)\right]
 \longrightarrow\mathsf P_q(H)
 \tag{7}
\]

for every event \(H\) in the full path sigmafield. In (2), the critical
operator is denoted \(P\); it is not the ordinary inverse counting operator
called \(L\) in the earlier component packet.

| Frozen source | Exact input or comparison |
|---|---|
| PR180, `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`, `research/high-variance-20261123/ANALYTIC_GLUING.md`, Sections 1--4 | Distinct-path estimate, coherent coordinate, actual common boundary, and bounded equivalence of the ordinary, critical, and trace path laws. |
| PR180, same SHA, `research/high-variance-20261123/ENTROPY_RIGIDITY.md`, Sections 1--3 | Retained whole-path law and distinction between the common boundary and its moving physical normalization. |
| PR185, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, Sections 1--2 | The source-qualified distinct-path and positive harmonic inputs behind (6). |
| PR178, `2169884b64871b448cda16c7d74a0d5914ed870b`, `research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md`, Section 1 | The precise canonical trace \(F=h_{\rm tr}\), kernel, and bounded observable in (2)--(3), (7). |
| Lyapunov Weaver, [Paper 12 v1](https://rstation.ai/problems/collatz/papers/12), Sections 8--10, Corollary 7 and Lemma 8, equations (26)--(29) | The canonical trace selection identity (7), including its full-path-event quantifier. Theorem 9 supplies the low-profile upper-frequency consequence reconstructed below. |
| Lyapunov Weaver, [Paper 131 v1](https://rstation.ai/problems/collatz/papers/131), Section 4, Lemmas 3--4 | Prior same-total separation and heavy-interval counting method. Its cap-five probability law and bounded residual-tail moment are **not** imported. |

The recent manuscript dependencies remain source-qualified. In particular,
their trace construction and population inputs have not been rebuilt here.
The new argument is the low-profile cone floor and its use with the actual
trace cylinder masses to control real overlaps.

## 2. A low trace value forces the whole inverse cone above a linear floor

Set

\[
 \rho=1/40,\qquad C_0=200/3,\qquad \delta=e^{-C_0}.
\]

Every finite inverse path here has distinct states. By (6), its product of
\(\lambda\)'s is at least \(\delta\). In particular,

\[
 \frac{a_rX_r}{q}
 =\prod_{j=1}^r\lambda(X_j)\ge\delta.
 \tag{8}
\]

Consequently \(R_r\) increases to a real limit \(R\), with
\(0\le R\le(1-\delta)q\). This is the real evaluation of the actual
inverse prefixes in (4).

**Lemma 1 (whole-cone floor).** If \(F(n)\le B\), then every ordinary
unit ancestor \(u\) of \(n\) satisfies

\[
 u\ge c_B n,\qquad c_B:=\alpha\delta/B>0.
 \tag{9}
\]

**Proof.** Let the actual path from \(u\) to \(n\) have multiplier
\(\omega\). Its positive term in iterated (2) gives
\(F(n)\ge\omega F(u)\ge\alpha\omega\). The same product calculation
as (8) gives \(\omega u/n\ge\delta\). Combining the two inequalities
proves (9), including the empty path. \(\square\)

This is a property of the entire cone, not merely of one likely continuation.
A late root on an escaping forward ray need not have low \(F\), so the
lemma does not discard the earlier root retained by that ray's large cone.

**Lemma 2 (deterministic low-profile shadow).** There is a constant
\(D=D(q,B)\ge1\) such that every depth-\(r\) prefix with \(F(X_r)\le B\)
has its **whole** real boundary image in

\[
 [R_r,R_r+D a_r^\rho].
 \tag{10}
\]

**Proof.** Set \(n=X_r\). Every state in every continued inverse path
from \(n\) is at least \(c_Bn\), by Lemma 1. Applying (6) to such a
continuation gives

\[
 \prod_{j>r}\lambda(X_j)
 \ge\exp\bigl(-C_0(c_Bn)^{-\rho}\bigr).
\]

Hence, using \(1-e^{-u}\le u\) and \(a_r n=q-R_r\le q\),

\[
 \begin{aligned}
 0\le R-R_r
 &=a_r n\left(1-\prod_{j>r}\lambda(X_j)\right)\\
 &\le C_0c_B^{-\rho}a_r n^{1-\rho}
 \le C_0c_B^{-\rho}q^{1-\rho}a_r^\rho.
 \end{aligned}
 \tag{11}
\]

Take \(D=\max\{1,C_0c_B^{-\rho}q^{1-\rho}\}\). The bound holds
for every continuation of the retained prefix. \(\square\)

## 3. Low-profile returns give exponentially small multipliers infinitely often

Fix \(B>\max\{2,\alpha\}\), and let

\[
 L_r=\#\{0\le j<r:F(X_j)\le B\},\qquad
 \vartheta_B=\frac{1-2/B}{2/\alpha-2/B}>0.
 \tag{12}
\]

The input (7) implies

\[
 \limsup_{r\to\infty}L_r/r\ge\vartheta_B
 \quad\mathsf P_q\text{-almost surely}.
 \tag{13}
\]

For clarity, this is only an upper-frequency assertion. Indeed,
\(g\le2/B+(2/\alpha-2/B)\mathbf1_{F\le B}\). On an event where the
limsup in (13) falls short by a fixed positive margin, the limsup of the
averages of \(g\) falls short of one by a fixed margin. Reverse Fatou for
these bounded averages contradicts (7) on that event. Countably many
margins prove (13).

Each unit \(n\) has two distinct legal unit parents with valuation at most
six. To see this, choose \(e_0\in\{1,2\}\) with
\(2^{e_0}n\equiv1\pmod3\). The three integral parents with exponents
\(e_0,e_0+2,e_0+4\) occupy all three residues modulo three; two are units.
At a node with \(F(n)\le B\), each of these two unit edges has canonical
probability at least

\[
 p_B:=\frac{3\alpha}{64B}>0.
 \tag{14}
\]

Their row probabilities sum to at most one, so \(p_B\le1/2\). No chosen
edge can therefore have probability greater than \(1-p_B\). With
\(\kappa_B=-\log(1-p_B)>0\), (5) yields the pathwise inequality

\[
 -\log\mathsf P_q(W_r)\ge\kappa_B L_r,
 \qquad
 a_r\le\frac{F(q)}\alpha e^{-\kappa_B L_r}.
 \tag{15}
\]

**Lemma 3 (good return subsequence).** There is a constant \(c>0\) such
that, almost surely, infinitely many depths \(r\) satisfy

\[
 F(X_r)\le B,\qquad a_r\le e^{-cr}.
 \tag{16}
\]

**Proof.** By (13), infinitely many integers \(N\) satisfy
\(L_N\ge\vartheta_B N/2\). For each, let \(r<N\) be the latest
low-profile time. Then \(r\to\infty\) along these choices, and
\(L_r=L_N-1\). Since \(r\le N\), for all sufficiently large choices
\(L_r\ge\vartheta_Br/4\). Formula (15) gives (16), for example with
\(c=\kappa_B\vartheta_B/8\), after absorbing the fixed factor
\(F(q)/\alpha\). \(\square\)

This step does not promote upper frequency to lower frequency. It produces
only the stated infinite subsequence of low-profile endpoints.

## 4. Same-total separation controls overlap under the actual probability

Fix depth \(r\) and total \(A\). Put

\[
 a=3^r2^{-A},\qquad t=Da^\rho,
\]

and retain the event

\[
 E_{r,A}=\{A_r=A,\ F(X_r)\le B\}.
\]

Distinct legal words of length \(r\) have distinct endpoints: their unique
forward histories recover the entire word. Endpoints are odd integers, so,
at this fixed total, (5) separates the offsets by at least \(2a\).

Suppose \(a\le1\), so that \(t\ge a\). Partition the real line into
half-open cells \(J_j=[jt,(j+1)t)\). If the real boundary of a retained
prefix belongs to \(J_j\), Lemma 2 puts its offset in an interval of
length \(2t\). At most \(t/a+1\) prefixes can do so. Each has its
**original**, unconditioned probability at most \(Ba/F(q)\), by (5).
Consequently, if \(\sigma_{r,A}\) is the real pushforward of
\(\mathbf1_{E_{r,A}}\mathsf P_q\), then

\[
 \boxed{\sigma_{r,A}(J_j)\le\frac{2B}{F(q)}t.}
 \tag{17}
\]

The bound concerns a restriction of the actual path law. No uniform law
over endpoints or over fixed-total words has been introduced.

Now let \(\eta\) be **any fixed probability measure on the real line**,
and take \(0<s<1\). If some \(u\in J_j\) satisfies
\(\eta([u-t,u+t])>t^s\), then
\(\eta([(j-1)t,(j+2)t])>t^s\). These closed enlarged cells overlap
at most four times. Thus at most \(4t^{-s}\) cells qualify. Equation
(17) gives

\[
 \boxed{\mathsf P_q\bigl(E_{r,A},\
       \eta([R-t,R+t])>t^s\bigr)
       \le\frac{8B}{F(q)}t^{1-s}.}
 \tag{18}
\]

The reference \(\eta\) is not required to be the real marginal of
\(\mathsf P_q\). This point will allow the same-law component transfer
without a weak-limit inference.

## 5. Summing the exact clock proves upper local dimension one

Retain only totals \(A\) with \(a=3^r2^{-A}\le e^{-cr}\), where \(c\)
is from Lemma 3. For all large \(r\), these scales satisfy \(t<1\).
Summing (18) over **all** such totals gives the convergent geometric sum

\[
 \begin{aligned}
 &\mathsf P_q\bigl(F(X_r)\le B,\ a_r\le e^{-cr},\
       \eta([R-Da_r^\rho,R+Da_r^\rho])
          >(Da_r^\rho)^s\bigr)\\
 &\hspace{2em}\le
 \frac{8B D^{1-s}}{F(q)}
 \frac{e^{-cr\rho(1-s)}}{1-2^{-\rho(1-s)}}.
 \end{aligned}
 \tag{19}
\]

There is no factor proportional to the number of possible valuation totals:
their contributions decay geometrically. There is also no upper cutoff
\(A_r=O(r)\) hidden in this estimate.

The right side is summable in \(r\). Borel--Cantelli and Lemma 3 imply
that, almost surely, there are infinitely many scales \(t\downarrow0\)
with

\[
 \eta([R-t,R+t])\le t^s.
 \tag{20}
\]

Intersecting over rational \(0<s<1\) proves the useful stronger statement

\[
 \boxed{\text{For every fixed real probability }\eta,\quad
 \limsup_{t\downarrow0}
 \frac{\log\eta([R-t,R+t])}{\log t}\ge1
 \quad\mathsf P_q\text{-almost surely}.}
 \tag{21}
\]

The exceptional null set may depend on \(\eta\). If a ball has zero
\(\eta\)-mass, its ratio is interpreted as \(+\infty\).

Take \(\eta=\mu_q:=\mathcal L_{\mathsf P_q}(R)\). For completeness,
every probability \(\mu\) with bounded support has upper local dimension
at most one at \(\mu\)-almost every point. At dyadic mesh \(2^{-k}\),
the total mass of cells of mass less than \(2^{-k(1+\varepsilon)}\)
is \(O(2^{-k\varepsilon})\), since only \(O(2^k)\) cells meet its
support. Borel--Cantelli shows that the containing dyadic cell has mass at
least \(2^{-k(1+\varepsilon)}\) eventually almost surely. That cell lies
inside the radius-\(2^{-k}\) ball. Interpolation between consecutive
dyadic radii and then \(\varepsilon\downarrow0\) prove the bound.
Combining it with (21) gives the main theorem:

\[
 \boxed{\overline{\dim}_{\rm loc}\mu_q(R)=1
        \quad\mathsf P_q\text{-almost surely}.}
 \tag{22}
\]

In particular \(\mu_q\) has no atoms, since the local dimension at an
atom is zero. A fixed nonzero affine normalization of \(R\) preserves
(22).

### The common actual component law

In the pinned component packet, let \(\mu_E\) be the law of the common
boundary \(Z\) under the ordinary whole-path law \(\Pi_E\). Condition on
any clock-zero vertex \(q\) of positive probability. Its conditional
ordinary inverse law is boundedly equivalent to (3), and the two real
coordinates obey exactly

\[
 R=q-\chi(q)Z.
 \tag{23}
\]

Apply (21) with the **fixed reference measure**
\(\eta=(z\mapsto q-\chi(q)z)_*\mu_E\). It implies upper local
dimension at least one for \(\mu_E\) at the sampled \(Z\), under the
trace law and hence under the equivalent conditional ordinary law. Take
the countable union over the clock-zero roots, then use the universal
upper bound from the preceding paragraph. Therefore

\[
 \boxed{\overline{\dim}_{\rm loc}\mu_E(Z)=1
        \quad\Pi_E\text{-almost surely}.}
 \tag{24}
\]

This is a statement about the original component law, not about an auxiliary
Frostman measure supported on the same set. Its bounded positive tilts have
the same conclusion: their real ball masses differ by fixed multiplicative
constants. In particular this applies to the \(Z\)-size bias describing
the critical \(G\)-law in the earlier packet, and to the bounded additional
trace tilt supplied there.

## 6. A separate nonatomicity proof using the full selection identity

This gives a shorter check of the no-atom part without the entropy-return
argument in Section 3. Let \(H_r\) be the least endpoint at inverse depth
\(r\) from \(q\). Then \(H_r\to\infty\). Indeed, each integer below
a fixed bound has at most one depth at which its forward orbit hits the
nonperiodic root; there are only finitely many such integers.

Every depth-\(r\) prefix consequently has
\(a_r\le q/H_r\). For any fixed real point \(z\), the same-total
separation and Lemma 2 show

\[
 \mathsf P_q(R=z,F(X_r)\le B,A_r=A)
 \le\frac{B}{F(q)}\left(\frac D2 a^\rho+a\right).
\]

Summing geometrically over totals with \(a\le q/H_r\) proves

\[
 \sup_z\mathsf P_q(R=z,F(X_r)\le B)
 =O_{q,B}\bigl((q/H_r)^\rho+q/H_r\bigr)\longrightarrow0.
 \tag{25}
\]

For the full-path event \(H=\{R=z\}\), use
\(g\le2/B+(2/\alpha)\mathbf1_{F\le B}\) in (7). Equations (7)
and (25), with ordinary Cesaro convergence, give

\[
 \mathsf P_q(H)\le\frac2B\mathsf P_q(H).
\]

Since \(B>2\), \(\mathsf P_q(H)=0\). Merely knowing positive upper
frequency would not justify this last deduction; it is the full-event
identity (7) that does so. The stronger proof in Sections 3--5 instead
uses a summable bad-event estimate along good return depths.

## 7. What is established and what remains to close

The finite arithmetic facts used here are exact: the two short unit
parents, the cylinder telescoping, and the same-total endpoint separation.
The new infinite proof retains the supplied canonical trace and its actual
probabilities. The key upgrade is that a low trace value forces a linear
floor for **every** predecessor, so that the infinite real tail is uniformly
controlled at those actual nodes. The old absence of a global residual-tail
moment is not assumed away.

The result excludes an atomic common real boundary and gives full upper
local dimension for that law. It does not give lower local dimension one:
the good depths in Lemma 3 may have arbitrarily long gaps. In particular,
neither a uniform Frostman bound nor an all-scale collision estimate follows
from (22)--(24).

The current critical target is still a bound for the **actual ternary
inverse-time marginal**, for example an upper collision estimate of order
\(3^{-\theta m}\), with \(\theta=0.949955527188\ldots\), on the clock
range in PR185's `COLLISION_LOGARITHMIC_GAIN.md`. That estimate would oppose
its retained lower bound \(c\sqrt m\,3^{-\theta m}\). The theorem here
controls real mass at path-dependent subsequences of scales. No step has
been supplied that converts those scales and masses into that same-law,
same-clock ternary estimate. The earlier common-boundary independence result
and the integer-lift cost of real/ternary quotients therefore remain relevant.

This is a new restriction on a hypothetical escaping component's actual
boundary law, and not a completed proof of Collatz.
