# Ordinary excursions, companion entropy, and conditioned inverse laws

**Collatz remains open.** This packet combines three independently assigned
GPT-6.2 Astra investigations with a coordinator's proof reconstruction and
actual Lean replay. It develops the ordinary least-source alternative, a
complete-lap arithmetic/entropy constraint, and a more precise inverse-law
interface. The results below have separate hypotheses and do not combine into
a proof of convergence.

Use the positive shortcut map

\[
T(x)=\begin{cases}x/2&2\mid x,\\(3x+1)/2&2\nmid x.\end{cases}
\]

`U` is its accelerated map on positive odd integers. An ordinary unit means
a positive odd integer prime to three. Unless explicitly marked as a Lean
kernel, an infinite theorem below is **PROPOSED written mathematics** with
the stated independent reconstruction. An imported analytic theorem remains
**SOURCE-QUALIFIED** even when its finite consumers compile.

## The main ordinary result

Assume a counterexample exists. Let `q` be the least positive odd tripling
disagreement for the basin of 1, and put `n=3q`. The pinned PR192 minimum
theorem supplies three actual facts: every positive integer through `q` is
good, `n` is bad, and every smaller positive multiple of three is good.
Under these hypotheses the actual orbit of `n`, within

\[
                         O(q^{49/100})
\]

shortcut steps, either exceeds `2n=6q`, or enters the following restricted
nontrivial cycle. In the cycle alternative `q=1 (mod 12)`, the minimum is
`(3q-1)/2`, every maximal odd run has at most five inputs, every such run is
followed by exactly one even input, and every odd-run entry is at most `6q`.
The absolute constant in the bound is not made small or numerically optimized.

The proof follows the actual original source. It does not restart a random
parity law at a selected endpoint. At an interior bad odd site `x=1 (mod 6)`,
a double-even exit would merge it with the good multiple `(x-1)/2`. A
singleton-even exit instead makes `2x+1` a bad multiple, giving the lower
height bound `(n-1)/2`. These comparisons force every completed interior run
to have length at most five. A reverse valuation formula makes the run map
injective on the relevant domain. Thus remaining in the bounded region
forces either a finite crossing or the explicitly identified cycle.

For the sharper clock bound, every odd input in a completed bounded run lies
in `[(n-1)/2,(8n-1)/3]`. Its logarithmic height follows the two-step walk
with increments `log_2(3/2)` or `log_2(3/2)-1`, with a controlled positive
error. An integer recurrence counts all possible 512-step paths in a
rational strip of width `2.44`, including every starting bin. Its count `C`
satisfies the exact integer inequality

\[
                            C^{100}<3^{49\cdot512}.
\]

Each retained parity word determines one terminal residue modulo `3^k`.
The distinct actual entries below `6q` can therefore be counted with
`k=ceil(log_3(6q+1))`. The last crossing run is handled separately, adding
only `O(log q)` clocks. This is the source of the exponent `0.49`.

For a sufficiently large minimum on the remaining cycle branch, write `h`
for its least shortcut period and `p` for the number of odd inputs. Then
`h/p`, reduced to lowest terms, is an upper continued-fraction convergent
to `log_2 3`, and

\[
                   0<h/p-\log_2 3\ll p^{-100/49}.
\]

No contradictory irrationality upper bound is supplied. The growing branch
also remains possible: after the first crossing, its comparison multiple
may be as large as the original bad multiple. Finite positive progressions
in the packet exhibit both a later genuine merger and a crossing after
arbitrarily many identical initial singleton choices.

[Ordinary proof](ordinary/README.md) ·
[Height strip and cycle consequence](ordinary/HEIGHT_STRIP.md) ·
[Exact strip checker](ordinary/check_strip.py) ·
[Ordinary Lean kernel](ordinary/OneEvenEscape.lean)

## Arithmetic information from a whole lap

For a primitive binary necklace of length `L` and odd density
`tau>beta=log_2(3/2)`, its positive periodic companion satisfies

\[
                  2^{1+e_i}w_{i+1}=3w_i+e_i.
\]

Let `d` be its common reduced denominator, which is prime to six. This is
the companion denominator, **not** the physical Collatz cycle denominator.
For every `beta<rho<tau`, a cyclic record argument selects at least
`(tau-rho)L/(1-rho)` phases with every backward partial odd density at least
`rho`. The selected companion phases are uniformly bounded in the real
coordinate. Their integer numerators and a complete ternary congruence
then make their past words of length `k=log_3 d+O_rho(1)` pairwise distinct.

This proves a factor-complexity/denominator tradeoff without a prescribed
substitution or carry factorization. A bounded circular string attractor
forces an exponential companion denominator; a fixed polynomial bound on
factor complexity forces stretched-exponential growth.

More significantly, suppose a sequence of these necklaces has
`log d <= (K+o(1)) log L`, with odd density bounded strictly above `rho`.
Every limiting empirical parity law dominates a positive multiple of a
stationary law `nu` satisfying

\[
                    \nu([1])\ge\rho,
                    \qquad h(\nu)\ge\frac{\log3}{K}.
\]

For an ergodic empirical limit, the limit itself is `nu`. A zero-entropy
limit therefore forces superpolynomial companion-denominator growth.
The proof gives the finite block entropy calculation explicitly, rather
than inferring entropy from mere agreement between models.

For primitive positive ordinary cycles with lengths tending to infinity,
the result gives

\[
 \liminf\frac{\log d}{\log L}
       \ge \frac{\log3}{H(\log 2/\log3)}=1.6684596861\ldots,
\]

where `H(t)=-t log t-(1-t)log(1-t)`. A separate theorem treats rational
approximants to the genuine dyadic companion of **one fixed escaping
ordinary source**, retaining the agreement length, total coefficient
height, and prime-to-six denominator separately. It requires sublinear
logarithmic height and polynomial prime-to-six denominator; neither is
asserted for all escaping sources.

[Companion packing and entropy proof](arithmetic/README.md) ·
[Actual-scalar approximation](arithmetic/ACTUAL_APPROXIMATION.md) ·
[Lean arithmetic kernel](arithmetic/CompanionPacking.lean)

## What the analytic machinery now yields

The external floor **F** is paper 48 v2, Lemma 7 (76), at its stated
independent geometric inverse-word law, exact central total, bounded real
offset, fixed initial ternary cylinder, and fractional extra ternary depth.
The paper's full analytic proof is not independently rebuilt here. The
extraction of its relevant conclusion and the deductions below were
reconstructed, with each additional source identified beside its use.

1. **A real annulus at a fixed total.** For length `b`, total
   `|s-2b|<=sqrt(b)`, precision `b+K` with `K<=delta(b-1)`, and
   `2^(-sqrt(b)/2)<=rho<=1`, each ternary unit residue receives at least
   `c rho 2^s/(3^(b+K)sqrt(b))` words whose real offset lies in
   `[c0 rho,rho]`. The changing first letter is charged explicitly; the
   old logarithmic cap is not silently retained on that letter.
2. **Conditional inverse laws.** Conditioning on this annulus and the
   exact central total still gives a ternary lower minorization. At
   stationarity an additional published/manuscript `L^p` estimate gives
   upper comparisons uniform over the annulus scale. The canonical
   Cesaro fibre theorem in paper 19 then yields a lower annulus bound
   from every specified ordinary inverse-tree root. Its bounded-selection
   identity also yields a positive almost-sure upper visitation frequency
   under that root's canonical inverse Markov law. None is a law for the
   deterministic forward orbit of the root.
3. **An exact scale identity needing no analytic floor.** For the
   stationary geometric offset law `nu`, every Borel `I` in `(0,1]` and
   integer `m>=0` satisfy
   `nu(2^(-m) I x A)=2^(-m) nu(I x 2^m A)`. Averaging the laws of
   `(2^m R,Z)` conditioned on these annuli over one complete unit period
   modulo `3^j` gives an exact product of the real conditional law and
   uniform ternary units. Only the real observation is rescaled. This is
   not pointwise mixing at a supplied ordinary integer.
4. **Shrinking windows and simultaneous digits.** Combining the existing
   PR201 antichain and PR203 mixed-prefix transport with Wu-Wang's actual
   three-term linear-form theorem gives positive relative basin counts
   in every interval of width `X/(log X)^sigma`, for any fixed
   `sigma<1/(2*4.1163051)`. One may simultaneously prescribe low binary
   and ternary digits of total depth `eta log X`, and the first-hit
   shortcut and odd-count residues modulo a growing `m`. If
   `m<=(log X)^mu`, the joint budget is
   `4.1163051 sigma+5.1163051 mu<1/2`, with a factor `m^-2` in the count.
   The synchronized-block version additionally uses PR146's theorem S.

The Wu-Wang input is **Theorem 1 on `1, log 2, log 3`**, not an inference
from an irrationality bound for `log 3` alone. The shrinking-window proof
credits the earlier antichain and depth-bank constructions; they are not
claimed as new here.

[Joint real floor and ordinary inverse law](analytic/JOINT_REAL_FLOOR.md) ·
[Exact dyadic scale averaging](analytic/DYADIC_ZOOM.md) ·
[Shrinking-window theorem](analytic/SHRINKING_WINDOWS.md)

### A Lean-checked obstruction to a direct inverse descent

For every literal positive odd inverse chain from an odd `q>1`, with odd
depth `b`, total valuation `s`, and outward source `y`,

\[
                       3^b2^s q\le10^b y.
\]

Consequently `y>q` whenever `b>0` and `4s>=7b`. In particular this holds
for **every** central word with `b>=16` and `s>=2b-sqrt(b)`. Allowing a
larger real carry or finer residue does not circumvent the inequality.
At a non-descending source `n`, such a word through a visited `q>=n`
cannot supply a rival source at most `n`. The exceptional target `q=1`
is expressly excluded. The finite theorem, its literal-chain induction,
and the integer central-window threshold compile in
[CentralInverseBarrier.lean](lean/CentralInverseBarrier.lean).

## Verification and exact review scope

The final replay checks **eight Lean modules and 66 explicitly printed
declaration axiom lists**: 18 declarations in new kernels, 14 replayed
from our PR202/203 kernels, and 34 in three byte-identical PR192 dependency
modules. All reported axiom lists are contained in
`{propext, Classical.choice, Quot.sound}`. No `sorry` or custom analytic
axiom is used by those checked declarations. The new/replay kernels use
`autoImplicit=false`; every module uses warnings as errors.

The compiler is Lean 4.34.1 at
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. All eight dependency checkouts
match the Mathlib manifest and have clean tracked files.

| Source | Actual result in this continuation |
|---|---|
| Original PR203 `MixedTransport.lean`, SHA `3f2c89f12b057b8bb8655bd6fc794c772aa8b65d` | Unmodified strict replay PASS; all six printed declarations audited. |
| Original PR202 `ClockTransport.lean`, SHA `3b10b24d12d4b349cb20f4cbc83086c8a09f807e` | Proofs elaborated, but strict replay FAIL on the unused `hB` hypothesis. |
| PR202 checked copy here | PASS after renaming that unused binder `_hB` and narrowing imports; propositions unchanged. |
| PR203 checked copy here | PASS with narrowed imports; propositions unchanged. |
| Infinite probability, entropy, asymptotic bounds, and the complete excursion theorem | Written proofs with scoped independent reconstruction; not fully formalized in Lean. |
| External F, trace/fibre and analytic regularity inputs | Source-qualified; no external formal rebuild claimed. |

The historical uncompiled header comments in the two copied kernels refer
to their original checkpoints; the dated receipts here record the new
execution. Exact original bytes and failure output remain in reports.

All four new exact checkers passed in normal and optimized Python modes.
The original PR202 and PR203 JavaScript controls reproduced their recorded
counts. The new controls include 5,176 marked pasts, 468 complete scaling
bijections, 1,872 residue histograms, 44,437 ordinary singleton edges,
24 full-progression fixtures, and the 512-step integer strip count. These
are bounded checks, not tests of the external analytic inputs.

[Compiler receipt](../../reports/astra-fixed-target-closure-20261124/LEAN_REPLAY.json) ·
[Original compiler attempts](../../reports/astra-fixed-target-closure-20261124/ORIGINAL_REPLAY.json) ·
[Bounded replay](../../reports/astra-fixed-target-closure-20261124/CONTROLS_REPLAY.json) ·
[Coordinator review and limitations](../../reports/astra-fixed-target-closure-20261124/ROOT_REVIEW.md)

For a pinned installed environment, the replay command is:

```bash
python -X utf8 -B research/astra-fixed-target-closure-20261124/replay_lean.py \
  --mathlib-root /absolute/path/to/mathlib \
  --lean-bin /absolute/path/to/lean-4.34.1-linux/bin > ../lean-replay.json
```

Generated oleans are kept in a temporary directory. The separate repository
integrity command is `python -X utf8 -B tools/validate.py`, in a clean
complete checkout, with any receipt written outside the checkout. Its
publication run is recorded in the PR; structural integrity is not proof
verification.

## The remaining universal step

The late intake includes
[PR204 at its frozen head](https://github.com/GettysburgResearch/collatz/blob/5d4698b692ec102b44cf77a59930a2a80b4104fd/research/astra-joint-closure-20261124/README.md).
It supplies a fixed-target paired row with at least
\(c_q X^{1/5}/\log X\) sources in a wide fixed multiplicative shell, using
a finite certificate independent of F. Its chosen clock/grade ratio is
uncontrolled. We inspected that result and its relationship to this packet;
we did not independently replay its large certificate. It supplies neither
paired mass in the selected small windows nor a smaller merger for the
supplied least disagreement.

The ordinary argument still has to exclude both surviving outcomes for the
actual least `q`. The arithmetic argument needs an unavoidable entropy or
height restriction that contradicts its denominator requirement. The
analytic argument needs control of the actual selected pair of forward
sources or a smaller ordinary merger partner, not just positive marginal
inverse mass. Those missing implications are not inserted as axioms or
hidden inside the statistical inputs.
