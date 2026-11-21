# Physical word erasure and source-preserving transport

This is a literature-inspired continuation of [PR184](https://github.com/GettysburgResearch/collatz/pull/184), frozen at `366dab89ee9548084ab9b5e4e90ff82abf287a20`. We use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

**Full Collatz remains open.** The purpose of this pass is to attack the universal completion step using primary literature, then keep the physical constructions and the exact missing estimate close together. No convergence axiom or admitted proof is added.

## First checkpoint

Three complementary investigations produced the following material.

1. **A physical replacement for part of a semigroup proof.** Applegate and Lagarias's weak Collatz theorem permits multiplication by additional integers. We derived the exact arithmetic cost of moving a multiplier through a legal Collatz prefix, and found a new ordinary eight-step identity

   \[
   T^8(256v+184)=T^8(768v+554)=27v+20\qquad(v\ge0).
   \]

   It supplies smaller ordinary partners after arbitrarily long initial odd runs. The standalone identity and the general coprime pullback arithmetic are checked in Lean core. The [complete lifting argument](LITERATURE_LIFTING.md) distinguishes these physical paths from multiplication allowed only in the semigroup.

2. **A checked incomplete cover of an infinite arithmetic branch.** The [certificate](certificates/al27_certificate.json) and [separate verifier](certificates/verify_al27.py) give physical smaller-source mergers on 446 of the 576 progressions refining `27 mod128` modulo `73728=2^13*3^2`. Each successful row works for every nonnegative progression parameter. Exactly 130 classes remain unresolved. Of the 446 successes, 116 lie beyond the union of the elementary smaller-predecessor test and direct descent through clock 13. This is a comparison with those two specified tests, not a novelty claim over every earlier repository certificate.

3. **A sharp finite transport budget.** [HarmonicTransport.lean](lean/HarmonicTransport.lean) proves that a positive original atom cannot visit infinitely many distinct endpoints in a finite mass space if reciprocal transport bounds have unbounded partial sums. Its explicit finite form is

   \[
   J a\le2CW
   \]

   whenever `2^J` endpoints are distinct, total mass is at most `W`, and `a<=C(k+1)w(x_k)` through that window. The [transport note](HARMONIC_TRANSPORT.md) develops a clock lift, an unconditional resolvent construction, and the precise quadratic saving that would imply full absorption, including exclusion of nontrivial cycles. The operator construction and its infinite-sum interpretation are written proofs at this checkpoint; the finite harmonic kernel is the part already checked in Lean.

The subsequent composition work is ongoing. The source and publication receipts identify exactly which files were compiled at each checkpoint.

## The global idea and its current boundary

PR173 proves that every positive ordinary orbit enters a marked odd band

\[
n=2^d+r,\qquad(d+1)r\le70\,2^d.
\]

The band can support long initial rises, so immediate descent is not a valid universal inference. The physical route instead seeks a smaller **marked representative of the same forward component**. Deleting an initial odd prefix through an exact endpoint identity is one way to construct that representative.

The analytic route keeps the original source atoms. Let `K` be the first-marked-return pushforward killed at one, `b_j=K^j a`, and `S_0` the original total mass. A clock coordinate separates successive visits even on a possible cycle. For the specific quadratic resolvent coefficients

\[
c_j=\frac1{(j+1)(j+2)},
\]

the exact clock fibers imply that any source `x` still surviving `k` returns forces

\[
\|\widehat U^k\|\ge
\frac{a(x)(k+1)(k+2)}{16S_0}.
\]

Thus a vanishing normalized quadratic bound along a subsequence **for that same weight** would force every source to terminate. The needed return-specific improvement is not proved. The generic construction with logarithmic coefficients uses a different weight and cannot be substituted here. Moreover a completely terminating decrement map can still have quadratic norms for a fixed polynomial spatial seed, so the proposed norm saving is sufficient, not an equivalence with termination.

## Exact source boundaries

The [source manifest](source-pins.json) records the repository heads and primary literature. In particular:

- PR173's forced-section theorem is inherited through the frozen PR184 packet.
- PR175's return-rank obstructions and PR178's phase/frequency results explain why phase or a two-feature rank alone does not supply descent.
- PR180's predecessor populations concern actual incoming paths but do not provide the original-mass upper bound required by the clock-fiber calculation.
- PR146 was refreshed at `f431078244e868dc699fad011044f0d5e7f76437`; its growing intervals and terminal-five comparisons still have an explicit universal closure obligation.

None of those neighboring results is relabeled as a universal coverage theorem.

## Reproduction

Run the exact arithmetic certificate verifier with

```sh
python -X utf8 -B research/literature-orbit-closure-20261121/certificates/verify_al27.py
```

The Lean packet uses Lean 4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The core pullback and eight-step files depend only on `Std`. No `native_decide` shortcut, `sorry`, or custom convergence axiom is used. Repository integrity validation is separate from mathematical proof checking.

The first unsupported step is a complete selection of physical erasures/mergers, or a source-preserving transport saving valid on every required ordinary input. Neither is supplied by the successful finite families.
