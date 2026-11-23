# Independent review: actual fibre density and clock residues

Reviewer: root agent. Date: 2026-11-23.

**Verdict: VERIFIED at the stated source-qualified and fixed-resolution
scope.** The new geometry and joining arguments were reconstructed from
the frozen text. They do not provide the actual ternary collision upper
bound or establish Collatz.

## Frozen targets

| File | SHA-256 |
|---|---|
| `research/profound-step-20261123/ENTROPY_ARITHMETIC.md` | `b2906cada26d3bfbc3412423fb2b4ce4f0398c8d23518dcfd894f72ec58ff2f6` |
| `research/profound-step-20261123/lean/ScaleAvoidance.lean` | `53dd7d9eefccdea3e159d6522639266957b55b820776d6932a239a0c0e17563b` |
| `research/profound-step-20261123/lean/ScaleAvoidanceAudit.lean` | `537181c77d173e46c436cd17954dd2763fd3bf4f977639d9cbc507c70c49db3a` |
| `research/profound-step-20261123/reports/scale-lean-check.json` | `ab54535a4d6ce38f264eb1439a8938cfffec0a6f9efc15260f746fe6e5f0fa3c` |

The review uses the retained canonical-boundary hypothesis exactly as stated
in the pinned predecessor packet. It does not independently reprove the
existence of that qualified trace, its floor, or its selection identity.
The specific inherited conclusion used here is full upper local dimension
of the actual common law, rather than dimension of its support.

## Reconstructed density argument

1. For each sufficiently small interval of width \(w\), the first scale
   crossing \(4/w\) is after the fixed tail index and lies between
   \(4/w\) and \(4L/w\). Arbitrarily large downward jumps cause no problem:
   only the one preceding scale and its permitted upward jump are used.

2. The proposed floor choice places a complete translate of the target
   arc strictly inside the scaled interval, with slack at both ends.
   Its pullback is a hole of relative width greater than
   \(\eta/(4L)\). Choosing \(2^h>32L/\eta\) guarantees a closed dyadic
   child within the hole. Half-open counting cells make their parent
   relation unambiguous; their discarded child's closure avoids the
   exceptional set, including boundary points.

3. The recurrence for the number of occupied cells yields upper box
   dimension below one. Restricting a positive amount of the original
   law to such a set, the elementary dyadic mass count and
   Borel–Cantelli give upper local dimension below one almost surely
   for the restriction. Since the original measure dominates that
   restriction up to a fixed constant, it also has upper local dimension
   below one there. This contradicts the supplied actual-law dimension
   hypothesis. Lower local dimension, exact dimensionality, and a
   uniform Frostman bound are not assumed.

4. The countable arc basis, all tail indices, and all denominators \(6^k\)
   can be handled simultaneously. The characters with denominator \(6^k\)
   generate the inverse-limit topology of \(X_6\). Density in every one
   of these circle factors therefore gives tail density in the full
   solenoid, not merely density in a single circle projection.

5. The physical class identity subtracts the same diagonal integer
   \(q_j\), so it preserves the intended source. The events \(E_j\)
   increase to full path probability. For almost every path they
   eventually all hold, while the same boundary point visits each open
   solenoid set infinitely often. Tonelli then proves the divergence
   of \(\sum_j p_j\kappa_j(V)\). No time-frequency lower bound is inferred
   from that divergent sum.

## Reconstructed critical-branch joining argument

The phase joining is a product because its conditional nonzero Fourier
modes would otherwise be nontrivial eigenfunctions of a Bernoulli shift.
The two-sided formulation and direction of time are explicit.

For the stronger clock statement, the combined coordinate
\(\beta=(K\bmod m+\theta)/m\) obeys the exact update
\(\beta\mapsto\beta+(\ell-a_0)/m\). Under the product reference measure,
nontrivial Fourier modes not divisible by \(m\) decay against bounded
gap-cylinder functions by the strict modulus of the geometric
characteristic function. Modes divisible by \(m\) have a nontrivial
irrational-rotation phase whose Cesaro mean vanishes. This proves
ergodicity, which is all that is required; ordinary mixing is not
incorrectly claimed for the rotation modes.

Any invariant lift of the already determined gap/phase base is dominated
by \(m\) times the uniform finite-fibre reference measure. Its invariant
density must be constant by ergodicity. The coordinate changes between
\(\beta\) and \((\theta,K\bmod m)\) have only finitely many discontinuity
boundaries, which carry zero mass because the projected phase is Haar.
Thus the weak-limit transport and the final product statement are valid.

This proves uniformity for each fixed global-clock modulus. It does not
make the total gap of a finite word independent of that word, establish
uniformity at a growing modulus, or make the real dilation continuous in
a profinite clock coordinate.

## Formal and literature scope

The four Lean proofs were read against their statements. They formalize
the first crossing, the explicit periodic hole, the relative hole width,
and the finite covering-count induction. The complete source-to-solenoid
measure argument and the joining theorems remain written. The recorded
fresh build and declaration audit pass on the pinned compiler and Mathlib,
with only the usual `propext`, `Classical.choice`, and `Quot.sound` axioms.

The primary Avila–Viana and Benoist–Quint sources were opened during this
review. The note correctly declines to infer independent random driving
from iid marginal gap blocks alone. A finite real probability lift is
not supplied by the escaping physical real coordinate. The cited
higher-rank, entropy-inverse, and scenery results are routes whose missing
hypotheses are stated, not unproved premises imported as conclusions.

## Corrections and retained boundary

Before freezing, the author clarified the closed containing interval,
the inherited source qualifications, and the null coordinate boundaries
in the finite-clock joining. The reviewed version includes these changes.

The crucial observable distinction remains explicit: in a compact
fundamental domain, the ternary coordinate contains the integer part of
the real scaling. It is not the original \(q_j\bmod3^r\). Hence full
density of these actual fibre classes does not by itself contradict the
previous strict collision bound for the original ternary time limit.
