# Direct machinery attacks: pumping, valuation clocks and ordinary transport

**Checkpoint 12, 22 November 2026. Full Collatz remains OPEN.** Three
parallel attacks and a separate graph-criticality attack tested the
closing arguments themselves. They did not obtain a positive universal
target-return estimate, a weighted survivor-decay estimate, or a proof of
the full theorem. The results below delimit specific proof mechanisms;
they are not estimates of how close the project is to completion.

This packet builds on the latest source-qualified ordinary transport,
joint minimum and terminal-energy interfaces. It does not replace a
fixed ordinary source by an ensemble of varying finite witnesses.

## Results and evidence

| Result | Precise output | Evidence |
| --- | --- | --- |
| [Certificate-language rigidity](CONTEXT_FREE_CERTIFICATE_OBSTRUCTION.md) | A sound context-free language of complete certificates over fixed bounded valuation gaps represents only finitely many odd sources. If the gap bound is `M` and the pumping threshold is `N`, each source is at most `2^(M*N)`. | Seven Lean theorems from the explicit `PumpsAt` hypothesis; the classical context-free pumping bridge is a written application. Independent mathematical and source review. |
| [Actual low-clock regime](ACTUAL_LOW_CLOCK.md) | Above the fixed floor 64, an actual positive finite path from `p ≤ 2^c` satisfies `5*A ≤ 8*s + 5*c`. Its low-clock word laws have an exponentially small support fraction in the ternary residue space, forcing normalized `L^q` growth. | One Lean theorem for the clock bound. Written counting, norm and renewal arguments. |
| [Actual compact joining](ACTUAL_COMPACT_JOINING.md) | One fixed hypothetical escaping source gives an invariant binary/ternary/phase joining with mean valuation at most `log_2(3)`. An explicit ergodic, nonatomic, zero-entropy rotation model satisfies those same compact constraints. | Written constructions and proofs. No Lean claim and no ordinary escaping source constructed. |
| [Critical ordinary network](CRITICAL_NETWORK.md) | Each hypothetical escaping component of the pinned harmonic transport has finite-support null functions. Its symmetrized network is recurrent and critical, admits no nonzero global Hardy weight, and already permits compact energy approximation. | Written proof and an application of the exact graph-criticality theorem. Depends on the pinned harmonic-reference and clock-layer identities. |

The exact theorem statements, qualifications and first missing steps are
next to their proofs. [Sources and review](SOURCES_AND_REVIEW.md) freezes
the upstream heads and records the independent review boundaries.

## 1. What the formal certificate theorem changes

For the actual odd map

\[
U(q)=(3q+1)/2^{v_2(3q+1)},
\]

take a language of complete valuation words, every one genuinely ending
at one. In a pumping family

\[
u\,v^k\,w\,x^k\,y\qquad(k\ge0),
\]

the fixed terminal suffix makes arbitrary inverse repetition of the
right block preserve its boundary source. Erasing that block makes the
same argument available for the left block. All family members therefore
have the same numerical source. A shortest accepted representative cannot
be pumpable, and the bounded alphabet supplies the explicit source bound.

The cofinal low-domain records from checkpoint 11 have valuation gaps at
most four and initial even exponent at most three. A sound context-free
grammar with threshold `N` could cover only records at most `2^(3+4*N)`.
It cannot cover all of them. Arithmetic guards, an unbounded arithmetic
state and more general word-changing rules remain outside this theorem.

The Lean core does **not** import a formal theorem identifying
`Language.IsContextFree` with `PumpsAt`. That bridge is the classical
pumping-lemma application stated in the written proof. No global closure
hypothesis is hidden in the proof.

## 2. Why the actual valuation regime matters for Fourier estimates

On any escaping positive orbit, choose one fixed tail lying above 64 and
write its initial value as `p ≤ 2^c`. Every subsequent prefix of `s` odd
steps then has total valuation

\[
A\le\tfrac85s+c.
\]

This is eventually separated by a linear distance from the central
geometric clock `2s`. A support count shows that a uniform normalized
`L^q` estimate for the central word law cannot simply be extended to this
whole low-clock regime. This does not rule out weighted pointwise bounds,
estimates incorporating the fixed source, or the multiscale sibling
comparison described below.

The critical affine-renewal theorem was also applied to an explicitly
specified tilted independent gap law. Its invariant Radon measure and
annular asymptotic do not supply a bound on ordinary integer values or on
shrinking ternary cylinders. The actual harmonic path law has an endpoint
factor that must still be controlled.

## 3. What the two infinite-dimensional constructions retain

The compact joining really is constructed from the occupation measures
of one fixed hypothetical escaping integer. However, compactness retains
neither an ordinary starting integer nor a positive metric-entropy lower
bound automatically. The rotation construction proves that all the
established compact constraints, including growing binary-run counts,
are compatible with zero entropy. Its points are not asserted to be
ordinary positive integers.

For the energy attack, the exact synchronous layer masses produce null
functions on the actual integer network. Infinite branching is retained,
and those functions are approximated by genuinely finite-support ones.
The resulting criticality theorem shows why an unweighted global Hardy
inequality or the existence of compact energy approximants cannot remove
the escaping component. It leaves open inequalities using the numerical
labels or binary runs.

## 4. The central estimates that remain unproved

The most direct analytic target retained from PR180 is its **finite
obstacle comparison, OPEN-F**, or its consequence **OPEN-S**. With the
canonical harmonic function `G`, sibling map `B(n)=64*n+21`, and

\[
\mathscr L_G(n)=\sum_{j\ge1}64^{-j}\frac{G(B^j(n))}{G(n)},
\]

OPEN-S asks, for each `eta > 0`, for constants `c_eta > 0` and `Q_eta`
such that

\[
G(n)\ge\eta n,\quad n\ge Q_\eta
\quad\Longrightarrow\quad
\mathscr L_G(n)\ge\frac{c_\eta}{\log(2+n)}.
\]

The upstream proof shows that this would contradict the summability of
`L_G` along an escaping path, under its stated canonical construction
inputs. Its numerical definitions, domain and finite-obstacle version
remain those of the pinned PR180 note. No such lower bound is established
here. The low-clock concentration result does not refute it: this is a
weighted comparison at actual linear spikes, not a uniform density norm.

PR177 supplies another direct target: an upper bound on the
run-weighted terminal Dirichlet mass that conflicts with its proved
divergence under escape. The criticality result concerns ordinary energy
and supplies no such weighted upper bound. A positive-cycle exclusion is
also still required for full Collatz; the escaping-source arguments must
not be presented as covering additional cycles by themselves.

On the arithmetic side, the joint source minimum still requires a
successful word-changing return for the target, with its lower-grade and
larger-same-grade hypotheses kept on the same supplied source. The new
language theorem excludes one route for compressing source certificates;
it does not discharge that return.

## Replay

The new formal core has **eight public theorem audits**. Its exact project
closure comprises nine pre-existing certificate modules and four new
proof/audit modules. Only these imports are rebuilt; this checkpoint does
not rerun the earlier research search or all previous proof packets.

`DEPENDENCIES.json` pins each source, Lean and Mathlib. Run from the repo:

```sh
python research/lean-global-resolvent-20261121/overview/machinery/check_machinery.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib4 \
  --out /absolute/path/to/empty-output \
  --receipt /absolute/path/to/receipt.json
```

The driver rejects a nonempty output directory or a pin mismatch, treats
warnings as errors, and checks source stability and the axiom reports.
The certificate proof itself uses Lean core, with no Mathlib import; the
clock proof uses the pinned Mathlib. Neither uses an admitted proof or a
native-decision proof step.

See the [execution report](../../../../reports/2026-11-22-machinery-attack/README.md)
for the actual fresh replay and its limits. Repository integrity checks
are reported separately and do not certify the written mathematics.
