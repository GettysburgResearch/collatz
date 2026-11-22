# The full source charge at a moving inverse clock

**Status: a new written global theorem for the canonical Green potential,
conditional on the explicitly pinned ordinary harmonic construction.**
It gives a uniform profile for every inverse cutoff, including cutoffs chosen
adaptively along the actual forward orbit, and identifies the exact energy
defect of finite Green approximation. It does not prove that this defect
vanishes, exclude nontrivial periodic cycles, or complete Collatz.
The energy statement is a new explicit canonical Green corollary of the
existing Green and Wold inputs, not an elimination estimate.

The direct closing attack in Section 6 concerns arithmetic siblings of actual
orbit points. Its required lower estimate is not established. That attempt
is distinct from the proved profile theorem.

## 1. Pinned inputs and the precise domain

Let \(N\) be the positive odd ternary units that are not themselves periodic
under the accelerated odd map \(U\). Forward transport is killed upon first
entering a periodic vertex. Preperiodic points remain in \(N\) until that time.
Write

\[
(La)(q)=\sum_{n\in N:Un=q}a(n),\quad
\lambda(n)=\frac{3n}{3n+1},\quad h(n)=G(n)/n,\quad
d(n)=(1-\lambda(n))h(n).
\tag{1}
\]

The frozen ordinary harmonic construction supplies

\[
L\nu=\nu,\qquad 0<\delta\nu\le h\le\nu\le A,\qquad
D:=\sum_{n\in N}d(n)<\infty.
\tag{2}
\]

The same construction gives \(G(n)\ge\gamma>0\) on \(N\).
Its critical inverse operator is
\[
(Pf)(q)=\sum_{n\in N:Un=q}
          \frac3{2^{v_2(3n+1)}}f(n),\qquad PG=G.
\]
Its source qualifications, including the predecessor-population input, are
retained. Define

\[
Kf=\frac{L(\nu f)}{\nu},\quad g=d/\nu,\quad
R_M=\sum_{j=0}^{M-1}K^jg,\quad
R=\sum_{j\ge0}K^jg=1-\frac{\lambda h}{\nu}\in[0,1].
\tag{3}
\]

The empty sum gives \(R_0=0\). The unchanged-source Green mass is

\[
W(q):=\nu(q)R(q)=\sum_{n\in\operatorname{Pred}(q)}d(n),
\tag{4}
\]

where the predecessor set includes \(q\). A nonperiodic point cannot be
visited twice, so (4) counts each original source exactly once.

For each escaping ordinary component \(C\), the pinned construction gives

\[
C_C=\lim_{k\to\infty}\nu(U^kx)>0,\quad
D_C=\sum_{n\in C}d(n)>0,\quad
\lim_{k\to\infty}R(U^kx)=D_C/C_C.
\tag{5}
\]

In particular \(D_C/C_C\le1\). On an eventually periodic component, the killed
forward value is eventually zero.

| Source | Frozen pin and exact use |
|---|---|
| PR185 | 53f01ca5b443ef57ef2160b4996dbb2cc87f7395, research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md: positive bounded stationary reference, canonical comparison, and finite charge. |
| PR175 | 728389c2ad4796853948250a90188b0697483d92, research/lean-global-closure-20261121/LITERATURE_DIRICHLET_BOUNDARY.md: complete Green identity, finite Green energy, weak convergence of gradients, and exact boundary identity (16) below. |
| PR183 | 68345f60a4f757acb42a69a4ac95910f8ce26163, research/profound-step-20261122/operator/WOLD_CHANNELS.md: ordinary component clocks, synchronous classes, their capacity, and the exact unitary projection. |

No assertion that \(R\) belongs to \(\ell^2(N,\nu)\) is used. No ordinary
pointwise convergence of the ternary densities \(D_t=P^t1\) is assumed.

## 2. Uniform profile at every cutoff

Fix an escaping original source \(x\), put \(q_k=U^kx\), and choose the
integer clock on its component \(C\) normalized by

\[
\ell_x(x)=0,\qquad \ell_x(Un)=\ell_x(n)+1.
\tag{6}
\]

Concretely, if \(U^in=U^jx\), set \(\ell_x(n)=j-i\). Any later meeting adds
the same amount to both clocks; absence of a cycle makes this independent
of the chosen meeting. For each fixed \(n\in C\), sufficiently large \(k\)
satisfies

\[
U^{\,k-\ell_x(n)}n=q_k.
\tag{7}
\]

Define the cumulative charge profile, for every integer \(s\), by

\[
\Phi_x(s)=\sum_{\substack{n\in C\\\ell_x(n)>-s}}d(n).
\tag{8}
\]

### Theorem 1: exact finite formula and uniform error

For every pair of nonnegative integers \(k,M\),

\[
\nu(q_k)R_M(q_k)=
\sum_{\substack{n\in\operatorname{Pred}(q_k)\\
                 \ell_x(n)>k-M}}d(n),
\tag{9}
\]

and consequently

\[
\boxed{
0\le\Phi_x(M-k)-\nu(q_k)R_M(q_k)
\le D_C-W(q_k)\longrightarrow0.}
\tag{10}
\]

The upper error is independent of \(M\). This is uniform over all cutoffs.

**Proof.** The identity \(\nu K^jg=L^jd\) retains every original source and
every collision. A source in \(\operatorname{Pred}(q_k)\) contributes at its
unique hitting time \(j=k-\ell_x(n)\). The inequality \(j<M\) is exactly the
strict clock inequality in (9). Comparing (9) with (8), the omitted terms
are a subset of \(C\setminus\operatorname{Pred}(q_k)\), whose total charge is
\(D_C-W(q_k)\).

These predecessor sets increase with \(k\) and exhaust \(C\): every source
in the same ordinary component eventually joins this actual forward tail.
Finite total charge gives \(W(q_k)\to D_C\) by monotone convergence. No
source is resampled, and mergers are not required to have equal clocks.
\(\square\)

Dividing by \(\nu(q_k)\), using \(\nu(q_k)\ge\nu(x)>0\) and (5), gives

\[
\boxed{
\sup_{M\ge0}\left|R_M(q_k)-\frac{\Phi_x(M-k)}{C_C}\right|
\longrightarrow0.}
\tag{11}
\]

Thus for an arbitrary sequence of integer cutoffs \(M_k\ge0\), including
one chosen from the observed orbit,

\[
\begin{array}{c|c}
\text{cutoff offset}&\lim_kR_{M_k}(q_k)\\\hline
M_k-k\to-\infty&0\\
M_k-k\to s\in\mathbb Z&\Phi_x(s)/C_C\\
M_k-k\to+\infty&D_C/C_C.
\end{array}
\tag{12}
\]

Convergence to a finite integer means eventual equality. If offsets
oscillate, (11), rather than an unjustified single limit, describes their
full profile.

At the central cutoff \(M=k\), the omitted charge contains the original
atom \(d(x)\):

\[
\lim_{k\to\infty}\bigl(R(q_k)-R_k(q_k)\bigr)
=\frac1{C_C}\sum_{\ell_x(n)\le0}d(n)
\ge\frac{d(x)}{C_C}>0.
\tag{13}
\]

An excess clock tending to infinity recovers this positive charge; it does
not make the complete charge vanish.

## 3. Global profile with all original charges retained

Choose any integer clock \(h_C\) on each escaping component. For \(s\in\mathbb Z\),
put

\[
\mathcal B(s)=
\sum_{C\ {\rm escaping}}\frac1{C_C}
\sum_{x,n\in C}d(x)d(n)
\mathbf1_{\{h_C(n)-h_C(x)>-s\}}.
\tag{14}
\]

All terms are nonnegative. The expression is independent of the additive
choice of clock and is at most

\[
b_\infty:=\sum_{C\ {\rm escaping}}D_C^2/C_C\le D.
\tag{15}
\]

The exact PR175 boundary theorem identifies this same quantity by

\[
\mathcal D(R)=2\sum_xd(x)R(x)-b_\infty,\qquad
\lim_{N\to\infty}N\mathcal D(A_NR)=b_\infty.
\tag{16}
\]

Here \(A_N=N^{-1}\sum_{j<N}C^j\), with \(C\) the killed forward-composition
isometry, and \(\mathcal D(f)=\|(I-C)f\|_{\ell^2(\nu)}^2\) whenever this
gradient is square summable. The operator \(C\) is distinguished by context
from an ordinary component.

### Theorem 2: uniform global original-source profile

With a killed term interpreted as zero,

\[
\boxed{
\sup_{M\ge0}\left|
\sum_{x\in N}d(x)R_M(U^kx)-\mathcal B(M-k)
\right|\longrightarrow0.}
\tag{17}
\]

**Proof.** For each escaping \(x\), (11) makes the supremum error over \(M\)
tend to zero. Both functions compared lie in \([0,1]\). For an eventually
periodic \(x\), the killed term is zero for all \(M\) once \(k\) exceeds
its killing time, and the profile is zero. Dominated convergence with the
fixed finite original measure \(d(x)\) bounds the supremum of the summed
error by a quantity tending to zero. Expanding the component profiles gives
exactly (14). No Haar density, source reweighting, or uncontrolled double
limit is used. \(\square\)

Equation (17) covers every moving sequence \(M_k\) globally. Its profile
increases from zero to \(b_\infty\) as the offset increases from minus
infinity to plus infinity.

## 4. The synchronous charge defect

For each escaping component, let

\[
d_{C,r}=\sum_{\substack{n\in C\\h_C(n)=r}}d(n),\qquad
E_{\rm sync}=
\sum_{C\ {\rm escaping}}\frac1{C_C}\sum_{r\in\mathbb Z}d_{C,r}^2.
\tag{18}
\]

The whole charge on one synchronous class is squared. Distinct original
sources that merge at the same clock are therefore not separated falsely.
All asynchronous comparisons remain in (14).

The two strict orderings of a pair of integer clocks have equal charge
by symmetry. The equal-clock region has charge (18). Consequently,

\[
\boxed{
\mathcal B(0)=\frac{b_\infty-E_{\rm sync}}2,\qquad
\mathcal B(1)=\frac{b_\infty+E_{\rm sync}}2.}
\tag{19}
\]

At offset one, the strict integer inequality in (14) becomes
\(h_C(n)\ge h_C(x)\). All rearrangements are of nonnegative summable terms,
and

\[
0\le E_{\rm sync}\le b_\infty\le D.
\tag{20}
\]

Strict positivity of the canonical charge at every vertex means that
one escaping component makes both \(E_{\rm sync}\) and \(b_\infty\)
strictly positive.

### Theorem 3: exact energy defect of finite Green approximation

The finite Green truncations satisfy

\[
\boxed{
\lim_{M\to\infty}\mathcal D(R_M)=\mathcal D(R)+E_{\rm sync},
\qquad
\lim_{M\to\infty}\mathcal D(R-R_M)=E_{\rm sync}.}
\tag{21}
\]

**Proof.** Each \(R_M\) belongs to \(\ell^2(N,\nu)\), and
\((I-K)R_M=g-K^Mg\). The isometry/adjoint identity gives

\[
\mathcal D(R_M)=
2\langle R_M,g\rangle_\nu-2\langle R_M,K^Mg\rangle_\nu.
\tag{22}
\]

For the Hilbert-space membership explicitly: \(0\le R_M\le1\) and
\(\|R_M\|_{L^1(\nu)}\le MD\), since \(K\) contracts nonnegative
\(L^1(\nu)\) mass. Therefore \(\|R_M\|_2^2\le MD\). Similarly
\(0\le g\le1\) and \(\sum\nu g=D\) give \(g\in\ell^2(N,\nu)\).

The first inner product tends to \(\sum_xd(x)R(x)\). Keeping the original
sources in the second gives exactly

\[
\langle R_M,K^Mg\rangle_\nu
=\sum_xd(x)R_M(U^Mx)\longrightarrow\mathcal B(0)
\tag{23}
\]

by (17) at \(k=M\). Equations (16), (19), and (22) prove the first limit.

Put \(a_M=(I-C)R_M\) and \(a=(I-C)R\). The uniform bound
\(\|a_M\|^2\le2D\) and coordinate convergence give weak convergence
\(a_M\rightharpoonup a\) in \(\ell^2(N,\nu)\), also proved in the pinned
PR175 argument. Thus

\[
\|a-a_M\|^2
=\|a\|^2+\|a_M\|^2-2\langle a,a_M\rangle
\longrightarrow E_{\rm sync},
\]

which is the second limit. \(\square\)

The monotone pointwise convergence \(R_M\uparrow R\) therefore does not
by itself give convergence in this energy. Under the pinned inputs,
\(\mathcal D(R-R_M)\to0\) is equivalent to exclusion of escaping components.
This is an identification of the remaining statement, not its proof.

### Existing Wold interpretation

PR183 already identifies the maximal unitary subspace as
\(\bigoplus_C\ell^2(\mathbb Z,C_C)\), over escaping components, and gives
the exact projection of a source density. Its equations W9--W10 applied
to \(g=d/\nu\) give

\[
\|\Pi_{\rm u}g\|_\nu^2=E_{\rm sync},\qquad
\lim_{M\to\infty}\|K^Mg\|_\nu^2=E_{\rm sync}.
\tag{24}
\]

These are credited consequences of the existing Wold identification,
not a new classification or an assertion that the isometry is pure.
The new conclusion (21) identifies exactly that same source sector as the
defect in canonical finite Green energy approximation; (10)--(17) give its
uniform moving-clock charge profile before any Hilbert-space projection.

## 5. Interaction with the new moving-clock estimate

The separate contact-law argument controls the canonical excess
\(P^rV-G\) after an excess inverse clock. That conclusion is compatible
with (12): the complete Green charge tends to \(D_C/C_C\), and its global
original-source pairing tends to \(b_\infty\), as the excess clock grows.
The two approximations concern different residuals.

In particular, tight first-contact endpoints, tight centered hitting time,
and small excess \(P^rV-G\) do not imply a zero escaping Green boundary.
They do not charge the positive term in (13). Equations (17)--(21) locate
exactly what an additional arithmetic estimate must remove. They preserve
the original finite charge \(d\), rather than replacing it by a favorable
seed or repeated first-contact resampling.

## 6. Direct attempt: current through arithmetic siblings

This section records the attempted closing inequality; the missing lower
estimate is not a proved result.

For every positive odd ternary unit set \(B(n)=64n+21\). Then \(B(n)\)
is a larger positive odd ternary unit and

\[
3B(n)+1=64(3n+1),\qquad U(B(n))=U(n).
\tag{25}
\]

If \(n\) and \(U(n)\) are retained, \(B(n)\) is retained as well: a periodic
point cannot lead to a nonperiodic point. Stationarity gives the exact
side-current identity

\[
\nu(U(n))-\nu(n)
=\sum_{\substack{Um=U(n)\\m\ne n}}\nu(m)\ge\nu(B(n)).
\tag{26}
\]

For a retained path \(q_j=U^jx\), define the complete relative side current
\[
\Lambda_j=
\frac{\sum_{Um=q_{j+1},\,m\ne q_j}\nu(m)}{\nu(q_j)}.
\]
There is an exact finite logarithmic telescope,

\[
\boxed{
\sum_{j<N}\log(1+\Lambda_j)
=\log\frac{\nu(q_N)}{\nu(x)}
\le\log\frac A{\nu(x)}.}
\tag{27}
\]

For an escaping path, the unnormalized complete side current sums to
\(C_C-\nu(x)\). Since \(\nu(q_j)\ge\nu(x)\), it follows that

\[
\sum_{j\ge0}\frac{\nu(B(q_j))}{\nu(q_j)}
\le\frac{C_C-\nu(x)}{\nu(x)}<\infty.
\tag{28}
\]

The canonical comparison (2) and \(B(n)/n\le85\) imply

\[
\boxed{
\sum_{j\ge0}\frac{G(64q_j+21)}{G(q_j)}
\le\frac{85}{\delta}
    \frac{C_C-\nu(x)}{\nu(x)}<\infty.}
\tag{29}
\]

Meanwhile every point on the same path has the persistent linear spike
\(G(q_j)\ge\delta\nu(x)q_j\). A nonsummability theorem for (29), specifically
along actual persistent spikes, would therefore contradict escaping
capacity directly. A relative lower estimate between these distinct
inverse subtrees is not supplied by \(PG=G\) or \(L\nu=\nu\).

The available absolute floor gives only \(\nu(B(q_j))\ge\gamma/B(q_j)\).
That lower series is compatible with the already proved finite reciprocal
sum along a nonperiodic orbit. At first crossings of successively doubled
heights it is geometrically small. Existing negative moments and finite
total charge provide no relative comparison between \(G(B(q_j))\) and
\(G(q_j)\) at those crossings.

A direct identical-word inverse-tree embedding fails arithmetically.
If a depth-\(r\) word has affine formula
\(F_w(z)=(3^rz+c_w)/2^a=n\), applying that same word to reach \(B(n)\)
would require

\[
z'=64z+\frac{21(3c_w+2^a)}{3^r}.
\tag{30}
\]

The numerator of the correction has ternary valuation exactly one, since
\(3c_w+2^a\) is a ternary unit. For \(r\ge2\) this is not an ordinary
integer. An adaptive change of inverse words with controlled canonical
mass is needed.

The full arithmetic cost can also be calculated. For \(j\ge1\), preserving
this same depth-\(r\) affine word while replacing \(n\) by \(B^j(n)\) requires

\[
z_j=64^jz+
\frac{(64^j-1)(3c_w+2^a)}{3^{r+1}}.
\tag{31}
\]

Since \(v_3(64^j-1)=2+v_3(j)\), integrality is equivalent to
\(3^{r-1}\mid j\). Thus even the first possible integer lift costs a
height factor \(64^{\,3^{r-1}}\). Requiring the oldest source to remain a
ternary unit can impose an additional residue condition; \(3^r\mid j\)
is sufficient to preserve that unit status as well. This is a lower cost
obstruction to direct deep-prefix copying, not an assertion that every
integral lift retains all domain conditions.

### A weaker multiscale comparison that would suffice

The stopped-mixing lane independently found the sibling-current attack
and supplied the following sharper version. Set

\[
\mathscr L_G(n)=
\sum_{j\ge1}64^{-j}\frac{G(B^j(n))}{G(n)}.
\tag{32}
\]

If the actual gap at \(q_i\) is \(e_i\), each \(B^j(q_i)\) is a distinct
unit parent of \(q_{i+1}\), with gap \(e_i+6j\). Positivity and \(PG=G\)
give

\[
\frac{G(q_{i+1})}{(3/2^{e_i})G(q_i)}
\ge1+\mathscr L_G(q_i).
\]

The actual path correction
\(\Lambda_N^{\rm path}=\prod_{i<N}\lambda(q_i)\ge\delta\) therefore yields
the finite product bound

\[
1+\sum_{i<N}\mathscr L_G(q_i)
\le\prod_{i<N}(1+\mathscr L_G(q_i))
\le\frac{h(q_N)}{h(x)\Lambda_N^{\rm path}}
\le\frac{A}{\delta h(x)}.
\tag{33}
\]

Consequently the full multiscale sibling leakage is summable on any
hypothetical escaping path.

An inverse-logarithmic lower comparison restricted to persistent linear
spikes would be enough to contradict (33):

\[
\boxed{
\text{For each }\eta>0,\quad
G(n)\ge\eta n,\ n\ge Q_\eta
\quad\Longrightarrow\quad
\mathscr L_G(n)\ge
\frac{c_\eta}{\log(2+n)},\qquad c_\eta>0.}
\tag{OPEN-S}
\]

Indeed, an escaping path satisfies \(G(q_i)\ge\delta\nu(x)q_i\), while the
actual affine step gives the correct growth bound
\(q_i+1\le(3/2)^i(x+1)\). The lower series in (OPEN-S) would then dominate
a divergent harmonic series. This is substantially weaker than a uniform
one-sibling Harnack ratio, but it is still **unproved**.

There is a concrete finite-obstacle formulation that avoids assuming
ordinary convergence of \(D_t\). Let \(u\) be the canonical unit obstacle,
\(V^{[0]}=u\), \(V^{[r+1]}=\max(u,PV^{[r]})\), and
\(V^{[r]}\uparrow V\). The existing normalization gives
\(G\le V\le2\chi G\). A sufficient finite comparison is: for every
\(\eta>0\), constants \(c_\eta>0,Q_\eta\) independent of \(n,r\) satisfy

\[
\begin{split}
n\ge Q_\eta,\quad V^{[r]}(n)\ge\eta n
\quad\Longrightarrow\quad
\exists J,s<\infty:\quad
\sum_{j=1}^{J}64^{-j}V^{[s]}(B^j(n))
\ge\frac{c_\eta V^{[r]}(n)}{\log(2+n)}.
\end{split}
\tag{OPEN-F}
\]

The depths \(J,s\) may depend on the actual \(n,r\); the lower constant
must not. To see sufficiency, choose \(r\) with \(V^{[r]}(n)\ge V(n)/2\)
and apply (OPEN-F) with parameter \(\eta/2\). Its left side is at most
\(2\chi G(n)\mathscr L_G(n)\), and its right side is at least
\(c_{\eta/2}G(n)/(2\log(2+n))\). This gives (OPEN-S) with constant
\(c_{\eta/2}/(4\chi)\).

Neither the finite comparison nor its infinite consequence has been
proved. The identical-word cost (31) is precisely why prefix copying by
itself supplies far too little weighted sibling mass. A finite small
value of \(D_s(B(n))\) is also not an upper bound on all later canonical
values \(G(B(n))\). The attempted closing estimate remains open rather
than being inferred from either of those finite calculations.

The new proved outputs are the uniform source profiles (10), (11), (17)
and the exact defect (21). The \(o(1/N)\) boundary estimate remains open.
The sibling-current attempt records the arithmetic estimate actually
attacked; it is not silently assumed inside a claimed Collatz proof.
