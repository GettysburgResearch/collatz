# Coordinator reconstruction and publication scope

24 November 2026. **Collatz remains OPEN.** This is a research continuation
on main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a, not an integration into
the scientific registry. Three explicitly selected GPT-6.2 Astra agents
worked on ordinary descent, arithmetic rigidity, and analytic inverse
machinery. Their independent cross-reviews are retained beside this file.
The coordinator reconstructed the deductions below and executed the
reported compiler and finite replays.

A compiled finite implication, a written infinite proof, and an external
source hypothesis receive separate verdicts. None of the available
implications is relabelled as universal convergence.

## Claim map

| Claim | Verdict and exact boundary |
|---|---|
| Ordinary least-disagreement excursion | Independently reconstructed written proof from the pinned PR192 least-disagreement hypotheses. The actual orbit crosses \(6q\) or enters the specified cycle within \(O(q^{49/100})\) shortcut clocks. Neither alternative is excluded. |
| Height strip, finite path count and continued fractions | The integer count was executed in normal and optimized Python, and independently by a different height-coordinate recurrence. Its use in an asymptotic orbit bound and Legendre's criterion remains written mathematics. |
| Companion packing and entropy | Independently reconstructed written proof for primitive positive companion words and the stated rational-approximation hypotheses. No necessary low-entropy law or cheap approximation for every escaping source is proved. |
| Real annulus, inverse-root minorization and visitation | Deductions reconstructed conditional on paper 48's floor F and the separately named paper 9/19 inputs. These apply to specified inverse laws. They do not assign those laws to an ordinary forward orbit. |
| Dyadic zoom and finite-scale product identity | Exact derivation from the stationary geometric series, independent of F. Stationary, conditioning and weak-convergence arguments remain written proofs; finite word bijections and residue histograms were replayed. |
| Short windows and growing clock moduli | Deductions reconstructed under F, the prior antichain and mixed-prefix inputs, and Wu-Wang Theorem 1; the critical-block variant additionally requires S. The budget is \(4.1163051\sigma+5.1163051\mu<1/2\). |
| All-words central inverse expansion | Seven new Lean declarations pass. Literal positive odd chains to \(q>1\) give \(3^b2^s q\le10^b y\), hence \(y>q\) when \(b>0,\ 4s\ge7b\). The physical interpretation of the inductive chain is explained below. |

The detailed proofs are linked from [the research overview](../../research/astra-fixed-target-closure-20261124/README.md).
Source hashes are recorded in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json);
the final file inventory is [MANIFEST.json](MANIFEST.json).

## Ordinary proof reconstructed

Let \(q\) be the least odd tripling disagreement and \(n=3q\). The imported
minimum theorem gives: every positive integer at most \(q\) is good, \(n\)
is bad, and every positive multiple of three below \(n\) is good. These are
properties of the actual basin of 1, not a parity measure.

For an odd input with \(x+1=2^m a\), \(a\) odd, put \(R=3^m a\).
The two exit classes yield different exact orbit mergers. The class
\(R=1\bmod4\) gives a double-even exit and merges \(x\) with \((x-1)/2\)
at different clocks. The class \(R=3\bmod4\) gives a singleton exit and
merges \(x\) with \(2x+1\); its next odd-run entry is \((R-1)/2\).
For a bad interior entry \(x=1\bmod6\) with \(x\le2n\), the double-even
case would reach a good multiple of three below \(n\). The singleton case
requires \(2x+1\ge n\), so \(x\ge(n-1)/2\).

I checked the initial cases separately. Starting at \(n\), either the
singleton chain has a nonrepeating root of class 0 modulo three, or the
double exit forces the recentered site \(s=(n-1)/2\). The latter requires
\(v_3(n)=1\) and \(q=1\bmod12\); the otherwise available smaller bad
multiple is forbidden. The exact reverse formula using
\(v_3(2F(x)+1)\) makes the allowed entry map injective. Any repeated entry
in the recentered chain rewinds to \(s\), so it gives a cycle with
minimum \(s\), including a bound on a full lap. The written proof also
tracks the different physical clocks that bring the original \(n\) onto
that recentered path, including a first edge that crosses immediately.

Every completed bounded-to-bounded run has at most five odd inputs and
one even input. The final crossing run need not obey that bound; its
length is charged separately as \(O(\log q)\). The asserted alternative
is inclusive: an intermediate value on a bounded-entry cycle can itself
already exceed the crossing threshold.

The sharper count uses every odd input in the completed bounded segment,
including those internal to a run. The range is
\([s,(8n-1)/3]\), not just the range of run entries. After the rational
rounding detailed in HEIGHT_STRIP, each block of 512 odd transitions lies
in a strip of width 2.44 with drift \(58496/100000\). The finite count
includes all 245 possible initial bins. Multiplication of the block
counts therefore only overcounts, even when successive bins are
incompatible. The final partial block costs an absolute factor.

For \(k=\lceil\log_3(2n+1)\rceil\), each length-\(k\) word determines its
terminal residue modulo \(3^k\). There is at most one positive run entry
at most \(2n\) in that residue. Apart from at most \(k\) initial entries,
each distinct entry has such a suffix. This converts
\(C^{100}<3^{49\cdot512}\) to the \(O(q^{49/100})\) bound. The exceptional
cycle's full period is bounded by the same argument.

On a cycle, multiplication around the full physical lap gives
\[
0<h/p-\log_2 3
 =p^{-1}\sum_{x\ {\rm odd}}\log_2(1+1/(3x))<1/s.
\]
The period estimate implies \(p^2/s=O(s^{-1/50})\), hence error
\(<1/(2p^2)\) eventually. If \(h/p=a/b\) in lowest terms, \(b\le p\),
so Legendre applies. Unbounded minima would force unbounded reduced
denominators and irrationality exponent at least \(100/49\). No
contradictory upper bound is supplied. The independent
[ordinary](ORDINARY_REVIEW.md) and [strip](ORDINARY_STRIP_REVIEW.md)
reports have the same scope.

The strip review pins the author's original bytes. The delivered strip
proof has one coordinator edit: its inaccessible Legendre citation was
replaced with Robert C. Vaughan's primary notes, Theorem 2.3, whose
statement and proof were inspected. The mathematical text is unchanged.
SOURCE_MANIFEST records both hashes and that citation-only edit.

## Arithmetic proof reconstructed

The common denominator here belongs to the positive periodic companion
of the binary word. It is not the denominator in the physical cycle's
affine fixed-point formula. A primitive word has distinct companion
phases: equality would give the same legal dyadic continuation and hence
a shorter period.

A cyclic record argument selects at least
\((\tau-\rho)L/(1-\rho)\) phases with all backward odd densities at least
\(\rho>\log_2(3/2)\). The geometric real sum bounds these phases by a
constant depending only on \(\rho\). After multiplying by the common
denominator \(d\), a length-\(k\) past fixes an integer numerator modulo
\(3^k\). Choosing \(3^k\) larger than the real numerator bound proves the
injection, with no unidentified factor of \(d\) discarded.

I checked the passage from distinct words to stationary entropy rather
than just finite complexity. The selected \(k\)-block law has entropy
\(\log |G|\); averaging its \(k\) shifts and applying the displayed
finite-block subadditivity estimate gives a stationary limit \(\nu\)
dominated by the limiting full empirical law after a positive rescaling.
The selection proportion does not vanish. This gives
\(h(\nu)\ge\log3/K\) under \(\log d\le(K+o(1))\log L\).
Ergodicity identifies \(\nu\) with the full empirical limit; without
ergodicity the dominated component is retained explicitly.

For actual positive cycles with lengths tending to infinity, minima tend
to infinity and odd densities tend to \(\log2/\log3\). The binary entropy
bound then gives the displayed exponent \(1.6684596861\ldots\). This is a
necessary denominator bound, not a denominator obstruction for every
word.

For the separate fixed-source theorem I checked all three resources:
dyadic agreement length, total real coefficient height, and prime-to-six
denominator. After the stated burn-in, trial phases are positive and lie
on the required integer grid. Repeated trial states would force a long
repeated physical parity prefix, making the difference of two distinct
actual source iterates divisible by a power of two larger than its
absolute value. The hypotheses ensure the height and burn-in costs are
sublinear in the available agreement length. No construction meeting
those hypotheses for every escaping ordinary source is supplied.

The [arithmetic cross-review](ARITHMETIC_REVIEW.md) records an independent
reconstruction. Four finite supporting theorems compile; the entropy,
weak-limit and actual-approximation conclusions remain written proofs.

## Analytic inputs and deductions reconstructed

Paper 48 v2, Lemma 7 (76), is used at its actual independent geometric
word law, exact central gap total, bounded real offset, fixed initial
ternary cylinder and fractional extra ternary depth. I checked the
displayed source statement. The entire external proof of F was not
reconstructed or formalized here.

The annulus construction puts its scale loss in an explicit first gap
\(v\asymp\log_2(1/\rho)\). A bounded congruence adjustment places the
tail in the initial cylinder required by F. The first gap has probability
\(2^{-v}\asymp\rho\); the remaining total stays central in the stated
range. The full-letter cap is enlarged for this exceptional gap. These
points prevent a hidden uniformity claim as \(\rho\) shrinks.

At stationarity, summing central totals, approximating finite cylinders,
and using closed-annulus Portmanteau gives the lower Haar minorization.
The upper \(L^p\) comparison uses paper 9's separately named regularity
estimate and a first-gap compression argument; it is not a consequence
of the lower floor alone. Paper 19's Cesaro trace theorem then yields an
annulus estimate on the canonical inverse law of every specified
ordinary unit. Its bounded-selection identity is used with its actual
bounded function. Conditional expectations approximate a full-path
event in \(L^1\); boundedness and reverse Fatou give the claimed positive
almost-sure upper visitation frequency. The conclusion concerns that
inverse Markov law, with no unstated Markov restart on a deterministic
forward path.

The dyadic scaling identity needs none of those external estimates.
Subtracting \(m\) from the first gap gives exactly the factor \(2^{-m}\)
and the ternary multiplication by \(2^m\). Averaging a full period of
the unit group modulo \(3^j\) gives an exact product with the real
conditional observation. This is averaging over scales, not a pointwise
fibre result. The finite-word checker excludes the one-letter endpoint
case in which subtracting the gap would create an illegal zero letter;
that boundary is retained as a negative control.

For the window result, I checked the exponent bookkeeping against
Wu-Wang **Theorem 1 on \(1,\log2,\log3\)**, including the proof's stated
change of basis. It is not an inference from the irrationality exponent
of \(\log3\). The relevant convergent denominator is bounded in terms of
\((m/w)^\kappa\), while the available depth trials are
\(\sqrt{\log X}/m\). With \(w=W/X\), this is the displayed joint budget.
The antichain is credited to PR201, the depth bank and mixed-prefix
transport to PR203, and the synchronized-block input S to PR146. Our
fixed-target one-arm result does not supply the paired source control in
the much smaller selected windows required by the surviving global
argument.

The [joint-floor cross-review](JOINT_REVIEW.md) and source ledger
[EXTERNAL_SOURCES.md](EXTERNAL_SOURCES.md) preserve those boundaries.

## Central inverse barrier and its physical interpretation

The new inductive Lean predicate records a literal outward word with
equations \(2^e x=3y+1\), positive gaps, odd outward sites, and an initial
lower bound \(q\ge3\). Its induction proves every outward site is at least
3 and multiplies \(3\cdot2^e x\le10y\). No analytic theorem appears as an
axiom or hypothesis.

Every literal positive odd inverse path to an odd \(q>1\) is represented:
the target is at least 3, all outward sites are odd, and the odd fixed
point 1 cannot precede \(q>1\), since its accelerated forward orbit stays
at 1. The exact path equations give the positive valuations required by
the constructor. The central product comparison uses the integer
inequality \(10368>10000\) after raising both sides to the fourth power.
For \(b\ge16\), the integer lower-central condition
\((2b-s)^2\le b\), with natural subtraction, implies \(4s\ge7b\).

Thus arbitrary real carries or ternary digits cannot make a central word
from a visited \(q\ge n>1\) provide an ancestor at most \(n\). This rules
out that particular direct descent mechanism. It does not rule out other
mergers, noncentral words, or every possible use of inverse density.

## Actual compiler and bounded execution evidence

[LEAN_REPLAY.json](LEAN_REPLAY.json) records Lean 4.34.1, compiler SHA-256,
Mathlib revision, all eight dependency revisions and clean tracked states,
commands, source hashes, exit codes, output, and parsed axiom lists.
Eight modules passed, with **66 explicitly printed declaration audits**:
18 in three new modules, 14 in the PR202/203 copies, and 34 in the three
byte-identical PR192 dependencies. This count is not added to older PR
counts, which can overlap.

All eight modules use warnings as errors. The new and replay kernels also
disable automatic implicit variables; the exact PR192 dependencies retain
their original elaboration setting. Every printed axiom list is contained
in the set {propext, Classical.choice, Quot.sound}. The checked declarations
have no sorry dependency or custom analytic axiom.

The original PR203 file passes unmodified. The original PR202 file
elaborates its eight declarations but fails the strict run because hB
is unused. The delivered copy only narrows the imports and renames that
unused hypothesis _hB; propositions and proof bodies are unchanged.
The PR203 working copy only narrows its import. Original bytes and
attempts remain in [ORIGINAL_REPLAY.json](ORIGINAL_REPLAY.json) and
the original-sources directory.

The first version of the aggregate replay harness used the wrong working
directory when compiling a temporary dependency with an explicit output
path. It failed before checking that dependency. The actual failure is
retained in [REPLAY_SETUP_FAILURE.json](REPLAY_SETUP_FAILURE.json).
The corrected harness uses the temporary source directory and the final
receipt passes. No failed output is represented as success.

All four new Python programs pass both normal and optimized execution
with output identical to their recorded controls. The two original
JavaScript programs reproduce their prior counts. The strip was also
recomputed by a second implementation, documented in its review. These
checks concern the displayed finite domains. They do not verify F, an
asymptotic theorem, or the full Collatz conjecture.

The separate repository validator must run on a clean committed complete
checkout, with its receipt outside the checkout. The publication PR
records the exact checked commit and the result. Repository integrity is
not mathematical proof verification.

## Late intake: PR204

After this packet's proofs and replays were completed, the repository
published PR204 at 5d4698b692ec102b44cf77a59930a2a80b4104fd. Its overview
and pressure/WEIGHTED_POINTWISE_ROWS.md were inspected by the coordinator
and the analytic agent. Its large finite certificate was not rerun in
this continuation; no independent full audit of PR204 is claimed.

The stated theorem gives, for each fixed positive odd unit \(q\), one row
\((e,p)\) containing at least \(c_qX^{1/5}/\log X\) paired sources in
\([X/2^{400},X]\), with both \((x,5x)\) reaching \((q,5q)\) at clock \(e\)
and grade \(p\). It does not use F. The row is selected after \(q,X\);
its grade-to-clock ratio is uncontrolled. Since its affine scale is
comparable to \(X\) with constants depending on \(q\), the guaranteed
normalized pressure is only of order \(X^{-4/5}/\log X\).

This is complementary to our one-arm relative density in smaller
prescribed windows. Neither statement supplies simultaneous pairing in
the required selected window at the central grade. Central inverse
expansion is consistent with PR204's deliberate production of large
ancestors. Its separate merger constructions have actual missed
progressions and do not give a smaller representative for the supplied
least disagreement. Thus neither surviving ordinary alternative or the
upper-convergent restriction is eliminated by this late input.

## What is still needed

A complete argument must exclude the actual threshold crossing and the
exceptional bounded cycle, or find a different unconditional ordinary
descent mechanism. The arithmetic lane would need a forced upper
restriction incompatible with its necessary denominator/entropy bound.
The analytic lane still needs a statement about the selected pair of
ordinary sources, or an actual smaller merger partner with the required
clocks. None of these missing steps is supplied by a numerical experiment,
an almost-everywhere statement, or a formalization of only its finite
consequences.
