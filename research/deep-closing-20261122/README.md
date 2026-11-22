# Actual-orbit entropy and direct closing attempts

Date: 2026-11-22. **Collatz remains OPEN.** This continuation of PR #185
refreshes the repository-wide research map and the latest source heads,
then attacks escape, cycles and source replacement in parallel. The main
positive result is a quantitative entropy restriction on **every empirical
limit of one actual positive orbit that is not eventually periodic**. Its finite engine is
proved in Lean. The opposing entropy estimate needed to exclude escape
has not been proved.

## Main result

Use the accelerated odd map

\[
U(q)=(3q+1)/2^{v_2(3q+1)},\qquad q_i=U^i(q_0).
\]

After discarding an initial transient, the states are positive odd ternary
units. Suppose the orbit is not eventually periodic, and let \(\mu\) be any weak limit of
its time-averaged laws on \(\mathbb Z_3^\times\). Write \(H_m(\mu)\) for
entropy of its residues modulo \(3^m\), using natural logarithms. Then

\[
H_m(\mu)\le m\Phi(\log_2 3)\quad(m\ge1),\qquad
\Phi(a)=a\log a-(a-1)\log(a-1),
\]

and therefore

\[
\overline{\dim}_{\mathrm{ent}}\mu
\le\theta:=\frac{\Phi(\log_2 3)}{\log3}
=H_2(\log_3 2)=0.949955527188\ldots<1.
\]

This is an unconditional written deduction from the exact integer
recurrence, with independent proof reviews. It assumes no GRH,
predecessor-density result, canonical potential, or independent-gap model.
It is a restriction on a hypothetical escape, not a contradiction and not
a claim that its limiting measure is entirely singular.

### Why the estimate holds

The last \(m\) actual odd gaps determine the endpoint modulo \(3^m\): the
initial-source term carries a factor \(3^m\) and every denominator is a
power of two. A geometric reference code bounds the entropy of their
arbitrary joint law by its mean gap cost. The exact logarithmic telescope
of the positive recurrence gives an asymptotic mean gap at most
\(\log_2 3\). A finite sliding-window count, followed by a fixed-precision
weak limit, yields the result.

The corresponding collision bound is

\[
\sum_{r\bmod3^m}\mu(r+3^m\mathbb Z_3)^2\ge3^{-\theta m}.
\]

See [the complete proof](ACTUAL_ORBIT_ENTROPY.md) and
[the exact formalization boundary](FORMALIZATION.md).

## Three direct attacks and their outcomes

| Attack | Result in this packet | First unsupported closing step |
|---|---|---|
| Actual escape law | Entropy ceiling at every ternary precision; finite source-to-entropy engine in Lean | A larger entropy lower bound, or smaller collision upper bound, for this same actual orbit law |
| Whole cycle denominator | Lean proof that \(\binom Ap^7<120^A\) in the nontrivial-cycle cone; the conditioned numerator law is asymptotically far from uniform under the stated existing logarithm bound | An atom-specific bound \(\rho_{A,p}(0)<A/\binom Ap\), with the complete denominator retained |
| Coupled source and target | All-length permutation rigidity for \([3,2,2,1]++[2]^k\), plus a complete lower-grade replacement for the previous long example | A legal replacement or target descent for every joint minimal counterexample |

The [sibling attempt](SIBLING_SMOOTHING_ATTEMPT.md) directly tests whether
same-future sources supply the needed entropy. They do become ternary
equidistributed, but obtaining that entropy has exponentially large first
gap cost. The ordinary family \(B^j(1)\), \(B(n)=64n+21\), has a Haar source
limit and maps to the point mass at 1 in one odd step. General source-to-time
entropy transfer therefore fails; an escape-specific estimate remains open.

The [cycle attempt](GRH_AFFINE_CYCLE_ATTEMPT.md) tests the GRH affine-mixing
theorem of Breuillard and Varju against the actual fixed-count law modulo
\(D=2^A-3^p\). The number of available words is exponentially smaller than
the modulus at this clock. Uniformity is unavailable even if stronger GRH
assumptions are granted. The note then pursues the narrower zero-residue
bound through Fourier and entropy identities; it does not prove that bound.

The [arithmetic attempt](ARITHMETIC_ATTACK.md) uses the full joint-minimum
premises from PR #177. Its rigidity theorem rules out arbitrary permutations
of one problematic prefix family as a source repair. The explicit new
source also shows that our previous long alphabet-four example is not
extremal in grade. Neither result establishes universal coverage.

## What changed after reading the latest repository work

The source refresh covers the latest 50 PR metadata entries and the five
advanced source branches #175, #176, #177, #178 and #180. It incorporates
#177's joint least-target/minimal-grade/maximal-source reduction, #176's
global source records, and #180's critical Green-energy and multiscale
sibling-current formulations. Earlier #146 and the band/merger work remain
in the inherited research map. This is a targeted mathematical delta read,
not a new audit of every historical theorem.

[SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json) freezes exact heads, exported
source-file hashes and reading scope. These newer branches are referenced
without importing their full histories. Neither new Lean module depends
on a theorem from them.

## Deep machinery tested

The coding principle already appears in [Paper 150, section 4](https://rstation.ai/problems/collatz/papers/150).
Here it is applied to actual forward sliding windows, with original time
weights and the real gap budget retained. The repository contribution is
this complete actual-orbit deduction and its finite Lean core; no priority
claim over all earlier entropy arguments is made.

Full-entropy capped inverse laws, affine Poisson boundaries, quantitative
mixing on the real/ternary quotient, GRH finite-field mixing, and fixed-rank
S-unit/Subspace methods were tested at their actual hypotheses. The
[joint-boundary attempt](JOINT_BOUNDARY_ATTEMPT.md) records why the quotient
mixing theorem does not yet yield the required integer estimate.
[SOURCES.json](SOURCES.json) separates inspected primary statements from
independently proved results. Fresh author manuscripts remain
SOURCE-QUALIFIED; none is silently promoted to a verified dependency.

## Evidence and reproduction

- `lean/OriginalSourceEntropy.lean`: 21 public theorem audits. Exact source
  paths, arbitrary weighted word laws, optimized mean cost, sliding-window
  multiplicity, and the finite logarithmic telescope.
- `lean/CycleWordEntropy.lean`: three public theorem audits for the exact
  all-parameter binomial bound.
- `reviews/`: independent mathematical reconstructions, bound to exact
  source bytes in [REVIEW_BINDING.json](REVIEW_BINDING.json).
- `certificates/`: small exact arithmetic and cycle-law controls, including
  intentionally damaged inputs, in normal and optimized Python modes.

Run the new packet alone against the pinned existing Lean/Mathlib runtime:

```sh
python -X utf8 -B research/deep-closing-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/built/mathlib \
  --build-dir /absolute/path/to/empty-external-build
```

The runner requires a clean complete checkout, compiles both unchanged
sources, audits every public theorem, replays the new controls and runs the
default repository gate. It does not rebuild unrelated earlier packets.
Detailed execution receipts belong under `reports/deep-closing-20261122/`.

The central next theorem is explicit: an actual escaping orbit must force
entropy above this ceiling, or violate an equivalent collision bound.
The current work establishes the ceiling and tests two proposed ways of
crossing it. It does not establish the opposing inequality.
