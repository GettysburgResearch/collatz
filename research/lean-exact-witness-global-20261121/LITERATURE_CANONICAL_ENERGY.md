# Canonical variation, recurrent symmetrization, and the run weight

Date: 2026-11-22.

**Status.** Written deductions from the explicitly pinned ordinary harmonic
construction, together with this branch's written binary-run forcing theorem.
No infinite analytic input is installed as a Lean axiom. This attempt does
not prove zero escaping capacity or exclude nontrivial cycles.

The canonical charge does give a new global estimate:

\[
\boxed{\sum_n\nu(n)|\mathcal R(n)-\mathsf C\mathcal R(n)|
\le 2D(1+\log\kappa)+\frac{16000A}{3}<\infty,\qquad
\kappa=\max(1,A/\gamma).}
\tag{1}
\]

This is absolute variation along all actual edges, including the killed
boundary. It is stronger than the previously available square-gradient
estimate. The proof keeps each original canonical charge and sums its
actual side current.

The corresponding run-weighted variation is infinite on a known convergent
basin: for every \(p>0\),

\[
\boxed{\sum_n\nu(n)4^{r(n)}
 |\mathcal R(n)-\mathsf C\mathcal R(n)|^p=\infty.}
\tag{2}
\]

Here \(r(n)\) counts maximal nonempty runs of one-bits. Equation (2) is proved
using only the explicit fiber \(U(n_j)=5\), not a hypothetical escaping orbit.
It does not assert divergence of the terminal-weighted energy in (31).
The source and endpoint weights are different.

The literature test also has an exact outcome. Every hypothetical escaping
component has a recurrent symmetric form, but the directed form fails the
strong sector condition already on the actual predecessor tree of \(5\).
For the canonical potential itself, the surviving antisymmetric pairing is
exactly the original component charge. The final section sharpens the
terminal run-mass lower bound to a rate proportional to \(\log\log N\).
No matching canonical upper bound is obtained.

## 1. Sources, domain, and retained qualifications

The repository is GettysburgResearch/collatz. These are frozen source
objects, not references to moving PR descriptions.

| Source | Exact commit and material used |
|---|---|
| PR185 | 4b0c2c27812db555061f5d9006de82a87e7e364f, research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md, (13)--(19): canonical reference, charge, antichain bound, and moments. Its new central-obstruction-20261122/ESCAPE_ATTEMPTS.md was inspected for the moving-root qualification. |
| PR175 | f63204765438c83def68154e7f253ee9b660979c, research/lean-global-closure-20261121/LATE_GREEN_HARMONIC_MOMENT.md, (5), and LITERATURE_DIRICHLET_BOUNDARY.md: least-predecessor estimate and finite actual-edge energy. The new central/DIRECT_CANONICAL_CHARGE_ATTEMPT.md retains the same source charge through contact reset. |
| PR180 | a9f471543d7fed0a76f348e6d97a9d6d44fa369e, research/central-step-20261122/CRITICAL_BOUNDARY.md: complete canonical Green identity and the moving-clock source profile. |
| PR183 | 68345f60a4f757acb42a69a4ac95910f8ce26163, research/profound-step-20261122/operator/WOLD_CHANNELS.md, W4--W7: actual integer clocks and the mass of each synchronous class. |
| This branch | BINARY_RUN_COMPACTNESS.md, Theorem A; TERMINAL_DIRICHLET_RUN_MASS.md, (14)--(17): finite run-forcing core and physical inverse-prefix lower bound. These are written proofs with their displayed formalization boundaries. |

Let \(\mathcal N\) be the positive odd ternary units that are not themselves
periodic. A point can later enter a periodic orbit. The map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

is killed on its first periodic state. Write \(\tau(n)\) for this killing
time, possibly infinite, and put

\[
\begin{gathered}
(La)(q)=\sum_{Un=q}a(n),\qquad
(\mathsf C f)(n)=\mathbf1_{\{\tau(n)>1\}}f(Un),\\
(Kf)(q)=\frac1{\nu(q)}\sum_{Un=q}\nu(n)f(n).
\end{gathered}
\tag{3}
\]

Every parent sum is over retained points. The imported construction gives

\[
\begin{gathered}
L\nu=\nu,\qquad \gamma/n\le h(n)=G(n)/n\le\nu(n)\le A,\\
\lambda(n)=\frac{3n}{3n+1},\qquad
d(n)=(1-\lambda(n))h(n),\qquad D=\sum_n d(n)<\infty,\\
\sum_{n\le X}\nu(n)\le 5A X^{39/40}.
\end{gathered}
\tag{4}
\]

These retain the source's predecessor-population and canonical-envelope
qualifications. In particular they are not new unconditional assertions
about a numerically constructed function.

The canonical potential has the exact identities

\[
\begin{gathered}
g=d/\nu,\qquad
\mathcal R=\sum_{j\ge0}K^j g
=1-\frac{\lambda h}{\nu}\in[0,1],\\
\nu(q)\mathcal R(q)=\sum_{n\in\operatorname{Pred}(q)}d(n),\qquad
\nu(q)=\lambda(q)h(q)+\sum_{n\in\operatorname{Pred}(q)}d(n).
\end{gathered}
\tag{5}
\]

Thus \(\nu\) is not the unweighted sum of \(h\) over all predecessors.
Each source in (5) is counted once, at its unique visit to a nonperiodic
target. We also use the pinned whole-predecessor estimate

\[
\mathcal R(q)\le 67\,\bigl(\min\operatorname{Pred}(q)\bigr)^{-1/40}.
\tag{6}
\]

It is essential here that the minimum is over all actual predecessors.

## 2. The charge pays finite absolute variation

For a source \(n\), let \(q_j=U^j n\) while the path is retained. Define
the contribution of this one original charge by

\[
\mathcal R^{[n]}(q)=
\frac{d(n)}{\nu(q)}\,
\mathbf1_{\{q=q_j\text{ for some }0\le j<\tau(n)\}}.
\tag{7}
\]

The full potential is the nonnegative sum of these contributions.
Set \(v_j=\nu(q_j)\). Harmonicity gives \(v_{j+1}\ge v_j>0\).
For a retained edge \(q_j\to q_{j+1}\), put

\[
\epsilon_j=1-\frac{v_j}{v_{j+1}}\ge0.
\]

There are four contributions to the absolute variation of (7).
The inverse parents entering \(n\) contribute \(d(n)\) in total.
The decrease along the displayed edge contributes \(d(n)\epsilon_j\).
All its other incoming parents together contribute the same amount:
their total reference mass is \(v_{j+1}-v_j\).
If the orbit is killed, its final boundary edge contributes \(d(n)\).
There are no other nonzero terms. Hence

\[
\begin{split}
&\sum_q\nu(q)
 |\mathcal R^{[n]}(q)-\mathsf C\mathcal R^{[n]}(q)|\\
&\quad=d(n)\left[
1+\mathbf1_{\{\tau(n)<\infty\}}
 +2\sum_{\substack{j\ge0\\j+1<\tau(n)}}\epsilon_j\right]\\
&\quad\le 2d(n)\left[1+\log\frac A{\nu(n)}\right].
\end{split}
\tag{8}
\]

For the last inequality, use \(1-a/b\le\log(b/a)\) and telescope finite
prefixes before taking a monotone limit. Thus the bound applies to both
finite and infinite paths and includes all collisions into the path.

The remaining logarithmic charge is summable. If
\(M(t)=\sum_{n\le t}\nu(n)\), Tonelli gives the exact integral

\[
\begin{split}
\sum_n\frac{\nu(n)(1+\log n)}n
&=\int_1^\infty M(t)\frac{\log t}{t^2}\,dt\\
&\le5A\int_1^\infty t^{-41/40}\log t\,dt
=8000A.
\end{split}
\tag{9}
\]

Since \(d(n)\le\nu(n)/(3n)\) and
\(\log(A/\nu(n))\le\log\kappa+\log n\),

\[
\sum_n d(n)\log\frac A{\nu(n)}
\le D\log\kappa+\frac{8000A}{3}.
\tag{10}
\]

The triangle inequality, (8), and nonnegative summation now prove (1).
This proof uses the specific canonical charge in (4); mere boundedness of
a Green potential would not establish (10).

In particular

\[
a:=\mathcal R-\mathsf C\mathcal R\in L^1(\nu).
\tag{11}
\]

Absolute convergence also licenses signed summation of the one-source
calculation. The on-path and off-path terms in (8) cancel with their signs.
The incoming term has sign minus; the killed term has sign plus. On an
escaping component \(\mathcal C\) this yields

\[
\boxed{\sum_{q\in\mathcal C}\nu(q)a(q)=-D_{\mathcal C},
\qquad D_{\mathcal C}=\sum_{q\in\mathcal C}d(q).}
\tag{12}
\]

Globally the signed integral is minus the total charge of escaping sources.
On a killed source contribution it is zero. Thus finite absolute variation
does not mean zero escaping current. Also
\(\int\mathsf C^j a\,d\nu=\int a\,d\nu\), since \(\mathsf C\) is an
\(L^1(\nu)\) isometry. Its Cesaro averages need not tend to zero in
\(L^1(\nu)\), although the previously proved square-gradient averages do
tend to zero in \(L^2(\nu)\).

## 3. The recurrence theorem and its precise hypotheses

The main literature test is Beznea--Cimpean--Rockner,
*Irreducible recurrence, ergodicity, and extremality of invariant measures
for resolvents*, SPA 128 (2018), 1405--1437,
[published Theorem 5.1 and Corollary 5.2](https://doi.org/10.1016/j.spa.2017.07.009).
For a Dirichlet form on \(L^2\) of a sigma-finite reference, recurrence of its
symmetric part transfers to the form under the homogeneous strong sector
inequality. The corollary characterizes recurrence by increasing unit
cutoffs with vanishing energy when that inequality holds. The theorem
numbers here refer to the final publication; the
[2015 author preprint](https://bibos.math.uni-bielefeld.de/preprints/14-09-473.pdf)
has different Section 5 numbering.

For our actual operators on \(\mathcal H=\ell^2(\mathcal N,\nu)\), define

\[
\mathcal E(f,g)=\langle(I-K)f,g\rangle_\nu,\qquad
\mathcal E_{\rm s}(f,g)=\tfrac12(\mathcal E(f,g)+\mathcal E(g,f)).
\tag{13}
\]

The form domain is all of \(\mathcal H\). The countable discrete space is
Lusin; every point has finite positive measure; the measure is sigma-finite.
The bounded sub-Markov semigroups generated by \(K-I\) and
\(\mathsf C-I\) are adjoint. Their forms are closed with the usual
norm-plus-energy norm. In particular a weak sector estimate follows from
boundedness, but that estimate contains an \(L^2\) term.
The homogeneous condition required for the recurrence transfer is

\[
|\mathcal E(f,g)|\le M\,
 \mathcal E(f,f)^{1/2}\mathcal E(g,g)^{1/2}
\quad\text{for all }f,g\in\mathcal H.
\tag{14}
\]

It is not implied by boundedness of \(K\).

The related capacity comparison in Gaudilliere--Landim,
[*A Dirichlet principle for non reversible Markov chains and some
recurrence theorems*, Lemma 2.6](https://arxiv.org/pdf/1111.2445v1),
also requires a homogeneous sector bound. Its Theorem 2.4 assumes an
irreducible countable chain and a finite complement of one boundary set.
On the full killed domain the reference is only sub-invariant for \(K\).
On an escaping component it is stationary, but the directed inverse
kernel is still not irreducible: it moves only to ancestors. That
variational theorem is therefore not invoked as an ordinary absorption
result.

### Recurrent symmetric form on an escaping component

Fix an escaping component \(\mathcal C\). The actual clock \(\ell\) satisfies
\(\ell(Uq)=\ell(q)+1\). Its synchronous layers have mass

\[
\sum_{\substack{q\in\mathcal C\\\ell(q)=j}}\nu(q)=C_{\mathcal C}
\quad(j\in\mathbb Z),
\qquad C_{\mathcal C}=\lim_{k\to\infty}\nu(U^kq)>0.
\tag{15}
\]

For completeness, at a reference ray \(q_r\) the fronts
\(\{x:U^{r-j}x=q_r\}\) increase to the layer of clock \(j\).
Their masses are \(\nu(q_r)\); monotone convergence proves (15).

On this component the symmetric kernel is
\((K+\mathsf C)/2\). Put

\[
f_N(q)=\max(0,1-|\ell(q)|/N).
\]

Every \(f_N\) is square integrable, because it uses finitely many layers of
finite mass. Direct calculation gives

\[
0\le f_N\uparrow1,\qquad
\|f_N\|_\nu^2=C_{\mathcal C}\frac{2N^2+1}{3N},\qquad
\mathcal E_{\rm s}(f_N,f_N)=\frac{C_{\mathcal C}}N.
\tag{16}
\]

The symmetric form satisfies (14) with constant one. Corollary 5.2 thus
applies and proves that this symmetric form is recurrent. No local
finiteness of the inverse graph or finite inverse fibers is assumed.

### The strong sector condition fails on the known predecessor tree of five

Let \(\mathcal B_k=\{x:U^kx=5\}\). These layers are disjoint, each has
mass \(\nu(5)\), and their union is a reducing subtree for the killed
operators because \(U(5)=1\). On layer-constant functions, \(K\) sends
\(\phi(k)\) to \(\phi(k+1)\), while \(\mathsf C\) sends it to
\(\phi(k-1)\), with value zero at depth zero.

For \(N\ge2\) take the finite clock packets

\[
\phi_N(k)=\max(0,1-|k-N|/N),\qquad
\psi_N(k)=\phi_N(k-N).
\]

Extend them by zero away from this subtree. They belong to \(\mathcal H\).
Their exact form values are

\[
\mathcal E(\phi_N,\phi_N)=\mathcal E(\psi_N,\psi_N)=\frac{\nu(5)}N,
\qquad
\mathcal E(\phi_N,\psi_N)=\nu(5)\frac{N-1}{2N}.
\tag{17}
\]

Indeed the last sum is
\(\nu(5)N^{-2}\sum_{i=0}^{N-1}i\).
The ratio in (14) equals \((N-1)/2\), so no finite \(M\) works.
This is a failure on actual known convergent integers, not an abstract
replacement system.

### The canonical pairing retains its current

The weaker attempt was to use only \(\mathcal R\) as the first argument
in (14). On the escaping component, finite layer support and boundedness
of \(\mathcal R\) justify

\[
\mathcal E(\mathcal R,f_N)=\sum_{q\in\mathcal C}d(q)f_N(q)
\longrightarrow D_{\mathcal C}.
\tag{18}
\]

Although \(\mathcal R\) need not belong to \(\mathcal H\), this displayed
pairing is defined by its actual Poisson equation
\((I-K)\mathcal R=g\). The reversed pairing is absolutely defined and is
\(\mathcal E(f_N,\mathcal R)=\sum_{\mathcal C}\nu f_Na\).
By (11)--(12) it tends to \(-D_{\mathcal C}\). Therefore

\[
\mathcal E_{\rm s}(\mathcal R,f_N)\longrightarrow0,\qquad
\boxed{\mathcal E_{\rm a}(\mathcal R,f_N)\longrightarrow D_{\mathcal C},}
\tag{19}
\]

where \(\mathcal E_{\rm a}\) is the antisymmetric half-difference.
The first limit also follows from the finite square-gradient budget and
(16) by Cauchy--Schwarz. The second is the exact original-source term that
this recurrence argument would have to eliminate. Equation (1) does not
eliminate it.

## 4. An exact arithmetic failure of the run-weighted variation

Consider the positive odd units

\[
n_j=\frac{40\cdot64^j-1}{3},\qquad j\ge0.
\tag{20}
\]

They satisfy \(n_0=13\), \(n_{j+1}=64n_j+21\), and

\[
3n_j+1=5\cdot2^{6j+3},\qquad U(n_j)=5.
\tag{21}
\]

Their ternary residue is one. Multiplication by \(64\) shifts the binary
expansion six places, and adding \(21\) appends the block \(010101\).
The leading zero separates its three runs from those of the preceding
odd integer. Since \(13\) has two runs,

\[
r(n_j)=2+3j,\qquad
W(n_j):=4^{r(n_j)}=16\cdot64^j.
\tag{22}
\]

The actual harmonic floor now gives a uniform positive lower bound,

\[
\nu(n_j)W(n_j)\ge\frac{\gamma W(n_j)}{n_j}
>\frac{6\gamma}{5}.
\tag{23}
\]

We also have \(\min\operatorname{Pred}(n_j)\to\infty\).
For any fixed bound \(B\), each of the finitely many sources at most \(B\)
can visit at most one member of (20) before its first visit to \(5\).
If it visits none there is nothing to count; after a visit to \(5\) it
reaches the periodic point \(1\). Thus only finitely many \(n_j\) have a
predecessor at most \(B\). Equation (6), with exactly this whole-predecessor
minimum, implies

\[
\mathcal R(n_j)\longrightarrow0,\qquad
\mathcal R(5)\ge g(5)>0.
\tag{24}
\]

Choose \(J\) such that
\(\mathcal R(n_j)\le\mathcal R(5)/2\) for all \(j\ge J\).
For every real \(p>0\),

\[
\nu(n_j)W(n_j)
 |\mathcal R(n_j)-\mathcal R(5)|^p
\ge\frac{6\gamma}{5}\left(\frac{\mathcal R(5)}2\right)^p
\quad(j\ge J).
\tag{25}
\]

This proves (2), including \(p=1\) and \(p=2\).
For the bounded truncation \(W_L=\min(W,4^L)\), the same proof gives

\[
\sum_n\nu(n)W_L(n)|a(n)|^p
\ge\frac{6\gamma}{5}\left(\frac{\mathcal R(5)}2\right)^p
 \left(\left\lfloor\frac{L-2}{3}\right\rfloor-J+1\right)_+.
\tag{26}
\]

Thus even this truncated source-weighted budget grows at least linearly
in \(L\). There is an operator version independent of \(\mathcal R\):
the function \(\mathbf1_{\{5\}}\) belongs to \(\ell^2(W\nu)\), but its
forward composition \(\mathsf C\mathbf1_{\{5\}}\) does not. Consequently
the unweighted isometry cannot be treated as a bounded operator in this
run-weighted space.

## 5. Endpoint weights and the remaining arithmetic correlation

The desired energy weights the terminal point. It must not be replaced
by the source-weighted expression just disproved.

For an arbitrary nonnegative terminal weight \(w\), the same one-source
edge accounting that proved (8) gives

\[
\begin{split}
&\sum_{\substack{q\in\mathcal N\\Uq\in\mathcal N}}
 \nu(q)w(Uq)
 |\mathcal R^{[n]}(Uq)-\mathcal R^{[n]}(q)|\\
&\qquad=d(n)\left[w(n)+
2\sum_{\substack{j\ge0\\j+1<\tau(n)}}
 w(q_{j+1})\left(1-\frac{\nu(q_j)}{\nu(q_{j+1})}\right)\right].
\end{split}
\tag{27}
\]

This identity holds for extended nonnegative sums. There is no weight
at the killed endpoint. For \(w=1\), the logarithmic telescope applies.
For \(w=W\), it leaves the actual run-weighted side-current series in
(27). The finite charge bound (10) does not bound this series.

At the full canonical level, subtraction in (5) gives, for a retained
edge \(q\to p\),

\[
\nu(q)\bigl(\mathcal R(p)-\mathcal R(q)\bigr)
=\frac{\nu(q)}{\nu(p)}d(p)
+\sum_{\substack{Ux=p\\x\ne q}}
 \frac{\nu(q)\nu(x)}{\nu(p)}
 \bigl(\mathcal R(x)-\mathcal R(q)\bigr).
\tag{28}
\]

The first term is canonical immigration. The second is the actual
conditional side-branch correlation, with no sign supplied by the
available comparisons. Taking absolute values and then multiplying by
\(W(p)\) requires

\[
\sum_p W(p)d(p)+
\sum_p\frac{W(p)}{\nu(p)}
 \sum_{\substack{Uq=p\\Ux=p}}\nu(q)\nu(x)
 |\mathcal R(x)-\mathcal R(q)|.
\tag{29}
\]

No finite bound for (29) is proved here. It cannot be replaced by the
unweighted budget, by a fresh reciprocal-height source, or by the
contracting contact reference: a last-contact forward escape is killed
by that induced contact operator but is retained here.

There is also an exact way to see the limitation of using (1) alone.
Define the fixed finite original measure
\(\beta(q)=\nu(q)|a(q)|\).
For the terminal energy below, the triangle inequality and
\(|\mathcal R(n)-\mathcal R(U^Nn)|\le1\) give

\[
\sum_q W(q)\mathfrak e_N(q)
\le\frac1N\sum_{k=1}^N
 \sum_{\tau(x)>k}\beta(x)W(U^kx).
\tag{30}
\]

The regrouping uses \(\sum_{U^j n=x}\nu(n)=\nu(x)\), so these are
unchanged original masses. By (12),
\(\beta(\mathcal C)\ge D_{\mathcal C}>0\) on every escaping component.
Thus the right side still contains an escaping original atom whenever
the left side's boundary coefficient is positive. Finiteness of
\(\beta\) is not a uniform moment bound for its forward images.
All statements with an unbounded \(W\) are interpreted as nonnegative
extended sums; bounded truncations justify the same calculations first.

## 6. A quantitative lower rate for the actual terminal energy

Retain the terminal measure from the frozen companion:

\[
\mathfrak e_N(q)=\frac1N
 \sum_{\substack{n\in\mathcal N\\U^Nn=q}}\nu(n)
 |\mathcal R(q)-\mathcal R(n)|^2,\qquad
b_\infty=\sum_{\mathcal C\ {\rm escaping}}
 C_{\mathcal C}F_{\mathcal C}^2,\quad
F_{\mathcal C}=\frac{D_{\mathcal C}}{C_{\mathcal C}}.
\tag{31}
\]

No source killed by time \(N\) appears in this definition. The frozen
companion handles the omitted killed energy and proves that its total
mass tends to zero. The following rate uses the physical lower bound,
so it does not apply a growing test function to a total-variation limit.

The binary-run theorem has the explicit core

\[
C_s=2^{(2s-1)(2\cdot4^s-1)}\quad(s\ge1):
\tag{32}
\]

every positive odd state at least \(C_s\) has a state with more than
\(s\) runs among its next \(4^s\) odd states, including the starting state.
On an injective escaping path \(q_j\), partition the first \(M\) indices
into blocks of length \(4^s\). At most \(C_s/2\) block starts are below
\(C_s\). Hence

\[
\#\{0\le j<M:r(q_j)>s\}
\ge\left\lfloor\frac M{4^s}\right\rfloor-\frac{C_s}{2}.
\tag{33}
\]

Use
\(W=4+3\sum_{s\ge1}4^s\mathbf1_{\{r>s\}}\).
For every integer \(L\ge2\),

\[
\frac1M\sum_{j<M}W(q_j)
\ge1+3L-\frac3M
 \sum_{s=1}^{L-1}4^s(1+C_s/2).
\tag{34}
\]

Here is an explicit finite error estimate. Since \(C_s\) is increasing,
the error term in (34) is at most

\[
\frac{4^L}{M}(1+C_L/2),\qquad C_L\le2^{4L4^L}.
\tag{34a}
\]

Fix \(0<\varepsilon<1\), put
\(L=\lfloor(1-\varepsilon)\log_4\log M\rfloor\), and assume

\[
\log M\ge
H_\varepsilon:=
\max\left\{(8/\varepsilon)^{2/\varepsilon},
                 16^{1/(1-\varepsilon)}\right\}.
\tag{34b}
\]

Then \(L\ge2\), \(4^L\le(\log M)^{1-\varepsilon}\), and
\[
\log C_L\le2(\log M)^{1-\varepsilon}\log\log M
\le\tfrac12\log M.
\]
For the last inequality, put \(u=\log M\); the first threshold in
(34b) ensures \(4\log u\le u^\varepsilon\).
It follows from (34)--(34a) that

\[
\boxed{\frac1M\sum_{j<M}W(q_j)
\ge\frac{3(1-\varepsilon)}{\log4}\log\log M
-2-\frac{3(\log M)^{1-\varepsilon}}{2\sqrt M}.}
\tag{34c}
\]

Letting \(M\) increase and then \(\varepsilon\) decrease to zero proves

\[
\boxed{\liminf_{M\to\infty}
 \frac{\frac1M\sum_{j<M}W(q_j)}{\log\log M}
\ge\frac3{\log4}.}
\tag{35}
\]

This bound is for the common accelerated odd clock. No ordinary-time
normalization is substituted.

For a fixed escaping component and a fixed anchor \(q_0\), the physical
prefix argument in the frozen companion gives, after choosing fixed
\(J,K\) and \(0<2\epsilon<F_{\mathcal C}\),

\[
\mathfrak e_N(q_j)\ge
\frac{\nu(q_0)(F_{\mathcal C}-2\epsilon)^2}{N}
\quad(J\le j\le N-K).
\tag{36}
\]

Apply (35) to this contiguous segment. Its omitted length is fixed.
Move the fixed anchor forward so that \(\nu(q_0)\) is arbitrarily
close to \(C_{\mathcal C}\), then let \(\epsilon\) decrease to zero.
For any finite set of escaping components their rays are disjoint,
so these lower bounds add. Exhaust the summable component coefficients
in (31). This proves the strengthened terminal result

\[
\boxed{\liminf_{N\to\infty}
 \frac{\sum_q4^{r(q)}\mathfrak e_N(q)}{\log\log N}
\ge\frac3{\log4}\,b_\infty.}
\tag{37}
\]

The moments in (37) may individually be infinite. No finiteness at a
fixed time is inferred by rearranging signed expressions.

## 7. Result of the closing attempt

The primary recurrence theorem was tested on the actual canonical
operators. Its symmetric hypothesis holds on an escaping component;
its required strong sector inequality fails even on a known convergent
subtree. The direct canonical calculation then established the finite
absolute variation (1), but retained the nonzero current (19).

The arithmetic run weight cannot be inserted at source edges: (20)--(26)
give an exact obstruction with known convergent integers. Keeping the
terminal weight instead leaves the genuine side-branch term (28)--(29)
and the unchanged-source forward moment (30). Neither the canonical
charge formula nor the inspected contact estimates supplied an upper
bound for those terms of order smaller than \(\log\log N\).

The new global outputs of this attempt are (1), the recurrent
symmetrization with the exact sector test, the concrete run-weighted
failure (2) and (26), and the quantitative terminal lower rate (37).
No canonical weighted upper bound, contradiction to \(b_\infty>0\), or
cycle exclusion is claimed.

All finite algebra and infinite-sum arguments in this note are written
proofs. The literature theorems and the imported canonical construction
are not represented as extra Lean declarations or custom axioms.

## 8. New continuation: every exponential run weight and finite forcing

The companion LITERATURE_ARITHMETIC_RETURN.md supplies a stronger written
arithmetic theorem:

\[
\boxed{\frac1N\#\{j<N:r(U^jx)\le S\}\longrightarrow0}
\quad\text{for every fixed }S
\tag{38}
\]

on every escaping odd orbit. Its primary input is
Evertse--Schlickewei--Schmidt,
[*Linear equations in variables which lie in a multiplicative group*,
Theorem 1.1](https://arxiv.org/pdf/math/0409604),
Annals of Mathematics 155 (2002), 807--836.
That theorem gives finiteness of nondegenerate solutions to a fixed linear
equation in a multiplicative group of finite rank over a characteristic-zero
field. The companion applies it over an algebraic closure of the rationals
to powers of \(2\) and \(3\). For a relation of length \(\ell\), normalization
uses a subgroup of rank \(2(\ell-1)\), with coefficients in \(\{1,-1\}\).

The arithmetic argument was independently checked here, in particular its
two distinct finiteness uses. A minimal zero subrelation containing the
largest initial endpoint term is fully nondegenerate: a zero proper
subset avoiding that term could be removed to contradict minimality.
If that subrelation has only endpoint terms, distinct signed powers of
two prevent it from staying on one endpoint side. Its mixed ratio then
has ternary valuation equal, up to sign, to the fixed odd clock \(h\).
The endpoint-only relation has at most \(4S\) terms, so its allowed clocks
belong to one finite set independent of \(h\).
Outside that set, a correction term must appear in the cluster. At each
fixed \(h\), its positive ratio to the largest initial term is bounded
below by the separate finite-ratio theorem with at most \(4S+h\) terms.
The actual relative correction tends to zero on escape, giving the
contradiction for that fixed clock. Progression packing then proves (38).
No assertion uniform in an unbounded clock is inserted.

### Terminal divergence for every \(\rho>1\)

Fix \(\rho>1\), and set

\[
w_\rho(n)=\rho^{r(n)},\qquad
w_{\rho,L}(n)=\min(w_\rho(n),\rho^L).
\]

By (38), the bounded function \(w_{\rho,L}\) equals \(\rho^L\) at a
set of odd times of density one. Consequently, on each escaping orbit,

\[
\frac1N\sum_{j<N}w_{\rho,L}(U^jx)\longrightarrow\rho^L.
\tag{39}
\]

Use the fixed-anchor lower bound (36), then move the anchor and exhaust
finitely many components exactly as in the proof of (37). The upper bound
is \(w_{\rho,L}\le\rho^L\), together with the already proved
\(\|\mathfrak e_N\|_1\to b_\infty\). This gives the exact bounded-weight
limit

\[
\boxed{\lim_{N\to\infty}
\sum_q w_{\rho,L}(q)\mathfrak e_N(q)=\rho^L b_\infty
\quad\text{for each fixed }L.}
\tag{40}
\]

In particular, if \(b_\infty>0\),

\[
\boxed{\sum_q\rho^{r(q)}\mathfrak e_N(q)\longrightarrow+\infty
\quad\text{for every }\rho>1.}
\tag{41}
\]

One first fixes \(L\), takes the time limit, and then increases \(L\).
No growing observable is applied to an unquantified total-variation error.
The conclusion permits infinite individual weighted moments.

### A nonempty interval of weights with finite canonical forcing

The critical weight \(4^{r(n)}\) is no longer necessary for the
divergence argument. Choose

\[
0<\alpha<\frac1{40},\qquad \rho=4^\alpha.
\tag{42}
\]

The elementary binary inequality \(4^{r(n)}\le3n+1\) and the exact
canonical charge give

\[
d(n)w_\rho(n)
\le \frac{h(n)}{(3n+1)^{1-\alpha}}
\le 3^{\alpha-1}\frac{\nu(n)}{n^{1-\alpha}}.
\tag{43}
\]

The imported moment (19) of PR185, with \(s=1-\alpha>39/40\), therefore
proves the explicit finite bound

\[
\boxed{\sum_n d(n)\rho^{r(n)}
\le B_\alpha:=
\frac{5\,3^{\alpha-1}(1-\alpha)A}{1/40-\alpha}<\infty.}
\tag{44}
\]

Thus every weight in
\(1<\rho<4^{1/40}\) has finite actual canonical forcing, while (41)
would make its terminal energy diverge on any escaping component.
The finite number in (44) weights the original charge once; it is not
permission to attach the same weight anew after transport.

The argument proving (2) no longer forces divergence below \(\rho=4\):
on its explicit fiber, the corresponding lower bounds form a geometric
series with ratio \(\rho^3/64<1\).
This does not prove convergence of the actual subcritical fiber moment.
Harmonicity gives a summable \(\nu(n_j)\) tail, without the exponential
upper estimate needed to make that further assertion.

### The exact remaining multiplication and transport commutators

For clarity, the residual can be written entirely with finite Green
truncations and bounded weights, before any limit is taken.
Let

\[
f=\mathcal R_M=\sum_{i=0}^{M-1}K^ig,\qquad
w=w_{\rho,L}.
\]

Then \(f\in\mathcal H\), \(0\le f\le1\), and
\((I-K)f=g-K^Mg\).
For \(N\ge1\), define

\[
\mathcal Q_{N,M}(w)=\frac1N
\sum_{\tau(x)>N}\nu(x)w(U^Nx)|f(x)-f(U^Nx)|^2.
\tag{45}
\]

All terms below are absolutely finite at fixed \(M,N,L\).
Adjointness and the identity
\((I-K^N)f=\sum_{j<N}K^j(I-K)f\) give

\[
\begin{split}
N\mathcal Q_{N,M}(w)
={}&2\sum_{j=0}^{N-1}
 \langle\mathsf C^j(wf),\,g-K^Mg\rangle_\nu\\
&+\langle\mathsf C^Nw-w,\,f^2\rangle_\nu.
\end{split}
\tag{46}
\]

For example, expand the square in (45). Its three terms regroup to
\(\langle w,K^Nf^2-2fK^Nf+f^2\rangle_\nu\); this equals
\(2\langle wf,(I-K^N)f\rangle_\nu+
\langle\mathsf C^Nw-w,f^2\rangle_\nu\).
The killed indicator is built into every \(\mathsf C^j\), including
\(\mathsf C^Nw\), so no boundary contribution is silently added.

Separate the static canonical forcing by defining

\[
\begin{split}
\mathfrak C_{N,M}(w)
:={}&\frac2N\sum_{j=0}^{N-1}\sum_xd(x)
 \left[\mathsf C^j(wf)(x)-w(x)\mathsf C^jf(x)\right]\\
&+\frac1N\sum_x\nu(x)f(x)^2
 \left[\mathsf C^Nw(x)-w(x)\right].
\end{split}
\tag{47}
\]

Equation (46) becomes the exact identity

\[
\begin{split}
\mathcal Q_{N,M}(w)
={}&\frac2N\sum_{j<N}\sum_x d(x)w(x)\mathsf C^jf(x)
+\mathfrak C_{N,M}(w)\\
&-\frac2N\sum_{j<N}
 \langle\mathsf C^j(wf),K^Mg\rangle_\nu.
\end{split}
\tag{48}
\]

The last term is nonpositive. The first term is at most \(2B_\alpha\)
by (44), uniformly in \(M,N,L\). Consequently

\[
\boxed{\mathcal Q_{N,M}(w_{\rho,L})
\le2B_\alpha+\mathfrak C_{N,M}(w_{\rho,L}).}
\tag{49}
\]

The first line of (47) is the actual failure of multiplication by the
run weight to commute with forward transport:
on a retained \(j\)-step path it equals
\[
\frac2N d(x)
\bigl(w(U^jx)-w(x)\bigr)f(U^jx)
\]
inside the time sum. The second line is the weighted boundary drift.
Neither has a proved sign or an adequate uniform upper bound here.
Their one-step version includes the sibling correlation in (28)--(29).
This is an explicit calculation on the canonical functions and original
charges, not a statement about arbitrary model kernels.

As \(M\) increases, \(f\) tends pointwise to \(\mathcal R\).
For bounded \(w\), Fatou gives
\(\sum_qw(q)\mathfrak e_N(q)\le
\liminf_M\mathcal Q_{N,M}(w)\).
No equality of the limiting signed terms in (46)--(48) is asserted:
the finite-Green energy defect in PR180 is precisely a reason to retain
this qualification.

The finite forcing estimate (44) therefore pays one genuine part of the
terminal bound. The unresolved part is the canonical commutator (47),
with its forward run-weight correlation and its killed-boundary drift.
The inspected estimates do not bound it uniformly in the required limits.
The ESS improvement opens an interval of admissible weights and supplies
(40)--(41); it does not, by itself, prove vanishing of \(b_\infty\).
