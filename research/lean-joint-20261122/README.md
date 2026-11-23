# Joint source induction, an intrinsic inverse horizon, and contact layers

**Full Collatz remains OPEN.** This research checkpoint starts from PR180
at `cfe70e02f246119a55fb5bf8fd573f148d746beb`. It connects the newly
advanced source-induction, finite-potential, and ordinary-boundary work
instead of extending one program in isolation. The
[source snapshot](SOURCE_SNAPSHOT.json) inventories all 122 open and 23
closed PRs and pins the seven branches advanced since the previous
checkpoint. That inventory is not a claim to have re-proved every branch.

The principal new results are an induction that can use a larger supplied
source at equal grade, an exactly calibrated inverse horizon with no
unknown finite-estimate constant, and a finite reference that controls
the entire original source law after **every** forward clock followed by
actual inverse contact. Their closing obligations remain explicit.

## 1. Complete source certificates can be shortened or reordered

The closures below are proved dispatcher steps under explicitly stated
lower-grade, equal-grade larger-source, and smaller-target induction
permissions. The full dispatcher is still an open obligation; none of
these permissions is installed as a new axiom.

PR177 reduced its normalized psi frontier to initial exponent two and
first odd gap three. Write

\[
S=4q,\qquad3q+1=8u,\qquad n=8q-1,
\]

where the known source has a supplied complete certificate beginning in
three. PR176's joint source/target induction permits smaller targets at
that **same original source**. Applying PR175's rising-run diamond at the
correct target gives an all-parameter split. Factor

\[
9u-1=2^t w,\qquad t\ge1,\quad w>0\text{ odd}.
\]

If `3^t w=1 mod4`, the target merges with the strictly smaller partner
`p=18u-3` at the exact shortcut clocks

\[
T^{t+8}(n)=T^{t+3}(p).
\]

The unchanged-source smaller-target hypothesis closes this phase with
every supplied tail. The failed phase has an exact ordinary reduction

\[
c=(3^{t+1}w-1)/4,\qquad
T^{t+7}(n)=6c+1,\qquad T^{t+3}(p)=c.
\]

Its entire arithmetic domain is classified by 18 residue classes of `t`
and a linear cofactor parameter. This first classification alone does
not prove the required reverse implication from `c` to `6c+1`.

### Interior deletion eliminates unbounded portions of the failed phase

An interior segment can be removed when it ends at a larger compatible
odd source. The literal supplied suffix and initial exponent are retained,
the complete grade decreases, and the known source becomes larger. Thus
its known interval includes the old interval. This is an interval rule,
not merely a merger at one numerical target.

In particular, prefixes `[3,1]` and `[3,2,1]` can be shortened to `[3]`
with their respective literal tails. The first disposes of `t=1`; the
second disposes of **every `t>=4`**. Before further tail surgery the only
failed-phase possibilities are the two affine families

| Valuation | `q` | `u` | `c` |
|---|---|---|---|
| `t=2` | `128j+13` | `48j+5` | `729j+74` |
| `t=3` | `256j+173` | `96j+65` | `2187j+1478` |

When all supplied gaps are at most four, the first has `j` even and
prefix `[3,4]`, while the second has prefix `[3,2,2]`. These are
constrained complete-source instances, not a theorem about every free
integer `c` in an affine progression.

### A finite source tie permits equal-grade improvements

The next rewrite preserves the entire grade. At a common suffix endpoint
`z`, prefixes `[3,4,2]` and `[2,3,4]` have equal length and equal exponent
sum, with affine corrections 161 and 53. Therefore

\[
3^3q=2^9z-161
\quad\Longrightarrow\quad
3^3(q+4)=2^9z-53.
\]

The replacement is an actual ordinary certificate with the same literal
tail and a larger supplied source. This cannot use a strictly-smaller-grade
hypothesis alone. A new finite tie resolves that issue: a complete source
of grade multiset `g` is at most `2^(sum g)`. At equal grade, increasing
the source strictly decreases the natural number

\[
\operatorname{defect}(g,S)=2^{\sum g}-S.
\]

This gives a well-founded source tie before the ordinary target tie. It
does not assume unrestricted induction over ever-larger sources. The
other new tail surgery, `[3,4,1]`, replaces the initial exponent two by
three and the odd prefix by `[3,3]`, while keeping the same suffix. It
deletes grade eight, so the new grade seven is allowed by strict grade
descent.

These rules exhaust the entire low-gap `t=2` family. Its even parameter
splits as follows: positive `j=0 mod8` forces `[3,4,2]`; `j=2 mod4`
forces `[3,4,1]`; and `j=4 mod8`, written `j=8h+4`, has the exact
ordinary descent

\[
\boxed{T^{13}(8192h+4199)=6561h+3364<8192h+4199.}
\]

The terminal case `j=0` has target 103 and is checked directly. Thus
the remaining low-gap head-three frontier is confined to

\[
\boxed{q=256j+173,\quad u=96j+65,\quad c=2187j+1478,}
\]

with the actual supplied prefix `[3,2,2]` and its complete suffix.

There is also a proved **written** unbounded rewrite within this remaining
program: for every `k>=1`,

\[
[3]\mathbin{+\!+}[2]^k\mathbin{+\!+}[4,1]
\quad\longmapsto\quad
[2,4]\mathbin{+\!+}[2]^{k-1}\mathbin{+\!+}[1,3].
\]

It preserves the multiset, increases the odd source from `q` to `q+4`,
and retains the literal suffix. The constructive proof carries each old
gap-two state `v` to `(v+1)/2`; parity follows backward from the gap-four
exit. This whole variable-length rewrite is not claimed as an additional
Lean theorem in the present checkpoint.

Further complete written deductions remove `j=3 mod4` by interior
deletion and all `j=0 mod16` by the permutation or an exact 16-step
descent. The low-gap premise excludes `j=8 mod16`. Thus the written
frontier is narrower still: `j=1 mod4`, `j=2 mod4`, or `j=4 mod8`,
always with the original supplied complete certificate.

The [mixed-cover proof](MIXED_COVER.md) states the exact induction premises,
clocks, interval inclusions, arithmetic classification and remaining
families. [MixedCoverAttack.lean](lean/MixedCoverAttack.lean) formalizes
the finite core. A complete successful dispatch for every residual
supplied word, and the general interval-cover obligation, remain open.

## 2. One exact finite error determines a superpolynomial horizon

For the actual ordinary inverse operator

\[
Pf(q)=\sum_{\substack{e\ge1\\2^e q=1\ (3)}}
\frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right),\qquad D_s=P^s1,
\]

define the finite rational error

\[
\epsilon_m=3^{-2m}\sum_{a\bmod3^{2m}}
|D_{2m}(a)-D_m(a\bmod3^m)|.
\]

The density arrays are computed exactly by grouping the **entire**
valuation series with period `2*3^r`; there is no discarded exponent tail.
If every actual unit predecessor of `q` through depth `K` is at least
`b>=9^m`, the explicit ordinary counting argument gives

\[
\boxed{
\max_{s\le K}\frac{D_s(q)}q
\le\frac{4^m}{b}+\frac{K(5K+4)}m\epsilon_m.}
\]

This finite bound has no unspecified mixing constant. Its calibrated
horizon is computed by exact rational comparisons.

An actual all-gap-one cylinder ending at `2*3^(2m)-1` supplies the new
strict lower bound

\[
\epsilon_m\ge2\bigl(4^{-m}-(2/9)^m\bigr)
\ge\frac29\,4^{-m}>0.
\]

Consequently the intrinsic maximum

\[
H_m^*=\max\{H\in\mathbb N:H^4\epsilon_m\le1\}
\]

is finite and computable without a regularizing term. Tao's cited
marginal mixing theorem implies that this **one sequence** eventually
exceeds every fixed polynomial in `m`. The same ordinary cylinder gives
the independent upper budget

\[
H_m^*\le(9/2)^{1/4}2^{m/2}.
\]

For a bounded obstacle `0<=g<=1`, finite positivity gives
`V_k<=sum_(j=0)^k D_j`. Therefore, when `k+1<=H_m^*` and the actual
unit predecessor floor holds through depth `k`,

\[
\boxed{\frac{V_k(q)}q\le
H_m^*\frac{4^m}{b}+\frac9{mH_m^*}.}
\]

This finite obstacle extension needs no population theorem, stationary
normalization, or infinite majorant. A violation at `q>=b` extracts an
actual unit ancestor below `b` at positive depth at most `k`. Both terms
decay faster than every fixed inverse power of `m` at floors `b>=9^m`.
The global gap is still a witness within this calibrated horizon; no
all-depth supremum is exchanged with the finite estimates.

[Finite horizon proof](FINITE_SPIKE_CLOSURE.md) ·
[Ordinary cylinder and intrinsic budget](CYLINDER_BUDGET.md) ·
[Exact finite certificate](finite-density-certificate.json)

## 3. A single finite reference supports all forward/contact clocks

Use the positive odd ternary units that are not themselves periodic,
with actual forward mass transport `L` killed on entering any periodic
state. The upstream ordinary harmonic flow `nu`, floor `h`, finite seed
`d`, and canonical potential retain their explicitly pinned analytic
qualifications. In particular

\[
L\nu=\nu,\quad0<\gamma/q\le h(q)\le\nu(q),\quad
h\ge\delta\nu,\quad Sd=\nu-\lambda h,
\]

where `S=sum_(k>=0)L^k`, `delta=exp(-200/3)` and
`lambda(q)=3q/(3q+1)`. Let contacts mean `V<=2`, and let `ell(q)` count
strict future contacts along the retained ordinary trajectory.

Every such count is finite: a future contact has height at most
`2/(delta*nu(q))`, and retained orbit states are distinct. Layer `j`
contains contacts with exactly `j` future contacts. For
`eta_j=nu 1_(layer j)`, the new exact identity is

\[
\boxed{S\eta_j(q)=\nu(q)\mathbf1_{\ell(q)\le j}.}
\]

Its proof uses actual inverse first contact, forces one inverse step
after a contacted state, and repeats finitely many times. It does not
infer a zero boundary remainder solely from a local difference equation.

Take

\[
c_j=(j+1)^{-1/2}-(j+2)^{-1/2},\qquad
\kappa=3\delta/4,\qquad
\sigma_*=d+\kappa\sum_{j\ge0}c_j\eta_j.
\]

Each layer is an ordinary antichain with the upstream finite mass budget.
The weights sum to one. Thus `sigma_*` is a finite, everywhere-positive
reference, with the exact occupation formula

\[
\boxed{S\sigma_*(q)=\nu(q)-\lambda(q)h(q)
 +\frac{\kappa\nu(q)}{\sqrt{\ell(q)+1}}\le\nu(q).}
\]

Let `Pi` be actual inverse first contact, including time zero at contacts.
Keep the original positive-integer law `n^-4`, project each original
label to its first odd ternary unit, and delete periodic projected states
under the fixed killing convention. Call this source measure `a`, and
let `a_N` keep labels at most `N`. For explicit finite constants `K,M`,

\[
\boxed{\Pi L^k a\le M\sigma_*,\qquad
\Pi L^k(a-a_N)\le2K N^{-1/2}\sigma_*\quad(k\ge0).}
\]

All clocks share the same reference and constants. The proof retains
every original label and every endpoint collision. For all finite `p>=1`,
the omitted-label density energy is at most

\[
\frac{(2K)^{p-1}}3N^{-(p+5)/2}.
\]

The actual densities `(Pi L^k a)/sigma_*` converge strongly in every
finite `Lp(sigma_*)`. Their limit is the complete escaping source mass
distributed over the last contacts of each escaping component according
to its ordinary harmonic capacity. This is a strong limit theorem; its
remaining mass is not proved zero.

The note also proves all-frequency Abel and Cesaro residue formulas for
every occupation-dominated finite source and every finite `p>1`. PR183's
original quadratic residue and PR176's last-contact theorem are credited
as inputs. The broader source class, all finite powers, common-reference
repair, and original-label bounds are the new statements.

[Full ordinary-boundary proof](ORDINARY_BOUNDARY.md) ·
[Arithmetic and quadratic core](lean/OrdinaryBoundary.lean) ·
[Layered scalar core](lean/LayeredContact.lean)

## 4. The reset clock must remain part of any closing argument

The canonical immigration seed alone does not support repeated inverse
contact: at the concrete convergent root 17, the first-contact law has
infinite quadratic density energy relative to `d`, although its input
atom has finite energy. An infinite ordinary unit-parent family proves
this domain failure. The layered reference above repairs that particular
failure for the specified all-clock source family.

It does not identify `Pi L^k` with `(Pi L)^k`. On escaping last contacts,
one reset from `x` to `y` at inverse depth `tau` changes the actual
component clock by

\[
h_C(y)-h_C(x)=1-\tau\le0.
\]

Every ordinary unit target has a noncontact unit parent in the class
`17 mod27`, with two preceding gap-one unit edges. This gives a strictly
positive probability of a strict clock drop. Equal-clock transitions
all retry the same first-contact law, so their holding time is geometric.
Repeated resets drive this integer clock to minus infinity almost surely
and admit no nonzero finite stationary measure on escaping last contacts.

Thus the strong limit of `Pi L^k a` is not a stationary measure for the
repeated-reset chain when escape is present. A closing argument needs
the missing control of actual forward survival or inverse depth; it
cannot reuse the proved domination under an unproved interchange of
these operators.

[Clock proof and precise composition boundary](CONTACT_CLOCK.md) ·
[Finite ordinary arithmetic](lean/ContactClock.lean)

## 5. What is formalized and how to replay it

The Lean files prove finite ordinary trace identities, complete-source
grade and interval rules, exact residue coverage, calibrated scalar
inequalities, and finite collision/energy consequences. The infinite
measure constructions, Tao input, and their analytic deductions remain
written source-qualified proofs. No `sorry`, added axiom, or finite
simulation is used to assert universal convergence.

`THEOREMS.json` is the exact public theorem inventory.
`DEPENDENCIES.json` pins the unchanged project dependencies at the
published parent and the Lean/Mathlib versions. The replay script builds
all project modules afresh in an empty output directory and separately
prints every new public theorem's axioms, rejecting any beyond
`propext`, `Classical.choice`, and `Quot.sound`.

The fresh replay **passed all 65 new public theorems in six modules**, with
warnings treated as errors. It built eight unchanged dependencies, six
new modules, and the independent combined audit: fifteen modules in total.
The exact compiler output, source hashes, and theorem counts are retained
in the linked reports.

```bash
python3 research/lean-joint-20261122/check_lean.py \
  --mathlib /absolute/path/to/pinned/mathlib4 \
  --lean /absolute/path/to/lean \
  --report-dir /absolute/path/to/replay-output

python3 research/lean-joint-20261122/finite_density_certificate.py \
  --max-block 3 \
  --check research/lean-joint-20261122/finite-density-certificate.json
```

The finite certificate covers densities through level six, 364 ternary
coarsening cells, and 120 literal positive odd inverse rows with their
complete geometric tails. It checks both calibrations and the rare-cell
lower bounds. All six calibrated maxima at `m=1,2,3` equal one; the
calculation is an arithmetic interface check, not a useful large cutoff.

Fresh replay receipts and independent claim reviews are in
[`reports/2026-11-22-joint-pass`](../../reports/2026-11-22-joint-pass).
The repository's required complete-checkout validation is separate from
the mathematical evidence.

## 6. Exact global obligations after this pass

The source program needs a complete successful rewrite/merge dispatch
on the remaining supplied words and the general interval cover. The
potential program needs an appropriately early finite critical witness
or another all-time estimate at a fixed ordinary predecessor floor. The
boundary program needs to prove its escaping mass zero while retaining
the actual transport and hitting clocks. Nontrivial cycles also require
their separate complete-denominator exclusion.

These are stated separately because success in one interface is not
automatically a theorem in another. The new source tie, computable
horizon, and common-reference theorem give concrete stronger inputs for
the next attack without changing any of those unresolved quantifiers.
