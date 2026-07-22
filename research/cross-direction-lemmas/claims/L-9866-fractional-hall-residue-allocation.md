# L-9866 -- Fractional Hall converse for residue allocation

Claim ID: `L-9866`  
Title: Hall no-outlet cuts exactly characterize finite fractional residue allocation  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01-a`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9860`  
Scope: finite fractional transportation of set-valued decoder demand into residue capacities  
Related counterexample candidates: none

## Definitions

Let `Q` be a finite residue set and let

\[
\mathscr P\subseteq 2^Q\setminus\{\varnothing\}
\tag{1}
\]

be a finite family of nonempty allowed-residue patterns. Give every pattern
`S in mathscr P` a demand `mu_S>=0`, and every residue `a in Q` a capacity
`c_a>=0`. Put

\[
d=\sum_{S\in\mathscr P}\mu_S,
\qquad
\mu(B)=\sum_{\substack{S\in\mathscr P\\S\subseteq B}}\mu_S,
\qquad
c(B)=\sum_{a\in B}c_a
\tag{2}
\]

for `B subseteq Q`.

A fractional residue allocation is an array

\[
f=(f_{S,a})_{S\in\mathscr P,\ a\in Q}
\tag{3}
\]

such that

\[
\boxed{
\begin{aligned}
f_{S,a}&\ge0,\qquad f_{S,a}=0\quad(a\notin S),\\
\sum_{a\in S}f_{S,a}&=\mu_S\quad(S\in\mathscr P),\\
\sum_{\substack{S\in\mathscr P\\a\in S}}f_{S,a}&\le c_a
\quad(a\in Q).
\end{aligned}
}
\tag{4}
\]

The first sum allocates all pattern demand; the second never exceeds the
available capacity of an ordinary residue class.

## Statement

### 1. Sharp fractional Hall converse

The following are equivalent:

\[
\boxed{
\begin{array}{ll}
\text{(i)}&\text{A fractional residue allocation (4) exists};\\[1mm]
\text{(ii)}&
\displaystyle
\mu(B)\le c(B)
\quad\text{for every }B\subseteq Q.
\end{array}
}
\tag{5}
\]

Equivalently, the no-outlet Hall cuts

\[
\boxed{
\sum_{\substack{S\in\mathscr P\\S\subseteq B}}\mu_S
\le
\sum_{a\in B}c_a
\qquad(B\subseteq Q)
}
\tag{6}
\]

are not only necessary but sufficient for this finite fractional problem.

This is a converse at the level of real-valued aggregate transportation. It
does not yet assign one residue, or one ordinary integer, to an individual
phase or orbit time.

### 2. Exact max-flow deficiency formula

Build a finite directed network with source `s`, sink `t`, one pattern node
for each `S in mathscr P`, and one residue node for each `a in Q`. Its edges
and capacities are

\[
\boxed{
\begin{array}{c|c}
\text{edge}&\text{capacity}\\ \hline
s\longrightarrow S&\mu_S\\
S\longrightarrow a\quad(a\in S)&K\\
a\longrightarrow t&c_a,
\end{array}
\qquad
K=d+c(Q)+1.
}
\tag{7}
\]

Let `v_max` be its maximum flow value. Then

\[
\boxed{
v_{\max}
=d-max_{B\subseteq Q}\bigl(\mu(B)-c(B)\bigr).
}
\tag{8}
\]

The maximum on the right is nonnegative because `B=emptyset` contributes
zero. Thus the largest Hall overload is exactly the mass which no fractional
allocation can route. In particular, (6) holds exactly when `v_max=d`, and
any maximum flow then gives `f_(S,a)` on the middle edges.

If all demands and capacities are rational, an allocation can be chosen
rational. After clearing denominators, any finite integral max-flow
algorithm constructs one. For arbitrary real data, (8) is the ordinary
finite real-capacity max-flow/min-cut theorem.

### 3. Equivalent unsaturated pattern-family cuts

For a collection `mathscr C subseteq mathscr P`, define its residue
neighborhood

\[
\Gamma(\mathscr C)=\bigcup_{S\in\mathscr C}S.
\tag{9}
\]

Then (6) is equivalent to the familiar family form

\[
\boxed{
\sum_{S\in\mathscr C}\mu_S
\le c\bigl(\Gamma(\mathscr C)\bigr)
\qquad(\mathscr C\subseteq\mathscr P).
}
\tag{10}
\]

The saturated cut `mu(B)` is the strongest demand collection whose entire
residue neighborhood is contained in `B`.

### 4. Tight cuts are saturated and impermeable

Call `B subseteq Q` tight when

\[
\mu(B)=c(B).
\tag{11}
\]

Assume the Hall conditions and let `f` be any feasible allocation. Put

\[
\ell_a=\sum_{\substack{S\in\mathscr P\\a\in S}}f_{S,a}.
\tag{12}
\]

Every tight cut has the following forced structure:

\[
\boxed{
\begin{aligned}
\ell_a&=c_a &&(a\in B),\\
f_{S,a}&=0 &&(S\not\subseteq B,\ a\in B).
\end{aligned}
}
\tag{13}
\]

Thus every residue in `B` is saturated by demand whose whole allowed set is
already inside `B`; crossing patterns cannot send any additional mass into
the cut. This conclusion holds for every feasible allocation, not only for
one selected max flow.

The tight cuts also form a lattice: if `B_1` and `B_2` are tight, then so are

\[
B_1\cap B_2
\qquad\text{and}\qquad
B_1\cup B_2.
\tag{14}
\]

### 5. Fractional relaxation of an ergodic set-valued decoder

Use the decoder setting of `L-9860` with

\[
Q=\mathbb Z/q\mathbb Z,
\qquad
\mathscr P=2^Q\setminus\{\varnothing\},
\qquad
E_S=\{x:D(x)=S\}.
\tag{15}
\]

For every nonempty decoder pattern define its weighted demand, and define
the residue capacity, by

\[
\boxed{
\mu_S
=\frac1m\int_{E_S}\frac1{R(x)}\,d\nu(x),
\qquad
c_a=\frac{M_a}{q}.
}
\tag{16}
\]

The fibers are disjoint, so the inequalities `L-9860/(14)` are precisely

\[
\sum_{S\subseteq B}\mu_S
=\frac1m\int_{\{x:D(x)\subseteq B\}}\frac1R\,d\nu
\le
\frac1q\sum_{a\in B}M_a
=\sum_{a\in B}c_a.
\tag{17}
\]

Consequently, the entire Hall family from `L-9860` passes if and only if
there are fractional masses `f_(S,a)` satisfying (4) with the data (16).

For `mu_S>0`, put

\[
p_{S,a}=\frac{f_{S,a}}{\mu_S}.
\tag{18}
\]

Then `(p_(S,a))_(a in S)` is a probability vector. Choosing an arbitrary
probability vector on each zero-demand pattern gives a patternwise stochastic
kernel

\[
p_a(x)=p_{D(x),a},
\qquad
p_a(x)=0\quad(a\notin D(x)),
\qquad
\sum_{a\in Q}p_a(x)=1.
\tag{19}
\]

Because there are finitely many Borel pattern fibers, this kernel is
measurable, and its aggregate weighted loads obey

\[
\boxed{
\frac1m\int_X\frac{p_a(x)}{R(x)}\,d\nu(x)
=\sum_{S\in\mathscr P}f_{S,a}
\le\frac{M_a}{q}.
}
\tag{20}
\]

Equations (18)--(20) are the exact fractional meaning of passing all Hall
cuts. They produce probability weights, not an actual residue-valued phase
decoder.

### 6. Interpretation boundary

The finite converse (5) does **not** prove any of the following:

1. a deterministic measurable selector `rho(x) in D(x)` with the same
   capacity bounds;
2. a selection of residues along the individual orbit times `x_n`;
3. a matching from those times to distinct or bounded-multiplicity positive
   integers in the selected residue classes;
4. compatibility with the moving size threshold, temporal order, normalized
   growth, or intermediate dynamics; or
5. coherence of selections at different moduli.

Even if a separate nonatomicity or purification theorem produced a
deterministic measurable selector, it would still not supply the integer or
dynamic assertions in items 2--5. The present result is a sharp static
fractional relaxation and nothing stronger.

## Proof

### Necessity of the cuts

Suppose `f` satisfies (4). For every `B subseteq Q`, all demand from a pattern
`S subseteq B` is supported inside `B`. Hence

\[
\begin{aligned}
\mu(B)
&=\sum_{S\subseteq B}\sum_{a\in S}f_{S,a}\\
&\le\sum_{a\in B}\sum_{\substack{S\in\mathscr P\\a\in S}}f_{S,a}
\le\sum_{a\in B}c_a
=c(B).
\end{aligned}
\tag{21}
\]

This proves necessity in (5).

### Sufficiency and the exact cut formula

Consider the network (7). Its total capacity out of the source is `d`, so
`v_max<=d`. The cut with only `s` on the source side has capacity exactly
`d`; hence a minimum cut has capacity at most `d<K` and cannot cross any
middle edge of capacity `K`.

Let `mathscr C` be the pattern nodes and `B` the residue nodes on the source
side of such a cut. Not crossing a middle edge says

\[
S\subseteq B
\qquad(S\in\mathscr C).
\tag{22}
\]

Its capacity is

\[
d-\sum_{S\in\mathscr C}\mu_S+c(B).
\tag{23}
\]

For fixed `B`, nonnegativity of the demands makes this smallest when
`mathscr C` contains every `S subseteq B`. The canonical cut therefore has
capacity

\[
d-\mu(B)+c(B).
\tag{24}
\]

Conversely, putting precisely those pattern nodes and the residues `B` on
the source side gives a cut with (24), and no middle edge crosses it. Thus
finite max-flow/min-cut gives

\[
v_{\max}
=\min_{B\subseteq Q}\bigl(d-\mu(B)+c(B)\bigr)
=d-\max_{B\subseteq Q}\bigl(\mu(B)-c(B)\bigr),
\tag{25}
\]

which is (8).

If all Hall cuts hold, (25) gives `v_max=d`. Every source edge is then
saturated. Flow conservation at a pattern node gives its row sum in (4),
and flow conservation at a residue node gives its column bound. The middle
edge flows are the required `f_(S,a)`. This proves sufficiency.

### Pattern families and tight-cut structure

If (6) holds and `mathscr C subseteq mathscr P`, take
`B=Gamma(mathscr C)`. Every member of `mathscr C` is contained in `B`, so

\[
\sum_{S\in\mathscr C}\mu_S
\le\mu(B)\le c(B),
\tag{26}
\]

which is (10). Conversely, for fixed `B`, take
`mathscr C={S in mathscr P:S subseteq B}` in (10). Its neighborhood is
contained in `B`, so `mu(B)<=c(Gamma(mathscr C))<=c(B)`. This proves
equivalence.

Now let `B` be tight. Patterns contained in `B` send all of their mass into
`B`, contributing exactly `mu(B)=c(B)`. Since the total load of `B` is at
most `c(B)`, no other mass can enter and the total load equals capacity.
Every individual deficit `c_a-ell_a` is nonnegative and their sum over `B`
is zero. Hence each is zero, proving (13).

Finally, `mu(B)` is supermodular. Indeed, for every fixed pattern `S`, the
indicator of `S subseteq B` satisfies

\[
\mathbf1_{\{S\subseteq B_1\}}
+\mathbf1_{\{S\subseteq B_2\}}
\le
\mathbf1_{\{S\subseteq B_1\cap B_2\}}
+\mathbf1_{\{S\subseteq B_1\cup B_2\}}.
\tag{27}
\]

After multiplication by `mu_S` and summation, this proves supermodularity.
Since `c(B)` is modular, the Hall slack

\[
h(B)=c(B)-\mu(B)
\tag{28}
\]

is submodular and nonnegative. If `h(B_1)=h(B_2)=0`, then

\[
0\le h(B_1\cap B_2)+h(B_1\cup B_2)
\le h(B_1)+h(B_2)=0.
\tag{29}
\]

Both new cuts are tight, proving (14).

### Ergodic specialization and quarantine

Equation (17) follows from (16), disjointness of the pattern fibers, and the
definition of the no-outlet region in `L-9860/(8)`. Applying (5) gives the
fractional allocation. Division by each positive row demand gives (18)--(19),
and

\[
\begin{aligned}
\frac1m\int_X\frac{p_a(x)}{R(x)}\,d\nu(x)
&=\sum_{S\in\mathscr P}
\frac1m\int_{E_S}\frac{p_{S,a}}{R(x)}\,d\nu(x)\\
&=\sum_{S\in\mathscr P}\mu_Sp_{S,a}
=\sum_{S\in\mathscr P}f_{S,a}.
\end{aligned}
\tag{30}
\]

The column constraint proves (20). Nothing in the finite flow labels an
individual phase or time by one residue, and nothing matches that label to
an integer. This proves exactly the fractional corollary and completes the
proof. QED

## Motivation

`L-9860` proves that every set-valued decoder must pass a finite collection
of no-outlet residue cuts. It deliberately leaves matching sufficiency open
because ordinary endpoint construction has much more structure than a
finite capacity comparison.

The present theorem closes precisely the static fractional layer. The Hall
cuts have no missing finite-dimensional obstruction: they are the min cuts
of one explicit transportation network. The remaining gap is therefore not
fractional capacity but deterministic selection, integer realization, and
dynamical coherence.

## Dependency audit

- The abstract equivalence, deficiency formula, tight-cut structure, and
  lattice property use only finite max-flow/min-cut and are proved here.
- `L-9860` supplies the ergodic pattern demands and proves that any actual
  bounded-multiplicity integer sequence satisfies the cuts.
- No measurable-selection, purification, integral matching, or ergodic
  decomposition theorem is used.
- No Collatz convergence, connectivity, or ordinary-orbit premise is used.

## Gap audit

- Fractional feasibility is not deterministic residue selection.
- Real-valued flow is not a matching of orbit times to ordinary integers.
- The capacities `M_a/q` are asymptotic aggregate capacities; the flow does
  not enforce finite-cutoff rounding or the moving threshold in `L-9860`.
- The theorem is single-modulus and does not make selections compatible
  under reduction from a larger modulus.
- No temporal, carry, chart, or intermediate-orbit constraint is represented
  in the network.
- Tight-cut decomposition isolates saturated aggregate channels only; it
  does not produce a dynamical decomposition of the phase system.

## Adversarial tests

- The relevant demand is `sum_(S subseteq B) mu_S`, not the demand of all
  patterns merely intersecting `B`.
- The middle-edge capacity `K` is chosen strictly larger than `d`, so a
  minimum cut never crosses an allowed pattern-to-residue edge. Treating it
  as a unit-capacity edge would give the wrong theorem.
- For a fixed residue cut `B`, every nonnegative-demand pattern contained in
  `B` belongs on the source side of the minimizing cut. Omitting one only
  increases the cut capacity.
- Column inequalities are capacities, not required equalities. Equality is
  forced only inside a tight cut, as in (13).
- A tight cut blocks incoming mass from crossing patterns; it does not force
  how its internal patterns split among its saturated residues.
- The measurable object in (19) is a probability vector, not a residue-valued
  selector.
- Rational max flow gives a rational fractional allocation, not an integral
  orbit matching unless additional divisibility and finite-instance data are
  supplied.

## Remaining uncertainty

Under what additional hypotheses can the fractional kernel (19) be purified
to a deterministic selector without violating capacities, and when can such
a selector be realized coherently along one uniquely ergodic orbit by actual
bounded-multiplicity integers? Neither question is answered by finite Hall
cuts alone.

## Suggested next attack

For one concrete return architecture, compute the tight-cut lattice and
contract its maximal proper members. The resulting unsaturated quotient
identifies exactly where deterministic residue choices still have freedom.
Then test whether the finite carry dynamics admits a selector on that
quotient which is compatible across the next power-of-two modulus; failure
would locate the first genuinely nonfractional obstruction.
