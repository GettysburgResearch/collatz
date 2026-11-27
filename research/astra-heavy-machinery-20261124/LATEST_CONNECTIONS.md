# Connections to the final repository refresh

This is a focused continuation, not a rebuild of earlier proof bundles. The preceding global-synthesis intake mapped the available PR heads. Before publishing this packet, the thirty most recently updated PRs were re-read as metadata, and the new mathematical material in the six branches below was inspected at these exact heads. A full snapshot is in `reports/astra-heavy-machinery-20261124/LATEST_HEADS.json`.

| PR | Frozen head | Relevant new source |
| --- | --- | --- |
| 188 | `f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d` | `research/astra-global-step-20261124/SHIFT_DISTANCE.md`, `AUXILIARY_RESIDUES.md` |
| 192 | `045be43632f274dd64faf15714e42cc8de27a2e9` | `research/astra-high-variance-20261124/CENTRAL_CLOSURE.md` and the original-floor return comparison |
| 195 | `07aa5124f7ca482b6665d61355fac0af5f6e55b2` | `research/astra-global-closure-20261124/closing/adelic/README.md`, `closing/cycles/NEAR_MINIMUM.md`; earlier GS1 pinned separately |
| 197 | `9ed095c3b3386d66c1dba103117e8dda0268b7aa` | `research/ayh-resource-reset-20261124/continuation/HEAD_EDGE_RIGIDITY.md` and inverse-word access |
| 199 | `d868f8e8405c08b8c501236853bea495ca593824` | `research/optimal-critical-ancestors-20261124/README.md`, `FIRST_PASSAGE.md` |
| 200 | `c43fcbe6643c3d816975a4fb4328dc19dbdac6fb` | `research/regularity-rigidity-20261124/AUTOMATA.md`, `LOCAL_BLOCKS.md` |

## The actual joint first-passage population

PR197 supplies the comparison of an ordinary head input `x` with `floor(x/81)`. PR199 turns a summable normalized population of failures into a full Collatz criterion, under its stated predecessor and uniform barrier inputs. This is stronger than merely producing a successful comparison in each component.

The new [HEAD_DIAGONAL theorem](ergodic/HEAD_DIAGONAL.md) joins our exact ordinary inverse lift to that interface. For each fixed odd unit `b`, it constructs a positive fraction of **each individual sufficiently high head band** on which the two actual first-passage roots are equal, at the same clock, and reach `b`. The same selected pairs work for every barrier between `b` and a fixed positive fraction of the head scale. It uses the fixed-target positive-density input alone. No independent replacement of the two first-passage laws is made.

The carry identity behind the comparison is `81m+65=2^L z`, with `L≥4`. The parent has odd-gap word `(1,1,1,L−3)` and the child has an initial halving run; both meet at the same shortcut clock `L`. A finite phase bank, bounded inverse choices, a fixed-rank E2 lift and bounded multiplicity put linearly many such pairs in the requested head band while retaining their original target. All pre-meeting states are a fixed fraction of the head scale, so both first passages occur after this merger.

This is a genuine lower bound on the diagonal of the joint law. PR199 needs an upper bound on its off-diagonal failures, summable over levels. The lower bound leaves that term uncontrolled. Repeatedly taking special dyadic dilates of one fixed input does not make independent trials: their constructed parents follow the same four-odd prefix back to the given input.

PR199 also obtains optimal ancestor exponents on its relaxed critical sections and a uniform-in-cutoff approximation of a component by fixed-target ancestor sets, using its extra uniform minimum-tail input. Our three-step critical arms control the same phase, exact rank and ordinary endpoint, rather than claiming the optimal global ancestor count. Neither result makes a selected endpoint smaller than the original least nonconverger.

## Adelic continuation and full rational normalization

PR195 GS1, already at `a24ef018147a1e16bf314d14085e2d0d6c620d32`, proves the ordinary-source equivalence between eventual periodicity, rationality and D-finiteness of `Σ2^A_j z^j`. This is prior work, recovered under `z↦z/2` in our basic two-place note. The new PR195 A2 gives a capacity bound for meromorphic continuation and, when the mean clock exists, an entire natural boundary.

[ADELIC_MAHLER.md](diophantine/ADELIC_MAHLER.md) combines that capacity mechanism with our physical pole argument. A hypothetical Mahler relation supplies meromorphic continuation on every local unit disk. Any Taylor radius larger than one would then make the adelic capacity positive and force rationality by Bost–Chambert-Loir. The exact local radii reduce the rational normalization to `±1/2`, and the companion integral series excludes both by the genuine Mahler-denominator theorem. Thus every nonzero rational normalization and every integer base is covered, even for an oscillating mean and for positive odd rational sources. No functional equation for every ordinary source is supplied.

For cycles, PR195's near-minimum theorem forces many multiplicatively independent suffix fixed centers, while PR188 forces large disagreement at every nontrivial rotation of a long primitive ordinary period. Those suffix centers need not lie in one fixed S-unit group, and the shift lower bound supplies no opposing cheap-rotation upper bound. Every periodic candidate already has a rational clock series. The full evaluated divisor `2^A−3^p` is therefore still an independent ordinary-cycle obligation.

## Automatic tests and weighted stopping clocks

PR200 Theorem C already gives an arbitrary-base sparse-error obstruction and a corresponding automatic-approximation criterion; it also constructs macroscopic same-target blocks and weighted-clock colors under its predecessor inputs. This packet does not claim priority for those conclusions.

The exact testing lemma here uses the stronger named ordinary-density and adjacent-coalescence inputs. [WEIGHTED_CLOCKS.md](dynamics/WEIGHTED_CLOCKS.md) applies it to PR200's weighted labels and obtains exact natural frequencies, including against every fixed automatic test in every radix. If `δ` is the convergence-basin density, each admissible weighted residue modulo `m` has coefficient `δ/m`. The proof kills every nontrivial Fourier character by compatible dilations by two and three; the constant character remains `δ`. It gives exact macroscopic block frequencies but no value for `δ`.

## The global shifted moment

PR192's `CENTRAL_CLOSURE.md` gives a single explicit independent-gap negative moment whose limit is the Dirichlet mass of **all** ordinary nonconvergers, including nontrivial cycles. Its vanishing would settle the complete conjecture. This is a useful full target against which to test the present machinery.

A fixed surviving integer contributes its full positive mass through one word at each depth, even when that word has exponentially small probability under the independent model. Our corrected-height recurrence concerns selected actual classes; the automatic-testing result concerns bounded source observables; the Mahler theorem supplies a regularity criterion without proving its premise. None controls the uniform integrability of that singular, same-word endpoint/carry statistic. Replacing its joint data by typical marginal residues would lose the contribution that the criterion is designed to retain.

The source comparisons produced the positive head-diagonal and adelic-normalization theorems above. They did not prove the remaining summability, analytic regularity, shifted-moment vanishing, or full numerical cycle exclusion.
