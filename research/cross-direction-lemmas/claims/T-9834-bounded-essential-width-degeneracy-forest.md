# T-9834 -- Bounded-essential-width degeneracy forests

Claim ID: `T-9834`
Title: Arbitrarily long zero sums with uniformly bounded nondegenerate leaves have a finite primitive leaf alphabet, and a height-carrying leaf is impossible
Status: `PROPOSED / SOURCE-QUALIFIED BOUNDED-ESSENTIAL-WIDTH CLOSURE`
Authoring agent: `gpt56-synthesis-01-wave22-fixed-width-sunit`
Reviewing agents: `gpt56-synthesis-01-wave22-h-sunit-transfer`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9831`, `T-9828`, `L-9900`, `L-9901`, `L-9902`; PR #33 at `c9d62bce3e93f5785f72e4520bc576863d9379eb`; PR #38 `ACL-N071` at `5ad965771869a647102e22115ed56749dbe2e254`; Evertse 1984 Corollary 1
Scope: exact integer zero-sum stage families of arbitrary nominal length that admit uniformly bounded zero-sum leaf decompositions
Related counterexample candidates: none; this is an exclusion and structural-reduction theorem
Related atom: PR #38 `ACL-N071`

## Motivation

`T-9831` closes every genuinely bounded-dimensional nondegenerate
almost-`S`-unit relation.  A tempting but false next step is to apply the same
argument directly when the number of displayed terms tends to infinity.
Evertse's dimension is fixed, and a word of arbitrary length over finitely many
admissible blocks can still carry unbounded combinatorial information.

There is nevertheless a rigorous extension.  A long degenerate relation can
be split into inclusion-minimal zero-sum leaves.  If those leaves have bounded
width and satisfy one uniform primitive endpoint-product gate, then only
finitely many primitive leaf types occur.  Moreover, if the leaf containing a
maximal raw coordinate retains divergent primitive height, even an
arbitrarily long ambient relation is impossible.  This isolates the exact
escape left for `ACL-N071`: genuinely unbounded essential width, loss of a
fixed internal prime union, a critical endpoint product, or height and
complexity stored only in block scales and forest assembly.

The source heads used here are frozen as follows:

- PR #33: `c9d62bce3e93f5785f72e4520bc576863d9379eb`;
- PR #38: `5ad965771869a647102e22115ed56749dbe2e254`.

The theorem does not import a growing-dimension version of Evertse.  Every
application below is made only after passing to a leaf of dimension at most a
fixed integer `W`.

## Definitions

Fix a finite set `S` of rational primes.  For a nonzero integer `z`, put

\[
 \operatorname{out}_S(z)
 =|z|\prod_{p\in S}|z|_p
 =\prod_{p\notin S}p^{v_p(z)}.
\tag{1}
\]

A **raw stage relation** is an ordered tuple

\[
 a=(a_1,\ldots,a_N)\in(\mathbf Z\setminus\{0\})^N,
 \qquad
 \sum_{i=1}^N a_i=0.
\tag{2}
\]

The nominal length `N` is unrestricted.  The coordinate set is divided into
endpoint slots `E` and internal slots `I=E^c`, with

\[
 \operatorname{out}_S(a_i)=1
 \qquad(i\in I).
\tag{3}
\]

Thus internal coordinates are integer `S`-units.  Fixed integral or rational
coefficient menus may first be absorbed into the coordinates exactly as in
`T-9831`; all coefficient and denominator primes must then be placed in the
one fixed set `S`.

A nonempty coordinate set `C\subseteq\{1,\ldots,N\}` is a **zero-sum
leaf** if

\[
 \sum_{i\in C}a_i=0
\tag{4}
\]

and no nonempty proper subset of `C` has sum zero.  Since every coordinate is
nonzero, every leaf has at least two elements.  A **zero-sum forest** is a
partition

\[
 \mathcal F=\{C_1,\ldots,C_q\}
\tag{5}
\]

of all coordinate slots into zero-sum leaves.  Its width is

\[
 \operatorname{width}(\mathcal F)=\max_r|C_r|.
\tag{6}
\]

The **partition-essential width** of `a` is the minimum of (6) over all its
zero-sum forests.  This is an existence notion: it does not assert that every
minimal zero-sum subset, or every possible forest, has the same bound.

For a leaf `C`, retain the ambient coordinate order and define

\[
 g_C=\gcd_{i\in C}|a_i|,
 \qquad
 x_C=(a_i/g_C)_{i\in C},
 \qquad
 h_C=\|x_C\|_\infty.
\tag{7}
\]

Also put

\[
 e_C=|C\cap E|,
 \qquad
 B_C=\prod_{i\in C\cap E}\operatorname{out}_S(a_i),
 \qquad
 P_C=\prod_{i\in C}\operatorname{out}_S(x_{C,i}).
\tag{8}
\]

Empty endpoint products equal one.  The vector `x_C` is the primitive ordered
representative of the leaf projective point.

## Lemma 1 -- forest existence and exact endpoint transfer

Every raw stage relation has a zero-sum forest.  For every leaf in every such
forest,

\[
 P_C
 =\prod_{i\in C\cap E}\operatorname{out}_S(x_{C,i})
 ={B_C\over\operatorname{out}_S(g_C)^{e_C}}
 \le B_C.
\tag{9}
\]

In particular, all normalized internal coordinates remain `S`-units.

### Proof

If the full coordinate set is a leaf, it is already a one-leaf forest.  If it
is not, choose a nonempty proper zero-sum subset `J`.  Its complement is also
nonempty and zero-sum.  Repeat on both pieces.  Cardinality decreases at every
split, so the finite binary splitting process terminates, and its terminal
pieces are precisely zero-sum leaves.  This proves existence.

For every `i\in C`, divisibility by `g_C` gives

\[
 \operatorname{out}_S(a_i/g_C)
 ={\operatorname{out}_S(a_i)\over
   \operatorname{out}_S(g_C)}.
\tag{10}
\]

If `C` contains an internal coordinate, then `g_C` divides an integer
`S`-unit, so `\operatorname{out}_S(g_C)=1`.  Every normalized internal
coordinate is consequently still an `S`-unit, and (9) follows.  If `C`
contains no internal coordinate, then `e_C=|C|`, and multiplying (10) over
all coordinates again gives (9).  The inequality uses
`\operatorname{out}_S(g_C)\ge1`.  **QED**

## Theorem 2 -- finite primitive leaf alphabet

Fix once and for all

\[
 S,\qquad W\ge2,\qquad C_0>0,
 \qquad 0\le d<1.
\tag{11}
\]

Let `\mathscr A` be any collection of raw stage relations, with no bound on
their nominal lengths.  Suppose each `a\in\mathscr A` is supplied with a
witness forest `\mathcal F(a)` such that every leaf `C\in\mathcal F(a)`
satisfies

\[
 |C|\le W,
 \qquad
 P_C\le C_0h_C^d.
\tag{12}
\]

Then the collection of all primitive ordered leaf vectors

\[
 \mathscr L
 =\{x_C:a\in\mathscr A, C\in\mathcal F(a)\}
\tag{13}
\]

is finite.  The conclusion remains true after decorating a leaf by its
endpoint mask or by any other fixed finite menu of local labels.

### Proof

Every leaf vector is primitive, has zero coordinate sum, and is
nondegenerate: a proper vanishing subsum would contradict the definition of a
leaf.  Lemma 1 and (12) give

\[
 \prod_{i\in C}\operatorname{out}_S(x_{C,i})
 \le C_0\|x_C\|_\infty^d.
\tag{14}
\]

For a fixed leaf size `r` with `3\le r\le W`, Evertse's 1984 Corollary 1
applies with source dimension `r-1`, the fixed set `S`, and the fixed constants
`C_0,d`.  It gives only finitely many primitive ordered `r`-tuples satisfying
(14).  A two-coordinate primitive zero-sum leaf is directly one of

\[
 (1,-1),\qquad(-1,1),
\tag{15}
\]

so size two is finite without an external theorem.  Taking the finite union
over `2\le r\le W` proves (13).  There are at most `2^W` endpoint masks and
only finitely many assumed local decorations, so adjoining them preserves
finiteness.  **QED**

## Theorem 3 -- marked height-core exclusion

Let `(a_m)` be an infinite sequence of raw stage relations.  Put

\[
 H_m=\max_i|a_{m,i}|,
\tag{16}
\]

and mark the least index attaining `H_m`.  Suppose that for every `m` there is
a witness forest of width at most one fixed `W`, and let `C_m` be the unique
leaf in that forest containing the marked coordinate.  No bound is imposed on
the number of other leaves.

Assume the internal prime set `S` is fixed and, for some fixed `C_0>0` and
`d<1`,

\[
 P_{C_m}\le C_0h_{C_m}^d.
\tag{17}
\]

If the marked primitive leaf heights are unbounded, or equivalently if the
marked primitive leaf projective points form an infinite set, then no such
stage sequence exists.

More intrinsically, along any subsequence on which `h_{C_m}\to\infty`, define

\[
 \Xi_{\rm core}
 =\limsup_{m\to\infty}
   {\log P_{C_m}\over\log h_{C_m}}.
\tag{18}
\]

The exact endpoint-method gate is

\[
 \boxed{\Xi_{\rm core}<1.}
\tag{19}
\]

Indeed, (19) itself supplies constants as in (17), so it also excludes the
sequence.

### Proof

Apply the proof of Theorem 2 only to the selected leaves `C_m`; no estimate on
the other leaves is used.  Their dimensions lie in the finite set
`\{2,\ldots,W\}`.  Equation (17) therefore permits only finitely many
primitive selected leaf vectors.  Their heights are bounded, contradicting
the assumed unboundedness.  Conversely, in bounded dimension an infinite set
of primitive integer projective points has unbounded height, so the two
formulations are equivalent after passage to a subsequence.

If (19) holds, choose

\[
 \Xi_{\rm core}<d<1.
\tag{20}
\]

Then eventually `P_{C_m}\le h_{C_m}^d`, which is (17) with `C_0=1`.
**QED**

The marked coordinate is used only to make the raw-height corollary below
automatic.  Any other architecture-defined leaf selector is equally valid if
its normalized leaf vectors are proved infinite or its primitive heights are
proved unbounded.

## Corollary 4 -- raw endpoint and leaf-gcd certificate

In Theorem 3, the marked leaf has raw height exactly `H_m`.  Write

\[
 g_m=g_{C_m},
 \qquad
 B_m=B_{C_m},
 \qquad
 h_{C_m}={H_m\over g_m}.
\tag{21}
\]

Assume `H_m\to\infty` and define

\[
 \gamma=\limsup_{m\to\infty}{\log g_m\over\log H_m}<1,
 \qquad
 \Theta=\limsup_{m\to\infty}{\log B_m\over\log H_m}.
\tag{22}
\]

For a prescribed `0<d<1`, the sufficient raw gate is

\[
 \boxed{\Theta<d(1-\gamma).}
\tag{23}
\]

Under (23), no such infinite sequence exists.  In particular, the marginal
raw certificate supplies some admissible Evertse exponent exactly when

\[
 \Theta<1-\gamma.
\tag{24}
\]

Here "marginal raw certificate" is essential: (24) is sufficient, not a
necessary substitute for the exact primitive invariant (18).

### Proof

Choose `\varepsilon>0` such that

\[
 (1+d)\varepsilon
 <d(1-\gamma)-\Theta,
 \qquad
 \varepsilon<1-\gamma.
\tag{25}
\]

Eventually,

\[
 g_m\le H_m^{\gamma+\varepsilon},
 \qquad
 B_m\le H_m^{\Theta+\varepsilon}.
\tag{26}
\]

Therefore

\[
 h_{C_m}\ge H_m^{1-\gamma-\varepsilon}
 \longrightarrow\infty,
\tag{27}
\]

and Lemma 1 gives

\[
 P_{C_m}
 \le B_m
 \le H_m^{\Theta+\varepsilon}
 \le H_m^{d(1-\gamma-\varepsilon)}
 \le h_{C_m}^d.
\tag{28}
\]

Theorem 3 now applies.  Condition (24) is equivalent to the existence of a
`d` strictly between `\Theta/(1-\gamma)` and one.  **QED**

The leaf product `B_m` in (22) may be replaced by the larger full-stage
endpoint product

\[
 \mathcal B_m
 =\prod_{i\in E_m}\operatorname{out}_S(a_{m,i}),
\tag{29}
\]

because `B_m\le\mathcal B_m`.  This replacement is often convenient but can
be very wasteful when the number of endpoints grows.

At the equality level, fixed constants still matter.  If

\[
 g_m\le C_gH_m^\gamma,
 \qquad
 B_m\le C_BH_m^{d(1-\gamma)},
 \qquad \gamma<1, d<1,
\tag{30}
\]

then

\[
 P_{C_m}\le C_BC_g^d h_{C_m}^d,
\tag{31}
\]

so Theorem 3 again applies.  The gcd in (22) and (30) is the gcd of the
selected leaf, not the gcd of the full ambient tuple.

## Corollary 5 -- finite-fibre architectural exclusion

Under the hypotheses of Theorem 2, suppose an architecture supplies a marked
leaf in each distinct physical stage and the map

\[
 \{
   \text{physical stages}
  \}
 \longrightarrow
 \{
   \text{decorated primitive marked leaves}
  \}
\tag{32}
\]

has finite fibres.  Then there are only finitely many physical stages.

This formulation covers a proved ratio separator, a state-recovery lemma, or
any other exact finite-to-one reconstruction from the marked leaf.  It does
not follow merely from distinctness of the full ambient tuples.

### Proof

Theorem 2 makes the target of (32) finite.  A finite union of finite fibres is
finite.  **QED**

## What can and cannot be frozen

For one finite ordered stage there are only finitely many set partitions.  If
an application proves that at least one witness forest satisfies the required
width and endpoint conditions, it may choose the lexicographically first such
forest.  Thus nonuniqueness causes no choice ambiguity.

Across stages of unbounded nominal length, however, the following distinction
is mandatory.

1. The entire partition, number of leaves, binary splitting tree, and sequence
   of leaf labels need not lie in any finite catalogue.  They cannot in
   general be frozen on an infinite subsequence.
2. A selected leaf dimension can be frozen because it belongs to
   `\{2,\ldots,W\}`.  Its endpoint mask and any genuinely finite local label
   can also be frozen.  Evertse needs only the dimension, fixed `S`, fixed
   constants, nondegeneracy, and primitivity; it does not need a frozen forest
   shape.
3. Primitivity must be imposed leaf-by-leaf through division by `g_C`.  A
   primitive full tuple can contain a leaf with an arbitrarily large gcd.
4. Projective distinctness of full tuples does not pass to selected leaves.
   It passes only through a leaf-level height argument, a leaf ratio
   separator, or a finite-fibre recovery theorem such as Corollary 5.
5. Theorem 2 freezes primitive leaf shapes, not their raw multipliers.  The
   raw leaves `q_Cx_C` may have unbounded `S`-unit scales even when `x_C`
   ranges over a finite set.

Consequently a bounded-essential-width degeneracy forest reduces a proposed
infinite construction to three pieces of residual data:

\[
 \boxed{
 \text{finite primitive leaf alphabet}
 +\text{ raw block scales}
 +\text{ unbounded forest word/tree}.}
\tag{33}
\]

Only the first piece is controlled by Evertse.

## Consequence for PR #33 and ACL-N071

The PR #33 relation is the one-leaf special case with width `258`, internal
prime set `\{2,3\}`, block gcd dividing `216`, and endpoint exponent at most

\[
 {6498\over346819}<{1\over50}.
\tag{34}
\]

The present theorem remains applicable if a later exact compiler expands that
relation into arbitrarily many cancelling pieces, provided a witness forest
has a height-carrying leaf of uniformly bounded width retaining the same
leaf-gcd and endpoint estimates.  Harmless nominal padding is therefore not a
new escape from the PR #33 arithmetic closure.

For `ACL-N071`, the result closes precisely the bounded-essential-width
branch.  Fresh endpoint primes are allowed: only their total primitive
outside-`S` product on the marked leaf is constrained.  Hence a proposed
collision or H architecture satisfying (19), or the raw certificate (23),
must fail if its growing height remains visible in one bounded leaf.

The theorem does **not** derive a contradiction from positive factor
complexity alone.  A finite leaf alphabet supports aperiodic and even
linear-complexity words.  To finish `ACL-N071`, the shrinking room/residue
classes must additionally force one of the following:

- a finite-fibre recovery map from a leaf;
- a bounded leaf whose primitive height diverges;
- a contradiction for the residual raw scale process; or
- a genuinely new theorem for unbounded essential width.

Thus this claim identifies the exact escape feature rather than relabelling a
growing-dimensional equation as fixed-dimensional.

## Sharp counterexamples and boundary tests

### 1. Unbounded essential width

For every `N\ge3`, the `N`-tuple

\[
 \left(
  2^{N-2},-2^0,-2^1,\ldots,-2^{N-3},-1
 \right)
\tag{35}
\]

is a primitive zero sum with exactly one positive coordinate.  With
`S=\{2\}`, every coordinate is an `S`-unit and its outside product is one.
No proper subset sums to zero, so its only forest has one leaf of size `N`.
The primitive height tends to infinity.  This is the diagonal obstruction:
fixed `S`, zero endpoint mass, and nondegeneracy do not compensate for
unbounded essential width.

### 2. No uniform subunit exponent

For `S=\{2\}`, take

\[
 x_m=(2^m,-(2^m-1),-1),
\tag{36}
\]

with the middle coordinate designated as the only endpoint.  This is a
primitive nondegenerate leaf of width three, but

\[
 h_m=2^m,
 \qquad
 P_m=2^m-1,
 \qquad
 {\log P_m\over\log h_m}\longrightarrow1.
\tag{37}
\]

Each individual leaf satisfies `P_m=h_m^{d_m}` for some `d_m<1`, but
`d_m\to1`.  Therefore stage-dependent exponents below one are useless; one
uniform `d<1`, or equivalently the strict limsup gate (19), is necessary.

### 3. No fixed prime union

Let `M_m` be the product of the first `m` primes and let `S_m` contain every
prime dividing `M_m(M_m-1)`.  Then

\[
 (M_m,-(M_m-1),-1)
\tag{38}
\]

is a primitive nondegenerate three-term `S_m`-unit zero sum with stagewise
outside product one and unbounded height.  The union of the `S_m` is infinite.
Thus "a finite alphabet at each stage" cannot replace one fixed finite union.

### 4. Full primitivity and height do not pass to a leaf

The full tuples

\[
 a_m=(2^m,-2^m,1,-1)
\tag{39}
\]

are primitive, projectively distinct, and have height `2^m`.  They have a
width-two forest, but both leaves normalize to `(1,-1)` up to the inherited
order.  The leaf containing a maximal coordinate has

\[
 g_{C_m}=2^m,
 \qquad h_{C_m}=1.
\tag{40}
\]

This proves that the full gcd, full height, and full projective distinctness
cannot replace the selected-leaf gcd and leaf-level distinctness.

### 5. A full-stage endpoint exponent need not be a leaf exponent

Let `Q_m=2^{m^2}` and concatenate the zero-sum blocks

\[
 (Q_m,-Q_m),
 \qquad
 (2^m,-(2^m-1),-1),
\tag{41}
\]

together with `m` copies of `(1,-1)`.  Designate only `-(2^m-1)` as an
endpoint and take `S=\{2\}`.  The nominal length tends to infinity, the full
tuple is primitive, its forest width is three, and

\[
 H_m=2^{m^2},
 \qquad
 \mathcal B_m=2^m-1,
 \qquad
 {\log\mathcal B_m\over\log H_m}\longrightarrow0.
\tag{42}
\]

Nevertheless the three-term leaf has primitive height `2^m` and endpoint
product `2^m-1`, hence local exponent one, while the maximal two-term leaf has
primitive height one.  A small endpoint exponent relative to an unrelated
ambient scale proves neither the marked-core gate nor a uniform gate for all
leaves.

### 6. Finite leaf types do not control forest words or block scales

Let

\[
 U=(1,-1),
 \qquad
 V=(1,1,-2),
\tag{43}
\]

and fix any Sturmian binary word `w_1w_2\ldots`.  At stage `m`, concatenate
the first `m` blocks, using `2^jU` when `w_j=0` and `2^jV` when `w_j=1`.
Every coordinate is an `S`-unit for `S=\{2\}`; the displayed forest has width
three and primitive outside product one on every leaf.  Yet the nominal
length and raw height grow, and the block directive has factor complexity
`n+1`.

All primitive leaves belong to the two-element alphabet `\{U,V\}`.  The
infinite information lives entirely in the powers-of-two block scales and the
forest word.  This example shows simultaneously that an entire forest type
cannot be frozen, that finite primitive leaf types do not imply finitely many
ambient stages, and that positive symbolic complexity alone does not complete
`ACL-N071`.

## Dependency audit

- Evertse 1984 Corollary 1 is used only in Theorem 2 and only at a fixed leaf
  size `r`, with source dimension `r-1`, fixed finite `S`, fixed `C_0,d`,
  primitivity, and nondegeneracy.
- The two-coordinate case is proved directly, so no unstated lower bound on
  Evertse's source dimension is used.
- `T-9831` supplies the source-qualified fixed-dimensional endpoint theorem
  and the distinction between the exact primitive invariant and the marginal
  raw certificate.  The present proof reconstructs the required hypotheses on
  every selected leaf.
- `T-9828` and PR #33 provide the specialization constants in (34).
- `L-9900` and `L-9901` supply the endpoint-product interpretation and the
  raw normalization pattern.  `L-9902` supplies the growing-dimension
  diagonal obstruction (35).
- PR #38 `ACL-N071` is used only to identify the target interface.  No theorem
  from that branch is imported.

## Source links

- [Evertse 1984, Corollary 1](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)
- [PR #33](https://github.com/gfreund123/collatz/pull/33)
- [PR #38](https://github.com/gfreund123/collatz/pull/38)

## Gap audit

- No statement applies Evertse to the ambient nominal dimension.
- Forest existence alone is not enough.  The width and endpoint gate must hold
  on one supplied witness forest, or at least on the marked leaf selected from
  it.
- A bound on partition-essential width does not bound every overlapping
  minimal zero-sum subset.  The proofs never require that stronger assertion.
- Forest partitions need not be unique.  The proof uses any witness; a
  lexicographic convention can make the choice canonical.
- Internal `S`-unit structure passes to a normalized leaf only because either
  the leaf contains an internal coordinate, forcing its gcd to be an
  `S`-unit, or every coordinate of the leaf is an endpoint.
- Full-stage primitivity, height divergence, and projective distinctness do
  not pass automatically to a leaf.  Equations (39)--(40) are the explicit
  obstruction.
- The raw certificate uses the selected-leaf gcd.  Replacing it by the full
  gcd is invalid.
- The global endpoint product may replace a leaf product only as an upper
  bound; its exponent must still be measured against a scale that survives
  leaf normalization.
- Constants and exponents are uniform before Evertse is invoked.  A sequence
  of exponents approaching one is not a finite type catalogue.
- A finite primitive leaf alphabet does not imply a finite-rank common group
  for the raw block multipliers, nor does it bound the number or ordering of
  leaves.
- The theorem does not derive low endpoint mass, bounded essential width,
  leaf-gcd control, a finite-fibre state recovery map, or physical validity of
  a proposed compiler.  These remain architecture-specific.
- No Collatz counterexample and no proof of the Collatz conjecture are
  claimed.

## Adversarial tests

The six families (35)--(43) independently test the main quantifiers:

1. width must be uniform;
2. the exponent and multiplicative constant must be uniform;
3. the internal prime union must be fixed;
4. primitive height and distinctness must survive on a leaf;
5. the endpoint budget must be relative to that leaf's primitive scale; and
6. a finite leaf alphabet does not freeze raw scales, multiplicities, forest
   shapes, or symbolic complexity.

The proof was also checked against the two endpoint-placement extremes.  If a
leaf contains an internal slot, its gcd has no prime outside `S`.  If it has no
internal slot, every coordinate is an endpoint and the full gcd correction in
(9) is retained.  Thus no unlisted mixed case is lost.

## Remaining uncertainty

There is no uncertainty in the finite-leaf or marked-core implication once
Evertse's cited corollary is accepted.  The unresolved issue for `ACL-N071` is
whether the collision or H room/residue constraints force divergent
primitive height in one bounded leaf, constrain the residual block scales and
forest word, or instead permit genuinely unbounded essential width.

## Suggested next attack

For each collision and H stage compiler, construct an explicit zero-sum forest
and mark the leaf containing the largest physical coordinate.  Compute its
own gcd and primitive endpoint product before using any global height bound.
If its width is bounded and (23) holds, this theorem closes the branch.  If
its primitive shape repeats, record the raw multiplier and the adjacent leaf
labels; the remaining task is then a scale/forest compatibility theorem, not
another fixed-dimensional `S`-unit estimate.
