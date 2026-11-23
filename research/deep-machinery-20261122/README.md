# Four direct attempts to use deep machinery for Collatz closure

**Continuation:** [actual-orbit phase and whole-repository synthesis](../whole-repo-synthesis-20261122/README.md)
adds a written polynomial phase estimate, its exact-edge Lean core, and
further source-preserving closure attempts. This earlier packet retains
its original claims and evidence below.

**22 November 2026. Full Collatz remains OPEN.** Three collaborating
researchers and the principal researcher pursued four distinct closing
routes against the refreshed repository. No universal descent theorem,
escape-exclusion theorem, or complete termination certificate resulted.
This packet records the attempted applications and their exact outcomes.
It adds written mathematics and reproducible arithmetic controls, not
new Lean-certified declarations.

The [source snapshot](SOURCE_SNAPSHOT.json) freezes the repository inputs.
It starts from our PR178 at
23456d145df23ef2b412f61f7e49e38a222bc2b1 and includes the newer
PR175/176/177/180/185 closing attempts. The extensive PR186 literature
guide is credited as an input. This packet executes selected applications;
it does not duplicate that guide's catalogue of possible theories.

## Outcomes by route

| Route | Attempted closing step | What the calculation establishes | What remains unproved |
|---|---|---|---|
| Actual mode-switch termination | Complete the existing maximal-corridor rank using size-change or a bounded number of mode refinements | For every b >= 3 and K >= 1, positive ordinary histories have K exact alternating maximal mode pairs (2,1),(b,1). From the first unsafe state, the current rank stays strictly above its initial value for 2K-1 modules. A pair-specific counter does decrease. | A well-founded rule paying for changes of the selected word or a nonuniform repayment theorem. |
| Directed recurrence and affine renewal | Transfer recurrence from symmetrization, or use the sharp perpetuity tail to exclude an escaping spine | Symmetrization is recurrent under the pinned harmonic inputs, but the actual clock channel violates the required strong sector condition. Kesten--Goldie applies to the genuine affine law with an explicit tail constant; its actual-prefix comparison gives a weaker orbit bound than the elementary one. | A quantitative arithmetic comparison for the actual conditioned inverse law. |
| Higher-order dilation rigidity | Upgrade guarded Collatz correlations to the invariances needed for rigidity | Exact multipoint residue-error identities. Even eliminating every error gives only an averaged dilation law; an explicit stationary Boolean process satisfies that law and fails separate dilation invariance. The qualified actual compact projection remains Haar times a label distribution. | Arithmetic control of shifted products and removal of the surviving invariant label. |
| Simultaneous Mahler equations | Force the basin generating function to be rational, which would imply full Collatz | Exact mixed dilation and all-prefix binary-to-ternary section identities. The first proposed finite system instead generates an unbounded root-of-unity ladder. The final rationality-to-convergence implication is written out. | A fixed finite-dimensional system for the actual all-time basin series. |

Read the proofs:

- [Mode refinement and the all-parameter rank test](termination/MODE_REFINEMENT_ATTEMPT.md).
- [Recurrence, the exact change of law, and implicit renewal](boundary/RECURRENCE_AND_AFFINE_BOUNDARY.md).
- [Guarded correlations and an explicit all-order control](rigidity/GUARDED_DILATION_ATTEMPT.md).
- [Direct follow-up on the actual sibling-current target](rigidity/SIBLING_REPAIR_ATTEMPT.md).
- [The attempted finite Mahler closure](mahler/MIXED_DILATION_ATTEMPT.md).

## 1. The current rank cannot be repaired in a fixed number of switches

For the existing maximal-corridor map A and rank R_*, put

\[
 H_b=g_b\circ g_2,
 \qquad H_b(n)=
 \frac{3^{b+2}n+13\cdot3^b-2^{b+3}}{2^{b+4}}.
\]

For every b >= 3 and K >= 1, one explicit simultaneous congruence
constructs infinitely many positive n_0 for which all K pairs are
literal shortcut histories and each maximal repetition count is one.
Writing n_j=H_b^j(n_0) and y_j=g_2(n_j), the same pre-existing rank is

\[
 R_*(n_j)=(n_j+5)^2/9,\qquad
 R_*(y_j)=(y_j+5)^2/81.
\]

Both subsequences strictly increase. In particular,

\[
 R_*(A^\ell(y_0))>R_*(y_0)
 \quad(1\le\ell\le2K-1).
\]

This directly refutes a fixed-module repayment completion of that
rank. It does not refute all possible ranks or prove that a single
ordinary source follows the pattern forever. The positive starting
integer depends on K. Complete source certificates could also carry
information that this target-only rank omits.

The repair for one selected pair is explicit:

\[
 Z_b(n)=(3^{b+2}-2^{b+4})n+13\cdot3^b-2^{b+3},
 \qquad
 v_2(Z_b(H_b(n)))=v_2(Z_b(n))-(b+4).
\]

The attempt then asks how to pay for changing from this counter to
another word's counter. No universal accounting argument was obtained.

## 2. A deep theorem really applies, but does not yield the needed bound

For independent geometric exponents with probability 2^(-e), let

\[
 R=\sum_{j\ge1}\frac{3^{j-1}}{2^{E_1+\cdots+E_j}}.
\]

The boundary note checks the implicit-renewal hypotheses and obtains

\[
 \lim_{t\to\infty}t\,\mathbb P(R>t)
 =\frac1{\log(27/16)}.
\]

Comparing the actual prefix of a hypothetical escaping ordinary orbit
with this law gives q_k squared <= C_p 3^k, under the displayed retained
path input. The elementary bound q_k+1 <= (3/2)^k(p+1) is stronger.
Thus the failed step is visible after applying the theorem and keeping
the original source; it is not hidden in an invocation of random drift.

The same note quantifies why the affine Poisson-boundary theorem cannot
be transferred to the ordinary inverse law without an additional
argument: an inverse word of r steps has likelihood ratio
3^r G(x_r)/G(q), and infinite ordinary legality has zero probability
under the independent-exponent law.

## 3. The rigidity conditions were tested at the level of full laws

Exact parity splitting gives a relation between all multipoint averages,
but with a specified ternary residue error. Even if those errors all
vanished, the process law would satisfy only

\[
 (D_2)_*\mu=\tfrac12\mu+\tfrac12(D_3)_*\mu.
\]

The rigidity note constructs a positive continuous circle density and
a stationary Boolean process satisfying this identity at every order
while failing separate dilation invariance. This tests the proposed
inference, not the Collatz conjecture. It is not asserted to be an
ordinary Collatz-invariant label.

The Mahler route has an equally explicit unproved premise: the exact
section identities do not give a finite kernel. The deep rationality
theorems require a fixed finite system; the note does not assume one.

## 4. Direct follow-up: the actual sibling current

The rigidity researcher then attacked PR180's OPEN-S and OPEN-F directly.
Pairing admissible inverse exponents by rank gives a legal,
prefix-preserving correspondence between retained ordinary inverse
trees. For paired depth-r words with terminal sources z and z', roots
n and m, and critical weights w_n and w_m, the exact cost is

\[
 \frac{w_m}{w_n}=\frac mn\frac z{z'}\frac{\Lambda'}\Lambda,
 \qquad \delta\le\Lambda,\Lambda'\le1.
\]

For m=B^j(n), where B(n)=64n+21, the actual sibling weight
64^(-j) cancels the leading factor m/n. The resulting finite stopping
inequality keeps the actual ordinary source heights and the canonical
obstacle. The remaining quantity is the weighted average of the
reciprocal height distortions z/z'. No lower bound of the necessary
order 1/log(2+n) was obtained. The crude depth comparison is explicitly
shown to be weaker than the existing obstacle floor; it is not claimed
as improved leakage.

## Evidence

The mathematical notes identify their imported hypotheses and primary
sources at the point of use. Recent manuscripts are separately marked
source-qualified. Written peer reviews and the reproduction scope are
recorded in the [accompanying report](../../reports/2026-11-22-deep-machinery-attempts/README.md).
Existing Lean source files are
unchanged; their earlier compiler receipts retain their original scope.

The [exact mode replay](termination/check_mode_refinement.py) checks 16
parameter cases, 60 pair returns, and 630 literal shortcut clocks. Its
[fixture](termination/mode-refinement-fixture.json) includes the ordinary
values, ranks, physical words, and counter changes. The all-parameter
claim is the written congruence and valuation proof, not an extrapolation
from that finite replay.

The published-head repository validation is recorded in PR178. That
gate checks repository integrity; it does not establish the missing
universal mathematical statements.
