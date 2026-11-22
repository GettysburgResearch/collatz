# Physical word erasure and source-preserving transport

**Latest continuation:** the [whole-repository attack](../whole-repo-closure-20261122/README.md)
adds an effective classification of every supplied fixed block cycle schema,
an all-parameter Lean cycle exclusion, ordinary harmonic collision transport,
and a literal-tail carry rule. The original proofs and their replay below
retain their separate source and execution boundaries.

This packet continues [PR184](https://github.com/GettysburgResearch/collatz/pull/184), frozen at `366dab89ee9548084ab9b5e4e90ff82abf287a20`. The map throughout is the ordinary shortcut Collatz map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

**The strongest unconditional result is a smaller marked common-future construction that works even when the original orbit has no descent through its entire binary horizon. Full Collatz is not proved.** A separate global route constructs the original survivor masses explicitly and proves that one precisely stated uniform transport improvement would imply the full theorem. That improvement remains a hypothesis.

All work stays on ordinary positive integers. No `sorry`, `native_decide`, or custom axiom is introduced. The reproducible checker audits every public theorem in the new Lean packet, including every literal certificate chunk.

## 1. The structural step: the marked band survives source deletion

The inherited forced-section theorem says that every positive orbit reaches a marked odd integer. In this repository,

\[
\operatorname{Marked}(n)\iff n\text{ is odd and }(d+1)(n-2^d)\le70\,2^d,
\qquad d=\lfloor\log_2n\rfloor.
\]

Consequently, it is enough to prove convergence for all marked sources. A useful induction certificate is a **smaller marked source with a common ordinary future**. The original orbit itself need not descend in the available window.

[MarkedErasure.lean](lean/MarkedErasure.lean) proves the new connection:

\[
x>0,\quad x\text{ odd},\quad n=2^r(x+1)-1,\quad\operatorname{Marked}(n)
\quad\Longrightarrow\quad\operatorname{Marked}(x).
\]

To see why, put `e=floor(log_2 x)`. Then

\[
\lfloor\log_2n\rfloor=e+r,\qquad
n-2^{e+r}=2^r(x-2^e)+(2^r-1).
\]

The marked inequality for `n`, after discarding the last nonnegative term and cancelling `2^r`, is stronger than the marked inequality for `x`.

This removes the height condition required when an arbitrary smaller partner must subsequently be forced back into the marked section. For this particular deletion construction, the partner is already marked.

### Turning an endpoint identity into a smaller marked source

[HalfSourceMerge.lean](lean/HalfSourceMerge.lean) proves the general lifting rule. Write

\[
n=2^ku-1,\quad x=2^{k-r}u-1,\quad v=3^{k-r}u,
\qquad0<r<k,\quad u>0.
\]

The initial odd runs have endpoints `3^k u-1` and `3^(k-r)u-1`. Thus any exact endpoint diamond

\[
T^h(v-1)=T^h(3^rv-1)
\]

gives

\[
T^{k-r+h}(x)=T^{k+h}(n),\qquad 2^r(x+1)=n+1,\qquad0<x<n.
\]

If `n` is marked, the preservation theorem makes `x` marked too. The source `n` is fixed throughout this argument.

A two-clock diamond applies when `v=3 mod 4`. A longer identity is

\[
T^8(256a+184)=T^8(768a+554)=27a+20\qquad(a\ge0).
\]

Combining short, long, and short diamonds gives, for `v=147 mod 256`,

\[
T^8(v-1)=T^8(3v-1)=T^8(9v-1)=T^8(27v-1).
\]

[LongDiamondErasure.lean](lean/LongDiamondErasure.lean) turns these into quarter-source and eighth-source partners. These are universal identities on the displayed progressions, not finite trajectory samples. The half-source specialization overlaps the phase mechanism already present in PR180; no priority claim is made for that special case.

## 2. A complete infinite family crossing the binary-horizon obstruction

For every `j>=0`, define

\[
k=64j+31,\qquad s=2j+8,\qquad d=k+s=66j+39,
\]

\[
n_j=2^d+2^k-1,\qquad x_j=\frac{n_j-3}{4}.
\]

[NewBandFamily.lean](lean/NewBandFamily.lean) proves simultaneously:

\[
\operatorname{Marked}(n_j),\quad\operatorname{Marked}(x_j),\quad0<x_j<n_j,
\quad\lfloor\log_2n_j\rfloor=d,
\]

\[
T^t(n_j)\ge n_j\quad(0\le t\le d),
\]

and

\[
T^{k+6}(x_j)=T^{k+8}(n_j),\qquad k+8\le d.
\]

So an orbit that only stays level or rises during its native binary horizon nevertheless shares a future with a marked source nearly four times smaller, by the end of that horizon. Both exponents `k,d` are odd, extending beyond the even-run and immediate smaller-predecessor branches used for the previous two-power family.

For `j=0`:

\[
n_0=551\,903\,297\,535,\qquad x_0=137\,975\,824\,383,
\]

\[
T^{39}(n_0)=T^{37}(x_0)=5\,580\,775\,646\,893\,631.
\]

The phase calculation uses `3^64=1 mod 256`, `3^29=147 mod 256`, and `2^s+1=1 mod 256`. Non-descent follows from `k>=2s`: the initial rise has `3^k>=2^(k+s)`, enough to pay for every possible halving during the remaining `s` clocks. The [complete written proof](NEW_BAND_FAMILY_PROOF.md) includes all inequalities and the marked-preservation argument.

**Exact consequence:** no member of this family can be the least marked counterexample. This does not independently prove convergence of the entire family: its partner need not belong to the same parameterized family, so induction only on `j` would be invalid. A complete smaller-partner cover is still needed. Moreover, the
[failed-strengthening note](SYNCHRONOUS_ERASURE_LIMIT.md) shows that pure
synchronous erasure alone is not a universal selector: marked source 7
already has opposite endpoint cycle phases for its admissible deletions.
Fixed unequal-clock identities on those same affine arms cannot cover an
infinite progression; their slopes force equal clocks. A complete policy
therefore needs additional partner formulas or genuinely variable-depth
ordinary arguments.

## 3. Physical coverage on the Applegate–Lagarias `27 mod 128` branch

The literature-guided search produces 446 infinite arithmetic rays among the 576 classes

\[
n=n_0+73728z,\qquad n_0\equiv27\pmod{128},\qquad z\ge0.
\]

Every successful row supplies `x=x_0+Sz`, with `0<x<n`, and an exact meeting identity

\[
T^{13}(n)=T^t(x),\qquad t\le16.
\]

[RayCertificates.lean](lean/RayCertificates.lean) proves the generic infinite-ray soundness theorem using the actual affine orbit-shift lemma. [AL27Certificates.lean](lean/AL27Certificates.lean) checks all 446 literal rows with kernel `decide`, proves distinct source residues, and instantiates the infinite-ray and strong-induction consequences. The source data are split into small chunks to keep kernel checking within memory limits.

| Classification within the 576 classes | Count |
|---|---:|
| Certified smaller-source common future | 446 |
| Unresolved by this certificate | 130 |
| Elementary smaller-predecessor baseline | 192 |
| Direct descent through clock 13 baseline | 207 |
| Union of those two baselines | 330 |
| Certified classes outside that union | 116 |

The 116 figure compares exactly those two tests; it is not a novelty claim against every earlier repository method. The 130 unresolved classes are explicitly listed in the [JSON certificate](certificates/al27_certificate.json). They are unresolved cases, not counterexamples.

One successful ray outside the two baseline tests is

\[
n=283+73728z,\qquad x=239+62208z,\qquad T^{13}(n)=T^8(x).
\]

A [separate Python verifier](certificates/verify_al27.py) checks the entire residue partition, parity words, affine constants, slopes, strict source inequalities, and baseline counts. [The generator](certificates/generate_al27_lean.py) checks that the Lean literals exactly match the JSON. The proof scope is infinite rays; the remaining coverage is incomplete.

## 4. A concrete global analytic target with original source atoms

The second route pursues the universal step using finite mass, motivated by the non-singular transformation literature. It never replaces the original source distribution at a return endpoint.

Let `R` be the actual complete marked-return map. Fix the explicit positive seed

\[
a(n)=c_n=\frac1{(n+1)(n+2)},\qquad\sum_{n\ge0}a(n)=1.
\]

[ExplicitSeed.lean](lean/ExplicitSeed.lean) proves the finite-mass bound by telescoping. [ActualSurvivorMass.lean](lean/ActualSurvivorMass.lean) defines

\[
b_k(y)=\sum_{\substack{n\text{ marked}\\R^kn=y\\R^jn\ne1\ (0\le j\le k)}}a(n).
\]

Formally this is the supremum of finite source sums. In particular, if one original source `n` survives through depth `k`, then

\[
a(n)\le b_k(R^kn),\qquad0\le b_j(y)\le1.
\]

For each fixed endpoint `y`, define the finite budget

\[
B_k(y)=\sum_{j=0}^{k}c_j2^{j-k}b_j(y),\qquad D_k=(k+1)(k+2).
\]

The earlier-depth terms use the same endpoint `y`; they are not measurements along a moving trajectory. [FiniteResolvent.lean](lean/FiniteResolvent.lean) proves

\[
B_k(y)\le\frac8{D_k}.
\]

The depth-`k` term alone gives the unconditional baseline

\[
\frac12b_k(y)\le\frac{D_k}{2}B_k(y).
\]

The precise unproved completion estimate is

\[
\boxed{\quad
\forall\varepsilon>0\;\exists k\;\forall y:\quad
\frac12b_k(y)\le\varepsilon D_kB_k(y).
\quad}
\]

[ExplicitClosure.lean](lean/ExplicitClosure.lean) proves that this estimate implies **full Collatz**, including exclusion of nontrivial cycles. Indeed, a surviving original source forces

\[
a(n)\le b_k(R^kn)\le16\varepsilon.
\]

Choose `epsilon=a(n)/32`; that is a contradiction. The same source retains its positive atom at every depth, regardless of what other sources enter its endpoint fiber.

This reduces the analytic route to an explicit uniform improvement of a bound that is already proved. It does **not** prove that improvement. A single fixed-factor saving is insufficient; arbitrarily small factors are required. Furthermore, a terminating decrement map can still have quadratic transport norms for this type of fixed seed, so the sufficient estimate is stronger than termination in general. The [transport note](HARMONIC_TRANSPORT.md) proves the exact operator interpretation, records this countermodel, and separates written infinite-sum arguments from the checked finite kernel.

[HarmonicTransport.lean](lean/HarmonicTransport.lean), [ClockAbsorption.lean](lean/ClockAbsorption.lean), and [BandAbsorption.lean](lean/BandAbsorption.lean) also prove the more general reciprocal-budget closing route. The clock lift distinguishes repeated visits even on a possible cycle. These implications keep their transport bounds explicit as hypotheses.

## 5. How the literature informed the construction

The [source manifest](source-pins.json) pins primary sources and refreshed repository heads.

- **Applegate–Lagarias, The 3x+1 Semigroup:** their weak Collatz theorem permits extra multiplication operations. To retain ordinary dynamics, [PullbackArithmetic.lean](lean/PullbackArithmetic.lean) proves the exact coprime correction criterion. If a legal prefix is `2^h T^h(n)=3^p n+B`, a multiplier `m` pulls back integrally through that same prefix precisely when `3^p` divides `m-1`. For multiplier 13, one odd step permits the correction `13n+4`; a particular two-odd-step prefix would require `9c=60`, which has no integral solution. This suggested looking for actual path diamonds instead of treating semigroup multiplication as an orbit edge.
- **Yolcu–Aaronson–Heule, An Automated Approach to the Collatz Conjecture:** mixed binary/ternary rewriting motivates explicit word identities and termination certificates. Their termination formulation is not an imported termination proof. Our diamonds are checked directly in the ordinary map.
- **Assani, Collatz map as a non-singular transformation:** the finite full-support perspective motivates preserving positive source atoms. The finite budget and clock-lift implications here are proved independently. A specific counting-measure limit claim that is not needed is qualified in the transport note.
- **Dubickas, On integer sequences generated by linear maps:** the parity-complexity theorem imposes a lower bound on a divergent language. It does not force the repetitions or upper-complexity estimate that would close a symbolic proof. We therefore use explicit realized words without assuming that an arbitrary admissible infinite word has the needed rationality or recurrence.

The [lifting note](LITERATURE_LIFTING.md) gives the detailed arithmetic and source distinctions. No GRH assumption is used.

## 6. Relation to the latest repository work

The packet starts from PR184's exact published head and uses its frozen PR173 forced-section inputs. PR146 was refreshed at `f431078244e868dc699fad011044f0d5e7f76437`, including its growing-interval and terminal-five comparisons. Its universal closure obligation remains explicit.

PR175's return-rank obstructions help explain the choice of a smaller component representative. PR178's phase results do not supply integer descent.

A follow-up refresh during this attack found PR176 at `486b0421f34f332645c46a723033eda480718d69` and PR180 at `d0349de2108abb7c8fb8393c086610e3372df116`. The latter now contains a written uniform predecessor lower bound `cX/a` for every `X>=Ca` and each positive ternary-unit target, with sources optionally restricted to odd units. It also constructs a canonical least excessive majorant and proves sublinearity throughout the ancestor basin of each fixed target. Its global marked upper estimate still permits moving targets and remains unproved; the fixed-basin result does not supply that uniformity. The parallel analytic attack uses this stronger update rather than only the older cofinal-octave statement. These analytic inputs remain source-qualified written proofs, not imported Lean axioms. None of the neighboring results is treated as complete coverage.

## 7. Parallel continuation: three further attacks

The subsequent pass kept three distinct attacks active and incorporated PR180's stronger published analytic checkpoint.

### Physical completion with unbounded clocks

Starting the erasure after three steps instead of seven reduces the prefix expansion from729/128 to9/8. [AL27HalfSelector.lean](lean/AL27HalfSelector.lean) now supplies a complete parameterized selector on **half of the entire27mod128 branch**:

\[
x=(9n-3)/16,\qquad T^{k+5}x=T^{k+9}n,
\qquad T^i n\ge n\quad(i\le k+9).
\]

Every k>=0 is permitted, with an explicit CRT source progression. This is an ordinary smaller-source merger before any direct source descent has occurred. [The half-branch proof](AL27_HALF_ROUTE.md) gives the selector and exact overlap: together with the earlier446 complete cells, the certified source set has relative natural density451/576 in this branch. There are120 previously unresolved cells untouched by these two constructions and10 now half covered. This is certificate coverage, not a convergence-density theorem.

[ResidualPrefixErasure.lean](lean/ResidualPrefixErasure.lean) proves the general expanding-prefix transfer and its explicit slope/carry conditions. [ResidualPhaseSelector.lean](lean/ResidualPhaseSelector.lean) retains a narrower family inside34587mod73728 with the stronger relation

\[
64x+51=9n,\qquad T^{k+9}x=T^{k+15}n.
\]

For k>=8 its original source never descends through the entire meeting clock. The example n=51791643 has x=7283199 and common endpoint88590800 at source clock23 and partner clock17. This narrower family is contained in the broad half; its density is not additional coverage. [The detailed route](RESIDUAL_PREFIX_ROUTE.md) distinguishes all guards and proof levels.

### A genuine global analytic gain

The [canonical-capacity proof](CANONICAL_FINITE_SPINE_CONCENTRATION.md), a **written source-qualified consequence** of PR180 at `d0349de2108abb7c8fb8393c086610e3372df116`, proves more than separate bounds on fixed basins. For its canonical inverse envelope V and population constant c, on nonperiodic odd units:

\[
\sum_{q\in A}\frac{V(q)}q\le\frac1c
\quad\text{for every finite reachability antichain }A,
\]

\[
\sum_q\frac{V(q)}{q^2}\le\frac{64}{3c^2}.
\]

At every positive normalized threshold, the high-value states lie on finitely many actual forward trajectories. A weighted interval slicing proof turns the antichain and reciprocal-chain budgets into the displayed summability theorem. It constructs an actual finite positive canonical weight on all nonperiodic unit states.

The same note constructs a positive ordinary harmonic flow nu with a global pointwise bound and finite sum(nu(q)/q). It does not prove finite **unweighted** mass for nu. A single escaping trajectory can still carry positive flow while having summable reciprocal heights. Periodic target nodes are explicitly outside these stopping-line arguments. These analytic conclusions are not advertised as Lean theorems or as a proof of the missing uniform survivor improvement.

### What a complete rewrite architecture must allow

The [fixed-clock no-cover theorem](FIXED_AFFINE_MARKED_COVER_LIMIT.md) proves that no finite collection of fixed affine maps with fixed meeting clocks can provide smaller marked partners for every large marked source. Shrinking marked width forces dyadic slopes; the unbounded initial odd runs of our proved family then make the affine odd-count equations incompatible with strict decrease. This is a written proof, with precisely scoped hypotheses. It leaves unbounded clocks and non-marked intermediate rewrites available.

A [signed-seed template](SIGNED_SEED_AFFINE_TEMPLATE.md) also derives genuine positive-source identities from finite negative trajectories. Its exact example is independently replayed as an affine identity. It already has direct descent, so it is retained as a route experiment, not promoted as an additional difficult-source exclusion. No full termination proof emerged from this third attack.

## 8. Reproduction and claim scope

With Lean 4.34.1 and a built Mathlib checkout at `d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
python -X utf8 -B research/literature-orbit-closure-20261121/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib \
  --build-dir /absolute/path/outside/the/checkout
```

The checker imports the documented PR184 module-format port for the three frozen upstream sources and uses the unchanged modern `OffsetDescent` module. It records the original and generated hashes, compiles the new packet, checks all 140 public theorem axiom sets, and replays the arithmetic certificate, exact JSON-to-Lean regeneration, finite endpoint-phase census, half-selector overlap, and signed-seed affine identities. Only the standard axioms `propext`, `Classical.choice`, and `Quot.sound` are allowed. It performs no downloads and writes no generated files into the checkout.

Repository integrity is a separate gate:

```sh
python -X utf8 -B tools/validate.py
```

Receipts and independent source reviews live in [the report directory](../../reports/literature-orbit-closure-20261121/). The mathematical frontier is a complete physical partner selection or the displayed uniform survivor-fiber improvement. Neither is inferred from the successful partial cover.
