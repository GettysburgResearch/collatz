# Canonical inverse capacity concentrates on finitely many forward trajectories

**Status: written analytic consequence of explicitly pinned inputs; not a Lean formalization and not a convergence theorem.**

This note combines the uniform ordinary predecessor population with the least excessive inverse envelope. It proves a global antichain budget, a lower-density bound for the canonical envelope, and finite-trajectory concentration of every positive normalized superlevel set. The trajectories may escape. No bound on them is assumed or asserted.

## 1. Pinned inputs and notation

The source repository is `GettysburgResearch/collatz`, PR180 at commit
`d0349de2108abb7c8fb8393c086610e3372df116`.
The relevant files are:

- `research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`, sections 2--6: the written fixed-total input and the derived uniform unit-source predecessor population `(PDU)`.
- `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`, sections 1--5: the finite least excessive majorant `V` and its fixed-basin uniform sublinearity `(BUE)`.

The non-elementary analytic input is the joint clock argument in `JOINT_CLOCK_MIXING.md`, as identified by those notes. The present argument does not independently formalize that input or replace it by an assumption of Collatz convergence.

Work with positive odd integers coprime to three, and write

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

An integer is **nonperiodic** if no positive iterate of `U` returns to it; an integer that eventually enters a cycle can still be nonperiodic. Let

\[
\operatorname{Pred}(q)=\{n>0:n\text{ odd},\ 3\nmid n,\ U^j(n)=q
\text{ for some }j\ge0\}.
\]

For odd unit targets, these are exactly the positive odd unit sources that reach the target under the ordinary shortcut map. The first input supplies absolute constants `c,C>0` such that

\[
X\ge Cq\quad\Longrightarrow\quad
\#(\operatorname{Pred}(q)\cap[1,X])\ge \frac{cX}{q}.
\tag{1}
\]

No numerical values of these constants are used.

The inverse operator and obstacle are

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^eq\equiv1\ (3)}}
\frac3{2^e}f\left(\frac{2^eq-1}{3}\right),
\qquad g(q)=\mathbf 1_{3\nmid q}.
\]

The second input constructs finite functions

\[
V_0=g,\qquad V_{N+1}=\max(g,PV_N),\qquad V=\sup_N V_N<\infty,
\tag{2}
\]

and proves that, for each fixed ordinary target `q`,

\[
\frac{V(n)}n\longrightarrow0
\quad\text{uniformly as }n\to\infty\text{ through }\operatorname{Pred}(q).
\tag{3}
\]

We write `H(q)=V(q)/q`.

## 2. Finite stopping lines give exactly the obstacle iterates

Fix a nonperiodic odd unit target `q`. Its inverse histories form a rooted tree: a source cannot reach `q` at two different odd depths, since that would make `q` periodic. A word `w=(e_1,\ldots,e_j)` has source `n_w` and weight

\[
\omega_w=\prod_{i=1}^j\frac3{2^{e_i}}.
\]

The empty word has source `q` and weight one. Positive ordinary affine arithmetic gives

\[
q\ge \omega_w n_w,\qquad \omega_w\le\frac q{n_w}.
\tag{4}
\]

A finite stopping line is a finite prefix-free set of inverse words with unit sources. Empty stopping lines are permitted. For depth at most `N`,

\[
V_N(q)=\sup_{\mathcal L}
\sum_{w\in\mathcal L}\omega_w.
\tag{5}
\]

To verify (5), stopping at the root contributes `g(q)`; otherwise one sums the optimal continuation values in the inverse children. This is exactly the recursion (2). Countable branching creates no additional hypothesis: every nonnegative parent sum is the supremum of its finite partial sums. At a finite collection of selected children, finite stopping lines approximate the corresponding continuation values simultaneously. Induction on `N` proves both inequalities. Sources divisible by three have both obstacle and continuation value zero and may be omitted.

The full predecessor basins of the sources in a stopping line are pairwise disjoint. If a source reached two such leaves, its deterministic forward path would put one leaf above the other, contradicting prefix-freeness. Nonperiodicity of `q` rules out any alternate traversal through a cycle.

## 3. A lower-natural-density bound for the canonical envelope

Let `L` be any finite stopping line, and choose

\[
X\ge C\max_{w\in\mathcal L}n_w.
\]

Applying (1) to each leaf, using the disjointness just proved and inclusion in `Pred(q)`, gives the finite-scale inequality

\[
\frac c q\sum_{w\in\mathcal L}\omega_w
\ \le\ c\sum_{w\in\mathcal L}\frac1{n_w}
\ \le\ \frac{\#(\operatorname{Pred}(q)\cap[1,X])}{X}.
\tag{6}
\]

Since (6) holds for every sufficiently large `X`, take its lower limit, then the supremum over finite stopping lines and depths. This yields

\[
\boxed{
H(q)=\frac{V(q)}q\le
\frac{\underline d(\operatorname{Pred}(q))}{c}
\le\frac1c
\qquad(q\text{ nonperiodic odd unit}).
}
\tag{7}
\]

Here the lower density is taken among all positive integers. No existence of a natural-density limit is required. In particular, an upper density is not needed in this estimate.

There is a useful finite-cutoff version. Let `K_M(q)` be the supremum of the stopping-line sums with every leaf source at most `M`, with no restriction on the depth. Then

\[
\frac c q K_M(q)\le
\frac{\#(\operatorname{Pred}(q)\cap[1,X])}{X}
\qquad(X\ge CM),
\qquad K_M(q)\uparrow V(q).
\tag{8}
\]

The monotone limit follows because every finite stopping line has finitely many ordinary source values. Formula (8) supplies no uniform bound on the leaf cutoff needed to approximate `V(q)` as `q` varies.

## 4. A global budget for incomparable targets

Let `A` be a finite set of nonperiodic odd unit targets, no two of which reach one another. Their predecessor basins are pairwise disjoint. Choose near-optimal finite stopping lines separately for the targets, and apply (1) simultaneously to all their leaves. The union still has pairwise disjoint predecessor basins. Dividing each stopping-line value by its own root and applying (4) gives

\[
\boxed{\sum_{q\in A}\frac{V(q)}q\le\frac1c.}
\tag{9}
\]

One may equivalently sum (7), since lower densities of finitely many disjoint sets have sum at most one. The direct stopping-line argument emphasizes that no additivity of upper natural density, countable density interchange, or uniform optimal stopping time is being used.

## 5. Every positive superlevel set lies on finitely many actual forward paths

Fix `epsilon>0` and define

\[
E_\epsilon=\{q:q\text{ nonperiodic odd unit},\ H(q)\ge\epsilon\}.
\]

For a fixed `q` in this set, (3) implies that
`E_epsilon intersect Pred(q)` is finite. It is nonempty because it contains `q`. Choose a member `m` of this finite set having no distinct earlier member in the same set. Such an `m` is globally minimal in `E_epsilon`: any other high state reaching `m` would also reach `q` and would contradict its selection.

Let `M_epsilon` be the set of all these globally minimal high states. Distinct members of `M_epsilon` are incomparable under forward reachability. By (9), every finite subset has cardinality at most `1/(c epsilon)`, so `M_epsilon` itself is finite and

\[
\#M_\epsilon\le\left\lfloor\frac1{c\epsilon}\right\rfloor.
\]

Every member of `E_epsilon` is reached from a member of `M_epsilon`. Therefore

\[
\boxed{
E_\epsilon\subseteq
\bigcup_{m\in M_\epsilon}\{U^j(m):j\ge0\},
\qquad
\#M_\epsilon\le\left\lfloor\frac1{c\epsilon}\right\rfloor.
}
\tag{10}
\]

This is global concentration, not merely a separate estimate on each fixed predecessor basin. It applies in particular to the nonperiodic marked states in the section introduced in PR173.

## 6. A global summable canonical weight

The pinned minimal-envelope note also proves a uniform reciprocal bound on every finite simple inverse path with nonperiodic intermediate nodes. With the same population constant `c`, one can take

\[
B=\frac{64}{3c}.
\]

Equivalently, every finite collection of nonperiodic odd unit states on one actual forward path satisfies

\[
\sum_{q\text{ in that collection}}\frac1q\le B.
\tag{11}
\]

For this equivalence, extend a finite forward segment one odd step beyond its last nonperiodic member, then reverse it. The final root is allowed to be periodic, while every included intermediate node is nonperiodic. Taking a subset only decreases the reciprocal sum.

Combining (11) with the antichain budget (9) gives the stronger global estimate

\[
\boxed{
\sum_{\substack{q>0\text{ odd},\ 3\nmid q\\q\text{ nonperiodic}}}
\frac{V(q)}{q^2}
\le\frac Bc=\frac{64}{3c^2}.
}
\tag{12}
\]

Here is an elementary proof, avoiding any infinite-poset decomposition theorem. Fix a finite set `F` of nonperiodic unit states, partially ordered by actual forward reachability. For `q` in `F`, let

\[
h(q)=\max\left\{\sum_{n\in K}\frac1n:
K\subseteq F\text{ is a chain with greatest element }q\right\}.
\]

By (11), `h(q)<=B`. Form the half-open interval

\[
I_q=(h(q)-1/q,h(q)]\subseteq[0,B].
\]

If distinct `p,q` in `F` satisfy `p -> q`, a maximizing chain ending at `p` may be extended by `q`. Hence `h(q)>=h(p)+1/q`, so `I_p` and `I_q` are disjoint. At any fixed real `t`, the states whose intervals contain `t` therefore form an antichain. Its total `H` is at most `1/c` by (9). Integrating this finite step function yields

\[
\sum_{q\in F}\frac{V(q)}{q^2}
=\sum_{q\in F}H(q)|I_q|
=\int_0^B\sum_{q\in F}\mathbf1_{I_q}(t)H(q)\,dt
\le\frac Bc.
\]

Take the supremum over finite `F` to obtain (12).

Thus the canonical inverse envelope supplies a finite positive weight `V(q)/q^2` on **all nonperiodic odd unit states**, using no assumption that these states eventually reach a cycle. This is a summability theorem, not an invariance or powerboundedness theorem for ordinary forward transport. In particular, it does not extend a proved support statement to the periodic nodes, and it does not give an effective method for deciding nonperiodicity.

For comparison, (10) and (11) alone yield the weak superlevel estimate

\[
\sum_{q\in E_\epsilon}\frac1q\le\frac B{c\epsilon}.
\]

The interval argument improves this to the strong summability in (12). Also, since `H<=1/c`, for every real `p>=1` one immediately has

\[
\sum_{q\text{ nonperiodic odd unit}}\frac{H(q)^p}{q}
\le\frac B{c^p}.
\tag{13}
\]

## 7. Finite immigration and a bounded ordinary harmonic flow

The pinned minimal-envelope construction also supplies a harmonic function

\[
PG=G,\qquad 0<G(q)\le V(q)
\]

on the units, with a uniform positive lower bound on `G`. In this section put `H_G(q)=G(q)/q`, and restrict the state space `D` to nonperiodic odd units. Define ordinary inverse counting, with no slope weights, by

\[
(Lf)(q)=\sum_{\substack{n\in D\\U(n)=q}}f(n).
\]

Every positive odd parent of a nonperiodic unit target is itself nonperiodic. Therefore the harmonic equation for `G` gives exactly

\[
H_G(q)=\sum_{U(n)=q}\frac{3n}{3n+1}H_G(n).
\tag{14}
\]

Set

\[
\mu(n)=\frac{3n}{3n+1}H_G(n),\qquad
a(n)=\frac{H_G(n)}{3n+1}.
\]

Thus `H_G=mu+a` pointwise, and (14) becomes

\[
L\mu=\mu+a.
\tag{15}
\]

The immigration `a` has finite total mass, by (12):

\[
A:=\sum_{n\in D}a(n)
\le\frac13\sum_{n\in D}\frac{G(n)}{n^2}
\le\frac B{3c}.
\tag{16}
\]

For each nonperiodic target `q`, a fixed source can hit `q` at most once. Consequently the forward Green sum has the exact pointwise expression

\[
(Sa)(q):=\sum_{j\ge0}(L^ja)(q)
=\sum_{n\in\operatorname{Pred}(q)}a(n)
\le A<\infty.
\tag{17}
\]

Nonnegative summation gives `LSa=Sa-a`. It follows that

\[
\boxed{\nu:=\mu+Sa>0,\qquad L\nu=\nu,\qquad
\nu(q)\le\frac1c+\frac B{3c}.}
\tag{18}
\]

This constructs an ordinary harmonic flow, bounded uniformly at every nonperiodic unit state. The construction concerns the ordinary counting operator `L`, not merely the slope-weighted operator `P`.

The new flow itself retains a finite weighted mass. Indeed, Tonelli's theorem and (11) give

\[
\begin{aligned}
\sum_{q\in D}\frac{\nu(q)}q
&\le\frac Bc+
\sum_{n\in D}a(n)
\sum_{\substack{j\ge0\\U^j(n)\in D}}\frac1{U^j(n)}\\
&\le\frac Bc+BA
\le\frac Bc+\frac{B^2}{3c}.
\end{aligned}
\tag{19}
\]

The ordinary forward path has no repeated state while it remains in `D`, so the inner sum uses (11), including when the path eventually enters a cycle and leaves `D`.

There is a precise obstruction to interpreting (18) as a finite stationary measure. Along an infinite nonperiodic forward path `q_j`, equation `Lnu=nu` gives `nu(q_{j+1})>=nu(q_j)>0`. Its total unweighted mass is then infinite, even though (19) can hold because `sum_j 1/q_j` is finite. The weight `nu(q)/q` is summable but is not asserted to be harmonic under `L`.

Likewise, (15) has the sign `Lmu-mu=a`, not `mu-Lmu=a`. Its finite Green correction produces the harmonic flow (18), not a finite invariant measure. Minimality of the original obstacle envelope has not been shown to remove an escaping forward flow: subtracting a spike supported on a forward tail loses the needed subharmonic inequality at the first supported source. The obstacle at that first source can be active. The inverse-ray atom-removal proof does not resolve this boundary sign.

## 8. What is proved, and the first unsupported step

Equations (7), (9), (10), (12), and (18)--(19) are consequences of the pinned population and minimal-envelope results. They use the original ordinary predecessor sets throughout. No source is resampled, and all finite simultaneous counting uses the common valid onset `X>=C max(source)`.

Equation (10) does **not** make the superlevel set finite. One of its finitely many actual forward paths can be an escaping path. Along such a path the predecessor basins are nested, so their positive densities do not consume a new disjoint fraction of the integers at each successive target. The finite-antichain budget is therefore compatible with a single escaping spine.

Nor does (12) eliminate this possibility. A fixed source on an escaping spine can have `V(q_j)/q_j` bounded below at its later states, while the proved reciprocal occupation bound makes `sum_j 1/q_j` finite. Such a spine is entirely compatible with (12). A finite source weight alone supplies no uniform decrease under its actual forward transport.

Periodic target nodes were excluded explicitly: the inverse histories then repeat the same ordinary sources, so the source-antichain stopping-line argument requires a separate first-hit or cycle calculation. Nonperiodic sources that eventually reach a cycle are covered, but the periodic nodes themselves are not.

To obtain the marked sublinearity needed by `MarkedDensityPotential.lean`, one would still need to prove that, for every `epsilon>0`, each of the finitely many forward paths in (10) contains only finitely many marked states with `H>=epsilon`, together with control of periodic states as their heights vary. No such statement is established here. It cannot be obtained merely by repeating the disjoint predecessor count along a single path.

The new result narrows a potential global failure to finitely many actual trajectories at every fixed height threshold. It does not supply the missing uniform survivor-mass decrease or claim to prove Collatz.
