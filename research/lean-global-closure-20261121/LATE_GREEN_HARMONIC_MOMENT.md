# A global harmonic moment for the canonical Green occupation

Date: 2026-11-22. **Status: new written deduction from the frozen harmonic
inputs below. Full Collatz remains OPEN.** The new result is an ordinary
global upper estimate for the normalized **complete** Green history:
its harmonic moment is finite, and it has a quantitative ordinary mean
decay. The transported seed and all its endpoint collisions are retained.

This result was obtained after the late PR182 and PR178 continuations.
The complete Green identity, canonical escape label, and its polynomial
rigidity interface are credited to PR182. The new argument combines them
with the whole-predecessor floor comparison and the finite orbit count;
it is not a replay of their proofs.

## 1. Frozen inputs and exact domain

Use the accelerated odd map \(U\). Let \(\mathcal N\) be the positive
odd ternary units that are not themselves periodic. A state in this
domain may later enter a cycle. Forward transport is killed on its first
periodic state.

| Source | Frozen head | Exact input |
|---|---|---|
| PR175 | 2bc2ad37b490a5aea63658eaf657bc048da4532e | CANONICAL_POTENTIAL_SUPERLEVELS.md, finite-chain bound including convergent preperiods; LITERATURE_TRANSPORT_ATTEMPT.md, reciprocal-path correction. Both in research/lean-global-closure-20261121/. |
| PR185 | 276be8154f4e867acc0230466b34d9cb224aacf5 | research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md, equations (12), (15), (16): ordinary harmonic correction and whole-predecessor floor comparison. |
| PR182 | 9dacd610ba7735e89e2e29e4ab01795983317980 | research/lean-dyadic-descent-20261121/HARMONIC_CAPTURE_BRIDGE.md: complete Green identity for the unchanged seed; CANONICAL_ESCAPE_LABEL.md: its component limit; INVARIANT_CORRELATION.md: polynomial rigidity, used only when explaining the attempted closing transfer. |
| PR178 | d06f97d955152edeeeb7acd5295d57aec9f4fb9c | research/global-synthesis-20261122/ORDINARY_MASS.md, (Q5)--(Q10): escape forces the stated first-minimum lower bounds; used only in the completion attempt. |

Write
\[
h(q)=G(q)/q,\quad
\lambda(q)=\frac{3q}{3q+1},\quad
d(q)=(1-\lambda(q))h(q),\quad
(Lf)(q)=\sum_{U(n)=q}f(n).
\]
The pinned harmonic construction supplies
\[
L(\lambda h)=h,\qquad
\nu=\lim_{j\to\infty}L^j h,\qquad
L\nu=\nu,\qquad 0<h\le\nu<\infty.
\tag{1}
\]
Its existence retains the source-qualified analytic inputs of the source
packet. No such hypothesis is installed as a Lean axiom here.

For a target \(q\in\mathcal N\), let
\[
\operatorname{Pred}(q)=\{n\in\mathcal N:U^j(n)=q
                                      \text{ for some }j\ge0\}.
\]
This set includes \(q\). If its whole domain lies above \(m\ge1\),
the existing finite-chain correction gives
\[
\frac{h(q)}{\nu(q)}\ge
\delta_m:=\exp\!\left(-\frac{200}{3}m^{-1/40}\right).
\tag{2}
\]
A minimum of a later forward suffix cannot be substituted for this
whole-predecessor hypothesis.

The elementary orbit count, including the possible preperiod of a
convergent orbit, is
\[
\#\{n\le X:n\in\mathcal N
          \text{ lies on one supplied forward orbit}\}
 \le5X^{39/40}\qquad(X\ge1).
\tag{3}
\]
The proof of (3) and the reciprocal-path bound used in (2) do not require
the uniform predecessor-population theorem. Once (1)--(2) are supplied,
the new estimate below uses neither its population constant nor a
stationary-density approximation.

## 2. A pointwise bound by the least actual predecessor

Put
\[
R(q)=1-\frac{\lambda(q)h(q)}{\nu(q)}\in[0,1],
\qquad
a(q)=\min\operatorname{Pred}(q).
\tag{4}
\]
The minimum exists in the positive ordinary integers and satisfies
\(1\le a(q)\le q\). Every actual inverse history of \(q\) lies in
this predecessor set, so (2) applies with exactly this \(a(q)\).

Since \(\lambda(q)\ge3a(q)/(3a(q)+1)\) and
\(1-e^{-u}\le u\),
\[
\begin{aligned}
R(q)
&\le1-\frac{3a(q)}{3a(q)+1}\delta_{a(q)}\\
&\le\frac1{3a(q)+1}
       +\frac{200}{3}a(q)^{-1/40}\\
&\le\boxed{67\,a(q)^{-1/40}.}
\end{aligned}\tag{5}
\]
The estimate can exceed one at small \(a(q)\); the separate bound
\(R\le1\) is retained.

Consequently, for \(0<t\le1\), every root with \(R(q)\ge t\)
lies on the actual forward orbit of some
\[
a\le(67/t)^{40}.
\]
The selected root is a real predecessor of \(q\), not a formal residue
or a changing finite witness. Taking a union over these finitely many
ordinary seeds and applying (3) gives
\[
\boxed{
N_t(X):=\#\{q\in\mathcal N:q\le X,\ R(q)\ge t\}
 \le\min\left(X,\ 5\cdot67^{40}\,t^{-40}X^{39/40}\right).
}\tag{6}
\]
Different seed orbits may overlap. An upper bound by the sum of their
counts is valid with those collisions included; disjointness is neither
claimed nor needed.

## 3. Global moments and an explicit ordinary mean rate

Set
\[
\eta=\frac1{1600},\qquad
C_R=\frac{40}{39}\,67\,5^{1/40}.
\]
Then
\[
\boxed{
\sum_{\substack{q\in\mathcal N\\q\le X}}R(q)
 \le C_R X^{1599/1600}\qquad(X\ge1).
}\tag{7}
\]

Indeed, use the finite layer-cake identity
\(\sum R(q)=\int_0^1N_t(X)\,dt\). Put
\[
t_0=67\,5^{1/40}X^{-1/1600}.
\]
If \(t_0\ge1\), the bound by \(X\) proves (7). Otherwise split
the integral at \(t_0\). The identity
\(5\cdot67^{40}X^{39/40}=Xt_0^{40}\) gives
\[
\sum R(q)
\le Xt_0+
 5\cdot67^{40}X^{39/40}\frac{t_0^{-39}-1}{39}
\le\frac{40}{39}Xt_0.
\]
This proves (7), including its constant.

For every \(0<p<40\), the same calculation with
\(p\int_0^1t^{p-1}N_t(X)\,dt\) gives
\[
\boxed{
\sum_{\substack{q\in\mathcal N\\q\le X}}R(q)^p
 \le C_p X^{1-p/1600},\qquad
C_p=\frac{40}{40-p}\,67^p5^{p/40}.
}\tag{8}
\]
Thus, for \(s>1-p/1600\),
\[
\boxed{
\sum_{q\in\mathcal N}\frac{R(q)^p}{q^s}
 \le\frac{sC_p}{s-1+p/1600}.
}\tag{9}
\]
This follows by the nonnegative identity
\(q^{-s}=s\int_q^\infty X^{-s-1}\,dX\). All exchanges are
Tonelli exchanges or finite sums.

In particular,
\[
\boxed{\sum_{q\in\mathcal N}\frac{R(q)}q\le1600C_R<\infty.}
\tag{10}
\]
Every positive power of \(R\) also has a finite harmonic moment:
for \(0<p<40\), (9) at \(s=1\) gives \(1600C_p/p\);
for \(p\ge40\), use \(R^p\le R\).

## 4. Complete unchanged-source Green occupation

PR182's new Green identity is
\[
W(q):=\sum_{k\ge0}L^kd(q)
     =\nu(q)-\lambda(q)h(q)=\nu(q)R(q).
\tag{11}
\]
For the same original source seed
\[
a_0(n)=h(n)/n=(3+1/n)d(n),\qquad b_k=L^ka_0,
\]
that source proves
\[
3R(q)\le\sum_{k\ge0}\frac{b_k(q)}{\nu(q)}
                         \le4R(q).
\tag{12}
\]
Equation (12) counts the entire history, including time zero, with every
original source mass unchanged and all endpoint collisions retained.

Combining it with (10) gives the new global all-time estimate
\[
\boxed{
\sum_{k\ge0}\sum_{q\in\mathcal N}
 \frac{L^ka_0(q)}{\nu(q)\,q}
 \le6400C_R<\infty.
}\tag{13}
\]
Nonnegativity justifies the order of the two sums. Formulae (8)--(9)
also apply to the normalized complete occupation in (12), with constants
multiplied by \(4^p\).

The spatial factor \(1/q\) in (13) is still essential. Along an
escaping orbit \(q_k\), an original atom of mass \(w>0\) contributes
\(w/(\nu(q_k)q_k)\), not a fixed positive cost per step.
The pinned path count already permits its reciprocal sum to be finite.
Thus (13) is a genuine upper bound, but not an unweighted occupation
or absorption theorem.

## 5. Direction of the Green drift

Let \(K_\nu(q,n)=1_{U(n)=q}\nu(n)/\nu(q)\). The exact identity
\(W=d+LW\) implies
\[
\boxed{K_\nu R=R-d/\nu.}\tag{14}
\]
Thus \(R\) is superharmonic for the inverse kernel. It is not licensed
as a nondecreasing function along each actual forward edge.

For an edge \(U(q)=q'\) remaining in \(\mathcal N\), exact subtraction
gives
\[
R(q')-R(q)=
\frac{d(q')+
 \sum_{\substack{U(n)=q'\\n\ne q}}
       \nu(n)\,[R(n)-R(q)]}{\nu(q')}.
\tag{15}
\]
The side-branch term has no sign supplied by the present estimates.
The two quantities \(W(q)\) and \(\nu(q)\) separately increase along
that edge, but the quotient need not inherit an order from that fact.
No forward monotonicity of \(R\) is used in this packet.

## 6. The ordinary extension has finite harmonic mass

Set \(R=0\) on periodic odd units. For each positive integer \(n\),
let \(\rho(n)\) be its first future odd ternary unit: take its odd
part if that is a unit, or its next accelerated odd value otherwise.
Define
\[
r(n)=R(\rho(n)).
\tag{16}
\]
This is the same extension convention used for the new canonical escape
label. It does not make \(r\) invariant.

Grouping first by odd part multiplies a harmonic sum by two. At an odd
nonunit \(x\) with \(U(x)=q\), write
\(x=(2^eq-1)/3\). For its legal positive value,
\[
1/x=\frac3{2^eq-1}\le\frac6{2^eq}.
\]
Sum over all \(e\ge1\); this also bounds the subset giving nonunits.
Consequently
\[
\boxed{
\sum_{n\ge1}\frac{r(n)}n
 \le14\sum_{q\in\mathcal N}\frac{R(q)}q
 \le22400C_R.
}\tag{17}
\]
All functions are nonnegative, and all rearrangements are justified.

In particular \(r\) is an ordinary Besicovitch-null sequence. For a
nonnegative function with finite harmonic mass, split its ordinary mean
at a fixed \(M\):
\[
X^{-1}\sum_{n\le X}r(n)
\le X^{-1}\sum_{n\le M}r(n)
       +\sum_{n>M}r(n)/n.
\]
First let \(X\) increase, then \(M\) increase. Its logarithmic mean
also tends to zero, with numerator bounded by (17).

## 7. Attempted transfer to the invariant escape label

For a nonnegative function \(f\) of finite harmonic mass, the actual
shortcut inverse fibers give
\[
\begin{aligned}
\sum_{n\ge1}\frac{f(Tn)}n
 &=\sum_{q\ge1}\frac{f(q)}{2q}
   +\sum_{\substack{q\ge2\\q\equiv2\ (3)}}
                       \frac{3f(q)}{2q-1}\\
 &\le\frac52\sum_{q\ge1}\frac{f(q)}q.
\end{aligned}\tag{18}
\]
The odd-parent bound uses \(3/(2q-1)\le2/q\) for \(q\ge2\).
Every fixed iterate \(r(T^kn)\), and every fixed finite time average,
therefore retains finite harmonic mass and is Besicovitch-null.

For each fixed \(0<\alpha<1\), the Abel average
\[
A_\alpha(n)=(1-\alpha)\sum_{k\ge0}\alpha^k r(T^kn)
\tag{19}
\]
is likewise Besicovitch-null. Its finite partial sums are null; its
uniform tail is at most \(\alpha^K\), since \(0\le r\le1\).
This conclusion for all fixed \(\alpha<1\) does not require extending
the harmonic bound in (18) through its divergent geometric range.

PR182 proves that on each escaping component
\[
R(U^kq)\longrightarrow F_{\mathcal C}
   =D_{\mathcal C}/C_{\mathcal C}>0.
\]
On each eventually periodic orbit the extension (16) is eventually zero.
Thus
\[
r(T^kn)\longrightarrow\widetilde F(n)
\]
pointwise for every positive ordinary source. The finite Cesàro averages
and the Abel averages (19), as their time parameter tends to its limit,
also converge pointwise to that specific invariant escape label.

This does **not** establish ordinary mean approximation of
\(\widetilde F\). It gives bounded pointwise limits of null sequences,
not convergence in the ordinary Besicovitch seminorm. Dominated
convergence for a fixed finite measure cannot be applied while the
ordinary source cutoff itself tends to infinity.

The five-energy attempt exposes the missing uniform estimate directly.
Use the repository's exact domain
\[
E_5(f)=\sum_{\substack{n>0\text{ odd}\\3\nmid n}}
                 \frac{|f(5n)-f(n)|}{n},
\qquad \|f\|_H=\sum_{n\ge1}|f(n)|/n.
\]
The same upper estimate also holds if the energy is summed over all
positive integers. The triangle inequality gives
\[
E_5(f)\le6\|f\|_H.
\]
For
\(C_N=N^{-1}\sum_{k=0}^{N-1}r\circ T^k\), (18) only yields
\[
\boxed{
E_5(C_N)\le
6\|r\|_H\,\frac{(5/2)^N-1}{(3/2)N}.
}\tag{20}
\]
Each energy is finite, but the bound grows exponentially. Fatou at
\(C_N\to\widetilde F\) supplies no finite limiting five energy.
A bound uniform in \(N\), or any independently proved mean approximation
of \(\widetilde F\), would be a substantive new closing estimate.

Indeed, if an escaping unit \(a\) exists, PDU gives
\[
\liminf_X\frac1X\sum_{n\le X}\widetilde F(n)
 \ge(c/a)\widetilde F(a)>0.
\]
For every fixed Abel or finite Cesàro approximant above, its ordinary
mean is zero, so its lower mean absolute error from \(\widetilde F\)
is exactly the lower mean of \(\widetilde F\), hence positive.
The latter assertion follows from
\(\big||\widetilde F-A|-\widetilde F\big|\le A\).
This is an exact failure of the proposed limit transfer if an escape
exists, not a proof that an escape does exist.

## 8. Attempted transfer to the new minimum bound

PR178 proves, conditional on its pinned PDU input, that an escaping
orbit forces
\[
\sum_{n\le X}m(n)\gg X\log X.
\]
The sums are over original odd units and \(m(n)\) is their actual
future minimum. A subsequence with this sum \(o(X\log X)\) would
therefore exclude all escapes.

The new upper bound (13) does not supply that missing minimum weight.
Even a pointwise charge \(m(n)\le C R(n)\) fails on a known convergent
basin. For example, the explicit odd units
\[
n_j=(5\cdot2^{6j+3}-1)/3,\qquad j\ge0,
\]
are unbounded and satisfy \(U(n_j)=5\), followed by \(U(5)=1\).
Through these ancestors of the nonperiodic target five,
\(m(n)=1\) but \(a(n)=\min\operatorname{Pred}(n)\to\infty\):
otherwise one of finitely many bounded sources would have infinitely
many distinct pre-hit states before its unique hit of five. Formula (5)
therefore gives \(R(n_j)\to0\). The explicit family makes this
counterexample independent of the predecessor-population theorem.

The complete Green sum has a spatial reciprocal cost; the minimum
estimate needs a growing ordinary minimum cost. No inequality paying
that difference has been proved. The all-exponent fixed-profile
obstruction already pushed in PR175 also does not furnish regularity
of \(R\), its orbit limit, or the minimum: it excludes a particular
nonzero finite-period asymptotic form, not arbitrary irregular traces.

The positive new outputs of this late synthesis are (5)--(10), the
complete unchanged-source occupation bound (13), and the harmonic
ordinary extension (17). The computed five-energy transfer (20) and
the source-minimum counterexample state exactly where the attempted full
completion stops. Eventual periodic cycles were killed at the domain
boundary throughout; their exclusion remains a separate obligation.
