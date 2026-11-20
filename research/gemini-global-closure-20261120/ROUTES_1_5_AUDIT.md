# Audit of Gemini's merger and transducer proposals

**Scope:** the attachment `collatz_multi_route_proposals_2026-11-20.zip`,
routes 1 and 5. This is a narrow audit of the actual claims and executable
evidence. It supplies neither a complete selector nor a Collatz proof.

Use the shortcut map `T(n)=n/2` for even n and `(3n+1)/2` for odd n.

## 1. What the attachment's computation establishes

| Item | Replayed result | Mathematical scope |
|---|---|---|
| `(n,3n)` affine meetings | 43 prefix-free cylinder leaves, Haar measure `41/256` | Whole positive progressions have the displayed finite meeting. |
| `5t+1` falls below t | 33 leaves, Haar measure `59/128` | The *second* arm falls below the first start. This does not establish that their orbits meet. |
| Route 5 coverage | 34 leaves, Haar measure `959/1024` | These are ordinary forward-descent certificates only. The coverage function performs no merger or mode synthesis. |
| Source 121 | `121 -> 182 -> 91` | Smaller partner 91, clocks `(2,0)`, endpoint 91. This is a direct two-step descent for one input. |

The first affine merger leaf is `n=32k+23`, `k>=0`. Its two words are
`11100` and `10001`, each of length five, with endpoint `27k+20`:

```
32k+23 -> 48k+35 -> 72k+53 -> 108k+80 -> 54k+40 -> 27k+20
96k+69 -> 144k+104 -> 72k+52 -> 36k+26 -> 18k+13 -> 27k+20.
```

These identities have identical slopes and intercepts and legal parity at
every positive lift. The finite replay is supported by elementary symbolic
algebra; agreement at four sampled integers alone would not prove it.

The absence of a fixed-word affine identity between `t` and `5t+1` is also
correct. Equality of endpoint slopes would imply
`3^p 2^j=5*3^q 2^i`, impossible by unique factorization. An additional
intermediate arm cannot evade this obstruction if its complete certificate
still consists of fixed affine words on a common progression. Adaptive
pointwise reasoning and induction are different possible proof architectures.

## 2. The proposed completeness steps remain unsupported

**Affine coverage is stronger than ordinary merging.** Here is a
self-contained obstruction, requiring no convergence assumption outside
the displayed known basin. For a convergent input x, put
`kappa(x)=d(x)-2a(x)`, with d its first hitting time of 1 and a the odd count
before that hit. At every clock i, including after reaching the 1--2 cycle,
`kappa(x)=i-2s_i(x)+kappa(T^i(x))`. An affine identity for `(n,3n)` forces
equal clocks and an odd-count difference of one by unique factorization
of the slopes. Its necessary invariant condition is therefore
`kappa(3n)-kappa(n)=2`. Direct finite paths give
`kappa(1)=0`, `kappa(3)=kappa(9)=1`, and initial halving gives
`kappa(2^r*x)=r+kappa(x)`. Thus the known convergent parameters `2^r` and
`3*2^r` never acquire `(n,3n)` affine-cylinder certificates, even at
unlimited depth.

The signed parameter -1 supplies an additional finite-cover obstruction:
its first arm stays -1, whereas its second arm runs `-3,-4,-2,-1,...`.
Before clock three their values differ, and afterwards their odd counts
differ by two instead of the required one. No affine-success cylinder can
contain -1. A finite collection of cylinders consequently omits every
positive integer `-1 mod 2^H` when H is at least their largest precision.
These deductions are included to make the audit self-contained, without
claiming a new global result or a new priority claim.

**Route 5 has no implemented composable selector.** Its coverage function
`transducer_descent_coverage` tests a strict inequality between a source and
one of its forward affine iterates. Its alleged transducer verification
checks only three supplied rank-tuple comparisons. No map associates these
tuples with arbitrary ordinary sources, no invariant proves the claimed
mode changes preserve the problem being solved, and no reset rule permits
reusing the finite tier budget. Proving that `N^3` with lexicographic order
is well-founded does not provide those missing data.

There is a separate input-validation defect: the advertised validator
returns `True` for

```
[((0,1,0), (-1,100,100))].
```

It never checks that rank coordinates are natural numbers. This does not
falsify its hard-coded positive example, but the function is not a general
validator for the stated natural-valued rank interface. Checking the domain
repairs only this software defect, not the absent selector or its invariants.

The source-121 computation does not resolve the source-121 obstruction in
the older inverse-only selector. It demonstrates that an ordinary forward
step can leave the restrictions of that particular inverse-only program.
A valid extension requires a total rule and a common decreasing rank for
all supported cases, including mode changes and ordinary source order.

## 3. Existing results make the next step precise

PR146, pinned at
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, already contains:

- `research/upper-bit-mergers/THREE_RAY_SMALLER.md`: reduction of all
  parameters `7 mod 8` to strictly smaller tripling comparisons, and an
  unbounded necessary clock theorem for this inductive proof graph.
- `research/upper-bit-mergers/THREE_RAY_DENSITY.md`: a true counterexample
  forces `D(X)` at least a positive multiple of `X^0.84` along an unbounded
  sequence, using the stated published predecessor-count input.
- `research/upper-bit-mergers/THREE_RAY_VARIATION.md`: an all-scale power
  lower bound for *true permanent failures*, with its stated Diophantine
  inputs and source qualifications.

The necessary clock theorem is stronger than merely observing a hard
finite residue class: if `2^i | X+1` and `3^A | X`, every smaller positive
start meeting `T^i(X)` needs more than `i+A` odd inputs on its own arm,
with no restriction on its clock. These are already existing project
results, not new claims of this audit.

A completion must control an adaptive certificate for every unchanged
ordinary source, or bound the number of genuine permanently nonmerging
pairs strongly enough to contradict the existing lower bounds. More
finite affine leaves or higher finite descent coverage do not supply
either statement.

## Reproduction

Run `check_routes_1_5.py --proposal-root PATH` against the extracted
attachment. The wrapper pins both source verifier hashes, replays every
reported route-1 affine leaf symbolically, independently recounts the
depth-10 route-5 descent residues, reconstructs the source-121 witness,
and exposes the negative-coordinate validation defect. Its explicit
checks remain active under Python `-O`. Its successful output verifies
these local facts and audit controls only.

Attachment verifier SHA-256 values:

```
route_1_merger_families_pr146/verify_merger_families.py
918bfd76af673d1ca950262dc1f5e07607ee0afeeb3056d8d02b109efac4eac9

route_5_transducer_merging_and_lean4_kernel/verify_transducer_merging.py
bcb71c5f35614017c11daddc0ba8f184c6384c08e753a94d87ebadb7afa97066
```
