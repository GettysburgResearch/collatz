# Independent review of the signed Hardy-flow lane

**Verdict: VERIFIED within the stated scope.** I independently reconstructed
CAF-001 through CAF-006, inspected the finite checker, and rebuilt finite
flows by a different procedure. No mathematical correction is requested
for the frozen files below. This is an internal review by a separate
collaborating agent, not external peer review or a formal proof.

The result is an explicit obstruction to identifying signed Hardy fixed
points with exceptional ordinary Collatz components. It does not resolve
Collatz, exclude arbitrary cycles, or prove convergence of an arbitrary
ordinary input. Every constructed eigenvector is supported on integers
whose convergence is already exhibited by finite paths.

## Exact reviewed bytes

| File | SHA256 |
|---|---|
| `research/creative-closure-20261120/analytic_flow.md` | `6261ef1916469bc8357ee00ef07e7b55c37f668275c14af545cb8e2aa6d64bc6` |
| `experiments/creative_analytic_flow.py` | `d989cf46752581db238a629cf2ac3f16c2bd8c09d96dae095df330f401fe0e9a` |
| `reports/2026-11-20-creative-closure/analytic-flow-report.json` | `8cefbc6c0aa687dfb9ffa54f4b4f284d8c4423af62fc1acb44e21c9f4b4245a2` |
| `reports/2026-11-20-creative-closure/analytic-independent-check.py` | `fd8d52ae97428ffb1716b39e203678a3b64bb3a8af7a1c8949fcbb4f202d042f` |
| `reports/2026-11-20-creative-closure/analytic-independent-report.json` | `6126e408e84795ea3571ddd17b25e3602d41c2a648048285cab741d2e3cb0a73` |

## Mathematical reconstruction

### Normalization and CAF-001

The shortcut map is the ordinary positive map, including its `1 <-> 2`
cycle. The Hilbert space has positive-index coefficients only. Directly
counting the at-most-two fibers proves boundedness of the pushforward
`Q`; the displayed pullback is its adjoint. In particular, the direction
of the two operators is consistent throughout the manuscript. Coefficient
comparison in the root-of-unity equation gives the pullback fixed-point
equation. On this Hilbert space its even-coordinate equations force a
nonzero coefficient to repeat infinitely often, so `ker(I-P)=0`.

For the inverse construction, the three admissible exponents run through
the required three residues modulo 9. Exactly one candidate is divisible
by 3. The other two are odd integers above their parent, with exact
ordinary shortcut clocks between 2 and 7. The monotone increase in the
inverse direction and the deterministic forward odd map rule out both
cross-branch collisions and repetitions at different depths. Every
selected node consequently has an explicit route to 5 and then 1. No
2-adic or nonintegral state is being substituted for an ordinary integer.

### CAF-002: full physical flow and infinite multiplicity

I checked the overlaps at the level of ordinary even integers. Every
interior even integer on a macro edge has odd part equal to that edge's
odd parent. Therefore only the two selected children of the same parent
can contribute to a shared interior location. Those contributions add;
at the zero-weight root their common portions cancel. This accounts for
all actual coordinates and avoids treating macro edges as disjoint
physical paths.

The odd generations have square energies `4/2^d`, whose total is 4.
Every nonroot odd parent contributes at most six times its square weight
to its interior even coordinates. At the root, the difference of the
two clocks is at most four. Thus the stated full norm bound `4 <= ||a||²
<= 32` follows. Conservation is valid on every coordinate, including the
root and unselected coordinates. The finite square norm and bounded
operator justify the resulting exact Hilbert-space equality.

For the roots labeled `0^k1`, selected-tree incomparability also means
incomparability under the actual forward odd map: each root's forward
path back to 5 is exactly its displayed ancestor path. An ordinary
integer cannot reach two such roots. The corresponding complete inverse
basins, and therefore the constructed physical supports, are disjoint.
This proves infinite orthogonal multiplicity without assuming the
conjecture. Infinite absolute mass is equally explicit: every odd
generation has absolute mass 2. These fixed vectors are not finite
signed source measures.

### CAF-003: complex eigenvalues and the tail

For a nonzero complex eigenvalue, propagation along one physical edge
requires dividing a child contribution by `lambda`. The assigned
`lambda^j` child weights and `lambda^k` interior weights satisfy exactly
that rule. Overlap contributions have the same complex phase relative
to the parent, while the two root contributions cancel on their common
portion. The argument therefore works for complex values, not only
positive real values.

Writing `r=|lambda|`, each nonroot parent's two children have total
square weight at most

\[
q(r)|a_p|^2,\qquad q(r)=\tfrac12\max(r^4,r^{14}).
\]

This maximum is required for `r<1`; replacing it by the largest-exponent
term alone would be incorrect. The stated bound is less than one on the
entire asserted disk. The first odd generation has energy at most `4q`,
and the even coordinates have the finite multiplier
`C(r)=sum_{k=1}^6 r^(2k)`. Hence the infinite full physical sequence is
square summable. The separate collision-pair construction at `lambda=0`
is valid, has disjoint pairs, and has explicitly convergent support.

The finite truncation defect is exactly `-lambda*a` on the last odd
generation, with no missing exterior image coordinate. If its last odd
generation has square energy `E_D`, a valid omitted square-tail bound is

\[
 E_D\frac{C(r)+q(r)}{1-q(r)}.
\]

Indeed the later odd generations cost at most `E_D*q/(1-q)`, and the
new interior edges from depth `D` onward cost at most `E_D*C/(1-q)`.
Their locations are new, since their odd parts are later parent nodes.
The published checker uses exactly this bound. For `lambda=1`, the
defect's square norm tends to zero but its absolute mass remains 2;
the manuscript explicitly distinguishes these two statements.

### CAF-004: the positive stationary cone

For a nonnegative fixed vector, `a[T(n)] >= a[n]`. A positive coefficient
on an orbit with infinitely many distinct states would therefore violate
every finite `ell^p` norm. On a cycle the coefficients are constant. At
each cycle node the preceding cycle node exhausts the incoming mass, so
all off-cycle incoming coefficients vanish; iteration excludes the
preperiodic part. The converse for summable combinations of cycle
indicators is immediate. This proves the precise statement for
`1 <= p < infinity`; it says nothing analogous about `ell^infinity`.
In particular, removing signed cancellation does not turn this
stationary cone into an escape detector.

### CAF-005: finite coercivity and the Fredholm boundary

The dyadic-ray proof includes the final difference outside the original
polynomial's support. This endpoint is essential. Telescoping from that
zero endpoint and applying Cauchy--Schwarz gives the displayed
`L(L+1)/2` constant; rays use distinct even residual coordinates, so
summing loses no sign information. The triangular examples supported on
`3*2^j` have no odd pullback predecessor term. Their exact norms give
residual-to-vector norm of order `1/log D`, establishing the asserted
order, without a claim that the numerical constant is optimal.

These normalized examples are approximate null vectors for the
injective operator `I-P`. They prove its range is not closed. The
closed-range theorem transfers this failure to `I-Q`; the adjoint
kernel identity proves the latter range is dense. Both failures and the
infinite exact fixed space preclude a conventional finite Fredholm
interpretation. Adding the zero coefficient only adds a fixed
one-dimensional summand and does not repair either issue. This is an
operator statement at the expressly chosen Hardy normalization, not a
refutation of results in different weighted spaces.

### CAF-006: natural-boundary control

For `3|m`, pulling back the lacunary series shifts its dyadic index,
leaving exactly `z^m`. At roots of unity of order dividing `m*2^k`, the
tail terms are positive along the radial approach and their sum tends
to infinity. Such points are dense on the unit circle. A holomorphic
continuation through any point would give a neighborhood containing
one of these singular points, so continuation through an arc is
impossible. The example need not belong to Hardy space, and the text
does not claim that it does. For `m=3` its arithmetic support is again
known to converge. The natural-boundary phenomenon is explicitly
credited as prior work.

## Source and novelty boundaries

I checked the relevant operator definitions and source limitations in
[Neklyudov, arXiv:2106.11859v9](https://arxiv.org/html/2106.11859v9)
and [Béhani, arXiv:2303.03203v1](https://arxiv.org/html/2303.03203v1).
The former's Proposition 4.2 and Lemma 4.3 give the displayed adjoint
pair; the present range and kernel analysis addresses the finite
Fredholm reading at this normalization. It does not assess every result
or every extended-index convention in that paper.

Béhani's Definition 2.2 and Proposition 2.3 explicitly contain earlier
signed two-ray vectors and their weighted norm criterion. For the
nonzero two-ray vectors with index `m>=1`, setting the coefficient
weights to one gives geometric square summability exactly when
`|lambda|<1`. Statements elsewhere in that source about a larger disk
use its Bergman or weighted spaces and are not imported into the
unweighted Hardy claim here. The manuscript makes no claim to be the
first construction of signed Collatz eigenvectors.

[Bell--Lagarias, arXiv:1408.6884v1](https://arxiv.org/abs/1408.6884v1)
is cited for the prior inverse-orbit natural-boundary phenomenon. The
special example in CAF-006 has a complete elementary proof in the
manuscript; it is not presented as a new natural-boundary discovery.
This review is not an exhaustive novelty search.

## Independent finite reconstruction and replay

The [independent checker](analytic-independent-check.py) imports no
production module. It generates candidate odd children by the
recurrence `q -> 4q+1`, checks their clocks by ordinary forward
iteration, and then uses a different construction of the entire flow:
assign current only to depth-`D` leaves, follow each leaf literally to
the root, and transport that current along the actual path. Its leaf
current is `sign*lambda^L/2^(D-1)`, where `L` is the replayed physical
length. Adding these transported currents reconstructs both intermediate
odd weights and every overlapping even weight. The root's total
received current cancels exactly.

The [independent report](analytic-independent-report.json) contains
24 flow cases: depths 1 through 8 for each of `lambda=1` and `21/20`,
plus depth-5 flows at eight antichain roots. Seventeen of these have
published counterparts, and all seventeen full vector hashes match.
The report also checks fourteen finite continuations against the
infinite-tail certificate, all 28 pairs of physical antichain supports,
and six triangular examples. It rejects an inserted root leak and an
unlisted exterior source.

Including the depth-3 setup for those negative controls, the independent
run replayed 1,284 leaf-to-root paths containing 39,496 literal shortcut
edges. Separately, it checked 3,801 candidate macro paths containing
17,130 edges and examined 8,720 full residual coordinates. These are
aggregate check counts with repeated edges, not counts of unique
ordinary integers. Finite continuation checks alone do not certify an
infinite tail; the bound was reconstructed above.

Both the ordinary generation and the optimized replay passed:

```sh
python reports/2026-11-20-creative-closure/analytic-independent-check.py --output reports/2026-11-20-creative-closure/analytic-independent-report.json
python -O reports/2026-11-20-creative-closure/analytic-independent-check.py --compare reports/2026-11-20-creative-closure/analytic-independent-report.json
python -O experiments/creative_analytic_flow.py --compare reports/2026-11-20-creative-closure/analytic-flow-report.json
```

The first command is a historical generation command: exclusive-create
writing intentionally refuses to overwrite the existing report. Use
`--compare` for routine replay. The independent checker verifies the
three frozen author-file hashes before running; all verification gates
use explicit exceptions and remain active under `python -O`.

The production replay matched the frozen report exactly: 17 main flow
cases, eight antichain cases, 18,312 macro edges, 82,682 positive
physical shortcut edges, 62,637 residual coordinates, 536 finite
coercivity cases, 64 zero-eigenvalue pairs, and five rejected negative
controls. Its separate negative-control prefix count is 3; those edges
are not folded into the positive physical-edge count.

No source files were modified during this analytic review. No global
closure claim or external-validation status follows from these checks.
