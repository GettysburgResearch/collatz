# Global cycle separation and persistent ordinary descent

**PROPOSED research checkpoint. Collatz remains unresolved.** This continues
[PR188's canonical-window and carry results](../astra-closure-20261124/README.md)
using the latest source pins in [LATEST_INPUTS.md](LATEST_INPUTS.md).
Three GPT-6.2 Astra lanes pursued cycle exclusion, ordinary descent, and
same-source residue information. The parent integrated the arguments and
added the actual shortcut-map interface in Lean. The new results are below.

## One smaller ordinary source through infinitely many paid returns

Write the two odd-gap blocks as $L=(2,1)$ and $P=(1,4)$, with
$2^{a_i}q_{i+1}=3q_i+1$. Consider an infinite actual positive input whose
maximal paid clusters have length one or two, with at least four L blocks
after a singleton and five after a doublet. Their order and the excess
number of light blocks are arbitrary.

At a suitable original odd boundary $q$, the next three light blocks force
$1024\mid q+7$. The explicit comparison source is
$$
\boxed{m=\frac{157(q+7)}{256}-5.}
$$
Lean proves that this is a positive odd integer, lies below both $q$ and its
first odd intermediate $(3q+1)/4$, and never reaches one. It follows the
**same** comparison orbit through all later graph transitions. No successive
replacement by a merely locally smaller state is used.

The underlying graph has cores $L$, $L^3PL$, and $L^3P^2L^2$. The two paid
cores use respectively 17 and 25 shortcut clocks. Their exact target words
have 10 and 14 odd inputs, so the affine identities lift from canonical
residue representatives to every permitted positive ordinary source.
Positivity, the initial divisibility, and unbounded comparison clocks are
derived in [ClusterShadow.lean](ClusterShadow.lean).

A second infinite graph carries either $x-10$ or $x-7$, where
$x=(q+7)/2$, and permits five additional repeatable transitions. These include
cores starting with each of PR192's residual prefixes PPLLL, PLLPP, and
PLLPL, and include short light gaps inside interacting paid clusters.
[Renewal.lean](Renewal.lean) proves persistence of the initial comparison
source and extracts a smaller odd nonconverger when that source is even.

The graph-boundary conclusions are kernel checked. The written phase
argument in [PERSISTENT_DESCENT.md](PERSISTENT_DESCENT.md) extends them to
every odd phase of the respective infinite languages. Thus a global least
nonconverger cannot lie in either language. This does **not** exclude every
nonconverging orbit in a language: the smaller nonconverger need not belong
to it. Nor is either language forced on every ordinary orbit. The note gives
their exact coverage and an expanding symbolic pattern outside both.

## A denominator constraint at every rotation of every primitive cycle

Let a primitive positive rational cycle have shortcut period $A$, $p$ odd
inputs, and full reduced denominator $d$. For each $0<r<A$, let $t(r)$ be
the number of parity disagreements between the cycle word and its rotation
by $r$. No coprimality of $A,p$, or $r$ is required.

With $s=\log_2 3$, $c=s-1$, and
$\Lambda=A\log2-p\log3>0$, the written argument proves
$$
\boxed{\log_2 d>
\frac{cA}{s^{t(r)+1}-1}-1-\frac{t(r)}2\log_2 3
-\log_2\left(1+\frac p{3\Lambda}\right).}
$$
This is a finite inequality for the **complete numerical denominator**.
After the pinned two-logarithm estimate, it implies for any increasing
sequence of primitive ordinary cycle periods
$$
\liminf_{A\to\infty}
\frac{\min_{0<r<A}t(r)}{\log A}
\ge\frac1{\log(\log_2 3)}.
$$
A second inequality uses the Euclidean data of each offset. It forces any
nearly agreeing rotation to have a short modular return. At most
$O_K((\log A)^3\log\log A)$ rotations can have
$t(r)\le K\log A$. At the physically specified rotation $r=p$, it also
gives a positive power lower bound, up to logarithms:
$$
t(p)\gg A^{1/(2\kappa+2)}
(\log(A+1))^{-(\kappa+2)/(2\kappa+2)},
$$
where $\kappa$ is any effective exponent in
$\|m\log_3 2\|\ge c_0m^{-\kappa}$. The proof supplies the analogous
bound for inverse odd-clock rotations at arbitrary clock gcds.

[SHIFT_DISTANCE.md](SHIFT_DISTANCE.md) contains the proofs, the
source-qualified small-offset corollary, and a family of high-floor rational
cycles with linear disagreement at every rotation. That family shows why
large disagreement alone leaves an ordinary-integrality question.

The compiled coverage is explicit. [RotationalDistance.lean](RotationalDistance.lean)
proves the paired height bound, full dyadic divisibility on a common word,
the geometric clock budget, suffix-height accounting, and the modular
return identity. [CycleRotation.lean](CycleRotation.lean) proves the
permutation seed, exact directed mismatch count, and noncollision of a
nonidentity rotation of a least-period deterministic cycle.
[ActualCycleSeparation.lean](ActualCycleSeparation.lean) defines the ordinary
natural-number shortcut map and attaches the finite statements to its
literal iterates. In particular, if two nonidentical phases of an actual
primitive cycle share $L$ parity bits, the larger phase value is at least
$2^L$. The analytic logarithmic inequalities are written proofs.

## Residue information from the same ordinary source

[AUXILIARY_RESIDUES.md](AUXILIARY_RESIDUES.md) contains six results, with
their exact quantifiers and the finite kernels in
[AuxiliaryResidues.lean](AuxiliaryResidues.lean).

**Every prescribed modulus.** For a stationary actual forward lift with
ergodic gap law of entropy rate $h$ and finite mean $b$,
$$
\liminf_{M\to\infty}\frac{H(q\bmod M)}{\log M}
\ge \frac{h}{\max(\log3,b\log2)}.
$$
The limit is over all integer moduli, including powers of one fixed prime.
The proof decodes an ordered word from its two boundary residues and its
total clock, and reuses boundaries across successive blocks. It permits
unbounded gaps. A separate finite-prefix theorem gives a lower entropy
bound at every prescribed polynomial-size modulus on the actual CW clocks.

**Bias has a quantified cost.** Let $p$ be a reference gap law with
$p_1p_2>0$, and let
$\Delta=\mathbb E[-\log p(a_0)]-h$. At each fixed modulus coprime to six,
$$
\|\nu_M-\operatorname{Unif}(\mathbf Z/M)\|_{\rm TV}
\le\frac{2(M-1)}{p_1p_2}\sqrt\Delta.
$$
If the gap law is iid, the residue is uniform and independent of the entire
two-sided gap word. The proof derives this independence from the actual
forward equations. A fixed nonzero residue bias therefore gives a strict,
explicit penalty above the earlier critical canonical growth exponent
$g=\log3/H_3=1.1385654599\ldots$. No universal positive bias is asserted.

**Moving residue concentration has an actual dynamical consequence.** If a
positive fraction $\delta$ of one source's first $N$ odd states occupy one
residue at moduli $M_N\to\infty$, then its stationary gap limit gives at
least mass $\delta$ to one phase of a periodic rational Collatz word.
The moduli, residues, and prime supports may all change. The finite proof
uses disjoint return clocks and a signed cross determinant; it never
cancels a nonunit modulo $M_N$. Hence a limiting gap law with no periodic
component forces maximal residue mass and collision probability to tend to
zero at all moving moduli above any prescribed diverging cutoff.
The rational period may be negative or nonintegral. The conclusion does not
make the original positive orbit periodic and provides no power decay rate.

## Verification and review

The six new modules contain **39 public theorem declarations and 33 printed
transitive axiom audits**. A fresh isolated build of exactly these six
sources passed with Lean 4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Every invocation used one
worker and warnings as errors. The replay also rejected any compiler
diagnostic, missing audit, or axiom outside `propext`, `Classical.choice`,
and `Quot.sound`. The sources contain no admitted proofs or custom axioms.

| Module | Printed audits | Formal scope |
|---|---:|---|
| `Renewal.lean` | 4 | General cylinder transfer and persistent two-state ordinary descent |
| `ClusterShadow.lean` | 3 | Derived integrality and the mixed single/double cluster shadow |
| `RotationalDistance.lean` | 9 | Paired walks, divisibility, height and clock estimates |
| `CycleRotation.lean` | 4 | Permutations, directed discrepancy balance, primitive noncollision |
| `ActualCycleSeparation.lean` | 5 | Literal ordinary shortcut-map specialization |
| `AuxiliaryResidues.lean` | 8 | Ordered-word decoding, translation, signed return determinants |

The two controls ran identically in normal and optimized Python. The cycle
replay covers 1,131 primitive contracting necklaces, 12,282 rotations,
148,558 phase comparisons, 1,818,380 interval discrepancies, and 124,251
additional Euclidean offsets. The descent replay covers 70 exact ordinary
cylinder comparisons. These are bounded checks of the displayed mechanisms.

[REPLAY.md](REPLAY.md) gives the commands.
The [Lean receipt](../../reports/astra-global-step-20261124/isolated-lean-replay.json),
[finite controls](../../reports/astra-global-step-20261124/finite-controls-replay.json),
and [review report](../../reports/astra-global-step-20261124/REVIEW.md)
record the executed scope. The new written proofs were reconstructed by
the parent and, for the residue and descent packets, a separate Astra lane.
This is a proposed branch contribution, with formal and written claims
kept separate.

## The remaining global implications

The descent graphs cover infinite ordinary languages, but a complete
selector must still handle every remaining actual source from its original
floor, including gap words outside L/P. The residue bounds do not yet give
the conditional information at complementary growing precisions needed to
contradict the same source's height. At the saturated window length, word
entropy can already use the entire $\log N$ entropy of the sampled index;
adding unconditional residue entropy would count that information twice.
For cycles, arbitrary primitive words with large disagreement still require
a full-denominator exclusion. No closing hypothesis is inserted as a custom
axiom or presented as a proved universal theorem.
