# Collatz frontier audit and new deductions — 24 November 2026

**Collatz remains open.** This packet records a fresh six-agent GPT-6.2 Astra investigation of the repository's current research frontier. It contains new written deductions, independent proof reviews, ten compiled Lean modules, and exact finite controls. It does not promote a conditional closure interface, a family of changing sources, or a finite census to a proof for every positive integer.

The base is main commit `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Twenty relevant PR heads were initially frozen in [frontier-pins.json](../../reports/astra-frontier-20261124/frontier-pins.json). A final refresh caught PR192–196, a substantive update to PR188, and an attribution correction in PR189; [late-frontier-pins.json](../../reports/astra-frontier-20261124/late-frontier-pins.json) freezes those incoming heads. The claim-specific reviews identify the bodies and arguments actually reconstructed; the inventories are not blanket mathematical certifications of every branch file.

## Results and evidence

| Claim | Result | Evidence and limit |
|---|---|---|
| AF-1 | Every infinite binary word fixed by a nonidentity binary substitution, coded into finite physical gap or parity blocks with infinite output, has a rational 2-adic completion exactly when the output is eventually periodic; otherwise its completion is transcendental. | **PROPOSED, independently verified written proof.** The main non-erasing gap-block extension also appears in incoming PR194 ABR-4. This packet gives an alternate fixed-letter proof, explicit raw-parity/erasing scope and empty codewords with infinite total output, and the additional formal regularity result AF-2. The analytic transcendence argument is not formalized here. |
| AF-2 | For nonempty binary image words at every physical monomial iterate, the Mahler determinant vanishes exactly when the words commute. Nonperiodicity of an actual fixed word therefore forces every determinant to be nonzero. | **VERIFIED in Lean**, including unequal lengths and proper prefixes. This is the finite regularity interface used by the written argument. |
| AF-3 | Any prescribed finite list of positive gap exponents for the accelerated odd map and any source class modulo a power of three occur in infinitely many ordinary predecessors that reach a prescribed positive odd ternary-unit target after one additional step. | **PROPOSED, independently verified written proof.** All positive representatives of one explicit exponent class work. Lean checks the exact gap for a supplied edge and the explicit gap-one family. General gluing and the exponent progression are written. Sources vary. |
| AF-4 | Within a fixed eligible target basin, every fixed gap/ternary cylinder, and every fixed odd dyadic/ternary residue class, has the basin's same lower and upper logarithmic counting exponents. | **PROPOSED written proof**, with an explicit bounded-multiplicity map and constant-factor comparison of counting functions. The cutoff constant depends on the fixed cylinder. |
| AF-5 | For every length and ternary precision, there is an explicit positive ordinary path with that many increasing gap-one steps, entirely in the residue minus one, followed by a step to one. | **VERIFIED in Lean** for the all-parameter divisibility and literal path equations; collision and canonical-scalar interpretations are written deductions. This exhibits arbitrary finite concentration in convergent trajectories. |
| AF-6 | An equal-length dictionary of K contracting parity words supports at most K squared blocks in a positive ordinary shortcut cycle's primitive block period. | **VERIFIED in Lean** for actual shortcut iterates. The elementary proof does not use the source-qualified logarithmic-form bound in PR177. |
| AF-7 | The first coefficient crossing from the minimum of a nontrivial cycle has at least 47,468 odd inputs and 75,235 shortcut steps. With Barina's published cutoff as an external input, these become 72,057,431,991 and 114,208,327,604. | **Written reduction plus specified finite computations.** Lean checks the local affine, envelope, logarithmic and Farey implications. Python checks exact numerical certificates. The local C++ census ran; Barina's computation was not replayed. |
| AF-8 | If a smaller source x merges into the end of an initial b-odd-step segment from n, its competing arm needs more than b plus v3(n) odd inputs. When v3(n) is positive it also needs more than v3(n) log2(3/2) even inputs. | **PROPOSED written proof.** The odd-count inequality independently appears in incoming PR193 S2 and is credited there. This packet adds the explicit even-input bound and exact-first-descent families, with written review and finite controls replaying both ordinary arms. |
| AF-9 | The current empirical and stationary collision estimates point in the same direction and are compatible. | **VERIFIED written audit with the stated source hypotheses.** PR180 first established the stationary collision-gap conclusion rederived by PR189. The missing opposing ordinary collision estimate remains open. |

### 1. Binary substitutions: a complete two-letter classification

[REDUCIBLE_SUBSTITUTIONS.md](REDUCIBLE_SUBSTITUTIONS.md) supplies the new cases. After the primitive case, an aperiodic fixed binary word must have, up to relabeling, a presentation

\[
\sigma(0)=v,\quad |v|_0=a\ge2,\quad |v|_1=b>0,
\qquad \sigma(1)=1^d,\ d\ge1.
\]

If k_i counts ones preceding zero i and h_t counts ones preceding zero t in v, then k_(ai+t)=bi+dk_i+h_t. The zero-indexed series therefore satisfies

\[
V(X,Y)=\left(\sum_{t<a}X^tY^{h_t}\right)V(X^aY^b,Y^d).
\]

Three arguments cover the growth regimes. When d>a, the explicit triangular matrix powers supply the positive weighted direction used in PR190. When a>d>=2 or a=d>=2, the Y parameter has negligible height relative to the X valuation; an auxiliary polynomial constructed over Q(Y) then gives the height-versus-order contradiction. When d=1, digit multiplicativity turns any polynomial recurrence into a constant recurrence, and the functional equation forces a periodic word. Erasing substitutions, empty output blocks, shared fixed points, and cuts inside output blocks are dealt with separately.

The full proof depends on PR190's specified written lemmas. Both those dependencies and the extension were independently reconstructed: [PR190 audit](../../reports/astra-frontier-20261124/PR190_AUDIT.md), [independent review](../../reports/astra-frontier-20261124/INDEPENDENT_REVIEW.md). The final intake also independently verified PR194's overlapping extension, including its different fixed-letter proof; see [PR194 review](../../reports/astra-frontier-20261124/PR194_REVIEW.md). No priority claim is made for that common theorem. The identity substitution is excluded because it fixes every binary word. A binary coding of a substitution on a larger alphabet need not have a presentation covered here. No theorem in the packet assigns such a presentation to every exceptional ordinary Collatz itinerary.

### 2. Ordinary predecessors, fixed basins and concentrated finite paths

[BRIDGE_AUDIT.md](BRIDGE_AUDIT.md) proves the finite gluing theorem with the full carry. For a prescribed gap word of length n, total gap A and carry C, a source reaching the chosen target t after one further gap r is

\[
x=\frac{2^{A+r}t-2^A-3C}{3^{n+1}}.
\]

One congruence modulo 3^(n+m+1) enforces both every intermediate integral inverse and x=u modulo 3^m. Since 2 generates the unit group of each power of three, the allowed r form one class of period P=2*3^(n+m). Backward positivity and oddness make every positive representative legal.

[QUANTITATIVE_GLUING.md](QUANTITATIVE_GLUING.md) makes this uniform in the terminal target: the least representative defines an injective map L(z) into the cylinder with L(z)<=Kz, where K=2^(A+P)/3^(n+1). A simple map of multiplicity at most two removes ternary nonunits. Thus, for an eligible fixed basin B and fixed cylinder C,

\[
N_{B\cap C}(X)\le N_B(X)\le2N_{B\cap C}(5KX).
\]

This preserves both logarithmic counting exponents. It is a theorem about many predecessors in one fixed basin. It gives no lower collision dimension for the time averages of one fixed forward orbit. The explicit family in `ExplicitConcentration.lean` shows why: arbitrarily long prefixes can have collision exactly one at any prescribed finite precision and then reach one. Their sources change with the length and precision.

### 3. Cycle structure and the minimum's first crossing

[CYCLE_CLOSURE.md](CYCLE_CLOSURE.md) proves that a cyclic rotation admits a one-lap partition into first coefficient-crossing words. Such a word has multiplier 3^p/2^A below one, while every proper prefix has multiplier at least one. Its last step is even, so A=floor(log2(3^p))+1. The exact carry envelope is

\[
E_0=0,\qquad E_{p+1}=3E_p+2^{\lfloor\log_2(3^p)\rfloor}.
\]

At the cycle minimum x, the first crossing exists within one lap and ends at least at x. Hence

\[
x\le\left\lfloor\frac{E_p}{2^A-3^p}\right\rfloor,
\qquad 3x(2^A-3^p)\le p3^p.
\]

The exact maximum floor for p<=47,467 is 206,178,386. An overflow-guarded C++ census checked strict descent from every start 2 through that cutoff, and induction supplies convergence throughout the interval. Therefore the first crossing from a nontrivial cycle's minimum must contain at least 47,468 odd inputs. This computation is separate from the Lean proof.

[MINIMUM_ARC.md](MINIMUM_ARC.md) gives a much larger source-qualified consequence. At x>=2^71, the local inequality puts A/p in the strict interval

\[
\log_2 3 < A/p < \log_2 3+\frac1{3\cdot2^{71}\log 2}.
\]

An exact rational logarithm enclosure places it strictly between the Farey neighbors 103768467013/65470613321 and 10439860591/6586818670. The determinant-one identity forces p>=72,057,431,991 and A>=114,208,327,604, even when A/p is not reduced. Applying this to every nontrivial cycle uses [Barina's published verification below 2^71](https://doi.org/10.1007/s11227-025-07337-0). That external computation was not replayed. His paper separately reports the larger bound 355,504,839,929 for the entire cycle; no period record or historical priority is claimed here.

For a dictionary of K arbitrary contracting words of one length A, the elementary center bound is below 3^A. Two boundaries sharing two successive dictionary words differ by a multiple of 4^A, so they coincide. This proves the K-squared primitive block-period bound directly. Neither argument supplies an upper bound on the first-crossing lengths of every possible cycle.

### 4. The cost of a smaller-source merger

[GLOBAL_CLOSURE_ATTEMPT.md](GLOBAL_CLOSURE_ATTEMPT.md) retains the original source bound x<n and quantifies over every alternative ordinary history. If 2^b divides n+1 and T^a(x)=T^b(n), then

\[
p_a(x)>b+v_3(n).
\]

The proof subtracts a carefully chosen integral offset from an intermediate source, keeps its full finite parity word, and uses the fact that negative integers stay negative. [EVEN_INPUT_REFINEMENT.md](EVEN_INPUT_REFINEMENT.md) strengthens this when e=v3(n)>=1:

\[
a-p_a(x)>e\log_2(3/2),\qquad a>b+1+e\log_2 3.
\]

For the minimum merger horizon tau(n)=min max(a,b), an explicit arithmetic progression has

\[
H+1\le\tau(n)\le\lceil H\log_2 3\rceil,
\]

and first numerical descent exactly at the upper clock. Its least source is below 2*9^H. Thus a uniform o(log n) merger-clock bound fails even on sources with a supplied strict descent. A separate construction in each fixed eligible basin rules out o(log log n) there. The constants in the basin comparison vary with H; this proof does not turn the latter statement into a fixed-basin log n bound.

## Incoming branches and combined results

[LATE_FRONTIER.md](LATE_FRONTIER.md) compares the newly arrived branches and records the stronger combined merger inequality a>b+2+v3(n) log2(3), for v3(n)>=1, obtained from PR193 S3 and this packet's even-input proof. PR193 S2 already contains both the odd-count obstruction and its representative-below-6^H CRT consequence. PR194 already contains the main binary gap-block rigidity theorem. These overlaps are credited rather than counted as new theorems. The same synthesis shows explicitly why the low canonical phase (2,1) repeated indefinitely meets both the latest growth and edit-distance lower bounds without being known to occur at an escaping ordinary source.

## Where the global proof still stops

| Route | Available conclusion | First missing universal statement |
|---|---|---|
| Substitution rigidity | Nonperiodic outputs in the specified class have transcendental physical sources. | Every possible exceptional ordinary orbit has enough structure to fall under a proved rigidity theorem. |
| Actual scalar and rational phases | Supplied contracting rational phases admit finite classification; finite carry and packing identities are available. | The actual scalar of every ordinary source is triadic, or another argument rules out the remaining low-mean/irrational cases. |
| Empirical collision | The two reviewed estimates give compatible lower collision bounds, with their original source hypotheses. | An opposing upper collision estimate on the actual same-source law, with the simultaneous scale control needed for the claimed conclusion. |
| Cycles and complete denominators | Literal first-crossing gates, finite exclusions, full-denominator packing and norm divisibility. | Exclusion of arbitrarily large surviving first-crossing words or a strict saving for every complete primitive cycle word. |
| Smaller ordinary mergers | Explicit finite families and necessary odd/even resource costs. | For every prescribed source n>1, existence of a smaller positive source whose forward orbit meets the orbit of n. |

The last existence statement would close the induction, but it is not established by a lower bound on its search cost. Excluding nonstandard cycles alone would also leave positive aperiodic divergent trajectories to address.

## Reproduction and review

The [Lean guide](lean/README.md) identifies the precise formal scope and toolchain. [LEAN_RECEIPT.json](../../reports/astra-frontier-20261124/LEAN_RECEIPT.json) records a fresh compilation of all ten final modules with `-j1 -DwarningAsError=true -DautoImplicit=false`. All 90 requested reports, including two private helper reports, use only `propext`, `Classical.choice`, and `Quot.sound`. The sources were compiled into a new temporary directory; no saved local `.olean` was used as a substitute for compiling these files.

The original round-12 phase module at its frozen PR182 head failed to compile because of two nonexistent lemma names and consequent trailing tactics. The portable repair passes. Original PR190 and round-11 files passed their direct checks. The original PR191 legacy import processes were canceled; its portable version with the same theorem statements and proof bodies passed. [FROZEN_SOURCE_AUDIT.json](../../reports/astra-frontier-20261124/FROZEN_SOURCE_AUDIT.json) preserves these distinctions.

Run the six exact Python controls from the repository root:

```sh
python -X utf8 -B research/astra-frontier-20261124/controls/replay.py --receipt /tmp/collatz-astra-controls.json
```

The runner requires zero Python `assert` nodes, checks each source is unchanged during replay, and compares normal and optimized output. [FINITE_CONTROLS.json](../../reports/astra-frontier-20261124/FINITE_CONTROLS.json) records the final replay. The large C++ ordinary census is separately reproducible using the commands in `CYCLE_CLOSURE.md`; its retained [completion log](../../reports/astra-frontier-20261124/ordinary-206178386.log) is not a kernel proof.

Written reviews: [binary substitutions and gluing](../../reports/astra-frontier-20261124/INDEPENDENT_REVIEW.md), [cycles and mergers](../../reports/astra-frontier-20261124/CYCLE_AND_MERGER_REVIEW.md), [minimum arc](../../reports/astra-frontier-20261124/MINIMUM_ARC_REVIEW.md), and [PR191 reconstruction](../../reports/astra-frontier-20261124/TWO_SIDED_REVIEW.md). The integrated merger control replaces the author's optimization-sensitive assertions with explicit raising guards and replays the same cases; the source hash quoted in the historical review identifies the original version.

Repository integrity is a further, separate gate. On a complete clean checkout, run `python -X utf8 -B tools/validate.py --receipt /tmp/collatz-checkout.json`. It checks repository structure and frozen integration identities. It does not establish mathematical truth or compile the research Lean files.
