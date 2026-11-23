# Global merger attack: preserve the section, then test the missing selector

**Full Collatz closure: OPEN.** This pass compared the new band, inverse-fan,
and component-merger packets with the older complete comparison reductions.
It produced two useful all-parameter statements: a direct way to keep a
dyadic affine merger inside the marked section, and a quantitative obstruction
to making the target-dependent population octaves uniformly small. Neither
statement supplies the remaining universal successful selector.

The map is the ordinary shortcut map, with every halving counted:

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

All sources, endpoints, and merger partners below are positive ordinary
integers. A merger means equality of two finite forward iterates; it does
not require the smaller partner to lie on the larger input's forward orbit.

## 1. Sources inspected at exact heads

| Source | Exact head | Interface used in the attempt |
|---|---|---|
| PR173 | `fa0c9e2a2851e6324391e39c17afcb5913185aec` | The actual marked section, bounded visits, and full marked-return criterion |
| PR184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Reserved inverse rebasing, original-source bounds, and lower marked component partners |
| PR183 | `8659cf62ac685540cadeef320e596c852fbb0959` | Lower-mark endpoint budget, quick-offset obstruction, and retained source entrance mass |
| PR176 | `3dbe5542fd6a5a1d63b354225d92391471c17002` | The checked finite marked fan and exact survivor-count criterion |
| PR180 | `9010a8790535002b6d9ff92304f0ba289e2e98fe` | Whole rising-block mergers, exact complementary odd-psi query, and target-dependent marked populations |
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | Older one-sided comparisons, high-bit merger interfaces, and shifted-power residuals |

The relevant mathematical reading surfaces are PR184's
`research/lean-band-coupling-20261121/README.md` and `LATEST_CONNECTIONS.md`;
PR180's `research/lean-forward-band-20261121/BAND_TRANSPORT_NOTE.md`,
`BAND_PARITY_BRIDGE_NOTE.md`, and `MARKED_PREDECESSOR_POPULATIONS.md`;
PR176's `research/lean-global-resolvent-20261121/section/README.md`; and
PR146's `research/upper-bit-mergers/README.md`. This was a targeted synthesis
of their actual hypotheses, not a blanket re-audit of those PRs.

## 2. New compatibility: dyadic extraction preserves markedness

Write `d=floor(log2 n)`. PR173 marks an odd integer `n` when

\[
(d+1)(n-2^d)\le70\,2^d.
\]

**Proposition.** Suppose `n` is marked, `x` is odd, `0<=j<=d`, and

\[
n=2^j x+c,\qquad 0\le c\le n-2^d.
\tag{M1}
\]

Then `x` is marked. If `j>0`, then `x<n`.

Put `q=d-j`. The offset guard gives

\[
2^d\le2^j x\le n<2^{d+1},
\]

so `floor(log2 x)=q`. Also

\[
n-2^d=2^j(x-2^q)+c.
\]

Consequently

\[
2^j(q+1)(x-2^q)
\le(d+1)(n-2^d)
\le70\,2^d
=2^j\,70\,2^q.
\]

Canceling `2^j` proves the exact mark inequality for `x`. Positivity and
`2^j>=2` prove strict size reduction when `j>0`.

In particular, **every odd leading binary prefix of a marked integer is
marked**: take `x=floor(n/2^j)` and `c=n mod2^j`. Since `2^d` is a multiple
of `2^j`, this remainder is at most `n-2^d`.

If an ordinary certificate also gives

\[
T^a(n)=T^b(x),
\tag{M2}
\]

then `(M1)` immediately produces a smaller marked component partner. This
does not need the much stronger absolute size condition
`4*sqrt(x)+2*log2(x)<=log2(n)` from the general small-partner bridge.
Here the shape of the partner itself keeps it in the section.

The file [MarkedDyadicTransport.lean](lean/MarkedDyadicTransport.lean)
encodes this statement, odd-prefix inheritance, the basin transfer, and
the exact global cover equivalence. Compilation status belongs to the
execution receipt for this pass; source text alone is not a compiler receipt.

### Exact global cover, without claiming its existence

Let `DyadicMarkedCover` assert that every marked `n>1` has some `j>0`, odd
`x`, and `c` satisfying `(M1)` and `(M2)`. Then

\[
\mathrm{Collatz}\iff\mathrm{DyadicMarkedCover}.
\tag{M3}
\]

The forward direction takes `j=d`, `x=1`, and `c=n-2^d`, using the actual
hit-to-one certificate. The reverse direction uses strong induction on
marked values, since `(M1)` gives a smaller marked partner and `(M2)`
transfers its basin status. The bounded-visit theorem then covers every
positive ordinary input. No ordinary convergence floor is inserted into
the marked induction.

The new statement is a compatibility theorem for possible selectors. The
existence of a successful selector in `(M3)` is still the global problem.

### A broader class: rounding the prefix upward

The nonnegative offset guard in `(M1)` is not the limit of section-preserving
extraction. If `1<=j<=d` and `x=ceil(n/2^j)` is odd, then **x is marked as
well**. For odd `n`, this ceiling is `floor(n/2^j)+1`.

To see the available rounding room, put `q=d-j`, `r=n-2^d`, and
`t=x-2^q`. The oddness condition excludes the upper power-of-two endpoint,
so `floor(log2 x)=q`. The quotient inequality gives

\[
2^j(t-1)\le r,
\qquad (q+2)(t-1)\le(d+1)(t-1)\le70\,2^q.
\]

For all `q>=0`, `(q+1)(q+2)<=3*2^q`. If `t<=q+2`, this directly bounds
`(q+1)t` by `70*2^q`. If `t>=q+2`, then
`(q+1)t<=(q+2)(t-1)`, and the displayed budget gives the same result.

`marked_odd_ceil_prefix` formalizes this all-depth statement;
`marked_upper_half_of_one_mod_four` records the immediate odd half-ceiling
case. Thus a prospective successful selector may use odd prefixes rounded
in either direction. The new result proves section membership, with an
actual ordinary merger still required before transferring convergence.
For `n>1`, both odd rounded prefixes at a positive depth are strictly
smaller: the upper choice is at most `(n+1)/2<n`. Thus the enlarged class
supports exactly the same marked strong-induction argument whenever
actual mergers cover every marked input.

In particular, every marked `n>1` has a canonical smaller marked candidate

\[
U(n)=2\lfloor n/4\rfloor+1.
\]

This is the lower half when `n=3 mod4` and the upper half when `n=1 mod4`.
The section is therefore closed under the entire ordinary decreasing
binary-prefix tree generated by `U`. A proof that each marked `n` actually
merges with `U(n)` would close Collatz by this tree. The solved rising
phase supplies only some of those edges; the existence of every remaining
ordinary merger edge is not asserted.

## 3. The whole solved rising phase now gives marked component descent

PR180 already proves the following actual word exchange. Write

\[
n=2^k u-1,\qquad k\ge2,\quad u>0,
\qquad 3^{k-1}u\equiv3\pmod4.
\tag{M4}
\]

For `m=2^(k-1)u-1=(n-1)/2`, one has

\[
T^{k+2}(n)=T^{k+1}(m).
\tag{M5}
\]

Indeed, if `3^(k-1)u=4z+3`, the complete rising prefixes land at `12z+8`
and `4z+2`. Both reach `3z+2` after two more shortcut steps. The guard in
`(M4)` is essential.

If `n` is marked, `m` is odd and `(M1)` holds with `j=1,c=1`; therefore
`m` is a **smaller marked** partner. This applies to the entire guarded
rising phase, not only the symbolic subfamilies highlighted in the recent
packets. The transport identity is credited to PR180; the section-preserving
composition is the additional connection here.

The familiar odd inverse lift also fits the same interface. If `m` is odd,
`n=4m+1` has `T^3(n)=T(m)`. Thus a marked `n` with `n mod8=5` has the
smaller marked partner `m=(n-1)/4`. This observation is a written elementary
consequence, separate from the current Lean declarations.

### Why repeatedly applying the solved exchange does not close the theorem

For a maximal rising block, take `u` odd. If `k>=3`, halving the solved
input changes the phase from

\[
3^{k-1}u\equiv3\pmod4
\quad\text{to}\quad
3^{k-2}u\equiv1\pmod4.
\]

So the next application lies in the complementary phase. The merger does
not provide an indefinitely repeatable decreasing rule.

In that complementary phase, `3^(k-1)u=4z+1`, the two arms reach
`12z+2` and `4z`; after two more steps they are `9z+2` and `z`.
PR180's parity bridge proves that the missing transfer is precisely the
original odd-psi query at unchanged rank. Supplying the smaller source's
certificate establishes its antecedent; it does not supply the consequent.
Choosing another dyadic split changes the bookkeeping but has not supplied
a new rank decrease in that query.

## 4. Even the offset-one residual retains the old shifted-power problem

For every `a>=0`, the integer

\[
n_a=2^{2a+2}+1
\]

is marked. Repeatedly applying the exact two-step identity

\[
T^2(2^{2r}v+1)=3\,2^{2r-2}v+1\qquad(r\ge1)
\]

gives

\[
T^{2a+2}(n_a)=3^{a+1}+1,
\qquad T^{2a+3}(n_a)=T(3^a).
\tag{M6}
\]

Hence `Basin(n_a) iff Basin(3^a)`. The first two ordinary steps from `n_a`
already decrease its size, but the endpoint generally leaves the shrinking
marked band. In a marked-only induction that ordinary decrease is not a
certificate of convergence.

There is a sharper limitation of the specific dyadic cover `(M3)`. For
`n=2^d+1`, `d>=1`, its guards force `c<=1`. Since `j>0` and `n` is odd,
the split `n=2^j*x+c` forces `c=1`. Consequently
`x=2^(d-j)`. Oddness of `x` then forces `j=d` and `x=1`.
Thus **the whole offset-one family has no intermediate partner under this
specific nonnegative-offset cover**. On the subfamily `(M6)`, supplying its dyadic-cover witness already
supplies a genuine hit to 1 for the corresponding power of three. This
explains precisely why section compatibility alone does not finish the
selector.

The rounded-up extension just proved does supply intermediate marked
candidates `2^(d-j)+1` for `j<d`. The preceding rigidity therefore does
not exclude a selector using those candidates. What remains absent is an
actual universal merger to one of them; markedness itself is now available.

This connects the most apparently favorable band offsets back to the older
shifted-power residuals in PR146. It does not claim that convergence of all
pure powers of three is itself known to imply full Collatz. The implication
under discussion is the exact basin equivalence `(M6)`.

## 5. A quantitative limit on uniform population-based repairs

The target-independent constant in PR180's marked-population theorem is
valuable, but its target-dependent successful octaves cannot be made uniformly
small merely by combining it with PR176's checked inverse fans.

### A large certified inverse antichain

Take any admissible `Q>=16` in PR176's cofinal sequence and apply its checked
finite fan to target 1. It gives a set `F` of `2^Q` distinct marked odd sources,

\[
2^Q\le x<2^{10Q},\qquad T^{k_x}(x)=1,
\qquad k_x<11Q.
\]

Map `x` to itself if `3` does not divide it, and to `T(x)` otherwise. The
image `Y` consists of ternary units between `2^Q` and `2^(10Q+1)`. The map
has fibers of size at most two: at most one unchanged source and one source
through the injective odd branch. Every image still reaches 1 before `11Q`.
Therefore `|Y|>=2^(Q-1)`.
The image targets may be even; the positive ternary-unit target version
of the population statement is the relevant version here.

Pigeonhole the images by their **first** hit-to-one clock. One clock class
`P` satisfies

\[
|P|\ge\frac{2^Q}{22Q},\qquad
p<2^{10Q+1}\quad(p\in P).
\tag{M7}
\]

No two distinct members of `P` lie on the same forward orbit in comparable
positions: they are above two and have the same first-hit clock. If one
reached another after a positive number of steps, their first-hit clocks
would differ by that number. Consequently their full ordinary predecessor
sets are pairwise disjoint. This uses explicit certified inputs and does
not assume an eternal counterexample or full Collatz convergence.

### Simultaneous marked populations must move to a large octave

Suppose that, for every `p in P`, a common octave `d` contains at least

\[
\gamma\frac{2^d}{(d+1)^2}
\]

distinct marked predecessors of `p`, where `gamma>0`. These sets are disjoint.
The mark inequality permits at most `71*2^d/(d+1)` marked values in that
octave: its interval has length at most `70*2^d/(d+1)`, and
`d+1<=2^d` absorbs the endpoint. Thus

\[
\gamma |P|\le71(d+1).
\]

Combining this with `(M7)` gives the exact restriction

\[
\boxed{d+1\ge\frac{\gamma\,2^Q}{1562Q}.}
\tag{M8}
\]

The allowed targets have binary height at most `10Q+1`, while their common
population octave must sometimes have exponentially larger binary height.
In particular, a uniform common witness octave of order the logarithm of
the largest target is impossible. The cofinal admissible scales already
suffice for that conclusion.

This is a paper deduction from the checked finite fan and elementary disjoint
counting. It does not require PR180's analytic theorem as an axiom: `(M8)`
is a necessary condition whenever such simultaneous populations are supplied.
PR180 asserts arbitrarily large **target-dependent** witness octaves, so it
does not make the disproved uniform assertion.

### Even a uniform horizon needs exponentially large height

The same packing argument does not require all targets to choose the same
octave. Suppose each `p in P` supplies such a population at its own octave
`d_p<=D`. Partition `P` into the sets `P_d` of targets choosing each octave.
For every `d`, disjointness gives `gamma*|P_d|<=71*(d+1)`. Summing yields

\[
\gamma |P|\le\frac{71}{2}(D+1)(D+2),
\qquad
\boxed{(D+1)(D+2)\ge\frac{\gamma\,2^Q}{781Q}.}
\tag{M9}
\]

Thus allowing a different successful octave for each target still cannot
give a uniform horizon proportional to the logarithm of the largest target.
The necessary horizon is at least of order `2^(Q/2)/sqrt(Q)` along these
certified antichains. This conclusion concerns where inverse populations
must be located; it is not a statement about forward stopping times.

[MergerPopulationPacking.lean](lean/MergerPopulationPacking.lean) formalizes
the equal-first-hit antichain, disjointness of its full predecessor sets,
the marked-octave capacity, and both integer and rational population packing.
The rational theorem gives `gamma*|P|<=71*(d+1)` for rational `gamma` from
the supplied common populations. Any positive real constant in the analytic
statement can be replaced by a smaller positive rational constant for this
purpose. Extraction of `(M7)` from PR176's finite fan and the final
substitutions into `(M8)`–`(M9)` remain written deductions, rather than an asserted
formal import of PR176 or PR180.

The obstruction explains why an inverse population cannot automatically be
converted into a small partner for a prescribed source. Moving to an octave
that accommodates all the targets may spend the entire source-height budget.
It also preserves the distinction between a large inverse tree in the known
basin and an upper bound on actual fixed-floor survivors.

## 6. The full attempt and the remaining assertion

The general reserved rebase in PR184 permits
`n=2^h*3^s*v+r` and substitutes another actual inverse history of `T^h(r)`.
For a fixed original `n`, however, its ternary reserve and cheaper-history
clock remain bounded by the binary size of that same `n`. Arbitrarily late
selected inverses or contraction exponents from other packets cannot be
inserted into it without supplying a new short history.

The section-preserving proposition above removes one unnecessary loss: a
dyadic affine partner of the right shape may be comparable in size to `n`
and still support marked induction. It does not produce that partner when
the rising phase is complementary or the source is a shifted-power residual.
The population calculation rules out a tempting uniform-octave shortcut to
that existence problem.

The remaining full-theorem task in this architecture is to choose, for every
marked `n>1`, an actual component merger satisfying `(M1)`–`(M2)`, using the
rounded-up extension, or using another globally sufficient rule. No such
total selector was obtained in this pass. The new formal file retains its
cover as an explicit proposition, not an axiom or an assumed proof.
