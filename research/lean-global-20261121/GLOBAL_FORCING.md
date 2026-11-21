# The global inverse-return attack and its exact obstruction

**Status:** the Lean statements listed here compile with Lean 4.34.1 using
only Lean core and the attributed imported definitions. They prove the
stated obstruction to an entire proposed completion architecture. They do
not prove Collatz, and do not rule out mixed or asymmetric certificate
transformations.

The attempted closing mechanism was to invert expanding balanced returns.
If a physical word with `p` odd inputs and `L` shortcut clocks has endpoint

\[
 q=(3^p x+B)/2^L,\qquad 3^p>2^L,
\]

its inverse has smaller starting height:

\[
 x=(2^Lq-B)/3^p<q.
\]

For a balanced pair, the same word system carries `x,5x` to `q,5q`, so
failure of the five comparison at `q` transfers to `x`. Thus a complete
ordinary inverse selector would appear to give the missing well-founded
induction. Expanding balanced returns really do exist; the issue is full
coverage. The analysis below rules out two natural versions of that
coverage target, including the version with no word-length bound.

## 1. A ternary hole for every bounded-rank dictionary

`Expansion.lean` proves directly for actual natural-number orbits that

\[
 2^L<3^{p(x,L)}
 \quad\Longrightarrow\quad
 T^L(x)\not\equiv1\pmod{3^{p(x,L)}}.
\tag{F1}
\]

The proof uses the exact ordinary high-bit lifting identity, a bound on
the canonical binary representative, and the affine lower bound. It does
not assume that an algebraic inverse is a legal path, or silently replace a
positive path by a signed one.

The global consequence in `Forcing.lean` is

\[
 T^L(x)=1+3^K r,\quad 2^L<3^{p(x,L)}
 \quad\Longrightarrow\quad p(x,L)>K.
\tag{F2}
\]

Indeed, if `p<=K`, then `3^p` divides `3^K`; reducing the endpoint modulo
`3^p` gives one and contradicts (F1). The relevant Lean theorem is
`expansion_depth_for_endpoint_lift`.

Consequently any collection of expanding words with odd count bounded by
`K` misses **every** ordinary endpoint `1+3^K r`. This also holds for an
infinite collection with bounded odd count, so in particular for every
finite dictionary. Taking even positive `r` and `K>=1` leaves arbitrarily
large odd ternary units uncovered. A finite exceptional height cutoff
cannot repair this hole. The theorem `bounded_expansion_misses_lift`
contains the exact bounded-rank statement.

This obstruction alone permits a selector with unbounded odd count.
The next result addresses its global geometry.

## 2. Unbounded inverse words still cannot cover the certified domain

Define

\[
 \mathcal U_C=\{q>0:q\text{ is odd},\;3\nmid q,\;q\text{ reaches }1\}.
\]

**Theorem F3.** For every cutoff `B`, there is `q in U_C`, `q>B`, such
that no `x in U_C` with `x<q` has `T^t(x)=q` at any ordinary clock `t`.
This is unconditional: it concerns infinitely many inputs already known
abstractly to have terminating certificates, not hypothetical failing
inputs.

Lean name: `certified_units_inverse_minimal`.

### Proof, including both finiteness and unboundedness

A terminating certificate bounds the entire future orbit. After its first
visit to one the orbit remains in `{1,2}`; before that visit only finitely
many integers occur. Thus every finite subset of `U_C` has a common bound
`M` on all its future orbit values. These facts are formalized as
`basin_orbit_bounded` and `finite_basin_orbits_bounded`.

The certified unit domain is unbounded by an explicit construction. For
odd `n` in the basin, `4n+1` is in the same basin: its first three shortcut
steps agree with the first step from `n`. Three repetitions give

\[
 n\longmapsto64n+21.
\]

This map preserves the class `1 mod6` and preserves basin membership.
Starting at one and iterating therefore gives arbitrarily large positive
certified odd ternary units. The exact Lean statements are
`certified_lift` and `certified_units_unbounded`.

Suppose instead every `q in U_C` above `B` had a smaller ancestor
`x in U_C`. Strong induction on `q` would put every such `q` in the union
of the forward orbits of the finitely many certified units at most `B`:
compose the ancestor path with the induction hypothesis. Equivalently,
strong induction gives the uniform bound `T^t(q)<=M` for every `q in U_C`
and every `t`. At `t=0` this says `q<=M` throughout an unbounded domain,
a contradiction.

The generic statement `no_inverse_descent_cover` isolates this argument
for any unbounded domain whose permitted finite bases have bounded forward
orbits. `arbitrarily_large_inverse_minimal` then supplies cofinally many
primitive inputs. There is no upper bound on the ancestor clock, no
assumption about affine slopes, and no restriction to balanced pairs.

### Exact consequence for the attempted proof

A uniform inverse-return selector reducing **every certified odd ternary
unit** to a smaller certified odd ternary unit cannot exist. Neither an
unbounded return dictionary nor arbitrarily many but finitely many base
cases repairs it. The obstruction concerns the class of selectors, rather
than failure to find a sufficiently large finite search.

This does **not** rule out a selector whose hypothesis includes an actual
failed comparison: the primitive inputs supplied by F3 are certified
sources, and this proof makes no assertion that their fivefold companions
fail. It also does not rule out leaving the unit domain temporarily while
using additional valid comparison transformations. Those distinctions are
needed before applying this obstruction to a larger certificate program.

## 3. What remains after the attempted completion

The latest forward compiler shrinks the available source-certificate
clock when it consumes a positive balanced return. An expanding inverse
move shrinks the source value but grows that clock. The two quantities
cannot simply be declared a common rank. In particular, following an
inverse balanced path and then consuming that very path returns to the
same comparison and certificate suffix. The companion retraction result
in this packet handles this identity exactly.

A possible escape must use an asymmetric transformation that changes the
comparison relation, or prove a failure-sensitive selector on the actual
residuals. The present work supplies neither universal asymmetric coverage
nor an absolute survivor estimate. The full theorem remains open.

## 4. Why the probabilistic and interval inputs did not close this step

The following current sources were inspected for a possible independent
way to force the missing selector; their existing theorems are credited,
not reclassified as new results here.

- PR173, `a09eb47197cd99f218b3fa013c681df65ea0f69a`,
  `research/lean-shell-cover/README.md`: the precise survivor count in
  prescribed shrinking intervals that is equivalent to universal
  convergence, and its actual early-horizon lower bound.
- PR146, `f431078244e868dc699fad011044f0d5e7f76437`,
  `research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md` and
  `FIVE_RETURN_CLOCK_AND_TERMINALS.md`: sharp block synchronization,
  growing ordinary blocks, finite last-return deadlines, and the complete
  occupied-prefix characterization of certified terminal sources.
- PR171, `2bd243b3e05eaa5543adeb2894637b053c9662ca`,
  `research/adaptive-closure-20261121/AFFINE_SECTION_ROOT_RETURN.md`:
  almost-sure paired returns, ordinary density one, and infinite
  subcritical pressure for the full label-blind return dictionary.
- PR168, `e4599b32e4b1a955ac9315d46782d4ad6a5db96c`,
  `research/closure-frontier-20261121/TERNARY_STATIONARY_BOUNDARY.md`:
  weighted coercivity, the source-qualified `L^1` density, failure of
  `L^2` control, and bounded-error conversion.

Those results do not supply the missing assertion about each fixed
ordinary failed input. The occupied-prefix theorem is particularly
relevant: every root-free prefix contains actual certified terminal
sources. Thus eliminating finite prefixes by alleging that they cannot
contain certified sources would contradict an existing construction.

The shift-dynamical alternative also retains a concrete gap. Arbitrarily
long blocks of each label put both constant configurations into the shift
orbit closure of a separating label. Each constant configuration gives an
invariant Dirac probability, so passing to an arbitrary invariant measure
or minimal subsystem does not force a single label at the original
ordinary input. No such regularity or selection property is supplied
here.

## 5. Formalization boundary

`Forcing.lean` imports `CollatzGlobal.Expansion`, which imports the exact
ordinary orbit-lift development. All new assertions are theorem proofs;
there are no added axioms, `sorry`, `admit`, or oracle evaluations. The
public global results use only Lean's standard logical axioms inherited
from the attributed dependency-free basin definitions. Compilation was
actually executed with warnings treated as errors; the repository's
publication receipt supplies the final commit and audit output.


## 6. Publication-refresh delta: PR173 and PR175

The initial PR173 inspection above remains pinned to
`a09eb47197cd99f218b3fa013c681df65ea0f69a`. A later refresh inspected
its README at **`9ca79e54bd2ae9d9cf4c80851f867364fc3a2d3e`**, the
GitHub comparison from that initial pin, and the new public theorem
headings and statement contexts in `PeriodicWindow.lean`,
`DyadicMixing.lean`, `OctaveCriterion.lean`, and `OctaveDeadline.lean`.
The original `ShellCover.lean` changes in that comparison only expose two
previously private supporting declarations. No new full proof audit or
replay of the imported Lean projects is claimed here.

The substantive addition is an exact **finite meeting criterion**. Put
`p=64^s`. For each `x` in `[p,6p)`, compare its trajectory with that of
`p+(x mod p)`, allowing the arms to meet at different clocks at most `t`.
Let `M_s(t)` count failures to meet. The new theorem
`collatz_iff_octave_comparisons` states

\[
 \mathrm{Collatz}\quad\Longleftrightarrow\quad
 \forall K\;\exists s\ge K\;\exists t:
       (24s+1)M_s(t)+1<2^s.
\]

This is a new global implication relevant to our attempt: sufficiently
few **actual ordinary nonmeetings**, along an unbounded sequence of
stages, would settle all components. Its supporting finite dyadic
identity and rigidity inequality keep all source starts within the
specified five blocks. They do not require an external periodic
approximation to be postulated first.

The closing estimate is nevertheless still absent. The same update's
`octave_deadline` proves, for every `s>=3`,

\[
 M_s(6s+\lfloor s/2\rfloor)\ge2^{s-1}.
\]

This exceeds the admissible budget, although the finite residue-square
identity already mixes at `6s`. The construction excludes meetings at
unequal clocks as well as equal clocks. Therefore quotient mixing cannot
supply the needed ordinary meeting estimate at that proposed horizon.
Our residual compiler and inverse-descent theorems do not bound
`M_s(t)` at the later times left open by this criterion.

For PR175, the packet README was inspected at
**`ad513f1ea609ed47dbcf997df0f09c16557264ee`**,
`research/lean-global-closure-20261121/README.md`. Its reported compiled
checkpoint proves that an actual positive orbit which never hits one
satisfies `2^(4t) <= 2^(7p_t) n^4` at every clock. It also gives a
source-relative convergence certificate and the equivalence
`ForwardFiveClosure iff RelativeBudgetReturns`. The README explicitly
leaves `RelativeBudgetReturns` unproved. This is a necessary parity
budget and a conditional closing interface; it supplies neither the
missing ordinary meeting estimate in PR173 nor a complete selector for
our residual sources. This refresh did not replay or independently audit
PR175's Lean proof or inspect the longer route note.
