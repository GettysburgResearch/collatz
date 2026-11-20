# Global certificate closure: actual source reductions and the remaining return

**Collatz is not proved in this packet.** The new statements are proposed
research with complete written proofs at their stated scopes and separate
internal reconstruction reviews. A successful restricted compiler, a
least-failure exclusion, and an all-input proof are distinct results.

This pass reviewed the latest PR146 and the new PR164--170 work, including
updates to older PRs during the investigation. It pursued a common
well-founded certificate argument and an absolute five-energy estimate.
The positive deductions below survived review; the global closing steps
did not. The [frozen source audit](SOURCES.md) distinguishes the newly
read heads from the earlier dependencies actually used in proofs.

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\]

the odd map `U(n)=(3n+1)/2^v2(3n+1)`, and the actual positive basin C
of 1. Every certificate in this packet is an ordinary positive path.

## Results

| Claims | Exact contribution | What is still required |
|---|---|---|
| [SF1--SF4](SMALLER_FIVE_FAILURES.md) | Every hard rank-five **global least reverse failure** produces an actual five failure q<X/13. Both q and 5U(q) have ordinary prefixes into the same certified initial interval. Two phases begin with valuations 4 and 3. | Certify the shifted targets 4(5U(q))-1 or 2(5U(q))-1, or return to a reverse query below the original X. Even completing this family would not cover every source rank. |
| [Arbitrary-tail c=3 descent](C3_ARBITRARY_TAIL_DESCENT.md) | The exact guard e>=3a+80 puts the target representative below X/176106 for **every positive tail w**. Actual eligible sources exist at every prescribed positive tail rank. | The complementary initial-block parameters remain. The separate 26-level resource exchange has no proved decreasing measure for returned witnesses. |
| [UF1--UF5](UNBOUNDED_FIRST_ONE_TRANSPORT.md) | Two unbounded first-one transport families, their whole disjoint cylinders, an explicit consuming compiler, and a valuation-controlled inverse fiber. They enlarge PR167's domain while retaining both strict renewal constants. | An absolute bound for the uncovered charge, or a successful transformation beyond homogeneous blocks. |
| [JF1--JF4](JOINT_FAILURE_CERTIFICATE_COSTS.md) | A finite conditional certificate program for every positive ternary unit, with sharp fixed-cover five-query cost 3669265/2239 and actual antecedent certificates before each call. | The unresolved physical-five calls need certificates. Combining the generic reverse cost with q<X/13 does not yield descent. |
| [NB1--NB3](NONHOMOGENEOUS_BOUNDARY.md) | Exact negative-offset debt for (1,3 repeated m times,b), actual certified unit sources at every rank>=2, and exclusion of complete homogeneous compilation from terminal base 1 even with padding. | A different clock/rank transformation or other certified terminal families can still work; their universal success is not proved here. |
| [Inverse-carry selector limit](INVERSE_CARRY_SELECTOR.md) | An infinite rank-one certified family has no positive integral inverse source below its endpoint anywhere in the PR170 carry family. | The supplied antecedents need a separate argument for their fivefold targets; they are not asserted to be failures. |

## 1. A smaller physical failure with its certificates retained

Let

\[
e=119+162j,\quad P=2^e,\quad
X=(1024P-2573)/243.
\]

Under the hypothesis that this X is the globally least eligible reverse
failure, define

\[
q=\begin{cases}
(32P-61)/135,&e=119\pmod{324},\\
(128P-271)/405,&e=281\pmod{324}.
\end{cases}
\]

Then

\[
q<X/13,\qquad q\in C,\qquad5U(q)\in C,\qquad5q\notin C.
\]

This is an actual smaller failed implication. The source membership is
proved by complete affine-prefix formulas and contracting ordinary
blocks, not assumed because q is smaller than a known convergent number.
The first phase uses the rational offset 19/5 and the five-clock slope 27/32;
the second uses offset 1/5 and slope 3/8. Exact geometric comparisons handle
all allowed exponents, with a stored 136-clock prefix for the one exceptional
base exponent 119. The successor-five values reach a smaller shifted power
and satisfy the same original least-failure floor.

The remaining negative shifts are explicit. Calling them convergent
merely because 5U(q) is certified would be an invalid closure step.

## 2. A reverse descent with no bound on the remaining tail rank

In the c=3 source kernel write

\[
X=(512z-175)/81,\quad z=41\pmod{81},\qquad
z=\frac{2^a(2^e w+1)}{3^a}-1.
\]

The actual prefix from z is `(1 repeated a-1 times,e+1)` and ends
at the supplied certified w. The lower comparison has representative

\[
R=\begin{cases}
3^{(e-1)/2}w,&e\text{ odd},\\
2\cdot3^{e/2}w+1,&e\text{ even}.
\end{cases}
\]

The integer inequality `e>=3a+80 =>176106R<X` is uniform in w.
The paper gives an explicit witness splice from R back to the actual
lower source. Under the same globally least X, the existing initial
interval theorem supplies R; more generally this is a finite compiler
using only reverse queries with upper antecedents below X.

The tail-rank statement is nonvacuous: a ternary residue permutation of
the credited ladder family constructs infinitely many such actual
sources at every positive tail rank, for each fixed guarded a,e.
The separate resource exchange reduces the known source rank by a and
its clock by a-26, but leaves 26 downward canonical calls whose returned
witness costs are uncontrolled. It is recorded as an attempt, not used
as a valid induction.

## 3. New unbounded words and the energy they actually control

Here `2^r` means r repeated letters two. For every r>=3,b>=4 the new
physical blocks are

\[
\begin{aligned}
(1,2^r,1,2,b)&\mapsto(1,1,4,2^{r-3},3,3,1,b-3),\\
(1,2^r,1,4,b)&\mapsto(1,1,4,2^{r-3},3,1,5,b-3).
\end{aligned}
\]

They take x to q and 5x to 5q at the same clock and odd count, with
q<=x/7. Their variable-run inverse fibers satisfy the exact identity

\[
v_3(2^{b+a+2}q-C_a)=r+3,
\qquad C_2=100,\quad C_4=148.
\]

Thus each a,q,b permits at most one r. Retaining this constraint and
all 486 endpoint residues modulo 729 proves, on the strictly enlarged domain,

\[
E_1(X)\le R_1^{new}(X)+\tfrac58E_1(X/3),
\]

\[
E_{21/25}(X)\le R_{21/25}^{new}(X)+\tfrac{91}{100}E_{21/25}(X/3).
\]

For an ordinary invariant metric label f,
`E_s(X)=sum x^(-s)d(f(5x),f(x))` over positive odd ternary units.
The remainder is the same sum on uncovered sources. The constants are
PR167's existing ones; the additional result is their validity on the
larger domain and the structural valuation bound. No independent sum
over all run lengths, floating-point coefficient test, or unproved
summability assumption enters the estimate.

The complete recognizer architecture belongs to PR167, with concurrent
versions in PR168/169. Our explicit language is a subset of it. The
finite residue certificate verifies the inequality; it does not bound
the remaining energy. Numerical coefficients on different domains and
cutoffs cannot be assigned to their union without another proof.

## 4. The exact global stopping point

The all-source five compiler makes the missing physical calls explicit.
Reusing the exact reverse unit cost A=2025217/23, its generic return
from a five failure q reaches some reverse failure below 5Aq. The new
forward interface gives q<X/13, but

\[
\frac{5A}{13}=\frac{10126085}{299}>1.
\]

The two proved size bounds therefore do not form a decreasing scalar
rank. This does not rule out a cheaper source-specific return, a
certificate-dependent rank, or a different proof.

There are two further limits. First, solving only the displayed rank-five
family would still leave higher-rank sources. Second, a homogeneous
dictionary cannot become a complete terminal-base 1 compiler merely by
adding more blocks: NB1--NB3 gives actual missed first-hit sources at
every rank p>=2, including arbitrary terminal padding. A universal
certificate procedure must use additional operations and prove their
termination. Alternatively, the energy route must bound its actual
uncovered remainder. Neither global statement is established here.

The new direct-R minimum in PR164 is different from the binary minimum
used here; its smaller constants cannot be substituted. PR169's paired
c=5 bypasses are genuine smaller calls on their two specified classes,
and its all-time fifth-denominator estimate is unconditional, but neither
statement supplies the missing universal selection or moving-residue
moment. These latest comparisons are recorded in the source audit.

The [first ternary-exit analysis](FIRST_TERNARY_EXIT.md) checks a concrete
attempt to recover the reverse height budget. After spending h levels of
ternary agreement, the proposed first exit exceeds the original bound
for h>=2 and always misses the required binary residue. For every h there
are infinitely many actual certified sources where that exit is a multiple
of three and has no integral odd predecessor. This excludes that proposed
continuation, not other adaptive words or forward excursions.

The [PR170 comparison](PR170_CARRY_AND_PHASE_COMPARISON.md) credits its
broader terminal-phase theorem: proportional native affine rewrites cannot
be complete using a terminal library whose phases are bounded below. NB3
is a quantitative specialization to the displayed hard prefix, not a claim
that the general phase obstruction is new. PR170's useful carry-four
blocks still lie inside the complete homogeneous recognition architecture.

The reverse orientation of that carry family gives genuine smaller five
failures on its eligible endpoint classes. It does not furnish a universal
selector: the [inverse-carry analysis](INVERSE_CARRY_SELECTOR.md) proves
that every certified rank-one source
`q_H=(2^(3^H+1)-1)/3`, H>=4, admits no positive integral carry inverse
x<q_H, even before imposing the ternary-unit guard on x. The proof covers
all run lengths and exit exponents. This does not classify the fivefold
targets as convergent or nonconvergent; it identifies a whole actual
antecedent family that requires another argument.

## Review and execution

The [review index and exact replay instructions](../../reports/2026-11-21-global-certificate-closure/README.md)
link the author proofs, independent reconstructions, full coefficient
tables, and the actual publication-time receipts. All scientific scripts
are standard-library Python and use checks that remain active under
optimized Python. The packet runner compares complete deterministic
reports, checks the frozen manifest, and requires a clean complete checkout
for publication verification. Repository integrity, finite replay, written
mathematics, and internal review are separately identified evidence.

The main branch and its accepted scientific registry are unchanged.
