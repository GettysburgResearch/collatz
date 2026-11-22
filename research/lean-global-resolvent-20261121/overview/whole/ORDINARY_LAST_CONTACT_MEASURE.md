# A finite ordinary last-contact measure for every escaping component

**Status: source-qualified written analytic deductions. No new Lean theorem or Collatz convergence claim is made.**

The ordinary harmonic flow from PR185 and the first-contact theorem from
PR176 together give a finite measure on actual positive integer sources.
Its total mass is exactly the sum of the capacities of all escaping
components. It represents the harmonic flow after the last contact with
the obstacle. The representation also gives an actual source-height
upper bound for short contact probabilities. It supplies no quantitative
lower bound on those probabilities.

## 1. Frozen inputs and exact scope

The repository is `GettysburgResearch/collatz`. The inputs are:

| Source | Frozen head | Input used |
|---|---|---|
| PR185, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md` | `276be8154f4e867acc0230466b34d9cb224aacf5` | The canonical ordinary harmonic flow, its antichain budget, positive component capacities, and the bounded change of inverse path law. |
| PR176, `research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md` and `CONTACT_CAPTURE_SYNTHESIS.md` and `WORD_DENSITY_ENVELOPE.md` | `8aeb843bba254f065743b6fa277a70906b51d520` | Almost-sure first contact with `{V <= 2}` under the critical harmonic inverse law, and the finite critical contact-front bound. |
| PR175 / PR180, as imported by the first source | `2bc2ad37b490a5aea63658eaf657bc048da4532e` / `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | Source-qualified predecessor populations and the finite canonical envelope underlying the flow and its comparisons. |

Let

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. As in PR185, `N` consists of positive odd
ternary units that are not themselves periodic. A member of `N` may
later enter a periodic orbit. Ordinary transport

\[
(Lf)(q)=\sum_{\substack{n\in N\\U(n)=q}}f(n)
\]

is killed on first entering any periodic orbit.

Write `E` for the subset of `N` whose forward orbits never enter a
periodic orbit. These orbits have distinct states, so their ordinary
heights tend to infinity. The set `E` is closed under forward iteration
and under taking positive odd unit predecessors. No assertion that `E`
is empty is used. No periodic orbit, known or hypothetical, belongs to
the domain of the new conclusions below.

The pinned sources provide the canonical envelope `V`, its harmonicization
`G`, and an ordinary flow `nu` such that

\[
L\nu=\nu,\qquad
0<\nu(q)\le A,\qquad
\delta\nu(q)\le \frac{V(q)}q,
\tag{1}
\]

where `A=203/(3c)` and `delta=exp(-200/3)` in the normalization of PR185.
Every finite reachability antichain satisfies

\[
\sum_{q\in B}\nu(q)\le A.
\tag{2}
\]

The ordinary inverse kernel is

\[
K_\nu(q,n)=\mathbf 1_{U(n)=q}\frac{\nu(n)}{\nu(q)}.
\tag{3}
\]

Its path law is mutually absolutely continuous, with bounded densities,
with the critical `G` inverse law; this is PR185 (24). Thus the pinned
first-contact theorem transfers to (3): from every fixed root in `N`,
the first visit to

\[
C=\{q\in N:V(q)\le2\}
\tag{4}
\]

is almost surely finite. This transfer uses the full path-law comparison,
not an independence assumption or a new limit interchange.

## 2. Every escaping path has a last contact

Fix `x` in `E` and put `q_i=U^i(x)`. Harmonicity gives
`nu(q_i) >= nu(x) > 0`. Hence (1) gives

\[
V(q_i)\ge\delta\nu(x)q_i\longrightarrow\infty.
\tag{5}
\]

There are therefore only finitely many contacts on any one forward
escaping path. The path need not have a contact after its chosen
starting point; an inverse ancestor supplies one when needed below.

Define the set of **ordinary last contacts** by

\[
\Lambda=\{x\in E: V(x)\le2\text{ and }V(U^j x)>2
\text{ for every }j\ge1\}.
\tag{6}
\]

If distinct members `x,y` of `Lambda` were comparable under forward
iteration, the earlier one's future would contain the later contact.
This contradicts (6). Thus `Lambda` is one global reachability
antichain, across all escaping components.

Define the measure on actual original integer sources

\[
\eta(x)=\nu(x)\mathbf 1_{\{x\in\Lambda\}}.
\tag{7}
\]

Applying (2) to finite subsets and then taking their increasing union
proves

\[
\boxed{\sum_x\eta(x)\le A.}
\tag{8}
\]

The definition uses an infinite-future predicate. It is canonical given
`V` and `nu`, but it is not claimed to be an effective algorithm for
recognizing escaping sources or last contacts.

## 3. Exact source representation and the capacity budget

Let

\[
B_+=\{q\in E:V(U^j q)>2\text{ for every }j\ge0\}
\tag{9}
\]

be the escaping states whose entire forward orbit avoids `C`. This
definition uses only the future of `q`; no unique prior history is
assumed. Every escaping spine eventually lies in `B_+` by (5).

Fix `q` in `B_+`. A first-contact inverse path ends at a source in
`Lambda`: its intermediate states have no contact, and all forward
states after `q` have no contact. Conversely, if `x` in `Lambda` reaches
`q`, its unique inverse path from `q` is a first-contact path. Uniqueness
uses nonperiodicity: one source cannot hit `q` at two different depths.

For such a path the transition probabilities in (3) telescope to
`nu(x)/nu(q)`. Almost-sure contact and nonnegative summation therefore
give the exact identity

\[
\boxed{
\nu(q)=\sum_{\substack{x\in\Lambda\\x\to q}}\eta(x)
\qquad(q\in B_+).
}
\tag{10}
\]

Here `x -> q` means that some nonnegative iterate of `x` equals `q`.
No inverse slope is attached to the original atom in (10).

There is also a global Green form. Put

\[
T=\Lambda\cup B_+
=\{q\in E:V(U^j q)>2\text{ for every }j\ge1\}.
\]

Then on all of `N`,

\[
\boxed{
\sum_{j\ge0}L^j\eta(q)=\nu(q)\mathbf 1_T(q),\qquad
\nu\mathbf 1_T-L(\nu\mathbf 1_T)=\eta.
}
\tag{11}
\]

For `q` in `B_+`, the first equality is (10). At a last contact,
the only last-contact ancestor is itself. At any other state, no
last-contact ancestor can reach it. The second equality follows by
shifting the nonnegative Green sum; every displayed pointwise sum is
finite by the first equality.

Two members of `E` belong to the same ordinary component if their
forward tails meet, possibly at different clocks. For a component
`mathcal C`, PR185 defines the positive finite capacity

\[
C_{\mathcal C}=\lim_{i\to\infty}\nu(U^i q)\in(0,A].
\]

Choose `q_0` in `B_+` in that component. The sets
`Lambda intersect Pred(U^i q_0)` increase with `i` and exhaust
`Lambda intersect mathcal C`: every last-contact source in the same
ordinary component eventually meets this spine. Applying monotone
convergence to (10) gives

\[
\boxed{
C_{\mathcal C}=\sum_{x\in\Lambda\cap\mathcal C}\eta(x),
\qquad
\sum_{\mathcal C\text{ escaping}}C_{\mathcal C}
=\sum_x\eta(x)\le A.
}
\tag{12}
\]

In particular every escaping component has a last-contact source.
If any escaping components exist, a largest positive capacity is
attained: a summable nonempty family of positive numbers has a maximum.
A smallest positive capacity need not be attained.

This is a finite measure on original boundary sources, not a finite
invariant measure on ordinary states. If `eta` is nonzero, each of its
positive atoms has an infinite escaping forward path, and Tonelli gives

\[
\sum_q\sum_{j\ge0}L^j\eta(q)=\infty.
\tag{13}
\]

Consequently finite-measure recurrence on ordinary states does not
follow from (8) or (12).

### The limiting contact-source law is atomic

Write `q_i=U^i q_0` with `q_0` in `B_+`. The first-contact source law is

\[
\mu_i(x)=\frac{\eta(x)\mathbf 1_{x\to q_i}}{\nu(q_i)}.
\]

On the component define the probability measure
`mu_infinity(x)=eta(x)/C_mathcal C`. Directly separating the ancestor
set from its complement proves the exact total-variation identity

\[
\boxed{
\|\mu_i-\mu_\infty\|_{\rm TV}
=1-\frac{\nu(q_i)}{C_{\mathcal C}}\longrightarrow0,
}
\tag{14}
\]

where total variation is `sup_D |mu_i(D)-mu_infinity(D)|`.
Thus finite boundary compactness concentrates on fixed ordinary
last-contact sources. It does not say that their distances from a
moving root remain short. These atoms are finite contact endpoints;
they are not atoms of the infinite inverse-path boundary.

## 4. A source-tail bound at the actual native inverse clock

For `q` in `B_+`, let `tau` be first contact under `K_nu` and define

\[
p_L^\nu(q)=\Pr_q^\nu(\tau<L),\qquad L\in\mathbb N.
\]

The strict inequality is intentional: depths are `0,...,L-1`.
The same telescoping calculation gives

\[
\nu(q)p_L^\nu(q)
=\sum_{\substack{x\in\Lambda,\ 0\le j<L\\U^j x=q}}\eta(x).
\tag{15}
\]

An actual odd step always obeys

\[
U(n)+1\le\frac32(n+1).
\]

Hence `U^j x=q` implies
`q+1 <= (3/2)^j(x+1)`. This is a deterministic inequality for every
physical inverse path, with no averaged-exponent assumption. Writing
`a=3/2`, (15) yields, for `L>=1`,

\[
\boxed{
\nu(q)p_L^\nu(q)
\le\eta\bigl(\{x:x+1\ge(q+1)a^{-L}\}\bigr).
}
\tag{16}
\]

Use natural logarithms and, for sufficiently large `q`, put

\[
L(q)=\left\lfloor
\frac{\log q-3\log\log(q+2)}{\log(3/2)}
\right\rfloor\ge1.
\tag{17}
\]

Since `a^L <= q/log(q+2)^3`, equation (16) gives

\[
\boxed{
\nu(q)p_{L(q)}^\nu(q)
\le\eta\bigl(\{x:x+1\ge\log(q+2)^3\}\bigr).
}
\tag{18}
\]

The right side tends to zero by (8). More precisely, for every fixed
`epsilon>0`, uniformly over the actual post-contact roots with
`nu(q)>=epsilon`,

\[
\sup_{\substack{q\in B_+,\ q\ge Q\\\nu(q)\ge\epsilon}}
p_{L(q)}^\nu(q)
\le\frac{\eta(\{x:x+1\ge\log(Q+2)^3\})}{\epsilon}
\longrightarrow0.
\tag{19}
\]

The supremum over an empty set may be read as zero. In particular every
hypothetical escaping spine, and every cofinal marked subsequence on it,
satisfies

\[
\boxed{p_{L(q_i)}^\nu(q_i)\longrightarrow0.}
\tag{20}
\]

The last assertion only uses (19), eventual membership in `B_+`, and
`nu(q_i)>=nu(q_0)>0`. It does not need a return-density assumption.

### Equivalent ordinary clock explanation

Fix one last-contact source `x` in the component. Once its forward
orbit meets the chosen spine, its unique distance to `q_i` has the form
`j_i=i-s_x` for a fixed integer offset `s_x`. The actual growth bound
`q_i+1 <= a^i(q_0+1)` implies

\[
i-L(q_i)\ge
\frac{3\log\log(q_i+2)-\log(q_0+1)}{\log a}
\longrightarrow\infty.
\tag{21}
\]

Thus `j_i<L(q_i)` eventually fails for each fixed original contact
source. The finite measure `eta` permits dominated convergence over
all sources. This is another proof of (20). The height-tail proof
(16)--(19) is stronger in being uniform over the indicated moving
roots and over every physical path.

## 5. Keep the prior finite-front bound in the same ordinary law

The preceding source-tail statement must be combined with the prior
quantitative contact-front estimate, not read in isolation. Let `w` be
an inverse word from `q` to `x`, let `omega_w` be its critical weight,
and let `Lambda_w` be its actual multiplicative correction. They obey

\[
\Lambda_w=\frac{\omega_w x}{q}.
\]

Appending any infinite inverse tail from `x` to this fixed word gives
`Lambda_w Lambda_tail >= delta`. PR185 (23), applied at `x`, therefore
gives

\[
\frac{\nu(x)}{h(x)}
=\mathbb E_h^x[\Lambda_{\rm tail}^{-1}]
\le\frac{\Lambda_w}{\delta},
\qquad h(x)=G(x)/x.
\]

Consequently the original source atom has the useful bound

\[
\boxed{
\nu(x)\le\frac{\omega_w G(x)}{q\delta}
\le\frac{\omega_w V(x)}{q\delta}.
}
\tag{22}
\]

The path and its appended tail are distinct ordinary states because
`q` is nonperiodic. This is where the uniform correction bound applies.

Let `F_L(q)` be the critical sum of `omega_w V(x)` over the first-contact
words of depth less than `L`. Summing (22), then using the pinned
finite-front estimate with contact threshold two, proves

\[
\boxed{
\nu(q)p_L^\nu(q)
\le\frac{F_L(q)}{q\delta}
\le\frac{16L(3/2)^L}{q\delta}.
}
\tag{23}
\]

This comparison holds at every root in `N`; the last-contact source
interpretation (15) additionally requires `q` in `B_+`. At the native
depth, (23) becomes

\[
\boxed{
\nu(q)p_{L(q)}^\nu(q)
\le\frac{16}{\delta\log(3/2)\log(q+2)^2}.
}
\tag{24}
\]

In particular, on an escaping spine with `nu(q_i)>=nu(q_0)>0`, the full
collection of prior inputs already implies

\[
p_{L(q_i)}^\nu(q_i)
\le\frac{16}{\delta\nu(q_0)\log(3/2)\log(q_i+2)^2}.
\tag{25}
\]

Thus a proved lower bound of order `1/log(q+2)` on its cofinal marked
roots, or more generally divergence of
`p_L^nu(q) log(q+2)^2` there, would contradict an escaping spine.
Neither lower bound has been supplied.

## 6. What this changes, and the exact remaining estimate

The prior finite-depth estimate bounds a contact front by
`O(L(3/2)^L)` through the critical word densities; (22)--(24) transfer it
to the ordinary flow without changing original source atoms.
Equations (10)--(19)
instead identify one finite **ordinary** source measure simultaneously
for all escaping components and then use a deterministic constraint
on how fast any of its atoms can reach a moving root. They do not
improve the existing quantitative front bound.

The qualitative statement (20), considered alone, would allow decay
slower than `1/log(q+2)^2`. Under the full imported inputs, the sharper
upper bound (25) is also available and must be retained. Finiteness of
`eta` alone supplies no rate for its height tail, no
positive lower bound for the mass in (15), and no comparison between
different components under multiplication by five. The component
capacity budget therefore does not discharge the moving-root capture
or finite-reference energy condition.

The first unsupported inference in a proposed closure would be to
infer such a quantitative lower bound from finite boundary mass,
almost-sure fixed-root contact, or total-variation convergence (14).
The actual representation shows why those facts do not provide that
clock estimate: the limiting law gives positive mass to fixed sources
whose distance from the root eventually exceeds the native clock.

All new infinite sums above are nonnegative, or are probability sums
controlled by (8). The new conclusions retain the source-qualified
status of their imported analytic inputs. They exclude no periodic
orbit and establish no new lower contact rate. Their new content is
the canonical last-contact measure, its exact Green representation,
the global capacity identity, and the actual source-tail comparison.
