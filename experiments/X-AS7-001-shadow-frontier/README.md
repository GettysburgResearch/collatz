# X-AS7-001 — exact inverse-shadow frontier checks

**Finite exact evidence. New theorem claims PROPOSED; no Collatz proof.**
The symbolic all-radius theorem and its limits are in
[INVERSE_SHADOW_FRONTIER.md](../../research/astra-critical-mass/INVERSE_SHADOW_FRONTIER.md).

## Scope

The experiment constructs the complete negative section-inverse tree rooted
at -2. A node with shortcut word length k, odd count q and ternary depth h
consumes e=q+h digits of initial ternary precision. The largest such e through
radius r, plus one, determines the exact budget B_r used here. The proof gives
B_r<=(r+1)^2+1 for every r, independently of the finite table.

The positive inverse search retains an increasing frontier: at D returns
remaining, keep even exits with h(y)-j<B_(D-1) and the optional odd boundary.
The generator uses the closed fan formula; the verifier obtains the entire
fan by literal reverse shortcut steps through residue class two. The complete
unpruned and the pruned balls are both reconstructed. Neither is replaced by
a guessed finite source cutoff.

## Exact coverage

| Check | Coverage |
|---|---:|
| Negative comparison cone through radius 10 | 984 vertices |
| Exact precision budgets r=0,...,10 | 11 |
| Complete/pruned positive inverse-ball comparisons | 478 |
| Sum of complete ball sizes across these cases | 63,939 |
| Sum of pruned ball sizes across these cases | 14,435 |
| Fan exits omitted under the proved guard | 11,395 |
| Complete positive/negative cone matching cases | 48 |
| Strict precision-record nodes through radius 8 | 102 |
| Ordinary record-frontier rank reductions | 1,632 |
| Delayed interior-chain cases | 10 |
| Shortcut steps in their certified bridges | 1,452 |
| Resealed corrupted reports rejected | 8 |

The sums of ball sizes are sums PER TEST CASE, not counts of globally distinct
integers. Their reduction is a finite performance observation, not an asymptotic
complexity estimate. The source-independent branching bound is proved in the
manuscript and is at most D^2+1 per node; total search complexity remains
exp(O(D log D)) under the coarse bound.

The positive ball corpus contains section sources 4..193 at radii 1..6,
18 additional large roots with ternary depths 8,16,32,64,128,256 at radii 1..5,
and four named controls. Units for the large roots are 1,5,17. All parameters
and rows are reconstructed by the verifier; coverage is not accepted from
an unverified manifest.

The guarded cone cases use r=0..5, j=0 or 2, u=1 or 5, and initial precision
B_r or B_r+2. Every paired positive vertex has the exact negative-node ternary
depth and rank greater than (64/3) times the original positive root's rank.
The two complete node sets are compared for equality.

Record-frontier cases use all 102 eligible negative nodes through radius eight,
j=0 or 2, two certified excess depths, both nonzero terminal ternary digits,
and two ordinary positive lifts. Each must have a physical positive path and
P(witness)<P(root)/4. The delayed family uses d=2..6; its longest single bridge
has 486 shortcut steps. These substitutions do not replace the all-parameter
proofs.

## Tests that block false closure claims

The old boundary-only radius-three algorithm at 208363 has seven nodes and
misses ancestor 4445077. The complete ball has twelve nodes. The new guarded
ball has eleven and DOES retain that minimum and its word 100000.

For 121, all positive sources with global rank below 243 are exhaustively
listed. Their complete forward orbit union is a 16-element invariant set,
not containing 121. This proves no inverse ancestor can lower rank at ANY
depth. The first intersection of the orbit of 121 with that union occurs at
shortcut time 54 at 40, proving the exact minimum possible maximum merging
clock is 54. This is an all-witness consequence of a finite complete set, not
an extrapolation from unsuccessful depth-limited search.

The self-test reseals each altered report after changing global scope, the
comparison coverage, a precision budget, record coverage, the recovered
minimum, the omitted-edge count, the complete low-rank witness set, or the
first possible meeting time. All eight must fail against reconstructed data.

## Replay

```bash
python experiments/X-AS7-001-shadow-frontier/run.py \
  --check experiments/X-AS7-001-shadow-frontier/results/canonical.json
python experiments/X-AS7-001-shadow-frontier/verify.py \
  experiments/X-AS7-001-shadow-frontier/results/canonical.json --self-test
```

Add `--full-output /tmp/as7-full.json` to either command to materialize the
entire reconstructed payload. The two full outputs were byte-identical.
An optimized-mode replay also passes: validation uses explicit exceptions,
not assertions removed by Python -O.

Semantic SHA-256:

    7fd1eab2f411c732f2af00b326bb36d67dcca0d1d46a73c1184b22041749b3d7

Full payload SHA-256:

    ab2cca5d69cbf1917317ca54334ed80802a9dcd00607adf6e6ce2de4624cfb60

The verifier imports neither generator code nor repository modules. It uses
physical signed inverse enumeration, Fraction-based reverse words, a separate
CRT inverse, and a backward precision-record reconstruction. Both programs
have the same author: implementation independence is NOT independent proof
review or formal verification.

No external theorem, expensive external certificate, new workflow or assumed
convergence of unexamined sources is a dependency. A failed finite rank search
is reported only at its actual finite scope, never as a counterexample.
