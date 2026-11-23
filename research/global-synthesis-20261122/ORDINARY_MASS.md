# A quantitative first-moment obstruction to every escaping ordinary orbit

**Status: SOURCE-QUALIFIED written deduction.** The new result in this
note is a finite-scale lower bound for the actual forward-orbit minimum,
conditional only on the pinned uniform ordinary predecessor-population
theorem (PDU). It strengthens the qualitative first-moment divergence in
`../literature-reframe-20261122/ORDINARY_RENEWAL.md`. No global upper bound
for that minimum, or full Collatz proof, is claimed.

The decisive quantitative conclusion is this. If even one positive ordinary
orbit escapes, then, with an absolute positive coefficient depending only
on (PDU),

\[
\sum_{\substack{n\le X\\n>0\text{ odd},\ 3\nmid n}}m(n)
 \gg X\log X,
\qquad
\sum_{\substack{n\le X\\n>0\text{ odd},\ 3\nmid n}}\frac{m(n)}n
 \gg (\log X)^2.                                      \tag{Q0}
\]

Here `m(n)` is the smallest **actual future odd value** of `n`. In
particular, the stronger old target of a bounded logarithmic first moment
is not required to exclude escapes: a sublogarithmic first moment already
suffices. Positive cycles remain a separate problem.

## 1. Exact sources and the map

The repository is `GettysburgResearch/collatz`. The following sources were
read at these exact heads:

| PR | Full inspected commit | File and claim used |
|---|---|---|
| 180 | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`, §5, (PDU): uniform finite-scale unit predecessor population. |
| 180 | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`, (M3), (M8), (BUE): canonical envelope, harmonicization, and fixed-basin sublinearity. Used only in the attempted upper-bound discussion below. |
| 180 | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md`, (E10), (E11): every-ordinary-point comparison between the canonical envelope, harmonicization, and critical finite densities. Used only in the upper-bound discussion. |
| 175 | `2bc2ad37b490a5aea63658eaf657bc048da4532e` | `research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md`, (M), (L1), (Lp): global weighted bounds for the normalized canonical potential. Used only in the upper-bound discussion. |
| 185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, (12), (15), (19), (27), (33)--(36): ordinary harmonic reference, retained-source transport, moments, and surviving-atom energy. Used only in the upper-bound discussion. |

The new inequalities (Q4), (Q6), and (Q9) below require **only (PDU)** and
the finite ordinary arithmetic reconstructed here. They do not import the
new stationary normalization, canonical moment estimates, or harmonic
reference as additional hypotheses. The analytic proof of (PDU), including
its use of Tao's nonnegative renewal estimate, remains source-qualified;
this note neither formalizes it nor promotes it to an unconditional axiom.

Write

\[
\mathcal O^*=\{n\in\mathbb N:n>0,\ n\text{ odd},\ 3\nmid n\},
\qquad
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

The map `U` preserves `O*`. For `n` in this set define

\[
m(n)=\min_{j\ge0}U^j(n),
\qquad
B(a)=\{n\in\mathcal O^*:U^j(n)=a\text{ for some }j\ge0\}.
\]

The minimum exists because the orbit is a nonempty set of positive
integers. It is not assumed that a trajectory is bounded or convergent.
For odd unit targets, ordinary shortcut reachability in (PDU) is precisely
the reachability used in this definition of `B(a)`.

After enlarging its onset constant if necessary, (PDU) says that there are
absolute `c>0` and `C>=1` such that

\[
\#(B(a)\cap[1,X])\ge\frac{cX}{a}
\quad(a\in\mathcal O^*,\ X\ge Ca).                    \tag{PDU}
\]

All means in this note are unnormalized sums over the odd units, divided
by `X` or `log X` as displayed. We do not silently multiply them by the
reciprocal of the density of odd units.

## 2. Disjoint basins with geometrically controlled roots

Suppose an odd unit orbit is injective. An ordinary orbit that is not
eventually periodic yields such an orbit after discarding a possible
initial odd multiple of three.

Choose the successive minima of its forward suffixes. More precisely,
let `t0` be the least value of the whole orbit, take its unique occurrence,
and let `t1` be the minimum of the suffix strictly following that occurrence.
Continue in this way. The values are distinct and increasing. Because the
first state after `tj` is `U(tj)`,

\[
t_{j+1}\le U(t_j)\le\frac{3t_j+1}{2},
\qquad
t_j+1\le(t_0+1)(3/2)^j.                             \tag{Q1}
\]

At every `tj`, among exponents `1<=e<=6` exactly two give positive odd unit
parents `(2^e tj-1)/3`: the allowed residues are `2^e tj=4 or 7 (mod 9)`.
At most one of these parents belongs to the supplied injective orbit.
Choose an off-orbit parent `bj`. Set

\[
K=\frac{64}{3},\qquad a=\frac32,
\qquad R=K(t_0+1).
\]

Then `bj<K tj`. The basins `B(bj)` are pairwise disjoint. Otherwise an
ordinary source would hit two different chosen branches. After hitting
the earlier branch it follows the original forward spine, and can never
enter the later off-spine branch.

Let `rj` be the least member of `B(bj)`. It is an odd unit and satisfies

\[
r_j\le b_j<Kt_j<R a^j.                              \tag{Q2}
\]

The `rj` are distinct; their basins `B(rj)` are disjoint subsets of the
disjoint `B(bj)`. Every state before a hit of `rj` also belongs to `B(bj)`
and is at least `rj`. The trajectory from `rj` to `bj` has the same
property. After `bj` it joins the original suffix at `tj`, whose minimum
is `tj`. Thus the exact relation on the entire selected basin is

\[
\boxed{n\in B(r_j)\quad\Longrightarrow\quad
       m(n)=\min(r_j,t_j)\ge r_j/K.}                 \tag{Q3}
\]

This uses actual fixed ordinary basins. It does not count nested ancestor
levels as disjoint, and it does not replace an orbit by its entire
predecessor population.

## 3. A finite-scale lower bound for the natural first moment

For any integer `N>=1` and real `X>=CR a^(N-1)`, every one of the first
`N` roots satisfies `X>=C rj`. Disjointness, (Q3), and (PDU) therefore give

\[
\begin{aligned}
A(X)&:=\sum_{\substack{n\in\mathcal O^*\\n\le X}}m(n)\\
&\ge\sum_{j=0}^{N-1}\sum_{\substack{n\in B(r_j)\\n\le X}}m(n)\\
&\ge\sum_{j=0}^{N-1}\frac{r_j}{K}\frac{cX}{r_j}
 =\frac{cX}{K}N.                                    \tag{Q4}
\end{aligned}
\]

For `X>=CR`, put `L=log(X/(CR))` and choose
`N=floor(L/log a)+1`. It follows in particular that

\[
\boxed{\frac{A(X)}X\ge\frac{c}{K\log a}
          \log\frac{X}{CR}\qquad(X\ge CR).}         \tag{Q5}
\]

The coefficient is absolute apart from the already specified population
constant `c`. The initial escape source enters only through the finite
onset `CR`. Hence even the weaker upper hypothesis

\[
\liminf_{X\to\infty}\frac{A(X)}{X\log X}=0
\]

would rule out **every** injective positive ordinary orbit. No bounded
natural first moment is needed for that implication.

## 4. The quadratic lower bound for the harmonic first moment

Let

\[
S(X)=\sum_{\substack{n\in\mathcal O^*\\n\le X}}\frac{m(n)}n.
\]

For any odd unit root `r` and `X>=Cr`, ordinary partial summation of the
counting function in (PDU) gives

\[
\sum_{\substack{n\in B(r)\\n\le X}}\frac1n
 \ge\frac cr\log\frac{X}{Cr}.
\]

The positive endpoint term has merely been dropped. It follows that for
every `N>=1` and `X>=CR a^(N-1)`,

\[
\boxed{
S(X)\ge\frac cK\left[
 N\log\frac{X}{CR}-\frac{N(N-1)}2\log a\right].}     \tag{Q6}
\]

To optimize, write `L/log a=k+u` with integer `k>=0` and `0<=u<1`, and
take `N=k+1`. The bracket in (Q6) is exactly

\[
\frac{L^2}{2\log a}+\frac L2+
             \frac{\log a}{2}u(1-u)
 \ge\frac{L^2}{2\log a}.
\]

Consequently

\[
\boxed{S(X)\ge\frac{c}{2K\log a}
               \left(\log\frac{X}{CR}\right)^2
               \qquad(X\ge CR).}                   \tag{Q7}
\]

Equivalently, for the earlier logarithmic first moment
`M(X)=S(X)/log X`, any one escaping orbit forces

\[
\boxed{\liminf_{X\to\infty}\frac{M(X)}{\log X}
       \ge\frac{3c}{128\log(3/2)}>0.}               \tag{Q8}
\]

The earlier conclusion `liminf M(X)=infinity` is therefore strengthened
to a specific minimum growth rate. An upper bound `M(X)=o(log X)`, or
even a sequence along which `M(X)/log X` tends to zero, would already
exclude all escapes. This argument does not require an exchange of an
infinite family with a lower density: at each `X` only the displayed
finite family is counted, with a common onset supplied by (PDU).

## 5. Truncation exposes the critical minimum tail

For `M>0` define `m_M(n)=min(m(n),M)`. If `rj<=KM`, then (Q3) gives
`m_M(n)>=rj/K` on `B(rj)`. Thus, for every `N>=1`,

\[
\boxed{
R a^{N-1}\le\min(KM,X/C)
\quad\Longrightarrow\quad
\frac1X\sum_{\substack{n\in\mathcal O^*\\n\le X}}m_M(n)
 \ge\frac cK N.}                                   \tag{Q9}
\]

For fixed `M>=t0+1`, choose
`N=floor(log(M/(t0+1))/log a)+1` and then let `X` increase. The same
choice in the harmonic estimate gives both

\[
\begin{aligned}
\liminf_{X\to\infty}\frac1X
 \sum_{\substack{n\in\mathcal O^*\\n\le X}}m_M(n)
 &\ge\frac{c}{K\log a}\log\frac{M}{t_0+1},\\
\liminf_{X\to\infty}\frac1{\log X}
 \sum_{\substack{n\in\mathcal O^*\\n\le X}}\frac{m_M(n)}n
 &\ge\frac{c}{K\log a}\log\frac{M}{t_0+1}.
\end{aligned}                                      \tag{Q10}
\]

The order here is explicit: the truncation `M` is fixed before the source
cutoff tends to infinity. Since `min(m,M)=integral_0^M 1_{m>t} dt`, these
are integrated tail bounds at the critical first-moment scale. They are
compatible with tail probabilities tending to zero and with all fixed
subcritical moments being finite. Almost-boundedness alone therefore
does not contradict (Q10).

## 6. Attempting the actual upper bound with the new canonical flow

The new PR175 and PR185 estimates provide more than the earlier Abel
antichain packing. On the nonperiodic odd units, write `V` for the least
inverse excessive majorant, `G` for its harmonicization, `h(q)=G(q)/q`,
and `nu` for PR185's ordinary harmonic correction. With
`theta=39/40`, the pinned results give

\[
0<h\le\nu\le e^{200/3}h,\qquad L\nu=\nu,
\qquad
\sum_q\frac{\nu(q)^p}{q^s}<\infty
\quad(p\ge1,\ s>\theta),                           \tag{Q11}
\]

where `Lf(q)=sum_{U(n)=q}f(n)` and sources are killed upon entering any
periodic orbit. In particular `sum nu(q)/q` is finite. The exact
stationary normalization also compares `V(q)/q` with `nu(q)` by absolute
constants at **every ordinary point**. These inputs genuinely remove a
normalization ambiguity; they do not compare the forward minimum with
that local inverse mass.

The direct domination route fails even on a known convergent basin. For
unit ancestors `n` of `5`, the ordinary future minimum is `m(n)=1`, while
fixed-basin sublinearity and (Q11) give `nu(n)->0` along unbounded such
ancestors. Thus neither `m(n)<=C nu(n)` nor a uniform pointwise charge of
the minimum to `nu(n)` is available. Using the finite weighted sum in
(Q11) to pay for an ordinary minimum would discard this missing factor.
This is an actual ordinary example, not a hypothetical escaping graph.

The retained-source collision route reaches the same issue in a different
form. PR185 proves exact contraction in

\[
\mathcal E_\nu(b)=\sum_q\frac{b(q)^2}{\nu(q)}.
\]

For one fixed source of mass `w` on an injective orbit `qk`, its energy is
exactly `w^2/nu(qk)`, and the pinned source proves that this tends to a
strictly positive limit. The finite positive reference
`a0(q)=G(q)/q^2` instead costs the explicit ratio

\[
\frac{\nu(q)}{a_0(q)}=q\frac{\nu(q)}{h(q)}\in[q,e^{200/3}q].
\]

Neither the weighted moments of the reference nor collision contraction
controls that moving height factor. They therefore do not supply the
sublogarithmic upper bound in (Q5) or (Q8). This checkpoint does not
relabel their finite energy as a finite-reference result.

**First unsupported inference in this attempted completion:** an upper
estimate for the actual ordinary minimum satisfying
`liminf A(X)/(X log X)=0` or `liminf S(X)/(log X)^2=0`, with unchanged
ordinary source weights. No estimate of that strength has been derived
here from the canonical weighted moments or from the stationary density.

The new work is the quantitative lower bound (Q4)--(Q10), including its
uniform finite-scale form and the weaker closing upper target. It proves
neither that this upper target holds nor that positive nontrivial cycles
are impossible. Full Collatz remains **OPEN**.

## 7. Lean evidence for the finite accounting

[OrdinaryBasinMoments.lean](lean/OrdinaryBasinMoments.lean) imports only
`Std`. Its two public theorems check the finite source accounting behind
the natural and truncated population aggregates:

- `retained_source_accounting`: adding the moments of selected basins
  cannot exceed the original source moment when each original source
  belongs to at most one selected basin.
- `disjoint_basin_minimum_moment`: if `J` selected basins satisfy
  `T<=root(j)*sum_owned weight(n)` and the minimum floor is written as
  `A*root(j)<=K*minimum(n)`, then
  `A*(J*T)<=K*sum_original weight(n)*minimum(n)`.

The ownership condition is imposed at each original source; it is not
replaced by an endpoint distinctness condition. The identical original
`weight(n)` occurs in both the population premise and the final moment.
The coefficients and weights are natural numbers, allowing a common
denominator to encode any finite nonnegative rational weighting. For
(Q3), the minimum-floor coefficients are `A=3` and `K=64`.

Executed successfully with Lean 4.34.1:

```text
lean -j1 -DwarningAsError=true OrdinaryBasinMoments.lean
```

The printed axiom lists are `[propext]` and `[propext, Quot.sound]`,
respectively. There is no analytic population axiom or convergence axiom.
The infinite suffix-minimum construction, real logarithmic estimates,
partial summation, and the source-qualified (PDU) input remain the written
proof above; this finite module is not presented as their formalization.
