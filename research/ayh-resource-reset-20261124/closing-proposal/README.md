# Least reverse defects and a Lean closing proposal

**Status: partial theorems and an explicit OPEN closing step. This packet does not prove Collatz.** It closes the entire two-odd-certificate layer of the least reverse defect, narrows a three-odd family to one possible first bad Mersenne exponent, and removes infinite subfamilies of that remaining row by ordinary contraction. The quantitative reverse return is also formalized in full. The complete Lean assembly has only the still-open higher-rank mathematical hypothesis as an argument.

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

Write \(C(n)\) for membership in the basin of 1. A **reverse defect** is a positive \(z\equiv17\pmod{48}\) for which \(C(3z)\) holds and \(C(z)\) fails. The preceding [directed-return packet](../directed-return/README.md) proves in Lean that universal positive convergence is equivalent to the absence of such defects. Thus a counterexample would give a least reverse defect. All descent arguments here use that minimum; they do not assume that every smaller ordinary integer converges.

## 1. The checked closing interface

[FinalProofProposal.lean](FinalProofProposal.lean) defines the following propositions and proves their assembly.

| Name | Exact role | Status |
|---|---|---|
| `QuantitativeReturn` | Every positive nonbasin \(n\) produces a reverse defect \(w\le2^{40}n\). | Unconditional kernel theorem in `QuantitativeReturn.lean`, including the whole finite coverage and numerical height bound. |
| `SourceProgress z` | Either \(C(z)\), or there is a positive \(n\) with \(2^{40}n<z\) and \(C(n)\leftrightarrow C(z)\). | Definition of the needed progress at the supplied ordinary source. |
| `two_odd_layer` | `SourceProgress z` whenever a certificate for \(3z\) uses exactly two odd inputs. | Unconditional kernel theorem. |
| `HigherRankProgress` | The same conclusion for every certificate with at least three odd inputs. | **OPEN. No proof is supplied.** |
| `collatz_from_proposal` | `HigherRankProgress → UniversalConvergence`. | Kernel theorem with the one open hypothesis explicit. |

The first two steps from \(3z\) are forced odd inputs, and its first two values cannot equal 1. Hence every upper certificate belongs to one of the two displayed layers. In the higher-layer consumer, a nonbasin endpoint \(n\) would return to a reverse defect strictly below \(z\), contradicting strong induction. The theorem `collatz_iff_higher_rank` also checks that, the remaining higher-rank proposition has the full strength of Collatz, with no additional external premise. Naming it does not discharge it.

There are no `sorry` declarations, project-specific axioms or assumed proof constants in this assembly. An axiom audit cannot erase explicit theorem hypotheses. The quantitative bound is proved; the higher-rank step is open.

## 2. An entire rank layer is removed

The pinned PR146 comparison certificate has 26 leaves. The greatest product of height majorants along any macro prefix is \(16384/9\). Completed batches strictly decrease their positive starting values. A first transition from nonbasin to basin occurs at a forward tripling source. The ordinary two-successor exchange, the 1-mod-16 to 11-mod-32 directed cover, and the final 17-mod-48 exchange give

\[
\frac{16384}{9}\cdot11\cdot
\frac{574854143371}{219537}\cdot2
=\frac{207205026269790208}{1975833}<2^{40}.
\]

This gives the sharp written height calculation. The new [quantitative kernel proof](QuantitativeReturn.lean) independently checks a coarser sufficient bound: 75 localized subbanks preserve the original affine source and its history, every localized query has both coefficients bounded, and the 26-leaf descent controls every required tripling source. Strong induction on the original ordinary integer gives the same final factor \(2^{40}\). [Certificate construction and replay](QUANTITATIVE_RETURN.md). Only macro vertices, including actual tripling query sources, need the descent height bound.

Now suppose \(3z\) has a certificate with exactly two odd inputs. Its remaining tail consists of halvings, so

\[
27z+5=4\cdot2^e.
\]

Below \(e=201\), the required residue leaves exactly \(e=39,93,147\). The three corresponding lower sources reach 1 in 168, 398 and 677 shortcut steps. For \(e\ge201\), put \(c=2^{e-201}\). Five steps from the original \(z\) reach \(4^{99}c+1\), and 99 odd-even pairs reach

\[
n=3^{99}c+1,\qquad 2^{40}n<z.
\]

The identity and inequality are all-quantified Lean theorems, rather than a numerical sample of the infinite family. If \(z\) were the least reverse defect, the return from its nonbasin endpoint would contradict leastness. Thus the least reverse defect has **at least three odd inputs in every convergence certificate for its triple**.

[Proof](RANK_TWO_DESCENT.md) · [kernel source](TwoOddCertificate.lean) · [independent reconstruction](../../../reports/ayh-resource-reset-20261124/closing-proposal/RANK_TWO_INDEPENDENT_REVIEW.md).

## 3. What happens at three odd inputs

Let \(e\) be the even run between the second and third upper odd inputs, and \(b\) the final even tail. The exact relation is

\[
81z+15+2^{e+2}=2^{e+b+3}.
\]

A written finite-certificate argument restricts a least reverse defect in this layer to **\(6\le e\le48\)**. It checks 156 contracting rational parity prefixes of length at most 343 and all 675 admitted positive small-tail sources, whose maximum first-hit time is 5,619. The rational prefixes certify finite words of actual ordinary sources; they are not substituted for an infinite ordinary orbit. This restriction retains written-proof status.

The first remaining family, at \(e=6\), has

\[
81z+271=2^{162m+18},\qquad T^7z=2^{162m+11}-1.
\]

[MersenneBarrier.lean](MersenneBarrier.lean) proves that the source stays at least \(9z/16\) through the entire displayed upper convergence clock. A known upper certificate therefore does not by itself supply the needed lower contraction. [FiniteHorizon.lean](FiniteHorizon.lean) separately proves that no fixed uniform number of ordinary steps suffices to merge all such source/triple pairs, even with the triple known to converge. Neither result rules out later source-dependent descent or directed comparisons.

### One family reduces to one first bad exponent

For the selected \(e=7\) family, put

\[
a=98+162m,\qquad81z+527=512\cdot2^a,\qquad M_j=2^j-1.
\]

[RankThreeFamily.lean](RankThreeFamily.lean) proves existence in the right residue, the complete three-odd upper certificate, and \(C(z)\leftrightarrow C(M_a)\). If this \(z\) is the least reverse defect, the first bad positive Mersenne exponent must lie between \(a-42\) and \(a\), using the now-proved quantitative return. Forty literal directed paths exclude offsets 3 through 42. They contain 80 forward comparison positions, all strictly smaller than the actual parent \(z\). The ordinary merger of each even-index Mersenne start with its preceding odd-index start removes offsets 0 and 2. Consequently

\[
\boxed{j=a-1=97+162m}
\]

is the only possible first bad exponent in this particular family. This conditional conclusion is kernel-checked in [MersenneFirstBad.lean](MersenneFirstBad.lean), consuming [all 40 paths](MersenneReturnKernel.lean) and [the ordinary even-exponent merger](MersenneParity.lean). It does not classify every three-odd source.

[Third-step restriction](RANK_THREE_RESTRICTION.md) · [Mersenne frontier](MERSENNE_FRONTIER.md).

## 4. A positive contraction on the remaining Mersenne row

The new mechanism uses a smaller reverse query whose lower arm joins the hypothetical bad Mersenne number, while its triple contracts sharply. This only needs the triple's endpoint to be smaller by the quantitative return factor; it need not already have a known explicit convergence certificate.

One complete infinite progression is

\[
j=29419+354294k,\qquad
w=\frac{2^{j+21}-3170149}{177147},\qquad
z=\frac{2^{j+10}-527}{81}.
\]

[OppositeArm.lean](OppositeArm.lean) proves actual positive integer witnesses, both residue conditions, \(w<z\), and

\[
T^{21}w=M_j,\qquad
T^{24}(3w)=2^{j-3}+1,\qquad
T^{224}(3w)<\frac{z}{2^{40}}.
\]

The 100 odd-even pairs after clock 24 give the endpoint \(3^{100}2^{j-203}+1\). For a least reverse defect, any nonbasin value below \(z/2^{40}\) would produce a still smaller reverse defect. Thus the last endpoint must be in the basin. It follows that \(3w\) is in the basin, whereas \(w\) shares the bad Mersenne basin status. This contradicts \(w<z\). The infinite ordinary identities are in Lean; this leastness application is written out in the companion proof.

The broader [literal certificate bank](OppositeArmQueries.json) contains 214 disjoint progressions. On the common modulus \(3^{10}=59049\) for the parameter in \(j=97+162m\), 616 classes have a power-of-two endpoint on the triple and another 384 have the contracting positive endpoint. **Exactly 1,000 classes are excluded; 58,049 remain outside this certificate.** That count does not estimate how close the overall conjecture is to a proof. This is still only one upper-rank-three family.

[Written proof](OPPOSITE_ARM_CONTRACTION.md) · [independent all-row review](../../../reports/ayh-resource-reset-20261124/closing-proposal/OPPOSITE_ARM_REVIEW.md).

## 5. Parallel analytic route and repository reassessment

[Local resampling](LOCAL_RESAMPLING.md) improves the earlier selected-color construction under its same source-qualified native merger and regeneration inputs P and R. Almost every selected discordant source has a positive proportion of genuine marked clocks with two thick, oppositely colored branches obtained by changing a short block of coarse bits. Their ordinary arguments lie in one arithmetic progression. The indices can have polynomial range while the ordinary stride is much larger; these are distinct statements.

A finite graph joins candidate ordinary sites when their orbits meet within a supplied horizon. Opposite invariant colors force every component to omit many sites. [LocalResampling.lean](LocalResampling.lean) checks this finite graph deduction and the exact stride. Under the additional fixed-target density input M, failure of Collatz yields infinitely many rows with a lower graph-deficiency fraction of order at least \(d^{-3}\), uniformly in each proposed horizon. A contradictory large-row upper estimate remains **OPEN**. The analytic probability and density statements are not formalized by the finite graph module.

The [gate-transport diagnosis](GATE_TRANSPORT.md) explains why existing inverse populations and ordinary typical-path bounds do not supply that upper estimate or the all-rank descent. A fixed gate consumes the available native binary clock. Distinct inverse prefixes reaching it then share the same subsequent ordinary future. An upper bound for a new unbiased source cannot simply be applied to that selected future.

The [repo-wide reassessment](REEVALUATION.md) records the different routes and their exact remaining obligations. The refresh inventories 143 open PRs and compares the relevant source families; it is not a claim to have independently proved every statement in every branch. The latest diffusive-row proposal is included as a qualified comparison, with its own fixed-total floor and intermediate-range upper gap preserved.

## 6. Replay and evidence

With Lean 4.34.1 and Mathlib at `d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
lake env bash /path/to/closing-proposal/check_lean.sh
python -B /path/to/closing-proposal/check_rank_two.py /path/to/directed-return/vendor/ReverseBasin.lean
python -B /path/to/closing-proposal/check_rank_three.py
python -B /path/to/closing-proposal/check_mersenne_returns.py
python -B /path/to/closing-proposal/check_opposite_arm_queries.py
python -B /path/to/closing-proposal/replay_quantitative_tables.py
```

The publisher's final fresh build compiled 17 mathematical modules plus `PublicAudit`, auditing 100 public declarations: 70 earlier dependency statements and 30 new ones. The five finite checkers also passed under `python -O`, with identical normal/optimized output. An independent verifier replayed 31,847 literal ordinary clocks across all 214 first family members. These execution events and source hashes are in the [report packet](../../../reports/ayh-resource-reset-20261124/closing-proposal/README.md).

The remaining decisive task is an all-rank argument for `HigherRankProgress`, or a genuinely opposing ordinary-source estimate in the analytic route. The present finite coverage, conditional consumers and tested constructions do not furnish it.
